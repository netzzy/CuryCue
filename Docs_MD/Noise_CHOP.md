# Noise CHOP

## 

Summary

The Noise CHOP makes an irregular wave that never repeats, with values approximately in the range -1 to +1. 

It generates both smooth curves and noise that is random each sample. It uses the same math as the [Noise SOP](<./Noise_SOP.md> "Noise SOP"). 

You can create several curves with different shapes, and you can adjust period, amplitude, harmonics and more. 

Optionally, an input can be connected. It is assumed that the input contains 1 to 3 channels representing X, Y and Z coordinates of points in space, and are used to sample anywhere in 3D noise space. One index in the input produces one sample in the output. 

All noise functions work identically with [Time Slicing](<./Time_Slicing.md> "Time Slicing") on and off, with the exception of Harmonic Summation and Brownian whose methods cannot be limited to 1 in Time Slice mode. When the [Timeline](<./Timeline.md> "Timeline") wraps around to frame 1, the noise functions will continue uninterrupted. 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[noiseCHOP_Class](<./NoiseCHOP_Class.md> "NoiseCHOP Class")

## 

Parameters - Noise Page

Type`type`\- ⊞ \- The noise function used to generate noise. The functions available are: 
* Sparse`sparse`\- Produces high quality, continuous noise based on Sparse Convolution.
* Hermite`hermite`\- Quicker than Sparse, but produces lower quality noise.
* Harmomic Summation`harmonic`\- Sparse noise with the ability to control the frequency step of the harmonics. Slowest type.
* Brownian`brownian`\- Works like a bug in random flight. With Num of Integrals at 2, its acceleration is changed randomly every frame.
* Random`random`\- (White Noise) Every sample is random and unrelated to any other sample. It is the same as "white noise" in audio.
* Alligator`alligator`\- Cell Noise.


Seed`seed`\- Any number, integer or non-integer, which starts the random number generator. Each number gives completely different noise patterns, but with similar characteristics. 

Period`period`\- The approximate separation between peaks of a noise cycle. It is expressed in Units. Increasing the period stretches the noise pattern out. 

Period is the opposite of frequency. If the period is 2 seconds, the base frequency is 0.5 cycles per second, or 0.5Hz for short. Hz refers to Hertz, the electrical and audio engineer of the 19th century, not the car guy. 

If the Type is set to Random, setting this to zero will produce completely random noise. Otherwise, the period should be greater than zero. __

Period Unit`periodunit`\- Select the units to use for this parameter, Samples, Frames, Seconds, or Fraction. 

Harmonics`harmon`\- The number of higher frequency components to layer on top of the base frequency. The higher this number, the bumpier the noise will be (as long as roughness is not set to zero). 0 harmonics give the base shape. 

Harmonics with a base frequency of 0.1Hz will by default produce harmonics at 0.2Hz, 0.4Hz, 0.8Hz, etc. (up to the number of harmonics specified by the Harmonics parameter). __

Harmonic Spread`spread`\- The factor by which the frequency of the harmonics are increased. It is normally 2. A spread of 3 and a base frequency of 0.1Hz will produce harmonics at 0.3Hz, 0.9Hz, 2.7Hz, etc. This parameter is only valid for the Harmonic Summation type. 

Roughness`rough`\- Controls the effect of the higher frequency noise. When roughness is zero, all harmonics above the base frequency have no effect. At one, all harmonics are equal in amplitude to the base frequency. When roughness is between one and zero, the amplitude of higher harmonics drops off exponentially from the base frequency. 

The default roughness is 0.5. This means the amplitude of the first harmonic is 0.5 of the base frequency, the second is 0.25, the third is 0.125. The harmonics are added to the base to give the final shape. The Harmonics parameter and the Roughness parameter must both be non-zero to see the harmonic effects. __

Exponent`exp`\- Pushes the noise values toward 0, or +1 and -1. (It raises the value to the power of the exponent.) Exponents greater than one will pull the channel toward zero, and powers less than one will pull peaks towards +1 and -1. It is used to reshape the channels. 

