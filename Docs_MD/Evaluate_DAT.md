# Evaluate DAT

## 

Summary

The Evaluate DAT changes the cells of the incoming DAT using string-editing and math expressions. 

In its simplest form, without an input DAT attached, you can put any python expression in the Expression parameter of an Evaluate DAT. To evaluate the expression every frame you may need to put the parameter into Expression [Parameter Mode](<./Parameter_Mode.md> "Parameter Mode"). 

With a DAT attached, it outputs a table with the same number of rows and columns as the input. 

The Scope page can be used to restrict which rows and columns of cells are affected. 
* When the Output menu is set to Expressions, it causes the input cells to be evaluated as Pythong expressions.`me.inputCell.val`is the value of the input cell.
* The optional second input DAT is an array of expressions which are matched to the cells of the input, then evaluated and output. If there are fewer rows in the second DAT than the first, the expressions in the last row of the second input are repeated. If there are fewer columns in the second DAT than the first, the last column is repeated.
* **Expressions are optimized by storing a compiled internal version, which runs much faster.** Use this where possible. If you are reusing expressions by repeating them in a table, having an input table with the few expressions you will cycle through separate from the data will also improve performance.


If the second DAT is one cell, like the Expression parameter, it applies its expression to all the input cells. A one-cell second DAT with`me.inputCell.val+1`adds 1 to all the first input's cells. 

If the second DAT is`me.inputCell.val`|`me.inputCell.val`---|---`me.inputCell.val`|`math.sin(math.radians(float(me.inputCell.val)))`then the first row and first column are left intact and the rest of the cells get their`sin()`computed. 

The Evaluate DAT maintains the format of the first input DAT (table or text) unless the Output Table Size parameter is used. 

See also the [Substitute DAT](<./Substitute_DAT.md> "Substitute DAT"), [Expression CHOP](<./Expression_CHOP.md> "Expression CHOP"). 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[evaluateDAT_Class](<./EvaluateDAT_Class.md> "EvaluateDAT Class")

## 

Expressions

