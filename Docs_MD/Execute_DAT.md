# Execute DAT

## 

Summary

The Execute DAT lets you edit scripts and run them based on conditions. It can be executed at the start or end of every frame, or at the start or end of the TouchDesigner process. 

Execute DATs are created with [default python method placeholders](<./ExecuteDAT_Class.md> "ExecuteDAT Class"). For each monitored condition in the parameters, there is a matching python method in the DAT. When a condition is turned on in the parameters, each time that condition is satisfied the corresponding python method will be executed. 

Text can also can be passed into the Text DAT through the node's input, however this text will not be editable. Text can be created in the DAT via the [Node Viewer](<./Node_Viewer.md> "Node Viewer") or an external text editor. 

See also [OP Execute DAT](<./OP_Execute_DAT.md> "OP Execute DAT"). 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[executeDAT_Class](<./ExecuteDAT_Class.md> "ExecuteDAT Class")

## 

Parameters - Execute Page

Active`active`\- While on, the DAT will respond to the events selected below. 

Execute from`executeloc`\- ⊞ \- ([Tscript](<./Operator_Language.md> "Operator Language") only) Determines the location the script is run from. 
* Current Node`current`\- ([Tscript](<./Operator_Language.md> "Operator Language") only) The script is executed from the current node location.
* This Node`here`\- The script is executed from the parent of the DAT. The DAT executes from the parent to make siblings of the DAT easy to access: DAT scripts used to execute from inside the DAT.
* Specified Operator`op`\- The script is executed from the operator specified in the From Operator parameter below.


From Operator`fromop`\- This component is also the path that the script will be executed from if the Execute From parameter is set to _Specified Operator_. 

Start`start`\- The onStart() method is executed when TouchDesigner starts. This method is never called in TouchEngine because components are loaded after TouchEngine has started. 

Create`create`\- The create() method is executed when the node is created. This can be triggered on start, by loading a component from disk, by copying & pasting, or any other way a node can be created. 

Exit`exit`\- The onExit() method is executed when the TouchDesigner process quits. 

Frame Start`framestart`\- The onFrameStart() method is executed at the start of every frame. 

Frame End`frameend`\- The onFrameEnd() method is executed at the end of every frame. 

Play State Change`playstatechange`\- The onPlayStateChange() method is executed each time the play state changes, ie. pause or play is used on the timeline. 

Device Change`devicechange`\- The onDeviceChange() method is executed each time devices are connected or disconnected from the computer. For example, plugging in MIDI devices, cameras, joysticks, etc. 

**NOTE:** When using multiple Execute DATs with Start and Create functions, they are triggered in numbered-alphanumeric order of the DAT's names. __

Edit..`edit`\- Clicking this opens a text editor to edit text in the DAT. 

**TIP:** To direct all "standard output" of python to a Text DAT, put this in the`start()`method:`sys.stdout = op('text1')`To safely to this and restore standard output: 
[code] 
    prev = sys.stdout
    sys.stdout = op('text1')
    sys.stdout = prev
    
[/code]

## 

Parameters - File Page

File`file`\- The filesystem path and name of the file to load. Accepts`.txt`and`.dat`files. 

Sync to File`syncfile`\- When On, loads the file from disk into the DAT when the projects starts. A filename must be specified. Turning on the option will load the file from disk immediately. If the file does not exist, it will be created the first time the DAT is updated. The file is monitored so that any changes made to the file will update the DAT, and any changes made to the DAT will be written to the file right away. If the file is removed, the DAT will retain its current contents. 

Load on Start`loadonstart`\- When On, reloads the file from disk into the DAT when the projects starts. 

Load File`loadonstartpulse`\- Instantly reloads the file. 

Write on Toe Save`write`\- When On, writes the contents of the DAT out to the file on disk when the project is saved. 

Write File`writepulse`\- Instantly write the file to disk. 

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

Extra Information for the Execute DAT can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). __

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


  
TouchDesigner Build: Latest\nwikieditor2022.241402021.100002018.28070before 2018.28070

