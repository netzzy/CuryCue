# Touch In CHOP

## 

Summary

The Touch In CHOP can be used to create a high speed connection between two TouchDesigner processes via CHOPs. 

Data is sent over TCP/IP. The Touch In CHOP (client) receives its data from a [Touch Out CHOP](<./Touch_Out_CHOP.md> "Touch Out CHOP") (server). The Touch In CHOP is similar to a [Pipe In CHOP](<./Pipe_In_CHOP.md> "Pipe In CHOP") but highly optimized for TouchDesigner-to-TouchDesigner communication. For interfacing with other software or devices, see the [Pipe In CHOP](<./Pipe_In_CHOP.md> "Pipe In CHOP") or the [TCP/IP DAT](<./TCP/IP_DAT.md> "TCP/IP DAT"). 

To receive network data from another "server" computer (e.g. from a Touch Out CHOP running remotely), a connection must be established between the server and the Touch In CHOP before data is sent. 

The data is received as time slices, and can be used to eliminate frame dropping if the sender or receiver is not running at its target frame rate. See [Time Slicing](<./Time_Slicing.md> "Time Slicing") and the [Time Slice CHOP](<./Time_Slice_CHOP.md> "Time Slice CHOP"). Can also be run non-time sliced to receive full channel data. 

To analyze the timing of the messages coming in, attach an [Info CHOP](<./Info_CHOP.md> "Info CHOP") to the Touch In CHOP. It will show the internal queue size and whether it is dropping or missing data (`queue_advanced_total`and`queue_retarded_total`should not be increasing, and`queue_length`should not be zero). 

**NOTE for Windows OS - If experiencing connection issues, confirm Windows Firewall is disabled for TouchDesigner.**

See also: [OSC In CHOP](<./OSC_In_CHOP.md> "OSC In CHOP")

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[touchinCHOP_Class](<./TouchinCHOP_Class.md> "TouchinCHOP Class")

## 

Parameters - Touch In Page

Protocol`protocol`\- ⊞ \- Selects which network protocol to use to transfer data. Different protocol's have methods of connecting and using the address parameter. For more information refer to the [Network Protocols](<./Network_Protocols.md> "Network Protocols") article. 
* Streaming (TCP/IP)`streaming`-
* Messaging (UDP)`msging`-
* Multi-Cast Messaging (UDP)`multicastmsging`-


Address`address`\- The computer name or IP address of the server computer. You can use an IP address (e.g.`100.123.45.78`) or the computer's network name can be used directly. If you put "`localhost`", it means the other end of the pipe is on the same computer. 

Network Port`port`\- The network port of the server. 

Active`active`\- While on, the CHOP receives information from the pipe or server. While off, no updating occurs. Data sent by a server is lost, but a pipe will store the data until Active is turned on again. If in Network mode, turning this parameter on initiates a connection, and turning it off breaks the connection. 

Queue Target`queuetarget`\- The target queue length the CHOP will attempt to maintain. 

Queue Target Unit`queuetargetunit`\- Choose between using Samples, Frames, or Seconds as the units for this parameter. 

Queue Variance`queuevariance`\- The range around the Queue Target that's acceptable. If the queue's length is within the target and variance range, the CHOP will not bother to adjust the queue length. 

Queue Variance Unit`queuevarianceunit`\- Choose between using Samples, Frames, or Seconds as the units for this parameter. 

Maximum Queue`maxqueue`\- The maximum size of the queue when full. Incoming samples will be dropped if the maximum queue is reached. 

Max Queue Unit`maxqueueunit`\- Choose between using Samples, Frames, or Seconds as the units for this parameter. 

Queue Adjust Time`adjusttime`\- Specifies how often to repeat/drop a samples in order to get closer to the queue target range. If the value = 1 and the units = seconds, then it will try to repeat/drop a sample once per second to maintain the queue target set in the Minimum Target and Maximum Target parameters above. 

Adjust Unit`adjusttimeunit`\- Choose between using Samples, Frames, or Seconds as the units for this parameter. 

