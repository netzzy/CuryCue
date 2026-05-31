# Timecode CHOP

## 

Summary

The Timecode CHOP generates [Timecode](<./Timecode.md> "Timecode") data (channels, a`.timecode`python object and other python members). Its Mode menu provides a variety of ways to get, set and generate timecode through its parameters, including being driven from a timecode string, a set of channels, or other OPs that have timecode such as video input devices. You can also set timecode with python functions. 

The timecode data is output as both channel data in the CHOP, and as a [Timecode object](<./Timecode_Class.md> "Timecode Class") via its [`.timecode`member](<./TimecodeCHOP_Class.htm#timecode> "TimecodeCHOP Class") in Python. 

The timecode can follow the SMPTE standard (ie. non-negative, frames-per-second up to 60, loops at 24 hours), or a more general format (ie. any number of frames per second, negative timecode allowed, loops at 100 hours). 

When being driven by channels, an input with channels named`negative`,`hour`,`minute`,`second`, or`frame`can be provided that is added to the Timecode CHOP's output. 

See also: [Timecode](<./Timecode.md> "Timecode"), [Timecode Class](<./Timecode_Class.md> "Timecode Class") and the OP Snippets for the Timecode CHOP. 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[timecodeCHOP_Class](<./TimecodeCHOP_Class.md> "TimecodeCHOP Class")

## 

Parameters - Timecode Page

SMPTE`smpte`\- When enabled the generated timecode will follow the [SMPTE timecode](<https://en.wikipedia.org/wiki/SMPTE_timecode>) standard, meaning no negative timecodes, and the timecode will loop at 24 hours. When disabled, the format will be more general, allowing for negative numbers and a maximum timecode of 100 hours. 

Mode`mode`\- ⊞ \- The source used for generating the timecode 
* Locked to Timeline`lockedtotimeline`\- Generates the timecode from the timeline's time.
* Specify Index`specifyindex`\- Generates the timecode from a single index value.
* Timecode String`timecodestr`\- Generates the timecode from a timecode string following the format:`hh:mm:ss:ff`or`hh:mm:ss.ff`* Hour, Minute, Second, Frame Parameters`timecodepar`\- Generates the timecode from hour, minute, second, and frame parameters. The parameters will overflow from one to the next, eg. specifying 120 seconds will output timecode as`00:02:00:00`. Fractional values are also allowed.
* Sequential`sequential`\- The timecode increases sequentially over time.
* Timecode Object`timecodeobj`\- Generates the timecode from a [timecode object](<./Timecode_Class.md> "Timecode Class").
* CHOP Channels`chop`\- Generates the timecode from a CHOP reference with some or all of the channels: negative, hour, minute, second, frame.
* OP Reference`op`\- Generates the timecode from an OP with a timecode Python member, eg. [MoviefileinTOP_Class](<./MoviefileinTOP_Class.md> "MoviefileinTOP Class").


Rate`rate`\- The timecode FPS. The timecode's max frame value is equal to`rate-1`. If a fractional rate is provided then the rate is rounded up to the nearest whole number and drop-frames will be calculated if enabled on the Drop Frame parameter. 

Drop Frame`dropframe`\- ⊞ \- Specify how to calculate [drop-frames](<https://en.wikipedia.org/wiki/SMPTE_timecode#Drop-frame_timecode>). Drop frames are used when the FPS is fractional. FPS cannot increment a fractional amount per frame so FPS is rounded to the next whole number and the accumulation of error is accommodated for by adding drop frames. 
* Off`off`\- Drop-frames will not added.
* Automatic`auto`\- Drop-frames will be added to the timecode when the rate is fractional. For special rate values such as 29.97, the defined standard solution is used (ie. 2 frames added every minute, except minutes that are divisible by 10). In other cases, a general solution is used by calculating the accumulated error.


Index`index`\- The index used to generate the timecode. Value is used in conjunction with the specified units. 

Index Unit`indexunit`\- ⊞ \- The index value units. 
* I`indices`-
* F`frames`-
* S`seconds`-


Timecode String`timecodestr`\- A timecode string following the format:`hh:mm:ss:ff`or`hh:mm:ss.ff`Frame`frame`\- Frame component of the timecode. 

Second`second`\- Second component of the timecode. 

Minute`minute`\- Minute component of the timecode. Allows for overflow. 

Hour`hour`\- Hour component of the timecode. 

Initialize`init`\- Used in sequential mode. Initializes the timecode value. 

Start`start`\- Used in sequential mode. Starts the timecode sequential increment. 

Play`play`\- When enabled, the sequential timecode will step forward. 

Timecode Object`timecodeobj`\- A [timecode object](<./Timecode_Class.md> "Timecode Class"). 

CHOP`chop`\- A CHOP reference which contains some or all of the following channels: negative, hour, minute, second, frame. 

OP`op`\- An OP reference that contains a timecode Python member: eg. [MoviefileinTOP_Class](<./MoviefileinTOP_Class.md> "MoviefileinTOP Class"). 

Custom Length`customlength`\- ⊞ \- If set to "By Value", then the Length parameter is used. If set to "By Timecode", then the Length Timecode Object is used. If set to "Off", then the default length will be 23:59:59:ff-1 for a SMPTE timecode and 99:59:59:ff-1 otherwise. 
* Off`off`\- When selected, will not use a custom length. The length will default to 23:59:59:ff-1 for a SMPTE timecode and 99:59:59:ff-1 otherwise.
* By Value`value`\- When selected, set the custom length from a value using the Length parameter.
* By Timecode Object`timecodeobj`\- When selected, set the custom length from a [timecode object](<./Timecode_Class.md> "Timecode Class") using the Length Timecode Object parameter.


Length`length`\- Specifies the custom length in either samples, frames, or seconds. 

Length Units`lengthunits`\- ⊞ \- The unit of the custom length. 
* I`samples`-
* F`frames`-
* S`seconds`-


Length Timecode Object`lengthtimecodeobj`\- Specifies the custom length as a [timecode object](<./Timecode_Class.md> "Timecode Class"). 

Extend Left`extendleft`\- ⊞ \- Set the timecode behavior when exceeding the lower bound of 00:00:00:00 for SMPTE timecode and -99:59:59:ff+1 otherwise. 
* Hold`hold`\- If selected, then the timecode will hold its value when exceeding lower bound: 00:00:00:00 for SMPTE timecode and -99:59:59:ff+1 otherwise.
* Cycle`cycle`\- If selected, then the timecode will cycle its value when exceeding lower bound. It will cycle to the length value for SMPTE timecode and 00:00:00:00 otherwise.


Extend Right`extendright`\- ⊞ \- Set the timecode behavior when exceeding the upper bound defined by the length parameters. 
* Hold`hold`\- If selected, then the timecode will hold its value to the length value.
* Cycle`cycle`\- If selected, then the timecode will cycle to 00:00:00:00 once it reaches length.

## 

Parameters - Output Page

Negative Chan`negativechan`\- When enabled, outputs the negative channel, which is true when the timecode is negative. Always false when using SMPTE standard. 

Frame Chan`framechan`\- When enabled, outputs the frame channel. 

Second Chan`secondchan`\- When enabled, outputs the second channel. 

Minute Chan`minutechan`\- When enabled, outputs the minute channel. 

Hour Chan`hourchan`\- When enabled, outputs the hour channel. 

Total Seconds Chan`totalseconds`\- When enabled, outputs the total_seconds channel, which is the timecode converted into seconds. 

Total Frames Chan`totalframes`\- When enabled, outputs the total_frames channel, which is the timecode into frames. 

Drop Frame Chan`dropframechan`\- When enabled, outputs the drop_frame channel, which is true when the timecode is drop-frame. 

FPS Chan`fpschan`\- When enabled, outputs the fps channel. 

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

## 

Operator Inputs
* Input 0:  \- Optional input CHOP with some or all of following channels: negative, hour, minute, second, frame. The input timecode value is added to the Timecode CHOP's output.


TouchDesigner Build: Latest\nwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditor2025.300002023.11280

CHOPs   
---  
[Ableton Link ](<./Ableton_Link_CHOP.md> "Ableton Link CHOP")• [Analyze ](<./Analyze_CHOP.md> "Analyze CHOP")• [Angle ](<./Angle_CHOP.md> "Angle CHOP")• [Attribute ](<./Attribute_CHOP.md> "Attribute CHOP")• [Audio Band EQ ](<./Audio_Band_EQ_CHOP.md> "Audio Band EQ CHOP")• [Audio Binaural ](<./Audio_Binaural_CHOP.md> "Audio Binaural CHOP")• [Audio Device In ](<./Audio_Device_In_CHOP.md> "Audio Device In CHOP")• [Audio Device Out ](<./Audio_Device_Out_CHOP.md> "Audio Device Out CHOP")• [Audio Dynamics ](<./Audio_Dynamics_CHOP.md> "Audio Dynamics CHOP")• [Audio File In ](<./Audio_File_In_CHOP.md> "Audio File In CHOP")• [Audio File Out ](<./Audio_File_Out_CHOP.md> "Audio File Out CHOP")• [Experimental:Audio File Out ](</index.php?title=Experimental:Audio_File_Out_CHOP&action=edit&redlink=1> "Experimental:Audio File Out CHOP \(page does not exist\)")• [Audio Filter ](<./Audio_Filter_CHOP.md> "Audio Filter CHOP")• [Audio Movie ](<./Audio_Movie_CHOP.md> "Audio Movie CHOP")• [Experimental:Audio Movie ](</index.php?title=Experimental:Audio_Movie_CHOP&action=edit&redlink=1> "Experimental:Audio Movie CHOP \(page does not exist\)")• [Audio NDI ](<./Audio_NDI_CHOP.md> "Audio NDI CHOP")• [Audio Oscillator ](<./Audio_Oscillator_CHOP.md> "Audio Oscillator CHOP")• [Audio Para EQ ](<./Audio_Para_EQ_CHOP.md> "Audio Para EQ CHOP")• [Audio Play ](<./Audio_Play_CHOP.md> "Audio Play CHOP")• [Audio Render ](<./Audio_Render_CHOP.md> "Audio Render CHOP")• [Experimental:Audio Render ](</index.php?title=Experimental:Audio_Render_CHOP&action=edit&redlink=1> "Experimental:Audio Render CHOP \(page does not exist\)")• [Audio Spectrum ](<./Audio_Spectrum_CHOP.md> "Audio Spectrum CHOP")• [Audio Stream In ](<./Audio_Stream_In_CHOP.md> "Audio Stream In CHOP")• [Audio Stream Out ](<./Audio_Stream_Out_CHOP.md> "Audio Stream Out CHOP")• [Audio VST ](<./Audio_VST_CHOP.md> "Audio VST CHOP")• [Audio Web Render ](<./Audio_Web_Render_CHOP.md> "Audio Web Render CHOP")• [Beat ](<./Beat_CHOP.md> "Beat CHOP")• [Bind ](<./Bind_CHOP.md> "Bind CHOP")• [BlackTrax ](<./BlackTrax_CHOP.md> "BlackTrax CHOP")• [Blend ](<./Blend_CHOP.md> "Blend CHOP")• [Blob Track ](<./Blob_Track_CHOP.md> "Blob Track CHOP")• [Body Track ](<./Body_Track_CHOP.md> "Body Track CHOP")• [Experimental:Body Track ](</index.php?title=Experimental:Body_Track_CHOP&action=edit&redlink=1> "Experimental:Body Track CHOP \(page does not exist\)")• [Bullet Solver ](<./Bullet_Solver_CHOP.md> "Bullet Solver CHOP")• [Experimental:CHOP ](</index.php?title=Experimental:CHOP&action=edit&redlink=1> "Experimental:CHOP \(page does not exist\)")• [Clip Blender ](<./Clip_Blender_CHOP.md> "Clip Blender CHOP")• [Clip ](<./Clip_CHOP.md> "Clip CHOP")• [Clock ](<./Clock_CHOP.md> "Clock CHOP")• [Experimental:Clock ](</index.php?title=Experimental:Clock_CHOP&action=edit&redlink=1> "Experimental:Clock CHOP \(page does not exist\)")• [Composite ](<./Composite_CHOP.md> "Composite CHOP")• [Constant ](<./Constant_CHOP.md> "Constant CHOP")• [Copy ](<./Copy_CHOP.md> "Copy CHOP")• [Count ](<./Count_CHOP.md> "Count CHOP")• [CPlusPlus ](<./CPlusPlus_CHOP.md> "CPlusPlus CHOP")• [Cross ](<./Cross_CHOP.md> "Cross CHOP")• [Cycle ](<./Cycle_CHOP.md> "Cycle CHOP")• [DAT to ](<./DAT_to_CHOP.md> "DAT to CHOP")• [Delay ](<./Delay_CHOP.md> "Delay CHOP")• [Delete ](<./Delete_CHOP.md> "Delete CHOP")• [DMX In ](<./DMX_In_CHOP.md> "DMX In CHOP")• [DMX Out ](<./DMX_Out_CHOP.md> "DMX Out CHOP")• [Experimental:DMX Out ](</index.php?title=Experimental:DMX_Out_CHOP&action=edit&redlink=1> "Experimental:DMX Out CHOP \(page does not exist\)")• [Envelope ](<./Envelope_CHOP.md> "Envelope CHOP")• [EtherDream ](<./EtherDream_CHOP.md> "EtherDream CHOP")• [Event ](<./Event_CHOP.md> "Event CHOP")• [Expression ](<./Expression_CHOP.md> "Expression CHOP")• [Extend ](<./Extend_CHOP.md> "Extend CHOP")• [Face Track ](<./Face_Track_CHOP.md> "Face Track CHOP")• [Experimental:Face Track ](</index.php?title=Experimental:Face_Track_CHOP&action=edit&redlink=1> "Experimental:Face Track CHOP \(page does not exist\)")• [Fan ](<./Fan_CHOP.md> "Fan CHOP")• [Feedback ](<./Feedback_CHOP.md> "Feedback CHOP")• [File In ](<./File_In_CHOP.md> "File In CHOP")• [File Out ](<./File_Out_CHOP.md> "File Out CHOP")• [Filter ](<./Filter_CHOP.md> "Filter CHOP")• [Experimental:Filter ](</index.php?title=Experimental:Filter_CHOP&action=edit&redlink=1> "Experimental:Filter CHOP \(page does not exist\)")• [FreeD In ](<./FreeD_In_CHOP.md> "FreeD In CHOP")• [FreeD Out ](<./FreeD_Out_CHOP.md> "FreeD Out CHOP")• [Function ](<./Function_CHOP.md> "Function CHOP")• [Gesture ](<./Gesture_CHOP.md> "Gesture CHOP")• [Handle ](<./Handle_CHOP.md> "Handle CHOP")• [Helios DAC ](<./Helios_DAC_CHOP.md> "Helios DAC CHOP")• [Hog ](<./Hog_CHOP.md> "Hog CHOP")• [Hokuyo ](<./Hokuyo_CHOP.md> "Hokuyo CHOP")• [Hold ](<./Hold_CHOP.md> "Hold CHOP")• [Import Select ](<./Import_Select_CHOP.md> "Import Select CHOP")• [In ](<./In_CHOP.md> "In CHOP")• [Info ](<./Info_CHOP.md> "Info CHOP")• [Interpolate ](<./Interpolate_CHOP.md> "Interpolate CHOP")• [Introduction To s Vid ](<./Introduction_To_CHOPs_Vid.md> "Introduction To CHOPs Vid")• [Inverse Curve ](<./Inverse_Curve_CHOP.md> "Inverse Curve CHOP")• [Inverse Kin ](<./Inverse_Kin_CHOP.md> "Inverse Kin CHOP")• [Join ](<./Join_CHOP.md> "Join CHOP")• [Joystick ](<./Joystick_CHOP.md> "Joystick CHOP")• [Keyboard In ](<./Keyboard_In_CHOP.md> "Keyboard In CHOP")• [Keyframe ](<./Keyframe_CHOP.md> "Keyframe CHOP")• [Kinect Azure ](<./Kinect_Azure_CHOP.md> "Kinect Azure CHOP")• [Kinect ](<./Kinect_CHOP.md> "Kinect CHOP")• [Lag ](<./Lag_CHOP.md> "Lag CHOP")• [Laser ](<./Laser_CHOP.md> "Laser CHOP")• [Experimental:Laser ](</index.php?title=Experimental:Laser_CHOP&action=edit&redlink=1> "Experimental:Laser CHOP \(page does not exist\)")• [Laser Device ](<./Laser_Device_CHOP.md> "Laser Device CHOP")• [Experimental:Laser Device ](</index.php?title=Experimental:Laser_Device_CHOP&action=edit&redlink=1> "Experimental:Laser Device CHOP \(page does not exist\)")• [Leap Motion ](<./Leap_Motion_CHOP.md> "Leap Motion CHOP")• [Leuze ROD4 ](<./Leuze_ROD4_CHOP.md> "Leuze ROD4 CHOP")• [LFO ](<./LFO_CHOP.md> "LFO CHOP")• [Limit ](<./Limit_CHOP.md> "Limit CHOP")• [Logic ](<./Logic_CHOP.md> "Logic CHOP")• [Lookup ](<./Lookup_CHOP.md> "Lookup CHOP")• [LTC In ](<./LTC_In_CHOP.md> "LTC In CHOP")• [LTC Out ](<./LTC_Out_CHOP.md> "LTC Out CHOP")• [Math ](<./Math_CHOP.md> "Math CHOP")• [Merge ](<./Merge_CHOP.md> "Merge CHOP")• [MIDI In ](<./MIDI_In_CHOP.md> "MIDI In CHOP")• [MIDI In Map ](<./MIDI_In_Map_CHOP.md> "MIDI In Map CHOP")• [MIDI Out ](<./MIDI_Out_CHOP.md> "MIDI Out CHOP")• [MoSys ](<./MoSys_CHOP.md> "MoSys CHOP")• [Mouse In ](<./Mouse_In_CHOP.md> "Mouse In CHOP")• [Mouse Out ](<./Mouse_Out_CHOP.md> "Mouse Out CHOP")• [Ncam ](<./Ncam_CHOP.md> "Ncam CHOP")• [Noise ](<./Noise_CHOP.md> "Noise CHOP")• [Null ](<./Null_CHOP.md> "Null CHOP")• [OAK Device ](<./OAK_Device_CHOP.md> "OAK Device CHOP")• [OAK Select ](<./OAK_Select_CHOP.md> "OAK Select CHOP")• [Object ](<./Object_CHOP.md> "Object CHOP")• [Oculus Audio ](<./Oculus_Audio_CHOP.md> "Oculus Audio CHOP")• [Oculus Rift ](<./Oculus_Rift_CHOP.md> "Oculus Rift CHOP")• [OpenVR ](<./OpenVR_CHOP.md> "OpenVR CHOP")• [OptiTrack In ](<./OptiTrack_In_CHOP.md> "OptiTrack In CHOP")• [OSC In ](<./OSC_In_CHOP.md> "OSC In CHOP")• [OSC Out ](<./OSC_Out_CHOP.md> "OSC Out CHOP")• [Out ](<./Out_CHOP.md> "Out CHOP")• [Override ](<./Override_CHOP.md> "Override CHOP")• [Experimental:Pan Tilt ](</index.php?title=Experimental:Pan_Tilt_CHOP&action=edit&redlink=1> "Experimental:Pan Tilt CHOP \(page does not exist\)")• [Panel ](<./Panel_CHOP.md> "Panel CHOP")• [Pangolin ](<./Pangolin_CHOP.md> "Pangolin CHOP")• [Experimental:Pangolin ](</index.php?title=Experimental:Pangolin_CHOP&action=edit&redlink=1> "Experimental:Pangolin CHOP \(page does not exist\)")• [Parameter ](<./Parameter_CHOP.md> "Parameter CHOP")• [Experimental:Parameter ](</index.php?title=Experimental:Parameter_CHOP&action=edit&redlink=1> "Experimental:Parameter CHOP \(page does not exist\)")• [Pattern ](<./Pattern_CHOP.md> "Pattern CHOP")• [Perform ](<./Perform_CHOP.md> "Perform CHOP")• [Phaser ](<./Phaser_CHOP.md> "Phaser CHOP")• [Pipe In ](<./Pipe_In_CHOP.md> "Pipe In CHOP")• [Pipe Out ](<./Pipe_Out_CHOP.md> "Pipe Out CHOP")• [Experimental:POP to ](</index.php?title=Experimental:POP_to_CHOP&action=edit&redlink=1> "Experimental:POP to CHOP \(page does not exist\)")• [PosiStageNet ](<./PosiStageNet_CHOP.md> "PosiStageNet CHOP")• [Pulse ](<./Pulse_CHOP.md> "Pulse CHOP")• [RealSense ](<./RealSense_CHOP.md> "RealSense CHOP")• [Record ](<./Record_CHOP.md> "Record CHOP")• [Rename ](<./Rename_CHOP.md> "Rename CHOP")• [Render Pick ](<./Render_Pick_CHOP.md> "Render Pick CHOP")• [RenderStream In ](<./RenderStream_In_CHOP.md> "RenderStream In CHOP")• [Reorder ](<./Reorder_CHOP.md> "Reorder CHOP")• [Replace ](<./Replace_CHOP.md> "Replace CHOP")• [Resample ](<./Resample_CHOP.md> "Resample CHOP")• [Experimental:Resample ](</index.php?title=Experimental:Resample_CHOP&action=edit&redlink=1> "Experimental:Resample CHOP \(page does not exist\)")• [S Curve ](<./S_Curve_CHOP.md> "S Curve CHOP")• [Scan ](<./Scan_CHOP.md> "Scan CHOP")• [Script ](<./Script_CHOP.md> "Script CHOP")• [Experimental:Script ](</index.php?title=Experimental:Script_CHOP&action=edit&redlink=1> "Experimental:Script CHOP \(page does not exist\)")• [Select ](<./Select_CHOP.md> "Select CHOP")• [Sequencer ](<./Sequencer_CHOP.md> "Sequencer CHOP")• [Serial ](<./Serial_CHOP.md> "Serial CHOP")• [Shared Mem In ](<./Shared_Mem_In_CHOP.md> "Shared Mem In CHOP")• [Shared Mem Out ](<./Shared_Mem_Out_CHOP.md> "Shared Mem Out CHOP")• [Shift ](<./Shift_CHOP.md> "Shift CHOP")• [Shuffle ](<./Shuffle_CHOP.md> "Shuffle CHOP")• [Slope ](<./Slope_CHOP.md> "Slope CHOP")• [SOP to ](<./SOP_to_CHOP.md> "SOP to CHOP")• [Sort ](<./Sort_CHOP.md> "Sort CHOP")• [Speed ](<./Speed_CHOP.md> "Speed CHOP")• [Experimental:Speed ](</index.php?title=Experimental:Speed_CHOP&action=edit&redlink=1> "Experimental:Speed CHOP \(page does not exist\)")• [Splice ](<./Splice_CHOP.md> "Splice CHOP")• [Spring ](<./Spring_CHOP.md> "Spring CHOP")• [Experimental:ST2110 Device ](</index.php?title=Experimental:ST2110_Device_CHOP&action=edit&redlink=1> "Experimental:ST2110 Device CHOP \(page does not exist\)")• [Stretch ](<./Stretch_CHOP.md> "Stretch CHOP")• [Experimental:Stretch ](</index.php?title=Experimental:Stretch_CHOP&action=edit&redlink=1> "Experimental:Stretch CHOP \(page does not exist\)")• [Stype In ](<./Stype_In_CHOP.md> "Stype In CHOP")• [Stype Out ](<./Stype_Out_CHOP.md> "Stype Out CHOP")• [Switch ](<./Switch_CHOP.md> "Switch CHOP")• [Sync In ](<./Sync_In_CHOP.md> "Sync In CHOP")• [Sync Out ](<./Sync_Out_CHOP.md> "Sync Out CHOP")• [Tablet ](<./Tablet_CHOP.md> "Tablet CHOP")• [Time Slice ](<./Time_Slice_CHOP.md> "Time Slice CHOP")• Timecode • [Experimental:Timecode ](</index.php?title=Experimental:Timecode_CHOP&action=edit&redlink=1> "Experimental:Timecode CHOP \(page does not exist\)")• [Timeline ](<./Timeline_CHOP.md> "Timeline CHOP")• [Timer ](<./Timer_CHOP.md> "Timer CHOP")• [Experimental:Timer ](</index.php?title=Experimental:Timer_CHOP&action=edit&redlink=1> "Experimental:Timer CHOP \(page does not exist\)")• [TOP to ](<./TOP_to_CHOP.md> "TOP to CHOP")• [Experimental:TOP to ](</index.php?title=Experimental:TOP_to_CHOP&action=edit&redlink=1> "Experimental:TOP to CHOP \(page does not exist\)")• [Touch In ](<./Touch_In_CHOP.md> "Touch In CHOP")• [Experimental:Touch In ](</index.php?title=Experimental:Touch_In_CHOP&action=edit&redlink=1> "Experimental:Touch In CHOP \(page does not exist\)")• [Touch Out ](<./Touch_Out_CHOP.md> "Touch Out CHOP")• [Trail ](<./Trail_CHOP.md> "Trail CHOP")• [Transform ](<./Transform_CHOP.md> "Transform CHOP")• [Transform XYZ ](<./Transform_XYZ_CHOP.md> "Transform XYZ CHOP")• [Trigger ](<./Trigger_CHOP.md> "Trigger CHOP")• [Experimental:Trigger ](</index.php?title=Experimental:Trigger_CHOP&action=edit&redlink=1> "Experimental:Trigger CHOP \(page does not exist\)")• [Trim ](<./Trim_CHOP.md> "Trim CHOP")• [Warp ](<./Warp_CHOP.md> "Warp CHOP")• [Wave ](<./Wave_CHOP.md> "Wave CHOP")• [WrnchAI ](<./WrnchAI_CHOP.md> "WrnchAI CHOP")• [ZED ](<./ZED_CHOP.md> "ZED CHOP")• [Experimental:ZED ](</index.php?title=Experimental:ZED_CHOP&action=edit&redlink=1> "Experimental:ZED CHOP \(page does not exist\)")
