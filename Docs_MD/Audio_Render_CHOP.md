# Audio Render CHOP

##   
  
Summary

**Note:** For Apple Silicon Macs, this operator only works starting with build 2022.33910. 

The Audio Render CHOP uses the [Steam Audio SDK](<https://steamcommunity.com/games/596420/announcements/detail/521693426582988261>) to spatially render audio based on the full transforms (translation, rotation, scale) of a listener and an audio source. The Audio Render CHOP takes sound audio sources as input, and spatially outputs the sound in the format specified from the Output Format parameter. The number of channels outputted by the Audio Render CHOP depends on the Output Format. 

You specify a 3D component for the transform of the listener, plus a 3D component for the transform of a source. 

The sample rate of the output is determined by the audio source, which must be either 44100 or 48000. 

An [Info DAT](<./Info_DAT.md> "Info DAT") can be used to populate the position and radius of baked probes in Simulation mode. 

Look at the Audio Render CHOP example in Help -> Operator Snippets. 

See also [Oculus Audio CHOP](<./Oculus_Audio_CHOP.md> "Oculus Audio CHOP"). 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[audiorenderCHOP_Class](<./AudiorenderCHOP_Class.md> "AudiorenderCHOP Class")

## 

Parameters - Audio Render Page

Active`active`\- Turns the Audio Render on or off. 

Mode`mode`\- ⊞ \- This menu determines which Steam Audio mode to use. 
* Simple Positional`simple`\- Sound simulation for only a mono source.
* Simulation`simulation`\- Sound simulation for multiple sources.


Output Format`outputformat`\- ⊞ \- The output format of the audio. 
* Binaural`Binaural`\- Spatialize sound based on 3D position of source relative to listener.
* Stereo`stereo`\- Spatialize sound based on left and right channels.
* Quadraphonic Surround`quadraphonic`\- Spatialize sound based on front left, front right, rear left, and rear right channels.
* 5.1 Surround`fiveone`\- Spatialize sound based on front left, front right, front center, LFE, rear left, and rear right channels.
* 7.1 Surround`sevenone`\- Spatialize sound based on Ffont left, front right, front center, LFE, rear left, rear right, side left, and side right channels.
* Custom Setup`custom`\- Custom Setup requires use of the Mapping Table.
* Ambisonics`ambisonics`\- Ambisonics is a format for encoding three-dimensional 360 degree audio. The Ambisonics format used in the Audio Render CHOP is the 3rd order SN3D format consisting of 16 encoded channels (WXYZ, RSTUV, KLMNOPQ) that define the sphere of sound. Ambisonics is disabled in Simulation mode when reflections are enabled.
* Direct Effect`direct`\- Used in Simulation mode only to simulate sound based on the direct path between a point source and listener. Direct Effect is disabled when reflections are enabled.


Enable Attenuation`attenuation`\- Attenuate the sound based on the distance between the center position of the listener and a source. The attenuation level is determined by the selected attenuation mode for each source. 

Ambisonics Order`ambisonicsorder`\- Ambisonics order of the output buffer. 

Mapping Table`mappingtable`\- A DAT Table that specifies the various speakers in the setup and their position. The Table must have 3 columns named x, y, z. Each row specifies an individual speaker, and the 3 columns specify its position. Used with the Custom Setup Output Format. The mapping table will create one channel per row. 

Listener Object COMP`listenerobject`\- A COMP that represents the listening head. Must be a COMP that contains transform data, such as a Geometry or Camera COMP. 

Source`source`\- Sequence of the audio sources. 

Object COMP`source0object`\- A COMP that represents the source of the sound. Must be a 3D Object COMP that contains transform data, such as a [Geometry COMP](<./Geometry_COMP.md> "Geometry COMP") or [Camera COMP](<./Camera_COMP.md> "Camera COMP"). 

Enable Directivity`source0directivity`\- Turns directivity on or off. When disabled, sound will emit from the source from all directions (i.e. omnidirectional) 

Dipole Weight`source0dipoleweight`\- The weight of the dipole to blend in the directivity pattern. 0 = pure omnidirectional, 1 = pure dipole, 0.5 = cardioid directivity pattern. 

Dipole Power`source0dipolepower`\- The sharpness of the dipole. Higher values make the sound direction narrower. 

Attenuation Mode`source0attnmode`\- ⊞ \- This menu determines which attenuation mode to use for the source. **Note:** Attenuation modes are disabled when reflections are enabled due to a known issue. If attenuation is enabled while reflections are on, it will revert to Steam Audio's default attenuation model of inverse distance with power of 1. 
* Inverse Distance`inverse`\- Attenuation level is calculated by an inverse distance falloff function.
* Custom Curve`custom`\- Attenuation level is calculated by a custom curve.


Attenuation Inverse Power`source0invpower`\- The power of the inverse falloff function. For example, a power of 2 causes an attenuation level of (1/distance)^2. 

Attenuation Curve CHOP`source0chop`\- The path of the custom attenuation curve CHOP being referenced. The CHOP must have exactly one channel to represent the curve. The vertical axis represents the attenuation level, and the horizontal axis represents the distance. Attenuation levels are clamped between [0, 1]. The distance should always be non-negative and assumes the CHOP is using samples as the unit. 

## 

Parameters - Meshes Page

Update Meshes`update`\- When enabled, any static mesh changes will automatically be updated in the simulation 

Update Meshes Pulse`updatepulse`\- When pulsed, will update the static meshes in the simulation if they changed. 

Mesh`mesh`\- Sequence of static meshes. 

Mesh Objects/POPs/SOPs`mesh0object`\- The object for the mesh which can be geometry COMP, POP, or SOP. COMPs must contain SOP or POP geometries in triangle polygon form. The root COMP's display flag can be off and still be collected. However, child COMPs will only be added to the scene if their display flag is on. 

Absorption`mesh0absorb`\- ⊞ \- The fraction of sound absorbed at low, medium, and high frequencies. 0 = no sound is absorbed, 1 = sound is fully absorbed by the mesh surface. 
* Absorption`mesh0absorb1`\- Absorption at low frequencies (0 - 800 Hz).
* Absorption`mesh0absorb2`\- Absorption at medium frequencies (800 Hz - 8 kHz).
* Absorption`mesh0absorb3`\- Absorption at high frequencies (8 kHz and above).


Scattering`mesh0scatter`\- Scatters sound for reflections. 0 = reflect at the same angle as it hit the surface (i.e. pure specular), 1 = reflect uniformly randomly (i.e. pure diffuse). 

Transmission`mesh0trans`\- ⊞ \- The fraction of sound transmitted through at low, medium, and high frequencies. 0 = no sound transmits through, 1 = sound fully transmits through the mesh surface. 
* Transmission`mesh0trans1`\- Transmission at low frequencies (0 - 800 Hz).
* Transmission`mesh0trans2`\- Transmission at medium frequencies (800 Hz - 8 kHz).
* Transmission`mesh0trans3`\- Transmission at high frequencies (8 kHz and above).

## 

Parameters - Simulation Page

Enable Air Absorption`airabsorb`\- Turns air absorption on or off for all sources. Air absorption is how much sound is lost over the distance travelling from source to listener. 

Enable Occlusion`occlusion`\- Turns raycast occlusion on or off for all meshes. If a single ray from listener to source is occluded, then the source is considered occluded. 

Number of Surfaces`numsurfaces`\- Maximum number of surfaces, starting from closest surface to the listener, whose transmission coefficients will be considered when calculating the total sound transmission. 

Enable Reflection`reflection`\- Turns reflection on or off for all meshes. 

Diffuse Samples`diffsamp`\- Number of directions to generate for reflecting rays. 

Duration`duration`\- Duration in seconds of the impulse responses generated. 

Ambisonics Order`refambixord`\- Ambisonics order of the impulse responses generated. 

Number of Rays`numrays`\- Number of rays to trace from the listener. 

Number of Threads`numthreads`\- Number of threads used for real-time reflection simulations. 

Number of Bounces`numbounces`\- Number of times each ray is reflected off a surface. 

Irradiance Min Distance`irmindist`\- The minimum distance used to calculate how much sound energy reaches a surface from a source. 

Reflection Bake Mode`bakemode`\- ⊞ \- This menu determines which bake mode to use. Baking is useful as an optimization tool when calculating reflections. Baking will generate probes that are uniformly spaced and placed above any mesh "floor" at a fixed height. The mesh "floor" is meant to resemble a floor or terrain, meaning meshes should be horizontal or lie along the XZ plane for any probes to be generated on top of it. The probes' region of influence is defined by a 3D position and a radius. Baking has two variations: static listener and static source. For example, if static listener is selected, baking assumes the position of the listener remains fixed. Each probe is then baked reflection data that simulates the sound between its position and the listener. Once baking is done, sources can move around dynamically, and as long as they are within the range of any baked probe, they will use the probe's baked reflection data to calculate its reflected sound, allowing for a reduction in computation and simulation time. If a source is not within the range of any baked probe, the source will not be influenced by any baked data and can lead to incorrect sound calculations. All parameters used for reflections will also be used for baking. Baking will not generate probes for any of the following reasons: Scene has no geometry, spawn box does not contain any of the geometries in the scene, all probes generated lie outside of the spawn box, or all geometries are X-Y or Y-Z planar. 
* Off`off`\- Baking is turned off. Turning baking off will disable any bakes that are currently active.
* Manual`manual`\- Baking is turned on, but Baked Reflections must be pulsed to start baking.
* Automatic`auto`\- Baking is turned on and will automatically start baking when changes to baking parameters have been made.


Bake Reflections`bake`\- Immediately start baking. Once complete, reflections will automatically used the baked data. Baking status can be monitored using the bake_complete channel in the Info CHOP. 

Baked Data Variation`variation`\- ⊞ \- This menu determines which objects will have a fixed position for baking. If the selected static object's position changes, you must re-bake or else the calculated reflections will be incorrect. 
* Static Listener`listener`\- Each baking probe calculates reflections with the source at the probe position and the listener at some fixed position. The listener's position must stay static. This mode is useful for modeling reflections from a moving source to a static listener.
* Static Source`source`\- Each baking probe calculates reflections with the listener at the probe position and the source at some fixed position. The source's position must stay static. This mode is useful for modeling reflections from a moving listener to a static source.


Probes Distance`probedist`\- The spacing between two neighboring probes. 

Y-Offset from Surface`yoffset`\- The height above the surface of a geometry all probes will be generated at. 

Size of Spawn Box`size`\- ⊞ \- Size of the spawn box along the X, Y, and Z axes where probes will be generated. 
* Size of Spawn Box`sizex`-
* Size of Spawn Box`sizey`-
* Size of Spawn Box`sizez`-


Origin of Spawn Box`origin`\- ⊞ \- These X,Y, and Z Values determine where the center of the spawn box is located. 
* Origin of Spawn Box`originx`-
* Origin of Spawn Box`originy`-
* Origin of Spawn Box`originz`-


Distance from Listener`lstnrdist`\- The maximum distance from the listener where baked data will be stored for probes. 

Save Duration`savedur`\- Duration in seconds of the impulse responses saved at each probe. 

Batch Size`batchsize`\- Number of probes to bake simultaneously. 

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

Extra Information for the Audio Render CHOP can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). 

