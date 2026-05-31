# Force COMP

## 

Summary

Force COMPs are used to added forces to a physics solver's simulation. [Bullet](<./Bullet_Dynamics.md> "Bullet Dynamics") supports linear/rotational forces and impulse forces (see Force page) and [Flex](<./Flex.md> "Flex") supports force fields (see Force Field page). 

### 

Active Force

Active forces are enabled using the Active toggle parameter on the Force page. 

An active force will create a force in the simulation that is applied over time. An active force can either be applied globally by being referenced on the [Bullet Solver COMP](<./Bullet_Solver_COMP.md> "Bullet Solver COMP"), or it can be applied locally by being referenced on an individual [Actor COMP](<./Actor_COMP.md> "Actor COMP"). The active force applies its force each frame, and the force applied over 1 second is equivalent to an impulse force of the same value applied in a single frame. 

The units for the force and torque parameters are in Newtons (N), equivalent to kg*m/s^2. This means that if a force of 10N is applied to an actor with mass equal to 5kg and no initial velocity, then after 1 second the velocity of that actor will be 2m/s => 10N / 5kg * 1 sec = 2m/s. If all the parameters were the same, but instead it was an impulse force, then the velocity would still be 2m/s. However, the impulse force's velocity would change instantaneously and stop increasing (unless pulsed again) whereas with the active force the velocity will continue to increase after 1 second. 

The center of mass is assumed to be center of the bounding box of the mass. By default, if a body is not constrained and not colliding, the force will not cause the body to rotate, unless the Relative Position parameter is set to a non-zero value. If Relative Position is set to +1 in X and the force is +1 in Y, it will cause the body to rotate counter-clockwise around the Z-axis and translate in Y. 

If the Torque is set to +1 in Z, it will cause the body to only rotate counter-clockwise in the Z-axis (a positive Z rotation), and not translate. 

To apply force/torque to specific bodies use a Feedback CHOP (see [Bullet Solver COMP](<./Bullet_Solver_COMP.md> "Bullet Solver COMP") or [Actor COMP](<./Actor_COMP.md> "Actor COMP")) and **force[xyz]** and **torque[xyz]** channels. 

### 

Impulse Force

Impulse forces are applied through the Impulse Force pulse parameter. 

An impulse force pulse will create a force in the simulation that is applied for 1 frame. In the real world, impulse forces are forces applied over a very short duration, however in [Bullet](<./Bullet_Dynamics.md> "Bullet Dynamics") this is somewhat simplified, and they are instead applied instantly (for a single frame). Examples of impulse forces are kicking a ball or shooting a cannon. The velocities of the affected bodies are changed in an instant by the impulse force, and after that instant the force no longer has an effect unless applied again. 

The resulting velocity of the bodies after the impulse force is applied is the same as an active force with the same values if the active force is applied for exactly 1 second. For example, if 10N of impulse force is applied to a body with mass 5kg then the resulting velocity will be 10N / 5kg * 1sec = 2m/s. 

### 

Force Field

Force fields are enabled through the Active parameter on the Force Field page. 

Force fields are spherical with a radius defined through the Radius parameter. Positive strength pushes bodies outward and negative strength pulls bodies inward. 

  
See also: [Flex](<./Flex.md> "Flex"), [Bullet Dynamics](<./Bullet_Dynamics.md> "Bullet Dynamics"), [Bullet Solver COMP](<./Bullet_Solver_COMP.md> "Bullet Solver COMP"), [Actor COMP](<./Actor_COMP.md> "Actor COMP"), [Constraint COMP](<./Constraint_COMP.md> "Constraint COMP"), [Bullet Solver CHOP](<./Bullet_Solver_CHOP.md> "Bullet Solver CHOP"), [Nvidia Flex TOP](<./Nvidia_Flex_TOP.md> "Nvidia Flex TOP"), [Nvidia Flex Solver COMP](<./Nvidia_Flex_Solver_COMP.md> "Nvidia Flex Solver COMP"). 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[forceCOMP_Class](</ForceCOMP_Class> "ForceCOMP Class")

## 

Parameters - Force Page

Active`active`\- Toggle the active force on/off in the simulation 

Force`force`\- ⊞ \- The linear force in Newtons that will be applied. 
* X`forcex`-
* Y`forcey`-
* Z`forcez`-


