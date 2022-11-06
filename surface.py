
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np 
from statistics import mean

f = open('Surface_Points.txt')
#f = open('30March2022_BPlate6_without_vac.txt')
lines=f.readlines()
x_values=[]
y_values = []
z_values = []
for x in lines:
    x_values.append(float(x.split('\t')[0]))
    y_values.append(float(x.split('\t')[1]))
    z_values.append(float(x.split('\t')[2]))
f.close()

fig = plt.figure()
ax = plt.axes(projection='3d')
im = ax.plot_trisurf(x_values, y_values, z_values, cmap = 'viridis', edgecolor = 'none')
# im = ax.plot(x_values, y_values, z_values)
ax.set_xlabel('x (mm)')
ax.set_ylabel('y (mm)')
ax.set_zlabel('z (mm)')
ax.set_zlim3d(-0.5,0.5)
plt.colorbar(im)
ax.view_init(90,270)
plt.show()
 
plt.scatter(x_values,y_values)
plt.show()
# plt.plot(x_values,y_values)
# plt.xlabel('X (mm)')
# plt.ylabel('Y (mm)')
# plt.show()

Jig_avg_pt = 31.02836
thickness = mean(z_values)-Jig_avg_pt
# print(mean(z_values))#,len(x_values),len(y_values),len(z_values))
# fig = plt.figure()
# ax = fig.add_subplot(projection='3d')
# xpos = x_values
# ypos = y_values
# zpos = 0
# dx = dy = 6



# dz = z_values


# cmap = cm.get_cmap('jet')
max_height = np.max(z_values)   # get range of colorbars so we can normalize
min_height = np.min(z_values)
# print(max_height)
# print(min_height)
# # scale each z to [0,1], and get their rgb values
# rgba = [cmap((k-min_height)/(max_height-min_height)) for k in z_values] 
# im = ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color= rgba,zsort='average')
# plt.colorbar(im)
# plt.show()
deltaz = max_height-min_height
#print(deltaz)
# print(np.sort(z_values))
# #plt.show()
