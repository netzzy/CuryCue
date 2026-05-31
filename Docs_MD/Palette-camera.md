# Palette:camera

##   
  
Summary

The camera component can be used to interactively control a camera's position in a 3D scene. It can be used directly in a network in place of the default [Camera COMP](<./Camera_COMP.md> "Camera COMP") and connected to a [Panel Component](<./Panel_Component.md> "Panel Component") to provide a 3D viewer equivalent to the built-in 3D [geometry viewer](<./Geometry_Viewer.md> "Geometry Viewer"). 

**Note** After referencing this camera in a [Render TOP](<./Render_TOP.md> "Render TOP"), it is important to also update the Render TOP parameter in the camera to reference the same Render TOP. Unlike the regular Camera OBJ, this camera component requires knowledge of the scene being rendered in order to calculate framing, pivot on geometry, and to update the viewer. 

The camera's extension Methods can be used to save and recall camera positions, get the current pivot position, align the camera to specific axis, and more. The extension class can also be used to implement additional navigation modes. 

By default, camera movements are controlled by dragging the mouse while holding the left, right or middle buttons or by scrolling with the mouse wheel. The component also supports the following keyboard shortcuts: 
* 'h'/'n' - Home/Front - Frame the scene and align the camera to face the negative z axis.
  * 'f' - Frame - Frame the scene while maintaining the current camera angle.
  * 't' - Top - Frame the scene from the top looking down the negative y axis.
  * 'r' - Right - Frame the scene from the right looking along the negative x axis.
  * 'l' - Left - Frame the scene from the left looking along the positive x axis.


First-person keyboard controls can be enabled using the 'WASD Keys Active' parameter on the Keyboard page. When enabled, these keys provide shortcuts that are equivalent to the 'Camera' navigation mode: 
* 'W' - Walk forward on the XZ plane.
  * 'A' - Step to the left.
  * 'D' - Step to the right.
  * 'S' - Walk backwards on the XZ plane.
  * 'Q' - Turn to the left.
  * 'E' - Turn to the right.


This camera also supports 3D mouse movement by enabling the 'Active' parameter on the 3D Mouse page. The input device can be selected from the drop down menu. 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[Palette:camera Ext](</index.php?title=Palette:camera_Ext&action=edit&redlink=1> "Palette:camera Ext \(page does not exist\)")

## 

Parameters - camera Page

Help`Help`\- Open this help page. 

Version`Version`\- The version number of the component. 

Camera OBJ`Cameraobj`\- A read-only reference to the internal [Camera COMP](<./Camera_COMP.md> "Camera COMP") where all of the camera logic is performed. 

Panel COMP`Panelcomp`\- The [Panel Component](<./Panel_Component.md> "Panel Component") receives the mouse and keyboard interactions, and is used to control the interaction. By default, this parameter is set to a basic container inside of the camera that is used as the node's viewer. You can change this reference to an external panel if you wish to control the camera from another view. **Note:** If you're using your own panel, make sure to enable the Mouse Wheel and Mouse UV Button parameters to enable full functionality. 

Render TOP`Rendertop`\- A reference to the [Render TOP](<./Render_TOP.md> "Render TOP") that is rendering the 3D scene. This is used to determine the bounds of the geometry for framing and homing, and to determine what geometry can be clicked on for pivoting. Only geometry that is included in the Render TOP's Geometry parameter is included in the camera calculations. By default, the render top is also used for the display in the node viewer. 

Reset Camera`Reset`\- Returns the camera to a default position facing towards the negative Z axis. Unlike Homing, resetting the camera goes to the same position regardless of the geometry in the scene. 

Navigation Mode`Navigationmode`\- ⊞ \- The navigation mode determines how mouse movements inside the [Panel Component](<./Panel_Component.md> "Panel Component") affect the camera's position and orientation. They are based off the [navigation modes](<./Geometry_Viewer.md> "Geometry Viewer") available through the 3D viewer's right-click menu. 
* Cursor`cursor`\- In this mode, left-clicking the mouse will pivot around the geometry under the cursor (or the center of the viewport if there is no geometry). The right mouse button will truck/pedestal the camera and the middle mouse button and mouse wheel will dolly (zoom) the camera towards or away from the cursor position.
* Object`object`\- In Object mode, the camera will always pivot around the center of the geometry when dragging with the left mouse button. Dragging with the right mouse button will truck/pedestal the camera and the middle mouse button and mouse wheel will dolly (zoom) the camera towards or away from the cursor position.
* Camera`camera`\- This mode uses a first-person style camera where dragging with the left mouse button will turn the camera left, right, up or down. Dragging the right mouse button will truck/pedestal the camera, while dragging the middle mouse button will dolly the camera forward or pan left and right. The mouse wheel will dolly (zoom) the camera towards or away from the cursor position.


