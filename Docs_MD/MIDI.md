# MIDI

MIDI is a standard used by musical instruments and interface controllers to send event data between devices. 

See the [MIDI Device Mapper Dialog](<./MIDI_Device_Mapper_Dialog.md> "MIDI Device Mapper Dialog"), [MIDI In DAT](<./MIDI_In_DAT.md> "MIDI In DAT"), [MIDI Event DAT](<./MIDI_Event_DAT.md> "MIDI Event DAT"), [MIDI In Map CHOP](<./MIDI_In_Map_CHOP.md> "MIDI In Map CHOP"), [MIDI In CHOP](<./MIDI_In_CHOP.md> "MIDI In CHOP"), [MIDI Out CHOP](<./MIDI_Out_CHOP.md> "MIDI Out CHOP"). 

To send MIDI events via Python to a MIDI device, use the [MidioutCHOP Class](<./MidioutCHOP_Class.md> "MidioutCHOP Class") with the [MIDI Out CHOP](<./MIDI_Out_CHOP.md> "MIDI Out CHOP"). For [Tscript](<./Tscript.md> "Tscript") use the Tscript`midi`command. 

### Types of MIDI Data
* Note Events - MIDI keyboards output note on/off events, pitch bend events, and aftertouch events. MIDI sequencer devices like the MIDI-enabled descendents of the Roland 808 give note on/off events as well, timed automatically. Many MIDI applications describe these events with english note names such as 'C2' or 'C3', denoting their position on a keyboard piano. TouchDesigner however deals only in index numbers. For example Note 60 may appear as C2 or C3, outside of TouchDesigner even though it represents the exact same MIDI event.
* Controller Events - MIDI controller devices, like the Peavey slider box.
* MCR box each output controller events, which are 0-127 values. Controller events can be used to control anything, and do not generally signify note on - note off events.
* Others event types - see the [MIDI In CHOP](<./MIDI_In_CHOP.md> "MIDI In CHOP").

## Using MIDI With CHOPs

To get MIDI events into CHOP channels, use a [MIDI In CHOP](<./MIDI_In_CHOP.md> "MIDI In CHOP") or the [MIDI Device Mapper Dialog](<./MIDI_Device_Mapper_Dialog.md> "MIDI Device Mapper Dialog") in conjunction with the [MIDI In Map CHOP](<./MIDI_In_Map_CHOP.md> "MIDI In Map CHOP"). 

**Using the MIDI In CHOP**
1. Create a [MIDI In CHOP](<./MIDI_In_CHOP.md> "MIDI In CHOP").
  2. In the MIDI Source parameter menu, select the MIDI input device which is receiving the MIDI events. It should say Serial Port 2, SoundBlaster Card, In From MIDI Yoke:1, or something to that effect.
  3. On the MIDI In CHOP's Control parameter page, make sure the Controller Index covers the an appropriate range for the input device you are using.
  4. Now TouchDesigner is ready to receive MIDI events. Make sure TouchDesigner is playing forward. Turn on the MIDI In CHOP's node viewer, it will display the MIDI values in the CHOP channels which have been created.


**Using the MIDI In Map CHOP**
1. Setup MIDI input devices in the [MIDI Device Mapper Dialog](<./MIDI_Device_Mapper_Dialog.md> "MIDI Device Mapper Dialog").
  2. Map the MIDI in controller events to Sliders and Buttons in the MIDI Device Mapper.
  3. Create a [MIDI In Map CHOP](<./MIDI_In_Map_CHOP.md> "MIDI In Map CHOP").
  4. In the MIDI In Map CHOP's parameters, scope the sliders and buttons you mapped in step 2.
  5. Now TouchDesigner is ready to receive MIDI events. Make sure TouchDesigner is playing forward. Turn on the MIDI In Map CHOP's node viewer, it will display the MIDI values in the CHOP channels which have been created.

### MIDI Events Translated to CHOP Channels

If you look at the middle-mouse button info menu on the CHOP, you will see which channels are being created. Among the CHOP channels, "ch1" means MIDI channel 1, c1 through c8 is controller 1 to 8, and ch1n is the note events of MIDI channel 1. 

By default, TouchDesigner listens to MIDI channel 1, and receives all note events from 0 to 127, and receives all controller events on controller 1 and 2 of MIDI channel 1. 

If you are sending data on other channels, put the channel range in the MIDI Channel parameter, such as "1-8". 1-16 will catch everything. 

If you are playing a MIDI controller box, you must know which controller numbers are going to be produced from your box. On the Control page, the Controller Index should be set to that range, or 1-32 for all controllers. Each controller will create a separate channel. 

Note: To find out what MIDI events are coming into TouchDesigner, open the [MIDI Device Mapper Dialog](<./MIDI_Device_Mapper_Dialog.md> "MIDI Device Mapper Dialog") and turn on the **In Events** tab. All incoming messages will be reported in the console area of the MIDI Device Mapper. 

Now you can play your instrument or move the sliders on your slider box. You should see channels changing in the graph. 

### Note Events on Separate CHOP Channels

