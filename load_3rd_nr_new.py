#try: paraview.simple
from paraview.simple import *
#from paraview.servermanager import *
paraview.simple._DisableFirstRenderCameraReset()

Connect('localhost',10001)

seb3rd_new_aa_pvtu = XMLUnstructuredGridReader( FileName=["/work/blueridge/maaayat/seb3rd_new/seb3rd_aa/seb3rd_new_aa.pvtu"] )
#view = CreateRenderView()
#dp = GetDisplayProperties(seb3rd_new_aa_pvtu)
#dp.Representation = 'Points'
#Show()
#Render()

seb3rd_new_aa_pvtu.PointArrayStatus = ['C']
seb3rd_new_aa_pvtu.CellArrayStatus = ['vtkOriginalCellIds']

#//////////////////// I added this here
a1_C_PVLookupTable = GetLookupTableForArray( "C", 1, RGBPoints=[0.0, 0.0, 0.0, 0.0, 255.0, 1.0, 1.0, 1.0], VectorMode='Magnitude', NanColor=[1.0, 0.0, 0.0], ColorSpace='RGB', ScalarRangeInitialized=1.0, AllowDuplicateScalars=1 )

a1_C_PiecewiseFunction = CreatePiecewiseFunction( Points=[0.0, 0.0, 0.5, 0.0, 255.0, 1.0, 0.5, 0.0] )
#//////////////////////////////////////////////////

RenderView2 = GetRenderView()
DataRepresentation1 = Show()
#///////////////////////added by me//////////////////
DataRepresentation1.Representation = 'Points'
DataRepresentation1.ScalarOpacityFunction = a1_C_PiecewiseFunction
DataRepresentation1.ColorArrayName = ('POINT_DATA', 'C')
DataRepresentation1.LookupTable = a1_C_PVLookupTable

a1_C_PVLookupTable.ScalarOpacityFunction = a1_C_PiecewiseFunction
#//////////////////////////////////////////////////////
DataRepresentation1.ScaleFactor = 4.7593899846076964
DataRepresentation1.ScalarOpacityUnitDistance = 0.13716410740132384
DataRepresentation1.SelectionPointFieldDataArrayName = 'C'
#DataRepresentation1.EdgeColor = [0.0, 0.0, 0.50000762951094835]

RenderView2.CenterOfRotation = [-4.7215995788574219, -22.108849942684174, 575.99838256835938]
Render()