from paraview.simple import *
paraview.simple._DisableFirstRenderCameraReset()
import sys, time
import paraview.servermanager as sm
# Creates a new built-in session and makes it the active session.
#def Connect(ds_host=None, ds_port=11111, rs_host=None, rs_port=11111)
#Connect()
#Connect('localhost',10001)
start_time = time.time()
Segment_aa_clean_try_ = XMLPartitionedUnstructuredGridReader( FileName=['/work/blueridge/maaayat/Segment_aa_clean_try_0.pvtu', '/work/blueridge/maaayat/Segment_aa_clean_try_1.pvtu', '/work/blueridge/maaayat/Segment_aa_clean_try_2.pvtu', '/work/blueridge/maaayat/Segment_aa_clean_try_3.pvtu', '/work/blueridge/maaayat/Segment_aa_clean_try_4.pvtu', '/work/blueridge/maaayat/Segment_aa_clean_try_5.pvtu', '/work/blueridge/maaayat/Segment_aa_clean_try_6.pvtu', '/work/blueridge/maaayat/Segment_aa_clean_try_7.pvtu', '/work/blueridge/maaayat/Segment_aa_clean_try_8.pvtu', '/work/blueridge/maaayat/Segment_aa_clean_try_9.pvtu', '/work/blueridge/maaayat/Segment_aa_clean_try_10.pvtu', '/work/blueridge/maaayat/Segment_aa_clean_try_11.pvtu', '/work/blueridge/maaayat/Segment_aa_clean_try_12.pvtu', '/work/blueridge/maaayat/Segment_aa_clean_try_13.pvtu', '/work/blueridge/maaayat/Segment_aa_clean_try_14.pvtu', '/work/blueridge/maaayat/Segment_aa_clean_try_15.pvtu', '/work/blueridge/maaayat/Segment_aa_clean_try_16.pvtu', '/work/blueridge/maaayat/Segment_aa_clean_try_17.pvtu', '/work/blueridge/maaayat/Segment_aa_clean_try_18.pvtu', '/work/blueridge/maaayat/Segment_aa_clean_try_19.pvtu', '/work/blueridge/maaayat/Segment_aa_clean_try_20.pvtu', '/work/blueridge/maaayat/Segment_aa_clean_try_21.pvtu', '/work/blueridge/maaayat/Segment_aa_clean_try_22.pvtu', '/work/blueridge/maaayat/Segment_aa_clean_try_23.pvtu', '/work/blueridge/maaayat/Segment_aa_clean_try_24.pvtu', '/work/blueridge/maaayat/Segment_aa_clean_try_25.pvtu', '/work/blueridge/maaayat/Segment_aa_clean_try_26.pvtu', '/work/blueridge/maaayat/Segment_aa_clean_try_27.pvtu', '/work/blueridge/maaayat/Segment_aa_clean_try_28.pvtu', '/work/blueridge/maaayat/Segment_aa_clean_try_29.pvtu', '/work/blueridge/maaayat/Segment_aa_clean_try_30.pvtu', '/work/blueridge/maaayat/Segment_aa_clean_try_31.pvtu', '/work/blueridge/maaayat/Segment_aa_clean_try_32.pvtu', '/work/blueridge/maaayat/Segment_aa_clean_try_33.pvtu', '/work/blueridge/maaayat/Segment_aa_clean_try_34.pvtu', '/work/blueridge/maaayat/Segment_aa_clean_try_35.pvtu', '/work/blueridge/maaayat/Segment_aa_clean_try_36.pvtu', '/work/blueridge/maaayat/Segment_aa_clean_try_37.pvtu', '/work/blueridge/maaayat/Segment_aa_clean_try_38.pvtu', '/work/blueridge/maaayat/Segment_aa_clean_try_39.pvtu', '/work/blueridge/maaayat/Segment_aa_clean_try_40.pvtu', '/work/blueridge/maaayat/Segment_aa_clean_try_41.pvtu', '/work/blueridge/maaayat/Segment_aa_clean_try_42.pvtu', '/work/blueridge/maaayat/Segment_aa_clean_try_43.pvtu', '/work/blueridge/maaayat/Segment_aa_clean_try_44.pvtu', '/work/blueridge/maaayat/Segment_aa_clean_try_45.pvtu', '/work/blueridge/maaayat/Segment_aa_clean_try_46.pvtu', '/work/blueridge/maaayat/Segment_aa_clean_try_47.pvtu', '/work/blueridge/maaayat/Segment_aa_clean_try_48.pvtu', '/work/blueridge/maaayat/Segment_aa_clean_try_49.pvtu']
 )

Segment_aa_clean_try_.PointArrayStatus = ['C']
Segment_aa_clean_try_.CellArrayStatus = ['vtkOriginalCellIds']

RenderView2 = GetRenderView()
XMLPartitionedUnstructuredGridReader1 = FindSource("XMLPartitionedUnstructuredGridReader1")
my_representation0 = GetDisplayProperties(XMLPartitionedUnstructuredGridReader1)
DataRepresentation1 = Show()
DataRepresentation1.ScaleFactor = 1.3661699652671815
DataRepresentation1.ScalarOpacityUnitDistance = 0.091610014263403095
DataRepresentation1.SelectionPointFieldDataArrayName = 'C'
DataRepresentation1.EdgeColor = [0.0, 0.0, 0.50000762951094835]

RenderView2.CameraClippingRange = [57.72381277421438, 90.676447770150162]

Render()
print "Time elapsed: ", time.time() - start_time, "s"