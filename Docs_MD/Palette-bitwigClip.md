# Palette:bitwigClip

##   
  
Summary

The bitwigClip COMP serves as an interface for controlling a specific launcher clip in Bitwig's clip launcher context. Users begin by choosing which track they are interested in; then the launcher clip, and subsequently decide to perform actions or read/modify the properties of a given launcher clip. 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[Palette:bitwigClip Ext](</index.php?title=Palette:bitwigClip_Ext&action=edit&redlink=1> "Palette:bitwigClip Ext \(page does not exist\)")

## 

Parameters - Bitwig Clip Launcher Page

Track`Track`\- A read-only string providing the currently selected Track name. 

Pin Track`Pintrack`\- Indicates whether the current selection is pinned to the current track. If the selection is un-pinned, the selection will follow whatever track is currently selected in the Bitwig UI. If the selection is pinned, the selection will remain on the currently selected track independently of the Bitwig UI selection. 

Prev Track`Prevtrack`\- Will change the current selection to the previous track in the Bitwig UI. 

Next Track`Nexttrack`\- Will change the current selection to the next track in the Bitwig UI. 

Make Visible In Arranger`Makevisibleinarranger`\- If the selected track is currently out of the Bitwig Arranger view, pressing pulse will scroll the arranger window so that the selected track is brought into view. 

Make Visible In Mixer`Makevisibleinmixer`\- If the selected track is currently out of the Bitwig Mixer view, pressing pulse will scroll the mixer window so that the selected track is brought into view. 

Select In Editor`Selectineditor`\- Places the Bitwig Editor cursor on the currently selected track. 

Select In Mixer`Selectinmixer`\- Places the Bitwig Mixer cursor on the currently selected track. 

Stop All Clips`Stopallclips`\- Stops playback of clips for the selected track. 

Clip Slot`Clipslot`\- The index and name of the currently selected Clip Slot 

Launch Quantization`Launchquantization`\- ⊞ \- The quantization amount for the selected clip slot. Will determine the interval at which the clip will start playback. Open the drop down to read about the different interval types. 
* Default`default`\- Use the project's default quantization amount, found in the project panel section of the Bitwig UI
* None`none`\- No quantization, start clips immediately
* 8`8`\- Start clips at the next interval of 8 bars
* 4`4`\- Start clips at the next interval of 4 bars
* 2`2`\- Start clips at the next interval of 2 bars
* 1`1`\- Start clips at the next interval of 1 bar
* 1/2`1/2`\- Start clips at the next interval of 1/2 note
* 1/4`1/4`\- Start clips at the next interval of 1/4 note
* 1/8`1/8`\- Start clips at the next interval of 1/8 note
* 1/16`1/16`\- Start clips at the next interval of 1/16 note


Launch Mode`Launchmode`\- ⊞ \- Determines the launch behavior for the specified clip. Open the drop down to read about the different modes. 
* Default`default`\- Use the project's defualt launch mode, found in the project panel section of the Bitwig UI
* From Start`from_start`\- Plays the clip from the start
* Continue / From Start`continue_or_from_start`\- Plays relative to the playing clips position, of if nothing playing, from the clip start
* Continue / Synced`continue_or_synced`\- Plays relative to the playing clips position, of if nothing playing, from the transport position
* Synced`synced`\- Starts relative to global transport position


Launch`Launch`\- Launch the chosen clip slot 

Select`Select`\- Places the Bitwig Clip Launcher cursor on the chosen clip slot 

Stop`Stop`\- Stop the chosen clip slot's playback 

Record`Record`\- Begin recording on the chosen clip slot 

Color`Color`\- The color in RGB of the launcher clip 

Play Start`Playstart`\- The start position of the launcher clip in quarter-notes 

Play Stop`Playstop`\- The stop position of the launcher clip in quarter-notes 

Loop Enabled`Loopenabled`\- Indicates if playback looping is enabled for the chosen launcher clip 

Loop Start`Loopstart`\- The launcher clip's loop start position in quarter-notes 

Loop Length`Looplength`\- The launcher clip's loop length in quarter-notes 