Num of Integrals`numint`\- Defines the number of times to integrate (see the Area CHOP p. 114) the Brownian noise. Higher values produce smoother curves with fewer features. Values beyond 4 produce somewhat identical curves. This parameter is only valid for the Random noise type. 

Amplitude`amp`\- Defines the noise value's amplitude (a scale on the values output). 

Reset`reset`\- Only available if operator's`Time Slice`Parameter is on. Toggling this parameter will reset the noise calculation and hold the value until the parameter is released again. 

Reset Pulse`resetpulse`\- Only available if operator's`Time Slice`Parameter is on. Pulsing this parameter will reset the noise calculation. 

## 

Parameters - Transform Page

The Translate, Rotate, Scale and Pivot parameters let you sample in a different part of the 3D noise space. Imagine a different noise value for every XYZ point in space. Normally, the Noise CHOP samples the noise space from (0,0,0) along the X-axis in steps of 2/period.`/tx /ty /tz /rx /ry /rx /sx /sy /sz /px /py /pz`By changing the transform, you are translating, rotating and scaling the line along which the Noise CHOPs samples the noise space. A slight Y-rotation is like walking in a straight path in the mountains, recording your altitude along the way, then re-starting from the same initial location, walking in a slightly different direction. Your altitude starts off being similar but then diverges.

Transform Order`xord`\- ⊞ \- Changing the Transform Order will change where things go much the same way as going a block and turning east gets you to a different place than turning east and then going a block. In matrix math terms, if we use the 'multiply vector on the right' (column vector) convention, a transform order of Scale, Rotate, Translate would be written as T * R * S * Position 
* Scale Rotate Translate`srt`-
* Scale Translate Rotate`str`-
* Rotate Scale Translate`rst`-
* Rotate Translate Scale`rts`-
* Translate Scale Rotate`tsr`-
* Translate Rotate Scale`trs`-


Rotate Order`rord`\- ⊞ \- As with transform order (above), changing the order in which the rotations take place will alter the final position and orientation. A Rotation order of Rx Ry Rz would create the final rotation matrix as follows R = Rz * Ry * Rx 
* Rx Ry Rz`xyz`-
* Rx Rz Ry`xzy`-
* Ry Rx Rz`yxz`-
* Ry Rz Rx`yzx`-
* Rz Rx Ry`zxy`-
* Rz Ry Rx`zyx`-


Translate`t`\- ⊞ \- XYZ translation values. 
* X`tx`-
* Y`ty`-
* Z`tz`-


Rotate`r`\- ⊞ \- XYZ rotation, in degrees. 
* X`rx`-
* Y`ry`-
* Z`rz`-


Scale`s`\- ⊞ \- XYZ scale to shrink or enlarge the transform. 
* X`sx`-
* Y`sy`-
* Z`sz`-


Pivot`p`\- ⊞ \- XYZ pivot to apply the above operations around. 
* X`px`-
* Y`py`-
* Z`pz`-

## 

Parameters - Constraints Page

Constraint`constraint`\- ⊞ \- Constraint and its parameters allows the noise curve to start and/or end at selected values. The mean value may also be enforced. **Note:** This only works when Time Slice is Off because time slicing has no pre-determined start/end. 
* None`none`\- No constraints set.
* Start Value`start`\- Sets the noise starting position to the value set in 'Starting Value' parameter below.
* End Value`end`\- Sets the noise ending position to the value set in 'Ending Value' parameter below.
* Mean Value`offset`\- Sets the noise mean position to the value set in the 'Mean Value' parameter below.
* Start/End Values`endpoints`\- Set the starting and ending position of the noise separately using the parameters below.


Starting Value`constrstart`\- Value for the starting position. 

Ending Value`constrend`\- Value for the ending position. 

Mean Value`constrmean`\- Value for the mean value of the noise. 

Normalize`normal`\- Ensures that all noise curves fall between -1 and 1. Applied before the Amplitude parameter. Only valid for Random and Harmonic Summation noise types, since Hermite and Sparse noise are always normalized. Normalizing random noise occurs between integrations, producing a more controlled curve. **Note:** This only works when Time Slice is Off because time slicing has no pre-determined start/end. 