### 

Specific Audio Render CHOP Info Channels
* audioposition_full_time -
* audioposition_panbin_time -
* distance_attenuation -

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


  
TouchDesigner Build: Latest\nwikieditorwikieditor2025.300002022.241402021.100002018.28070before 2018.28070

CHOPs   
---  
[Ableton Link ](<./Ableton_Link_CHOP.md> "Ableton Link CHOP")• [Analyze ](<./Analyze_CHOP.md> "Analyze CHOP")• [Angle ](<./Angle_CHOP.md> "Angle CHOP")• [Attribute ](<./Attribute_CHOP.md> "Attribute CHOP")• [Audio Band EQ ](<./Audio_Band_EQ_CHOP.md> "Audio Band EQ CHOP")• [Audio Binaural ](<./Audio_Binaural_CHOP.md> "Audio Binaural CHOP")• [Audio Device In ](<./Audio_Device_In_CHOP.md> "Audio Device In CHOP")• [Audio Device Out ](<./Audio_Device_Out_CHOP.md> "Audio Device Out CHOP")• [Audio Dynamics ](<./Audio_Dynamics_CHOP.md> "Audio Dynamics CHOP")• [Audio File In ](<./Audio_File_In_CHOP.md> "Audio File In CHOP")• [Audio File Out ](<./Audio_File_Out_CHOP.md> "Audio File Out CHOP")• [Audio Filter ](<./Audio_Filter_CHOP.md> "Audio Filter CHOP")• [Audio Movie ](<./Audio_Movie_CHOP.md> "Audio Movie CHOP")• [Audio NDI ](<./Audio_NDI_CHOP.md> "Audio NDI CHOP")• [Audio Oscillator ](<./Audio_Oscillator_CHOP.md> "Audio Oscillator CHOP")• [Audio Para EQ ](<./Audio_Para_EQ_CHOP.md> "Audio Para EQ CHOP")• [Audio Play ](<./Audio_Play_CHOP.md> "Audio Play CHOP")• Audio Render • [Audio Spectrum ](<./Audio_Spectrum_CHOP.md> "Audio Spectrum CHOP")• [Audio Stream In ](<./Audio_Stream_In_CHOP.md> "Audio Stream In CHOP")• [Audio Stream Out ](<./Audio_Stream_Out_CHOP.md> "Audio Stream Out CHOP")• [Audio VST ](<./Audio_VST_CHOP.md> "Audio VST CHOP")• [Audio Web Render ](<./Audio_Web_Render_CHOP.md> "Audio Web Render CHOP")• [Beat ](<./Beat_CHOP.md> "Beat CHOP")• [Bind ](<./Bind_CHOP.md> "Bind CHOP")• [BlackTrax ](<./BlackTrax_CHOP.md> "BlackTrax CHOP")• [Blend ](<./Blend_CHOP.md> "Blend CHOP")• [Blob Track ](<./Blob_Track_CHOP.md> "Blob Track CHOP")• [Body Track ](<./Body_Track_CHOP.md> "Body Track CHOP")• [Bullet Solver ](<./Bullet_Solver_CHOP.md> "Bullet Solver CHOP")• [CHOP ](<./CHOP.md> "CHOP")• [Clip Blender ](<./Clip_Blender_CHOP.md> "Clip Blender CHOP")• [Clip ](<./Clip_CHOP.md> "Clip CHOP")• [Clock ](<./Clock_CHOP.md> "Clock CHOP")• [Composite ](<./Composite_CHOP.md> "Composite CHOP")• [Constant ](<./Constant_CHOP.md> "Constant CHOP")• [Copy ](<./Copy_CHOP.md> "Copy CHOP")• [Count ](<./Count_CHOP.md> "Count CHOP")• [CPlusPlus ](<./CPlusPlus_CHOP.md> "CPlusPlus CHOP")• [Cross ](<./Cross_CHOP.md> "Cross CHOP")• [Cycle ](<./Cycle_CHOP.md> "Cycle CHOP")• [DAT to ](<./DAT_to_CHOP.md> "DAT to CHOP")• [Delay ](<./Delay_CHOP.md> "Delay CHOP")• [Delete ](<./Delete_CHOP.md> "Delete CHOP")• [DMX In ](<./DMX_In_CHOP.md> "DMX In CHOP")• [DMX Out ](<./DMX_Out_CHOP.md> "DMX Out CHOP")• [Envelope ](<./Envelope_CHOP.md> "Envelope CHOP")• [EtherDream ](<./EtherDream_CHOP.md> "EtherDream CHOP")• [Event ](<./Event_CHOP.md> "Event CHOP")• [Expression ](<./Expression_CHOP.md> "Expression CHOP")• [Extend ](<./Extend_CHOP.md> "Extend CHOP")• [Face Track ](<./Face_Track_CHOP.md> "Face Track CHOP")• [Fan ](<./Fan_CHOP.md> "Fan CHOP")• [Feedback ](<./Feedback_CHOP.md> "Feedback CHOP")• [File In ](<./File_In_CHOP.md> "File In CHOP")• [File Out ](<./File_Out_CHOP.md> "File Out CHOP")• [Filter ](<./Filter_CHOP.md> "Filter CHOP")• [FreeD In ](<./FreeD_In_CHOP.md> "FreeD In CHOP")• [FreeD Out ](<./FreeD_Out_CHOP.md> "FreeD Out CHOP")• [Function ](<./Function_CHOP.md> "Function CHOP")• [Gesture ](<./Gesture_CHOP.md> "Gesture CHOP")• [Handle ](<./Handle_CHOP.md> "Handle CHOP")• [Helios DAC ](<./Helios_DAC_CHOP.md> "Helios DAC CHOP")• [Hog ](<./Hog_CHOP.md> "Hog CHOP")• [Hokuyo ](<./Hokuyo_CHOP.md> "Hokuyo CHOP")• [Hold ](<./Hold_CHOP.md> "Hold CHOP")• [Import Select ](<./Import_Select_CHOP.md> "Import Select CHOP")• [In ](<./In_CHOP.md> "In CHOP")• [Info ](<./Info_CHOP.md> "Info CHOP")• [Interpolate ](<./Interpolate_CHOP.md> "Interpolate CHOP")• [Introduction To s Vid ](<./Introduction_To_CHOPs_Vid.md> "Introduction To CHOPs Vid")• [Inverse Curve ](<./Inverse_Curve_CHOP.md> "Inverse Curve CHOP")• [Inverse Kin ](<./Inverse_Kin_CHOP.md> "Inverse Kin CHOP")• [Join ](<./Join_CHOP.md> "Join CHOP")• [Joystick ](<./Joystick_CHOP.md> "Joystick CHOP")• [Keyboard In ](<./Keyboard_In_CHOP.md> "Keyboard In CHOP")• [Keyframe ](<./Keyframe_CHOP.md> "Keyframe CHOP")• [Kinect Azure ](<./Kinect_Azure_CHOP.md> "Kinect Azure CHOP")• [Kinect ](<./Kinect_CHOP.md> "Kinect CHOP")• [Lag ](<./Lag_CHOP.md> "Lag CHOP")• [Laser ](<./Laser_CHOP.md> "Laser CHOP")• [Laser Device ](<./Laser_Device_CHOP.md> "Laser Device CHOP")• [Leap Motion ](<./Leap_Motion_CHOP.md> "Leap Motion CHOP")• [Leuze ROD4 ](<./Leuze_ROD4_CHOP.md> "Leuze ROD4 CHOP")• [LFO ](<./LFO_CHOP.md> "LFO CHOP")• [Limit ](<./Limit_CHOP.md> "Limit CHOP")• [Logic ](<./Logic_CHOP.md> "Logic CHOP")• [Lookup ](<./Lookup_CHOP.md> "Lookup CHOP")• [LTC In ](<./LTC_In_CHOP.md> "LTC In CHOP")• [LTC Out ](<./LTC_Out_CHOP.md> "LTC Out CHOP")• [Math ](<./Math_CHOP.md> "Math CHOP")• [Merge ](<./Merge_CHOP.md> "Merge CHOP")• [MIDI In ](<./MIDI_In_CHOP.md> "MIDI In CHOP")• [MIDI In Map ](<./MIDI_In_Map_CHOP.md> "MIDI In Map CHOP")• [MIDI Out ](<./MIDI_Out_CHOP.md> "MIDI Out CHOP")• [MoSys ](<./MoSys_CHOP.md> "MoSys CHOP")• [Mouse In ](<./Mouse_In_CHOP.md> "Mouse In CHOP")• [Mouse Out ](<./Mouse_Out_CHOP.md> "Mouse Out CHOP")• [Ncam ](<./Ncam_CHOP.md> "Ncam CHOP")• [Noise ](<./Noise_CHOP.md> "Noise CHOP")• [Null ](<./Null_CHOP.md> "Null CHOP")• [OAK Device ](<./OAK_Device_CHOP.md> "OAK Device CHOP")• [OAK Select ](<./OAK_Select_CHOP.md> "OAK Select CHOP")• [Object ](<./Object_CHOP.md> "Object CHOP")• [Oculus Audio ](<./Oculus_Audio_CHOP.md> "Oculus Audio CHOP")• [Oculus Rift ](<./Oculus_Rift_CHOP.md> "Oculus Rift CHOP")• [OpenVR ](<./OpenVR_CHOP.md> "OpenVR CHOP")• [OptiTrack In ](<./OptiTrack_In_CHOP.md> "OptiTrack In CHOP")• [OSC In ](<./OSC_In_CHOP.md> "OSC In CHOP")• [OSC Out ](<./OSC_Out_CHOP.md> "OSC Out CHOP")• [Out ](<./Out_CHOP.md> "Out CHOP")• [Override ](<./Override_CHOP.md> "Override CHOP")• [Pan Tilt ](<./Pan_Tilt_CHOP.md> "Pan Tilt CHOP")• [Panel ](<./Panel_CHOP.md> "Panel CHOP")• [Pangolin ](<./Pangolin_CHOP.md> "Pangolin CHOP")• [Parameter ](<./Parameter_CHOP.md> "Parameter CHOP")• [Pattern ](<./Pattern_CHOP.md> "Pattern CHOP")• [Perform ](<./Perform_CHOP.md> "Perform CHOP")• [Phaser ](<./Phaser_CHOP.md> "Phaser CHOP")• [Pipe In ](<./Pipe_In_CHOP.md> "Pipe In CHOP")• [Pipe Out ](<./Pipe_Out_CHOP.md> "Pipe Out CHOP")• [POP to ](<./POP_to_CHOP.md> "POP to CHOP")• [PosiStageNet ](<./PosiStageNet_CHOP.md> "PosiStageNet CHOP")• [Pulse ](<./Pulse_CHOP.md> "Pulse CHOP")• [RealSense ](<./RealSense_CHOP.md> "RealSense CHOP")• [Record ](<./Record_CHOP.md> "Record CHOP")• [Rename ](<./Rename_CHOP.md> "Rename CHOP")• [Render Pick ](<./Render_Pick_CHOP.md> "Render Pick CHOP")• [RenderStream In ](<./RenderStream_In_CHOP.md> "RenderStream In CHOP")• [Reorder ](<./Reorder_CHOP.md> "Reorder CHOP")• [Replace ](<./Replace_CHOP.md> "Replace CHOP")• [Resample ](<./Resample_CHOP.md> "Resample CHOP")• [S Curve ](<./S_Curve_CHOP.md> "S Curve CHOP")• [Scan ](<./Scan_CHOP.md> "Scan CHOP")• [Script ](<./Script_CHOP.md> "Script CHOP")• [Select ](<./Select_CHOP.md> "Select CHOP")• [Sequencer ](<./Sequencer_CHOP.md> "Sequencer CHOP")• [Serial ](<./Serial_CHOP.md> "Serial CHOP")• [Shared Mem In ](<./Shared_Mem_In_CHOP.md> "Shared Mem In CHOP")• [Shared Mem Out ](<./Shared_Mem_Out_CHOP.md> "Shared Mem Out CHOP")• [Shift ](<./Shift_CHOP.md> "Shift CHOP")• [Shuffle ](<./Shuffle_CHOP.md> "Shuffle CHOP")• [Slope ](<./Slope_CHOP.md> "Slope CHOP")• [SOP to ](<./SOP_to_CHOP.md> "SOP to CHOP")• [Sort ](<./Sort_CHOP.md> "Sort CHOP")• [Speed ](<./Speed_CHOP.md> "Speed CHOP")• [Splice ](<./Splice_CHOP.md> "Splice CHOP")• [Spring ](<./Spring_CHOP.md> "Spring CHOP")• [ST2110 Device ](<./ST2110_Device_CHOP.md> "ST2110 Device CHOP")• [Stretch ](<./Stretch_CHOP.md> "Stretch CHOP")• [Stype In ](<./Stype_In_CHOP.md> "Stype In CHOP")• [Stype Out ](<./Stype_Out_CHOP.md> "Stype Out CHOP")• [Switch ](<./Switch_CHOP.md> "Switch CHOP")• [Sync In ](<./Sync_In_CHOP.md> "Sync In CHOP")• [Sync Out ](<./Sync_Out_CHOP.md> "Sync Out CHOP")• [Tablet ](<./Tablet_CHOP.md> "Tablet CHOP")• [Time Slice ](<./Time_Slice_CHOP.md> "Time Slice CHOP")• [Timecode ](<./Timecode_CHOP.md> "Timecode CHOP")• [Timeline ](<./Timeline_CHOP.md> "Timeline CHOP")• [Timer ](<./Timer_CHOP.md> "Timer CHOP")• [TOP to ](<./TOP_to_CHOP.md> "TOP to CHOP")• [Touch In ](<./Touch_In_CHOP.md> "Touch In CHOP")• [Touch Out ](<./Touch_Out_CHOP.md> "Touch Out CHOP")• [Trail ](<./Trail_CHOP.md> "Trail CHOP")• [Transform ](<./Transform_CHOP.md> "Transform CHOP")• [Transform XYZ ](<./Transform_XYZ_CHOP.md> "Transform XYZ CHOP")• [Trigger ](<./Trigger_CHOP.md> "Trigger CHOP")• [Trim ](<./Trim_CHOP.md> "Trim CHOP")• [Warp ](<./Warp_CHOP.md> "Warp CHOP")• [Wave ](<./Wave_CHOP.md> "Wave CHOP")• [WrnchAI ](<./WrnchAI_CHOP.md> "WrnchAI CHOP")• [ZED ](<./ZED_CHOP.md> "ZED CHOP")
