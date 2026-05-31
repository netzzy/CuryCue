# OP Execute DAT

## 

Summary

The OP Execute DAT runs a script when the state of an [operator](<./Operator.md> "Operator") changes. 

OP Execute DATs are created with default python method placeholders. For each monitored condition in the parameters, there is a [matching python method](<./OpexecuteDAT_Class.md> "OpexecuteDAT Class") in the DAT. When a condition is turned on in the parameters, each time that condition is satisfied the corresponding python method will be executed. 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[opexecuteDAT_Class](<./OpexecuteDAT_Class.md> "OpexecuteDAT Class")

## 

Parameters - OP Execute Page

Active`active`\- While on, the DAT will respond to the OP that is referenced. 

Execute from`executeloc`\- ⊞ \- ([Tscript](<./Operator_Language.md> "Operator Language") only) Determines the location the script is run from. 
* Current Node`current`\- ([Tscript](<./Operator_Language.md> "Operator Language") only) The script is executed from the current node location.
* This Node`here`\- The script is executed from the parent of the DAT. The DAT executes from the parent to make siblings of the DAT easy to access: DAT scripts used to execute from inside the DAT.
* Specified Operator`op`\- The script is executed from the operator specified in the From Operator parameter below.


From Operator`fromop`\- The path that the script will be executed from if the Execute From parameter is set to _Specified Operator_. 

Monitor OPs`op`\- Specify which operators to monitor to trigger the scripts. 

Pre Cook`precook`\- The`onPreCook()`method is triggered before the operator is cooked. 

Post Cook`postcook`\- The`onPostCook()`method is triggered after the operator is cooked. 

Destroy`opdelete`\- The`onDestroy()`method is triggered when the operator is deleted. 

Flag Change`flagchange`\- The`onFlagChange()`method is triggered when one of the operator's [Flags](</index.php?title=Flags&action=edit&redlink=1> "Flags \(page does not exist\)") changes state. This includes all the flags in the Common Flags list of an [OP_Class](<./OP_Class.htm#Common_Flags> "OP Class"), plus all the python accessible flags listed in [COMP_Class](<./COMP_Class.htm#Common_Flags> "COMP Class"), [SOP_Class](<./SOP_Class.htm#Common_Flags> "SOP Class"), [CHOP_Class](<./CHOP_Class.htm#Common_Flags> "CHOP Class"). 

Wire Change`wirechange`\- The`onWireChange()`method is triggered when the operator's inputs are rewired (connected, disconnected, swapped). 

Name Change`namechange`\- The`onNameChange()`method is triggered when the name of the operator is changed. 

Path Change`pathchange`\- The`onPathChange()`method is triggered when the path of the operator is changed. 

UI Change`uichange`\- The`onUIChange()`method is triggered when operator is resized or moved in the network editor. 

Number Children Change`numchildrenchange`\- The onNumChildrenChange() method is triggered if the number of children an operator has changes. Only works with [Component](<./Component.md> "Component") type operators. 

Child Rename`childrename`\- The`onChildRename()`method is triggered if a child of the operator is renamed. 

Current Child Change`currentchildchange`\- The`onCurrentChildChange()`method is triggered if a child of the operator is made current in a network. Only works with Component type operators. 

Extension Change`extensionchange`\- The`onExtensionChange()`method is triggered when an extension of the operator is changed. 

Edit..`edit`\- Clicking this opens a text editor to edit text in the DAT. 

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

Extra Information for the OP Execute DAT can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). __

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


  
TouchDesigner Build: Latest\n2022.241402021.100002018.28070before 2018.28070

