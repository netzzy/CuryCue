# Palette:bloom

##   
  
Summary

The Bloom COMP is a combination of several image effects that selects and remap the brightest pixels of a TOP. The pixels in the second input TOP are warped around the selection defined by the blur parameters.  
  
The blur parameters modifies the selection of the brightest pixels of the input 1 TOP. For example increasing the “Contrast” parameter would reshape the selection to narrow the range of brightness, selecting the brightest pixels. The glow parameters overlays the pixels selected in the blur parameters with the RGB values selected by the “Glow Color” parameters.   
  
A [Ramp TOP](<./Ramp_TOP.md> "Ramp TOP") with a color spectrum is the default second input for this COMP. The ramp can be replaced by attaching a TOP to the second input of the component, or the built-one ramp can be edited with the Open Ramp Parameters pulse. 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[Palette:bloom Ext](</index.php?title=Palette:bloom_Ext&action=edit&redlink=1> "Palette:bloom Ext \(page does not exist\)")

## 

Parameters - Bloom Page

Help`Help`\- Opens this page. 

Version`Version`\- Current version of this COMP. 

Blur Size`Blursize`\- The amount of blur in pixels. 

Iterations`Iterations`\- The number of times the filter is iterated. 

Threshold`Threshold`\- Controls the darkest pixels in the TOP, any pixel with a value less than or equal to this will be faded out. 

Intensity`Intensity`\- Increases or decreases the brightness of an image. Brightness can be considered the arithmetic mean of the RGB channels. The Brightness parameter adds or subtracts an offset into the R, G, and B channels. Low brightness will result in dark tones, while high brightness will wash the color out towards white. 

Gamma`Gamma`\- The Gamma parameter applies a gamma correction to the image. Gamma is the relationship between the brightness of a pixel as it appears on the screen, and the numerical value of that pixel. This is often represented by a gamma curve. The difference between brightness and gamma is that gamma also affects the ratio of red to green to blue. A straight, linear gamma curve with a value of 1 means no change. 

Contrast`Contrast`\- Contrast applies a scale factor (gain) to the RGB channels. Increasing contrast will brighten the light areas and darken the dark areas of the image, making the difference between the light and dark areas of the image stronger. 

Bloom Level`Bloom`\- Intensity of the Bloom effect. 

Glow Level`Glow`\- Controls the intensity of the overlay in the “Glow Color” parameter. 

Glow Color`Glowcolor`\- ⊞ \- Overlays the value selected in the RGB parameters on the brightest pixels of the TOP. 
* Glow Color`Glowcolorr`\- Sets the red color channel.
* Glow Color`Glowcolorg`\- Sets the green color channel.
* Glow Color`Glowcolorb`\- Sets the blue color channel.


Ramp Glow Level`Glowinputramp`\- Controls the ramp’s glow intensity. 

Open Ramp Parameters`Openramp`\- Opens the ramp's parameters. 

Input Level (Mix Out)`Inputlevel`\- Controls the opacity of the input TOP. 

Blur Type`Blurtype`\- ⊞ \- Determines the mathematical function used to create the blur. 
* Catmull-Rom`catmull`\- A spline approximation to a Gaussian kernel. Gives sharper textures and more accurate edges.
* Gaussian`gaussian`\- A normal distribution where pixels at the center have more effect on the resulting pixel. Gaussian lacks sharpness but handles ringing and aliasing well.
* Box`box`\- Each pixel within the box is weighted evenly. Inexpensive and gives a "boxy" look.
* Bartlette`bartlette`\- A triangle filter. The weight of each pixel is a linear function of its distance from the center.
* Sinc`sinc`\- A sharpening filter. Some pixels contribute a negative weight to the result, artifacts may occur in the form of "ringing". Keeps small details and edges better than Gaussian.
* Hanning`hanning`\- A cosine approximation to a Gaussian kernel.
* Blackman`blackman`\- A higher order cosine approximation to a Gaussian kernel.


Pre-Shrink`Preshrink`\- Reduces the image's resolution before applying the blur. 

Sample Step`Samplestep`\- When sampling the image, this determines the distance from each pixel to the sample pixel. When units are set to pixels, it is the number of pixels away from the current pixel which is sampled to blur the image. A Sample Step of 3 would sample pixels 3 pixels away. 

