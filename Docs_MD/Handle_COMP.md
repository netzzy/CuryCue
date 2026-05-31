# Handle COMP

##   
  
Summary

The Handle Component is a new IK tool designed for manipulating groups of bones. Whereas the previous IK tools only allowed for a single end-affector per bone chain, this new method allows for several end-affectors per bone. Furthermore, the bones need not be a chain. Any setup, including branches, are handled. 

One typical example is the use of motion capture data. In higher-end systems, you could have a cloud of marker positions and a skeleton to be driven by it. 

This Handle Component works in tandem with the [Handle CHOP](<./Handle_CHOP.md> "Handle CHOP"). The following setup is commonly used: Given a hierarchy of bones, attach one or more Handle Components to specific locations on each Bone Component. Assign each handle a target in space to follow. Create a Handle CHOP which collects this information and calculates the rotation channels for the bones. Export these values back to the bones. 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[handleCOMP_Class](<./HandleCOMP_Class.md> "HandleCOMP Class")

## 

Parameters - Handle Page

Target`target`\- Where the Handle will pull the bone towards (like an end-affector). 

Translate`t`\- ⊞ \- Displacement tx,ty,tz relative to the origin of the bone where the handle is anchored. 
* X`tx`-
* Y`ty`-
* Z`tz`-


Weight`weight`\- When multiple handles are attached to a bone, higher weighted handles draw closer to their target. 

Twist Only`twistonly`\- When enabled the handle only contributes the the z rotation of the bone, when disabled it points the bone (rx, ry, and rz). 

Falloff`falloff`\- This value affects how much parent bones are affected when the child bone is reaching a target. It affects the flexibility of the chain. 

Rotation Limits X`dorxlimit`\- These affects how much the bone is allowed to rotate with respect to its parent. 

Limit X`lrx`\- ⊞ \- Set the minimum and maximum rotation range in X axis. 

  *`lrxmin`-


  *`lrxmax`-


Rotation Limits Y`dorylimit`\- These affects how much the bone is allowed to rotate with respect to its parent. 

Limit Y`lry`\- ⊞ \- Set the minimum and maximum rotation range in Y axis. 

  *`lrymin`-


  *`lrymax`-


Rotation Limits Z`dorzlimit`\- These affects how much the bone is allowed to rotate with respect to its parent. 

Limit Z`lrz`\- ⊞ \- Set the minimum and maximum rotation range in Z axis. 

  *`lrzmin`-


  *`lrzmax`-

## 

Parameters - Render Page

The Display parameter page controls the component's [material](</index.php?title=Material&action=edit&redlink=1> "Material \(page does not exist\)") and [rendering](<./Rendering.md> "Rendering") settings. 

Material`material`\- Selects a [MAT](<./MAT.md> "MAT") to apply to the geometry inside. 

Render`render`\- Whether the Component's geometry is visible in the [Render TOP](<./Render_TOP.md> "Render TOP"). This parameter works in conjunction (logical AND) with the Component's [Render Flag](<./Render_Flag.md> "Render Flag"). 

Draw Priority`drawpriority`\- Determines the order in which the Components are drawn. Smaller values get drawn after larger values. The value is compared with other Components in the same parent Component, or if the Component is the top level one listed in the Render TOP's 'Geometry' parameter, then against other top-level Components listed there. This value is most often used to help with [Transparency](<./Transparency.md> "Transparency"). 

Pick Priority`pickpriority`\- When using a [Render Pick CHOP](<./Render_Pick_CHOP.md> "Render Pick CHOP") or a [Render Pick DAT](<./Render_Pick_DAT.md> "Render Pick DAT"), there is an option to have a 'Search Area'. If multiple objects are found within the search area, the pick priority can be used to select one object over another. A higher value will get picked over a lower value. This does not affect draw order, or objects that are drawn over each other on the same pixel. Only one will be visible for a pick per pixel. 

Wireframe Color`wcolor`\- ⊞ \- Use the R, G, and B fields to set the Component's color when displayed in wireframe shading mode. 
* Red`wcolorr`-
* Green`wcolorg`-
* Blue`wcolorb`-


