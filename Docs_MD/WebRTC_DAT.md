# WebRTC DAT

##   
  
Summary

A WebRTC DAT represents a peer on one end of any number of [WebRTC](<./WebRTC.md> "WebRTC") peer-to-peer connections. 

Each connection is represented in TouchDesigner by a generated UUID. The UUID must be passed to [WebrtcDAT Class](<./WebrtcDAT_Class.md> "WebrtcDAT Class") connection-level python methods. 

The WebRTC DAT output is a table formatted with a row per connection, with columns: id (ie. UUID), [connection_state](<https://developer.mozilla.org/en-US/docs/Web/API/RTCPeerConnection/connectionState>), [signaling_state](<https://developer.mozilla.org/en-US/docs/Web/API/RTCPeerConnection/signalingState>), [ice_connection_state](<https://developer.mozilla.org/en-US/docs/Web/API/RTCPeerConnection/iceConnectionState>), and [ice_gathering_state](<https://developer.mozilla.org/en-US/docs/Web/API/RTCPeerConnection/iceGatheringState>). 

The columns altogether describe the state of a connection and can also be useful for debugging. For example, if ice_connection_state failed then that means there's an issue pairing local and remote ICE candidates for streaming over the network. It could be that NAT traversal failed, and if using a STUN server that might indicate a need for a TURN server (see <https://en.wikipedia.org/wiki/STUN#Limitations>). 

WebRTC video and audio input/output is done via the [Video Stream In TOP](<./Video_Stream_In_TOP.md> "Video Stream In TOP"), [Video Stream Out TOP](<./Video_Stream_Out_TOP.md> "Video Stream Out TOP"), [Audio Stream In CHOP](<./Audio_Stream_In_CHOP.md> "Audio Stream In CHOP"), and [Audio Stream Out CHOP](<./Audio_Stream_Out_CHOP.md> "Audio Stream Out CHOP"). 

See also [WebRTC](<./WebRTC.md> "WebRTC"). 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[webrtcDAT_Class](<./WebrtcDAT_Class.md> "WebrtcDAT Class")

## 

Parameters - Connection Page

Active`active`\- When active, can connect to peers and send media/data. When deactivated, all existing connections will be closed. 

Reset`reset`\- Resets the peer associated with the DAT. Equivalent to deactivating then reactivating the active parameter. 

Custom Bit Rate Limits`bitratelimits`\- When enabled, custom min/max bit rates can be specified. These max bit rate limits are expressed in kbps and apply to all tracks associated with the WebRTC DAT. 

Minimum Bit Rate (kbps)`minbitrate`\- Minimum bit rate for all tracks associated with the WebRTC DAT. 

Maximum Bit Rate (kbps)`maxbitrate`\- Maximum bit rate for all tracks associated with the WebRTC DAT. 

Callbacks DAT`callbacks`\- Reference to a DAT containing WebRTC callbacks. 

## 

Parameters - ICE Page

STUN Server URL`stun`\- URL of the STUN server. See [WebRTC#ICE](<./WebRTC.htm#ICE> "WebRTC") for more details regarding STUN. 

TURN Username`username`\- Username for access to the specified TURN servers. 

TURN Password`password`\- Password for access to the specified TURN servers. 

TURN Server`turn`\- Sequence of TURN server urls. 

TURN Server URL 0`turn0server`\- URL of the TURN server. See [WebRTC#ICE](<./WebRTC.htm#ICE> "WebRTC") for more details regarding TURN. 

## 

Parameters - Common Page

Language`language`\- ⊞ \- Select how the DAT decides which script language to operate on. 
* Input`input`\- The DAT uses the inputs script language.
* Node`node`\- The DAT uses it's own script language.


Edit/View Extension`extension`\- ⊞ \- Select the file extension this DAT should expose to external editors. 
* dat`dat`\- various common file extensions.
* frag`frag`-
* glsl`glsl`-
* html`html`-
* md`md`-
* py`py`-
* rtf`rtf`-
* tsv`tsv`-
* txt`txt`-
* vert`vert`-
* xml`xml`-
* From Language`languageext`\- pick extension from DATs script language.
* Custom Extension`customext`\- Specify a custom extension.


Custom Extension`customext`\- Specifiy the custom extension. 

Word Wrap`wordwrap`\- ⊞ \- Enable Word Wrap for Node Display. 
* Input`input`\- The DAT uses the inputs setting.
* On`on`\- Turn on Word Wrap.
* Off`off`\- Turn off Word Wrap.


TouchDesigner Build: Latest\nwikieditorwikieditor2022.24140before 2022.24140

DATs   
---  
[Art-Net ](<./Art-Net_DAT.md> "Art-Net DAT")• [Audio Devices ](<./Audio_Devices_DAT.md> "Audio Devices DAT")• [CHOP Execute ](<./CHOP_Execute_DAT.md> "CHOP Execute DAT")• [CHOP to ](<./CHOP_to_DAT.md> "CHOP to DAT")• [Clip ](<./Clip_DAT.md> "Clip DAT")• [Convert ](<./Convert_DAT.md> "Convert DAT")• [CPlusPlus ](<./CPlusPlus_DAT.md> "CPlusPlus DAT")• [DAT ](<./DAT.md> "DAT")• [ Execute ](<./DAT_Execute_DAT.md> "DAT Execute DAT")• [DAT Export ](<./DAT_Export.md> "DAT Export")• [Error ](<./Error_DAT.md> "Error DAT")• [EtherDream ](<./EtherDream_DAT.md> "EtherDream DAT")• [Evaluate ](<./Evaluate_DAT.md> "Evaluate DAT")• [Examine ](<./Examine_DAT.md> "Examine DAT")• [Execute ](<./Execute_DAT.md> "Execute DAT")• [FIFO ](<./FIFO_DAT.md> "FIFO DAT")• [File In ](<./File_In_DAT.md> "File In DAT")• [File Out ](<./File_Out_DAT.md> "File Out DAT")• [Folder ](<./Folder_DAT.md> "Folder DAT")• [In ](<./In_DAT.md> "In DAT")• [Indices ](<./Indices_DAT.md> "Indices DAT")• [Info ](<./Info_DAT.md> "Info DAT")• [Insert ](<./Insert_DAT.md> "Insert DAT")• [JSON ](<./JSON_DAT.md> "JSON DAT")• [Keyboard In ](<./Keyboard_In_DAT.md> "Keyboard In DAT")• [Lookup ](<./Lookup_DAT.md> "Lookup DAT")• [Media File Info ](<./Media_File_Info_DAT.md> "Media File Info DAT")• [Merge ](<./Merge_DAT.md> "Merge DAT")• [MIDI Event ](<./MIDI_Event_DAT.md> "MIDI Event DAT")• [MIDI In ](<./MIDI_In_DAT.md> "MIDI In DAT")• [Monitors ](<./Monitors_DAT.md> "Monitors DAT")• [MPCDI ](<./MPCDI_DAT.md> "MPCDI DAT")• [MQTT Client ](<./MQTT_Client_DAT.md> "MQTT Client DAT")• [Multi Touch In ](<./Multi_Touch_In_DAT.md> "Multi Touch In DAT")• [NDI ](<./NDI_DAT.md> "NDI DAT")• [Null ](<./Null_DAT.md> "Null DAT")• [OP Execute ](<./OP_Execute_DAT.md> "OP Execute DAT")• [OP Find ](<./OP_Find_DAT.md> "OP Find DAT")• [OSC In ](<./OSC_In_DAT.md> "OSC In DAT")• [OSC Out ](<./OSC_Out_DAT.md> "OSC Out DAT")• [Out ](<./Out_DAT.md> "Out DAT")• [Panel Execute ](<./Panel_Execute_DAT.md> "Panel Execute DAT")• [Parameter ](<./Parameter_DAT.md> "Parameter DAT")• [Parameter Execute ](<./Parameter_Execute_DAT.md> "Parameter Execute DAT")• [ParGroup Execute ](<./ParGroup_Execute_DAT.md> "ParGroup Execute DAT")• [Perform ](<./Perform_DAT.md> "Perform DAT")• [POP to ](<./POP_to_DAT.md> "POP to DAT")• [Render Pick ](<./Render_Pick_DAT.md> "Render Pick DAT")• [Reorder ](<./Reorder_DAT.md> "Reorder DAT")• [Script ](<./Script_DAT.md> "Script DAT")• [Select ](<./Select_DAT.md> "Select DAT")• [Serial ](<./Serial_DAT.md> "Serial DAT")• [Serial Devices ](<./Serial_Devices_DAT.md> "Serial Devices DAT")• [SocketIO ](<./SocketIO_DAT.md> "SocketIO DAT")• [SOP to ](<./SOP_to_DAT.md> "SOP to DAT")• [Sort ](<./Sort_DAT.md> "Sort DAT")• [Substitute ](<./Substitute_DAT.md> "Substitute DAT")• [Switch ](<./Switch_DAT.md> "Switch DAT")• [Table ](<./Table_DAT.md> "Table DAT")• [TCP/IP ](<./TCP/IP_DAT.md> "TCP/IP DAT")• [Text ](<./Text_DAT.md> "Text DAT")• [Touch In ](<./Touch_In_DAT.md> "Touch In DAT")• [Touch Out ](<./Touch_Out_DAT.md> "Touch Out DAT")• [Transpose ](<./Transpose_DAT.md> "Transpose DAT")• [TUIO In ](<./TUIO_In_DAT.md> "TUIO In DAT")• [UDP In ](<./UDP_In_DAT.md> "UDP In DAT")• [UDP Out ](<./UDP_Out_DAT.md> "UDP Out DAT")• [UDT In ](<./UDT_In_DAT.md> "UDT In DAT")• [UDT Out ](<./UDT_Out_DAT.md> "UDT Out DAT")• [Video Devices ](<./Video_Devices_DAT.md> "Video Devices DAT")• [Web Client ](<./Web_Client_DAT.md> "Web Client DAT")• [Web ](<./Web_DAT.md> "Web DAT")• [Web Server ](<./Web_Server_DAT.md> "Web Server DAT")• WebRTC • [WebSocket ](<./WebSocket_DAT.md> "WebSocket DAT")• [XML ](<./XML_DAT.md> "XML DAT")
