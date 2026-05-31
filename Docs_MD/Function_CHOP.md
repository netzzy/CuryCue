# Function CHOP

## 

Summary

The Function CHOP provides more complicated math functions than found in the [Math CHOP](<./Math_CHOP.md> "Math CHOP") : trigonometic functions, logarithmic functions and exponential functions, and also audio decibels (dB)-power-amplitude conversions. 

Most of the functions require only one parameter, and they are applied as a unary operator to each input channel. Some functions take two parameters, and these require the use of the second input. The first parameter, X, is always a value from a channel in the first input. The second parameter, Y, is a value from a corresponding channel in the second input. Channels from each input are paired by name or index. 

Since many of these functions can produce math errors, an error handling tab is provided for error handling and recovery. Errors can be handled by replacing the bad sample with a pre-defined value or by using the value of the previous sample. Alternatively, cooking can be aborted upon error for debugging networks. 

Function types in decibels: as you would employ for audio or other signal strengths. -10dB means 1/10 the power, -20dB means 1/100 the power. It turns out that each 3dB means almost exactly double the power, so +12dB is 2*2*2*2 = 16 times the power. Power is proportional to the square of the amplitude. So -20dB means 1/10 the amplitude, and 6dB is double the amplitude. 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[functionCHOP_Class](<./FunctionCHOP_Class.md> "FunctionCHOP Class")

## 

Parameters - Function Page

Function`func`\- ⊞ \- Which math function to apply to the channels. All of the functions are unary functions except for the binary functions 'arctan (Input1/Input2)' and 'Input1 ^ Input2'. In the cases of power functions, a negative base is inverted first to avoid imaginary numbers, and the result is negated. 
* sqrt(x) Square Root`sqrt`\- Square Root of Input 1.
* abs(x) Absolute Value`abs`\- Absolute Value of Input 1.
* sign(x) Sign`sign`\- Sign of Input 1.
* cos(x) Cosine`cos`\- Cosine of Input 1.
* sin(x) Sine`sin`\- Sine of Input 1.
* tan(x) Tangent`tan`\- Tangent of Input 1.
* acos(x) Arccosine`acos`\- Arccosine of Input 1.
* asin(x) Arcsine`asin`\- Arcsine of Input 1.
* atan(x) Arctan( Input1 )`atan`\- Arctan of Input 1.
* atan2(y,x) Arctan( Input1 / Input2 )`atan2`\- Arctan of (Input 1 / Input 2).
* cosh(x) Hyperbolic Cosine`cosh`\- Hyperbolic Cosine of Input 1.
* sinh(x) Hyperbolic Sine`sinh`\- Hyperbolic Sine of Input 1.
* tanh(x) Hyperbolic Tangent`tanh`\- Hyperbolic Tangent of Input 1.
* log10(x) Log base 10`log`\- Log base 10 of Input 1.
* logN(x) Log base N`logb`\- Log base Base Value of Input 1.
* ln(x) Natural Log`ln`\- Natural Log of Input 1.
* pow(10,x) 10 ^ Input1`pow10`\- 10 to the power of Input 1.
* exp(x) e ^ Input1`exp`\- e to the power of Input 1.
* pow(x) Base ^ Input1`powe`\- Base value to the power of Input 1. If Base value is negative result is -((-Base Value) ^ Input 1)
* pow(x) Input1 ^ Exponent`powb`\- Input 1 to the power of Exponent value. If Input 1 is negative result is -((-Input 1) ^ Exponent Value).
* pow(x,y) Input1 ^ Input2`pow`\- ((-Input 1) ^ Input 2)
* dB to Power`dbtopower`\- Decibel (Input 1) to amplitude.
* Power to dB`powertodb`\- Amplitude (Input 1) to decibel.
* dB to Amplitude`dbtoamp`\- Decibel (Input 1) to amplitude.
* Amplitude to dB`amptodb`\- Amplitude (Input 1) to decibel.


