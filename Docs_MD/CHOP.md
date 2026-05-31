# CHOP

## 

Summary

**CHOPs** , or **CHannel OPerators** , are a powerful technology which enables the processing of motion, audio, math, logic, MIDI data, numeric info and data streamed from/to devices and protocols. 

CHOPs are an [Operator Family](<./Operator_Family.md> "Operator Family") which operate on [Channels](<./Channel.md> "Channel") (a sequence of numbers ([Samples](<./Sample.md> "Sample"))). 

CHOPs provide a unique way of creating and editing motion and audio. The combination of procedural editing of motion, keyframe animation, motion capture and live controls provides you with a wide range of animation techniques. In keeping with the TouchDesigner procedural paradigm, channel operators combine and refine the data without destroying the original data. CHOPs were designed to reduce the tedium of motion editing and to help build and manage more complex motion. CHOPs enable creators to think about motion at a more creative level and to experiment with motion more than any other animation technology. 

A CHOP contains one or more named **channels**. The channels of a CHOP is made of a sequence of one or more "**samples** ". A sample is one floating point number per channel. 

A CHOP has a **sample rate** , which is the number samples-per-second, which matters only when a CHOP represents animation or audio over time. 

The length of a CHOP is expressed in samples, and when the CHOP represents animation or audio, the length can also be expressed in seconds or frames. A frame is a unit of time of the timeline, typically 1/60 of a second. 

A CHOP creates or modifies the [Channel](<./Channel.md> "Channel"), and then passes the channels on to the next CHOP in a network. CHOPs are then connected to object motion or any other animated part of TouchDesigner via "[exporting](<./Export.md> "Export")" and "channel references". 

See also [Category:CHOPs](<./Category-CHOPs.md> "Category:CHOPs") for a full list of articles related to CHOPs, especially [Anatomy of a CHOP](<./Anatomy_of_a_CHOP.md> "Anatomy of a CHOP") and [Time Slicing](<./Time_Slicing.md> "Time Slicing"). 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[CHOP Class](<./CHOP_Class.md> "CHOP Class")

## Sweet 16 CHOPs

Click the [video](<./Sweet_16_CHOPs_Vid.md> "Sweet 16 CHOPs Vid") above to watch an overview of all Sweet 16 CHOPs. Watch individual CHOP videos by clicking on the appropriate CHOP's video icon below. The following 16 CHOPs are commonly used, we recommend familiarizing yourself with them. 

CHOP | Purpose | Related CHOP  
---|---|---  
[Constant](<./Constant_CHOP.md> "Constant CHOP") | Create new channels. | [Pattern](<./Pattern_CHOP.md> "Pattern CHOP")  
[LFO](<./LFO_CHOP.md> "LFO CHOP") | Low Frequency Oscillator. | [Audio Oscillator](<./Audio_Oscillator_CHOP.md> "Audio Oscillator CHOP")  
[Noise](<./Noise_CHOP.md> "Noise CHOP") | Create semi-random patterns. |   
[Select](<./Select_CHOP.md> "Select CHOP") | Grab a channel from any other CHOP. | [Switch](<./Switch_CHOP.md> "Switch CHOP"), [Cross](<./Cross_CHOP.md> "Cross CHOP")  
[Merge](<./Merge_CHOP.md> "Merge CHOP") | Merge channels from two or more CHOPs. | [Shuffle](<./Shuffle_CHOP.md> "Shuffle CHOP")  
[Math](<./Math_CHOP.md> "Math CHOP") | Add, multiply or scale channels. | [Logic](<./Logic_CHOP.md> "Logic CHOP"), [Script](<./Script_CHOP.md> "Script CHOP")  
[Lag](<./Lag_CHOP.md> "Lag CHOP") | Smooth and delay a channel. | [Filter](<./Filter_CHOP.md> "Filter CHOP")  
[Speed](<./Speed_CHOP.md> "Speed CHOP") | Use speed to calculate distance. | [Count](<./Count_CHOP.md> "Count CHOP"), [Slope](<./Slope_CHOP.md> "Slope CHOP")  
[Lookup](<./Lookup_CHOP.md> "Lookup CHOP") | Use one channel to get values from another CHOP. | [Keyframe](<./Keyframe_CHOP.md> "Keyframe CHOP")  
[Trail](<./Trail_CHOP.md> "Trail CHOP") | Watch a time-history of CHOP channels. | [Perform](<./Perform_CHOP.md> "Perform CHOP")  
[SOP to](<./SOP_to_CHOP.md> "SOP to CHOP") | Record a time-history of channels. | [DAT to](<./DAT_to_CHOP.md> "DAT to CHOP"), [TOP to](<./TOP_to_CHOP.md> "TOP to CHOP")  
[Limit](<./Limit_CHOP.md> "Limit CHOP") | Restrict channels to a range or certain step values. | [Analyze](<./Analyze_CHOP.md> "Analyze CHOP")  
[Audio Device In](<./Audio_Device_In_CHOP.md> "Audio Device In CHOP") | Get audio from input device. | [Audio File In](<./Audio_File_In_CHOP.md> "Audio File In CHOP")  
[OSC In](<./OSC_In_CHOP.md> "OSC In CHOP") | Open Sound Control, MIDI. | [MIDI In Map](<./MIDI_In_Map_CHOP.md> "MIDI In Map CHOP")  
[Panel](<./Panel_CHOP.md> "Panel CHOP") | Get state, u, v etc values from any panel gadget. | [Info](<./Info_CHOP.md> "Info CHOP")  
[Timer](<./Timer_CHOP.md> "Timer CHOP") | Run timers, loops, delays and trigger events. | [Beat](<./Beat_CHOP.md> "Beat CHOP")  
  