Shuffle`Shuffle`\- Indicates if the clip's shuffle mode is active. 

Accent`Accent`\- Indicates the clip's accent value. 

## 

Parameters - Callbacks Page

Enable Callbacks`Enablecallbacks`\- Enables the clip launcher callbacks associated with this COMP. 

Callback DAT`Callbackdat`\- A reference to the Text DAT containing the callbacks for this COMP

Print Callbacks`Printcallbacks`\- When enabled, callback information will be printed to the text port as they are called. 

## 

Parameters - TDBitwig Page

TDBitwig Comp`Tdbitwigcomp`\- A reference to the Bitwig Main COMP

Connect`Connect`\- A toggle to manually enable or disable listeners associated with this COMP. 

Listener Index`Listenerindex`\- The index of the Cursor object which this COMP is communicating with. 

Debug Messages`Debugmessages`\- Print information about extension method calls for the Component

Timeslice OSC Chop`Timesliceoscchop`\- If timeslice is enabled, the OSC Chop will cook every frame. If disabled, OSC Chop will cook only during changes, but cook time may be longer. Using time slice for performance optimization will usually depend on the particular use case. 

Strip CHOP Name Prefixes`Stripchopnameprefixes`\- Strip off the given number of address segments in the output CHOP channel names 

Name Channel Prefix`Namechannelprefix`\- If enabled, the output CHOP channel names will include with the name of the currently selected Track object. Otherwise, the channel names will begin with the integer index of the Cursor this COMP is connected to. 

## 

Parameters - About Page

Help`Help`\- Opens this documentation page 

Version`Version`\- The TDBitwig version that this Component is updated to 

.tox Save Build`Toxsavebuild`\- The TouchDesigner build version that this Component was saved in 

Update`Update`\- If the tdBitwigPackage COMP is present in the TouchDesigner project, pressing pulse will update this Component to the newest version 

## 

Operator Outputs
* Output 0 \- A CHOP containing a channel for each listener property associated with this COMP
* Output 1 \- A Table DAT providing information about all clip slots for the chosen Track. Includes the slot index, name, and if the slot contains any content
* Output 2 \- A Table DAT providing information about clip playback. Includes info about the currently playing clip as well as the clip queued for playback.


TouchDesigner Build: Latest\nwikieditorwikieditor

