# TouchDesigner Glossary

## Learn to Speak the Language of TouchDesigner

**[.toe](<./.md> ".toe")** : TOuch Environment file, the file type used by TouchDesigner to save your entire project.

**[.tox](<./.md> ".tox")** : TouchDesigner Component file, the file type used to save a [Component](<./Component.md> "Component") of your TouchDesigner project.

**[Absolute Time](<./Absolute_Time.md> "Absolute Time")** or **[absTime](<./Absolute_Time.md> "Absolute Time")** : Absolute Time starts counting from 0 when the TouchDesigner process starts, and is always increasing. It will pause if the Power 0/1 button at the top of the UI is Off.

**[Adaptive Homing](<./Viewer.md> "Viewer")** : In the [Node Viewer](<./Node_Viewer.md> "Node Viewer") of a Geometry COMP or any POP, the Adaptive Homing option will continually keep in-view the 3D geometry being displayed, even when the geometry changes shape, size and animated position.

**[Annotate](<./Annotate_COMP.md> "Annotate COMP")** or **[Annotation](<./Annotate_COMP.md> "Annotate COMP")** : Annotates are displayed in the Network Editor as colored rectangles containing user-authored text and graphics. It is based on the [Annotate COMP](<./Annotate_COMP.md> "Annotate COMP") and allows you to document your networks with useful information like comments and node grouping.

**[Attributes](<./Attribute.md> "Attribute")** : Attributes are data associated with [POP](<./POP.md> "POP") geometry. [Points](<./Point.md> "Point"), [Vertex (Vertices)](<./Vertex.md> "Vertex") and [Primitives](<./Primitive.md> "Primitive") (polygons, lines, etc) can have any number of attributes. In POPs, position (`P`) is standard, and built-in optional attributes are [normals](<./Normals.md> "Normals") (`N`), texture coordinates (`Tex`), color (`Color`), etc.

**[Backdrop](<./Backdrop.md> "Backdrop")** : The Backdrop is the grid of node viewers that are visible behind the [Network](<./Network.md> "Network"), set by turning on [Display Flags](<./Display_Flag.md> "Display Flag") and the network RMB -> Display... Backdrop OPs.

**[Binding](<./Binding.md> "Binding")** : Binding is a [Parameter Mode](<./Parameter_Mode.md> "Parameter Mode") that ties two or more parameters' values together, where changing the value of any one of the bound parameters changes all of them. The actual value is stored in one place.

**[Bookmarks](<./Bookmark.md> "Bookmark")** : A pull-down list at the top of a network [Pane](<./Pane.md> "Pane") containing jump-to [Network Paths](<./Network_Path.md> "Network Path").

**[Bypass](<./Bypass_Flag.md> "Bypass Flag")** or **[Bypass Flag](<./Bypass_Flag.md> "Bypass Flag")** : An operator whose Bypass flag is set does nothing: All data going into its first input appears at its output unaffected.

**[Callback](<./Callback.md> "Callback")** : Some operators have a DAT [docked](<./Docking.md> "Docking") to them that contains some python functions. These functions, called "callbacks", get called when something in the operator changes.

**[Channel](<./Channel.md> "Channel")** : A [CHOP](<./CHOP.md> "CHOP") outputs one or more channels, where a channel is simply a sequence of numbers ([Samples](<./Sample.md> "Sample")), representing motion, audio, etc. Channels are passed between CHOPs in TouchDesigner networks. Channels can be [Exported](<./Export.md> "Export") to [Parameters](<./Parameter.md> "Parameter").

**[CHOP](<./CHOP.md> "CHOP")** or **[Channel Operator](<./CHOP.md> "CHOP")** : An [Operator Family](<./Operator_Family.md> "Operator Family") which operate on [Channels](<./Channel.md> "Channel") (a sequence of numbers ([Samples](<./Sample.md> "Sample"))) which are used for animation, audio, mathematics, simulation, logic, UI construction, and data streamed from/to devices and protocols.

**[Clone](<./Clone.md> "Clone")** : Cloning makes multiple components match the contents of a master component. A [Component](<./Component.md> "Component") whose Clone parameter is set will be forced to contain the same nodes, wiring and parameters as its master component. Cloning does not create new components as does the [Replicator COMP](<./Replicator_COMP.md> "Replicator COMP").

**[Component](<./Component.md> "Component")** or **[COMP](<./Component.md> "Component")** : An [Operator Family](<./Operator_Family.md> "Operator Family") that contains its own [Network](<./Network.md> "Network"). There are sixteen 3D [Object Component](<./Object_Component.md> "Object Component") and ten 2D [Panel Component](<./Panel_Component.md> "Panel Component") types. See also [Network Path](<./Network_Path.md> "Network Path").

**[Connector](<./Connector.md> "Connector")** : The notches on the left and right of each [Node](<./Node.md> "Node") that let you [Wire](<./Wire.md> "Wire") the output of one [Operator](<./Operator.md> "Operator") to the input of another of the same [Operator Family](<./Operator.md> "Operator"). The notches on the top and bottom of [3D Object Components](<./Object.md> "Object") and [Panel Components](<./Panel_Component.md> "Panel Component") that tie the components of each sub-[Family](<./Operator_Family.md> "Operator Family") in a [Hierarchy](<./Hierarchy.md> "Hierarchy").

