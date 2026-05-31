# Engine COMP

## 

Summary

The Engine COMP will run a`.tox file`(component) in a separate process. It uses [TouchEngine](<./TouchEngine.md> "TouchEngine") to manage these processes and pass data between the loaded component and the main project. 

The Engine COMP also allows components loaded in the Engine COMP to open a [Window COMP](<./Window_COMP.md> "Window COMP") (and go into Perform Mode). The Clock Mode must be set Independent (on the Tune page) to enable this - which is required to allow UI events to be serviced. 

**Inputs and Outputs**

The chosen component's top-level Inputs and Outputs are exposed as inputs and outputs on the Engine COMP. Only [TOP](<./TOP.md> "TOP"), [CHOP](<./CHOP.md> "CHOP") and [DAT](<./DAT.md> "DAT") inputs and outputs are supported. 

**Custom Parameters**

Any [custom parameters](<./Custom_Parameters.md> "Custom Parameters") on the top-level component are added to the Engine COMP's parameters. Custom parameters which refer to other nodes in the network, such as [TOP](<./TOP.md> "TOP"), [CHOP](<./CHOP.md> "CHOP") and [DAT](<./DAT.md> "DAT") parameters, are not supported - you should use inputs to connect those nodes instead. 

Note that parameters work in one direction only - you cannot set a parameter from within the loaded`.tox`. 

**External File Paths**

By default, relative paths on OPs or in scripts **inside** the loaded component are relative to the`.tox`file's location. This can be changed with the 'Asset Paths' parameter. Relative paths as file or folder custom parameters **of** the component - those that show up on the Engine COMP \- are always relative to the main project. 

**Monitoring Engine Status**

It is useful to monitor the state and performance of the Engine COMP. By default, an [Info DAT](<./Info_DAT.md> "Info DAT") is docked to the Engine COMP and contains file path and process ID. A docked [Info CHOP](<./Info_CHOP.md> "Info CHOP") contains three sets of monitoring channels: The Info Type menu is by default set to TouchEngine Status which gives loading / running / error status of the Engine process. Changing the menu to TouchEngine Perform gives the engine's performance statistics, and changing the menu to Initialize/Start give ready / running state information specifically about your loaded component since it can be paused, timed and re-initialized. 

**Controlling Engine State**

The Engine process will be started by the TouchDesigner process and it will run your`.tox`component automatically. But you can have more control over the time/memory management of multiple components using the Unload, Reload pulse parameters for the currently-loaded`.tox`file. On the Advanced page, the Launch and Quit Engine Process parameters give you terminate/restart control of the entire Engine process. 

**Component Lifetime**

Under TouchEngine, components are loaded into an already-running instance. For this reason, an [Execute DAT](<./Execute_DAT.md> "Execute DAT")'s`onStart()`and`onExit()`method will never be executed under TouchEngine. The`onCreate()`method will be executed when the component is loaded, and is a good place to do any setup you would normally do in`onStart()`. 

**Time in TouchEngine**

When the Engine COMP starts the component (after it has loaded, if 'Start when Initialized' is On), the component time in TouchEngine is`0`. It will then increase either in sync with the Engine COMP or according to TouchEngine's internal clock, depending on the setting of the 'Clock' parameter on the Tune parameter page. 

An input buffer and output buffer are used to allow for differences in cook rate between the Engine COMP and TouchEngine. Often you may want to adjust the parameters on the Tune page to suit your particular setup. The Engine COMP will cook frames to fill its input buffer, if required, prior to starting to cook the component in TouchEngine - then will cook frames in TouchEngine to fill its output buffer prior to emitting output from the Engine COMP. The Auto setting will attempt to keep small buffers sufficient to avoid dropped frames, but you may wish to set a fixed buffer size to suit your setup, particularly if working with audio. 

**TouchEngine Versions**

