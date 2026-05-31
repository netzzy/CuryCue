# Palette:webRTC Ext

These Extensions reference a specific [Palette:webRTC](<./Palette-webRTC.md> "Palette:webRTC"). The extension of the webRTC COMP. 

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

# WebRTCExt

The WebRTCExt constructor drives the WebRTC COMP and exposes various promoted methods in addition to holding data during a WebRTC session between the local peer and one or more remote peers. 

## Members`Connections`→`List[Connection]`: 

> A list of Connection objects that are currently in the same WebRTC session as the webRTC COMP.`CurrentConnections`→`DAT`: 

> A reference to a DAT, copy of the Connections member.`CurrentTracks`→`DAT`: 

> A reference to a DAT. It lists all Track objects stored on each Connection object in the`track`member.`SignalingClient`→`COMP`: 

> A reference to the signalingClient COMP the webRTC COMP is relying on.`SignalingClientMessagesTypes`→`List[str]`: 

> A list of message types used for WebRTC specific signaling. Those types are passed when the webRTC COMP is subscribing to the signalingClient COMP.`WebRTCDAT`→`DAT`: 

> A reference to the [WebRTC DAT](<./WebRTC_DAT.md> "WebRTC DAT") that is at the core of the webRTC COMP.

## Methods`WebRTCExt.AddDataChannel(connection: WebRTCExt.Connection, dataChannelLabel: str, source=None)`→`None`: 

> Called to add a DataChannel 
> 
> Args: 
> 
>   * connection (Connection): A Connection object on which to add the DataChannel
>   * dataChannelLabel (str): A label to identify the DataChannel over the RTCPeerConnection
>   * source (op, optional): An operator compatible with DataChannels. Must be a DAT or a CHOP. Only DATs are fully supported. Defaults to None.
>`WebRTCExt.AddTrack(connection: WebRTCExt.Connection, trackLabel: str, direction: str, trackType: str, source=None)`→`None`: 

> Main method to add a track. 
> 
> In the WebRTC COMP context, it is called when setting up default tracks while initializing the RTCPeerConnection. It is also called following a click event to add a track from the Track Manager. 
> 
> Args: 
> 
>   * connection (Connection): A Connection object on which to add the track.
>   * trackLabel (str): The Label of the track with which the track can be identified over the RTCPeerConnection.
>   * direction (str): Tracks being unidirectional, this argument is used to identify whether the track is incoming and is added following an onAddTrack event, or whether it is outgoing and was added by this end of the RTCPeerConnection.
>   * trackType (str): Whether the track is an audio or video track.
>   * source (OP, optional): Mandatory when the track is outgoing. This can be a CHOP for an audio track or a TOP for a video track. Defaults to None.
>`WebRTCExt.GetConnectionById(id: str)`→`WebRTCExt.Connection`: 

> Return a Connection object, if a valid Connection object matching the specified connection ID was found in the current list of Connections. 
> 
> Args: 
> 
>   * id (str): The ID of the RTCPeerConnection
> 

> 
> Returns: 
> 
>   * Optional[Connection]: The Connection object matching the specified connection ID. None if no matching Connection was found.
>`WebRTCExt.GetConnectionByTargetAddress(targetAddress: str)`→`WebRTCExt.Connection`: 

> Return a Connection object, if a valid Connection object matching the specified target address was found in the current list of Connections. 
> 
> Args: 
> 
>   * targetAddress (str): The ip:port combo of the remote end of the RTCPeerConnection
> 

> 
> Returns: 
> 
>   * Optional[Connection]: The Connection object matching the specified target address.
>`WebRTCExt.GetConnectionByTargetId(targetId: str)`→`WebRTCExt.Connection`: 

> Return a Connection object, if a valid Connection object matching the specified target ID was found in the current list of Connections. 
> 
> Args: 
> 
>   * targetId (str): The ID of the remote end of the RTCPeerConnection
> 

> 
> Returns: 
> 
>   * Optional[Connection]: The Connection object matching the specified connection ID. None if no matching Connection was found.
>`WebRTCExt.GetConnectionIndexById(connectionId: str)`→`int`: 

> Return the index of the Connection object within the list of Connections, if a valid Connection object matching the specified ID was found. 
> 
> Args: 
> 
>   * connectionId (str): The ID of the Connection object.
> 

> 
> Returns: 
> 
>   * int: The index in the current list of Connections.
>`WebRTCExt.GetDataChannelById(connection: WebRTCExt.Connection, dataChannelId: str)`→`WebRTCExt.Track`: 

> Return a DataChannel on the specified Connection object that matches the specified dataChannel ID. 
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
>`WebRTCExt.GetDataChannelsByLabel(connection: WebRTCExt.Connection, dataChannelLabel: str)`→`List[WebRTCExt.Track]`: 

> Return a list of DataChannels (Track objects) on the specified Connection object that match the specified dataChannel Label. 
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
>`WebRTCExt.GetTrackById(connection: WebRTCExt.Connection, trackId: str)`→`WebRTCExt.Track or None`: 

> Return a track on the specified Connection object that match the specified track ID. 
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
>`WebRTCExt.GetTrackByLabel(connection: WebRTCExt.Connection, trackLabel: str)`→`WebRTCExt.Track or None`: 

> Return a track on the specified Connection object that match the specified track Label. 
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
>`WebRTCExt.OnCallEnd(id: str)`→`None`: 

> End an ongoing PeerConnection between self and a remote peer by providing a connection ID. 
> 
> Args: 
> 
>   * id (str): The ID of the PeerConnection to end.
>`WebRTCExt.OnCallStart(id: str)`→`None`: 

