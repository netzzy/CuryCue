# MIDI In CHOP

##   
  
Summary

The MIDI In CHOP reads Note events, Controller events, Program Change events, System Exclusive messages and Timing events from both MIDI devices and files. See also [MIDI In Map CHOP](<./MIDI_In_Map_CHOP.md> "MIDI In Map CHOP"). 

The MIDI In CHOP receives [MIDI](<./MIDI.md> "MIDI") events from MIDI devices connected to the serial port, reads MIDI events internal to the workstation (i.e. the built-in software synth), and interprets musical scores in MIDI files. Supported MIDI events are: 

    Note On, Note Off
    Polyphonic Aftertouch
    Channel Pressure
    Program Change
    Control Change (MIDI controller devices)
    Pitch Wheel
    Timer Events including beat pulses
    Bar Messages
    Start, Stop, Continue
    Song Position Pointer
    System Exclusive Messages

MIDI events arriving on separate MIDI channels may be recorded on separate CHOP channels. Also, any number of MIDI CHOPs can read from the same or different sources. TouchDesigner can be configured such that MIDI Start, Stop, or Continue events can control the [Timeline](<./Timeline.md> "Timeline") and [Beat Dialog](<./Beat_Dialog.md> "Beat Dialog"). 

The 'Simplified Output' option creates a channel for every type of MIDI event received, so number of channels expands while the devices is being used. No need to specify name, channel and index patterns. 

**Note** : The values of the MIDI inputs are saved into the TouchDesigner .toe file, and are restored when the file is reloaded. The physical controllers may be in a different position when the .toe is restarted, causing the values to jump when the controllers are moved. This is unavoidable. 

See also the [MIDI In DAT](<./MIDI_In_DAT.md> "MIDI In DAT"), [MIDI Event DAT](<./MIDI_Event_DAT.md> "MIDI Event DAT"), [MIDI In Map CHOP](<./MIDI_In_Map_CHOP.md> "MIDI In Map CHOP"), [MIDI Out CHOP](<./MIDI_Out_CHOP.md> "MIDI Out CHOP"). 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[midiinCHOP_Class](<./MidiinCHOP_Class.md> "MidiinCHOP Class")

## 

Parameters - Source Page

Active`active`\- Enable or disable the MIDI In CHOP. 

MIDI Source`source`\- ⊞ \- Get MIDI input from a device or a file. 
* Device`device`\- The MIDI events come live from a device.
* File`file`\- The MIDI events come from an existing file.


Device Table`device`\- Path to the MIDI device [Table DAT](<./Table_DAT.md> "Table DAT")

Device ID`id`\- Specify the id of which device to use. 

MIDI File`file`\- If MIDI file is selected as the MIDI source use this field to specify the name of the MIDI file to read. The file can be read in from disk or from the web. Use http:// when specifying a URL. 

Read Entire MIDI File`entire`\- If enabled, the entire MIDI file is read. Otherwise, the Start and End parameters on the Channel page determine the segment of the file to read. 

Reset Channels`resetchannels`\- Deletes all channels when set to On, new channels will not be added until Reset Channels is turned Off. 

Reset Channels Pulse`resetchannelspulse`\- Instantly deletes all channels. 

Reset Values`resetvalues`\- Resets all channel values to 0 when On, channel values will not be updated until Reset Values is turned Off. 

Reset Channels Pulse`resetchannelspulse`\- Instantly resets all channels to 0. 

Simplified Output`simplified`\- When this is on channels are automatically created when MIDI signal is detected from the selected MIDI device. 

Preserve Pulses`preservepulses`\- When on, quick value transitions (pulses) are spaced out over consecutive output samples. Use this option when pulse frequencies approach or exceed the timeline rate, otherwise they risk overlapping each other and being lost. 

1 Based Index`onebased`\- Make the index 1 based instead of the default 0 based. 

MIDI Channels`channel`\- The CHOP may read from any number of MIDI channels, numbered 1-16. Ranges and multiple entries are supported (i.e. "1 4 6", "1-7 12", "1-5:2"). 

    If Channel Prefix is left blank, then the input streams from multiple MIDI channels will be combined into one set of CHOP channels (i.e., a "note 64 on" event on channel 12 followed by a "note 64 off" event on channel 8 appears in the note 64 CHOP channel as a single note).

