# Timer CHOP

## 

Summary

The Timer CHOP is an engine for running timed processes. It outputs channels such as timing fractions, counters, pulses and timer states, and it calls python functions (callbacks) when various timing events occur. 

Examples using the Timer CHOP include triggering multiple timed cues, running playlists, timelines, state machines, and driving pre-animated animation components in 3D scenes. See Help -> Operator Snippets for numerous examples. 

You set a timer to a number of seconds (or unlimited), frames or samples, and trigger it to start via the Start parameter or the second input CHOP. The Timer CHOP outputs in seconds, frames, samples, fraction and on-off states as it’s counting, including a`done`channel that goes on when it is complete. When it reaches certain states like end-of-cycles or when it’s done, various python callbacks are called allowing you to customize its behavior. 

The Timer CHOP gets triggered by events (via pulsing its parameters or driving its two inputs). It takes events in, counts time, changes state. Via its python callback functions, you can send events out to other nodes, set parameters, get/set values in DATs, CHOPs and storage, restart itself, or trigger other nodes. As such, it can operate as a state machine. 

It has play/pause, plus a speed control to slow down or speed up the timer. 

It can also cycle indefinitely and then can be signaled to end immediately or at the end of the current cycle. 

**Recommended** : the **OP Snippets for Timer CHOP**. See the channel descriptions in [Initialize Start](<./Initialize_Start.md> "Initialize Start"). 

**Multiple Timer segments** \- One Timer CHOP can also have multiple timers within it. By attaching a Table DAT you can define one timer (segment) per row. In Serial Timers mode it allows for one time segment followed by another. In Parallel Timers mode, the timers all run in parallel, each with its own begin time and length, and its own set of output channels. 

The Timer CHOP can be Locked to Timeline in a deterministic way, or run more freely in Sequential Mode. When run independently from the timeline, you can jump ahead, break out of cycles, pause,`goTo()`exact position or timecode in the timer, and dynamically adjust the speed. 

Attach an Info DAT to the Timer CHOP to see the timecodes, or use the`.timecode`members. Custom text strings can be placed in the Info DAT for each segment, and custom animated channels can be created. 

To make an entire Timer CHOP loop after the last segment, set the On Done menu to Re-Start. 

**Tip: What happens when you press Start** \- The timers are at 0 when you Initialize, for example`timer_frames`= 0. On the frame when you press Start, by default, the`running`channel goes from 0 to 1, and all the`timer_`counter channels step forward by 1 frame. If you want the timers to hold at 0 until the next frame, set the Run Value parameter to Zero. This is useful when you are cutting from black or other media to a visible first-frame of a movie when`running`goes to 1. 

**Chaining Timers** \- The Timer CHOPs can be chained together, so that when one ends, the next can begin. They just need to all be Initialized together, where the`ready_pulse`channel of one Timer CHOP is exported to the Initialize parameter of the next Timer CHOP. Then they can be run in sequence, where the output of one Timer CHOP’s`done_pulse`channel is wired to the Start input (or exported to the Start parameter) of the next Timer CHOP. You start the chain of timers by starting the first Timer CHOP. By using some Timer CHOPs to loop awaiting input or response, or by adding logic to decide which CHOP to start next, state machines can be implemented. 

### Callbacks

The callbacks are called at different moments during the timer progression.`onInitialize()`gets called when you pulse the Initialize parameter. Here you can prepare any part of your setup prior to starting. At the end of Initialize the timer goes into a "ready" state.`onStart()`gets called on the frame that the Start parameter is pulsed. The timer then goes into a "running" state.`onTimerActive()`gets called every frame that the timer is running and there is no Delay or Play is off.`onCycleStart()`gets called if the timer is set to cycle via the Cycle parameters. 

Before a cycle or segment ends, an`onCycleEndAlert()`callback based on the Cycle End Alert parameter can be called to allow you to prepare for the next cycle, segment or Timer CHOP.`onSegmentEnter()`and`onSegmentExit()`get called if the timer is being driven by a Segments DAT which acts like several timers in one. The argument`segment`in these callbacks is actually an object with useful members including any custom columns you have in your segment table: In`onSegmentEnter()`, put the code`print(help(segment))``onDone()`gets called when the timer reaches its finished state. 

You can initialize at a specific time by using`.masterSeconds`in`onInitialize()`. 

