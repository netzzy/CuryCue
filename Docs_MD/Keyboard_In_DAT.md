# Keyboard In DAT

##   
  
Summary

The Keyboard In DAT lists the most recent key events in its FIFO (first in/first out) table. There is one row for every key press down and every key-up, including Shift, Ctrl and Alt, with distinction between left and right side. For convenience, with each key press, a column indicates if the Shift, Ctrl and Alt were being held down at the time. 

You get key presses even of the cursor is outside the TouchDesigner windows, whether they are control panels, Perform Mode or the network editor window. Exceptions: while entering text in the editor window. 

You can set a filter to watch only certain keys. Custom shortcuts can be defined and handled by a [python callback in the attached script](<./KeyboardinDAT_Class.md> "KeyboardinDAT Class"). 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[keyboardinDAT_Class](<./KeyboardinDAT_Class.md> "KeyboardinDAT Class")

## 

Parameters - Keyboard In Page

Active`active`\- Inhibits and allows message to be added to log. 

Perform Window Only`perform`\- When on, key events are only detected while in perform mode. 

Keys`keys`\- List of keys to allow through the filter. Just put the characters in the list, space-separated. Eg. '1 2 g h' for the 1, 2, g and h keys. Only these keys will be added to the log and generate an event. If blank, no filtering will be done. List of accepted keys: [Keyboard UI](</Keyboard_UI> "Keyboard UI")

Shortcuts`shortcuts`\- List of shortcuts to watch for. See "Shortcuts" in the notes for defining shortcuts. 

Panels`panels`\- Optional list of references to panels to detect events from. Events will only be fired when any of the listed panels has focus. 

Left/Right Modifiers`lrmodifiers`\- When on, the states of the left and right modifier keys (see Notes) will be added to the table. Switching the state of this parameter will reset the table's contents. 

## 

Parameters - Log Page

Callbacks DAT`callbacks`\- Path to a DAT containing callbacks for each keyboard event received. See keyboardinDAT_Class for usage. 

Execute from`executeloc`\- ⊞ \- Determines the location the script is run from. 
* Current Node`current`\- The script is executed from the current node location (for example, where 'cc' points to).
* Callbacks DAT`callbacks`-
* Specified Operator`op`\- The script is executed from the operator specified in the From Operator parameter below.


From Operator`fromop`\- The operator whose state change will trigger the DAT to execute its script when Execute is set to Specified Operator. This operator is also the path that the script will be executed from if the Execute From parameter is set to Specified Operator. 

Clamp Output`clamp`\- The DAT is limited to 100 messages by default but with Clamp Output, this can be set to anything including unlimited. 

Maximum Lines`maxlines`\- Limits the number of messages, older messages are removed from the list first. 

Clear Output`clear`\- Deletes all lines except the heading. To clear with a python script`op(_"opname"_).par.clear.pulse()`## 

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

Notes

**Shortcuts** are defined by a list of modifier keys (see below) and a "trigger" key separated by .'s. 

For example,`ctrl.shift.a`the modifier keys are ctrl and shift, and the trigger key is a. This shortcut will be activated when one of the ctrl and shift keys are pressed and the trigger key, a is pressed down. If any other modifier keys are pressed, the shortcut will not be detected. 

Modifier Keys - The following are all the valid modifier keys: 

  *`lalt`\- Left alt key.
  *`ralt`\- Right alt key.
  *`alt`\- Either left or right alt key.
  *`lctrl`\- Left ctrl key.
  *`rctrl`\- Right ctrl key.
  *`ctrl`\- Either left or right ctrl key.
  *`lshift`\- Left shift key.
  *`rshift`\- Right shift key.
  *`shift`\- Either left or right shift key.

## 

Operator Inputs
* Input 0:  -

## 

Info CHOP Channels

