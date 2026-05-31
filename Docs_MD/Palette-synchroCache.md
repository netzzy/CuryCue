# Palette:synchroCache

##   
  
Summary

Incoming video frames from the first input are cached and indexed according to the frame index coming in on the second input. The second input expects a single channel of the name "frame_stream". The third input expects a single channel of the name "frame_sync". The "frame_sync" channel will typically come over the network via SyncIn CHOP. 

The "frame_sync" channel is the frame index that the server of the frame index expects all clients to play. If everything works correctly, then all clients will play the same frame at the same time. 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[Palette:synchroCache Ext](</index.php?title=Palette:synchroCache_Ext&action=edit&redlink=1> "Palette:synchroCache Ext \(page does not exist\)")

## 

Parameters - Synchro Cache Page

Sync Lock`Synccache`\- When active the Sync CHOP looks for an active SyncOut CHOP to act as a server for a frame index. 

Frame Stream`Framestream`\- The frame index from the video stream. Alternatively passed using the second input of this component. 

Frame Sync`Framesync`\- The frame index of the frame server - that is received by the synchroClient component or other sync frame source. Alternatively received in the third input of this component. 

Cache Size`Cachesize`\- The number of frames to buffer from the stream in device. 

Resolution`Resolution`\- ⊞ \- The resolution of output of this component. 
* Resolution`Resolutionw`-
* Resolution`Resolutionh`-


Reset Stats`Resetstats`\- Resets the Sync information stats table. 

Fit To Viewer`Fittoviewer`\- Fits the viewer display so the video raster is completely visible. 

Dashboard`Dashboard`\- Activates the DAT info dashboard in the component viewer. 

## 

Parameters - Overlays Page

Display Overlays`Overlays`\- Displays the overlays text overlarys - in particular the frame index info 

Text Overlay Color`Statstextcolor`\- ⊞ \- The color of the text overlay 
* Text Overlay Color`Statstextcolorr`-
* Text Overlay Color`Statstextcolorg`-
* Text Overlay Color`Statstextcolorb`-
* Text Overlay Color`Statstextcolora`-


Display Frame Index`Displayframeindex`\- Activates the display of the frame index over the video feed. 

Frame Index Font Size`Frameindexfontsize`\- The size of the font for the frame overlay. 

## 

Parameters - About Page

Help`Help`\- A link to the help for this component. 

Version`Version`\- The version number for this component. 

## 

Operator Inputs
* Input 0: in1 -
  * Input 1: in2 -
  * Input 2: in3 -

## 

Operator Outputs
* Output 0 -


TouchDesigner Build: Latest\n2022.24140before 2022.24140

