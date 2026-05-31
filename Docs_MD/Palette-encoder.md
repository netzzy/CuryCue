# Palette:encoder

##   
  
Summary

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[Palette:encoder Ext](</index.php?title=Palette:encoder_Ext&action=edit&redlink=1> "Palette:encoder Ext \(page does not exist\)")

## 

Parameters - Output Settings Page

Folder`Folder`\- The folder to save newly encoded files to. 

View Folder`Viewfolder`\- Open file browser to the specified folder. 

Filename 1`Filename1`\- Define a string for part 1 of the filename. 

Filename 2`Filename2`\- Define a string for part 2 of the filename. 

Filename 3`Filename3`\- Define a string for part 3 of the filename. 

Filename 4`Filename4`\- Define a string for part 4 of the filename. 

Filename 5`Filename5`\- Define a string for part 5 of the filename. 

Record Start`Recordstart`\- Starts encoding and recording the file to disk. 

Record Stop`Recordstop`\- Stops encoding and recording of the file. 

Record Active`Recordactive`\- Relays the state of encoding. Its on when recording and off when not recording. This state is for informational purposes only. 

Audio CHOP`Audiochop`\- Provide a chop with an audiostream for recording audio into the file. 

Header Source DAT`Headerdat`\- Specify a DAT that holds desired meta information for encoding data into the header of the file. 

Custom Resolution`Customresolution`\- When active a custom resolution is used instead of the incoming resolution. 

Resolution`Resolution`\- ⊞ \- A custom resolution to override that which is coming in via the TOP connector. 
* Resolution`Resolutionw`-
* Resolution`Resolutionh`-


Record Range`Recordrange`\- When active, the specfied frame range is used and once the range has been recorded, the encoder stops automatically. 

Frame Range`Framerange`\- ⊞ \- The frame range to record when Record Range paramater is active. 
* Frame Range`Framerange1`-
* Frame Range`Framerange2`-


Rate (FPS)`Rate`\- The frame rate to record at. 

Use Timeline`Locktotimeline`\- Not supported yet. 

Cook Every Frame`Cookeveryframe`\- When active, the real-time mode for TouchDesigner is turned off, and every frame step is full cooked and encoded to file. When not active, the real-time that is currently set is used. 

Reload Movie Meta Data`Reload`\- Forces a reload of movie file information from the first moviefileinTOP that is found connected upstream of the input TOP connection. 

Match Timeline To Media`Matchmedia`\- Matches tthe main TouchDesigner timeline settings to the settings set in this encoder component. 

Match Record Settings to Timeline`Matchtimeline`\- Matches the settings in this encoder component to match that of the time settings for the timeline. 

## 

Parameters - Codec Page

Codec`Videocodec`\- ⊞ \- Select the video compression codec used to encode the movie. 
* Animation`rle`-
* Hap`hap`-
* Hap Q`hapq`-
* Hap R`hapr`-
* Hap HDR`haphdr`-
* H.264 (NVIDIA GPU)`h264nvgpu`-
* H.265/HEVC (NVIDIA GPU)`h265nvgpu`-
* GIF`gif`-
* NotchLC`notchlc`-
* VP8`vp8`-
* VP9`vp9`-


Movie Pixel Format`Moviepixelformat`\- ⊞ \- Options for the pixel format based on the Video Codec selected. 
* RGB`rgb`-
* RGBA (Hap Q Alpha)`rgbabc4`-


Audio Codec`Audiocodec`\- ⊞ \- Select the audio compression codec used to encode the audio. 
* ALAC (Apple Lossless)`alac`-
* MP3`mp3`-
* Uncompressed 16-bit (PCM)`pcm16`-
* Uncompressed 24-bit (PCM)`pcm24`-
* Uncompressed 32-bit (PCM)`pcm32`-
* Vorbis`vorbis`-


Quality`Quality`\- Select the quality of the movie compression. NOTE: Some codecs can not output lossless compression. 

Stall for File Open`Stallforopen`\- When this is on playback will stall until the file is opened and ready to receive frames, to make sure the frame that was inputted when Record was turned on gets recorded. When this is off recording may start on a later frame, after the file has been opened. Turning this off can avoid a stall in playback, if missing recording some frames at the start is acceptable. 