Relative Position`relpos`\- ⊞ \- The position at which to apply the linear force, relative to the center of the body (Note: the physical center of the object, not the center of mass). Having a nonzero relative position will also cause the body to rotate due to added torque. 
* X`relposx`-
* Y`relposy`-
* Z`relposz`-


Torque`torque`\- ⊞ \- The rotational force in Newtons that will be applied. 
* X`torquex`-
* Y`torquey`-
* Z`torquez`-


Impulse Force`impulse`\- Applies an impulse force in the simulation for 1 frame with the above parameters. 

## 

Parameters - Force Field Page

Active`ffactive`\- Toggle the force field on/off in the simulation 

Strength`strength`\- The strength of the force field. Positive strength pushes bodies outward and negative strength pulls bodies inward. 

Radius`radius`\- The radius of the force field. 

Linear Falloff`falloff`\- Applies linear falloff to the strength of the force field based on the distance from the center. 

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

Extra Information for the Force COMP can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). __

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


  
TouchDesigner Build: Latest\nwikieditor2021.100002020.200002019.146502018.28070

COMPs   
---  
[Actor ](<./Actor_COMP.md> "Actor COMP")• [Ambient Light ](<./Ambient_Light_COMP.md> "Ambient Light COMP")• [Animation ](<./Animation_COMP.md> "Animation COMP")• [Annotate ](<./Annotate_COMP.md> "Annotate COMP")• [Base ](<./Base_COMP.md> "Base COMP")• [Blend ](<./Blend_COMP.md> "Blend COMP")• [Bone ](<./Bone_COMP.md> "Bone COMP")• [Bullet Solver ](<./Bullet_Solver_COMP.md> "Bullet Solver COMP")• [Button ](<./Button_COMP.md> "Button COMP")• [Camera Blend ](<./Camera_Blend_COMP.md> "Camera Blend COMP")• [Camera ](<./Camera_COMP.md> "Camera COMP")• [MediaWiki:Common.js ](<./MediaWiki-Common.md> "MediaWiki:Common.js")• [COMP ](<./COMP.md> "COMP")• [Component ](<./Component.md> "Component")• [Constraint ](<./Constraint_COMP.md> "Constraint COMP")• [Container ](<./Container_COMP.md> "Container COMP")• [Engine ](<./Engine_COMP.md> "Engine COMP")• [Environment Light ](<./Environment_Light_COMP.md> "Environment Light COMP")• [FBX ](<./FBX_COMP.md> "FBX COMP")• [Field ](<./Field_COMP.md> "Field COMP")• Force • [Geo Text ](<./Geo_Text_COMP.md> "Geo Text COMP")• [Geometry ](<./Geometry_COMP.md> "Geometry COMP")• [GLSL ](<./GLSL_COMP.md> "GLSL COMP")• [Handle ](<./Handle_COMP.md> "Handle COMP")• [Impulse Force ](<./Impulse_Force_COMP.md> "Impulse Force COMP")• [Light ](<./Light_COMP.md> "Light COMP")• [List ](<./List_COMP.md> "List COMP")• [Null ](<./Null_COMP.md> "Null COMP")• [NVIDIA Flex Solver ](<./NVIDIA_Flex_Solver_COMP.md> "NVIDIA Flex Solver COMP")• [NVIDIA Flow Emitter ](<./NVIDIA_Flow_Emitter_COMP.md> "NVIDIA Flow Emitter COMP")• [OP Viewer ](<./OP_Viewer_COMP.md> "OP Viewer COMP")• [Parameter ](<./Parameter_COMP.md> "Parameter COMP")• [Replicator ](<./Replicator_COMP.md> "Replicator COMP")• [Select ](<./Select_COMP.md> "Select COMP")• [Shared Mem In ](<./Shared_Mem_In_COMP.md> "Shared Mem In COMP")• [Shared Mem Out ](<./Shared_Mem_Out_COMP.md> "Shared Mem Out COMP")• [Slider ](<./Slider_COMP.md> "Slider COMP")• [Table ](<./Table_COMP.md> "Table COMP")• [Text ](<./Text_COMP.md> "Text COMP")• [Time ](<./Time_COMP.md> "Time COMP")• [USD ](<./USD_COMP.md> "USD COMP")• [Widget ](<./Widget_COMP.md> "Widget COMP")• [Window ](<./Window_COMP.md> "Window COMP")