Auto Rotate`Autorotate`\- Turning on this feature will give the camera rotation some inertia so that it continues to rotate after the mouse is released. The speed of the movement is determined by how fast the mouse is moved. The camera will continue to rotate indefinitely, and will not slow down. 

Home All`Homeall`\- Pulsing this button will set the camera to face the negative Z axis and to frame all of the geometry defined in the Render TOP parameter. The 'H' key can also be used as a shortcut for homing. 

Frame All`Frameall`\- Pulsing this button will move the camera to fit all of the geometry in the current scene while maintaining the existing camera direction. The 'F' key can also be used as a shortcut for framing. 

## 

Parameters - Buttons Page

Tumble Mouse Button`Tumblemouse`\- ⊞ \- The mouse button to hold to 'tumble/pivot/rotate' the camera. How the camera tumbles depends on the current navigation mode. 
* Left`left`\- The camera will tumble when holding down the **left** mouse button and moving the mouse.
* Right`right`\- The camera will tumble when holding down the **right** mouse button and moving the mouse.
* Middle`middle`\- The camera will tumble when holding down the **middle** mouse button and moving the mouse.


Tumble Modifier`Tumblemod`\- ⊞ \- Select whether users must hold down an additional key to tumble the camera. This can be useful to enable multiple camera movements with the same mouse button e.g. LMB is pan, Alt+LMB is tumble. 
* None`none`-
* Alt`alt`-
* Ctrl`ctrl`-
* Shift`shift`-


Tumble Speed Multiplier`Tumblemult`\- Control how quickly the camera tumbles relative to the amount of mouse movement. 

Dolly Mouse Button`Dollymouse`\- ⊞ \- The mouse button to hold to 'dolly' the camera (move forward or backward). How the camera dollys depends on the current navigation mode. 
* Left`left`-
* Right`right`-
* Middle`middle`-


Dolly Modifier`Dollymod`\- ⊞ \- Select whether users must hold down an additional key to dolly the camera. This can be useful to enable multiple camera movements with the same mouse button e.g. LMB is pan, Alt+LMB is tumble. 
* None`none`-
* Alt`alt`-
* Ctrl`ctrl`-
* Shift`shift`-


Dolly Speed Multiplier`Dollymult`\- Control how quickly the camera dollys relative to the amount of mouse movement. The speed of the camera movement is also depending on the distance to the current pivot point. 

Pan Mouse Button`Panmouse`\- ⊞ \- The mouse button to hold to 'pan/track' the camera. How the camera pans depends on the current navigation mode. 
* Left`left`-
* Right`right`-
* Middle`middle`-


Pan Modifier`Panmod`\- ⊞ \- Select whether users must hold down an additional key to pan the camera. This can be useful to enable multiple camera movements with the same mouse button e.g. LMB is pan, Alt+LMB is tumble. 
* None`none`-
* Alt`alt`-
* Ctrl`ctrl`-
* Shift`shift`-


Pan Speed Multiplier`Panmult`\- Control how quickly the camera pans relative to the amount of mouse movement. The pan speed is also based on the distance to the current pivot point. 

Mouse Wheel Multiplier`Wheelmult`\- Controls how quickly the camera moves when the user turns the mouse wheel. The camera speed is also based on the distance to the current pivot point. 

## 

Parameters - 3D Mouse Page

Active`Mouse3dactive`\- Enable control of the camera using a 3D mouse or joystick. The camera uses an internal [Joystick CHOP](<./Joystick_CHOP.md> "Joystick CHOP") to obtain up to 6 degrees of movement from an attached device. 

Device`Mouse3ddevice`\- ⊞ \- Choose which device will control the camera. 
* default`default`-
* Player 1 Controller`player1controller`-
* Player 2 Controller`player2controller`-
* Player 3 Controller`player3controller`-
* Player 4 Controller`player4controller`-
* 3Dconnexion KMJ Emulator`tdjoy:p:3Dconnexion KMJ Emulator:l:0x5:`-


3D Mouse Speed Multiplier`Mouse3dmult`\- Controls how quickly the camera moves relative to the input values from the attached device. Camera speed is also based on the distance to the current pivot point. 

## 

Parameters - Keyboard Page

WASD Keys Active`Keysactive`\- Allows controlling the camera using the W, S, A, D, Q and E keys on the keyboard similar to a first-person game camera. 

Turn Speed Multiplier`Turnmult`\- Controls how quickly the camera turns when a user holds the Q and E keys. 

