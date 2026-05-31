# Palette:recorder

##   
  
Summary

The recorder component is a wrapper for the moviefileout TOP. Its purpose is to simplify the video recording process as a single component. It is recommended to be used as the recording system in larger video applications.  
  
To use the recorder:  
# Connect your video source TOP to the input  
# Set the output folder and filename parts (supports up to 7 filename segments separated by underscores)  
# Configure video settings: resolution (custom or from input), frame rate, and frame range  
# For audio recording, connect an audio CHOP to the Audio CHOP parameter  
# Click Record Start to begin recording, Record Stop to end (or let it auto-stop if using frame range)  
  
Key features:  
* Automatic filename generation with configurable segments and auto-incrementing index (N parameter)  
* Support for timeline synchronization and frame-accurate recording  
* Cook Every Frame option for offline vs real-time recording modes  
* Custom resolution override capability  
* Header metadata support via DAT input  
* Timeline matching utilities for synchronizing recorder settings with project timeline 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)Palette:recorder

## 

Parameters - Output Settings Page

Configure file output, recording controls, resolution, frame range, and timeline settings 

Folder`Folder`\- The directory where the recorded video files are saved. 

View Folder`Viewfolder`\- Opens a file browser to where the recorded video files will be saved. 

Filename 1`Filename1`\- Allows the user to set multiple filename strings. Each string is separated by an underscore. 

Filename 2`Filename2`\- Allows the user to set multiple filename strings. Each string is separated by an underscore. 

Filename 3`Filename3`\- Allows the user to set multiple filename strings. Each string is separated by an underscore. 

Filename 4`Filename4`\- Allows the user to set multiple filename strings. Each string is separated by an underscore. 

Filename 5`Filename5`\- Allows the user to set multiple filename strings. Each string is separated by an underscore. 

Filename 6`Filename6`\- Allows the user to set multiple filename strings. Each string is separated by an underscore. 

Filename 7`Filename7`\- Allows the user to set multiple filename strings. Each string is separated by an underscore. 

N`N`\- This parameter increases by 1 each time a recording is generated. The N index is postfixed to the file name and thus filename collisions can be avoided. 

File Path`Filepath`\- Shows the complete path (Folder \+ Filename) where the video will be saved. 

Record Start`Recordstart`\- Triggers the start of the recording. 

Record Stop`Recordstop`\- Stops the recording. 

Record Active`Recordactive`\- Indicates if recording is currently active or not. 

Audio CHOP`Audiochop`\- Provide a chop with an audiostream for recording audio into the file. 

Header Source DAT`Headerdat`\- Specify a DAT that holds desired meta information for encoding data into the header of the file. 

Custom Resolution`Customresolution`\- When active a custom resolution is used instead of the incoming resolution. 

Resolution`Resolution`\- ⊞ \- A custom resolution to override that which is coming in via the TOP connector. 
* Resolution`Resolutionw`-
* Resolution`Resolutionh`-


Record Range`Recordrange`\- When active, the specfied frame range is used and once the range has been recorded, the encoder stops automatically. This range corresponds to the timeline range. 

Frame Range`Framerange`\- ⊞ \- The frame range to record when Record Range paramater is active. 
* Frame Range`Framerange1`-
* Frame Range`Framerange2`-


Rate (FPS)`Rate`\- The frame rate to record at. 

Use Timeline`Locktotimeline`\- Ensures the recording is synchronized with a specified timeline or timecode. 

Cook Every Frame`Cookeveryframe`\- You want this on if you are doing a high quality offline render. You want this off if you are recording in real-time. 

Reload Movie Meta Data`Reload`\- Forces a reload of movie file information from the first moviefileinTOP that is found connected upstream of the input TOP connection. 

Match Timeline To Media`Matchmedia`\- Ensures the recorder's settings match the settings of another media file or source. 

Match Record Settings to Timeline`Matchrecordtotimeline`\- Sets the recorder comp settings to match the timeline 

Match Timeline to Record Settings`Matchtimelinetorecord`\- Matches the timeline to the recorder comp settings 

## 

Parameters - Codec Page

Configure video and audio codec settings for encoding 

Codec`Videocodec`\- ⊞ \- Select the video compression codec used to encode the movie. 

