"""
This script corrects the faulty nomenclature for the BEs in the Backside_results.txt

Helper library: Auxillary.py

********* Caution: Check if you have already done it ******************
"""

# from config.Auxillary import find_line
# import os
# import sys
# import argparse


# Corrections = [['BE1','BE5'],['BE2', 'BE4'], ['BE4', 'BE2'], ['BE5', 'BE1']]

# parser = argparse.ArgumentParser(description='CMM data correction')
# parser.add_argument('--folder'  , default=None, help = 'Folder containing the baseplate data')

# args = parser.parse_args()

# if args.folder is None:
#     print('Folder is MANDATORY, parse the folder by --folder')
#     sys.exit(0)



# currentPath = os.getcwd()
# inputDir = os.path.join(currentPath , args.folder)
# outputDir = inputDir.replace("inputs","outputs")
# if not os.path.exists(outputDir):
#     os.makedirs(outputDir)


# baseplateList=[]
# for x in os.listdir(inputDir):
#     if x.startswith("Baseplate"):
#         baseplateList.append(x)


# for bplate in baseplateList:
#     print('======== Correcting results for %s ==========='% bplate)
#     with open(os.path.join(inputDir, bplate, "Backside_results.txt"))  as fp:
#         data = fp.read()
#         data = data.replace('BE1', 'BE7')
#         data = data.replace('BE2', 'BE8')
#         data = data.replace('BE4', 'BE2')
#         data = data.replace('BE5', 'BE1')
#         data = data.replace('BE7', 'BE5')
#         data = data.replace('BE8', 'BE4')
#     with open(os.path.join(inputDir, bplate, "Backside_results.txt"), 'w')  as fp:
#         fp.write(data)
#     fp.close()


    


