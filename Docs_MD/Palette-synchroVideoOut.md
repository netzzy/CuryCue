# Palette:synchroVideoOut

##   
  
Summary

Sends out a video stream encoded with a frame index using either SDI or NDI. 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[Palette:synchroVideoOut Ext](</index.php?title=Palette:synchroVideoOut_Ext&action=edit&redlink=1> "Palette:synchroVideoOut Ext \(page does not exist\)")

## 

Parameters - Synchro Video Out Page

Frame To Stream`Frame`\- The server frame index 

Resolution`Resolution`\- ⊞ \- The resolution of the output stream 
* Resolution`Resolutionw`-
* Resolution`Resolutionh`-


Fit To Viewer`Fittoviewer`\- Fit the content frame into the viewer such that all pixels are framed. 

Reset Stats`Resetstats`\- Reset the video out stats. 

NDI Out`Ndiout`\- 

Active`Activendi`\- Activate NDI video output stream. 

Source Name`Name`\- The name of the NDI stream. 

FPS`Fps`\- The frame rate of the output video stream. 

Include Alpha`Includealpha`\- Include the alpha channel for the NDI stream. 

Audio CHOP`Audiochopndi`\- Reference to an audio stream from a CHOP. 

SDI Out`Sdiout`\- 

Active`Activesdi`\- Activate and SDI stream for this output. 

Library`Library`\- ⊞ \- Which driver to use for this output stream. 
* Blackmagic`blackmagic`-
* BlueFish444`bluefish444`-
* AJA`aja`-
* Deltacast`deltacast`-


Device`Device`\- ⊞ \- Which device to use for this driver. 
* Corvid88 - 0 - SDI Channel 1`V1`-
* Corvid88 - 0 - SDI Channel 2`V1`-
* Corvid88 - 0 - SDI Channel 3`V1`-
* Corvid88 - 0 - SDI Channel 4`V1`-
* Corvid88 - 0 - SDI Channel 5`V1`-
* Corvid88 - 0 - SDI Channel 6`V1`-
* Corvid88 - 0 - SDI Channel 7`V1`-
* Corvid88 - 0 - SDI Channel 8`V1`-


