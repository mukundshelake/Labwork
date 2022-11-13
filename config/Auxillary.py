# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 22:32:14 2022

@author: Om
"""
import math


Features = {
              'Plane' :   ['Flatness_Plane'],
              'Circle':   ['Hole','Notch1','Notch2','Notch3','Notch4','Notch5','Notch6',
                            'MB1','MB2','MB3','MB4','MB5','MB6','F1','F2','F3','F4','F5','F6','F7',
                            'F8','F9','F10','F11','F12','F13','F14','F15','F16','F17','F18','F19'],
              'Ellipse':  ['Slot'],
              'Line'  :   ['BE1','BE2','BE3','BE4','BE5','BE6','FE1','FE2','FE3','FE4','FE5','FE6',
                            'KE1','KE2','KE3','KE4','KE5','KE6'],
              'Distance': ['Hole_Depth','Slot_Depth','C1_Depth','C2_Depth','C3_Depth',
                            'C4_Depth','C5_Depth','C6_Depth']
}

shift = { 'Line':    {'X':{'down':1,'right':3},'Y':{'down':2,'right':3},
                      'Z':{'down':3,'right':3},'Angle':{'down':4,'right':3}},
          'Circle':  {'X':{'down':1,'right':3},'Y':{'down':2,'right':3},
                      'Z':{'down':3,'right':3},'Diameter':{'down':4,'right':2}},
          'Ellipse': {'X':{'down':1,'right':3},'Y':{'down':2,'right':3},'Z':{'down':3,'right':3},
                      'Diameter_1':{'down':8,'right':2},'Diameter_2':{'down':9,'right':2}},
          'Plane':   {'Flatness':{'down':5,'right':2}},
          'Distance':{'DZ':{'down':1,'right':2}}
          }

def find_line(word,file_name):
    with open(file_name, 'r') as fp:
        lines = fp.readlines()
        for row in lines:
            if row.find(word) >= 0:
                return lines.index(row)
        return -1

def check(path):
    Line  = {}
    for value in Features.values():
      for feature in value:
        line_no=find_line(feature,path)
        if find_line(feature + '_Modified',path) > 0:
            line_no=find_line(feature + '_Modified',path)
        if line_no < 0:
            print('%s Not found'%(feature))
        Line[feature]=line_no
    return Line

def dist2D(x1,y1,x2,y2):
  d = math.sqrt((x2-x1)**2 + (y2-y1)**2)
  return round(d,3)

def pointLineDist(pt, ptOnLine, LineSlope):
  a = math.tan(math.radians(LineSlope))
  b = -1
  c = ptOnLine[1] - a*ptOnLine[0]
  d = abs((a * pt[0] + b * pt[1] + c)) / (math.sqrt(a * a + b * b))
  return round(d,3)


def maxInsc(center, ptsOnLines, thetas):
  delta = 0.001
  steps = 1000
  R = 50.0
  maxCenter = center
  for i in range(steps):
    for j in range(steps):
      center = [center[0] + (i-steps/2)*delta, center[1] + (j-steps/2)*delta] 
      for i in range(len(thetas)):
        D = 100.0
        d = pointLineDist(center, ptsOnLines[i], thetas[i])
        if d < D:
          D = d
      if D > R:
        R = D
        maxCenter = [round(center[0],3),round(center[1],3)]
  width = round(2.0*R,3)
  return maxCenter, width
  
##################################################

def dist(thetas,ptsOnLine,point):
  Ds = []
  for i in range(len(thetas)):
    d= distance(point[0],point[1],math.tan(math.radians(thetas[i])),-1,ptsOnLine[i][1]-math.tan(math.radians(thetas[i]))*ptsOnLine[i][0])
    Ds.append(d)
  return (min(Ds))


def max_insc(thetas,ptsOnLine):
    Center=[80,0]
    delta=0.001
    steps=1000
    R = 50
    for i in range(steps):
      for j in range(steps):
        point = [80.0+(i-steps/2)*delta,0.0+(j-steps/2)*delta]
        X = dist(thetas,ptsOnLine,point)
        print(X)
        if X > R:
          R = X
          Center = point
    return(Center, R)   