**[Container](<./Container_COMP.md> "Container COMP")** : The Container component type is a [Panel Component](<./Panel_Component.md> "Panel Component") that holds, lays out and displays any number of other Panel Components.

**[Cook](<./Cook.md> "Cook")** : To re-compute the output data of the [Operators](<./Operator.md> "Operator"). An operator cooks when (1) its inputs change, (2) its [Parameters](<./Parameter.md> "Parameter") change, (3) when the timeline moves forward in some cases, or (4) [Scripting](<./Script.md> "Script") commands are run on the node. When the operator is a [Panel Component](<./Panel_Component.md> "Panel Component"), it also cooks when a user interacts with it. When an operator cooks, it usually causes operators connected to its output to re-cook. When TouchDesigner draws the screen, it re-cooks all the [Dependencies](<./Dependency.md> "Dependency") \- the necessary operators in all [Networks](<./Network.md> "Network"), contributing to a frame's total "cook time".

**[DAT](<./DAT.md> "DAT")** or **[Data Operator](<./DAT.md> "DAT")** : An [Operator Family](<./Operator_Family.md> "Operator Family") that manipulates text strings: multi-line text or tables. Multi-line text is often a python [Script](<./Script.md> "Script") or [GLSL](<./GLSL.md> "GLSL") Shader, but can be any multi-line text. [Tables](<./Table_DAT.md> "Table DAT") are rows and columns of cells, each containing a text string.

**[Dependency](<./Dependency.md> "Dependency")** : is the [Procedural](<./Procedural.md> "Procedural") mechanism in TouchDesigner, where if one piece of data changes, it automatically causes other operators and expressions to re-[Cook](<./Cook.md> "Cook").

**[Designer Mode](<./Designer_Mode.md> "Designer Mode")** : You edit your networks in Designer Mode. See [Perform Mode](<./Perform_Mode.md> "Perform Mode").

**[Dialog](<./Dialog.md> "Dialog")** : Any floating window that is not a [Pane](<./Pane.md> "Pane") or [Viewer](<./Viewer.md> "Viewer").

**[Dimension](<./Dimension.md> "Dimension")** : Dimension is metadata of a POP that describes the structure of the point list, which may be made of rows and columns of points (which is two dimensions of size nrows and ncolumns).

**[Display Flag](<./Display_Flag.md> "Display Flag")** : The blue [flag](<./Flag.md> "Flag") on Geometry components and SOP operators determines if the geometry contained in that operator is visible in node viewers and geometry viewer panes. See [Render Flag](<./Render_Flag.md> "Render Flag").

**[Docking](<./Docking.md> "Docking")** or **[Docked](<./Docking.md> "Docking")** : Any [node](<./Node.md> "Node") can be docked to another node. This helps organize networks as two node that are docked together will stay together when the dock parent is moved in a network editor. A docked node can be collapsed into a small icon under the dock parent, reducing network clutter.

**[Event](<./Event.md> "Event")** : Events are single-moment occurrences that are generated from a variety of conditions - from input actions that a user causes, from external devices and software, and from internal TouchDesigner states. A wide set of operator types respond to events and give the user a place to write python code that reacts to events.

**[Export](<./Export.md> "Export")** : Exporting is the connection of CHOP channels to parameters of operators. The output of each exporting CHOP is one or more channels, active only while the [CHOP Viewer](<./CHOP_Viewer.md> "CHOP Viewer") is on. The current value of a channel can be exported to a parameter of any operator, overriding that parameter's value. See [Parameter](<./Parameter.md> "Parameter").

**[Expression](<./Expression.md> "Expression")** : A text string that contains data (string, float, list, boolean, etc.) and operators (+ * < etc) that are evaluated by the node's language (python or Tscript) and returns a string, float list or boolean, etc. Expressions are used in parameters, [DATs](<./DAT.md> "DAT") and in scripts.

**[Extend Conditions](<./Extend_Conditions.md> "Extend Conditions")** or **[Extend Region](<./Extend_Conditions.md> "Extend Conditions")** : In CHOPs, Extend Conditions determine what numbers you get when you try to get a channel value that is outside its start-end range - in its Extend Regions.

**[Extensions](<./Extensions.md> "Extensions")** : Any component can be extended with its own Python classes which contain python functions and data.

**[File Metadata](<./File_Metadata.md> "File Metadata")** : Read and write different types of file metadata.

**[Filter](<./Filter.md> "Filter")** : Operators that need 1 or more inputs are called Filters in TouchDesigner, like a Math CHOP. See [Generator](<./Generator.md> "Generator").

**[Filter per Sample](<./Filter_per_Sample.md> "Filter per Sample")** : A powerful feature of CHOPs that filter over time, like the [Lag CHOP](<./Lag_CHOP.md> "Lag CHOP") and [Filter CHOP](<./Filter_CHOP.md> "Filter CHOP") where each sample acts as its own filter.

**[Flag](<./Flag.md> "Flag")** : Indicator of certain states of an operator (bypass, display, lock, viewer active).

**[Folder](<./Folder.md> "Folder")** : A Folder in TouchDesigner always refers to a Windows or macOS operating system directory/folder system that contain files and other folders. It does not refer to operators within TouchDesigner. See [Network Path](<./Network_Path.md> "Network Path").

