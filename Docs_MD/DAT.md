# DAT

##   
  
Summary

See also [Category:DATs](</index.php?title=Category:DATs&action=edit&redlink=1> "Category:DATs \(page does not exist\)") for a full list of articles related to DATs. 

**DATa Operators** (or **DATs**) are used to hold text data like strings, scripts, and XML. DATs either contain multiple lines of text as in a script, or a table of rows and columns of cells, each containing one string. You can edit the contents of the DAT directly in the [DAT Viewer](<./DAT_Viewer.md> "DAT Viewer"). 

Access a DAT containing normal text using`op('text1').text`. Access a cell in a DAT containing a table using`op('table1')[1,2]`or by row/col names`op('table1')['rowname', 'colname']`. 

**IMPORTANT** :`op('table1')[1,2]`is a python [cell object](<./Cell_Class.md> "Cell Class") which usually gets converted for you to the string in the cell. More safely use`op('table1')[1,2].val`which always gives you the string. 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[DAT Class](<./DAT_Class.md> "DAT Class")

## Sweet Sixteen DATs

The following 16 DATs are commonly used, we recommend familiarizing yourself with them. 

DAT | Purpose | Related DAT  
---|---|---  
[Text](<./Text_DAT.md> "Text DAT") | A place to edit and hold any text data. |   
[Table](<./Table_DAT.md> "Table DAT") | Edit tables of text in rows and columns of "cells". | [Convert](<./Convert_DAT.md> "Convert DAT")  
[Merge](<./Merge_DAT.md> "Merge DAT") | Merges tables or text DATs into one. | [Switch](<./Switch_DAT.md> "Switch DAT")  
[Select](<./Select_DAT.md> "Select DAT") | Select specific columns or rows from a DAT. | [Substitute](<./Substitute_DAT.md> "Substitute DAT")  
[Reorder](<./Reorder_DAT.md> "Reorder DAT") | Re-orders and repeats rows or columns in a DAT. | [Transpose](<./Transpose_DAT.md> "Transpose DAT")  
[Insert](<./Insert_DAT.md> "Insert DAT") | Adds one row or column to a table filling with text in the new cells. |   
[Evaluate](<./Evaluate_DAT.md> "Evaluate DAT") | Evaluates expressions in DATs. | [Script](<./Script_DAT.md> "Script DAT")  
[CHOP to](<./CHOP_to_DAT.md> "CHOP to DAT") | Converts CHOP channels to DATs. | [SOP to](<./SOP_to_DAT.md> "SOP to DAT")  
[CHOP Execute](<./CHOP_Execute_DAT.md> "CHOP Execute DAT") | Runs the DAT as a script when a CHOP changes. |   
[Panel Execute](<./Panel_Execute_DAT.md> "Panel Execute DAT") | Runs the DAT as a script when a [Panel](<./Panel.md> "Panel") changes. |   
[DAT Execute](<./DAT_Execute_DAT.md> "DAT Execute DAT") | Runs the DAT as a script when another DAT changes. | [Execute](<./Execute_DAT.md> "Execute DAT")  
[OSC In](<./OSC_In_DAT.md> "OSC In DAT")/[UDP In](<./UDP_In_DAT.md> "UDP In DAT") | Receive data from other applications via Open Sound Control. | [OSC Out](<./OSC_Out_DAT.md> "OSC Out DAT")/[UDP Out](<./UDP_Out_DAT.md> "UDP Out DAT")  
[Web](<./Web_DAT.md> "Web DAT") | Fetch a page on the internet based on a URL. | [XML](<./XML_DAT.md> "XML DAT")  
[Render Pick](<./Render_Pick_DAT.md> "Render Pick DAT") | Use mouse to pick 3D objects and surfaces. | [Info](<./Info_DAT.md> "Info DAT")  
[Multi Touch In](<./Multi_Touch_In_DAT.md> "Multi Touch In DAT") | Receive input from Windows 7+ multi-touch devices. |   
[MIDI In](<./MIDI_In_DAT.md> "MIDI In DAT") | Get MIDI controller and button data. | [Serial](<./Serial_DAT.md> "Serial DAT")  
  