TouchEngine is installed as part of TouchDesigner, and the currently running version will be used to load the given`.tox`. If you wish to use a different version of TouchEngine you can either set the [environment variable](<./Variables.htm#System_Environment_Variables> "Variables")`TOUCHENGINE_APP_PATH`to the path to a TouchDesigner installation (an installation directory on Windows, or a TouchDesigner app on macOS) _or_ install TouchDesigner into a folder named`TouchEngine`alongside the`.tox`(on macOS rename an application from TouchDesigner to TouchEngine) _or_ create a link named`TouchEngine`alongside the`.tox`which points to an installation directory or TouchDesigner app. 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[engineCOMP_Class](<./EngineCOMP_Class.md> "EngineCOMP Class")

## 

Parameters - Engine Page

Tox File`file`\- Specify the`.tox`file to load with TouchEngine. 

Unload`unload`\- Unload the currently loaded component. 

Reload`reload`\- Reload the currently loaded component. 

Reload on Crash`reloadoncrash`\- If the TouchEngine instance quits for any reason, restart it. 

Asset Paths`assetpaths`\- ⊞ \- Specify how relative paths inside the component are resolved. 
* Relative to Project File (`.toe`)`project`\- Relative paths inside the component are relative to the project file running TouchEngine.
* Relative to COMP File (`.tox`)`comp`\- Relative paths inside the component are relative to the component (`.tox`file).


Callbacks DAT`callbacks`\- The Callbacks DAT will execute for events related to the TouchEngine instance. 

## 

Parameters - Tune Page

Clock`clock`\- ⊞ \- Specify the temporal connection to the TouchEngine instance. 
* Synchronized`synced`\- Time is strictly synchronized between the Engine COMP and the TouchEngine instance.
* Independent`independent`\- The TouchEngine instance runs according to its own internal clock.


Match Local Component Rate`matchrate`\- When on, the component will be cooked in TouchEngine at the same rate as the Engine COMP. 

Frames per Second`fps`\- The framerate for cooking the component in TouchEngine. 

Wait for Render`wait`\- When enabled, if a frame takes a long time to cook in TouchEngine the Engine COMP will wait during cooking rather than dropping the late frame. 

This behaviour is affected by the size of the output buffer: eg if Out Buffer Frames is 4, the Engine COMP will wait for the 4th most recent frame to complete. __

Render Timeout`timeout`\- When waiting for a frame, TouchEngine will give up waiting after this many milliseconds. 

In Buffer Auto`inauto`\- Automatically manage the number of input frames queued. 

In Buffer Frames`inframes`\- The number of input frames to queue before passing them to the TouchEngine instance. 

To accommodate potential fluctuations in time-slice in the TouchEngine instance, CHOP inputs must send a number of frames ahead of time. __

Out Buffer Auto`outauto`\- Automatically manage the number of output frames queued. 

Out Buffer Frames`outframes`\- The number of output frames to queue after receiving them from the TouchEngine instance. 

To accommodate potential fluctuations in time-slice in the Engine COMP, CHOP outputs must send a number of frames ahead of time. __

## 

Parameters - InitStart Page

Pre-Roll`preroll`\- At initialization, run for this long before entering the ready state. 

Pre-Roll Units`prerollunits`\- ⊞ \- The units in which the Pre-Roll is measured. 
* F`frames`\- The Pre-Roll is measured in frames.
* S`seconds`\- The Pre-Roll is measured in seconds.


Ready when`readywhen`\- ⊞ \- Specify when the Engine COMP will go into the ready state. 
* Component Loaded`loaded`\- The Engine COMP will go into the ready state when TouchEngine has loaded the component.
* Output Buffered`buffered`\- The Engine COMP will go into the ready state when TouchEngine has loaded the component and sufficient frames have been cooked to fill the input and output buffers.
* Component Running`running`\- The Engine COMP will go into the ready state when TouchEngine has loaded the component, sufficient frames have been cooked to fill the input and output buffers and the component is running.


Start when Initialized`startoninit`\- When enabled, playback will start as soon as the component has initialized and is in the ready state. 

Initialize`initialize`\- Reload the .tox file, restarting the TouchEngine instance. 

Start`start`\- Starts playback of the component in the TouchEngine instance. 

Play`play`\- Turn cooking in the TouchEngine instance on or off. 

Go to Done`gotodone`\- Puts the Engine COMP in the done state. 

On Done`ondone`\- ⊞ \- Determines the actions taken, if any, when the Engine COMP enters the done state. 
* Do Nothing`donothing`\- Apart from the state change, nothing happens and TouchEngine continues to run the component.
* Pause`pause`\- Playback of the loaded component is paused.
* Unload`unload`\- The loaded component is unloaded.
* Re-Initialize`reinit`\- The loaded component is unloaded and then initialization takes place.
* Re-Start`restart`\- The component remains loaded and playback begins again.
* Quit Engine Process`quit`\- TouchEngine is completely shut down.

## 

Parameters - Advanced Page

On Engine COMP Create`oncompcreate`\- ⊞ \- Specify what happens when the Engine COMP is created, for example when the project is loaded. 
* Do Nothing`nothing`\- Nothing happens when the Engine COMP is created.
* Launch Engine`launch`\- TouchEngine is started when the Engine COMP is created. Any specified component is not loaded.
* Load and Initialize`initialize`\- TouchEngine is started and any specified component is loaded and the Engine COMP is initialized and put into the ready state.


Launch Engine Process`launch`\- Starts the TouchEngine process if it is not running. 

Quit Engine Process`quit`\- Stops the TouchEngine process if it is running. 

Allow UI`allowui`\- When enabled, components loaded in TouchEngine may open Window COMPs or enter perform mode. Use a parameter on the top-level component or a script to do this. 

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

Extra Information for the Engine COMP can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). 

