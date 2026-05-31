# OP Find DAT

##   
  
Summary

The OP Find DAT traverses the component hierarchy starting at one component and looking at all nodes within that component, and outputs a table with one row per node that matches criteria the user chooses. For example, the criteria could be all Ramp TOPs, or all nodes whose name starts with “`wave`”, or all nodes with the Clone parameter set to “`master1`”, or all Geometry components with a tag called “`emitter`”. 

The criteria can limited to include only nodes of certain families, or certain operator types. It can filter on matching its path, certain parameters containing certain values (both constant and expressions), comments, tags, or the content of a DAT containing certain strings. 

You can also cause the DAT to only look to some depth of the hierarchy from the specified component, such as 2 levels down, or limitless. 

Criteria can be case-sensitive or not, but case-sensitive On or Off applies to all criteria in the OP Find DAT. 

Furthermore you can exclude some nodes using more specialized criteria by returning a True of False in a callback contained in the attached callback DAT. 

With the Combine Filters Menu (Any or All, Default is All), you can do an "or" or "and" on the pattern matching criterea. 

It also takes an optional DAT containing a list of operators (eg, another OP Find DAT) which can be used to chain filters. 

### Output Columns

There is a variety of columns that you can select from including`name`,`id`,`paths`,`type`and`tags`. (`id`is a member of the operator, which is an integer unique to the node, and doesn't change during the running of the TouchDesigner process.) 

You can also output custom columns by defining the column names in the callback DAT, and filling in the column cells via another function in the callback DAT. For example, you can output a custom column which is the`tx`parameter value of the node. 

You can control when the OP Find DAT cooks. Normally it cooks whenever any of the nodes in the specified hierarchy changes. Using the Active Cook menu parameter, you can also force-cook it every frame, or turn off cooking entirely. You can also click the Pulse parameter on Active Cook in order to force-cook it once, or do the equivalent using the node.cookpulse.pulse() python call. 

Instead of being give the path to a component to start at, the OP Find DAT can take an input DAT containing a pre-generated list of paths to nodes to start from, and merge the results of each input line together in the output. To use this, the input DAT should contain the node “id” as the first column, which can be generated with another OP Find DAT with the Column called “ID” turned on. 

For example, say you first list all components that are panels, then you separate into groups based on type or Clone parameter. The first OP Find DAT pre-filters a huge hierarchy to a small fraction of the nodes, the subsequent OP Find DATs are operating on simpler sets to eliminate a lot of checking and cooking. 

Refer to Help -> [Operator Snippets](<./OP_Snippets.md> "OP Snippets"). 

See also: [Script DAT](<./Script_DAT.md> "Script DAT")

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[opfindDAT_Class](<./OpfindDAT_Class.md> "OpfindDAT Class")

## 

Parameters - Component Page

Active Cook`activecook`\- ⊞ \- Determines when to cook the DAT. 
* Off`off`\- This stops the operator from cooking altogether.
* Automatic`auto`\- Only cook / update the contents when the results would change.
* Always`always`\- Continually cook this operator repeatedly for update cases that might be missed.
* Incremental`incremental`\- This will cook each frame, but only add one result per cook, until all results are added. At that point cooking stops.


Cook Pulse`cookpulse`\- Manually force the OP Find DAT to update. 

Component`component`\- The path to the component where the search starts from. 

Include Component`includecomponent`\- Include the component the search starts from in the search itself. 

Include Wire Hierarchy`includewired`\- Any components wired to the starting component are included in the search. 

Minimum Depth`mindepth`\- Set a minmum depth for the sub-components the OP Find DAT should recursively search through. 

Limit Max Depth`limitmaxdepth`\- Turns on the Maximum Depth parameter to limit searching through sub-components. Turning this toggle off will search through all sub-networks. 

Maximum Depth`maxdepth`\- Set the maximum depth for the sub-components the OP Find DAT should recursively search through. 

Limit Max Operators`limitmaxops`\- Limit the total number of operators iterated in the search. 

Maximum Operators`maxops`\- Number of operators the search is limited to. 

## 

Parameters - Families Page

The page of parameters determines which operator families are included in the search. 

Object COMPs`objects`\- Include Object COMPs, like Geo COMP, in the search. 

Panel COMPs`panels`\- Include Panel COMPs, like Container COMP, in the search. 

Other COMPs`other`\- Include other type COMPs, like Base COMP, in the search. 

TOPs`tops`\- Include DAT family operators in the search. 

CHOPs`chops`\- Include CHOP family operators in the search. 

SOPs`sops`\- Include SOP family operators in the search. 

MATs`mats`\- Include MAT family operators in the search. 

DATs`dats`\- Include DAT family operators in the search. 

## 

Parameters - Filters Page

Case Sensitive`casesensitive`\- Use case sensitivity in all pattern matching below. 

Combine Filters`combinefilters`\- ⊞ \- Combine 'All', 'Any' or 'Custom' of the filters below to get a match. 'Custom' allows for specifying a subselection of filters with 'or' and 'and' keywords. 
* All`all`\- All filters must match for an operator to be included in the search result. (AND)
* Any`any`\- Any of the filter conditions must be met for an operator to be included in the search result. (OR)
* Custom`custom`-


Custom Combine`customcombine`\- Specify which filters to combine in the search. 

Name`namefilter`\- Use the operator's names like 'wave1', 'wave2', etc. 

Type`typefilter`\- Use names like`waveCHOP`and`panelexecuteDAT`. Look at the column Type to see the syntax. 

Parent Shortcut`parentshortcutfilter`\- Only match operators that include the here specified Parent Shortcut. 

OP Shortcut`opshortcutfilter`\- Only match operators that include the here specified OP Shortcut. 

Path`pathfilter`\- Specify a path that the operator should be located in. 

Parent Path (relative)`parentfilter`\- Specify a relative parent path that operators should be located in. This is a filter option on the`parentPath`column of this DAT that can be enabled by toggling the`Parent Path`parameter on this DAT's`Columns`page. 

Exclude Path (relative)`excludefilter`\- Specify a relative path that should be excluded from the search. 

Wire Path`wirepathfilter`\- 

Comment`commentfilter`\- Only match operators that include the here specified comment string. 

Tags`tagsfilter`\- Only match operators that match the here specified tags. Multiple tags can be searched for as a space seperated list. 

DAT Text`textfilter`\- Only include operators that - in the case of being from the DAT family - match specified string in their content. 

Par Name`parnamefilter`\- Only match operators with specified parameter name. Parameters must match ALL of name, value and expression to be included. 

Par Value`parvaluefilter`\- Only include operators that match specified parameter value. Parameters must match ALL of name, value and expression to be included. 

Par Expression`parexpressionfilter`\- Only include operators that match specified parameter expression string. Parameters must match ALL of name, value and expression to be included. 

Par Non-Default Only`parnondefaultonly`\- Only match with parameters that are non-default values. 

## 

Parameters - Columns Page

Use Legacy Columns`legacycols`\- Use only when expecting column headers to be named with legacy titles. 

ID`idcol`\- An integer that uniquely defines the node in this process. It's the same number for the duration of the process, but may be different when you run the process again. 

Name`namecol`\- Inlcude the name of the operator in the result table. 

Type`typecol`\- Include the operator type in the result table. For example`rampTOP`. 

Parent Shortcut`parentshortcutcol`\- Include the operator's Parent Shortcut in the result table. 

OP Shortcut`opshortcutcol`\- Include the operator's OP Shortcut in the result table. 

Path`pathcol`\- Include the operator's path in the result table. 

Relative Path`relpathcol`\- Include the operator's, relative to the search root, path in the result table. 

Parent Path`parentpath`\- Include the parent path. 

Wire Path`wirepathcol`\- Include the operator's wire path in the result table. 

Depth`depthcol`\- Include a column showing the relative depth to the root path of the found operator. 

Cook Times`cooktimescol`\- Include cook-time of found operators. 

Tags`tagscol`\- Include the operator's tags. 

General Properties`genprop`\- Include the operator's name, id, isCOMP, node position, node size and dock id in the result table. 

CPU Time`cputime`\- Include the operator's CPU cooktime in the result table. 

GPU Time`gputime`\- Include the operator's GPU cooktime in the result table. 

CPU Memory`cpumem`\- Include the operator's CPU memory in the result table. 

GPU Memory`gpumem`\- Include the operator's GPU memory in the result table. 

Children`children`\- Include the children of the operator in the result table. 

## 

Parameters - Callbacks Page

Callbacks DAT`callbacks`\- Path to a DAT containing callbacks for each event received. See [opfindDAT_Class](<./OpfindDAT_Class.md> "OpfindDAT Class") for usage. 

Convert Bool to Int`convertbool`\- For boolean logic values, the value will be '1' or '0'. When this parameter is Off, they will be 'True" or 'False'. 

Convert None to Empty`convertnone`\- For 'None' values, the value will be converted to Empty. 

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


TouchDesigner Build: Latest\n2021.100002018.28070before 2018.28070

DATs   
---  
[Art-Net ](<./Art-Net_DAT.md> "Art-Net DAT")• [Audio Devices ](<./Audio_Devices_DAT.md> "Audio Devices DAT")• [CHOP Execute ](<./CHOP_Execute_DAT.md> "CHOP Execute DAT")• [CHOP to ](<./CHOP_to_DAT.md> "CHOP to DAT")• [Clip ](<./Clip_DAT.md> "Clip DAT")• [Convert ](<./Convert_DAT.md> "Convert DAT")• [CPlusPlus ](<./CPlusPlus_DAT.md> "CPlusPlus DAT")• [DAT ](<./DAT.md> "DAT")• [ Execute ](<./DAT_Execute_DAT.md> "DAT Execute DAT")• [DAT Export ](<./DAT_Export.md> "DAT Export")• [Error ](<./Error_DAT.md> "Error DAT")• [EtherDream ](<./EtherDream_DAT.md> "EtherDream DAT")• [Evaluate ](<./Evaluate_DAT.md> "Evaluate DAT")• [Examine ](<./Examine_DAT.md> "Examine DAT")• [Execute ](<./Execute_DAT.md> "Execute DAT")• [FIFO ](<./FIFO_DAT.md> "FIFO DAT")• [File In ](<./File_In_DAT.md> "File In DAT")• [File Out ](<./File_Out_DAT.md> "File Out DAT")• [Folder ](<./Folder_DAT.md> "Folder DAT")• [In ](<./In_DAT.md> "In DAT")• [Indices ](<./Indices_DAT.md> "Indices DAT")• [Info ](<./Info_DAT.md> "Info DAT")• [Insert ](<./Insert_DAT.md> "Insert DAT")• [JSON ](<./JSON_DAT.md> "JSON DAT")• [Keyboard In ](<./Keyboard_In_DAT.md> "Keyboard In DAT")• [Lookup ](<./Lookup_DAT.md> "Lookup DAT")• [Media File Info ](<./Media_File_Info_DAT.md> "Media File Info DAT")• [Merge ](<./Merge_DAT.md> "Merge DAT")• [MIDI Event ](<./MIDI_Event_DAT.md> "MIDI Event DAT")• [MIDI In ](<./MIDI_In_DAT.md> "MIDI In DAT")• [Monitors ](<./Monitors_DAT.md> "Monitors DAT")• [MPCDI ](<./MPCDI_DAT.md> "MPCDI DAT")• [MQTT Client ](<./MQTT_Client_DAT.md> "MQTT Client DAT")• [Multi Touch In ](<./Multi_Touch_In_DAT.md> "Multi Touch In DAT")• [NDI ](<./NDI_DAT.md> "NDI DAT")• [Null ](<./Null_DAT.md> "Null DAT")• [OP Execute ](<./OP_Execute_DAT.md> "OP Execute DAT")• OP Find • [OSC In ](<./OSC_In_DAT.md> "OSC In DAT")• [OSC Out ](<./OSC_Out_DAT.md> "OSC Out DAT")• [Out ](<./Out_DAT.md> "Out DAT")• [Panel Execute ](<./Panel_Execute_DAT.md> "Panel Execute DAT")• [Parameter ](<./Parameter_DAT.md> "Parameter DAT")• [Parameter Execute ](<./Parameter_Execute_DAT.md> "Parameter Execute DAT")• [ParGroup Execute ](<./ParGroup_Execute_DAT.md> "ParGroup Execute DAT")• [Perform ](<./Perform_DAT.md> "Perform DAT")• [POP to ](<./POP_to_DAT.md> "POP to DAT")• [Render Pick ](<./Render_Pick_DAT.md> "Render Pick DAT")• [Reorder ](<./Reorder_DAT.md> "Reorder DAT")• [Script ](<./Script_DAT.md> "Script DAT")• [Select ](<./Select_DAT.md> "Select DAT")• [Serial ](<./Serial_DAT.md> "Serial DAT")• [Serial Devices ](<./Serial_Devices_DAT.md> "Serial Devices DAT")• [SocketIO ](<./SocketIO_DAT.md> "SocketIO DAT")• [SOP to ](<./SOP_to_DAT.md> "SOP to DAT")• [Sort ](<./Sort_DAT.md> "Sort DAT")• [Substitute ](<./Substitute_DAT.md> "Substitute DAT")• [Switch ](<./Switch_DAT.md> "Switch DAT")• [Table ](<./Table_DAT.md> "Table DAT")• [TCP/IP ](<./TCP/IP_DAT.md> "TCP/IP DAT")• [Text ](<./Text_DAT.md> "Text DAT")• [Touch In ](<./Touch_In_DAT.md> "Touch In DAT")• [Touch Out ](<./Touch_Out_DAT.md> "Touch Out DAT")• [Transpose ](<./Transpose_DAT.md> "Transpose DAT")• [TUIO In ](<./TUIO_In_DAT.md> "TUIO In DAT")• [UDP In ](<./UDP_In_DAT.md> "UDP In DAT")• [UDP Out ](<./UDP_Out_DAT.md> "UDP Out DAT")• [UDT In ](<./UDT_In_DAT.md> "UDT In DAT")• [UDT Out ](<./UDT_Out_DAT.md> "UDT Out DAT")• [Video Devices ](<./Video_Devices_DAT.md> "Video Devices DAT")• [Web Client ](<./Web_Client_DAT.md> "Web Client DAT")• [Web ](<./Web_DAT.md> "Web DAT")• [Web Server ](<./Web_Server_DAT.md> "Web Server DAT")• [WebRTC ](<./WebRTC_DAT.md> "WebRTC DAT")• [WebSocket ](<./WebSocket_DAT.md> "WebSocket DAT")• [XML ](<./XML_DAT.md> "XML DAT")
