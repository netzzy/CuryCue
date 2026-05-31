# Parameter DAT

##   
  
Summary

The Parameter DAT outputs a table of parameter names and values of an operator, including custom parameters, from any OP type. 

It can output pre-evaluated expressions, the [Parameter Mode](<./Parameter_Mode.md> "Parameter Mode") plus all attributes that define parameters - their type, label, ranges, menu items, limits, etc. in up to 24 columns of information. 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[parameterDAT_Class](<./ParameterDAT_Class.md> "ParameterDAT Class")

## 

Parameters - Parameter Page

Operators`ops`\- The operators determine where to obtain the channels. Specify or more operator names or paths. Examples:`wave1`,`slider*`,`constant[1-9] constant[10-19:2]`,`../base1`. Or select the operators using the menu. 

Parameters`parameters`\- The list of parameters names (which can include wildcards) you want to get from the OP(s). One or more parameter, or * for all parameters. You can also specify a "NOT" selection with an`^`. Or select the parameter using the menu. See [Pattern Matching](<./Pattern_Matching.md> "Pattern Matching"). 

Include Op Name`includeopname`\- Adds the OP name to the beginning of each parameter name in the table 

Rename from`renamefrom`\- See [Pattern Matching](<./Pattern_Matching.md> "Pattern Matching"). 

Rename to`renameto`\- See [Pattern Expansion](<./Pattern_Expansion.md> "Pattern Expansion"). 

Custom`custom`\- Output the operators' custom parameters. 

Built-In`builtin`\- Output the operators' built-in parameters. 

## 

Parameters - Output Page

Toggles for information about the parameter and its value 

Header`header`\- Outputs the column headers. 

Name`name`\- Outputs the parameter name. 

Value`value`\- Outputs the evaluated parameter value. 

Eval`eval`\- Outputs the evaluated parameter value as a python object. 

Constant`constant`\- Outputs the current constant value of the parameter. 

Expression`expression`\- Outputs the current python expression of the parameter. 

Export`export`\- Outputs the export path of the parameter. 

Mode`mode`\- Outputs the current mode of the parameter (constant, expression, or export). 

Style`style`\- Outputs what format the parameter is (eg. Float for float parameters, Menu for menu parameters etc.). 

Tuplet Name`tupletname`\- Outputs the name of the tuplet the parameter is in. For example, tx on the Geometry COMP is a part of the 't' tuplet. 

Size`size`\- Outputs the size of the tuplet. For example, tx on the Geometry COMP would have a tuplet size of 3 since it's a part of the 't' tuplet with 3 parameters. 

Path`path`\- Outputs the path to the node. 

Menu Index`menuindex`\- If the parameter is a menu, then output the selected index of the menu. 

## 

Parameters - Define Page

Toggles for information that define the parameter. 

Min/Max`minmax`\- Outputs the minimum and maximum values of the parameter. These values will clamp the value parameter to be within the range. If clampmin is 0 then the minimum will not clamp and the row/column entry will be 0. If clampmax is 0 then the maximum will not clamp and the row/column entry will be 1. 

Clamp Min/Max`clampminmax`\- Outputs whether or not the parameter has a clamped min or clamped max. If true, then the values are defined by min/max columns. 

Norm Min/Max`normminmax`\- Outputs the minimum and maximum values of the parameter in the interface (ie. the minimum and maximum values of a slider). 

Default`default`\- Outputs the default value of the parameter 

Enabled`enabled`\- Outputs whether the parameter is currently enabled 

Read Only`readonly`\- Outputs whether the parameter is currently read-only 

Section`section`\- Outputs whether the parameter has a section divider/separator (ie. line) above it. 

Menu Names`menunames`\- Outputs a list of the menu names for any menu parameters. 

Menu Labels`menulabels`\- Outputs a list of the menu labels for any menu parameters. 

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


TouchDesigner Build: Latest\n2021.100002019.146502018.28070