### 

Specific Engine COMP Info Channels
* input_buffer_frames \- The number of frames in the input buffer. This is affected by parameters on the Tune parameter page.
* output_buffer_frames \- The number of frames in the output buffer. This is affected by parameters on the Tune parameter page.
* output_cook_abs_frame \- The value of cook_abs_frame when the current output was cooked. This is affected by the number of frames in the output buffer.
* output_did_wait \- 1 when the Engine COMP waited for output to cook. This will only be 1 when Wait for Render is On and is affected by the time taken to complete a frame in TouchEngine and the number of input and output buffers. See the Tune parameter page for more details.
* initializing \- 1 while the Engine COMP is in the initializing state.
* initialize_fail \- 1 if an error occurred during initialization. This would normally indicate an error loading the component in TouchEngine.
* ready \- 1 after initialization completes and before starting.
* running \- 1 after starting and until the Engine COMP enters the done state or is re-initialized.
* done \- 1 when the Engine COMP is in the done state.
* timer_seconds \- In the Engine COMP, this matches playing_seconds.
* playing_seconds \- Seconds elapsed since starting, accounting for play state.
* running_seconds \- Seconds elapsed since starting.
* engine_launching \- 1 when TouchEngine is starting, prior to loading any component.
* engine_running \- 1 when TouchEngine has started and is running.
* engine_none \- 1 when TouchEngine is not running.
* engine_error \- 1 when TouchEngine has encountered an error unrelated to the component.
* component_loading \- 1 when TouchEngine is loading a component.
* component_loaded \- 1 when TouchEngine has successfully loaded a component.
* component_unloading \- 1 when TouchEngine is unloading a component.
* component_none \- 1 when TouchEngine has no loaded component.
* component_error \- 1 when TouchEngine encountered an error loading or running a component.
* crash_reload_count \- The number of times the component has been reloaded due to an error when Reload on Crash is On.
* engine_absolute_frame \- The value for absolute time in frames in TouchEngine.
* engine_absolute_seconds \- The value for absolute time in seconds in TouchEngine.
* engine_fps \- The number of frames rendered in the last second in TouchEngine.
* engine_frame_msec \- Amount of time each frame takes to cook in msec in TouchEngine.
* engine_cook \- Is equal to 1 when a frame is cooked and equal to 0 when a frame is skipped in TouchEngine.
* engine_dropped_frames \- The number of frames dropped between the last frame and the current frame in TouchEngine.
* engine_read_ahead_misses \- How many times the movie read ahead failed to maintain the number of specified Read Ahead frames in TouchEngine.
* engine_gpu_mem_used \- Amount of GPU memory used in TouchEngine (in megabytes).
* engine_total_gpu_mem \- Total amount of GPU memory available on the system (in megabytes).
* engine_active_ops \- How many OPs are actively cooking in TouchEngine.
* engine_deactivated_ops \- Number of calls to cook a component that has its Cooking Flag turned off in TouchEngine.
* engine_total_ops \- Total number of OPs in TouchEngine.
* engine_cpu_mem_used \- Amount of CPU memory used in TouchEngine (in megabytes).
* engine_cookstate \- Monitors which frames actually cooked in TouchEngine.
* engine_cookrealtime \- Monitors the state of the realtime flag, determining if TouchEngine is running in realtime mode or not.
* engine_cookrate \- The global target cook rate (frames per second) of TouchEngine. This is the frames per second of the root component, root.time.rate, typically 60, though due to frames taking too long to cook, the actual frames per second may be lower.
* engine_timeslice_step \- The number of frames that TouchEngine stepped forward for the current cook. It's the length of the Time Slice in frames. It will be equal to 1 when the system is taking 1000/root.time.rate msec or less to complete one frame (16.666 msec for a rate of 60).
* engine_timeslice_msec \- The length of the current Time Slice in milliseconds.
* engine_active_expressions \- The number of active python expressions found in TouchEngine.
* engine_active_expressions \- The number of python expressions that have been optimized in TouchEngine.
* engine_cached_expressions \- The number of python expressions that have been cached in TouchEngine.

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


  
TouchDesigner Build: Latest\nwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditormw-replace2025.300002023.112802022.241402021.100002020.200002019.146502018.28070before 2018.28070

