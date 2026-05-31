# Palette:bitwigSong

##   
  
Summary

The bitwigSong COMP acts as a bi-directional interface for Bitwig's global transport; including timing, playback, and recording functionality. It also stores information about scenes and cues, and supports control for their playback 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[Palette:bitwigSong1 Ext](</index.php?title=Palette:bitwigSong1_Ext&action=edit&redlink=1> "Palette:bitwigSong1 Ext \(page does not exist\)")

## 

Parameters - Bitwig Song Page

Project Name`Projectname`\- A read only string providing the current Bitwig project name. 

Play`Play`\- Starts playback of the Bitwig timeline. 

Stop`Stop`\- Stops playback of the Bitwig timeline. 

Restart`Restart`\- Restart playback. If timeline is currently stopped, restart will return the play position to the start position and begin playback. If timeline is currently playing, restart will stop playback. 

Play State`Playstate`\- Indicates whether or not playback is currently active. 

Record`Record`\- Indicates whether or not recording is currently active. 

Tempo`Tempo`\- Provides the project's BPM (beats/quarter-notes per minute). Can be adjusted manually. 

Tempo Tap`Tempotap`\- Set the tempo manually by pulsing this parameter on the beat at the desired tempo. 

Tempo Nudge Up`Temponudgeup`\- Increase the tempo by one BPM 

Tempo Nudge Down`Temponudgedown`\- Decrease the tempo by one BPM 

Signature Numerator`Signaturenumerator`\- The number of beats per measure/bar. 

Signature Denominator`Signaturedenominator`\- ⊞ \- The time-subdivision used to define one beat in a bar. 
* 2`2`\- one beat is a half note
* 4`4`\- one beat is a quarter-note
* 8`8`\- one beat is an eight note
* 16`16`\- one beat is a sixteenth note


Default Launch Quantization`Defaultlaunchquantization`\- ⊞ \- Defines the project's default quantization for launching clips. 
* None`None`\- No quantization, start clips immediately
* 8`8`\- Start clips at the next interval of 8 bars
* 4`4`\- Start clips at the next interval of 4 bars
* 2`2`\- Start clips at the next interval of 2 bars
* 1`1`\- Start clips at the next interval of 1 bar
* 1/2`1/2`\- Start clips at the next interval of 1/2 note
* 1/4`1/4`\- Start clips at the next interval of 1/4 note
* 1/8`1/8`\- Start clips at the next interval of 1/8 note
* 1/16`1/16`\- Start clips at the next interval of 1/16 note


Loop Enabled`Loopenabled`\- Enables or disables looping playback 

Loop Start`Loopstart`\- Defines the start position of the loop in quarter-notes. 

Loop Duration`Loopduration`\- Defines the length of the loop in quarter-notes. 

Cue`Cue`\- The name of the desired cue marker to launch 

Launch Cue`Launchcue`\- Move the current timeline position to the chosen cue marker and start playback. 

Jump To Prev Cue`Jumptoprevcue`\- Move the current timeline position to the previous cue marker. 

Jump To Next Cue`Jumptonextcue`\- Move the current timeline position to the next cue marker. 

Fraction Cue`Fractioncue`\- The cue whose position will define the cueFraction channel in the output CHOP. The cueFraction amount represents the current play position divided by the cue position. Since Bitwig's timeline does not have a definitive end position, you can create a cue marking the end of a song, and set that cue as the Fractio Cue to get the song playback progress as a fractional value. 

Scene`Scene`\- The name of the desired scene to launch 

Launch Scene`Launchscene`\- Begin playback of all clips within the chosen scene. 

Stop Scenes`Stopscenes`\- Stop playback of all clips within the chosen scene. 

Return To Arrangement`Returntoarrangement`\- Switch the playback mode from clip launcher to arranger for all tracks. 

## 

Parameters - Callbacks Page

Project Name`Projectname`\- A read only string providing the current Bitwig project name. 

