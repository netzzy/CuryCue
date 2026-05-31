# Audio Device In CHOP

##   
  
Summary

The Audio Device In CHOP receives audio from any of the attached audio input devices using DirectSound/CoreAudio or ASIO. It always outputs time sliced audio data. 

If you want to capture the data in memory, use a [Trail CHOP](<./Trail_CHOP.md> "Trail CHOP") or [Record CHOP](<./Record_CHOP.md> "Record CHOP"). If you want to record to a file, use [Audio File Out CHOP](<./Audio_File_Out_CHOP.md> "Audio File Out CHOP") or [Movie File Out TOP](<./Movie_File_Out_TOP.md> "Movie File Out TOP"). 

The Audio Device In CHOP can receive analog control voltages (**CVs**) as long as your audio device's analog to digital converters can handle constant non-zero voltages. 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[audiodeviceinCHOP_Class](<./AudiodeviceinCHOP_Class.md> "AudiodeviceinCHOP Class")

## 

Parameters - Audio Device In Page

Active`active`\- Turns the audio input on or off. 

Driver`driver`\- ⊞ \- Select between default DirectSound/CoreAudio, ASIO, or native device supported drivers. 
* DirectSound/CoreAudio`default`\- The default Windows audio driver (a.k.a. WDM) or macOS CoreAudio driver, depending on your OS.
* ASIO`asio`\- Low-latency drivers which usually come from the hardware's manufacturer.
* DataPath (RGBEASY)`datapath`\- Native support for capturing the audio from DataPath devices.
* Blackmagic`blackmagic`\- Native support for capturing the audio from [Blackmagic Design](<./Blackmagic_Design.md> "Blackmagic Design") devices.
* AJA`aja`\- Native support for capturing the audio from [AJA](<./AJA.md> "AJA") devices.


Device`device`\- A menu of available audio devices to receive input from. Selecting _default_ sets the audio device to that which is selected in Windows Control Panel>Sounds and Audio Devices>Audio>Sound Recording. 

Error if Missing`errormissing`\- The CHOP will error if the specified device is not found. 

Inputs`inputs`\- When Driver is set to ASIO on Windows or CoreAudio on macOS, this parameter lets you pick which input channels to use. 

Format`format`\- ⊞ \- When Driver is set to DirectSound, this set mono, stereo, or multi-channel. Also determines how many channels are created 1(mono) or 2(stereo left and stereo right), or when set to multi-channel set the number of channels active on the Input 1 and Input 2 parameter pages. 
* Mono`mono`\- Uses a single mono channel.
* Stereo`stereo`\- USes 2 channels for stereo left and right.
* Multi-Channel`multichannel`\- Uses whichever channels are turned On on the Input 1 and Input 2 parameter pages.


Rate`rate`\- Audio input sample rate expressed in samples per second. 

Buffer Length`bufferlength`\- The size of the input buffer, will effect latency. The larger the buffer the more latency is introduced. 

Number of Channels`numchan`\- When using Driver Blackmagic or AJA, use this parameter to set the number of channels. 

## 

Parameters - Input 1 Page

The toggles on this page are used when the Driver is set to DirectSound. The channels names are from legacy DirectSound terms, but can also be considered more simply chan1, chan2, chan3 and so on. For example, you can access the 7 microphone array from a **Kinect Azure** sensor using DirectSound and turning on the first 7 toggles here. 

Front Left`frontleft`\- Enable this input if available (or simply adds another input channel). 

Front Right`frontright`\- Enable this input if available (or simply adds another input channel). 

Front Center`frontcenter`\- Enable this input if available (or simply adds another input channel). 

Low Frequency`lowfrequency`\- Enable this input if available (or simply adds another input channel). 

Back Left`backleft`\- Enable this input if available (or simply adds another input channel). 

Back Right`backright`\- Enable this input if available (or simply adds another input channel). 

Front Left of Center`frontleftcenter`\- Enable this input if available (or simply adds another input channel). 

Front Right of Center`frontrightcenter`\- Enable this input if available (or simply adds another input channel). 

Back Center`backcenter`\- Enable this input if available (or simply adds another input channel). 

## 

Parameters - Input 2 Page

The toggles on this page are used when the Driver is set to DirectSound. The channels names are from legacy DirectSound terms, but can also be considered more simply chan1, chan2, chan3 and so on. 

Side Left`sideleft`\- Enable this input if available (or simply adds another input channel). 

Side Right`sideright`\- Enable this input if available (or simply adds another input channel). 

Top Center`topcenter`\- Enable this input if available (or simply adds another input channel). 

Top Front Left`topfrontleft`\- Enable this input if available (or simply adds another input channel). 

Top Front Center`topfrontcenter`\- Enable this input if available (or simply adds another input channel). 

Top Front Right`topfrontright`\- Enable this input if available (or simply adds another input channel). 

Top Back Left`topbackleft`\- Enable this input if available (or simply adds another input channel). 

Top Back Center`topbackcenter`\- Enable this input if available (or simply adds another input channel). 

Top Back Right`topbackright`\- Enable this input if available (or simply adds another input channel). 

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

Extra Information for the Audio Device In CHOP can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). 

### 

Specific Audio Device In CHOP Info Channels
* queue_speed -
* queue_read_pos -
* queue_write_pos -
* queue_length -
* queue_recovers -

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


  
TouchDesigner Build: Latest\n2022.241402021.100002018.28070before 2018.28070Error while fetching data from URL [https://3.21.8.37/api.php?action=query&list=categorymembers&cmtitle=Category:CHOPs&format=xml&cmlimit=500](<https://3.21.8.37/api.php?action=query&list=categorymembers&cmtitle=Category:CHOPs&format=xml&cmlimit=500>): $2.  
Error fetching URL: SSL: certificate subject name '*.derivative.ca' does not match target host name '3.21.8.37'  
There was a problem during the HTTP request: 0 Error  
Could not get URL [https://3.21.8.37/api.php?action=query&list=categorymembers&cmtitle=Category:CHOPs&format=xml&cmlimit=500](<https://3.21.8.37/api.php?action=query&list=categorymembers&cmtitle=Category:CHOPs&format=xml&cmlimit=500>) after 3 tries.

CHOPs   
---
