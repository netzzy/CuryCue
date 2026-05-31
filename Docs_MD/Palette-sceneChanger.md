# Palette:sceneChanger

##   
  
Summary

This component provides a framework for creating a scene based show where each scene of a show is a component that outputs video from a single TOP called out1. The sceneChanger component references a "Scenes" component from which it will load all "Scene" components it finds inside. The SceneChanger is able to play each component and will cross fade from one component to the next. The workflow of this system, if correctly followed, is implicitly optimized in the sense that scenes that are not being played currently will also not cook. 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[Palette:sceneChanger Ext](<./Palette-sceneChanger_Ext.md> "Palette:sceneChanger Ext")

### Getting Started

**Note:** There is never a need to go inside the sceneChanger component. It is designed to work along side your own network. 
1. Drag in the sceneChanger component from the Tools section of the Palette.
  2. Create an empty BaseCOMP beside the newly created sceneChanger component, and name the baseCOMP "scenes".
  3. Reference the "scenes" BaseCOMP in the **Scenes COMP** parameter of the sceneChanger component.
  4. Click the "Generate Scene Template" pulse button found on the sceneChanger custom parameters. This will generate a sceneTemplate component. Cut this component and paste it into the "scenes" BaseCOMP.
  5. Rename the sceneTemplate component to any name you like for the first scene.
  6. Anything can go into a scene component. The only requirement is that the out1 TOP must be present. If this operator is removed, renamed or the type is changed to something other than a TOP then the scene will be broken.
  7. By default there is a TextTOP with its "text" parameter set to SceneTemplate. Change each scene to make them unique.
  8. All scenes must be the same resolution. This limitation is purposeful as a cleanly running show should have a strict resolution. TOP networks that dynamically change resolution cause new memory allocations which lead to frame drops. This regime ensures the TOP resolutions that pass trough the out1 TOP are always linked to the resolution of the scene component they are inside. Ideally all resolution parameters of the system are bound hierarchically to a custom resolution parameter at the top level of the show system. This will also result in a system that has the flexibility to change to any resolution easily.
  9. To make another scene simply copy a previously created scene.

### What is the Scenes component?

The scenes component is created by you, the user of the sceneChanger. The scenes component can therefore be customized in whatever way you desire. There is no specification for the scenes component other than the fact it must be referenced by the **Scenes COMP** parameter of the sceneChanger component. Once the reference is made, you put Scene components inside and the sceneChanger will find the scenes and will allow you to change between them. 

### What is a Scene Component?

A scene component can be created by clicking **Generate Scene Template** button parameter located on the Scene Changer page of sceneChanger. You can copy and paste this component into the scenes component that you make. 

A scene component is configured with the following attributes: 
* A parent shortcut that is called Scene.
  * A tag called TDScene.
  * A custom parameter page called Scene Settings.
  * The contents of the scene component can be replaced except for the out1 TOP.
  * Do not add custom parameters to the Scene component. It is meant to be a wrapper for any component you wish to put inside.
  * If you are building a system that may require custom parameters or its own extension, it is recommended you start by working inside a new child component such that you can add your own parameters to it. This will also make features that you add to your scenes more portable.

### Scene Component Parameters

The Start pulse button is run by the sceneChanger system when a new scene has been fired. The Start pulse is run, and then the sceneChanger is loaded into the sceneChanger AB mixer and is faded into. The Init pulse button is run after the scene is faded out of. This provides an event for cleaning up and resetting the scene such that it is ready to be started again. 

The Play and Length parameters are provided to the user but serve no purpose for the sceneChanger system. 

Fade In and Fade Out time parameters will be used by sceneChanger system if the SceneChange function keyword argument for FadeTime is not specified. 

To change scenes using Python there is a SceneChange() custom method. 
[code] 
    SceneChange(sceneIndexOrName, fadeTime=None)
    
[/code]

**Usage 1:** Blends to scene index number 2 - which is the 3rd scene listed in the scene index table. No fadeTime is specified so the fade in time from the new scene and the fade out time from the current scene are used in the cross fade. 
[code] 
    op('sceneChanger').SceneChange(2)
    