Recover Outside Range`recover`\- If the queue size goes outside of the target size range for more than the 'adjust time', then if this option is on it will stop delivering new data or throw away a lot of data, until queue size is back in the middle of the min/max target. If this option is of the queue size will be slowly inched towards the target size instead (by dropping or repeating single frames every once in a while). 

Use Synced Ports`syncports`\- ⊞ \- This parameter lets you send the the data in a single global pipe if required. This can be important if various data streams must be sent in frame sync. For more information, refer to [Touch In/Out Synced Ports](<./Touch_In/Out_Synced_Ports.md> "Touch In/Out Synced Ports"). 
* Off`off`\- Uses separate ports for each port number assigned.
* On`on`\- Uses a single global pipe for all Touch Out CHOPs using this Transfer Port Type. The global pipe uses port 10500 internally to send all the global port type data together at once. The Network Port parameter is still used to determine which Touch In CHOP gets the data on the receiving side.

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

Info CHOP Channels

Extra Information for the Touch In CHOP can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). 

### 

Specific Touch In CHOP Info Channels
* read_index -
* time_queue_under_min_target -
* time_queue_over_max_target -
* queue_retarded_total -
* queue_advanced_total -
* queue_recover_total -
* queue_size_start -
* queue_added -
* queue_size_end -
* queue_bumped -
* read_repeat -
* read_filled -
* frames_received -
* send_receive_diff -
* local_clock_rate -
* remote_clock_rate -
* remote_elapsed_time -
* remote_frame -
* remote_frame_lag -
* remote_frame_range -
* io_errors -
* connected -
* names_resent -

### 

Common CHOP Info Channels
* start \- Start of the CHOP interval in samples.
* length \- Number of samples in the CHOP.
* sample_rate \- The samplerate of the channels in frames per second.
* num_channels \- Number of channels in the CHOP.
* time_slice \- 1 if CHOP is Time Slice enabled, 0 otherwise.
* export_sernum \- A count of how often the export connections have been updated.

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


  
TouchDesigner Build: Latest\nwikieditor2025.300002021.100002018.28070before 2018.28070

