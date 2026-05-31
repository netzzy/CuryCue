# Constraint COMP

##   
  
Summary

A Constraint COMP is used to restrict the movement of the bodies in a set of [Actor COMPs](<./Actor_COMP.md> "Actor COMP"). Currently this can be done in a few ways: point to point, hinge or slider. Constraints can either be applied on a single body or between two bodies. Constraints can be used to create connectivity between bodies, or to create bodies that can move but need to have that movement restricted in some way. Some examples of constraints in the real world: a train, a door, an arm. 

If a point to point constraint is applied to a single body, then that body will be restricted to 3 degrees of freedom (DOF). It will still have all 3 degrees of freedom for rotation (ie. All 3 axes), but the 3 degrees of freedom for translation will all be constrained. If a point to point constraint is applied between two bodies, then they will both be similarly constrained to 3 DOF. However, they will be able to move (translate) along all 3 axes but they will do it connected to each other at their pivot points. By using this constraint method, a chain of bodies can be created. For instance, point to point constraints can be used to simulate train cars connected to each other. 

If a hinge constraint is applied to a single body, then that body will be restricted to 1 DOF relative to the other body. It will only be able to rotate around 1 axis, and that axis is defined using the Axis parameter on the Constraint COMP. Much like the point to point constraint, the hinge also as a pivot point around which it will rotate. If a hinge constraint is applied between two bodies, then they will both be able to move with 3 DOF but they will do it connected to each other at their pivot points. However, they will still only be able to rotate around their respective axis. The simplest example of a hinge constraint is a door. 

If a slider constraint is applied to a single body, then that body's translation/rotation will be constrained to just that axis. In other words, the body can only move along that axis (either direction) and can only rotate along that axis (either direction). 

See also: [Bullet Dynamics](<./Bullet_Dynamics.md> "Bullet Dynamics"), [Bullet Solver COMP](<./Bullet_Solver_COMP.md> "Bullet Solver COMP"), [Actor COMP](<./Actor_COMP.md> "Actor COMP"), [Force COMP](<./Force_COMP.md> "Force COMP"), [Impulse Force COMP](<./Impulse_Force_COMP.md> "Impulse Force COMP"), [Bullet Solver CHOP](<./Bullet_Solver_CHOP.md> "Bullet Solver CHOP"). 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[constraintCOMP_Class](</ConstraintCOMP_Class> "ConstraintCOMP Class")

## 

Parameters - Constraint Page

Active`active`\- Toggle the constraint on/off in the simulation. 

Type`type`\- ⊞ \- The type of constraint to create: point to point, hinge, or slider. 
* Point To Point`p2p`-
* Hinge`hinge`-
* Slider`slider`-


Body to Body`bodytobody`\- Toggle body to body mode on/off. Body to body mode creates a constraint between two bodies (Actor 1 Bodies and Actor 2 Bodies). When toggled off it will create constrain bodies individually. If Actor 1 Bodies and Actor 2 Bodies contain the same number of referenced bodies, then this mode will create a constraint between each respective pair. For instance, if Actor 1 Bodies contains the string "0 1 2", and Actor 2 Bodies contains the string "3 4 5" then this will create 3 constraints: 0->3, 1->4, 2->5\. It is a 1 to 1 relationship between these two parameters. However, if Actor 1 Bodies has more bodies than Actor 2 Bodies, then the remaining "unmatched" bodies of Actor 1 Bodies will instead be individually constrained. For instance, if Actor 1 Bodies contains the string "0 1 2" and Actor 2 Bodies contains the string "3 4", then two constraints will be created between bodies: 0->3, 1->4\. Body 2 will be constrained individually. If Actor 2 Bodies contains more bodies than Actor 1 Bodies, then any unmatched bodies in Actor 2 Bodies will simply be disregarded (no constraint created for them). 

Collisions between Bodies`collisions`\- Turns on/off collisions between the body to body constraints. 

Display Constraint`dispcom`\- Turns on/off the display of the constraint guide in the viewer. 

Actor COMP`actor1`\- A reference to an Actor COMP. This specifies the Actor COMP of which you want to constrain some bodies. 

Actor Bodies`bodies1`\- A list (regular expression) of the IDs of the bodies in actor1 to constrain. If an Actor COMP contains N bodies, then body IDs will go from 0 to N-1 for that Actor COMP. The number of bodies can be verified using the [Bullet Solver CHOP](<./Bullet_Solver_CHOP.md> "Bullet Solver CHOP"). 

Pivot`pivot1`\- ⊞ \- The pivot point for the constraint. 
* X`pivot1x`-
* Y`pivot1y`-
* Z`pivot1z`-


Hinge Axis`axis1`\- ⊞ \- The axis around which to create the hinge. Each value is typically a number between 0 and 1. For example, to spin around the Z axis set to 0, 0, 1. 
* X`axis1x`-
* Y`axis1y`-
* Z`axis1z`-


Slider Rotation`sliderrot1`\- ⊞ \- The rotation of the slider constraint axis. By default the slider constraint is applied on the X axis. 
* X`sliderrot1x`-
* Y`sliderrot1y`-
* Z`sliderrot1z`-