All CHOPs are documented in the [Category:CHOPs](<./Category-CHOPs.md> "Category:CHOPs"). 

## CHOPs Create and Process Channels

CHOPs are procedural networks, where "procedural" means the operators are wired together so the output of one CHOP flows into the input of one or more other CHOPs, and the data flows automatically every time the display is updated (by default, 60 times per second). 

Some CHOPs, generator CHOPs, create CHOP channels from scratch. Some examples are the Constant CHOP, the Wave CHOP, and the Timing CHOP. CHOPs can also take data from 
* on-screen sliders, buttons, menus, XY-controllers, XYZ values from clicking in 3D viewers.
  * hardware devices including data via MIDI and OSC protocols.
  * other processes/applications feeding TouchDesigner through pipes.


CHOPs process channel data and connect the results to any other part of TouchDesigner. 

## Parts of a CHOP

A CHOP contains a set of **Channels** , plus control **[Parameters](</index.php?title=Parameters&action=edit&redlink=1> "Parameters \(page does not exist\)")** , a **sample rate** , some on/off **[Flags](</index.php?title=Flags&action=edit&redlink=1> "Flags \(page does not exist\)")** , and a **start/end interval**. 

The channels of a CHOP can represent motion, MIDI, audio, color maps, rolloff curves or lookup tables. Any data that can be represented as a sequence of numbers can be represent in CHOP channels. The sequence of numbers are called **samples**. 

Like all [Operators](<./Operator.md> "Operator"), CHOPs have **[Parameters](</index.php?title=Parameters&action=edit&redlink=1> "Parameters \(page does not exist\)")** used to define the data, plus the data channels, which are input/output from the CHOP as its data stream. The parameters are usually constant-valued, but can be time-dependent expressions. 

CHOPs' parameters can be expressed in different CHOP **units** : samples (indexes), frames or seconds. These units are selected by the user in a menu to the right of such parameters. Each sample index, starting from 0, corresponds to some frame number (based on frames per second), and a moment in time (seconds). 

The **sample rate** (samples per second) is used if the CHOP contains time-dependent motion or audio data. Audio has a high sample rate when compared to animated motion. 

Each CHOP has **flags** : 
* The Display flag marks the CHOP to be displayed in a [CHOP Viewer](<./CHOP_Viewer.md> "CHOP Viewer").
  * The Export flag causes the CHOP channel [exports](<./Export.md> "Export") to toggle on and off.
  * The Lock flag causes the CHOP to be locked and then can be hand-edited.
  * The [Bypass Flag](<./Bypass_Flag.md> "Bypass Flag") is a convenient way for a CHOP's effect to be disabled.