DATs   
---  
[Art-Net ](<./Art-Net_DAT.md> "Art-Net DAT")• [Audio Devices ](<./Audio_Devices_DAT.md> "Audio Devices DAT")• [CHOP Execute ](<./CHOP_Execute_DAT.md> "CHOP Execute DAT")• [CHOP to ](<./CHOP_to_DAT.md> "CHOP to DAT")• [Clip ](<./Clip_DAT.md> "Clip DAT")• [Convert ](<./Convert_DAT.md> "Convert DAT")• [CPlusPlus ](<./CPlusPlus_DAT.md> "CPlusPlus DAT")• [DAT ](<./DAT.md> "DAT")• [ Execute ](<./DAT_Execute_DAT.md> "DAT Execute DAT")• [DAT Export ](<./DAT_Export.md> "DAT Export")• [Error ](<./Error_DAT.md> "Error DAT")• [EtherDream ](<./EtherDream_DAT.md> "EtherDream DAT")• [Evaluate ](<./Evaluate_DAT.md> "Evaluate DAT")• [Examine ](<./Examine_DAT.md> "Examine DAT")• [Execute ](<./Execute_DAT.md> "Execute DAT")• [FIFO ](<./FIFO_DAT.md> "FIFO DAT")• [File In ](<./File_In_DAT.md> "File In DAT")• [File Out ](<./File_Out_DAT.md> "File Out DAT")• [Folder ](<./Folder_DAT.md> "Folder DAT")• [In ](<./In_DAT.md> "In DAT")• [Indices ](<./Indices_DAT.md> "Indices DAT")• [Info ](<./Info_DAT.md> "Info DAT")• [Insert ](<./Insert_DAT.md> "Insert DAT")• [JSON ](<./JSON_DAT.md> "JSON DAT")• [Keyboard In ](<./Keyboard_In_DAT.md> "Keyboard In DAT")• [Lookup ](<./Lookup_DAT.md> "Lookup DAT")• [Media File Info ](<./Media_File_Info_DAT.md> "Media File Info DAT")• [Merge ](<./Merge_DAT.md> "Merge DAT")• [MIDI Event ](<./MIDI_Event_DAT.md> "MIDI Event DAT")• [MIDI In ](<./MIDI_In_DAT.md> "MIDI In DAT")• [Monitors ](<./Monitors_DAT.md> "Monitors DAT")• [MPCDI ](<./MPCDI_DAT.md> "MPCDI DAT")• [MQTT Client ](<./MQTT_Client_DAT.md> "MQTT Client DAT")• [Multi Touch In ](<./Multi_Touch_In_DAT.md> "Multi Touch In DAT")• [NDI ](<./NDI_DAT.md> "NDI DAT")• [Null ](<./Null_DAT.md> "Null DAT")• [OP Execute ](<./OP_Execute_DAT.md> "OP Execute DAT")• [OP Find ](<./OP_Find_DAT.md> "OP Find DAT")• [OSC In ](<./OSC_In_DAT.md> "OSC In DAT")• [OSC Out ](<./OSC_Out_DAT.md> "OSC Out DAT")• [Out ](<./Out_DAT.md> "Out DAT")• [Panel Execute ](<./Panel_Execute_DAT.md> "Panel Execute DAT")• Parameter • [Parameter Execute ](<./Parameter_Execute_DAT.md> "Parameter Execute DAT")• [ParGroup Execute ](<./ParGroup_Execute_DAT.md> "ParGroup Execute DAT")• [Perform ](<./Perform_DAT.md> "Perform DAT")• [POP to ](<./POP_to_DAT.md> "POP to DAT")• [Render Pick ](<./Render_Pick_DAT.md> "Render Pick DAT")• [Reorder ](<./Reorder_DAT.md> "Reorder DAT")• [Script ](<./Script_DAT.md> "Script DAT")• [Select ](<./Select_DAT.md> "Select DAT")• [Serial ](<./Serial_DAT.md> "Serial DAT")• [Serial Devices ](<./Serial_Devices_DAT.md> "Serial Devices DAT")• [SocketIO ](<./SocketIO_DAT.md> "SocketIO DAT")• [SOP to ](<./SOP_to_DAT.md> "SOP to DAT")• [Sort ](<./Sort_DAT.md> "Sort DAT")• [Substitute ](<./Substitute_DAT.md> "Substitute DAT")• [Switch ](<./Switch_DAT.md> "Switch DAT")• [Table ](<./Table_DAT.md> "Table DAT")• [TCP/IP ](<./TCP/IP_DAT.md> "TCP/IP DAT")• [Text ](<./Text_DAT.md> "Text DAT")• [Touch In ](<./Touch_In_DAT.md> "Touch In DAT")• [Touch Out ](<./Touch_Out_DAT.md> "Touch Out DAT")• [Transpose ](<./Transpose_DAT.md> "Transpose DAT")• [TUIO In ](<./TUIO_In_DAT.md> "TUIO In DAT")• [UDP In ](<./UDP_In_DAT.md> "UDP In DAT")• [UDP Out ](<./UDP_Out_DAT.md> "UDP Out DAT")• [UDT In ](<./UDT_In_DAT.md> "UDT In DAT")• [UDT Out ](<./UDT_Out_DAT.md> "UDT Out DAT")• [Video Devices ](<./Video_Devices_DAT.md> "Video Devices DAT")• [Web Client ](<./Web_Client_DAT.md> "Web Client DAT")• [Web ](<./Web_DAT.md> "Web DAT")• [Web Server ](<./Web_Server_DAT.md> "Web Server DAT")• [WebRTC ](<./WebRTC_DAT.md> "WebRTC DAT")• [WebSocket ](<./WebSocket_DAT.md> "WebSocket DAT")• [XML ](<./XML_DAT.md> "XML DAT")
