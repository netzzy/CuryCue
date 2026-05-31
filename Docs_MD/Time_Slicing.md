# Time Slicing

Time Slicing is a feature in TouchDesigner that keeps your CHOP channels smooth, even when your overall frame rate goes down and your timeline skips frames. Time Slicing keeps your overall animation smoother and more accurate, and helps keep your audio from popping when your frame rate drops.   
  
A **Time Slice** is the time from the last cook frame to the current cook frame. (See [Absolute Time](<./Absolute_Time.md> "Absolute Time").) In [CHOPs](<./CHOP.md> "CHOP") it is the set of short channels that contain the CHOP channels' samples between the last and the current cook frame. 

If the global frame rate is 60 frames per second, the time slice is a multiple of 1/60 second. For example, if TouchDesigner skipped a frame, the time slice is 2 samples and is 2/60 seconds. 

You can see the time slice sizes by creating a [Perform CHOP](<./Perform_CHOP.md> "Perform CHOP") and sending it to a [Trail CHOP](<./Trail_CHOP.md> "Trail CHOP") and setting Perform to the Cook and Time Slice Step channels,`cook`and`timeslice_step`. 

See the [Time Slice CHOP](<./Time_Slice_CHOP.md> "Time Slice CHOP") in [OP Snippets](<./OP_Snippets.md> "OP Snippets"). 

Many CHOPs, like the [Filter CHOP](<./Filter_CHOP.md> "Filter CHOP") cook a timeslice of samples to assure that curves are smooth and pulses are accurate, even if the TouchDesigner process is skipping frames. In contrast, the [Constant CHOP](<./Constant_CHOP.md> "Constant CHOP") is not time sliced - it it always one sample long. 

Time Slice is a **Common** page parameter on each CHOP and is automatically set/unset on most CHOPs. 

**Example** : If the current frame is 77 and the previously-displayed frame is 73, then the time slice is 4 frames long (frames 74 to 77). This means that TouchDesigner jumped ahead 4 frames to keep up with the real-time clock. Assuming the timeline frame rate is 60 frames per second, if the CHOP contains audio at its default 44100 samples per second, there will be 44100*4/60 = 2940 samples in the CHOP containing audio. 

You can check if a CHOP is time sliced via the [MMB](<./Mouse_Click.md> "Mouse Click") info pop-up on any CHOP node. 

**Note** : The maximum length of a time slice is set via the preference in Edit -> Preferences -> CHOPs. It is currently 200 msec. See the audio tip in [Audio Device Out CHOP](<./Audio_Device_Out_CHOP.md> "Audio Device Out CHOP"). 

These short channels can be computed much faster than a full animation range channel, and uses less memory. This gain in speed and memory efficiency is extremely important for interactive 3D, puppeteering and audio processing. 

[**Time Slicing Tutorial**](<./Time_Slicing_Vid.md> "Time Slicing Vid")

CHOPs often calculate the channel over a long start-end frame range. This is a good method for pre-animated channels and keyframed channels which do not need to be re-generated or re-calculated each frame. 

However, if the channel does need to be evaluated every frame due to user input (with for example a Mouse, Keyboard or MIDI CHOPs) or other realtime data input, and we are only interested in the values over the last few frames, then cooking the entire range of the channel is unnecessary. It is more efficient to calculate only the fraction of the channel that is needed. This fraction is known as a "Time Slice". 

When you view the info on a CHOP, it reports its frame range and whether it is time sliced or not. 

See also [Absolute Time](<./Absolute_Time.md> "Absolute Time"), the [OP Snippets](<./OP_Snippets.md> "OP Snippets") for the [Time Slice CHOP](<./Time_Slice_CHOP.md> "Time Slice CHOP"), the [Timeline](<./Timeline.md> "Timeline"), the [Hog CHOP](<./Hog_CHOP.md> "Hog CHOP") and the Tscript:timeslice Command. 

To Time Slice a CHOP, set its flag on the Common page. Try the [Noise CHOP](<./Noise_CHOP.md> "Noise CHOP") to see the effect with Time Slice On and Off. 

Send a [Constant CHOP](<./Constant_CHOP.md> "Constant CHOP") to a [Filter CHOP](<./Filter_CHOP.md> "Filter CHOP"), play forward and adjust the Constant CHOP slider to see the results of a Time Sliced CHOP. 

With Time Slicing, samples do not get lost or un-processed when TouchDesigner cannot keep up with the [timeline](<./Timeline.md> "Timeline")'s sample rate, default 60 frames per second. All frames get processed, albeit in batches of 1, 2 or more at a time. This gives TouchDesigner more accurate curves and timing. 