Channel Prefix`prefix`\- When recording from multiple MIDI channels, putting a string like "ch" in this parameter causes the MIDI channel to be split into separate CHOP channels per MIDI channel. Otherwise the MIDI channels are all merged into one set of CHOP channels. 

## 

Parameters - Record Page

The parameters here are only enabled when 'Simplied Output' on the Source Page is Off. 

Record Method`recordtype`\- ⊞ \- Determine what to record. 
* Single Frame`single`\- This only outputs the current value of notes, controllers, etc. It does not retain prior values. It creates a CHOP at frame 1 always, so the CHOP causes cooking only when MIDI events come in.
* Current Frame`current`\- Same as "Single Frame", but the CHOP frame is always at the current frame, so the CHOP changes every frame, causing other CHOPs to recook every frame.
* Current Time Slice`ind`\- The CHOP frame is always at the current [Time Slice](</index.php?title=Time_Slice&action=edit&redlink=1> "Time Slice \(page does not exist\)").
* Full Length`timeline`\- The entire length of the timeline is recorded.


Record`record`\- This parameter is used as a button to start and stop recording into the CHOP channels. 

## 

Parameters - Note Page

The parameters here are only enabled when 'Simplied Output' on the Source Page is Off. 

Note Name`notename`\- Put an "n" in here to generate channels for note events. It is the base name of the CHOP channel used to record notes. If blank, notes are ignored. If the Note Output parameter is set to Separate Channels, then CHOP channels will be created for each note in the Note Scope, of the form: notename 

Note Scope`notescope`\- The scope of notes to record. Multiple ranges and notes can be recorded (i.e., "50-60", "64 65 66 70-80"). 

Note Output`notemeth`\- ⊞ \- Describes how multiple notes are handled. (As one channel, or individual). 
* One Multiplexed Channel`mult`\- One CHOP channel per MIDI channel is used for all notes. The value in the note channel is the number of the note currently playing (in the case of multiple notes playing, the most recent note is selected).
* Separate Channels`sep`\- Each note number gets its own CHOP channel.


Velocity`velocity`\- ⊞ \- Describes how multiple velocity events are recorded. (Separate channels or combined in one channel as separate samples). 
* Off`veloff`\- Velocity is not recorded.
* Note Amplitude`velencode`\- The velocity is recorded as the amplitude of the note. Only valid when Note Output is set to Separate Channels.
* Separate Channels`velsep`\- Velocity is recorded in separate CHOP channels. Each note channel will have a corresponding velocity channel.


Velocity Name`velname`\- When Velocity is set to Separate Channels, this parameter is the base name of the Velocity CHOP channel (try "v"). If blank, no velocity channels will be recorded. 

Aftertouch Name`aftername`\- The base name of the polyphonic Aftertouch CHOP channels. One aftertouch channel is created for each note in the Note Scope. If blank, no aftertouch channels will be created. 

Pressure Name`pressname`\- The name of the Channel Pressure channel. If multiple channels are being recorded, all channel pressure changes of interest will be recording on this CHOP channel. If blank, this channel will not be created. 

Normalize`notenorm`\- ⊞ \- Note values can be normalized for convenience: 
* None`off`\- When Normalize is Off, 7 bit controllers will return values in the range 0-127 and 14 bit controllers will return values in the range 0-16383.
* 0 to 1`0to1`\- These values are normalized to lie in the range 0 to 1.


Pitch Wheel Name`pitchname`\- The name of the Pitch Wheel CHOP channel. Pitch wheel values range from -1 to +1. If blank, this channel will not be created. Put "p" in here to generate a channel. 

## 

Parameters - Control Page

The parameters here are only enabled when 'Simplied Output' on the Source Page is Off. 

Controller Name`controlname`\- The base name of the Control Change CHOP channels. The channel names are appended with the controller index (0-127). If blank, control changes will not be recorded. It typically contains "c". 

