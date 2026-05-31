# Palette:projectorBlend

## 

Summary

ProjectorBlend is a tool to smoothly blend projector arrays based on the ofxProjectorBlend add-on by Jeffrey Crouse ([ofxProjectorBlend on GitHub](<https://github.com/Flightphase/ofxProjectorBlend>)) 

On a technical level it incorporates Paul Bourkes [Edge blending using commodity projectors](<http://paulbourke.net/texture_colour/edgeblend/>) paper. 

See also [Projection Mapping](<./Projection_Mapping.md> "Projection Mapping"), [Vioso](<./Vioso.md> "Vioso"), [Scalable Displays](<./Scalable_Display_TOP.md> "Scalable Display TOP"), [kantanMapper](<./Palette-kantanMapper.md> "Palette:kantanMapper"), [camSchnappr](<./Palette-camSchnappr.md> "Palette:camSchnappr"). 

## Usage

ProjectorBlend will take any input and stretch it to the projector array size. The output is blended but - depending on your hardware setup - might need to be rearranged for output to the projectors. 

The parameters on the Projector Blend page are used for setting up a general environment, how many projectors are being used and what each projectors resolution is (all projectors need to be the same resolution). Also an overall blankout area around the projection can be specified. 

Separate parameters per projector can be set on the Projector Parameter pages. Here the blend-area can be specified as well as the parameters dictating the blends general behavior. If necessary there is the option to switch to a "per side control" which enables non-straight blending areas and separate color control of each projector edge. 

### Parameters - Projector Blend Page

Projector Array`Projectorarray1 / Projectorarray2`\- Specify the size of your projector array in x and y. A 1x2 array would mean you have 2 projectors aligned vertically. Changing this parameter will add or remove additional parameter pages for all projectors. 

Projector Resolution`Projectorres1 / Projectorres2`\- Specify the individual projector resolution in pixels. 

Blankout Edges`Blankout1 / Blankout2 / Blankout3 / Blankout4`\- Specify the size of the blank-out on all sides of the projection area in pixels. 

Solid Edge`Solidedge`\- Draws the blend area as a solid color. 

Solid Edge Color`Solidedgecolorr / Solidedgecolorg / Solidedgecolorb`\- Specify the Solid Edge Color. 

### Parameters - Projector[1-x] Page

Blankout`Projector[1-x]blankout1 / Projector[1-x]blankout2 / Projector[1-x]blankout3 / Projector[1-x]blankout4`\- Specify the Left, Right, Bottom and Top blank-out area of the projector in pixels. 

Overlap`Projector[1-x]overlap1 / Projector[1-x]overlap2 / Projector[1-x]overlap3 / Projector[1-x]overlap4`\- Specify the Left, Right, Bottom and Top blend area of the projector in pixels. 

Blend`Projector[1-x]blend`\- Adjust the blend stength. 

Luminance`Projector[1-x]luminance`\- Adjust the luminance of the blend area. 

Gamma`Projector[1-x]gamma1 / Projector[1-x]gamma2 / Projector[1-x]gamma3`\- Adjust the RGB gamma levels of the blend area. 

Hue Adjust RGB`Projector[1-x]hue1 / Projector[1-x]hue2 / Projector[1-x]hue3`\- Adjust the hue of the projector. 

Saturation Adjust RGB`Projector[1-x]sat1 / Projector[1-x]sat2 / Projector[1-x]sat3`\- Adjust the saturation of the projector. 

Value Adjust RGB`Projector[1-x]val1 / Projector[1-x]val2 / Projector[1-x]val3`\- Adjust the value of the projector. 

Per Side Control`Projector[1-x]perside`\- Enable separate blending controls for individual projector sides. 

Blankout Left / Right / Top / Bottom`Projector[1-x]pos[0-3]c01 / Projector[1-x]pos[0-3]c02`\- Set the size of the blank-out area per projector side. There are 2 parameters you can adjust for not fully horizontal or vertical blending areas. 

Overlap Left / Right / Top / Bottom`Projector[1-x]pos[0-3]c11 / Projector[1-x]pos[0-3]c12`\- Set the size of the blend area per projector side. There are 2 parameters you can adjust for not fully horizontal or vertical blending areas. 

Blend Left / Right / Top / Bottom`Projector[1-x]blends[0-3]`\- Adjust the blend strength per projector side. 

Luminance Left / Right / Top / Bottom`Projector[1-x]luminance[0-3]`\- Adjust the luminance level of the blend area per projector side. 

Gamma Left / Right / Top / Bottom`Projector[1-x]gammas[0-3]1 / Projector[1-x]gammas[0-3]2 / Projector[1-x]gammas[0-3]3`\- Adjust the RGB gamma levels of the blend area per projector side. 

## Creating Blend Masks for single Projectors

If it is desired to just create blending masks which can be multiplied with single parts of the output to projectors, set the Projector Array parameter to 1x1 and enable the Per Side Control parameter on the Projector1 page. 

This will allow to set each side of the blend mask individually. The output can be saved or locked to prevent any further cooking of the projectorBlend component. 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[Palette:projectorBlend Ext](</index.php?title=Palette:projectorBlend_Ext&action=edit&redlink=1> "Palette:projectorBlend Ext \(page does not exist\)")

## 

Parameters - Projector Blend Page

Help`Help`\- 

Version`Version`\- 

Projector Array`Projectorarray`\- ⊞ \- 
* Projector Array`Projectorarray1`-
* Projector Array`Projectorarray2`-


Projector Resolution`Projectorres`\- ⊞ \- 
* Projector Resolution`Projectorres1`-
* Projector Resolution`Projectorres2`-


Blankout Edges`Blankout`\- ⊞ \- 
* Blankout Edges`Blankout1`-
* Blankout Edges`Blankout2`-
* Blankout Edges`Blankout3`-
* Blankout Edges`Blankout4`-


Solid Edge`Solidedge`\- 

Solid Edge Color`Solidedgecolor`\- ⊞ \- 
* Solid Edge Color`Solidedgecolorr`-
* Solid Edge Color`Solidedgecolorg`-
* Solid Edge Color`Solidedgecolorb`-

## 

Parameters - Projector1 Page

Blankout`Projector1blankout`\- ⊞ \- 
* Blankout`Projector1blankout1`-
* Blankout`Projector1blankout2`-
* Blankout`Projector1blankout3`-
* Blankout`Projector1blankout4`-


Overlap`Projector1overlap`\- ⊞ \- 
* Overlap`Projector1overlap1`-
* Overlap`Projector1overlap2`-
* Overlap`Projector1overlap3`-
* Overlap`Projector1overlap4`-


Blend`Projector1blend`\- 

Luminance`Projector1luminance`\- 

Gamma`Projector1gamma`\- ⊞ \- 
* Gamma`Projector1gamma1`-
* Gamma`Projector1gamma2`-
* Gamma`Projector1gamma3`-


Hue Adjust RGB`Projector1hue`\- ⊞ \- 
* Hue Adjust RGB`Projector1hue1`-
* Hue Adjust RGB`Projector1hue2`-
* Hue Adjust RGB`Projector1hue3`-


Saturation Adjust RGB`Projector1sat`\- ⊞ \- 
* Saturation Adjust RGB`Projector1sat1`-
* Saturation Adjust RGB`Projector1sat2`-
* Saturation Adjust RGB`Projector1sat3`-


Value Adjust RGB`Projector1val`\- ⊞ \- 
* Value Adjust RGB`Projector1val1`-
* Value Adjust RGB`Projector1val2`-
* Value Adjust RGB`Projector1val3`-


Per Side Control`Projector1perside`\- 

Blankout Left`Projector1pos0c0`\- ⊞ \- 
* Blankout Left`Projector1pos0c01`-
* Blankout Left`Projector1pos0c02`-


Overlap Left`Projector1pos0c1`\- ⊞ \- 
* Overlap Left`Projector1pos0c11`-
* Overlap Left`Projector1pos0c12`-


Blend Left`Projector1blends0`\- 

Luminance Left`Projector1luminances0`\- 

Gamma Left`Projector1gammas0`\- ⊞ \- 
* Gamma Left`Projector1gammas01`-
* Gamma Left`Projector1gammas02`-
* Gamma Left`Projector1gammas03`-


Blankout Right`Projector1pos1c0`\- ⊞ \- 
* Blankout Right`Projector1pos1c01`-
* Blankout Right`Projector1pos1c02`-


Overlap Right`Projector1pos1c1`\- ⊞ \- 
* Overlap Right`Projector1pos1c11`-
* Overlap Right`Projector1pos1c12`-


Blend Right`Projector1blends1`\- 

Luminance Right`Projector1luminances1`\- 

Gamma Right`Projector1gammas1`\- ⊞ \- 
* Gamma Right`Projector1gammas11`-
* Gamma Right`Projector1gammas12`-
* Gamma Right`Projector1gammas13`-


Blankout Top`Projector1pos2c0`\- ⊞ \- 
* Blankout Top`Projector1pos2c01`-
* Blankout Top`Projector1pos2c02`-


Overlap Top`Projector1pos2c1`\- ⊞ \- 
* Overlap Top`Projector1pos2c11`-
* Overlap Top`Projector1pos2c12`-


Blend Top`Projector1blends2`\- 

Luminance Top`Projector1luminances2`\- 

Gamma Top`Projector1gammas2`\- ⊞ \- 
* Gamma Top`Projector1gammas21`-
* Gamma Top`Projector1gammas22`-
* Gamma Top`Projector1gammas23`-


Blankout Bottom`Projector1pos3c0`\- ⊞ \- 
* Blankout Bottom`Projector1pos3c01`-
* Blankout Bottom`Projector1pos3c02`-


Overlap Bottom`Projector1pos3c1`\- ⊞ \- 
* Overlap Bottom`Projector1pos3c11`-
* Overlap Bottom`Projector1pos3c12`-


Blend Bottom`Projector1blends3`\- 

Luminance Bottom`Projector1luminances3`\- 

Gamma Bottom`Projector1gammas3`\- ⊞ \- 
* Gamma Bottom`Projector1gammas31`-
* Gamma Bottom`Projector1gammas32`-
* Gamma Bottom`Projector1gammas33`-

## 

Parameters - Projector2 Page

Blankout`Projector2blankout`\- ⊞ \- 
* Blankout`Projector2blankout1`-
* Blankout`Projector2blankout2`-
* Blankout`Projector2blankout3`-
* Blankout`Projector2blankout4`-


Overlap`Projector2overlap`\- ⊞ \- 
* Overlap`Projector2overlap1`-
* Overlap`Projector2overlap2`-
* Overlap`Projector2overlap3`-
* Overlap`Projector2overlap4`-


Blend`Projector2blend`\- 

Luminance`Projector2luminance`\- 

Gamma`Projector2gamma`\- ⊞ \- 
* Gamma`Projector2gamma1`-
* Gamma`Projector2gamma2`-
* Gamma`Projector2gamma3`-


Hue Adjust RGB`Projector2hue`\- ⊞ \- 
* Hue Adjust RGB`Projector2hue1`-
* Hue Adjust RGB`Projector2hue2`-
* Hue Adjust RGB`Projector2hue3`-


Saturation Adjust RGB`Projector2sat`\- ⊞ \- 
* Saturation Adjust RGB`Projector2sat1`-
* Saturation Adjust RGB`Projector2sat2`-
* Saturation Adjust RGB`Projector2sat3`-


Value Adjust RGB`Projector2val`\- ⊞ \- 
* Value Adjust RGB`Projector2val1`-
* Value Adjust RGB`Projector2val2`-
* Value Adjust RGB`Projector2val3`-


Per Side Control`Projector2perside`\- 

Blankout Left`Projector2pos0c0`\- ⊞ \- 
* Blankout Left`Projector2pos0c01`-
* Blankout Left`Projector2pos0c02`-


Overlap Left`Projector2pos0c1`\- ⊞ \- 
* Overlap Left`Projector2pos0c11`-
* Overlap Left`Projector2pos0c12`-


Blend Left`Projector2blends0`\- 

Luminance Left`Projector2luminances0`\- 

Gamma Left`Projector2gammas0`\- ⊞ \- 
* Gamma Left`Projector2gammas01`-
* Gamma Left`Projector2gammas02`-
* Gamma Left`Projector2gammas03`-


Blankout Right`Projector2pos1c0`\- ⊞ \- 
* Blankout Right`Projector2pos1c01`-
* Blankout Right`Projector2pos1c02`-


Overlap Right`Projector2pos1c1`\- ⊞ \- 
* Overlap Right`Projector2pos1c11`-
* Overlap Right`Projector2pos1c12`-


Blend Right`Projector2blends1`\- 

Luminance Right`Projector2luminances1`\- 

Gamma Right`Projector2gammas1`\- ⊞ \- 
* Gamma Right`Projector2gammas11`-
* Gamma Right`Projector2gammas12`-
* Gamma Right`Projector2gammas13`-


Blankout Top`Projector2pos2c0`\- ⊞ \- 
* Blankout Top`Projector2pos2c01`-
* Blankout Top`Projector2pos2c02`-


Overlap Top`Projector2pos2c1`\- ⊞ \- 
* Overlap Top`Projector2pos2c11`-
* Overlap Top`Projector2pos2c12`-


Blend Top`Projector2blends2`\- 

Luminance Top`Projector2luminances2`\- 

Gamma Top`Projector2gammas2`\- ⊞ \- 
* Gamma Top`Projector2gammas21`-
* Gamma Top`Projector2gammas22`-
* Gamma Top`Projector2gammas23`-


Blankout Bottom`Projector2pos3c0`\- ⊞ \- 
* Blankout Bottom`Projector2pos3c01`-
* Blankout Bottom`Projector2pos3c02`-


Overlap Bottom`Projector2pos3c1`\- ⊞ \- 
* Overlap Bottom`Projector2pos3c11`-
* Overlap Bottom`Projector2pos3c12`-


Blend Bottom`Projector2blends3`\- 

Luminance Bottom`Projector2luminances3`\- 

Gamma Bottom`Projector2gammas3`\- ⊞ \- 
* Gamma Bottom`Projector2gammas31`-
* Gamma Bottom`Projector2gammas32`-
* Gamma Bottom`Projector2gammas33`-

## 

Operator Inputs
* Input 0: in1 -

## 

Operator Outputs
* Output 0 -


TouchDesigner Build: Latest\n2021.100002018.28070

Palette  
---  
[Palette ](<./Palette.md> "Palette")• [Palette:arcBallCamera ](<./Palette-arcBallCamera.md> "Palette:arcBallCamera")• [Palette:arcBallGeometry ](<./Palette-arcBallGeometry.md> "Palette:arcBallGeometry")• [Palette:audioAnalysis ](<./Palette-audioAnalysis.md> "Palette:audioAnalysis")• [Palette:audioSet ](<./Palette-audioSet.md> "Palette:audioSet")• [Palette:autoMediaPlayer ](<./Palette-autoMediaPlayer.md> "Palette:autoMediaPlayer")• [Palette:battery ](<./Palette-battery.md> "Palette:battery")• [Palette:bitwigClip ](<./Palette-bitwigClip.md> "Palette:bitwigClip")• [Palette:bitwigClipSlot ](<./Palette-bitwigClipSlot.md> "Palette:bitwigClipSlot")• [Palette:bitwigDeviceRemotes ](<./Palette-bitwigDeviceRemotes.md> "Palette:bitwigDeviceRemotes")• [Palette:bitwigMain ](<./Palette-bitwigMain.md> "Palette:bitwigMain")• [Palette:bitwigNote ](<./Palette-bitwigNote.md> "Palette:bitwigNote")• [Palette:bitwigProjectRemotes ](<./Palette-bitwigProjectRemotes.md> "Palette:bitwigProjectRemotes")• [Palette:bitwigRemotesDevice ](<./Palette-bitwigRemotesDevice.md> "Palette:bitwigRemotesDevice")• [Palette:bitwigRemotesProject ](<./Palette-bitwigRemotesProject.md> "Palette:bitwigRemotesProject")• [Palette:bitwigRemotesTrack ](<./Palette-bitwigRemotesTrack.md> "Palette:bitwigRemotesTrack")• [Palette:bitwigSelect ](<./Palette-bitwigSelect.md> "Palette:bitwigSelect")• [Palette:bitwigSong ](<./Palette-bitwigSong.md> "Palette:bitwigSong")• [Palette:bitwigTrack ](<./Palette-bitwigTrack.md> "Palette:bitwigTrack")• [Palette:bitwigTrackRemotes ](<./Palette-bitwigTrackRemotes.md> "Palette:bitwigTrackRemotes")• [Palette:blendModes ](<./Palette-blendModes.md> "Palette:blendModes")• [Palette:bloom ](<./Palette-bloom.md> "Palette:bloom")• [Palette:camera ](<./Palette-camera.md> "Palette:camera")• [Palette:cameraBrowser ](<./Palette-cameraBrowser.md> "Palette:cameraBrowser")• [Palette:cameraViewport ](<./Palette-cameraViewport.md> "Palette:cameraViewport")• [Palette:camSchnappr ](<./Palette-camSchnappr.md> "Palette:camSchnappr")• [Palette:changeColor ](<./Palette-changeColor.md> "Palette:changeColor")• [Palette:changeToColor ](<./Palette-changeToColor.md> "Palette:changeToColor")• [Palette:checker ](<./Palette-checker.md> "Palette:checker")• [Palette:chromaKey ](<./Palette-chromaKey.md> "Palette:chromaKey")• [Palette:colorThreshold ](<./Palette-colorThreshold.md> "Palette:colorThreshold")• [Palette:compareComp ](<./Palette-compareComp.md> "Palette:compareComp")• [Palette:convolve ](<./Palette-convolve.md> "Palette:convolve")• [Palette:cornerPinPOP ](<./Palette-cornerPinPOP.md> "Palette:cornerPinPOP")• [Palette:cornerPinSOP ](<./Palette-cornerPinSOP.md> "Palette:cornerPinSOP")• [Palette:cppParsTemplateGen ](<./Palette-cppParsTemplateGen.md> "Palette:cppParsTemplateGen")• [Palette:customAttributes ](<./Palette-customAttributes.md> "Palette:customAttributes")• [Palette:debugControl ](<./Palette-debugControl.md> "Palette:debugControl")• [Palette:dent ](<./Palette-dent.md> "Palette:dent")• [Palette:depthExtract ](<./Palette-depthExtract.md> "Palette:depthExtract")• [Palette:depthProjection ](<./Palette-depthProjection.md> "Palette:depthProjection")• [Palette:dilate ](<./Palette-dilate.md> "Palette:dilate")• [Palette:domeViewer ](<./Palette-domeViewer.md> "Palette:domeViewer")• [Palette:encoder ](<./Palette-encoder.md> "Palette:encoder")• [Palette:equalizer ](<./Palette-equalizer.md> "Palette:equalizer")• [Palette:feedback ](<./Palette-feedback.md> "Palette:feedback")• [Palette:feedbackEdge ](<./Palette-feedbackEdge.md> "Palette:feedbackEdge")• [Palette:firmata ](<./Palette-firmata.md> "Palette:firmata")• [Palette:gal ](<./Palette-gal.md> "Palette:gal")• [Palette:geoPanel ](<./Palette-geoPanel.md> "Palette:geoPanel")• [Palette:gestureCapture ](<./Palette-gestureCapture.md> "Palette:gestureCapture")• [Palette:graphPlot ](<./Palette-graphPlot.md> "Palette:graphPlot")• [Palette:histogram ](<./Palette-histogram.md> "Palette:histogram")• [Palette:hsvBlur ](<./Palette-hsvBlur.md> "Palette:hsvBlur")• [Palette:imageSearch ](<./Palette-imageSearch.md> "Palette:imageSearch")• [Palette:julia ](<./Palette-julia.md> "Palette:julia")• [Palette:kantanMapper ](<./Palette-kantanMapper.md> "Palette:kantanMapper")• [Palette:kinectCalibration ](<./Palette-kinectCalibration.md> "Palette:kinectCalibration")• [Palette:kinectPointcloud ](<./Palette-kinectPointcloud.md> "Palette:kinectPointcloud")• [Palette:leapPaint ](<./Palette-leapPaint.md> "Palette:leapPaint")• [Palette:lightTunnel ](<./Palette-lightTunnel.md> "Palette:lightTunnel")• [Palette:logger ](<./Palette-logger.md> "Palette:logger")• [Palette:mandelbrot ](<./Palette-mandelbrot.md> "Palette:mandelbrot")• [Palette:materialDesignIcons ](<./Palette-materialDesignIcons.md> "Palette:materialDesignIcons")• [Palette:mesh ](<./Palette-mesh.md> "Palette:mesh")• [Palette:monochrome ](<./Palette-monochrome.md> "Palette:monochrome")• [Palette:motionSense ](<./Palette-motionSense.md> "Palette:motionSense")• [Palette:movieEngine ](<./Palette-movieEngine.md> "Palette:movieEngine")• [Palette:moviePlayer ](<./Palette-moviePlayer.md> "Palette:moviePlayer")• [Palette:moviePlaylist ](<./Palette-moviePlaylist.md> "Palette:moviePlaylist")• [Palette:multiLevel ](<./Palette-multiLevel.md> "Palette:multiLevel")• [Palette:multiMix ](<./Palette-multiMix.md> "Palette:multiMix")• [Palette:noise ](<./Palette-noise.md> "Palette:noise")• [Palette:onScreenKeyboard ](<./Palette-onScreenKeyboard.md> "Palette:onScreenKeyboard")• [Palette:operatorPath ](<./Palette-operatorPath.md> "Palette:operatorPath")• [Palette:opticalFlow ](<./Palette-opticalFlow.md> "Palette:opticalFlow")• [Palette:particlesGpu ](<./Palette-particlesGpu.md> "Palette:particlesGpu")• [Palette:pixelate ](<./Palette-pixelate.md> "Palette:pixelate")• [Palette:pixelRelocator ](<./Palette-pixelRelocator.md> "Palette:pixelRelocator")• [Palette:pointGenerator ](<./Palette-pointGenerator.md> "Palette:pointGenerator")• [Palette:pointillize ](<./Palette-pointillize.md> "Palette:pointillize")• [Palette:pointMerge ](<./Palette-pointMerge.md> "Palette:pointMerge")• [Palette:pointRender ](<./Palette-pointRender.md> "Palette:pointRender")• [Palette:pointRepack ](<./Palette-pointRepack.md> "Palette:pointRepack")• [Palette:pointTransform ](<./Palette-pointTransform.md> "Palette:pointTransform")• [Palette:pointWeight ](<./Palette-pointWeight.md> "Palette:pointWeight")• [Palette:popDialog ](<./Palette-popDialog.md> "Palette:popDialog")• [Palette:probe ](<./Palette-probe.md> "Palette:probe")• Palette:projectorBlend • [Palette:pushPins ](<./Palette-pushPins.md> "Palette:pushPins")• [Palette:puzzle ](<./Palette-puzzle.md> "Palette:puzzle")• [Palette:quadReproject ](<./Palette-quadReproject.md> "Palette:quadReproject")• [Palette:radialBlur ](<./Palette-radialBlur.md> "Palette:radialBlur")• [Palette:recorder ](<./Palette-recorder.md> "Palette:recorder")• [Palette:remotePanel ](<./Palette-remotePanel.md> "Palette:remotePanel")• [Palette:rgbaBlur ](<./Palette-rgbaBlur.md> "Palette:rgbaBlur")• [Palette:rgbaDelay ](<./Palette-rgbaDelay.md> "Palette:rgbaDelay")• [Palette:rgbContrast ](<./Palette-rgbContrast.md> "Palette:rgbContrast")• [Palette:sceneChanger ](<./Palette-sceneChanger.md> "Palette:sceneChanger")• [Palette:search ](<./Palette-search.md> "Palette:search")• [Palette:searchReplace ](<./Palette-searchReplace.md> "Palette:searchReplace")• [Palette:sharpen ](<./Palette-sharpen.md> "Palette:sharpen")• [Palette:sickEngine ](<./Palette-sickEngine.md> "Palette:sickEngine")• [Palette:signalingClient ](<./Palette-signalingClient.md> "Palette:signalingClient")• [Palette:signalingServer ](<./Palette-signalingServer.md> "Palette:signalingServer")• [Palette:softenAlpha ](<./Palette-softenAlpha.md> "Palette:softenAlpha")• [Palette:solarize ](<./Palette-solarize.md> "Palette:solarize")• [Palette:sopRender ](<./Palette-sopRender.md> "Palette:sopRender")• [Palette:splitter ](<./Palette-splitter.md> "Palette:splitter")• [Palette:stitcher ](<./Palette-stitcher.md> "Palette:stitcher")• [Palette:stoner ](<./Palette-stoner.md> "Palette:stoner")• [Palette:superFormula ](<./Palette-superFormula.md> "Palette:superFormula")• [Palette:SVG ](<./Palette-SVG.md> "Palette:SVG")• [Palette:sweetSpot ](<./Palette-sweetSpot.md> "Palette:sweetSpot")• [Palette:sweetSpotPreviz ](<./Palette-sweetSpotPreviz.md> "Palette:sweetSpotPreviz")• [Palette:synchroCache ](<./Palette-synchroCache.md> "Palette:synchroCache")• [Palette:synchroClient ](<./Palette-synchroClient.md> "Palette:synchroClient")• [Palette:synchroFrameIn ](<./Palette-synchroFrameIn.md> "Palette:synchroFrameIn")• [Palette:synchroFrameOut ](<./Palette-synchroFrameOut.md> "Palette:synchroFrameOut")• [Palette:synchroNDIIn ](<./Palette-synchroNDIIn.md> "Palette:synchroNDIIn")• [Palette:synchroSDIIn ](<./Palette-synchroSDIIn.md> "Palette:synchroSDIIn")• [Palette:synchroVideoOut ](<./Palette-synchroVideoOut.md> "Palette:synchroVideoOut")• [Palette:tdBitwigPackage ](<./Palette-tdBitwigPackage.md> "Palette:tdBitwigPackage")• [Palette:tdPyEnvManager ](<./Palette-tdPyEnvManager.md> "Palette:tdPyEnvManager")• [Palette:TDVR ](<./Palette-TDVR.md> "Palette:TDVR")• [Palette:testGrid ](<./Palette-testGrid.md> "Palette:testGrid")• [Palette:threadManagerClient ](<./Palette-threadManagerClient.md> "Palette:threadManagerClient")• [Palette:threadsMonitor ](<./Palette-threadsMonitor.md> "Palette:threadsMonitor")• [Palette:transitMap ](<./Palette-transitMap.md> "Palette:transitMap")• [Palette:twirl ](<./Palette-twirl.md> "Palette:twirl")• [Palette:vectorScope ](<./Palette-vectorScope.md> "Palette:vectorScope")• [Palette:virtualFile ](<./Palette-virtualFile.md> "Palette:virtualFile")• [Palette:waveformMonitor ](<./Palette-waveformMonitor.md> "Palette:waveformMonitor")• [Palette:webBrowser ](<./Palette-webBrowser.md> "Palette:webBrowser")• [Palette:webRTC ](<./Palette-webRTC.md> "Palette:webRTC")• [Palette:webRTCPanel ](<./Palette-webRTCPanel.md> "Palette:webRTCPanel")• [Palette:webRTCPanelRcv ](<./Palette-webRTCPanelRcv.md> "Palette:webRTCPanelRcv")• [Palette:xyScope ](<./Palette-xyScope.md> "Palette:xyScope")• [Thread Manager ](<./Thread_Manager.md> "Thread Manager")