**[Frame](<./Frame.md> "Frame")** : The term "Frame" is a measurement of time used (1) in the [Timeline](<./Timeline.md> "Timeline"), (2) as a time-unit in CHOPs, and (3) as a time unit in movie files that are read into [TOPs](<./TOP.md> "TOP") and written out from TOPs. The frame rate is the frames per second ([FPS](</index.php?title=FPS&action=edit&redlink=1> "FPS \(page does not exist\)")).

**[Frame Rate](<./Frame_Rate.md> "Frame Rate")** or **[FPS](<./Frame_Rate.md> "Frame Rate")** : The [Frames](<./Frame.md> "Frame")-per-Second that TouchDesigner's [Timeline](<./Timeline.md> "Timeline") runs at. Set with`project.cookRate`.

**[Generator](<./Generator.md> "Generator")** : Operators that do not need any inputs connected are called Generators in TouchDesigner, like a Pattern CHOP. See [Filter](<./Filter.md> "Filter").

**[Geometry](<./Geometry_COMP.md> "Geometry COMP")** : The 3D data held in SOPs and passed for rendering by the [Geometry COMP](<./Geometry_COMP.md> "Geometry COMP").

**[Geometry Spreadsheet](<./Geometry_Spreadsheet.md> "Geometry Spreadsheet")** : Currently, use a [SOP to DAT](<./SOP_to_DAT.md> "SOP to DAT") to look at SOP point/polygon XYZ and other attributes. Formerly a [Pane](<./Pane.md> "Pane") type.

**[Geometry Viewer](<./Geometry_Viewer.md> "Geometry Viewer")** : A 3D viewport for viewing and manipulating 3D scenes or objects interactively. A geometry viewer can be found in [Panes](<./Pane.md> "Pane") (alt+3 in any pane) or the [Node Viewers](<./Node_Viewer.md> "Node Viewer") of all Geometry Object components.

**[Global OP Shortcut](<./Global_OP_Shortcut.md> "Global OP Shortcut")** : A name for a component that is accessible from any node in a project, which can be declared in a component's Global Operator Shortcut parameter.

**[GPU](<./GPU.md> "GPU")** : The Graphics Processing Unit. This is the high-speed, many-core processor of the graphics card/chip that takes geometry, images and data from the CPU and creates images and processed data.

**[Group](<./Group.md> "Group")** : A Group in POPs and SOPs is a named subset of points or primitives. It is created with the [Group POP](<./Group_POP.md> "Group POP") or Group SOP. Numerous operations in POPs and SOPs (using a Group parameter) can be restricted to affect the points or primitives in selected groups, and not affect others.

**[Hierarchy](<./Hierarchy.md> "Hierarchy")** : Hierarchy relates components with other components. There are two groups of Hierarchy in TouchDesigner. 3D Object Components, and 2D Panel Components. Hierarchies let one component to be positioned relative to another. Each group can be connected via lines between the bottoms/tops of nodes in a network, or by placing one component inside the other.

**[Immune](<./Immune.md> "Immune")** : Every node has an [Immune Flag](<./Immune_Flag.md> "Immune Flag"), when on and the node is inside a [Clone](<./Clone.md> "Clone"), it is not affected by any change to the clone master, so you can store extra data in the clone or set a node to be ignored by the cloning process.

**[Instance](<./Instance.md> "Instance")** : (1) A [Geometry Component](<./Geometry_COMP.md> "Geometry COMP") can instance and render its SOP geometry many times: once for each sample in a CHOP, row of a DAT table, pixel in a TOP, or point of a SOP, (2) An instance is an OP that doesn't actually have its own data, but rather just refers to an OP (or has an input) whose data it uses. This includes Null OPs, Switch OPs and in some cases Select OPs.

**[Internal Operators](<./Internal_Operators.md> "Internal Operators")** : Internal Operators (iOPs) provide a simple shortcut to a frequently-used operator, accessing from anywhere in that component.

**[Internal Parameters](<./Internal_Parameters.md> "Internal Parameters")** : Internal Parameters (iPars) act like local variables in a component. They provide a simple shortcut to collections of parameters that you create within a component, and access from anywhere in that component.

**[Interoperability](<./Interoperability.md> "Interoperability")** or **[Interops](<./Interoperability.md> "Interoperability")** : The devices, protocols and software tools that TouchDesigner interfaces to, via native [Operators](<./Operator.md> "Operator") and [Palette](<./Palette.md> "Palette") components.

**[Keyboard Shortcuts](<./Keyboard_Shortcuts.md> "Keyboard Shortcuts")** : There are two types of keyboard shortcuts: [Application Shortcuts](<./Application_Shortcuts.md> "Application Shortcuts") that are built-in to TouchDesigner's authoring interface, and [Panel Shortcuts](<./Panel_Shortcuts.md> "Panel Shortcuts") that you create for any custom built panels.

**[Keyframe](<./Keyframe.md> "Keyframe")** : In the [Animation component](<./Animation_COMP.md> "Animation COMP") each keyframe specifies a channel's value at a specific time (or frame). A keyframe holds a value, slopes and accelerations, and an interpolation type. A channel's keyframes are used to interpolate and determine the values of all the samples of the channel.

