# Palette:camSchnappr

## 

Summary

camSchnappr is a interactive mapping application entirely inspired by MAPAMOK, created by Kyle McDonald at the YCAM Interlab. With Kyle publishing the source code for MAPAMOK, we had a chance to look at it and convert it into TouchDesigner. For the original tool and source have a look [here](<https://github.com/YCAMInterlab/ProCamToolkit/wiki/mapamok-%28English%29>): 

Kyle describes the significance of the tool as the use of OpenCV's cameraCalibrate to calibrate a projector via a model of the to be mapped structure instead of using a checkerboard. With TouchDesigner’s integration of Python, we were able to implement the same functionality into a standalone tool which lets you map complex structures in a small amount of time. 

See also [Projection Mapping](<./Projection_Mapping.md> "Projection Mapping"), [Palette:kantanMapper](<./Palette-kantanMapper.md> "Palette:kantanMapper"), [Vioso](<./Vioso.md> "Vioso"), [Scalable Display TOP](<./Scalable_Display_TOP.md> "Scalable Display TOP"), [projectorBlend](<./Palette-projectorBlend.md> "Palette:projectorBlend")

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[Palette:camSchnappr Ext](</index.php?title=Palette:camSchnappr_Ext&action=edit&redlink=1> "Palette:camSchnappr Ext \(page does not exist\)")

## 

What it does

If you have a physical 3D structure plus a virtual 3D model of that structure, you will be able to project a rendered virtual model onto that physical structure perfectly-aligned. You will be selecting points on your 3D Model and align them with the real world positions as you see them on the projector output. In order to support multiple projectors, the output of blend-masks from multiple camSchnapprs is now supported. 

Using your 6 or more alignment points, CamSchnappr will compute the position, rotation, scale and viewing angle of a specified TouchDesigner Camera component used for the rendering. Internally, an openCV function called`calibrateCamera`will be run and the “intrinsics and extrinsics” of the camera will be calculated and stored in the Camera component. 

## 

What you need
* TouchDesigner
  * a projector. **Note:** Make sure your projector has all digital transformations like keystone or zoom reset.
  * a physical structure to project on
  * a 3D Model of the to-be-mapped structure

## Getting Started

camSchnappr is located in the Palette in 'Mapping' folder. To begin, open the [Palette](<./Palette.md> "Palette") and drag`camSchnappr`from Palette>Mapping onto your network pane. 

## 

Parameters - camSchnappr Page

Project`Project`\- Specify a [Camera COMP](<./Camera_COMP.md> "Camera COMP") that will be used as the camera to be calibrated. By default the internal Camera COMP called "project" is being used. When dropping a new Camera COMP onto this parameter, a selection of parameters will be created. 

Geo SOP`Geosop`\- Assign the [SOP](<./SOP.md> "SOP") which holds the geometry you are calibrating. _Do not specify a SOP that is a [Material SOP](<./Material_SOP.md> "Material SOP") or is from a branch with a Material SOP in it as this would break the blending. Instead reference the Texture via the Color Map Parameter._

Use Point Group`Usepointgroup`\- Enable if the source geometry contains point groups that should be used as calibration points. This is useful when dealing with large models where you can't select points but want to use a predetermined set of points. 

Geo Group`Geogroup`\- The available point groups that can be selected as a source for predetermined calibration points. 

Calibration Error`Calibrationerror`\- Displays the calibration Error returned from OpenCV after cv2.calibrateCamera has been executed. That is, the total sum of squared distances between the observed feature points _imagePoints_ and the projected (using the current estimates for camera parameters and the poses) object points _objectPoints_. 

Open Main Window`Openmain`\- Open the camSchnappr editing window. 

Close Main Window`Closemain`\- Close the camSchnappr editing window. 

Output Monitor`Monitor`\- Assign which Monitor the output window will open on. This should be your projector. 

Output is Part of Canvas`Outputcanvas`\- Enable if the projector output is part of a canvas. The main output might be a single window which is split to multiple projectors. 

Projector Resolution`Projectorres`\- The resolution of the individual projector in the output canvas. 

Grid Position`Gridpos`\- The pixel position of the individual projector in the output canvas from bottom left. 

Open Output`Open`\- Open the output window. 

Close Output`Close`\- Close the output window. 

Open Output on Primary (framed)`Openmainedit`\- Open the output as a framed window on the main monitor. This can be useful to select and move points on the projection when they are not easily identifiable. 

Show Guides`Guides`\- Show the guides on the output monitor. 

Guides Color`Guidescolor`\- Control the color of the guides on the output. 

Guides Thickness`Guidesthickness`\- Control the thickness of the guides on the output. 

Reverse Geo Vertex`Reversevertex`\- Reverse both U and V for the Hull. 

Color Geo Randomly`Colorrandom`\- Color each primitive of the geometry by random. This can be useful when schnapping complex objects. 

Color Map`Colormap`\- Assign a TOP which is used as texture in the editing viewport and the output. 

Texture Alpha`Texturealpha`\- Control the texture alpha. 

Show Wireframe`Wireframe`\- Show or hide the geometrie's wireframe. 

Wireframe Line Width`Wirewidth`\- Control the wireframe strength of the geometry in the output window. 

Clear`Clear`\- Clear the calibration data including any selected points. 

Backlight Dimmer`Blightdimmer`\- Control the backlight amount of the output window. 

Wireframe Color`Wirecolor`\- ⊞ \- Set the wireframe color of the geometry in the output window. 
* Wireframe Color`Wirecolorr`-
* Wireframe Color`Wirecolorg`-
* Wireframe Color`Wirecolorb`-


Backlight Color`Blightcolor`\- ⊞ \- Set the background color of the output window. 
* Backlight Color`Blightcolorr`-
* Backlight Color`Blightcolorg`-
* Backlight Color`Blightcolorb`-


Alt-key Multiplier`Altmodifier`\- Control the offset of a selected point when moving it with the Alt+Arrow Keys in the output window. 

## 

Parameters - Auto Blend Page

The Autoblend feature uses [Light COMPs](<./Light_COMP.md> "Light COMP") to retrieve overlapping areas by comapring uvs from the lights projection area. Further it uses the Blend, Gamma and Luminance Parameters to adjust the blend region after the principles outlined in Paul Bourke's Paper: <http://paulbourke.net/miscellaneous/edgeblend/>

camSchnappr Cameras`Camschnapprcams`\- Specify all other camSchnappr [Camera COMPs](<./Camera_COMP.md> "Camera COMP") in order to calculate the blend-mask for the projector. 

Blend`Blend`\- Adjust the power of the blend function. 

Gamma Red`Gammared`\- Adjust the gamma for the red channel. 

Gamma Green`Gammagreen`\- Adjust the gamma for the green channel. 

Gamma Blue`Gammablue`\- Adjust the gamma for the blue channel. 

Luminance`Luminance`\- Adjust the luminance for the blend function. 

## 

Parameters - openCV Page

Near`Near`\- This control allows you to designate the near clipping plane. Geometry closer from the lens than this distance will not be visible. 

Far`Far`\- This control allows you to designate the far clipping planes. Geometry further away from the lens than this distance will not be visible. 

FOV`Fov`\- Specify the initial FOV (field of view) estimation for the camera matrix given to the`cv2.calibrateCamera`function. 

Intrinsic Guess`Intrinsic`\- The initial cameraMatrix passed to`cv2.calibrateCamera`contains valid initial values of focal length and principal point that are optimized further. Otherwise, the principal point is initially set to the image center ( imageSize is used), and focal distances are computed in a least-squares fashion. It sets the flag`cv2.CALIB_USE_INTRINSIC_GUESS`Fix Aspect Ratio`Fixaspect`\- This considers only the vertical focal length as a free parameter. This should always be enabled unless you have an unusual projector with non-square pixels. It sets the flag`cv2.CALIB_FIX_ASPECT_RATIO`Zero Tangent Distance`Zerotangentdist`\- Tangential distortion is set to zero. It's enabled by default because most projectors have very little tangential distortion. It sets the flag`cv2.CALIB_ZERO_TANGENT_DIST`Fix Principal Point`Fixprincipal`\- The principal point is not changed during the optimization. You should enable this if you have a high quality lens with zero lens shift. It sets the flag`cv2.CALIB_FIX_PRINCIPAL_POINT`Fix Focal Length`Fixfocal`\- 

Fix K1`Fixk1`\- The corresponding radial distortion coefficient is not changed during the optimization. For extremely wide fisheye lenses or lenses with radial distortion try enabling these. It sets the flag`cv2.CALIB_FIX_K1`Fix K2`Fixk2`\- The corresponding radial distortion coefficient is not changed during the optimization. For extremely wide fisheye lenses or lenses with radial distortion try enabling these. It sets the flag`cv2.CALIB_FIX_K2`Fix K3`Fixk3`\- The corresponding radial distortion coefficient is not changed during the optimization. For extremely wide fisheye lenses or lenses with radial distortion try enabling these. It sets the flag`cv2.CALIB_FIX_K3`Max Iterations`Maxiterations`\- Specify the number of iterations the algorithm should terminate after. 

Precision`Precision`\- Specify the value of accuracy at which, when reaching it, the algorithm should terminate. 

## 

Parameters - ArcBall Page

The ArcBall parameters give control over the transform multipliers of the Main Window's arcBall camera. When using geometries with large dimensions, it can be necessary to adjust the Translate, Dolly and Rotate Multipliers to efficiently make use of the ArcBall Viewport. 

Translate Multiplier`Transmult`\- Control the Translate Multiplier of the ArcBall camera. 

Dolly Multiplier`Dolmult`\- Control the Dolly Multiplier of the Arcball camera. 

Rotate Multiplier`Rotmult`\- Control the Rotate Multiplier of the Arcball camera. 

## 

Parameters - OSC Page

camSchnappr now allows you to control it from a mobile device using [TouchOSC](<https://hexler.net/products/touchosc>) Download the TouchOSC layouts for IPad [File:camSchnappr.touchosc](</File:CamSchnappr.touchosc> "File:CamSchnappr.touchosc") or IPhone [File:camSchnapprIPhone.touchosc](</File:CamSchnapprIPhone.touchosc> "File:CamSchnapprIPhone.touchosc"). Make sure to turn on Touch Messages (/z) in the TouchOSC options as some of the interactions require this message to be send through. 

Active`Active`\- Activate OSC access to camSchnappr via TouchOSC. 

Port`Port`\- Set the portnumber specified in TouchOSC here. MAke sure in TouchOSC incoming and outgoing ports are set to the same value. 

## 

Parameters - About Page

Help`Help`\- Opens this page. 

Version`Version`\- Current version of this COMP. 

.tox Save Build`Toxsavebuild`\- TouchDesigner build this component was saved in. 

## 

The Viewport

Open the viewport by clicking the Open Main Window parameter. 

You can interact with the viewport as follows: 
* *       * NEW***:
  * left-mouse click and drag to tumble
  * middle-mouse click and drag to zoom
  * right-mouse click and drag to pan
  * h to home the geometry
  * create control points by ctrl+left-mouse clicking on the geometry
  * make control points active by ctrl+left-mouse clicking on blue spheres
  * delete control points by ctrl+right-mouse clicking onto spheres
  * tab to cycle through selected points


When you select points a little flag with the point number will be displayed. 

## 

The Mapping Viewport

Once you selected the correct output Monitor via the Output Monitor parameter, click the Open Output parameter. 

The interface is quite simple: 
* a red crosshair indicates your current cursor position on the screen
  * a dark yellow crosshair indicates an inactive point previously selected to be mapped in the main viewport
  * a yellow crosshair indicates an active point previously selected to be mapped in the main viewport


You can drag points to their real-world position on the screen or use the arrow keys on the keyboard. For faster movement, use alt+arrowkey to move points. 

You can also Shift+Left-click onto the viewport to move points directly to their corresponding real-world position. 

Tab will cycle through the available points. 

Using the keyboard arrow keys, you can move the points 1 pixel at a time. 

Using Alt+Arrow keyboard keys will move the point by the Alt-Multiplier Parameter amount (by default 10 pixel). 

## 

Workflow
* Create a simple render setup with the model of the object you want to map onto.
  * select the camSchnappr Camera COMP.
  * Optional: Drag your Camera COMP onto the Project Parameter of camSchnappr.
  * Drag the SOP containing the geometry of the to be mapped object onto the Geo SOP parameter.
  * Select the number of the output your Projector is connected to via the Output Monitor parameter.
  * Open the Main Window of camSchnappr by clicking the Open Main Window parameter.
  * Open the mapping Viewport by clicking the Open Output parameter, if somehow the output now overlays your main viewport, just hit escape and select a different Monitor Output number via the Output Monitor parameter.
  * In the main viewport align the geometry to the camera so it’s similar to what the projector sees.
  * Select a point in the main viewport and move it in the mapper viewport to the corresponding position on the real world object. You can also hold the Shift key and click in the mapper viewport onto the corresponding real world position.
  * Repeat the last step for at least 6 points total.
  * After you have aligned 6 points, the camera should be calibrated and you should see the projection mapped onto the object.
  * If everything is correct you can close the mapping output and the camSchnappr viewport by clicking the Close Output and Close camSchnappr parameter. The Camera Calibration values are saved inside your camSchnappr Project Camera COMP as 2 Table DATs.
  * If you used an externa Camera COMP as a project, you can now also delete camSchnappr.

## 

OSC Controls

camSchnappr can be controlled using following osc channels: 
* /1/selectPointNext [0|1] - selects the next controlpoint
  * /1/selectPointPrev [0|1] - selects the prev control point
  * /1/pointCoarse [float] [float] - move the currently selected controlpoint by u/v amount.
  * /1/pointFine [float] [float] - move the currently selected controlpoint by a fraction of u/v amount.
  * /1/pointFine/z [0|1] - if`1`start fine movement, if`0`finish fine movement
  * /1/left [0|1] - if`1`move selected point by 1 pixel left.
  * /1/right [0|1] - if`1`move selected point by 1 pixel right.
  * /1/up [0|1] - if`1`move selected point by 1 pixel up.
  * /1/down [0|1] - if`1`move selected point by 1 pixel down.
  * /1/altleft [0|1] - if`1`move selected point by 10 pixels left.
  * /1/altright [0|1] - if`1`move selected point by 10 pixels right.
  * /1/altup [0|1] - if`1`move selected point by 10 pixels up.
  * /1/altdown [0|1] - if`1`move selected point by 10 pixels down.
  * /1/openCloseOutput [0|1] - open / close the main poutput.
  * /1/selectCamSchnappr [0|1] - select the next camSchnappr in your setup.
  * /1/selectCamSchnapprPrev [0|1] - select the previous camSchnappr in your setup.

## 

Operator Outputs
* Output 0 \- When using multiple camSchnappr cameras, this output will be the blendmask between them.


TouchDesigner Build: Latest\nwikieditorwikieditorwikieditorwikieditorwikieditormw-undo2021.100002020.236802019.146502018.28070before 2018.28070

Palette  
---  
[Palette ](<./Palette.md> "Palette")• [Palette:arcBallCamera ](<./Palette-arcBallCamera.md> "Palette:arcBallCamera")• [Palette:arcBallGeometry ](<./Palette-arcBallGeometry.md> "Palette:arcBallGeometry")• [Palette:audioAnalysis ](<./Palette-audioAnalysis.md> "Palette:audioAnalysis")• [Palette:audioSet ](<./Palette-audioSet.md> "Palette:audioSet")• [Palette:autoMediaPlayer ](<./Palette-autoMediaPlayer.md> "Palette:autoMediaPlayer")• [Palette:battery ](<./Palette-battery.md> "Palette:battery")• [Palette:bitwigClip ](<./Palette-bitwigClip.md> "Palette:bitwigClip")• [Palette:bitwigClipSlot ](<./Palette-bitwigClipSlot.md> "Palette:bitwigClipSlot")• [Palette:bitwigDeviceRemotes ](<./Palette-bitwigDeviceRemotes.md> "Palette:bitwigDeviceRemotes")• [Palette:bitwigMain ](<./Palette-bitwigMain.md> "Palette:bitwigMain")• [Palette:bitwigNote ](<./Palette-bitwigNote.md> "Palette:bitwigNote")• [Palette:bitwigProjectRemotes ](<./Palette-bitwigProjectRemotes.md> "Palette:bitwigProjectRemotes")• [Palette:bitwigRemotesDevice ](<./Palette-bitwigRemotesDevice.md> "Palette:bitwigRemotesDevice")• [Palette:bitwigRemotesProject ](<./Palette-bitwigRemotesProject.md> "Palette:bitwigRemotesProject")• [Palette:bitwigRemotesTrack ](<./Palette-bitwigRemotesTrack.md> "Palette:bitwigRemotesTrack")• [Palette:bitwigSelect ](<./Palette-bitwigSelect.md> "Palette:bitwigSelect")• [Palette:bitwigSong ](<./Palette-bitwigSong.md> "Palette:bitwigSong")• [Palette:bitwigTrack ](<./Palette-bitwigTrack.md> "Palette:bitwigTrack")• [Palette:bitwigTrackRemotes ](<./Palette-bitwigTrackRemotes.md> "Palette:bitwigTrackRemotes")• [Palette:blendModes ](<./Palette-blendModes.md> "Palette:blendModes")• [Palette:bloom ](<./Palette-bloom.md> "Palette:bloom")• [Palette:camera ](<./Palette-camera.md> "Palette:camera")• [Palette:cameraBrowser ](<./Palette-cameraBrowser.md> "Palette:cameraBrowser")• [Palette:cameraViewport ](<./Palette-cameraViewport.md> "Palette:cameraViewport")• Palette:camSchnappr • [Palette:changeColor ](<./Palette-changeColor.md> "Palette:changeColor")• [Palette:changeToColor ](<./Palette-changeToColor.md> "Palette:changeToColor")• [Palette:checker ](<./Palette-checker.md> "Palette:checker")• [Palette:chromaKey ](<./Palette-chromaKey.md> "Palette:chromaKey")• [Palette:colorThreshold ](<./Palette-colorThreshold.md> "Palette:colorThreshold")• [Palette:compareComp ](<./Palette-compareComp.md> "Palette:compareComp")• [Palette:convolve ](<./Palette-convolve.md> "Palette:convolve")• [Experimental:Palette:cornerPinPOP ](</index.php?title=Experimental:Palette:cornerPinPOP&action=edit&redlink=1> "Experimental:Palette:cornerPinPOP \(page does not exist\)")• [Palette:cornerPinSOP ](<./Palette-cornerPinSOP.md> "Palette:cornerPinSOP")• [Palette:cppParsTemplateGen ](<./Palette-cppParsTemplateGen.md> "Palette:cppParsTemplateGen")• [Palette:customAttributes ](<./Palette-customAttributes.md> "Palette:customAttributes")• [Palette:debugControl ](<./Palette-debugControl.md> "Palette:debugControl")• [Palette:dent ](<./Palette-dent.md> "Palette:dent")• [Palette:depthExtract ](<./Palette-depthExtract.md> "Palette:depthExtract")• [Palette:depthProjection ](<./Palette-depthProjection.md> "Palette:depthProjection")• [Palette:dilate ](<./Palette-dilate.md> "Palette:dilate")• [Experimental:Palette:domeViewer ](</index.php?title=Experimental:Palette:domeViewer&action=edit&redlink=1> "Experimental:Palette:domeViewer \(page does not exist\)")• [Palette:encoder ](<./Palette-encoder.md> "Palette:encoder")• [Palette:equalizer ](<./Palette-equalizer.md> "Palette:equalizer")• [Palette:feedback ](<./Palette-feedback.md> "Palette:feedback")• [Palette:feedbackEdge ](<./Palette-feedbackEdge.md> "Palette:feedbackEdge")• [Palette:firmata ](<./Palette-firmata.md> "Palette:firmata")• [Palette:gal ](<./Palette-gal.md> "Palette:gal")• [Palette:geoPanel ](<./Palette-geoPanel.md> "Palette:geoPanel")• [Palette:gestureCapture ](<./Palette-gestureCapture.md> "Palette:gestureCapture")• [Palette:graphPlot ](<./Palette-graphPlot.md> "Palette:graphPlot")• [Palette:histogram ](<./Palette-histogram.md> "Palette:histogram")• [Palette:hsvBlur ](<./Palette-hsvBlur.md> "Palette:hsvBlur")• [Palette:imageSearch ](<./Palette-imageSearch.md> "Palette:imageSearch")• [Palette:julia ](<./Palette-julia.md> "Palette:julia")• [Palette:kantanMapper ](<./Palette-kantanMapper.md> "Palette:kantanMapper")• [Palette:kinectCalibration ](<./Palette-kinectCalibration.md> "Palette:kinectCalibration")• [Palette:kinectPointcloud ](<./Palette-kinectPointcloud.md> "Palette:kinectPointcloud")• [Palette:leapPaint ](<./Palette-leapPaint.md> "Palette:leapPaint")• [Palette:lightTunnel ](<./Palette-lightTunnel.md> "Palette:lightTunnel")• [Palette:logger ](<./Palette-logger.md> "Palette:logger")• [Experimental:Palette:logger ](</index.php?title=Experimental:Palette:logger&action=edit&redlink=1> "Experimental:Palette:logger \(page does not exist\)")• [Palette:mandelbrot ](<./Palette-mandelbrot.md> "Palette:mandelbrot")• [Palette:materialDesignIcons ](<./Palette-materialDesignIcons.md> "Palette:materialDesignIcons")• [Palette:mesh ](<./Palette-mesh.md> "Palette:mesh")• [Palette:monochrome ](<./Palette-monochrome.md> "Palette:monochrome")• [Palette:motionSense ](<./Palette-motionSense.md> "Palette:motionSense")• [Palette:movieEngine ](<./Palette-movieEngine.md> "Palette:movieEngine")• [Palette:moviePlayer ](<./Palette-moviePlayer.md> "Palette:moviePlayer")• [Palette:moviePlaylist ](<./Palette-moviePlaylist.md> "Palette:moviePlaylist")• [Palette:multiLevel ](<./Palette-multiLevel.md> "Palette:multiLevel")• [Palette:multiMix ](<./Palette-multiMix.md> "Palette:multiMix")• [Palette:noise ](<./Palette-noise.md> "Palette:noise")• [Palette:onScreenKeyboard ](<./Palette-onScreenKeyboard.md> "Palette:onScreenKeyboard")• [Palette:operatorPath ](<./Palette-operatorPath.md> "Palette:operatorPath")• [Palette:opticalFlow ](<./Palette-opticalFlow.md> "Palette:opticalFlow")• [Palette:particlesGpu ](<./Palette-particlesGpu.md> "Palette:particlesGpu")• [Palette:pixelate ](<./Palette-pixelate.md> "Palette:pixelate")• [Palette:pixelRelocator ](<./Palette-pixelRelocator.md> "Palette:pixelRelocator")• [Palette:pointGenerator ](<./Palette-pointGenerator.md> "Palette:pointGenerator")• [Palette:pointillize ](<./Palette-pointillize.md> "Palette:pointillize")• [Palette:pointMerge ](<./Palette-pointMerge.md> "Palette:pointMerge")• [Palette:pointRender ](<./Palette-pointRender.md> "Palette:pointRender")• [Palette:pointRepack ](<./Palette-pointRepack.md> "Palette:pointRepack")• [Palette:pointTransform ](<./Palette-pointTransform.md> "Palette:pointTransform")• [Palette:pointWeight ](<./Palette-pointWeight.md> "Palette:pointWeight")• [Palette:popDialog ](<./Palette-popDialog.md> "Palette:popDialog")• [Experimental:Palette:popDialog ](</index.php?title=Experimental:Palette:popDialog&action=edit&redlink=1> "Experimental:Palette:popDialog \(page does not exist\)")• [Palette:probe ](<./Palette-probe.md> "Palette:probe")• [Palette:projectorBlend ](<./Palette-projectorBlend.md> "Palette:projectorBlend")• [Palette:pushPins ](<./Palette-pushPins.md> "Palette:pushPins")• [Palette:puzzle ](<./Palette-puzzle.md> "Palette:puzzle")• [Palette:quadReproject ](<./Palette-quadReproject.md> "Palette:quadReproject")• [Palette:radialBlur ](<./Palette-radialBlur.md> "Palette:radialBlur")• [Palette:recorder ](<./Palette-recorder.md> "Palette:recorder")• [Experimental:Palette:recorder ](</index.php?title=Experimental:Palette:recorder&action=edit&redlink=1> "Experimental:Palette:recorder \(page does not exist\)")• [Palette:remotePanel ](<./Palette-remotePanel.md> "Palette:remotePanel")• [Palette:rgbaBlur ](<./Palette-rgbaBlur.md> "Palette:rgbaBlur")• [Palette:rgbaDelay ](<./Palette-rgbaDelay.md> "Palette:rgbaDelay")• [Palette:rgbContrast ](<./Palette-rgbContrast.md> "Palette:rgbContrast")• [Palette:sceneChanger ](<./Palette-sceneChanger.md> "Palette:sceneChanger")• [Palette:search ](<./Palette-search.md> "Palette:search")• [Palette:searchReplace ](<./Palette-searchReplace.md> "Palette:searchReplace")• [Palette:sharpen ](<./Palette-sharpen.md> "Palette:sharpen")• [Palette:sickEngine ](<./Palette-sickEngine.md> "Palette:sickEngine")• [Palette:signalingClient ](<./Palette-signalingClient.md> "Palette:signalingClient")• [Palette:signalingServer ](<./Palette-signalingServer.md> "Palette:signalingServer")• [Palette:softenAlpha ](<./Palette-softenAlpha.md> "Palette:softenAlpha")• [Palette:solarize ](<./Palette-solarize.md> "Palette:solarize")• [Palette:sopRender ](<./Palette-sopRender.md> "Palette:sopRender")• [Palette:splitter ](<./Palette-splitter.md> "Palette:splitter")• [Palette:stitcher ](<./Palette-stitcher.md> "Palette:stitcher")• [Palette:stoner ](<./Palette-stoner.md> "Palette:stoner")• [Palette:superFormula ](<./Palette-superFormula.md> "Palette:superFormula")• [Palette:SVG ](<./Palette-SVG.md> "Palette:SVG")• [Palette:sweetSpot ](<./Palette-sweetSpot.md> "Palette:sweetSpot")• [Palette:sweetSpotPreviz ](<./Palette-sweetSpotPreviz.md> "Palette:sweetSpotPreviz")• [Palette:synchroCache ](<./Palette-synchroCache.md> "Palette:synchroCache")• [Palette:synchroClient ](<./Palette-synchroClient.md> "Palette:synchroClient")• [Palette:synchroFrameIn ](<./Palette-synchroFrameIn.md> "Palette:synchroFrameIn")• [Palette:synchroFrameOut ](<./Palette-synchroFrameOut.md> "Palette:synchroFrameOut")• [Palette:synchroNDIIn ](<./Palette-synchroNDIIn.md> "Palette:synchroNDIIn")• [Palette:synchroSDIIn ](<./Palette-synchroSDIIn.md> "Palette:synchroSDIIn")• [Palette:synchroVideoOut ](<./Palette-synchroVideoOut.md> "Palette:synchroVideoOut")• [Palette:tdBitwigPackage ](<./Palette-tdBitwigPackage.md> "Palette:tdBitwigPackage")• [Experimental:Palette:tdPyEnvManager ](</index.php?title=Experimental:Palette:tdPyEnvManager&action=edit&redlink=1> "Experimental:Palette:tdPyEnvManager \(page does not exist\)")• [Palette:TDVR ](<./Palette-TDVR.md> "Palette:TDVR")• [Palette:testGrid ](<./Palette-testGrid.md> "Palette:testGrid")• [Experimental:Palette:threadManagerClient ](</index.php?title=Experimental:Palette:threadManagerClient&action=edit&redlink=1> "Experimental:Palette:threadManagerClient \(page does not exist\)")• [Experimental:Palette:threadsMonitor ](</index.php?title=Experimental:Palette:threadsMonitor&action=edit&redlink=1> "Experimental:Palette:threadsMonitor \(page does not exist\)")• [Palette:transitMap ](<./Palette-transitMap.md> "Palette:transitMap")• [Palette:twirl ](<./Palette-twirl.md> "Palette:twirl")• [Palette:vectorScope ](<./Palette-vectorScope.md> "Palette:vectorScope")• [Palette:virtualFile ](<./Palette-virtualFile.md> "Palette:virtualFile")• [Palette:waveformMonitor ](<./Palette-waveformMonitor.md> "Palette:waveformMonitor")• [Palette:webBrowser ](<./Palette-webBrowser.md> "Palette:webBrowser")• [Palette:webRTC ](<./Palette-webRTC.md> "Palette:webRTC")• [Palette:webRTCPanel ](<./Palette-webRTCPanel.md> "Palette:webRTCPanel")• [Palette:webRTCPanelRcv ](<./Palette-webRTCPanelRcv.md> "Palette:webRTCPanelRcv")• [Palette:xyScope ](<./Palette-xyScope.md> "Palette:xyScope")• [Experimental:Thread Manager ](</index.php?title=Experimental:Thread_Manager&action=edit&redlink=1> "Experimental:Thread Manager \(page does not exist\)")
