# Substitute DAT

##   
  
Summary

The Substitute DAT changes the cells of the incoming DAT using pattern matching and substitution strings. It outputs a table with the same number of rows and columns. 

See examples below. Also you can use the second input to provide a table of strings to substitute, the first column being the "before" strings and the second column being the "after" strings. 

**See also** : the Python`.replace()`[[1]](<https://www.w3schools.com/python/ref_string_replace.asp>), which is a method you can apply to any string. You can do that in an [Evaluate DAT](<./Evaluate_DAT.md> "Evaluate DAT") or [Script DAT](<./Script_DAT.md> "Script DAT"). 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[substituteDAT_Class](</SubstituteDAT_Class> "SubstituteDAT Class")

## 

Parameters - Substitute Page

Before`before`\- Search term to replace. The following special characters may be used: 
* * - match any number of characters
  * ? - match a single character
  * [] - match any character defined within the brackets


To match these special characters exactly, put a backslash (`\`) before the special character. __

After`after`\- The replacement term. This replaces everything matched in the search term. Spaces are permitted. 

Match`match`\- ⊞ \- Specify where to match: 
* Anywhere`anywhere`\- Matches any part of the string.
* Exact`exact`\- The string must match the search term exactly.
* At Start`start`\- Match the search term to the beginning of the string.
* At End`end`\- Match the search term to the end of the string.


Case Sensitive`case`\- Respect case sensitivity in search term. 

Expand the From String`expand`\- Expand variables and back quotes in the From string. 

Expand the To String`expandto`\- Expand variables and back quotes in the To string. 

First Match Only`first`\- Replaces only the first instance of the matching string. 

## 

Parameters - Scope Page

Exclude First Row`xfirstrow`\- Forces the first row to be ignored even if it is not specified by the Select Rows settings. 

Exclude First Col`xfirstcol`\- Forces the first column to be ignored even if it is not specified by the Select Cols settings. 

Select Rows`extractrows`\- ⊞ \- This parameter allows you to pick different ways of specifying the rows scoped. 
* All`all`\- All rows scoped.
* by Name`byname`\- Rows scoped using Start Row Name and End Row Name parameters.
* by Index`byindex`\- Rows scoped using Start Row Index and End Row Index parameters.
* by Start Name, End Index`bynameindex`\- Rows scoped using Start Row Name and End Row Index parameters.
* by Start Index, End Name`byindexname`\- Rows scoped using Start Row Index and End Row Name parameters.
* by Values`bynames`\- Rows scoped by specifying the row values explicitly.
* by Condition`byexpr`\- Rows scoped by an expression to be evaluated for the from column.


Start Row Name`rownamestart`\- Specify the row name to start the scope range from. 

Start Row Index`rowindexstart`\- Specify the row index to start the scope range from. 

End Row Name`rownameend`\- Specify the row name to end the scope range. 

End Row Index`rowindexend`\- Specify the row index to end the scope range. 

Row Select Values`rownames`\- Specify actual row names that you want to scope. You can use pattern matching, for example row[1-4] will scope all the rows names row1 thru row4. 

Row Select Condition`rowexpr`\- Specify an expression that will be evaluated. If the expression evaluates to true, the row will be selected. 

Expand the parameter and you will see that it is in [expression mode](<./Parameter_Mode.md> "Parameter Mode"). 

By default, the [Python](<./Python.md> "Python") expression is`re.match('.*',me.inputCell.val) != None`.`'.*'`means match any character multiple times, so this expression matches all values. If you want to match the parent's operator name followed by any numeric number you can use`parent().name+'[0-9]*'`, where`'[0-9]*'`matches any numerical string.`'.*'+parent().name+'.*'`will match any cell that contains the operator's parent name. You can check [Regular Expression Operations](<https://docs.python.org/3.7/library/re.html>) for additional information on how to use the Python Regular Expression module. __

From Column`fromcol`\- When selecting rows by values, this parameter selects which column to use when matching cell values to Selected Row Values to determine which rows are scoped. 

Select Cols`extractcols`\- ⊞ \- This parameter allows you to pick different ways of specifying the columns scoped. 
* All`all`\- All columns scoped.
* by Name`byname`\- Columns scoped using Start Col Name and End Col Name parameters.
* by Index`byindex`\- Columns scoped using Start Col Index and End Col Index parameters.
* by Start Name, End Index`bynameindex`\- Columns scoped using Start Col Name and End Col Index parameters.
* by Start Index, End Name`byindexname`\- Columns scoped using Start Col Index and End Col Name parameters.
* by Values`bynames`\- Columns scoped by specifying the column values explicitly.
* by Condition`byexpr`\- Columns scoped by an expression to be evaluated for the from row.


Start Col Name`colnamestart`\- Specify the column name to start the scope range from. 

Start Col Index`colindexstart`\- Specify the column index to start the scope range from. 

End Col Name`colnameend`\- Specify the column name to end the scope range. 

End Col Index`colindexend`\- Specify the column index to end the scope range. 

Col Select Values`colnames`\- Specify actual column names that you want to scope. You can use pattern matching, for example colvalue[1-4] will scope all the columns named colvalue1 thru colvalue4. 

Col Select Condition`colexpr`\- Specify an expression that will be evaluated. If the expression evaluates to true, the column will be scoped. See Row Select Condition for more details. 

From Row`fromrow`\- When scoping columns by Specified Names, this parameter selects which row to use when matching cell values to Selected Col Values to determine which columns are scoped. 

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

## 

Operator Inputs
* Input 0:  \- Data to operate on.
  * Input 1:  \- _(optional)_ A [Table DAT](<./Table_DAT.md> "Table DAT") with a`before`and`after`column containing strings to sustitute in the first input. This doesn't have to be the whole cell content but can be any partial string as well.

## 

Info CHOP Channels

Extra Information for the Substitute DAT can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). __

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
[Art-Net ](<./Art-Net_DAT.md> "Art-Net DAT")• [Audio Devices ](<./Audio_Devices_DAT.md> "Audio Devices DAT")• [CHOP Execute ](<./CHOP_Execute_DAT.md> "CHOP Execute DAT")• [CHOP to ](<./CHOP_to_DAT.md> "CHOP to DAT")• [Clip ](<./Clip_DAT.md> "Clip DAT")• [Convert ](<./Convert_DAT.md> "Convert DAT")• [CPlusPlus ](<./CPlusPlus_DAT.md> "CPlusPlus DAT")• [DAT ](<./DAT.md> "DAT")• [ Execute ](<./DAT_Execute_DAT.md> "DAT Execute DAT")• [DAT Export ](<./DAT_Export.md> "DAT Export")• [Error ](<./Error_DAT.md> "Error DAT")• [EtherDream ](<./EtherDream_DAT.md> "EtherDream DAT")• [Evaluate ](<./Evaluate_DAT.md> "Evaluate DAT")• [Examine ](<./Examine_DAT.md> "Examine DAT")• [Execute ](<./Execute_DAT.md> "Execute DAT")• [FIFO ](<./FIFO_DAT.md> "FIFO DAT")• [File In ](<./File_In_DAT.md> "File In DAT")• [File Out ](<./File_Out_DAT.md> "File Out DAT")• [Folder ](<./Folder_DAT.md> "Folder DAT")• [In ](<./In_DAT.md> "In DAT")• [Indices ](<./Indices_DAT.md> "Indices DAT")• [Info ](<./Info_DAT.md> "Info DAT")• [Insert ](<./Insert_DAT.md> "Insert DAT")• [JSON ](<./JSON_DAT.md> "JSON DAT")• [Keyboard In ](<./Keyboard_In_DAT.md> "Keyboard In DAT")• [Lookup ](<./Lookup_DAT.md> "Lookup DAT")• [Media File Info ](<./Media_File_Info_DAT.md> "Media File Info DAT")• [Merge ](<./Merge_DAT.md> "Merge DAT")• [MIDI Event ](<./MIDI_Event_DAT.md> "MIDI Event DAT")• [MIDI In ](<./MIDI_In_DAT.md> "MIDI In DAT")• [Monitors ](<./Monitors_DAT.md> "Monitors DAT")• [MPCDI ](<./MPCDI_DAT.md> "MPCDI DAT")• [MQTT Client ](<./MQTT_Client_DAT.md> "MQTT Client DAT")• [Multi Touch In ](<./Multi_Touch_In_DAT.md> "Multi Touch In DAT")• [NDI ](<./NDI_DAT.md> "NDI DAT")• [Null ](<./Null_DAT.md> "Null DAT")• [OP Execute ](<./OP_Execute_DAT.md> "OP Execute DAT")• [OP Find ](<./OP_Find_DAT.md> "OP Find DAT")• [OSC In ](<./OSC_In_DAT.md> "OSC In DAT")• [OSC Out ](<./OSC_Out_DAT.md> "OSC Out DAT")• [Out ](<./Out_DAT.md> "Out DAT")• [Panel Execute ](<./Panel_Execute_DAT.md> "Panel Execute DAT")• [Parameter ](<./Parameter_DAT.md> "Parameter DAT")• [Parameter Execute ](<./Parameter_Execute_DAT.md> "Parameter Execute DAT")• [ParGroup Execute ](<./ParGroup_Execute_DAT.md> "ParGroup Execute DAT")• [Perform ](<./Perform_DAT.md> "Perform DAT")• [POP to ](<./POP_to_DAT.md> "POP to DAT")• [Render Pick ](<./Render_Pick_DAT.md> "Render Pick DAT")• [Reorder ](<./Reorder_DAT.md> "Reorder DAT")• [Script ](<./Script_DAT.md> "Script DAT")• [Select ](<./Select_DAT.md> "Select DAT")• [Serial ](<./Serial_DAT.md> "Serial DAT")• [Serial Devices ](<./Serial_Devices_DAT.md> "Serial Devices DAT")• [SocketIO ](<./SocketIO_DAT.md> "SocketIO DAT")• [SOP to ](<./SOP_to_DAT.md> "SOP to DAT")• [Sort ](<./Sort_DAT.md> "Sort DAT")• Substitute • [Switch ](<./Switch_DAT.md> "Switch DAT")• [Table ](<./Table_DAT.md> "Table DAT")• [TCP/IP ](<./TCP/IP_DAT.md> "TCP/IP DAT")• [Text ](<./Text_DAT.md> "Text DAT")• [Touch In ](<./Touch_In_DAT.md> "Touch In DAT")• [Touch Out ](<./Touch_Out_DAT.md> "Touch Out DAT")• [Transpose ](<./Transpose_DAT.md> "Transpose DAT")• [TUIO In ](<./TUIO_In_DAT.md> "TUIO In DAT")• [UDP In ](<./UDP_In_DAT.md> "UDP In DAT")• [UDP Out ](<./UDP_Out_DAT.md> "UDP Out DAT")• [UDT In ](<./UDT_In_DAT.md> "UDT In DAT")• [UDT Out ](<./UDT_Out_DAT.md> "UDT Out DAT")• [Video Devices ](<./Video_Devices_DAT.md> "Video Devices DAT")• [Web Client ](<./Web_Client_DAT.md> "Web Client DAT")• [Web ](<./Web_DAT.md> "Web DAT")• [Web Server ](<./Web_Server_DAT.md> "Web Server DAT")• [WebRTC ](<./WebRTC_DAT.md> "WebRTC DAT")• [WebSocket ](<./WebSocket_DAT.md> "WebSocket DAT")• [XML ](<./XML_DAT.md> "XML DAT")
