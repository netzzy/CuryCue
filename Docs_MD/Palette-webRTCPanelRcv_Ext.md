# Palette:webRTCPanelRcv Ext

These Extensions reference a specific [Palette:webRTCPanelRcv](<./Palette-webRTCPanelRcv.md> "Palette:webRTCPanelRcv"). The extension of the webRTCPanelRcv COMP.   
  
# Track

The Track class describes a WebRTC Track, including Data Channels, within the context of its connection, from the point of view of the current peer. 

It does not follow exactly the MediaStream API MediaStreamTrack class as there are some tweaks specific to TouchDesigner. 

## Members`id`→`str`: 

> The id attribute is passed to the createTrack method of the WebRTC DAT when creating a track. In version 0.0.1, if a Track was created following an onTrack event, it means that it is an incoming track - in that case, the id will be a UUID provided by the WebRTC DAT.`label`→`str`: 

> The label attribute will match the ID for outgoing tracks, which could be human readable. In version 0.0.1, the incoming track label will be a UUID matching the ID.`direction`→`str`: 

> Tracks are unidirectional, when they are not dataChannels. The direction attribute can be either 'in', or 'out'. In the case of dataChannels, two tracks are added, one 'in' and one 'out'.`type`→`str`: 

> The type attribute describes whether we are dealing with an audio track, a video track, or a dataChannel.`source`→`str`: 

> The source attribute is only used for outgoing tracks. TOP for video, CHOP for audio, and DAT for DataChannels. CHOP data is partially supported for DataChannels and would be sent out as a byteArray.`family`→`str`: 

> The family attribute describes what type of DataChannel is being sent out.

# Connection

The Connection class describes a WebRTC Connection, from the point of view of the current peer. 

It does not follow exactly the WebRTC API RTCPeerConnection class as they are some tweaks specific to TouchDesigner. 

## Members`id`→`str`: 

> The id attribute is returned by the WebRTC DAT when calling openConnection(). If None, an issue likely occurred while opening the RTCPeerConnection.`sender`→`SignalingClientExt.Client`: 

> The sender attribute should always point to the [SignalingClientExt.Client](<./Palette-signalingClient_Ext.md> "Palette:signalingClient Ext") object stored in the SignalingClientExt.AsClient variable.`target`→`SignalingClientExt.Client`: 

> The target attribute is the remote end of the connection, as a [SignalingClientExt.Client](<./Palette-signalingClient_Ext.md> "Palette:signalingClient Ext") object.`polite`→`bool`: 

> The polite attribute is used to avoid offer collisions and complete the perfect negotiation pattern. More details here: <https://developer.mozilla.org/en-US/docs/Web/API/WebRTC_API/Perfect_negotiation>`makingOffer`→`bool`: 

> The makingOffer attribute is also part of the perfect negotiation pattern.`answering`→`bool`: 

> The answering attribute is also part of the perfect negotiation pattern.`tracks`→`List[Track]`: 

> The tracks attribute is listing all incoming and outgoing Track objects, including dataChannels.

# WebRTCPanelRcvExt

## Members`CurrentConnection`→`Connection`: 

> The Connection object representing the current connection between this WebRTCPanel and a receiver.`SignalingClient`→`COMP`: 

> A reference to the signalingClient COMP the webRTCPanelRcv COMP is relying on.`SignalingClientMessagesTypes`→`List[str]`: 

> A list of message types used for WebRTC specific signaling. Those types are passed when the webRTCPanelRcv COMP is subscribing to the signalingClient COMP.`WebRTCDAT`→`DAT`: 

> A reference to the [WebRTC DAT](<./WebRTC_DAT.md> "WebRTC DAT") that is at the core of the webRTCPanelRcv COMP.

## Methods`WebRTCPanelRcvExt.AddDataChannel(connection: WebRTCPanelRcvExt.Connection, dataChannelLabel: str, source=None)`→`None`: 

> Called to add a DataChannel 
> 
> Args: 
> 
>   * connection (Connection): A Connection object on which to add the DataChannel dataChannel
>   * Label (str): A label to identify the DataChannel over the RTCPeerConnection
>   * source (op, optional): An operator compatible with DataChannels. Must be a DAT or a CHOP. Only DATs are fully supported. Defaults to None.
>`WebRTCPanelRcvExt.AddTrack(connection: WebRTCPanelRcvExt.Connection, trackLabel: str, direction: str, trackType: str, source=None)`→`None`: 

> Main method to add a track.In the WebRTCPanelRcv COMP context, it is called when setting up default trackswhile initializing the RTCPeerConnection. It is also called following aclick event to add a track from the Track Manager. 
> 
> Args: 
> 
>   * connection (Connection): A Connection object on which to add the track.
>   * trackLabel (str): The Label of the track with which the track can be identified over the RTCPeerConnection.
>   * direction (str): Tracks being unidirectional, this argument is used to identify whether the track is incoming and is added following an onAddTrack event, or whether it is outgoing and was added by this end of the RTCPeerConnection.
>   * trackType (str): Whether the track is an audio or video track.
>   * source (OP, optional): Mandatory when the track is outgoing. This can be a CHOP for an audio track or a TOP for a video track. Defaults to None.
>`WebRTCPanelRcvExt.GetDataChannelById(connection: WebRTCPanelRcvExt.Connection, dataChannelId: str)`→`Optional[WebRTCPanelRcvExt.Track] or None`: 

