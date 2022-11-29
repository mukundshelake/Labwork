import math
# Functions

def pointLineDist(pt, ptOnLine, LineSlope):
  a = math.tan(math.radians(LineSlope))
  b = -1
  c = ptOnLine[1] - a*ptOnLine[0]
  d = abs((a * pt[0] + b * pt[1] + c)) / (math.sqrt(a * a + b * b))
  return round(d,3)


def maxInsc(center, ptsOnLines, thetas):
  print(center)
  print(ptsOnLines)
  print(thetas)
  delta = 0.001
  steps = 1000
  R = 50.0
  D = 100.0
  maxCenter = center
  for i in range(steps):
    for j in range(steps):
      center = [0.0 + (i-steps/2)*delta, 0.0 + (j-steps/2)*delta] 
      for k in range(len(thetas)):
        d = pointLineDist(center, ptsOnLines[k], thetas[k])
        # print(d)
        if d < D:
          D = d
          # print(d,D)
      if D > R:
        R = D
        # print(d,D,R)
        maxCenter = [round(center[0],3),round(center[1],3)]
  width = round(2.0*R,3)
  return maxCenter, width


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
    Center=[0,0]
    delta=0.001
    steps=1000
    R = 50
    for i in range(steps):
      for j in range(steps):
        point = [0.0+(i-steps/2)*delta,0.0+(j-steps/2)*delta]
        X = dist(thetas,ptsOnLine,point)
        if X > R:
          R = X
          Center = [0.0+(i-steps/2)*delta,0.0+(j-steps/2)*delta]

    return(Center, R)   
##############################################
def Insc(ptsOnLines, thetas):
  Center = [0.0,0.0]
  delta = 0.001
  steps = 1000
  R = 50.0
  for i in range(steps):
    for j in range(steps):
      Center = [0.0+(i-steps/2)*delta, 0.0+(j-steps/2)*delta]
      D = 100.0
      for k in range(6):
        d = pointLineDist(Center, ptsOnLines[k], thetas[k])
        if d<D:
          D = d
      if D > R:
        R = D
        maxCenter = [round(Center[0],3),round(Center[1],3)]
  return maxCenter, round(2.0*R,3)

def maxInsc(center, ptsOnLines, thetas):
  print(center)
  print(ptsOnLines)
  print(thetas)
  delta = 0.001
  steps = 2000
  R = 50.0
  D = 100.0
  maxCenter = center
  for i in range(steps):
    for j in range(steps):
      center = [center[0] + (i-steps/2)*delta, center[1] + (j-steps/2)*delta] 
      for k in range(len(thetas)):
        d = pointLineDist(center, ptsOnLines[k], thetas[k])
        # print(d)
        if d < D:
          D = d
          # print(d,D)
      if D > R:
        R = D
        # print(d,D,R)
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










thetas = [120.002, 0.022, 240.008, 299.986, 0.044, 60.068]
ptsOnLine = [[-72.263, -41.789], [0.891, -83.478], [76.061, -35.264], [70.43, 45.108], [-31.11, 83.491], [-85.135, 19.557]]



#### Baseplate 2
ptsOnLine = [[-72.853, -40.686], [7.284, -83.451], [66.429, -51.865], [69.941, 45.943], [-6.045, 83.519], [-82.388, 24.379]]
thetas = [120.009, 359.993, 240.007, 299.984, 359.998, 60.036]



#### Baseplate 3
# ptsOnLine = [[-68.284, -48.748], [6.283, -83.475], [79.504, -29.327], [67.648, 49.953], [-6.159, 83.565], [-81.815, 25.373]]
# thetas = [120.011, 180.056, 239.971, 299.975, 0.017, 60.065]

# #### Baseplate 4
# ptsOnLine = [[-68.05, -49.06], [3.424, -83.452], [76.141, -35.044], [68.5, 48.452], [2.673, 83.531], [-79.028, 30.172]]   
# thetas = [120.002, 0.019, 240.02, 299.999, 0.035, 60.029]


center,R = max_insc(thetas,ptsOnLine)
print(center,2*R)

for i in range(6):
  print(2*pointLineDist(center,ptsOnLine[i],thetas[i]))

# cent,w = maxInsc([0.0,0.0],ptsOnLine,thetas)
# print(cent,w)



cent,w = Insc(ptsOnLine, thetas)
print(cent,w)

for i in range(6):
  print(2*pointLineDist(cent,ptsOnLine[i],thetas[i]))