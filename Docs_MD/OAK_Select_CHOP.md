# OAK Select CHOP

##   
  
Summary

The OAK Select CHOP is like a [Script CHOP](<./Script_CHOP.md> "Script CHOP") combined with a [Select CHOP](<./Select_CHOP.md> "Select CHOP"), and any of the other hardware-specific CHOPs. The basic operation involves providing an [OAK Device CHOP](<./OAK_Device_CHOP.md> "OAK Device CHOP") and a stream name. In the simplest case, the stream's data will show up as well-named channels. For example, [ImgDetections](<https://docs.luxonis.com/projects/api/en/latest/components/messages/img_detections/>) messages indicating the 2D coordinates and labels of detected objects will show up as CHOP channels without any manual coding. In more complex cases such as hand landmark tracking, the stream may be of [NNData](<https://docs.luxonis.com/projects/api/en/latest/components/messages/nn_data/>) or [Buffer](<https://docs.luxonis.com/projects/api/en/latest/components/messages/buffer/>) type, requiring the user to implement a callback and parse the data. 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[oakselectCHOP_Class](<./OakselectCHOP_Class.md> "OakselectCHOP Class")

## 

Parameters - OAK Page

Active`active`\- Toggle whether the OAK Select CHOP cooks. 

OAK Device CHOP`chop`\- An OAK Device CHOP running a depthai pipeline. 

Stream`stream`\- The name of the stream to be received. 

Queue Size`queuesize`\- For memory efficiency, this parameter controls the number of messages TouchDesigner reuses when receiving messages from OAK. See "Queue Size" below. 

Max Items`maxitems`\- This parameter helps the OAK Select CHOP output a consistent number of channels. When running an image detection pipeline, the number of detected items will vary from frame to frame, but we want TouchDesigner to output a consistent number of channels. 

Output Format`outputformat`\- ⊞ \- The default option "Items As Separate Channels" enables time-slicing while "Items as Separate Samples" does not. If the stream is one which automatically fills in the CHOP, then "Items as Separate Samples" is a useful way to make the CHOP output **Max Items** samples consistently. 
* Items As Separate Channels`itemsaschannels`-
* Items As Separate Samples`itemsassamples`-


Use First Sample Only`firstsample`\- Only use the most recently received message with the OAK Select CHOP. For example, for an IMU stream which is sending very high-frame rate data, toggling this parameter will only show the latest sample. 

Sample Rate`rate`\- The sample rate of the CHOP. The default sample rate is`me.time.rate`. 

Callbacks DAT`callbacks`\- Specifies the DAT which holds the callbacks. 

Setup Parameters`setuppars`\- Clicking the button runs the setupParameters() callback function. 

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

## 

Info CHOP Channels

Extra Information for the oakselect CHOP can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). __

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


  
TouchDesigner Build: Latest\n2023.11280before 2023.11280