Signal Format`Signalformat`\- ⊞ \- The signal format for this SDI stream. 
* 1280x720p 23.98Hz`f1280x720p-23.98hz`-
* 1280x720p 25.00Hz`f1280x720p-25.00hz`-
* 1280x720p 59.94Hz`f1280x720p-59.94hz`-
* 1280x720p 50.00Hz`f1280x720p-50.00hz`-
* 1280x720p 60.00Hz`f1280x720p-60.00hz`-
* 1920x1080i 50.00Hz`f1920x1080i-50.00hz`-
* 1920x1080i 59.94Hz`f1920x1080i-59.94hz`-
* 1920x1080i 60.00Hz`f1920x1080i-60.00hz`-
* 1920x1080p 23.98Hz`f1920x1080p-23.98hz`-
* 1920x1080p 24.00Hz`f1920x1080p-24.00hz`-
* 1920x1080p 25.00Hz`f1920x1080p-25.00hz`-
* 1920x1080p 29.97Hz`f1920x1080p-29.97hz`-
* 1920x1080p 30.00Hz`f1920x1080p-30.00hz`-
* 1920x1080p 50.00Hz`f1920x1080p-50.00hz`-
* 1920x1080p 59.94Hz`f1920x1080p-59.94hz`-
* 1920x1080p 60.00Hz`f1920x1080p-60.00hz`-
* 1080PsF 24.00Hz (3G-A)`f1920x1080psf-24.00hz`-
* 1080PsF 25.00Hz (3G-A)`f1920x1080psf-25.00hz`-
* 1080PsF 29.97Hz (3G-A)`f1920x1080psf-29.97hz`-
* 1080PsF 30.00Hz (3G-A)`f1920x1080psf-30.00hz`-
* 2048x1080p 23.98Hz`f2048x1080p-23.98hz`-
* 2048x1080p 24.00Hz`f2048x1080p-24.00hz`-
* 2048x1080p 25.00Hz`f2048x1080p-25.00hz`-
* 2048x1080p 29.97Hz`f2048x1080p-29.97hz`-
* 2048x1080p 30.00Hz`f2048x1080p-30.00hz`-
* 2048x1080p 48.00Hz`f2048x1080p-48.00hz`-
* 2048x1080p 50.00Hz`f2048x1080p-50.00hz`-
* 2048x1080p 59.94Hz`f2048x1080p-59.94hz`-
* 2048x1080p 60.00Hz`f2048x1080p-60.00hz`-
* 3840x2160p (Quad Link) 23.98Hz`f3840x2160p-ql-23.98hz`-
* 3840x2160p (Quad Link) 24.00Hz`f3840x2160p-ql-24.00hz`-
* 3840x2160p (Quad Link) 25.00Hz`f3840x2160p-ql-25.00hz`-
* 3840x2160p (Quad Link) 29.97Hz`f3840x2160p-ql-29.97hz`-
* 3840x2160p (Quad Link) 30.00Hz`f3840x2160p-ql-30.00hz`-
* 3840x2160p (Quad Link) 50.00Hz`f3840x2160p-ql-50.00hz`-
* 3840x2160p (Quad Link) 59.94Hz`f3840x2160p-ql-59.94hz`-
* 3840x2160p (Quad Link) 60.00Hz`f3840x2160p-ql-60.00hz`-
* 4096x2160p (Quad Link) 23.98Hz`f4096x2160p-ql-23.98hz`-
* 4096x2160p (Quad Link) 24.00Hz`f4096x2160p-ql-24.00hz`-
* 4096x2160p (Quad Link) 25.00Hz`f4096x2160p-ql-25.00hz`-
* 4096x2160p (Quad Link) 29.97Hz`f4096x2160p-ql-29.97hz`-
* 4096x2160p (Quad Link) 30.00Hz`f4096x2160p-ql-30.00hz`-
* 4096x2160p (Quad Link) 47.95Hz`f4096x2160p-ql-47.95hz`-
* 4096x2160p (Quad Link) 48.00Hz`f4096x2160p-ql-48.00hz`-
* 4096x2160p (Quad Link) 50.00Hz`f4096x2160p-ql-50.00hz`-
* 4096x2160p (Quad Link) 59.94Hz`f4096x2160p-ql-59.94hz`-
* 4096x2160p (Quad Link) 60.00Hz`f4096x2160p-ql-60.00hz`-
* 3840x2160psf-23.98Hz`f3840x2160psf-23-98hz`-
* 3840x2160psf-24.00Hz`f3840x2160psf-24-00hz`-
* 3840x2160psf-25.00Hz`f3840x2160psf-25-00hz`-
* 3840x2160p 23.98Hz`f3840x2160p-23.98hz`-
* 3840x2160p 24.00Hz`f3840x2160p-24.00hz`-
* 3840x2160p 25.00Hz`f3840x2160p-25.00hz`-
* 3840x2160p 29.97Hz`f3840x2160p-29.97hz`-
* 3840x2160p 30.00Hz`f3840x2160p-30.00hz`-
* 3840x2160psf-29.97Hz`f3840x2160psf-29-97hz`-
* 3840x2160psf-30.00Hz`f3840x2160psf-30-00hz`-
* 3840x2160p 50.00Hz`f3840x2160p-50.00hz`-
* 3840x2160p 59.94Hz`f3840x2160p-59.94hz`-
* 3840x2160p 60.00Hz`f3840x2160p-60.00hz`-
* 4096x2160psf-23.98Hz`f4096x2160psf-23-98hz`-
* 4096x2160psf-24.00Hz`f4096x2160psf-24-00hz`-
* 4096x2160psf-25.00Hz`f4096x2160psf-25-00hz`-
* 4096x2160p 23.98Hz`f4096x2160p-23.98hz`-
* 4096x2160p 24.00Hz`f4096x2160p-24.00hz`-
* 4096x2160p 25.00Hz`f4096x2160p-25.00hz`-
* 4096x2160p 29.97Hz`f4096x2160p-29.97hz`-
* 4096x2160p 30.00Hz`f4096x2160p-30.00hz`-
* 4096x2160psf-29.97Hz`f4096x2160psf-29-97hz`-
* 4096x2160psf-30.00Hz`f4096x2160psf-30-00hz`-
* 4096x2160p-47.95Hz`f4096x2160p-47.95hz`-
* 4096x2160p-48.00Hz`f4096x2160p-48.00hz`-
* 4096x2160p 50.00Hz`f4096x2160p-50.00hz`-
* 4096x2160p 59.94Hz`f4096x2160p-59.94hz`-
* 4096x2160p 60.00Hz`f4096x2160p-60.00hz`-
* 4096x2160p-119.88Hz`f4096x2160p-119.88hz`-
* 4096x2160p-120.00Hz`f4096x2160p-120.00hz`-
* 7680x4320p (Quad Link) 23.98Hz`f7680x4320p-ql-23.98hz`-
* 7680x4320p (Quad Link) 24.00Hz`f7680x4320p-ql-24.00hz`-
* 7680x4320p (Quad Link) 25.00Hz`f7680x4320p-ql-25.00hz`-
* 7680x4320p (Quad Link) 29.97Hz`f7680x4320p-ql-29.97hz`-
* 7680x4320p (Quad Link) 30.00Hz`f7680x4320p-ql-30.00hz`-
* 7680x4320p (Quad Link) 50.00Hz`f7680x4320p-ql-50.00hz`-
* 7680x4320p (Quad Link) 59.94Hz`f7680x4320p-ql-59.94hz`-
* 7680x4320p (Quad Link) 60.00Hz`f7680x4320p-ql-60.00hz`-
* 8192x4320p (Quad Link) 23.98Hz`f8192x4320p-ql-23.98hz`-
* 8192x4320p (Quad Link) 24.00Hz`f8192x4320p-ql-24.00hz`-
* 8192x4320p (Quad Link) 25.00Hz`f8192x4320p-ql-25.00hz`-
* 8192x4320p (Quad Link) 29.97Hz`f8192x4320p-ql-29.97hz`-
* 8192x4320p (Quad Link) 30.00Hz`f8192x4320p-ql-30.00hz`-
* 8192x4320p (Quad Link) 47.95hz`f8192x4320p-ql-47.95hz`-
* 8192x4320p (Quad Link) 48.00hz`f8192x4320p-ql-48.00hz`-
* 8192x4320p (Quad Link) 50.00Hz`f8192x4320p-ql-50.00hz`-
* 8192x4320p (Quad Link) 59.94Hz`f8192x4320p-ql-59.94hz`-
* 8192x4320p (Quad Link) 60.00Hz`f8192x4320p-ql-60.00hz`-


