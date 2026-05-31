# Audio Dynamics CHOP

##   
  
Summary

The Audio Dynamics CHOP is designed to control the dynamic range of an audio signal. Dynamic range refers to how loud and quiet the audio is over some period of time. The Operator contains two types of dynamic control: compression and limiting. It is recommended that you [link](<./Link.md> "Link") this CHOP to an [Info CHOP](<./Info_CHOP.md> "Info CHOP"), so that you can have some visual feedback: The amount of compression or limiting which is being applied will be displayed in the Info CHOP. 

**Compressor** The goal of a compressor is to reduce the amplitude of a signal when it crosses a certain threshold, while introducing little to no harmonic distortion. The desired threshold is set by the user, and the amount of compression to be applied is determined by the compression ratio. The attack and release parameters determine how quickly the compression will be applied and released, as incoming signal goes above and below the threshold. 

**Limiter** The purpose of a limiter is to ensure a signal is within a certain dynamic range, while introducing as little harmonic distortion as possible. Unlike the compressor, the goal is not to apply a smooth or musical form of dynamic control, but instead to keep the signal within a 'safe' range that is compatible with any CHOPS that are downstream (for example, an Audio Device Out). This means that the Limiter has a much more abrupt (instant) attack value, which cannot be adjusted by the user. 

Input 2: **Side Chain Channels** \- Other audio channels coming in can be used to determine the gains that are applied to the audio channels of the first input. 

