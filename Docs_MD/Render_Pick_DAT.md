# Render Pick DAT

##   
  
Summary

The Render Pick DAT lets you get information about the 3D surface at any pixel of any 3D render, allowing you to implement multi-touch on a 3D rendered scene. It samples a rendering (from a [Render TOP](<./Render_TOP.md> "Render TOP") or a [Render Pass TOP](<./Render_Pass_TOP.md> "Render Pass TOP")) and returns 3D information from the geometry at the specified pick locations. 

You feed it a DAT with minimum three columns:`select`,`u`and`v`. A [Multi Touch In DAT](<./Multi_Touch_In_DAT.md> "Multi Touch In DAT") is usually connected to the Render Pick DAT, where the Multi Touch In DAT points to a container that is displaying the output of the Render TOP. 

  
You can pick from multiple cameras simultaneously. You can specify a`camera`which allows the pick to occur from the point of a view other than the first camera listed in the [Render TOP](<./Render_TOP.md> "Render TOP"). The value in the column can either be a path (relative to the Render Pick DAT, or absolute) to a Camera COMP, or it can be an integer index, started at 0. If it's an index it will select the camera to use if there are multiple cameras listed in the [Render TOP](<./Render_TOP.md> "Render TOP"), or if there are cameras listed in the 'Custom Pick Camera(s)' parameter. This is useful for various [Multi-Camera Rendering](<./Multi-Camera_Rendering.md> "Multi-Camera Rendering") setups, and cases such as VR where your picking isn't coming from the point of view of your eye cameras, but instead hand controllers. 

The pick location is a u,v (horizontal, vertical) coordinate placed in the table that you connect to the Render Pick DAT input. Each row of the input table represents one pick point to be sampled, except for the first row which contains column headings`select`,`u`and`v`(plus any other unused columns you want). The`select`,`u`and`v`columns are what you would get from a [Panel CHOP](<./Panel_CHOP.md> "Panel CHOP"). The u and v values goes 0 to 1 left to right and bottom to top, no matter what the aspect ratio of the render is. 

When Strategy is Always, that u,v location is always sampled and the results are displayed in the corresponding row in the Render Pick DAT output. 

The output table will show the path of the geometry that was picked, its position (in a choice of reference frames), surface normal (excluding bump mapping), distance from camera, texture UV coordinate, color, alpha and instance id. It properly picks surfaces with deforming vertices. 

There are some examples here: 
* [geoPanel](<./Palette-geoPanel.md> "Palette:geoPanel") in the palette.
  * [multiTouch](<./Palette-multiTouch.md> "Palette:multiTouch") in the palette under Techniques.


See also the single-sample [Render Pick CHOP](<./Render_Pick_CHOP.md> "Render Pick CHOP"). 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[renderpickDAT_Class](<./RenderpickDAT_Class.md> "RenderpickDAT Class")

## 

Parameters - Render Pick Page

Strategy`strategy`\- ⊞ \- Decides when to update values based on pick interactions. 
* While Select`select`\- Continuously updates values when being selected/picked.
* Hold First Picked`holdfirst`\- Holds the values first returned when geometry picked.
* Hold Last Picked`holdlast`\- Holds the values last returned when geometry picked. This differs from the Continuous strategy in that it will hold the last values picked on geometry if the pick starts sampling empty space (no geometry in that part of the scene). Alternatively, using the Continuous strategy the values will be cleared to zero if the pick starts sampling empty space.
* Always`always`\- Continuously updates values at the location picked.


Clear Previous Pick on New Pick`clearprev`\- This parameter is only enabled when the Strategy is set to Hold Last Picked. When this is on, starting a new pick on empty space will clear the values. When off, the last values will be held if the pick starts on empty space. 

Response Time`responsetime`\- ⊞ \- Determines when the values are updated. 
* Next Cook (Faster)`nextcook`\- The values are captured on the current frame and updated next frame. Results are from the previous frame, but much faster cook times.
* This Cook (Slower)`thiscook`\- The values are captured and updated in the current frame.