**[Layout](<./Layout.md> "Layout")** : (1) The TouchDesigner window is made of a menu bar at the top, a [Timeline](<./Timeline.md> "Timeline") at the bottom, plus one of a choice of Layouts in the middle. A Layout is made on one or more Panes, each Pane can contain a Network Editor, Viewer, Panel, etc. See [Pane](<./Pane.md> "Pane") and [Bookmark](<./Bookmark.md> "Bookmark"). (2) Nodes in a network are arranged using Layout commands in the RMB menu.

**[Link](<./Link.md> "Link")** or **[Reference](<./Link.md> "Link")** : A Link or Reference is a dashed line between nodes that represent other data flowing between nodes. Examples are CHOP [Exports](<./Export.md> "Export"), node [Paths](<./Network_Path.md> "Network Path") in parameters, and [expressions](<./Expression.md> "Expression") in parameters referencing CHOP channels, DAT tables and other nodes. In contrast is a [Wire](<./Wire.md> "Wire") that connects nodes in the same [Operator Family](<./Operator_Family.md> "Operator Family").

**[Lock Flag](<./Lock_Flag.md> "Lock Flag")** : When an operator is locked, it does not [cook](<./Cook.md> "Cook") and its output data remains frozen, even when the TouchDesigner session is saved to a [.toe](<./.md> ".toe") file and restarted.

**[Macro](<./Macro.md> "Macro")** : The F1 to F12 keys run macros. The F1 macro puts you in [Perform Mode](<./Perform_Mode.md> "Perform Mode"). Pressing F9 or F10 over a panel brings up the network of the panel element you are pointing at. Macros are written in the legacy [Tscript](<./Tscript.md> "Tscript").

**[MAT](<./MAT.md> "MAT")** or **[Material](<./MAT.md> "MAT")** : MATs or Materials are an [Operator Family](<./Operator_Family.md> "Operator Family") that applies a [Shader](<./Shader.md> "Shader") to a SOP or 3D Geometry Object for rendering textured surfaces with lighting.

**[Menu Bar](<./Menu_Bar.md> "Menu Bar")** : The bar at the top of the [Designer Mode](<./Designer_Mode.md> "Designer Mode") interface that contains menus, links, status messages and other controls.

**[MultiTouch](<./MultiTouch.md> "MultiTouch")** or **[Multi-Touch](<./MultiTouch.md> "MultiTouch")** : Display devices in TouchDesigner that support multiple-finger or control-point input.

**[Network](<./Network.md> "Network")** : Every component contains a network of operators that create and modify data. The operators are connected by wires that define where data is routed after the operator cooks its inputs and generates an output.

**[Network Editor](<./Network_Editor.md> "Network Editor")** : A pane type where networks of operators can be created and edited.

**[Node](<./Node.md> "Node")** : The generic thing that holds an [Operator](<./Operator.md> "Operator"), and includes [Flags](<./Flag.md> "Flag") (display, bypass, lock, render, immune) and its position/size in the network. Whether you "lay down an Operator" or "lay down an Node", you're doing the same thing.

**[Node Viewer](<./Node_Viewer.md> "Node Viewer")** : The viewer found on each operator in a [Network Editor](<./Network_Editor.md> "Network Editor") pane. This viewer is turned on by clicking the [Viewer Flag](<./Viewer_Flag.md> "Viewer Flag").

**[Object](<./Object.md> "Object")** or **[3D Object](<./Object.md> "Object")** or **[Object Space](<./Object.md> "Object")** : The sub-[Family](<./Operator_Family.md> "Operator Family") of [Component](<./Component.md> "Component") types that are used to define and render 3D scenes. A [Geometry Component](<./Geometry_COMP.md> "Geometry COMP") is an Object that contains the 3D shapes to render. A [Camera COMP](<./Camera_COMP.md> "Camera COMP") and [Light COMP](<./Light_COMP.md> "Light COMP") are other Object types. Separately, "Objects" also refers to Python objects.

**[OP Create Menu](<./OP_Create_Menu.md> "OP Create Menu")** : The menu used to select and create a new operator. Can be opened in the [Network Editor](<./Network_Editor.md> "Network Editor") by pressing the <tab> key or double-clicking the background, or by clicking the [MMB](<./Mouse_Click.md> "Mouse Click") or [RMB](<./Mouse_Click.md> "Mouse Click") on an operator's output connector, or by the **+** sign in the [Pane Bar](<./Pane.md> "Pane").

**[OP](<./Operator.md> "Operator")** or **[Operator](<./Operator.md> "Operator")** : Any of the procedural data operators. OPs do all the work in TouchDesigner. They "cook" and output data to other OPs, which ultimately result in new images, data and audio being generated. See [Node](<./Node.md> "Node").

**[Operator Family](<./Operator_Family.md> "Operator Family")** or **[Family](<./Operator_Family.md> "Operator Family")** : The Operator Families are [TOPs](<./TOP.md> "TOP"), [CHOPs](<./CHOP.md> "CHOP"), [POPs](<./POP.md> "POP") (Point Operators), [MATs](<./MAT.md> "MAT") (Materials), [DATs](<./DAT.md> "DAT") (data operators), [SOPs](<./SOP.md> "SOP") and [Components](<./Component.md> "Component") (Panel Gadgets and Objects).

**[Palette](<./Palette.md> "Palette")** : A built-in panel in TouchDesigner that contains a library of components and media that can be dragged-dropped into a TouchDesigner network.

