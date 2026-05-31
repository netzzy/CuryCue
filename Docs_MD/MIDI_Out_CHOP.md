# MIDI Out CHOP

## 

Summary

The MIDI Out CHOP sends [MIDI](<./MIDI.md> "MIDI") events to any available MIDI devices when its input channels change. More flexibly, the Python [midioutCHOP Class](<./MidioutCHOP_Class.md> "MidioutCHOP Class") can be used to send any type of MIDI event to a MIDI device via an existing MIDI Out CHOP. In [Tscript](<./Tscript.md> "Tscript"), the`midi`command can output MIDI events. 

The MIDI devices can be other software programs (such as midisynth) or devices attached to the serial ports. Channels are used to control the sending of the MIDI events. The channels are evaluated over the last time slice (from the last [Timeline](<./Timeline.md> "Timeline") position to the current). 

The MIDI Out CHOP sends MIDI events based on any changes to its input channels. The channels have to be named appropriately, like`ch3c14`and`ch7n60`. 

An event is sent every time a channel changes its value during this slice. All timing is preserved, as long as the [Timeline](<./Timeline.md> "Timeline") is running in realtime (the "Realtime" flag is in the top menu bar). 

Naming the CHOP channels: Channels are mapped to events by their name. Events like notes, controllers and velocities must be followed by the note/controller number (n65, c7). If the number is left off a note event, the note number is the value of the channel. Other events, which are sent to the entire channel, do not need a trailing number (pc, pw). The channel prefix can be used to identify the MIDI channel the event should be sent on (i.e. "ch1n45" assigns that TouchDesigner channel to note 45 messages on MIDI channel 1). Channels can always be renamed with a [Rename CHOP](<./Rename_CHOP.md> "Rename CHOP") before entering the MIDI Out CHOP. 

The MIDI Out CHOP sends MIDI velocity as well. The values of the channels entering the MIDI Out CHOPs are sent as the velocity of the note. If Normalize is "None", the channel needs to be 0 to 127. If Normalize is "0 to 1", channel values between 0 and 1 are scaled to be MIDI 0 to 127. 

The "Cook Every Frame" option cooks the CHOP every frame, even if the CHOP isn't being displayed. All Volume Off and All Volume On flags are new and emit events for Controller 7 of all 16 channels. MIDI output go in a separate thread to allow output that slows TouchDesigner less. It now works in Time Slice mode for note events and controller events. (Not for Program Change or Sysex messages yet) Note channels only trigger anew Note On when the input channel goes from 0 or less to a value greater than zero. Similar for Note Off events.The channel name determines how it is interpreted. 

For example, 

    ch3n60 - this channel is interpreted as channel3 note 60. A Note On event is sent when the value goes from 0 or less to greater than zero
    ch5n - This channel will contain note numbers.¬† The value quantized to an integer, and when the integer value changes, the note of the old value goes off and the note of the new value goes on. If the channel steps from 53 to 78, it sends a Note Off event for note 53, and a Note On event for note 78.
    ch14c7 - the value of the channel is sent to controller 7 (volume) of channel 14. By default, the values 0 to 1 are mapped to MIDI value 0 to 127.

These features work in Time Slice mode: 

    By default, channels are to start with "ch" followed by the channel number (1-16). In the case of notes, it is followed by "n" for notes, then digits for the note number. In the case of controllers, it is followed by "c" and a controller number. These prefixes can be altered. MIDI Out now interprets aftertouch, pressure, pitchwheel channels, and outputs these events to the MIDI stream. Note-normalization is added allowing 0 to 127 and 0 to 1 ranges. MIDI Out reads a bar ramp channel to output MIDI clock events¬† (with a channel popup menu to the parameter to select the channel name). Program change events are implemented through the "pc" channels.both 7 and 14 bit controller events can be output. You can capture a MIDI stream and output it to a file.

