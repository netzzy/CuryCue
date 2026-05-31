# Operator

## 

Summary

Operators are the "[Nodes](<./Node.md> "Node")" in TouchDesigner networks, and they output data to other operators. Each operator is customized with its [Parameters](<./Parameter.md> "Parameter") and [Flags](<./Flag.md> "Flag"). 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[OP Class](<./OP_Class.md> "OP Class")

## Operator Families

There are six **Families** of built-in Operators. Of the six families, five are basic operator families and one is the [Component](<./Component.md> "Component") family which can further contain networks of operators. Components containing components form the TouchDesigner hierarchy and give rise to the operator [Paths](<./Network_Path.md> "Network Path"). 
* **[COMPs - Components](<./Component.md> "Component")** \- [Object Components](<./Object.md> "Object") (3D objects), [Panel Components](<./Panel_Component.md> "Panel Component") (2D UI gadgets), and other miscellaneous components. Components contain other operators.
  * **[TOPs - Texture Operators](<./TOP.md> "TOP")** \- all 2D image operations.
  * **[CHOPs - Channel Operators](<./CHOP.md> "CHOP")** \- motion, audio, animation, control signals.
  * **[SOPs - Surface Operators](<./SOP.md> "SOP")** \- 3D points, polygons and other 3D "primitives".
  * **[DATs - Data Operators](<./DAT.md> "DAT")** \- ASCII text as plain text, scripts, XML, or organized in tables of cells.
  * **[MATs - Material Operators](<./MAT.md> "MAT")** \- materials and shaders.


Within each operator family, "generator" operators have 0 inputs and create data, and "filter" operators have 1 or more input and filter data. 

Each operator family is a unique color. Only operators of the same family (color) can be [Wired](<./Wire.md> "Wire") together. Many operators have parameters that are references to operators in other families: [Links](<./Link.md> "Link"). Also [Exporting](<./Export.md> "Export") flows numeric data from CHOPs to all operators. 

[Custom Operators](<./Custom_Operators.md> "Custom Operators") of type TOP, CHOP, SOP, and DAT can be created using [C++](<./Category-C++.md> "Category:C++"), allowing you to extend TouchDesigner's functionality. They will show up in the [OP Create Dialog](<./OP_Create_Dialog.md> "OP Create Dialog") under the 'Custom' tab. 

See also: [![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>) [OP_Class](<./OP_Class.md> "OP Class")

## Creating Operators

To add new operators to a network, use the [OP Create Dialog](<./OP_Create_Dialog.md> "OP Create Dialog"). The OP Create Dialog can be opened by pressing the **< tab>** key, double-clicking on the network background, clicking the "+" button in the [Pane Bar](<./Pane_Bar.md> "Pane Bar"), selecting **Add Operator** from the right-click menu in any network, or by right-clicking on the input or output of another operator. 

## Converting data between OP Families

You can convert data between different Operator families using the following conversion operators. For example, you can convert geometry into a DAT list of point positions using the SOP to DAT operator, or convert a TOP image's pixel values into red, green, and blue channels in CHOP using the TOP to CHOP operator. 
* [TOP to CHOP](<./TOP_to_CHOP.md> "TOP to CHOP")
  * [CHOP to TOP](<./CHOP_to_TOP.md> "CHOP to TOP")
  * [CHOP to DAT](<./CHOP_to_DAT.md> "CHOP to DAT")
  * [CHOP to SOP](<./CHOP_to_SOP.md> "CHOP to SOP")
  * [DAT to CHOP](<./DAT_to_CHOP.md> "DAT to CHOP")
  * [DAT to SOP](<./DAT_to_SOP.md> "DAT to SOP")
  * [SOP to CHOP](<./SOP_to_CHOP.md> "SOP to CHOP")
  * [SOP to DAT](<./SOP_to_DAT.md> "SOP to DAT")
  * [Object CHOP](<./Object_CHOP.md> "Object CHOP")

## See also

[Node](<./Node.md> "Node"), [Wire](<./Wire.md> "Wire"), [Link](<./Link.md> "Link"), [Flag](<./Flag.md> "Flag"), [Connector](<./Connector.md> "Connector"), [Viewer](<./Viewer.md> "Viewer"), [OP Create Dialog](<./OP_Create_Dialog.md> "OP Create Dialog")
