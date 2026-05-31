# Video Devices DAT

##   
  
Summary

The Video Devices DAT provides information about all detected video devices including driver, direction (input or output), label, and name that can be referenced in the [Video Device In TOP](<./Video_Device_In_TOP.md> "Video Device In TOP") and [Video Device Out TOP](<./Video_Device_Out_TOP.md> "Video Device Out TOP"). 

You can also set it to display all available video devices. 

It runs a callback script when a change in video devices has been detected and returns a list of names corresponding to the changed devices. 

The 'name' column is a unique identifier for the device that is built up using a few pieces. The pieces are separated using ||| as a delimiter E.g  
  
V1|||83514832|||0|||0|||DeckLink 8K Pro (1)  
  
Which splits up into:  
  
Name Version Number ||| Unique Device ID ||| Device Index ||| Device Sub Index ||| Device Label  
  
Where:  
Name Version Number - If the format of this name changes in the future, this will allow future versions know how to parse this. For now it's always set to V1.  
Device Unique ID - A unique ID obtained for the device, when possible. Sometimes it's serial number, sometimes it's based on the PCIe port is connected to. Some manufacturers such as Blackmagic assign a different ID to each connector, while others such as AJA have one ID for the entire card, and the extra connectors are differentiated via the 'Device Sub Index' field.  
Device Index - The index of the device, in the order it was enumerated from the driver.  
Device Sub Index - Within a device, the connectors may be referenced by a sub-index, which would change here.  
Device Label - An English-readable label for the device. Usually unique by adding extra (#) and - # suffixes to differentiate between identical devices.  


Unlike most menus, the contents of the string the menu is set to does not need to be an exact match to the devices available on the system. This is done to allow falling back to other devices when a project moves from one machine to another. It will first try to find devices that match using both 'Device Unique ID' and 'Device Sub Index'. If there are no devices on the system that match both of those it will then try to match using both 'Device Label' and 'Device Sub Index'. If there are still no matches, it will finally try to match using both 'Device Index' and 'Device Sub Index'. 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[videodevicesDAT_Class](<./VideodevicesDAT_Class.md> "VideodevicesDAT Class")

## 

Parameters - Video Devices Page

Driver`driver`\- ⊞ \- Menu of available drivers, table will only include devices belonging to selected driver. 
* DirectShow (WDM)`directshow`-
* Media Foundation`mediafoundation`-
* Imaging Source - Not Supported`imagingsource`-
* DataPath (RGBEASY)`datapath`-
* Blackmagic`blackmagic`-
* Allied Vision (GigE)`alliedvisiongige`-
* Imaging Development Systems (IDS)`ids`-
* FLIR / Point Grey (FlyCapture2)`pointgreyflycapture`-
* FLIR / Point Grey (Spinnaker)`flirspinnaker`-
* AVFoundation (macOS)`avfoundation`-
* BlueFish444`bluefish444`-
* AJA`aja`-
* Ximea`ximea`-
* Deltacast`deltacast`-


All Drivers`alldrivers`\- While on, the table will display devices from all available drivers. 

Input Devices`input`\- Toggle to include input devices. 

Output Devices`output`\- Toggle to include output devices. 

Callbacks DAT`callbacks`\- Runs this script once for each change to the table (ie. device state change). 

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

Extra Information for the Video Devices DAT can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). __

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


  
TouchDesigner Build: Latest\nwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditor2023.11280