See also the [MIDI In DAT](<./MIDI_In_DAT.md> "MIDI In DAT"), [MIDI Event DAT](<./MIDI_Event_DAT.md> "MIDI Event DAT"), [MIDI In Map CHOP](<./MIDI_In_Map_CHOP.md> "MIDI In Map CHOP"), [MIDI In CHOP](<./MIDI_In_CHOP.md> "MIDI In CHOP"),`midi`command. 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[midioutCHOP_Class](<./MidioutCHOP_Class.md> "MidioutCHOP Class")

## 

Parameters - Dest Page

Active`active`\- Enable or disable the MIDI Out CHOP. 

MIDI Destination`destination`\- ⊞ \- Where the MIDI events are sent to. MIDI Mapper is the default destination. 
* Device`device`-
* File`file`-


Device Table`device`\- Path to the MIDI device [Table DAT](<./Table_DAT.md> "Table DAT"). 

Device ID`id`\- Specify the id of which device to use. 

One Based Index`onebased`\- Make the index 1 based instead of the default 0 based. 

MIDI File`file`\- The filename of the output MIDI file. 

Write MIDI File`writefile`\- Writes all the data to a MIDI file. 

Channel Prefix`prefix`\- The prefix string that all input channels must have in order to extract the channel number from their name (i.e. "ch1note44", with a channel prefix of "ch"). 

Cook Every Frame`cookalways`\- Forces a cook of the CHOP every frame. It should be On because the MIDI Out CHOP will otherwise only cook if the CHOP leads to a graphics display viewer. You want it to cooks whether you are displaying anything or not. 

## 

Parameters - Output Page

Automatic Note Off`autonoteoff`\- ⊞ \- A MIDI 'All Note Off' event can be sent upon the start and/or end of the output. 
* None`none`-
* At Playback Start`start`-
* At Playback End`end`-
* At Playback Start and End`both`-


All Notes Off`reset`\- Sends an All Notes Off message to all MIDI channels. 

All Volume Off`volumeoff`\- Sends an All Notes Off message to all MIDI channels. 

All Volume On`volumeon`\- Sends an All Notes On message to all MIDI channels. 

Send Start/Stop/Continue Events`startstop`\- Sends the appropriate events when the framebar starts or stops. 

Send MIDI Timecode`sendmtc`\- While enabled, the MIDI Out CHOP will send MIDI Timecode (MTC) as a stream of quarter frame messages. 

Timecode Object/CHOP/DAT`timecodeop`\- The MIDI Timecode value to send. Should be a reference to either a CHOP with channels 'hour', 'second', 'minute', 'frame', a DAT with a timecode string in its first cell, or a [Timecode Class](<./Timecode_Class.md> "Timecode Class") object. 

## 

Parameters - Note Page

Note Name`notename`\- The base name of the note channels. If input channels have a number after the name, it is assumed to be the note number. If not, the channel value is assumed to contain the note number. 

Aftertouch Name`aftername`\- The name of the aftertouch channel. 

Pressure Name`pressname`\- The name of the channel pressure channel. 

Normalize`notenorm`\- ⊞ \- Values in the range 0-1 are mapped to MIDI value 0-127. 
* None`off`-
* 0 to 1`0to1`-


Pitch Wheel Name`pitchname`\- The name of the pitch wheel channel. 

## 

Parameters - Control Page

Controller Name`controlname`\- The base name of the controller channels. 

Controller Format`controlformat`\- ⊞ \- Sends 7 or 14 bit controller events. 
* 7 bit Controllers`7bit`-
* 14 bit Controllers`14bit`-


Normalize`controlnorm`\- ⊞ \- Maps channel values from different ranges to 0-127. 
* None`off`-
* 0 to 1`0to1`-
* -1 to 1`-1to1`-
* On/Off`onoff`-


Program Change`progname`\- The name of the program change channel. 

Bar Ramp Name`barname`\- Clock ticks frequency is determined by the period of the ramp. The ramp must be 0 to 1. An incoming channel name for a 0 to 1 ramp over each 4-beat bar. 

Ticks per Bar`barticks`\- Default is 96 = 4 beats * 24 ticks per beat. 

## 

Parameters - Common Page