DATs   
---  
[Art-Net ](<./Art-Net_DAT.md> "Art-Net DAT")• [Audio Devices ](<./Audio_Devices_DAT.md> "Audio Devices DAT")• [CHOP Execute ](<./CHOP_Execute_DAT.md> "CHOP Execute DAT")• [CHOP to ](<./CHOP_to_DAT.md> "CHOP to DAT")• [Clip ](<./Clip_DAT.md> "Clip DAT")• [Convert ](<./Convert_DAT.md> "Convert DAT")• [CPlusPlus ](<./CPlusPlus_DAT.md> "CPlusPlus DAT")• [DAT ](<./DAT.md> "DAT")• [ Execute ](<./DAT_Execute_DAT.md> "DAT Execute DAT")• [DAT Export ](<./DAT_Export.md> "DAT Export")• [Error ](<./Error_DAT.md> "Error DAT")• [EtherDream ](<./EtherDream_DAT.md> "EtherDream DAT")• [Evaluate ](<./Evaluate_DAT.md> "Evaluate DAT")• [Examine ](<./Examine_DAT.md> "Examine DAT")• [Execute ](<./Execute_DAT.md> "Execute DAT")• [FIFO ](<./FIFO_DAT.md> "FIFO DAT")• [File In ](<./File_In_DAT.md> "File In DAT")• [File Out ](<./File_Out_DAT.md> "File Out DAT")• [Folder ](<./Folder_DAT.md> "Folder DAT")• [In ](<./In_DAT.md> "In DAT")• [Indices ](<./Indices_DAT.md> "Indices DAT")• [Info ](<./Info_DAT.md> "Info DAT")• [Insert ](<./Insert_DAT.md> "Insert DAT")• [JSON ](<./JSON_DAT.md> "JSON DAT")• [Keyboard In ](<./Keyboard_In_DAT.md> "Keyboard In DAT")• [Lookup ](<./Lookup_DAT.md> "Lookup DAT")• [Media File Info ](<./Media_File_Info_DAT.md> "Media File Info DAT")• [Merge ](<./Merge_DAT.md> "Merge DAT")• [MIDI Event ](<./MIDI_Event_DAT.md> "MIDI Event DAT")• [MIDI In ](<./MIDI_In_DAT.md> "MIDI In DAT")• [Monitors ](<./Monitors_DAT.md> "Monitors DAT")• [MPCDI ](<./MPCDI_DAT.md> "MPCDI DAT")• [MQTT Client ](<./MQTT_Client_DAT.md> "MQTT Client DAT")• [Multi Touch In ](<./Multi_Touch_In_DAT.md> "Multi Touch In DAT")• [NDI ](<./NDI_DAT.md> "NDI DAT")• [Null ](<./Null_DAT.md> "Null DAT")• OP Execute • [OP Find ](<./OP_Find_DAT.md> "OP Find DAT")• [OSC In ](<./OSC_In_DAT.md> "OSC In DAT")• [OSC Out ](<./OSC_Out_DAT.md> "OSC Out DAT")• [Out ](<./Out_DAT.md> "Out DAT")• [Panel Execute ](<./Panel_Execute_DAT.md> "Panel Execute DAT")• [Parameter ](<./Parameter_DAT.md> "Parameter DAT")• [Parameter Execute ](<./Parameter_Execute_DAT.md> "Parameter Execute DAT")• [ParGroup Execute ](<./ParGroup_Execute_DAT.md> "ParGroup Execute DAT")• [Perform ](<./Perform_DAT.md> "Perform DAT")• [POP to ](<./POP_to_DAT.md> "POP to DAT")• [Render Pick ](<./Render_Pick_DAT.md> "Render Pick DAT")• [Reorder ](<./Reorder_DAT.md> "Reorder DAT")• [Script ](<./Script_DAT.md> "Script DAT")• [Select ](<./Select_DAT.md> "Select DAT")• [Serial ](<./Serial_DAT.md> "Serial DAT")• [Serial Devices ](<./Serial_Devices_DAT.md> "Serial Devices DAT")• [SocketIO ](<./SocketIO_DAT.md> "SocketIO DAT")• [SOP to ](<./SOP_to_DAT.md> "SOP to DAT")• [Sort ](<./Sort_DAT.md> "Sort DAT")• [Substitute ](<./Substitute_DAT.md> "Substitute DAT")• [Switch ](<./Switch_DAT.md> "Switch DAT")• [Table ](<./Table_DAT.md> "Table DAT")• [TCP/IP ](<./TCP/IP_DAT.md> "TCP/IP DAT")• [Text ](<./Text_DAT.md> "Text DAT")• [Touch In ](<./Touch_In_DAT.md> "Touch In DAT")• [Touch Out ](<./Touch_Out_DAT.md> "Touch Out DAT")• [Transpose ](<./Transpose_DAT.md> "Transpose DAT")• [TUIO In ](<./TUIO_In_DAT.md> "TUIO In DAT")• [UDP In ](<./UDP_In_DAT.md> "UDP In DAT")• [UDP Out ](<./UDP_Out_DAT.md> "UDP Out DAT")• [UDT In ](<./UDT_In_DAT.md> "UDT In DAT")• [UDT Out ](<./UDT_Out_DAT.md> "UDT Out DAT")• [Video Devices ](<./Video_Devices_DAT.md> "Video Devices DAT")• [Web Client ](<./Web_Client_DAT.md> "Web Client DAT")• [Web ](<./Web_DAT.md> "Web DAT")• [Web Server ](<./Web_Server_DAT.md> "Web Server DAT")• [WebRTC ](<./WebRTC_DAT.md> "WebRTC DAT")• [WebSocket ](<./WebSocket_DAT.md> "WebSocket DAT")• [XML ](<./XML_DAT.md> "XML DAT")
