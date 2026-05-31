# Face Track CHOP

##   
  
Summary

**NOTE**

**OS:** This operator is only supported under the **Microsoft Windows** operating system.  
**Hardware:** This operator uses the Augmented Reality (AR) SDK of the Nvidia Maxine system and requires a 20, 30, 40 or 50 series Nvidia RTX card to operate. 

**The models for this node must be separately downloaded via the AR SDK for your GPU from <https://www.nvidia.com/en-us/geforce/broadcasting/broadcast-sdk/resources/>.  
  
**The Face Track CHOP can detect faces and facial landmark points in an image, as well as the direction the face is looking relative to the camera. Using a compatible 3D Morphable Face Model (3DMM) and the [Face Track SOP](<./Face_Track_SOP.md> "Face Track SOP"), it can also be used to fit and animate a 3D mesh to the detected face. 

The input image is taken from a provided TOP and can be of any resolution or format, and either a still image or video. If multiple faces are present in an image, the CHOP will attempt to track the largest one detected. 

The coordinates of the detected features are given in u, v positions relative to the bottom-left corner of the input image. By default, the values range from 0 to 1, but the 'Aspect Correct' parameter can be enabled to scale the values so that they can be used as 3D coordinates while maintaining the aspect ratio of the original image. 

**Tip** : Look at the several examples of the Face Track CHOP/SOP in [OP Snippets](<./OP_Snippets.md> "OP Snippets"). 

To align a 3D rendering of the points with the original input image, set the 'Projection' of your [Camera COMP](<./Camera_COMP.md> "Camera COMP") to 'Orthographic', the 'Ortho Origin' parameter to 'Bottom-Left', and the 'Ortho Width' to 1, while also enabling 'Aspect Correct' on the Face Track CHOP. 

To use the mesh fitting features you will need a compatible face mesh file in the Nvidia '`nvf`' format. We recommend using the`face_model2.nvf`file that is now included in the`Config/Models`folder inside your TouchDesigner installation. **Note:** Mesh files generated for previous versions of TouchDesigner will no longer work. 

See also: [Face Track SOP](<./Face_Track_SOP.md> "Face Track SOP")

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[facetrackCHOP_Class](<./FacetrackCHOP_Class.md> "FacetrackCHOP Class")

## 

Parameters - FaceTrack Page

Active`active`\- Enables the face tracking features. 

Model Folder`modelfolder`\- The location of the AI model files used for face detection. By default these files are located in the Config/Models folder. 

Mesh File`meshfile`\- The 3D morphable mesh file in Nvidia 'nvf' format to use in mesh fitting. When available, the fitted mesh can be accessed with a [Face Track SOP](<./Face_Track_SOP.md> "Face Track SOP"). 

TOP`top`\- A path to the TOP operator that will provides the image to perform face tracking on. 

Bounding Boxes`bbox`\- Output channels that describe a bounding box around the detected face. The channels give the u and v positions of the center of the face as well as the width and height of the box. The positions are relative to the bottom-left corner of the input image. 

Bounding Box Confidence`bboxconfidence`\- Outputs a channel that describes the level of certainty that the AI model has detected a face in the input image. Higher numbers indicate greater confidence. 

Rotations`rotations`\- Output rx, ry, and rz values that indicate how the face is oriented in the image. (0,0,0) indicates that the face is oriented directly towards the camera. Values can range from +/- 180 degrees as the subject turns away from the camera. 

Number of Landmarks`landmarks`\- ⊞ \- 
* None`none`\- The number of facial landmark points to output. Points are numbered beginning from 1 and always represent a fixed feature on the face such as the chin, eyebrow, nose, etc. Positions are given as u and v coordinates relative to the bottom-left corner of the input image.
* 68 (Multi-PIE Mark-ups)`num68`\- A standard set of facial landmark features used in AI research. [See Reference Diagram.](<https://www.researchgate.net/figure/The-68-Multi-PIE-landmarks-scheme-and-the-landmarks-selected-for-our-method-marked-by-the_fig1_311741971>)
* 126`num126`\- An extended set of landmark features.


Landmark Confidence`landmarkconfidence`\- Adds a confidence value for each landmark feature. Higher values indicate the feature is more likely to be accurate. 

Mesh Transform`meshtransform`\- Enable to output translate, rotate and scale channels for the fitted face mesh. This feature requires a valid 3D morphable face mesh file (see notes above). The values from these channels can be used to transform the mesh produced by an attached [Face Track SOP](<./Face_Track_SOP.md> "Face Track SOP") so that it aligns with the input image. By default the fitted mesh is pre-transformed to align with the image, but if 'Pre-Transform' is disabled in the SOP, these values can be used instead for more control and speed. 

Aspect Correct UVs`aspectcorrectuv`\- Rescales the the u and v positions so that they have the correct aspect ratio of the input image. This is useful when using the u, v positions as 3D coordinates rather than as image positions. 

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

Extra Information for the Face Track CHOP can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). __

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


  
TouchDesigner Build: Latest\nwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditor2025.300002022.24140before 2022.24140

