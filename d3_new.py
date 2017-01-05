from paraview import servermanager
from paraview.simple import *
import os
import sys
import time



def test_d3():
    
    from paraview import simple
    #  reader = simple.XMLUnstructuredGridReader(FileName = [ "/work/blueridge/maaayat/seb3rd_new/seb3rd_new_aa.vtu"])
    t0 = time.time()
    reader = simple.XMLUnstructuredGridReader(FileName = [ "/work/blueridge/maaayat/seb3rd_new/seb3rd_new_aa.vtu"])
    print time.time() - t0
    print "Done loading"
    t0 = time.time()
    d3 = simple.D3(Input = reader)
    d3.MinimalMemory = 1
    #view = simple.CreateRenderView()
    #dp = simple.GetDisplayProperties(d3)
    #dp.Representation = 'Points'
    #Show()
    #Render()
    print time.time() - t0
    
    t0 = time.time()
    writer = paraview.simple.XMLPUnstructuredGridWriter(Input = d3,FileName=["/work/blueridge/maaayat/seb3rd_new/seb3rd_aa/seb3rd_new_aa.pvtu"])
    #writer.Writealltimestepsasfileseries = 1
    writer.UpdatePipeline()
    print time.time() - t0
