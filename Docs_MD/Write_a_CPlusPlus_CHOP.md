# Write a CPlusPlus CHOP

## Overview  
  
**Make sure you've read through[Write a CPlusPlus Plugin](<./Write_a_CPlusPlus_Plugin.md> "Write a CPlusPlus Plugin") first for general information about writing a plugin for a CPlusPlus CHOP**. 

The CPlusPlus CHOP allows you to manipulate CHOP data using custom code, or bring in/output CHOP data to and from external sources or file formats. 

## Output Channels

You can use one of the CHOP's inputs to determine the number of channels, channel names, sample rate etc. of the output, or you can specify them in code (in getOutputInfo()). 

To get started it is much easier to output non-[Time Sliced](</index.php?title=Time_Slice&action=edit&redlink=1> "Time Slice \(page does not exist\)") data, where you specify the length of the channels and you just fill that much data every frame. The example that comes with the TouchDesigner installer outputs a [Time Slice](</index.php?title=Time_Slice&action=edit&redlink=1> "Time Slice \(page does not exist\)") for illustration though. 

## Time Sliced Data

If you are unfamiliar with what a time slice is, see the [Time Slicing](<./Time_Slicing.md> "Time Slicing") article. 

If the plugin is outputting time sliced data then TouchDesigner will tell you how many samples it wants you to output. The number of samples depends on how long it's been since TouchDesigner last cooked (due to skipped frames), and the sample rate of the [Time Slice](</index.php?title=Time_Slice&action=edit&redlink=1> "Time Slice \(page does not exist\)") vs the sample rate of the CHOP. For example let's say the CHOP is outputting 120hz sample rate data and the [Timeline](<./Timeline.md> "Timeline") is running at 60hz. If TouchDesigner skipped cooking the last frame the [Time Slice](</index.php?title=Time_Slice&action=edit&redlink=1> "Time Slice \(page does not exist\)") size will be 2 frames long. Since the CHOPs sample rate is 120hz vs. the 60hz of the timeline, you will be asked to provide 4 samples of data per channel to fill the Time Slice. 

## See Also

[Write a CPlusPlus Plugin](<./Write_a_CPlusPlus_Plugin.md> "Write a CPlusPlus Plugin")  
[Write a CPlusPlus TOP](<./Write_a_CPlusPlus_TOP.md> "Write a CPlusPlus TOP")  
[Upgrading Custom Operators and CPlusPlus Plugins to 2022 and Newer Builds](</index.php?title=Upgrading_Custom_Operators_and_CPlusPlus_Plugins_to_2022_and_Newer_Builds&action=edit&redlink=1> "Upgrading Custom Operators and CPlusPlus Plugins to 2022 and Newer Builds \(page does not exist\)")