The Evaluate DAT can be used to (1) build strings or (2) do math operations.`me.inputCell`refers to the corresponding input cell that is used to evaluate the current cell. [evaluateDAT_Class](<./EvaluateDAT_Class.md> "EvaluateDAT Class") has a list of members that refer to incoming data. You can use [Python](<./Python.md> "Python") to fetch data, like`op('datpath')[row,col]`to access DAT data and`op('choppath')['channame'][sampleindex]`to access CHOP data. A few examples: 
[code] 
    # access data from a particular row from the input table at the currently evaluated column
    me.inputTable['rowname',me.inputCol]
    
    # prefix the data in the current cell the input row and column
    # a string in the first cell will be formatted as [0,0]:string
    '['+str(me.inputRow)+','+str(me.inputCol)+']:'+me.inputCell
    
    # add the numeric data in the current cell to numeric data from another table
    op('datpath")[me.inputRow,'colname'] + me.inputCell
    
    # concatenate the numeric data in the current cell to string data from another table with a space between
    op('datpath')[me.inputRow,'colname'] + ' ' + me.inputCell
    
    # concatenate the current row number to string data from another table with a space between
    op('datpath')[me.inputRow,'colname'] + ' ' + str(me.inputRow)
    
    # concatenate a sample at the currrent row index from a chop channel with the current cell
    me.inputCell + ':' + str(op('choppath')['channame'][me.inputRow])
    
[/code]

See [Working with DATs in Python](<./Working_with_DATs_in_Python.md> "Working with DATs in Python") and [Working with CHOPs in Python](<./Working_with_CHOPs_in_Python.md> "Working with CHOPs in Python") for more examples of accessing data in other operators. 

You can also use any [Tscript Expressions](<./Tscript_Expressions.md> "Tscript Expressions") to fetch data, like``tab("_tabpath_ ",_row_ ,_col_)``and``chop("_choppath_ ")``. A list of local variables, such as`$V`for the value of the corresponding input cell, is available, and you can use other Tscript [Variables](<./Variables.md> "Variables") like`$F`and`$SYS_XRES`. 

A few Tscript expressions`v()`and`vs()`are special to the Evaluate DAT and can access all cells in the input.`vs()`differs from`v()`as it always output strings, not floats. 

The expressions`v(row,col)`and`vs(row,col)`can use the local variables`R`(the cell's row) and`C`(the cell's column). 

  *`v($R,$C)`is the same as`$V`.
  *`v($C,$R)`transposes the cells.
  * You could address relative rows/columns with`$C`,`$C-1`,`$C+1`, and address the cell at the first column with`v($R,0)`.`v`will return the cell contents as floats.`vs`will return cell contents as strings.


The expressions that let you get at cells by row/column names are: 

  *`vr(_rowname_ ,_colnum_)`*`vc(_rownum_ ,_colname_)`*`vrc(_rowname_ ,_colname_)`and the string versions of the above: 

  *`vsr(_rowname_ ,_colnum_)`*`vsc(_rownum_ ,_colname_)`*`vsrc(_rowname_ ,_colname_)`Example:`vrc("john","august")`The local variables`NR`and`NC`give the number of rows and columns of the input table. 

## 

Parameters - Evaluate Page

Input Data DAT`dat`\- An alternative DAT table to be used in place of an input table. 

Expressions DAT`datexpr`\- An alternative DAT table to be used in place of a formula table. 

Output`output`\- ⊞ \- Determines what format will be used for output from the DAT. 
* Evaluate`evaluate`\- Evaluates input data as python expressions. **Compiled**.
* Input Data`data`\- Passes through data from first input without manipulation.
* Input Expression`expression`\- Passes through first input if there is no second input. Otherwise passes through second input. If the first input has more rows or columns than the second one, then the last row or column of the second is repeated to fill out the extra cells.


Expression`expr`\- Expression used to evaluate each cell if an Expression input or DAT is not supplied. 

Output Table Size`outputsize`\- ⊞ \- If the Output Table Size parameter is Strings, Expressions, or Commands, and there is a second input, you can choose the output table size to be either Input DAT or the Formula DAT. If the Formula DAT is chosen and its table size is greater than the input data table, then the last cell in each row or column will be used when evaluating the remaining formulas. 
* Input 1 (Data)`in1`-
* Input 2 (Expressions)`in2`-


Monitor Data Dependencies`dependency`\- If the Output parameter is set to Strings or Expressions, the DAT will monitor any nodes used by the data, as well as check for time dependencies, and cook accordingly. This toggle is on by default. If you only want the DAT to cook based on input changes, you can turn this off to avoid unnecessary updates. 

Convert Backslash Characters`backslash`\- Will convert things like \n to newlines, \t to tabs etc. Note that \n, \t will be converted to spaces if the input DAT is a table. 

## 

Parameters - Scope Page

Exclude First Row`xfirstrow`\- Forces the first row to be selected even if it is not specified by the Select Rows settings. 

Exclude First Col`xfirstcol`\- Forces the first column to be selected even if it is not specified by the Select Cols settings. 

Select Rows`extractrows`\- ⊞ \- This parameter allows you to pick different ways of specifying the rows selected. 
* All`all`\- All rows selected.
* by Name`byname`\- Rows selected using Start Row Name and End Row Name parameters.
* by Index`byindex`\- Rows selected using Start Row Index and End Row Index parameters.
* by Start Name, End Index`bynameindex`\- Rows selected using Start Row Name and End Row Index parameters.
* by Start Index, End Name`byindexname`\- Rows selected using Start Row Index and End Row Name parameters.
* by Values`bynames`\- Rows selected by specifying the row values explicitly.
* by Condition`byexpr`\- Rows selected by an expression to be evaluated for the from column.


Start Row Name`rownamestart`\- Specify the row name to start the selection range from. 

Start Row Index`rowindexstart`\- Specify the row index to start the selection range from. 

End Row Name`rownameend`\- Specify the row name to end the selection range. 

End Row Index`rowindexend`\- Specify the row index to end the selection range. 

Row Select Values`rownames`\- Specify actual row names that you want to select. You can use pattern matching, for example`row[1-4]`will select all the rows names row1 thru row4. 

Row Select Condition`rowexpr`\- Specify an expression that will be evaluated. If the expression evaluates to true, the row will be selected. 

Expand the parameter and you will see that it is in [expression mode](<./Parameter_Mode.md> "Parameter Mode"). 

By default, the [Python](<./Python.md> "Python") expression is`re.match('.*',me.inputCell.val) != None`.`'.*'`means match any character multiple times, so this expression matches all values. If you want to match the parent's operator name followed by any numeric number you can use`parent().name+'[0-9]*'`, where`'[0-9]*'`matches any numerical string.`'.*'+parent().name+'.*'`will match any cell that contains the operator's parent name. You can check [Regular Expression Operations](<https://docs.python.org/3.3/library/re.html>) for additional information on how to use the Python Regular Expression module. 

In Tscript, you can access the cell value with the local variable`$V`, and the row and column with`$R`and`$C`__

From Column`fromcol`\- When selecting rows by values, this parameter selects which column to use when matching cell values to Selected Row Values to determine which rows are selected. 

Select Cols`extractcols`\- ⊞ \- This parameter allows you to pick different ways of specifying the columns selected. 
* All`all`\- All columns selected.
* by Name`byname`\- Columns selected using Start Col Name and End Col Name parameters.
* by Index`byindex`\- Columns selected using Start Col Index and End Col Index parameters.
* by Start Name, End Index`bynameindex`\- Columns selected using Start Col Name and End Col Index parameters.
* by Start Index, End Name`byindexname`\- Columns selected using Start Col Index and End Col Name parameters.
* by Values`bynames`\- Columns selected by specifying the column values explicitly.
* by Condition`byexpr`\- Rows selected by an expression to be evaluated for the from row.


Start Col Name`colnamestart`\- Specify the column name to start the selection range from. 

Start Col Index`colindexstart`\- Specify the column index to start the selection range from. 

End Col Name`colnameend`\- Specify the column name to end the selection range. 

End Col Index`colindexend`\- Specify the column index to end the selection range. 

Col Select Values`colnames`\- Specify actual column names that you want to select. You can use pattern matching, for example`colvalue[1-4]`will select all the columns named colvalue1 thru colvalue4. 

Col Select Condition`colexpr`\- Specify an expression that will be evaluated. If the expression evaluates to true, the column will be selected. See Row Select Condition for more details. 

From Row`fromrow`\- When extracting columns by Specified Names, this parameter selects which row to use when matching cell values to Selected Col Values to determine which columns are selected. 

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
  * Input 1:  -

## 

Info CHOP Channels

Extra Information for the Evaluate DAT can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). __

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
[Art-Net ](<./Art-Net_DAT.md> "Art-Net DAT")• [Audio Devices ](<./Audio_Devices_DAT.md> "Audio Devices DAT")• [CHOP Execute ](<./CHOP_Execute_DAT.md> "CHOP Execute DAT")• [CHOP to ](<./CHOP_to_DAT.md> "CHOP to DAT")• [Clip ](<./Clip_DAT.md> "Clip DAT")• [Convert ](<./Convert_DAT.md> "Convert DAT")• [CPlusPlus ](<./CPlusPlus_DAT.md> "CPlusPlus DAT")• [DAT ](<./DAT.md> "DAT")• [ Execute ](<./DAT_Execute_DAT.md> "DAT Execute DAT")• [DAT Export ](<./DAT_Export.md> "DAT Export")• [Error ](<./Error_DAT.md> "Error DAT")• [EtherDream ](<./EtherDream_DAT.md> "EtherDream DAT")• Evaluate • [Examine ](<./Examine_DAT.md> "Examine DAT")• [Execute ](<./Execute_DAT.md> "Execute DAT")• [FIFO ](<./FIFO_DAT.md> "FIFO DAT")• [File In ](<./File_In_DAT.md> "File In DAT")• [File Out ](<./File_Out_DAT.md> "File Out DAT")• [Folder ](<./Folder_DAT.md> "Folder DAT")• [In ](<./In_DAT.md> "In DAT")• [Indices ](<./Indices_DAT.md> "Indices DAT")• [Info ](<./Info_DAT.md> "Info DAT")• [Insert ](<./Insert_DAT.md> "Insert DAT")• [JSON ](<./JSON_DAT.md> "JSON DAT")• [Keyboard In ](<./Keyboard_In_DAT.md> "Keyboard In DAT")• [Lookup ](<./Lookup_DAT.md> "Lookup DAT")• [Media File Info ](<./Media_File_Info_DAT.md> "Media File Info DAT")• [Merge ](<./Merge_DAT.md> "Merge DAT")• [MIDI Event ](<./MIDI_Event_DAT.md> "MIDI Event DAT")• [MIDI In ](<./MIDI_In_DAT.md> "MIDI In DAT")• [Monitors ](<./Monitors_DAT.md> "Monitors DAT")• [MPCDI ](<./MPCDI_DAT.md> "MPCDI DAT")• [MQTT Client ](<./MQTT_Client_DAT.md> "MQTT Client DAT")• [Multi Touch In ](<./Multi_Touch_In_DAT.md> "Multi Touch In DAT")• [NDI ](<./NDI_DAT.md> "NDI DAT")• [Null ](<./Null_DAT.md> "Null DAT")• [OP Execute ](<./OP_Execute_DAT.md> "OP Execute DAT")• [OP Find ](<./OP_Find_DAT.md> "OP Find DAT")• [OSC In ](<./OSC_In_DAT.md> "OSC In DAT")• [OSC Out ](<./OSC_Out_DAT.md> "OSC Out DAT")• [Out ](<./Out_DAT.md> "Out DAT")• [Panel Execute ](<./Panel_Execute_DAT.md> "Panel Execute DAT")• [Parameter ](<./Parameter_DAT.md> "Parameter DAT")• [Parameter Execute ](<./Parameter_Execute_DAT.md> "Parameter Execute DAT")• [ParGroup Execute ](<./ParGroup_Execute_DAT.md> "ParGroup Execute DAT")• [Perform ](<./Perform_DAT.md> "Perform DAT")• [POP to ](<./POP_to_DAT.md> "POP to DAT")• [Render Pick ](<./Render_Pick_DAT.md> "Render Pick DAT")• [Reorder ](<./Reorder_DAT.md> "Reorder DAT")• [Script ](<./Script_DAT.md> "Script DAT")• [Select ](<./Select_DAT.md> "Select DAT")• [Serial ](<./Serial_DAT.md> "Serial DAT")• [Serial Devices ](<./Serial_Devices_DAT.md> "Serial Devices DAT")• [SocketIO ](<./SocketIO_DAT.md> "SocketIO DAT")• [SOP to ](<./SOP_to_DAT.md> "SOP to DAT")• [Sort ](<./Sort_DAT.md> "Sort DAT")• [Substitute ](<./Substitute_DAT.md> "Substitute DAT")• [Switch ](<./Switch_DAT.md> "Switch DAT")• [Table ](<./Table_DAT.md> "Table DAT")• [TCP/IP ](<./TCP/IP_DAT.md> "TCP/IP DAT")• [Text ](<./Text_DAT.md> "Text DAT")• [Touch In ](<./Touch_In_DAT.md> "Touch In DAT")• [Touch Out ](<./Touch_Out_DAT.md> "Touch Out DAT")• [Transpose ](<./Transpose_DAT.md> "Transpose DAT")• [TUIO In ](<./TUIO_In_DAT.md> "TUIO In DAT")• [UDP In ](<./UDP_In_DAT.md> "UDP In DAT")• [UDP Out ](<./UDP_Out_DAT.md> "UDP Out DAT")• [UDT In ](<./UDT_In_DAT.md> "UDT In DAT")• [UDT Out ](<./UDT_Out_DAT.md> "UDT Out DAT")• [Video Devices ](<./Video_Devices_DAT.md> "Video Devices DAT")• [Web Client ](<./Web_Client_DAT.md> "Web Client DAT")• [Web ](<./Web_DAT.md> "Web DAT")• [Web Server ](<./Web_Server_DAT.md> "Web Server DAT")• [WebRTC ](<./WebRTC_DAT.md> "WebRTC DAT")• [WebSocket ](<./WebSocket_DAT.md> "WebSocket DAT")• [XML ](<./XML_DAT.md> "XML DAT")
