#  Pointcloud_Server.py
#  
#
#  Created by Ayat Mohammed on 8/12/15.
#
from paraview.simple import *
import paraview.servermanager as sm


# Creates a new built-in session and makes it the active session.
#def Connect(ds_host=None, ds_port=11111, rs_host=None, rs_port=11111)
#Connect()
Connect('localhost',10001)

#sphere=Sphere()
#for x in range(0, 50):
reader = sm.sources.XMLUnstructuredGridReader(FileName = "/work/blueridge/maaayat/seb3rd_new/seb3rd_new_al.vtu")
d3 = sm.filters.D3(Input = reader)
    #d3output = sm.Fetch(d3)
writer = sm.writers.XMLPUnstructuredGridWriter(Input = d3, FileName = "/work/blueridge/maaayat/seb3rd_new/seb3rd_new_al.pvtu")
writer.UpdatePipeline()

renModule = sm.CreateRenderView()
cone = Cone()
display = sm.CreateRepresentation(cone, renModule)

# Creates a new render view on the active session.
view = sm.CreateRenderView()
repr = sm.CreateRepresentation(d3, view)
"""
reader.UpdatePipeline()
dataInfo = reader.GetDataInformation()
pointDataInfo = dataInfo.GetPointDataInformation()
arrayInfo = pointDataInfo.GetArrayInformation("displacement9")
"""


# Create a new sphere proxy on the active session and register it
# in the sources group.
#sphere = sm.sources.SphereSource(registrationGroup="sources", ThetaResolution=16, PhiResolution=32)

# Create a representation for the sphere proxy and adds it to the render
# module.
#display = sm.CreateRepresentation(sphere, renModule)
#cone = Cone()
#display = sm.CreateRepresentation(cone, renModule)
#help(cone)
renModule.StillRender()
view.StillRender()
#sm.Disconnect()
