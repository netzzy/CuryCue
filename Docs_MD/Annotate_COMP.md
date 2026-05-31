# Annotate COMP

## 

Summary

Annotates are displayed in the Network Editor as colored rectangles containing user-authored text and graphics. It is based on the Annotate COMP and allows you to document your networks with useful information like comments and node grouping. 

There are three built-in forms of the Annotate COMP: [Comments, Network Boxes, and Annotates](<./Network_Utilities-_Comments,_Network_Boxes,_Annotates.md> "Network Utilities: Comments, Network Boxes, Annotates") that can be easily created: 
* **[Comments](<./Network_Utilities-_Comments,_Network_Boxes,_Annotates.md> "Network Utilities: Comments, Network Boxes, Annotates")** are simple, text-only post-it notes. They can be created via the network RMB menu or with the shortcut Shift-C
  * **[Network Boxes](<./Network_Utilities-_Comments,_Network_Boxes,_Annotates.md> "Network Utilities: Comments, Network Boxes, Annotates")** group nodes together for labeling/dragging. They can be created via the network RMB menu or with the shortcut Shift-B
  * **[Annotates](<#Default_Setup>)** (Default Setup) do all of the above and incorporate a powerful node-viewing feature. They can be created via the network RMB menu, with the shortcut Shift-A, by holding Alt and left-dragging in the network, or by selecting Annotate from the COMP family in the [OP Create Dialog](<./OP_Create_Dialog.md> "OP Create Dialog").


[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[annotateCOMP_Class](<./AnnotateCOMP_Class.md> "AnnotateCOMP Class")

## 

Default Setup

The default setup of Annotate COMPs is a full-featured comment, network box, and node viewer, designed to be a flexible network organization and documentation tool. The following features are built using internal nodes and an extension and are not inherent parts of the Annotate COMP itself. 

The **lock icon** in the top-right of the box locks and unlocks text editing in the Annotate. In a locked Annotate, you cannot edit text and clicking on the body area clicks through to the network below. Annotates also have a **RMB menu** for quick access to many features. It is always accessible through the title bar, and accessible through the body when the Annotate is unlocked. 

You can **size** Annotates by dragging the edges and **move** them by dragging the title bar. In Comment mode, which has no title bar, you can drag the Annotate by the text body. When the **Enclose OPs** feature is on, dragging an Annotate will **drag all enclosed nodes** (including other Annotates) with it. To drag an annotate without dragging its contents, you can hold down Alt while dragging. 

Annotates have powerful built-in **Operator Viewer features** , including positioning and interaction, which can be controlled using [Parameters - OP Viewer Page](<#Parameters_-_OP_Viewer_Page>). For basic **text features** see [Parameters - Text Page](<#Parameters_-_Text_Page>). For deeper **text editing and color features** including limiting text width, wrapping, and more, see [Parameters - Settings Page](<#Parameters_-_Settings_Page>). 

Annotates are **layered in the network** so that smaller boxes are in front of larger boxes, but you have more control with the Depth Layer parameter. Annotates are positioned behind the grid by default, but you can put them in front of the grid, or even on top of the nodes tiles. For example, put an image with transparency in the Viewer OP and turn Back Color Alpha to 0, then set Layer Zone to be Above Nodes. 

Because the Enter shortcut and zoom-to-enter are disabled in Annotates, to **get inside an Annotate**, use one of the following methods: 
1. Box-pick an Annotate, then right-click on the network and select "Jump Down".
  2. Find the Annotate via the path bar at the top of the network pane.
  3. Box-pick an Annotate, right-click on the "i" icon on the Parameter Dialog and select Enter Annotation from the node menu.


You can switch between the three built-in Annotate modes by using the Mode parameter of the Annotate COMP or the **Mode** menu in the right-click menu. The Annotate COMP's .utility flag controls whether or not the Annotation operators are included in OP searches etc. This flag is easily accessible via the **Utility** parameter descrbed below. 

### 

Parameters - Text Page

Basic text features including editable/searchable parameters holding the Annotate's text. 

Title Text`Titletext`\- Text in the title bar. 

Title Height`Titleheight`\- Height of the title bar. Title font height adjusts automatically to fill. 

Title Align`Titlealign`\- ⊞ \- Alignment of title text. 
* Left`left`-
* Center`center`-
* Right`right`-


Body Text`Bodytext`\- Text in the body area. Use an expression for newlines etc. 

Body Font Size`Bodyfontsize`\- Size of text in the body area. 

Limit Body Text Width`Bodylimitwidth`\- Limit the width of the text area. 

Max Body Text Width`Bodymaxwidth`\- Width limit that will cause wraparound or cut-off. Measured in Panel units. 

### 

Parameters - Settings Page

More advanced text control and color parameters. 

Mode`Mode`\- ⊞ \- Switch between Comment, Network Box, and Annotate Modes. For more, see [Network Utilities: Comments, Network Boxes, Annotates](<./Network_Utilities-_Comments,_Network_Boxes,_Annotates.md> "Network Utilities: Comments, Network Boxes, Annotates"). 
* Comment`comment`\- Simple text only, no title or OP Viewer.
* Network Box`networkbox`\- Use this to group/move/label a set of nodes only.
  * Annotate`annotate`\- All features available.


Smart Quote`Smartquote`\- Converts quotes, ellipsis, and dashes to more typographically nice unicode versions. 

Body Word Wrap`Bodywordwrap`\- Wrap body text when it extends past right bound. 

Back Color`Backcolor`\- ⊞ \- Background color base. 
* Back Color`Backcolorr`-
* Back Color`Backcolorg`-
* Back Color`Backcolorb`-


Back Color Alpha`Backcoloralpha`\- Back color alpha. 

Annotate Opacity`Opacity`\- Opacity of the entire Annotate. 

### 

Parameters - OP Viewer Page

Controls for the embedded Operator viewer. 

Viewer Display`Opviewerdisplay`\- Turn the visibility of the viewer specified in the OP parameter below on or off. 

OP`Opviewer`\- The operator whose viewer is displayed in the Annotate. 

OP Viewer Interactive`Opviewerinteractive`\- Allow interaction with the OP viewer. 

Size/Aspect Override`Opvieweroversize`\- ⊞ \- Use the Size/Aspect Override to control viewer's size in the background. 
* Natural`natural`-
* Specify`specify`-
* Auto-fit`autofit`-


Size/Aspect`Opviewersize`\- ⊞ \- Diplay viewer as-if it were being displayed at this resolution. This is particularly useful for zooming into operators that don't have a built-in resolution, like CHOPs, SOPs, and DATs. 
* Size/Aspect`Opviewersizew`-
* Size/Aspect`Opviewersizeh`-


Scale`Opviewerscale`\- Scale the viewer by this factor. 

Justify X`Opviewerjustifyx`\- Move the border of the viewer towards left edge of Annotate when negative or towards right edge when positive. 

Justify Y`Opviewerjustifyy`\- Move the border of the viewer towards bottom edge of Annotate when negative or towards top edge when positive. 

Cover Body and Title`Opviewerfillbodytitle`\- When True, allow viewer to display in the Annotate title area as well as body. 

OP Viewer Zoom`Opviewerzoom`\- Zoom the viewer by this scale factor without increasing the size of its display area in the Annotate. 

OP Viewer Offset`Opvieweroffset`\- ⊞ \- Offsets the displayed area within the viewer. Combined with OP Viewer Zoom, this lets you display a specific area of a viewer, such as a CHOP channel or table cell. 
* OP Viewer Offset`Opvieweroffsetx`-
* OP Viewer Offset`Opvieweroffsety`-


Fill Alpha`Opviewerfillalpha`\- Alpha value of the background area in the OP Viewer. 

### 

Parameters - About Page

Version`Version`\- Annotate COMP default setup version. 

Help`Help`\- Click to open this page. 

### 

Annotate Extension

#### Members`BodyColor`→`[R, G, B, A]`**(Read Only)** : 

> RGBA of color used for body.`BodyFontColor`→`[R, G, B, A]`**(Read Only)** : 

> RGBA of font color used in body.`BodySelectColor`→`[R, G, B, A]`**(Read Only)** : 

> RGBA of selection color for body text.`BodyText`→ : 

> Text of body.`Color`→`[R, G, B]`**(Read Only)** : 

> RGB of base color set in Back Color parameter`EncloseOPs`→`bool`: 

> If True, Annotate encloses operators in its network area for movement and other features`TitleColor`→`[R, G, B, A]`**(Read Only)** : 

> RGBA background color of title area`TitleFontColor`→`[R, G, B, A]`**(Read Only)** : 

> RGBA font color of title area`TitleSelectColor`→`[R, G, B, A]`**(Read Only)** : 

> RGBA of selection color for title text`TitleText`→ : 

> Text in title area

#### Methods`OnCreate(Mode)`: 

> Called on initial creation of Annotate. Mode can be "annotate", "comment", or "networkbox"

## 

Parameters - Annotate Page

Operator Viewer`opviewer`\- The operator whose view is displayed in the Annotate area. This defines what the entire Annotate looks like and is not to be confused with the OP parameter in the OP Viewer page, which is an integrated viewer _within_ the annotate. 

Enable Interaction`enable`\- When False, disables _all_ interaction with the Annotate and passes any clicks through to the network below. 

Enclose Operators`encloseops`\- When True, other operators in the Annotate's area will move with it when it is moved. 

Utility`utility`\- Sets whether or not this is a [Utility node](<./Network_Utilities-_Comments,_Network_Boxes,_Annotates.htm#Network_Utility_Node_Details> "Network Utilities: Comments, Network Boxes, Annotates"). This controls whether or not the operator is findable in searches, etc. 

Include in Order`includeinorder`\- Include this Annotate in the Order of annotateCOMPs in this network. 

Order`order`\- Order number of this annotateCOMP 

Layer Zone`layerzone`\- ⊞ \- Where this annotateCOMP is layered with regards to other items in the network. 
* Below Grid`belowgrid`\- Behind everything, including the grid.
* Between Grid and Nodes`betweengridnodes`\- Behind nodes but in front of grid
* Above Nodes`abovenodes`\- Above everything, including grid and nodes.


Depth Layer`layer`\- Last ditch layering index. AnnotateCOMPs in the same zone will always attempt to display smaller annotateCOMPs they enclose on top. 

## 

Parameters - Extensions Page

The Extensions parameter page sets the component's python extensions. Please see [extensions](<./Extensions.md> "Extensions") for more information. 

Re-Init Extensions`reinitextensions`\- Recompile all extension objects. Normally extension objects are compiled only when they are referenced and their definitions have changed. 

Init Extensions On Start`initextonstart`\- Perform a Re-Init automatically when TouchDEsigner Starts 

Extension`ext`\- Sequence of info for creating extensions on this component 

Object`ext0object`\- A number of class instances that can be attached to the component. 

Name`ext0name`\- Optional name to search by, instead of the instance class name. 

Promote`ext0promote`\- Controls whether or not the extensions are visible directly at the component level, or must be accessed through the`.ext`member. Example:`n.Somefunction`vs`n.ext.Somefunction`## 

Parameters - Common Page

The Common parameter page sets the component's [node viewer](<./Node_Viewer.md> "Node Viewer") and [clone](<./Clone.md> "Clone") relationships. 

Parent Shortcut`parentshortcut`\- Specifies a name you can use anywhere inside the component as the path to that component. See [Parent Shortcut](<./Parent_Shortcut.md> "Parent Shortcut"). 

Global OP Shortcut`opshortcut`\- Specifies a name you can use anywhere at all as the path to that component. See [Global OP Shortcut](<./Global_OP_Shortcut.md> "Global OP Shortcut"). 

Internal OP`iop`\- Sequence header for internal operators. 

Shortcut`iop0shortcut`\- Specifies a name you can use anywhere inside the component as a path to "Internal OP" below. See [Internal Operators](<./Internal_Operators.md> "Internal Operators"). 

OP`iop0op`\- The path to the Internal OP inside this component. See [Internal Operators](<./Internal_Operators.md> "Internal Operators"). 

Operator Viewer`opviewer`\- Select which operator's node viewer to use when the Node View parameter above is set to Operator Viewer. 

Enable Cloning`enablecloning`\- Control if the OP should be actively cloneing. Turning this off causes this node to stop cloning it's 'Clone Master'. 

Enable Cloning Pulse`enablecloningpulse`\- Instantaneously clone the contents. 

Clone Master`clone`\- Path to a component used as the Master [Clone](<./Clone.md> "Clone"). 

Load on Demand`loadondemand`\- Loads the component into memory only when required. Good to use for components that are not always used in the project. 

Enable External .tox`enableexternaltox`\- When on (default), the external .tox file will be loaded when the .toe starts and the contents of the COMP will match that of the external .tox. This can be turned off to avoid loading from the referenced external .tox on startup if desired (the contents of the COMP are instead loaded from the .toe file). Useful if you wish to have a COMP reference an external .tox but not always load from it unless you specifically push the Re-Init Network parameter button. 

Enable External .tox Pulse`enableexternaltoxpulse`\- This button will re-load from the external`.tox`file (if present). 

External .tox Path`externaltox`\- Path to a`.tox`file on disk which will source the component's contents upon start of a`.toe`. This allows for components to contain networks that can be updated independently. If the`.tox`file can not be found, whatever the`.toe`file was saved with will be loaded. 

Reload Custom Parameters`reloadcustom`\- When this checkbox is enabled, the values of the component's [Custom Parameters](<./Custom_Parameters.md> "Custom Parameters") are reloaded when the [.tox](<./.md> ".tox") is reloaded. This only affects top-level parameters on the component, all parameters on nodes inside the component are always reloaded with the [.tox](<./.md> ".tox"). 

Reload Built-In Parameters`reloadbuiltin`\- When this checkbox is enabled, the values of the component's built-in parameters are reloaded when the [.tox](<./.md> ".tox") is reloaded. This only affects top-level parameters on the component, all parameters on nodes inside the component are always reloaded with the [.tox](<./.md> ".tox"). 

Save Backup of External`savebackup`\- When this checkbox is enabled, a backup copy of the component specified by the External`.tox`parameter is saved in the`.toe`file. This backup copy will be used if the External`.tox`can not be found. This may happen if the`.tox`was renamed, deleted, or the`.toe`file is running on another computer that is missing component media. 

Sub-Component to Load`subcompname`\- When loading from an External`.tox`file, this option allows you to reach into the`.tox`and pull out a COMP and make that the top-level COMP, ignoring everything else in the file (except for the contents of that COMP). For example if a`.tox`file named`project1.tox`contains`project1/geo1`, putting`geo1`as the Sub-Component to Load, will result in`geo1`being loaded in place of the current COMP. If this parameter is blank, it just loads the`.tox`file normally using the top level COMP in the file. 

Relative File Path Behavior`relpath`\- ⊞ \- Set whether the child file paths within this COMP are relative to the .toe itself or the .tox, or inherit from parent. 
* Use Parent's Behavior`inherit`\- Inherit setting from parent.
* Relative to Project File (.toe)`project`\- The path, when specified as a relative path, will be relative to the .toe file.
* Relative to External COMP File (.tox)`externaltox`\- The path, when specified as a relative path, will be relative to the .tox file. When no external COMP file is specified, or when Enable External .tox is not toggled on, this doesn't have any impact.

## 

Info CHOP Channels

Extra Information for the Annotate COMP can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). __

### 

Common COMP Info Channels
* num_children \- Number of children in this component.

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


  
TouchDesigner Build: Latest\nwikieditorwikieditorwikieditor2023.112802022.24140before 2022.24140

COMPs   
---  
[Actor ](<./Actor_COMP.md> "Actor COMP")• [Ambient Light ](<./Ambient_Light_COMP.md> "Ambient Light COMP")• [Animation ](<./Animation_COMP.md> "Animation COMP")• Annotate • [Base ](<./Base_COMP.md> "Base COMP")• [Blend ](<./Blend_COMP.md> "Blend COMP")• [Bone ](<./Bone_COMP.md> "Bone COMP")• [Bullet Solver ](<./Bullet_Solver_COMP.md> "Bullet Solver COMP")• [Button ](<./Button_COMP.md> "Button COMP")• [Camera Blend ](<./Camera_Blend_COMP.md> "Camera Blend COMP")• [Camera ](<./Camera_COMP.md> "Camera COMP")• [MediaWiki:Common.js ](<./MediaWiki-Common.md> "MediaWiki:Common.js")• [COMP ](<./COMP.md> "COMP")• [Component ](<./Component.md> "Component")• [Constraint ](<./Constraint_COMP.md> "Constraint COMP")• [Container ](<./Container_COMP.md> "Container COMP")• [Engine ](<./Engine_COMP.md> "Engine COMP")• [Environment Light ](<./Environment_Light_COMP.md> "Environment Light COMP")• [FBX ](<./FBX_COMP.md> "FBX COMP")• [Field ](<./Field_COMP.md> "Field COMP")• [Force ](<./Force_COMP.md> "Force COMP")• [Geo Text ](<./Geo_Text_COMP.md> "Geo Text COMP")• [Geometry ](<./Geometry_COMP.md> "Geometry COMP")• [GLSL ](<./GLSL_COMP.md> "GLSL COMP")• [Handle ](<./Handle_COMP.md> "Handle COMP")• [Impulse Force ](<./Impulse_Force_COMP.md> "Impulse Force COMP")• [Light ](<./Light_COMP.md> "Light COMP")• [List ](<./List_COMP.md> "List COMP")• [Null ](<./Null_COMP.md> "Null COMP")• [NVIDIA Flex Solver ](<./NVIDIA_Flex_Solver_COMP.md> "NVIDIA Flex Solver COMP")• [NVIDIA Flow Emitter ](<./NVIDIA_Flow_Emitter_COMP.md> "NVIDIA Flow Emitter COMP")• [OP Viewer ](<./OP_Viewer_COMP.md> "OP Viewer COMP")• [Parameter ](<./Parameter_COMP.md> "Parameter COMP")• [Replicator ](<./Replicator_COMP.md> "Replicator COMP")• [Select ](<./Select_COMP.md> "Select COMP")• [Shared Mem In ](<./Shared_Mem_In_COMP.md> "Shared Mem In COMP")• [Shared Mem Out ](<./Shared_Mem_Out_COMP.md> "Shared Mem Out COMP")• [Slider ](<./Slider_COMP.md> "Slider COMP")• [Table ](<./Table_COMP.md> "Table COMP")• [Text ](<./Text_COMP.md> "Text COMP")• [Time ](<./Time_COMP.md> "Time COMP")• [USD ](<./USD_COMP.md> "USD COMP")• [Widget ](<./Widget_COMP.md> "Widget COMP")• [Window ](<./Window_COMP.md> "Window COMP")
