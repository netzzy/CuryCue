# OSC In DAT

##   
  
Summary

The OSC In DAT receives and parses full Open Sound Control packets using UDP by default. Each packet is parsed and appended as a row in the DAT's table. The table is FIFO "fisrt-in first-out" and limited to parameter-set number of lines. An optional script may be run for each packet received. Each packet/row represents either one OSC message, or an entire OSC bundle. Each argument is translated into readable ASCII text. 

See also [OSC](<./OSC.md> "OSC"), [OSC Out DAT](<./OSC_Out_DAT.md> "OSC Out DAT"), [Peer Class](<./Peer_Class.md> "Peer Class"), [OSC In CHOP](<./OSC_In_CHOP.md> "OSC In CHOP"), [OSC Out CHOP](<./OSC_Out_CHOP.md> "OSC Out CHOP"), [iOS and OSC](<./IOS_and_OSC.md> "IOS and OSC"), [Network Protocols](<./Network_Protocols.md> "Network Protocols"). 

The supported argument tag types are: 
* i int32
  * f float32
  * s OSC-string
  * b OSC-blob
  * h 64 bit big-endian two's complement integer
  * t OSC-timetag
  * d 64 bit ("double") IEEE 754 floating point number
  * S alternate type represented as an OSC-string
  * c ASCII character
  * r 32 bit RGBA color
  * m 4 byte MIDI message
  * T True
  * F False
  * N Nil
  * I Infinitum
  * [ Beginning of an array
  * ] End of an array


  
In the case of multi-vectored arguments (example "blob", "midi", "rgb", etc), the list of values is enclosed in double quotes. In the case of unknown argument types, a quoted list of decimal values representing the bytes of that argument are included instead. 

**NOTE for Windows OS - If experiencing connection issues make sure Windows Firewall is disabled.**

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[oscinDAT_Class](<./OscinDAT_Class.md> "OscinDAT Class")

## 

Parameters - Connect Page

Active`active`\- While on, the DAT receives information sent to the network port. While Off, no updating occurs. Data sent to the port is lost. 

Protocol`protocol`\- ⊞ \- Select which protocol to use, refer to the [Network Protocols](<./Network_Protocols.md> "Network Protocols") article for more information. 
* Messaging (UDP)`msging`-
* Multi-Cast Messaging (UDP)`multicastmsging`-
* Reliable Messaging (UDT Library)`reliablemsging`-


Network Address`address`\- For multi-cast protocol, this is the multi-cast address to listen for. For UDT protocol this is the IP address of the server. 

Port`port`\- The port which OSC-In will accept packets on. 

Local Address`localaddress`\- Specify an IP address to receive on, useful when the system has mulitple NICs (Network Interface Card) and you want to select which one to use. 

Shared Connection`shared`\- Use the same connection as other networking DATs using the same network protocol. 

OSC Address Scope`addscope`\- To reduce which message are generated, you can use message address name patterns to include or exclude messages. For example,`^*accel*`will exclude accelerometer messages coming in from an iOS or iPhone app like mrmr. See [Pattern Matching](<./Pattern_Matching.md> "Pattern Matching") for the syntax of the possible address name patterns. 

Include Type Tag`typetag`\- Includes the argument list type tag in each message. It includes the parameter type keywords (in case the parsing application needs to identify parameter types). 

Split Bundle into Messages`splitbundle`\- When On, each message contained within a bundle is given its own row. 

Split Message into Columns`splitmessage`\- When On, OSC address and arguments are given individual columns, otherwise they are included in the message column. 

Bundle Timestamp Column`bundletimestamp`\- When On, each bundle timestamp value is included in a column. 

## 

Parameters - Received Messages Page

Callbacks DAT`callbacks`\- The Callbacks DAT will execute once for each message received. See [oscinDAT_Class](<./OscinDAT_Class.md> "OscinDAT Class") for usage. 

Execute from`executeloc`\- ⊞ \- Determines the location the script is run from. 
* Current Node`current`\- The script is executed from the current node location.
* Callbacks DAT`callbacks`\- The script is executed from the location of the DAT specified in the Callbacks DAT parameter.
* Specified Operator`op`\- The script is executed from the operator specified in the From Operator parameter below.


From Operator`fromop`\- The operator whose state change will trigger the DAT to execute its script when Execute from is set to Specified Operator. This operator is also the path that the script will be executed from if the Execute From parameter is set to Specified Operator. 

Clamp Output`clamp`\- The DAT is limited to 100 messages by default but with Clamp Output, this can be set to anything including unlimited. 

Maximum Lines`maxlines`\- Limits the number of messages, older messages are removed from the list first. 

Clear Output`clear`\- Deletes all lines except the heading. To clear with a python script`op(_"opname"_).par.clear.pulse()`Bytes Column`bytes`\- Outputs the raw bytes of the message in a separate column. 

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

Operator Inputs
* Input 0:  -

## 

Info CHOP Channels

Extra Information for the OSC In DAT can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). 

### 

