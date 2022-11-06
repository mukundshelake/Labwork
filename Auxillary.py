# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 22:32:14 2022

@author: Om
"""
import math
# Functions

def distance(x1, y1, a, b, c):
      
    d = abs((a * x1 + b * y1 + c)) / (math.sqrt(a * a + b * b))
    return d

def dist(thetas,ptsOnLine,point):
  Ds = []
  for i in range(len(thetas)):
    d= distance(point[0],point[1],math.tan(math.radians(thetas[i])),-1,ptsOnLine[i][1]-math.tan(math.radians(thetas[i]))*ptsOnLine[i][0])
    #print(d)
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

def find_line(word,file_name):
    # string to search in file
    with open(file_name, 'r') as fp:
        # read all lines using readline()
        lines = fp.readlines()
        for row in lines:
            # check if string present on a current line
        
           # print(row.find(word))
            # find() method returns -1 if the value is not found,
            # if found it return 0
            if row.find(word) >= 0:
                #print('string exists in file')
                #print('line Number:', lines.index(row))
                return lines.index(row)
        return -1

shift = {'Line':{'X':1,'Y':2,'Z':3,'Angle':4},'Circle':{'X':1,'Y':2,'Z':3,'Diameter':4},'Ellipse':{'X':1,'Y':2,'Z':3,'Diameter_1':8,'Diameter_2':9},'Plane':{'Flatness':5},'Distance':{'SC':1,'DZ':2},'Depth':{'DZ':1}}