DATs   
---  
[Art-Net ](<./Art-Net_DAT.md> "Art-Net DAT")• [Audio Devices ](<./Audio_Devices_DAT.md> "Audio Devices DAT")• [CHOP Execute ](<./CHOP_Execute_DAT.md> "CHOP Execute DAT")• [CHOP to ](<./CHOP_to_DAT.md> "CHOP to DAT")• [Clip ](<./Clip_DAT.md> "Clip DAT")• [Convert ](<./Convert_DAT.md> "Convert DAT")• [CPlusPlus ](<./CPlusPlus_DAT.md> "CPlusPlus DAT")• [DAT ](<./DAT.md> "DAT")• [ Execute ](<./DAT_Execute_DAT.md> "DAT Execute DAT")• [DAT Export ](<./DAT_Export.md> "DAT Export")• [Error ](<./Error_DAT.md> "Error DAT")• [EtherDream ](<./EtherDream_DAT.md> "EtherDream DAT")• [Evaluate ](<./Evaluate_DAT.md> "Evaluate DAT")• [Examine ](<./Examine_DAT.md> "Examine DAT")• [Execute ](<./Execute_DAT.md> "Execute DAT")• [FIFO ](<./FIFO_DAT.md> "FIFO DAT")• [File In ](<./File_In_DAT.md> "File In DAT")• [File Out ](<./File_Out_DAT.md> "File Out DAT")• [Folder ](<./Folder_DAT.md> "Folder DAT")• [In ](<./In_DAT.md> "In DAT")• [Indices ](<./Indices_DAT.md> "Indices DAT")• [Info ](<./Info_DAT.md> "Info DAT")• [Insert ](<./Insert_DAT.md> "Insert DAT")• [JSON ](<./JSON_DAT.md> "JSON DAT")• [Keyboard In ](<./Keyboard_In_DAT.md> "Keyboard In DAT")• [Lookup ](<./Lookup_DAT.md> "Lookup DAT")• [Media File Info ](<./Media_File_Info_DAT.md> "Media File Info DAT")• [Merge ](<./Merge_DAT.md> "Merge DAT")• [MIDI Event ](<./MIDI_Event_DAT.md> "MIDI Event DAT")• [MIDI In ](<./MIDI_In_DAT.md> "MIDI In DAT")• [Monitors ](<./Monitors_DAT.md> "Monitors DAT")• [MPCDI ](<./MPCDI_DAT.md> "MPCDI DAT")• [MQTT Client ](<./MQTT_Client_DAT.md> "MQTT Client DAT")• [Multi Touch In ](<./Multi_Touch_In_DAT.md> "Multi Touch In DAT")• [NDI ](<./NDI_DAT.md> "NDI DAT")• [Null ](<./Null_DAT.md> "Null DAT")• [OP Execute ](<./OP_Execute_DAT.md> "OP Execute DAT")• [OP Find ](<./OP_Find_DAT.md> "OP Find DAT")• [OSC In ](<./OSC_In_DAT.md> "OSC In DAT")• [OSC Out ](<./OSC_Out_DAT.md> "OSC Out DAT")• [Out ](<./Out_DAT.md> "Out DAT")• [Panel Execute ](<./Panel_Execute_DAT.md> "Panel Execute DAT")• [Parameter ](<./Parameter_DAT.md> "Parameter DAT")• [Parameter Execute ](<./Parameter_Execute_DAT.md> "Parameter Execute DAT")• [ParGroup Execute ](<./ParGroup_Execute_DAT.md> "ParGroup Execute DAT")• [Perform ](<./Perform_DAT.md> "Perform DAT")• [POP to ](<./POP_to_DAT.md> "POP to DAT")• [Render Pick ](<./Render_Pick_DAT.md> "Render Pick DAT")• [Reorder ](<./Reorder_DAT.md> "Reorder DAT")• [Script ](<./Script_DAT.md> "Script DAT")• [Select ](<./Select_DAT.md> "Select DAT")• [Serial ](<./Serial_DAT.md> "Serial DAT")• [Serial Devices ](<./Serial_Devices_DAT.md> "Serial Devices DAT")• [SocketIO ](<./SocketIO_DAT.md> "SocketIO DAT")• [SOP to ](<./SOP_to_DAT.md> "SOP to DAT")• [Sort ](<./Sort_DAT.md> "Sort DAT")• [Substitute ](<./Substitute_DAT.md> "Substitute DAT")• [Switch ](<./Switch_DAT.md> "Switch DAT")• [Table ](<./Table_DAT.md> "Table DAT")• [TCP/IP ](<./TCP/IP_DAT.md> "TCP/IP DAT")• [Text ](<./Text_DAT.md> "Text DAT")• [Touch In ](<./Touch_In_DAT.md> "Touch In DAT")• [Touch Out ](<./Touch_Out_DAT.md> "Touch Out DAT")• [Transpose ](<./Transpose_DAT.md> "Transpose DAT")• [TUIO In ](<./TUIO_In_DAT.md> "TUIO In DAT")• [UDP In ](<./UDP_In_DAT.md> "UDP In DAT")• [UDP Out ](<./UDP_Out_DAT.md> "UDP Out DAT")• [UDT In ](<./UDT_In_DAT.md> "UDT In DAT")• [UDT Out ](<./UDT_Out_DAT.md> "UDT Out DAT")• Video Devices • [Web Client ](<./Web_Client_DAT.md> "Web Client DAT")• [Web ](<./Web_DAT.md> "Web DAT")• [Web Server ](<./Web_Server_DAT.md> "Web Server DAT")• [WebRTC ](<./WebRTC_DAT.md> "WebRTC DAT")• [WebSocket ](<./WebSocket_DAT.md> "WebSocket DAT")• [XML ](<./XML_DAT.md> "XML DAT")