Actor COMP`actor2`\- A reference to an Actor COMP. This specifies the Actor COMP of which you want to constrain some bodies. This Actor COMP is only used when body to body mode is toggled on. 

Actor Bodies`bodies2`\- A list (regular expression) of the IDs of the bodies in actor2 to constrain. If an Actor COMP contains N bodies, then body IDs will go from 0 to N-1 for that Actor COMP. The number of bodies can be verified using the Bullet Solver CHOP. 

Pivot`pivot2`\- ⊞ \- The pivot point for the constraint. 
* X`pivot2x`-
* Y`pivot2y`-
* Z`pivot2z`-


Hinge Axis`axis2`\- ⊞ \- The axis around which to create the hinge. Each value is typically a number between 0 and 1. For example, to spin around the Z axis set to 0, 0, 1. 
* X`axis2x`-
* Y`axis2y`-
* Z`axis2z`-


Slider Rotation`sliderrot2`\- ⊞ \- The rotation of the slider constraint axis. By default the slider constraint is applied on the X axis. 
* X`sliderrot2x`-
* Y`sliderrot2y`-
* Z`sliderrot2z`-

## 

Parameters - Limits Page

Enable Limits`enablelimits`\- Enables limits on the constraint. Without constraints, the bodies will be able to rotate a full 360 degrees, or translate any distance. 

Lower Linear Limit`lowerlinlim`\- The lower limit for translation of the body along the constraint. Only used with slider constraints. 

Upper Linear Limit`upperlinlim`\- The upper limit for translation of the body along the constraint. Only used with slider constraints. 

Lower Angular Limit`loweranglim`\- The lower limit for rotation of the body around its axis. Used with slider constraints or hinge constraints. 

Upper Angular Limit`upperanglim`\- The upper limit for rotation of the body around its axis. Used with slider constraints or hinge constraints. 

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

## 

Info CHOP Channels

Extra Information for the Constraint COMP can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). __

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


  
TouchDesigner Build: Latest\nwikieditor2022.241402021.100002019.146502018.28070

COMPs   
---  
[Actor ](<./Actor_COMP.md> "Actor COMP")• [Ambient Light ](<./Ambient_Light_COMP.md> "Ambient Light COMP")• [Animation ](<./Animation_COMP.md> "Animation COMP")• [Annotate ](<./Annotate_COMP.md> "Annotate COMP")• [Base ](<./Base_COMP.md> "Base COMP")• [Blend ](<./Blend_COMP.md> "Blend COMP")• [Bone ](<./Bone_COMP.md> "Bone COMP")• [Bullet Solver ](<./Bullet_Solver_COMP.md> "Bullet Solver COMP")• [Button ](<./Button_COMP.md> "Button COMP")• [Camera Blend ](<./Camera_Blend_COMP.md> "Camera Blend COMP")• [Camera ](<./Camera_COMP.md> "Camera COMP")• [MediaWiki:Common.js ](<./MediaWiki-Common.md> "MediaWiki:Common.js")• [COMP ](<./COMP.md> "COMP")• [Component ](<./Component.md> "Component")• Constraint • [Container ](<./Container_COMP.md> "Container COMP")• [Engine ](<./Engine_COMP.md> "Engine COMP")• [Environment Light ](<./Environment_Light_COMP.md> "Environment Light COMP")• [FBX ](<./FBX_COMP.md> "FBX COMP")• [Field ](<./Field_COMP.md> "Field COMP")• [Force ](<./Force_COMP.md> "Force COMP")• [Geo Text ](<./Geo_Text_COMP.md> "Geo Text COMP")• [Geometry ](<./Geometry_COMP.md> "Geometry COMP")• [GLSL ](<./GLSL_COMP.md> "GLSL COMP")• [Handle ](<./Handle_COMP.md> "Handle COMP")• [Impulse Force ](<./Impulse_Force_COMP.md> "Impulse Force COMP")• [Light ](<./Light_COMP.md> "Light COMP")• [List ](<./List_COMP.md> "List COMP")• [Null ](<./Null_COMP.md> "Null COMP")• [NVIDIA Flex Solver ](<./NVIDIA_Flex_Solver_COMP.md> "NVIDIA Flex Solver COMP")• [NVIDIA Flow Emitter ](<./NVIDIA_Flow_Emitter_COMP.md> "NVIDIA Flow Emitter COMP")• [OP Viewer ](<./OP_Viewer_COMP.md> "OP Viewer COMP")• [Parameter ](<./Parameter_COMP.md> "Parameter COMP")• [Replicator ](<./Replicator_COMP.md> "Replicator COMP")• [Select ](<./Select_COMP.md> "Select COMP")• [Shared Mem In ](<./Shared_Mem_In_COMP.md> "Shared Mem In COMP")• [Shared Mem Out ](<./Shared_Mem_Out_COMP.md> "Shared Mem Out COMP")• [Slider ](<./Slider_COMP.md> "Slider COMP")• [Table ](<./Table_COMP.md> "Table COMP")• [Text ](<./Text_COMP.md> "Text COMP")• [Time ](<./Time_COMP.md> "Time COMP")• [USD ](<./USD_COMP.md> "USD COMP")• [Widget ](<./Widget_COMP.md> "Widget COMP")• [Window ](<./Window_COMP.md> "Window COMP")