Controller Type`controltype`\- ⊞ \- There are 128 different controllers available. By choosing By Index Only, you can specify any number of controllers in the Control Index parameter. Otherwise, you can select a controller from the list from this menu. Some controllers have multiple instances, such as Sound Controllers 1-10. Selecting a controller with multiple instances allows you to use the Control Index parameter to select which instances you want. Any invalid control indices will be ignored. 
* By Index Only`index`\- Specify the controller by its index, as opposed to specifying a specific type below.
* Bank Select`n0`-
* Modulation Wheel`n1`-
* Breath Control`n2`-
* Foot Controller`n3`-
* Portamento Time`n4`-
* Data Entry`n5`-
* Channel Volume`n6`-
* Balance`n7`-
* Pan`n8`-
* Expression Control`n9`-
* Effect Control 1-2`n10`-
* 14 bit General Purpose 1-4`n11`-
* Sustain on/off`n12`-
* Portamento on/off`n13`-
* Sustenuto on/off`n14`-
* Soft Pedal on/off`n15`-
* Legato Footswitch on/off`n16`-
* Hold 2 on/off`n17`-
* Sound Controller 1-10`n18`-
* 7 bit General Purpose 5-8`n19`-
* Portamento Control`n20`-
* Effect Depth 1-5`n21`-
* Non-Registered Parameter`n22`-
* Registered Parameter`n23`-


Controller Index`controlind`\- Used to select controllers by number, or multiple controllers by ranges. When in By Index Only Controller Type mode, you can select up to the full 128 controllers or sub-ranges thereof (i.e. "1-10", "2 34 70", "1-32 70-80:2"). 

Controller Format`format`\- ⊞ \- Some controllers can be paired together to form 14 bit controllers, rather than the normal 7 bit controllers (controller indices 0-31, 98 and 100). Selecting 14 bit Controllers interprets a pair as one 14 bit controller. Otherwise, they are interpreted as separate 7 bit Controllers. 
* 7 bit Controllers`7bit`\- Controllers are assumed to be regular 7 bit value messages.
* 14 bit Controllers`14bit`\- Controllers are received as two 7 bit value messages.


Normalize`norm`\- ⊞ \- Controller values can be normalized for convenience: 
* None`off`\- When Normalize is Off, 7 bit controllers will return values in the range 0-127 and 14 bit controllers will return values in the range 0-16383.
* 0 to 1`0to1`\- These values are normalized to lie in the range 0 to 1.
* -1 to 1`-1to1`\- These values are normalized to lie in the range -1 to +1.
* On/Off`onoff`\- Several of the controllers are simply on/off states. When Convert to On/Off is enabled, values greater than or equal to 64 will be interpreted as "1" and all values less than 64 will be interpreted as "0".


Unwrap`unwrap`\- When on, values do not jump between min and max, but are modified to be continuous ramps. Use with knob controllers for examples. 

Program Change`progname`\- The name of the Program Change CHOP channel. All program change messages will be recorded onto this channel. If blank, this channel will not be created. 

## 

Parameters - Timer Page

The parameters here are only enabled when 'Simplied Output' on the Source Page is Off. 

Timer Pulse Name`pulsename`\- Record timer pulse messages. 

Timer Ramp Name`rampname`\- Record timer ramp messages. 

Timer Period`timerperiod`\- Record timer period messages. 

Timer Start`timerstart`\- Record timer start messages. 

Ticks per Beat`ticks`\- Specify the expected ticks per beat. This will influence the timer and bar output values. 

Bar Ramp Name`barname`\- Output the current bar position. 

Bar Period`barperiod`\- Output the current bar period events. 

Bar Start`barstart`\- Output when a bar starts. 

Bar Message`barmsg`\- Capture bar messages. Place a V in the message to specify which value the channel should have. 

Song Pos Name`songpos`\- Capture song position messages. 

## 

Parameters - Sys Page

The parameters here are only enabled when 'Simplied Output' on the Source Page is Off. 

System Exclusive`sysex`\- Sequence of system exclusive message handlers 

Channel Name`sysex0name`\- Name of a specific exclusive message to be captured. 

Message`sysex0msg`\- Contents of the exclusive message. Place a V in the message to specify which value the channel should have. 

## 

Parameters - Chan Page

This is similar to other generators' Channel page. However, there are a few points to consider on how they affect the Midi In CHOP. 

Start`start`\- Defines where recording begins. In "Tie to Time Line" mode, any events received before the start time will be ignored. In "Time Line Independent" mode, recording will start at this point and continue on (not looping back). If reading from a MIDI File, Start/End will determine the start of the segment to read. 