Pick Radius`pickradius`\- Controls the radius of the search area for the pick. If nothing is found at the pick's center it will keep searching for geometry in the search area defined by the Pick Radius. 

Pick Radial Step`pickradstep`\- Used to reduce the searching within the search area. The search area is sampled at locations that correspond to 'spokes' outwards from the center pick point. 

Pick Circular Step`pickcirstep`\- Used to reduce the searching within the search area. The search area is sampled at locations that correspond to 'rings' outwards from the center pick point. 

Render/RenderPass TOP`rendertop`\- Specifies which scene to pick on, and which camera to pick from. By default the first camera listed in the [Render TOP](<./Render_TOP.md> "Render TOP") will be used for picking. Another camera can be specified with the 'Custom Pick Camera(s)' parameter, and multiple different cameras can be selected using the`camera`input column. 

Custom Pick Camera(s)`custompickcameras`\- Picking can be done from the viewport of custom camera(s) by specifying one or more [Camera COMP](<./Camera_COMP.md> "Camera COMP") here. If this parameter is blank the cameras from the Render TOP are used. To pick from the viewpoint of multiple different cameras, a`camera`column must be specified in the input DAT. 

Allow Multi-Camera Rendering`allowmulticamera`\- [Multi-Camera Rendering](<./Multi-Camera_Rendering.md> "Multi-Camera Rendering") is a faster way to render multiple passes at the same time, and is thus a speed improvement for doing many picks at the same time. This feature may not work correctly for some older [GLSL MATs](<./GLSL_MAT.md> "GLSL MAT") made in 088 though, so this parameter allows forcing off this speed improvement if necessary. Generally it should be left on though. 

Use Pickable Flags`usepickableflags`\- When turned on only geometry whose [Pickable Flag](<./Flag.md> "Flag") is on can be selected by the Render Pick DAT. The Pickable Flag is found on all [Object](<./Object.md> "Object") components. 

Include Non-Pickable Objects`includenonpickable`\- Includes the non-pickable objects in the picking algorithm such that non-pickable objects may occlude pickable objects. For example, if there is only one pickable object in the scene with lots of additional non-pickable geometry is present, turning this parameter on will prevent the pickable object from being selected if it is behind a non-pickage object (occluded by the non-pickage object). 

Merge Input DAT`mergeinputdat`\- Appends input table to the Render Pick DATs columns. 

Activate Callbacks`activatecallbacks`\- Enables Callback DAT for each pick event. 

Callbacks DAT`callbacks`\- Path to a DAT containing callbacks for pick event received. 

## 

Parameters - Options Page

Fetch Position`position`\- ⊞ \- Returns the position of the point picked on the geometry. Columns _tx, ty, tz_. 
* No`no`\- Do not return position values.
* In SOP Space`sopspace`\- Return position of point picked in SOP transform space.
* In World Space`worldspace`\- Return position of point picked in world transform space.
* In Camera Space`cameraspace`\- Return position of point picked in camera transform space.
* Relative to Object`relativetoobj`\- Return position of point picked relative to object specified in **Reference Object** parameter.


Fetch Normal`normal`\- ⊞ \- Returns the normals of the point picked on the geometry. Columns _nx, ny, nz_. 
* No`no`\- Do not return normal values.
* In SOP Space`sopspace`\- Return normals of point picked in SOP transform space.
* In World Space`worldspace`\- Return normals of point picked in world transform space.
* In Camera Space`cameraspace`\- Return normals of point picked in camera transform space.
* Relative to Object`relativetoobj`\- Return normals of point picked relative to object specified in **Reference Object** parameter.


Reference Object`referenceobj`\- Object used when fetching position or normals **Relative to Object**. 

Fetch Point Color`color`\- Returns the point color of the point picked on the geometry. Columns _cr, cg, cb, ca_. 

Fetch Texture UV`uv`\- Returns the texture coordinates of the point picked on the geometry. Columns _mapu, mapv, mapw_. 