COMPs   
---  
[Actor ](<./Actor_COMP.md> "Actor COMP")• [Ambient Light ](<./Ambient_Light_COMP.md> "Ambient Light COMP")• [Animation ](<./Animation_COMP.md> "Animation COMP")• [Annotate ](<./Annotate_COMP.md> "Annotate COMP")• [Base ](<./Base_COMP.md> "Base COMP")• [Blend ](<./Blend_COMP.md> "Blend COMP")• [Bone ](<./Bone_COMP.md> "Bone COMP")• [Bullet Solver ](<./Bullet_Solver_COMP.md> "Bullet Solver COMP")• [Button ](<./Button_COMP.md> "Button COMP")• [Camera Blend ](<./Camera_Blend_COMP.md> "Camera Blend COMP")• [Camera ](<./Camera_COMP.md> "Camera COMP")• [MediaWiki:Common.js ](<./MediaWiki-Common.md> "MediaWiki:Common.js")• [COMP ](<./COMP.md> "COMP")• [Component ](<./Component.md> "Component")• [Constraint ](<./Constraint_COMP.md> "Constraint COMP")• [Container ](<./Container_COMP.md> "Container COMP")• Engine • [Environment Light ](<./Environment_Light_COMP.md> "Environment Light COMP")• [FBX ](<./FBX_COMP.md> "FBX COMP")• [Field ](<./Field_COMP.md> "Field COMP")• [Force ](<./Force_COMP.md> "Force COMP")• [Geo Text ](<./Geo_Text_COMP.md> "Geo Text COMP")• [Geometry ](<./Geometry_COMP.md> "Geometry COMP")• [GLSL ](<./GLSL_COMP.md> "GLSL COMP")• [Handle ](<./Handle_COMP.md> "Handle COMP")• [Impulse Force ](<./Impulse_Force_COMP.md> "Impulse Force COMP")• [Light ](<./Light_COMP.md> "Light COMP")• [List ](<./List_COMP.md> "List COMP")• [Null ](<./Null_COMP.md> "Null COMP")• [NVIDIA Flex Solver ](<./NVIDIA_Flex_Solver_COMP.md> "NVIDIA Flex Solver COMP")• [NVIDIA Flow Emitter ](<./NVIDIA_Flow_Emitter_COMP.md> "NVIDIA Flow Emitter COMP")• [OP Viewer ](<./OP_Viewer_COMP.md> "OP Viewer COMP")• [Parameter ](<./Parameter_COMP.md> "Parameter COMP")• [Replicator ](<./Replicator_COMP.md> "Replicator COMP")• [Select ](<./Select_COMP.md> "Select COMP")• [Shared Mem In ](<./Shared_Mem_In_COMP.md> "Shared Mem In COMP")• [Shared Mem Out ](<./Shared_Mem_Out_COMP.md> "Shared Mem Out COMP")• [Slider ](<./Slider_COMP.md> "Slider COMP")• [Table ](<./Table_COMP.md> "Table COMP")• [Text ](<./Text_COMP.md> "Text COMP")• [Time ](<./Time_COMP.md> "Time COMP")• [USD ](<./USD_COMP.md> "USD COMP")• [Widget ](<./Widget_COMP.md> "Widget COMP")• [Window ](<./Window_COMP.md> "Window COMP")