Callback DAT`Callbackdat`\- A reference to the Text DAT containing the Bitwig Song COMP callback methods. 

Print Callbacks`Printcallbacks`\- When enabled, callback information will be printed to the text port as they are called. 

## 

Parameters - TDBitwig Page

TDBitwig Comp`Tdbitwigcomp`\- A reference to the Bitwig Main COMP

Connect`Connect`\- A toggle to manually enable or disable listeners associated with this COMP. 

Debug Messages`Debugmessages`\- Print information about extension method calls for the Component

Clear Chop`Clearchop`\- Clear the channels in the OSC In CHOP

Strip CHOP Prefix Segments`Stripchopprefixsegments`\- Strip off the given number of address segments in the output CHOP channel names 

## 

Parameters - About Page

Help`Help`\- Opens this documentation page 

Version`Version`\- The TDBitwig version that this Component is updated to 

.tox Save Build`Toxsavebuild`\- The TouchDesigner build version that this Component was saved in 

Update`Update`\- If the tdBitwigPackage COMP is present in the TouchDesigner project, pressing pulse will update this Component to the newest version 

## 

Operator Outputs
* Output 0 \- A CHOP containing a channel for each listener property associated with this COMP
* Output 1 \- A CHOP providing tempo and transport information resembling the format of the Beat CHOP
* Output 2 \- A DAT table of Cue Marker information including names and timeline positions in quarter-note units
* Output 3 \- A DAT table of Scene information including the scene names
* Output 4 \- A DAT table providing the name and index of the most recent cue passed in playback


TouchDesigner Build: Latest\nwikieditorwikieditor