**See also** : [Trigger CHOP](<./Trigger_CHOP.md> "Trigger CHOP"), [Event CHOP](<./Event_CHOP.md> "Event CHOP"), [Speed CHOP](<./Speed_CHOP.md> "Speed CHOP"), [Count CHOP](<./Count_CHOP.md> "Count CHOP"), [Beat CHOP](<./Beat_CHOP.md> "Beat CHOP"), [Event CHOP](<./Event_CHOP.md> "Event CHOP"), [Clock CHOP](<./Clock_CHOP.md> "Clock CHOP"), [Delay CHOP](<./Delay_CHOP.md> "Delay CHOP"), [CHOP Execute DAT](<./CHOP_Execute_DAT.md> "CHOP Execute DAT"), [LFO CHOP](<./LFO_CHOP.md> "LFO CHOP"). time measurements{| class="wikitable"|+ Time Measurements and what affects them|- ! Name !! Speed !! Play !! Cycles !! Go To and Cueing !! Subrange !! Delay Between Segments|-| Cumulative Time Count | | slows if speed<1 | | pauses when off | | keeps counting | | jumps | | jumps | | pauses|-| Playing Time Count | | unaffected | | pauses when off | | keeps counting | | keeps counting | | keeps counting | | keeps counting|-| Running Time Count | | unaffected | | unaffected | | keeps counting | | keeps counting | | keeps counting | | keeps counting|-| Master Time Count | | slows if speed<1 | | pauses when off | | see note * | | jumps | | jumps | | keeps counting|-| Segment + Fraction | | 0 to 1 per-segment | | pauses when off | | see note * | | jumps | | jumps | | pauses|} **note: jumps back every cycle if Cycle Limit is off. keeps counting up if Cycle Limit is on.**

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[timerCHOP_Class](<./TimerCHOP_Class.md> "TimerCHOP Class")

## 

Parameters - Timer Page

Active`active`\- ⊞ \- The Timer cooks: Never / Always / While Running (while in "running" state) / While Playing (while in "running" state and Play is on). 
* Never`never`-
* Always`always`-
* While Running`running`-
* While Playing`playing`-


Time Control`timecontrol`\- ⊞ \- **Sequential** (timeline-independent) or **Locked to Timeline**. In Locked to Timeline, non-deterministic features are disabled. **External CHOP Channel** lets you drive the master time (`.masterSeconds`etc) using a CHOP channel defined by the parameters on the External page. **External Timecode** lets you drive the master time using a timecode CHOP/DAT/Object. 
* Lock To Timeline`lock`\- Output is determined by the current frame position.
* Sequential`sequential`\- Output runs continuously, regardless of current frame position.
* External CHOP Channel`chop`\- Output is determined by external CHOP channel value.
* External Timecode`timecode`\- Output is determined by the value of an external timecode.


Defer Par Changes`deferpars`\- When On, parameter changes like Length, Cycles and others are ignored until the next Intitalize. When Off, paraameter changes affect the timer immediately (possibly giving jumps in state). 

Initialize`initialize`\- (pulse parameter) Initialize is the signal to get the timer ready: sets the frames, samples and fraction counters to zero (delay, timer, cycle, segment), set the output channels in the proper state,`done`to be off, the onInitialize() callback is run, and when initialize is complete, it indicates it’s ready by turning on the`ready`channel, awaiting a Start pulse. 

Start`start`\- (pulse) Start is the signal to begin the timers counting. It will count through the delay first, then the timer length. It does an Initialize if it is not already initialized, and then starts counting. 

Length Type`lengthtype`\- ⊞ \- Describes how the length is defined. 
* Fixed`fixed`\- Lengths are finite, that is of a specific duration.
* Infinite`infinite`\- The segments run continuously without end.


Length`length`\- ⊞ \- (float) the time-length of the timer. Set the Units menu to Seconds, Frames or Samples. 
* Length`length`-
* Length Units`lengthunits`-


Delay`delay`\- ⊞ \- (float) after Start, the delay before the timer begins counting. 
* Delay`delay`-
* Delay Units`delayunits`-


Run Values`runvalues`\- ⊞ \- On the frame that Start is triggered and the`running`channel goes from 0 to 1, this determines what the channels`timer_frames`,`timer_samples`and`timer_fraction`will be. If the menu is set to Zero, these channels will be 0 as they are when the timer is initialized. If set to One, on the first frame running is 1,`timer_frames`and`timer_samples`will be set to one frame, and`timer_fraction`will also have stepped forward by a frame. 
* Zero`zero`-
* One`one`-


Play`play`\- (onoff) Pauses the timer. It is basically a 0 or 1 multiplier on the Speed. 

Speed`speed`\- (default 1) Slows down or speeds up the timer. 

Cue`cue`\- ⊞ \- Freezes playing at the Cue Point. 
* Cue`cue`-
* Cue Pulse`cuepulse`-


Cue Point`cuepoint`\- ⊞ \- Time (Seconds, Frames or Fraction) which the cue point is frozen to. 
* Cue Point`cuepoint`-
* Cue Units`cueunits`-


Cycle`cycle`\- (default Off) causes the timer to loop back to 0 when it reaches the end of the cycle. 

Cycle Limit`cyclelimit`\- When the Cycle parameter is On, this determines if it will cycle indefinitely or cycle some maximum number of cycles. 

Maximum Cycles`maxcycles`\- When Cycle is on and Cycle Limit is on, this sets the maximum number of cycles. 

Cycle End Alert`cycleendalert`\- ⊞ \- The number of seconds, frames or samples before a cycle, segment or done state is reached that the`onCycleEndAlert()`callback is called. This allows you to prepare for the next cycle, segment or timer. 
* Cycle End Alert`cycleendalert`-
* Notify Units`notifyunits`-


Exit Segment at End of Cycle`exitendcycle`\- When pulsed, it will exit the cycle (and segment) at the end of the currently-playing cycle. 

Go to End of Cycle`gotoendcycle`\- When pulsed, it will exit the cycle (and segment) immediately. 

Go to Done`gotodone`\- Will immediately go to the Done state. 