**NOTE** : This is a useful article for procedurally [mixing audio for games](<http://gameaudionoise.blogspot.co.uk/p/all-in-mix-importance-of-real-time.html>). 

See [Audio Filter CHOP](<./Audio_Filter_CHOP.md> "Audio Filter CHOP"), [Audio Para EQ CHOP](<./Audio_Para_EQ_CHOP.md> "Audio Para EQ CHOP"), [Audio Band EQ CHOP](<./Audio_Band_EQ_CHOP.md> "Audio Band EQ CHOP"), [Audio Spectrum CHOP](<./Audio_Spectrum_CHOP.md> "Audio Spectrum CHOP") See also: [Envelope CHOP](<./Envelope_CHOP.md> "Envelope CHOP"). 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[audiodynamicsCHOP_Class](<./AudiodynamicsCHOP_Class.md> "AudiodynamicsCHOP Class")

## 

Parameters - Pre Page

Input Gain (dB)`inputgain`\- This parameter controls the volume of the channel before it reaches the compressor. If the signal to be compressed is not in a useful dynamic range, this parameter can be used to repair it. 

## 

Parameters - Compressor Page

Enable Compressor`enablecompressor`\- Turns the compressor on or off. 

Compression Type`compressiontype`\- ⊞ \- Determines which compression method to use. 
* Automatic Gain Control`compagc`\- This type of compression is suitable for passages of audio which are varying in amplitude over an extended period of time. To apply this type of compression, set the threshold to a value which is near the maximum volume that you want to hear. Apply a large compression ratio (around 1.0), and set the attack and release to high values. As the passage of audio crosses the threshold value, compression will slowly be applied, and if set properly, the signal will be compressed to a constant range. Setting the attack and release too low will cause the output volume to waver too quickly, while high values may cause the compression to be applied too slowly.
* Musical Dynamics`compmus`\- If a passage of vocals or a musical instrument is varying in amplitude and needs to be brought into a uniform dynamic range, try applying this type of compression. Unless a heavy compression sound is desired, it is best to use this effect lightly. Set the threshold into the volume range that you want to compress and apply a low compression ratio. Try different values of attack and release until you achieve a good dynamic balance.


Channel Linking`chanlinkingcomp`\- ⊞ \- As various channels come into the CHOP, they can either be compressed by an equal amount, or individually. If they are compressed equally, all of the channels will be evaluated for the highest peak value, and this value will be used to determine the compression amount. 

If they are compressed separately, each channel will be evaluated and compressed by different amounts. 
* Compress Equally`compequally`-
* Compress Individually`compindividually`-


Threshold (dB)`thresholdcompressor`\- This parameter sets the threshold value which a signal must cross before compression is applied. It uses a decibel scale, where '0 decibels' would be considered the loudest possible signal*, and '-60 decibels' would be nearly inaudible. This is assuming that input signals are normalized to a "-1 to +1" range. 

Ratio`ratiocompressor`\- The ratio is the amount of compression that will be applied to the signal, with respect to how far the signal has gone past the threshold value. A ratio of '0' will apply no compression. A value of '1' will cause a signals amplitude to be held down to the threshold value. With values over '1', the signal will become quieter as it passes the threshold. 

Knee`kneecompressor`\- The knee defines how the CHOP will transition into compression as signals approach or cross the threshold. With a knee of '0' (a hard knee), think of the compressor as applying a flat compression response, where: 

compression_gain(db) = amount_that_signal_has_crossed_threshold(dB) * compression_ratio This type of compression is not always desirable, as it can have a strong effect upon the dynamics of a sound. Increasing the knee parameter will cause there to be a smoothed transition into the compression. See the Knee diagram below. 

Attack (msec=10**val)`attackcompressor`\- The attack will control how quickly the compressor responds when a signal crosses the threshold. Increasing the attack parameter will cause the compressor to apply compression at a slower and smoother rate. Increasing the parameter too much, will cause compression to be applied too slowly. 

Release (msec=10**val)`releasecompressor`\- The release will control how quickly the compressor responds when a signal drops to a lower level, or goes below the threshold altogether. Just like the attack, higher value will slow down the response, but too high of a value will be too slow. 

Output Gain (dB)`gaincompressor`\- After applying compression, the signal can be reduced with Gain to a lower volume level. To make up the lost volume, this parameter can be increased. 

## 

Parameters - Limiter Page

Enable Limiter`enablelimiter`\- Turns the limiter on or off. 

Channel Linking`chanlinkinglim`\- ⊞ \- Same as compressor. 
* Limit Equally`compequally`-
* Limit Individually`compindividually`-


Threshold (dB)`thresholdlimiter`\- This is the threshold value which a signal must cross before limiting is applied. Usually, this value should be left at '0' decibels. Just like the compressor, a value of '0' decibels is considered to be the loudest possible signal. 

From the perspective of digital audio, a signal level which varies between "+1 <-> -1" is at a volume level of "0" decibels, because it is not possible for a digital system to respresent any values larger than "+1 <-> -1". Instead, they will simply be clipped as they proceed to the output device. The limiter allows you to stop your audio from being clipped if you exceed this range, and applies a much smoother form of fast compression, which is barely audible. Lowering the threshold value will cause the output to be clamped to a lower level. __

Release (msec=10**val)`releaselimiter`\- Although the attack of a limiter is always quick, the release can still be set by the user. This will determine how long the limiter takes to transition out of a limiting situation. Increasing the release will help smooth out the effect of the limiter. Too high of a value may cause the limiter to release too slowly. For example, after an excessively loud tone burst, the limiter's gain may have been pushed up to an extreme value. This extreme value will take a long time to be fully released. 

Each channel can be different by putting expressions with the channel index,`me.channelIndex`in parameters like the frequency channel. __

Knee`kneelimiter`\- Similar to the compressor, this parameter controls how the CHOP will transition into limiting, when a signal becomes louder. A larger knee will mean a smoother transition. See the Knee diagram above. 

If set to '0', no limiting will be applied until a signal goes over the threshold value. When increasing the knee parameter, some limiting will be applied before a signal goes beyond the threshold value, in an attempt to smooth out the effects of limiting overall. __

## 

Parameters - Post Page

Dry / Wet Mix`drywet`\- As this parameter is reduced from 1 (Wet) toward 0 (Dry), it removes the effect of the filter. 

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

  *`compressor_multiplier`\- the amount that the compressor reduced the loudness. 1 means no-change. expressed not in dB – linear
  *`limiter_multiplier`\- the amount that the limiter reduced the loudness. not db – linear
  *`compressor_db`\- same as above but expressed in decibels
  *`limiter_db`*`compressor_attack_msec`\- this is in milliseconds, computed from the parameter which is 1 msec at value 1 and 100,000 msec at value 5 (10**val)
  *`compressor_release_msec`*`limiter_release_msec`## 

Operator Inputs
* Input 0:  -
  * Input 1:  -

## 

Info CHOP Channels

Extra Information for the Audio Dynamics CHOP can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). 