Specific OSC In DAT Info Channels
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
[Art-Net ](<./Art-Net_DAT.md> "Art-Net DAT")• [Audio Devices ](<./Audio_Devices_DAT.md> "Audio Devices DAT")• [CHOP Execute ](<./CHOP_Execute_DAT.md> "CHOP Execute DAT")• [CHOP to ](<./CHOP_to_DAT.md> "CHOP to DAT")• [Clip ](<./Clip_DAT.md> "Clip DAT")• [Convert ](<./Convert_DAT.md> "Convert DAT")• [CPlusPlus ](<./CPlusPlus_DAT.md> "CPlusPlus DAT")• [DAT ](<./DAT.md> "DAT")• [ Execute ](<./DAT_Execute_DAT.md> "DAT Execute DAT")• [DAT Export ](<./DAT_Export.md> "DAT Export")• [Error ](<./Error_DAT.md> "Error DAT")• [EtherDream ](<./EtherDream_DAT.md> "EtherDream DAT")• [Evaluate ](<./Evaluate_DAT.md> "Evaluate DAT")• [Examine ](<./Examine_DAT.md> "Examine DAT")• [Execute ](<./Execute_DAT.md> "Execute DAT")• [FIFO ](<./FIFO_DAT.md> "FIFO DAT")• [File In ](<./File_In_DAT.md> "File In DAT")• [File Out ](<./File_Out_DAT.md> "File Out DAT")• [Folder ](<./Folder_DAT.md> "Folder DAT")• [In ](<./In_DAT.md> "In DAT")• [Indices ](<./Indices_DAT.md> "Indices DAT")• [Info ](<./Info_DAT.md> "Info DAT")• [Insert ](<./Insert_DAT.md> "Insert DAT")• [JSON ](<./JSON_DAT.md> "JSON DAT")• [Keyboard In ](<./Keyboard_In_DAT.md> "Keyboard In DAT")• [Lookup ](<./Lookup_DAT.md> "Lookup DAT")• [Media File Info ](<./Media_File_Info_DAT.md> "Media File Info DAT")• [Merge ](<./Merge_DAT.md> "Merge DAT")• [MIDI Event ](<./MIDI_Event_DAT.md> "MIDI Event DAT")• [MIDI In ](<./MIDI_In_DAT.md> "MIDI In DAT")• [Monitors ](<./Monitors_DAT.md> "Monitors DAT")• [MPCDI ](<./MPCDI_DAT.md> "MPCDI DAT")• [MQTT Client ](<./MQTT_Client_DAT.md> "MQTT Client DAT")• [Multi Touch In ](<./Multi_Touch_In_DAT.md> "Multi Touch In DAT")• [NDI ](<./NDI_DAT.md> "NDI DAT")• [Null ](<./Null_DAT.md> "Null DAT")• [OP Execute ](<./OP_Execute_DAT.md> "OP Execute DAT")• [OP Find ](<./OP_Find_DAT.md> "OP Find DAT")• OSC In • [OSC Out ](<./OSC_Out_DAT.md> "OSC Out DAT")• [Out ](<./Out_DAT.md> "Out DAT")• [Panel Execute ](<./Panel_Execute_DAT.md> "Panel Execute DAT")• [Parameter ](<./Parameter_DAT.md> "Parameter DAT")• [Parameter Execute ](<./Parameter_Execute_DAT.md> "Parameter Execute DAT")• [ParGroup Execute ](<./ParGroup_Execute_DAT.md> "ParGroup Execute DAT")• [Perform ](<./Perform_DAT.md> "Perform DAT")• [POP to ](<./POP_to_DAT.md> "POP to DAT")• [Render Pick ](<./Render_Pick_DAT.md> "Render Pick DAT")• [Reorder ](<./Reorder_DAT.md> "Reorder DAT")• [Script ](<./Script_DAT.md> "Script DAT")• [Select ](<./Select_DAT.md> "Select DAT")• [Serial ](<./Serial_DAT.md> "Serial DAT")• [Serial Devices ](<./Serial_Devices_DAT.md> "Serial Devices DAT")• [SocketIO ](<./SocketIO_DAT.md> "SocketIO DAT")• [SOP to ](<./SOP_to_DAT.md> "SOP to DAT")• [Sort ](<./Sort_DAT.md> "Sort DAT")• [Substitute ](<./Substitute_DAT.md> "Substitute DAT")• [Switch ](<./Switch_DAT.md> "Switch DAT")• [Table ](<./Table_DAT.md> "Table DAT")• [TCP/IP ](<./TCP/IP_DAT.md> "TCP/IP DAT")• [Text ](<./Text_DAT.md> "Text DAT")• [Touch In ](<./Touch_In_DAT.md> "Touch In DAT")• [Touch Out ](<./Touch_Out_DAT.md> "Touch Out DAT")• [Transpose ](<./Transpose_DAT.md> "Transpose DAT")• [TUIO In ](<./TUIO_In_DAT.md> "TUIO In DAT")• [UDP In ](<./UDP_In_DAT.md> "UDP In DAT")• [UDP Out ](<./UDP_Out_DAT.md> "UDP Out DAT")• [UDT In ](<./UDT_In_DAT.md> "UDT In DAT")• [UDT Out ](<./UDT_Out_DAT.md> "UDT Out DAT")• [Video Devices ](<./Video_Devices_DAT.md> "Video Devices DAT")• [Web Client ](<./Web_Client_DAT.md> "Web Client DAT")• [Web ](<./Web_DAT.md> "Web DAT")• [Web Server ](<./Web_Server_DAT.md> "Web Server DAT")• [WebRTC ](<./WebRTC_DAT.md> "WebRTC DAT")• [WebSocket ](<./WebSocket_DAT.md> "WebSocket DAT")• [XML ](<./XML_DAT.md> "XML DAT")