Fetch Depth`depth`\- Returns the depth of the point picked on the geometry. This value a non-linear ratio of the point's position between the near and far planes of the [Depth Buffer](</index.php?title=Depth_Buffer&action=edit&redlink=1> "Depth Buffer \(page does not exist\)"). Column is _depth_. 

Fetch Instance ID`instanceid`\- Returns the Instance ID of the object. This will always be 0 if instancing is off. Column is _instance_. 

Custom Attrib 1`customattrib1`\- Specify which custom attributes to return from the object. 

Custom Attrib 1 Type`customattrib1type`\- The type of attribute is selected from this menu. 

Custom Attrib 2`customattrib2`\- Specify which custom attributes to return from the object. 

Custom Attrib 2 Type`customattrib2type`\- The type of attribute is selected from this menu. 

Custom Attrib 3`customattrib3`\- Specify which custom attributes to return from the object. 

Custom Attrib 3 Type`customattrib3type`\- The type of attribute is selected from this menu. 

Custom Attrib 4`customattrib4`\- Specify which custom attributes to return from the object. 

Custom Attrib 4 Type`customattrib4type`\- The type of attribute is selected from this menu. 

## 

Parameters - Common Page

Language`language`\- ⊞ \- Select how the DAT decides which script language to operate on. 
* Input`input`\- The DAT uses the inputs script language.
* Node`node`\- The DAT uses it's own script language.


Edit/View Extension`extension`\- ⊞ \- Select the file extension this DAT should expose to external editors. 
* dat`dat`\- various common file extensions.
* From Language`language`\- pick extension from DATs script language.
* Custom Extension`custom`\- Specify a custom extension.


Custom Extension`customext`\- Specifiy the custom extension. 

Word Wrap`wordwrap`\- ⊞ \- Enable Word Wrap for Node Display. 
* Input`input`\- The DAT uses the inputs setting.
* On`on`\- Turn on Word Wrap.
* Off`off`\- Turn off Word Wrap.

## 

Operator Inputs
* Input 0:  -

## 

Info CHOP Channels

Extra Information for the Render Pick DAT can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). __

### 

Common DAT Info Channels
* num_rows \- Number of rows in this DAT.
* num_cols \- Number of columns in this DAT.

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