On Done`ondone`\- ⊞ \- Determines which action to take when the timer gets to the end, ie "is done" or finished. Note there is also a onDone callback that can be used for customizing behavior. 
* Do Nothing`donothing`\- No action taken.
* Re-Initialize`reinit`\- Will re-initialize the timer, this is the same as pulsing the Initialize parameter above.
* Re-Start`restart`\- Will re-initialize and re-start the timer, this is the same as pulsing the Start parameter above.
* Re-Start without Initializing`restartnoinit`\- Will re-star the timeer without re-initializing.


Callbacks DAT`callbacks`\- The path to the DAT containing callbacks for this Timer CHOP. 

Length Units`lengthunits`\- ⊞ \- Choose between using Samples, Frames, or Seconds as the units for this parameter. 
* I`samples`-
* F`frames`-
* S`seconds`-


Delay Units`delayunits`\- ⊞ \- Choose between using Samples, Frames, or Seconds as the units for this parameter. 
* I`samples`-
* F`frames`-
* S`seconds`-


Cue Pulse`cuepulse`\- Jump instantly to the Cue Point. 

Cue Units`cueunits`\- ⊞ \- Choose between using Samples, Frames, Seconds, Fraction(0-1) as the units for this parameter. 
* I`samples`-
* F`frames`-
* S`seconds`-
* %`fraction`-


Notify Units`notifyunits`\- ⊞ \- Choose between using Samples, Frames, or Seconds as the units for this parameter. 
* I`samples`-
* F`frames`-
* S`seconds`-

## 

Parameters - Segments Page

You can specify multiple timers in one Timer CHOP. A "segment" acts as one timer, with its own length, delay time, number of cycles to repeat and other conditions. 

Segments DAT`segdat`\- A table DAT that contains one row per timer (segment). The column headings can be`delay`or`begin`,`length`,`cycle`,`cyclelimit`,`maxcycles`and`cycleendalert`, which override the equivalent parameters. (These are the internal names for the corresponding parameters.)`begin`is unique as it replaces`delay`, and it represents the time from Start that the timer will begin counting, whether the CHOP is set to Serial Timers or Parallel Timers (see Segment Method). 

The Segments DAT also can include any number of custom columns. See Columns to Custom Channels and Columns to Info DAT below. __

Segment Method`segmethod`\- ⊞ \- If the Segment Method is **Serial Timers** , the timers will be played back-to-back. If the Segment Method is **Parallel Timers** , the timers can be played at the same time, and a set of channels will be output for each timer. 
* Serial Timers`serial`-
* Parallel Timers`parallel`-


Segment Units`segunits`\- ⊞ \- For the columns`delay`,`begin`,`length`and`cycleendalert`, you specify whether it’s seconds, frames or samples with this menu. 
* Samples`samples`-
* Frames`frames`-
* Seconds`seconds`-


Segments End Time`segsendtime`\- ⊞ \- Describes how the end time is calculated. 
* From Segments DAT`dat`\- The end time is based on the Segments DAT values.
* From Length Parameter`par`\- The end time is based on the Length parameter value.
* Max of Parameter/Table`max`\- The end time is based on the greater of the Length parameter value and the Segments DAT values.


Columns to Custom Channels`channelcolumns`\- Optional extra columns (any name) in the segments DAT can be output as extra channels (the columns must contain numbers). Specify their names in the Columns to Channels parameter. The channel name will be the column name. You can also output the`length`,`delay`, etc columns as channels. 

Custom Channel Interpolation`interpolation`\- ⊞ \- By default, custom channels step to their new value at the begin of the segment. This menu lets you interpolate to the new value linearly, or any combination of ease-in and ease-out. 
* Step to Value`steptovalue`-
* Linear to Value`lineartovalue`-
* Ease In to Value`easeintovalue`-
* Ease Out to Value`easeouttovalue`-
* Ease In-Out to Value`easeinouttovalue`-


Columns to Info DAT`infocolumns`\- Optional extra columns (any name) in the segments DAT can be output to the Info DAT (attach an Info DAT to the Timer CHOP) if you specify their names in this parameter. 

Go to Previous Segment`gotoprevseg`\- (pulse) Jump to Previous Segment. 

Go to Next Segment`gotonextseg`\- (pulse) Jump to Next Segment. 

_Lingo_
* Segment – each segment acts as one timer, with delay time, length, number of cycles to repeat and other conditions.
  * Begin – in Parallel Timers, the number of seconds after a Start (frames or samples) after which each timer starts counting up from zero.
  * Done – The state it goes into when all the timers has finished counting, whether they are in Parallel or Serial, Segments or not.
  * End – Cycle End is the end of each cycle, Segment End is the end of the segment.
  * Cumulative Time – Zero at Start, a count that is affected by speed and rises while timers are active (not during delays).
  * Running Time – Zero at Start, the wall-clock time since Start was called no matter what are the delays, speeds, cycles or premature clicking of Go To Segment End. It stops counting when Done has been reached.

## 

Parameters - Sub Range Page

Operate the timer within a sub range of the total length. 

Sub Range`subrange`\- Turn this parameter on to limit the timer output to a subrange of the full length. 