CHOPs   
---  
[Ableton Link ](<./Ableton_Link_CHOP.md> "Ableton Link CHOP")• [Analyze ](<./Analyze_CHOP.md> "Analyze CHOP")• [Angle ](<./Angle_CHOP.md> "Angle CHOP")• [Attribute ](<./Attribute_CHOP.md> "Attribute CHOP")• [Audio Band EQ ](<./Audio_Band_EQ_CHOP.md> "Audio Band EQ CHOP")• [Audio Binaural ](<./Audio_Binaural_CHOP.md> "Audio Binaural CHOP")• [Audio Device In ](<./Audio_Device_In_CHOP.md> "Audio Device In CHOP")• [Audio Device Out ](<./Audio_Device_Out_CHOP.md> "Audio Device Out CHOP")• [Audio Dynamics ](<./Audio_Dynamics_CHOP.md> "Audio Dynamics CHOP")• [Audio File In ](<./Audio_File_In_CHOP.md> "Audio File In CHOP")• [Audio File Out ](<./Audio_File_Out_CHOP.md> "Audio File Out CHOP")• [Experimental:Audio File Out ](</Experimental:Audio_File_Out_CHOP> "Experimental:Audio File Out CHOP")• [Audio Filter ](<./Audio_Filter_CHOP.md> "Audio Filter CHOP")• [Audio Movie ](<./Audio_Movie_CHOP.md> "Audio Movie CHOP")• [Experimental:Audio Movie ](</Experimental:Audio_Movie_CHOP> "Experimental:Audio Movie CHOP")• [Audio NDI ](<./Audio_NDI_CHOP.md> "Audio NDI CHOP")• [Audio Oscillator ](<./Audio_Oscillator_CHOP.md> "Audio Oscillator CHOP")• [Audio Para EQ ](<./Audio_Para_EQ_CHOP.md> "Audio Para EQ CHOP")• [Audio Play ](<./Audio_Play_CHOP.md> "Audio Play CHOP")• [Audio Render ](<./Audio_Render_CHOP.md> "Audio Render CHOP")• [Experimental:Audio Render ](</Experimental:Audio_Render_CHOP> "Experimental:Audio Render CHOP")• [Audio Spectrum ](<./Audio_Spectrum_CHOP.md> "Audio Spectrum CHOP")• [Audio Stream In ](<./Audio_Stream_In_CHOP.md> "Audio Stream In CHOP")• [Audio Stream Out ](<./Audio_Stream_Out_CHOP.md> "Audio Stream Out CHOP")• [Audio VST ](<./Audio_VST_CHOP.md> "Audio VST CHOP")• [Audio Web Render ](<./Audio_Web_Render_CHOP.md> "Audio Web Render CHOP")• [Beat ](<./Beat_CHOP.md> "Beat CHOP")• [Bind ](<./Bind_CHOP.md> "Bind CHOP")• [BlackTrax ](<./BlackTrax_CHOP.md> "BlackTrax CHOP")• [Blend ](<./Blend_CHOP.md> "Blend CHOP")• [Blob Track ](<./Blob_Track_CHOP.md> "Blob Track CHOP")• [Body Track ](<./Body_Track_CHOP.md> "Body Track CHOP")• [Experimental:Body Track ](</Experimental:Body_Track_CHOP> "Experimental:Body Track CHOP")• [Bullet Solver ](<./Bullet_Solver_CHOP.md> "Bullet Solver CHOP")• [Clip Blender ](<./Clip_Blender_CHOP.md> "Clip Blender CHOP")• [Clip ](<./Clip_CHOP.md> "Clip CHOP")• [Clock ](<./Clock_CHOP.md> "Clock CHOP")• [Experimental:Clock ](</Experimental:Clock_CHOP> "Experimental:Clock CHOP")• [Composite ](<./Composite_CHOP.md> "Composite CHOP")• [Constant ](<./Constant_CHOP.md> "Constant CHOP")• [Copy ](<./Copy_CHOP.md> "Copy CHOP")• [Count ](<./Count_CHOP.md> "Count CHOP")• [CPlusPlus ](<./CPlusPlus_CHOP.md> "CPlusPlus CHOP")• [Cross ](<./Cross_CHOP.md> "Cross CHOP")• [Cycle ](<./Cycle_CHOP.md> "Cycle CHOP")• [DAT to ](<./DAT_to_CHOP.md> "DAT to CHOP")• [Delay ](<./Delay_CHOP.md> "Delay CHOP")• [Delete ](<./Delete_CHOP.md> "Delete CHOP")• [DMX In ](<./DMX_In_CHOP.md> "DMX In CHOP")• [DMX Out ](<./DMX_Out_CHOP.md> "DMX Out CHOP")• [Experimental:DMX Out ](</Experimental:DMX_Out_CHOP> "Experimental:DMX Out CHOP")• [Envelope ](<./Envelope_CHOP.md> "Envelope CHOP")• [EtherDream ](<./EtherDream_CHOP.md> "EtherDream CHOP")• [Event ](<./Event_CHOP.md> "Event CHOP")• [Expression ](<./Expression_CHOP.md> "Expression CHOP")• [Extend ](<./Extend_CHOP.md> "Extend CHOP")• [Face Track ](<./Face_Track_CHOP.md> "Face Track CHOP")• [Experimental:Face Track ](</Experimental:Face_Track_CHOP> "Experimental:Face Track CHOP")• [Fan ](<./Fan_CHOP.md> "Fan CHOP")• [Feedback ](<./Feedback_CHOP.md> "Feedback CHOP")• [File In ](<./File_In_CHOP.md> "File In CHOP")• [File Out ](<./File_Out_CHOP.md> "File Out CHOP")• [Filter ](<./Filter_CHOP.md> "Filter CHOP")• [Experimental:Filter ](</Experimental:Filter_CHOP> "Experimental:Filter CHOP")• [FreeD In ](<./FreeD_In_CHOP.md> "FreeD In CHOP")• [FreeD Out ](<./FreeD_Out_CHOP.md> "FreeD Out CHOP")• [Function ](<./Function_CHOP.md> "Function CHOP")• [Gesture ](<./Gesture_CHOP.md> "Gesture CHOP")• [Handle ](<./Handle_CHOP.md> "Handle CHOP")• [Helios DAC ](<./Helios_DAC_CHOP.md> "Helios DAC CHOP")• [Hog ](<./Hog_CHOP.md> "Hog CHOP")• [Hokuyo ](<./Hokuyo_CHOP.md> "Hokuyo CHOP")• [Hold ](<./Hold_CHOP.md> "Hold CHOP")• [Import Select ](<./Import_Select_CHOP.md> "Import Select CHOP")• [In ](<./In_CHOP.md> "In CHOP")• [Info ](<./Info_CHOP.md> "Info CHOP")• [Interpolate ](<./Interpolate_CHOP.md> "Interpolate CHOP")• [Introduction To s Vid ](<./Introduction_To_CHOPs_Vid.md> "Introduction To CHOPs Vid")• [Inverse Curve ](<./Inverse_Curve_CHOP.md> "Inverse Curve CHOP")• [Inverse Kin ](<./Inverse_Kin_CHOP.md> "Inverse Kin CHOP")• [Join ](<./Join_CHOP.md> "Join CHOP")• [Joystick ](<./Joystick_CHOP.md> "Joystick CHOP")• [Keyboard In ](<./Keyboard_In_CHOP.md> "Keyboard In CHOP")• [Keyframe ](<./Keyframe_CHOP.md> "Keyframe CHOP")• [Kinect Azure ](<./Kinect_Azure_CHOP.md> "Kinect Azure CHOP")• [Kinect ](<./Kinect_CHOP.md> "Kinect CHOP")• [Lag ](<./Lag_CHOP.md> "Lag CHOP")• [Laser ](<./Laser_CHOP.md> "Laser CHOP")• [Experimental:Laser ](</Experimental:Laser_CHOP> "Experimental:Laser CHOP")• [Laser Device ](<./Laser_Device_CHOP.md> "Laser Device CHOP")• [Experimental:Laser Device ](</Experimental:Laser_Device_CHOP> "Experimental:Laser Device CHOP")• [Leap Motion ](<./Leap_Motion_CHOP.md> "Leap Motion CHOP")• [Leuze ROD4 ](<./Leuze_ROD4_CHOP.md> "Leuze ROD4 CHOP")• [LFO ](<./LFO_CHOP.md> "LFO CHOP")• [Limit ](<./Limit_CHOP.md> "Limit CHOP")• [Logic ](<./Logic_CHOP.md> "Logic CHOP")• [Lookup ](<./Lookup_CHOP.md> "Lookup CHOP")• [LTC In ](<./LTC_In_CHOP.md> "LTC In CHOP")• [LTC Out ](<./LTC_Out_CHOP.md> "LTC Out CHOP")• [Math ](<./Math_CHOP.md> "Math CHOP")• [Merge ](<./Merge_CHOP.md> "Merge CHOP")• [MIDI In ](<./MIDI_In_CHOP.md> "MIDI In CHOP")• [MIDI In Map ](<./MIDI_In_Map_CHOP.md> "MIDI In Map CHOP")• [MIDI Out ](<./MIDI_Out_CHOP.md> "MIDI Out CHOP")• [MoSys ](<./MoSys_CHOP.md> "MoSys CHOP")• [Mouse In ](<./Mouse_In_CHOP.md> "Mouse In CHOP")• [Mouse Out ](<./Mouse_Out_CHOP.md> "Mouse Out CHOP")• [Ncam ](<./Ncam_CHOP.md> "Ncam CHOP")• [Noise ](<./Noise_CHOP.md> "Noise CHOP")• [Null ](<./Null_CHOP.md> "Null CHOP")• [OAK Device ](<./OAK_Device_CHOP.md> "OAK Device CHOP")• OAK Select • [Object ](<./Object_CHOP.md> "Object CHOP")• [Oculus Audio ](<./Oculus_Audio_CHOP.md> "Oculus Audio CHOP")• [Oculus Rift ](<./Oculus_Rift_CHOP.md> "Oculus Rift CHOP")• [OpenVR ](<./OpenVR_CHOP.md> "OpenVR CHOP")• [OptiTrack In ](<./OptiTrack_In_CHOP.md> "OptiTrack In CHOP")• [OSC In ](<./OSC_In_CHOP.md> "OSC In CHOP")• [OSC Out ](<./OSC_Out_CHOP.md> "OSC Out CHOP")• [Out ](<./Out_CHOP.md> "Out CHOP")• [Override ](<./Override_CHOP.md> "Override CHOP")• [Experimental:Pan Tilt ](</Experimental:Pan_Tilt_CHOP> "Experimental:Pan Tilt CHOP")• [Panel ](<./Panel_CHOP.md> "Panel CHOP")• [Pangolin ](<./Pangolin_CHOP.md> "Pangolin CHOP")• [Experimental:Pangolin ](</Experimental:Pangolin_CHOP> "Experimental:Pangolin CHOP")• [Parameter ](<./Parameter_CHOP.md> "Parameter CHOP")• [Experimental:Parameter ](</Experimental:Parameter_CHOP> "Experimental:Parameter CHOP")• [Pattern ](<./Pattern_CHOP.md> "Pattern CHOP")• [Perform ](<./Perform_CHOP.md> "Perform CHOP")• [Phaser ](<./Phaser_CHOP.md> "Phaser CHOP")• [Pipe In ](<./Pipe_In_CHOP.md> "Pipe In CHOP")• [Pipe Out ](<./Pipe_Out_CHOP.md> "Pipe Out CHOP")• [Experimental:POP to ](</Experimental:POP_to_CHOP> "Experimental:POP to CHOP")• [PosiStageNet ](<./PosiStageNet_CHOP.md> "PosiStageNet CHOP")• [Pulse ](<./Pulse_CHOP.md> "Pulse CHOP")• [RealSense ](<./RealSense_CHOP.md> "RealSense CHOP")• [Record ](<./Record_CHOP.md> "Record CHOP")• [Rename ](<./Rename_CHOP.md> "Rename CHOP")• [Render Pick ](<./Render_Pick_CHOP.md> "Render Pick CHOP")• [RenderStream In ](<./RenderStream_In_CHOP.md> "RenderStream In CHOP")• [Reorder ](<./Reorder_CHOP.md> "Reorder CHOP")• [Replace ](<./Replace_CHOP.md> "Replace CHOP")• [Resample ](<./Resample_CHOP.md> "Resample CHOP")• [Experimental:Resample ](</Experimental:Resample_CHOP> "Experimental:Resample CHOP")• [S Curve ](<./S_Curve_CHOP.md> "S Curve CHOP")• [Scan ](<./Scan_CHOP.md> "Scan CHOP")• [Script ](<./Script_CHOP.md> "Script CHOP")• [Experimental:Script ](</Experimental:Script_CHOP> "Experimental:Script CHOP")• [Select ](<./Select_CHOP.md> "Select CHOP")• [Sequencer ](<./Sequencer_CHOP.md> "Sequencer CHOP")• [Serial ](<./Serial_CHOP.md> "Serial CHOP")• [Shared Mem In ](<./Shared_Mem_In_CHOP.md> "Shared Mem In CHOP")• [Shared Mem Out ](<./Shared_Mem_Out_CHOP.md> "Shared Mem Out CHOP")• [Shift ](<./Shift_CHOP.md> "Shift CHOP")• [Shuffle ](<./Shuffle_CHOP.md> "Shuffle CHOP")• [Slope ](<./Slope_CHOP.md> "Slope CHOP")• [SOP to ](<./SOP_to_CHOP.md> "SOP to CHOP")• [Sort ](<./Sort_CHOP.md> "Sort CHOP")• [Speed ](<./Speed_CHOP.md> "Speed CHOP")• [Experimental:Speed ](</Experimental:Speed_CHOP> "Experimental:Speed CHOP")• [Splice ](<./Splice_CHOP.md> "Splice CHOP")• [Spring ](<./Spring_CHOP.md> "Spring CHOP")• [Experimental:ST2110 Device ](</Experimental:ST2110_Device_CHOP> "Experimental:ST2110 Device CHOP")• [Stretch ](<./Stretch_CHOP.md> "Stretch CHOP")• [Experimental:Stretch ](</Experimental:Stretch_CHOP> "Experimental:Stretch CHOP")• [Stype In ](<./Stype_In_CHOP.md> "Stype In CHOP")• [Stype Out ](<./Stype_Out_CHOP.md> "Stype Out CHOP")• [Switch ](<./Switch_CHOP.md> "Switch CHOP")• [Sync In ](<./Sync_In_CHOP.md> "Sync In CHOP")• [Sync Out ](<./Sync_Out_CHOP.md> "Sync Out CHOP")• [Tablet ](<./Tablet_CHOP.md> "Tablet CHOP")• [Time Slice ](<./Time_Slice_CHOP.md> "Time Slice CHOP")• [Timecode ](<./Timecode_CHOP.md> "Timecode CHOP")• [Experimental:Timecode ](</Experimental:Timecode_CHOP> "Experimental:Timecode CHOP")• [Timeline ](<./Timeline_CHOP.md> "Timeline CHOP")• [Timer ](<./Timer_CHOP.md> "Timer CHOP")• [Experimental:Timer ](</Experimental:Timer_CHOP> "Experimental:Timer CHOP")• [TOP to ](<./TOP_to_CHOP.md> "TOP to CHOP")• [Experimental:TOP to ](</Experimental:TOP_to_CHOP> "Experimental:TOP to CHOP")• [Touch In ](<./Touch_In_CHOP.md> "Touch In CHOP")• [Experimental:Touch In ](</Experimental:Touch_In_CHOP> "Experimental:Touch In CHOP")• [Touch Out ](<./Touch_Out_CHOP.md> "Touch Out CHOP")• [Trail ](<./Trail_CHOP.md> "Trail CHOP")• [Transform ](<./Transform_CHOP.md> "Transform CHOP")• [Transform XYZ ](<./Transform_XYZ_CHOP.md> "Transform XYZ CHOP")• [Trigger ](<./Trigger_CHOP.md> "Trigger CHOP")• [Experimental:Trigger ](</Experimental:Trigger_CHOP> "Experimental:Trigger CHOP")• [Trim ](<./Trim_CHOP.md> "Trim CHOP")• [Warp ](<./Warp_CHOP.md> "Warp CHOP")• [Wave ](<./Wave_CHOP.md> "Wave CHOP")• [WrnchAI ](<./WrnchAI_CHOP.md> "WrnchAI CHOP")• [ZED ](<./ZED_CHOP.md> "ZED CHOP")• [Experimental:ZED ](</Experimental:ZED_CHOP> "Experimental:ZED CHOP")  
  