Palette  
---  
[Palette ](<./Palette.md> "Palette")• [Palette:arcBallCamera ](<./Palette-arcBallCamera.md> "Palette:arcBallCamera")• [Palette:arcBallGeometry ](<./Palette-arcBallGeometry.md> "Palette:arcBallGeometry")• [Palette:audioAnalysis ](<./Palette-audioAnalysis.md> "Palette:audioAnalysis")• [Palette:audioSet ](<./Palette-audioSet.md> "Palette:audioSet")• [Palette:battery ](<./Palette-battery.md> "Palette:battery")• Palette:bitwigClip • [Palette:bitwigClipSlot ](<./Palette-bitwigClipSlot.md> "Palette:bitwigClipSlot")• [Palette:bitwigDeviceRemotes ](<./Palette-bitwigDeviceRemotes.md> "Palette:bitwigDeviceRemotes")• [Palette:bitwigMain ](<./Palette-bitwigMain.md> "Palette:bitwigMain")• [Palette:bitwigNote ](<./Palette-bitwigNote.md> "Palette:bitwigNote")• [Palette:bitwigProjectRemotes ](<./Palette-bitwigProjectRemotes.md> "Palette:bitwigProjectRemotes")• [Palette:bitwigRemotesDevice ](<./Palette-bitwigRemotesDevice.md> "Palette:bitwigRemotesDevice")• [Palette:bitwigRemotesProject ](<./Palette-bitwigRemotesProject.md> "Palette:bitwigRemotesProject")• [Palette:bitwigRemotesTrack ](<./Palette-bitwigRemotesTrack.md> "Palette:bitwigRemotesTrack")• [Palette:bitwigSelect ](<./Palette-bitwigSelect.md> "Palette:bitwigSelect")• [Palette:bitwigSong ](<./Palette-bitwigSong.md> "Palette:bitwigSong")• [Palette:bitwigTrack ](<./Palette-bitwigTrack.md> "Palette:bitwigTrack")• [Palette:bitwigTrackRemotes ](<./Palette-bitwigTrackRemotes.md> "Palette:bitwigTrackRemotes")• [Palette:blendModes ](<./Palette-blendModes.md> "Palette:blendModes")• [Palette:bloom ](<./Palette-bloom.md> "Palette:bloom")• [Palette:camera ](<./Palette-camera.md> "Palette:camera")• [Palette:cameraBrowser ](<./Palette-cameraBrowser.md> "Palette:cameraBrowser")• [Palette:cameraViewport ](<./Palette-cameraViewport.md> "Palette:cameraViewport")• [Palette:camSchnappr ](<./Palette-camSchnappr.md> "Palette:camSchnappr")• [Palette:changeColor ](<./Palette-changeColor.md> "Palette:changeColor")• [Palette:changeToColor ](<./Palette-changeToColor.md> "Palette:changeToColor")• [Palette:checker ](<./Palette-checker.md> "Palette:checker")• [Palette:chromaKey ](<./Palette-chromaKey.md> "Palette:chromaKey")• [Palette:colorThreshold ](<./Palette-colorThreshold.md> "Palette:colorThreshold")• [Palette:compareComp ](<./Palette-compareComp.md> "Palette:compareComp")• [Palette:convolve ](<./Palette-convolve.md> "Palette:convolve")• [Experimental:Palette:cornerPinPOP ](</Experimental:Palette:cornerPinPOP> "Experimental:Palette:cornerPinPOP")• [Palette:cornerPinSOP ](<./Palette-cornerPinSOP.md> "Palette:cornerPinSOP")• [Palette:cppParsTemplateGen ](<./Palette-cppParsTemplateGen.md> "Palette:cppParsTemplateGen")• [Palette:customAttributes ](<./Palette-customAttributes.md> "Palette:customAttributes")• [Palette:debugControl ](<./Palette-debugControl.md> "Palette:debugControl")• [Palette:dent ](<./Palette-dent.md> "Palette:dent")• [Palette:depthExtract ](<./Palette-depthExtract.md> "Palette:depthExtract")• [Palette:depthProjection ](<./Palette-depthProjection.md> "Palette:depthProjection")• [Palette:dilate ](<./Palette-dilate.md> "Palette:dilate")• [Experimental:Palette:domeViewer ](</Experimental:Palette:domeViewer> "Experimental:Palette:domeViewer")• [Palette:encoder ](<./Palette-encoder.md> "Palette:encoder")• [Palette:equalizer ](<./Palette-equalizer.md> "Palette:equalizer")• [Palette:feedback ](<./Palette-feedback.md> "Palette:feedback")• [Palette:feedbackEdge ](<./Palette-feedbackEdge.md> "Palette:feedbackEdge")• [Palette:firmata ](<./Palette-firmata.md> "Palette:firmata")• [Palette:gal ](<./Palette-gal.md> "Palette:gal")• [Palette:geoPanel ](<./Palette-geoPanel.md> "Palette:geoPanel")• [Palette:gestureCapture ](<./Palette-gestureCapture.md> "Palette:gestureCapture")• [Palette:graphPlot ](<./Palette-graphPlot.md> "Palette:graphPlot")• [Palette:histogram ](<./Palette-histogram.md> "Palette:histogram")• [Palette:hsvBlur ](<./Palette-hsvBlur.md> "Palette:hsvBlur")• [Palette:imageSearch ](<./Palette-imageSearch.md> "Palette:imageSearch")• [Palette:julia ](<./Palette-julia.md> "Palette:julia")• [Palette:kantanMapper ](<./Palette-kantanMapper.md> "Palette:kantanMapper")• [Palette:kinectCalibration ](<./Palette-kinectCalibration.md> "Palette:kinectCalibration")• [Palette:kinectPointcloud ](<./Palette-kinectPointcloud.md> "Palette:kinectPointcloud")• [Palette:leapPaint ](<./Palette-leapPaint.md> "Palette:leapPaint")• [Palette:lightTunnel ](<./Palette-lightTunnel.md> "Palette:lightTunnel")• [Palette:logger ](<./Palette-logger.md> "Palette:logger")• [Experimental:Palette:logger ](</Experimental:Palette:logger> "Experimental:Palette:logger")• [Palette:mandelbrot ](<./Palette-mandelbrot.md> "Palette:mandelbrot")• [Palette:materialDesignIcons ](<./Palette-materialDesignIcons.md> "Palette:materialDesignIcons")• [Palette:mesh ](<./Palette-mesh.md> "Palette:mesh")• [Palette:monochrome ](<./Palette-monochrome.md> "Palette:monochrome")• [Palette:motionSense ](<./Palette-motionSense.md> "Palette:motionSense")• [Palette:movieEngine ](<./Palette-movieEngine.md> "Palette:movieEngine")• [Palette:moviePlayer ](<./Palette-moviePlayer.md> "Palette:moviePlayer")• [Palette:moviePlaylist ](<./Palette-moviePlaylist.md> "Palette:moviePlaylist")• [Palette:multiLevel ](<./Palette-multiLevel.md> "Palette:multiLevel")• [Palette:multiMix ](<./Palette-multiMix.md> "Palette:multiMix")• [Palette:noise ](<./Palette-noise.md> "Palette:noise")• [Palette:onScreenKeyboard ](<./Palette-onScreenKeyboard.md> "Palette:onScreenKeyboard")• [Palette:operatorPath ](<./Palette-operatorPath.md> "Palette:operatorPath")• [Palette:opticalFlow ](<./Palette-opticalFlow.md> "Palette:opticalFlow")• [Palette:particlesGpu ](<./Palette-particlesGpu.md> "Palette:particlesGpu")• [Palette:pixelate ](<./Palette-pixelate.md> "Palette:pixelate")• [Palette:pixelRelocator ](<./Palette-pixelRelocator.md> "Palette:pixelRelocator")• [Palette:pointGenerator ](<./Palette-pointGenerator.md> "Palette:pointGenerator")• [Palette:pointillize ](<./Palette-pointillize.md> "Palette:pointillize")• [Palette:pointMerge ](<./Palette-pointMerge.md> "Palette:pointMerge")• [Palette:pointRender ](<./Palette-pointRender.md> "Palette:pointRender")• [Palette:pointRepack ](<./Palette-pointRepack.md> "Palette:pointRepack")• [Palette:pointTransform ](<./Palette-pointTransform.md> "Palette:pointTransform")• [Palette:pointWeight ](<./Palette-pointWeight.md> "Palette:pointWeight")• [Palette:popDialog ](<./Palette-popDialog.md> "Palette:popDialog")• [Experimental:Palette:popDialog ](</Experimental:Palette:popDialog> "Experimental:Palette:popDialog")• [Palette:probe ](<./Palette-probe.md> "Palette:probe")• [Palette:projectorBlend ](<./Palette-projectorBlend.md> "Palette:projectorBlend")• [Palette:pushPins ](<./Palette-pushPins.md> "Palette:pushPins")• [Palette:puzzle ](<./Palette-puzzle.md> "Palette:puzzle")• [Palette:quadReproject ](<./Palette-quadReproject.md> "Palette:quadReproject")• [Palette:radialBlur ](<./Palette-radialBlur.md> "Palette:radialBlur")• [Palette:recorder ](<./Palette-recorder.md> "Palette:recorder")• [Experimental:Palette:recorder ](</Experimental:Palette:recorder> "Experimental:Palette:recorder")• [Palette:remotePanel ](<./Palette-remotePanel.md> "Palette:remotePanel")• [Palette:rgbaBlur ](<./Palette-rgbaBlur.md> "Palette:rgbaBlur")• [Palette:rgbaDelay ](<./Palette-rgbaDelay.md> "Palette:rgbaDelay")• [Palette:rgbContrast ](<./Palette-rgbContrast.md> "Palette:rgbContrast")• [Palette:sceneChanger ](<./Palette-sceneChanger.md> "Palette:sceneChanger")• [Palette:search ](<./Palette-search.md> "Palette:search")• [Palette:searchReplace ](<./Palette-searchReplace.md> "Palette:searchReplace")• [Palette:sharpen ](<./Palette-sharpen.md> "Palette:sharpen")• [Palette:sickEngine ](<./Palette-sickEngine.md> "Palette:sickEngine")• [Palette:signalingClient ](<./Palette-signalingClient.md> "Palette:signalingClient")• [Palette:signalingServer ](<./Palette-signalingServer.md> "Palette:signalingServer")• [Palette:softenAlpha ](<./Palette-softenAlpha.md> "Palette:softenAlpha")• [Palette:solarize ](<./Palette-solarize.md> "Palette:solarize")• [Palette:sopRender ](<./Palette-sopRender.md> "Palette:sopRender")• [Palette:splitter ](<./Palette-splitter.md> "Palette:splitter")• [Palette:stitcher ](<./Palette-stitcher.md> "Palette:stitcher")• [Palette:stoner ](<./Palette-stoner.md> "Palette:stoner")• [Palette:superFormula ](<./Palette-superFormula.md> "Palette:superFormula")• [Palette:SVG ](<./Palette-SVG.md> "Palette:SVG")• [Palette:sweetSpot ](<./Palette-sweetSpot.md> "Palette:sweetSpot")• [Palette:sweetSpotPreviz ](<./Palette-sweetSpotPreviz.md> "Palette:sweetSpotPreviz")• [Palette:synchroCache ](<./Palette-synchroCache.md> "Palette:synchroCache")• [Palette:synchroClient ](<./Palette-synchroClient.md> "Palette:synchroClient")• [Palette:synchroFrameIn ](<./Palette-synchroFrameIn.md> "Palette:synchroFrameIn")• [Palette:synchroFrameOut ](<./Palette-synchroFrameOut.md> "Palette:synchroFrameOut")• [Palette:synchroNDIIn ](<./Palette-synchroNDIIn.md> "Palette:synchroNDIIn")• [Palette:synchroSDIIn ](<./Palette-synchroSDIIn.md> "Palette:synchroSDIIn")• [Palette:synchroVideoOut ](<./Palette-synchroVideoOut.md> "Palette:synchroVideoOut")• [Palette:tdBitwigPackage ](<./Palette-tdBitwigPackage.md> "Palette:tdBitwigPackage")• [Experimental:Palette:tdPyEnvManager ](</Experimental:Palette:tdPyEnvManager> "Experimental:Palette:tdPyEnvManager")• [Palette:TDVR ](<./Palette-TDVR.md> "Palette:TDVR")• [Palette:testGrid ](<./Palette-testGrid.md> "Palette:testGrid")• [Experimental:Palette:threadManagerClient ](</Experimental:Palette:threadManagerClient> "Experimental:Palette:threadManagerClient")• [Experimental:Palette:threadsMonitor ](</Experimental:Palette:threadsMonitor> "Experimental:Palette:threadsMonitor")• [Palette:transitMap ](<./Palette-transitMap.md> "Palette:transitMap")• [Palette:twirl ](<./Palette-twirl.md> "Palette:twirl")• [Palette:vectorScope ](<./Palette-vectorScope.md> "Palette:vectorScope")• [Palette:virtualFile ](<./Palette-virtualFile.md> "Palette:virtualFile")• [Palette:waveformMonitor ](<./Palette-waveformMonitor.md> "Palette:waveformMonitor")• [Palette:webBrowser ](<./Palette-webBrowser.md> "Palette:webBrowser")• [Palette:webRTC ](<./Palette-webRTC.md> "Palette:webRTC")• [Palette:webRTCPanel ](<./Palette-webRTCPanel.md> "Palette:webRTCPanel")• [Palette:webRTCPanelRcv ](<./Palette-webRTCPanelRcv.md> "Palette:webRTCPanelRcv")• [Palette:xyScope ](<./Palette-xyScope.md> "Palette:xyScope")• [Experimental:Thread Manager ](</Experimental:Thread_Manager> "Experimental:Thread Manager")