Output Pixel Format`Outputpixelformat`\- ⊞ \- The pixel format for this stream. 
* 8-bit`fixed8`-
* 8-bit + 8-bit Key (Alpha)`fixed8key8`-
* 10-bit`fixed10`-
* 12-bit`fixed12`-


Reference Source`Referencesource`\- ⊞ \- The sync reference signal input index. 
* Default`default`-
* External Ref In`external`-
* SDI Input 1`sdi1`-
* SDI Input 2`sdi2`-
* SDI Input 3`sdi3`-
* SDI Input 4`sdi4`-
* SDI Input 5`sdi5`-
* SDI Input 6`sdi6`-
* SDI Input 7`sdi7`-
* SDI Input 8`sdi8`-


Audio CHOP`Audiochopsdi`\- The CHOP reference for the audio stream. 

Buffer Length`Bufferlength`\- The buffer length of the audiostream for this SDI stream. 

Transfer Mode`Transfermode`\- ⊞ \- The memory copy mode for this SDI stream. 
* Automatic`automatic`-
* Default`default`-
* Pinned`pinned`-

## 

Parameters - Overlays Page

Overlays`Overlays`\- Turns on / off the overlays for the video stream. 

Stats`Stats`\- Turns on / off the stats for the overlay. 

Stats Text Color`Statstextcolor`\- ⊞ \- The color of the text overlay for stats. 
* Stats Text Color`Statstextcolorr`-
* Stats Text Color`Statstextcolorg`-
* Stats Text Color`Statstextcolorb`-


