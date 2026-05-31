# Creating Audio with CHOPs

## 

Introduction

Audio is managed with CHOPs in TouchDesigner. CHOPs can generate sounds and can read sounds into TouchDesigner from external sources. Audio can be generated, played from audio files, filtered, mixed and recorded. 

The ways to obtain audio in CHOPs include: from files, movies, microphones or line in. These are described in detail in the section below. To hear audio output from CHOPs, send the audio to an [Audio Device Out CHOP](<./Audio_Device_Out_CHOP.md> "Audio Device Out CHOP"). 

For example, the [Audio Oscillator CHOP](<./Audio_Oscillator_CHOP.md> "Audio Oscillator CHOP") can generate a constant-frequency audio signal. The [Trigger CHOP](<./Trigger_CHOP.md> "Trigger CHOP") takes an on-off control from TouchDesigner, and generates a volume envelope with a delay, attack, decay, sustain and release transition that can multiplied with an audio CHOP with a [Math CHOP](<./Math_CHOP.md> "Math CHOP") controlling its loudness. The [Math CHOP](<./Math_CHOP.md> "Math CHOP") and [Audio Dynamics CHOP](<./Audio_Dynamics_CHOP.md> "Audio Dynamics CHOP") act as a mixer and the [Audio Para EQ CHOP](<./Audio_Para_EQ_CHOP.md> "Audio Para EQ CHOP") filters the spectrum of audio. 

## 

Quick Audio Startup

To quickly get audio going, try the following: [File:Audio with CHOPS ex.tox](</File:Audio_with_CHOPS_ex.tox> "File:Audio with CHOPS ex.tox")
* Connect a default LFO CHOP to a default Audio Oscillator CHOP.
  * Connect the Audio Oscillator CHOP to an Audio Device Out CHOP.
  * You should hear a rising and falling tone.
  * Connect the LFO CHOP to a new Audio Oscillator CHOP and set the oscillator's Base Frequency to 330.
  * Connect the two Oscillators to a Merge CHOP. Connect the Merge CHOP to the Audio Device Out CHOP. You should hear one oscillator in each left and right channels.


Next use an Audio File In CHOP as a sound source, connecting it to the Audio Device Out CHOP. 

## 

Loading Audio

[Audio File In CHOP](<./Audio_File_In_CHOP.md> "Audio File In CHOP") \- loads audio from a file as it plays. This method of streaming uses very little memory as it only loads the samples of audio it needs at the time, ideal for large audio files. The CHOP channels created are [time-sliced](<./Time_Slicing.md> "Time Slicing"). 

[Audio Movie CHOP](<./Audio_Movie_CHOP.md> "Audio Movie CHOP") \- loads the audio track from a movie that has been loaded into a [Movie File In TOP](<./Movie_File_In_TOP.md> "Movie File In TOP"). Playback is controlled from Movie File In TOP. The CHOP channels created are [time-sliced](<./Time_Slicing.md> "Time Slicing"). 

[File In CHOP](<./File_In_CHOP.md> "File In CHOP") \- loads the entire audio file into CHOPs. The audio is loaded into CHOPs at the sample rate of the audio file. The higher the sample rate, the more memory CHOPs will use to load the audio. The channels created are not [time-sliced](<./Time_Slicing.md> "Time Slicing"). When completely loaded into CHOPs, it is easy to manipulate the audio downstream with additional Filter CHOPs; stretch, splice, pitch, volume, etc. Care must be taken running real-time systems with large audio files and high sample rates, as CPU usage for these operations is very high. 

[Audio Device In CHOP](<./Audio_Device_In_CHOP.md> "Audio Device In CHOP") \- streams audio into TouchDesigner from any audio input device attached to the computer. The CHOP channels created are [time-sliced](<./Time_Slicing.md> "Time Slicing"). 

[Audio Play CHOP](<./Audio_Play_CHOP.md> "Audio Play CHOP") \- plays back a sound file directly to the audio output device. Great for simple triggering of sounds. Plays back just a single file or selects from a list of files stored in a [DAT](<./DAT.md> "DAT") list. Can also be triggered using the Tscript`audioplay`Command. Audio is not passed further down the CHOP network. 

### 

Scrub Controls 

When using a Audio File In CHOP, audio can be cued or scrubbed at least 3 ways: 
* Audio File In's parameter Play Mode must first be set to Sequential. Select a Cue Point and press Cue Pulse.
  * Audio File In's parameter Play Mode must first be set to Specify Index. using the Index parameter. Turn off the Repeat parameter to stop audio buzzing when not scrubbing.
  * When using the Audio Movie CHOP, scrubbing the audio can be done through the Movie File In TOP which is referenced. As the movie playback is scrubbed, the audio will follow.


Using a File In CHOP, audio can be scrubbed by scrubbing TouchDesigner's main [Timeline](<./Timeline.md> "Timeline") throughout the frame range of the File In CHOP. 

### 

Repeating Audio

When using an [Audio File In CHOP](<./Audio_File_In_CHOP.md> "Audio File In CHOP"), set the Repeat parameter to On. 