**[Pane](<./Pane.md> "Pane")** : A work area in TouchDesigner's layout that includes the [Network Editor](<./Network_Editor.md> "Network Editor") and 7 other pane types used for different tasks. The TouchDesigner interface can consist of a single pane, or be split into multiple panes.

**[Pane Type](<./Pane.md> "Pane")** : There are 8 pane types; Network, Panel, Textport, Geometry Viewer, TOP Viewer, CHOP Viewer, Parameters, Graph Editor for CHOP Channels, or a Geometry Spreadsheet.

**[Panel Component](<./Panel_Component.md> "Panel Component")** : The sub-[Family](<./Operator_Family.md> "Operator Family") of [Components](<./Component.md> "Component") that are used to create custom interactive 2D control [panels](<./Panel.md> "Panel") (Container, Widget, Text COMP Slider, Button, etc.).

**[Panel Value](<./Panel_Value.md> "Panel Value")** : The internal states of a panel component are Panel Values, and are accessed with a Panel CHOP, a`OP.panel`Python expression, or a [Panel Execute DAT](<./Panel_Execute_DAT.md> "Panel Execute DAT").

**[Panel](<./Panel.md> "Panel")** or **[Control Panel](<./Panel.md> "Panel")** : A custom interactive control panel built within TouchDesigner. Panels are created using [Panel Components](<./Panel_Component.md> "Panel Component").

**[Parameter](<./Parameter.md> "Parameter")** : Every operator in TouchDesigner has a set of control Parameters that can be integer or floating point numbers, menus, binary toggles, text strings or operator [paths](<./Network_Path.md> "Network Path"), which determine the output of the operator.

**[Parameter Dialog](<./Parameter_Dialog.md> "Parameter Dialog")** : A floating dialog, pane type, or dialog in a Network Editor that displays one operator's parameters.

**[Parameter Expression](<./Parameter_Expression.md> "Parameter Expression")** : A parameter expression is a python expression that is in the expression field of a parameter.

**[Parameter Mode](<./Parameter_Mode.md> "Parameter Mode")** : Every Parameter can be in one of four modes: Constant Mode, [Expression](<./Expression.md> "Expression") Mode, [Export](<./Export.md> "Export") Mode or Bind ([Binding](<./Binding.md> "Binding")) Mode.

**[Parameter Reference](<./Parameter_Reference.md> "Parameter Reference")** : A parameter reference can be setup between any two parameters by putting an expression in one parameter that refers to another parameter. This creates a [Link](<./Link.md> "Link") between the two parameters such that when one changes, the other will change automatically (known in other software as a "constraint").

**[Parameter Value](<./Parameter.md> "Parameter")** : Parameter Value refers to the constant, the expression, the export, the bind reference and the [Parameter Mode](<./Parameter_Mode.md> "Parameter Mode") that are used together to determine the "evaluated" parameter value.

**[Parent](<./Parent.md> "Parent")** : There are 2 kinds of parenting. The "parent component" is the component in which a node resides. The metaphor is extended to include grand parents, grand-grand parents, etc. The root`/`is the ultimate parent to all nodes. See also [3D Parenting](<./3D_Parenting.md> "3D Parenting") and panel [Parenting](<./Parent.md> "Parent").

**[Parent Shortcut](<./Parent_Shortcut.md> "Parent Shortcut")** : A Parent Shortcut is a parameter on a component that contains a name that you can use anywhere inside the component to refer to that component using the syntax`parent.Name`, for example`parent.Effect.width`to obtain panel width.

**[ParGroup](<./ParGroup.md> "ParGroup")** or **[Parameter Group](<./ParGroup.md> "ParGroup")** : A ParGroup is a group of related parameters that you can set and get as a whole instead of its individual parameters, like ParGroup`t`is`tx ty tz`.

**[Path](<./Network_Path.md> "Network Path")** or **[Network Path](<./Network_Path.md> "Network Path")** : The location of an operator within the TouchDesigner environment, for example,`/geo1/circle1`, a node called`circle1`in a component called`geo1`. The path`/`is called [Root](<./Root.md> "Root"). This path is displayed at the top of every [Pane](<./Pane.md> "Pane"), showing which Component's network you are currently in. To refer instead to a filesystem folder, directory, disk file or`http:`address, see [Folder](<./Folder.md> "Folder").

**[Pattern Expansion](<./Pattern_Expansion.md> "Pattern Expansion")** : Pattern Expansion takes a short string and expands it to generate a longer string of individual elements.

**[Pattern Matching](<./Pattern_Matching.md> "Pattern Matching")** : Matching names using wildcard characters and bracketing. Useful in "[Select](<./Select_CHOP.md> "Select CHOP")" type parameters to select multiple operators, paths, channels, etc.

**[Pattern Matching](<./Pattern_Matching_Support.md> "Pattern Matching Support")** : Matching names using wildcard characters and bracketing. Useful in "[Select](<./Select_CHOP.md> "Select CHOP")" type parameters to select multiple operators, paths, channels, etc.

**[Pattern Replacement](<./Pattern_Replacement.md> "Pattern Replacement")** : Used in conjunction with Pattern Matching to replace all or portions of matched strings with new data. Used in places such as the [Rename CHOP](<./Rename_CHOP.md> "Rename CHOP").

