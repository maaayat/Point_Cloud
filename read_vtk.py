from paraview.simple import *

from vtk import vtkStructuredPointsReader
from vtk.util import numpy_support as VN
import matplotlib.pyplot as plt
from scipy.interpolate import griddata
import numpy as np
import vtk
from vtk.util.numpy_support import vtk_to_numpy
from evtk.hl import gridToVTK
from evtk.hl import pointsToVTK
from vtk.numpy_interface import algorithms as algs


reader = vtkStructuredPointsReader()
reader.SetFileName('/Users/Ayat/Downloads/u.res.hdf5.vtk')
reader.ReadAllVectorsOn()
reader.ReadAllScalarsOn()
reader.Update()

data = reader.GetOutput()

reader2 = vtkStructuredPointsReader()
reader2.SetFileName('/Users/Ayat/Downloads/v.res.hdf5.vtk')
reader2.ReadAllVectorsOn()
reader2.ReadAllScalarsOn()
reader2.Update()

data2 = reader2.GetOutput()

reader3 = vtkStructuredPointsReader()
reader3.SetFileName('/Users/Ayat/Downloads/w.res.hdf5.vtk')
reader3.ReadAllVectorsOn()
reader3.ReadAllScalarsOn()
reader3.Update()

data3 = reader3.GetOutput()

#data.GetPointData().AddArray(data2.GetPointData().GetArray('v'))
Vx = data.GetPointData().GetArray('u')
Vy = data2.GetPointData().GetArray('v')
Vz = data3.GetPointData().GetArray('w')
numpy_Vx = vtk_to_numpy(Vx)
numpy_Vy = vtk_to_numpy(Vy)
numpy_Vz = vtk_to_numpy(Vz)
velocity = algs.make_vector (numpy_Vx, numpy_Vy, numpy_Vz)
for ind in range(data.GetNumberOfPoints()):
    for j in range(3):
        numpy_velocity[ind,j]=velocity[ind][j]

numpy_velocity = vtk_to_numpy(velocity)
#data.PointData.append(velocity)
numpy_velocity = np.zeros(data.GetNumberOfPoints())

x = np.zeros(data.GetNumberOfPoints())
y = np.zeros(data.GetNumberOfPoints())
z = np.zeros(data.GetNumberOfPoints())

for i in range(data.GetNumberOfPoints()):
    x[i],y[i],z[i] = data.GetPoint(i)

f = open('workfile.vtk', 'w')
f.write('# vtk DataFile Version 4.0\n')
f.write('vtk output\n')
f.write('ASCII\n')
f.write('DATASET STRUCTURED_GRID\n')
f.write('DIMENSIONS 202 102 102\n')
f.write('POINTS 2101608 float\n')
#temp = [numpy_Vx, numpy_Vy, numpy_Vz]
#f.write(str(temp))
#f.write(" ".join(map(str,numpy_Vx)))

#for row in zip(x, y, z):
    #f.write(row.join('\n'))

for ind in range(data.GetNumberOfPoints()):
    f.write(str(x[ind]))
    f.write(" ")
    f.write(str(y[ind]))
    f.write(" ")
    f.write(str(z[ind]))
    f.write('\n')
            
f.write('VECTORS velocity float\n')

for ind in range(data.GetNumberOfPoints()):
    f.write(str(numpy_Vx[ind]))
    f.write(" ")
    f.write(str(numpy_Vy[ind]))
    f.write(" ")
    f.write(str(numpy_Vz[ind]))
    f.write('\n')

f.close()


temp = np.zeros([202, 102, 102])

pointsToVTK("./velocity_points_2", x, y, z, data = {"Velocity" : velocity})
#gridToVTK("./velocity_points", x, y, z, data = {"Velocity" : velocity})
#pointsToVTK("./points", x, y, z, data = {"temp" : temp, "pressure" : pressure})
#Get the coordinates of the nodes and their temperatures
#nodes_vtk_array= data.GetPoint()
#print vtk_to_numpy(nodes_vtk_array)
#nodes_nummpy_array = vtk_to_numpy(nodes_vtk_array)
#x,y,z= nodes_nummpy_array[:,0] , nodes_nummpy_array[:,1] , nodes_nummpy_array[:,2]
#pointsToVTK("./velocity_points", x, y, z, data = {"u" : Vx, "v" : Vy, "w" : Vz})
#Show()
#Render()