Time Slice`timeslice`\- Turning this on forces the channels to be "[Time Sliced](<./Time_Slicing.md> "Time Slicing")". A Time Slice is the time between the last cook frame and the current cook frame. 

Scope`scope`\- To determine which channels get affected, some CHOPs use a Scope string on the Common page. See [Pattern Matching](<./Pattern_Matching.md> "Pattern Matching"). 

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

Rename from`commonrenamefrom`\- The channel pattern to rename. See [Pattern Matching](<./Pattern_Matching.md> "Pattern Matching"). 

Rename to`commonrenameto`\- The replacement pattern for the names. The default parameters do not rename the channels. See [Pattern Replacement](<./Pattern_Replacement.md> "Pattern Replacement"). 

**Example:**

    Channel Names:`c[1-10:2] ambient`Rename From:`c* ambient`Rename To:`b[1-5] amb`This example fetches channels`c1 c3 c5 c7 c9`and`ambient`. 

They are then renamed to to`b1 b2 b3 b4 b5`and`amb`. 

See the [Rename CHOP](<./Rename_CHOP.md> "Rename CHOP") for a further description of rename patterns. __

## 

Operator Inputs
* Input 0:  -

## 

Info CHOP Channels

Extra Information for the MIDI Out CHOP can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). 

### 

Specific MIDI Out CHOP Info Channels
* events_sent -

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


  
TouchDesigner Build: Latest\nwikieditor2021.100002018.28070before 2018.28070

