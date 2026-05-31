# Window COMP

## 

Summary

The Window Component allows you to create and maintain a separate floating or fixed window displaying the contents of any [Panel](<./Panel.md> "Panel") or any [Node Viewer](<./Node_Viewer.md> "Node Viewer"). 

Most frequently you are setting up the Window COMP`/perform`in the default TouchDesigner project.`/perform`is the default window for [Perform Mode](<./Perform_Mode.md> "Perform Mode"). In the Parameter dialog of the Window component you adjust its settings such as resolution, centering, and which monitor(s) the window will get displayed on. 

You then press F1 to go into [Perform Mode](<./Perform_Mode.md> "Perform Mode") and operate/display the panel standalone. 

Press Esc over a window to close it and go back to [Designer Mode](<./Designer_Mode.md> "Designer Mode"). 

You can create more Window Components, point them to panels or other Operators like TOPs, adjust their parameters and then pulse the parameter Open as Separate Window to see its effect. 

Use the Dialog-> [Window Placement Dialog](<./Window_Placement_Dialog.md> "Window Placement Dialog") which controls which window COMPs get displayed on startup. All Window COMPS in your project are listed there and you can test them individually. 

A window can be fit to a single monitor, or span several monitors. 

Attach an [Info CHOP](<./Info_CHOP.md> "Info CHOP") to the Window component - it will show you the window's current location and size, and whether the window is actually open. 

See also [Window](<./Window.md> "Window"), [Multiple Monitors](<./Multiple_Monitors.md> "Multiple Monitors"). 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[windowCOMP_Class](<./WindowCOMP_Class.md> "WindowCOMP Class")

## 

Parameters - Window Page

Window Operator`winop`\- Specifies the operator the window will display. 

Title`title`\- Specify the window's title. 

Justisy and Offset to...`justifyoffsetto`\- ⊞ \- All the positioning parameters below are done relative to the location you specify here. Your window can span more than the specified 'area', it's just used as the reference for positioning. **Note for macOS** : When using 'Bounds of all Monitors' you must turn off the 'Displays have separate Spaces' toggle in System Preferences > Desktop & Dock > Mission Control, see [Multiple_Monitors#macOS](<./Multiple_Monitors.htm#macOS> "Multiple Monitors") for details. 
* Primary Display`primarydisplay`\- The primary display which is sometimes referred to as the **main display** in Windows control panel or the **primary display** in the NVIDIA control panel.
* Specify Display`specifydisplay`\- Defines the location to be the display specified in the 'Display' parameter below.
* Bounds of All Displays`alldisplays`\- Defines the location to include all displays. The TaskBar is ignored when using this option.


Ignore Taskbar`ignoretaskbar`\- The Windows taskBar is ignored when this option is 'On'. When off the taskbar is accounted for so position and sizing will not cover it up. 

Display`display`\- Specify the display index when Area is set to **Single Monitor**. 

Justify Horizontal`justifyh`\- ⊞ \- Aligns the window horizontally with the monitor or bounds of all monitors. 
* Left`left`\- Align window so that left edge coincides with left edge of specified area.
* Center`center`\- Align window so that horizontal center coincides with horizontal center of specified area.
* Right`right`\- Align window so that right edge coincides with right edge of specified area.
* Mouse`mouse`\- Align window so it opens horizontally centered on the mouse cursor.


Justify Vertical`justifyv`\- ⊞ \- Aligns the window vertically with the monitor or bounds of all monitors. 
* Top`top`\- Align window so that top edge coincides with top edge of specified area.
* Center`center`\- Align window so that vertical center coincides with vertical center of specified area.
* Bottom`bottom`\- Align window so that bottom edge coincides with bottom edge of specified area.
* Mouse`mouse`\- Align window so it opens vertically centered on the mouse cursor.


Offset`winoffset`\- ⊞ \- Horizontal offset applied to window after justifying. 
* X`winoffsetx`\- Horizontal offset applied to window after justifying.
* Y`winoffsety`\- Vertical offset applied to window after justifying.


Shift to Single Display`single`\- ⊞ \- This menu has options for shifting the opening window. You can either shift to a single display or shift to the display the cursor is over when the window opens. 
* Off`off`-
* Keep on Single Display`singledisplay`-
* Keep on Display with Cursor`cursordisplay`-


DPI Scaling`dpiscaling`\- ⊞ \- Options for managing DPI scaling on high DPI monitors. To inspect a monitor's DPI scaling setting, you can use the [Monitors DAT](<./Monitors_DAT.md> "Monitors DAT") and refer to the`dpi_scale`column. 
* Native`native`\- Uses the full resolution of the monitor's native pixels, regardless of the operating system's display scaling setting for that monitor. ie Display Scale = 1.0
* Use DPI Scale`usedpiscale`\- Uses the resolution set by the operating system's display scaling setting for that monitor. For example, a 3840x2160 monitor with display scaling set to 2.0 results in an addressable resolution of 1920x1080. On Windows system this would be a Display Scaling setting of 200%.