CHOPs   
---  
[Ableton Link ](<./Ableton_Link_CHOP.md> "Ableton Link CHOP")• [Analyze ](<./Analyze_CHOP.md> "Analyze CHOP")• [Angle ](<./Angle_CHOP.md> "Angle CHOP")• [Attribute ](<./Attribute_CHOP.md> "Attribute CHOP")• [Audio Band EQ ](<./Audio_Band_EQ_CHOP.md> "Audio Band EQ CHOP")• [Audio Binaural ](<./Audio_Binaural_CHOP.md> "Audio Binaural CHOP")• [Audio Device In ](<./Audio_Device_In_CHOP.md> "Audio Device In CHOP")• [Audio Device Out ](<./Audio_Device_Out_CHOP.md> "Audio Device Out CHOP")• [Audio Dynamics ](<./Audio_Dynamics_CHOP.md> "Audio Dynamics CHOP")• [Audio File In ](<./Audio_File_In_CHOP.md> "Audio File In CHOP")• [Audio File Out ](<./Audio_File_Out_CHOP.md> "Audio File Out CHOP")• [Experimental:Audio File Out ](</index.php?title=Experimental:Audio_File_Out_CHOP&action=edit&redlink=1> "Experimental:Audio File Out CHOP \(page does not exist\)")• [Audio Filter ](<./Audio_Filter_CHOP.md> "Audio Filter CHOP")• [Audio Movie ](<./Audio_Movie_CHOP.md> "Audio Movie CHOP")• [Experimental:Audio Movie ](</index.php?title=Experimental:Audio_Movie_CHOP&action=edit&redlink=1> "Experimental:Audio Movie CHOP \(page does not exist\)")• [Audio NDI ](<./Audio_NDI_CHOP.md> "Audio NDI CHOP")• [Audio Oscillator ](<./Audio_Oscillator_CHOP.md> "Audio Oscillator CHOP")• [Audio Para EQ ](<./Audio_Para_EQ_CHOP.md> "Audio Para EQ CHOP")• [Audio Play ](<./Audio_Play_CHOP.md> "Audio Play CHOP")• [Audio Render ](<./Audio_Render_CHOP.md> "Audio Render CHOP")• [Experimental:Audio Render ](</index.php?title=Experimental:Audio_Render_CHOP&action=edit&redlink=1> "Experimental:Audio Render CHOP \(page does not exist\)")• [Audio Spectrum ](<./Audio_Spectrum_CHOP.md> "Audio Spectrum CHOP")• [Audio Stream In ](<./Audio_Stream_In_CHOP.md> "Audio Stream In CHOP")• [Audio Stream Out ](<./Audio_Stream_Out_CHOP.md> "Audio Stream Out CHOP")• [Audio VST ](<./Audio_VST_CHOP.md> "Audio VST CHOP")• [Audio Web Render ](<./Audio_Web_Render_CHOP.md> "Audio Web Render CHOP")• [Beat ](<./Beat_CHOP.md> "Beat CHOP")• [Bind ](<./Bind_CHOP.md> "Bind CHOP")• [BlackTrax ](<./BlackTrax_CHOP.md> "BlackTrax CHOP")• [Blend ](<./Blend_CHOP.md> "Blend CHOP")• [Blob Track ](<./Blob_Track_CHOP.md> "Blob Track CHOP")• [Body Track ](<./Body_Track_CHOP.md> "Body Track CHOP")• [Experimental:Body Track ](</index.php?title=Experimental:Body_Track_CHOP&action=edit&redlink=1> "Experimental:Body Track CHOP \(page does not exist\)")• [Bullet Solver ](<./Bullet_Solver_CHOP.md> "Bullet Solver CHOP")• [Experimental:CHOP ](</index.php?title=Experimental:CHOP&action=edit&redlink=1> "Experimental:CHOP \(page does not exist\)")• [Clip Blender ](<./Clip_Blender_CHOP.md> "Clip Blender CHOP")• [Clip ](<./Clip_CHOP.md> "Clip CHOP")• [Clock ](<./Clock_CHOP.md> "Clock CHOP")• [Experimental:Clock ](</index.php?title=Experimental:Clock_CHOP&action=edit&redlink=1> "Experimental:Clock CHOP \(page does not exist\)")• [Composite ](<./Composite_CHOP.md> "Composite CHOP")• [Constant ](<./Constant_CHOP.md> "Constant CHOP")• [Copy ](<./Copy_CHOP.md> "Copy CHOP")• [Count ](<./Count_CHOP.md> "Count CHOP")• [CPlusPlus ](<./CPlusPlus_CHOP.md> "CPlusPlus CHOP")• [Cross ](<./Cross_CHOP.md> "Cross CHOP")• [Cycle ](<./Cycle_CHOP.md> "Cycle CHOP")• [DAT to ](<./DAT_to_CHOP.md> "DAT to CHOP")• [Delay ](<./Delay_CHOP.md> "Delay CHOP")• [Delete ](<./Delete_CHOP.md> "Delete CHOP")• [DMX In ](<./DMX_In_CHOP.md> "DMX In CHOP")• [DMX Out ](<./DMX_Out_CHOP.md> "DMX Out CHOP")• [Experimental:DMX Out ](</index.php?title=Experimental:DMX_Out_CHOP&action=edit&redlink=1> "Experimental:DMX Out CHOP \(page does not exist\)")• [Envelope ](<./Envelope_CHOP.md> "Envelope CHOP")• [EtherDream ](<./EtherDream_CHOP.md> "EtherDream CHOP")• [Event ](<./Event_CHOP.md> "Event CHOP")• [Expression ](<./Expression_CHOP.md> "Expression CHOP")• [Extend ](<./Extend_CHOP.md> "Extend CHOP")• Face Track • [Experimental:Face Track ](</index.php?title=Experimental:Face_Track_CHOP&action=edit&redlink=1> "Experimental:Face Track CHOP \(page does not exist\)")• [Fan ](<./Fan_CHOP.md> "Fan CHOP")• [Feedback ](<./Feedback_CHOP.md> "Feedback CHOP")• [File In ](<./File_In_CHOP.md> "File In CHOP")• [File Out ](<./File_Out_CHOP.md> "File Out CHOP")• [Filter ](<./Filter_CHOP.md> "Filter CHOP")• [Experimental:Filter ](</index.php?title=Experimental:Filter_CHOP&action=edit&redlink=1> "Experimental:Filter CHOP \(page does not exist\)")• [FreeD In ](<./FreeD_In_CHOP.md> "FreeD In CHOP")• [FreeD Out ](<./FreeD_Out_CHOP.md> "FreeD Out CHOP")• [Function ](<./Function_CHOP.md> "Function CHOP")• [Gesture ](<./Gesture_CHOP.md> "Gesture CHOP")• [Handle ](<./Handle_CHOP.md> "Handle CHOP")• [Helios DAC ](<./Helios_DAC_CHOP.md> "Helios DAC CHOP")• [Hog ](<./Hog_CHOP.md> "Hog CHOP")• [Hokuyo ](<./Hokuyo_CHOP.md> "Hokuyo CHOP")• [Hold ](<./Hold_CHOP.md> "Hold CHOP")• [Import Select ](<./Import_Select_CHOP.md> "Import Select CHOP")• [In ](<./In_CHOP.md> "In CHOP")• [Info ](<./Info_CHOP.md> "Info CHOP")• [Interpolate ](<./Interpolate_CHOP.md> "Interpolate CHOP")• [Introduction To s Vid ](<./Introduction_To_CHOPs_Vid.md> "Introduction To CHOPs Vid")• [Inverse Curve ](<./Inverse_Curve_CHOP.md> "Inverse Curve CHOP")• [Inverse Kin ](<./Inverse_Kin_CHOP.md> "Inverse Kin CHOP")• [Join ](<./Join_CHOP.md> "Join CHOP")• [Joystick ](<./Joystick_CHOP.md> "Joystick CHOP")• [Keyboard In ](<./Keyboard_In_CHOP.md> "Keyboard In CHOP")• [Keyframe ](<./Keyframe_CHOP.md> "Keyframe CHOP")• [Kinect Azure ](<./Kinect_Azure_CHOP.md> "Kinect Azure CHOP")• [Kinect ](<./Kinect_CHOP.md> "Kinect CHOP")• [Lag ](<./Lag_CHOP.md> "Lag CHOP")• [Laser ](<./Laser_CHOP.md> "Laser CHOP")• [Experimental:Laser ](</index.php?title=Experimental:Laser_CHOP&action=edit&redlink=1> "Experimental:Laser CHOP \(page does not exist\)")• [Laser Device ](<./Laser_Device_CHOP.md> "Laser Device CHOP")• [Experimental:Laser Device ](</index.php?title=Experimental:Laser_Device_CHOP&action=edit&redlink=1> "Experimental:Laser Device CHOP \(page does not exist\)")• [Leap Motion ](<./Leap_Motion_CHOP.md> "Leap Motion CHOP")• [Leuze ROD4 ](<./Leuze_ROD4_CHOP.md> "Leuze ROD4 CHOP")• [LFO ](<./LFO_CHOP.md> "LFO CHOP")• [Limit ](<./Limit_CHOP.md> "Limit CHOP")• [Logic ](<./Logic_CHOP.md> "Logic CHOP")• [Lookup ](<./Lookup_CHOP.md> "Lookup CHOP")• [LTC In ](<./LTC_In_CHOP.md> "LTC In CHOP")• [LTC Out ](<./LTC_Out_CHOP.md> "LTC Out CHOP")• [Math ](<./Math_CHOP.md> "Math CHOP")• [Merge ](<./Merge_CHOP.md> "Merge CHOP")• [MIDI In ](<./MIDI_In_CHOP.md> "MIDI In CHOP")• [MIDI In Map ](<./MIDI_In_Map_CHOP.md> "MIDI In Map CHOP")• [MIDI Out ](<./MIDI_Out_CHOP.md> "MIDI Out CHOP")• [MoSys ](<./MoSys_CHOP.md> "MoSys CHOP")• [Mouse In ](<./Mouse_In_CHOP.md> "Mouse In CHOP")• [Mouse Out ](<./Mouse_Out_CHOP.md> "Mouse Out CHOP")• [Ncam ](<./Ncam_CHOP.md> "Ncam CHOP")• [Noise ](<./Noise_CHOP.md> "Noise CHOP")• [Null ](<./Null_CHOP.md> "Null CHOP")• [OAK Device ](<./OAK_Device_CHOP.md> "OAK Device CHOP")• [OAK Select ](<./OAK_Select_CHOP.md> "OAK Select CHOP")• [Object ](<./Object_CHOP.md> "Object CHOP")• [Oculus Audio ](<./Oculus_Audio_CHOP.md> "Oculus Audio CHOP")• [Oculus Rift ](<./Oculus_Rift_CHOP.md> "Oculus Rift CHOP")• [OpenVR ](<./OpenVR_CHOP.md> "OpenVR CHOP")• [OptiTrack In ](<./OptiTrack_In_CHOP.md> "OptiTrack In CHOP")• [OSC In ](<./OSC_In_CHOP.md> "OSC In CHOP")• [OSC Out ](<./OSC_Out_CHOP.md> "OSC Out CHOP")• [Out ](<./Out_CHOP.md> "Out CHOP")• [Override ](<./Override_CHOP.md> "Override CHOP")• [Experimental:Pan Tilt ](</Experimental:Pan_Tilt_CHOP> "Experimental:Pan Tilt CHOP")• [Panel ](<./Panel_CHOP.md> "Panel CHOP")• [Pangolin ](<./Pangolin_CHOP.md> "Pangolin CHOP")• [Experimental:Pangolin ](</Experimental:Pangolin_CHOP> "Experimental:Pangolin CHOP")• [Parameter ](<./Parameter_CHOP.md> "Parameter CHOP")• [Experimental:Parameter ](</Experimental:Parameter_CHOP> "Experimental:Parameter CHOP")• [Pattern ](<./Pattern_CHOP.md> "Pattern CHOP")• [Perform ](<./Perform_CHOP.md> "Perform CHOP")• [Phaser ](<./Phaser_CHOP.md> "Phaser CHOP")• [Pipe In ](<./Pipe_In_CHOP.md> "Pipe In CHOP")• [Pipe Out ](<./Pipe_Out_CHOP.md> "Pipe Out CHOP")• [Experimental:POP to ](</Experimental:POP_to_CHOP> "Experimental:POP to CHOP")• [PosiStageNet ](<./PosiStageNet_CHOP.md> "PosiStageNet CHOP")• [Pulse ](<./Pulse_CHOP.md> "Pulse CHOP")• [RealSense ](<./RealSense_CHOP.md> "RealSense CHOP")• [Record ](<./Record_CHOP.md> "Record CHOP")• [Rename ](<./Rename_CHOP.md> "Rename CHOP")• [Render Pick ](<./Render_Pick_CHOP.md> "Render Pick CHOP")• [RenderStream In ](<./RenderStream_In_CHOP.md> "RenderStream In CHOP")• [Reorder ](<./Reorder_CHOP.md> "Reorder CHOP")• [Replace ](<./Replace_CHOP.md> "Replace CHOP")• [Resample ](<./Resample_CHOP.md> "Resample CHOP")• [Experimental:Resample ](</Experimental:Resample_CHOP> "Experimental:Resample CHOP")• [S Curve ](<./S_Curve_CHOP.md> "S Curve CHOP")• [Scan ](<./Scan_CHOP.md> "Scan CHOP")• [Script ](<./Script_CHOP.md> "Script CHOP")• [Experimental:Script ](</Experimental:Script_CHOP> "Experimental:Script CHOP")• [Select ](<./Select_CHOP.md> "Select CHOP")• [Sequencer ](<./Sequencer_CHOP.md> "Sequencer CHOP")• [Serial ](<./Serial_CHOP.md> "Serial CHOP")• [Shared Mem In ](<./Shared_Mem_In_CHOP.md> "Shared Mem In CHOP")• [Shared Mem Out ](<./Shared_Mem_Out_CHOP.md> "Shared Mem Out CHOP")• [Shift ](<./Shift_CHOP.md> "Shift CHOP")• [Shuffle ](<./Shuffle_CHOP.md> "Shuffle CHOP")• [Slope ](<./Slope_CHOP.md> "Slope CHOP")• [SOP to ](<./SOP_to_CHOP.md> "SOP to CHOP")• [Sort ](<./Sort_CHOP.md> "Sort CHOP")• [Speed ](<./Speed_CHOP.md> "Speed CHOP")• [Experimental:Speed ](</Experimental:Speed_CHOP> "Experimental:Speed CHOP")• [Splice ](<./Splice_CHOP.md> "Splice CHOP")• [Spring ](<./Spring_CHOP.md> "Spring CHOP")• [Experimental:ST2110 Device ](</Experimental:ST2110_Device_CHOP> "Experimental:ST2110 Device CHOP")• [Stretch ](<./Stretch_CHOP.md> "Stretch CHOP")• [Experimental:Stretch ](</Experimental:Stretch_CHOP> "Experimental:Stretch CHOP")• [Stype In ](<./Stype_In_CHOP.md> "Stype In CHOP")• [Stype Out ](<./Stype_Out_CHOP.md> "Stype Out CHOP")• [Switch ](<./Switch_CHOP.md> "Switch CHOP")• [Sync In ](<./Sync_In_CHOP.md> "Sync In CHOP")• [Sync Out ](<./Sync_Out_CHOP.md> "Sync Out CHOP")• [Tablet ](<./Tablet_CHOP.md> "Tablet CHOP")• [Time Slice ](<./Time_Slice_CHOP.md> "Time Slice CHOP")• [Timecode ](<./Timecode_CHOP.md> "Timecode CHOP")• [Experimental:Timecode ](</Experimental:Timecode_CHOP> "Experimental:Timecode CHOP")• [Timeline ](<./Timeline_CHOP.md> "Timeline CHOP")• [Timer ](<./Timer_CHOP.md> "Timer CHOP")• [Experimental:Timer ](</Experimental:Timer_CHOP> "Experimental:Timer CHOP")• [TOP to ](<./TOP_to_CHOP.md> "TOP to CHOP")• [Experimental:TOP to ](</Experimental:TOP_to_CHOP> "Experimental:TOP to CHOP")• [Touch In ](<./Touch_In_CHOP.md> "Touch In CHOP")• [Experimental:Touch In ](</Experimental:Touch_In_CHOP> "Experimental:Touch In CHOP")• [Touch Out ](<./Touch_Out_CHOP.md> "Touch Out CHOP")• [Trail ](<./Trail_CHOP.md> "Trail CHOP")• [Transform ](<./Transform_CHOP.md> "Transform CHOP")• [Transform XYZ ](<./Transform_XYZ_CHOP.md> "Transform XYZ CHOP")• [Trigger ](<./Trigger_CHOP.md> "Trigger CHOP")• [Experimental:Trigger ](</Experimental:Trigger_CHOP> "Experimental:Trigger CHOP")• [Trim ](<./Trim_CHOP.md> "Trim CHOP")• [Warp ](<./Warp_CHOP.md> "Warp CHOP")• [Wave ](<./Wave_CHOP.md> "Wave CHOP")• [WrnchAI ](<./WrnchAI_CHOP.md> "WrnchAI CHOP")• [ZED ](<./ZED_CHOP.md> "ZED CHOP")• [Experimental:ZED ](</Experimental:ZED_CHOP> "Experimental:ZED CHOP")
