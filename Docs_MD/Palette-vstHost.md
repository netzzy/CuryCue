# VST Host

VSTHost is an experimental component for loading and hosting VST plugins. A VST Host loads VST-plugins, and provides a framework for synchronizing playback, routing MIDI events and audio channel data and mapping parameters for control, modulation and automation. 

This example also includes a MIDI In CHOP configured to work with a device like a keyboard or MIDI sequencer. As well it includes a basic sequencer built with TouchDesigner. 

## Overview

Audio plugins in general come in two types. There are instrument VSTs and filter VSTs. Instrument VSTs can be further divided into 2 sub categories. There are sequencer instruments that only generate MIDI event data and there are instruments that generate audio like keyboard synthesizers. There are also VSTs that are both sequencers and generate audio like models of the Roland TB303 and drum machines like 808, 909 etc. 

Although there are different types of VSTs they are all hosted by the same [Audio VST CHOP](<./Audio_VST_CHOP.md> "Audio VST CHOP"). 

The VST Host component demonstrates how an instrument VST can be loaded and controlled by sending MIDI events using the Python functions included with the [AudiovstCHOP_Class](<./AudiovstCHOP_Class.md> "AudiovstCHOP Class"). Instrument VSTs are the only type of VSTs that will respond to the functions found here. 

## Developers of VST3 Plugins

Links and status of VST3 Plugins that have been tested. 
* <https://www.arturia.com/> \- Most if not all plugins work.
  * <https://www.native-instruments.com/en/> \- Those plugins that are VST3 do work well.
  * <https://hy-plugins.com/> \- Most if not all plugins work.
  * <https://www.fabfilter.com/> \- Most if not all plugins work.

## MIDI Configuration

You can connect a MIDI Keyboard and play VSTs loaded into TouchDesigner. To do this you need to map your MIDI device so that it has a valid mapping ID. This is done using the [MIDI Mapper Dialog](<./MIDI_Mapper_Dialog.md>). 

The midiin1 CHOP is mapped to DeviceID 1. 

The midiin1_callbacks DAT receives midi events from the midiin1 DAT. The callback function passes along a raw bytes object on to the VST instrument loaded into the audiovst1 CHOP. This permits everything from note to control MIDI data to reach the VST. 
[code] 
    op('audiovst1').send(bytes)
    
[/code]

### Monitoring MIDI

To monitor the MIDI coming in use a [MIDI Event DAT](<./MIDI_Event_DAT.md> "MIDI Event DAT"). 

It also handy to have a third party MIDI monitoring console as you set things up. Here are some tools you can download to make the process easier. 

#### MacOS
* <https://www.snoize.com/midimonitor/>
  * <https://hautetechnique.com/midi/midiview/>

#### Windows
* <https://nerds.de/en/loopbe1.html>

### Sending Notes

When a keyboard key is pressed a MIDI note event is received by the midiin CHOP. The midiin callbacks DAT passes the note event along to the audioVST chop using the VST chop's send() function. 

### Sending Control

When a MIDI controller is used, the MIDI controller event is passed along using the VST chop's send() function. This is the case for any other event like pitch bend or aftertouch. 

[MIDI In CHOP](<./MIDI_In_CHOP.md> "MIDI In CHOP") \- Or more modern approach here 

## Timing Clock and Sequencer Plugins

The sequencer type of VST Instrument requires a clock to drive the sequencer forward. VST Sequencers are currently not supported. 

## Using External Sequencers

You can use an external MIDI sequencer like Ableton Live, Bitwig or hardware midi sequencers simply by using the same MIDI mapper configuration as a keyboard. If you wanted to add a sequencer to this VSTHost setup, you can simply copy and paste the midiin1 DAT along with its respective callbacks DAT and change the new miniin DAT device ID to the sequencer's ID in the MIDI Mapper. 

## Build Your Own Sequencer

You can build your own MIDI sequencer to control an instrument VST. To do this you first need a clock source, and then you need an array of sequenced data to lookup as the clock counts forward. In this example the clock source is a [timer CHOP](<./Timer_CHOP.md> "Timer CHOP"). This is an excellent clock source as it has many powerful features. 

### Clock Source

The timer CHOP is configured with a length of 4 seconds and it is cycle parameter is toggled on. This means the sequencer will run forever until stopped. To stop and start the sequencer use the Initialize button to stop and Start button to start. 

The timer CHOP generates a ramp that goes from 0 to 1 over its length. This ramp is used read the music data at a rate of 60 beats per minute. For more information on working with music time and seconds refer to this website [https://toolstud.io/music/bpm.php?bpm=60&bpm_unit=4%2F4](<https://toolstud.io/music/bpm.php?bpm=60&bpm_unit=4%2F4>). 

### Music Data Array

There are 4 properties used to generate music notes over time. First there are the properties pertaining to pitch and loudness - which are note and velocity. Because we are using CHOPs we express MIDI notes and velocity as integers between 0-127. 

Pitch 

Velocity 

Gate 

Trigger 

#### Using an External Sequencer

How to configure MIDI for use with an external sequencer like Numerology / HY32 etc
