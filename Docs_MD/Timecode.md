# Timecode

## Timecode in TouchDesigner

Timecode is a way of expressing time as a combination of hours, minutes, seconds, and frames. It can be expressed in a string, for example`03:22:11:10`, or as a bit pattern, as in LTC timecode embedded in audio streams. The prevalent standard for timecode, SMPTE Timecode, was originally designed for video tape machines, tapes and broadcast transmissions. 

In TouchDesigner we try to represent time everywhere possible as timecode, though the fundamental time units are expressed as frames on the timeline, and in seconds or frames in [Absolute Time](<./Absolute_Time.md> "Absolute Time"). 

Timecode in TouchDesigner is represented in a`tdu.Timecode`object (see [Timecode_Class](<./Timecode_Class.md> "Timecode Class")). These objects are built into some operators, or can be created as their own entities in python. 

Numerous operators (see below) that deal with time in various ways have a`.timecode`member that report the timecode of the data in that operator in various formats and units. 

The [Timecode CHOP](<./Timecode_CHOP.md> "Timecode CHOP") contains a`.timecode`member and is an easy-to-use UI to set the current timecode of the CHOP, do some simple arithmetic with timecodes, and convert between different representations of timecode. It gets its timecode values from (1) its parameters, (2) channels coming into the CHOP, (3) other operators, or (4) expressions. 

Timecode anywhere in TouchDesigner can be conformed (with limitations) into the SMPTE standard for timecode, or by un-setting a`.smpte`flag on a`.timecode`object, it can be allowed to non-conform, like go past 24 hours, express negative time, or be set to above 60 frames per second. 

**Tip** : See the **OP Snippets** for the [Timecode CHOP](<./Timecode_CHOP.md> "Timecode CHOP"). 

**Tip** : A useful hardware box for monitoring timecode: [Rosendahl Timecode](<https://rosendahl-studiotechnik.com/mif4.html>)

## The`tdu.Timecode`Object

See: [Timecode Class](<./Timecode_Class.md> "Timecode Class")

## Operators with a`.timecode`Member
* [Timecode CHOP](<./Timecode_CHOP.md> "Timecode CHOP")
  * [Movie File In TOP](<./Movie_File_In_TOP.md> "Movie File In TOP")
  * [Audio File In CHOP](<./Audio_File_In_CHOP.md> "Audio File In CHOP")
  * [Video Device In TOP](<./Video_Device_In_TOP.md> "Video Device In TOP")
  * [LTC In CHOP](<./LTC_In_CHOP.md> "LTC In CHOP")
  * [LTC Out CHOP](<./LTC_Out_CHOP.md> "LTC Out CHOP")
  * [Timer CHOP](<./Timer_CHOP.md> "Timer CHOP") \- has 3 members:`.timecode`,`.runningTimecode`, and`.runningLengthTimecode`– **BACKWARD COMPATIBILITY** : these used to return strings but were updated to return a`tdu.Timecode`instead. There is also`.masterTimecode`,`.playingTimecode`,`.cumulativeTimecode`.
  * [Stype In CHOP](<./Stype_In_CHOP.md> "Stype In CHOP")
  * [Stype TOP](<./Stype_TOP.md> "Stype TOP")
  * [Timeline CHOP](<./Timeline_CHOP.md> "Timeline CHOP")
  * [Time COMP](<./Time_COMP.md> "Time COMP")
  * [Sync In CHOP](<./Sync_In_CHOP.md> "Sync In CHOP")
  * [Sync Out CHOP](<./Sync_Out_CHOP.md> "Sync Out CHOP")
  * [DMX In CHOP](<./DMX_In_CHOP.md> "DMX In CHOP")
  * [Clock CHOP](<./Clock_CHOP.md> "Clock CHOP")
  * [MIDI In CHOP](<./MIDI_In_CHOP.md> "MIDI In CHOP")
  * [OAK-D](<./OAK-D.md> "OAK-D") OPs


**Note** : Any OP with a`.timecode`member will also have a Timecode Info Type available on its [Info CHOP](<./Info_CHOP.md> "Info CHOP") that provides the timecode value as a set of CHOP channels. 

## The SMPTE Timecode Standard

See: 
* <https://en.wikipedia.org/wiki/SMPTE_timecode>
  * <http://www.philrees.co.uk/articles/timecode.htm>


If the`.smpte`flag is off in any Timecode object or CHOP, you can break the standard and have time greater than 24 hours, negative time, and any number of frames per second above SMPTE's 60 limit. 

## Frames

Frames in timecode are not the same as frames on the timeline or frames in CHOPs. The timeline can be set to any integer number of frames per second, but timecode coming into or out-of TouchDesigner can have another assumption of frames per second. Typically timecode uses 24, 25, 30, 48, 50 or 60 frames per second, or 29.97 frames per second, implementing what is called "drop frames" in the video industry. 

## Drop Frame

See: <https://sonix.ai/resources/what-is-drop-frame-vs-non-drop-frame-timecode/>
