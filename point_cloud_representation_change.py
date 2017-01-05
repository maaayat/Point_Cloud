#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# find source
seb3rd_new_agpvtu = FindSource('seb3rd_new_ag.pvtu')

# set active source
SetActiveSource(seb3rd_new_agpvtu)

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1073, 575]

# get display properties
seb3rd_new_agpvtuDisplay = GetDisplayProperties(seb3rd_new_agpvtu, view=renderView1)

# set scalar coloring
ColorBy(seb3rd_new_agpvtuDisplay, ('POINTS', 'C'))

# rescale color and/or opacity maps used to include current data range
seb3rd_new_agpvtuDisplay.RescaleTransferFunctionToDataRange(True)

# show color bar/color legend
seb3rd_new_agpvtuDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'C'
cLUT = GetColorTransferFunction('C')
cLUT.LockDataRange = 0
cLUT.InterpretValuesAsCategories = 0
cLUT.ShowCategoricalColorsinDataRangeOnly = 0
cLUT.RescaleOnVisibilityChange = 0
cLUT.EnableOpacityMapping = 0
cLUT.RGBPoints = [0.0, 0.0, 0.0, 0.0, 255.0, 1.0, 1.0, 1.0]
cLUT.UseLogScale = 0
cLUT.ColorSpace = 'RGB'
cLUT.UseBelowRangeColor = 0
cLUT.BelowRangeColor = [0.0, 0.0, 0.0]
cLUT.UseAboveRangeColor = 0
cLUT.AboveRangeColor = [1.0, 1.0, 1.0]
cLUT.NanColor = [1.0, 0.0, 0.0]
cLUT.Discretize = 1
cLUT.NumberOfTableValues = 256
cLUT.ScalarRangeInitialized = 1.0
cLUT.HSVWrap = 0
cLUT.VectorComponent = 0
cLUT.VectorMode = 'Magnitude'
cLUT.AllowDuplicateScalars = 1
cLUT.Annotations = []
cLUT.ActiveAnnotatedValues = []
cLUT.IndexedColors = []

# get opacity transfer function/opacity map for 'C'
cPWF = GetOpacityTransferFunction('C')
cPWF.Points = [0.0, 0.0, 0.5, 0.0, 255.0, 1.0, 0.5, 0.0]
cPWF.AllowDuplicateScalars = 1
cPWF.ScalarRangeInitialized = 1

# change representation type
seb3rd_new_agpvtuDisplay.SetRepresentationType('Points')

# hide color bar/color legend
seb3rd_new_agpvtuDisplay.SetScalarBarVisibility(renderView1, False)

# find source
seb3rd_new_ahpvtu = FindSource('seb3rd_new_ah.pvtu')

# set active source
SetActiveSource(seb3rd_new_ahpvtu)

# get display properties
seb3rd_new_ahpvtuDisplay = GetDisplayProperties(seb3rd_new_ahpvtu, view=renderView1)

# set scalar coloring
ColorBy(seb3rd_new_ahpvtuDisplay, ('POINTS', 'C'))

# rescale color and/or opacity maps used to include current data range
seb3rd_new_ahpvtuDisplay.RescaleTransferFunctionToDataRange(True)

# show color bar/color legend
seb3rd_new_ahpvtuDisplay.SetScalarBarVisibility(renderView1, True)

# change representation type
seb3rd_new_ahpvtuDisplay.SetRepresentationType('Points')

# hide color bar/color legend
seb3rd_new_ahpvtuDisplay.SetScalarBarVisibility(renderView1, False)

# find source
seb3rd_new_aipvtu = FindSource('seb3rd_new_ai.pvtu')

# set active source
SetActiveSource(seb3rd_new_aipvtu)

# get display properties
seb3rd_new_aipvtuDisplay = GetDisplayProperties(seb3rd_new_aipvtu, view=renderView1)

# set scalar coloring
ColorBy(seb3rd_new_aipvtuDisplay, ('POINTS', 'C'))

# rescale color and/or opacity maps used to include current data range
seb3rd_new_aipvtuDisplay.RescaleTransferFunctionToDataRange(True)

# show color bar/color legend
seb3rd_new_aipvtuDisplay.SetScalarBarVisibility(renderView1, True)

# change representation type
seb3rd_new_aipvtuDisplay.SetRepresentationType('Points')

# hide color bar/color legend
seb3rd_new_aipvtuDisplay.SetScalarBarVisibility(renderView1, False)

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [8.3302001953125, -16.93390029668808, 743.7521609859978]
renderView1.CameraFocalPoint = [8.3302001953125, -16.93390029668808, 575.0546875]
renderView1.CameraParallelScale = 43.66211899885375

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).