# DAT Execute DAT

## 

Summary

The DAT Execute DAT monitors another DAT's contents and runs a script when those contents change. The other DAT is usually a table. 

DAT Execute DATs are created with [default python method placeholders](<./DatexecuteDAT_Class.htm#Callbacks> "DatexecuteDAT Class"). For each monitored condition in the parameters, there is a matching python method in the DAT. When a condition is turned on in the parameters, each time that condition is satisfied the corresponding python method will be executed. 

**Note for 2025.30000 and later builds** \- A new`onTableChange`method does everything now, the other 4 legacy methods (`onRowChange`,`onColChange`,`onCellChange`, and`onSizeChange`) are now deprecated. DAT Execute DATs loaded from older builds will not have updated usage comments for the new onTableChange callback. You can get this information by created a new DAT Execute DAT in your network or from the code snippet below. 
[code] 
    # me - this DAT.
    # 
    # dat - the changed DAT
    # prevDAT - the DAT containing previous contents.
    #
    # Info contains specific details on what's changed:
    #
    #	rowsChanged	- list of row indices with different contents
    #   rowsAdded		- list of added row name indices (in dat)
    #   rowsRemoved	- list of removed row name indices (in prevDAT)
    #
    #	colsChanged	- list of column indices with different contents
    #   colsAdded		- list of added column name indices (in dat)
    #   colsRemoved	- list of removed column name indices (in prevDAT)
    #
    #	cellsChanged 	- list of cells that have changed content
    #
    #	sizeChanged	- bool, true if number of rows or columns changed
    # 
    # Make sure the corresponding toggle is enabled in the DAT Execute DAT.
    # 
    
    # This callback can be used to evaluate several change conditions simultaneously.
    
    def onTableChange(dat, prevDAT, info):
    	return
    
[/code]

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[datexecuteDAT_Class](<./DatexecuteDAT_Class.md> "DatexecuteDAT Class")

## 

Parameters - DAT Execute Page

Active`active`\- While on, the DAT will respond to the CHOP that is referenced. 

Execute from`executeloc`\- ⊞ \- ([Tscript](<./Operator_Language.md> "Operator Language") only) Determines the location the script is run from. 
* Current Node`current`\- ([Tscript](<./Operator_Language.md> "Operator Language") only) The script is executed from the current node location.
* This Node`here`\- The script is executed from the parent of the DAT. The DAT executes from the parent to make siblings of the DAT easy to access: DAT scripts used to execute from inside the DAT.
* Specified Operator`op`\- The script is executed from the operator specified in the From Operator parameter below.


From Operator`fromop`\- ([Tscript](<./Operator_Language.md> "Operator Language") only) The path that the script will be executed from if the Execute From parameter is set to _Specified Operator_. 

DAT`dat`\- The DAT which is monitored and will trigger the script to execute when its contents change. 

Table Change`tablechange`\- The onTableChange() method is called if the table changes in any way since the last cook. 

Row Change`rowchange`\- Deprecated, use onTableChange() now. The onRowChange() method is called once for every row that changed (since its last cook). 

Column Change`colchange`\- Deprecated, use onTableChange() now. The onColChange() method is called once for every column that changed (since its last cook). 

Cell Change`cellchange`\- Deprecated, use onTableChange() now. The onCellChange() method is called for every cell that changed since the last cook. 

Size Change`sizechange`\- Deprecated, use onTableChange() now. The onSizeChange() method is called for every table size change since the last cook. 

Execute`execute`\- ⊞ \- Determines if the methods are executed at the start of the frame or end of the frame. 
* Start of Frame`start`\- The method will be called from the start of the frame. If a row changes 4 times during a frame then the method will run 4 times as well (useful for [Multi Touch In DAT](<./Multi_Touch_In_DAT.md> "Multi Touch In DAT") events for example).
* End of Frame`end`\- The method will execute at most one time per frame, at the end of the frame, even if it triggered several times in one frame. If, for example, Monitor is set to Row, a row may change several times in a frame, but it will be called only once for each row.


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

Extra Information for the DAT Execute DAT can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). __

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


  
TouchDesigner Build: Latest\n2025.300002022.241402021.100002018.28070before 2018.28070