All DATs are documented in the [Category:DATs](</index.php?title=Category:DATs&action=edit&redlink=1> "Category:DATs \(page does not exist\)"). 

## DATs for Scripting

DATs can be linked together to select, re-arrange and evaluate data and expressions, making DATs a powerful **procedural scripting tool**. 

DATs that contain scripts can be triggered by events like mouse clicks and any operation of gadgets in TouchDesigner control panels. DAT scripts can also be triggered by channel changes in CHOPs. 

    **Script Example**: This will create a button that plays a sound when you click it: Create a Button component (Tab -> COMP -> Button). Go inside it (Enter) and create an Audio Play CHOP (Tab -> CHOP -> Audio Play).

    Then create a Panel Execute DAT (Tab -> DAT -> Panel Execute) and make its [Viewer Active](<./Viewer_Active.md> "Viewer Active"). Then click in its viewer and and change the`offToOn()`function to be:
[code]
    def offToOn(panelValue):
         op('audioplay1').par.trigger.pulse()
         return
    
[/code]

Click outside the node to end text entry. Go back up (u), make the button a Momentary button via its Button page and Button Type parameter. Then make the button [Viewer Active](<./Viewer_Active.md> "Viewer Active"). Click on the viewer of the button. It should make a Notify sound. 

You can also run a script in a Text DAT by using the "`run`" command from the textport or another DAT. 

## DATs for Tables

DAT tables are rows and columns of cells containing text strings. 

The DAT whose name is [Table DAT](<./Table_DAT.md> "Table DAT") is used to define new tables. To manually add, delete rows and columns of tables, press RMB over the table when [Viewer Active](<./Viewer_Active.md> "Viewer Active") is on and select from the menu. 

The tables are then manipulated by the [Select DAT](<./Select_DAT.md> "Select DAT"), [Evaluate DAT](<./Evaluate_DAT.md> "Evaluate DAT"), [Merge DAT](<./Merge_DAT.md> "Merge DAT"), [Switch DAT](<./Switch_DAT.md> "Switch DAT"), [Sort DAT](<./Sort_DAT.md> "Sort DAT") and others. 

You can use table DATs to export to parameters. See [DAT Export](<./DAT_Export.md> "DAT Export"). 

DAT tables can be modified with the`tabcell`command. 

Table cells are read with a`tab()`,`tabr()`,`tabc()`or`tabrc()`expression. See Help -> Commands and Expressions. 

    **Table Example** : This will create two TOP images with names in it: Create a Table DAT (Tab -> DAT -> Table). Make its [Viewer Active](<./Viewer_Active.md> "Viewer Active"). Right-click on the viewer and select Add Column, and then Add Row, and again Add Row, which should give you 3 rows and 2 columns of empty cells (or put 2 and 3 in the parameters.)

    Click in the top left cell and type`name`, top right type`age`, and fill in the remaining cells with`joe`,`9`,`jane`,`21`.

    Now create a Text TOP (Tab -> TOP -> Text) and in its parameter called Text, type this expression to retrieve a cell from the table:``tabc("table1", $OD, "name")``. You should see "joe" in the Text TOP viewer. Copy/paste the Text TOP (Ctrl-C, Ctrl-V). The new TOP should be called`text2`and its viewer should say "jane".

    That`tabc()`expression gets from the table,`table1`, the node you edited. It gets from the column called`name`. And the row is`$OD`, which is a variable you can use in any node that means "operator digits", the digits at the end of the operator name, which in this case is`1`and`2`for`text1`and`text2`.

    In the TOPs' expressions, you can replace`"name"`with`"age"`.

## DATs for manipulating Web and XML Data

The [Web Client DAT](<./Web_Client_DAT.md> "Web Client DAT") gets HTML or other data by passing a URL to the internet and receiving a response. The result and any XML data can be filtered with an [XML DAT](<./XML_DAT.md> "XML DAT"), then further processed with the other DATs. 

## DATs for Raw Text