[/code]

**Usage 2:** Blends to scene index number 2 with a fade in and fade out time of 3. Currently fadeTime specifies both. 
[code] 
    op('sceneChanger').SceneChange(2, fadeTime=3)
    
[/code]

**Usage 3:** Blends to scene string name with a fade in and fade out time of 3. 
[code] 
    op('sceneChanger').SceneChange('MySceneName', fadeTime=3)
    
[/code]

## 

Parameters - Scene Changer Page

Help`Help`\- Opens this help page. 

Version`Version`\- Shows the current version of this component. 

Resolution`Resolution`\- ⊞ \- Sets the resolution for the sceneChanger component. All scene components should match this resolution. Ideally this parameter is bound to the same parent parameter as the scene component resolution parameter. 
* Resolution`Resolutionw`-
* Resolution`Resolutionh`-


Scenes COMP`Scenescomp`\- Specifies the parent scenes component that holds all the scene components which will be controlled by this sceneChanger. 

Next Scene`Nextscene`\- Specifies the index of the next scene that will be played when the **Fire Scene** parameter is clicked. 

Fade Time`Fadetime`\- The global cross fade time for blending from one scene to the next. This blend time can also be specified using the scripting commands or the local fade settings of each scene component. 

Fire Scene`Firescene`\- This will activate the next scene as specified by the Next Scene parameter. The sceneChanger will immediately run the Start pulse button the specified next scene component. As well it will cross from the current scene component to the next over the time period specified by the fade time settings. 

Current Scene`Currentscene`\- The index of the current scene. 

View Scene Index`Viewsceneindex`\- Displays the scenes DAT that shows a mapping of scene index to scene component name. 

Generate UI`Generateui`\- Create a simple widget based (radio buttons) UI that allows for fast changing between each scenes available in the referenced Scenes COMP. 

Generate Scene Template`Generatescenetemplate`\- Create a simple COMP with a predefined set of parameters that the sceneChanger COMP can make use of when firing a scene change. 

Reset`Reset`\- Reset the sceneChanger COMP to a default state. 

## 

Operator Inputs
* Input 0: in1 \- Accepts a table of scene names. The table format is a single column of names. The first row is the header called "Name". This table allows the user of sceneChanger to build their own scene changing solution.

## 

Operator Outputs
* Output 0 \- The final output of the show sceneChange system. This is the final output which can be passed along to other systems, streamed or displays.