Temporal Smooth`Temporalsmooth`\- Controls the amount of motion blur per frame. 

Input Filter Type`Inputfiltertype`\- ⊞ \- This controls pixel filtering on the input image of the TOP. 
* Nearest Pixel`nearest`\- Uses nearest pixel or accurate image representation. Images will look jaggy when viewing at any zoom level other than Native Resolution.
* Interpolate Pixels`linear`\- Uses linear filtering between pixels. This is how you get TOP images in viewers to look good at various zoom levels, especially useful when using any Fill Viewer setting other than Native Resolution.
* Mipmap Pixels`mipmap`\- Uses [mipmap](<./Mipmapping.md>) filtering when scaling images. This can be used to reduce artifacts and sparkling in moving/scaling images that have lots of detail.


Pixel Format`Format`\- ⊞ \- Format used to store data for each channel in the image (ie. R, G, B, and A). Refer to Pixel Formats for more information. 
* Use Input`useinput`\- Uses the input's pixel format.
* 11-bit float (RGB), Positive Values Only`rgba11float`\- A RGB floating point format that has 11 bits for the Red and Green channels, and 10-bits for the Blue Channel, 32-bits total per pixel (therefore the same memory usage as 8-bit RGBA). The Alpha channel in this format will always be 1. Values can go above one, but can't be negative. ie. the range is [0, infinite).
* 16-bit float (RGB)`rgb16float`-
* 32-bit float (RGB)`rgb32float`-

## 

Operator Inputs
* Input 0: in1 -
  * Input 1: in2 -

## 

Operator Outputs
* Output 0 -


TouchDesigner Build: Latest\n2021.100002018.28070before 2018.28070