DATs   
---  
[Art-Net ](<./Art-Net_DAT.md> "Art-Net DAT")• [Audio Devices ](<./Audio_Devices_DAT.md> "Audio Devices DAT")• [CHOP Execute ](<./CHOP_Execute_DAT.md> "CHOP Execute DAT")• [CHOP to ](<./CHOP_to_DAT.md> "CHOP to DAT")• [Clip ](<./Clip_DAT.md> "Clip DAT")• [Convert ](<./Convert_DAT.md> "Convert DAT")• [CPlusPlus ](<./CPlusPlus_DAT.md> "CPlusPlus DAT")• [DAT ](<./DAT.md> "DAT")• [ Execute ](<./DAT_Execute_DAT.md> "DAT Execute DAT")• [DAT Export ](<./DAT_Export.md> "DAT Export")• [Error ](<./Error_DAT.md> "Error DAT")• [EtherDream ](<./EtherDream_DAT.md> "EtherDream DAT")• [Evaluate ](<./Evaluate_DAT.md> "Evaluate DAT")• [Examine ](<./Examine_DAT.md> "Examine DAT")• [Execute ](<./Execute_DAT.md> "Execute DAT")• [FIFO ](<./FIFO_DAT.md> "FIFO DAT")• [File In ](<./File_In_DAT.md> "File In DAT")• [File Out ](<./File_Out_DAT.md> "File Out DAT")• [Folder ](<./Folder_DAT.md> "Folder DAT")• [In ](<./In_DAT.md> "In DAT")• [Indices ](<./Indices_DAT.md> "Indices DAT")• [Info ](<./Info_DAT.md> "Info DAT")• [Insert ](<./Insert_DAT.md> "Insert DAT")• [JSON ](<./JSON_DAT.md> "JSON DAT")• [Keyboard In ](<./Keyboard_In_DAT.md> "Keyboard In DAT")• [Lookup ](<./Lookup_DAT.md> "Lookup DAT")• [Media File Info ](<./Media_File_Info_DAT.md> "Media File Info DAT")• [Merge ](<./Merge_DAT.md> "Merge DAT")• [MIDI Event ](<./MIDI_Event_DAT.md> "MIDI Event DAT")• [MIDI In ](<./MIDI_In_DAT.md> "MIDI In DAT")• [Monitors ](<./Monitors_DAT.md> "Monitors DAT")• [MPCDI ](<./MPCDI_DAT.md> "MPCDI DAT")• [MQTT Client ](<./MQTT_Client_DAT.md> "MQTT Client DAT")• [Multi Touch In ](<./Multi_Touch_In_DAT.md> "Multi Touch In DAT")• [NDI ](<./NDI_DAT.md> "NDI DAT")• [Null ](<./Null_DAT.md> "Null DAT")• [OP Execute ](<./OP_Execute_DAT.md> "OP Execute DAT")• [OP Find ](<./OP_Find_DAT.md> "OP Find DAT")• [OSC In ](<./OSC_In_DAT.md> "OSC In DAT")• [OSC Out ](<./OSC_Out_DAT.md> "OSC Out DAT")• [Out ](<./Out_DAT.md> "Out DAT")• [Panel Execute ](<./Panel_Execute_DAT.md> "Panel Execute DAT")• [Parameter ](<./Parameter_DAT.md> "Parameter DAT")• [Parameter Execute ](<./Parameter_Execute_DAT.md> "Parameter Execute DAT")• [ParGroup Execute ](<./ParGroup_Execute_DAT.md> "ParGroup Execute DAT")• [Perform ](<./Perform_DAT.md> "Perform DAT")• [POP to ](<./POP_to_DAT.md> "POP to DAT")• Render Pick • [Reorder ](<./Reorder_DAT.md> "Reorder DAT")• [Script ](<./Script_DAT.md> "Script DAT")• [Select ](<./Select_DAT.md> "Select DAT")• [Serial ](<./Serial_DAT.md> "Serial DAT")• [Serial Devices ](<./Serial_Devices_DAT.md> "Serial Devices DAT")• [SocketIO ](<./SocketIO_DAT.md> "SocketIO DAT")• [SOP to ](<./SOP_to_DAT.md> "SOP to DAT")• [Sort ](<./Sort_DAT.md> "Sort DAT")• [Substitute ](<./Substitute_DAT.md> "Substitute DAT")• [Switch ](<./Switch_DAT.md> "Switch DAT")• [Table ](<./Table_DAT.md> "Table DAT")• [TCP/IP ](<./TCP/IP_DAT.md> "TCP/IP DAT")• [Text ](<./Text_DAT.md> "Text DAT")• [Touch In ](<./Touch_In_DAT.md> "Touch In DAT")• [Touch Out ](<./Touch_Out_DAT.md> "Touch Out DAT")• [Transpose ](<./Transpose_DAT.md> "Transpose DAT")• [TUIO In ](<./TUIO_In_DAT.md> "TUIO In DAT")• [UDP In ](<./UDP_In_DAT.md> "UDP In DAT")• [UDP Out ](<./UDP_Out_DAT.md> "UDP Out DAT")• [UDT In ](<./UDT_In_DAT.md> "UDT In DAT")• [UDT Out ](<./UDT_Out_DAT.md> "UDT Out DAT")• [Video Devices ](<./Video_Devices_DAT.md> "Video Devices DAT")• [Web Client ](<./Web_Client_DAT.md> "Web Client DAT")• [Web ](<./Web_DAT.md> "Web DAT")• [Web Server ](<./Web_Server_DAT.md> "Web Server DAT")• [WebRTC ](<./WebRTC_DAT.md> "WebRTC DAT")• [WebSocket ](<./WebSocket_DAT.md> "WebSocket DAT")• [XML ](<./XML_DAT.md> "XML DAT")