> Return a DataChannel on the specified Connection object that matches thespecified dataChannel ID. 
> 
> Args: 
> 
>   * connection (Connection): A Connection object that holds the dataChannel to look for.
>   * dataChannelId (str): The ID of the dataChannel to return.
> 

> 
> Returns: 
> 
>   * Optional[Track]: The track object to return. None if no match was found.
>`WebRTCPanelRcvExt.GetDataChannelsByLabel(connection: WebRTCPanelRcvExt.Connection, dataChannelLabel: str)`→`List[WebRTCPanelRcvExt.Track] or List[]`: 

> Return a list of DataChannels (Track objects) on the specifiedConnection object that match the specified dataChannel Label. 
> 
> Args: 
> 
>   * connection (Connection): A Connection object that holds the dataChannel to look for.
>   * dataChannelLabel (str): The Label of the dataChannel(s) to return.
> 

> 
> Returns: 
> 
>   * List[Track]: A list of DataChannels that are available on the specified Connection and match the specified Label. Return an empty list when no match is found.
>`WebRTCPanelRcvExt.GetTrackById(connection: WebRTCPanelRcvExt.Connection, trackId: str)`→`Optional[WebRTCPanelRcvExt.Track] or None`: 

> Return a track on the specified Connection object that matches thespecified track ID. 
> 
> Args: 
> 
>   * connection (Connection): A Connection object that holds the Track to look for.
>   * trackId (str): The ID of the track to look for.
> 

> 
> Returns: 
> 
>   * Optional[Track]: The track object to return. None if no match was found.
>`WebRTCPanelRcvExt.GetTrackByLabel(connection: WebRTCPanelRcvExt.Connection, trackLabel: str)`→`Optional[WebRTCPanelRcvExt.Track] or None`: 

> Return a track on the specified Connection object that matches thespecified track Label. 
> 
> Args: 
> 
>   * connection (Connection): A Connection object that holds the Track to look for.
>   * trackLabel (str): The Label of the track to look for.
> 

> 
> Returns: 
> 
>   * Optional[Track]: The track object to return. None if no match was found.
>`WebRTCPanelRcvExt.OnMessageReceived(message: dict)`→`None`: 

> An arbitrary message was passed from the SignalingClient to the WebRTCPanelRcv COMP. This message was passed because the WebRTCPanelRcv COMP is likely subscribed toa signalingClient COMP. This method is Promoted and called from theSignalingClient, it should not be used directly by advanced users.Users should instead add custom signaling message types andsubscribe to the signalingClient COMP with a new type array. Then, newcustom methods can be created and prefixed by onMessageReceived followedby the signaling message type. 
> 
> Args: 
> 
>   * message (dict): A dictionary following the Signaling messaging API and complying to the JSON Schema.
>`WebRTCPanelRcvExt.RemoveDataChannel(connection: WebRTCPanelRcvExt.Connection, dataChannelId: str=None, dataChannelLabel: str=None)`→`None`: 

> Remove a DataChannel from the specified Connection object and close iton the RTCPeerConnection. 
> 
> Args: 
> 
>   * connection (Connection): The specified Connection object that ownsthe DataChannels
>   * dataChannelId (str, optional): A DataChannel IDthat matches a DataChannel in the Connection object. Defaults to None.
>   * dataChannelLabel (str, optional): A DataChannel Label that matches aDataChannel in the Connection object. Defaults to None.
>`WebRTCPanelRcvExt.RemoveTrack(connection: WebRTCPanelRcvExt.Connection, trackId: str=None, trackLabel: str=None)`→`None`: 

> Main method to remove a track. Can be called externally. While bothtrackId and trackLabel are optional arguments, one or the other must befilled and match a track object available in the passed Connectionobject. 
> 
> Args: 
> 
>   * connection (Connection): A Connection object on which to remove the track
>   * trackId (str, optional): The ID of the track to be removed. Defaults to None.
>   * trackLabel (str, optional): The Label of the track to be removed. Defaults to None.
>`WebRTCPanelRcvExt.Reset(self)`→`None`: 

> Reset the WebRTC session and all states of the WebRTCPanelRcv COMP and its WebRTCPanelRcvExt.`WebRTCPanelRcvExt.SendData(connectionId, dataChannelName, jsonDict: dict=None)`→`None`: 

> Called by Send*Data. Main method used to send data as JSON over a dataChannel on the connection specified.`WebRTCPanelRcvExt.SendKeyboardData(dat)`→`None`: 

> Method used to send keyboard events over a dataChannel while interacting with a Remote Panel.`WebRTCPanelRcvExt.SendMouseData(dat)`→`None`: 

> Method used to send mouse events over a dataChannel while interacting with a Remote Panel.`WebRTCPanelRcvExt.Subscribe(signalingClient=None) -> bool`→`bool`: 

> This method is called on init of the WebRTCExt or when theSignalingClient Par changed.It is using the Subscribe features of the SignalingClient COMP. 
> 
> Args: 
> 
>   * signalingClient (COMP, optional): An optional SignalingClient COMP. Attempt to use an already registered SignalingClient COMP when None was passed. Defaults to None.
> 

> 
> Returns: 
> 
>   * bool: Whether the subscription to the SignalingClient succeeded or not.
> 


TouchDesigner Build: Latest\nmw-removed-redirectmw-new-redirect2023.11280