Time Slicing especially reduces the memory requirements of high sample-rate CHOPs like those in audio networks, and provides nearly instantaneous results when you tweak audio parameters in a network. Since even a short audio clip can use over a megabyte of storage, storing and processing only the necessary fraction of the clip reduces the memory requirements significantly, especially in large CHOP networks. 

Time Sliced CHOPs do not maintain any more history about the channel than is needed, and they recook every frame. This makes them well suited to realtime applications. Even so, they can be used to "perform" and record an animation, instead of keyframing it. 

## 

How Time Slicing Works

Time Sliced CHOPs cook whenever the [Timeline](<./Timeline.md> "Timeline") is moved forward. The amount of time that the Timeline jumps ahead is the size of the current Time Slice. The Time Slice is synchronized with the Timeline so that its first sample begins just after the previous Time Slice's last sample, and its last sample is at the current frame. If the Timeline is playing forwards, the Time Slices generated will never overlap, nor will there be any gaps between them. All Time Sliced CHOPs will have the same Time Slice interval for a given cook. 

When the CHOP network needs to cook, the Time Slice interval is computed and a single Time Slice is passed through the network. Since the current frame is always contained within the slice, the slice can be easily exported to any parameter. 

## 

Interface

**CHOP Parameter Dialog ** \- The Time Slice toggle is located in the Common page of the parameter dialog of all CHOPs. This toggle is greyed-out for CHOPs that do not have Time Slice capability, and for some CHOPs which always operate in Time Slice mode. 

**Edit - > Preferences -> CHOPs** **Dialog** \- The Time Slice preferences can be changed using this dialog. They can also be changed from the Textport, using the timeslice Command. 

## 

CHOPs that are Always Time Sliced

Most CHOPs do not need Time Slice capability; they will work on time sliced input in the same manner that they would on normal channel data. Time Sliced CHOPs and non-Time Sliced CHOPs can be mixed within the same CHOP network. The Time Slice option is provided for CHOPs that perform operations that read or modify other samples in the channel other than the current sample, or that maintain internal states. 

Generally, if you want to create a time sliced CHOP network, all CHOPs with Time Slice capability should have their Time Slice flags (located on their Common page) on. 

## 

CHOPs which are Occasionally Time Sliced

The following CHOPs will output Time Slices under certain conditions, but are not considered Time Sliced CHOPs. The Time Slice button in the Common page is greyed out for these CHOPs. 

[Trim CHOP](<./Trim_CHOP.md> "Trim CHOP") \- The Trim CHOP can trim the current time slice out of any input CHOP. This function is selected by changing the Unit Values menu to Current Time Slice. 

[Record CHOP](<./Record_CHOP.md> "Record CHOP") \- This CHOP can be used to record the output of a Time Sliced CHOP over the animation range. It can also be used to interpolate a Time Slice from a CHOP that outputs a single frame (like the Mouse or Keyboard CHOPs). The input can be sampled over the entire Time Slice, or only at the current frame using the Record Input parameter. The output range can be selected using the Record Output parameter. 

## 

Null CHOP Can Stop Overcooking

See the [Null CHOP](<./Null_CHOP.md> "Null CHOP") Cook Type -> Selective option. 

## 

Time Slice Options

Time Slice preferences can be changed using the **Edit - > Preferences -> CHOPs** dialog. 

**Maximum Time Slice Size (ms)** \- This option allows you to limit the maximum size of a Time Slice in milliseconds. The default maximum is 200ms. This is useful if you only need a few frames of history, and the Timeline is jumping ahead by large intervals. If a Time Slice is larger than this maximum size, it will be clipped from the current frame backwards (causing a gap between this slice and the previous one). The slice will always end on the current frame. 

## 

Uses for Time Slicing

### 

Realtime Puppeteering and Control

Time Slicing speeds up the animation response to user input. It provides you with a variety of effects to layer onto the input, such as lag, springs, and filtering. It is otherwise more difficult to achieve these effects on realtime input. 

### 

Animation Performance 

Sometimes an animation is much easier to perform with an input device than it is to keyframe or produce using CHOPs. The input can be recorded with a Record CHOP and locked. This data can then be manipulated with CHOPs, or performed again as needed. 

### 

Realtime Audio Processing 

The performance increase of Time Sliced audio processing versus normal audio processing is quite significant. With Time Slicing, it is possible to process realtime audio input and use the data to control animations. You can also do the opposite - use features of the animation to control audio output. Without Time Slicing, it is difficult to set up a network to do these actions in realtime. 

### 

General Audio Processing 

Time Slicing allows you to clean up or add effects to audio files more efficiently. You can turn all the Time Slice capable CHOPs on and manipulate the audio while playing it, getting realtime results. When you are satisfied with the new audio, the Time Sliced CHOPs are turned off and the final audio clip is generated for the full range. This allows much more rapid tweaking of parameters to produce a desired effect.