CHOPs   
---  
[Ableton Link ](<./Ableton_Link_CHOP.md> "Ableton Link CHOP")• [Analyze ](<./Analyze_CHOP.md> "Analyze CHOP")• [Angle ](<./Angle_CHOP.md> "Angle CHOP")• [Attribute ](<./Attribute_CHOP.md> "Attribute CHOP")• [Audio Band EQ ](<./Audio_Band_EQ_CHOP.md> "Audio Band EQ CHOP")• [Audio Binaural ](<./Audio_Binaural_CHOP.md> "Audio Binaural CHOP")• [Audio Device In ](<./Audio_Device_In_CHOP.md> "Audio Device In CHOP")• [Audio Device Out ](<./Audio_Device_Out_CHOP.md> "Audio Device Out CHOP")• [Audio Dynamics ](<./Audio_Dynamics_CHOP.md> "Audio Dynamics CHOP")• [Audio File In ](<./Audio_File_In_CHOP.md> "Audio File In CHOP")• [Audio File Out ](<./Audio_File_Out_CHOP.md> "Audio File Out CHOP")• [Audio Filter ](<./Audio_Filter_CHOP.md> "Audio Filter CHOP")• [Audio Movie ](<./Audio_Movie_CHOP.md> "Audio Movie CHOP")• [Audio NDI ](<./Audio_NDI_CHOP.md> "Audio NDI CHOP")• [Audio Oscillator ](<./Audio_Oscillator_CHOP.md> "Audio Oscillator CHOP")• [Audio Para EQ ](<./Audio_Para_EQ_CHOP.md> "Audio Para EQ CHOP")• [Audio Play ](<./Audio_Play_CHOP.md> "Audio Play CHOP")• [Audio Render ](<./Audio_Render_CHOP.md> "Audio Render CHOP")• [Audio Spectrum ](<./Audio_Spectrum_CHOP.md> "Audio Spectrum CHOP")• [Audio Stream In ](<./Audio_Stream_In_CHOP.md> "Audio Stream In CHOP")• [Audio Stream Out ](<./Audio_Stream_Out_CHOP.md> "Audio Stream Out CHOP")• [Audio VST ](<./Audio_VST_CHOP.md> "Audio VST CHOP")• [Audio Web Render ](<./Audio_Web_Render_CHOP.md> "Audio Web Render CHOP")• [Beat ](<./Beat_CHOP.md> "Beat CHOP")• [Bind ](<./Bind_CHOP.md> "Bind CHOP")• [BlackTrax ](<./BlackTrax_CHOP.md> "BlackTrax CHOP")• [Blend ](<./Blend_CHOP.md> "Blend CHOP")• [Blob Track ](<./Blob_Track_CHOP.md> "Blob Track CHOP")• [Body Track ](<./Body_Track_CHOP.md> "Body Track CHOP")• [Bullet Solver ](<./Bullet_Solver_CHOP.md> "Bullet Solver CHOP")• [CHOP ](<./CHOP.md> "CHOP")• [Clip Blender ](<./Clip_Blender_CHOP.md> "Clip Blender CHOP")• [Clip ](<./Clip_CHOP.md> "Clip CHOP")• [Clock ](<./Clock_CHOP.md> "Clock CHOP")• [Composite ](<./Composite_CHOP.md> "Composite CHOP")• [Constant ](<./Constant_CHOP.md> "Constant CHOP")• [Copy ](<./Copy_CHOP.md> "Copy CHOP")• [Count ](<./Count_CHOP.md> "Count CHOP")• [CPlusPlus ](<./CPlusPlus_CHOP.md> "CPlusPlus CHOP")• [Cross ](<./Cross_CHOP.md> "Cross CHOP")• [Cycle ](<./Cycle_CHOP.md> "Cycle CHOP")• [DAT to ](<./DAT_to_CHOP.md> "DAT to CHOP")• [Delay ](<./Delay_CHOP.md> "Delay CHOP")• [Delete ](<./Delete_CHOP.md> "Delete CHOP")• [DMX In ](<./DMX_In_CHOP.md> "DMX In CHOP")• [DMX Out ](<./DMX_Out_CHOP.md> "DMX Out CHOP")• [Envelope ](<./Envelope_CHOP.md> "Envelope CHOP")• [EtherDream ](<./EtherDream_CHOP.md> "EtherDream CHOP")• [Event ](<./Event_CHOP.md> "Event CHOP")• [Expression ](<./Expression_CHOP.md> "Expression CHOP")• [Extend ](<./Extend_CHOP.md> "Extend CHOP")• [Face Track ](<./Face_Track_CHOP.md> "Face Track CHOP")• [Fan ](<./Fan_CHOP.md> "Fan CHOP")• [Feedback ](<./Feedback_CHOP.md> "Feedback CHOP")• [File In ](<./File_In_CHOP.md> "File In CHOP")• [File Out ](<./File_Out_CHOP.md> "File Out CHOP")• [Filter ](<./Filter_CHOP.md> "Filter CHOP")• [FreeD In ](<./FreeD_In_CHOP.md> "FreeD In CHOP")• [FreeD Out ](<./FreeD_Out_CHOP.md> "FreeD Out CHOP")• [Function ](<./Function_CHOP.md> "Function CHOP")• [Gesture ](<./Gesture_CHOP.md> "Gesture CHOP")• [Handle ](<./Handle_CHOP.md> "Handle CHOP")• [Helios DAC ](<./Helios_DAC_CHOP.md> "Helios DAC CHOP")• [Hog ](<./Hog_CHOP.md> "Hog CHOP")• [Hokuyo ](<./Hokuyo_CHOP.md> "Hokuyo CHOP")• [Hold ](<./Hold_CHOP.md> "Hold CHOP")• [Import Select ](<./Import_Select_CHOP.md> "Import Select CHOP")• [In ](<./In_CHOP.md> "In CHOP")• [Info ](<./Info_CHOP.md> "Info CHOP")• [Interpolate ](<./Interpolate_CHOP.md> "Interpolate CHOP")• [Introduction To s Vid ](<./Introduction_To_CHOPs_Vid.md> "Introduction To CHOPs Vid")• [Inverse Curve ](<./Inverse_Curve_CHOP.md> "Inverse Curve CHOP")• [Inverse Kin ](<./Inverse_Kin_CHOP.md> "Inverse Kin CHOP")• [Join ](<./Join_CHOP.md> "Join CHOP")• [Joystick ](<./Joystick_CHOP.md> "Joystick CHOP")• [Keyboard In ](<./Keyboard_In_CHOP.md> "Keyboard In CHOP")• [Keyframe ](<./Keyframe_CHOP.md> "Keyframe CHOP")• [Kinect Azure ](<./Kinect_Azure_CHOP.md> "Kinect Azure CHOP")• [Kinect ](<./Kinect_CHOP.md> "Kinect CHOP")• [Lag ](<./Lag_CHOP.md> "Lag CHOP")• [Laser ](<./Laser_CHOP.md> "Laser CHOP")• [Laser Device ](<./Laser_Device_CHOP.md> "Laser Device CHOP")• [Leap Motion ](<./Leap_Motion_CHOP.md> "Leap Motion CHOP")• [Leuze ROD4 ](<./Leuze_ROD4_CHOP.md> "Leuze ROD4 CHOP")• [LFO ](<./LFO_CHOP.md> "LFO CHOP")• [Limit ](<./Limit_CHOP.md> "Limit CHOP")• [Logic ](<./Logic_CHOP.md> "Logic CHOP")• [Lookup ](<./Lookup_CHOP.md> "Lookup CHOP")• [LTC In ](<./LTC_In_CHOP.md> "LTC In CHOP")• [LTC Out ](<./LTC_Out_CHOP.md> "LTC Out CHOP")• [Math ](<./Math_CHOP.md> "Math CHOP")• [Merge ](<./Merge_CHOP.md> "Merge CHOP")• [MIDI In ](<./MIDI_In_CHOP.md> "MIDI In CHOP")• [MIDI In Map ](<./MIDI_In_Map_CHOP.md> "MIDI In Map CHOP")• MIDI Out • [MoSys ](<./MoSys_CHOP.md> "MoSys CHOP")• [Mouse In ](<./Mouse_In_CHOP.md> "Mouse In CHOP")• [Mouse Out ](<./Mouse_Out_CHOP.md> "Mouse Out CHOP")• [Ncam ](<./Ncam_CHOP.md> "Ncam CHOP")• [Noise ](<./Noise_CHOP.md> "Noise CHOP")• [Null ](<./Null_CHOP.md> "Null CHOP")• [OAK Device ](<./OAK_Device_CHOP.md> "OAK Device CHOP")• [OAK Select ](<./OAK_Select_CHOP.md> "OAK Select CHOP")• [Object ](<./Object_CHOP.md> "Object CHOP")• [Oculus Audio ](<./Oculus_Audio_CHOP.md> "Oculus Audio CHOP")• [Oculus Rift ](<./Oculus_Rift_CHOP.md> "Oculus Rift CHOP")• [OpenVR ](<./OpenVR_CHOP.md> "OpenVR CHOP")• [OptiTrack In ](<./OptiTrack_In_CHOP.md> "OptiTrack In CHOP")• [OSC In ](<./OSC_In_CHOP.md> "OSC In CHOP")• [OSC Out ](<./OSC_Out_CHOP.md> "OSC Out CHOP")• [Out ](<./Out_CHOP.md> "Out CHOP")• [Override ](<./Override_CHOP.md> "Override CHOP")• [Pan Tilt ](<./Pan_Tilt_CHOP.md> "Pan Tilt CHOP")• [Panel ](<./Panel_CHOP.md> "Panel CHOP")• [Pangolin ](<./Pangolin_CHOP.md> "Pangolin CHOP")• [Parameter ](<./Parameter_CHOP.md> "Parameter CHOP")• [Pattern ](<./Pattern_CHOP.md> "Pattern CHOP")• [Perform ](<./Perform_CHOP.md> "Perform CHOP")• [Phaser ](<./Phaser_CHOP.md> "Phaser CHOP")• [Pipe In ](<./Pipe_In_CHOP.md> "Pipe In CHOP")• [Pipe Out ](<./Pipe_Out_CHOP.md> "Pipe Out CHOP")• [POP to ](<./POP_to_CHOP.md> "POP to CHOP")• [PosiStageNet ](<./PosiStageNet_CHOP.md> "PosiStageNet CHOP")• [Pulse ](<./Pulse_CHOP.md> "Pulse CHOP")• [RealSense ](<./RealSense_CHOP.md> "RealSense CHOP")• [Record ](<./Record_CHOP.md> "Record CHOP")• [Rename ](<./Rename_CHOP.md> "Rename CHOP")• [Render Pick ](<./Render_Pick_CHOP.md> "Render Pick CHOP")• [RenderStream In ](<./RenderStream_In_CHOP.md> "RenderStream In CHOP")• [Reorder ](<./Reorder_CHOP.md> "Reorder CHOP")• [Replace ](<./Replace_CHOP.md> "Replace CHOP")• [Resample ](<./Resample_CHOP.md> "Resample CHOP")• [S Curve ](<./S_Curve_CHOP.md> "S Curve CHOP")• [Scan ](<./Scan_CHOP.md> "Scan CHOP")• [Script ](<./Script_CHOP.md> "Script CHOP")• [Select ](<./Select_CHOP.md> "Select CHOP")• [Sequencer ](<./Sequencer_CHOP.md> "Sequencer CHOP")• [Serial ](<./Serial_CHOP.md> "Serial CHOP")• [Shared Mem In ](<./Shared_Mem_In_CHOP.md> "Shared Mem In CHOP")• [Shared Mem Out ](<./Shared_Mem_Out_CHOP.md> "Shared Mem Out CHOP")• [Shift ](<./Shift_CHOP.md> "Shift CHOP")• [Shuffle ](<./Shuffle_CHOP.md> "Shuffle CHOP")• [Slope ](<./Slope_CHOP.md> "Slope CHOP")• [SOP to ](<./SOP_to_CHOP.md> "SOP to CHOP")• [Sort ](<./Sort_CHOP.md> "Sort CHOP")• [Speed ](<./Speed_CHOP.md> "Speed CHOP")• [Splice ](<./Splice_CHOP.md> "Splice CHOP")• [Spring ](<./Spring_CHOP.md> "Spring CHOP")• [ST2110 Device ](<./ST2110_Device_CHOP.md> "ST2110 Device CHOP")• [Stretch ](<./Stretch_CHOP.md> "Stretch CHOP")• [Stype In ](<./Stype_In_CHOP.md> "Stype In CHOP")• [Stype Out ](<./Stype_Out_CHOP.md> "Stype Out CHOP")• [Switch ](<./Switch_CHOP.md> "Switch CHOP")• [Sync In ](<./Sync_In_CHOP.md> "Sync In CHOP")• [Sync Out ](<./Sync_Out_CHOP.md> "Sync Out CHOP")• [Tablet ](<./Tablet_CHOP.md> "Tablet CHOP")• [Time Slice ](<./Time_Slice_CHOP.md> "Time Slice CHOP")• [Timecode ](<./Timecode_CHOP.md> "Timecode CHOP")• [Timeline ](<./Timeline_CHOP.md> "Timeline CHOP")• [Timer ](<./Timer_CHOP.md> "Timer CHOP")• [TOP to ](<./TOP_to_CHOP.md> "TOP to CHOP")• [Touch In ](<./Touch_In_CHOP.md> "Touch In CHOP")• [Touch Out ](<./Touch_Out_CHOP.md> "Touch Out CHOP")• [Trail ](<./Trail_CHOP.md> "Trail CHOP")• [Transform ](<./Transform_CHOP.md> "Transform CHOP")• [Transform XYZ ](<./Transform_XYZ_CHOP.md> "Transform XYZ CHOP")• [Trigger ](<./Trigger_CHOP.md> "Trigger CHOP")• [Trim ](<./Trim_CHOP.md> "Trim CHOP")• [Warp ](<./Warp_CHOP.md> "Warp CHOP")• [Wave ](<./Wave_CHOP.md> "Wave CHOP")• [WrnchAI ](<./WrnchAI_CHOP.md> "WrnchAI CHOP")• [ZED ](<./ZED_CHOP.md> "ZED CHOP")
