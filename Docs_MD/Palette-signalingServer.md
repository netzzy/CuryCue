# Palette:signalingServer

## 

Summary

The signalingServer COMP is a component that can be used to run a signaling server within TouchDesigner. 

A signaling server is used as an intermediary between clients to route arbitrary messages between a client A and a client B, where A and B don't know how to reach each other and should "signal" themselves. 

More details about the Signaling API are available in this page at the Signaling API section. The current communication protocol is WebSocket. 

It is often used as part of WebRTC sessions. 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[Palette:signalingServer Ext](<./Palette-signalingServer_Ext.md> "Palette:signalingServer Ext")

## 

Signaling API

The Signaling API is describing the message types being exchanged between a signaling server and its clients or between client and client when they are routing message through the signaling server. 

If a 3rd party application wishes to connect with TouchDesigner's own signaling server, the messages being exchanged should comply with the Signaling API described in the following section. 

Note that some components can be developed to subscribe to signaling messages through the [signalingClient COMP](<./Palette-signalingClient.md> "Palette:signalingClient")`Subscribe(`) method. 

i.e. The WebRTC COMP is subscribing to messages being exchanged through the signaling server and clients, and complying with the Signaling API. 

### 

JSON Schema

**Available in version 1.0.0 and above**. All signaling messages implemented in the current Signaling API have a matching [JSON Schema](<https://json-schema.org/>) file. 

Making use of those schemas, a user can validate its signaling messages before sending them to the server. 

On the signalingServer COMP and the signalingClient COMP, find the JSON Schema related parameters. You can validate messages being sent from / to each signaling components. While you would likely **not use schema validation in a production environment** , they are useful during development. 

When signaling messages are failing to be parsed by the target of the message, you will get detailed information if for some reason your message is not complying with our API. It is particularly useful if you write a signalingClient from scratch in another environment than TouchDesigner and wish to connect with the signalingServer we provide. 

We provide a default endpoint where the signalingServer and signalingClient COMPs can fetch the schemas. If you do not have an internet connection or if the endpoint is unavailable for some reason, you can find the latest schema versions at the top of this page or in [this GitHub repository](<https://github.com/TouchDesigner/SignalingAPI>). While we try to keep the following section describing signaling messages up to date, the one source of truth will always be in this GitHub repository. 

The repository also includes Signaling messages schemas for signalingTypes specific to the [WebRTC COMP](<./Palette-webRTC.md> "Palette:webRTC"). 

**Note:** When using remote schemas, we attempt to cache the schemas (and some related objects necessary to validation) progressively as new signaling message types are being sent / received. This cache can be emptied when pulsing the "Clear schema cache" parameter of the component. The same caching occurs on the [Palette:signalingClient](<./Palette-signalingClient.md> "Palette:signalingClient") COMP as well. With that in mind, note that the first few messages being exchanged could trigger frame drops. 

When using local schema files, the cache is being built when the folder to the schema files is being set or changing using the "Local Schema Folder" parameter. You can clear the cache as well and it will be rebuilt on the next signaling messages exchange. 

### 

Signaling messages, base structure.

All signaling messages have the mandatory properties: 
* metadata - The mandatory metadata dictionary describing the API version and its origin
  * signalingType - The type of signaling message that is being sent or received (ClientEnter, ClientEntered, ClientExit, Clients)
  * content - The content of the message being carried over the signaling API


Additionally, the following properties can be present for some specific message types: 
* sender - The sender address in the format IP:port as perceived by the signaling server
  * target - The target address in the format IP:port as set by the sender

### 

Metadata

The metadata dictionary is made of the following mandatory properties: 
* apiVersion - The version number of the Signaling API being implemented
  * compVersion - The version number of the component, or the external application version number, from which the message originated
  * compOrigin - The path of the component within the TouchDesigner project, or the URI of an external application, from which the message originated
  * projectName - The name of the TouchDesigner project, or external application, from which the message originated

### 

signalingType - ClientEnter

A signaling message sent from the signaling server to clients in the signaling session to make them aware that a client entered the signaling session. 

The signaling message type property should be set to`ClientEnter`, and a Client dictionary should be set in the client property of the content dictionary. 
[code] 
    "content": {
       "client": {
          "id":"The unique identifier of the client generated by the signaling server when entering the signaling session",
          "address":"The address of the client as perceived by the signaling server in the IP:port format",
          "properties":"An arbitrary dictionary that can be used to carry custom properties across the signaling protocol. A 'domain' property should be available in the object."
       }
    }
    
[/code]

### 

signalingType - ClientEntered

A signaling message sent from the signaling server to a client to acknowledge that the client entered the signaling session and was registered by the signaling server. 

The signaling message type property should be set to`ClientEntered`, and a Client dictionary should be set in the self property of the content dictionary. 
[code] 
    "content": {
       "self": {
          "id":"The unique identifier of the client generated by the signaling server when entering the signaling session",
          "address":"The address of the client as perceived by the signaling server in the IP:port format",
          "properties": "An arbitrary dictionary that can be used to carry custom properties across the signaling protocol. A 'domain' property should be available in the object."
       }
    }
    
[/code]

### 

signalingType - ClientExit

A signaling message sent from the signaling server to clients in the signaling session to make them aware that a client left the signaling session 

The signaling message type property should be set to`ClientExit`, and a Client ID should be set in the id property of the content dictionary. 
[code] 
    "content": {
          "client": {
             "id":"The unique identifier of the client generated by the signaling server when entering the signaling session",
             "address":"The address of the client as perceived by the signaling server in the IP:port format",
             "properties": "An arbitrary dictionary that can be used to carry custom properties across the signaling protocol. A 'domain' property should be available in the object."
       }
    }
    
[/code]

### 

signalingType - Clients

A signaling message sent from the signaling server to a client to make it aware of other signaling clients within the signaling session 

The signaling message type property should be set to`Clients`, and a list of clients should be set in the clients property of the content dictionary. 
[code] 
    "content": {
       "clients": [{
       "id":"The unique identifier of the client generated by the signaling server when entering the signaling session",
       "address":"The address of the client as perceived by the signaling server in the IP:port format",
       "properties":"An arbitrary dictionary that can be used to carry custom properties across the signaling protocol. A 'domain' property should be available in the object."
       }]
    }
    
[/code]

## 

Parameters - Signaling Server Page

Active`Active`\- Start or stop the signaling server. 

Restart`Restart`\- Restart the signaling server and reset all states. 

Port`Port`\- Port on which the signaling clients can connect to the signaling server and on which the signaling server can receive messages. 

Secure (TLS)`Secure`\- When enabled, this will force clients to connect to the signaling server using TLS and exchange messages securely. 

Private Key File Path`Privatekey`\- The required private key when the signaling server should be secure. 

Certificate File Path`Certificate`\- The required certificate when the signaling server should be secure. 

Certificate Password`Password`\- The required certificate password when the signaling server should be secure. 

Pass Through`Passthrough`\- When enabled, if messages sent to the server do not have the property`target`, the messages are broadcasted to all clients in the signaling session and on the same domain. 

Use JSON Schema In`Usejsonschemain`\- Validate incoming Signaling API messages against JSON Schema. 

Use JSON Schema Out`Usejsonschemaout`\- Validate outgoing Signaling API messages against JSON Schema. 

Use local RefResolver`Uselocalrefresolver`\- Use JSON Schema files installed locally rather than validating from remote sources. Schema files available at <https://github.com/TouchDesigner/SignalingAPI>

Local Schema Folder`Localschemafolder`\- A folder where the JSON Schema files for the Signaling API are available locally. 

Clear schema cache`Clearschemacache`\- Signaling API schema files are loaded once. Clearing the cache force them to reload on the next call that requires JSON Schema. 

Signaling API Version`Signalingapiversion`\- The Signaling API version. When a signaling client is being used, the API version of both the server and client should match. 

Signaling API Schema Endpoint`Signalingapischemaendpoint`\- The endpoint being used to fetch the JSON Schema files. 

## 

Parameters - Logger Page

Enable Log`Enablelogging`\- Enable advanced log features. Useful to debug and track the signaling server activity. 

Log to File`Logtofile`\- When enabled, log messages will be written to a time rotated log file. 

Log Folder`Logfolder`\- Path to the folder in which the log files should be written. 

File Rotation`Filerotation`\- Number of backup files to be kept when rotating log. 

Log to Textport`Logtotextport`\- When enabled, log messages will be displayed in the textport. 

Log to Status Bar`Logtostatusbar`\- When enabled, log messages will be displayed in the status bar. 

Log Level`Loglevel`\- ⊞ \- Filter level of log messages. The selected level is included as well as all levels above. I.e. if Warning is selected, Warning and Error messages will be included while Info messages will be excluded. 
* INFO`INFO`-
* DEBUG`DEBUG`-
* WARNING`WARNING`-
* ERROR`ERROR`-
* CRITICAL`CRITICAL`-

## 

Parameters - About Page

Help`Help`\- Open COMP Help page in external browser. 

Version`Version`\- The COMP version number. 

TouchDesigner Build: Latest\nwikieditor2022.24140before 2022.24140

Palette  
---  
[Palette ](<./Palette.md> "Palette")• [Palette:arcBallCamera ](<./Palette-arcBallCamera.md> "Palette:arcBallCamera")• [Palette:arcBallGeometry ](<./Palette-arcBallGeometry.md> "Palette:arcBallGeometry")• [Palette:audioAnalysis ](<./Palette-audioAnalysis.md> "Palette:audioAnalysis")• [Palette:audioSet ](<./Palette-audioSet.md> "Palette:audioSet")• [Palette:autoMediaPlayer ](<./Palette-autoMediaPlayer.md> "Palette:autoMediaPlayer")• [Palette:battery ](<./Palette-battery.md> "Palette:battery")• [Palette:bitwigClip ](<./Palette-bitwigClip.md> "Palette:bitwigClip")• [Palette:bitwigClipSlot ](<./Palette-bitwigClipSlot.md> "Palette:bitwigClipSlot")• [Palette:bitwigDeviceRemotes ](<./Palette-bitwigDeviceRemotes.md> "Palette:bitwigDeviceRemotes")• [Palette:bitwigMain ](<./Palette-bitwigMain.md> "Palette:bitwigMain")• [Palette:bitwigNote ](<./Palette-bitwigNote.md> "Palette:bitwigNote")• [Palette:bitwigProjectRemotes ](<./Palette-bitwigProjectRemotes.md> "Palette:bitwigProjectRemotes")• [Palette:bitwigRemotesDevice ](<./Palette-bitwigRemotesDevice.md> "Palette:bitwigRemotesDevice")• [Palette:bitwigRemotesProject ](<./Palette-bitwigRemotesProject.md> "Palette:bitwigRemotesProject")• [Palette:bitwigRemotesTrack ](<./Palette-bitwigRemotesTrack.md> "Palette:bitwigRemotesTrack")• [Palette:bitwigSelect ](<./Palette-bitwigSelect.md> "Palette:bitwigSelect")• [Palette:bitwigSong ](<./Palette-bitwigSong.md> "Palette:bitwigSong")• [Palette:bitwigTrack ](<./Palette-bitwigTrack.md> "Palette:bitwigTrack")• [Palette:bitwigTrackRemotes ](<./Palette-bitwigTrackRemotes.md> "Palette:bitwigTrackRemotes")• [Palette:blendModes ](<./Palette-blendModes.md> "Palette:blendModes")• [Palette:bloom ](<./Palette-bloom.md> "Palette:bloom")• [Palette:camera ](<./Palette-camera.md> "Palette:camera")• [Palette:cameraBrowser ](<./Palette-cameraBrowser.md> "Palette:cameraBrowser")• [Palette:cameraViewport ](<./Palette-cameraViewport.md> "Palette:cameraViewport")• [Palette:camSchnappr ](<./Palette-camSchnappr.md> "Palette:camSchnappr")• [Palette:changeColor ](<./Palette-changeColor.md> "Palette:changeColor")• [Palette:changeToColor ](<./Palette-changeToColor.md> "Palette:changeToColor")• [Palette:checker ](<./Palette-checker.md> "Palette:checker")• [Palette:chromaKey ](<./Palette-chromaKey.md> "Palette:chromaKey")• [Palette:colorThreshold ](<./Palette-colorThreshold.md> "Palette:colorThreshold")• [Palette:compareComp ](<./Palette-compareComp.md> "Palette:compareComp")• [Palette:convolve ](<./Palette-convolve.md> "Palette:convolve")• [Palette:cornerPinPOP ](<./Palette-cornerPinPOP.md> "Palette:cornerPinPOP")• [Palette:cornerPinSOP ](<./Palette-cornerPinSOP.md> "Palette:cornerPinSOP")• [Palette:cppParsTemplateGen ](<./Palette-cppParsTemplateGen.md> "Palette:cppParsTemplateGen")• [Palette:customAttributes ](<./Palette-customAttributes.md> "Palette:customAttributes")• [Palette:debugControl ](<./Palette-debugControl.md> "Palette:debugControl")• [Palette:dent ](<./Palette-dent.md> "Palette:dent")• [Palette:depthExtract ](<./Palette-depthExtract.md> "Palette:depthExtract")• [Palette:depthProjection ](<./Palette-depthProjection.md> "Palette:depthProjection")• [Palette:dilate ](<./Palette-dilate.md> "Palette:dilate")• [Palette:domeViewer ](<./Palette-domeViewer.md> "Palette:domeViewer")• [Palette:encoder ](<./Palette-encoder.md> "Palette:encoder")• [Palette:equalizer ](<./Palette-equalizer.md> "Palette:equalizer")• [Palette:feedback ](<./Palette-feedback.md> "Palette:feedback")• [Palette:feedbackEdge ](<./Palette-feedbackEdge.md> "Palette:feedbackEdge")• [Palette:firmata ](<./Palette-firmata.md> "Palette:firmata")• [Palette:gal ](<./Palette-gal.md> "Palette:gal")• [Palette:geoPanel ](<./Palette-geoPanel.md> "Palette:geoPanel")• [Palette:gestureCapture ](<./Palette-gestureCapture.md> "Palette:gestureCapture")• [Palette:graphPlot ](<./Palette-graphPlot.md> "Palette:graphPlot")• [Palette:histogram ](<./Palette-histogram.md> "Palette:histogram")• [Palette:hsvBlur ](<./Palette-hsvBlur.md> "Palette:hsvBlur")• [Palette:imageSearch ](<./Palette-imageSearch.md> "Palette:imageSearch")• [Palette:julia ](<./Palette-julia.md> "Palette:julia")• [Palette:kantanMapper ](<./Palette-kantanMapper.md> "Palette:kantanMapper")• [Palette:kinectCalibration ](<./Palette-kinectCalibration.md> "Palette:kinectCalibration")• [Palette:kinectPointcloud ](<./Palette-kinectPointcloud.md> "Palette:kinectPointcloud")• [Palette:leapPaint ](<./Palette-leapPaint.md> "Palette:leapPaint")• [Palette:lightTunnel ](<./Palette-lightTunnel.md> "Palette:lightTunnel")• [Palette:logger ](<./Palette-logger.md> "Palette:logger")• [Palette:mandelbrot ](<./Palette-mandelbrot.md> "Palette:mandelbrot")• [Palette:materialDesignIcons ](<./Palette-materialDesignIcons.md> "Palette:materialDesignIcons")• [Palette:mesh ](<./Palette-mesh.md> "Palette:mesh")• [Palette:monochrome ](<./Palette-monochrome.md> "Palette:monochrome")• [Palette:motionSense ](<./Palette-motionSense.md> "Palette:motionSense")• [Palette:movieEngine ](<./Palette-movieEngine.md> "Palette:movieEngine")• [Palette:moviePlayer ](<./Palette-moviePlayer.md> "Palette:moviePlayer")• [Palette:moviePlaylist ](<./Palette-moviePlaylist.md> "Palette:moviePlaylist")• [Palette:multiLevel ](<./Palette-multiLevel.md> "Palette:multiLevel")• [Palette:multiMix ](<./Palette-multiMix.md> "Palette:multiMix")• [Palette:noise ](<./Palette-noise.md> "Palette:noise")• [Palette:onScreenKeyboard ](<./Palette-onScreenKeyboard.md> "Palette:onScreenKeyboard")• [Palette:operatorPath ](<./Palette-operatorPath.md> "Palette:operatorPath")• [Palette:opticalFlow ](<./Palette-opticalFlow.md> "Palette:opticalFlow")• [Palette:particlesGpu ](<./Palette-particlesGpu.md> "Palette:particlesGpu")• [Palette:pixelate ](<./Palette-pixelate.md> "Palette:pixelate")• [Palette:pixelRelocator ](<./Palette-pixelRelocator.md> "Palette:pixelRelocator")• [Palette:pointGenerator ](<./Palette-pointGenerator.md> "Palette:pointGenerator")• [Palette:pointillize ](<./Palette-pointillize.md> "Palette:pointillize")• [Palette:pointMerge ](<./Palette-pointMerge.md> "Palette:pointMerge")• [Palette:pointRender ](<./Palette-pointRender.md> "Palette:pointRender")• [Palette:pointRepack ](<./Palette-pointRepack.md> "Palette:pointRepack")• [Palette:pointTransform ](<./Palette-pointTransform.md> "Palette:pointTransform")• [Palette:pointWeight ](<./Palette-pointWeight.md> "Palette:pointWeight")• [Palette:popDialog ](<./Palette-popDialog.md> "Palette:popDialog")• [Palette:probe ](<./Palette-probe.md> "Palette:probe")• [Palette:projectorBlend ](<./Palette-projectorBlend.md> "Palette:projectorBlend")• [Palette:pushPins ](<./Palette-pushPins.md> "Palette:pushPins")• [Palette:puzzle ](<./Palette-puzzle.md> "Palette:puzzle")• [Palette:quadReproject ](<./Palette-quadReproject.md> "Palette:quadReproject")• [Palette:radialBlur ](<./Palette-radialBlur.md> "Palette:radialBlur")• [Palette:recorder ](<./Palette-recorder.md> "Palette:recorder")• [Palette:remotePanel ](<./Palette-remotePanel.md> "Palette:remotePanel")• [Palette:rgbaBlur ](<./Palette-rgbaBlur.md> "Palette:rgbaBlur")• [Palette:rgbaDelay ](<./Palette-rgbaDelay.md> "Palette:rgbaDelay")• [Palette:rgbContrast ](<./Palette-rgbContrast.md> "Palette:rgbContrast")• [Palette:sceneChanger ](<./Palette-sceneChanger.md> "Palette:sceneChanger")• [Palette:search ](<./Palette-search.md> "Palette:search")• [Palette:searchReplace ](<./Palette-searchReplace.md> "Palette:searchReplace")• [Palette:sharpen ](<./Palette-sharpen.md> "Palette:sharpen")• [Palette:sickEngine ](<./Palette-sickEngine.md> "Palette:sickEngine")• [Palette:signalingClient ](<./Palette-signalingClient.md> "Palette:signalingClient")• Palette:signalingServer • [Palette:softenAlpha ](<./Palette-softenAlpha.md> "Palette:softenAlpha")• [Palette:solarize ](<./Palette-solarize.md> "Palette:solarize")• [Palette:sopRender ](<./Palette-sopRender.md> "Palette:sopRender")• [Palette:splitter ](<./Palette-splitter.md> "Palette:splitter")• [Palette:stitcher ](<./Palette-stitcher.md> "Palette:stitcher")• [Palette:stoner ](<./Palette-stoner.md> "Palette:stoner")• [Palette:superFormula ](<./Palette-superFormula.md> "Palette:superFormula")• [Palette:SVG ](<./Palette-SVG.md> "Palette:SVG")• [Palette:sweetSpot ](<./Palette-sweetSpot.md> "Palette:sweetSpot")• [Palette:sweetSpotPreviz ](<./Palette-sweetSpotPreviz.md> "Palette:sweetSpotPreviz")• [Palette:synchroCache ](<./Palette-synchroCache.md> "Palette:synchroCache")• [Palette:synchroClient ](<./Palette-synchroClient.md> "Palette:synchroClient")• [Palette:synchroFrameIn ](<./Palette-synchroFrameIn.md> "Palette:synchroFrameIn")• [Palette:synchroFrameOut ](<./Palette-synchroFrameOut.md> "Palette:synchroFrameOut")• [Palette:synchroNDIIn ](<./Palette-synchroNDIIn.md> "Palette:synchroNDIIn")• [Palette:synchroSDIIn ](<./Palette-synchroSDIIn.md> "Palette:synchroSDIIn")• [Palette:synchroVideoOut ](<./Palette-synchroVideoOut.md> "Palette:synchroVideoOut")• [Palette:tdBitwigPackage ](<./Palette-tdBitwigPackage.md> "Palette:tdBitwigPackage")• [Palette:tdPyEnvManager ](<./Palette-tdPyEnvManager.md> "Palette:tdPyEnvManager")• [Palette:TDVR ](<./Palette-TDVR.md> "Palette:TDVR")• [Palette:testGrid ](<./Palette-testGrid.md> "Palette:testGrid")• [Palette:threadManagerClient ](<./Palette-threadManagerClient.md> "Palette:threadManagerClient")• [Palette:threadsMonitor ](<./Palette-threadsMonitor.md> "Palette:threadsMonitor")• [Palette:transitMap ](<./Palette-transitMap.md> "Palette:transitMap")• [Palette:twirl ](<./Palette-twirl.md> "Palette:twirl")• [Palette:vectorScope ](<./Palette-vectorScope.md> "Palette:vectorScope")• [Palette:virtualFile ](<./Palette-virtualFile.md> "Palette:virtualFile")• [Palette:waveformMonitor ](<./Palette-waveformMonitor.md> "Palette:waveformMonitor")• [Palette:webBrowser ](<./Palette-webBrowser.md> "Palette:webBrowser")• [Palette:webRTC ](<./Palette-webRTC.md> "Palette:webRTC")• [Palette:webRTCPanel ](<./Palette-webRTCPanel.md> "Palette:webRTCPanel")• [Palette:webRTCPanelRcv ](<./Palette-webRTCPanelRcv.md> "Palette:webRTCPanelRcv")• [Palette:xyScope ](<./Palette-xyScope.md> "Palette:xyScope")• [Thread Manager ](<./Thread_Manager.md> "Thread Manager")