White Line Test`Whitelinetest`\- Activates the white line test which is useful for visually detecting frame drops. 

Width`Width`\- The width of the white line in pixels. The width should be evenly divisible into the horizontal resolution of the incoming video raster. 

Pixels Per Frame`Pixelsperframe`\- The number of pixels to step each frame. The step size should be large enough for the white line to travel across the screen in under 2 seconds. 

Flash Frame Active`Flashframeactive`\- Activates of frame flash - which is useful for ensureing all ouputs are synchronized. 

Flash Color`Flashcolor`\- ⊞ \- The color of the sync flash. 
* Flash Color`Flashcolorr`-
* Flash Color`Flashcolorg`-
* Flash Color`Flashcolorb`-


Cook Dot`Cookdot`\- Activates a visual dot overlay that will flash every time the server application drops a frame. This is useful to understand if the server application is suffering from performance issues. 

Cook Dot Color`Cookdotcolor`\- ⊞ \- The color of the cook dot flash. 
* Cook Dot Color`Cookdotcolorr`-
* Cook Dot Color`Cookdotcolorg`-
* Cook Dot Color`Cookdotcolorb`-


Cook Dot Scale`Cookdotscale`\- The scale of the cook dot. 

Dashboard`Dashboard`\- Displays the information dashboard for this output viewer. 

## 

Parameters - About Page

Help`Help`\- The help for this component. 

Version`Version`\- The version for this component. 

## 

Operator Inputs
* Input 0: in1 -
  * Input 1: in2 -

## 

Operator Outputs
* Output 0 -


TouchDesigner Build: Latest\n2022.24140before 2022.24140