Walk Speed Multiplier`Walkmult`\- Controls how quickly the camera moves when a user holds the W, A, S and D keys. 

TouchDesigner Build: Latest\n2021.10000before 2021.10000

Palette  
---  
[Palette ](<./Palette.md> "Palette")• [Palette:arcBallCamera ](<./Palette-arcBallCamera.md> "Palette:arcBallCamera")• [Palette:arcBallGeometry ](<./Palette-arcBallGeometry.md> "Palette:arcBallGeometry")• [Palette:audioAnalysis ](<./Palette-audioAnalysis.md> "Palette:audioAnalysis")• [Palette:audioSet ](<./Palette-audioSet.md> "Palette:audioSet")• [Palette:autoMediaPlayer ](<./Palette-autoMediaPlayer.md> "Palette:autoMediaPlayer")• [Palette:battery ](<./Palette-battery.md> "Palette:battery")• [Palette:bitwigClip ](<./Palette-bitwigClip.md> "Palette:bitwigClip")• [Palette:bitwigClipSlot ](<./Palette-bitwigClipSlot.md> "Palette:bitwigClipSlot")• [Palette:bitwigDeviceRemotes ](<./Palette-bitwigDeviceRemotes.md> "Palette:bitwigDeviceRemotes")• [Palette:bitwigMain ](<./Palette-bitwigMain.md> "Palette:bitwigMain")• [Palette:bitwigNote ](<./Palette-bitwigNote.md> "Palette:bitwigNote")• [Palette:bitwigProjectRemotes ](<./Palette-bitwigProjectRemotes.md> "Palette:bitwigProjectRemotes")• [Palette:bitwigRemotesDevice ](<./Palette-bitwigRemotesDevice.md> "Palette:bitwigRemotesDevice")• [Palette:bitwigRemotesProject ](<./Palette-bitwigRemotesProject.md> "Palette:bitwigRemotesProject")• [Palette:bitwigRemotesTrack ](<./Palette-bitwigRemotesTrack.md> "Palette:bitwigRemotesTrack")• [Palette:bitwigSelect ](<./Palette-bitwigSelect.md> "Palette:bitwigSelect")• [Palette:bitwigSong ](<./Palette-bitwigSong.md> "Palette:bitwigSong")• [Palette:bitwigTrack ](<./Palette-bitwigTrack.md> "Palette:bitwigTrack")• [Palette:bitwigTrackRemotes ](<./Palette-bitwigTrackRemotes.md> "Palette:bitwigTrackRemotes")• [Palette:blendModes ](<./Palette-blendModes.md> "Palette:blendModes")• [Palette:bloom ](<./Palette-bloom.md> "Palette:bloom")• Palette:camera • [Palette:cameraBrowser ](<./Palette-cameraBrowser.md> "Palette:cameraBrowser")• [Palette:cameraViewport ](<./Palette-cameraViewport.md> "Palette:cameraViewport")• [Palette:camSchnappr ](<./Palette-camSchnappr.md> "Palette:camSchnappr")• [Palette:changeColor ](<./Palette-changeColor.md> "Palette:changeColor")• [Palette:changeToColor ](<./Palette-changeToColor.md> "Palette:changeToColor")• [Palette:checker ](<./Palette-checker.md> "Palette:checker")• [Palette:chromaKey ](<./Palette-chromaKey.md> "Palette:chromaKey")• [Palette:colorThreshold ](<./Palette-colorThreshold.md> "Palette:colorThreshold")• [Palette:compareComp ](<./Palette-compareComp.md> "Palette:compareComp")• [Palette:convolve ](<./Palette-convolve.md> "Palette:convolve")• [Palette:cornerPinPOP ](<./Palette-cornerPinPOP.md> "Palette:cornerPinPOP")• [Palette:cornerPinSOP ](<./Palette-cornerPinSOP.md> "Palette:cornerPinSOP")• [Palette:cppParsTemplateGen ](<./Palette-cppParsTemplateGen.md> "Palette:cppParsTemplateGen")• [Palette:customAttributes ](<./Palette-customAttributes.md> "Palette:customAttributes")• [Palette:debugControl ](<./Palette-debugControl.md> "Palette:debugControl")• [Palette:dent ](<./Palette-dent.md> "Palette:dent")• [Palette:depthExtract ](<./Palette-depthExtract.md> "Palette:depthExtract")• [Palette:depthProjection ](<./Palette-depthProjection.md> "Palette:depthProjection")• [Palette:dilate ](<./Palette-dilate.md> "Palette:dilate")• [Palette:domeViewer ](<./Palette-domeViewer.md> "Palette:domeViewer")• [Palette:encoder ](<./Palette-encoder.md> "Palette:encoder")• [Palette:equalizer ](<./Palette-equalizer.md> "Palette:equalizer")• [Palette:feedback ](<./Palette-feedback.md> "Palette:feedback")• [Palette:feedbackEdge ](<./Palette-feedbackEdge.md> "Palette:feedbackEdge")• [Palette:firmata ](<./Palette-firmata.md> "Palette:firmata")• [Palette:gal ](<./Palette-gal.md> "Palette:gal")• [Palette:geoPanel ](<./Palette-geoPanel.md> "Palette:geoPanel")• [Palette:gestureCapture ](<./Palette-gestureCapture.md> "Palette:gestureCapture")• [Palette:graphPlot ](<./Palette-graphPlot.md> "Palette:graphPlot")• [Palette:histogram ](<./Palette-histogram.md> "Palette:histogram")• [Palette:hsvBlur ](<./Palette-hsvBlur.md> "Palette:hsvBlur")• [Palette:imageSearch ](<./Palette-imageSearch.md> "Palette:imageSearch")• [Palette:julia ](<./Palette-julia.md> "Palette:julia")• [Palette:kantanMapper ](<./Palette-kantanMapper.md> "Palette:kantanMapper")• [Palette:kinectCalibration ](<./Palette-kinectCalibration.md> "Palette:kinectCalibration")• [Palette:kinectPointcloud ](<./Palette-kinectPointcloud.md> "Palette:kinectPointcloud")• [Palette:leapPaint ](<./Palette-leapPaint.md> "Palette:leapPaint")• [Palette:lightTunnel ](<./Palette-lightTunnel.md> "Palette:lightTunnel")• [Palette:logger ](<./Palette-logger.md> "Palette:logger")• [Palette:mandelbrot ](<./Palette-mandelbrot.md> "Palette:mandelbrot")• [Palette:materialDesignIcons ](<./Palette-materialDesignIcons.md> "Palette:materialDesignIcons")• [Palette:mesh ](<./Palette-mesh.md> "Palette:mesh")• [Palette:monochrome ](<./Palette-monochrome.md> "Palette:monochrome")• [Palette:motionSense ](<./Palette-motionSense.md> "Palette:motionSense")• [Palette:movieEngine ](<./Palette-movieEngine.md> "Palette:movieEngine")• [Palette:moviePlayer ](<./Palette-moviePlayer.md> "Palette:moviePlayer")• [Palette:moviePlaylist ](<./Palette-moviePlaylist.md> "Palette:moviePlaylist")• [Palette:multiLevel ](<./Palette-multiLevel.md> "Palette:multiLevel")• [Palette:multiMix ](<./Palette-multiMix.md> "Palette:multiMix")• [Palette:noise ](<./Palette-noise.md> "Palette:noise")• [Palette:onScreenKeyboard ](<./Palette-onScreenKeyboard.md> "Palette:onScreenKeyboard")• [Palette:operatorPath ](<./Palette-operatorPath.md> "Palette:operatorPath")• [Palette:opticalFlow ](<./Palette-opticalFlow.md> "Palette:opticalFlow")• [Palette:particlesGpu ](<./Palette-particlesGpu.md> "Palette:particlesGpu")• [Palette:pixelate ](<./Palette-pixelate.md> "Palette:pixelate")• [Palette:pixelRelocator ](<./Palette-pixelRelocator.md> "Palette:pixelRelocator")• [Palette:pointGenerator ](<./Palette-pointGenerator.md> "Palette:pointGenerator")• [Palette:pointillize ](<./Palette-pointillize.md> "Palette:pointillize")• [Palette:pointMerge ](<./Palette-pointMerge.md> "Palette:pointMerge")• [Palette:pointRender ](<./Palette-pointRender.md> "Palette:pointRender")• [Palette:pointRepack ](<./Palette-pointRepack.md> "Palette:pointRepack")• [Palette:pointTransform ](<./Palette-pointTransform.md> "Palette:pointTransform")• [Palette:pointWeight ](<./Palette-pointWeight.md> "Palette:pointWeight")• [Palette:popDialog ](<./Palette-popDialog.md> "Palette:popDialog")• [Palette:probe ](<./Palette-probe.md> "Palette:probe")• [Palette:projectorBlend ](<./Palette-projectorBlend.md> "Palette:projectorBlend")• [Palette:pushPins ](<./Palette-pushPins.md> "Palette:pushPins")• [Palette:puzzle ](<./Palette-puzzle.md> "Palette:puzzle")• [Palette:quadReproject ](<./Palette-quadReproject.md> "Palette:quadReproject")• [Palette:radialBlur ](<./Palette-radialBlur.md> "Palette:radialBlur")• [Palette:recorder ](<./Palette-recorder.md> "Palette:recorder")• [Palette:remotePanel ](<./Palette-remotePanel.md> "Palette:remotePanel")• [Palette:rgbaBlur ](<./Palette-rgbaBlur.md> "Palette:rgbaBlur")• [Palette:rgbaDelay ](<./Palette-rgbaDelay.md> "Palette:rgbaDelay")• [Palette:rgbContrast ](<./Palette-rgbContrast.md> "Palette:rgbContrast")• [Palette:sceneChanger ](<./Palette-sceneChanger.md> "Palette:sceneChanger")• [Palette:search ](<./Palette-search.md> "Palette:search")• [Palette:searchReplace ](<./Palette-searchReplace.md> "Palette:searchReplace")• [Palette:sharpen ](<./Palette-sharpen.md> "Palette:sharpen")• [Palette:sickEngine ](<./Palette-sickEngine.md> "Palette:sickEngine")• [Palette:signalingClient ](<./Palette-signalingClient.md> "Palette:signalingClient")• [Palette:signalingServer ](<./Palette-signalingServer.md> "Palette:signalingServer")• [Palette:softenAlpha ](<./Palette-softenAlpha.md> "Palette:softenAlpha")• [Palette:solarize ](<./Palette-solarize.md> "Palette:solarize")• [Palette:sopRender ](<./Palette-sopRender.md> "Palette:sopRender")• [Palette:splitter ](<./Palette-splitter.md> "Palette:splitter")• [Palette:stitcher ](<./Palette-stitcher.md> "Palette:stitcher")• [Palette:stoner ](<./Palette-stoner.md> "Palette:stoner")• [Palette:superFormula ](<./Palette-superFormula.md> "Palette:superFormula")• [Palette:SVG ](<./Palette-SVG.md> "Palette:SVG")• [Palette:sweetSpot ](<./Palette-sweetSpot.md> "Palette:sweetSpot")• [Palette:sweetSpotPreviz ](<./Palette-sweetSpotPreviz.md> "Palette:sweetSpotPreviz")• [Palette:synchroCache ](<./Palette-synchroCache.md> "Palette:synchroCache")• [Palette:synchroClient ](<./Palette-synchroClient.md> "Palette:synchroClient")• [Palette:synchroFrameIn ](<./Palette-synchroFrameIn.md> "Palette:synchroFrameIn")• [Palette:synchroFrameOut ](<./Palette-synchroFrameOut.md> "Palette:synchroFrameOut")• [Palette:synchroNDIIn ](<./Palette-synchroNDIIn.md> "Palette:synchroNDIIn")• [Palette:synchroSDIIn ](<./Palette-synchroSDIIn.md> "Palette:synchroSDIIn")• [Palette:synchroVideoOut ](<./Palette-synchroVideoOut.md> "Palette:synchroVideoOut")• [Palette:tdBitwigPackage ](<./Palette-tdBitwigPackage.md> "Palette:tdBitwigPackage")• [Palette:tdPyEnvManager ](<./Palette-tdPyEnvManager.md> "Palette:tdPyEnvManager")• [Palette:TDVR ](<./Palette-TDVR.md> "Palette:TDVR")• [Palette:testGrid ](<./Palette-testGrid.md> "Palette:testGrid")• [Palette:threadManagerClient ](<./Palette-threadManagerClient.md> "Palette:threadManagerClient")• [Palette:threadsMonitor ](<./Palette-threadsMonitor.md> "Palette:threadsMonitor")• [Palette:transitMap ](<./Palette-transitMap.md> "Palette:transitMap")• [Palette:twirl ](<./Palette-twirl.md> "Palette:twirl")• [Palette:vectorScope ](<./Palette-vectorScope.md> "Palette:vectorScope")• [Palette:virtualFile ](<./Palette-virtualFile.md> "Palette:virtualFile")• [Palette:waveformMonitor ](<./Palette-waveformMonitor.md> "Palette:waveformMonitor")• [Palette:webBrowser ](<./Palette-webBrowser.md> "Palette:webBrowser")• [Palette:webRTC ](<./Palette-webRTC.md> "Palette:webRTC")• [Palette:webRTCPanel ](<./Palette-webRTCPanel.md> "Palette:webRTCPanel")• [Palette:webRTCPanelRcv ](<./Palette-webRTCPanelRcv.md> "Palette:webRTCPanelRcv")• [Palette:xyScope ](<./Palette-xyScope.md> "Palette:xyScope")• [Thread Manager ](<./Thread_Manager.md> "Thread Manager")