CHOPs can have any start/end indexes but all channels in a single CHOP share the same **start-end interval**. The interval goes from a start index to an end index and is not restricted to the length of any animation or timeline. 

Each CHOP also has a **comment field** to add a note to a CHOP to explain what it is doing in the network. An **info pop-up** can be opened by middle-clicking on the CHOP, this lists channel names and values, sample rate and intervals. 

In CHOPs, **Extend Conditions** determine what numbers you get when you try to get a channel value that is outside its start-end range - in its **Extend Regions** , before the CHOP's start time or after its end time. The CHOP may hold its last value, it may cycle, repeat, or be held at a default value. You can see a CHOP's extend conditions in the info pop-up (middle-mouse click on the CHOP), or by looking at a CHOP in the channel viewer outside its start-end range. You will see that a [Pattern CHOP](<./Pattern_CHOP.md> "Pattern CHOP") cycles and a [Keyframe CHOP](<./Keyframe_CHOP.md> "Keyframe CHOP") holds in the Extend Regions. 

You can change the Extend Conditions with an [Extend CHOP](<./Extend_CHOP.md> "Extend CHOP") or via menus on the Channel page in many CHOPs. 

See also [Anatomy of a CHOP](<./Anatomy_of_a_CHOP.md> "Anatomy of a CHOP"). 

## Inputs and Outputs

Each CHOP receives channels at its inputs. When the CHOP [cooks](<./Cook.md> "Cook"), the channels of the inputs are combined. The CHOP outputs the resulting channels to other CHOPs. 

CHOPs output their data channels as arrays of numbers, not keyframed, interpolated segments. Some CHOPs ([Keyframe CHOP](<./Keyframe_CHOP.md> "Keyframe CHOP")) retain interpolated segments internally, but all CHOPs always output their data as raw samples. If the CHOP's inputs are not changing and the control parameters are not time-dependent, the CHOP will be non-time-dependent and it will not cook every time the animation frame on the timeline advances. 

Some CHOPs output or use CHOP **attributes** , such as channels grouped as quaternion rotation channels. 

## Referencing and Exporting CHOP Channels

    _Main article:[Export](<./Export.md> "Export")_

Parameters of any node are able to get values from CHOP channels with expressions like the following: 
[code] 
    op('filter1')[0]
    op('filter1')['chan2']
    op('pattern1')['chan1'][99]    # gets the 100th sample of chan1
    
[/code]

However, exporting is preferred where possible. It is faster and involves less typing. 

CHOP data channels are exported to Components, SOPs, etc. to drive their parameters. CHOPs can be exported to any TouchDesigner operator's parameter. Each CHOP has an Export flag (and an Export Prefix, infrequently used), causing the CHOP to connect its channels to Components, SOPs, TOPs and so on. The Export flag and Export Prefix can also use automatic matching of channels names to find export destinations. For example, a CHOP "tx" channel could map to an Geometry Component's tx parameter. When a CHOP exports to an object, SOP or TOP, the parameters exported to are said to be overridden. 

## Difference Between a Sample and a Frame

A frame always refers to the timeline, which is expressed in frames or seconds, and frames & seconds are tied via a certain number of "frames per second" or FPS. The default FPS for TouchDesigner is 60, and with FPS of 60, there will always be 60 frames per second. A CHOP range can start at any frame number (or second), and end at any later frame number. A frame will always correspond to a certain time expressed in seconds. Precisely, seconds is`(frame-1)/FPS`. 

The sample index may have no relation to time or frame, as when a CHOP is used as lookup table. But when "index" is tied to time, the CHOP's samples per second (sample rate), determines how many samples per second there are, and even how many samples per frame. Some CHOPs default to 60 samples per second, which is 1 sample per frame. But CHOPs can be created or resampled to any sample rate, so a CHOP's sample rate of 240 samples per second gives 4 samples per frame, and audio at 24,000 samples per second is 400 samples per frame. 

Even if a CHOP is shifted in time to start at a frame number like 301 (10 seconds), its sample index always starts at 0. Its`op('wave1').sampleIndex`is 0 at its first sample. 

**NOTE** : Set the "frames per second" of the timeline for the project via the bottom of the timeline, or in Python`project.cookRate = 120`, for example. It is better to DO IT AT THE START OF A PROJECT, lest you get tripped up. Note each component can have its own timeline and its own sample rate. See [Timeline](<./Timeline.md> "Timeline"). 

