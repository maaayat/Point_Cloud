try: paraview.simple
except: from paraview.simple import *


u_res_hdf5_vtk = LegacyVTKReader( FileNames=['/Users/Ayat/Downloads/u.res.hdf5.vtk'] )
vu = u_res_hdf5_vtk.PointData['u']

v_res_hdf5_vtk = LegacyVTKReader( FileNames=['/Users/Ayat/Downloads/v.res.hdf5.vtk'] )
vv = v_res_hdf5_vtk.PointData['v']

w_res_hdf5_vtk = LegacyVTKReader( FileNames=['/Users/Ayat/Downloads/w.res.hdf5.vtk'] )
vw = w_res_hdf5_vtk.PointData['w']

pdi = w_res_hdf5_vtk.GetPolyDataInput()

nodes_vtk_array= u_res_hdf5_vtk.GetOutput().GetPoints().GetData()

gridToVTK("./structured", x, y, z, cellData = {"pressure" : pressure}, pointData = {"temp" : temp})

coord = pdi.GetPoint(0)
print coord
Calculator1= Calculator(Function = 'vu*iHat+vv*jHat+vw*kHat')
Show()
Glyph1 = Glyph(
               Vectors = ['POINTS', 'Result'],
               GlyphType = 'Arrow',
               SetScaleFactor = 1.0,
               )
Show()

Render()
w_res_hdf5_vtk.PointData[:]
dataInfo = w_res_hdf5_vtk.GetDataInformation()
pointDataInfo = dataInfo.GetPointDataInformation()
arrayInfo = pointDataInfo.GetArrayInformation("w")