Extra Information for the Keyboard In DAT can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). __

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
[Art-Net ](<./Art-Net_DAT.md> "Art-Net DAT")• [Audio Devices ](<./Audio_Devices_DAT.md> "Audio Devices DAT")• [CHOP Execute ](<./CHOP_Execute_DAT.md> "CHOP Execute DAT")• [CHOP to ](<./CHOP_to_DAT.md> "CHOP to DAT")• [Clip ](<./Clip_DAT.md> "Clip DAT")• [Convert ](<./Convert_DAT.md> "Convert DAT")• [CPlusPlus ](<./CPlusPlus_DAT.md> "CPlusPlus DAT")• [DAT ](<./DAT.md> "DAT")• [ Execute ](<./DAT_Execute_DAT.md> "DAT Execute DAT")• [DAT Export ](<./DAT_Export.md> "DAT Export")• [Error ](<./Error_DAT.md> "Error DAT")• [EtherDream ](<./EtherDream_DAT.md> "EtherDream DAT")• [Evaluate ](<./Evaluate_DAT.md> "Evaluate DAT")• [Examine ](<./Examine_DAT.md> "Examine DAT")• [Execute ](<./Execute_DAT.md> "Execute DAT")• [FIFO ](<./FIFO_DAT.md> "FIFO DAT")• [File In ](<./File_In_DAT.md> "File In DAT")• [File Out ](<./File_Out_DAT.md> "File Out DAT")• [Folder ](<./Folder_DAT.md> "Folder DAT")• [In ](<./In_DAT.md> "In DAT")• [Indices ](<./Indices_DAT.md> "Indices DAT")• [Info ](<./Info_DAT.md> "Info DAT")• [Insert ](<./Insert_DAT.md> "Insert DAT")• [JSON ](<./JSON_DAT.md> "JSON DAT")• Keyboard In • [Lookup ](<./Lookup_DAT.md> "Lookup DAT")• [Media File Info ](<./Media_File_Info_DAT.md> "Media File Info DAT")• [Merge ](<./Merge_DAT.md> "Merge DAT")• [MIDI Event ](<./MIDI_Event_DAT.md> "MIDI Event DAT")• [MIDI In ](<./MIDI_In_DAT.md> "MIDI In DAT")• [Monitors ](<./Monitors_DAT.md> "Monitors DAT")• [MPCDI ](<./MPCDI_DAT.md> "MPCDI DAT")• [MQTT Client ](<./MQTT_Client_DAT.md> "MQTT Client DAT")• [Multi Touch In ](<./Multi_Touch_In_DAT.md> "Multi Touch In DAT")• [NDI ](<./NDI_DAT.md> "NDI DAT")• [Null ](<./Null_DAT.md> "Null DAT")• [OP Execute ](<./OP_Execute_DAT.md> "OP Execute DAT")• [OP Find ](<./OP_Find_DAT.md> "OP Find DAT")• [OSC In ](<./OSC_In_DAT.md> "OSC In DAT")• [OSC Out ](<./OSC_Out_DAT.md> "OSC Out DAT")• [Out ](<./Out_DAT.md> "Out DAT")• [Panel Execute ](<./Panel_Execute_DAT.md> "Panel Execute DAT")• [Parameter ](<./Parameter_DAT.md> "Parameter DAT")• [Parameter Execute ](<./Parameter_Execute_DAT.md> "Parameter Execute DAT")• [ParGroup Execute ](<./ParGroup_Execute_DAT.md> "ParGroup Execute DAT")• [Perform ](<./Perform_DAT.md> "Perform DAT")• [POP to ](<./POP_to_DAT.md> "POP to DAT")• [Render Pick ](<./Render_Pick_DAT.md> "Render Pick DAT")• [Reorder ](<./Reorder_DAT.md> "Reorder DAT")• [Script ](<./Script_DAT.md> "Script DAT")• [Select ](<./Select_DAT.md> "Select DAT")• [Serial ](<./Serial_DAT.md> "Serial DAT")• [Serial Devices ](<./Serial_Devices_DAT.md> "Serial Devices DAT")• [SocketIO ](<./SocketIO_DAT.md> "SocketIO DAT")• [SOP to ](<./SOP_to_DAT.md> "SOP to DAT")• [Sort ](<./Sort_DAT.md> "Sort DAT")• [Substitute ](<./Substitute_DAT.md> "Substitute DAT")• [Switch ](<./Switch_DAT.md> "Switch DAT")• [Table ](<./Table_DAT.md> "Table DAT")• [TCP/IP ](<./TCP/IP_DAT.md> "TCP/IP DAT")• [Text ](<./Text_DAT.md> "Text DAT")• [Touch In ](<./Touch_In_DAT.md> "Touch In DAT")• [Touch Out ](<./Touch_Out_DAT.md> "Touch Out DAT")• [Transpose ](<./Transpose_DAT.md> "Transpose DAT")• [TUIO In ](<./TUIO_In_DAT.md> "TUIO In DAT")• [UDP In ](<./UDP_In_DAT.md> "UDP In DAT")• [UDP Out ](<./UDP_Out_DAT.md> "UDP Out DAT")• [UDT In ](<./UDT_In_DAT.md> "UDT In DAT")• [UDT Out ](<./UDT_Out_DAT.md> "UDT Out DAT")• [Video Devices ](<./Video_Devices_DAT.md> "Video Devices DAT")• [Web Client ](<./Web_Client_DAT.md> "Web Client DAT")• [Web ](<./Web_DAT.md> "Web DAT")• [Web Server ](<./Web_Server_DAT.md> "Web Server DAT")• [WebRTC ](<./WebRTC_DAT.md> "WebRTC DAT")• [WebSocket ](<./WebSocket_DAT.md> "WebSocket DAT")• [XML ](<./XML_DAT.md> "XML DAT")