Start and end of the interval, expressed in Units (seconds, frames or samples). The parameters are expressed in the`Units`found on the Common page. To set the CHOP to be 100 samples long, Set`Units`to Samples,`Single Frame`Off and`Start`/`End`to 0 and 99. __

Start Unit`startunit`\- ⊞ \- Select the units to use for this parameter, Samples, Frames, or Seconds. 
* I`samples`\- Use samples.
* F`frames`\- Use frames.
* S`seconds`\- Use seconds.


End`end`\- Defines the end of the segment to read for MIDI Files. 

End Unit`endunit`\- ⊞ \- Select the units to use for this parameter, Samples, Frames, or Seconds. 
* I`samples`\- Use samples.
* F`frames`\- Use frames.
* S`seconds`\- Use seconds.


Sample Rate`rate`\- Defines the sample rate of this CHOP, in samples per second. If the sample rate is too low, a rapidly changing input may be misrepresented. 

**Note** : If the sample rate is too low, you may miss MIDI events. A note event may set a sample value to 1, and then the next note event less than 1/30 second later can set it to 0 on the same sample in the CHOP channel. So the event will be missed. Make the sample rate higher, like 600, to catch these events, or make sure that your on-off events coming in are a minimum time separation, as can be achieved through Opcode's MAX. __

Extend Left`left`\- ⊞ \- The left extend conditions (before range). 
* Hold`hold`\- Hold the current value of the channel.
* Slope`slope`\- Continue the slope before the start of the channel.
* Cycle`cycle`\- Cycle the channel repeatedly.
* Mirror`mirror`\- Cycle the channel repeatedly, mirroring every other cycle.
* Default Value`default`\- Use the constant value specified in the Default Value parameter.


Extend Right`right`\- ⊞ \- The right extend conditions (after range). 
* Hold`hold`\- Hold the current value of the channel.
* Slope`slope`\- Continue the slope after the end of the channel.
* Cycle`cycle`\- Cycle the channel repeatedly.
* Mirror`mirror`\- Cycle the channel repeatedly, mirroring every other cycle.
* Default Value`default`\- Use the constant value specified in the Default Value parameter.


Default Value`defval`\- The value used for the Default Value extend condition. 

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

Extra Information for the MIDI In CHOP can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). __

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


  
TouchDesigner Build: Latest\nwikieditorwikieditorwikieditor2021.100002020.236802020.200002018.28070before 2018.28070