## 

Parameters - Channel Page

Channel Names`channelname`\- You can creates many channels with simple patterns like "`chan[1-20]`", which generates 20 channels from chan1 to chan20. See the section, Common CHOP Parameters for a description of this and all Options. See [Scope and Channel Name Matching](<./CHOP_Common_Page.htm#Scope> "CHOP Common Page") Options. Each channel has a unique seed, so all channels will be different with the same parameter settings. 

Start`start`\- Start of the interval, expressed in Units (seconds, frames or samples). 

Start Unit`startunit`\- Select the units to use for this parameter, Samples, Frames, or Seconds. 

End`end`\- End of the interval, expressed in Units (seconds, frames or samples). 

End Unit`endunit`\- Select the units to use for this parameter, Samples, Frames, or Seconds. 

Sample Rate`rate`\- The sample rate of the channels, in samples per second. Default:`me.time.rate`Extend Left`left`\- ⊞ \- The left extend conditions (before/after range). 
* Hold`hold`\- Hold the current value of the channel.
* Slope`slope`\- Continue the slope before the start of the channel.
* Cycle`cycle`\- Cycle the channel repeatedly.
* Mirror`mirror`\- Cycle the channel repeatedly, mirroring every other cycle.
* Default Value`default`\- Use the constant value specified in the Default Value parameter.


Extend Right`right`\- ⊞ \- The right extend conditions (before/after range). 
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

Operator Inputs
* Input 0:  -

## 

Info CHOP Channels

Extra Information for the Noise CHOP can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). __

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


  
TouchDesigner Build: Latest\n2021.100002018.28070before 2018.28070