Sub Start`substart`\- ⊞ \- The beginning point of the sub range. 
* Sub Start`substart`-
* Sub Start Units`substartunits`-


Sub End`subend`\- ⊞ \- The end point of the sub range. 
* Sub End`subend`-
* Sub End Units`subendunits`-


Sub End Action`subendaction`\- ⊞ \- Controls the behavior once the sub range end point is reached: Loop at End, or Pause at End. 
* Pause at End`pause`-
* Loop at End`loop`-


Sub Start Units`substartunits`\- ⊞ \- Choose between using Samples, Frames, or Seconds as the units for this parameter. 
* I`samples`-
* F`frames`-
* S`seconds`-


Sub End Units`subendunits`\- ⊞ \- Choose between using Samples, Frames, or Seconds as the units for this parameter. 
* I`samples`-
* F`frames`-
* S`seconds`-

## 

Parameters - Outputs Page

Timer Fraction`outfraction`\- Outputs channel`timer_fraction`for each segment. 

Timer Count`outtimercount`\- ⊞ \- Outputs the elapsed Seconds channel as`timer_seconds`, Frames outputs channel as`timer_frames`, or Samples outputs channel as`timer_samples`. Because this is elapsed time,`timer_frames`starts at 0, as do the others. 
* Off`off`-
* Samples`samples`-
* Frames`frames`-
* Seconds`seconds`-
* All`all`-


Timer Active`outtimeractive`\- Outputs channel`timer_active`which is on only while the timer fraction is counting (is non-zero). 

Timer Pulse`outtimerpulse`\- Outputs channel`timer_pulse`when the timer reaches its length. 

Delay Fraction`outdelayfraction`\- Outputs a 0-1 fraction in`delay_fraction`while the delay occurs. 

Delay Count`outdelaycount`\- ⊞ \- Outputs the delay count in seconds, frames or samples. 
* Off`off`-
* Samples`samples`-
* Frames`frames`-
* Seconds`seconds`-
* All`all`-


Initializing`outinit`\- Outputs channel`initializing`= 1 while the timer is initalizing (i.e. while the callback`onInitialize()`returns non-zero). 

Ready`outready`\- Outputs channel`ready`which is 1 after an Initialize and before a Start. 

Ready Pulse`outreadypulse`\- Outputs a pulse when initialization has finished and the timer is ready to start. It pulses even when the timer starts rights away after an initialization. 

Running`outrunning`\- Outputs channel`running`which is 1 after a Start and before the Done. 

Done`outdone`\- Outputs channel`done`when done or complete. 

Done Pulse`outdonepulse`\- Outputs channel`done`when the all timers have reached their completion. 

Cycles`outcycle`\- Outputs channel`cycles`, which is the number of cycles completed (In a segment), starting with 0 during the entire first cycle. If you jump to Done, cycle is incremented as if it played normally to the done state. 

Cycle Pulse`outcyclepulse`\- Outputs a pulse at the end of every cycle, even on the first and only cycle. 

Cycles + Fraction`outcycleplusfraction`\- Outputs channel`cycle_plus_fraction`, starting with 0 for entire first cycle. 

Segment`outseg`\- Outputs channel`segment`, starting with 0 for first segment. 

Segment Pulse`outsegpulse`\- Outputs channel`segment_pulse`which is a pulse at the end of each segment. 

Segment + Fraction`outsegplusfraction`\- Outputs channel`segment_plus_fraction`, starting with 0 for first segment ending at #segments at end. 

Length`outlength`\- ⊞ \- Outputs channel`length`, starting with 0 for first segment ending at #segments at end. 
* Off`off`-
* Seconds`seconds`-
* Frames`frames`-
* Samples`samples`-
* All`all`-


Cumulative Timer Count`outcumulativecount`\- ⊞ \- Outputs`cumulative_seconds`,`cumulative_frames`or`cumulative_samples`. It is a time count that adds up all the Timer Active times for all segments since Start: it is affected by "Speed", and counts up only while`timer_active`(Play) is on. See the python member`.cumulativeSeconds`. 
* Off`off`-
* Samples`samples`-
* Frames`frames`-
* Seconds`seconds`-
* All`all`-


Playing Timer Count`outplayingcount`\- ⊞ \- Outputs`playing_seconds`,`playing_frames`or`playing_samples`. It is a time count that adds up all the Timer Active times for all segments since Start: it is not affected by "Speed", and counts up only while`timer_active`and`play`is on. See the python member`.playingSeconds`. 
* Off`off`-
* Seconds`seconds`-
* Frames`frames`-
* Samples`samples`-
* All`all`-


Running Time Count`outrunningcount`\- ⊞ \- Outputs the "wall-clock" time since Start occurred, no matter what are the delays, speeds, cycles or pre-mature clicking of Go To Segment End, etc. It stops counting when Done has been reached.`running_seconds`,`running_frames`, or`running_samples`. When CHOP is set to Parallel Timers, this will output a channel per segment plus one global running time channel. See the python member`.runningSeconds`. 
* Off`off`-
* Samples`samples`-
* Frames`frames`-
* Seconds`seconds`-
* All`all`-


