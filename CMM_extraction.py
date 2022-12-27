"""
This is the main script that extracts the useful information from 
the CMM raw output.

Inputs: Folder path contaning the baseplate folders with CMM data inside.
Output: A python dictionary with all the relevant data concentrated.

Helper library: Auxillary.py
Status: 
To Do: Correct the maximum inscribed circle calculation.
"""
from config.Auxillary import dist,maxInsc,find_line,shift,check,Features, dist2D, pointLineDist

import os
import argparse
import sys
import linecache
import json
import math
import xlsxwriter
import numpy as np




def DerivedQtts():
    """
    Calculate the derived quantities from the extracted ones.
    ## HoleSlotDist
    ## MaxInsCircle also HoleToEdge
    ## KaptGlueThickness
    ## CopperEdgeDist
    ## Cutouts
    ## NotchToEdge
    ## InterNotch
    ## InterMB
    ## InterFid
    ## Centers
    """
    HoleToEdge = {}
    NotchToEdge = {}
    thetas = []
    ptsOnLines = []
    KapGlueTSum = 0.0
    CopperEdgeDSum = 0.0

    for i in range(6):
        edge = 'Edge'+str(i+1)
        BEi = 'BE'+str(i+1)
        KEi = 'KE'+str(i+1)
        FEi = 'FE'+str(i+1)
        coutDepth = 'C'+str(i+1)+'_Depth' 
        Notchi = 'Notch' + str(i+1)
        HoleToEdge[edge] = pointLineDist([Dict['Hole']['X'], Dict['Hole']['Y']], [Dict[BEi]['X'], Dict[BEi]['Y']], Dict[BEi]['Angle'])
        thetas.append(Dict[BEi]['Angle'])
        ptsOnLines.append([Dict[BEi]['X'], Dict[BEi]['Y']])
        KapGlueTSum += Dict[coutDepth]['DZ']
        CopperEdgeDSum += pointLineDist([Dict['Hole']['X'], Dict['Hole']['Y']], [Dict[FEi]['X'], Dict[FEi]['Y']], Dict[FEi]['Angle'])-pointLineDist([Dict['Hole']['X'], Dict['Hole']['Y']], [Dict[KEi]['X'], Dict[KEi]['Y']], Dict[KEi]['Angle'])
        Notchi = 'Notch' + str(i+1)
        BEi = 'BE'+str((i+1)%2+i)
        NotchToEdge[Notchi] = pointLineDist([Dict[Notchi]['X'], Dict[Notchi]['Y']], [Dict[BEi]['X'], Dict[BEi]['Y']], Dict[BEi]['Angle'])
        
    Dict['HoleSlotDist'] = dist2D(Dict['Hole']['X'], Dict['Hole']['Y'], Dict['Slot']['X'], Dict['Slot']['Y'])    
    Dict['HoleToEdge'] = HoleToEdge
    Dict['NotchToEdge'] = NotchToEdge
    MaxCenter, width = maxInsc([Dict['Hole']['X'], Dict['Hole']['Y']], ptsOnLines, thetas)
    Dict['MaxInsc_Circle'] = {'MaxInsc_Center':MaxCenter, 'Width':width}
    Dict['KaptGlueThickness'] = round(KapGlueTSum/6,3)
    Dict['CopperEdgeDistance'] = round(CopperEdgeDSum/6,3)
    print('HoleSlotDistance:%s' %Dict['HoleSlotDist'])
    print('HoleToEdge:',HoleToEdge)
    print('NotchToEdge:',NotchToEdge)
    print('MaxInsc_Circle:', MaxCenter)
    print('Width: %f' % width)
    print('KatonGlueThickness: %f' % round(KapGlueTSum/6,3))
    print('CopperEdgeDistance: %f' % round(CopperEdgeDSum/6,3))



# Step 1: Get the parsers ready
parser = argparse.ArgumentParser(description='CMM data extraction')
parser.add_argument('--folder'  , default=None, help = 'Folder containing the baseplate data')

args = parser.parse_args()

if args.folder is None:
    print('Folder is MANDATORY, parse the folder by --folder')
    sys.exit(0)

print('========> Input directory is %s <========='% args.folder)

# Step 2: Get input and output folders ready
currentPath = os.getcwd()
inputDir = os.path.join(currentPath , args.folder)
outputDir = inputDir.replace("inputs","outputs")
if not os.path.exists(outputDir):
    os.makedirs(outputDir)