Using a [File In CHOP](<./File_In_CHOP.md> "File In CHOP"), which statically loads the entire audio file, you can set the Extend Left and Extend Right parameters to Cycle. 

[Audio Play CHOPs](<./Audio_Play_CHOP.md> "Audio Play CHOP") need to be repeatedly triggered to repeat the audio. 

### 

TouchDesigner Audio Output Volume

The Audio Device Out CHOP sets the overall output level to the speakers. This is sent to the volume controls in Windows. 

## 

Outputting Audio to a File

You can output the audio in any CHOP using the [RMB](<./Mouse_Click.md> "Mouse Click") menu on the CHOP. Select Save Data Channels in the menu and hit the arrow button to see the file format suffixes that can be used on your output files, such as`.aif`. You can check the file by playing it with [VLC](<http://www.videolan.org/vlc/index.html>) or [QuickTime](<http://support.apple.com/kb/DL837>) or another audio player. 

Note, the CHOP may be [time-sliced](<./Time_Slicing.md> "Time Slicing"), in which case you will need to first record it into a [Record CHOP](<./Record_CHOP.md> "Record CHOP") or [Trail CHOP](<./Trail_CHOP.md> "Trail CHOP"). 

## 

Modifying Audio
* [Math CHOP](<./Math_CHOP.md> "Math CHOP") \- Increase/decrease volume, mix sounds, stereo to mono, perform functions of a level mixer.
  * [Audio Oscillator CHOP](<./Audio_Oscillator_CHOP.md> "Audio Oscillator CHOP") \- Make audible tones & LFO (low frequency oscillator).
  * [Constant CHOP](<./Constant_CHOP.md> "Constant CHOP") \- Provide constant-pitch control for oscillator.
  * [LFO CHOP](<./LFO_CHOP.md> "LFO CHOP") \- Add vibrato or LFO.
  * [Noise CHOP](<./Noise_CHOP.md> "Noise CHOP") \- Generate white noise.
  * [Audio Band EQ CHOP](<./Audio_Band_EQ_CHOP.md> "Audio Band EQ CHOP") \- Graphic equalizer.
  * [Audio Para EQ CHOP](<./Audio_Para_EQ_CHOP.md> "Audio Para EQ CHOP") \- Filter, echo, pitch shift.
  * [Audio Filter CHOP](<./Audio_Filter_CHOP.md> "Audio Filter CHOP") \- Low pass, high pass, band pass filter.
  * [Resample CHOP](<./Resample_CHOP.md> "Resample CHOP") \- Change the sample rate of a sound.
  * [Trigger CHOP](<./Trigger_CHOP.md> "Trigger CHOP") \- Make volume envelope with delay, attack, decay, sustain, release.
  * [Timer CHOP](<./Timer_CHOP.md> "Timer CHOP") \- Cross-dissolve one sound to another.
  * [Lag CHOP](<./Lag_CHOP.md> "Lag CHOP") \- Make glissando pitch sweeps.
  * [Envelope CHOP](<./Envelope_CHOP.md> "Envelope CHOP") \- Follow the loudness of a sound.


When you are processing an audio clip by reading the whole file into an [File In CHOP](<./File_In_CHOP.md> "File In CHOP"): 
* [Trim CHOP](<./Trim_CHOP.md> "Trim CHOP") \- Shorten the audio.
  * [Cycle CHOP](<./Cycle_CHOP.md> "Cycle CHOP") \- Make it repeat.
  * [Wave CHOP](<./Wave_CHOP.md> "Wave CHOP") \- Add vibrato or LFO.
  * [Shift CHOP](<./Shift_CHOP.md> "Shift CHOP") \- Re-time the sounds, simple echo, delay.
  * [Stretch CHOP](<./Stretch_CHOP.md> "Stretch CHOP") \- Make a sound slower or faster, but shifting pitch too.
  * [Copy CHOP](<./Copy_CHOP.md> "Copy CHOP") \- Use triggers to copy sounds along a timeline.
  * [Pulse CHOP](<./Pulse_CHOP.md> "Pulse CHOP") \- Time pulses to produce rhythms as a sequencer.
  * [Composite CHOP](<./Composite_CHOP.md> "Composite CHOP") \- Layer one sound over a longer sound.
  * [Lookup CHOP](<./Lookup_CHOP.md> "Lookup CHOP") \- Soft limit amplitudes etc.

## 

3D Audio

CHOPs can take events from a 3D scene, imported through the [SOP to CHOP](<./SOP_to_CHOP.md> "SOP to CHOP") or [Object CHOP](<./Object_CHOP.md> "Object CHOP"), and be used to trigger sounds and control the placement of sounds in 3D space. 

An object, particle, or point position in 3D space can be used to set the left-right ear separation, or used as reverb controls which add a cue that simulates proximity of the sound. 

Audio can be generated for offscreen objects, adding more 3D cues and realism. 

[Filter Animation Channels](</index.php?title=Filter_Animation_Channels&action=edit&redlink=1> "Filter Animation Channels \(page does not exist\)")
