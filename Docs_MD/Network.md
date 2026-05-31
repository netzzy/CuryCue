# Network

[![](./images/thumb/b/b4/NetworkExample.jpg/400px-NetworkExample.jpg)](</File:NetworkExample.jpg>)  
  
[](</File:NetworkExample.jpg> "Enlarge")

A TouchDesigner network

A network is a group of inter-connected [Nodes](<./Node.md> "Node") of [Operators](<./Operator.md> "Operator") in one [Component](<./Component.md> "Component"). Every component contains a network, and every network lives in a component. 

Network nodes are connected by colored [wires](<./Wire.md> "Wire") showing the data flow from operator to operator of the same family (e.g. CHOP to CHOP), each operator cooking its inputs and generating its output. 

Some network elements may not be directly wired. Dashed straight gray lines indicate other data references: 
* A [Python](<./Python.md> "Python") expression in a [parameter](<./Parameter.md> "Parameter") that refers to another operator.
  * A CHOP channel [exports](<./Export.md> "Export") to a parameter of another operator.
  * A parameter contains the [path](<./Network_Path.md> "Network Path") to another operator.


Components contain their own networks that use their input nodes (In OPs) to generate its output (Out OPs). 

Some nodes may be referenced by scripts in DATs, between which where no connecting lines are drawn. 

Generally, nodes are wired together with data flowing from left to right. 

See also: [Network Editor](<./Network_Editor.md> "Network Editor"), [Network Path](<./Network_Path.md> "Network Path").
