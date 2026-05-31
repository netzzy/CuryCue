# Component

## 

Summary

See also [Category:Components](</index.php?title=Category:Components&action=edit&redlink=1> "Category:Components \(page does not exist\)") for a full list of articles related to Components. 

**Components** (or **COMPs**) are unique compared to other operator families in that they contain their own networks. To make a new network in your project, create a new Component using the [OP Create Menu](<./OP_Create_Menu.md> "OP Create Menu") and select from the **COMP** tab. Then go inside your new component and start building your network. Component networks can contain operators and/or additional sub-networks (additional components). Sub-networks create a hierarchy of networks that can be navigated (using the [network path](<./Network_Path.md> "Network Path")) and forms the overall hierarchical structure of`.toe`/`.tox`files. 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[COMP Class](<./COMP_Class.md> "COMP Class")

## Component Types

There are two special sub-[Families](<./Operator_Family.md> "Operator Family") of components: [Object Components](<./Object.md> "Object") and [Panel Components](<./Panel_Component.md> "Panel Component"), as well as numerous other components. These are listed in four separate columns in the OP Create Menu. 

### Object Components (3D objects for rendering)
* [Ambient Light COMP](<./Ambient_Light_COMP.md> "Ambient Light COMP")
  * [Blend COMP](<./Blend_COMP.md> "Blend COMP")
  * [Bone COMP](<./Bone_COMP.md> "Bone COMP")
  * [Camera COMP](<./Camera_COMP.md> "Camera COMP")
  * [Camera Blend COMP](<./Camera_Blend_COMP.md> "Camera Blend COMP")
  * [Environment Light COMP](<./Environment_Light_COMP.md> "Environment Light COMP")
  * [Nvidia Flow Emitter COMP](<./Nvidia_Flow_Emitter_COMP.md> "Nvidia Flow Emitter COMP")
  * [Geometry COMP](<./Geometry_COMP.md> "Geometry COMP")
  * [Handle COMP](<./Handle_COMP.md> "Handle COMP")
  * [Light COMP](<./Light_COMP.md> "Light COMP")
  * [Null COMP](<./Null_COMP.md> "Null COMP")
  * [Shared Mem In COMP](<./Shared_Mem_In_COMP.md> "Shared Mem In COMP")
  * [Shared Mem Out COMP](<./Shared_Mem_Out_COMP.md> "Shared Mem Out COMP")
  * [FBX COMP](<./FBX_COMP.md> "FBX COMP")
  * [USD COMP](<./USD_COMP.md> "USD COMP")


Object components can be parented in a hierarchy by connecting them together vertically (using their connectors on the top and bottom of the nodes). 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>) [ObjectCOMP_Class](<./ObjectCOMP_Class.md> "ObjectCOMP Class")

### Panel Components (interactive 2D panels)
* [Button COMP](<./Button_COMP.md> "Button COMP")
  * [Container COMP](<./Container_COMP.md> "Container COMP")
  * [Field COMP](<./Field_COMP.md> "Field COMP")
  * [List COMP](<./List_COMP.md> "List COMP")
  * [OP Viewer COMP](<./OP_Viewer_COMP.md> "OP Viewer COMP")
  * [Parameter COMP](<./Parameter_COMP.md> "Parameter COMP")
  * [Select COMP](<./Select_COMP.md> "Select COMP")
  * [Slider COMP](<./Slider_COMP.md> "Slider COMP")
  * [Table COMP](<./Table_COMP.md> "Table COMP")
  * [Widget COMP](<./Widget_COMP.md> "Widget COMP")


Panel components can be parented in a hierarchy by connecting them together vertically (using their connectors on the top and bottom of the nodes). 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>) [PanelCOMP_Class](<./PanelCOMP_Class.md> "PanelCOMP Class")

### Miscellaneous Components
* [Base COMP](<./Base_COMP.md> "Base COMP") \- the Base COMP has no panel gadgets and no object gadgets. It is the most basic shell of a component and can be used when a new network is required.
  * [Engine COMP](<./Engine_COMP.md> "Engine COMP") \- the Engine COMP will run a .tox file (component) in a separate process.
  * [Time COMP](<./Time_COMP.md> "Time COMP") \- the Time COMP contains a network of operators that can drive a Timeline, drive animations in Animation COMPs, or be used to drive any custom time-based system.
  * [Animation COMP](<./Animation_COMP.md> "Animation COMP") \- the Animation COMP is used to create keyframe animation data. Keyframed channels are stored inside the component and can be edited by scoping the Animation COMP in the [Animation Editor](<./Animation_Editor.md> "Animation Editor").
  * [Replicator COMP](<./Replicator_COMP.md> "Replicator COMP") \- the Replicator COMP creates a node for every row of a table, adding and deleting nodes ("replicants") as the table changes.
  * [Window COMP](<./Window_COMP.md> "Window COMP") \- the Window COMP create a separate floating application window. This can be used for [control panels](<./Panel_Component.md> "Panel Component") or when outputting to [multiple monitors](<./Multiple_Monitors.md> "Multiple Monitors").

### Component Inputs and Outputs

Components can have operator inputs and outputs on the left/right sides of the node if their network contains In and/or Out operators (of most types: TOP, CHOP, SOP, DAT. e.g. In TOP and Out CHOP). 

