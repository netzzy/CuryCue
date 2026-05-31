# Folder DAT

## 

Summary

The Folder DAT lists the files and subfolders found in a file system folder and monitors any changes. 

For each item found, a row is created in the table with optional columns for the following information: 
* Name
  * Base Name
  * Extension
  * Type
  * Size
  * Depth
  * Folder
  * Path
  * Relative Path
  * Date Created
  * Date Modified
  * Date Accessed


[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[folderDAT_Class](<./FolderDAT_Class.md> "FolderDAT Class")

## 

Parameters - Folder Page

Active`active`\- When off, the DAT outputs a single-row table with only the headings, useful when dormant or when sending the DAT to a [Replicator COMP](<./Replicator_COMP.md> "Replicator COMP"). 

Root Folder`rootfolder`\- The folder in the filesystem whose contents will be displayed in the DAT list. 

Refresh`refresh`\- When on, it monitors the specified folder(s) of the filesystem. 

Refresh Pulse`refreshpulse`\- The pulse button reads the folder contents once. 

Asynchronous Update`async`\- When on, the update happens asynchronously from the main thread so it doesn't make TouchDesigner drop frames or pause. As a result, the Folder DAT way not update its data within the next frame after the change on disk. 

Name Format`nameformat`\- ⊞ \- Select whether to include the filename extension or not. 
* Include Extension`extension`-
* No Extension`noextension`-


Date Format`dateformat`\- ⊞ \- The format used to display the item's dates in the table. 
* Standard`std`\- A standard date format.
* Epoch`epoch`\- A reference date format.


Type`type`\- ⊞ \- The types of contents to display. 
* Files`files`\- Include files.
* Folders`folders`\- Include folders.
* Files and Folders`filesandfolders`\- Include both files and folders.


Folders`folders`\- Use [Pattern Matching](<./Pattern_Matching.md> "Pattern Matching") to specify which folders are included. Matches the folder path. Delimiters used are spaces and commas. To match spaces, enclose the entire search term in double quotes. 

Names`names`\- Use [Pattern Matching](<./Pattern_Matching.md> "Pattern Matching") to specify which names are included. Delimiters used are spaces and commas. To match spaces, enclose the entire search term in double quotes. 

All Extensions`allextensions`\- Includes all file extensions. 

Image Extensions`imageextensions`\- Includes image contents that are supported by TouchDesigner. See supported [File Types](<./File_Types.md> "File Types"). 

Movie Extensions`movieextensions`\- Includes movie contents that are supported by TouchDesigner. See supported [File Types](<./File_Types.md> "File Types"). 

Audio Extensions`audioextensions`\- Includes audio contents that are supported by TouchDesigner. See supported [File Types](<./File_Types.md> "File Types"). 

Extensions`extensions`\- Use [Pattern Matching](<./Pattern_Matching.md> "Pattern Matching") to specify which extensions are included. Extensions listed here should not include the period. E.g *txt, not *.txt. 

Include Subfolders`subfolders`\- Includes the subfolders from the root folder specified. 

Minumum Depth`mindepth`\- Set a minmum depth for the subfolders the Folder DAT should recursively search through. 

Limit Depth`limitdepth`\- Turns on the Maximum Depth parameter to limit searching through subfolders. Turning this toggle off will search through all subtrees. 

Maximum Depth`maxdepth`\- Set the maximum depth for the subfolders the Folder DAT should recursively search through. 

## 

Parameters - Columns Page

Name`namecol`\- The name of the folder or file. In the case of a file this includes the extension. ie.`myfile.txt`Base Name`basenamecol`\- The name of the folder or file. In the case of a file this form does not includes the extension. ie.`myfile`Extension`extensioncol`\- The file extension of the file, blank for folders. ie.`txt`Type`typecol`\- The type of file as reported by the operating system. 

Size`sizecol`\- The size of the file in Bytes. Folders do not report any size. 

Depth`depthcol`\- How many folders deep the item is found from the Root Folder. Items on the Root Folder level have a depth of 0. 

Folder`foldercol`\- The path of the folder, or in the case of a file, the path of the folder the file is found in. 

Path`pathcol`\- The full path to the folder or file. 

Relative Path`relpathcol`\- The relative path to the folder or file from the Root Folder. 

Date Created`datecreatedcol`\- The date of creation. 

Date Modified`datemodifiedcol`\- The date of most recent modification. 

Date Accessed`dateaccessedcol`\- The date of most recent access or opening. 

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

Extra Information for the Folder DAT can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). __

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
[Art-Net ](<./Art-Net_DAT.md> "Art-Net DAT")• [Audio Devices ](<./Audio_Devices_DAT.md> "Audio Devices DAT")• [CHOP Execute ](<./CHOP_Execute_DAT.md> "CHOP Execute DAT")• [CHOP to ](<./CHOP_to_DAT.md> "CHOP to DAT")• [Clip ](<./Clip_DAT.md> "Clip DAT")• [Convert ](<./Convert_DAT.md> "Convert DAT")• [CPlusPlus ](<./CPlusPlus_DAT.md> "CPlusPlus DAT")• [DAT ](<./DAT.md> "DAT")• [ Execute ](<./DAT_Execute_DAT.md> "DAT Execute DAT")• [DAT Export ](<./DAT_Export.md> "DAT Export")• [Error ](<./Error_DAT.md> "Error DAT")• [EtherDream ](<./EtherDream_DAT.md> "EtherDream DAT")• [Evaluate ](<./Evaluate_DAT.md> "Evaluate DAT")• [Examine ](<./Examine_DAT.md> "Examine DAT")• [Execute ](<./Execute_DAT.md> "Execute DAT")• [FIFO ](<./FIFO_DAT.md> "FIFO DAT")• [File In ](<./File_In_DAT.md> "File In DAT")• [File Out ](<./File_Out_DAT.md> "File Out DAT")• Folder • [In ](<./In_DAT.md> "In DAT")• [Indices ](<./Indices_DAT.md> "Indices DAT")• [Info ](<./Info_DAT.md> "Info DAT")• [Insert ](<./Insert_DAT.md> "Insert DAT")• [JSON ](<./JSON_DAT.md> "JSON DAT")• [Keyboard In ](<./Keyboard_In_DAT.md> "Keyboard In DAT")• [Lookup ](<./Lookup_DAT.md> "Lookup DAT")• [Media File Info ](<./Media_File_Info_DAT.md> "Media File Info DAT")• [Merge ](<./Merge_DAT.md> "Merge DAT")• [MIDI Event ](<./MIDI_Event_DAT.md> "MIDI Event DAT")• [MIDI In ](<./MIDI_In_DAT.md> "MIDI In DAT")• [Monitors ](<./Monitors_DAT.md> "Monitors DAT")• [MPCDI ](<./MPCDI_DAT.md> "MPCDI DAT")• [MQTT Client ](<./MQTT_Client_DAT.md> "MQTT Client DAT")• [Multi Touch In ](<./Multi_Touch_In_DAT.md> "Multi Touch In DAT")• [NDI ](<./NDI_DAT.md> "NDI DAT")• [Null ](<./Null_DAT.md> "Null DAT")• [OP Execute ](<./OP_Execute_DAT.md> "OP Execute DAT")• [OP Find ](<./OP_Find_DAT.md> "OP Find DAT")• [OSC In ](<./OSC_In_DAT.md> "OSC In DAT")• [OSC Out ](<./OSC_Out_DAT.md> "OSC Out DAT")• [Out ](<./Out_DAT.md> "Out DAT")• [Panel Execute ](<./Panel_Execute_DAT.md> "Panel Execute DAT")• [Parameter ](<./Parameter_DAT.md> "Parameter DAT")• [Parameter Execute ](<./Parameter_Execute_DAT.md> "Parameter Execute DAT")• [ParGroup Execute ](<./ParGroup_Execute_DAT.md> "ParGroup Execute DAT")• [Perform ](<./Perform_DAT.md> "Perform DAT")• [POP to ](<./POP_to_DAT.md> "POP to DAT")• [Render Pick ](<./Render_Pick_DAT.md> "Render Pick DAT")• [Reorder ](<./Reorder_DAT.md> "Reorder DAT")• [Script ](<./Script_DAT.md> "Script DAT")• [Select ](<./Select_DAT.md> "Select DAT")• [Serial ](<./Serial_DAT.md> "Serial DAT")• [Serial Devices ](<./Serial_Devices_DAT.md> "Serial Devices DAT")• [SocketIO ](<./SocketIO_DAT.md> "SocketIO DAT")• [SOP to ](<./SOP_to_DAT.md> "SOP to DAT")• [Sort ](<./Sort_DAT.md> "Sort DAT")• [Substitute ](<./Substitute_DAT.md> "Substitute DAT")• [Switch ](<./Switch_DAT.md> "Switch DAT")• [Table ](<./Table_DAT.md> "Table DAT")• [TCP/IP ](<./TCP/IP_DAT.md> "TCP/IP DAT")• [Text ](<./Text_DAT.md> "Text DAT")• [Touch In ](<./Touch_In_DAT.md> "Touch In DAT")• [Touch Out ](<./Touch_Out_DAT.md> "Touch Out DAT")• [Transpose ](<./Transpose_DAT.md> "Transpose DAT")• [TUIO In ](<./TUIO_In_DAT.md> "TUIO In DAT")• [UDP In ](<./UDP_In_DAT.md> "UDP In DAT")• [UDP Out ](<./UDP_Out_DAT.md> "UDP Out DAT")• [UDT In ](<./UDT_In_DAT.md> "UDT In DAT")• [UDT Out ](<./UDT_Out_DAT.md> "UDT Out DAT")• [Video Devices ](<./Video_Devices_DAT.md> "Video Devices DAT")• [Web Client ](<./Web_Client_DAT.md> "Web Client DAT")• [Web ](<./Web_DAT.md> "Web DAT")• [Web Server ](<./Web_Server_DAT.md> "Web Server DAT")• [WebRTC ](<./WebRTC_DAT.md> "WebRTC DAT")• [WebSocket ](<./WebSocket_DAT.md> "WebSocket DAT")• [XML ](<./XML_DAT.md> "XML DAT")