Palette  
---  
[Palette ](<./Palette.md> "Palette")• [Palette:arcBallCamera ](<./Palette-arcBallCamera.md> "Palette:arcBallCamera")• [Palette:arcBallGeometry ](<./Palette-arcBallGeometry.md> "Palette:arcBallGeometry")• [Palette:audioAnalysis ](<./Palette-audioAnalysis.md> "Palette:audioAnalysis")• [Palette:audioSet ](<./Palette-audioSet.md> "Palette:audioSet")• [Palette:autoMediaPlayer ](<./Palette-autoMediaPlayer.md> "Palette:autoMediaPlayer")• [Palette:battery ](<./Palette-battery.md> "Palette:battery")• [Palette:bitwigClip ](<./Palette-bitwigClip.md> "Palette:bitwigClip")• [Palette:bitwigClipSlot ](<./Palette-bitwigClipSlot.md> "Palette:bitwigClipSlot")• [Palette:bitwigDeviceRemotes ](<./Palette-bitwigDeviceRemotes.md> "Palette:bitwigDeviceRemotes")• [Palette:bitwigMain ](<./Palette-bitwigMain.md> "Palette:bitwigMain")• [Palette:bitwigNote ](<./Palette-bitwigNote.md> "Palette:bitwigNote")• [Palette:bitwigProjectRemotes ](<./Palette-bitwigProjectRemotes.md> "Palette:bitwigProjectRemotes")• [Palette:bitwigRemotesDevice ](<./Palette-bitwigRemotesDevice.md> "Palette:bitwigRemotesDevice")• [Palette:bitwigRemotesProject ](<./Palette-bitwigRemotesProject.md> "Palette:bitwigRemotesProject")• [Palette:bitwigRemotesTrack ](<./Palette-bitwigRemotesTrack.md> "Palette:bitwigRemotesTrack")• [Palette:bitwigSelect ](<./Palette-bitwigSelect.md> "Palette:bitwigSelect")• [Palette:bitwigSong ](<./Palette-bitwigSong.md> "Palette:bitwigSong")• [Palette:bitwigTrack ](<./Palette-bitwigTrack.md> "Palette:bitwigTrack")• [Palette:bitwigTrackRemotes ](<./Palette-bitwigTrackRemotes.md> "Palette:bitwigTrackRemotes")• [Palette:blendModes ](<./Palette-blendModes.md> "Palette:blendModes")• Palette:bloom • [Palette:camera ](<./Palette-camera.md> "Palette:camera")• [Palette:cameraBrowser ](<./Palette-cameraBrowser.md> "Palette:cameraBrowser")• [Palette:cameraViewport ](<./Palette-cameraViewport.md> "Palette:cameraViewport")• [Palette:camSchnappr ](<./Palette-camSchnappr.md> "Palette:camSchnappr")• [Palette:changeColor ](<./Palette-changeColor.md> "Palette:changeColor")• [Palette:changeToColor ](<./Palette-changeToColor.md> "Palette:changeToColor")• [Palette:checker ](<./Palette-checker.md> "Palette:checker")• [Palette:chromaKey ](<./Palette-chromaKey.md> "Palette:chromaKey")• [Palette:colorThreshold ](<./Palette-colorThreshold.md> "Palette:colorThreshold")• [Palette:compareComp ](<./Palette-compareComp.md> "Palette:compareComp")• [Palette:convolve ](<./Palette-convolve.md> "Palette:convolve")• [Experimental:Palette:cornerPinPOP ](</index.php?title=Experimental:Palette:cornerPinPOP&action=edit&redlink=1> "Experimental:Palette:cornerPinPOP \(page does not exist\)")• [Palette:cornerPinSOP ](<./Palette-cornerPinSOP.md> "Palette:cornerPinSOP")• [Palette:cppParsTemplateGen ](<./Palette-cppParsTemplateGen.md> "Palette:cppParsTemplateGen")• [Palette:customAttributes ](<./Palette-customAttributes.md> "Palette:customAttributes")• [Palette:debugControl ](<./Palette-debugControl.md> "Palette:debugControl")• [Palette:dent ](<./Palette-dent.md> "Palette:dent")• [Palette:depthExtract ](<./Palette-depthExtract.md> "Palette:depthExtract")• [Palette:depthProjection ](<./Palette-depthProjection.md> "Palette:depthProjection")• [Palette:dilate ](<./Palette-dilate.md> "Palette:dilate")• [Experimental:Palette:domeViewer ](</index.php?title=Experimental:Palette:domeViewer&action=edit&redlink=1> "Experimental:Palette:domeViewer \(page does not exist\)")• [Palette:encoder ](<./Palette-encoder.md> "Palette:encoder")• [Palette:equalizer ](<./Palette-equalizer.md> "Palette:equalizer")• [Palette:feedback ](<./Palette-feedback.md> "Palette:feedback")• [Palette:feedbackEdge ](<./Palette-feedbackEdge.md> "Palette:feedbackEdge")• [Palette:firmata ](<./Palette-firmata.md> "Palette:firmata")• [Palette:gal ](<./Palette-gal.md> "Palette:gal")• [Palette:geoPanel ](<./Palette-geoPanel.md> "Palette:geoPanel")• [Palette:gestureCapture ](<./Palette-gestureCapture.md> "Palette:gestureCapture")• [Palette:graphPlot ](<./Palette-graphPlot.md> "Palette:graphPlot")• [Palette:histogram ](<./Palette-histogram.md> "Palette:histogram")• [Palette:hsvBlur ](<./Palette-hsvBlur.md> "Palette:hsvBlur")• [Palette:imageSearch ](<./Palette-imageSearch.md> "Palette:imageSearch")• [Palette:julia ](<./Palette-julia.md> "Palette:julia")• [Palette:kantanMapper ](<./Palette-kantanMapper.md> "Palette:kantanMapper")• [Palette:kinectCalibration ](<./Palette-kinectCalibration.md> "Palette:kinectCalibration")• [Palette:kinectPointcloud ](<./Palette-kinectPointcloud.md> "Palette:kinectPointcloud")• [Palette:leapPaint ](<./Palette-leapPaint.md> "Palette:leapPaint")• [Palette:lightTunnel ](<./Palette-lightTunnel.md> "Palette:lightTunnel")• [Palette:logger ](<./Palette-logger.md> "Palette:logger")• [Experimental:Palette:logger ](</index.php?title=Experimental:Palette:logger&action=edit&redlink=1> "Experimental:Palette:logger \(page does not exist\)")• [Palette:mandelbrot ](<./Palette-mandelbrot.md> "Palette:mandelbrot")• [Palette:materialDesignIcons ](<./Palette-materialDesignIcons.md> "Palette:materialDesignIcons")• [Palette:mesh ](<./Palette-mesh.md> "Palette:mesh")• [Palette:monochrome ](<./Palette-monochrome.md> "Palette:monochrome")• [Palette:motionSense ](<./Palette-motionSense.md> "Palette:motionSense")• [Palette:movieEngine ](<./Palette-movieEngine.md> "Palette:movieEngine")• [Palette:moviePlayer ](<./Palette-moviePlayer.md> "Palette:moviePlayer")• [Palette:moviePlaylist ](<./Palette-moviePlaylist.md> "Palette:moviePlaylist")• [Palette:multiLevel ](<./Palette-multiLevel.md> "Palette:multiLevel")• [Palette:multiMix ](<./Palette-multiMix.md> "Palette:multiMix")• [Palette:noise ](<./Palette-noise.md> "Palette:noise")• [Palette:onScreenKeyboard ](<./Palette-onScreenKeyboard.md> "Palette:onScreenKeyboard")• [Palette:operatorPath ](<./Palette-operatorPath.md> "Palette:operatorPath")• [Palette:opticalFlow ](<./Palette-opticalFlow.md> "Palette:opticalFlow")• [Palette:particlesGpu ](<./Palette-particlesGpu.md> "Palette:particlesGpu")• [Palette:pixelate ](<./Palette-pixelate.md> "Palette:pixelate")• [Palette:pixelRelocator ](<./Palette-pixelRelocator.md> "Palette:pixelRelocator")• [Palette:pointGenerator ](<./Palette-pointGenerator.md> "Palette:pointGenerator")• [Palette:pointillize ](<./Palette-pointillize.md> "Palette:pointillize")• [Palette:pointMerge ](<./Palette-pointMerge.md> "Palette:pointMerge")• [Palette:pointRender ](<./Palette-pointRender.md> "Palette:pointRender")• [Palette:pointRepack ](<./Palette-pointRepack.md> "Palette:pointRepack")• [Palette:pointTransform ](<./Palette-pointTransform.md> "Palette:pointTransform")• [Palette:pointWeight ](<./Palette-pointWeight.md> "Palette:pointWeight")• [Palette:popDialog ](<./Palette-popDialog.md> "Palette:popDialog")• [Experimental:Palette:popDialog ](</index.php?title=Experimental:Palette:popDialog&action=edit&redlink=1> "Experimental:Palette:popDialog \(page does not exist\)")• [Palette:probe ](<./Palette-probe.md> "Palette:probe")• [Palette:projectorBlend ](<./Palette-projectorBlend.md> "Palette:projectorBlend")• [Palette:pushPins ](<./Palette-pushPins.md> "Palette:pushPins")• [Palette:puzzle ](<./Palette-puzzle.md> "Palette:puzzle")• [Palette:quadReproject ](<./Palette-quadReproject.md> "Palette:quadReproject")• [Palette:radialBlur ](<./Palette-radialBlur.md> "Palette:radialBlur")• [Palette:recorder ](<./Palette-recorder.md> "Palette:recorder")• [Experimental:Palette:recorder ](</index.php?title=Experimental:Palette:recorder&action=edit&redlink=1> "Experimental:Palette:recorder \(page does not exist\)")• [Palette:remotePanel ](<./Palette-remotePanel.md> "Palette:remotePanel")• [Palette:rgbaBlur ](<./Palette-rgbaBlur.md> "Palette:rgbaBlur")• [Palette:rgbaDelay ](<./Palette-rgbaDelay.md> "Palette:rgbaDelay")• [Palette:rgbContrast ](<./Palette-rgbContrast.md> "Palette:rgbContrast")• [Palette:sceneChanger ](<./Palette-sceneChanger.md> "Palette:sceneChanger")• [Palette:search ](<./Palette-search.md> "Palette:search")• [Palette:searchReplace ](<./Palette-searchReplace.md> "Palette:searchReplace")• [Palette:sharpen ](<./Palette-sharpen.md> "Palette:sharpen")• [Palette:sickEngine ](<./Palette-sickEngine.md> "Palette:sickEngine")• [Palette:signalingClient ](<./Palette-signalingClient.md> "Palette:signalingClient")• [Palette:signalingServer ](<./Palette-signalingServer.md> "Palette:signalingServer")• [Palette:softenAlpha ](<./Palette-softenAlpha.md> "Palette:softenAlpha")• [Palette:solarize ](<./Palette-solarize.md> "Palette:solarize")• [Palette:sopRender ](<./Palette-sopRender.md> "Palette:sopRender")• [Palette:splitter ](<./Palette-splitter.md> "Palette:splitter")• [Palette:stitcher ](<./Palette-stitcher.md> "Palette:stitcher")• [Palette:stoner ](<./Palette-stoner.md> "Palette:stoner")• [Palette:superFormula ](<./Palette-superFormula.md> "Palette:superFormula")• [Palette:SVG ](<./Palette-SVG.md> "Palette:SVG")• [Palette:sweetSpot ](<./Palette-sweetSpot.md> "Palette:sweetSpot")• [Palette:sweetSpotPreviz ](<./Palette-sweetSpotPreviz.md> "Palette:sweetSpotPreviz")• [Palette:synchroCache ](<./Palette-synchroCache.md> "Palette:synchroCache")• [Palette:synchroClient ](<./Palette-synchroClient.md> "Palette:synchroClient")• [Palette:synchroFrameIn ](<./Palette-synchroFrameIn.md> "Palette:synchroFrameIn")• [Palette:synchroFrameOut ](<./Palette-synchroFrameOut.md> "Palette:synchroFrameOut")• [Palette:synchroNDIIn ](<./Palette-synchroNDIIn.md> "Palette:synchroNDIIn")• [Palette:synchroSDIIn ](<./Palette-synchroSDIIn.md> "Palette:synchroSDIIn")• [Palette:synchroVideoOut ](<./Palette-synchroVideoOut.md> "Palette:synchroVideoOut")• [Palette:tdBitwigPackage ](<./Palette-tdBitwigPackage.md> "Palette:tdBitwigPackage")• [Experimental:Palette:tdPyEnvManager ](</index.php?title=Experimental:Palette:tdPyEnvManager&action=edit&redlink=1> "Experimental:Palette:tdPyEnvManager \(page does not exist\)")• [Palette:TDVR ](<./Palette-TDVR.md> "Palette:TDVR")• [Palette:testGrid ](<./Palette-testGrid.md> "Palette:testGrid")• [Experimental:Palette:threadManagerClient ](</index.php?title=Experimental:Palette:threadManagerClient&action=edit&redlink=1> "Experimental:Palette:threadManagerClient \(page does not exist\)")• [Experimental:Palette:threadsMonitor ](</index.php?title=Experimental:Palette:threadsMonitor&action=edit&redlink=1> "Experimental:Palette:threadsMonitor \(page does not exist\)")• [Palette:transitMap ](<./Palette-transitMap.md> "Palette:transitMap")• [Palette:twirl ](<./Palette-twirl.md> "Palette:twirl")• [Palette:vectorScope ](<./Palette-vectorScope.md> "Palette:vectorScope")• [Palette:virtualFile ](<./Palette-virtualFile.md> "Palette:virtualFile")• [Palette:waveformMonitor ](<./Palette-waveformMonitor.md> "Palette:waveformMonitor")• [Palette:webBrowser ](<./Palette-webBrowser.md> "Palette:webBrowser")• [Palette:webRTC ](<./Palette-webRTC.md> "Palette:webRTC")• [Palette:webRTCPanel ](<./Palette-webRTCPanel.md> "Palette:webRTCPanel")• [Palette:webRTCPanelRcv ](<./Palette-webRTCPanelRcv.md> "Palette:webRTCPanelRcv")• [Palette:xyScope ](<./Palette-xyScope.md> "Palette:xyScope")• [Experimental:Thread Manager ](</index.php?title=Experimental:Thread_Manager&action=edit&redlink=1> "Experimental:Thread Manager \(page does not exist\)")