DATs can also be use to hold raw text which can then used by the [Text TOP](<./Text_TOP.md> "Text TOP") and [Text SOP](<./Text_SOP.md> "Text SOP") for use in compositing and 3D. They can also be used to leave comments your networks or for pop-up help messages for panel gadgets. 

## Editing DATs

DATs can be edited directly in their viewers by turning on the [Viewer Active Flag](<./Viewer_Active_Flag.md> "Viewer Active Flag"). 

You can also edit DATs in the [Textport](<./Textport.md> "Textport") by right-clicking on a DAT and selecting **Edit Contents in Textport**. 

Some DAT generators and most DAT filters can not be edited because their data is fed to them from their input. This is indicated in the viewer by a more muted text color compared to those DATs which can be edited. If you need to temporarily edit the contents of one of these DATs you can lock the DAT using the [Lock Flag](<./Lock_Flag.md> "Lock Flag") and then edit it. However, these changes will be lost when the DAT is unlocked and locking it keeps it from [cooking](<./Cook.md> "Cook"), so this is generally only useful for troubleshooting and debugging. 

By default, text-type DATs display line numbers in the left margin area and table-type DATs display row and column numbers. The display of these numbers can be controlled in [Preferences](</index.php?title=Preferences_Dialog&action=edit&redlink=1> "Preferences Dialog \(page does not exist\)"). 

## Editing DAT Text in an External Editor

In any DAT (or any parameter), if you right-click the DAT node and select **Edit Contents...** you will be editing the text in an external editor. Notepad is Windows default text editor. 

To change the text editor to something else, like Notepad++, Vim, Sublime, etc. you need to change the Text Editor and Table Editor preference values. These preferences can be found in the Preferences dialog under the DATs page. Set their values to the path of the installed application executable (.exe) of the editor you want to use. For example,`C:/Program Files ..`. 

Everyone has a favorite, have a look at Sublime Text 2. 

To see how you set an environment variable, see [Variables](<./Variables.md> "Variables"). 

## Using DATs
* text data, text and table formats (tab delimited)
  * use for scripts, commands, storage of values and arrays
  * can be edited in the viewer, textport, or any external text editor
  * Import: Text DAT, Table DAT, Web DAT
  * Export: (right-click to save)