## Sample Index and Value
* The horizontal axis is called the i-axis or the sample index-axis.
  * The vertical axis is called the v-axis or the value-axis.
  * A sample index is a point along the i-axis, denoted by i.
  * A value is a point along the v-axis, denoted by v.
  * A sample is an index-value pair (i,v). i.e. the value of a channel at a certain sample index.
  * A sample is made of a sample index and a sample value.
  * An interval is an index range, which goes from a start index to an end index.
  * A value range goes from a start value to an end value.
  * The index duration is the end index minus the start index + 1.
  * CHOP data channels are arrays of raw samples, in 32-bit floating point format, all computations are done at 64 bits, and parameters are stored as 64 bits.
  * Channels in a CHOP may be control (parameter) channels or data channels. CHOPs manipulate the data channels.
  * CHOPs can be evaluated at integer and non-integer indexes.
  * Frame is used when the index corresponds to time.
  * When speaking of animation frames, you can refer to start frame, end frame and frame range.

## Using`.chanIndex`in CHOP Parameters

A "Channel Index" is the channel number of a CHOP, 0 being the first channel, and is available for use in parameters in some CHOPs as`me.chanIndex`. Numerous CHOPs like the [Pattern CHOP](<./Pattern_CHOP.md> "Pattern CHOP"), [Math CHOP](<./Math_CHOP.md> "Math CHOP") and [Delay CHOP](<./Delay_CHOP.md> "Delay CHOP") have extra local members that allow the customization of each channel: The Python object for the operator has a`.chanIndex`member. For example, if the Pattern CHOP generates three channels you can put something like`[3, 4, 5][me.chanIndex]`in the Amplitude parameter to customize its value for each channel. The first channel will be evaluated with an Amplitude value 3, the second channel with a value of 5, etc. Search`me.chanIndex`in the wiki. See also the Scope parameter on most CHOPs to affect selective channels. 

## Common CHOP Members

There are Python members of a CHOP that are common to many or all CHOPs. See [CHOP Class](<./CHOP_Class.md> "CHOP Class") and [Channel Class](<./Channel_Class.md> "Channel Class"). 

## See Also