Base Value`baseval`\- The value of the base for 'Log base N' and 'Base ^ Input1'. parameter name`/baseval`Exponent Value`expval`\- The value of the exponent for`'Input1 ^ Exponent'`. channel name`/expval`Angle Units`angunit`\- ⊞ \- For trigonometric functions, the angles can be measured in Degrees, Radians, or Cycles (0 to 1). 
* Degrees`deg`-
* Radians`rad`-
* Cycles`cycle`-


Match by`match`\- ⊞ \- How to pair channels together from the two inputs for the binary functions, by name or by channel index. 
* Channel Number`index`-
* Channel Name`name`-

## 

Parameters - Error Page

Error Handling`error`\- ⊞ \- How to correct samples with math errors: 
* Abort With Error Message`abort`\- Cooking aborts.
* Replace With Specified Values`replace`\- Values specified below.
* Use The Previous Value`useprev`\- Uses the last good result.


\+ Infinity Value`pinfval`\- Value to use when an infinity error occurs. Caused by sinh(), cosh() and tan(). 

\- Infinity Value`ninfval`\- Value to use when a negative infinity error occurs. Caused by sinh() and tan(). 

Domain Error Value`domval`\- Value to use when a domain error occurs. Caused by asin(), acos(), log10(), logN(), ln() and sqrt(). 

Divide Error Value`divval`\- Value to use when a divide by zero error occurs. Caused by pow(x,y). 

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
  * Input 1:  -

## 

Info CHOP Channels

