# Palette:gestureCapture

## 

Summary

The gestureCapture COMP records movement and then displays the curves as (1) rendered lines and/or (2) a dot following the curves and/or (3) free-hand drawn shapes. The outputs of`gestureCapture`are (a) the rendered image, (b) a SOP containing all paths as polygonal lines, (c) a CHOP containing the merged lines and (d) number of lines. Internally you can access a CHOP and a SOP for every gesture recorded. 

By default you click and draw on the panel. It uses the x and y position of the cursor over the component, plus the left-click mouse button state to start/run capturing each gesture. Random colors are artificially added via the Color page to illustrate that any channels can be recorded with the positions. 

Undo deletes the last curve. Clear deletes them all. 

To record your own input channels, put any set of channels in input 1 of this component, for instance, the channels from an HTC Vive controller. If you have channels named`tx`,`ty`, and/or`tz`scaled in the XY range -1 to +1, you will see the paths in the default viewer (`tz`is overriden internally so you will have to remove it from`linemaster0`. 

In the second input, attach an on/off "select" channel to start, run and end the capturing of the gesture. It can be a keyboard key, MIDI button or controller button or some motion threshold. 

In the third input you can optionally send a “clear all lines” channel to signal to remove all lines. In the fourth input you can send a “undo” channel to signal to remove the last line drawn. Alternately you can clear and undo using the Clear and Undo pulse parameters. 

For every frame while recording a gesture, a keyframe is generated for every incoming channel. Recording as keyframes enables the recorded data to be better smoothed. Some parameters on the Gesture page set the threshold of motion, affecting whether keyframes are created or not. With a non-zero threhold, when the motion is deemed still, it will not add new keyframes. Channel groups like`tx`,`ty`,`tz`has their own threshold of motion vs stillness, and you can set thresholds for other sets of channels. 

Each gesture is stored as a component at`gestureCapture/lines/line1`,`line2`... It outputs 3 CHOPs and a SOP: 

  *`out3`\- SOP \- the smoothed gesture as a polygonal line.
  *`out2`\- CHOP \- the smoothed and generated channels. It contains 18 channels including channels that compute the gesture speed, velocity, direction and distance travelled, which can be readily used by your applications.
  *`out4`\- CHOP \- the length of time of the gesture, in seconds.


To watch the data while it is being gathered and processed, press the Keys and Chans buttons in the`gestureCapture`panel to see floating data viewers. 

The number of lines is stored in`ipar.Gesture.Nlines`and output to`out3`. (The max of the CHOP output's`lineindex`channel also indicates how many lines there are.) 

The SOP has a '`width`' attribute and is rendered with the [Line MAT](<./Line_MAT.md> "Line MAT"). 

Note: This component is set up by default to use '`u`' and '`v`' from the panel, '`select`' from the panel left-click. '`tz`' is set to 0, and random colors are artificially added. remove`sero_tx`and`sero_color`or replace them if you wish. 

**Dot page** : The moving dot (controlled from the Dot page) is`gestureCapture/dotCycle1`, an example of moving objects by sampling the gesture curves. 

**PolyFill page** : You can also draw closed shapes by turning on Render Fill in the PolyFill page. Simple smoothing so no Illustrator quality here. 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[Palette:gestureCapture Ext](</index.php?title=Palette:gestureCapture_Ext&action=edit&redlink=1> "Palette:gestureCapture Ext \(page does not exist\)")

## 

Parameters - Control Page

Help`Help`\- Opens this page. 

Version`Version`\- Current version of this COMP. 

Wireframe Width`Width`\- This value is the width of the stroke. This value is in pixels. 

Blur`Blur`\- The amount of blur in pixels. 

Clear`Clear`\- Clears all lines. 

Undo`Undo`\- Clears the last line drawn. 

Threshold Xlate Speed`Transthresh`\- 

Xlate Chans`Transchans`\- 

Threshold Rotate Speed`Rotthresh`\- 

Rotate Chans`Rotchans`\- 

Threshold Other`Otherthresh`\- 

Other Chans`Otherchans`\- 

Always Moving`Alwaysmoving`\- 

Resample by Edge Length`Resamplelength`\- Forces the length of each stroke to be the value set in the “Edge Length” parameter. 

Edge Length`Edgelength`\- The length of each stroke. 

Keep Last Edge Point`Keeplast`\- Turning off this parameter will remove the ends of strokes that are less than the value in the ‘Edge Length’ parameter. 

## 

Operator Inputs
* Input 0: in1 -
  * Input 1: in2 -
  * Input 2: in3 -
  * Input 3: in4 -

## 

Operator Outputs
* Output 0 -
* Output 1 -
* Output 2 -


TouchDesigner Build: Latest\n2022.241402021.100002018.28070before 2018.28070

Palette  
---  
[Palette ](<./Palette.md> "Palette")• [Palette:arcBallCamera ](<./Palette-arcBallCamera.md> "Palette:arcBallCamera")• [Palette:arcBallGeometry ](<./Palette-arcBallGeometry.md> "Palette:arcBallGeometry")• [Palette:audioAnalysis ](<./Palette-audioAnalysis.md> "Palette:audioAnalysis")• [Palette:audioSet ](<./Palette-audioSet.md> "Palette:audioSet")• [Palette:autoMediaPlayer ](<./Palette-autoMediaPlayer.md> "Palette:autoMediaPlayer")• [Palette:battery ](<./Palette-battery.md> "Palette:battery")• [Palette:bitwigClip ](<./Palette-bitwigClip.md> "Palette:bitwigClip")• [Palette:bitwigClipSlot ](<./Palette-bitwigClipSlot.md> "Palette:bitwigClipSlot")• [Palette:bitwigDeviceRemotes ](<./Palette-bitwigDeviceRemotes.md> "Palette:bitwigDeviceRemotes")• [Palette:bitwigMain ](<./Palette-bitwigMain.md> "Palette:bitwigMain")• [Palette:bitwigNote ](<./Palette-bitwigNote.md> "Palette:bitwigNote")• [Palette:bitwigProjectRemotes ](<./Palette-bitwigProjectRemotes.md> "Palette:bitwigProjectRemotes")• [Palette:bitwigRemotesDevice ](<./Palette-bitwigRemotesDevice.md> "Palette:bitwigRemotesDevice")• [Palette:bitwigRemotesProject ](<./Palette-bitwigRemotesProject.md> "Palette:bitwigRemotesProject")• [Palette:bitwigRemotesTrack ](<./Palette-bitwigRemotesTrack.md> "Palette:bitwigRemotesTrack")• [Palette:bitwigSelect ](<./Palette-bitwigSelect.md> "Palette:bitwigSelect")• [Palette:bitwigSong ](<./Palette-bitwigSong.md> "Palette:bitwigSong")• [Palette:bitwigTrack ](<./Palette-bitwigTrack.md> "Palette:bitwigTrack")• [Palette:bitwigTrackRemotes ](<./Palette-bitwigTrackRemotes.md> "Palette:bitwigTrackRemotes")• [Palette:blendModes ](<./Palette-blendModes.md> "Palette:blendModes")• [Palette:bloom ](<./Palette-bloom.md> "Palette:bloom")• [Palette:camera ](<./Palette-camera.md> "Palette:camera")• [Palette:cameraBrowser ](<./Palette-cameraBrowser.md> "Palette:cameraBrowser")• [Palette:cameraViewport ](<./Palette-cameraViewport.md> "Palette:cameraViewport")• [Palette:camSchnappr ](<./Palette-camSchnappr.md> "Palette:camSchnappr")• [Palette:changeColor ](<./Palette-changeColor.md> "Palette:changeColor")• [Palette:changeToColor ](<./Palette-changeToColor.md> "Palette:changeToColor")• [Palette:checker ](<./Palette-checker.md> "Palette:checker")• [Palette:chromaKey ](<./Palette-chromaKey.md> "Palette:chromaKey")• [Palette:colorThreshold ](<./Palette-colorThreshold.md> "Palette:colorThreshold")• [Palette:compareComp ](<./Palette-compareComp.md> "Palette:compareComp")• [Palette:convolve ](<./Palette-convolve.md> "Palette:convolve")• [Experimental:Palette:cornerPinPOP ](</index.php?title=Experimental:Palette:cornerPinPOP&action=edit&redlink=1> "Experimental:Palette:cornerPinPOP \(page does not exist\)")• [Palette:cornerPinSOP ](<./Palette-cornerPinSOP.md> "Palette:cornerPinSOP")• [Palette:cppParsTemplateGen ](<./Palette-cppParsTemplateGen.md> "Palette:cppParsTemplateGen")• [Palette:customAttributes ](<./Palette-customAttributes.md> "Palette:customAttributes")• [Palette:debugControl ](<./Palette-debugControl.md> "Palette:debugControl")• [Palette:dent ](<./Palette-dent.md> "Palette:dent")• [Palette:depthExtract ](<./Palette-depthExtract.md> "Palette:depthExtract")• [Palette:depthProjection ](<./Palette-depthProjection.md> "Palette:depthProjection")• [Palette:dilate ](<./Palette-dilate.md> "Palette:dilate")• [Experimental:Palette:domeViewer ](</index.php?title=Experimental:Palette:domeViewer&action=edit&redlink=1> "Experimental:Palette:domeViewer \(page does not exist\)")• [Palette:encoder ](<./Palette-encoder.md> "Palette:encoder")• [Palette:equalizer ](<./Palette-equalizer.md> "Palette:equalizer")• [Palette:feedback ](<./Palette-feedback.md> "Palette:feedback")• [Palette:feedbackEdge ](<./Palette-feedbackEdge.md> "Palette:feedbackEdge")• [Palette:firmata ](<./Palette-firmata.md> "Palette:firmata")• [Palette:gal ](<./Palette-gal.md> "Palette:gal")• [Palette:geoPanel ](<./Palette-geoPanel.md> "Palette:geoPanel")• Palette:gestureCapture • [Palette:graphPlot ](<./Palette-graphPlot.md> "Palette:graphPlot")• [Palette:histogram ](<./Palette-histogram.md> "Palette:histogram")• [Palette:hsvBlur ](<./Palette-hsvBlur.md> "Palette:hsvBlur")• [Palette:imageSearch ](<./Palette-imageSearch.md> "Palette:imageSearch")• [Palette:julia ](<./Palette-julia.md> "Palette:julia")• [Palette:kantanMapper ](<./Palette-kantanMapper.md> "Palette:kantanMapper")• [Palette:kinectCalibration ](<./Palette-kinectCalibration.md> "Palette:kinectCalibration")• [Palette:kinectPointcloud ](<./Palette-kinectPointcloud.md> "Palette:kinectPointcloud")• [Palette:leapPaint ](<./Palette-leapPaint.md> "Palette:leapPaint")• [Palette:lightTunnel ](<./Palette-lightTunnel.md> "Palette:lightTunnel")• [Palette:logger ](<./Palette-logger.md> "Palette:logger")• [Experimental:Palette:logger ](</index.php?title=Experimental:Palette:logger&action=edit&redlink=1> "Experimental:Palette:logger \(page does not exist\)")• [Palette:mandelbrot ](<./Palette-mandelbrot.md> "Palette:mandelbrot")• [Palette:materialDesignIcons ](<./Palette-materialDesignIcons.md> "Palette:materialDesignIcons")• [Palette:mesh ](<./Palette-mesh.md> "Palette:mesh")• [Palette:monochrome ](<./Palette-monochrome.md> "Palette:monochrome")• [Palette:motionSense ](<./Palette-motionSense.md> "Palette:motionSense")• [Palette:movieEngine ](<./Palette-movieEngine.md> "Palette:movieEngine")• [Palette:moviePlayer ](<./Palette-moviePlayer.md> "Palette:moviePlayer")• [Palette:moviePlaylist ](<./Palette-moviePlaylist.md> "Palette:moviePlaylist")• [Palette:multiLevel ](<./Palette-multiLevel.md> "Palette:multiLevel")• [Palette:multiMix ](<./Palette-multiMix.md> "Palette:multiMix")• [Palette:noise ](<./Palette-noise.md> "Palette:noise")• [Palette:onScreenKeyboard ](<./Palette-onScreenKeyboard.md> "Palette:onScreenKeyboard")• [Palette:operatorPath ](<./Palette-operatorPath.md> "Palette:operatorPath")• [Palette:opticalFlow ](<./Palette-opticalFlow.md> "Palette:opticalFlow")• [Palette:particlesGpu ](<./Palette-particlesGpu.md> "Palette:particlesGpu")• [Palette:pixelate ](<./Palette-pixelate.md> "Palette:pixelate")• [Palette:pixelRelocator ](<./Palette-pixelRelocator.md> "Palette:pixelRelocator")• [Palette:pointGenerator ](<./Palette-pointGenerator.md> "Palette:pointGenerator")• [Palette:pointillize ](<./Palette-pointillize.md> "Palette:pointillize")• [Palette:pointMerge ](<./Palette-pointMerge.md> "Palette:pointMerge")• [Palette:pointRender ](<./Palette-pointRender.md> "Palette:pointRender")• [Palette:pointRepack ](<./Palette-pointRepack.md> "Palette:pointRepack")• [Palette:pointTransform ](<./Palette-pointTransform.md> "Palette:pointTransform")• [Palette:pointWeight ](<./Palette-pointWeight.md> "Palette:pointWeight")• [Palette:popDialog ](<./Palette-popDialog.md> "Palette:popDialog")• [Experimental:Palette:popDialog ](</index.php?title=Experimental:Palette:popDialog&action=edit&redlink=1> "Experimental:Palette:popDialog \(page does not exist\)")• [Palette:probe ](<./Palette-probe.md> "Palette:probe")• [Palette:projectorBlend ](<./Palette-projectorBlend.md> "Palette:projectorBlend")• [Palette:pushPins ](<./Palette-pushPins.md> "Palette:pushPins")• [Palette:puzzle ](<./Palette-puzzle.md> "Palette:puzzle")• [Palette:quadReproject ](<./Palette-quadReproject.md> "Palette:quadReproject")• [Palette:radialBlur ](<./Palette-radialBlur.md> "Palette:radialBlur")• [Palette:recorder ](<./Palette-recorder.md> "Palette:recorder")• [Experimental:Palette:recorder ](</index.php?title=Experimental:Palette:recorder&action=edit&redlink=1> "Experimental:Palette:recorder \(page does not exist\)")• [Palette:remotePanel ](<./Palette-remotePanel.md> "Palette:remotePanel")• [Palette:rgbaBlur ](<./Palette-rgbaBlur.md> "Palette:rgbaBlur")• [Palette:rgbaDelay ](<./Palette-rgbaDelay.md> "Palette:rgbaDelay")• [Palette:rgbContrast ](<./Palette-rgbContrast.md> "Palette:rgbContrast")• [Palette:sceneChanger ](<./Palette-sceneChanger.md> "Palette:sceneChanger")• [Palette:search ](<./Palette-search.md> "Palette:search")• [Palette:searchReplace ](<./Palette-searchReplace.md> "Palette:searchReplace")• [Palette:sharpen ](<./Palette-sharpen.md> "Palette:sharpen")• [Palette:sickEngine ](<./Palette-sickEngine.md> "Palette:sickEngine")• [Palette:signalingClient ](<./Palette-signalingClient.md> "Palette:signalingClient")• [Palette:signalingServer ](<./Palette-signalingServer.md> "Palette:signalingServer")• [Palette:softenAlpha ](<./Palette-softenAlpha.md> "Palette:softenAlpha")• [Palette:solarize ](<./Palette-solarize.md> "Palette:solarize")• [Palette:sopRender ](<./Palette-sopRender.md> "Palette:sopRender")• [Palette:splitter ](<./Palette-splitter.md> "Palette:splitter")• [Palette:stitcher ](<./Palette-stitcher.md> "Palette:stitcher")• [Palette:stoner ](<./Palette-stoner.md> "Palette:stoner")• [Palette:superFormula ](<./Palette-superFormula.md> "Palette:superFormula")• [Palette:SVG ](<./Palette-SVG.md> "Palette:SVG")• [Palette:sweetSpot ](<./Palette-sweetSpot.md> "Palette:sweetSpot")• [Palette:sweetSpotPreviz ](<./Palette-sweetSpotPreviz.md> "Palette:sweetSpotPreviz")• [Palette:synchroCache ](<./Palette-synchroCache.md> "Palette:synchroCache")• [Palette:synchroClient ](<./Palette-synchroClient.md> "Palette:synchroClient")• [Palette:synchroFrameIn ](<./Palette-synchroFrameIn.md> "Palette:synchroFrameIn")• [Palette:synchroFrameOut ](<./Palette-synchroFrameOut.md> "Palette:synchroFrameOut")• [Palette:synchroNDIIn ](<./Palette-synchroNDIIn.md> "Palette:synchroNDIIn")• [Palette:synchroSDIIn ](<./Palette-synchroSDIIn.md> "Palette:synchroSDIIn")• [Palette:synchroVideoOut ](<./Palette-synchroVideoOut.md> "Palette:synchroVideoOut")• [Palette:tdBitwigPackage ](<./Palette-tdBitwigPackage.md> "Palette:tdBitwigPackage")• [Experimental:Palette:tdPyEnvManager ](</index.php?title=Experimental:Palette:tdPyEnvManager&action=edit&redlink=1> "Experimental:Palette:tdPyEnvManager \(page does not exist\)")• [Palette:TDVR ](<./Palette-TDVR.md> "Palette:TDVR")• [Palette:testGrid ](<./Palette-testGrid.md> "Palette:testGrid")• [Experimental:Palette:threadManagerClient ](</index.php?title=Experimental:Palette:threadManagerClient&action=edit&redlink=1> "Experimental:Palette:threadManagerClient \(page does not exist\)")• [Experimental:Palette:threadsMonitor ](</index.php?title=Experimental:Palette:threadsMonitor&action=edit&redlink=1> "Experimental:Palette:threadsMonitor \(page does not exist\)")• [Palette:transitMap ](<./Palette-transitMap.md> "Palette:transitMap")• [Palette:twirl ](<./Palette-twirl.md> "Palette:twirl")• [Palette:vectorScope ](<./Palette-vectorScope.md> "Palette:vectorScope")• [Palette:virtualFile ](<./Palette-virtualFile.md> "Palette:virtualFile")• [Palette:waveformMonitor ](<./Palette-waveformMonitor.md> "Palette:waveformMonitor")• [Palette:webBrowser ](<./Palette-webBrowser.md> "Palette:webBrowser")• [Palette:webRTC ](<./Palette-webRTC.md> "Palette:webRTC")• [Palette:webRTCPanel ](<./Palette-webRTCPanel.md> "Palette:webRTCPanel")• [Palette:webRTCPanelRcv ](<./Palette-webRTCPanelRcv.md> "Palette:webRTCPanelRcv")• [Palette:xyScope ](<./Palette-xyScope.md> "Palette:xyScope")• [Experimental:Thread Manager ](</index.php?title=Experimental:Thread_Manager&action=edit&redlink=1> "Experimental:Thread Manager \(page does not exist\)")
