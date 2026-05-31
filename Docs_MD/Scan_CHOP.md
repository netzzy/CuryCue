# Scan CHOP

## 

Summary

**DEPRECATED:** use the [Laser CHOP](<./Laser_CHOP.md> "Laser CHOP") instead. 

The Scan CHOP converts a [SOP](<./SOP.md> "SOP") or [TOP](<./TOP.md> "TOP") to oscilloscope or laser friendly control waves. The output is usually in the audible range and can be heard directly via an [Audio Device Out CHOP](<./Audio_Device_Out_CHOP.md> "Audio Device Out CHOP"), or used to drive the X and Y deflector inputs of an oscilloscope, or a laser projector recreating the imagery. The output can also be visualized through use of a [Limit SOP](<./Limit_SOP.md> "Limit SOP"). 

A sample component found at: [Op to Audio CHOP example](<http://www.derivative.ca/Forum/viewtopic.php?f=22&t=1201>)

A sample video can be found at: [Total Internal Reflection](<http://vimeo.com/channels/touchdesigner#3750626>)

See also: [EtherDream CHOP](<./EtherDream_CHOP.md> "EtherDream CHOP"), [EtherDream DAT](<./EtherDream_DAT.md> "EtherDream DAT")

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[scanCHOP_Class](</ScanCHOP_Class> "ScanCHOP Class")

## 

Parameters - Scan Page

Source OP`source`\- ⊞ \- Choose the source node family. 
* TOP`top`\- A raster image is converted to control signals by converting each pixel's location to X and Y amplitude values.
* SOP`sop`\- A geometry is converted to control signals by converting each point's position to X and Y amplitude values.
* CHOP`chop`\- A waveform is converted to control signals by converting each graph into corresponding horizontal and vertical offsets.


Sample Rate`rate`\- Samples per second, the output sample rate. 

Swap Output`swap`\- Reverse the X and Y channel outputs. 

X Scale`xscale`\- Scale the x amplitude. 

Y Scale`yscale`\- Scale the y amplitude. 

Rotate`rotate`\- Specified in degrees, rotates the output x,y values. 

Randomize Samples`randomize`\- Output all samples in a random order. Creates a fuzzy chaotic image on an oscilloscope. 

Output Color`color`\- If on, r,g,b channels are created.If on, r,g,b channels are created. 

Red Scale`redscale`\- Scale the output r channel. 

Green Scale`greenscale`\- Scale the output g channel. 

Blue Scale`bluescale`\- Scale the output b channel. 

Blanking Count`blankingcount`\- In the case of SOP input, the number of black/off positions to insert between geometry primitives. In the case of TOP input, the number of black/off positions to insert between full raster scans. Color output must be enabled.In the case of SOP input, the number of black/off positions to insert between geometry primitives. In the case of TOP input, the number of black/off positions to insert between full raster scans. Color output must be enabled. 

## 

Parameters - TOP Page

A raster image is converted to control signals by converting each pixel's location to X and Y amplitude values. The luminance is controlled by how long each sample is "drawn" on the scope. Since the output is low bandwidth, different resampling and ordering options are available for minimizing (or enhancing) flicker. 

TOP`top`\- Path to the TOP node. 

Width`width`\- The number of columns to resample the image at. 

Height`height`\- The number of rows to resample the image at. 

Level`level`\- The number of brightness levels each pixel can have. 

Auto Reduce`limit`\- Automatically reduce the number of rows and columns dynamically to keep the output frame rate 

at a constant level. __

Layered`layered`\- Output the pixels in order of brightness, else they are output left to right for each row. 

Interleave`interleave`\- ⊞ \- Controls the order in which rows are output to minimize flicker. 
* Sweep`sweep`\- The rows are output in order, from top to bottom.
* Even Odd`evenodd`\- The rows are output in two passes, first even, then odd.
* Max`max`\- The rows are output in fully interleaved fashion.

## 

Parameters - SOP Page

Every point in a SOP creates a frame-buffered, stereo audio sample, where the SOP vertex X is placed on the X channel and Y is placed on the Y channel. The oscilloscope output thus contains no aliased lines, just razor-sharp vectors. 

SOP`sop`\- Path to the SOP node. 

Vertex Order`vertexorder`\- Output the points in the same order as the vertices of each polygon, instead of the order in which the points are defined in the geometry. 

Limit Step Size`limitstep`\- Breakup long x,y jumps into several smaller incremental jumps. 

Step Size`stepsize`\- The distance each x,y can change when above option enabled. 

Vertex Repeat`vertexrepeat`\- Repeat each vertex of the each primitive multiple times. 

Camera`camera`\- Project the geometry onto a 2D plane from this camera, otherwise, only the original x,y components of the geometry are used. 

## 

Parameters - CHOP Page

A waveform is converted to control signals by converting each graph into corresponding horizontal and vertical offsets, reproducing the original CHOP waveform. The CHOP should not be [Time Sliced](</index.php?title=Time_Slice&action=edit&redlink=1> "Time Slice \(page does not exist\)"), but instead have some length (example a [Trail CHOP](<./Trail_CHOP.md> "Trail CHOP") or animated [Wave CHOP](<./Wave_CHOP.md> "Wave CHOP")). 

CHOP`chop`\- Path to the CHOP node. 

Trigger`trigger`\- The output graph will begin where its value exceeds this value. This allows for steady 'frozen' waveforms, analagous to an oscilloscope triggered sweep. 

Trigger Value`triggerval`\- The value to begin the trigger. 

Trim`trim`\- Limit the length of the CHOP to be scanned. 

Trim Value`trimval`\- The length of the CHOP to be scanned. 

Trim Units`trimunits`\- Select the units to use for this parameter, Samples, Frames, or Seconds. 

## 

Parameters - Common Page

Time Slice`timeslice`\- Turning this on forces the channels to be "[Time Sliced](<./Time_Slicing.md> "Time Slicing")". A Time Slice is the time between the last cook frame and the current cook frame. 

Scope`scope`\- To determine which channels get affected, some CHOPs use a Scope string on the Common page. 

Sample Rate Match`srselect`\- ⊞ \- Handle cases where multiple input CHOPs' sample rates are different. When Resampling occurs, the curves are interpolated according to the Interpolation Method Option, or "Linear" if the Interpolate Options are not available. 
* Resample At First Input's Rate`first`\- Use rate of first input to resample others.
* Resample At Maximum Rate`max`\- Resample to the highest sample rate.
* Resample At Minimum Rate`min`\- Resample to the lowest sample rate.
* Error If Rates Differ`err`\- Doesn't accept conflicting sample rates.


Export Method`exportmethod`\- ⊞ \- This will determine how to connect the CHOP channel to the parameter. Refer to the [Export](<./Export.md> "Export") article for more information. 
* DAT Table by Index`datindex`\- Uses the docked DAT table and references the channel via the index of the channel in the CHOP.
* DAT Table by Name`datname`\- Uses the docked DAT table and references the channel via the name of the channel in the CHOP.
* Channel Name is Path:Parameter`autoname`\- The channel is the full destination of where to export to, such has`geo1/transform1:tx`.


Export Root`autoexportroot`\- This path points to the root node where all of the paths that exporting by **Channel Name is Path:Parameter** are relative to. 

Export Table`exporttable`\- The DAT used to hold the export information when using the DAT Table Export Methods (See above). 

TouchDesigner Build: Latest\nwikieditor2021.100002018.28070before 2018.28070

CHOPs   
---  
[Ableton Link ](<./Ableton_Link_CHOP.md> "Ableton Link CHOP")• [Analyze ](<./Analyze_CHOP.md> "Analyze CHOP")• [Angle ](<./Angle_CHOP.md> "Angle CHOP")• [Attribute ](<./Attribute_CHOP.md> "Attribute CHOP")• [Audio Band EQ ](<./Audio_Band_EQ_CHOP.md> "Audio Band EQ CHOP")• [Audio Binaural ](<./Audio_Binaural_CHOP.md> "Audio Binaural CHOP")• [Audio Device In ](<./Audio_Device_In_CHOP.md> "Audio Device In CHOP")• [Audio Device Out ](<./Audio_Device_Out_CHOP.md> "Audio Device Out CHOP")• [Audio Dynamics ](<./Audio_Dynamics_CHOP.md> "Audio Dynamics CHOP")• [Audio File In ](<./Audio_File_In_CHOP.md> "Audio File In CHOP")• [Audio File Out ](<./Audio_File_Out_CHOP.md> "Audio File Out CHOP")• [Experimental:Audio File Out ](</Experimental:Audio_File_Out_CHOP> "Experimental:Audio File Out CHOP")• [Audio Filter ](<./Audio_Filter_CHOP.md> "Audio Filter CHOP")• [Audio Movie ](<./Audio_Movie_CHOP.md> "Audio Movie CHOP")• [Experimental:Audio Movie ](</Experimental:Audio_Movie_CHOP> "Experimental:Audio Movie CHOP")• [Audio NDI ](<./Audio_NDI_CHOP.md> "Audio NDI CHOP")• [Audio Oscillator ](<./Audio_Oscillator_CHOP.md> "Audio Oscillator CHOP")• [Audio Para EQ ](<./Audio_Para_EQ_CHOP.md> "Audio Para EQ CHOP")• [Audio Play ](<./Audio_Play_CHOP.md> "Audio Play CHOP")• [Audio Render ](<./Audio_Render_CHOP.md> "Audio Render CHOP")• [Experimental:Audio Render ](</Experimental:Audio_Render_CHOP> "Experimental:Audio Render CHOP")• [Audio Spectrum ](<./Audio_Spectrum_CHOP.md> "Audio Spectrum CHOP")• [Audio Stream In ](<./Audio_Stream_In_CHOP.md> "Audio Stream In CHOP")• [Audio Stream Out ](<./Audio_Stream_Out_CHOP.md> "Audio Stream Out CHOP")• [Audio VST ](<./Audio_VST_CHOP.md> "Audio VST CHOP")• [Audio Web Render ](<./Audio_Web_Render_CHOP.md> "Audio Web Render CHOP")• [Beat ](<./Beat_CHOP.md> "Beat CHOP")• [Bind ](<./Bind_CHOP.md> "Bind CHOP")• [BlackTrax ](<./BlackTrax_CHOP.md> "BlackTrax CHOP")• [Blend ](<./Blend_CHOP.md> "Blend CHOP")• [Blob Track ](<./Blob_Track_CHOP.md> "Blob Track CHOP")• [Body Track ](<./Body_Track_CHOP.md> "Body Track CHOP")• [Experimental:Body Track ](</Experimental:Body_Track_CHOP> "Experimental:Body Track CHOP")• [Bullet Solver ](<./Bullet_Solver_CHOP.md> "Bullet Solver CHOP")• [Clip Blender ](<./Clip_Blender_CHOP.md> "Clip Blender CHOP")• [Clip ](<./Clip_CHOP.md> "Clip CHOP")• [Clock ](<./Clock_CHOP.md> "Clock CHOP")• [Experimental:Clock ](</Experimental:Clock_CHOP> "Experimental:Clock CHOP")• [Composite ](<./Composite_CHOP.md> "Composite CHOP")• [Constant ](<./Constant_CHOP.md> "Constant CHOP")• [Copy ](<./Copy_CHOP.md> "Copy CHOP")• [Count ](<./Count_CHOP.md> "Count CHOP")• [CPlusPlus ](<./CPlusPlus_CHOP.md> "CPlusPlus CHOP")• [Cross ](<./Cross_CHOP.md> "Cross CHOP")• [Cycle ](<./Cycle_CHOP.md> "Cycle CHOP")• [DAT to ](<./DAT_to_CHOP.md> "DAT to CHOP")• [Delay ](<./Delay_CHOP.md> "Delay CHOP")• [Delete ](<./Delete_CHOP.md> "Delete CHOP")• [DMX In ](<./DMX_In_CHOP.md> "DMX In CHOP")• [DMX Out ](<./DMX_Out_CHOP.md> "DMX Out CHOP")• [Experimental:DMX Out ](</Experimental:DMX_Out_CHOP> "Experimental:DMX Out CHOP")• [Envelope ](<./Envelope_CHOP.md> "Envelope CHOP")• [EtherDream ](<./EtherDream_CHOP.md> "EtherDream CHOP")• [Event ](<./Event_CHOP.md> "Event CHOP")• [Expression ](<./Expression_CHOP.md> "Expression CHOP")• [Extend ](<./Extend_CHOP.md> "Extend CHOP")• [Face Track ](<./Face_Track_CHOP.md> "Face Track CHOP")• [Experimental:Face Track ](</Experimental:Face_Track_CHOP> "Experimental:Face Track CHOP")• [Fan ](<./Fan_CHOP.md> "Fan CHOP")• [Feedback ](<./Feedback_CHOP.md> "Feedback CHOP")• [File In ](<./File_In_CHOP.md> "File In CHOP")• [File Out ](<./File_Out_CHOP.md> "File Out CHOP")• [Filter ](<./Filter_CHOP.md> "Filter CHOP")• [Experimental:Filter ](</Experimental:Filter_CHOP> "Experimental:Filter CHOP")• [FreeD In ](<./FreeD_In_CHOP.md> "FreeD In CHOP")• [FreeD Out ](<./FreeD_Out_CHOP.md> "FreeD Out CHOP")• [Function ](<./Function_CHOP.md> "Function CHOP")• [Gesture ](<./Gesture_CHOP.md> "Gesture CHOP")• [Handle ](<./Handle_CHOP.md> "Handle CHOP")• [Helios DAC ](<./Helios_DAC_CHOP.md> "Helios DAC CHOP")• [Hog ](<./Hog_CHOP.md> "Hog CHOP")• [Hokuyo ](<./Hokuyo_CHOP.md> "Hokuyo CHOP")• [Hold ](<./Hold_CHOP.md> "Hold CHOP")• [Import Select ](<./Import_Select_CHOP.md> "Import Select CHOP")• [In ](<./In_CHOP.md> "In CHOP")• [Info ](<./Info_CHOP.md> "Info CHOP")• [Interpolate ](<./Interpolate_CHOP.md> "Interpolate CHOP")• [Introduction To s Vid ](<./Introduction_To_CHOPs_Vid.md> "Introduction To CHOPs Vid")• [Inverse Curve ](<./Inverse_Curve_CHOP.md> "Inverse Curve CHOP")• [Inverse Kin ](<./Inverse_Kin_CHOP.md> "Inverse Kin CHOP")• [Join ](<./Join_CHOP.md> "Join CHOP")• [Joystick ](<./Joystick_CHOP.md> "Joystick CHOP")• [Keyboard In ](<./Keyboard_In_CHOP.md> "Keyboard In CHOP")• [Keyframe ](<./Keyframe_CHOP.md> "Keyframe CHOP")• [Kinect Azure ](<./Kinect_Azure_CHOP.md> "Kinect Azure CHOP")• [Kinect ](<./Kinect_CHOP.md> "Kinect CHOP")• [Lag ](<./Lag_CHOP.md> "Lag CHOP")• [Laser ](<./Laser_CHOP.md> "Laser CHOP")• [Experimental:Laser ](</Experimental:Laser_CHOP> "Experimental:Laser CHOP")• [Laser Device ](<./Laser_Device_CHOP.md> "Laser Device CHOP")• [Experimental:Laser Device ](</Experimental:Laser_Device_CHOP> "Experimental:Laser Device CHOP")• [Leap Motion ](<./Leap_Motion_CHOP.md> "Leap Motion CHOP")• [Leuze ROD4 ](<./Leuze_ROD4_CHOP.md> "Leuze ROD4 CHOP")• [LFO ](<./LFO_CHOP.md> "LFO CHOP")• [Limit ](<./Limit_CHOP.md> "Limit CHOP")• [Logic ](<./Logic_CHOP.md> "Logic CHOP")• [Lookup ](<./Lookup_CHOP.md> "Lookup CHOP")• [LTC In ](<./LTC_In_CHOP.md> "LTC In CHOP")• [LTC Out ](<./LTC_Out_CHOP.md> "LTC Out CHOP")• [Math ](<./Math_CHOP.md> "Math CHOP")• [Merge ](<./Merge_CHOP.md> "Merge CHOP")• [MIDI In ](<./MIDI_In_CHOP.md> "MIDI In CHOP")• [MIDI In Map ](<./MIDI_In_Map_CHOP.md> "MIDI In Map CHOP")• [MIDI Out ](<./MIDI_Out_CHOP.md> "MIDI Out CHOP")• [MoSys ](<./MoSys_CHOP.md> "MoSys CHOP")• [Mouse In ](<./Mouse_In_CHOP.md> "Mouse In CHOP")• [Mouse Out ](<./Mouse_Out_CHOP.md> "Mouse Out CHOP")• [Ncam ](<./Ncam_CHOP.md> "Ncam CHOP")• [Noise ](<./Noise_CHOP.md> "Noise CHOP")• [Null ](<./Null_CHOP.md> "Null CHOP")• [OAK Device ](<./OAK_Device_CHOP.md> "OAK Device CHOP")• [OAK Select ](<./OAK_Select_CHOP.md> "OAK Select CHOP")• [Object ](<./Object_CHOP.md> "Object CHOP")• [Oculus Audio ](<./Oculus_Audio_CHOP.md> "Oculus Audio CHOP")• [Oculus Rift ](<./Oculus_Rift_CHOP.md> "Oculus Rift CHOP")• [OpenVR ](<./OpenVR_CHOP.md> "OpenVR CHOP")• [OptiTrack In ](<./OptiTrack_In_CHOP.md> "OptiTrack In CHOP")• [OSC In ](<./OSC_In_CHOP.md> "OSC In CHOP")• [OSC Out ](<./OSC_Out_CHOP.md> "OSC Out CHOP")• [Out ](<./Out_CHOP.md> "Out CHOP")• [Override ](<./Override_CHOP.md> "Override CHOP")• [Experimental:Pan Tilt ](</Experimental:Pan_Tilt_CHOP> "Experimental:Pan Tilt CHOP")• [Panel ](<./Panel_CHOP.md> "Panel CHOP")• [Pangolin ](<./Pangolin_CHOP.md> "Pangolin CHOP")• [Experimental:Pangolin ](</Experimental:Pangolin_CHOP> "Experimental:Pangolin CHOP")• [Parameter ](<./Parameter_CHOP.md> "Parameter CHOP")• [Experimental:Parameter ](</Experimental:Parameter_CHOP> "Experimental:Parameter CHOP")• [Pattern ](<./Pattern_CHOP.md> "Pattern CHOP")• [Perform ](<./Perform_CHOP.md> "Perform CHOP")• [Phaser ](<./Phaser_CHOP.md> "Phaser CHOP")• [Pipe In ](<./Pipe_In_CHOP.md> "Pipe In CHOP")• [Pipe Out ](<./Pipe_Out_CHOP.md> "Pipe Out CHOP")• [Experimental:POP to ](</Experimental:POP_to_CHOP> "Experimental:POP to CHOP")• [PosiStageNet ](<./PosiStageNet_CHOP.md> "PosiStageNet CHOP")• [Pulse ](<./Pulse_CHOP.md> "Pulse CHOP")• [RealSense ](<./RealSense_CHOP.md> "RealSense CHOP")• [Record ](<./Record_CHOP.md> "Record CHOP")• [Rename ](<./Rename_CHOP.md> "Rename CHOP")• [Render Pick ](<./Render_Pick_CHOP.md> "Render Pick CHOP")• [RenderStream In ](<./RenderStream_In_CHOP.md> "RenderStream In CHOP")• [Reorder ](<./Reorder_CHOP.md> "Reorder CHOP")• [Replace ](<./Replace_CHOP.md> "Replace CHOP")• [Resample ](<./Resample_CHOP.md> "Resample CHOP")• [Experimental:Resample ](</Experimental:Resample_CHOP> "Experimental:Resample CHOP")• [S Curve ](<./S_Curve_CHOP.md> "S Curve CHOP")• Scan • [Script ](<./Script_CHOP.md> "Script CHOP")• [Experimental:Script ](</Experimental:Script_CHOP> "Experimental:Script CHOP")• [Select ](<./Select_CHOP.md> "Select CHOP")• [Sequencer ](<./Sequencer_CHOP.md> "Sequencer CHOP")• [Serial ](<./Serial_CHOP.md> "Serial CHOP")• [Shared Mem In ](<./Shared_Mem_In_CHOP.md> "Shared Mem In CHOP")• [Shared Mem Out ](<./Shared_Mem_Out_CHOP.md> "Shared Mem Out CHOP")• [Shift ](<./Shift_CHOP.md> "Shift CHOP")• [Shuffle ](<./Shuffle_CHOP.md> "Shuffle CHOP")• [Slope ](<./Slope_CHOP.md> "Slope CHOP")• [SOP to ](<./SOP_to_CHOP.md> "SOP to CHOP")• [Sort ](<./Sort_CHOP.md> "Sort CHOP")• [Speed ](<./Speed_CHOP.md> "Speed CHOP")• [Experimental:Speed ](</Experimental:Speed_CHOP> "Experimental:Speed CHOP")• [Splice ](<./Splice_CHOP.md> "Splice CHOP")• [Spring ](<./Spring_CHOP.md> "Spring CHOP")• [Experimental:ST2110 Device ](</Experimental:ST2110_Device_CHOP> "Experimental:ST2110 Device CHOP")• [Stretch ](<./Stretch_CHOP.md> "Stretch CHOP")• [Experimental:Stretch ](</Experimental:Stretch_CHOP> "Experimental:Stretch CHOP")• [Stype In ](<./Stype_In_CHOP.md> "Stype In CHOP")• [Stype Out ](<./Stype_Out_CHOP.md> "Stype Out CHOP")• [Switch ](<./Switch_CHOP.md> "Switch CHOP")• [Sync In ](<./Sync_In_CHOP.md> "Sync In CHOP")• [Sync Out ](<./Sync_Out_CHOP.md> "Sync Out CHOP")• [Tablet ](<./Tablet_CHOP.md> "Tablet CHOP")• [Time Slice ](<./Time_Slice_CHOP.md> "Time Slice CHOP")• [Timecode ](<./Timecode_CHOP.md> "Timecode CHOP")• [Experimental:Timecode ](</Experimental:Timecode_CHOP> "Experimental:Timecode CHOP")• [Timeline ](<./Timeline_CHOP.md> "Timeline CHOP")• [Timer ](<./Timer_CHOP.md> "Timer CHOP")• [Experimental:Timer ](</Experimental:Timer_CHOP> "Experimental:Timer CHOP")• [TOP to ](<./TOP_to_CHOP.md> "TOP to CHOP")• [Experimental:TOP to ](</Experimental:TOP_to_CHOP> "Experimental:TOP to CHOP")• [Touch In ](<./Touch_In_CHOP.md> "Touch In CHOP")• [Experimental:Touch In ](</Experimental:Touch_In_CHOP> "Experimental:Touch In CHOP")• [Touch Out ](<./Touch_Out_CHOP.md> "Touch Out CHOP")• [Trail ](<./Trail_CHOP.md> "Trail CHOP")• [Transform ](<./Transform_CHOP.md> "Transform CHOP")• [Transform XYZ ](<./Transform_XYZ_CHOP.md> "Transform XYZ CHOP")• [Trigger ](<./Trigger_CHOP.md> "Trigger CHOP")• [Experimental:Trigger ](</Experimental:Trigger_CHOP> "Experimental:Trigger CHOP")• [Trim ](<./Trim_CHOP.md> "Trim CHOP")• [Warp ](<./Warp_CHOP.md> "Warp CHOP")• [Wave ](<./Wave_CHOP.md> "Wave CHOP")• [WrnchAI ](<./WrnchAI_CHOP.md> "WrnchAI CHOP")• [ZED ](<./ZED_CHOP.md> "ZED CHOP")• [Experimental:ZED ](</Experimental:ZED_CHOP> "Experimental:ZED CHOP")
