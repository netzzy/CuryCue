# XML DAT

##   
  
Summary

The XML DAT can be used to parse arbitrary XML and SGML/HTML formatted data. Once formatted, selected sections of the text can be output for further processing. 

One approach to parsing with the XML DAT is to read the XML with a Text DAT or a Web DAT, and pass that to a default XML DAT. Then you start to refine your selection by changing the match-all pattern (the "*"), to strings that reduce the elements that are in the output. 

### 

XML and HTML Background

XML and HTML data consists of a tree like structure consisting of elements. Each element can be either tagged or contain arbitrary text. Elements may be nested. Tagged elements begin with an opening section and usually are terminated with a closing section. 

Example: 
[code] 
     <greeting a="1" b="2" c="3"> Hello there. </greeting>			
    
[/code]

In the example above are two elements. The first is a **tag** element named _greeting_ with attributes _a, b_ and _c_. The second element is a **text** element consisting of "_Hello there._ " 

### 

XML DAT Operation

The XML DAT begins by parsing its input, creating an internal tree of elements. 

The **Element Scope** parameters are then used to filter out unwanted elements. The remaining elements are then used to create the output. The format of the output is determined by the **Format** parameters. The **Output** parameters can then be used to futher limit the information displayed for each scoped element. 

Each parsed element contains a number of details: 

**Label** \- Each element is given an arbitrary label named n0, n1, n2 etc. All elements are children of the reserved element labelled 'root'. 

**Type** \- Elements are mainly of type 'tag' or 'text', though tag types can be further classified into 'doctype', 'declaration', 'comment' or 'entity'. 

**Text** \- The text of an element refers to the tag attribute of an element, or the arbitrary text contents. In the above example, the first element would be of type 'tag' and contain text of 'greeting'. The second element would be of type 'text' and contain text of 'Hello there.' 

**Level** \- This describes how deeply nested an element is. For example the single root element always has a level of 0. 

**Parent** \- Each element contains one parent. The root element does not have a parent. 

**Children** \- Each element can have an arbitrary number of children elements. 

**Attributes** \- Each tagged element can have an arbitrary number of attributes. Each attribute consists of a name and a value. In the above example, the greeting tag would contain 3 attributes (with names a, b and c and values 1, 2, and 3 respectively). 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[xmlDAT_Class](<./XmlDAT_Class.md> "XmlDAT Class")

## 

Parameters - Format Page

Parse SGML/HTML`sgml`\- If enabled, the input should be in SGML/HTML format. This includes form data. If disabled, XML format is assumed. 

Merge`merge`\- ⊞ \- Merge and label can be used to combine two inputs of data. The second input must be XML formatted, and not SGML/HTML. These two parameters control where and how the second input is merged. 
* Before Element`before`\- The second input is merged before the specified element label.
* After Element`after`\- The second input is merged after the specified element label.
* Inside Element`inside`\- The second input is merged as a child of the specified element label.
* Replace Element`replace`\- The second input replaces the specified element label.


Label`mlabel`\- Specify the element at which the merge occurs. 

## 

Parameters - Element Scope Page

This section of parameters controls which elements are selected for output. By default all elements are selected. 

Label`label`\- Element labels must match this parameter. 

Type`type`\- Element types must match this parameter. 

Text`text`\- Element text must match this parameter. 

Name`name`\- If an element contains attributes, at least one must have a name matching this parameter. 

Value`value`\- If an element contains attributes, at least one must have a value matching this parameter. 

Parent Label`plabel`\- Elements must have a parent whose label matches this parameter. 

Parent Type`ptype`\- Elements must have a parent whose type matches this parameter. 

Parent Text`ptext`\- Elements must have a parent whose text matches this parameter. 

Parent Name`pname`\- Elements must have a parent with an attribute whose name matches this parameter. 

Parent Value`pvalue`\- Elements must have a parent with an attribute whose value matches this parameter. 

## 

Parameters - Output Page

Once a selection of elements have been selected for output, its output can be further refined. 

Name Attributes`oaname`\- Only output attributes whos name match this parameter. 

Value Attributes`oavalue`\- Only output attributes whose value match this parameter. 

Children Labels`oclabel`\- Only output children whose label match this parameter. 

Show`show`\- ⊞ \- This controls how the selected elements are presented. 
* Summary Table`sumtable`-
* Summary Tree`sumtree`\- This output selection is similar to the summary table, except it outputs an indented ascii representation of the tree. It can be used to quickly identify areas of interest while picking appropriate parameters.
* XML`xml`\- This outputs an XML compliant tree of the selected elements. It can then be fed into another XML DAT for further processing.
* Attributes per Row`attribs`\- This outputs a table of all attributes for the selected elements. Each element attribute is output on a separate row.
* Attributes per Column`attribscol`\- This outputs a table of all attributes for the selected elements. Each element is output in output on a single row, where each column represents one attribute.
* Children`children`\- This outputs a table of all children for the selected elements.
* Text`text`\- This outputs all text contents from all elements of type 'text'.


Label Prefix`lprefix`\- This determines whether or not the element label is prefixed when outputting tables or attributes or children. 

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
* Input 0:  -
  * Input 1:  -

## 

Info CHOP Channels