Palette  
---  
[Palette ](<./Palette.md> "Palette")• [Palette:arcBallCamera ](<./Palette-arcBallCamera.md> "Palette:arcBallCamera")• [Palette:arcBallGeometry ](<./Palette-arcBallGeometry.md> "Palette:arcBallGeometry")• [Palette:audioAnalysis ](<./Palette-audioAnalysis.md> "Palette:audioAnalysis")• [Palette:audioSet ](<./Palette-audioSet.md> "Palette:audioSet")• [Palette:autoMediaPlayer ](<./Palette-autoMediaPlayer.md> "Palette:autoMediaPlayer")• [Palette:battery ](<./Palette-battery.md> "Palette:battery")• [Palette:bitwigClip ](<./Palette-bitwigClip.md> "Palette:bitwigClip")• [Palette:bitwigClipSlot ](<./Palette-bitwigClipSlot.md> "Palette:bitwigClipSlot")• [Palette:bitwigDeviceRemotes ](<./Palette-bitwigDeviceRemotes.md> "Palette:bitwigDeviceRemotes")• [Palette:bitwigMain ](<./Palette-bitwigMain.md> "Palette:bitwigMain")• [Palette:bitwigNote ](<./Palette-bitwigNote.md> "Palette:bitwigNote")• [Palette:bitwigProjectRemotes ](<./Palette-bitwigProjectRemotes.md> "Palette:bitwigProjectRemotes")• [Palette:bitwigRemotesDevice ](<./Palette-bitwigRemotesDevice.md> "Palette:bitwigRemotesDevice")• [Palette:bitwigRemotesProject ](<./Palette-bitwigRemotesProject.md> "Palette:bitwigRemotesProject")• [Palette:bitwigRemotesTrack ](<./Palette-bitwigRemotesTrack.md> "Palette:bitwigRemotesTrack")• [Palette:bitwigSelect ](<./Palette-bitwigSelect.md> "Palette:bitwigSelect")• [Palette:bitwigSong ](<./Palette-bitwigSong.md> "Palette:bitwigSong")• [Palette:bitwigTrack ](<./Palette-bitwigTrack.md> "Palette:bitwigTrack")• [Palette:bitwigTrackRemotes ](<./Palette-bitwigTrackRemotes.md> "Palette:bitwigTrackRemotes")• [Palette:blendModes ](<./Palette-blendModes.md> "Palette:blendModes")• [Palette:bloom ](<./Palette-bloom.md> "Palette:bloom")• [Palette:camera ](<./Palette-camera.md> "Palette:camera")• [Palette:cameraBrowser ](<./Palette-cameraBrowser.md> "Palette:cameraBrowser")• [Palette:cameraViewport ](<./Palette-cameraViewport.md> "Palette:cameraViewport")• [Palette:camSchnappr ](<./Palette-camSchnappr.md> "Palette:camSchnappr")• [Palette:changeColor ](<./Palette-changeColor.md> "Palette:changeColor")• [Palette:changeToColor ](<./Palette-changeToColor.md> "Palette:changeToColor")• [Palette:checker ](<./Palette-checker.md> "Palette:checker")• [Palette:chromaKey ](<./Palette-chromaKey.md> "Palette:chromaKey")• [Palette:colorThreshold ](<./Palette-colorThreshold.md> "Palette:colorThreshold")• [Palette:compareComp ](<./Palette-compareComp.md> "Palette:compareComp")• [Palette:convolve ](<./Palette-convolve.md> "Palette:convolve")• [Palette:cornerPinPOP ](<./Palette-cornerPinPOP.md> "Palette:cornerPinPOP")• [Palette:cornerPinSOP ](<./Palette-cornerPinSOP.md> "Palette:cornerPinSOP")• [Palette:cppParsTemplateGen ](<./Palette-cppParsTemplateGen.md> "Palette:cppParsTemplateGen")• [Palette:customAttributes ](<./Palette-customAttributes.md> "Palette:customAttributes")• [Palette:debugControl ](<./Palette-debugControl.md> "Palette:debugControl")• [Palette:dent ](<./Palette-dent.md> "Palette:dent")• [Palette:depthExtract ](<./Palette-depthExtract.md> "Palette:depthExtract")• [Palette:depthProjection ](<./Palette-depthProjection.md> "Palette:depthProjection")• [Palette:dilate ](<./Palette-dilate.md> "Palette:dilate")• [Palette:domeViewer ](<./Palette-domeViewer.md> "Palette:domeViewer")• [Palette:encoder ](<./Palette-encoder.md> "Palette:encoder")• [Palette:equalizer ](<./Palette-equalizer.md> "Palette:equalizer")• [Palette:feedback ](<./Palette-feedback.md> "Palette:feedback")• [Palette:feedbackEdge ](<./Palette-feedbackEdge.md> "Palette:feedbackEdge")• [Palette:firmata ](<./Palette-firmata.md> "Palette:firmata")• [Palette:gal ](<./Palette-gal.md> "Palette:gal")• [Palette:geoPanel ](<./Palette-geoPanel.md> "Palette:geoPanel")• [Palette:gestureCapture ](<./Palette-gestureCapture.md> "Palette:gestureCapture")• [Palette:graphPlot ](<./Palette-graphPlot.md> "Palette:graphPlot")• [Palette:histogram ](<./Palette-histogram.md> "Palette:histogram")• [Palette:hsvBlur ](<./Palette-hsvBlur.md> "Palette:hsvBlur")• [Palette:imageSearch ](<./Palette-imageSearch.md> "Palette:imageSearch")• [Palette:julia ](<./Palette-julia.md> "Palette:julia")• [Palette:kantanMapper ](<./Palette-kantanMapper.md> "Palette:kantanMapper")• [Palette:kinectCalibration ](<./Palette-kinectCalibration.md> "Palette:kinectCalibration")• [Palette:kinectPointcloud ](<./Palette-kinectPointcloud.md> "Palette:kinectPointcloud")• [Palette:leapPaint ](<./Palette-leapPaint.md> "Palette:leapPaint")• [Palette:lightTunnel ](<./Palette-lightTunnel.md> "Palette:lightTunnel")• [Palette:logger ](<./Palette-logger.md> "Palette:logger")• [Palette:mandelbrot ](<./Palette-mandelbrot.md> "Palette:mandelbrot")• [Palette:materialDesignIcons ](<./Palette-materialDesignIcons.md> "Palette:materialDesignIcons")• [Palette:mesh ](<./Palette-mesh.md> "Palette:mesh")• [Palette:monochrome ](<./Palette-monochrome.md> "Palette:monochrome")• [Palette:motionSense ](<./Palette-motionSense.md> "Palette:motionSense")• [Palette:movieEngine ](<./Palette-movieEngine.md> "Palette:movieEngine")• [Palette:moviePlayer ](<./Palette-moviePlayer.md> "Palette:moviePlayer")• [Palette:moviePlaylist ](<./Palette-moviePlaylist.md> "Palette:moviePlaylist")• [Palette:multiLevel ](<./Palette-multiLevel.md> "Palette:multiLevel")• [Palette:multiMix ](<./Palette-multiMix.md> "Palette:multiMix")• [Palette:noise ](<./Palette-noise.md> "Palette:noise")• [Palette:onScreenKeyboard ](<./Palette-onScreenKeyboard.md> "Palette:onScreenKeyboard")• [Palette:operatorPath ](<./Palette-operatorPath.md> "Palette:operatorPath")• [Palette:opticalFlow ](<./Palette-opticalFlow.md> "Palette:opticalFlow")• [Palette:particlesGpu ](<./Palette-particlesGpu.md> "Palette:particlesGpu")• [Palette:pixelate ](<./Palette-pixelate.md> "Palette:pixelate")• [Palette:pixelRelocator ](<./Palette-pixelRelocator.md> "Palette:pixelRelocator")• [Palette:pointGenerator ](<./Palette-pointGenerator.md> "Palette:pointGenerator")• [Palette:pointillize ](<./Palette-pointillize.md> "Palette:pointillize")• [Palette:pointMerge ](<./Palette-pointMerge.md> "Palette:pointMerge")• [Palette:pointRender ](<./Palette-pointRender.md> "Palette:pointRender")• [Palette:pointRepack ](<./Palette-pointRepack.md> "Palette:pointRepack")• [Palette:pointTransform ](<./Palette-pointTransform.md> "Palette:pointTransform")• [Palette:pointWeight ](<./Palette-pointWeight.md> "Palette:pointWeight")• [Palette:popDialog ](<./Palette-popDialog.md> "Palette:popDialog")• [Palette:probe ](<./Palette-probe.md> "Palette:probe")• [Palette:projectorBlend ](<./Palette-projectorBlend.md> "Palette:projectorBlend")• [Palette:pushPins ](<./Palette-pushPins.md> "Palette:pushPins")• [Palette:puzzle ](<./Palette-puzzle.md> "Palette:puzzle")• [Palette:quadReproject ](<./Palette-quadReproject.md> "Palette:quadReproject")• [Palette:radialBlur ](<./Palette-radialBlur.md> "Palette:radialBlur")• [Palette:recorder ](<./Palette-recorder.md> "Palette:recorder")• [Palette:remotePanel ](<./Palette-remotePanel.md> "Palette:remotePanel")• [Palette:rgbaBlur ](<./Palette-rgbaBlur.md> "Palette:rgbaBlur")• [Palette:rgbaDelay ](<./Palette-rgbaDelay.md> "Palette:rgbaDelay")• [Palette:rgbContrast ](<./Palette-rgbContrast.md> "Palette:rgbContrast")• [Palette:sceneChanger ](<./Palette-sceneChanger.md> "Palette:sceneChanger")• [Palette:search ](<./Palette-search.md> "Palette:search")• [Palette:searchReplace ](<./Palette-searchReplace.md> "Palette:searchReplace")• [Palette:sharpen ](<./Palette-sharpen.md> "Palette:sharpen")• [Palette:sickEngine ](<./Palette-sickEngine.md> "Palette:sickEngine")• [Palette:signalingClient ](<./Palette-signalingClient.md> "Palette:signalingClient")• [Palette:signalingServer ](<./Palette-signalingServer.md> "Palette:signalingServer")• [Palette:softenAlpha ](<./Palette-softenAlpha.md> "Palette:softenAlpha")• [Palette:solarize ](<./Palette-solarize.md> "Palette:solarize")• [Palette:sopRender ](<./Palette-sopRender.md> "Palette:sopRender")• [Palette:splitter ](<./Palette-splitter.md> "Palette:splitter")• [Palette:stitcher ](<./Palette-stitcher.md> "Palette:stitcher")• [Palette:stoner ](<./Palette-stoner.md> "Palette:stoner")• [Palette:superFormula ](<./Palette-superFormula.md> "Palette:superFormula")• [Palette:SVG ](<./Palette-SVG.md> "Palette:SVG")• [Palette:sweetSpot ](<./Palette-sweetSpot.md> "Palette:sweetSpot")• [Palette:sweetSpotPreviz ](<./Palette-sweetSpotPreviz.md> "Palette:sweetSpotPreviz")• Palette:synchroCache • [Palette:synchroClient ](<./Palette-synchroClient.md> "Palette:synchroClient")• [Palette:synchroFrameIn ](<./Palette-synchroFrameIn.md> "Palette:synchroFrameIn")• [Palette:synchroFrameOut ](<./Palette-synchroFrameOut.md> "Palette:synchroFrameOut")• [Palette:synchroNDIIn ](<./Palette-synchroNDIIn.md> "Palette:synchroNDIIn")• [Palette:synchroSDIIn ](<./Palette-synchroSDIIn.md> "Palette:synchroSDIIn")• [Palette:synchroVideoOut ](<./Palette-synchroVideoOut.md> "Palette:synchroVideoOut")• [Palette:tdBitwigPackage ](<./Palette-tdBitwigPackage.md> "Palette:tdBitwigPackage")• [Palette:tdPyEnvManager ](<./Palette-tdPyEnvManager.md> "Palette:tdPyEnvManager")• [Palette:TDVR ](<./Palette-TDVR.md> "Palette:TDVR")• [Palette:testGrid ](<./Palette-testGrid.md> "Palette:testGrid")• [Palette:threadManagerClient ](<./Palette-threadManagerClient.md> "Palette:threadManagerClient")• [Palette:threadsMonitor ](<./Palette-threadsMonitor.md> "Palette:threadsMonitor")• [Palette:transitMap ](<./Palette-transitMap.md> "Palette:transitMap")• [Palette:twirl ](<./Palette-twirl.md> "Palette:twirl")• [Palette:vectorScope ](<./Palette-vectorScope.md> "Palette:vectorScope")• [Palette:virtualFile ](<./Palette-virtualFile.md> "Palette:virtualFile")• [Palette:waveformMonitor ](<./Palette-waveformMonitor.md> "Palette:waveformMonitor")• [Palette:webBrowser ](<./Palette-webBrowser.md> "Palette:webBrowser")• [Palette:webRTC ](<./Palette-webRTC.md> "Palette:webRTC")• [Palette:webRTCPanel ](<./Palette-webRTCPanel.md> "Palette:webRTCPanel")• [Palette:webRTCPanelRcv ](<./Palette-webRTCPanelRcv.md> "Palette:webRTCPanelRcv")• [Palette:xyScope ](<./Palette-xyScope.md> "Palette:xyScope")• [Thread Manager ](<./Thread_Manager.md> "Thread Manager")