Opening Size`size`\- ⊞ \- Determines how the size of the window is determined. 
* Automatic from Panel COMP/TOP`automatic`\- Determines the size automatically from the size of the COMP/TOP specified.
* Fill Location`fill`\- Fills the location specified in the Justify and Offset To... parameter above.
* Custom`custom`\- Use the Width and Height parameters below to specify a custom size.
* Single Display Exclusive`exclusive`-


Width`winw`\- The width of the window when Opening Size parameter is set to Custom. 

Height`winh`\- The height of the window when Opening Size parameter is set to Custom. 

Update Settings from Window`update`\- When the window is open you can reposition and resize it. Clicking this button will then read its current windows settings and apply them to the parameters above. 

Borders`borders`\- Controls whether or not the window contains borders and a title bar. 

Include Borders in Size`bordersinsize`\- When 'On' the borders are included in the size of the window. 

Always on Top`alwaysontop`\- Controls whether or not the window always sits atop other floating windows. 

Cursor Visible`cursorvisible`\- ⊞ \- Controls whether or not the cursor remains visible when over this window. 
* Never`nocursor`\- The cursor is never visible over the window.
* When Moving`cursoronmove`\- The cursor will only be visible when moving and for a short period after it stops moving.
* Always`alwaysvisible`\- The cursor will always be visble when over the window.


Constrain Cursor`constraincursor`\- ⊞ \- Control the area in which the cursor can operate. 
* Off`off`\- Cursor can move to any area of any display.
* Window`window`\- Cursor is constrained to the bounds of this window.
* Display`display`\- Cursor is limited to a specific display.


Cursor Display`cursordisplay`\- Specify display index, when cursor is constrained to a specific display. 

Allow Viewer Interaction`interact`\- Enables interactions with the operator specified in the Window Operator parameter. 

Allow Minimize`allowminimize`\- Enables the window to be minimized in the taskbar (dock in macOS). 

Window Pixel Format`windowpixelformat`\- ⊞ \- Controls the pixel format of the window that is created. This affects both the bit depth (8, 10, 16 bit) and the color space the window will given the content as. This settings only works if a working [Color Space](<./Color_Space.md> "Color Space") is active. 
* SDR 8-Bit fixed`sdr8fixed`\- The content will be converted from the working [Color Space](<./Color_Space.md> "Color Space") to 8-bit fixed SDR (sRGB) when presented to the window.
* SDR 10-Bit fixed`sdr10fixed`\- The content will be converted from the working [Color Space](<./Color_Space.md> "Color Space") to 10-bit fixed SDR (sRGB) when presented to the window.
* HDR 10-Bit fixed`hdr10fixed`\- The content will be converted from the working [Color Space](<./Color_Space.md> "Color Space") to a 10-bit fixed HDR color space. The OS will then convert that color space so it is shown correctly based on the OS/driver/monitor settings. HDR should be enabled in your monitor settings when using this mode, to avoid a flicker when the window is opened.
* HDR 16-Bit float`hdr16float`\- The content will be converted from the working [Color Space](<./Color_Space.md> "Color Space") to a 16-bit float HDR color space. The OS will then convert that color space so it is shown correctly based on the OS/driver/monitor settings. HDR should be enabled in your monitor settings when using this mode, to avoid a flicker when the window is opened. Note that although the OS will be given 16-float content, this does not mean 16-bit data will be sent to the monitor. It will likely convert the data to another format the monitor accepts. Using this mode ensures as much information as possible is given to the OS for it's final color space conversion.


V-Sync Mode`vsyncmode`\- ⊞ \- Controls how the window is updated with regards to V-Sync. Enabled means it will update in sync with the monitors refresh which avoids tearing and lost frames. Disabled means it can update at any point during the refresh which can result in tearing or lost frames. FPS is Half Monitor Rate should be used when doing things such as running a 30fps file on a 60Hz display. This makes each update be shown for exactly 2 refreshes which keeps motion looking smooth. 
* Disabled`disabled`\- Vertical Sync off.
* Enabled`enabled`\- Vertical Sync on.
* FPS is Half Monitor Rate`halfmonitorrate`\- This allows you to run your project at 30FPS on a 60Hz monitor, but ensuring every image is shown for exactly 2 refreshes. Without this option an image may be shown for 1 or 3 refreshes, which makes the content look like it is stuttering. Currently this feature is not functional in the 2022.20000+ series of builds, but we hope to bring back this feature when Vulkan adds support for it.
* FPS is Half Display Rate`halfdisplayrate`-


Draw Window`drawwindow`\- When disabled the window will not update it's contents at all. Useful for processes that arn't doing rendering such as Audio or networking processes, or for when using VR devices. 

