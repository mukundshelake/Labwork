# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 22:32:14 2022

@author: Om
"""
import math


Features = {
              'Plane' :   ['Plane: Flatness_Plane'],
              'Circle':   ['Circle: Hole','Circle: Notch1','Circle: Notch2','Circle: Notch3','Circle: Notch4','Circle: Notch5','Circle: Notch6',
                            'Circle: MB','Circle: MB','Circle: MB3','Circle: MB4','Circle: MB5','Circle: MB6','Circle: F1','Circle: F2','Circle: F3','Circle: F4','Circle: F5','Circle: F6','Circle: F7',
                            'Circle: F8','Circle: F9','Circle: F10','Circle: F11','Circle: F12','Circle: F13','Circle: F14','Circle: F15','Circle: F16','Circle: F17','Circle: F18','Circle: F19'],
              'Ellipse':  ['Ellipse: Slot'],
              'Line'  :   ['Line: BE1','Line: BE2','Line: BE3','Line: BE4','Line: BE5','Line: BE6','Line: FE1','Line: FE2','Line: FE3','Line: FE4','Line: FE5','Line: FE6',
                            'Line: KE1','Line: KE2','Line: KE3','Line: KE4','Line: KE5','Line: KE6'],
              'Distance': ['Distance: Hole_Depth','Distance: Slot_Depth','Distance: C1_Depth','Distance: C2_Depth','Distance: C3_Depth',
                            'Distance: C4_Depth','Distance: C5_Depth','Distance: C6_Depth']
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


def Insc(center, ptsOnLines, thetas):
  delta = 0.001
  steps = 1000
  R = 50.0
  for i in range(steps):
    for j in range(steps):
      Center = [center[0]+(i-steps/2)*delta, center[1]+(j-steps/2)*delta]
      D = 100.0
      for k in range(6):
        d = pointLineDist(Center, ptsOnLines[k], thetas[k])
        if d<D:
          D = d
      if D > R:
        R = D
        maxCenter = [round(Center[0],3),round(Center[1],3)]
  return maxCenter, round(2.0*R,3)