### Script CHOP Functionality

The OAK Select CHOP mimics the [Script CHOP](<./Script_CHOP.md> "Script CHOP") in several ways. There's a callback for`onSetupParameters`, where custom parameters can be added. Also, in the other callbacks such as`onReceiveNNData`,`onReceiveBuffer`, and`onReceiveSystemInformation`it's possible to append channels and write data. When implementing a custom callback like below, if you want to disable time-slicing or set the number of output samples, the **Output Format** parameter should be "Items as Separate Samples". 
[code] 
    import depthai as dai
    def onReceiveNNData(oakSelectOp, oakNnData: dai.NNData):
        oakSelectOp.clear()
        oakSelectOp.appendChan('foo')
        oakSelectOp.numSamples = 1  # Output Format must be "Items as Separate Samples"
        oakSelectOp['foo'][0] = 42    
        return
    
[/code]

### Queue Size

The Queue Size parameter helps TouchDesigner avoid holding onto too many messages while also re-using memory for a minimum number of messages. For example, picking 2 is a good choice because TouchDesigner can show 1 message to the user while 1 remaining message can asynchronously be written to with new data. However, if the stream is meant to be high frame-rate, such as [IMU](<https://docs.luxonis.com/projects/api/en/latest/components/messages/imu_data/>) data, then the queue size should be at least double the number of messages you expect to receive in a single TouchDesigner frame. If TouchDesigner were to drop a video frame, then the next cook would want to use two times the number of messages that would have normally be shown, requiring the queue size to be at least twice as large. 

### Max Items

Some messages can be described as items. For example, [ImgDetections](<https://docs.luxonis.com/projects/api/en/latest/components/messages/img_detections/>) can be grouped into item0's channels, item1's channels, item2's channels and so on. For these kinds of streams, it can be helpful to have a constant number of channels in the OAK Select CHOP, regardless of whether an item exists in the most recent message. 

### Output Format

The default Output Format is "Items as Separate Channels". For example, when receiving [ImgDetections](<https://docs.luxonis.com/projects/api/en/latest/components/messages/img_detections/>) from MobileNet, each detection would require 6 channels ("confidence", "label", "xmin", "xmax", "ymin", "ymax"). The total number of channels would be 6 times the **Max Items** built-in parameter. In this situation, time-slicing is enabled, so the number of samples will vary according to time-slicing. 

If you're willing to sacrifice time-slicing, you can set the output format to "Items as Separate Samples". This will shuffle the latest messages into 6 channels by **Max Items** samples. In other words, each ImgDetection item will correspond to a CHOP sample. Another reason to use "Items as Separate Samples" is if you're implementing a callback such as`onReceiveNNData`and need to set the number of samples (`oakSelectOp.numSamples = 1`). 

### Use First Sample Only

Like the [Shuffle CHOP](<./Shuffle_CHOP.md> "Shuffle CHOP"), the **Use First Sample Only** parameter makes it easy to only use the most recently received message with the OAK Select CHOP. For example, an IMU stream might be sending very high-frame rate data, and toggling this parameter on would be like using a [Trim CHOP](<./Trim_CHOP.md> "Trim CHOP") in "Absolute" value mode to only show the latest sample. 

### Info CHOP

When an OAK Select CHOP is connected to an [Info CHOP](<./Info_CHOP.md> "Info CHOP"), in addition to the regular cook-related channels, there will be a few OAK-specific ones: 
* sequence_num: (see "sequenceNum" in the depthai [documentation](<https://docs.luxonis.com/projects/api/en/latest/components/messages/img_detections/>))
  * messages_received: the total number of messages received with stream name set on the OAK Select CHOP
  * fps: The effective frames-per-second of this stream, i.e., how quickly TouchDesigner is receiving messages. This is not the target FPS of the stream.

### See Also
* [OAK-D](<./OAK-D.md> "OAK-D")
  * [OAK Device CHOP](<./OAK_Device_CHOP.md> "OAK Device CHOP")
  * [OAK Select TOP](<./OAK_Select_TOP.md> "OAK Select TOP")