Palette  
---  
[Palette ](<./Palette.md> "Palette")• [Palette:arcBallCamera ](<./Palette-arcBallCamera.md> "Palette:arcBallCamera")• [Palette:arcBallGeometry ](<./Palette-arcBallGeometry.md> "Palette:arcBallGeometry")• [Palette:audioAnalysis ](<./Palette-audioAnalysis.md> "Palette:audioAnalysis")• [Palette:audioSet ](<./Palette-audioSet.md> "Palette:audioSet")• [Palette:battery ](<./Palette-battery.md> "Palette:battery")• [Palette:bitwigClip ](<./Palette-bitwigClip.md> "Palette:bitwigClip")• [Palette:bitwigClipSlot ](<./Palette-bitwigClipSlot.md> "Palette:bitwigClipSlot")• [Palette:bitwigDeviceRemotes ](<./Palette-bitwigDeviceRemotes.md> "Palette:bitwigDeviceRemotes")• [Palette:bitwigMain ](<./Palette-bitwigMain.md> "Palette:bitwigMain")• [Palette:bitwigNote ](<./Palette-bitwigNote.md> "Palette:bitwigNote")• [Palette:bitwigProjectRemotes ](<./Palette-bitwigProjectRemotes.md> "Palette:bitwigProjectRemotes")• [Palette:bitwigRemotesDevice ](<./Palette-bitwigRemotesDevice.md> "Palette:bitwigRemotesDevice")• [Palette:bitwigRemotesProject ](<./Palette-bitwigRemotesProject.md> "Palette:bitwigRemotesProject")• [Palette:bitwigRemotesTrack ](<./Palette-bitwigRemotesTrack.md> "Palette:bitwigRemotesTrack")• [Palette:bitwigSelect ](<./Palette-bitwigSelect.md> "Palette:bitwigSelect")• Palette:bitwigSong • [Palette:bitwigTrack ](<./Palette-bitwigTrack.md> "Palette:bitwigTrack")• [Palette:bitwigTrackRemotes ](<./Palette-bitwigTrackRemotes.md> "Palette:bitwigTrackRemotes")• [Palette:blendModes ](<./Palette-blendModes.md> "Palette:blendModes")• [Palette:bloom ](<./Palette-bloom.md> "Palette:bloom")• [Palette:camera ](<./Palette-camera.md> "Palette:camera")• [Palette:cameraBrowser ](<./Palette-cameraBrowser.md> "Palette:cameraBrowser")• [Palette:cameraViewport ](<./Palette-cameraViewport.md> "Palette:cameraViewport")• [Palette:camSchnappr ](<./Palette-camSchnappr.md> "Palette:camSchnappr")• [Palette:changeColor ](<./Palette-changeColor.md> "Palette:changeColor")• [Palette:changeToColor ](<./Palette-changeToColor.md> "Palette:changeToColor")• [Palette:checker ](<./Palette-checker.md> "Palette:checker")• [Palette:chromaKey ](<./Palette-chromaKey.md> "Palette:chromaKey")• [Palette:colorThreshold ](<./Palette-colorThreshold.md> "Palette:colorThreshold")• [Palette:compareComp ](<./Palette-compareComp.md> "Palette:compareComp")• [Palette:convolve ](<./Palette-convolve.md> "Palette:convolve")• [Experimental:Palette:cornerPinPOP ](</Experimental:Palette:cornerPinPOP> "Experimental:Palette:cornerPinPOP")• [Palette:cornerPinSOP ](<./Palette-cornerPinSOP.md> "Palette:cornerPinSOP")• [Palette:cppParsTemplateGen ](<./Palette-cppParsTemplateGen.md> "Palette:cppParsTemplateGen")• [Palette:customAttributes ](<./Palette-customAttributes.md> "Palette:customAttributes")• [Palette:debugControl ](<./Palette-debugControl.md> "Palette:debugControl")• [Palette:dent ](<./Palette-dent.md> "Palette:dent")• [Palette:depthExtract ](<./Palette-depthExtract.md> "Palette:depthExtract")• [Palette:depthProjection ](<./Palette-depthProjection.md> "Palette:depthProjection")• [Palette:dilate ](<./Palette-dilate.md> "Palette:dilate")• [Experimental:Palette:domeViewer ](</Experimental:Palette:domeViewer> "Experimental:Palette:domeViewer")• [Palette:encoder ](<./Palette-encoder.md> "Palette:encoder")• [Palette:equalizer ](<./Palette-equalizer.md> "Palette:equalizer")• [Palette:feedback ](<./Palette-feedback.md> "Palette:feedback")• [Palette:feedbackEdge ](<./Palette-feedbackEdge.md> "Palette:feedbackEdge")• [Palette:firmata ](<./Palette-firmata.md> "Palette:firmata")• [Palette:gal ](<./Palette-gal.md> "Palette:gal")• [Palette:geoPanel ](<./Palette-geoPanel.md> "Palette:geoPanel")• [Palette:gestureCapture ](<./Palette-gestureCapture.md> "Palette:gestureCapture")• [Palette:graphPlot ](<./Palette-graphPlot.md> "Palette:graphPlot")• [Palette:histogram ](<./Palette-histogram.md> "Palette:histogram")• [Palette:hsvBlur ](<./Palette-hsvBlur.md> "Palette:hsvBlur")• [Palette:imageSearch ](<./Palette-imageSearch.md> "Palette:imageSearch")• [Palette:julia ](<./Palette-julia.md> "Palette:julia")• [Palette:kantanMapper ](<./Palette-kantanMapper.md> "Palette:kantanMapper")• [Palette:kinectCalibration ](<./Palette-kinectCalibration.md> "Palette:kinectCalibration")• [Palette:kinectPointcloud ](<./Palette-kinectPointcloud.md> "Palette:kinectPointcloud")• [Palette:leapPaint ](<./Palette-leapPaint.md> "Palette:leapPaint")• [Palette:lightTunnel ](<./Palette-lightTunnel.md> "Palette:lightTunnel")• [Palette:logger ](<./Palette-logger.md> "Palette:logger")• [Experimental:Palette:logger ](</Experimental:Palette:logger> "Experimental:Palette:logger")• [Palette:mandelbrot ](<./Palette-mandelbrot.md> "Palette:mandelbrot")• [Palette:materialDesignIcons ](<./Palette-materialDesignIcons.md> "Palette:materialDesignIcons")• [Palette:mesh ](<./Palette-mesh.md> "Palette:mesh")• [Palette:monochrome ](<./Palette-monochrome.md> "Palette:monochrome")• [Palette:motionSense ](<./Palette-motionSense.md> "Palette:motionSense")• [Palette:movieEngine ](<./Palette-movieEngine.md> "Palette:movieEngine")• [Palette:moviePlayer ](<./Palette-moviePlayer.md> "Palette:moviePlayer")• [Palette:moviePlaylist ](<./Palette-moviePlaylist.md> "Palette:moviePlaylist")• [Palette:multiLevel ](<./Palette-multiLevel.md> "Palette:multiLevel")• [Palette:multiMix ](<./Palette-multiMix.md> "Palette:multiMix")• [Palette:noise ](<./Palette-noise.md> "Palette:noise")• [Palette:onScreenKeyboard ](<./Palette-onScreenKeyboard.md> "Palette:onScreenKeyboard")• [Palette:operatorPath ](<./Palette-operatorPath.md> "Palette:operatorPath")• [Palette:opticalFlow ](<./Palette-opticalFlow.md> "Palette:opticalFlow")• [Palette:particlesGpu ](<./Palette-particlesGpu.md> "Palette:particlesGpu")• [Palette:pixelate ](<./Palette-pixelate.md> "Palette:pixelate")• [Palette:pixelRelocator ](<./Palette-pixelRelocator.md> "Palette:pixelRelocator")• [Palette:pointGenerator ](<./Palette-pointGenerator.md> "Palette:pointGenerator")• [Palette:pointillize ](<./Palette-pointillize.md> "Palette:pointillize")• [Palette:pointMerge ](<./Palette-pointMerge.md> "Palette:pointMerge")• [Palette:pointRender ](<./Palette-pointRender.md> "Palette:pointRender")• [Palette:pointRepack ](<./Palette-pointRepack.md> "Palette:pointRepack")• [Palette:pointTransform ](<./Palette-pointTransform.md> "Palette:pointTransform")• [Palette:pointWeight ](<./Palette-pointWeight.md> "Palette:pointWeight")• [Palette:popDialog ](<./Palette-popDialog.md> "Palette:popDialog")• [Experimental:Palette:popDialog ](</Experimental:Palette:popDialog> "Experimental:Palette:popDialog")• [Palette:probe ](<./Palette-probe.md> "Palette:probe")• [Palette:projectorBlend ](<./Palette-projectorBlend.md> "Palette:projectorBlend")• [Palette:pushPins ](<./Palette-pushPins.md> "Palette:pushPins")• [Palette:puzzle ](<./Palette-puzzle.md> "Palette:puzzle")• [Palette:quadReproject ](<./Palette-quadReproject.md> "Palette:quadReproject")• [Palette:radialBlur ](<./Palette-radialBlur.md> "Palette:radialBlur")• [Palette:recorder ](<./Palette-recorder.md> "Palette:recorder")• [Experimental:Palette:recorder ](</Experimental:Palette:recorder> "Experimental:Palette:recorder")• [Palette:remotePanel ](<./Palette-remotePanel.md> "Palette:remotePanel")• [Palette:rgbaBlur ](<./Palette-rgbaBlur.md> "Palette:rgbaBlur")• [Palette:rgbaDelay ](<./Palette-rgbaDelay.md> "Palette:rgbaDelay")• [Palette:rgbContrast ](<./Palette-rgbContrast.md> "Palette:rgbContrast")• [Palette:sceneChanger ](<./Palette-sceneChanger.md> "Palette:sceneChanger")• [Palette:search ](<./Palette-search.md> "Palette:search")• [Palette:searchReplace ](<./Palette-searchReplace.md> "Palette:searchReplace")• [Palette:sharpen ](<./Palette-sharpen.md> "Palette:sharpen")• [Palette:sickEngine ](<./Palette-sickEngine.md> "Palette:sickEngine")• [Palette:signalingClient ](<./Palette-signalingClient.md> "Palette:signalingClient")• [Palette:signalingServer ](<./Palette-signalingServer.md> "Palette:signalingServer")• [Palette:softenAlpha ](<./Palette-softenAlpha.md> "Palette:softenAlpha")• [Palette:solarize ](<./Palette-solarize.md> "Palette:solarize")• [Palette:sopRender ](<./Palette-sopRender.md> "Palette:sopRender")• [Palette:splitter ](<./Palette-splitter.md> "Palette:splitter")• [Palette:stitcher ](<./Palette-stitcher.md> "Palette:stitcher")• [Palette:stoner ](<./Palette-stoner.md> "Palette:stoner")• [Palette:superFormula ](<./Palette-superFormula.md> "Palette:superFormula")• [Palette:SVG ](<./Palette-SVG.md> "Palette:SVG")• [Palette:sweetSpot ](<./Palette-sweetSpot.md> "Palette:sweetSpot")• [Palette:sweetSpotPreviz ](<./Palette-sweetSpotPreviz.md> "Palette:sweetSpotPreviz")• [Palette:synchroCache ](<./Palette-synchroCache.md> "Palette:synchroCache")• [Palette:synchroClient ](<./Palette-synchroClient.md> "Palette:synchroClient")• [Palette:synchroFrameIn ](<./Palette-synchroFrameIn.md> "Palette:synchroFrameIn")• [Palette:synchroFrameOut ](<./Palette-synchroFrameOut.md> "Palette:synchroFrameOut")• [Palette:synchroNDIIn ](<./Palette-synchroNDIIn.md> "Palette:synchroNDIIn")• [Palette:synchroSDIIn ](<./Palette-synchroSDIIn.md> "Palette:synchroSDIIn")• [Palette:synchroVideoOut ](<./Palette-synchroVideoOut.md> "Palette:synchroVideoOut")• [Palette:tdBitwigPackage ](<./Palette-tdBitwigPackage.md> "Palette:tdBitwigPackage")• [Experimental:Palette:tdPyEnvManager ](</Experimental:Palette:tdPyEnvManager> "Experimental:Palette:tdPyEnvManager")• [Palette:TDVR ](<./Palette-TDVR.md> "Palette:TDVR")• [Palette:testGrid ](<./Palette-testGrid.md> "Palette:testGrid")• [Experimental:Palette:threadManagerClient ](</Experimental:Palette:threadManagerClient> "Experimental:Palette:threadManagerClient")• [Experimental:Palette:threadsMonitor ](</Experimental:Palette:threadsMonitor> "Experimental:Palette:threadsMonitor")• [Palette:transitMap ](<./Palette-transitMap.md> "Palette:transitMap")• [Palette:twirl ](<./Palette-twirl.md> "Palette:twirl")• [Palette:vectorScope ](<./Palette-vectorScope.md> "Palette:vectorScope")• [Palette:virtualFile ](<./Palette-virtualFile.md> "Palette:virtualFile")• [Palette:waveformMonitor ](<./Palette-waveformMonitor.md> "Palette:waveformMonitor")• [Palette:webBrowser ](<./Palette-webBrowser.md> "Palette:webBrowser")• [Palette:webRTC ](<./Palette-webRTC.md> "Palette:webRTC")• [Palette:webRTCPanel ](<./Palette-webRTCPanel.md> "Palette:webRTCPanel")• [Palette:webRTCPanelRcv ](<./Palette-webRTCPanelRcv.md> "Palette:webRTCPanelRcv")• [Palette:xyScope ](<./Palette-xyScope.md> "Palette:xyScope")• [Experimental:Thread Manager ](</Experimental:Thread_Manager> "Experimental:Thread Manager")
