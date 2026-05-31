# TCP/IP DAT

## 

Summary

The TCP/IP DAT is used for sending and receiving information over a TCP/IP connection between two remotely located computers. It captures all the messages without any queuing or buffering, and allows you to send it any messages you want. 

Send messages using the [tcpipDAT_Class](<../TcpipDAT_Class.md> "TcpipDAT Class"). Handle received messages using the callback DAT attached to the TCP/IP DAT. See [Network Protocols](<../Network_Protocols.md> "Network Protocols"). 

This DAT can be used to intercept all the raw information being sent from a Pipe Out CHOP for example. The [Pipe In CHOP](<../Pipe_In_CHOP.md> "Pipe In CHOP") and [Pipe Out CHOP](<../Pipe_Out_CHOP.md> "Pipe Out CHOP") also communicate through a TCP/IP connection, though they use a specific syntax. 

See also [Peer Class](<../Peer_Class.md> "Peer Class"), [UDP In DAT](<../UDP_In_DAT.md> "UDP In DAT"), [UDP Out DAT](<../UDP_Out_DAT.md> "UDP Out DAT"). 

For Tscript. see Tscript`send`Command. 

**NOTE for Windows OS - If experiencing connection issues make sure Windows Firewall is disabled.**

[![PythonIcon.png](../images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[tcpipDAT_Class](<../TcpipDAT_Class.md> "TcpipDAT Class")

## 

Parameters - Connect Page

Connection Mode`mode`\- ⊞ \- Specify if this operator is communicating as a **client** or a **server**. 
* This Operator is Client`client`-
* This Operator is Server`server`-


Network Address`address`\- If this node is communicating as a client, this should be the IP address of the server. 

Port`port`\- The network port to listen on or connect to, depending on of the node is the server or client respectively. 

Shared Connection`shared`\- Use the same connection as other networking DATs using the same network protocol. 

Row/Callback Format`format`\- ⊞ \- Determines how the incoming data is parsed into the table. 
* One Per Byte`perbyte`\- One row is added to the table per byte received.
* One Per Line`perline`\- One row is added to the table per line received. The end of a line is delimited by \n, \r or a null character (\0).   
**Note: In this format messages will not be logged until one of those characters are received.**
* One For All Received Data`all`\- One row is added to the table per message received. Since TCP/IP is a stream-based protocol, the end of a 'message' is arbitrary. It is simply the contents of the last read operation from the socket. If you are reading a custom message format, you'll likely need to build up a full message from multiple reads from the socket in Python.


Active`active`\- This check box enables the connection. 

## 

Parameters - Received Data Page

Callbacks DAT`callbacks`\- The Callbacks DAT will execute once for each message received. 

Execute from`executeloc`\- ⊞ \- Determines the location the script is run from. 
* Current Node`current`\- The script is executed from the current node location.
* Callbacks DAT`callbacks`\- The script is executed from the location of the DAT specified in the Script DAT parameter.
* Specified Operator`op`\- The script is executed from the component specified in the Component parameter below.


From Operator`fromop`\- The component who's state change will trigger the DAT to execute its script when Execute from is set to On Panel Change. This component is also the path that the script will be executed from if the Execute from parameter is set to Specified Component. 

Clamp Output`clamp`\- The DAT is limited to 100 messages by default but with Clamp Output, this can be set to anything including unlimited. 

Maximum Lines`maxlines`\- Limits the number of messages, older messages are removed from the list first. 

Clear Output`clear`\- Deletes all lines except the heading. To clear with a script command, here is an example:`opparm -c /serial1 clear`Bytes Column`bytes`\- Outputs the raw bytes of the message in a separate column. 

## 

Parameters - Common Page

Language`language`\- ⊞ \- Select how the DAT decides which script language to operate on. 
* Input`input`\- The DAT uses the inputs script language.
* Node`node`\- The DAT uses it's own script language.


Edit/View Extension`extension`\- ⊞ \- Select the file extension this DAT should expose to external editors. 
* dat`dat`\- various common file extensions.
* From Language`language`\- pick extension from DATs script language.
* Custom Extension`custom`\- Specify a custom extension.


Custom Extension`customext`\- Specifiy the custom extension. 

Word Wrap`wordwrap`\- ⊞ \- Enable Word Wrap for Node Display. 
* Input`input`\- The DAT uses the inputs setting.
* On`on`\- Turn on Word Wrap.
* Off`off`\- Turn off Word Wrap.

## 

Info CHOP Channels

Extra Information for the TCP/IP DAT can be accessed via an [Info CHOP](<../Info_CHOP.md> "Info CHOP"). 

### 

Specific TCP/IP DAT Info Channels
* connections -
* messages_pending -

### 

Common DAT Info Channels
* num_rows \- Number of rows in this DAT.
* num_cols \- Number of columns in this DAT.

### 

Common Operator Info Channels
* total_cooks \- Number of times the operator has cooked since the process started.
* cook_time \- Duration of the last cook in milliseconds.
* cook_frame \- Frame number when this operator was last cooked relative to the component timeline.
* cook_abs_frame \- Frame number when this operator was last cooked relative to the absolute time.
* cook_start_time \- Time in milliseconds at which the operator started cooking in the frame it was cooked.
* cook_end_time \- Time in milliseconds at which the operator finished cooking in the frame it was cooked.
* cooked_this_frame \- 1 if operator was cooked this frame.
* warnings \- Number of warnings in this operator if any.
* errors \- Number of errors in this operator if any.


  
TouchDesigner Build: Latest\n2021.100002018.28070before 2018.28070

DATs   
---  
[Art-Net ](<../Art-Net_DAT.md> "Art-Net DAT")• [Audio Devices ](<../Audio_Devices_DAT.md> "Audio Devices DAT")• [CHOP Execute ](<../CHOP_Execute_DAT.md> "CHOP Execute DAT")• [CHOP to ](<../CHOP_to_DAT.md> "CHOP to DAT")• [Clip ](<../Clip_DAT.md> "Clip DAT")• [Convert ](<../Convert_DAT.md> "Convert DAT")• [CPlusPlus ](<../CPlusPlus_DAT.md> "CPlusPlus DAT")• [DAT ](<../DAT.md> "DAT")• [ Execute ](<../DAT_Execute_DAT.md> "DAT Execute DAT")• [DAT Export ](<../DAT_Export.md> "DAT Export")• [Error ](<../Error_DAT.md> "Error DAT")• [EtherDream ](<../EtherDream_DAT.md> "EtherDream DAT")• [Evaluate ](<../Evaluate_DAT.md> "Evaluate DAT")• [Examine ](<../Examine_DAT.md> "Examine DAT")• [Execute ](<../Execute_DAT.md> "Execute DAT")• [FIFO ](<../FIFO_DAT.md> "FIFO DAT")• [File In ](<../File_In_DAT.md> "File In DAT")• [File Out ](<../File_Out_DAT.md> "File Out DAT")• [Folder ](<../Folder_DAT.md> "Folder DAT")• [In ](<../In_DAT.md> "In DAT")• [Indices ](<../Indices_DAT.md> "Indices DAT")• [Info ](<../Info_DAT.md> "Info DAT")• [Insert ](<../Insert_DAT.md> "Insert DAT")• [JSON ](<../JSON_DAT.md> "JSON DAT")• [Keyboard In ](<../Keyboard_In_DAT.md> "Keyboard In DAT")• [Lookup ](<../Lookup_DAT.md> "Lookup DAT")• [Media File Info ](<../Media_File_Info_DAT.md> "Media File Info DAT")• [Merge ](<../Merge_DAT.md> "Merge DAT")• [MIDI Event ](<../MIDI_Event_DAT.md> "MIDI Event DAT")• [MIDI In ](<../MIDI_In_DAT.md> "MIDI In DAT")• [Monitors ](<../Monitors_DAT.md> "Monitors DAT")• [MPCDI ](<../MPCDI_DAT.md> "MPCDI DAT")• [MQTT Client ](<../MQTT_Client_DAT.md> "MQTT Client DAT")• [Multi Touch In ](<../Multi_Touch_In_DAT.md> "Multi Touch In DAT")• [NDI ](<../NDI_DAT.md> "NDI DAT")• [Null ](<../Null_DAT.md> "Null DAT")• [OP Execute ](<../OP_Execute_DAT.md> "OP Execute DAT")• [OP Find ](<../OP_Find_DAT.md> "OP Find DAT")• [OSC In ](<../OSC_In_DAT.md> "OSC In DAT")• [OSC Out ](<../OSC_Out_DAT.md> "OSC Out DAT")• [Out ](<../Out_DAT.md> "Out DAT")• [Panel Execute ](<../Panel_Execute_DAT.md> "Panel Execute DAT")• [Parameter ](<../Parameter_DAT.md> "Parameter DAT")• [Parameter Execute ](<../Parameter_Execute_DAT.md> "Parameter Execute DAT")• [ParGroup Execute ](<../ParGroup_Execute_DAT.md> "ParGroup Execute DAT")• [Perform ](<../Perform_DAT.md> "Perform DAT")• [POP to ](<../POP_to_DAT.md> "POP to DAT")• [Render Pick ](<../Render_Pick_DAT.md> "Render Pick DAT")• [Reorder ](<../Reorder_DAT.md> "Reorder DAT")• [Script ](<../Script_DAT.md> "Script DAT")• [Select ](<../Select_DAT.md> "Select DAT")• [Serial ](<../Serial_DAT.md> "Serial DAT")• [Serial Devices ](<../Serial_Devices_DAT.md> "Serial Devices DAT")• [SocketIO ](<../SocketIO_DAT.md> "SocketIO DAT")• [SOP to ](<../SOP_to_DAT.md> "SOP to DAT")• [Sort ](<../Sort_DAT.md> "Sort DAT")• [Substitute ](<../Substitute_DAT.md> "Substitute DAT")• [Switch ](<../Switch_DAT.md> "Switch DAT")• [Table ](<../Table_DAT.md> "Table DAT")• TCP/IP • [Text ](<../Text_DAT.md> "Text DAT")• [Touch In ](<../Touch_In_DAT.md> "Touch In DAT")• [Touch Out ](<../Touch_Out_DAT.md> "Touch Out DAT")• [Transpose ](<../Transpose_DAT.md> "Transpose DAT")• [TUIO In ](<../TUIO_In_DAT.md> "TUIO In DAT")• [UDP In ](<../UDP_In_DAT.md> "UDP In DAT")• [UDP Out ](<../UDP_Out_DAT.md> "UDP Out DAT")• [UDT In ](<../UDT_In_DAT.md> "UDT In DAT")• [UDT Out ](<../UDT_Out_DAT.md> "UDT Out DAT")• [Video Devices ](<../Video_Devices_DAT.md> "Video Devices DAT")• [Web Client ](<../Web_Client_DAT.md> "Web Client DAT")• [Web ](<../Web_DAT.md> "Web DAT")• [Web Server ](<../Web_Server_DAT.md> "Web Server DAT")• [WebRTC ](<../WebRTC_DAT.md> "WebRTC DAT")• [WebSocket ](<../WebSocket_DAT.md> "WebSocket DAT")• [XML ](<../XML_DAT.md> "XML DAT")