Light Mask`lightmask`\- By default all lights used in the [Render TOP](<./Render_TOP.md> "Render TOP") will affect geometry renderer. This parameter can be used to specify a sub-set of lights to be used for this particular geometry. The lights must be listed in the [Render TOP](<./Render_TOP.md> "Render TOP") as well as this parameter to be used. 

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

Node View`nodeview`\- ⊞ \- Determines what is displayed in the node viewer, also known as the [Node Viewer](<./Node_Viewer.md> "Node Viewer"). Some options will not be available depending on the Component type ([Object Component](<./Object_Component.md> "Object Component"), [Panel Component](<./Panel_Component.md> "Panel Component"), Misc.) 
* Default Viewer`default`\- Displays the default viewer for the component type, a 3D Viewer for Object COMPS and a Control Panel Viewer for Panel COMPs.
* Operator Viewer`opviewer`\- Displays the node viewer from any operator specified in the Operator Viewer parameter below.


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


Parameter Color Space`parmcolorspace`\- ⊞ \- Controls how all color parameters on this node are interpreted. The color values as treated as being in the selected color space, and are converted to the Working [Color Space](<./Color_Space.md> "Color Space") before they are used as part of the node's operation. Note that this does not change the color space of the node itself, as that is always in the Working Color Space. 
* sRGB`srgb`\- [sRGB](<https://en.wikipedia.org/wiki/SRGB>) color space, with sRGB transfer function. Considered an SDR color space with respect to Reference White.
* sRGB - Linear`srgblinear`\- [sRGB](<https://en.wikipedia.org/wiki/SRGB>) color space, with linear transfer function. Considered an SDR color space with respect to Reference White.
* Rec.601 (NTSC)`rec601ntsc`\- [Rec.601](<https://en.wikipedia.org/wiki/Rec._601>) with NTSC primaries color space, with Rec.601 transfer function. Considered an SDR color space with respect to Reference White.
* Rec.709`rec709`\- [Rec.709](<https://en.wikipedia.org/wiki/Rec._709>) color space, with Rec.709 (same as Rec.2020) transfer function. Considered an SDR color space with respect to Reference White.
* Rec.2020`rec2020`\- [Rec.2020](<https://en.wikipedia.org/wiki/Rec._2020>) color space, with Rec.2020 (same as Rec.709) transfer function. Considered an HDR color space with respect to Reference White.
* DCI-P3`dcip3`\- [DCI-P3](<https://en.wikipedia.org/wiki/DCI-P3>) color space, with D65 white point and 2.6 gamma transfer function. Considered an HDR color space with respect to Reference White.
* DCI-P3 (D60)`dcip3d60`\- [DCI-P3 "D60 sim"](<https://en.wikipedia.org/wiki/DCI-P3>) color space, with D60 white point, and 2.6 gamma transfer function. Considered an HDR color space with respect to Reference White.
* Display-P3 (D65)`displayp3d65`\- [Display-P3](<https://en.wikipedia.org/wiki/DCI-P3>) color space, with D65 white point, and sRGB gamma transfer function. Considered an HDR color space with respect to Reference White.
* ACES2065-1`aces2065-1`\- [ACES 2065-1](<https://en.wikipedia.org/wiki/Academy_Color_Encoding_System>) (also known as ACES AP0) color space, with a linear gamma transfer function. Considered an HDR color space with respect to Reference White.
* ACEScg`acescg`\- [ACEScg](<https://en.wikipedia.org/wiki/Academy_Color_Encoding_System>) (also known as ACES AP1) color space, with a linear gamma transfer function. Considered an HDR color space with respect to Reference White.
* Passthrough`passthrough`\- When selected, the color values will be used as-is in the operation, without any modification or attempt to convert them into the Working Color Space.


Parameter Reference White`parmreferencewhite`\- ⊞ \- When converting a parameter color value to the Working Color Space, this controls how it should be treated with respect to [Reference White](<./Color_Space.htm#Reference_White> "Color Space"). If the Working Color Space is the same Reference White, then no adjustment is done. If they are different, then the Reference White level (brightness) of this color will be adjusted to the range expected by the Working Color Space. For example if the project is set to have a SDR Reference White of 120 nits, and the HDR Reference White is 80 nits, then a color of (1, 1, 1), which is 120 nits in the SDR color space, will be converted to be (1.5, 1.5, 1.5), which is 120 nits still in the HDR Working Color Space. 
* Default For Color Space`default`\- Will use either the SDR or the HDR Reference White, based on the color space selected.
* Use Parent Panel`useparent`\- Will use the Reference White that the parent panel has selected. If the top-level panel also has 'Use Parent' selected, then 'UI Reference White' will be used.
* Standard (SDR)`sdr`\- Will treat the Parameter Color Space as SDR for it's reference white value.
* High (HDR)`hdr`\- Will treat the Parameter Color Space as HDR for it's reference white value.
* UI`ui`\- Will treat the Parameter Color Space as UI for it's reference white value. This uses the 'UI Reference White Nits' value for it's brightness.

## 

Info CHOP Channels

Extra Information for the Handle COMP can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). __

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


  
TouchDesigner Build: Latest\nwikieditor2021.100002018.28070before 2018.28070

COMPs   
---  
[Actor ](<./Actor_COMP.md> "Actor COMP")• [Ambient Light ](<./Ambient_Light_COMP.md> "Ambient Light COMP")• [Animation ](<./Animation_COMP.md> "Animation COMP")• [Annotate ](<./Annotate_COMP.md> "Annotate COMP")• [Base ](<./Base_COMP.md> "Base COMP")• [Blend ](<./Blend_COMP.md> "Blend COMP")• [Bone ](<./Bone_COMP.md> "Bone COMP")• [Bullet Solver ](<./Bullet_Solver_COMP.md> "Bullet Solver COMP")• [Button ](<./Button_COMP.md> "Button COMP")• [Camera Blend ](<./Camera_Blend_COMP.md> "Camera Blend COMP")• [Camera ](<./Camera_COMP.md> "Camera COMP")• [MediaWiki:Common.js ](<./MediaWiki-Common.md> "MediaWiki:Common.js")• [COMP ](<./COMP.md> "COMP")• [Component ](<./Component.md> "Component")• [Constraint ](<./Constraint_COMP.md> "Constraint COMP")• [Container ](<./Container_COMP.md> "Container COMP")• [Engine ](<./Engine_COMP.md> "Engine COMP")• [Environment Light ](<./Environment_Light_COMP.md> "Environment Light COMP")• [FBX ](<./FBX_COMP.md> "FBX COMP")• [Field ](<./Field_COMP.md> "Field COMP")• [Force ](<./Force_COMP.md> "Force COMP")• [Geo Text ](<./Geo_Text_COMP.md> "Geo Text COMP")• [Geometry ](<./Geometry_COMP.md> "Geometry COMP")• [GLSL ](<./GLSL_COMP.md> "GLSL COMP")• Handle • [Impulse Force ](<./Impulse_Force_COMP.md> "Impulse Force COMP")• [Light ](<./Light_COMP.md> "Light COMP")• [List ](<./List_COMP.md> "List COMP")• [Null ](<./Null_COMP.md> "Null COMP")• [NVIDIA Flex Solver ](<./NVIDIA_Flex_Solver_COMP.md> "NVIDIA Flex Solver COMP")• [NVIDIA Flow Emitter ](<./NVIDIA_Flow_Emitter_COMP.md> "NVIDIA Flow Emitter COMP")• [OP Viewer ](<./OP_Viewer_COMP.md> "OP Viewer COMP")• [Parameter ](<./Parameter_COMP.md> "Parameter COMP")• [Replicator ](<./Replicator_COMP.md> "Replicator COMP")• [Select ](<./Select_COMP.md> "Select COMP")• [Shared Mem In ](<./Shared_Mem_In_COMP.md> "Shared Mem In COMP")• [Shared Mem Out ](<./Shared_Mem_Out_COMP.md> "Shared Mem Out COMP")• [Slider ](<./Slider_COMP.md> "Slider COMP")• [Table ](<./Table_COMP.md> "Table COMP")• [Text ](<./Text_COMP.md> "Text COMP")• [Time ](<./Time_COMP.md> "Time COMP")• [USD ](<./USD_COMP.md> "USD COMP")• [Widget ](<./Widget_COMP.md> "Widget COMP")• [Window ](<./Window_COMP.md> "Window COMP")