By default, all note events of one MIDI channel are combined in on one CHOP channel. In Note Output on the Note page, you can make separate channels by selecting Separate Channels. But it will produce 127 channels unless you reduce the range in the Note Scope. 

### MIDI Channels Merged to one set of CHOP Channels

Also, by default, the events coming in on MIDI Channel 1 are output on a different set of CHOP channels than MIDI Channel 2. If you don't care which MIDI channel the data is coming in on, you can change the Channel Prefix field from "ch" to "" (blank), merging all the MIDI channels selected in the MIDI Channel parameter. 

### Recording While Playing

Record Method on the Record page controls how the CHOP channels are formed. By default, it records into channels at the current frame of a CHOP, so you need to be playing the animation for the recording to take place. When TouchDesigner is stopped, values are still recorded, but they overwrite values at the current frame. 

If you don't care about recording your values (sounds like declaring your religion), you can set Record Method to Single Frame or Current Frame. 

Sometimes you may want to record channels by putting the Midi In CHOP in Single Frame or Current Frame, and passing that to a Record CHOP, which has more controls over what to do with the MIDI channels. From here, you are ready to jam. 

### Scaling, Offseting and Naming Channels

You may want to first change the values in each of the controller channels from a 0-to-1 range into any other range. This means scaling and offseting the channels. 

If it is just one channel that needs to be scaled/offset, or all channels need to be scaled/offset by the same amount, simply use the Range page of a Math CHOP. 

Otherwise, a good way of scaling/offsetting a group of channels is to use a Constant CHOP to hold the scale values for all these channels, and another Constant CHOP to hold the offsets (lower limit) for the channels. 

Then you can use a Math CHOP to scale (multiply two inputs, the Midi In CHOP and the Constant CHOP containing scales). You can use another Math CHOP to offset (add two inputs, the prior Math CHOP and the Constant CHOP containing offsets). 

The MIDI channels eventually get mapped to channel names. They can be mapped using a Rename CHOP. Better yet, you can name the channels of the Constant CHOPs as the desired channel names. If they are the first input of the Math CHOP, the result will take on the names of the Constant CHOPs' channels. 

See the inputs CHOPnet of the demo in $HD/CHOPs/WeirdGuy for an example of the use of Constant and Math CHOPs to scale, offset and rename channels. 

### Lags or Filters on MIDI Data

To generate channels in realtime that are lagging, you need a second or more of the most recent MIDI data. You can use a Trim CHOP with an Absolute Value range of $T-1 to $T, then pass it to a Lag CHOP and adjust the Lag parameters. Use the "Cook to Current Frame" options. 

See the input CHOPnet of the WeirdGuy demo for an example of trimming and lagging channels being recorded. 

### Sliders Control Blends

MIDI slider boxes are often used to mix other pre-animated things in realtime. The MIDI CHOP can be attached to a Blend CHOP and used as the weighting factors. 

### Using MIDI to Assist Keyframe Animation

This is a technique to edit keyframes from normal TouchDesigner channels, such as position and rotation channels of objects. Instead of selecting channels and editing values using the mouse, one channel at a time, you can use an input device like a MIDI slider box or a Puppetworks device to jump between different animation frames and easily edit multiple channel values with the sliders. 

### Start, Stop, Continue Playing in TouchDesigner

If your MIDI device that feeds your workstation is capable of outputting MIDI Start, Stop and Continue messages, TouchDesigner will start at the current start frame, stop at the current frame, and continue from the current frame, respectively. 

### Ticks, Beats and Bars

If your MIDI device that feeds your worksation is capable of outputting clock ticks and optionally Bar Messages, then you can use MIDI to make animations cycle with the music. 

The Timer Ramp Name parameter of the Midi In CHOP creates a ramp that starts at 0 at the start of a musical beat, and increases to 1 at the end of a musical beat. (It uses MIDI timer pulses.) 

The Bar Ramp Name parameter of the Midi In CHOP creates a ramp that starts at 0 at the start of a musical bar, and increases to 1 at the end of a musical bar. (It uses a MIDI sysex code defined by the Bar Message, followed by a MIDI timer pulse.) 

## MIDI Device Manufacturers

There are a number of MIDI devices that are suitable for TouchDesigner. Naturally they all have their pros and cons. Cons frequently include the poor resolution of devices... MIDI controllers usually output integers from 0 to 127. 

Any MIDI hardware like slider devices are good for setting things up, but because the sliders cannot be forced to a previous state, they become less useful to edit existing slider settings in a CHOP. However the Constant CHOP allows the editing of slider-data using relative motion of the sliders. 

### General Transducer Devices

[www.infusionsystems.com Infusion Systems] make I-Cube, a set of transducers and output devices that are configurable as parts. 

### Keyboard Devices

TouchDesigner can be used with virtually any MIDI keyboard to receive note events, pitch bend, velocity and aftertouch. TouchDesigner can also be used with MIDI sequencers. 

## See Also
* [OSC](<./OSC.md> "OSC")
  * [MIDI Topics](</index.php?title=Category:MIDI&action=edit&redlink=1> "Category:MIDI \(page does not exist\)")
  * [Wikipedia on MIDI](<http://en.wikipedia.org/wiki/Musical_Instrument_Digital_Interface>)