Introduction to CHOPs | [Uses of CHOPs](<./Uses_of_CHOPs.md> "Uses of CHOPs") | [Exporting from CHOPs to Parameters](<./Export.md> "Export")  
---|---|---  
[Common page of all CHOPs](<./CHOP_Common_Page.md> "CHOP Common Page") | [Channel page of CHOPs](<./CHOP_Channel_Page.md> "CHOP Channel Page") | [Other Frequent Parameters](<./Edit_Keyframes.md> "Edit Keyframes")  
[The Idea of Time Slicing](<./Time_Slicing.md> "Time Slicing") | [Exporting Channels](<./Export.md> "Export") | [CHOP Operator Variables](<./Variables.md> "Variables")  
[CHOP File Formats](<./File_Types.md> "File Types") | [Tscript Expressions](<./Expression.md> "Expression") | [Category:MIDI](</index.php?title=Category:MIDI&action=edit&redlink=1> "Category:MIDI \(page does not exist\)") and [OSC](<./OSC.md> "OSC")  
[Manually Editing Key Frames](<./Edit_Keyframes.md> "Edit Keyframes") | [CHOP Techniques](<./CHOP_Techniques.md> "CHOP Techniques") | [Working with Audio](</index.php?title=Category:Audio&action=edit&redlink=1> "Category:Audio \(page does not exist\)")  
CHOPs   
---  
[Ableton Link ](<./Ableton_Link_CHOP.md> "Ableton Link CHOP")• [Analyze ](<./Analyze_CHOP.md> "Analyze CHOP")• [Angle ](<./Angle_CHOP.md> "Angle CHOP")• [Attribute ](<./Attribute_CHOP.md> "Attribute CHOP")• [Audio Band EQ ](<./Audio_Band_EQ_CHOP.md> "Audio Band EQ CHOP")• [Audio Binaural ](<./Audio_Binaural_CHOP.md> "Audio Binaural CHOP")• [Audio Device In ](<./Audio_Device_In_CHOP.md> "Audio Device In CHOP")• [Audio Device Out ](<./Audio_Device_Out_CHOP.md> "Audio Device Out CHOP")• [Audio Dynamics ](<./Audio_Dynamics_CHOP.md> "Audio Dynamics CHOP")• [Audio File In ](<./Audio_File_In_CHOP.md> "Audio File In CHOP")• [Audio File Out ](<./Audio_File_Out_CHOP.md> "Audio File Out CHOP")• [Experimental:Audio File Out ](</index.php?title=Experimental:Audio_File_Out_CHOP&action=edit&redlink=1> "Experimental:Audio File Out CHOP \(page does not exist\)")• [Audio Filter ](<./Audio_Filter_CHOP.md> "Audio Filter CHOP")• [Audio Movie ](<./Audio_Movie_CHOP.md> "Audio Movie CHOP")• [Experimental:Audio Movie ](</index.php?title=Experimental:Audio_Movie_CHOP&action=edit&redlink=1> "Experimental:Audio Movie CHOP \(page does not exist\)")• [Audio NDI ](<./Audio_NDI_CHOP.md> "Audio NDI CHOP")• [Audio Oscillator ](<./Audio_Oscillator_CHOP.md> "Audio Oscillator CHOP")• [Audio Para EQ ](<./Audio_Para_EQ_CHOP.md> "Audio Para EQ CHOP")• [Audio Play ](<./Audio_Play_CHOP.md> "Audio Play CHOP")• [Audio Render ](<./Audio_Render_CHOP.md> "Audio Render CHOP")• [Experimental:Audio Render ](</index.php?title=Experimental:Audio_Render_CHOP&action=edit&redlink=1> "Experimental:Audio Render CHOP \(page does not exist\)")• [Audio Spectrum ](<./Audio_Spectrum_CHOP.md> "Audio Spectrum CHOP")• [Audio Stream In ](<./Audio_Stream_In_CHOP.md> "Audio Stream In CHOP")• [Audio Stream Out ](<./Audio_Stream_Out_CHOP.md> "Audio Stream Out CHOP")• [Audio VST ](<./Audio_VST_CHOP.md> "Audio VST CHOP")• [Audio Web Render ](<./Audio_Web_Render_CHOP.md> "Audio Web Render CHOP")• [Beat ](<./Beat_CHOP.md> "Beat CHOP")• [Bind ](<./Bind_CHOP.md> "Bind CHOP")• [BlackTrax ](<./BlackTrax_CHOP.md> "BlackTrax CHOP")• [Blend ](<./Blend_CHOP.md> "Blend CHOP")• [Blob Track ](<./Blob_Track_CHOP.md> "Blob Track CHOP")• [Body Track ](<./Body_Track_CHOP.md> "Body Track CHOP")• [Experimental:Body Track ](</index.php?title=Experimental:Body_Track_CHOP&action=edit&redlink=1> "Experimental:Body Track CHOP \(page does not exist\)")• [Bullet Solver ](<./Bullet_Solver_CHOP.md> "Bullet Solver CHOP")• [Experimental:CHOP ](</Experimental:CHOP> "Experimental:CHOP")• [Clip Blender ](<./Clip_Blender_CHOP.md> "Clip Blender CHOP")• [Clip ](<./Clip_CHOP.md> "Clip CHOP")• [Clock ](<./Clock_CHOP.md> "Clock CHOP")• [Experimental:Clock ](</Experimental:Clock_CHOP> "Experimental:Clock CHOP")• [Composite ](<./Composite_CHOP.md> "Composite CHOP")• [Constant ](<./Constant_CHOP.md> "Constant CHOP")• [Copy ](<./Copy_CHOP.md> "Copy CHOP")• [Count ](<./Count_CHOP.md> "Count CHOP")• [CPlusPlus ](<./CPlusPlus_CHOP.md> "CPlusPlus CHOP")• [Cross ](<./Cross_CHOP.md> "Cross CHOP")• [Cycle ](<./Cycle_CHOP.md> "Cycle CHOP")• [DAT to ](<./DAT_to_CHOP.md> "DAT to CHOP")• [Delay ](<./Delay_CHOP.md> "Delay CHOP")• [Delete ](<./Delete_CHOP.md> "Delete CHOP")• [DMX In ](<./DMX_In_CHOP.md> "DMX In CHOP")• [DMX Out ](<./DMX_Out_CHOP.md> "DMX Out CHOP")• [Experimental:DMX Out ](</Experimental:DMX_Out_CHOP> "Experimental:DMX Out CHOP")• [Envelope ](<./Envelope_CHOP.md> "Envelope CHOP")• [EtherDream ](<./EtherDream_CHOP.md> "EtherDream CHOP")• [Event ](<./Event_CHOP.md> "Event CHOP")• [Expression ](<./Expression_CHOP.md> "Expression CHOP")• [Extend ](<./Extend_CHOP.md> "Extend CHOP")• [Face Track ](<./Face_Track_CHOP.md> "Face Track CHOP")• [Experimental:Face Track ](</Experimental:Face_Track_CHOP> "Experimental:Face Track CHOP")• [Fan ](<./Fan_CHOP.md> "Fan CHOP")• [Feedback ](<./Feedback_CHOP.md> "Feedback CHOP")• [File In ](<./File_In_CHOP.md> "File In CHOP")• [File Out ](<./File_Out_CHOP.md> "File Out CHOP")• [Filter ](<./Filter_CHOP.md> "Filter CHOP")• [Experimental:Filter ](</Experimental:Filter_CHOP> "Experimental:Filter CHOP")• [FreeD In ](<./FreeD_In_CHOP.md> "FreeD In CHOP")• [FreeD Out ](<./FreeD_Out_CHOP.md> "FreeD Out CHOP")• [Function ](<./Function_CHOP.md> "Function CHOP")• [Gesture ](<./Gesture_CHOP.md> "Gesture CHOP")• [Handle ](<./Handle_CHOP.md> "Handle CHOP")• [Helios DAC ](<./Helios_DAC_CHOP.md> "Helios DAC CHOP")• [Hog ](<./Hog_CHOP.md> "Hog CHOP")• [Hokuyo ](<./Hokuyo_CHOP.md> "Hokuyo CHOP")• [Hold ](<./Hold_CHOP.md> "Hold CHOP")• [Import Select ](<./Import_Select_CHOP.md> "Import Select CHOP")• [In ](<./In_CHOP.md> "In CHOP")• [Info ](<./Info_CHOP.md> "Info CHOP")• [Interpolate ](<./Interpolate_CHOP.md> "Interpolate CHOP")• [Introduction To s Vid ](<./Introduction_To_CHOPs_Vid.md> "Introduction To CHOPs Vid")• [Inverse Curve ](<./Inverse_Curve_CHOP.md> "Inverse Curve CHOP")• [Inverse Kin ](<./Inverse_Kin_CHOP.md> "Inverse Kin CHOP")• [Join ](<./Join_CHOP.md> "Join CHOP")• [Joystick ](<./Joystick_CHOP.md> "Joystick CHOP")• [Keyboard In ](<./Keyboard_In_CHOP.md> "Keyboard In CHOP")• [Keyframe ](<./Keyframe_CHOP.md> "Keyframe CHOP")• [Kinect Azure ](<./Kinect_Azure_CHOP.md> "Kinect Azure CHOP")• [Kinect ](<./Kinect_CHOP.md> "Kinect CHOP")• [Lag ](<./Lag_CHOP.md> "Lag CHOP")• [Laser ](<./Laser_CHOP.md> "Laser CHOP")• [Experimental:Laser ](</Experimental:Laser_CHOP> "Experimental:Laser CHOP")• [Laser Device ](<./Laser_Device_CHOP.md> "Laser Device CHOP")• [Experimental:Laser Device ](</Experimental:Laser_Device_CHOP> "Experimental:Laser Device CHOP")• [Leap Motion ](<./Leap_Motion_CHOP.md> "Leap Motion CHOP")• [Leuze ROD4 ](<./Leuze_ROD4_CHOP.md> "Leuze ROD4 CHOP")• [LFO ](<./LFO_CHOP.md> "LFO CHOP")• [Limit ](<./Limit_CHOP.md> "Limit CHOP")• [Logic ](<./Logic_CHOP.md> "Logic CHOP")• [Lookup ](<./Lookup_CHOP.md> "Lookup CHOP")• [LTC In ](<./LTC_In_CHOP.md> "LTC In CHOP")• [LTC Out ](<./LTC_Out_CHOP.md> "LTC Out CHOP")• [Math ](<./Math_CHOP.md> "Math CHOP")• [Merge ](<./Merge_CHOP.md> "Merge CHOP")• [MIDI In ](<./MIDI_In_CHOP.md> "MIDI In CHOP")• [MIDI In Map ](<./MIDI_In_Map_CHOP.md> "MIDI In Map CHOP")• [MIDI Out ](<./MIDI_Out_CHOP.md> "MIDI Out CHOP")• [MoSys ](<./MoSys_CHOP.md> "MoSys CHOP")• [Mouse In ](<./Mouse_In_CHOP.md> "Mouse In CHOP")• [Mouse Out ](<./Mouse_Out_CHOP.md> "Mouse Out CHOP")• [Ncam ](<./Ncam_CHOP.md> "Ncam CHOP")• [Noise ](<./Noise_CHOP.md> "Noise CHOP")• [Null ](<./Null_CHOP.md> "Null CHOP")• [OAK Device ](<./OAK_Device_CHOP.md> "OAK Device CHOP")• [OAK Select ](<./OAK_Select_CHOP.md> "OAK Select CHOP")• [Object ](<./Object_CHOP.md> "Object CHOP")• [Oculus Audio ](<./Oculus_Audio_CHOP.md> "Oculus Audio CHOP")• [Oculus Rift ](<./Oculus_Rift_CHOP.md> "Oculus Rift CHOP")• [OpenVR ](<./OpenVR_CHOP.md> "OpenVR CHOP")• [OptiTrack In ](<./OptiTrack_In_CHOP.md> "OptiTrack In CHOP")• [OSC In ](<./OSC_In_CHOP.md> "OSC In CHOP")• [OSC Out ](<./OSC_Out_CHOP.md> "OSC Out CHOP")• [Out ](<./Out_CHOP.md> "Out CHOP")• [Override ](<./Override_CHOP.md> "Override CHOP")• [Experimental:Pan Tilt ](</Experimental:Pan_Tilt_CHOP> "Experimental:Pan Tilt CHOP")• [Panel ](<./Panel_CHOP.md> "Panel CHOP")• [Pangolin ](<./Pangolin_CHOP.md> "Pangolin CHOP")• [Experimental:Pangolin ](</Experimental:Pangolin_CHOP> "Experimental:Pangolin CHOP")• [Parameter ](<./Parameter_CHOP.md> "Parameter CHOP")• [Experimental:Parameter ](</Experimental:Parameter_CHOP> "Experimental:Parameter CHOP")• [Pattern ](<./Pattern_CHOP.md> "Pattern CHOP")• [Perform ](<./Perform_CHOP.md> "Perform CHOP")• [Phaser ](<./Phaser_CHOP.md> "Phaser CHOP")• [Pipe In ](<./Pipe_In_CHOP.md> "Pipe In CHOP")• [Pipe Out ](<./Pipe_Out_CHOP.md> "Pipe Out CHOP")• [Experimental:POP to ](</Experimental:POP_to_CHOP> "Experimental:POP to CHOP")• [PosiStageNet ](<./PosiStageNet_CHOP.md> "PosiStageNet CHOP")• [Pulse ](<./Pulse_CHOP.md> "Pulse CHOP")• [RealSense ](<./RealSense_CHOP.md> "RealSense CHOP")• [Record ](<./Record_CHOP.md> "Record CHOP")• [Rename ](<./Rename_CHOP.md> "Rename CHOP")• [Render Pick ](<./Render_Pick_CHOP.md> "Render Pick CHOP")• [RenderStream In ](<./RenderStream_In_CHOP.md> "RenderStream In CHOP")• [Reorder ](<./Reorder_CHOP.md> "Reorder CHOP")• [Replace ](<./Replace_CHOP.md> "Replace CHOP")• [Resample ](<./Resample_CHOP.md> "Resample CHOP")• [Experimental:Resample ](</Experimental:Resample_CHOP> "Experimental:Resample CHOP")• [S Curve ](<./S_Curve_CHOP.md> "S Curve CHOP")• [Scan ](<./Scan_CHOP.md> "Scan CHOP")• [Script ](<./Script_CHOP.md> "Script CHOP")• [Experimental:Script ](</Experimental:Script_CHOP> "Experimental:Script CHOP")• [Select ](<./Select_CHOP.md> "Select CHOP")• [Sequencer ](<./Sequencer_CHOP.md> "Sequencer CHOP")• [Serial ](<./Serial_CHOP.md> "Serial CHOP")• [Shared Mem In ](<./Shared_Mem_In_CHOP.md> "Shared Mem In CHOP")• [Shared Mem Out ](<./Shared_Mem_Out_CHOP.md> "Shared Mem Out CHOP")• [Shift ](<./Shift_CHOP.md> "Shift CHOP")• [Shuffle ](<./Shuffle_CHOP.md> "Shuffle CHOP")• [Slope ](<./Slope_CHOP.md> "Slope CHOP")• [SOP to ](<./SOP_to_CHOP.md> "SOP to CHOP")• [Sort ](<./Sort_CHOP.md> "Sort CHOP")• [Speed ](<./Speed_CHOP.md> "Speed CHOP")• [Experimental:Speed ](</Experimental:Speed_CHOP> "Experimental:Speed CHOP")• [Splice ](<./Splice_CHOP.md> "Splice CHOP")• [Spring ](<./Spring_CHOP.md> "Spring CHOP")• [Experimental:ST2110 Device ](</Experimental:ST2110_Device_CHOP> "Experimental:ST2110 Device CHOP")• [Stretch ](<./Stretch_CHOP.md> "Stretch CHOP")• [Experimental:Stretch ](</Experimental:Stretch_CHOP> "Experimental:Stretch CHOP")• [Stype In ](<./Stype_In_CHOP.md> "Stype In CHOP")• [Stype Out ](<./Stype_Out_CHOP.md> "Stype Out CHOP")• [Switch ](<./Switch_CHOP.md> "Switch CHOP")• [Sync In ](<./Sync_In_CHOP.md> "Sync In CHOP")• [Sync Out ](<./Sync_Out_CHOP.md> "Sync Out CHOP")• [Tablet ](<./Tablet_CHOP.md> "Tablet CHOP")• [Time Slice ](<./Time_Slice_CHOP.md> "Time Slice CHOP")• [Timecode ](<./Timecode_CHOP.md> "Timecode CHOP")• [Experimental:Timecode ](</Experimental:Timecode_CHOP> "Experimental:Timecode CHOP")• [Timeline ](<./Timeline_CHOP.md> "Timeline CHOP")• [Timer ](<./Timer_CHOP.md> "Timer CHOP")• [Experimental:Timer ](</Experimental:Timer_CHOP> "Experimental:Timer CHOP")• [TOP to ](<./TOP_to_CHOP.md> "TOP to CHOP")• [Experimental:TOP to ](</Experimental:TOP_to_CHOP> "Experimental:TOP to CHOP")• [Touch In ](<./Touch_In_CHOP.md> "Touch In CHOP")• [Experimental:Touch In ](</Experimental:Touch_In_CHOP> "Experimental:Touch In CHOP")• [Touch Out ](<./Touch_Out_CHOP.md> "Touch Out CHOP")• [Trail ](<./Trail_CHOP.md> "Trail CHOP")• [Transform ](<./Transform_CHOP.md> "Transform CHOP")• [Transform XYZ ](<./Transform_XYZ_CHOP.md> "Transform XYZ CHOP")• [Trigger ](<./Trigger_CHOP.md> "Trigger CHOP")• [Experimental:Trigger ](</Experimental:Trigger_CHOP> "Experimental:Trigger CHOP")• [Trim ](<./Trim_CHOP.md> "Trim CHOP")• [Warp ](<./Warp_CHOP.md> "Warp CHOP")• [Wave ](<./Wave_CHOP.md> "Wave CHOP")• [WrnchAI ](<./WrnchAI_CHOP.md> "WrnchAI CHOP")• [ZED ](<./ZED_CHOP.md> "ZED CHOP")• [Experimental:ZED ](</Experimental:ZED_CHOP> "Experimental:ZED CHOP")
