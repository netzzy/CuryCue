# Palette:webRTC

##   
  
Summary

The WebRTC COMP is a component that can be used to initiate real-time communications (RTC) between TouchDesigner instances and TouchDesigner or WebRTC compatible devices such as most Web browser capable devices, including some IoT devices. 

It **requires** a [signalingClient COMP](<./Palette-signalingClient.md> "Palette:signalingClient") connected to a [supported signaling server](<./Palette-signalingServer.md> "Palette:signalingServer"). 

Before getting started with WebRTC, it is highly recommended to give a read to the introduction available on [MDN Web Docs](<https://developer.mozilla.org/en-US/docs/Web/API/WebRTC_API/Protocols>). 

Reading this doc will help you get familiar with some of the vocabulary used in our WebRTC related docs. 

There is a large consortium of actors working around WebRTC. With that in mind, TouchDesigner will attempts to not reinvent it in a way that would make it too different from what is already heavily documented. We have wrapped some of the features and flow available in the WebRTC API (native in modern web browsers) as well as the Media Capture and Streams API. 

What it means for WebRTC in TouchDesigner: for most of the methods, variable names, callbacks... etc used, it should match the WebRTC API and / or the Media Capture and Streams API. 

i.e.`onNegotiationNeeded`method in the webRTC COMP extension, is an event callback firing when one end of an RTCPeerConnection is requiring re-negotiation. If you go to MDN, you will easily find more details about`onNegotiationNeeded`with just a copy / paste of the method name. 

The WebRTC API is detailed here: <https://developer.mozilla.org/en-US/docs/Web/API/WebRTC_API>

The MediaStream API is detailed here: <https://developer.mozilla.org/en-US/docs/Web/API/Media_Streams_API>

**Known issues:**
* Because the Video Stream In / Out TOPs and Audio Stream In / Out CHOPs (some of the underlying operators of this component) are relying on Libwebrtc's own encoder / decoder and the library does not support hardware encoding / decoding, passing high resolution video can be resource intensive and users should be cautious. We are working on a solution to improve performances.


[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[Palette:webRTC Ext](<./Palette-webRTC_Ext.md> "Palette:webRTC Ext")

## 

Good to know

### 

Signaling

Signaling is part of the WebRTC discovery and negotiation process. 

While we do follow the recommended flows and messaging styles available at MDN and / or Google, including "Perfect Negotiation", there are a few nuances in our signaling process that does not make the WebRTC COMP plug'n'play with other Signaling APIs. 

While we plan to add support for Unity and Unreal Engine versions of Signaling in the future (which are both different), advanced users will likely want to just take inspiration from the webRTC COMP and its [WebRTCExt](<./Palette-webRTC_Ext.md> "Palette:webRTC Ext") and adapt those to their own signaling needs. 

i.e. You could run a pre-existing signaling server in NodeJS rather than our [signalingServer COMP](<./Palette-signalingServer.md> "Palette:signalingServer"), and use a protocol different than WebSocket for exchanging messages, such as XMPP. 

On the other hand, advanced users could also adapt signaling servers outside of TouchDesigner while still following our own Signaling API. 

More details about the Signaling API are available [at the following page](<./Palette-signalingServer.md> "Palette:signalingServer"). 

### 

TURN/STUN

A STUN (Session Traversal Utilities for NAT) is used to discover your public IP address and determine whether or not your NAT is open for this protocol and the required ports. 

You can specify a STUN Server in the WebRTC COMP parameters dialog. **Note** : The default is a public STUN provided by Google. It is **highly advised** not to use this server in a production context. 

A TURN (Traversal Using Relays around NAT) server could help in achieving a reliable connection between two or more peers and bypass NAT restrictions. 

You can specify one TURN Server URL and Username / password in the WebRTC COMP parameters dialog. Additional TURN Servers can be added to the [WebRTC DAT](<./WebRTC_DAT.md> "WebRTC DAT") in the webRTC COMP. 

### 

Security

Encryption is a mandatory feature of WebRTC. All components used in the WebRTC context are exchanging encrypted data. 

Note that if you are concerned about security, a user should at the very least use a secured WebSocket (wss) connection at the signaling server level as well. 

That being said, there are security considerations around WebRTC and its underlying technologies. Advanced users should read the following draft, especially when using WebRTC on a public network: <https://datatracker.ietf.org/doc/html/rfc8826>

## 

Shortcomings and other considerations

Consider this component a playground, demo and experiment. Note that it is used in conjunction with our [signalingClient COMP](<./Palette-signalingClient.md> "Palette:signalingClient") and [signalingServer COMP](<./Palette-signalingServer.md> "Palette:signalingServer"), fully peer to peer. 

Due to the complexity and the variety of applications around [WebRTC](<./WebRTC.md> "WebRTC"), it is highly likely that this component could not be used (or at least, not fully) in a production context and environment. 

One of the main concerns here would be scalability. 

In most cases, you will want to rely on what we often refer to as SFU (Selective Forwarding Unit) or MCU (Multipoint Conferencing Units) to handle large groups of sources. A few names to look into or consider are [AntMedia](<https://antmedia.io/>), [Jitsi Videobridge](<https://jitsi.org/jitsi-videobridge/>), [Kurento](<https://www.kurento.org/>), [Janus](<https://github.com/meetecho/janus-gateway>).. etc 

While we didn't test this specific use case, advanced users _could_ consider running TouchDesigner as an SFU or MCU. 

Another important point is that it is likely that you will encounter firewall restrictions and a closed or moderate NAT. Proper STUN (and optionally TURN) server configurations should help with that. We recommend [Coturn](<https://github.com/coturn/coturn>) as a private TURN server. 

## 

Setup

To start a WebRTC connection between two TouchDesigner instances, either locally or on the local network, only the Palette components from the WebRTC folder are required. 

In this example, we will consider two TouchDesigner processes running on the same machine, A and B. 

In process A, drag n drop the signalingServer from the Palette → Change its Active par to ON. 

In process A, drag n drop a signalingClient from the Palette → Change its Active par to ON. Change its Forward to Subscribers par to ON. 

In process A, drag n drop a webRTC COMP from the Palette → Reference the signalingClient COMP to the webRTC COMP's signalingClient par. 

In process B, drag n drop a signalingClient from the Palette → Change its Active par to ON. Change its Forward to Subscribers par to ON. 

In process B, drag n drop a webRTC COMP from the Palette → Reference the signalingClient COMP to the webRTC COMP's signalingClient par. 

Now if you look at the signalingServer, you’ll see 2 signalingClients showing up. 

On each signalingClient, you will see the other signalingClient. 

On each WebRTC COMP, you will see the other client (the client that represents a signalingClient which is not the one assigned to the WebRTC COMP you are looking at) 

You just have to go in active mode to start a call. 

## 

Track Manager

In the WebRTC COMP viewer, after initializing a connection from a peer to another, click the manage tracks button. 

Here, you can see all the current tracks, per connections, of the WebRTC COMP. 

Using the ID dropdown menu at the bottom of the window, you can filter tracks per connection IDs. You can manually delete tracks using the RemoveTrack button in the table. 

Finally, using the form at the bottom, you can add tracks of various types. Tip: You can drag an OP of a type matching the Type dropdown to the Source field. 

## 

dataChannels

When first initializing a connection from one WebRTC COMP to another, a default dataChannel is set. You can interact with the viewer of the WebRTC COMP with mouse clicks / moves and the position is being sent over a "Mouse" dataChannel. On the receiving end, a circle/pointer is being drawn and composited back into the image. 

Additionally, you can go in the track manager (described in the previous section) and add a new dataChannel. Name the dataChannel`GenericCHOP`(respect spelling, case sensitive) and select its type from the dropdown menu to be`dataChannel:CHOP`. Last, create a CHOP of **5 channels of 1 sample each, non time-sliced**. **All those are mandatory as well and important for the example to work, we will describe why later**. You can now click`Add`. 

On the receiving end of the connection, add a Select CHOP and enter the following expression: 
[code]
    op('webRTC/receiver/item1').findChildren(parValue='GenericCHOP', parName='Label')[0]
    
[/code]

You are receiving over the connection your CHOP channels. Behind the scene, the sender converted the CHOP channels to a NumPy Array, and converted the NumPy Array to a bytearray to be sent over the dataChannel. The receiver does the conversion back from bytearray, to NumPy Array, to CHOP channels. Because we are sending data that can be totally arbitrary and working with bytearrays over the network, this example is not activated by default and values are hardcoded (to support 5 channels of 1 sample) so that the receiver can convert everything back to the CHOP pipeline. 

If you wish to adapt this example, you can edit the [Palette:webRTC_Ext](<./Palette-webRTC_Ext.md> "Palette:webRTC Ext") extension and add a new method named`onDataReceived`followed by your channel name. i.e. If we want to add a dataChannel named`Animal`, the method name would be`onDataReceivedAnimal`. You can then take inspiration on the`onDataReceivedGenericCHOP`method and change the shape of the NumPy Array using the NumPy method`numpyArray.reshape()`. 

## 

Signaling message types specific to WebRTC

Those signaling messages are following the standards as set and detailed in the [Palette:signalingServer](<./Palette-signalingServer.md> "Palette:signalingServer") Signaling API section. They also have matching JSON Schema files. 

### 

signalingType - Offer

A signaling message sent from a client with a WebRTC Offer to another client, and transiting through the signaling server. 

The signaling message type property should be set to`Offer`, and an SDP should be set in the sdp property of the content dictionnary. 
[code] 
    "content": {
       "sdp": "The Session Description protocol (SDP) of the local peer following a WebRTC offer"
    }
    
[/code]

### 

signalingType - Answer

A signaling message sent from a client with a WebRTC Answer to another client, and transiting through the signaling server. 

The signaling message type property should be set to`Answer`, and an SDP should be set in the sdp property of the content dictionnary. 
[code] 
    "content": {
       "sdp": "The Session Description protocol (SDP) of the local peer following a WebRTC answer"
    }
    
[/code]

### 

signalingType - Ice

A signaling message sent from a client with a WebRTC Ice to another client, and transiting through the signaling server. 

The signaling message type property should be set to`Ice`, and a dictionnary describing a candidate should be set in the sdpCandidate, sdpMLineIndex, sdpMid properties of the content dictionnary. 
[code] 
    "content": {
       "sdpCandidate": "The Session Description protocol (SDP) Candidate of the local peer following a WebRTC RTCIceCandidate event"
       "sdpMLineIndex": "The index of the media description of the SDP candidate following a WebRTC RTCIceCandidate event"
       "sdpMid": "The media stream identification of the SDP candidate following a WebRTC RTCIceCandidate event"
    }
    
[/code]

## 

Parameters - WebRTC Page

Signaling Client`Signalingclient`\- The signaling client with which this WebRTC COMP will subscribe to send or receive signaling messages. 

Default Tracks Behaviour`Defaulttracksbehaviour`\- ⊞ \- When starting an RTCPeerConnection, initiate the negotiation with default tracks. Various default combinations are available. 
* 1V1A1DC`1V1A1DC`-
* 1V0A0DC`1V0A0DC`-
* 0V1A0DC`0V1A0DC`-
* 1V0A1DC`1V0A1DC`-
* 0V1A1DC`0V1A1DC`-
* 1V1A0DC`1V1A0DC`-


STUN Server URL`Stun`\- URL of the STUN server. 

TURN Server URL`Turn0`\- URL of the TURN server. See [WebRTC#ICE](<./WebRTC.htm#ICE> "WebRTC") for more details regarding TURN. 

TURN Username`Username`\- Username for access to the specified TURN servers. 

TURN Password`Password`\- Password for access to the specified TURN servers. 

Reset`Reset`\- Reset the WebRTC COMP states and kill all ongoing peer connections. 

Signaling API Version`Signalingapiversion`\- The Signaling API version. When a signaling client is being used, the API versions of both the server and client should match. 

## 

Parameters - Logger Page

Enable Logging`Enablelogging`\- Enable advanced logging features. Useful to debug and track the WebRTC COMP activity. 

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

Help`Help`\- Open Help page in external browser. 

Version`Version`\- The component version number. 

TouchDesigner Build: Latest\n2022.24140before 2022.24140

Palette  
---  
[Palette ](<./Palette.md> "Palette")• [Palette:arcBallCamera ](<./Palette-arcBallCamera.md> "Palette:arcBallCamera")• [Palette:arcBallGeometry ](<./Palette-arcBallGeometry.md> "Palette:arcBallGeometry")• [Palette:audioAnalysis ](<./Palette-audioAnalysis.md> "Palette:audioAnalysis")• [Palette:audioSet ](<./Palette-audioSet.md> "Palette:audioSet")• [Palette:autoMediaPlayer ](<./Palette-autoMediaPlayer.md> "Palette:autoMediaPlayer")• [Palette:battery ](<./Palette-battery.md> "Palette:battery")• [Palette:bitwigClip ](<./Palette-bitwigClip.md> "Palette:bitwigClip")• [Palette:bitwigClipSlot ](<./Palette-bitwigClipSlot.md> "Palette:bitwigClipSlot")• [Palette:bitwigDeviceRemotes ](<./Palette-bitwigDeviceRemotes.md> "Palette:bitwigDeviceRemotes")• [Palette:bitwigMain ](<./Palette-bitwigMain.md> "Palette:bitwigMain")• [Palette:bitwigNote ](<./Palette-bitwigNote.md> "Palette:bitwigNote")• [Palette:bitwigProjectRemotes ](<./Palette-bitwigProjectRemotes.md> "Palette:bitwigProjectRemotes")• [Palette:bitwigRemotesDevice ](<./Palette-bitwigRemotesDevice.md> "Palette:bitwigRemotesDevice")• [Palette:bitwigRemotesProject ](<./Palette-bitwigRemotesProject.md> "Palette:bitwigRemotesProject")• [Palette:bitwigRemotesTrack ](<./Palette-bitwigRemotesTrack.md> "Palette:bitwigRemotesTrack")• [Palette:bitwigSelect ](<./Palette-bitwigSelect.md> "Palette:bitwigSelect")• [Palette:bitwigSong ](<./Palette-bitwigSong.md> "Palette:bitwigSong")• [Palette:bitwigTrack ](<./Palette-bitwigTrack.md> "Palette:bitwigTrack")• [Palette:bitwigTrackRemotes ](<./Palette-bitwigTrackRemotes.md> "Palette:bitwigTrackRemotes")• [Palette:blendModes ](<./Palette-blendModes.md> "Palette:blendModes")• [Palette:bloom ](<./Palette-bloom.md> "Palette:bloom")• [Palette:camera ](<./Palette-camera.md> "Palette:camera")• [Palette:cameraBrowser ](<./Palette-cameraBrowser.md> "Palette:cameraBrowser")• [Palette:cameraViewport ](<./Palette-cameraViewport.md> "Palette:cameraViewport")• [Palette:camSchnappr ](<./Palette-camSchnappr.md> "Palette:camSchnappr")• [Palette:changeColor ](<./Palette-changeColor.md> "Palette:changeColor")• [Palette:changeToColor ](<./Palette-changeToColor.md> "Palette:changeToColor")• [Palette:checker ](<./Palette-checker.md> "Palette:checker")• [Palette:chromaKey ](<./Palette-chromaKey.md> "Palette:chromaKey")• [Palette:colorThreshold ](<./Palette-colorThreshold.md> "Palette:colorThreshold")• [Palette:compareComp ](<./Palette-compareComp.md> "Palette:compareComp")• [Palette:convolve ](<./Palette-convolve.md> "Palette:convolve")• [Palette:cornerPinPOP ](<./Palette-cornerPinPOP.md> "Palette:cornerPinPOP")• [Palette:cornerPinSOP ](<./Palette-cornerPinSOP.md> "Palette:cornerPinSOP")• [Palette:cppParsTemplateGen ](<./Palette-cppParsTemplateGen.md> "Palette:cppParsTemplateGen")• [Palette:customAttributes ](<./Palette-customAttributes.md> "Palette:customAttributes")• [Palette:debugControl ](<./Palette-debugControl.md> "Palette:debugControl")• [Palette:dent ](<./Palette-dent.md> "Palette:dent")• [Palette:depthExtract ](<./Palette-depthExtract.md> "Palette:depthExtract")• [Palette:depthProjection ](<./Palette-depthProjection.md> "Palette:depthProjection")• [Palette:dilate ](<./Palette-dilate.md> "Palette:dilate")• [Palette:domeViewer ](<./Palette-domeViewer.md> "Palette:domeViewer")• [Palette:encoder ](<./Palette-encoder.md> "Palette:encoder")• [Palette:equalizer ](<./Palette-equalizer.md> "Palette:equalizer")• [Palette:feedback ](<./Palette-feedback.md> "Palette:feedback")• [Palette:feedbackEdge ](<./Palette-feedbackEdge.md> "Palette:feedbackEdge")• [Palette:firmata ](<./Palette-firmata.md> "Palette:firmata")• [Palette:gal ](<./Palette-gal.md> "Palette:gal")• [Palette:geoPanel ](<./Palette-geoPanel.md> "Palette:geoPanel")• [Palette:gestureCapture ](<./Palette-gestureCapture.md> "Palette:gestureCapture")• [Palette:graphPlot ](<./Palette-graphPlot.md> "Palette:graphPlot")• [Palette:histogram ](<./Palette-histogram.md> "Palette:histogram")• [Palette:hsvBlur ](<./Palette-hsvBlur.md> "Palette:hsvBlur")• [Palette:imageSearch ](<./Palette-imageSearch.md> "Palette:imageSearch")• [Palette:julia ](<./Palette-julia.md> "Palette:julia")• [Palette:kantanMapper ](<./Palette-kantanMapper.md> "Palette:kantanMapper")• [Palette:kinectCalibration ](<./Palette-kinectCalibration.md> "Palette:kinectCalibration")• [Palette:kinectPointcloud ](<./Palette-kinectPointcloud.md> "Palette:kinectPointcloud")• [Palette:leapPaint ](<./Palette-leapPaint.md> "Palette:leapPaint")• [Palette:lightTunnel ](<./Palette-lightTunnel.md> "Palette:lightTunnel")• [Palette:logger ](<./Palette-logger.md> "Palette:logger")• [Palette:mandelbrot ](<./Palette-mandelbrot.md> "Palette:mandelbrot")• [Palette:materialDesignIcons ](<./Palette-materialDesignIcons.md> "Palette:materialDesignIcons")• [Palette:mesh ](<./Palette-mesh.md> "Palette:mesh")• [Palette:monochrome ](<./Palette-monochrome.md> "Palette:monochrome")• [Palette:motionSense ](<./Palette-motionSense.md> "Palette:motionSense")• [Palette:movieEngine ](<./Palette-movieEngine.md> "Palette:movieEngine")• [Palette:moviePlayer ](<./Palette-moviePlayer.md> "Palette:moviePlayer")• [Palette:moviePlaylist ](<./Palette-moviePlaylist.md> "Palette:moviePlaylist")• [Palette:multiLevel ](<./Palette-multiLevel.md> "Palette:multiLevel")• [Palette:multiMix ](<./Palette-multiMix.md> "Palette:multiMix")• [Palette:noise ](<./Palette-noise.md> "Palette:noise")• [Palette:onScreenKeyboard ](<./Palette-onScreenKeyboard.md> "Palette:onScreenKeyboard")• [Palette:operatorPath ](<./Palette-operatorPath.md> "Palette:operatorPath")• [Palette:opticalFlow ](<./Palette-opticalFlow.md> "Palette:opticalFlow")• [Palette:particlesGpu ](<./Palette-particlesGpu.md> "Palette:particlesGpu")• [Palette:pixelate ](<./Palette-pixelate.md> "Palette:pixelate")• [Palette:pixelRelocator ](<./Palette-pixelRelocator.md> "Palette:pixelRelocator")• [Palette:pointGenerator ](<./Palette-pointGenerator.md> "Palette:pointGenerator")• [Palette:pointillize ](<./Palette-pointillize.md> "Palette:pointillize")• [Palette:pointMerge ](<./Palette-pointMerge.md> "Palette:pointMerge")• [Palette:pointRender ](<./Palette-pointRender.md> "Palette:pointRender")• [Palette:pointRepack ](<./Palette-pointRepack.md> "Palette:pointRepack")• [Palette:pointTransform ](<./Palette-pointTransform.md> "Palette:pointTransform")• [Palette:pointWeight ](<./Palette-pointWeight.md> "Palette:pointWeight")• [Palette:popDialog ](<./Palette-popDialog.md> "Palette:popDialog")• [Palette:probe ](<./Palette-probe.md> "Palette:probe")• [Palette:projectorBlend ](<./Palette-projectorBlend.md> "Palette:projectorBlend")• [Palette:pushPins ](<./Palette-pushPins.md> "Palette:pushPins")• [Palette:puzzle ](<./Palette-puzzle.md> "Palette:puzzle")• [Palette:quadReproject ](<./Palette-quadReproject.md> "Palette:quadReproject")• [Palette:radialBlur ](<./Palette-radialBlur.md> "Palette:radialBlur")• [Palette:recorder ](<./Palette-recorder.md> "Palette:recorder")• [Palette:remotePanel ](<./Palette-remotePanel.md> "Palette:remotePanel")• [Palette:rgbaBlur ](<./Palette-rgbaBlur.md> "Palette:rgbaBlur")• [Palette:rgbaDelay ](<./Palette-rgbaDelay.md> "Palette:rgbaDelay")• [Palette:rgbContrast ](<./Palette-rgbContrast.md> "Palette:rgbContrast")• [Palette:sceneChanger ](<./Palette-sceneChanger.md> "Palette:sceneChanger")• [Palette:search ](<./Palette-search.md> "Palette:search")• [Palette:searchReplace ](<./Palette-searchReplace.md> "Palette:searchReplace")• [Palette:sharpen ](<./Palette-sharpen.md> "Palette:sharpen")• [Palette:sickEngine ](<./Palette-sickEngine.md> "Palette:sickEngine")• [Palette:signalingClient ](<./Palette-signalingClient.md> "Palette:signalingClient")• [Palette:signalingServer ](<./Palette-signalingServer.md> "Palette:signalingServer")• [Palette:softenAlpha ](<./Palette-softenAlpha.md> "Palette:softenAlpha")• [Palette:solarize ](<./Palette-solarize.md> "Palette:solarize")• [Palette:sopRender ](<./Palette-sopRender.md> "Palette:sopRender")• [Palette:splitter ](<./Palette-splitter.md> "Palette:splitter")• [Palette:stitcher ](<./Palette-stitcher.md> "Palette:stitcher")• [Palette:stoner ](<./Palette-stoner.md> "Palette:stoner")• [Palette:superFormula ](<./Palette-superFormula.md> "Palette:superFormula")• [Palette:SVG ](<./Palette-SVG.md> "Palette:SVG")• [Palette:sweetSpot ](<./Palette-sweetSpot.md> "Palette:sweetSpot")• [Palette:sweetSpotPreviz ](<./Palette-sweetSpotPreviz.md> "Palette:sweetSpotPreviz")• [Palette:synchroCache ](<./Palette-synchroCache.md> "Palette:synchroCache")• [Palette:synchroClient ](<./Palette-synchroClient.md> "Palette:synchroClient")• [Palette:synchroFrameIn ](<./Palette-synchroFrameIn.md> "Palette:synchroFrameIn")• [Palette:synchroFrameOut ](<./Palette-synchroFrameOut.md> "Palette:synchroFrameOut")• [Palette:synchroNDIIn ](<./Palette-synchroNDIIn.md> "Palette:synchroNDIIn")• [Palette:synchroSDIIn ](<./Palette-synchroSDIIn.md> "Palette:synchroSDIIn")• [Palette:synchroVideoOut ](<./Palette-synchroVideoOut.md> "Palette:synchroVideoOut")• [Palette:tdBitwigPackage ](<./Palette-tdBitwigPackage.md> "Palette:tdBitwigPackage")• [Palette:tdPyEnvManager ](<./Palette-tdPyEnvManager.md> "Palette:tdPyEnvManager")• [Palette:TDVR ](<./Palette-TDVR.md> "Palette:TDVR")• [Palette:testGrid ](<./Palette-testGrid.md> "Palette:testGrid")• [Palette:threadManagerClient ](<./Palette-threadManagerClient.md> "Palette:threadManagerClient")• [Palette:threadsMonitor ](<./Palette-threadsMonitor.md> "Palette:threadsMonitor")• [Palette:transitMap ](<./Palette-transitMap.md> "Palette:transitMap")• [Palette:twirl ](<./Palette-twirl.md> "Palette:twirl")• [Palette:vectorScope ](<./Palette-vectorScope.md> "Palette:vectorScope")• [Palette:virtualFile ](<./Palette-virtualFile.md> "Palette:virtualFile")• [Palette:waveformMonitor ](<./Palette-waveformMonitor.md> "Palette:waveformMonitor")• [Palette:webBrowser ](<./Palette-webBrowser.md> "Palette:webBrowser")• Palette:webRTC • [Palette:webRTCPanel ](<./Palette-webRTCPanel.md> "Palette:webRTCPanel")• [Palette:webRTCPanelRcv ](<./Palette-webRTCPanelRcv.md> "Palette:webRTCPanelRcv")• [Palette:xyScope ](<./Palette-xyScope.md> "Palette:xyScope")• [Thread Manager ](<./Thread_Manager.md> "Thread Manager")
