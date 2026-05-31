# Parameter Dialog

A floating dialog, pane type, or dialog in a Network Editor that displays one operator's parameters.   
  
A Parameter Dialog allows you to view and manipulate all the [Parameters](</index.php?title=Parameters&action=edit&redlink=1> "Parameters \(page does not exist\)") of an Operator. Each Operator has one or more pages (or "tabs") of parameters viewable in the dialog, some tabs are unique to individual OPs, while others are common to different OP types. 

[![Parameter Dialog](./images/b/b5/Parameters_Dialog.png)](</File:Parameters_Dialog.png> "Parameter Dialog")

The dialog is viewable in three different areas in the TouchDesigner user interface. The Parameter Dialog is viewable in the Network Editor pane by pressing the **p** key. This will also hide the dialog if it is already visible. Parameters Dialog can also be an floating window by selecting it from the right-click menu on nodes. Finally, it can be viewed as a [Pane](<./Pane.md> "Pane") type. 

All of the parameter dialogs have a similar layout with the same set of gadgets to manipulate the various parameter values. Parameter dialogs are displayed on the right side of a network. Multiple parameter dialogs can be open at once, by flipping either the Network or Pane Sticky button. The topmost visible parameter dialog is the currently selected OP. 

**Note** : You can put a parameter dialog in a panel with the [Parameter COMP](<./Parameter_COMP.md> "Parameter COMP") and customize which pages and parameters to display. 

## Header

The header section in the parameter dialog displays the type and name of the operator and provides a number of buttons for basic operations as described below. The background color of the parameter header indicates the operator's family type. 

**Top Section**
* OP Type
  * OP Name


**Bottom Section**
* Operator Help
  * Python Class Help
  * Operator Info
  * Comment
  * Clipboard
  * Python/Tscript Operator Language Toggle
  * Hide/Show Default Parameters

## Parameter Pages

Each page displays a different parameter page for the operator. 

## Parameters

**Left click** on any parameter name/label to expand the Parameter Modes (See section below). Left click in a parameter's editable field to enter a new value. 

**Middle click** on and numeric parameter to bring up the [Value Ladder](<./Value_Ladder.md> "Value Ladder") to adjust the value. If the parameter is a double/triple/quadruple parameter (such as **Offset** in the [Displace TOP](<./Displace_TOP.md> "Displace TOP") or **Translate** in the [Geometry COMP](<./Geometry_COMP.md> "Geometry COMP")), opening the value ladder on the parameter's name/label will adjust all two/three/four at the same time. For individual parameter adjustment middle-mouse click on the numeric field itself. 

**Right click** on any parameter to open a popup menu of options for the parameter. 

## Working with Parameters of Multiple Operators

When selecting multiple operators of the same type, you can quickly set the parameter value for all the selected operators at to the same value at the same time. Simply select the multiple nodes to change, then change the parameter of the current one and all selected will also be updated. 

Also with multiple operators selected you can set which parameter page is first available when you go to the individual operator's parameters. This can be a time saver when going through many nodes to make individual changes on their parameters when you always need to access the same parameter page. For example, when you have 5 Text TOPs and need to change the color of each to a unique color. Instead of having to select the Color page of parameters each time, you can select all the operators and then select the Color page of the current operator. Now each time you individually select one of the other Text TOPs, the parameter page shown will already be set to the Color page, letting you change the colors more quickly. 

## Working with Parameter Modes

Every [Parameter](<./Parameter.md> "Parameter") can be in one of four modes, Constant Mode, [Expression](<./Expression.md> "Expression") Mode, [Export](<./Export.md> "Export") Mode, or [Bind](<./Binding.md> "Binding") mode. The Parameter Mode lets you quickly switch modes to test new values, expressions, export, or bind settings. 
* **Constant** \- this is the default mode which handles number and string values as entered into the parameter.
  * **Expression** \- this mode is for using a python or tscript expression to set the parameter's value.
  * **Export** \- this mode is for driving the parameter by [Exporting](<./Export.md> "Export") from a CHOP or DAT.
  * **Bind** \- this mode is for driving the parameter by [Binding](<./Binding.md> "Binding") to a parameter, table cell, [Bind CHOP](<./Bind_CHOP.md> "Bind CHOP"), or [Dependency Class](<./Dependency_Class.md> "Dependency Class").


To access the parameter modes, expand the parameter by clicking on the parameter's name/label area with the [LMB](<./Mouse_Click.md> "Mouse Click"). This will open an editing area for the parameter as well 4 toggles to switch between modes. To close this area, simply click on the parameter name/label or "-" icon. 

When the parameter is expanded, you will see the internal name of the parameter. This name is used for scripting and directly accessing the parameter. 

To the right of the internal name there are 4 square buttons to switch between modes. The grey button is for constant mode, the blue button for expression mode, the green button for export mode (must first have an exported value to the parameter to switch to export mode) and the purple button is for bind mode. 

The image below show 3 parameters expanded: the Seed parameter in constant mode, the Period parameter in expression mode, the Harmonics parameter in export mode, and the Harmonic Spread parameter in bind mode. 

  
The values of all 4 modes are saved in the parameter. This provides an ability to setup a constant value, an expression, an export, and a bind in the same parameter and freely switch between the 4 modes. If there is an expression, export, or bind set in a parameter but that mode is not currently selected, the mode button will indicate this by displaying a small square in the lower-left corner of the mode toggle button. 

The image below shows a parameter in constant mode with an expression, export, and bind set and ready to use. 

The advantages of working with parameter modes are rapid prototyping and testing and debugging capabilities. If you have a parameter driven by expression, export, or bind, you can easily jump to constant mode to stop the expression/export driving the parameter. While in constant mode you can test particular values or examine the system with certain set value. At any time you can switch the parameter mode back to expression/export/bind to reconnect the previous logic. 

## Parameter Manipulators
* [Parameter Dialog Gadgets](<./Parameter_Dialog_Gadgets.md> "Parameter Dialog Gadgets")

## Parameter Help

Parameter Help will popup by holding down the alt key and hovering the cursor over a parameter label. 

#### See also
* [Value Ladders](<./Value_Ladder.md> "Value Ladder")