Master Time Count`outmastercount`\- ⊞ \- Outputs`master_seconds`,`master_frames`or`master_samples`. It is a time count that adds up all the Timer Active times for all segments since Start: it is affected by "Speed", and counts up only while`timer_active`and`play`is on. It also includes any delay times. See the python member`.masterSeconds`. 
* Off`off`-
* Seconds`seconds`-
* Frames`frames`-
* Samples`samples`-
* All`all`-

## 

Parameters - External Page

External CHOP`extchop`\- The CHOP used to control the current point in the timer. 

External Units`extunits`\- ⊞ \- Choose between using Samples, Frames, or Seconds as the units for this parameter. 
* I`samples`-
* F`frames`-
* S`seconds`-
* %`fraction`-


External Channel`extchannel`\- The channel that will control the current point of the timer. 

External Timecode Object/CHOP/DAT`exttcop`\- Time is specified using a timecode. Should be a reference to either a CHOP with channels 'hour', 'second', 'minute', 'frame', a DAT with a timecode string in its first cell, or a [Timecode Class](<./Timecode_Class.md> "Timecode Class") object. 

External Start Offset`extstartoff`\- Specifies the external time at which the timer should start. 

External Initialize Offset`extinitoff`\- Specifies the external time at which the timer should initialize. 

Sample Rate`rate`\- The sample rate that the CHOP outputs at, which is also used when the units of Length, Delay and Cycle End Alert time are set to Samples. The default sample rate is 60 samples per second. 

External Timecode Object`exttcobj`\- Time is specified using a timecode. Should be a reference to either a CHOP with channels 'hour', 'second', 'minute', 'frame', a DAT with a timecode string in its first cell, or a [Timecode Class](<./Timecode_Class.md> "Timecode Class") object. 

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
  * Input 1:  -

## 

Info CHOP Channels

Extra Information for the Timer CHOP can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). 

### 

Specific Timer CHOP Info Channels
* frames_timer -
* frames_segment -
* frames_cumulative -
* frames_running -

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


  
TouchDesigner Build: Latest\nwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditor2025.300002023.112802022.241402021.100002018.28070before 2018.28070