Profile`Profile`\- ⊞ \- Select the H.264 profile to use. 
* Auto-Select`autoselect`-
* Baseline`baseline`-
* Main`main`-
* High`high`-


Preset`Preset`\- ⊞ \- Select from the available presets. 
* None`none`-
* Lossless`lossless`-


Bit Rate Mode`Bitratemode`\- ⊞ \- Select between Constant or Variable bit rate, and regular or high quality bit rate modes. 
* Constant (CBR)`constant`-
* Variable (VBR)`variable`-
* Constant HQ (CBR)`constanthq`-
* Variable HQ (VBR)`variablehq`-


Average Bit Rate`Avgbitrate`\- Set the average bitrate target for the encoding. 

Peak Bit Rate`Peakbitrate`\- Set the peak bitrate allowed for the encoding. 

Keyframe Internval`Keyframeinterval`\- Set the number of frames between key-frames (I-frames) while encoding. 

Max B-Frames`Maxbframes`\- Bi-directional predicted (B) frames/slices (macroblocks) 

Motion Prediction`Motionpredict`\- ⊞ \- This setting can effect the final size of the compressed video but depends greatly on the complexity of the scene being encoded. The menu entries refers to the distance between pixels (quarter distance, half distance, or full distance which is a full pixel) as the motion vector precision for motion estimation during video compression. Quarter pixel precision can increase the quality of the motion prediction signal over half pixel precision, and this can sometimes result in better overall size compression if the improved prediction signal can offset the additional bits it takes to encode the higher precision motion vectors. 
* Default`default`-
* Quarter`quarter`-
* Half`half`-
* Full`full`-


Frame Slicing`Frameslicing`\- Enables frame slicing in the encoding which can control error resiliance of the video. 

Num Slices`Numslices`\- The number of slices to use when Frame Slicing is On. 

Secondarycompression`Secondarycompression`\- Hap uses a secondary CPU compression stage usually. Encoding video without this compression will result in faster playback, but potentially larger file sizes (which would require faster drives to play back). 

## 

Parameters - About Page

Help`Help`\- 

Version`Version`\- 

.tox Save Build`Toxsavebuild`\- 

## 

Operator Inputs
* Input 0: in1 -