DATs   
---  
[Art-Net ](<./Art-Net_DAT.md> "Art-Net DAT")• [Audio Devices ](<./Audio_Devices_DAT.md> "Audio Devices DAT")• [CHOP Execute ](<./CHOP_Execute_DAT.md> "CHOP Execute DAT")• [CHOP to ](<./CHOP_to_DAT.md> "CHOP to DAT")• [Clip ](<./Clip_DAT.md> "Clip DAT")• [Convert ](<./Convert_DAT.md> "Convert DAT")• [CPlusPlus ](<./CPlusPlus_DAT.md> "CPlusPlus DAT")• DAT • [ Execute ](<./DAT_Execute_DAT.md> "DAT Execute DAT")• [DAT Export ](<./DAT_Export.md> "DAT Export")• [Error ](<./Error_DAT.md> "Error DAT")• [EtherDream ](<./EtherDream_DAT.md> "EtherDream DAT")• [Evaluate ](<./Evaluate_DAT.md> "Evaluate DAT")• [Examine ](<./Examine_DAT.md> "Examine DAT")• [Execute ](<./Execute_DAT.md> "Execute DAT")• [FIFO ](<./FIFO_DAT.md> "FIFO DAT")• [File In ](<./File_In_DAT.md> "File In DAT")• [File Out ](<./File_Out_DAT.md> "File Out DAT")• [Folder ](<./Folder_DAT.md> "Folder DAT")• [In ](<./In_DAT.md> "In DAT")• [Indices ](<./Indices_DAT.md> "Indices DAT")• [Info ](<./Info_DAT.md> "Info DAT")• [Insert ](<./Insert_DAT.md> "Insert DAT")• [JSON ](<./JSON_DAT.md> "JSON DAT")• [Keyboard In ](<./Keyboard_In_DAT.md> "Keyboard In DAT")• [Lookup ](<./Lookup_DAT.md> "Lookup DAT")• [Media File Info ](<./Media_File_Info_DAT.md> "Media File Info DAT")• [Merge ](<./Merge_DAT.md> "Merge DAT")• [MIDI Event ](<./MIDI_Event_DAT.md> "MIDI Event DAT")• [MIDI In ](<./MIDI_In_DAT.md> "MIDI In DAT")• [Monitors ](<./Monitors_DAT.md> "Monitors DAT")• [MPCDI ](<./MPCDI_DAT.md> "MPCDI DAT")• [MQTT Client ](<./MQTT_Client_DAT.md> "MQTT Client DAT")• [Multi Touch In ](<./Multi_Touch_In_DAT.md> "Multi Touch In DAT")• [NDI ](<./NDI_DAT.md> "NDI DAT")• [Null ](<./Null_DAT.md> "Null DAT")• [OP Execute ](<./OP_Execute_DAT.md> "OP Execute DAT")• [OP Find ](<./OP_Find_DAT.md> "OP Find DAT")• [OSC In ](<./OSC_In_DAT.md> "OSC In DAT")• [OSC Out ](<./OSC_Out_DAT.md> "OSC Out DAT")• [Out ](<./Out_DAT.md> "Out DAT")• [Panel Execute ](<./Panel_Execute_DAT.md> "Panel Execute DAT")• [Parameter ](<./Parameter_DAT.md> "Parameter DAT")• [Parameter Execute ](<./Parameter_Execute_DAT.md> "Parameter Execute DAT")• [ParGroup Execute ](<./ParGroup_Execute_DAT.md> "ParGroup Execute DAT")• [Perform ](<./Perform_DAT.md> "Perform DAT")• [POP to ](<./POP_to_DAT.md> "POP to DAT")• [Render Pick ](<./Render_Pick_DAT.md> "Render Pick DAT")• [Reorder ](<./Reorder_DAT.md> "Reorder DAT")• [Script ](<./Script_DAT.md> "Script DAT")• [Select ](<./Select_DAT.md> "Select DAT")• [Serial ](<./Serial_DAT.md> "Serial DAT")• [Serial Devices ](<./Serial_Devices_DAT.md> "Serial Devices DAT")• [SocketIO ](<./SocketIO_DAT.md> "SocketIO DAT")• [SOP to ](<./SOP_to_DAT.md> "SOP to DAT")• [Sort ](<./Sort_DAT.md> "Sort DAT")• [Substitute ](<./Substitute_DAT.md> "Substitute DAT")• [Switch ](<./Switch_DAT.md> "Switch DAT")• [Table ](<./Table_DAT.md> "Table DAT")• [TCP/IP ](<./TCP/IP_DAT.md> "TCP/IP DAT")• [Text ](<./Text_DAT.md> "Text DAT")• [Touch In ](<./Touch_In_DAT.md> "Touch In DAT")• [Touch Out ](<./Touch_Out_DAT.md> "Touch Out DAT")• [Transpose ](<./Transpose_DAT.md> "Transpose DAT")• [TUIO In ](<./TUIO_In_DAT.md> "TUIO In DAT")• [UDP In ](<./UDP_In_DAT.md> "UDP In DAT")• [UDP Out ](<./UDP_Out_DAT.md> "UDP Out DAT")• [UDT In ](<./UDT_In_DAT.md> "UDT In DAT")• [UDT Out ](<./UDT_Out_DAT.md> "UDT Out DAT")• [Video Devices ](<./Video_Devices_DAT.md> "Video Devices DAT")• [Web Client ](<./Web_Client_DAT.md> "Web Client DAT")• [Web ](<./Web_DAT.md> "Web DAT")• [Web Server ](<./Web_Server_DAT.md> "Web Server DAT")• [WebRTC ](<./WebRTC_DAT.md> "WebRTC DAT")• [WebSocket ](<./WebSocket_DAT.md> "WebSocket DAT")• [XML ](<./XML_DAT.md> "XML DAT")