CHOPs   
---  
[Ableton Link ](<./Ableton_Link_CHOP.md> "Ableton Link CHOP")• [Analyze ](<./Analyze_CHOP.md> "Analyze CHOP")• [Angle ](<./Angle_CHOP.md> "Angle CHOP")• [Attribute ](<./Attribute_CHOP.md> "Attribute CHOP")• [Audio Band EQ ](<./Audio_Band_EQ_CHOP.md> "Audio Band EQ CHOP")• [Audio Binaural ](<./Audio_Binaural_CHOP.md> "Audio Binaural CHOP")• [Audio Device In ](<./Audio_Device_In_CHOP.md> "Audio Device In CHOP")• [Audio Device Out ](<./Audio_Device_Out_CHOP.md> "Audio Device Out CHOP")• [Audio Dynamics ](<./Audio_Dynamics_CHOP.md> "Audio Dynamics CHOP")• [Audio File In ](<./Audio_File_In_CHOP.md> "Audio File In CHOP")• [Audio File Out ](<./Audio_File_Out_CHOP.md> "Audio File Out CHOP")• [Experimental:Audio File Out ](</index.php?title=Experimental:Audio_File_Out_CHOP&action=edit&redlink=1> "Experimental:Audio File Out CHOP \(page does not exist\)")• [Audio Filter ](<./Audio_Filter_CHOP.md> "Audio Filter CHOP")• [Audio Movie ](<./Audio_Movie_CHOP.md> "Audio Movie CHOP")• [Experimental:Audio Movie ](</index.php?title=Experimental:Audio_Movie_CHOP&action=edit&redlink=1> "Experimental:Audio Movie CHOP \(page does not exist\)")• [Audio NDI ](<./Audio_NDI_CHOP.md> "Audio NDI CHOP")• [Audio Oscillator ](<./Audio_Oscillator_CHOP.md> "Audio Oscillator CHOP")• [Audio Para EQ ](<./Audio_Para_EQ_CHOP.md> "Audio Para EQ CHOP")• [Audio Play ](<./Audio_Play_CHOP.md> "Audio Play CHOP")• [Audio Render ](<./Audio_Render_CHOP.md> "Audio Render CHOP")• [Experimental:Audio Render ](</index.php?title=Experimental:Audio_Render_CHOP&action=edit&redlink=1> "Experimental:Audio Render CHOP \(page does not exist\)")• [Audio Spectrum ](<./Audio_Spectrum_CHOP.md> "Audio Spectrum CHOP")• [Audio Stream In ](<./Audio_Stream_In_CHOP.md> "Audio Stream In CHOP")• [Audio Stream Out ](<./Audio_Stream_Out_CHOP.md> "Audio Stream Out CHOP")• [Audio VST ](<./Audio_VST_CHOP.md> "Audio VST CHOP")• [Audio Web Render ](<./Audio_Web_Render_CHOP.md> "Audio Web Render CHOP")• [Beat ](<./Beat_CHOP.md> "Beat CHOP")• [Bind ](<./Bind_CHOP.md> "Bind CHOP")• [BlackTrax ](<./BlackTrax_CHOP.md> "BlackTrax CHOP")• [Blend ](<./Blend_CHOP.md> "Blend CHOP")• [Blob Track ](<./Blob_Track_CHOP.md> "Blob Track CHOP")• [Body Track ](<./Body_Track_CHOP.md> "Body Track CHOP")• [Experimental:Body Track ](</index.php?title=Experimental:Body_Track_CHOP&action=edit&redlink=1> "Experimental:Body Track CHOP \(page does not exist\)")• [Bullet Solver ](<./Bullet_Solver_CHOP.md> "Bullet Solver CHOP")• [Experimental:CHOP ](</index.php?title=Experimental:CHOP&action=edit&redlink=1> "Experimental:CHOP \(page does not exist\)")• [Clip Blender ](<./Clip_Blender_CHOP.md> "Clip Blender CHOP")• [Clip ](<./Clip_CHOP.md> "Clip CHOP")• [Clock ](<./Clock_CHOP.md> "Clock CHOP")• [Experimental:Clock ](</index.php?title=Experimental:Clock_CHOP&action=edit&redlink=1> "Experimental:Clock CHOP \(page does not exist\)")• [Composite ](<./Composite_CHOP.md> "Composite CHOP")• [Constant ](<./Constant_CHOP.md> "Constant CHOP")• [Copy ](<./Copy_CHOP.md> "Copy CHOP")• [Count ](<./Count_CHOP.md> "Count CHOP")• [CPlusPlus ](<./CPlusPlus_CHOP.md> "CPlusPlus CHOP")• [Cross ](<./Cross_CHOP.md> "Cross CHOP")• [Cycle ](<./Cycle_CHOP.md> "Cycle CHOP")• [DAT to ](<./DAT_to_CHOP.md> "DAT to CHOP")• [Delay ](<./Delay_CHOP.md> "Delay CHOP")• [Delete ](<./Delete_CHOP.md> "Delete CHOP")• [DMX In ](<./DMX_In_CHOP.md> "DMX In CHOP")• [DMX Out ](<./DMX_Out_CHOP.md> "DMX Out CHOP")• [Experimental:DMX Out ](</index.php?title=Experimental:DMX_Out_CHOP&action=edit&redlink=1> "Experimental:DMX Out CHOP \(page does not exist\)")• [Envelope ](<./Envelope_CHOP.md> "Envelope CHOP")• [EtherDream ](<./EtherDream_CHOP.md> "EtherDream CHOP")• [Event ](<./Event_CHOP.md> "Event CHOP")• [Expression ](<./Expression_CHOP.md> "Expression CHOP")• [Extend ](<./Extend_CHOP.md> "Extend CHOP")• [Face Track ](<./Face_Track_CHOP.md> "Face Track CHOP")• [Experimental:Face Track ](</index.php?title=Experimental:Face_Track_CHOP&action=edit&redlink=1> "Experimental:Face Track CHOP \(page does not exist\)")• [Fan ](<./Fan_CHOP.md> "Fan CHOP")• [Feedback ](<./Feedback_CHOP.md> "Feedback CHOP")• [File In ](<./File_In_CHOP.md> "File In CHOP")• [File Out ](<./File_Out_CHOP.md> "File Out CHOP")• [Filter ](<./Filter_CHOP.md> "Filter CHOP")• [Experimental:Filter ](</index.php?title=Experimental:Filter_CHOP&action=edit&redlink=1> "Experimental:Filter CHOP \(page does not exist\)")• [FreeD In ](<./FreeD_In_CHOP.md> "FreeD In CHOP")• [FreeD Out ](<./FreeD_Out_CHOP.md> "FreeD Out CHOP")• [Function ](<./Function_CHOP.md> "Function CHOP")• [Gesture ](<./Gesture_CHOP.md> "Gesture CHOP")• [Handle ](<./Handle_CHOP.md> "Handle CHOP")• [Helios DAC ](<./Helios_DAC_CHOP.md> "Helios DAC CHOP")• [Hog ](<./Hog_CHOP.md> "Hog CHOP")• [Hokuyo ](<./Hokuyo_CHOP.md> "Hokuyo CHOP")• [Hold ](<./Hold_CHOP.md> "Hold CHOP")• [Import Select ](<./Import_Select_CHOP.md> "Import Select CHOP")• [In ](<./In_CHOP.md> "In CHOP")• [Info ](<./Info_CHOP.md> "Info CHOP")• [Interpolate ](<./Interpolate_CHOP.md> "Interpolate CHOP")• [Introduction To s Vid ](<./Introduction_To_CHOPs_Vid.md> "Introduction To CHOPs Vid")• [Inverse Curve ](<./Inverse_Curve_CHOP.md> "Inverse Curve CHOP")• [Inverse Kin ](<./Inverse_Kin_CHOP.md> "Inverse Kin CHOP")• [Join ](<./Join_CHOP.md> "Join CHOP")• [Joystick ](<./Joystick_CHOP.md> "Joystick CHOP")• [Keyboard In ](<./Keyboard_In_CHOP.md> "Keyboard In CHOP")• [Keyframe ](<./Keyframe_CHOP.md> "Keyframe CHOP")• [Kinect Azure ](<./Kinect_Azure_CHOP.md> "Kinect Azure CHOP")• [Kinect ](<./Kinect_CHOP.md> "Kinect CHOP")• [Lag ](<./Lag_CHOP.md> "Lag CHOP")• [Laser ](<./Laser_CHOP.md> "Laser CHOP")• [Experimental:Laser ](</index.php?title=Experimental:Laser_CHOP&action=edit&redlink=1> "Experimental:Laser CHOP \(page does not exist\)")• [Laser Device ](<./Laser_Device_CHOP.md> "Laser Device CHOP")• [Experimental:Laser Device ](</index.php?title=Experimental:Laser_Device_CHOP&action=edit&redlink=1> "Experimental:Laser Device CHOP \(page does not exist\)")• [Leap Motion ](<./Leap_Motion_CHOP.md> "Leap Motion CHOP")• [Leuze ROD4 ](<./Leuze_ROD4_CHOP.md> "Leuze ROD4 CHOP")• [LFO ](<./LFO_CHOP.md> "LFO CHOP")• [Limit ](<./Limit_CHOP.md> "Limit CHOP")• [Logic ](<./Logic_CHOP.md> "Logic CHOP")• [Lookup ](<./Lookup_CHOP.md> "Lookup CHOP")• [LTC In ](<./LTC_In_CHOP.md> "LTC In CHOP")• [LTC Out ](<./LTC_Out_CHOP.md> "LTC Out CHOP")• [Math ](<./Math_CHOP.md> "Math CHOP")• [Merge ](<./Merge_CHOP.md> "Merge CHOP")• [MIDI In ](<./MIDI_In_CHOP.md> "MIDI In CHOP")• [MIDI In Map ](<./MIDI_In_Map_CHOP.md> "MIDI In Map CHOP")• [MIDI Out ](<./MIDI_Out_CHOP.md> "MIDI Out CHOP")• [MoSys ](<./MoSys_CHOP.md> "MoSys CHOP")• [Mouse In ](<./Mouse_In_CHOP.md> "Mouse In CHOP")• [Mouse Out ](<./Mouse_Out_CHOP.md> "Mouse Out CHOP")• [Ncam ](<./Ncam_CHOP.md> "Ncam CHOP")• [Noise ](<./Noise_CHOP.md> "Noise CHOP")• [Null ](<./Null_CHOP.md> "Null CHOP")• [OAK Device ](<./OAK_Device_CHOP.md> "OAK Device CHOP")• [OAK Select ](<./OAK_Select_CHOP.md> "OAK Select CHOP")• [Object ](<./Object_CHOP.md> "Object CHOP")• [Oculus Audio ](<./Oculus_Audio_CHOP.md> "Oculus Audio CHOP")• [Oculus Rift ](<./Oculus_Rift_CHOP.md> "Oculus Rift CHOP")• [OpenVR ](<./OpenVR_CHOP.md> "OpenVR CHOP")• [OptiTrack In ](<./OptiTrack_In_CHOP.md> "OptiTrack In CHOP")• [OSC In ](<./OSC_In_CHOP.md> "OSC In CHOP")• [OSC Out ](<./OSC_Out_CHOP.md> "OSC Out CHOP")• [Out ](<./Out_CHOP.md> "Out CHOP")• [Override ](<./Override_CHOP.md> "Override CHOP")• [Experimental:Pan Tilt ](</index.php?title=Experimental:Pan_Tilt_CHOP&action=edit&redlink=1> "Experimental:Pan Tilt CHOP \(page does not exist\)")• [Panel ](<./Panel_CHOP.md> "Panel CHOP")• [Pangolin ](<./Pangolin_CHOP.md> "Pangolin CHOP")• [Experimental:Pangolin ](</index.php?title=Experimental:Pangolin_CHOP&action=edit&redlink=1> "Experimental:Pangolin CHOP \(page does not exist\)")• [Parameter ](<./Parameter_CHOP.md> "Parameter CHOP")• [Experimental:Parameter ](</index.php?title=Experimental:Parameter_CHOP&action=edit&redlink=1> "Experimental:Parameter CHOP \(page does not exist\)")• [Pattern ](<./Pattern_CHOP.md> "Pattern CHOP")• [Perform ](<./Perform_CHOP.md> "Perform CHOP")• [Phaser ](<./Phaser_CHOP.md> "Phaser CHOP")• [Pipe In ](<./Pipe_In_CHOP.md> "Pipe In CHOP")• [Pipe Out ](<./Pipe_Out_CHOP.md> "Pipe Out CHOP")• [Experimental:POP to ](</index.php?title=Experimental:POP_to_CHOP&action=edit&redlink=1> "Experimental:POP to CHOP \(page does not exist\)")• [PosiStageNet ](<./PosiStageNet_CHOP.md> "PosiStageNet CHOP")• [Pulse ](<./Pulse_CHOP.md> "Pulse CHOP")• [RealSense ](<./RealSense_CHOP.md> "RealSense CHOP")• [Record ](<./Record_CHOP.md> "Record CHOP")• [Rename ](<./Rename_CHOP.md> "Rename CHOP")• [Render Pick ](<./Render_Pick_CHOP.md> "Render Pick CHOP")• [RenderStream In ](<./RenderStream_In_CHOP.md> "RenderStream In CHOP")• [Reorder ](<./Reorder_CHOP.md> "Reorder CHOP")• [Replace ](<./Replace_CHOP.md> "Replace CHOP")• [Resample ](<./Resample_CHOP.md> "Resample CHOP")• [Experimental:Resample ](</index.php?title=Experimental:Resample_CHOP&action=edit&redlink=1> "Experimental:Resample CHOP \(page does not exist\)")• [S Curve ](<./S_Curve_CHOP.md> "S Curve CHOP")• [Scan ](<./Scan_CHOP.md> "Scan CHOP")• [Script ](<./Script_CHOP.md> "Script CHOP")• [Experimental:Script ](</index.php?title=Experimental:Script_CHOP&action=edit&redlink=1> "Experimental:Script CHOP \(page does not exist\)")• [Select ](<./Select_CHOP.md> "Select CHOP")• [Sequencer ](<./Sequencer_CHOP.md> "Sequencer CHOP")• [Serial ](<./Serial_CHOP.md> "Serial CHOP")• [Shared Mem In ](<./Shared_Mem_In_CHOP.md> "Shared Mem In CHOP")• [Shared Mem Out ](<./Shared_Mem_Out_CHOP.md> "Shared Mem Out CHOP")• [Shift ](<./Shift_CHOP.md> "Shift CHOP")• [Shuffle ](<./Shuffle_CHOP.md> "Shuffle CHOP")• [Slope ](<./Slope_CHOP.md> "Slope CHOP")• [SOP to ](<./SOP_to_CHOP.md> "SOP to CHOP")• [Sort ](<./Sort_CHOP.md> "Sort CHOP")• [Speed ](<./Speed_CHOP.md> "Speed CHOP")• [Experimental:Speed ](</index.php?title=Experimental:Speed_CHOP&action=edit&redlink=1> "Experimental:Speed CHOP \(page does not exist\)")• [Splice ](<./Splice_CHOP.md> "Splice CHOP")• [Spring ](<./Spring_CHOP.md> "Spring CHOP")• [Experimental:ST2110 Device ](</index.php?title=Experimental:ST2110_Device_CHOP&action=edit&redlink=1> "Experimental:ST2110 Device CHOP \(page does not exist\)")• [Stretch ](<./Stretch_CHOP.md> "Stretch CHOP")• [Experimental:Stretch ](</index.php?title=Experimental:Stretch_CHOP&action=edit&redlink=1> "Experimental:Stretch CHOP \(page does not exist\)")• [Stype In ](<./Stype_In_CHOP.md> "Stype In CHOP")• [Stype Out ](<./Stype_Out_CHOP.md> "Stype Out CHOP")• [Switch ](<./Switch_CHOP.md> "Switch CHOP")• [Sync In ](<./Sync_In_CHOP.md> "Sync In CHOP")• [Sync Out ](<./Sync_Out_CHOP.md> "Sync Out CHOP")• [Tablet ](<./Tablet_CHOP.md> "Tablet CHOP")• [Time Slice ](<./Time_Slice_CHOP.md> "Time Slice CHOP")• [Timecode ](<./Timecode_CHOP.md> "Timecode CHOP")• [Experimental:Timecode ](</index.php?title=Experimental:Timecode_CHOP&action=edit&redlink=1> "Experimental:Timecode CHOP \(page does not exist\)")• [Timeline ](<./Timeline_CHOP.md> "Timeline CHOP")• Timer • [Experimental:Timer ](</index.php?title=Experimental:Timer_CHOP&action=edit&redlink=1> "Experimental:Timer CHOP \(page does not exist\)")• [TOP to ](<./TOP_to_CHOP.md> "TOP to CHOP")• [Experimental:TOP to ](</index.php?title=Experimental:TOP_to_CHOP&action=edit&redlink=1> "Experimental:TOP to CHOP \(page does not exist\)")• [Touch In ](<./Touch_In_CHOP.md> "Touch In CHOP")• [Experimental:Touch In ](</index.php?title=Experimental:Touch_In_CHOP&action=edit&redlink=1> "Experimental:Touch In CHOP \(page does not exist\)")• [Touch Out ](<./Touch_Out_CHOP.md> "Touch Out CHOP")• [Trail ](<./Trail_CHOP.md> "Trail CHOP")• [Transform ](<./Transform_CHOP.md> "Transform CHOP")• [Transform XYZ ](<./Transform_XYZ_CHOP.md> "Transform XYZ CHOP")• [Trigger ](<./Trigger_CHOP.md> "Trigger CHOP")• [Experimental:Trigger ](</index.php?title=Experimental:Trigger_CHOP&action=edit&redlink=1> "Experimental:Trigger CHOP \(page does not exist\)")• [Trim ](<./Trim_CHOP.md> "Trim CHOP")• [Warp ](<./Warp_CHOP.md> "Warp CHOP")• [Wave ](<./Wave_CHOP.md> "Wave CHOP")• [WrnchAI ](<./WrnchAI_CHOP.md> "WrnchAI CHOP")• [ZED ](<./ZED_CHOP.md> "ZED CHOP")• [Experimental:ZED ](</index.php?title=Experimental:ZED_CHOP&action=edit&redlink=1> "Experimental:ZED CHOP \(page does not exist\)")
