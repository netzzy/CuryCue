# Operator Family

There are seven **Families** of built-in [Operators](<./Operator.md> "Operator"). Of the six families, five are basic operator families and one is the [Component](<./Component.md> "Component") family which can further contain networks of operators. Components containing components form the TouchDesigner hierarchy and give rise to the operator [Paths](<./Network_Path.md> "Network Path"). 
* **[COMPs - Components](<./Component.md> "Component")** \- [Object Components](<./Object.md> "Object") (3D objects), [Panel Components](<./Panel_Component.md> "Panel Component") (2D UI gadgets), and other component types. Components contain other operators.
  * **[TOPs - Texture Operators](<./TOP.md> "TOP")** \- all 2D image operations.
  * **[CHOPs - Channel Operators](<./CHOP.md> "CHOP")** \- motion, audio, animation, control signals.
  * **[POPs - Point Operators](<./POP.md> "POP")** \- 3D points, primitives, polygons, point clouds, particles and GPU-based data operations.
  * **[DATs - Data Operators](<./DAT.md> "DAT")** \- ASCII text as plain text, scripts, XML, or organized in tables of cells.
  * **[MATs - Material Operators](<./MAT.md> "MAT")** \- materials and shaders.
  * **[SOPs - Surface Operators](<./SOP.md> "SOP")** \- legacy 3D points, polygons and other 3D primitives, with some capabilities not possible in POPs yet.


Within each operator family, "**generator** " operators have 0 inputs and create data, and "**filter** " operators have 1 or more input and filter data. 

Each operator family is a unique color. Only operators of the same family (color) can be [Wired](<./Wire.md> "Wire") together. Many operators have parameters that are references to operators in other families: [Links](<./Link.md> "Link"). Also [Exporting](<./Export.md> "Export") flows numeric data from CHOPs to all operators. 

[Custom Operators](<./Custom_Operators.md> "Custom Operators") of family TOP, CHOP, POP, SOP, DAT and SOP can be created using [C++](<./Category-C++.md> "Category:C++"), allowing you to extend TouchDesigner's functionality. They will show up in the [OP Create Dialog](<./OP_Create_Dialog.md> "OP Create Dialog") under the 'Custom' tab.