**[Perform Mode](<./Perform_Mode.md> "Perform Mode")** : Perform Mode is an optimized mode for live performance that only renders one specified [Window COMP](<./Window_COMP.md> "Window COMP") which is one window that contains your video outputs and your (optional) control interface. In Perform Mode the network editing window is not open - you edit your networks in [Designer Mode](<./Designer_Mode.md> "Designer Mode"). Alternate with F1 and Esc.

**[Performance Monitor](<./Performance_Monitor.md> "Performance Monitor")** : The tool built-in to TouchDesigner that analyzes and displays what TouchDesigner is doing as it generates the output images, audio and data.

**[Pipe](<./Pipe.md> "Pipe")** : A way of moving data from one TouchDesigner process to another. Images are moved via Touch Out / In TOPs, channels are moved via Touch Out / In CHOPs and Pipe Out / In CHOPs. Data moves via TCP/IP or UDP.

**[Playbar](<./Timeline.md> "Timeline")** : Playbar is the former name for Timeline. See [Timeline](<./Timeline.md> "Timeline").

**[Point](<./Point.md> "Point")** : Each SOP has a list of Points. Each point has an XYZ 3D position value plus other optional attributes. Each polygon [Primitive](<./Primitive.md> "Primitive") is defined by a vertex list, which is list of point numbers.

**[Polygon](<./Polygon.md> "Polygon")** : A polygon is a type of [Primitive](<./Primitive.md> "Primitive") that is formed from a set of [Vertices](<./Vertex.md> "Vertex") in 3D that are implicitly connected together to form a multi-edge shape.

**[POP](<./POP.md> "POP")** or **[Point Operators](<./POP.md> "POP")** : POPs (**Point Operators**) is a new [Operator Family](<./Operator_Family.md> "Operator Family") of TouchDesigner that runs on the GPU accelerated graphics card or chips, and creates/modifies 3D data which is rendered by the [Render TOP](<./Render_TOP.md> "Render TOP") or passed to devices like DMX lighting, LED arrays, lasers or other external systems.

**[Popup Help](<./Popup_Help.md> "Popup Help")** : Help messages appear when (1) moving the cursor over the TouchDesigner user interface, (2) clicking the ? help button on the corner of each operator's Parameters page, (3) holding the Alt key while moving the cursor over the parameter names in the Parameter Dialogs, and (4) evaluating selected text in parameter expressions.

**[Primitive](<./Primitive.md> "Primitive")** : A surface type in [SOPs](<./SOP.md> "SOP") that includes polygon, curve (NURBS and Bezier), patch (NURBS and Bezier) and other basic shapes like sphere, tube and metaball. [Points](<./Point.md> "Point") and Primitives are part of the [Geometry Detail](<./Geometry_Detail.md> "Geometry Detail"), which is a part of a [SOP](<./SOP.md> "SOP").

**[Privacy](<./Privacy.md> "Privacy")** : Privacy of TouchDesigner Components (`.tox`files) or Projects (`.toe`files) is the protection of networks that enables them to be used but not be visible or editable.

**[Procedural](<./Procedural.md> "Procedural")** : Procedural means the automatic generation of outputs based on live inputs and the current state of TouchDesigner. It is the chain-reaction mechanism of TouchDesigner, where if one piece of data changes, it automatically causes other "[dependent](<./Dependency.md> "Dependency")" operators and expressions to re-[Cook](<./Cook.md> "Cook") and re-generate the outputs.

**[Projection Mapping](<./Projection_Mapping.md> "Projection Mapping")** : A technique or workflow that allows for displaying content on often irregular shapes and surfaces.

**[Pulse](<./Pulse.md> "Pulse")** : To "pulse" a parameter is to send it a signal from (1) an [exported](<./Export.md> "Export") CHOP channel or (2) a python command or (3) a mouse click that causes a new action to occur immediately. A pulse via python is via the`.pulse()`function on a pulse-type parameter, such as Reset parameter in a [Speed CHOP](<./Speed_CHOP.md> "Speed CHOP"). A pulse from a CHOP is typically a 0 to 1 to 0 signal in an exported channel.

**[Quad Reprojection](<./Quad_Reprojection.md> "Quad Reprojection")** : Quad Reprojection renders pixel-perfect perspective-correct images for flat TVs and LED panels hung at any orientation.

**[Reference](<./Reference.md> "Reference")** : The grey dashed lines between nodes is a Reference (or [Link](<./Link.md> "Link")). A Reference is (1) a [Parameter Reference](<./Parameter_Reference.md> "Parameter Reference"), a parameter in an OP that is a name or path to another operator, (2) a [Node Reference](</index.php?title=Node_Reference&action=edit&redlink=1> "Node Reference \(page does not exist\)"), an expression in a parameter or DAT script that contains the name or path of another operator, (3) a DAT Cell Reference or (4) a CHOP Channel Reference.

**[Reference](<./Link.md> "Link")** or **[Link](<./Link.md> "Link")** : A [Link](<./Link.md> "Link"). The grey dashed lines between nodes is a Reference or Link that indicates one operator is getting data from another operator from any [Operator Family](<./Operator_Family.md> "Operator Family").

**[Render Flag](<./Flag.md> "Flag")** : The purple flag on COMP and SOP nodes that determines if the node will be rendered in a [Render TOP](<./Render_TOP.md> "Render TOP") or [Render Pass TOP](<./Render_Pass_TOP.md> "Render Pass TOP"). The operator must also be listed in the Render / Render Pass TOP's 'Geometry' parameter.