Palette  
---  
[Palette ](<./Palette.md> "Palette")• [Palette:arcBallCamera ](<./Palette-arcBallCamera.md> "Palette:arcBallCamera")• [Palette:arcBallGeometry ](<./Palette-arcBallGeometry.md> "Palette:arcBallGeometry")• [Palette:audioAnalysis ](<./Palette-audioAnalysis.md> "Palette:audioAnalysis")• [Palette:audioSet ](<./Palette-audioSet.md> "Palette:audioSet")• [Palette:battery ](<./Palette-battery.md> "Palette:battery")• [Palette:bitwigClip ](<./Palette-bitwigClip.md> "Palette:bitwigClip")• [Palette:bitwigClipSlot ](<./Palette-bitwigClipSlot.md> "Palette:bitwigClipSlot")• [Palette:bitwigDeviceRemotes ](<./Palette-bitwigDeviceRemotes.md> "Palette:bitwigDeviceRemotes")• [Palette:bitwigMain ](<./Palette-bitwigMain.md> "Palette:bitwigMain")• [Palette:bitwigNote ](<./Palette-bitwigNote.md> "Palette:bitwigNote")• [Palette:bitwigProjectRemotes ](<./Palette-bitwigProjectRemotes.md> "Palette:bitwigProjectRemotes")• [Palette:bitwigRemotesDevice ](<./Palette-bitwigRemotesDevice.md> "Palette:bitwigRemotesDevice")• [Palette:bitwigRemotesProject ](<./Palette-bitwigRemotesProject.md> "Palette:bitwigRemotesProject")• [Palette:bitwigRemotesTrack ](<./Palette-bitwigRemotesTrack.md> "Palette:bitwigRemotesTrack")• [Palette:bitwigSelect ](<./Palette-bitwigSelect.md> "Palette:bitwigSelect")• [Palette:bitwigSong ](<./Palette-bitwigSong.md> "Palette:bitwigSong")• [Palette:bitwigTrack ](<./Palette-bitwigTrack.md> "Palette:bitwigTrack")• [Palette:bitwigTrackRemotes ](<./Palette-bitwigTrackRemotes.md> "Palette:bitwigTrackRemotes")• [Palette:blendModes ](<./Palette-blendModes.md> "Palette:blendModes")• [Palette:bloom ](<./Palette-bloom.md> "Palette:bloom")• [Palette:camera ](<./Palette-camera.md> "Palette:camera")• [Palette:cameraBrowser ](<./Palette-cameraBrowser.md> "Palette:cameraBrowser")• [Palette:cameraViewport ](<./Palette-cameraViewport.md> "Palette:cameraViewport")• [Palette:camSchnappr ](<./Palette-camSchnappr.md> "Palette:camSchnappr")• [Palette:changeColor ](<./Palette-changeColor.md> "Palette:changeColor")• [Palette:changeToColor ](<./Palette-changeToColor.md> "Palette:changeToColor")• [Palette:checker ](<./Palette-checker.md> "Palette:checker")• [Palette:chromaKey ](<./Palette-chromaKey.md> "Palette:chromaKey")• [Palette:colorThreshold ](<./Palette-colorThreshold.md> "Palette:colorThreshold")• [Palette:compareComp ](<./Palette-compareComp.md> "Palette:compareComp")• [Palette:convolve ](<./Palette-convolve.md> "Palette:convolve")• [Experimental:Palette:cornerPinPOP ](</Experimental:Palette:cornerPinPOP> "Experimental:Palette:cornerPinPOP")• [Palette:cornerPinSOP ](<./Palette-cornerPinSOP.md> "Palette:cornerPinSOP")• [Palette:cppParsTemplateGen ](<./Palette-cppParsTemplateGen.md> "Palette:cppParsTemplateGen")• [Palette:customAttributes ](<./Palette-customAttributes.md> "Palette:customAttributes")• [Palette:debugControl ](<./Palette-debugControl.md> "Palette:debugControl")• [Palette:dent ](<./Palette-dent.md> "Palette:dent")• [Palette:depthExtract ](<./Palette-depthExtract.md> "Palette:depthExtract")• [Palette:depthProjection ](<./Palette-depthProjection.md> "Palette:depthProjection")• [Palette:dilate ](<./Palette-dilate.md> "Palette:dilate")• [Experimental:Palette:domeViewer ](</Experimental:Palette:domeViewer> "Experimental:Palette:domeViewer")• Palette:encoder • [Palette:equalizer ](<./Palette-equalizer.md> "Palette:equalizer")• [Palette:feedback ](<./Palette-feedback.md> "Palette:feedback")• [Palette:feedbackEdge ](<./Palette-feedbackEdge.md> "Palette:feedbackEdge")• [Palette:firmata ](<./Palette-firmata.md> "Palette:firmata")• [Palette:gal ](<./Palette-gal.md> "Palette:gal")• [Palette:geoPanel ](<./Palette-geoPanel.md> "Palette:geoPanel")• [Palette:gestureCapture ](<./Palette-gestureCapture.md> "Palette:gestureCapture")• [Palette:graphPlot ](<./Palette-graphPlot.md> "Palette:graphPlot")• [Palette:histogram ](<./Palette-histogram.md> "Palette:histogram")• [Palette:hsvBlur ](<./Palette-hsvBlur.md> "Palette:hsvBlur")• [Palette:imageSearch ](<./Palette-imageSearch.md> "Palette:imageSearch")• [Palette:julia ](<./Palette-julia.md> "Palette:julia")• [Palette:kantanMapper ](<./Palette-kantanMapper.md> "Palette:kantanMapper")• [Palette:kinectCalibration ](<./Palette-kinectCalibration.md> "Palette:kinectCalibration")• [Palette:kinectPointcloud ](<./Palette-kinectPointcloud.md> "Palette:kinectPointcloud")• [Palette:leapPaint ](<./Palette-leapPaint.md> "Palette:leapPaint")• [Palette:lightTunnel ](<./Palette-lightTunnel.md> "Palette:lightTunnel")• [Palette:logger ](<./Palette-logger.md> "Palette:logger")• [Experimental:Palette:logger ](</Experimental:Palette:logger> "Experimental:Palette:logger")• [Palette:mandelbrot ](<./Palette-mandelbrot.md> "Palette:mandelbrot")• [Palette:materialDesignIcons ](<./Palette-materialDesignIcons.md> "Palette:materialDesignIcons")• [Palette:mesh ](<./Palette-mesh.md> "Palette:mesh")• [Palette:monochrome ](<./Palette-monochrome.md> "Palette:monochrome")• [Palette:motionSense ](<./Palette-motionSense.md> "Palette:motionSense")• [Palette:movieEngine ](<./Palette-movieEngine.md> "Palette:movieEngine")• [Palette:moviePlayer ](<./Palette-moviePlayer.md> "Palette:moviePlayer")• [Palette:moviePlaylist ](<./Palette-moviePlaylist.md> "Palette:moviePlaylist")• [Palette:multiLevel ](<./Palette-multiLevel.md> "Palette:multiLevel")• [Palette:multiMix ](<./Palette-multiMix.md> "Palette:multiMix")• [Palette:noise ](<./Palette-noise.md> "Palette:noise")• [Palette:onScreenKeyboard ](<./Palette-onScreenKeyboard.md> "Palette:onScreenKeyboard")• [Palette:operatorPath ](<./Palette-operatorPath.md> "Palette:operatorPath")• [Palette:opticalFlow ](<./Palette-opticalFlow.md> "Palette:opticalFlow")• [Palette:particlesGpu ](<./Palette-particlesGpu.md> "Palette:particlesGpu")• [Palette:pixelate ](<./Palette-pixelate.md> "Palette:pixelate")• [Palette:pixelRelocator ](<./Palette-pixelRelocator.md> "Palette:pixelRelocator")• [Palette:pointGenerator ](<./Palette-pointGenerator.md> "Palette:pointGenerator")• [Palette:pointillize ](<./Palette-pointillize.md> "Palette:pointillize")• [Palette:pointMerge ](<./Palette-pointMerge.md> "Palette:pointMerge")• [Palette:pointRender ](<./Palette-pointRender.md> "Palette:pointRender")• [Palette:pointRepack ](<./Palette-pointRepack.md> "Palette:pointRepack")• [Palette:pointTransform ](<./Palette-pointTransform.md> "Palette:pointTransform")• [Palette:pointWeight ](<./Palette-pointWeight.md> "Palette:pointWeight")• [Palette:popDialog ](<./Palette-popDialog.md> "Palette:popDialog")• [Experimental:Palette:popDialog ](</Experimental:Palette:popDialog> "Experimental:Palette:popDialog")• [Palette:probe ](<./Palette-probe.md> "Palette:probe")• [Palette:projectorBlend ](<./Palette-projectorBlend.md> "Palette:projectorBlend")• [Palette:pushPins ](<./Palette-pushPins.md> "Palette:pushPins")• [Palette:puzzle ](<./Palette-puzzle.md> "Palette:puzzle")• [Palette:quadReproject ](<./Palette-quadReproject.md> "Palette:quadReproject")• [Palette:radialBlur ](<./Palette-radialBlur.md> "Palette:radialBlur")• [Palette:recorder ](<./Palette-recorder.md> "Palette:recorder")• [Experimental:Palette:recorder ](</Experimental:Palette:recorder> "Experimental:Palette:recorder")• [Palette:remotePanel ](<./Palette-remotePanel.md> "Palette:remotePanel")• [Palette:rgbaBlur ](<./Palette-rgbaBlur.md> "Palette:rgbaBlur")• [Palette:rgbaDelay ](<./Palette-rgbaDelay.md> "Palette:rgbaDelay")• [Palette:rgbContrast ](<./Palette-rgbContrast.md> "Palette:rgbContrast")• [Palette:sceneChanger ](<./Palette-sceneChanger.md> "Palette:sceneChanger")• [Palette:search ](<./Palette-search.md> "Palette:search")• [Palette:searchReplace ](<./Palette-searchReplace.md> "Palette:searchReplace")• [Palette:sharpen ](<./Palette-sharpen.md> "Palette:sharpen")• [Palette:sickEngine ](<./Palette-sickEngine.md> "Palette:sickEngine")• [Palette:signalingClient ](<./Palette-signalingClient.md> "Palette:signalingClient")• [Palette:signalingServer ](<./Palette-signalingServer.md> "Palette:signalingServer")• [Palette:softenAlpha ](<./Palette-softenAlpha.md> "Palette:softenAlpha")• [Palette:solarize ](<./Palette-solarize.md> "Palette:solarize")• [Palette:sopRender ](<./Palette-sopRender.md> "Palette:sopRender")• [Palette:splitter ](<./Palette-splitter.md> "Palette:splitter")• [Palette:stitcher ](<./Palette-stitcher.md> "Palette:stitcher")• [Palette:stoner ](<./Palette-stoner.md> "Palette:stoner")• [Palette:superFormula ](<./Palette-superFormula.md> "Palette:superFormula")• [Palette:SVG ](<./Palette-SVG.md> "Palette:SVG")• [Palette:sweetSpot ](<./Palette-sweetSpot.md> "Palette:sweetSpot")• [Palette:sweetSpotPreviz ](<./Palette-sweetSpotPreviz.md> "Palette:sweetSpotPreviz")• [Palette:synchroCache ](<./Palette-synchroCache.md> "Palette:synchroCache")• [Palette:synchroClient ](<./Palette-synchroClient.md> "Palette:synchroClient")• [Palette:synchroFrameIn ](<./Palette-synchroFrameIn.md> "Palette:synchroFrameIn")• [Palette:synchroFrameOut ](<./Palette-synchroFrameOut.md> "Palette:synchroFrameOut")• [Palette:synchroNDIIn ](<./Palette-synchroNDIIn.md> "Palette:synchroNDIIn")• [Palette:synchroSDIIn ](<./Palette-synchroSDIIn.md> "Palette:synchroSDIIn")• [Palette:synchroVideoOut ](<./Palette-synchroVideoOut.md> "Palette:synchroVideoOut")• [Palette:tdBitwigPackage ](<./Palette-tdBitwigPackage.md> "Palette:tdBitwigPackage")• [Experimental:Palette:tdPyEnvManager ](</Experimental:Palette:tdPyEnvManager> "Experimental:Palette:tdPyEnvManager")• [Palette:TDVR ](<./Palette-TDVR.md> "Palette:TDVR")• [Palette:testGrid ](<./Palette-testGrid.md> "Palette:testGrid")• [Experimental:Palette:threadManagerClient ](</Experimental:Palette:threadManagerClient> "Experimental:Palette:threadManagerClient")• [Experimental:Palette:threadsMonitor ](</Experimental:Palette:threadsMonitor> "Experimental:Palette:threadsMonitor")• [Palette:transitMap ](<./Palette-transitMap.md> "Palette:transitMap")• [Palette:twirl ](<./Palette-twirl.md> "Palette:twirl")• [Palette:vectorScope ](<./Palette-vectorScope.md> "Palette:vectorScope")• [Palette:virtualFile ](<./Palette-virtualFile.md> "Palette:virtualFile")• [Palette:waveformMonitor ](<./Palette-waveformMonitor.md> "Palette:waveformMonitor")• [Palette:webBrowser ](<./Palette-webBrowser.md> "Palette:webBrowser")• [Palette:webRTC ](<./Palette-webRTC.md> "Palette:webRTC")• [Palette:webRTCPanel ](<./Palette-webRTCPanel.md> "Palette:webRTCPanel")• [Palette:webRTCPanelRcv ](<./Palette-webRTCPanelRcv.md> "Palette:webRTCPanelRcv")• [Palette:xyScope ](<./Palette-xyScope.md> "Palette:xyScope")• [Experimental:Thread Manager ](</Experimental:Thread_Manager> "Experimental:Thread Manager")