[Template:ParameterMenuItem](</index.php?title=Template:ParameterMenuItem&action=edit&redlink=1> "Template:ParameterMenuItem \(page does not exist\)")[Template:ParameterMenuItem](</index.php?title=Template:ParameterMenuItem&action=edit&redlink=1> "Template:ParameterMenuItem \(page does not exist\)")[Template:ParameterMenuItem](</index.php?title=Template:ParameterMenuItem&action=edit&redlink=1> "Template:ParameterMenuItem \(page does not exist\)")[Template:ParameterMenuItem](</index.php?title=Template:ParameterMenuItem&action=edit&redlink=1> "Template:ParameterMenuItem \(page does not exist\)")[Template:ParameterMenuItem](</index.php?title=Template:ParameterMenuItem&action=edit&redlink=1> "Template:ParameterMenuItem \(page does not exist\)")[Template:ParameterMenuItem](</index.php?title=Template:ParameterMenuItem&action=edit&redlink=1> "Template:ParameterMenuItem \(page does not exist\)")

Video Codec Type`Videocodectype`\- Some video codecs such as Apple ProRes, Hap and Hap Q have a various different types such as ProRes 442 HQ, ProRe 4444 HQ etc. 

Movie Pixel Format`Moviepixelformat`\- Options for the pixel format based on the Video Codec selected. Use this parameter to change the color quality of the output (how many bits are used, YUV sampling etc.), as well as selecting formats that include alpha for codecs that support alpha. 

Audio Codec`Audiocodec`\- Select the audio compression codec used to encode the audio. 

Quality`Quality`\- Select the quality of the movie compression. NOTE: Some codecs can not output lossless compression. 

Stall for File Open`Stallforopen`\- When this is on playback will stall until the file is opened and ready to receive frames, to make sure the frame that was inputted when Record was turned on gets recorded. When this is off recording may start on a later frame, after the file has been opened. Turning this off can avoid a stall in playback, if missing recording some frames at the start is acceptable. 

Profile`Profile`\- Select the H.264 profile to use. 

Preset`Preset`\- The H264 preset to use. 

Bit Rate Mode`Bitratemode`\- Select between Constant or Variable bit rate, and regular or high quality bit rate modes. 

Average Bit Rate`Avgbitrate`\- Set the average bitrate target for the encoding. 

Peak Bit Rate`Peakbitrate`\- Set the peak bitrate allowed for the encoding. 

Keyframe Interval`Keyframeinterval`\- Set the number of frames between key-frames (I-frames) while encoding. 

Max B-Frames`Maxbframes`\- Controls the maximum number of B-frames (bi-directional frames) that will be created between pairs of key-frames. 

Motion Prediction`Motionpredict`\- Controls the quality of the Motion Prediction used when encoding H264/H265. 

Frame Slicing`Frameslicing`\- Controls if H264/H265 frames are sliced into multiple pieces, allowing them to be decoded using multiple CPUs more easily. 

Num Slices`Numslices`\- The number of slices each frame is split into. 

Secondary Compression`Secondarycompression`\- Hap uses a secondary CPU compression stage usually. Encoding video without this compression will result in faster playback, but potentially larger file sizes (which would require faster drives to play back). 

## 

Operator Inputs
* Input 0: in1 \- Video input to be recorded


TouchDesigner Build: Latest\nwikieditorwikieditorwikieditorwikieditorwikieditorwikieditor2025.300002023.11280