**[Rendering](<./Rendering.md> "Rendering")** : Rendering is the creation of a 3D image with the Render TOP. Rendering is also used more generally to include the compositing (with TOPs) to generate an output image.

**[Replicator](<./Replicator_COMP.md> "Replicator COMP")** : Creates copies of a component, one for every row in a table or using a Number of Replicants parameter - it is the "for-loop" of operators. Unlike [Clone](<./Clone.md> "Clone"), it automatically creates copies of a master component.

**[Resolution](<./Resolution_TOP.md> "Resolution TOP")** : The width and height of an image in pixels. Most TOPs, like the [Movie File In TOP](<./Movie_File_In_TOP.md> "Movie File In TOP") can set the image resolution. See [Aspect Ratio](<./TOP_Generator_Common_Page.md> "TOP Generator Common Page") for the width/height ratio of an image, taking into account non-square pixels.

**[RMB Menu](<./RMB_Menu.md> "RMB Menu")** : The menu that appears when clicking the right mouse button on different parts of TouchDesigner. (Sometimes you need to be holding down Ctrl.)

**[Root](<./Root.md> "Root")** : TouchDesigner is a hierarchy of components. "root" is the top-most network in the hierarchy. The [Network Path](<./Network_Path.md> "Network Path") or Path for root is simply`/`. A typical path is`/project1/moviein1`.

**[Sample Rate](<./CHOP.md> "CHOP")** or **[Sample](<./CHOP.md> "CHOP")** : samples-per-second of a [CHOP](<./CHOP.md> "CHOP"). Each CHOP in your network has a sample rate. In contrast, the overall timeline has a [Frame Rate](<./Frame_Rate.md> "Frame Rate"), which is the number of frames to [cook](<./Cook.md> "Cook") and display per second, generally your monitor display frequency, default 60.

**[Scope](<./Scope.md> "Scope")** : A parameter in most CHOPs that restricts which channels of that CHOP will be affected. Normally all channels of a CHOP are affected by the operator. TOPs have Channel Mask, a similar feature.

**[Script](<./Script.md> "Script")** : A set of commands located in a Text DAT that are triggered to run under certain conditions. There are two scripting languages in TouchDesigner: [Python](<./Python.md> "Python") and the original [Tscript](<./Tscript.md> "Tscript"). Scripts and single-line commands can also be run in the [Textport](<./Textport.md> "Textport").

**[Sequential Parameters](<./Sequential_Parameters.md> "Sequential Parameters")** or **[Sequence Blocks](<./Sequential_Parameters.md> "Sequential Parameters")** : Sequential Parameters are blocks of parameters (Sequential Blocks) that can be reproduced multiple times by a user to create multiple entities.

**[Shader](<./Shader.md> "Shader")** : The OpenGL (pre-2022) or Vulkan (2022-) code that runs on the GPU and creates rendered images from polygons and textures. A shader is programmed in [Text DATs](<./Text_DAT.md> "Text DAT") and referenced by a [GLSL Material](<./GLSL_MAT.md> "GLSL MAT") or a [GLSL TOP](<./GLSL_TOP.md> "GLSL TOP"). Shaders are composed of up to three parts: Vertex Shader, Pixel Shader and Compute Shader.

**[Shortcut](<./Operator_Shortcuts.md> "Operator Shortcuts")** : Operator shortcuts are Python objects that return operators (or sometimes parameters). These include [Parent Shortcuts](<./Parent_Shortcut.md> "Parent Shortcut") for accessing a component from within that component, and [Global OP Shortcuts](<./Global_OP_Shortcut.md> "Global OP Shortcut") that access a unique component from anywhere in TouchDesigner.

**[Snippets](<./OP_Snippets.md> "OP Snippets")** : [OP Snippets](<./OP_Snippets.md> "OP Snippets") is a set of 700+ live examples of TouchDesigner operators. You can access snippets via the Help menu, or by right-clicking on network operators, or r-clicking on OP Create dialog items.

**[SOP](<./SOP.md> "SOP")** or **[Surface Operator](<./SOP.md> "SOP")** : A [Operator Family](<./Operator_Family.md> "Operator Family") that reads, creates and modifies 3D points, polygons, lines, particles, surfaces, spheres and meatballs. Particles and point clouds are now done primarily on the GPU using TOPs.

**[Status Bar](<./Status_Bar.md> "Status Bar")** : The line of text at the top of the TouchDesigner window which displays messages from TouchDesigner when certain events succeed or fail.

**[Storage](<./Storage.md> "Storage")** : Storage is a python dictionary in each operator, where users can store and fetch extra data.

**[Synth](<./Synth.md> "Synth")** : Synths is a legacy term for the artworks created by TouchDesigner. A Synth consists of the [.toe](<./.md> ".toe") file created by TouchDesigner and all the associates media files that are needed to run an artwork in [TouchPlayer](<./TouchPlayer.md> "TouchPlayer") or, in [Perform Mode](<./Perform_Mode.md> "Perform Mode"), [TouchDesigner](<./TouchDesigner.md> "TouchDesigner").