Palette  
---  
[Palette ](<./Palette.md> "Palette")• [Palette:arcBallCamera ](<./Palette-arcBallCamera.md> "Palette:arcBallCamera")• [Palette:arcBallGeometry ](<./Palette-arcBallGeometry.md> "Palette:arcBallGeometry")• [Palette:audioAnalysis ](<./Palette-audioAnalysis.md> "Palette:audioAnalysis")• [Palette:audioSet ](<./Palette-audioSet.md> "Palette:audioSet")• [Palette:autoMediaPlayer ](<./Palette-autoMediaPlayer.md> "Palette:autoMediaPlayer")• [Palette:battery ](<./Palette-battery.md> "Palette:battery")• [Palette:bitwigClip ](<./Palette-bitwigClip.md> "Palette:bitwigClip")• [Palette:bitwigClipSlot ](<./Palette-bitwigClipSlot.md> "Palette:bitwigClipSlot")• [Palette:bitwigDeviceRemotes ](<./Palette-bitwigDeviceRemotes.md> "Palette:bitwigDeviceRemotes")• [Palette:bitwigMain ](<./Palette-bitwigMain.md> "Palette:bitwigMain")• [Palette:bitwigNote ](<./Palette-bitwigNote.md> "Palette:bitwigNote")• [Palette:bitwigProjectRemotes ](<./Palette-bitwigProjectRemotes.md> "Palette:bitwigProjectRemotes")• [Palette:bitwigRemotesDevice ](<./Palette-bitwigRemotesDevice.md> "Palette:bitwigRemotesDevice")• [Palette:bitwigRemotesProject ](<./Palette-bitwigRemotesProject.md> "Palette:bitwigRemotesProject")• [Palette:bitwigRemotesTrack ](<./Palette-bitwigRemotesTrack.md> "Palette:bitwigRemotesTrack")• [Palette:bitwigSelect ](<./Palette-bitwigSelect.md> "Palette:bitwigSelect")• [Palette:bitwigSong ](<./Palette-bitwigSong.md> "Palette:bitwigSong")• [Palette:bitwigTrack ](<./Palette-bitwigTrack.md> "Palette:bitwigTrack")• [Palette:bitwigTrackRemotes ](<./Palette-bitwigTrackRemotes.md> "Palette:bitwigTrackRemotes")• [Palette:blendModes ](<./Palette-blendModes.md> "Palette:blendModes")• [Palette:bloom ](<./Palette-bloom.md> "Palette:bloom")• [Palette:camera ](<./Palette-camera.md> "Palette:camera")• [Palette:cameraBrowser ](<./Palette-cameraBrowser.md> "Palette:cameraBrowser")• [Palette:cameraViewport ](<./Palette-cameraViewport.md> "Palette:cameraViewport")• [Palette:camSchnappr ](<./Palette-camSchnappr.md> "Palette:camSchnappr")• [Palette:changeColor ](<./Palette-changeColor.md> "Palette:changeColor")• [Palette:changeToColor ](<./Palette-changeToColor.md> "Palette:changeToColor")• [Palette:checker ](<./Palette-checker.md> "Palette:checker")• [Palette:chromaKey ](<./Palette-chromaKey.md> "Palette:chromaKey")• [Palette:colorThreshold ](<./Palette-colorThreshold.md> "Palette:colorThreshold")• [Palette:compareComp ](<./Palette-compareComp.md> "Palette:compareComp")• [Palette:convolve ](<./Palette-convolve.md> "Palette:convolve")• [Palette:cornerPinPOP ](<./Palette-cornerPinPOP.md> "Palette:cornerPinPOP")• [Palette:cornerPinSOP ](<./Palette-cornerPinSOP.md> "Palette:cornerPinSOP")• [Palette:cppParsTemplateGen ](<./Palette-cppParsTemplateGen.md> "Palette:cppParsTemplateGen")• [Palette:customAttributes ](<./Palette-customAttributes.md> "Palette:customAttributes")• [Palette:debugControl ](<./Palette-debugControl.md> "Palette:debugControl")• [Palette:dent ](<./Palette-dent.md> "Palette:dent")• [Palette:depthExtract ](<./Palette-depthExtract.md> "Palette:depthExtract")• [Palette:depthProjection ](<./Palette-depthProjection.md> "Palette:depthProjection")• [Palette:dilate ](<./Palette-dilate.md> "Palette:dilate")• [Palette:domeViewer ](<./Palette-domeViewer.md> "Palette:domeViewer")• [Palette:encoder ](<./Palette-encoder.md> "Palette:encoder")• [Palette:equalizer ](<./Palette-equalizer.md> "Palette:equalizer")• [Palette:feedback ](<./Palette-feedback.md> "Palette:feedback")• [Palette:feedbackEdge ](<./Palette-feedbackEdge.md> "Palette:feedbackEdge")• [Palette:firmata ](<./Palette-firmata.md> "Palette:firmata")• [Palette:gal ](<./Palette-gal.md> "Palette:gal")• [Palette:geoPanel ](<./Palette-geoPanel.md> "Palette:geoPanel")• [Palette:gestureCapture ](<./Palette-gestureCapture.md> "Palette:gestureCapture")• [Palette:graphPlot ](<./Palette-graphPlot.md> "Palette:graphPlot")• [Palette:histogram ](<./Palette-histogram.md> "Palette:histogram")• [Palette:hsvBlur ](<./Palette-hsvBlur.md> "Palette:hsvBlur")• [Palette:imageSearch ](<./Palette-imageSearch.md> "Palette:imageSearch")• [Palette:julia ](<./Palette-julia.md> "Palette:julia")• [Palette:kantanMapper ](<./Palette-kantanMapper.md> "Palette:kantanMapper")• [Palette:kinectCalibration ](<./Palette-kinectCalibration.md> "Palette:kinectCalibration")• [Palette:kinectPointcloud ](<./Palette-kinectPointcloud.md> "Palette:kinectPointcloud")• [Palette:leapPaint ](<./Palette-leapPaint.md> "Palette:leapPaint")• [Palette:lightTunnel ](<./Palette-lightTunnel.md> "Palette:lightTunnel")• [Palette:logger ](<./Palette-logger.md> "Palette:logger")• [Palette:mandelbrot ](<./Palette-mandelbrot.md> "Palette:mandelbrot")• [Palette:materialDesignIcons ](<./Palette-materialDesignIcons.md> "Palette:materialDesignIcons")• [Palette:mesh ](<./Palette-mesh.md> "Palette:mesh")• [Palette:monochrome ](<./Palette-monochrome.md> "Palette:monochrome")• [Palette:motionSense ](<./Palette-motionSense.md> "Palette:motionSense")• [Palette:movieEngine ](<./Palette-movieEngine.md> "Palette:movieEngine")• [Palette:moviePlayer ](<./Palette-moviePlayer.md> "Palette:moviePlayer")• [Palette:moviePlaylist ](<./Palette-moviePlaylist.md> "Palette:moviePlaylist")• [Palette:multiLevel ](<./Palette-multiLevel.md> "Palette:multiLevel")• [Palette:multiMix ](<./Palette-multiMix.md> "Palette:multiMix")• [Palette:noise ](<./Palette-noise.md> "Palette:noise")• [Palette:onScreenKeyboard ](<./Palette-onScreenKeyboard.md> "Palette:onScreenKeyboard")• [Palette:operatorPath ](<./Palette-operatorPath.md> "Palette:operatorPath")• [Palette:opticalFlow ](<./Palette-opticalFlow.md> "Palette:opticalFlow")• [Palette:particlesGpu ](<./Palette-particlesGpu.md> "Palette:particlesGpu")• [Palette:pixelate ](<./Palette-pixelate.md> "Palette:pixelate")• [Palette:pixelRelocator ](<./Palette-pixelRelocator.md> "Palette:pixelRelocator")• [Palette:pointGenerator ](<./Palette-pointGenerator.md> "Palette:pointGenerator")• [Palette:pointillize ](<./Palette-pointillize.md> "Palette:pointillize")• [Palette:pointMerge ](<./Palette-pointMerge.md> "Palette:pointMerge")• [Palette:pointRender ](<./Palette-pointRender.md> "Palette:pointRender")• [Palette:pointRepack ](<./Palette-pointRepack.md> "Palette:pointRepack")• [Palette:pointTransform ](<./Palette-pointTransform.md> "Palette:pointTransform")• [Palette:pointWeight ](<./Palette-pointWeight.md> "Palette:pointWeight")• [Palette:popDialog ](<./Palette-popDialog.md> "Palette:popDialog")• [Palette:probe ](<./Palette-probe.md> "Palette:probe")• [Palette:projectorBlend ](<./Palette-projectorBlend.md> "Palette:projectorBlend")• [Palette:pushPins ](<./Palette-pushPins.md> "Palette:pushPins")• [Palette:puzzle ](<./Palette-puzzle.md> "Palette:puzzle")• [Palette:quadReproject ](<./Palette-quadReproject.md> "Palette:quadReproject")• [Palette:radialBlur ](<./Palette-radialBlur.md> "Palette:radialBlur")• [Palette:recorder ](<./Palette-recorder.md> "Palette:recorder")• [Palette:remotePanel ](<./Palette-remotePanel.md> "Palette:remotePanel")• [Palette:rgbaBlur ](<./Palette-rgbaBlur.md> "Palette:rgbaBlur")• [Palette:rgbaDelay ](<./Palette-rgbaDelay.md> "Palette:rgbaDelay")• [Palette:rgbContrast ](<./Palette-rgbContrast.md> "Palette:rgbContrast")• Palette:sceneChanger • [Palette:search ](<./Palette-search.md> "Palette:search")• [Palette:searchReplace ](<./Palette-searchReplace.md> "Palette:searchReplace")• [Palette:sharpen ](<./Palette-sharpen.md> "Palette:sharpen")• [Palette:sickEngine ](<./Palette-sickEngine.md> "Palette:sickEngine")• [Palette:signalingClient ](<./Palette-signalingClient.md> "Palette:signalingClient")• [Palette:signalingServer ](<./Palette-signalingServer.md> "Palette:signalingServer")• [Palette:softenAlpha ](<./Palette-softenAlpha.md> "Palette:softenAlpha")• [Palette:solarize ](<./Palette-solarize.md> "Palette:solarize")• [Palette:sopRender ](<./Palette-sopRender.md> "Palette:sopRender")• [Palette:splitter ](<./Palette-splitter.md> "Palette:splitter")• [Palette:stitcher ](<./Palette-stitcher.md> "Palette:stitcher")• [Palette:stoner ](<./Palette-stoner.md> "Palette:stoner")• [Palette:superFormula ](<./Palette-superFormula.md> "Palette:superFormula")• [Palette:SVG ](<./Palette-SVG.md> "Palette:SVG")• [Palette:sweetSpot ](<./Palette-sweetSpot.md> "Palette:sweetSpot")• [Palette:sweetSpotPreviz ](<./Palette-sweetSpotPreviz.md> "Palette:sweetSpotPreviz")• [Palette:synchroCache ](<./Palette-synchroCache.md> "Palette:synchroCache")• [Palette:synchroClient ](<./Palette-synchroClient.md> "Palette:synchroClient")• [Palette:synchroFrameIn ](<./Palette-synchroFrameIn.md> "Palette:synchroFrameIn")• [Palette:synchroFrameOut ](<./Palette-synchroFrameOut.md> "Palette:synchroFrameOut")• [Palette:synchroNDIIn ](<./Palette-synchroNDIIn.md> "Palette:synchroNDIIn")• [Palette:synchroSDIIn ](<./Palette-synchroSDIIn.md> "Palette:synchroSDIIn")• [Palette:synchroVideoOut ](<./Palette-synchroVideoOut.md> "Palette:synchroVideoOut")• [Palette:tdBitwigPackage ](<./Palette-tdBitwigPackage.md> "Palette:tdBitwigPackage")• [Palette:tdPyEnvManager ](<./Palette-tdPyEnvManager.md> "Palette:tdPyEnvManager")• [Palette:TDVR ](<./Palette-TDVR.md> "Palette:TDVR")• [Palette:testGrid ](<./Palette-testGrid.md> "Palette:testGrid")• [Palette:threadManagerClient ](<./Palette-threadManagerClient.md> "Palette:threadManagerClient")• [Palette:threadsMonitor ](<./Palette-threadsMonitor.md> "Palette:threadsMonitor")• [Palette:transitMap ](<./Palette-transitMap.md> "Palette:transitMap")• [Palette:twirl ](<./Palette-twirl.md> "Palette:twirl")• [Palette:vectorScope ](<./Palette-vectorScope.md> "Palette:vectorScope")• [Palette:virtualFile ](<./Palette-virtualFile.md> "Palette:virtualFile")• [Palette:waveformMonitor ](<./Palette-waveformMonitor.md> "Palette:waveformMonitor")• [Palette:webBrowser ](<./Palette-webBrowser.md> "Palette:webBrowser")• [Palette:webRTC ](<./Palette-webRTC.md> "Palette:webRTC")• [Palette:webRTCPanel ](<./Palette-webRTCPanel.md> "Palette:webRTCPanel")• [Palette:webRTCPanelRcv ](<./Palette-webRTCPanelRcv.md> "Palette:webRTCPanelRcv")• [Palette:xyScope ](<./Palette-xyScope.md> "Palette:xyScope")• [Thread Manager ](<./Thread_Manager.md> "Thread Manager")
