import numpy as np
import Auxillary
import math
thetas = [300.0064, 239.9840, 180.0091, 120.0022, 59.9955, 359.9950]
ptsOnLine = [[149.0838, 47.2476], [154.6896, -37.4743], [84.3724, -83.3639],
                [9.1576, -44.0578], [2.7990, 33.1220], [78.2479, 83.4422]]

# cen,rad = Auxillary.max_insc(thetas,ptsOnLine)
# print(cen,rad)
point = [80.005, 0.039]
for i in range(6):

    D = Auxillary.distance(point[0],point[1],math.tan(math.radians(thetas[i])),-1,ptsOnLine[i][1]-math.tan(math.radians(thetas[i]))*ptsOnLine[i][0])
    print(D)