# print(path)
# print(inputDir)


# Step 3: Get the list of all baseplates in the folder 
baseplateList=[]
for x in os.listdir(inputDir):
    if x.startswith("Baseplate"):
        baseplateList.append(x)
# print(baseplateList)

print('\nFound %d baseplates in the input directory'% len(baseplateList))

# Step 4: Merge the backside and frontside into results.txt for all the baseplates
for bplate in baseplateList:
    print('======== Merging results for %s ==========='% bplate)
    results = ""
    with open(os.path.join(inputDir, bplate, "Backside_results.txt")) as fp:
        results += fp.read() 
    results += "\n"
    with open(os.path.join(inputDir, bplate, "Frontside_results.txt")) as fp:
        results += fp.read()
    with open (os.path.join(inputDir, bplate, "Results.txt"), 'w') as fp:
        fp.write(results)   
        fp.close() 
print('**************** Merge done *******************')


# Step 5: Checking if all the baseplates have all the features and filled the Ref in dictionary.
LineRef = {}
for bplate in baseplateList:
    print('======== Checking features in %s ==========='% bplate)
    path = os.path.join(inputDir,bplate,"Results.txt")
    Line = check(path)
    LineRef[bplate] = Line
print('***************** The features have been checked with the above exceptions **************')

# Step 6: Extract the results in the dictionary.

print('================= Extracting the feature values ===============')
Data = {}
for bplate in baseplateList:
    path = os.path.join(inputDir,bplate,"Results.txt")
    print('======== Extracting features from %s ==========='% bplate)
    Dict = {}
    for key in Features:
        for value in Features[key]:
            if LineRef[bplate][value] < 0:
                continue
            Dict[value] = {}
            for param in shift[key]:
                featureValue = linecache.getline(path,LineRef[bplate][value]+shift[key][param]['down']+1).split()[shift[key][param]['right']]
                Dict[value][param]=round(float(featureValue),3)
                print(bplate,key,value,param,featureValue)
    DerivedQtts() # Step 7: Calculate the derived quantities
    Data[bplate] = Dict



# Step 8: Dump the dictionary into the json and save it in the folder.

with open(os.path.join(outputDir,'Data.txt'), 'w') as fp:
    fp.write(json.dumps(Data))
    fp.close()
print('================= Data stored in the Data.txt in the input folder ===============')

# step 9: Filling up a excel sheet.

workbook = xlsxwriter.Workbook(os.path.join(outputDir,'Baseplate_Survey.xlsx'))
worksheet = workbook.add_worksheet()
row = 5
col = 5
for i in range(len(baseplateList)):
    bplate = baseplateList[i]
    worksheet.write(row,col+i,Data[bplate]['Flatness_Plane']['Flatness'])
    worksheet.write(row+1,col+i,Data[bplate]['Hole']['Diameter'])
    worksheet.write(row+2,col+i,Data[bplate]['Hole_Depth']['DZ'])
    worksheet.write(row+3,col+i,Data[bplate]['Slot']['Diameter_1'])
    worksheet.write(row+4,col+i,Data[bplate]['Slot']['Diameter_2'])
    worksheet.write(row+5,col+i,Data[bplate]['Slot_Depth']['DZ'])
    HoleSlotDist = dist2D(float(Data[bplate]['Hole']['X']),float(Data[bplate]['Hole']['Y']),float(Data[bplate]['Slot']['X']),float(Data[bplate]['Slot']['Y']))
    worksheet.write(row+6,col+i,HoleSlotDist)
    KaptGlueThickness = np.average([float(Data[bplate]['C1_Depth']['DZ']),float(Data[bplate]['C2_Depth']['DZ']),
                            float(Data[bplate]['C3_Depth']['DZ']),float(Data[bplate]['C4_Depth']['DZ']),
                            float(Data[bplate]['C5_Depth']['DZ']),float(Data[bplate]['C6_Depth']['DZ'])])
    worksheet.write(row+7,col+i,KaptGlueThickness)
    for j in range(6):
        Notchi = 'Notch'+str(j+1)
        worksheet.write(row+8+j,col+i,Data[bplate][Notchi]['Diameter'])
    for j in range(6):
        MBi = 'MB'+str(j+1)
        worksheet.write(row+14+j,col+i,Data[bplate][MBi]['Diameter'])
workbook.close()