DATs   
---  
[Art-Net ](<./Art-Net_DAT.md> "Art-Net DAT")• [Audio Devices ](<./Audio_Devices_DAT.md> "Audio Devices DAT")• [CHOP Execute ](<./CHOP_Execute_DAT.md> "CHOP Execute DAT")• [CHOP to ](<./CHOP_to_DAT.md> "CHOP to DAT")• [Clip ](<./Clip_DAT.md> "Clip DAT")• [Convert ](<./Convert_DAT.md> "Convert DAT")• [CPlusPlus ](<./CPlusPlus_DAT.md> "CPlusPlus DAT")• [DAT ](<./DAT.md> "DAT")•  Execute • [DAT Export ](<./DAT_Export.md> "DAT Export")• [Error ](<./Error_DAT.md> "Error DAT")• [EtherDream ](<./EtherDream_DAT.md> "EtherDream DAT")• [Evaluate ](<./Evaluate_DAT.md> "Evaluate DAT")• [Examine ](<./Examine_DAT.md> "Examine DAT")• [Execute ](<./Execute_DAT.md> "Execute DAT")• [FIFO ](<./FIFO_DAT.md> "FIFO DAT")• [File In ](<./File_In_DAT.md> "File In DAT")• [File Out ](<./File_Out_DAT.md> "File Out DAT")• [Folder ](<./Folder_DAT.md> "Folder DAT")• [In ](<./In_DAT.md> "In DAT")• [Indices ](<./Indices_DAT.md> "Indices DAT")• [Info ](<./Info_DAT.md> "Info DAT")• [Insert ](<./Insert_DAT.md> "Insert DAT")• [JSON ](<./JSON_DAT.md> "JSON DAT")• [Keyboard In ](<./Keyboard_In_DAT.md> "Keyboard In DAT")• [Lookup ](<./Lookup_DAT.md> "Lookup DAT")• [Media File Info ](<./Media_File_Info_DAT.md> "Media File Info DAT")• [Merge ](<./Merge_DAT.md> "Merge DAT")• [MIDI Event ](<./MIDI_Event_DAT.md> "MIDI Event DAT")• [MIDI In ](<./MIDI_In_DAT.md> "MIDI In DAT")• [Monitors ](<./Monitors_DAT.md> "Monitors DAT")• [MPCDI ](<./MPCDI_DAT.md> "MPCDI DAT")• [MQTT Client ](<./MQTT_Client_DAT.md> "MQTT Client DAT")• [Multi Touch In ](<./Multi_Touch_In_DAT.md> "Multi Touch In DAT")• [NDI ](<./NDI_DAT.md> "NDI DAT")• [Null ](<./Null_DAT.md> "Null DAT")• [OP Execute ](<./OP_Execute_DAT.md> "OP Execute DAT")• [OP Find ](<./OP_Find_DAT.md> "OP Find DAT")• [OSC In ](<./OSC_In_DAT.md> "OSC In DAT")• [OSC Out ](<./OSC_Out_DAT.md> "OSC Out DAT")• [Out ](<./Out_DAT.md> "Out DAT")• [Panel Execute ](<./Panel_Execute_DAT.md> "Panel Execute DAT")• [Parameter ](<./Parameter_DAT.md> "Parameter DAT")• [Parameter Execute ](<./Parameter_Execute_DAT.md> "Parameter Execute DAT")• [ParGroup Execute ](<./ParGroup_Execute_DAT.md> "ParGroup Execute DAT")• [Perform ](<./Perform_DAT.md> "Perform DAT")• [POP to ](<./POP_to_DAT.md> "POP to DAT")• [Render Pick ](<./Render_Pick_DAT.md> "Render Pick DAT")• [Reorder ](<./Reorder_DAT.md> "Reorder DAT")• [Script ](<./Script_DAT.md> "Script DAT")• [Select ](<./Select_DAT.md> "Select DAT")• [Serial ](<./Serial_DAT.md> "Serial DAT")• [Serial Devices ](<./Serial_Devices_DAT.md> "Serial Devices DAT")• [SocketIO ](<./SocketIO_DAT.md> "SocketIO DAT")• [SOP to ](<./SOP_to_DAT.md> "SOP to DAT")• [Sort ](<./Sort_DAT.md> "Sort DAT")• [Substitute ](<./Substitute_DAT.md> "Substitute DAT")• [Switch ](<./Switch_DAT.md> "Switch DAT")• [Table ](<./Table_DAT.md> "Table DAT")• [TCP/IP ](<./TCP/IP_DAT.md> "TCP/IP DAT")• [Text ](<./Text_DAT.md> "Text DAT")• [Touch In ](<./Touch_In_DAT.md> "Touch In DAT")• [Touch Out ](<./Touch_Out_DAT.md> "Touch Out DAT")• [Transpose ](<./Transpose_DAT.md> "Transpose DAT")• [TUIO In ](<./TUIO_In_DAT.md> "TUIO In DAT")• [UDP In ](<./UDP_In_DAT.md> "UDP In DAT")• [UDP Out ](<./UDP_Out_DAT.md> "UDP Out DAT")• [UDT In ](<./UDT_In_DAT.md> "UDT In DAT")• [UDT Out ](<./UDT_Out_DAT.md> "UDT Out DAT")• [Video Devices ](<./Video_Devices_DAT.md> "Video Devices DAT")• [Web Client ](<./Web_Client_DAT.md> "Web Client DAT")• [Web ](<./Web_DAT.md> "Web DAT")• [Web Server ](<./Web_Server_DAT.md> "Web Server DAT")• [WebRTC ](<./WebRTC_DAT.md> "WebRTC DAT")• [WebSocket ](<./WebSocket_DAT.md> "WebSocket DAT")• [XML ](<./XML_DAT.md> "XML DAT")