DATs   
---  
[Art-Net ](<./Art-Net_DAT.md> "Art-Net DAT")• [Audio Devices ](<./Audio_Devices_DAT.md> "Audio Devices DAT")• [CHOP Execute ](<./CHOP_Execute_DAT.md> "CHOP Execute DAT")• [CHOP to ](<./CHOP_to_DAT.md> "CHOP to DAT")• [Clip ](<./Clip_DAT.md> "Clip DAT")• [Convert ](<./Convert_DAT.md> "Convert DAT")• [CPlusPlus ](<./CPlusPlus_DAT.md> "CPlusPlus DAT")• [DAT ](<./DAT.md> "DAT")• [ Execute ](<./DAT_Execute_DAT.md> "DAT Execute DAT")• [DAT Export ](<./DAT_Export.md> "DAT Export")• [Error ](<./Error_DAT.md> "Error DAT")• [EtherDream ](<./EtherDream_DAT.md> "EtherDream DAT")• [Evaluate ](<./Evaluate_DAT.md> "Evaluate DAT")• [Examine ](<./Examine_DAT.md> "Examine DAT")• Execute • [FIFO ](<./FIFO_DAT.md> "FIFO DAT")• [File In ](<./File_In_DAT.md> "File In DAT")• [File Out ](<./File_Out_DAT.md> "File Out DAT")• [Folder ](<./Folder_DAT.md> "Folder DAT")• [In ](<./In_DAT.md> "In DAT")• [Indices ](<./Indices_DAT.md> "Indices DAT")• [Info ](<./Info_DAT.md> "Info DAT")• [Insert ](<./Insert_DAT.md> "Insert DAT")• [JSON ](<./JSON_DAT.md> "JSON DAT")• [Keyboard In ](<./Keyboard_In_DAT.md> "Keyboard In DAT")• [Lookup ](<./Lookup_DAT.md> "Lookup DAT")• [Media File Info ](<./Media_File_Info_DAT.md> "Media File Info DAT")• [Merge ](<./Merge_DAT.md> "Merge DAT")• [MIDI Event ](<./MIDI_Event_DAT.md> "MIDI Event DAT")• [MIDI In ](<./MIDI_In_DAT.md> "MIDI In DAT")• [Monitors ](<./Monitors_DAT.md> "Monitors DAT")• [MPCDI ](<./MPCDI_DAT.md> "MPCDI DAT")• [MQTT Client ](<./MQTT_Client_DAT.md> "MQTT Client DAT")• [Multi Touch In ](<./Multi_Touch_In_DAT.md> "Multi Touch In DAT")• [NDI ](<./NDI_DAT.md> "NDI DAT")• [Null ](<./Null_DAT.md> "Null DAT")• [OP Execute ](<./OP_Execute_DAT.md> "OP Execute DAT")• [OP Find ](<./OP_Find_DAT.md> "OP Find DAT")• [OSC In ](<./OSC_In_DAT.md> "OSC In DAT")• [OSC Out ](<./OSC_Out_DAT.md> "OSC Out DAT")• [Out ](<./Out_DAT.md> "Out DAT")• [Panel Execute ](<./Panel_Execute_DAT.md> "Panel Execute DAT")• [Parameter ](<./Parameter_DAT.md> "Parameter DAT")• [Parameter Execute ](<./Parameter_Execute_DAT.md> "Parameter Execute DAT")• [ParGroup Execute ](<./ParGroup_Execute_DAT.md> "ParGroup Execute DAT")• [Perform ](<./Perform_DAT.md> "Perform DAT")• [POP to ](<./POP_to_DAT.md> "POP to DAT")• [Render Pick ](<./Render_Pick_DAT.md> "Render Pick DAT")• [Reorder ](<./Reorder_DAT.md> "Reorder DAT")• [Script ](<./Script_DAT.md> "Script DAT")• [Select ](<./Select_DAT.md> "Select DAT")• [Serial ](<./Serial_DAT.md> "Serial DAT")• [Serial Devices ](<./Serial_Devices_DAT.md> "Serial Devices DAT")• [SocketIO ](<./SocketIO_DAT.md> "SocketIO DAT")• [SOP to ](<./SOP_to_DAT.md> "SOP to DAT")• [Sort ](<./Sort_DAT.md> "Sort DAT")• [Substitute ](<./Substitute_DAT.md> "Substitute DAT")• [Switch ](<./Switch_DAT.md> "Switch DAT")• [Table ](<./Table_DAT.md> "Table DAT")• [TCP/IP ](<./TCP/IP_DAT.md> "TCP/IP DAT")• [Text ](<./Text_DAT.md> "Text DAT")• [Touch In ](<./Touch_In_DAT.md> "Touch In DAT")• [Touch Out ](<./Touch_Out_DAT.md> "Touch Out DAT")• [Transpose ](<./Transpose_DAT.md> "Transpose DAT")• [TUIO In ](<./TUIO_In_DAT.md> "TUIO In DAT")• [UDP In ](<./UDP_In_DAT.md> "UDP In DAT")• [UDP Out ](<./UDP_Out_DAT.md> "UDP Out DAT")• [UDT In ](<./UDT_In_DAT.md> "UDT In DAT")• [UDT Out ](<./UDT_Out_DAT.md> "UDT Out DAT")• [Video Devices ](<./Video_Devices_DAT.md> "Video Devices DAT")• [Web Client ](<./Web_Client_DAT.md> "Web Client DAT")• [Web ](<./Web_DAT.md> "Web DAT")• [Web Server ](<./Web_Server_DAT.md> "Web Server DAT")• [WebRTC ](<./WebRTC_DAT.md> "WebRTC DAT")• [WebSocket ](<./WebSocket_DAT.md> "WebSocket DAT")• [XML ](<./XML_DAT.md> "XML DAT")