Palette  
---  
[Palette ](<./Palette.md> "Palette")• [Palette:arcBallCamera ](<./Palette-arcBallCamera.md> "Palette:arcBallCamera")• [Palette:arcBallGeometry ](<./Palette-arcBallGeometry.md> "Palette:arcBallGeometry")• [Palette:audioAnalysis ](<./Palette-audioAnalysis.md> "Palette:audioAnalysis")• [Palette:audioSet ](<./Palette-audioSet.md> "Palette:audioSet")• [Palette:autoMediaPlayer ](<./Palette-autoMediaPlayer.md> "Palette:autoMediaPlayer")• [Palette:battery ](<./Palette-battery.md> "Palette:battery")• [Palette:bitwigClip ](<./Palette-bitwigClip.md> "Palette:bitwigClip")• [Palette:bitwigClipSlot ](<./Palette-bitwigClipSlot.md> "Palette:bitwigClipSlot")• [Palette:bitwigDeviceRemotes ](<./Palette-bitwigDeviceRemotes.md> "Palette:bitwigDeviceRemotes")• [Palette:bitwigMain ](<./Palette-bitwigMain.md> "Palette:bitwigMain")• [Palette:bitwigNote ](<./Palette-bitwigNote.md> "Palette:bitwigNote")• [Palette:bitwigProjectRemotes ](<./Palette-bitwigProjectRemotes.md> "Palette:bitwigProjectRemotes")• [Palette:bitwigRemotesDevice ](<./Palette-bitwigRemotesDevice.md> "Palette:bitwigRemotesDevice")• [Palette:bitwigRemotesProject ](<./Palette-bitwigRemotesProject.md> "Palette:bitwigRemotesProject")• [Palette:bitwigRemotesTrack ](<./Palette-bitwigRemotesTrack.md> "Palette:bitwigRemotesTrack")• [Palette:bitwigSelect ](<./Palette-bitwigSelect.md> "Palette:bitwigSelect")• [Palette:bitwigSong ](<./Palette-bitwigSong.md> "Palette:bitwigSong")• [Palette:bitwigTrack ](<./Palette-bitwigTrack.md> "Palette:bitwigTrack")• [Palette:bitwigTrackRemotes ](<./Palette-bitwigTrackRemotes.md> "Palette:bitwigTrackRemotes")• [Palette:blendModes ](<./Palette-blendModes.md> "Palette:blendModes")• [Palette:bloom ](<./Palette-bloom.md> "Palette:bloom")• [Palette:camera ](<./Palette-camera.md> "Palette:camera")• [Palette:cameraBrowser ](<./Palette-cameraBrowser.md> "Palette:cameraBrowser")• [Palette:cameraViewport ](<./Palette-cameraViewport.md> "Palette:cameraViewport")• [Palette:camSchnappr ](<./Palette-camSchnappr.md> "Palette:camSchnappr")• [Palette:changeColor ](<./Palette-changeColor.md> "Palette:changeColor")• [Palette:changeToColor ](<./Palette-changeToColor.md> "Palette:changeToColor")• [Palette:checker ](<./Palette-checker.md> "Palette:checker")• [Palette:chromaKey ](<./Palette-chromaKey.md> "Palette:chromaKey")• [Palette:colorThreshold ](<./Palette-colorThreshold.md> "Palette:colorThreshold")• [Palette:compareComp ](<./Palette-compareComp.md> "Palette:compareComp")• [Palette:convolve ](<./Palette-convolve.md> "Palette:convolve")• [Experimental:Palette:cornerPinPOP ](</index.php?title=Experimental:Palette:cornerPinPOP&action=edit&redlink=1> "Experimental:Palette:cornerPinPOP \(page does not exist\)")• [Palette:cornerPinSOP ](<./Palette-cornerPinSOP.md> "Palette:cornerPinSOP")• [Palette:cppParsTemplateGen ](<./Palette-cppParsTemplateGen.md> "Palette:cppParsTemplateGen")• [Palette:customAttributes ](<./Palette-customAttributes.md> "Palette:customAttributes")• [Palette:debugControl ](<./Palette-debugControl.md> "Palette:debugControl")• [Palette:dent ](<./Palette-dent.md> "Palette:dent")• [Palette:depthExtract ](<./Palette-depthExtract.md> "Palette:depthExtract")• [Palette:depthProjection ](<./Palette-depthProjection.md> "Palette:depthProjection")• [Palette:dilate ](<./Palette-dilate.md> "Palette:dilate")• [Experimental:Palette:domeViewer ](</index.php?title=Experimental:Palette:domeViewer&action=edit&redlink=1> "Experimental:Palette:domeViewer \(page does not exist\)")• [Palette:encoder ](<./Palette-encoder.md> "Palette:encoder")• [Palette:equalizer ](<./Palette-equalizer.md> "Palette:equalizer")• [Palette:feedback ](<./Palette-feedback.md> "Palette:feedback")• [Palette:feedbackEdge ](<./Palette-feedbackEdge.md> "Palette:feedbackEdge")• [Palette:firmata ](<./Palette-firmata.md> "Palette:firmata")• [Palette:gal ](<./Palette-gal.md> "Palette:gal")• [Palette:geoPanel ](<./Palette-geoPanel.md> "Palette:geoPanel")• [Palette:gestureCapture ](<./Palette-gestureCapture.md> "Palette:gestureCapture")• [Palette:graphPlot ](<./Palette-graphPlot.md> "Palette:graphPlot")• [Palette:histogram ](<./Palette-histogram.md> "Palette:histogram")• [Palette:hsvBlur ](<./Palette-hsvBlur.md> "Palette:hsvBlur")• [Palette:imageSearch ](<./Palette-imageSearch.md> "Palette:imageSearch")• [Palette:julia ](<./Palette-julia.md> "Palette:julia")• [Palette:kantanMapper ](<./Palette-kantanMapper.md> "Palette:kantanMapper")• [Palette:kinectCalibration ](<./Palette-kinectCalibration.md> "Palette:kinectCalibration")• [Palette:kinectPointcloud ](<./Palette-kinectPointcloud.md> "Palette:kinectPointcloud")• [Palette:leapPaint ](<./Palette-leapPaint.md> "Palette:leapPaint")• [Palette:lightTunnel ](<./Palette-lightTunnel.md> "Palette:lightTunnel")• [Palette:logger ](<./Palette-logger.md> "Palette:logger")• [Experimental:Palette:logger ](</index.php?title=Experimental:Palette:logger&action=edit&redlink=1> "Experimental:Palette:logger \(page does not exist\)")• [Palette:mandelbrot ](<./Palette-mandelbrot.md> "Palette:mandelbrot")• [Palette:materialDesignIcons ](<./Palette-materialDesignIcons.md> "Palette:materialDesignIcons")• [Palette:mesh ](<./Palette-mesh.md> "Palette:mesh")• [Palette:monochrome ](<./Palette-monochrome.md> "Palette:monochrome")• [Palette:motionSense ](<./Palette-motionSense.md> "Palette:motionSense")• [Palette:movieEngine ](<./Palette-movieEngine.md> "Palette:movieEngine")• [Palette:moviePlayer ](<./Palette-moviePlayer.md> "Palette:moviePlayer")• [Palette:moviePlaylist ](<./Palette-moviePlaylist.md> "Palette:moviePlaylist")• [Palette:multiLevel ](<./Palette-multiLevel.md> "Palette:multiLevel")• [Palette:multiMix ](<./Palette-multiMix.md> "Palette:multiMix")• [Palette:noise ](<./Palette-noise.md> "Palette:noise")• [Palette:onScreenKeyboard ](<./Palette-onScreenKeyboard.md> "Palette:onScreenKeyboard")• [Palette:operatorPath ](<./Palette-operatorPath.md> "Palette:operatorPath")• [Palette:opticalFlow ](<./Palette-opticalFlow.md> "Palette:opticalFlow")• [Palette:particlesGpu ](<./Palette-particlesGpu.md> "Palette:particlesGpu")• [Palette:pixelate ](<./Palette-pixelate.md> "Palette:pixelate")• [Palette:pixelRelocator ](<./Palette-pixelRelocator.md> "Palette:pixelRelocator")• [Palette:pointGenerator ](<./Palette-pointGenerator.md> "Palette:pointGenerator")• [Palette:pointillize ](<./Palette-pointillize.md> "Palette:pointillize")• [Palette:pointMerge ](<./Palette-pointMerge.md> "Palette:pointMerge")• [Palette:pointRender ](<./Palette-pointRender.md> "Palette:pointRender")• [Palette:pointRepack ](<./Palette-pointRepack.md> "Palette:pointRepack")• [Palette:pointTransform ](<./Palette-pointTransform.md> "Palette:pointTransform")• [Palette:pointWeight ](<./Palette-pointWeight.md> "Palette:pointWeight")• [Palette:popDialog ](<./Palette-popDialog.md> "Palette:popDialog")• [Experimental:Palette:popDialog ](</index.php?title=Experimental:Palette:popDialog&action=edit&redlink=1> "Experimental:Palette:popDialog \(page does not exist\)")• [Palette:probe ](<./Palette-probe.md> "Palette:probe")• [Palette:projectorBlend ](<./Palette-projectorBlend.md> "Palette:projectorBlend")• [Palette:pushPins ](<./Palette-pushPins.md> "Palette:pushPins")• [Palette:puzzle ](<./Palette-puzzle.md> "Palette:puzzle")• [Palette:quadReproject ](<./Palette-quadReproject.md> "Palette:quadReproject")• [Palette:radialBlur ](<./Palette-radialBlur.md> "Palette:radialBlur")• Palette:recorder • [Experimental:Palette:recorder ](</index.php?title=Experimental:Palette:recorder&action=edit&redlink=1> "Experimental:Palette:recorder \(page does not exist\)")• [Palette:remotePanel ](<./Palette-remotePanel.md> "Palette:remotePanel")• [Palette:rgbaBlur ](<./Palette-rgbaBlur.md> "Palette:rgbaBlur")• [Palette:rgbaDelay ](<./Palette-rgbaDelay.md> "Palette:rgbaDelay")• [Palette:rgbContrast ](<./Palette-rgbContrast.md> "Palette:rgbContrast")• [Palette:sceneChanger ](<./Palette-sceneChanger.md> "Palette:sceneChanger")• [Palette:search ](<./Palette-search.md> "Palette:search")• [Palette:searchReplace ](<./Palette-searchReplace.md> "Palette:searchReplace")• [Palette:sharpen ](<./Palette-sharpen.md> "Palette:sharpen")• [Palette:sickEngine ](<./Palette-sickEngine.md> "Palette:sickEngine")• [Palette:signalingClient ](<./Palette-signalingClient.md> "Palette:signalingClient")• [Palette:signalingServer ](<./Palette-signalingServer.md> "Palette:signalingServer")• [Palette:softenAlpha ](<./Palette-softenAlpha.md> "Palette:softenAlpha")• [Palette:solarize ](<./Palette-solarize.md> "Palette:solarize")• [Palette:sopRender ](<./Palette-sopRender.md> "Palette:sopRender")• [Palette:splitter ](<./Palette-splitter.md> "Palette:splitter")• [Palette:stitcher ](<./Palette-stitcher.md> "Palette:stitcher")• [Palette:stoner ](<./Palette-stoner.md> "Palette:stoner")• [Palette:superFormula ](<./Palette-superFormula.md> "Palette:superFormula")• [Palette:SVG ](<./Palette-SVG.md> "Palette:SVG")• [Palette:sweetSpot ](<./Palette-sweetSpot.md> "Palette:sweetSpot")• [Palette:sweetSpotPreviz ](<./Palette-sweetSpotPreviz.md> "Palette:sweetSpotPreviz")• [Palette:synchroCache ](<./Palette-synchroCache.md> "Palette:synchroCache")• [Palette:synchroClient ](<./Palette-synchroClient.md> "Palette:synchroClient")• [Palette:synchroFrameIn ](<./Palette-synchroFrameIn.md> "Palette:synchroFrameIn")• [Palette:synchroFrameOut ](<./Palette-synchroFrameOut.md> "Palette:synchroFrameOut")• [Palette:synchroNDIIn ](<./Palette-synchroNDIIn.md> "Palette:synchroNDIIn")• [Palette:synchroSDIIn ](<./Palette-synchroSDIIn.md> "Palette:synchroSDIIn")• [Palette:synchroVideoOut ](<./Palette-synchroVideoOut.md> "Palette:synchroVideoOut")• [Palette:tdBitwigPackage ](<./Palette-tdBitwigPackage.md> "Palette:tdBitwigPackage")• [Experimental:Palette:tdPyEnvManager ](</index.php?title=Experimental:Palette:tdPyEnvManager&action=edit&redlink=1> "Experimental:Palette:tdPyEnvManager \(page does not exist\)")• [Palette:TDVR ](<./Palette-TDVR.md> "Palette:TDVR")• [Palette:testGrid ](<./Palette-testGrid.md> "Palette:testGrid")• [Experimental:Palette:threadManagerClient ](</index.php?title=Experimental:Palette:threadManagerClient&action=edit&redlink=1> "Experimental:Palette:threadManagerClient \(page does not exist\)")• [Experimental:Palette:threadsMonitor ](</index.php?title=Experimental:Palette:threadsMonitor&action=edit&redlink=1> "Experimental:Palette:threadsMonitor \(page does not exist\)")• [Palette:transitMap ](<./Palette-transitMap.md> "Palette:transitMap")• [Palette:twirl ](<./Palette-twirl.md> "Palette:twirl")• [Palette:vectorScope ](<./Palette-vectorScope.md> "Palette:vectorScope")• [Palette:virtualFile ](<./Palette-virtualFile.md> "Palette:virtualFile")• [Palette:waveformMonitor ](<./Palette-waveformMonitor.md> "Palette:waveformMonitor")• [Palette:webBrowser ](<./Palette-webBrowser.md> "Palette:webBrowser")• [Palette:webRTC ](<./Palette-webRTC.md> "Palette:webRTC")• [Palette:webRTCPanel ](<./Palette-webRTCPanel.md> "Palette:webRTCPanel")• [Palette:webRTCPanelRcv ](<./Palette-webRTCPanelRcv.md> "Palette:webRTCPanelRcv")• [Palette:xyScope ](<./Palette-xyScope.md> "Palette:xyScope")• [Experimental:Thread Manager ](</index.php?title=Experimental:Thread_Manager&action=edit&redlink=1> "Experimental:Thread Manager \(page does not exist\)")