Palette  
---  
[Palette ](<./Palette.md> "Palette")• [Palette:arcBallCamera ](<./Palette-arcBallCamera.md> "Palette:arcBallCamera")• [Palette:arcBallGeometry ](<./Palette-arcBallGeometry.md> "Palette:arcBallGeometry")• [Palette:audioAnalysis ](<./Palette-audioAnalysis.md> "Palette:audioAnalysis")• [Palette:audioSet ](<./Palette-audioSet.md> "Palette:audioSet")• [Palette:autoMediaPlayer ](<./Palette-autoMediaPlayer.md> "Palette:autoMediaPlayer")• [Palette:battery ](<./Palette-battery.md> "Palette:battery")• [Palette:bitwigClip ](<./Palette-bitwigClip.md> "Palette:bitwigClip")• [Palette:bitwigClipSlot ](<./Palette-bitwigClipSlot.md> "Palette:bitwigClipSlot")• [Palette:bitwigDeviceRemotes ](<./Palette-bitwigDeviceRemotes.md> "Palette:bitwigDeviceRemotes")• [Palette:bitwigMain ](<./Palette-bitwigMain.md> "Palette:bitwigMain")• [Palette:bitwigNote ](<./Palette-bitwigNote.md> "Palette:bitwigNote")• [Palette:bitwigProjectRemotes ](<./Palette-bitwigProjectRemotes.md> "Palette:bitwigProjectRemotes")• [Palette:bitwigRemotesDevice ](<./Palette-bitwigRemotesDevice.md> "Palette:bitwigRemotesDevice")• [Palette:bitwigRemotesProject ](<./Palette-bitwigRemotesProject.md> "Palette:bitwigRemotesProject")• [Palette:bitwigRemotesTrack ](<./Palette-bitwigRemotesTrack.md> "Palette:bitwigRemotesTrack")• [Palette:bitwigSelect ](<./Palette-bitwigSelect.md> "Palette:bitwigSelect")• [Palette:bitwigSong ](<./Palette-bitwigSong.md> "Palette:bitwigSong")• [Palette:bitwigTrack ](<./Palette-bitwigTrack.md> "Palette:bitwigTrack")• [Palette:bitwigTrackRemotes ](<./Palette-bitwigTrackRemotes.md> "Palette:bitwigTrackRemotes")• [Palette:blendModes ](<./Palette-blendModes.md> "Palette:blendModes")• [Palette:bloom ](<./Palette-bloom.md> "Palette:bloom")• [Palette:camera ](<./Palette-camera.md> "Palette:camera")• [Palette:cameraBrowser ](<./Palette-cameraBrowser.md> "Palette:cameraBrowser")• [Palette:cameraViewport ](<./Palette-cameraViewport.md> "Palette:cameraViewport")• [Palette:camSchnappr ](<./Palette-camSchnappr.md> "Palette:camSchnappr")• [Palette:changeColor ](<./Palette-changeColor.md> "Palette:changeColor")• [Palette:changeToColor ](<./Palette-changeToColor.md> "Palette:changeToColor")• [Palette:checker ](<./Palette-checker.md> "Palette:checker")• [Palette:chromaKey ](<./Palette-chromaKey.md> "Palette:chromaKey")• [Palette:colorThreshold ](<./Palette-colorThreshold.md> "Palette:colorThreshold")• [Palette:compareComp ](<./Palette-compareComp.md> "Palette:compareComp")• [Palette:convolve ](<./Palette-convolve.md> "Palette:convolve")• [Palette:cornerPinPOP ](<./Palette-cornerPinPOP.md> "Palette:cornerPinPOP")• [Palette:cornerPinSOP ](<./Palette-cornerPinSOP.md> "Palette:cornerPinSOP")• [Palette:cppParsTemplateGen ](<./Palette-cppParsTemplateGen.md> "Palette:cppParsTemplateGen")• [Palette:customAttributes ](<./Palette-customAttributes.md> "Palette:customAttributes")• [Palette:debugControl ](<./Palette-debugControl.md> "Palette:debugControl")• [Palette:dent ](<./Palette-dent.md> "Palette:dent")• [Palette:depthExtract ](<./Palette-depthExtract.md> "Palette:depthExtract")• [Palette:depthProjection ](<./Palette-depthProjection.md> "Palette:depthProjection")• [Palette:dilate ](<./Palette-dilate.md> "Palette:dilate")• [Palette:domeViewer ](<./Palette-domeViewer.md> "Palette:domeViewer")• [Palette:encoder ](<./Palette-encoder.md> "Palette:encoder")• [Palette:equalizer ](<./Palette-equalizer.md> "Palette:equalizer")• [Palette:feedback ](<./Palette-feedback.md> "Palette:feedback")• [Palette:feedbackEdge ](<./Palette-feedbackEdge.md> "Palette:feedbackEdge")• [Palette:firmata ](<./Palette-firmata.md> "Palette:firmata")• [Palette:gal ](<./Palette-gal.md> "Palette:gal")• [Palette:geoPanel ](<./Palette-geoPanel.md> "Palette:geoPanel")• [Palette:gestureCapture ](<./Palette-gestureCapture.md> "Palette:gestureCapture")• [Palette:graphPlot ](<./Palette-graphPlot.md> "Palette:graphPlot")• [Palette:histogram ](<./Palette-histogram.md> "Palette:histogram")• [Palette:hsvBlur ](<./Palette-hsvBlur.md> "Palette:hsvBlur")• [Palette:imageSearch ](<./Palette-imageSearch.md> "Palette:imageSearch")• [Palette:julia ](<./Palette-julia.md> "Palette:julia")• [Palette:kantanMapper ](<./Palette-kantanMapper.md> "Palette:kantanMapper")• [Palette:kinectCalibration ](<./Palette-kinectCalibration.md> "Palette:kinectCalibration")• [Palette:kinectPointcloud ](<./Palette-kinectPointcloud.md> "Palette:kinectPointcloud")• [Palette:leapPaint ](<./Palette-leapPaint.md> "Palette:leapPaint")• [Palette:lightTunnel ](<./Palette-lightTunnel.md> "Palette:lightTunnel")• [Palette:logger ](<./Palette-logger.md> "Palette:logger")• [Palette:mandelbrot ](<./Palette-mandelbrot.md> "Palette:mandelbrot")• [Palette:materialDesignIcons ](<./Palette-materialDesignIcons.md> "Palette:materialDesignIcons")• [Palette:mesh ](<./Palette-mesh.md> "Palette:mesh")• [Palette:monochrome ](<./Palette-monochrome.md> "Palette:monochrome")• [Palette:motionSense ](<./Palette-motionSense.md> "Palette:motionSense")• [Palette:movieEngine ](<./Palette-movieEngine.md> "Palette:movieEngine")• [Palette:moviePlayer ](<./Palette-moviePlayer.md> "Palette:moviePlayer")• [Palette:moviePlaylist ](<./Palette-moviePlaylist.md> "Palette:moviePlaylist")• [Palette:multiLevel ](<./Palette-multiLevel.md> "Palette:multiLevel")• [Palette:multiMix ](<./Palette-multiMix.md> "Palette:multiMix")• [Palette:noise ](<./Palette-noise.md> "Palette:noise")• [Palette:onScreenKeyboard ](<./Palette-onScreenKeyboard.md> "Palette:onScreenKeyboard")• [Palette:operatorPath ](<./Palette-operatorPath.md> "Palette:operatorPath")• [Palette:opticalFlow ](<./Palette-opticalFlow.md> "Palette:opticalFlow")• [Palette:particlesGpu ](<./Palette-particlesGpu.md> "Palette:particlesGpu")• [Palette:pixelate ](<./Palette-pixelate.md> "Palette:pixelate")• [Palette:pixelRelocator ](<./Palette-pixelRelocator.md> "Palette:pixelRelocator")• [Palette:pointGenerator ](<./Palette-pointGenerator.md> "Palette:pointGenerator")• [Palette:pointillize ](<./Palette-pointillize.md> "Palette:pointillize")• [Palette:pointMerge ](<./Palette-pointMerge.md> "Palette:pointMerge")• [Palette:pointRender ](<./Palette-pointRender.md> "Palette:pointRender")• [Palette:pointRepack ](<./Palette-pointRepack.md> "Palette:pointRepack")• [Palette:pointTransform ](<./Palette-pointTransform.md> "Palette:pointTransform")• [Palette:pointWeight ](<./Palette-pointWeight.md> "Palette:pointWeight")• [Palette:popDialog ](<./Palette-popDialog.md> "Palette:popDialog")• [Palette:probe ](<./Palette-probe.md> "Palette:probe")• [Palette:projectorBlend ](<./Palette-projectorBlend.md> "Palette:projectorBlend")• [Palette:pushPins ](<./Palette-pushPins.md> "Palette:pushPins")• [Palette:puzzle ](<./Palette-puzzle.md> "Palette:puzzle")• [Palette:quadReproject ](<./Palette-quadReproject.md> "Palette:quadReproject")• [Palette:radialBlur ](<./Palette-radialBlur.md> "Palette:radialBlur")• [Palette:recorder ](<./Palette-recorder.md> "Palette:recorder")• [Palette:remotePanel ](<./Palette-remotePanel.md> "Palette:remotePanel")• [Palette:rgbaBlur ](<./Palette-rgbaBlur.md> "Palette:rgbaBlur")• [Palette:rgbaDelay ](<./Palette-rgbaDelay.md> "Palette:rgbaDelay")• [Palette:rgbContrast ](<./Palette-rgbContrast.md> "Palette:rgbContrast")• [Palette:sceneChanger ](<./Palette-sceneChanger.md> "Palette:sceneChanger")• [Palette:search ](<./Palette-search.md> "Palette:search")• [Palette:searchReplace ](<./Palette-searchReplace.md> "Palette:searchReplace")• [Palette:sharpen ](<./Palette-sharpen.md> "Palette:sharpen")• [Palette:sickEngine ](<./Palette-sickEngine.md> "Palette:sickEngine")• [Palette:signalingClient ](<./Palette-signalingClient.md> "Palette:signalingClient")• [Palette:signalingServer ](<./Palette-signalingServer.md> "Palette:signalingServer")• [Palette:softenAlpha ](<./Palette-softenAlpha.md> "Palette:softenAlpha")• [Palette:solarize ](<./Palette-solarize.md> "Palette:solarize")• [Palette:sopRender ](<./Palette-sopRender.md> "Palette:sopRender")• [Palette:splitter ](<./Palette-splitter.md> "Palette:splitter")• [Palette:stitcher ](<./Palette-stitcher.md> "Palette:stitcher")• [Palette:stoner ](<./Palette-stoner.md> "Palette:stoner")• [Palette:superFormula ](<./Palette-superFormula.md> "Palette:superFormula")• [Palette:SVG ](<./Palette-SVG.md> "Palette:SVG")• [Palette:sweetSpot ](<./Palette-sweetSpot.md> "Palette:sweetSpot")• [Palette:sweetSpotPreviz ](<./Palette-sweetSpotPreviz.md> "Palette:sweetSpotPreviz")• [Palette:synchroCache ](<./Palette-synchroCache.md> "Palette:synchroCache")• [Palette:synchroClient ](<./Palette-synchroClient.md> "Palette:synchroClient")• [Palette:synchroFrameIn ](<./Palette-synchroFrameIn.md> "Palette:synchroFrameIn")• [Palette:synchroFrameOut ](<./Palette-synchroFrameOut.md> "Palette:synchroFrameOut")• [Palette:synchroNDIIn ](<./Palette-synchroNDIIn.md> "Palette:synchroNDIIn")• [Palette:synchroSDIIn ](<./Palette-synchroSDIIn.md> "Palette:synchroSDIIn")• Palette:synchroVideoOut • [Palette:tdBitwigPackage ](<./Palette-tdBitwigPackage.md> "Palette:tdBitwigPackage")• [Palette:tdPyEnvManager ](<./Palette-tdPyEnvManager.md> "Palette:tdPyEnvManager")• [Palette:TDVR ](<./Palette-TDVR.md> "Palette:TDVR")• [Palette:testGrid ](<./Palette-testGrid.md> "Palette:testGrid")• [Palette:threadManagerClient ](<./Palette-threadManagerClient.md> "Palette:threadManagerClient")• [Palette:threadsMonitor ](<./Palette-threadsMonitor.md> "Palette:threadsMonitor")• [Palette:transitMap ](<./Palette-transitMap.md> "Palette:transitMap")• [Palette:twirl ](<./Palette-twirl.md> "Palette:twirl")• [Palette:vectorScope ](<./Palette-vectorScope.md> "Palette:vectorScope")• [Palette:virtualFile ](<./Palette-virtualFile.md> "Palette:virtualFile")• [Palette:waveformMonitor ](<./Palette-waveformMonitor.md> "Palette:waveformMonitor")• [Palette:webBrowser ](<./Palette-webBrowser.md> "Palette:webBrowser")• [Palette:webRTC ](<./Palette-webRTC.md> "Palette:webRTC")• [Palette:webRTCPanel ](<./Palette-webRTCPanel.md> "Palette:webRTCPanel")• [Palette:webRTCPanelRcv ](<./Palette-webRTCPanelRcv.md> "Palette:webRTCPanelRcv")• [Palette:xyScope ](<./Palette-xyScope.md> "Palette:xyScope")• [Thread Manager ](<./Thread_Manager.md> "Thread Manager")