These allow operator data to flow in and out of the component's network, allowing a Component to share its internal data with other components, operators, and other parts of your project. Adding these OPs inside a Component will add alphanumerically-ordered inputs/outputs on the left/right side of the component that data can flow through. Inputs are on Component’s left side, outputs on the right. 

An output preview window is displayed when the cursor is over one of the outputs of a component. [MMB](<./Mouse_Click.md> "Mouse Click") on output preview to see info about that output. [RMB](<./Mouse_Click.md> "Mouse Click") on output preview brings up OP Create menu. 

#### Example

A noise component has been constructed to take a TOP, CHOP, and SOP input, apply noise to each one, then output the results. The component's internal network looks like this: 

The image below shows how the inputs and outputs of the Component can be connected into a network. 

### Component Flags

Components have the 4 common [Flags](</index.php?title=Flags&action=edit&redlink=1> "Flags \(page does not exist\)") along their left side: the [Viewer Flag](<./Viewer_Flag.md> "Viewer Flag"), the [Clone Immune Flag](<./Immune.md> "Immune"), the [Cooking Flag](<./Cooking_Flag.md> "Cooking Flag"), and the [Lock Flag](<./Lock_Flag.md> "Lock Flag"). [Object Components](<./Object.md> "Object") also have a [Bypass Flag](<./Bypass_Flag.md> "Bypass Flag") and an additional 3 flags in their lower right corner: the [Pickable Flag](<./Pickable_Flag.md> "Pickable Flag") (orange), the [Render Flag](<./Render_Flag.md> "Render Flag") (purple), and the [Display Flag](<./Display_Flag.md> "Display Flag") (blue). 

### Saving Components to Files

You can save out a Component into a [.tox file](<./.md> ".tox") with a RMB -> Save Component on the node. This is handy for sharing networks with other TouchDesigner users and projects. Any commonly-used tool or network you create in TouchDesigner is good candidate for a Component. 

To embed other files, like images, into .tox files, see [Virtual File System (VFS)](<./Virtual_File_System.md> "Virtual File System"). 

  
See Also [Category:Components](</index.php?title=Category:Components&action=edit&redlink=1> "Category:Components \(page does not exist\)")

COMPs   
---  
[Actor ](<./Actor_COMP.md> "Actor COMP")• [Ambient Light ](<./Ambient_Light_COMP.md> "Ambient Light COMP")• [Animation ](<./Animation_COMP.md> "Animation COMP")• [Annotate ](<./Annotate_COMP.md> "Annotate COMP")• [Base ](<./Base_COMP.md> "Base COMP")• [Blend ](<./Blend_COMP.md> "Blend COMP")• [Bone ](<./Bone_COMP.md> "Bone COMP")• [Bullet Solver ](<./Bullet_Solver_COMP.md> "Bullet Solver COMP")• [Button ](<./Button_COMP.md> "Button COMP")• [Camera Blend ](<./Camera_Blend_COMP.md> "Camera Blend COMP")• [Camera ](<./Camera_COMP.md> "Camera COMP")• [MediaWiki:Common.js ](<./MediaWiki-Common.md> "MediaWiki:Common.js")• [COMP ](<./COMP.md> "COMP")• Component • [Constraint ](<./Constraint_COMP.md> "Constraint COMP")• [Container ](<./Container_COMP.md> "Container COMP")• [Engine ](<./Engine_COMP.md> "Engine COMP")• [Environment Light ](<./Environment_Light_COMP.md> "Environment Light COMP")• [FBX ](<./FBX_COMP.md> "FBX COMP")• [Field ](<./Field_COMP.md> "Field COMP")• [Force ](<./Force_COMP.md> "Force COMP")• [Geo Text ](<./Geo_Text_COMP.md> "Geo Text COMP")• [Geometry ](<./Geometry_COMP.md> "Geometry COMP")• [GLSL ](<./GLSL_COMP.md> "GLSL COMP")• [Handle ](<./Handle_COMP.md> "Handle COMP")• [Impulse Force ](<./Impulse_Force_COMP.md> "Impulse Force COMP")• [Light ](<./Light_COMP.md> "Light COMP")• [List ](<./List_COMP.md> "List COMP")• [Null ](<./Null_COMP.md> "Null COMP")• [NVIDIA Flex Solver ](<./NVIDIA_Flex_Solver_COMP.md> "NVIDIA Flex Solver COMP")• [NVIDIA Flow Emitter ](<./NVIDIA_Flow_Emitter_COMP.md> "NVIDIA Flow Emitter COMP")• [OP Viewer ](<./OP_Viewer_COMP.md> "OP Viewer COMP")• [Parameter ](<./Parameter_COMP.md> "Parameter COMP")• [Replicator ](<./Replicator_COMP.md> "Replicator COMP")• [Select ](<./Select_COMP.md> "Select COMP")• [Shared Mem In ](<./Shared_Mem_In_COMP.md> "Shared Mem In COMP")• [Shared Mem Out ](<./Shared_Mem_Out_COMP.md> "Shared Mem Out COMP")• [Slider ](<./Slider_COMP.md> "Slider COMP")• [Table ](<./Table_COMP.md> "Table COMP")• [Text ](<./Text_COMP.md> "Text COMP")• [Time ](<./Time_COMP.md> "Time COMP")• [USD ](<./USD_COMP.md> "USD COMP")• [Widget ](<./Widget_COMP.md> "Widget COMP")• [Window ](<./Window_COMP.md> "Window COMP")