**[Table DAT](<./Table_DAT.md> "Table DAT")** : A form of [DATs](<./DAT.md> "DAT") (Data Operators) that is structured as rows and columns of text strings.

**[Tag](<./Tag.md> "Tag")** : Each operator can have a set of text strings that are its "tags". You can set them and search for them within TouchDesigner.

**[Textport](<./Textport.md> "Textport")** : The dialog box in which commands and scripts can typed in manually. Output to the textport includes script errors and messages from`print()`and`debug()`calls in python code. You can also edit DATs in the textport.

**[Time Slice](<./Time_Slicing.md> "Time Slicing")** or **[Time Slicing](<./Time_Slicing.md> "Time Slicing")** : A Time Slice is the time from the last cook frame to the current cook frame. In CHOPs it is the set of short channels that contain the CHOP channels' samples between the last and the current cook frame.

**[Timeline](<./Timeline.md> "Timeline")** : The panel at the bottom of TouchDesigner, it controls the current global looping [Time](<./Time_COMP.md> "Time COMP") your TouchDesigner project, or of just one component.

**[TOP](<./SOP.md> "SOP")** or **[Texture Operator](<./SOP.md> "SOP")** : An [Operator Family](<./Operator_Family.md> "Operator Family") that creates, composites and modifies images, and reads/writes images and movies to/from files and the network. TOPs run on the graphics card's GPU.

**[TOP](<./TOP.md> "TOP")** or **[Texture Operator](<./TOP.md> "TOP")** : An [Operator Family](<./Operator_Family.md> "Operator Family") that creates, composites and modifies images, and reads/writes images and movies to/from files and the network. TOPs run on the graphics card's GPU.

**[Tscript](<./Tscript.md> "Tscript")** : TouchDesigner's original built-in Command scripting language prior to [Python](<./Python.md> "Python").

**[Tuplet](<./Tuplet.md> "Tuplet")** : A tuplet is the set of parameters that appear on one line of the parameter dialog. Tuplets occupy a [page](<./Page_Class.md> "Page Class") of parameters.

**[Unicode](<./Unicode.md> "Unicode")** : Unicode text is fully supported in TouchDesigner. Unicode can be typed into parameters, DATs, Python scripts etc. Unicode encoded text files can be loaded into DATs. File paths can include any unicode character that is legal for a file path.

**[Vertex](<./Vertex.md> "Vertex")** or **[Vertices](<./Vertex.md> "Vertex")** : A sequence of vertices form a [Polygon](<./Polygon.md> "Polygon") in a [SOP](<./SOP.md> "SOP"). Each vertex is an integer index into the [Point List](<./Point_List.md> "Point List"), and each [Point](<./Point.md> "Point") holds an XYZ position and attributes like Normals and Texture Coordinates.

**[VFS](<./Virtual_File_System.md> "Virtual File System")** or **[Virtual File System](<./Virtual_File_System.md> "Virtual File System")** : Lets you embed files inside a`[.tox](<./.md> ".tox")`or`[.toe](<./.md> ".toe")`file. Operators like the Movie File In TOP that read regular files can also read the embedded VFS files using a`vfs:`syntax.

**[Viewer](<./Viewer.md> "Viewer")** : The viewer of a node can be (1) the interior of a node (the [Node Viewer](<./Node_Viewer.md> "Node Viewer")), (2) a floating window (RMB->View... on node), or (3) a [Pane](<./Pane.md> "Pane") that graphically shows the results of an operator.

**[Viewer Active](<./Viewer_Active.md> "Viewer Active")** : A state of a node where you can operate the contents of its viewer (the + at botton-right of any node), like operating the gadgets of a panel in a node viewer, or the 3D data in the viewer of a Geometry component. With Viewer Active off you can select, move and delete nodes by clicking/dragging on them, even if the viewer is visible.

**[Viewer flag](<./Node_Viewer.md> "Node Viewer")** : Each node has a viewer flag that turns on/off the node's viewer in the [Node Viewer](<./Node_Viewer.md> "Node Viewer").

**[Widgets](<./Widgets.md> "Widgets")** : Widgets is a diverse collection of components located in the Palette, designed for building user interfaces.

**[Window](<./Window.md> "Window")** : A Window in TouchDesigner is a window in Microsoft Windows or macOS that contains either (1) the TouchDesigner editing interface that exists in [Designer Mode](<./Designer_Mode.md> "Designer Mode"), or (2) a user-created [Panel](<./Panel.md> "Panel") inside a [Window Component](<./Window_COMP.md> "Window COMP"). The user-created windows can span [Multiple Monitors](<./Multiple_Monitors.md> "Multiple Monitors") borderless, or be floating windows with borders, or popups.

**[Wire](<./Wire.md> "Wire")** : The connection of an output of one node to the input of another node in a network. In contrast, see [Link](<./Link.md> "Link").

**[WYSIWID](<./Network.md> "Network")** : TouchDesigner is WYSIWID \- What You See Is What It's Doing. All nodes can have interactive viewers of their data.

Now you are fluent in Touchese. 

To add: Sequential Block (or is it "Sequence Blocks" on the Sequential Parameters page), Attribute Class, Normal, Tangent, POP, Attribute Array, Input Block, Legacy mode for parameters or operators, Dimension, Swizzling, 3D Texture, Built-in Attribute Edit: [Attribute](<./Attribute.md> "Attribute"),
