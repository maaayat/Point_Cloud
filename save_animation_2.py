try: paraview.simple
except: from paraview.simple import *
paraview.simple._DisableFirstRenderCameraReset()

RenderView2 = GetRenderView()
WriteAnimation('/Users/Ayat/Desktop/3rd_br_1.avi', Magnification=4, Quality=2, FrameRate=15.000000)


Render()
