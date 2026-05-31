# Laser CHOP

## 

Summary

The Laser CHOP produces channels that can drive a laser projector. It uses the points and lines of a POP, SOP or CHOP and outputs the channels at a specified sample rate, typically 10,000 to 96,000 samples per second. The Laser CHOP gives optimal control over the movement of the reflectors of the laser projector as well as enhanced color control. In particular, it gives better control of lines being straight, end-points being not cut off or over-drawn, and eliminating tails, all adjustable using a set of parameters. 

When sending CHOP channels to the Laser CHOP, the CHOP expects`x`and`y`channels and every sample will be interpreted as a point to be drawn. To draw multiple shapes, also specify a channel named`id`to identify each shape. Points with`id = 0`are part of the first shape, points with`id = 1`form the second shape. All other channels will be interpreted as color channels and blanking will be applied to those. This makes it possible to drive lasers that have more than just RGB diodes active. 

The channels output from the Laser CHOP can be sent to the [Laser Device CHOP](<./Laser_Device_CHOP.md> "Laser Device CHOP") in case of controlling a Laser via the [ILDA Protocol](<https://en.wikipedia.org/wiki/International_Laser_Display_Association>), or the [Audio Device Out CHOP](<./Audio_Device_Out_CHOP.md> "Audio Device Out CHOP") in case of using one of LaserAnimation Sollinger's [AVB](<https://en.wikipedia.org/wiki/Audio_Video_Bridging>) capable devices, where the audio is output via the [Audio Device Out CHOP](<./Audio_Device_Out_CHOP.md> "Audio Device Out CHOP") to a low-latency AVB-ready audio device like those from MOTU, RME, LaserAnimation Sollinger or Apple macOS. 

[LaserAnimation Sollinger's AVB2ILDA devices](<https://laseranimation.com/en/products/avb-devices>) give you access to features for the professional sector. See [Lasers](<./Lasers.md> "Lasers"). 

The CHOP was developed with the help of [LaserAnimation Sollinger](<https://laseranimation.com/en/>) who guided us in speccing and implementing the necessary parameters, especially in regards of the blanking timing settings. 

**Tip** : See the [OP Snippets](<./OP_Snippets.md> "OP Snippets") for setup and usage examples. 

(The Laser CHOP replaces the legacy Scan CHOP.) 

**LASERS ARE DANGEROUS - DAMAGE TO YOUR OR THE AUDIENCE'S EYE SIGHT IS A VERY REAL RISK**
* If you plan to use lasers
1. Understand all the laws and regulations for laser operation in your area.
  2. Become a certified Laser Safety Officer (this is required by law in some areas). Courses are available from ILDA directly: [ILDA Laser Safety Courses](<https://www.ilda.com/LSOcourse.htm>)
* Make sure an emergency stop button is close to you at all times.
  * Do not let anyone enter the laser projection area unless all precautions have been taken to limit the output.
  * Make sure there are no reflective surfaces in the projection area that might cause the beam to reflect unintendedly.

### Corner Points

The Laser CHOP categorizes input points as either corner points or guide points. Prior to the 2025.30000 series of builds, all points were considered corner points. 

All input points are corner points by default. To set a point as either a corner or guide point, use a boolean attribute named`LasCorner`for SOP/POP inputs, or a`lascorner`channel for CHOP inputs.`LasCorner = 1`means it is a corner point. 

Guide points are simply points that help move the laser along a path or curve, and they will not have abrupt changes in line direction between the two line segments they're a part of. Guide points are only output once and never repeated. Guide points are also useful for point interpolation when stepping is done along the curve. 

Corner points essentially define the start/end points of an individual line strip on the laser. Interpolation of color and point position stepping is done between corner points, with guide points used for weighting. Corner points should also be used when there is an abrupt change in the laser direction (eg. right or acute angle) so that appropriate hold points can be added to increase sharpness of the image. 

Corner points repeat as a function of their angle and the corner hold parameters. Additionally, for extra per-point control, corner hold look-up factor and hold add can be used through special attributes in SOP/POP inputs, or channels in CHOP inputs: 

  *`LasCornerHoldAdd`(SOP or POP) or`lascornerholdadd`(CHOP)
  *`LasCornerHoldLookupFactor`(SOP or POP) or`lascornerholdlookupfactor`(CHOP)


Corner hold repeat is calculated as follows, where H is the hold value calculated from the angle/parameters: 
[code] 
    NumRepeatPoints = HoldAdd + HoldLookupFactor * H
[/code]

### Blanking

Blanking is the capability of a laser projector to rapidly turn on / off the laser when displaying animations. For example when displaying multiple shapes, the laser needs the ability of blanking to omit the empty spots between the shapes. Blanking is done automatically between shapes but quantity of blanking points is controlled through the set of blanking delay parameters on the Color Page, as well as the Blanking Step Size parameter on the Scanning Page. 

As the laser's mirrors are driven by motors, the positional data that is send to the laser is likely to be ahead of the actual mirror position - the mirror must catch up to the data. The Color data though is in time and as a result the effect can be visible tails at points where the laser switches off its color. Adjusting the blanking parameters can help prevent this. 

See also: [Laser Device CHOP](<./Laser_Device_CHOP.md> "Laser Device CHOP"), [Pangolin CHOP](<./Pangolin_CHOP.md> "Pangolin CHOP"), [Line Smooth POP](<./Line_Smooth_POP.md> "Line Smooth POP")

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[laserCHOP_Class](<./LaserCHOP_Class.md> "LaserCHOP Class")

## 

Parameters - Laser Page

Active`active`\- When disabled, the CHOP will zero out all channels. 

Source OP`source`\- ⊞ \- Select the source operator type for the laser image. 
* SOP`sop`\- Use a SOP as the source for the Laser image. Apart from position attributes, the SOP's point color attributes are used to determine the color output.
* CHOP`chop`\- Use a CHOP as the source for the Laser image. Tthe CHOP expects`x`and`y`channels and every sample will be interpreted as a point to be drawn. To draw multiple shapes, also specify a channel named`id`to identify each shape. Points with`id = 0`are part of the first shape, points with`id = 1`form the second shape. All other channels will be interpreted as color channels and blanking will be applied to those. This makes it possible to drive lasers that have more than just RGB diodes active.
* POP`pop`\- Use a POP as the source for the Laser image. Apart from position attributes, the POP's color attributes are used to determine the color output.


SOP`sop`\- Path to the SOP. The SOP's position and color attributes (as well as other miscellaneous attributes such as`LasCorner`) will be used to generate the laser points. 

CHOP`chop`\- Path to the CHOP. The input CHOP must have **x** , **y** channels for the point positions. In addition, it also supports **z** , **r** , **g** , **b** , and **id** channels. The **id** channel is used for grouping points together as a single shape. By default when no **id** channel is present, each point is separate and unconnected. Additional and arbitrarily named colour channels may be added for laser projectors that accept more than just r, g, b. Additional channels include: "lascorner", "lascornerholdadd", and "lascornerholdlookupfactor". 

POP`pop`\- Path to the POP. The POP's position and color attributes (as well as other miscellaneous attributes such as`LasCorner`) will be used to generate the laser points. 

Output Sample Rate`outputrate`\- The sample rate of the Laser CHOP, and the sample rate at which it will output to the laser. With the default 48000 samples per second and a 60fps frame rate, the Laser CHOP can output 800 position and color values per frame. 

Swap Output`swap`\- Lets you swap the x and y axis of the output. 

X Scale`xscale`\- Control the horizontal scale of the output. 

Y Scale`yscale`\- Control the vertical scale of the output. 

Rotate`rotate`\- Control the rotation of the output. 

Camera`camera`\- Specify the path to a Camera COMP used to draw a SOP from the cameras view. 

Update Method`updatemethod`\- ⊞ \- Control how the Laser CHOP pulls data from its source. 

In most cases you will want to keep this at the default setting "When All Points Drawn". 

There is a specific usage case that requires the "Every Frame" update method. Background is that the Laser CHOP might have to draw the input values over multiple frames. For example given a source with 200 sampling values. After applying all blanking and step sizes at a certain sample rate, the Laser might need more than one frame to draw the full image. The effect will be visible by the Laser image flickering. With the default setting, the Laser will grab a new set of samples from its input once it has completed drawing all previous values. With the "Every Frame" update method, the Laser will grab the updated values for the remaining samples after each frame. 
* When All Points Drawn`alldrawn`\- The Laser CHOP will read the source data once all points of the previous frame have been drawn.
* Every Frame`everyframe`\- The Laser CHOP will update the input every frame, no matter if it finished drawing the previous frame or not.


Frame Start Pulse`startpulse`\- When enabled, will insert a sample with all colors set to -1 at the beginning of the laser frame. 

Debug Channel`debugchan`\- When enabled, an extra channel with point state will be included: 
* -1 : Frame Start Pulse
  * 0 : Color
  * 1 : Corner Hold Point
  * 2 : Start Point Hold Time
  * 3 : Pre Blank On
  * 4 : Post Blank On
  * 5 : Blanking
  * 6 : Pre Blank Off
  * 7 : Post Blank Off


Corner Attribute Name`cornerattr`\- For SOP and POP inputs, optionally change the point attribute name used to specifiy if a point is a corner point. Default is`LasCorner`. 

Corner Hold Add Attribute Name`cornerholdaddattr`\- For SOP and POP inputs, optionally change the name of the point attribute used to add a constant value to the corner hold time. Default is`LasCornerHoldAdd`. 

Corner Hold Factor Attribute Name`cornerholdfactorattr`\- For SOP and POP inputs, optionally change the name of the point attribute used to apply a lookup factor to the corner point hold. Default is`LasCornerHoldLookupFactor`. 

## 

Parameters - Scanning Page

Step Size`stepsize`\- The distance each x,y can change while outputing color. 

Blanking Step Size`bstepsize`\- The distance each x,y can change while not outputing color (blanking). 

Minimum Corner Hold`mincornerhold`\- The minimum value of the corner hold of a point. The value of the corner hold of a point is calculated linearly in the range from the minimum to maximum corner hold, based on the steepness of the angle at the point. This angle is calculated with the following three points: the previous point, the point itself, and the next point. Example: when the angle at the point is 180 degrees then the corner hold of the point will be the minimum value. 

Maximum Corner Hold`maxcornerhold`\- The maximum value of the corner hold of a point. See Minimum corner Hold for more details. When the angle at the point is 0 degrees, then the corner hold will be the maximum value. If the maximum value is lower than the minimum then the maximum will be clamped upward. 

Corner Hold Lookup CHOP`cornerholdchop`\- Reference to a CHOP to use as the custom lookup curve when interpolating from min to max hold. By default (ie. when no CHOP is specified), then it is linearly interpolated. 

Closed Shape Overlap`closedoverlap`\- For closed shapes, the number of points (specified in milliseconds) to overlap the start/end, to utilize color interpolation and get a more uniform shape. 

## 

Parameters - Color Page

These parameters let you control how the color channels for the Laser are created. Especially paying attention to the blanking settings which will have to be adjusted matching the capabilities of your laser projector. 

Red Scale`redscale`\- Set the intensity of the Red Channel. 

Green Scale`greenscale`\- Set the intensity of the Green Channel. 

Blue Scale`bluescale`\- Set the intensity of the Blue Channel. 

Pre Blanking On Delay`preblankon`\- Set the time in ms the Laser should wait at a position before turning the color output off. 

Post Blanking On Delay`postblankon`\- Set the time in ms the Laser should wait at a position after turning the color output off. 

Pre Blanking Off Delay`preblankoff`\- Set the time in ms the Laser should wait at a position before turning the color output on. 

Post Blanking Off Delay`postblankoff`\- Set the time in ms the Laser should wait at a position after turning the color output on. 

Start-Point Hold Time`starthold`\- Set the time in ms the Laser should wait at the first point of a new data frame before continuing on. 

Color Delay`colordelay`\- Set the delay in ms of the color channels in the output. 

Interpolate Colors`interpcolors`\- When enabled, interpolates colors between points. 

Brightness Curve Lookup CHOP`brightnesscurvechop`\- Reference a CHOP to use as a custom look-up for soft-edge blending of closed shapes. 

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

Extra Information for the Laser CHOP can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). __

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


  
TouchDesigner Build: Latest\nwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditor2025.300002021.100002020.20000before 2020.20000

CHOPs   
---  
[Ableton Link ](<./Ableton_Link_CHOP.md> "Ableton Link CHOP")• [Analyze ](<./Analyze_CHOP.md> "Analyze CHOP")• [Angle ](<./Angle_CHOP.md> "Angle CHOP")• [Attribute ](<./Attribute_CHOP.md> "Attribute CHOP")• [Audio Band EQ ](<./Audio_Band_EQ_CHOP.md> "Audio Band EQ CHOP")• [Audio Binaural ](<./Audio_Binaural_CHOP.md> "Audio Binaural CHOP")• [Audio Device In ](<./Audio_Device_In_CHOP.md> "Audio Device In CHOP")• [Audio Device Out ](<./Audio_Device_Out_CHOP.md> "Audio Device Out CHOP")• [Audio Dynamics ](<./Audio_Dynamics_CHOP.md> "Audio Dynamics CHOP")• [Audio File In ](<./Audio_File_In_CHOP.md> "Audio File In CHOP")• [Audio File Out ](<./Audio_File_Out_CHOP.md> "Audio File Out CHOP")• [Audio Filter ](<./Audio_Filter_CHOP.md> "Audio Filter CHOP")• [Audio Movie ](<./Audio_Movie_CHOP.md> "Audio Movie CHOP")• [Audio NDI ](<./Audio_NDI_CHOP.md> "Audio NDI CHOP")• [Audio Oscillator ](<./Audio_Oscillator_CHOP.md> "Audio Oscillator CHOP")• [Audio Para EQ ](<./Audio_Para_EQ_CHOP.md> "Audio Para EQ CHOP")• [Audio Play ](<./Audio_Play_CHOP.md> "Audio Play CHOP")• [Audio Render ](<./Audio_Render_CHOP.md> "Audio Render CHOP")• [Audio Spectrum ](<./Audio_Spectrum_CHOP.md> "Audio Spectrum CHOP")• [Audio Stream In ](<./Audio_Stream_In_CHOP.md> "Audio Stream In CHOP")• [Audio Stream Out ](<./Audio_Stream_Out_CHOP.md> "Audio Stream Out CHOP")• [Audio VST ](<./Audio_VST_CHOP.md> "Audio VST CHOP")• [Audio Web Render ](<./Audio_Web_Render_CHOP.md> "Audio Web Render CHOP")• [Beat ](<./Beat_CHOP.md> "Beat CHOP")• [Bind ](<./Bind_CHOP.md> "Bind CHOP")• [BlackTrax ](<./BlackTrax_CHOP.md> "BlackTrax CHOP")• [Blend ](<./Blend_CHOP.md> "Blend CHOP")• [Blob Track ](<./Blob_Track_CHOP.md> "Blob Track CHOP")• [Body Track ](<./Body_Track_CHOP.md> "Body Track CHOP")• [Bullet Solver ](<./Bullet_Solver_CHOP.md> "Bullet Solver CHOP")• [CHOP ](<./CHOP.md> "CHOP")• [Clip Blender ](<./Clip_Blender_CHOP.md> "Clip Blender CHOP")• [Clip ](<./Clip_CHOP.md> "Clip CHOP")• [Clock ](<./Clock_CHOP.md> "Clock CHOP")• [Composite ](<./Composite_CHOP.md> "Composite CHOP")• [Constant ](<./Constant_CHOP.md> "Constant CHOP")• [Copy ](<./Copy_CHOP.md> "Copy CHOP")• [Count ](<./Count_CHOP.md> "Count CHOP")• [CPlusPlus ](<./CPlusPlus_CHOP.md> "CPlusPlus CHOP")• [Cross ](<./Cross_CHOP.md> "Cross CHOP")• [Cycle ](<./Cycle_CHOP.md> "Cycle CHOP")• [DAT to ](<./DAT_to_CHOP.md> "DAT to CHOP")• [Delay ](<./Delay_CHOP.md> "Delay CHOP")• [Delete ](<./Delete_CHOP.md> "Delete CHOP")• [DMX In ](<./DMX_In_CHOP.md> "DMX In CHOP")• [DMX Out ](<./DMX_Out_CHOP.md> "DMX Out CHOP")• [Envelope ](<./Envelope_CHOP.md> "Envelope CHOP")• [EtherDream ](<./EtherDream_CHOP.md> "EtherDream CHOP")• [Event ](<./Event_CHOP.md> "Event CHOP")• [Expression ](<./Expression_CHOP.md> "Expression CHOP")• [Extend ](<./Extend_CHOP.md> "Extend CHOP")• [Face Track ](<./Face_Track_CHOP.md> "Face Track CHOP")• [Fan ](<./Fan_CHOP.md> "Fan CHOP")• [Feedback ](<./Feedback_CHOP.md> "Feedback CHOP")• [File In ](<./File_In_CHOP.md> "File In CHOP")• [File Out ](<./File_Out_CHOP.md> "File Out CHOP")• [Filter ](<./Filter_CHOP.md> "Filter CHOP")• [FreeD In ](<./FreeD_In_CHOP.md> "FreeD In CHOP")• [FreeD Out ](<./FreeD_Out_CHOP.md> "FreeD Out CHOP")• [Function ](<./Function_CHOP.md> "Function CHOP")• [Gesture ](<./Gesture_CHOP.md> "Gesture CHOP")• [Handle ](<./Handle_CHOP.md> "Handle CHOP")• [Helios DAC ](<./Helios_DAC_CHOP.md> "Helios DAC CHOP")• [Hog ](<./Hog_CHOP.md> "Hog CHOP")• [Hokuyo ](<./Hokuyo_CHOP.md> "Hokuyo CHOP")• [Hold ](<./Hold_CHOP.md> "Hold CHOP")• [Import Select ](<./Import_Select_CHOP.md> "Import Select CHOP")• [In ](<./In_CHOP.md> "In CHOP")• [Info ](<./Info_CHOP.md> "Info CHOP")• [Interpolate ](<./Interpolate_CHOP.md> "Interpolate CHOP")• [Introduction To s Vid ](<./Introduction_To_CHOPs_Vid.md> "Introduction To CHOPs Vid")• [Inverse Curve ](<./Inverse_Curve_CHOP.md> "Inverse Curve CHOP")• [Inverse Kin ](<./Inverse_Kin_CHOP.md> "Inverse Kin CHOP")• [Join ](<./Join_CHOP.md> "Join CHOP")• [Joystick ](<./Joystick_CHOP.md> "Joystick CHOP")• [Keyboard In ](<./Keyboard_In_CHOP.md> "Keyboard In CHOP")• [Keyframe ](<./Keyframe_CHOP.md> "Keyframe CHOP")• [Kinect Azure ](<./Kinect_Azure_CHOP.md> "Kinect Azure CHOP")• [Kinect ](<./Kinect_CHOP.md> "Kinect CHOP")• [Lag ](<./Lag_CHOP.md> "Lag CHOP")• Laser • [Laser Device ](<./Laser_Device_CHOP.md> "Laser Device CHOP")• [Leap Motion ](<./Leap_Motion_CHOP.md> "Leap Motion CHOP")• [Leuze ROD4 ](<./Leuze_ROD4_CHOP.md> "Leuze ROD4 CHOP")• [LFO ](<./LFO_CHOP.md> "LFO CHOP")• [Limit ](<./Limit_CHOP.md> "Limit CHOP")• [Logic ](<./Logic_CHOP.md> "Logic CHOP")• [Lookup ](<./Lookup_CHOP.md> "Lookup CHOP")• [LTC In ](<./LTC_In_CHOP.md> "LTC In CHOP")• [LTC Out ](<./LTC_Out_CHOP.md> "LTC Out CHOP")• [Math ](<./Math_CHOP.md> "Math CHOP")• [Merge ](<./Merge_CHOP.md> "Merge CHOP")• [MIDI In ](<./MIDI_In_CHOP.md> "MIDI In CHOP")• [MIDI In Map ](<./MIDI_In_Map_CHOP.md> "MIDI In Map CHOP")• [MIDI Out ](<./MIDI_Out_CHOP.md> "MIDI Out CHOP")• [MoSys ](<./MoSys_CHOP.md> "MoSys CHOP")• [Mouse In ](<./Mouse_In_CHOP.md> "Mouse In CHOP")• [Mouse Out ](<./Mouse_Out_CHOP.md> "Mouse Out CHOP")• [Ncam ](<./Ncam_CHOP.md> "Ncam CHOP")• [Noise ](<./Noise_CHOP.md> "Noise CHOP")• [Null ](<./Null_CHOP.md> "Null CHOP")• [OAK Device ](<./OAK_Device_CHOP.md> "OAK Device CHOP")• [OAK Select ](<./OAK_Select_CHOP.md> "OAK Select CHOP")• [Object ](<./Object_CHOP.md> "Object CHOP")• [Oculus Audio ](<./Oculus_Audio_CHOP.md> "Oculus Audio CHOP")• [Oculus Rift ](<./Oculus_Rift_CHOP.md> "Oculus Rift CHOP")• [OpenVR ](<./OpenVR_CHOP.md> "OpenVR CHOP")• [OptiTrack In ](<./OptiTrack_In_CHOP.md> "OptiTrack In CHOP")• [OSC In ](<./OSC_In_CHOP.md> "OSC In CHOP")• [OSC Out ](<./OSC_Out_CHOP.md> "OSC Out CHOP")• [Out ](<./Out_CHOP.md> "Out CHOP")• [Override ](<./Override_CHOP.md> "Override CHOP")• [Pan Tilt ](<./Pan_Tilt_CHOP.md> "Pan Tilt CHOP")• [Panel ](<./Panel_CHOP.md> "Panel CHOP")• [Pangolin ](<./Pangolin_CHOP.md> "Pangolin CHOP")• [Parameter ](<./Parameter_CHOP.md> "Parameter CHOP")• [Pattern ](<./Pattern_CHOP.md> "Pattern CHOP")• [Perform ](<./Perform_CHOP.md> "Perform CHOP")• [Phaser ](<./Phaser_CHOP.md> "Phaser CHOP")• [Pipe In ](<./Pipe_In_CHOP.md> "Pipe In CHOP")• [Pipe Out ](<./Pipe_Out_CHOP.md> "Pipe Out CHOP")• [POP to ](<./POP_to_CHOP.md> "POP to CHOP")• [PosiStageNet ](<./PosiStageNet_CHOP.md> "PosiStageNet CHOP")• [Pulse ](<./Pulse_CHOP.md> "Pulse CHOP")• [RealSense ](<./RealSense_CHOP.md> "RealSense CHOP")• [Record ](<./Record_CHOP.md> "Record CHOP")• [Rename ](<./Rename_CHOP.md> "Rename CHOP")• [Render Pick ](<./Render_Pick_CHOP.md> "Render Pick CHOP")• [RenderStream In ](<./RenderStream_In_CHOP.md> "RenderStream In CHOP")• [Reorder ](<./Reorder_CHOP.md> "Reorder CHOP")• [Replace ](<./Replace_CHOP.md> "Replace CHOP")• [Resample ](<./Resample_CHOP.md> "Resample CHOP")• [S Curve ](<./S_Curve_CHOP.md> "S Curve CHOP")• [Scan ](<./Scan_CHOP.md> "Scan CHOP")• [Script ](<./Script_CHOP.md> "Script CHOP")• [Select ](<./Select_CHOP.md> "Select CHOP")• [Sequencer ](<./Sequencer_CHOP.md> "Sequencer CHOP")• [Serial ](<./Serial_CHOP.md> "Serial CHOP")• [Shared Mem In ](<./Shared_Mem_In_CHOP.md> "Shared Mem In CHOP")• [Shared Mem Out ](<./Shared_Mem_Out_CHOP.md> "Shared Mem Out CHOP")• [Shift ](<./Shift_CHOP.md> "Shift CHOP")• [Shuffle ](<./Shuffle_CHOP.md> "Shuffle CHOP")• [Slope ](<./Slope_CHOP.md> "Slope CHOP")• [SOP to ](<./SOP_to_CHOP.md> "SOP to CHOP")• [Sort ](<./Sort_CHOP.md> "Sort CHOP")• [Speed ](<./Speed_CHOP.md> "Speed CHOP")• [Splice ](<./Splice_CHOP.md> "Splice CHOP")• [Spring ](<./Spring_CHOP.md> "Spring CHOP")• [ST2110 Device ](<./ST2110_Device_CHOP.md> "ST2110 Device CHOP")• [Stretch ](<./Stretch_CHOP.md> "Stretch CHOP")• [Stype In ](<./Stype_In_CHOP.md> "Stype In CHOP")• [Stype Out ](<./Stype_Out_CHOP.md> "Stype Out CHOP")• [Switch ](<./Switch_CHOP.md> "Switch CHOP")• [Sync In ](<./Sync_In_CHOP.md> "Sync In CHOP")• [Sync Out ](<./Sync_Out_CHOP.md> "Sync Out CHOP")• [Tablet ](<./Tablet_CHOP.md> "Tablet CHOP")• [Time Slice ](<./Time_Slice_CHOP.md> "Time Slice CHOP")• [Timecode ](<./Timecode_CHOP.md> "Timecode CHOP")• [Timeline ](<./Timeline_CHOP.md> "Timeline CHOP")• [Timer ](<./Timer_CHOP.md> "Timer CHOP")• [TOP to ](<./TOP_to_CHOP.md> "TOP to CHOP")• [Touch In ](<./Touch_In_CHOP.md> "Touch In CHOP")• [Touch Out ](<./Touch_Out_CHOP.md> "Touch Out CHOP")• [Trail ](<./Trail_CHOP.md> "Trail CHOP")• [Transform ](<./Transform_CHOP.md> "Transform CHOP")• [Transform XYZ ](<./Transform_XYZ_CHOP.md> "Transform XYZ CHOP")• [Trigger ](<./Trigger_CHOP.md> "Trigger CHOP")• [Trim ](<./Trim_CHOP.md> "Trim CHOP")• [Warp ](<./Warp_CHOP.md> "Warp CHOP")• [Wave ](<./Wave_CHOP.md> "Wave CHOP")• [WrnchAI ](<./WrnchAI_CHOP.md> "WrnchAI CHOP")• [ZED ](<./ZED_CHOP.md> "ZED CHOP")