Extra Information for the XML DAT can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). __

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
[Art-Net ](<./Art-Net_DAT.md> "Art-Net DAT")• [Audio Devices ](<./Audio_Devices_DAT.md> "Audio Devices DAT")• [CHOP Execute ](<./CHOP_Execute_DAT.md> "CHOP Execute DAT")• [CHOP to ](<./CHOP_to_DAT.md> "CHOP to DAT")• [Clip ](<./Clip_DAT.md> "Clip DAT")• [Convert ](<./Convert_DAT.md> "Convert DAT")• [CPlusPlus ](<./CPlusPlus_DAT.md> "CPlusPlus DAT")• [DAT ](<./DAT.md> "DAT")• [ Execute ](<./DAT_Execute_DAT.md> "DAT Execute DAT")• [DAT Export ](<./DAT_Export.md> "DAT Export")• [Error ](<./Error_DAT.md> "Error DAT")• [EtherDream ](<./EtherDream_DAT.md> "EtherDream DAT")• [Evaluate ](<./Evaluate_DAT.md> "Evaluate DAT")• [Examine ](<./Examine_DAT.md> "Examine DAT")• [Execute ](<./Execute_DAT.md> "Execute DAT")• [FIFO ](<./FIFO_DAT.md> "FIFO DAT")• [File In ](<./File_In_DAT.md> "File In DAT")• [File Out ](<./File_Out_DAT.md> "File Out DAT")• [Folder ](<./Folder_DAT.md> "Folder DAT")• [In ](<./In_DAT.md> "In DAT")• [Indices ](<./Indices_DAT.md> "Indices DAT")• [Info ](<./Info_DAT.md> "Info DAT")• [Insert ](<./Insert_DAT.md> "Insert DAT")• [JSON ](<./JSON_DAT.md> "JSON DAT")• [Keyboard In ](<./Keyboard_In_DAT.md> "Keyboard In DAT")• [Lookup ](<./Lookup_DAT.md> "Lookup DAT")• [Media File Info ](<./Media_File_Info_DAT.md> "Media File Info DAT")• [Merge ](<./Merge_DAT.md> "Merge DAT")• [MIDI Event ](<./MIDI_Event_DAT.md> "MIDI Event DAT")• [MIDI In ](<./MIDI_In_DAT.md> "MIDI In DAT")• [Monitors ](<./Monitors_DAT.md> "Monitors DAT")• [MPCDI ](<./MPCDI_DAT.md> "MPCDI DAT")• [MQTT Client ](<./MQTT_Client_DAT.md> "MQTT Client DAT")• [Multi Touch In ](<./Multi_Touch_In_DAT.md> "Multi Touch In DAT")• [NDI ](<./NDI_DAT.md> "NDI DAT")• [Null ](<./Null_DAT.md> "Null DAT")• [OP Execute ](<./OP_Execute_DAT.md> "OP Execute DAT")• [OP Find ](<./OP_Find_DAT.md> "OP Find DAT")• [OSC In ](<./OSC_In_DAT.md> "OSC In DAT")• [OSC Out ](<./OSC_Out_DAT.md> "OSC Out DAT")• [Out ](<./Out_DAT.md> "Out DAT")• [Panel Execute ](<./Panel_Execute_DAT.md> "Panel Execute DAT")• [Parameter ](<./Parameter_DAT.md> "Parameter DAT")• [Parameter Execute ](<./Parameter_Execute_DAT.md> "Parameter Execute DAT")• [ParGroup Execute ](<./ParGroup_Execute_DAT.md> "ParGroup Execute DAT")• [Perform ](<./Perform_DAT.md> "Perform DAT")• [POP to ](<./POP_to_DAT.md> "POP to DAT")• [Render Pick ](<./Render_Pick_DAT.md> "Render Pick DAT")• [Reorder ](<./Reorder_DAT.md> "Reorder DAT")• [Script ](<./Script_DAT.md> "Script DAT")• [Select ](<./Select_DAT.md> "Select DAT")• [Serial ](<./Serial_DAT.md> "Serial DAT")• [Serial Devices ](<./Serial_Devices_DAT.md> "Serial Devices DAT")• [SocketIO ](<./SocketIO_DAT.md> "SocketIO DAT")• [SOP to ](<./SOP_to_DAT.md> "SOP to DAT")• [Sort ](<./Sort_DAT.md> "Sort DAT")• [Substitute ](<./Substitute_DAT.md> "Substitute DAT")• [Switch ](<./Switch_DAT.md> "Switch DAT")• [Table ](<./Table_DAT.md> "Table DAT")• [TCP/IP ](<./TCP/IP_DAT.md> "TCP/IP DAT")• [Text ](<./Text_DAT.md> "Text DAT")• [Touch In ](<./Touch_In_DAT.md> "Touch In DAT")• [Touch Out ](<./Touch_Out_DAT.md> "Touch Out DAT")• [Transpose ](<./Transpose_DAT.md> "Transpose DAT")• [TUIO In ](<./TUIO_In_DAT.md> "TUIO In DAT")• [UDP In ](<./UDP_In_DAT.md> "UDP In DAT")• [UDP Out ](<./UDP_Out_DAT.md> "UDP Out DAT")• [UDT In ](<./UDT_In_DAT.md> "UDT In DAT")• [UDT Out ](<./UDT_Out_DAT.md> "UDT Out DAT")• [Video Devices ](<./Video_Devices_DAT.md> "Video Devices DAT")• [Web Client ](<./Web_Client_DAT.md> "Web Client DAT")• [Web ](<./Web_DAT.md> "Web DAT")• [Web Server ](<./Web_Server_DAT.md> "Web Server DAT")• [WebRTC ](<./WebRTC_DAT.md> "WebRTC DAT")• [WebSocket ](<./WebSocket_DAT.md> "WebSocket DAT")• XML
