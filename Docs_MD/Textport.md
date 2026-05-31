# Textport

The **Textport** is the dialog box in which commands and scripts can typed in manually. Output to the textport includes script errors and messages from`print()`and`debug()`calls in python code. You can also edit DATs in the textport.   
  
Dialogs -> Textport brings up the main textport, but you can also press F4 to open the Textport as a floating window. F4 will also work in [Perform Mode](<./Perform_Mode.md> "Perform Mode"). 

You can type python expressions and get them evaluated, as simple as`2+3`, which prints`5`on the next line. 

**Tip** : If you mis-type a line and press Enter, to edit it you can press the up-arrow to get the last lines you typed, and you can edit them with arrow/backspace/delete characters, then press Enter to re-execute it. 

If you are writing an expression like`op('/project1/geo1').par.tx`, you can more easily type`op('`, then drag the node to the textport (which adds its path to the string), and then type`').par.tx`and Enter: It will do the same thing. 

**Tip** : You can edit several DATs in the textport at once. Right-click on a DAT and select Edit Contents in Textport.... It will open a new tab in the textport where you can edit or view code. 

Note that some startup and system errors are output to Dialogs -> Console. 

You can put textports in [panes](<./Pane.md> "Pane") by setting the Pane Type menu to **Textport and DATs**. 

There are two scripting languages in TouchDesigner: [Python](<./Python.md> "Python") and the obsolete [Tscript](<./Tscript.md> "Tscript"). For Tscript, all commands are described in [Tscript Commands](<./Tscript_Commands.md> "Tscript Commands") and [Tscript Expressions](<./Tscript_Expressions.md> "Tscript Expressions"), and its scripting syntax is found in [Tscript](<./Tscript.md> "Tscript").`textport`is a [Tscript](<./Tscript.md> "Tscript") command that can be used to manipulate the contents of the dialog. 

You can redirect Python`stdout`and`stderr`to any DAT. Then you can use the OP Viewer TOP or COMP to convert that DAT into a texture and integrate it into your UI. 

## Textport Dialog

The textport can be opened from the **Dialogs** menu or by using the _Alt+Shift+T_ keyboard shortcut. Textport can also be opened as a [Pane](<./Pane.md> "Pane"). 

The simplest method to input Python scripts is through the textport. The textport, like all scripting in TouchDesigner, allows scripts to be specified in either Python or Tscript. 

After opening the textport, make sure it is set to Python language. This is controlled by the small toggle button in the upper left side of the textport. 

When it is set to **Py** , all input is interpreted as Python. When set to **T** it is interpreted as tscript. 

In addition the textport prompt and text color have different values for each language, making it easier to identify which state the textport is in: 

Text DAT contents can be edited directly in the textport as well. Dragging a Text DAT onto the Textport will give you the following options: 
* _Run DAT_ \- paste the command to execute the DAT as a script into the Textport. This option is only available in the main Textport tab.
  * _Open DAT_ \- open the contents of the DAT in a new tab in the Textport. You can switch between tabs by clicking on the tab header near the top of the dialog box.
  * _Paste Text_ \- pastes in the DAT's path name just like other OPs.


Additionally, any selected text can be dragged onto the Textport from anywhere on the interface. 

**Shortcut : Textport History**

A history or recent commands can be brought up by right-clicking anywhere in the textport. Pressing the "up" arrow key will step back through the command history. Pressing the down arrow key will step forward through command history. 

**Textport Search**

The search field at the top of the textport can be used to find strings in the scrollable text of the textport. 

**Textport History**

When working with DATs in the textport, a history of viewed DATs will be available on the right side of the Textport header. 

## Tips for Working in the Textport
* Holding shift and clicking on textport text will select the text between the cursor and the mouse position instead of just moving the cursor.

## Python in the Textport

In the textport, you can enter`help`for a list of available commands or`help(object)`for any python object, like`help(op('/project1').par.x)`. 

Script errors and messages from`print()`commands are also output to this dialog box. 

The main textport also receives the error messages and`print()`commands from all scripts that are run in [DATs](<./DAT.md> "DAT"). 

However startup and system errors are output to **Dialogs - > Console**. 

You can save typing OP path names by simply dragging any OP onto the Textport. Just drag the OP onto the Textport using the left mouse button. 

  
As a simple test type the following into the textport:`help(op)`This will output all help related to the`op()`method found in the [td Module](<./Td_Module.md> "Td Module"). 

The [td Module](<./Td_Module.md> "Td Module") is the main module containing all TouchDesigner related classes and objects. It is imported by default when the application begins.   
Another useful item is the [TDU Class](<./TDU_Class.md> "TDU Class"). This object contains some specific TouchDesigner utility functions useful during scripting and is available automatically through the`tdu`object. 

## TScript in the Textport

In the textport, you can enter`help`for a list of available commands or`exhelp`for a list of available expression functions. You can also access Tscript commands and expressions from the **Help** menu by selecting **Commands and Expressions**. 

Script errors and messages from`echo`commands are also output to this dialog box. 

The main textport also receives the error messages and`echo`commands from all scripts that are run in [DATs](<./DAT.md> "DAT"). 

However startup and system errors are output to **Dialogs - > Console**. 

You can save typing OP path names by simply dragging any OP onto the Textport. Just drag the OP onto the Textport using the left mouse button. 

##`textport`Command (Tscript only)

The`textport`command is used to manipulate the Textport dialog. One of the advantages of using`textport`is the ability to load DATs without having to navigate to them through the [Network](<./Network.md> "Network") pane. For example, to load a DAT in a floating Textport, the following code can be used: 
[code] 
     textport -l _/datpath/datname_
    
[/code]

This can be particularly useful while debugging scripts or [monitoring network performance](<./Optimize.md> "Optimize").