CHOPs   
---  
[Ableton Link ](<./Ableton_Link_CHOP.md> "Ableton Link CHOP")• [Analyze ](<./Analyze_CHOP.md> "Analyze CHOP")• [Angle ](<./Angle_CHOP.md> "Angle CHOP")• [Attribute ](<./Attribute_CHOP.md> "Attribute CHOP")• [Audio Band EQ ](<./Audio_Band_EQ_CHOP.md> "Audio Band EQ CHOP")• [Audio Binaural ](<./Audio_Binaural_CHOP.md> "Audio Binaural CHOP")• [Audio Device In ](<./Audio_Device_In_CHOP.md> "Audio Device In CHOP")• [Audio Device Out ](<./Audio_Device_Out_CHOP.md> "Audio Device Out CHOP")• [Audio Dynamics ](<./Audio_Dynamics_CHOP.md> "Audio Dynamics CHOP")• [Audio File In ](<./Audio_File_In_CHOP.md> "Audio File In CHOP")• [Audio File Out ](<./Audio_File_Out_CHOP.md> "Audio File Out CHOP")• [Audio Filter ](<./Audio_Filter_CHOP.md> "Audio Filter CHOP")• [Audio Movie ](<./Audio_Movie_CHOP.md> "Audio Movie CHOP")• [Audio NDI ](<./Audio_NDI_CHOP.md> "Audio NDI CHOP")• [Audio Oscillator ](<./Audio_Oscillator_CHOP.md> "Audio Oscillator CHOP")• [Audio Para EQ ](<./Audio_Para_EQ_CHOP.md> "Audio Para EQ CHOP")• [Audio Play ](<./Audio_Play_CHOP.md> "Audio Play CHOP")• [Audio Render ](<./Audio_Render_CHOP.md> "Audio Render CHOP")• [Audio Spectrum ](<./Audio_Spectrum_CHOP.md> "Audio Spectrum CHOP")• [Audio Stream In ](<./Audio_Stream_In_CHOP.md> "Audio Stream In CHOP")• [Audio Stream Out ](<./Audio_Stream_Out_CHOP.md> "Audio Stream Out CHOP")• [Audio VST ](<./Audio_VST_CHOP.md> "Audio VST CHOP")• [Audio Web Render ](<./Audio_Web_Render_CHOP.md> "Audio Web Render CHOP")• [Beat ](<./Beat_CHOP.md> "Beat CHOP")• [Bind ](<./Bind_CHOP.md> "Bind CHOP")• [BlackTrax ](<./BlackTrax_CHOP.md> "BlackTrax CHOP")• [Blend ](<./Blend_CHOP.md> "Blend CHOP")• [Blob Track ](<./Blob_Track_CHOP.md> "Blob Track CHOP")• [Body Track ](<./Body_Track_CHOP.md> "Body Track CHOP")• [Bullet Solver ](<./Bullet_Solver_CHOP.md> "Bullet Solver CHOP")• [CHOP ](<./CHOP.md> "CHOP")• [Clip Blender ](<./Clip_Blender_CHOP.md> "Clip Blender CHOP")• [Clip ](<./Clip_CHOP.md> "Clip CHOP")• [Clock ](<./Clock_CHOP.md> "Clock CHOP")• [Composite ](<./Composite_CHOP.md> "Composite CHOP")• [Constant ](<./Constant_CHOP.md> "Constant CHOP")• [Copy ](<./Copy_CHOP.md> "Copy CHOP")• [Count ](<./Count_CHOP.md> "Count CHOP")• [CPlusPlus ](<./CPlusPlus_CHOP.md> "CPlusPlus CHOP")• [Cross ](<./Cross_CHOP.md> "Cross CHOP")• [Cycle ](<./Cycle_CHOP.md> "Cycle CHOP")• [DAT to ](<./DAT_to_CHOP.md> "DAT to CHOP")• [Delay ](<./Delay_CHOP.md> "Delay CHOP")• [Delete ](<./Delete_CHOP.md> "Delete CHOP")• [DMX In ](<./DMX_In_CHOP.md> "DMX In CHOP")• [DMX Out ](<./DMX_Out_CHOP.md> "DMX Out CHOP")• [Envelope ](<./Envelope_CHOP.md> "Envelope CHOP")• [EtherDream ](<./EtherDream_CHOP.md> "EtherDream CHOP")• [Event ](<./Event_CHOP.md> "Event CHOP")• [Expression ](<./Expression_CHOP.md> "Expression CHOP")• [Extend ](<./Extend_CHOP.md> "Extend CHOP")• [Face Track ](<./Face_Track_CHOP.md> "Face Track CHOP")• [Fan ](<./Fan_CHOP.md> "Fan CHOP")• [Feedback ](<./Feedback_CHOP.md> "Feedback CHOP")• [File In ](<./File_In_CHOP.md> "File In CHOP")• [File Out ](<./File_Out_CHOP.md> "File Out CHOP")• [Filter ](<./Filter_CHOP.md> "Filter CHOP")• [FreeD In ](<./FreeD_In_CHOP.md> "FreeD In CHOP")• [FreeD Out ](<./FreeD_Out_CHOP.md> "FreeD Out CHOP")• [Function ](<./Function_CHOP.md> "Function CHOP")• [Gesture ](<./Gesture_CHOP.md> "Gesture CHOP")• [Handle ](<./Handle_CHOP.md> "Handle CHOP")• [Helios DAC ](<./Helios_DAC_CHOP.md> "Helios DAC CHOP")• [Hog ](<./Hog_CHOP.md> "Hog CHOP")• [Hokuyo ](<./Hokuyo_CHOP.md> "Hokuyo CHOP")• [Hold ](<./Hold_CHOP.md> "Hold CHOP")• [Import Select ](<./Import_Select_CHOP.md> "Import Select CHOP")• [In ](<./In_CHOP.md> "In CHOP")• [Info ](<./Info_CHOP.md> "Info CHOP")• [Interpolate ](<./Interpolate_CHOP.md> "Interpolate CHOP")• [Introduction To s Vid ](<./Introduction_To_CHOPs_Vid.md> "Introduction To CHOPs Vid")• [Inverse Curve ](<./Inverse_Curve_CHOP.md> "Inverse Curve CHOP")• [Inverse Kin ](<./Inverse_Kin_CHOP.md> "Inverse Kin CHOP")• [Join ](<./Join_CHOP.md> "Join CHOP")• [Joystick ](<./Joystick_CHOP.md> "Joystick CHOP")• [Keyboard In ](<./Keyboard_In_CHOP.md> "Keyboard In CHOP")• [Keyframe ](<./Keyframe_CHOP.md> "Keyframe CHOP")• [Kinect Azure ](<./Kinect_Azure_CHOP.md> "Kinect Azure CHOP")• [Kinect ](<./Kinect_CHOP.md> "Kinect CHOP")• [Lag ](<./Lag_CHOP.md> "Lag CHOP")• [Laser ](<./Laser_CHOP.md> "Laser CHOP")• [Laser Device ](<./Laser_Device_CHOP.md> "Laser Device CHOP")• [Leap Motion ](<./Leap_Motion_CHOP.md> "Leap Motion CHOP")• [Leuze ROD4 ](<./Leuze_ROD4_CHOP.md> "Leuze ROD4 CHOP")• [LFO ](<./LFO_CHOP.md> "LFO CHOP")• [Limit ](<./Limit_CHOP.md> "Limit CHOP")• [Logic ](<./Logic_CHOP.md> "Logic CHOP")• [Lookup ](<./Lookup_CHOP.md> "Lookup CHOP")• [LTC In ](<./LTC_In_CHOP.md> "LTC In CHOP")• [LTC Out ](<./LTC_Out_CHOP.md> "LTC Out CHOP")• [Math ](<./Math_CHOP.md> "Math CHOP")• [Merge ](<./Merge_CHOP.md> "Merge CHOP")• MIDI In • [MIDI In Map ](<./MIDI_In_Map_CHOP.md> "MIDI In Map CHOP")• [MIDI Out ](<./MIDI_Out_CHOP.md> "MIDI Out CHOP")• [MoSys ](<./MoSys_CHOP.md> "MoSys CHOP")• [Mouse In ](<./Mouse_In_CHOP.md> "Mouse In CHOP")• [Mouse Out ](<./Mouse_Out_CHOP.md> "Mouse Out CHOP")• [Ncam ](<./Ncam_CHOP.md> "Ncam CHOP")• [Noise ](<./Noise_CHOP.md> "Noise CHOP")• [Null ](<./Null_CHOP.md> "Null CHOP")• [OAK Device ](<./OAK_Device_CHOP.md> "OAK Device CHOP")• [OAK Select ](<./OAK_Select_CHOP.md> "OAK Select CHOP")• [Object ](<./Object_CHOP.md> "Object CHOP")• [Oculus Audio ](<./Oculus_Audio_CHOP.md> "Oculus Audio CHOP")• [Oculus Rift ](<./Oculus_Rift_CHOP.md> "Oculus Rift CHOP")• [OpenVR ](<./OpenVR_CHOP.md> "OpenVR CHOP")• [OptiTrack In ](<./OptiTrack_In_CHOP.md> "OptiTrack In CHOP")• [OSC In ](<./OSC_In_CHOP.md> "OSC In CHOP")• [OSC Out ](<./OSC_Out_CHOP.md> "OSC Out CHOP")• [Out ](<./Out_CHOP.md> "Out CHOP")• [Override ](<./Override_CHOP.md> "Override CHOP")• [Pan Tilt ](<./Pan_Tilt_CHOP.md> "Pan Tilt CHOP")• [Panel ](<./Panel_CHOP.md> "Panel CHOP")• [Pangolin ](<./Pangolin_CHOP.md> "Pangolin CHOP")• [Parameter ](<./Parameter_CHOP.md> "Parameter CHOP")• [Pattern ](<./Pattern_CHOP.md> "Pattern CHOP")• [Perform ](<./Perform_CHOP.md> "Perform CHOP")• [Phaser ](<./Phaser_CHOP.md> "Phaser CHOP")• [Pipe In ](<./Pipe_In_CHOP.md> "Pipe In CHOP")• [Pipe Out ](<./Pipe_Out_CHOP.md> "Pipe Out CHOP")• [POP to ](<./POP_to_CHOP.md> "POP to CHOP")• [PosiStageNet ](<./PosiStageNet_CHOP.md> "PosiStageNet CHOP")• [Pulse ](<./Pulse_CHOP.md> "Pulse CHOP")• [RealSense ](<./RealSense_CHOP.md> "RealSense CHOP")• [Record ](<./Record_CHOP.md> "Record CHOP")• [Rename ](<./Rename_CHOP.md> "Rename CHOP")• [Render Pick ](<./Render_Pick_CHOP.md> "Render Pick CHOP")• [RenderStream In ](<./RenderStream_In_CHOP.md> "RenderStream In CHOP")• [Reorder ](<./Reorder_CHOP.md> "Reorder CHOP")• [Replace ](<./Replace_CHOP.md> "Replace CHOP")• [Resample ](<./Resample_CHOP.md> "Resample CHOP")• [S Curve ](<./S_Curve_CHOP.md> "S Curve CHOP")• [Scan ](<./Scan_CHOP.md> "Scan CHOP")• [Script ](<./Script_CHOP.md> "Script CHOP")• [Select ](<./Select_CHOP.md> "Select CHOP")• [Sequencer ](<./Sequencer_CHOP.md> "Sequencer CHOP")• [Serial ](<./Serial_CHOP.md> "Serial CHOP")• [Shared Mem In ](<./Shared_Mem_In_CHOP.md> "Shared Mem In CHOP")• [Shared Mem Out ](<./Shared_Mem_Out_CHOP.md> "Shared Mem Out CHOP")• [Shift ](<./Shift_CHOP.md> "Shift CHOP")• [Shuffle ](<./Shuffle_CHOP.md> "Shuffle CHOP")• [Slope ](<./Slope_CHOP.md> "Slope CHOP")• [SOP to ](<./SOP_to_CHOP.md> "SOP to CHOP")• [Sort ](<./Sort_CHOP.md> "Sort CHOP")• [Speed ](<./Speed_CHOP.md> "Speed CHOP")• [Splice ](<./Splice_CHOP.md> "Splice CHOP")• [Spring ](<./Spring_CHOP.md> "Spring CHOP")• [ST2110 Device ](<./ST2110_Device_CHOP.md> "ST2110 Device CHOP")• [Stretch ](<./Stretch_CHOP.md> "Stretch CHOP")• [Stype In ](<./Stype_In_CHOP.md> "Stype In CHOP")• [Stype Out ](<./Stype_Out_CHOP.md> "Stype Out CHOP")• [Switch ](<./Switch_CHOP.md> "Switch CHOP")• [Sync In ](<./Sync_In_CHOP.md> "Sync In CHOP")• [Sync Out ](<./Sync_Out_CHOP.md> "Sync Out CHOP")• [Tablet ](<./Tablet_CHOP.md> "Tablet CHOP")• [Time Slice ](<./Time_Slice_CHOP.md> "Time Slice CHOP")• [Timecode ](<./Timecode_CHOP.md> "Timecode CHOP")• [Timeline ](<./Timeline_CHOP.md> "Timeline CHOP")• [Timer ](<./Timer_CHOP.md> "Timer CHOP")• [TOP to ](<./TOP_to_CHOP.md> "TOP to CHOP")• [Touch In ](<./Touch_In_CHOP.md> "Touch In CHOP")• [Touch Out ](<./Touch_Out_CHOP.md> "Touch Out CHOP")• [Trail ](<./Trail_CHOP.md> "Trail CHOP")• [Transform ](<./Transform_CHOP.md> "Transform CHOP")• [Transform XYZ ](<./Transform_XYZ_CHOP.md> "Transform XYZ CHOP")• [Trigger ](<./Trigger_CHOP.md> "Trigger CHOP")• [Trim ](<./Trim_CHOP.md> "Trim CHOP")• [Warp ](<./Warp_CHOP.md> "Warp CHOP")• [Wave ](<./Wave_CHOP.md> "Wave CHOP")• [WrnchAI ](<./WrnchAI_CHOP.md> "WrnchAI CHOP")• [ZED ](<./ZED_CHOP.md> "ZED CHOP")