CHOPs   
---  
[Ableton Link ](<./Ableton_Link_CHOP.md> "Ableton Link CHOP")• [Analyze ](<./Analyze_CHOP.md> "Analyze CHOP")• [Angle ](<./Angle_CHOP.md> "Angle CHOP")• [Attribute ](<./Attribute_CHOP.md> "Attribute CHOP")• [Audio Band EQ ](<./Audio_Band_EQ_CHOP.md> "Audio Band EQ CHOP")• [Audio Binaural ](<./Audio_Binaural_CHOP.md> "Audio Binaural CHOP")• [Audio Device In ](<./Audio_Device_In_CHOP.md> "Audio Device In CHOP")• [Audio Device Out ](<./Audio_Device_Out_CHOP.md> "Audio Device Out CHOP")• [Audio Dynamics ](<./Audio_Dynamics_CHOP.md> "Audio Dynamics CHOP")• [Audio File In ](<./Audio_File_In_CHOP.md> "Audio File In CHOP")• [Audio File Out ](<./Audio_File_Out_CHOP.md> "Audio File Out CHOP")• [Experimental:Audio File Out ](</index.php?title=Experimental:Audio_File_Out_CHOP&action=edit&redlink=1> "Experimental:Audio File Out CHOP \(page does not exist\)")• [Audio Filter ](<./Audio_Filter_CHOP.md> "Audio Filter CHOP")• [Audio Movie ](<./Audio_Movie_CHOP.md> "Audio Movie CHOP")• [Experimental:Audio Movie ](</index.php?title=Experimental:Audio_Movie_CHOP&action=edit&redlink=1> "Experimental:Audio Movie CHOP \(page does not exist\)")• [Audio NDI ](<./Audio_NDI_CHOP.md> "Audio NDI CHOP")• [Audio Oscillator ](<./Audio_Oscillator_CHOP.md> "Audio Oscillator CHOP")• [Audio Para EQ ](<./Audio_Para_EQ_CHOP.md> "Audio Para EQ CHOP")• [Audio Play ](<./Audio_Play_CHOP.md> "Audio Play CHOP")• [Audio Render ](<./Audio_Render_CHOP.md> "Audio Render CHOP")• [Experimental:Audio Render ](</index.php?title=Experimental:Audio_Render_CHOP&action=edit&redlink=1> "Experimental:Audio Render CHOP \(page does not exist\)")• [Audio Spectrum ](<./Audio_Spectrum_CHOP.md> "Audio Spectrum CHOP")• [Audio Stream In ](<./Audio_Stream_In_CHOP.md> "Audio Stream In CHOP")• [Audio Stream Out ](<./Audio_Stream_Out_CHOP.md> "Audio Stream Out CHOP")• [Audio VST ](<./Audio_VST_CHOP.md> "Audio VST CHOP")• [Audio Web Render ](<./Audio_Web_Render_CHOP.md> "Audio Web Render CHOP")• [Beat ](<./Beat_CHOP.md> "Beat CHOP")• [Bind ](<./Bind_CHOP.md> "Bind CHOP")• [BlackTrax ](<./BlackTrax_CHOP.md> "BlackTrax CHOP")• [Blend ](<./Blend_CHOP.md> "Blend CHOP")• [Blob Track ](<./Blob_Track_CHOP.md> "Blob Track CHOP")• [Body Track ](<./Body_Track_CHOP.md> "Body Track CHOP")• [Experimental:Body Track ](</index.php?title=Experimental:Body_Track_CHOP&action=edit&redlink=1> "Experimental:Body Track CHOP \(page does not exist\)")• [Bullet Solver ](<./Bullet_Solver_CHOP.md> "Bullet Solver CHOP")• [Experimental:CHOP ](</index.php?title=Experimental:CHOP&action=edit&redlink=1> "Experimental:CHOP \(page does not exist\)")• [Clip Blender ](<./Clip_Blender_CHOP.md> "Clip Blender CHOP")• [Clip ](<./Clip_CHOP.md> "Clip CHOP")• [Clock ](<./Clock_CHOP.md> "Clock CHOP")• [Experimental:Clock ](</index.php?title=Experimental:Clock_CHOP&action=edit&redlink=1> "Experimental:Clock CHOP \(page does not exist\)")• [Composite ](<./Composite_CHOP.md> "Composite CHOP")• [Constant ](<./Constant_CHOP.md> "Constant CHOP")• [Copy ](<./Copy_CHOP.md> "Copy CHOP")• [Count ](<./Count_CHOP.md> "Count CHOP")• [CPlusPlus ](<./CPlusPlus_CHOP.md> "CPlusPlus CHOP")• [Cross ](<./Cross_CHOP.md> "Cross CHOP")• [Cycle ](<./Cycle_CHOP.md> "Cycle CHOP")• [DAT to ](<./DAT_to_CHOP.md> "DAT to CHOP")• [Delay ](<./Delay_CHOP.md> "Delay CHOP")• [Delete ](<./Delete_CHOP.md> "Delete CHOP")• [DMX In ](<./DMX_In_CHOP.md> "DMX In CHOP")• [DMX Out ](<./DMX_Out_CHOP.md> "DMX Out CHOP")• [Experimental:DMX Out ](</index.php?title=Experimental:DMX_Out_CHOP&action=edit&redlink=1> "Experimental:DMX Out CHOP \(page does not exist\)")• [Envelope ](<./Envelope_CHOP.md> "Envelope CHOP")• [EtherDream ](<./EtherDream_CHOP.md> "EtherDream CHOP")• [Event ](<./Event_CHOP.md> "Event CHOP")• [Expression ](<./Expression_CHOP.md> "Expression CHOP")• [Extend ](<./Extend_CHOP.md> "Extend CHOP")• [Face Track ](<./Face_Track_CHOP.md> "Face Track CHOP")• [Experimental:Face Track ](</index.php?title=Experimental:Face_Track_CHOP&action=edit&redlink=1> "Experimental:Face Track CHOP \(page does not exist\)")• [Fan ](<./Fan_CHOP.md> "Fan CHOP")• [Feedback ](<./Feedback_CHOP.md> "Feedback CHOP")• [File In ](<./File_In_CHOP.md> "File In CHOP")• [File Out ](<./File_Out_CHOP.md> "File Out CHOP")• [Filter ](<./Filter_CHOP.md> "Filter CHOP")• [Experimental:Filter ](</index.php?title=Experimental:Filter_CHOP&action=edit&redlink=1> "Experimental:Filter CHOP \(page does not exist\)")• [FreeD In ](<./FreeD_In_CHOP.md> "FreeD In CHOP")• [FreeD Out ](<./FreeD_Out_CHOP.md> "FreeD Out CHOP")• [Function ](<./Function_CHOP.md> "Function CHOP")• [Gesture ](<./Gesture_CHOP.md> "Gesture CHOP")• [Handle ](<./Handle_CHOP.md> "Handle CHOP")• [Helios DAC ](<./Helios_DAC_CHOP.md> "Helios DAC CHOP")• [Hog ](<./Hog_CHOP.md> "Hog CHOP")• [Hokuyo ](<./Hokuyo_CHOP.md> "Hokuyo CHOP")• [Hold ](<./Hold_CHOP.md> "Hold CHOP")• [Import Select ](<./Import_Select_CHOP.md> "Import Select CHOP")• [In ](<./In_CHOP.md> "In CHOP")• [Info ](<./Info_CHOP.md> "Info CHOP")• [Interpolate ](<./Interpolate_CHOP.md> "Interpolate CHOP")• [Introduction To s Vid ](<./Introduction_To_CHOPs_Vid.md> "Introduction To CHOPs Vid")• [Inverse Curve ](<./Inverse_Curve_CHOP.md> "Inverse Curve CHOP")• [Inverse Kin ](<./Inverse_Kin_CHOP.md> "Inverse Kin CHOP")• [Join ](<./Join_CHOP.md> "Join CHOP")• [Joystick ](<./Joystick_CHOP.md> "Joystick CHOP")• [Keyboard In ](<./Keyboard_In_CHOP.md> "Keyboard In CHOP")• [Keyframe ](<./Keyframe_CHOP.md> "Keyframe CHOP")• [Kinect Azure ](<./Kinect_Azure_CHOP.md> "Kinect Azure CHOP")• [Kinect ](<./Kinect_CHOP.md> "Kinect CHOP")• [Lag ](<./Lag_CHOP.md> "Lag CHOP")• [Laser ](<./Laser_CHOP.md> "Laser CHOP")• [Experimental:Laser ](</index.php?title=Experimental:Laser_CHOP&action=edit&redlink=1> "Experimental:Laser CHOP \(page does not exist\)")• [Laser Device ](<./Laser_Device_CHOP.md> "Laser Device CHOP")• [Experimental:Laser Device ](</index.php?title=Experimental:Laser_Device_CHOP&action=edit&redlink=1> "Experimental:Laser Device CHOP \(page does not exist\)")• [Leap Motion ](<./Leap_Motion_CHOP.md> "Leap Motion CHOP")• [Leuze ROD4 ](<./Leuze_ROD4_CHOP.md> "Leuze ROD4 CHOP")• [LFO ](<./LFO_CHOP.md> "LFO CHOP")• [Limit ](<./Limit_CHOP.md> "Limit CHOP")• [Logic ](<./Logic_CHOP.md> "Logic CHOP")• [Lookup ](<./Lookup_CHOP.md> "Lookup CHOP")• [LTC In ](<./LTC_In_CHOP.md> "LTC In CHOP")• [LTC Out ](<./LTC_Out_CHOP.md> "LTC Out CHOP")• [Math ](<./Math_CHOP.md> "Math CHOP")• [Merge ](<./Merge_CHOP.md> "Merge CHOP")• [MIDI In ](<./MIDI_In_CHOP.md> "MIDI In CHOP")• [MIDI In Map ](<./MIDI_In_Map_CHOP.md> "MIDI In Map CHOP")• [MIDI Out ](<./MIDI_Out_CHOP.md> "MIDI Out CHOP")• [MoSys ](<./MoSys_CHOP.md> "MoSys CHOP")• [Mouse In ](<./Mouse_In_CHOP.md> "Mouse In CHOP")• [Mouse Out ](<./Mouse_Out_CHOP.md> "Mouse Out CHOP")• [Ncam ](<./Ncam_CHOP.md> "Ncam CHOP")• [Noise ](<./Noise_CHOP.md> "Noise CHOP")• [Null ](<./Null_CHOP.md> "Null CHOP")• [OAK Device ](<./OAK_Device_CHOP.md> "OAK Device CHOP")• [OAK Select ](<./OAK_Select_CHOP.md> "OAK Select CHOP")• [Object ](<./Object_CHOP.md> "Object CHOP")• [Oculus Audio ](<./Oculus_Audio_CHOP.md> "Oculus Audio CHOP")• [Oculus Rift ](<./Oculus_Rift_CHOP.md> "Oculus Rift CHOP")• [OpenVR ](<./OpenVR_CHOP.md> "OpenVR CHOP")• [OptiTrack In ](<./OptiTrack_In_CHOP.md> "OptiTrack In CHOP")• [OSC In ](<./OSC_In_CHOP.md> "OSC In CHOP")• [OSC Out ](<./OSC_Out_CHOP.md> "OSC Out CHOP")• [Out ](<./Out_CHOP.md> "Out CHOP")• [Override ](<./Override_CHOP.md> "Override CHOP")• [Experimental:Pan Tilt ](</index.php?title=Experimental:Pan_Tilt_CHOP&action=edit&redlink=1> "Experimental:Pan Tilt CHOP \(page does not exist\)")• [Panel ](<./Panel_CHOP.md> "Panel CHOP")• [Pangolin ](<./Pangolin_CHOP.md> "Pangolin CHOP")• [Experimental:Pangolin ](</index.php?title=Experimental:Pangolin_CHOP&action=edit&redlink=1> "Experimental:Pangolin CHOP \(page does not exist\)")• [Parameter ](<./Parameter_CHOP.md> "Parameter CHOP")• [Experimental:Parameter ](</index.php?title=Experimental:Parameter_CHOP&action=edit&redlink=1> "Experimental:Parameter CHOP \(page does not exist\)")• [Pattern ](<./Pattern_CHOP.md> "Pattern CHOP")• [Perform ](<./Perform_CHOP.md> "Perform CHOP")• [Phaser ](<./Phaser_CHOP.md> "Phaser CHOP")• [Pipe In ](<./Pipe_In_CHOP.md> "Pipe In CHOP")• [Pipe Out ](<./Pipe_Out_CHOP.md> "Pipe Out CHOP")• [Experimental:POP to ](</index.php?title=Experimental:POP_to_CHOP&action=edit&redlink=1> "Experimental:POP to CHOP \(page does not exist\)")• [PosiStageNet ](<./PosiStageNet_CHOP.md> "PosiStageNet CHOP")• [Pulse ](<./Pulse_CHOP.md> "Pulse CHOP")• [RealSense ](<./RealSense_CHOP.md> "RealSense CHOP")• [Record ](<./Record_CHOP.md> "Record CHOP")• [Rename ](<./Rename_CHOP.md> "Rename CHOP")• [Render Pick ](<./Render_Pick_CHOP.md> "Render Pick CHOP")• [RenderStream In ](<./RenderStream_In_CHOP.md> "RenderStream In CHOP")• [Reorder ](<./Reorder_CHOP.md> "Reorder CHOP")• [Replace ](<./Replace_CHOP.md> "Replace CHOP")• [Resample ](<./Resample_CHOP.md> "Resample CHOP")• [Experimental:Resample ](</index.php?title=Experimental:Resample_CHOP&action=edit&redlink=1> "Experimental:Resample CHOP \(page does not exist\)")• [S Curve ](<./S_Curve_CHOP.md> "S Curve CHOP")• [Scan ](<./Scan_CHOP.md> "Scan CHOP")• [Script ](<./Script_CHOP.md> "Script CHOP")• [Experimental:Script ](</index.php?title=Experimental:Script_CHOP&action=edit&redlink=1> "Experimental:Script CHOP \(page does not exist\)")• [Select ](<./Select_CHOP.md> "Select CHOP")• [Sequencer ](<./Sequencer_CHOP.md> "Sequencer CHOP")• [Serial ](<./Serial_CHOP.md> "Serial CHOP")• [Shared Mem In ](<./Shared_Mem_In_CHOP.md> "Shared Mem In CHOP")• [Shared Mem Out ](<./Shared_Mem_Out_CHOP.md> "Shared Mem Out CHOP")• [Shift ](<./Shift_CHOP.md> "Shift CHOP")• [Shuffle ](<./Shuffle_CHOP.md> "Shuffle CHOP")• [Slope ](<./Slope_CHOP.md> "Slope CHOP")• [SOP to ](<./SOP_to_CHOP.md> "SOP to CHOP")• [Sort ](<./Sort_CHOP.md> "Sort CHOP")• [Speed ](<./Speed_CHOP.md> "Speed CHOP")• [Experimental:Speed ](</index.php?title=Experimental:Speed_CHOP&action=edit&redlink=1> "Experimental:Speed CHOP \(page does not exist\)")• [Splice ](<./Splice_CHOP.md> "Splice CHOP")• [Spring ](<./Spring_CHOP.md> "Spring CHOP")• [Experimental:ST2110 Device ](</index.php?title=Experimental:ST2110_Device_CHOP&action=edit&redlink=1> "Experimental:ST2110 Device CHOP \(page does not exist\)")• [Stretch ](<./Stretch_CHOP.md> "Stretch CHOP")• [Experimental:Stretch ](</index.php?title=Experimental:Stretch_CHOP&action=edit&redlink=1> "Experimental:Stretch CHOP \(page does not exist\)")• [Stype In ](<./Stype_In_CHOP.md> "Stype In CHOP")• [Stype Out ](<./Stype_Out_CHOP.md> "Stype Out CHOP")• [Switch ](<./Switch_CHOP.md> "Switch CHOP")• [Sync In ](<./Sync_In_CHOP.md> "Sync In CHOP")• [Sync Out ](<./Sync_Out_CHOP.md> "Sync Out CHOP")• [Tablet ](<./Tablet_CHOP.md> "Tablet CHOP")• [Time Slice ](<./Time_Slice_CHOP.md> "Time Slice CHOP")• [Timecode ](<./Timecode_CHOP.md> "Timecode CHOP")• [Experimental:Timecode ](</index.php?title=Experimental:Timecode_CHOP&action=edit&redlink=1> "Experimental:Timecode CHOP \(page does not exist\)")• [Timeline ](<./Timeline_CHOP.md> "Timeline CHOP")• [Timer ](<./Timer_CHOP.md> "Timer CHOP")• [Experimental:Timer ](</index.php?title=Experimental:Timer_CHOP&action=edit&redlink=1> "Experimental:Timer CHOP \(page does not exist\)")• [TOP to ](<./TOP_to_CHOP.md> "TOP to CHOP")• [Experimental:TOP to ](</index.php?title=Experimental:TOP_to_CHOP&action=edit&redlink=1> "Experimental:TOP to CHOP \(page does not exist\)")• Touch In • [Experimental:Touch In ](</index.php?title=Experimental:Touch_In_CHOP&action=edit&redlink=1> "Experimental:Touch In CHOP \(page does not exist\)")• [Touch Out ](<./Touch_Out_CHOP.md> "Touch Out CHOP")• [Trail ](<./Trail_CHOP.md> "Trail CHOP")• [Transform ](<./Transform_CHOP.md> "Transform CHOP")• [Transform XYZ ](<./Transform_XYZ_CHOP.md> "Transform XYZ CHOP")• [Trigger ](<./Trigger_CHOP.md> "Trigger CHOP")• [Experimental:Trigger ](</index.php?title=Experimental:Trigger_CHOP&action=edit&redlink=1> "Experimental:Trigger CHOP \(page does not exist\)")• [Trim ](<./Trim_CHOP.md> "Trim CHOP")• [Warp ](<./Warp_CHOP.md> "Warp CHOP")• [Wave ](<./Wave_CHOP.md> "Wave CHOP")• [WrnchAI ](<./WrnchAI_CHOP.md> "WrnchAI CHOP")• [ZED ](<./ZED_CHOP.md> "ZED CHOP")• [Experimental:ZED ](</index.php?title=Experimental:ZED_CHOP&action=edit&redlink=1> "Experimental:ZED CHOP \(page does not exist\)")