Hardware Frame-Lock`hwframelock`\- Use of this feature in the Window COMP is deprecated. It is highly recommended that [Direct Display Out TOPs](<./Direct_Display_Out_TOP.md> "Direct Display Out TOP") be used for Frame-Lock. This feature provides multi-GPU frame-lock sync using [Nvidia Quadro Sync](<https://www.nvidia.com/en-us/design-visualization/solutions/quadro-sync/>) sync cards. For more information, see [Syncing Multiple Computers](<./Syncing_Multiple_Computers.md> "Syncing Multiple Computers") and [Hardware Frame Lock](<./Hardware_Frame_Lock.md> "Hardware Frame Lock"). 

## 

Parameters - Open/Close Page

Open as Perform Window`performance`\- Opens this Window COMP in [Perform Mode](<./Perform_Mode.md> "Perform Mode"). Any Window COMP can be set as default Perform Window (opens using F1 shortcut) using the [Window Placement Dialog](<./Window_Placement_Dialog.md> "Window Placement Dialog"). This button allows you to open this Window COMP in Perform Mode without changing what is currently selected as the 'default' Perform Window. 

Open as Separate Window`winopen`\- Opens this Window COMP as its own floating window, not as the Perform Window. Useful for things such as dialog boxes, popups, or testing, but should not be used for putting final rendered content to outputs. Use a single large Perform Window for that instead of separate windows. 

Close`winclose`\- Closes the window, if it's open. 

Set as Perform Window`setperform`\- Permanently changes the Perform Window setting in the Window Placement dialog to this window. 

Window Placement Dialog`opendialog`\- A shortcut to open the Window Placement dialog. 

Include in Placement Dialog`includedialog`\- When 'On' this Window COMP will be displayed in the Window Placement Dialog. 

Prevent Display Sleep`blocksleep`\- When 'On' the display will not go to sleep regardless of the system's power and sleep settings. 

Close on Escape Key`closeescape`\- When 'On' pressing the escape key over this window will close it. **TIP** : Shift-Escape will always close it, whether this parameter is on or off. 

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

Extra Information for the Window COMP can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). 

### 

Specific Window COMP Info Channels
* winx -
* winy -
* winw -
* winh -
* winopen -
* fill -
* borders -

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


  
TouchDesigner Build: Latest\nwikieditorwikieditorwikieditorwikieditorwikieditor2025.300002021.100002018.28070before 2018.28070

COMPs   
---  
[Actor ](<./Actor_COMP.md> "Actor COMP")• [Ambient Light ](<./Ambient_Light_COMP.md> "Ambient Light COMP")• [Animation ](<./Animation_COMP.md> "Animation COMP")• [Annotate ](<./Annotate_COMP.md> "Annotate COMP")• [Base ](<./Base_COMP.md> "Base COMP")• [Blend ](<./Blend_COMP.md> "Blend COMP")• [Bone ](<./Bone_COMP.md> "Bone COMP")• [Bullet Solver ](<./Bullet_Solver_COMP.md> "Bullet Solver COMP")• [Button ](<./Button_COMP.md> "Button COMP")• [Camera Blend ](<./Camera_Blend_COMP.md> "Camera Blend COMP")• [Camera ](<./Camera_COMP.md> "Camera COMP")• [MediaWiki:Common.js ](<./MediaWiki-Common.md> "MediaWiki:Common.js")• [COMP ](<./COMP.md> "COMP")• [Component ](<./Component.md> "Component")• [Constraint ](<./Constraint_COMP.md> "Constraint COMP")• [Container ](<./Container_COMP.md> "Container COMP")• [Engine ](<./Engine_COMP.md> "Engine COMP")• [Environment Light ](<./Environment_Light_COMP.md> "Environment Light COMP")• [FBX ](<./FBX_COMP.md> "FBX COMP")• [Field ](<./Field_COMP.md> "Field COMP")• [Force ](<./Force_COMP.md> "Force COMP")• [Geo Text ](<./Geo_Text_COMP.md> "Geo Text COMP")• [Geometry ](<./Geometry_COMP.md> "Geometry COMP")• [GLSL ](<./GLSL_COMP.md> "GLSL COMP")• [Handle ](<./Handle_COMP.md> "Handle COMP")• [Impulse Force ](<./Impulse_Force_COMP.md> "Impulse Force COMP")• [Light ](<./Light_COMP.md> "Light COMP")• [List ](<./List_COMP.md> "List COMP")• [Null ](<./Null_COMP.md> "Null COMP")• [NVIDIA Flex Solver ](<./NVIDIA_Flex_Solver_COMP.md> "NVIDIA Flex Solver COMP")• [NVIDIA Flow Emitter ](<./NVIDIA_Flow_Emitter_COMP.md> "NVIDIA Flow Emitter COMP")• [OP Viewer ](<./OP_Viewer_COMP.md> "OP Viewer COMP")• [Parameter ](<./Parameter_COMP.md> "Parameter COMP")• [Replicator ](<./Replicator_COMP.md> "Replicator COMP")• [Select ](<./Select_COMP.md> "Select COMP")• [Shared Mem In ](<./Shared_Mem_In_COMP.md> "Shared Mem In COMP")• [Shared Mem Out ](<./Shared_Mem_Out_COMP.md> "Shared Mem Out COMP")• [Slider ](<./Slider_COMP.md> "Slider COMP")• [Table ](<./Table_COMP.md> "Table COMP")• [Text ](<./Text_COMP.md> "Text COMP")• [Time ](<./Time_COMP.md> "Time COMP")• [USD ](<./USD_COMP.md> "USD COMP")• [Widget ](<./Widget_COMP.md> "Widget COMP")• Window