CHOPs   
---  
[Ableton Link ](<./Ableton_Link_CHOP.md> "Ableton Link CHOP")• [Analyze ](<./Analyze_CHOP.md> "Analyze CHOP")• [Angle ](<./Angle_CHOP.md> "Angle CHOP")• [Attribute ](<./Attribute_CHOP.md> "Attribute CHOP")• [Audio Band EQ ](<./Audio_Band_EQ_CHOP.md> "Audio Band EQ CHOP")• [Audio Binaural ](<./Audio_Binaural_CHOP.md> "Audio Binaural CHOP")• [Audio Device In ](<./Audio_Device_In_CHOP.md> "Audio Device In CHOP")• [Audio Device Out ](<./Audio_Device_Out_CHOP.md> "Audio Device Out CHOP")• [Audio Dynamics ](<./Audio_Dynamics_CHOP.md> "Audio Dynamics CHOP")• [Audio File In ](<./Audio_File_In_CHOP.md> "Audio File In CHOP")• [Audio File Out ](<./Audio_File_Out_CHOP.md> "Audio File Out CHOP")• [Audio Filter ](<./Audio_Filter_CHOP.md> "Audio Filter CHOP")• [Audio Movie ](<./Audio_Movie_CHOP.md> "Audio Movie CHOP")• [Audio NDI ](<./Audio_NDI_CHOP.md> "Audio NDI CHOP")• [Audio Oscillator ](<./Audio_Oscillator_CHOP.md> "Audio Oscillator CHOP")• [Audio Para EQ ](<./Audio_Para_EQ_CHOP.md> "Audio Para EQ CHOP")• [Audio Play ](<./Audio_Play_CHOP.md> "Audio Play CHOP")• [Audio Render ](<./Audio_Render_CHOP.md> "Audio Render CHOP")• [Audio Spectrum ](<./Audio_Spectrum_CHOP.md> "Audio Spectrum CHOP")• [Audio Stream In ](<./Audio_Stream_In_CHOP.md> "Audio Stream In CHOP")• [Audio Stream Out ](<./Audio_Stream_Out_CHOP.md> "Audio Stream Out CHOP")• [Audio VST ](<./Audio_VST_CHOP.md> "Audio VST CHOP")• [Audio Web Render ](<./Audio_Web_Render_CHOP.md> "Audio Web Render CHOP")• [Beat ](<./Beat_CHOP.md> "Beat CHOP")• [Bind ](<./Bind_CHOP.md> "Bind CHOP")• [BlackTrax ](<./BlackTrax_CHOP.md> "BlackTrax CHOP")• [Blend ](<./Blend_CHOP.md> "Blend CHOP")• [Blob Track ](<./Blob_Track_CHOP.md> "Blob Track CHOP")• [Body Track ](<./Body_Track_CHOP.md> "Body Track CHOP")• [Bullet Solver ](<./Bullet_Solver_CHOP.md> "Bullet Solver CHOP")• [CHOP ](<./CHOP.md> "CHOP")• [Clip Blender ](<./Clip_Blender_CHOP.md> "Clip Blender CHOP")• [Clip ](<./Clip_CHOP.md> "Clip CHOP")• [Clock ](<./Clock_CHOP.md> "Clock CHOP")• [Composite ](<./Composite_CHOP.md> "Composite CHOP")• [Constant ](<./Constant_CHOP.md> "Constant CHOP")• [Copy ](<./Copy_CHOP.md> "Copy CHOP")• [Count ](<./Count_CHOP.md> "Count CHOP")• [CPlusPlus ](<./CPlusPlus_CHOP.md> "CPlusPlus CHOP")• [Cross ](<./Cross_CHOP.md> "Cross CHOP")• [Cycle ](<./Cycle_CHOP.md> "Cycle CHOP")• [DAT to ](<./DAT_to_CHOP.md> "DAT to CHOP")• [Delay ](<./Delay_CHOP.md> "Delay CHOP")• [Delete ](<./Delete_CHOP.md> "Delete CHOP")• [DMX In ](<./DMX_In_CHOP.md> "DMX In CHOP")• [DMX Out ](<./DMX_Out_CHOP.md> "DMX Out CHOP")• [Envelope ](<./Envelope_CHOP.md> "Envelope CHOP")• [EtherDream ](<./EtherDream_CHOP.md> "EtherDream CHOP")• [Event ](<./Event_CHOP.md> "Event CHOP")• [Expression ](<./Expression_CHOP.md> "Expression CHOP")• [Extend ](<./Extend_CHOP.md> "Extend CHOP")• [Face Track ](<./Face_Track_CHOP.md> "Face Track CHOP")• [Fan ](<./Fan_CHOP.md> "Fan CHOP")• [Feedback ](<./Feedback_CHOP.md> "Feedback CHOP")• [File In ](<./File_In_CHOP.md> "File In CHOP")• [File Out ](<./File_Out_CHOP.md> "File Out CHOP")• [Filter ](<./Filter_CHOP.md> "Filter CHOP")• [FreeD In ](<./FreeD_In_CHOP.md> "FreeD In CHOP")• [FreeD Out ](<./FreeD_Out_CHOP.md> "FreeD Out CHOP")• [Function ](<./Function_CHOP.md> "Function CHOP")• [Gesture ](<./Gesture_CHOP.md> "Gesture CHOP")• [Handle ](<./Handle_CHOP.md> "Handle CHOP")• [Helios DAC ](<./Helios_DAC_CHOP.md> "Helios DAC CHOP")• [Hog ](<./Hog_CHOP.md> "Hog CHOP")• [Hokuyo ](<./Hokuyo_CHOP.md> "Hokuyo CHOP")• [Hold ](<./Hold_CHOP.md> "Hold CHOP")• [Import Select ](<./Import_Select_CHOP.md> "Import Select CHOP")• [In ](<./In_CHOP.md> "In CHOP")• [Info ](<./Info_CHOP.md> "Info CHOP")• [Interpolate ](<./Interpolate_CHOP.md> "Interpolate CHOP")• [Introduction To s Vid ](<./Introduction_To_CHOPs_Vid.md> "Introduction To CHOPs Vid")• [Inverse Curve ](<./Inverse_Curve_CHOP.md> "Inverse Curve CHOP")• [Inverse Kin ](<./Inverse_Kin_CHOP.md> "Inverse Kin CHOP")• [Join ](<./Join_CHOP.md> "Join CHOP")• [Joystick ](<./Joystick_CHOP.md> "Joystick CHOP")• [Keyboard In ](<./Keyboard_In_CHOP.md> "Keyboard In CHOP")• [Keyframe ](<./Keyframe_CHOP.md> "Keyframe CHOP")• [Kinect Azure ](<./Kinect_Azure_CHOP.md> "Kinect Azure CHOP")• [Kinect ](<./Kinect_CHOP.md> "Kinect CHOP")• [Lag ](<./Lag_CHOP.md> "Lag CHOP")• [Laser ](<./Laser_CHOP.md> "Laser CHOP")• [Laser Device ](<./Laser_Device_CHOP.md> "Laser Device CHOP")• [Leap Motion ](<./Leap_Motion_CHOP.md> "Leap Motion CHOP")• [Leuze ROD4 ](<./Leuze_ROD4_CHOP.md> "Leuze ROD4 CHOP")• [LFO ](<./LFO_CHOP.md> "LFO CHOP")• [Limit ](<./Limit_CHOP.md> "Limit CHOP")• [Logic ](<./Logic_CHOP.md> "Logic CHOP")• [Lookup ](<./Lookup_CHOP.md> "Lookup CHOP")• [LTC In ](<./LTC_In_CHOP.md> "LTC In CHOP")• [LTC Out ](<./LTC_Out_CHOP.md> "LTC Out CHOP")• [Math ](<./Math_CHOP.md> "Math CHOP")• [Merge ](<./Merge_CHOP.md> "Merge CHOP")• [MIDI In ](<./MIDI_In_CHOP.md> "MIDI In CHOP")• [MIDI In Map ](<./MIDI_In_Map_CHOP.md> "MIDI In Map CHOP")• [MIDI Out ](<./MIDI_Out_CHOP.md> "MIDI Out CHOP")• [MoSys ](<./MoSys_CHOP.md> "MoSys CHOP")• [Mouse In ](<./Mouse_In_CHOP.md> "Mouse In CHOP")• [Mouse Out ](<./Mouse_Out_CHOP.md> "Mouse Out CHOP")• [Ncam ](<./Ncam_CHOP.md> "Ncam CHOP")• Noise • [Null ](<./Null_CHOP.md> "Null CHOP")• [OAK Device ](<./OAK_Device_CHOP.md> "OAK Device CHOP")• [OAK Select ](<./OAK_Select_CHOP.md> "OAK Select CHOP")• [Object ](<./Object_CHOP.md> "Object CHOP")• [Oculus Audio ](<./Oculus_Audio_CHOP.md> "Oculus Audio CHOP")• [Oculus Rift ](<./Oculus_Rift_CHOP.md> "Oculus Rift CHOP")• [OpenVR ](<./OpenVR_CHOP.md> "OpenVR CHOP")• [OptiTrack In ](<./OptiTrack_In_CHOP.md> "OptiTrack In CHOP")• [OSC In ](<./OSC_In_CHOP.md> "OSC In CHOP")• [OSC Out ](<./OSC_Out_CHOP.md> "OSC Out CHOP")• [Out ](<./Out_CHOP.md> "Out CHOP")• [Override ](<./Override_CHOP.md> "Override CHOP")• [Pan Tilt ](<./Pan_Tilt_CHOP.md> "Pan Tilt CHOP")• [Panel ](<./Panel_CHOP.md> "Panel CHOP")• [Pangolin ](<./Pangolin_CHOP.md> "Pangolin CHOP")• [Parameter ](<./Parameter_CHOP.md> "Parameter CHOP")• [Pattern ](<./Pattern_CHOP.md> "Pattern CHOP")• [Perform ](<./Perform_CHOP.md> "Perform CHOP")• [Phaser ](<./Phaser_CHOP.md> "Phaser CHOP")• [Pipe In ](<./Pipe_In_CHOP.md> "Pipe In CHOP")• [Pipe Out ](<./Pipe_Out_CHOP.md> "Pipe Out CHOP")• [POP to ](<./POP_to_CHOP.md> "POP to CHOP")• [PosiStageNet ](<./PosiStageNet_CHOP.md> "PosiStageNet CHOP")• [Pulse ](<./Pulse_CHOP.md> "Pulse CHOP")• [RealSense ](<./RealSense_CHOP.md> "RealSense CHOP")• [Record ](<./Record_CHOP.md> "Record CHOP")• [Rename ](<./Rename_CHOP.md> "Rename CHOP")• [Render Pick ](<./Render_Pick_CHOP.md> "Render Pick CHOP")• [RenderStream In ](<./RenderStream_In_CHOP.md> "RenderStream In CHOP")• [Reorder ](<./Reorder_CHOP.md> "Reorder CHOP")• [Replace ](<./Replace_CHOP.md> "Replace CHOP")• [Resample ](<./Resample_CHOP.md> "Resample CHOP")• [S Curve ](<./S_Curve_CHOP.md> "S Curve CHOP")• [Scan ](<./Scan_CHOP.md> "Scan CHOP")• [Script ](<./Script_CHOP.md> "Script CHOP")• [Select ](<./Select_CHOP.md> "Select CHOP")• [Sequencer ](<./Sequencer_CHOP.md> "Sequencer CHOP")• [Serial ](<./Serial_CHOP.md> "Serial CHOP")• [Shared Mem In ](<./Shared_Mem_In_CHOP.md> "Shared Mem In CHOP")• [Shared Mem Out ](<./Shared_Mem_Out_CHOP.md> "Shared Mem Out CHOP")• [Shift ](<./Shift_CHOP.md> "Shift CHOP")• [Shuffle ](<./Shuffle_CHOP.md> "Shuffle CHOP")• [Slope ](<./Slope_CHOP.md> "Slope CHOP")• [SOP to ](<./SOP_to_CHOP.md> "SOP to CHOP")• [Sort ](<./Sort_CHOP.md> "Sort CHOP")• [Speed ](<./Speed_CHOP.md> "Speed CHOP")• [Splice ](<./Splice_CHOP.md> "Splice CHOP")• [Spring ](<./Spring_CHOP.md> "Spring CHOP")• [ST2110 Device ](<./ST2110_Device_CHOP.md> "ST2110 Device CHOP")• [Stretch ](<./Stretch_CHOP.md> "Stretch CHOP")• [Stype In ](<./Stype_In_CHOP.md> "Stype In CHOP")• [Stype Out ](<./Stype_Out_CHOP.md> "Stype Out CHOP")• [Switch ](<./Switch_CHOP.md> "Switch CHOP")• [Sync In ](<./Sync_In_CHOP.md> "Sync In CHOP")• [Sync Out ](<./Sync_Out_CHOP.md> "Sync Out CHOP")• [Tablet ](<./Tablet_CHOP.md> "Tablet CHOP")• [Time Slice ](<./Time_Slice_CHOP.md> "Time Slice CHOP")• [Timecode ](<./Timecode_CHOP.md> "Timecode CHOP")• [Timeline ](<./Timeline_CHOP.md> "Timeline CHOP")• [Timer ](<./Timer_CHOP.md> "Timer CHOP")• [TOP to ](<./TOP_to_CHOP.md> "TOP to CHOP")• [Touch In ](<./Touch_In_CHOP.md> "Touch In CHOP")• [Touch Out ](<./Touch_Out_CHOP.md> "Touch Out CHOP")• [Trail ](<./Trail_CHOP.md> "Trail CHOP")• [Transform ](<./Transform_CHOP.md> "Transform CHOP")• [Transform XYZ ](<./Transform_XYZ_CHOP.md> "Transform XYZ CHOP")• [Trigger ](<./Trigger_CHOP.md> "Trigger CHOP")• [Trim ](<./Trim_CHOP.md> "Trim CHOP")• [Warp ](<./Warp_CHOP.md> "Warp CHOP")• [Wave ](<./Wave_CHOP.md> "Wave CHOP")• [WrnchAI ](<./WrnchAI_CHOP.md> "WrnchAI CHOP")• [ZED ](<./ZED_CHOP.md> "ZED CHOP")