### 

Specific Audio Dynamics CHOP Info Channels
* compressor_multiplier -
* compressor_db -
* compressor_attack_msec -
* compressor_release_msec -
* limiter_multiplier -
* limiter_db -
* limiter_release_msec -

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


  
TouchDesigner Build: Latest\n2022.241402021.100002018.28070before 2018.28070

CHOPs   
---  
[Ableton Link ](<./Ableton_Link_CHOP.md> "Ableton Link CHOP")• [Analyze ](<./Analyze_CHOP.md> "Analyze CHOP")• [Angle ](<./Angle_CHOP.md> "Angle CHOP")• [Attribute ](<./Attribute_CHOP.md> "Attribute CHOP")• [Audio Band EQ ](<./Audio_Band_EQ_CHOP.md> "Audio Band EQ CHOP")• [Audio Binaural ](<./Audio_Binaural_CHOP.md> "Audio Binaural CHOP")• [Audio Device In ](<./Audio_Device_In_CHOP.md> "Audio Device In CHOP")• [Audio Device Out ](<./Audio_Device_Out_CHOP.md> "Audio Device Out CHOP")• Audio Dynamics • [Audio File In ](<./Audio_File_In_CHOP.md> "Audio File In CHOP")• [Audio File Out ](<./Audio_File_Out_CHOP.md> "Audio File Out CHOP")• [Audio Filter ](<./Audio_Filter_CHOP.md> "Audio Filter CHOP")• [Audio Movie ](<./Audio_Movie_CHOP.md> "Audio Movie CHOP")• [Audio NDI ](<./Audio_NDI_CHOP.md> "Audio NDI CHOP")• [Audio Oscillator ](<./Audio_Oscillator_CHOP.md> "Audio Oscillator CHOP")• [Audio Para EQ ](<./Audio_Para_EQ_CHOP.md> "Audio Para EQ CHOP")• [Audio Play ](<./Audio_Play_CHOP.md> "Audio Play CHOP")• [Audio Render ](<./Audio_Render_CHOP.md> "Audio Render CHOP")• [Audio Spectrum ](<./Audio_Spectrum_CHOP.md> "Audio Spectrum CHOP")• [Audio Stream In ](<./Audio_Stream_In_CHOP.md> "Audio Stream In CHOP")• [Audio Stream Out ](<./Audio_Stream_Out_CHOP.md> "Audio Stream Out CHOP")• [Audio VST ](<./Audio_VST_CHOP.md> "Audio VST CHOP")• [Audio Web Render ](<./Audio_Web_Render_CHOP.md> "Audio Web Render CHOP")• [Beat ](<./Beat_CHOP.md> "Beat CHOP")• [Bind ](<./Bind_CHOP.md> "Bind CHOP")• [BlackTrax ](<./BlackTrax_CHOP.md> "BlackTrax CHOP")• [Blend ](<./Blend_CHOP.md> "Blend CHOP")• [Blob Track ](<./Blob_Track_CHOP.md> "Blob Track CHOP")• [Body Track ](<./Body_Track_CHOP.md> "Body Track CHOP")• [Bullet Solver ](<./Bullet_Solver_CHOP.md> "Bullet Solver CHOP")• [CHOP ](<./CHOP.md> "CHOP")• [Clip Blender ](<./Clip_Blender_CHOP.md> "Clip Blender CHOP")• [Clip ](<./Clip_CHOP.md> "Clip CHOP")• [Clock ](<./Clock_CHOP.md> "Clock CHOP")• [Composite ](<./Composite_CHOP.md> "Composite CHOP")• [Constant ](<./Constant_CHOP.md> "Constant CHOP")• [Copy ](<./Copy_CHOP.md> "Copy CHOP")• [Count ](<./Count_CHOP.md> "Count CHOP")• [CPlusPlus ](<./CPlusPlus_CHOP.md> "CPlusPlus CHOP")• [Cross ](<./Cross_CHOP.md> "Cross CHOP")• [Cycle ](<./Cycle_CHOP.md> "Cycle CHOP")• [DAT to ](<./DAT_to_CHOP.md> "DAT to CHOP")• [Delay ](<./Delay_CHOP.md> "Delay CHOP")• [Delete ](<./Delete_CHOP.md> "Delete CHOP")• [DMX In ](<./DMX_In_CHOP.md> "DMX In CHOP")• [DMX Out ](<./DMX_Out_CHOP.md> "DMX Out CHOP")• [Envelope ](<./Envelope_CHOP.md> "Envelope CHOP")• [EtherDream ](<./EtherDream_CHOP.md> "EtherDream CHOP")• [Event ](<./Event_CHOP.md> "Event CHOP")• [Expression ](<./Expression_CHOP.md> "Expression CHOP")• [Extend ](<./Extend_CHOP.md> "Extend CHOP")• [Face Track ](<./Face_Track_CHOP.md> "Face Track CHOP")• [Fan ](<./Fan_CHOP.md> "Fan CHOP")• [Feedback ](<./Feedback_CHOP.md> "Feedback CHOP")• [File In ](<./File_In_CHOP.md> "File In CHOP")• [File Out ](<./File_Out_CHOP.md> "File Out CHOP")• [Filter ](<./Filter_CHOP.md> "Filter CHOP")• [FreeD In ](<./FreeD_In_CHOP.md> "FreeD In CHOP")• [FreeD Out ](<./FreeD_Out_CHOP.md> "FreeD Out CHOP")• [Function ](<./Function_CHOP.md> "Function CHOP")• [Gesture ](<./Gesture_CHOP.md> "Gesture CHOP")• [Handle ](<./Handle_CHOP.md> "Handle CHOP")• [Helios DAC ](<./Helios_DAC_CHOP.md> "Helios DAC CHOP")• [Hog ](<./Hog_CHOP.md> "Hog CHOP")• [Hokuyo ](<./Hokuyo_CHOP.md> "Hokuyo CHOP")• [Hold ](<./Hold_CHOP.md> "Hold CHOP")• [Import Select ](<./Import_Select_CHOP.md> "Import Select CHOP")• [In ](<./In_CHOP.md> "In CHOP")• [Info ](<./Info_CHOP.md> "Info CHOP")• [Interpolate ](<./Interpolate_CHOP.md> "Interpolate CHOP")• [Introduction To s Vid ](<./Introduction_To_CHOPs_Vid.md> "Introduction To CHOPs Vid")• [Inverse Curve ](<./Inverse_Curve_CHOP.md> "Inverse Curve CHOP")• [Inverse Kin ](<./Inverse_Kin_CHOP.md> "Inverse Kin CHOP")• [Join ](<./Join_CHOP.md> "Join CHOP")• [Joystick ](<./Joystick_CHOP.md> "Joystick CHOP")• [Keyboard In ](<./Keyboard_In_CHOP.md> "Keyboard In CHOP")• [Keyframe ](<./Keyframe_CHOP.md> "Keyframe CHOP")• [Kinect Azure ](<./Kinect_Azure_CHOP.md> "Kinect Azure CHOP")• [Kinect ](<./Kinect_CHOP.md> "Kinect CHOP")• [Lag ](<./Lag_CHOP.md> "Lag CHOP")• [Laser ](<./Laser_CHOP.md> "Laser CHOP")• [Laser Device ](<./Laser_Device_CHOP.md> "Laser Device CHOP")• [Leap Motion ](<./Leap_Motion_CHOP.md> "Leap Motion CHOP")• [Leuze ROD4 ](<./Leuze_ROD4_CHOP.md> "Leuze ROD4 CHOP")• [LFO ](<./LFO_CHOP.md> "LFO CHOP")• [Limit ](<./Limit_CHOP.md> "Limit CHOP")• [Logic ](<./Logic_CHOP.md> "Logic CHOP")• [Lookup ](<./Lookup_CHOP.md> "Lookup CHOP")• [LTC In ](<./LTC_In_CHOP.md> "LTC In CHOP")• [LTC Out ](<./LTC_Out_CHOP.md> "LTC Out CHOP")• [Math ](<./Math_CHOP.md> "Math CHOP")• [Merge ](<./Merge_CHOP.md> "Merge CHOP")• [MIDI In ](<./MIDI_In_CHOP.md> "MIDI In CHOP")• [MIDI In Map ](<./MIDI_In_Map_CHOP.md> "MIDI In Map CHOP")• [MIDI Out ](<./MIDI_Out_CHOP.md> "MIDI Out CHOP")• [MoSys ](<./MoSys_CHOP.md> "MoSys CHOP")• [Mouse In ](<./Mouse_In_CHOP.md> "Mouse In CHOP")• [Mouse Out ](<./Mouse_Out_CHOP.md> "Mouse Out CHOP")• [Ncam ](<./Ncam_CHOP.md> "Ncam CHOP")• [Noise ](<./Noise_CHOP.md> "Noise CHOP")• [Null ](<./Null_CHOP.md> "Null CHOP")• [OAK Device ](<./OAK_Device_CHOP.md> "OAK Device CHOP")• [OAK Select ](<./OAK_Select_CHOP.md> "OAK Select CHOP")• [Object ](<./Object_CHOP.md> "Object CHOP")• [Oculus Audio ](<./Oculus_Audio_CHOP.md> "Oculus Audio CHOP")• [Oculus Rift ](<./Oculus_Rift_CHOP.md> "Oculus Rift CHOP")• [OpenVR ](<./OpenVR_CHOP.md> "OpenVR CHOP")• [OptiTrack In ](<./OptiTrack_In_CHOP.md> "OptiTrack In CHOP")• [OSC In ](<./OSC_In_CHOP.md> "OSC In CHOP")• [OSC Out ](<./OSC_Out_CHOP.md> "OSC Out CHOP")• [Out ](<./Out_CHOP.md> "Out CHOP")• [Override ](<./Override_CHOP.md> "Override CHOP")• [Pan Tilt ](<./Pan_Tilt_CHOP.md> "Pan Tilt CHOP")• [Panel ](<./Panel_CHOP.md> "Panel CHOP")• [Pangolin ](<./Pangolin_CHOP.md> "Pangolin CHOP")• [Parameter ](<./Parameter_CHOP.md> "Parameter CHOP")• [Pattern ](<./Pattern_CHOP.md> "Pattern CHOP")• [Perform ](<./Perform_CHOP.md> "Perform CHOP")• [Phaser ](<./Phaser_CHOP.md> "Phaser CHOP")• [Pipe In ](<./Pipe_In_CHOP.md> "Pipe In CHOP")• [Pipe Out ](<./Pipe_Out_CHOP.md> "Pipe Out CHOP")• [POP to ](<./POP_to_CHOP.md> "POP to CHOP")• [PosiStageNet ](<./PosiStageNet_CHOP.md> "PosiStageNet CHOP")• [Pulse ](<./Pulse_CHOP.md> "Pulse CHOP")• [RealSense ](<./RealSense_CHOP.md> "RealSense CHOP")• [Record ](<./Record_CHOP.md> "Record CHOP")• [Rename ](<./Rename_CHOP.md> "Rename CHOP")• [Render Pick ](<./Render_Pick_CHOP.md> "Render Pick CHOP")• [RenderStream In ](<./RenderStream_In_CHOP.md> "RenderStream In CHOP")• [Reorder ](<./Reorder_CHOP.md> "Reorder CHOP")• [Replace ](<./Replace_CHOP.md> "Replace CHOP")• [Resample ](<./Resample_CHOP.md> "Resample CHOP")• [S Curve ](<./S_Curve_CHOP.md> "S Curve CHOP")• [Scan ](<./Scan_CHOP.md> "Scan CHOP")• [Script ](<./Script_CHOP.md> "Script CHOP")• [Select ](<./Select_CHOP.md> "Select CHOP")• [Sequencer ](<./Sequencer_CHOP.md> "Sequencer CHOP")• [Serial ](<./Serial_CHOP.md> "Serial CHOP")• [Shared Mem In ](<./Shared_Mem_In_CHOP.md> "Shared Mem In CHOP")• [Shared Mem Out ](<./Shared_Mem_Out_CHOP.md> "Shared Mem Out CHOP")• [Shift ](<./Shift_CHOP.md> "Shift CHOP")• [Shuffle ](<./Shuffle_CHOP.md> "Shuffle CHOP")• [Slope ](<./Slope_CHOP.md> "Slope CHOP")• [SOP to ](<./SOP_to_CHOP.md> "SOP to CHOP")• [Sort ](<./Sort_CHOP.md> "Sort CHOP")• [Speed ](<./Speed_CHOP.md> "Speed CHOP")• [Splice ](<./Splice_CHOP.md> "Splice CHOP")• [Spring ](<./Spring_CHOP.md> "Spring CHOP")• [ST2110 Device ](<./ST2110_Device_CHOP.md> "ST2110 Device CHOP")• [Stretch ](<./Stretch_CHOP.md> "Stretch CHOP")• [Stype In ](<./Stype_In_CHOP.md> "Stype In CHOP")• [Stype Out ](<./Stype_Out_CHOP.md> "Stype Out CHOP")• [Switch ](<./Switch_CHOP.md> "Switch CHOP")• [Sync In ](<./Sync_In_CHOP.md> "Sync In CHOP")• [Sync Out ](<./Sync_Out_CHOP.md> "Sync Out CHOP")• [Tablet ](<./Tablet_CHOP.md> "Tablet CHOP")• [Time Slice ](<./Time_Slice_CHOP.md> "Time Slice CHOP")• [Timecode ](<./Timecode_CHOP.md> "Timecode CHOP")• [Timeline ](<./Timeline_CHOP.md> "Timeline CHOP")• [Timer ](<./Timer_CHOP.md> "Timer CHOP")• [TOP to ](<./TOP_to_CHOP.md> "TOP to CHOP")• [Touch In ](<./Touch_In_CHOP.md> "Touch In CHOP")• [Touch Out ](<./Touch_Out_CHOP.md> "Touch Out CHOP")• [Trail ](<./Trail_CHOP.md> "Trail CHOP")• [Transform ](<./Transform_CHOP.md> "Transform CHOP")• [Transform XYZ ](<./Transform_XYZ_CHOP.md> "Transform XYZ CHOP")• [Trigger ](<./Trigger_CHOP.md> "Trigger CHOP")• [Trim ](<./Trim_CHOP.md> "Trim CHOP")• [Warp ](<./Warp_CHOP.md> "Warp CHOP")• [Wave ](<./Wave_CHOP.md> "Wave CHOP")• [WrnchAI ](<./WrnchAI_CHOP.md> "WrnchAI CHOP")• [ZED ](<./ZED_CHOP.md> "ZED CHOP")