> Start a PeerConnection between self and a remote peer based on a remote client ID. 
> 
> Args: 
> 
>   * id (str): The ID of the client to call.
>`WebRTCExt.OnMessageReceived(message: dict)`→`None`: 

> An arbitrary message was passed from the SignalingClient to the WebRTC COMP. 
> 
> This message was passed because the WebRTC COMP is likely subscribed to a signalingClient COMP. This method is Promoted and called from the SignalingClient, **it should not be used directly by advanced users.**
> 
> Users should instead add custom signaling message types and subscribe to the signalingClient COMP with a new type array. Then, new custom methods can be created and **prefixed by`onMessageReceived`followed by the signaling message type**. 
> 
> Args: 
> 
>   * message (dict): A dictionary following the Signaling messaging API and complying to the JSON Schema.
>`WebRTCExt.onDataReceived(connectionId: str, channelName: str, data: bytearray)`→`None`: 

> An arbitrary dataChannel update was received from another peer over a connection. 
> 
> This message was passed because this peer likely has an open dataChannel with another peer. **This method should not be used directly by advanced users.**
> 
> Users should instead add a custom method to the webRTCExt class. The new method named`onDataReceived`followed by your channel name. 
> 
> i.e. If we want to add a dataChannel named`Animal`, the method name would be`onDataReceivedAnimal`. You can then take inspiration on the`onDataReceivedMouse`or`onDataReceivedGenericCHOP`methods. 
> 
> The`onDataReceivedMouse`method is an example of DAT data being sent over a dataChannel. You can use the helpers method related to DAT to JSON and JSON to DAT to attempt to convert / read the data on both ends of the RTCPeerConnection. If you want to take a different approach when **sending** the DAT data over a dataChannel, the SendData method should be modified or extended. (i.e. A custom SendDataChannelName method would be a good approach, where ChannelName is the name of your new dataChannel). 
> 
> The`onDataReceivedGenericCHOP`method is an example of CHOP data being sent over a dataChannel. The code can be used as your base for your new method, but change the shape of the NumPy Array using the NumPy method`numpyArray.reshape()`to match the shape of the numPy Array you are sending. i.e. Sending 3 channels of 100 samples would be`numpyArray.reshape(3, 100)`.`WebRTCExt.RemoveDataChannel(connection: WebRTCExt.Connection, dataChannelId: str=None, dataChannelLabel: str=None)`→`None`: 

> Remove a DataChannel from the specified Connection object and close it on the RTCPeerConnection. 
> 
> Args: 
> 
>   * connection (Connection): The specified Connection object that owns the DataChannels
>   * dataChannelId (str, optional): A DataChannel ID that matches a DataChannel in the Connection object. Defaults to None.
>   * dataChannelLabel (str, optional): A DataChannel Label that matches a DataChannel in the Connection object. Defaults to None.
>`WebRTCExt.RemoveTrack(connection: WebRTCExt.Connection, trackId: str=None, trackLabel: str=None)`→`None`: 

> Main method to remove a track. Can be called externally. While both trackId and trackLabel are optional arguments, one or the other must be filled and match a track object available in the passed Connection object. 
> 
> Args: 
> 
>   * connection (Connection): A Connection object on which to remove the track
>   * trackId (str, optional): The ID of the track to be removed. Defaults to None.
>   * trackLabel (str, optional): The Label of the track to be removed. Defaults to None.
>`WebRTCExt.Reset(self)`→`None`: 

> Reset the WebRTC session and all states of the WebRTC COMP and its WebRTCExt.`WebRTCExt.SendData(connectionId: str, channelName: str, family: str, bytesArray: bytearray=None, jsonDict: dict=None, target=None)`: 

> A promoted method to be used to send arbitrary data over a RTCDataChannel, provided a valid RTCPeerConnection ID and a valid RTCDataChannel label. 
> 
> If connectionId is specified, the DataChannel used will be over this connectionIdIf no connectionId is specified but a target is specified, the DataChannel used will be on the connection with the matching target. 
> 
> NOTE: Sending Data here, is using WebRTC DataChannels, it is not to be mixed up with the Signaling messages, therefore, the JSON string being sent doesn't follow a specific API and doesn't contain an API Version. 
> 
> Args: 
> 
>   * connectionId (str): The ID of the RTCPeerConnection on which the RTCDataChannel data is transiting.
>   * channelName (str): The name of the RTCDataChannel on this end of the RTCPeerConnection.
>   * family (str): The OP family name to be used. DATs are converted to valid JSON while CHOPs are byteArrays. **(experimental)**
>   * bytesArray (bytearray, optional): The bytesArray used when the data being exchanged is from CHOPs.
>   * jsonDict (dict, optional): The JSON dict used when the data being exchanged is from DATs.
>   * target (Client, optional): An optional argument to be used if no connectionId (None) was passed.
>`WebRTCExt.Subscribe(signalingClient=None)`→`bool`: 

> This method is called on init of the WebRTCExt or when the signalingClient Par changed. 
> 
> It is using the Subscribe features of the signalingClient COMP. 
> 
> Args: 
> 
>   * signalingClient (COMP, optional): An optional signalingClient COMP. Attempt to use an already registered signalingClient COMP when None was passed. Defaults to None.
> 

> 
> Returns: 
> 
>   * bool: Whether the subscription to the SignalingClient succeeded or not.
> 


TouchDesigner Build: Latest\nmw-removed-redirectmw-new-redirectmw-changed-redirect-targetmw-changed-redirect-target2022.24140