Extra Information for the Function CHOP can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). __

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
[Ableton Link ](<./Ableton_Link_CHOP.md> "Ableton Link CHOP")• [Analyze ](<./Analyze_CHOP.md> "Analyze CHOP")• [Angle ](<./Angle_CHOP.md> "Angle CHOP")• [Attribute ](<./Attribute_CHOP.md> "Attribute CHOP")• [Audio Band EQ ](<./Audio_Band_EQ_CHOP.md> "Audio Band EQ CHOP")• [Audio Binaural ](<./Audio_Binaural_CHOP.md> "Audio Binaural CHOP")• [Audio Device In ](<./Audio_Device_In_CHOP.md> "Audio Device In CHOP")• [Audio Device Out ](<./Audio_Device_Out_CHOP.md> "Audio Device Out CHOP")• [Audio Dynamics ](<./Audio_Dynamics_CHOP.md> "Audio Dynamics CHOP")• [Audio File In ](<./Audio_File_In_CHOP.md> "Audio File In CHOP")• [Audio File Out ](<./Audio_File_Out_CHOP.md> "Audio File Out CHOP")• [Audio Filter ](<./Audio_Filter_CHOP.md> "Audio Filter CHOP")• [Audio Movie ](<./Audio_Movie_CHOP.md> "Audio Movie CHOP")• [Audio NDI ](<./Audio_NDI_CHOP.md> "Audio NDI CHOP")• [Audio Oscillator ](<./Audio_Oscillator_CHOP.md> "Audio Oscillator CHOP")• [Audio Para EQ ](<./Audio_Para_EQ_CHOP.md> "Audio Para EQ CHOP")• [Audio Play ](<./Audio_Play_CHOP.md> "Audio Play CHOP")• [Audio Render ](<./Audio_Render_CHOP.md> "Audio Render CHOP")• [Audio Spectrum ](<./Audio_Spectrum_CHOP.md> "Audio Spectrum CHOP")• [Audio Stream In ](<./Audio_Stream_In_CHOP.md> "Audio Stream In CHOP")• [Audio Stream Out ](<./Audio_Stream_Out_CHOP.md> "Audio Stream Out CHOP")• [Audio VST ](<./Audio_VST_CHOP.md> "Audio VST CHOP")• [Audio Web Render ](<./Audio_Web_Render_CHOP.md> "Audio Web Render CHOP")• [Beat ](<./Beat_CHOP.md> "Beat CHOP")• [Bind ](<./Bind_CHOP.md> "Bind CHOP")• [BlackTrax ](<./BlackTrax_CHOP.md> "BlackTrax CHOP")• [Blend ](<./Blend_CHOP.md> "Blend CHOP")• [Blob Track ](<./Blob_Track_CHOP.md> "Blob Track CHOP")• [Body Track ](<./Body_Track_CHOP.md> "Body Track CHOP")• [Bullet Solver ](<./Bullet_Solver_CHOP.md> "Bullet Solver CHOP")• [CHOP ](<./CHOP.md> "CHOP")• [Clip Blender ](<./Clip_Blender_CHOP.md> "Clip Blender CHOP")• [Clip ](<./Clip_CHOP.md> "Clip CHOP")• [Clock ](<./Clock_CHOP.md> "Clock CHOP")• [Composite ](<./Composite_CHOP.md> "Composite CHOP")• [Constant ](<./Constant_CHOP.md> "Constant CHOP")• [Copy ](<./Copy_CHOP.md> "Copy CHOP")• [Count ](<./Count_CHOP.md> "Count CHOP")• [CPlusPlus ](<./CPlusPlus_CHOP.md> "CPlusPlus CHOP")• [Cross ](<./Cross_CHOP.md> "Cross CHOP")• [Cycle ](<./Cycle_CHOP.md> "Cycle CHOP")• [DAT to ](<./DAT_to_CHOP.md> "DAT to CHOP")• [Delay ](<./Delay_CHOP.md> "Delay CHOP")• [Delete ](<./Delete_CHOP.md> "Delete CHOP")• [DMX In ](<./DMX_In_CHOP.md> "DMX In CHOP")• [DMX Out ](<./DMX_Out_CHOP.md> "DMX Out CHOP")• [Envelope ](<./Envelope_CHOP.md> "Envelope CHOP")• [EtherDream ](<./EtherDream_CHOP.md> "EtherDream CHOP")• [Event ](<./Event_CHOP.md> "Event CHOP")• [Expression ](<./Expression_CHOP.md> "Expression CHOP")• [Extend ](<./Extend_CHOP.md> "Extend CHOP")• [Face Track ](<./Face_Track_CHOP.md> "Face Track CHOP")• [Fan ](<./Fan_CHOP.md> "Fan CHOP")• [Feedback ](<./Feedback_CHOP.md> "Feedback CHOP")• [File In ](<./File_In_CHOP.md> "File In CHOP")• [File Out ](<./File_Out_CHOP.md> "File Out CHOP")• [Filter ](<./Filter_CHOP.md> "Filter CHOP")• [FreeD In ](<./FreeD_In_CHOP.md> "FreeD In CHOP")• [FreeD Out ](<./FreeD_Out_CHOP.md> "FreeD Out CHOP")• Function • [Gesture ](<./Gesture_CHOP.md> "Gesture CHOP")• [Handle ](<./Handle_CHOP.md> "Handle CHOP")• [Helios DAC ](<./Helios_DAC_CHOP.md> "Helios DAC CHOP")• [Hog ](<./Hog_CHOP.md> "Hog CHOP")• [Hokuyo ](<./Hokuyo_CHOP.md> "Hokuyo CHOP")• [Hold ](<./Hold_CHOP.md> "Hold CHOP")• [Import Select ](<./Import_Select_CHOP.md> "Import Select CHOP")• [In ](<./In_CHOP.md> "In CHOP")• [Info ](<./Info_CHOP.md> "Info CHOP")• [Interpolate ](<./Interpolate_CHOP.md> "Interpolate CHOP")• [Introduction To s Vid ](<./Introduction_To_CHOPs_Vid.md> "Introduction To CHOPs Vid")• [Inverse Curve ](<./Inverse_Curve_CHOP.md> "Inverse Curve CHOP")• [Inverse Kin ](<./Inverse_Kin_CHOP.md> "Inverse Kin CHOP")• [Join ](<./Join_CHOP.md> "Join CHOP")• [Joystick ](<./Joystick_CHOP.md> "Joystick CHOP")• [Keyboard In ](<./Keyboard_In_CHOP.md> "Keyboard In CHOP")• [Keyframe ](<./Keyframe_CHOP.md> "Keyframe CHOP")• [Kinect Azure ](<./Kinect_Azure_CHOP.md> "Kinect Azure CHOP")• [Kinect ](<./Kinect_CHOP.md> "Kinect CHOP")• [Lag ](<./Lag_CHOP.md> "Lag CHOP")• [Laser ](<./Laser_CHOP.md> "Laser CHOP")• [Laser Device ](<./Laser_Device_CHOP.md> "Laser Device CHOP")• [Leap Motion ](<./Leap_Motion_CHOP.md> "Leap Motion CHOP")• [Leuze ROD4 ](<./Leuze_ROD4_CHOP.md> "Leuze ROD4 CHOP")• [LFO ](<./LFO_CHOP.md> "LFO CHOP")• [Limit ](<./Limit_CHOP.md> "Limit CHOP")• [Logic ](<./Logic_CHOP.md> "Logic CHOP")• [Lookup ](<./Lookup_CHOP.md> "Lookup CHOP")• [LTC In ](<./LTC_In_CHOP.md> "LTC In CHOP")• [LTC Out ](<./LTC_Out_CHOP.md> "LTC Out CHOP")• [Math ](<./Math_CHOP.md> "Math CHOP")• [Merge ](<./Merge_CHOP.md> "Merge CHOP")• [MIDI In ](<./MIDI_In_CHOP.md> "MIDI In CHOP")• [MIDI In Map ](<./MIDI_In_Map_CHOP.md> "MIDI In Map CHOP")• [MIDI Out ](<./MIDI_Out_CHOP.md> "MIDI Out CHOP")• [MoSys ](<./MoSys_CHOP.md> "MoSys CHOP")• [Mouse In ](<./Mouse_In_CHOP.md> "Mouse In CHOP")• [Mouse Out ](<./Mouse_Out_CHOP.md> "Mouse Out CHOP")• [Ncam ](<./Ncam_CHOP.md> "Ncam CHOP")• [Noise ](<./Noise_CHOP.md> "Noise CHOP")• [Null ](<./Null_CHOP.md> "Null CHOP")• [OAK Device ](<./OAK_Device_CHOP.md> "OAK Device CHOP")• [OAK Select ](<./OAK_Select_CHOP.md> "OAK Select CHOP")• [Object ](<./Object_CHOP.md> "Object CHOP")• [Oculus Audio ](<./Oculus_Audio_CHOP.md> "Oculus Audio CHOP")• [Oculus Rift ](<./Oculus_Rift_CHOP.md> "Oculus Rift CHOP")• [OpenVR ](<./OpenVR_CHOP.md> "OpenVR CHOP")• [OptiTrack In ](<./OptiTrack_In_CHOP.md> "OptiTrack In CHOP")• [OSC In ](<./OSC_In_CHOP.md> "OSC In CHOP")• [OSC Out ](<./OSC_Out_CHOP.md> "OSC Out CHOP")• [Out ](<./Out_CHOP.md> "Out CHOP")• [Override ](<./Override_CHOP.md> "Override CHOP")• [Pan Tilt ](<./Pan_Tilt_CHOP.md> "Pan Tilt CHOP")• [Panel ](<./Panel_CHOP.md> "Panel CHOP")• [Pangolin ](<./Pangolin_CHOP.md> "Pangolin CHOP")• [Parameter ](<./Parameter_CHOP.md> "Parameter CHOP")• [Pattern ](<./Pattern_CHOP.md> "Pattern CHOP")• [Perform ](<./Perform_CHOP.md> "Perform CHOP")• [Phaser ](<./Phaser_CHOP.md> "Phaser CHOP")• [Pipe In ](<./Pipe_In_CHOP.md> "Pipe In CHOP")• [Pipe Out ](<./Pipe_Out_CHOP.md> "Pipe Out CHOP")• [POP to ](<./POP_to_CHOP.md> "POP to CHOP")• [PosiStageNet ](<./PosiStageNet_CHOP.md> "PosiStageNet CHOP")• [Pulse ](<./Pulse_CHOP.md> "Pulse CHOP")• [RealSense ](<./RealSense_CHOP.md> "RealSense CHOP")• [Record ](<./Record_CHOP.md> "Record CHOP")• [Rename ](<./Rename_CHOP.md> "Rename CHOP")• [Render Pick ](<./Render_Pick_CHOP.md> "Render Pick CHOP")• [RenderStream In ](<./RenderStream_In_CHOP.md> "RenderStream In CHOP")• [Reorder ](<./Reorder_CHOP.md> "Reorder CHOP")• [Replace ](<./Replace_CHOP.md> "Replace CHOP")• [Resample ](<./Resample_CHOP.md> "Resample CHOP")• [S Curve ](<./S_Curve_CHOP.md> "S Curve CHOP")• [Scan ](<./Scan_CHOP.md> "Scan CHOP")• [Script ](<./Script_CHOP.md> "Script CHOP")• [Select ](<./Select_CHOP.md> "Select CHOP")• [Sequencer ](<./Sequencer_CHOP.md> "Sequencer CHOP")• [Serial ](<./Serial_CHOP.md> "Serial CHOP")• [Shared Mem In ](<./Shared_Mem_In_CHOP.md> "Shared Mem In CHOP")• [Shared Mem Out ](<./Shared_Mem_Out_CHOP.md> "Shared Mem Out CHOP")• [Shift ](<./Shift_CHOP.md> "Shift CHOP")• [Shuffle ](<./Shuffle_CHOP.md> "Shuffle CHOP")• [Slope ](<./Slope_CHOP.md> "Slope CHOP")• [SOP to ](<./SOP_to_CHOP.md> "SOP to CHOP")• [Sort ](<./Sort_CHOP.md> "Sort CHOP")• [Speed ](<./Speed_CHOP.md> "Speed CHOP")• [Splice ](<./Splice_CHOP.md> "Splice CHOP")• [Spring ](<./Spring_CHOP.md> "Spring CHOP")• [ST2110 Device ](<./ST2110_Device_CHOP.md> "ST2110 Device CHOP")• [Stretch ](<./Stretch_CHOP.md> "Stretch CHOP")• [Stype In ](<./Stype_In_CHOP.md> "Stype In CHOP")• [Stype Out ](<./Stype_Out_CHOP.md> "Stype Out CHOP")• [Switch ](<./Switch_CHOP.md> "Switch CHOP")• [Sync In ](<./Sync_In_CHOP.md> "Sync In CHOP")• [Sync Out ](<./Sync_Out_CHOP.md> "Sync Out CHOP")• [Tablet ](<./Tablet_CHOP.md> "Tablet CHOP")• [Time Slice ](<./Time_Slice_CHOP.md> "Time Slice CHOP")• [Timecode ](<./Timecode_CHOP.md> "Timecode CHOP")• [Timeline ](<./Timeline_CHOP.md> "Timeline CHOP")• [Timer ](<./Timer_CHOP.md> "Timer CHOP")• [TOP to ](<./TOP_to_CHOP.md> "TOP to CHOP")• [Touch In ](<./Touch_In_CHOP.md> "Touch In CHOP")• [Touch Out ](<./Touch_Out_CHOP.md> "Touch Out CHOP")• [Trail ](<./Trail_CHOP.md> "Trail CHOP")• [Transform ](<./Transform_CHOP.md> "Transform CHOP")• [Transform XYZ ](<./Transform_XYZ_CHOP.md> "Transform XYZ CHOP")• [Trigger ](<./Trigger_CHOP.md> "Trigger CHOP")• [Trim ](<./Trim_CHOP.md> "Trim CHOP")• [Warp ](<./Warp_CHOP.md> "Warp CHOP")• [Wave ](<./Wave_CHOP.md> "Wave CHOP")• [WrnchAI ](<./WrnchAI_CHOP.md> "WrnchAI CHOP")• [ZED ](<./ZED_CHOP.md> "ZED CHOP")
