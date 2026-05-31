# Panel Component

## 

Summary

Panel Components are a sub-[Family](<./Operator_Family.md> "Operator Family") of [Components](<./Component.md> "Component"), used to create custom interactive 2D control panels and user interfaces (also called [Panels](<./Panel.md> "Panel")). They are found in the second column of Components in the OP Create dialog. 

Examples are in Help > OP Snippets

The panel components are: 

[Container COMP](<./Container_COMP.md> "Container COMP") \- holds any number of other buttons, sliders, fields, containers, etc 

[Widget COMP](<./Widget_COMP.md> "Widget COMP") \- a Container COMP with extra functionality to support the library of [Widgets](<./Widgets.md> "Widgets"). 

[Text COMP](<./Text_COMP.md> "Text COMP") \- for entering text strings and rendering text in Panels. 

[Slider COMP](<./Slider_COMP.md> "Slider COMP") \- simple sliders in X, Y and XY, and outputs 1 or 2 channels 

[Button COMP](<./Button_COMP.md> "Button COMP") \- simple on/off buttons, including toggle, momentary, and sets of radio buttons 

[List COMP](<./List_COMP.md> "List COMP") \- lets you create and define lists using python 

[OP Viewer COMP](<./OP_Viewer_COMP.md> "OP Viewer COMP") \- creates a panel out of any operator's viewer 

[Parameter COMP](<./Parameter_COMP.md> "Parameter COMP") \- creates a panel out of any operator's parameters 

[Select COMP](<./Select_COMP.md> "Select COMP") \- selects a Panel Component from any other location 

[Table COMP](<./Table_COMP.md> "Table COMP") \- a concise and optimized way to create a grid of user interface gadgets 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>) [PanelCOMP_Class](<./PanelCOMP_Class.md> "PanelCOMP Class")

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[PanelCOMP Class](<./PanelCOMP_Class.md> "PanelCOMP Class")

### Panels within Panels

In 2D control panels, a Panel component is displayed within another panel ([Parenting](<./Parent.md> "Parent")) in two possible ways: 
* by placing the panel inside another Panel component (normally a Container component).
  * by a node being attached to another node in the same network like in [3D Parenting](<./3D_Parenting.md> "3D Parenting").

### Scripting with Panels

See [Panel Value](<./Panel_Value.md> "Panel Value"), [Panel Execute DAT](<./Panel_Execute_DAT.md> "Panel Execute DAT"), [PanelValue Class](<./PanelValue_Class.md> "PanelValue Class"), [PanelCOMP Class](<./PanelCOMP_Class.md> "PanelCOMP Class"), and the individual Panel COMP classes.
