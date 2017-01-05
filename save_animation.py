try: paraview.simple
except: from paraview.simple import *
paraview.simple._DisableFirstRenderCameraReset()

WriteAnimation('/Users/Ayat/Desktop/3rd_br.avi', Magnification=4, Quality=2, FrameRate=30.000000)


RenderView2 = GetRenderViews()[0]
AnimationScene2 = GetAnimationScene()
RenderView2.ViewTime = 0.0
RenderView2.CameraPosition = [-1.0233499999999998, -45.014499999999998, 628.37]
RenderView2.UseCache = 0
RenderView2.CameraClippingRange = [17.600694698125487, 107.36887334406487]

AnimationScene2.AnimationTime = 0.0

Render()
