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
  """
  Finds the linenumber a word FIRST appears in
  :param word: string containing the word to look for
  :param file_name: string containing file address to open
  :return: integer containing the first line number the word appears in
  """
    with open(file_name, 'r') as fp:
        lines = fp.readlines()
        for row in lines:
            if row.find(word) >= 0:
                return lines.index(row)
        return -1

def check(path):
  """
  Checks for and prints missing features from the features dict
  :param path: string containing full pathname to combined results.txt
  :return: Dict containing line numbers for each feature {feature:line_no}
  TODO Return and handle missing features instead of just printing
  """
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
  """
  :param x1,y1, x2, y2: x and y coordinates of the first and second points respectively
  :return: Float containing 2 Dimensional distances between the 2 given points
  """
  d = math.sqrt((x2-x1)**2 + (y2-y1)**2)
  return round(d,3)

def pointLineDist(pt, ptOnLine, LineAngle):
  """
  Calculates the distance of a point from a line
  :param pt: list containing coords of the point from which distance is to be calculated
  :param ptONLine: list containing coords of the point that lies on the line
  :param LineAngle: float containing angle of the line wrt X axis?
  :return: Float containing the shortest distance between point and the given line
  """
  a = math.tan(math.radians(LineAngle))
  b = -1
  c = ptOnLine[1] - a*ptOnLine[0]
  d = abs((a * pt[0] + b * pt[1] + c)) / (math.sqrt(a * a + b * b))
  return round(d,3)


def Insc(center, ptsOnLines, thetas):
  """
  Try to inscribe a circle of the maximum size by scanning near the central region a lot of 
  times and insribing circles of maximum sizes
  :param center: list containing the center of the hexagon as measured by CMM
  :param ptsONLine: list containing points on line of each of the six edges
  :param thetas: list containing angles of each of the six edges
  :return: ? Center of the calculated maximum inscribed circle?
  TODO Implement proper circle inscribing algorithm using midpoint of each edge
  """
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







