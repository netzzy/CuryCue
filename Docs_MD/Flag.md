# Flag

The term "flag" in TouchDesigner refers to the indicator of states of an [Operator](<./Operator.md> "Operator") (the Bypass flag, Display flag, Lock flag, etc).   
  
### Operator Flags

Operator flags are located along on the left edge and bottom edge of a [Node](<./Node.md> "Node") in the [Network Editor](<./Network_Editor.md> "Network Editor"). 

Flags are also visible in a network's "Table View": Press "T" in the network to go to/from Table View. It shows nodes in a table format, where the complete set of flags is visible on the columns. 

Flags are not parameters and therefore changing a flag does not in itself cause a node to cook. You cannot export to a flag. 

Some flags are specific to certain operator families, like the Render flag for 3d Geometry operators. 

All flags are set using, for example,`op('nodename').lock = True`. 

To program in Python all common operator flags, see the Flags section in: [![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>) [OP_Class](<./OP_Class.md> "OP Class"), and the classes for each operator family. 

#### Flags on all Nodes
* [Viewer](<./Viewer_Flag.md> "Viewer Flag") \- turns on the data viewer in the center of the node.
  * [Viewer Active](<./Viewer_Active_Flag.md> "Viewer Active Flag") \- makes the viewer interactive so you can inspect the node's output data further, or operate a panel.
  * [Lock](<./Lock_Flag.md> "Lock Flag") \- the data the node outputs is frozen in memory (and saved in the`.toe``.tox`)
  * [Bypass](<./Bypass_Flag.md> "Bypass Flag") \- the first input is passed directly to the output. Bypass on a component causes all nodes inside it to be bypassed.
  * [Cooking](<./Cooking_Flag.md> "Cooking Flag") \- on a component, will cause nodes inside not to cook.
  * [Immune](<./Immune_Flag.md> "Immune Flag") \- a node inside a clone can be immune from cloning.
  * [Current](<./Current_Flag.md> "Current Flag") \- the node is the current node in a network
  * [Selected](<./Selected_Flag.md> "Selected Flag") \- the node is one of the selected nodes in a network.
  * [Expose](<./Expose_Flag.md> "Expose Flag") \- the node can be hidden from view in a network.
  * Python - a flag that sets the language of the content of a node to be Python (the default). Visible on the Parameter Dialog only.

#### Flags on 3D Object components
* [Render](<./Render_Flag.md> "Render Flag") \- if off, the object will not be seen in any render of the Render TOP or Render Pass TOP.
  * [Display](<./Display_Flag.md> "Display Flag") \- if off, the object will not be seen in any camera viewer.
  * [Pickable](<./Pickable_Flag.md> "Pickable Flag") \- if off, the object will not be selectable in [3D Geometry Viewers](<./Geometry_Viewer.md> "Geometry Viewer") or the [SOP Editor](<./SOP_Editor.md> "SOP Editor").

#### Flags on CHOPs
* [Export](<./Export_Flag.md> "Export Flag") \- if off, nothing is exported from that CHOP.

#### Flags on SOPs
* [Compare](<./Compare_Flag.md> "Compare Flag") \- displays the SOP's input geometry as a green wireframe for comparisons.
  * [Template](<./Template_Flag.md> "Template Flag") \- displays the SOP as templated geometry in 3D viewers. The grey wireframe template is not selectable or editable.
