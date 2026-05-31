# Using Multiple Graphic Cards

## Overview

Installing multiple graphics card in your computer can have benefits in some cases, depending on your situation. The most common case is adding support for more monitors, however you need to setup you system in a very specific was to get optimal performance. 

See also [Multiple Monitors](<./Multiple_Monitors.md> "Multiple Monitors"), [Sync In CHOP](<./Sync_In_CHOP.md> "Sync In CHOP")

## Multi-GPU Mosaic and EyeFinity

Multi-GPU Mosaic (Nvidia Quadro cards) and EyeFinity (AMD cards) binds multiple GPUs together to drive a large array of outputs. Using this you can output to many more monitors, which seem like a single large monitor connected to a single virtual GPU to Windows. This is done using a bridge cable such as the SLI, NVLink or Crossfire cable to bridge the GPUs together. On Nvidia this mode was previously known as 'SLI Mosaic', but is now known as 'Premium Mosaic'. 

Although multiple GPUs are used in this mode, the extra GPUs do not add performance to the system. In fact, using this mode will actually result in worse performance than an identical output canvas on a single GPU. This is because a every GPU is duplicating the work, and simply showing the sub-portion of the final output they need from their outputs. The cost of synchronizing this duplicated work is extra cost that a single GPU configuration doesn't have. It is however useful in some situations where you need more pixels than is possible to output from a single GPU, but don't want to deal with multi-GPU/multi-process sync issues. 

If the number of pixels you want to output can be done with the 4-6 outputs your single GPU has, then a splitter such as a DataPath splitter can be used with a single GPU instead of multiple GPUs. This will perform better than using multiple GPUs. 

### Nvidia Specifics

Although Multi-GPU Mosaic uses the same bridge cable needed for SLI, it is a different mode for the GPUs. Regular SLI involves connecting multiple cards for better rendering performance, but it displays the outputs on the extra GPUs. Multi-GPU Mosaic is intended to group all of the outputs of multiple cards into a single virtual desktop, which is driven by a single virtual GPU. 

Consider using the "Nvidia Mosaic Utility" (search for the latest version on their website), to more easily setup the Mosaic outputs. 

Note that the SLI connector (also known as Quadro Link) has been removed in the latest GPUs, and the communication is just done via the PCIe bus. 

## GPU Affinity

GPU Affinity is supported by all GPUs models starting with TouchDesigner 2022.20000 series. 

GPU affinity binds a single instance of TouchDesigner (one process) to a single GPU. With multiple GPUs in the system you can have multiple instances of TouchDesigner, each bound to a unique GPU. This avoids any GPU->GPU communication and puts multiple GPUs to work. One process could be using it's 2 outputs to send data to projectors, while the 2nd GPU is connected to monitors you are using to run a 2nd TouchDesigner process that is controlling the show (sending commands and data streams to the first instance via the various networking OPs). 

It is also a good solution if you are having [ Horizontal Tearing](<./Vertical_Sync_and_Horizontal_Tearing.md> "Vertical Sync and Horizontal Tearing") by avoiding connecting outputs with different resolution/refresh rate (EDIDs) to the same graphics card. 

When using GPU Affinity, make sure that the windows from the TouchDesigner process which is bound to a particular GPU do not overlap onto the desktop space of the other GPU(s). If windows are shown on the wrong GPUs it will cause the data to get copied between GPUs which is what we are trying to avoid by using GPU affinity. This is acceptable for creating and editing your files, but during performance playback you should keep the windows only on monitors connected to the GPU that the process is bound to. 

#### Affinity Usage

GPU Affinity is used by using the`-gpuformonitor`command line option when launching TouchDesigner. This command binds the process to the GPU connected to the specified monitor. The monitors are indexed the same way they are in the [Monitors DAT](<./Monitors_DAT.md> "Monitors DAT"), which is left to right and bottom to top. You can specify any monitor that is connected to the particular GPU you want to bind to. For example if you only want run two instances of TouchDesigner, each running on the first and second graphic card respectively, and each GPU has only 1 monitor connected, you'd launch them with a .bat file like this: 
[code] 
     set APPPATH=C:\Program Files\Derivative\TouchDesigner\bin
     start "%APPPATH%" "%APPPATH%\TouchDesigner" -gpuformonitor 0 C:/Projects/Playback.toe
     start "%APPPATH%" "%APPPATH%\TouchDesigner" -gpuformonitor 1 C:/Projects/Control.toe
    
[/code]

To see if the binding is working as you expected, use the [Monitors DAT](<./Monitors_DAT.md> "Monitors DAT") and look at the 'affinity' column. 

## SLI and Crossfire

SLI (Nvidia) and Crossfire (AMD) is a feature where two graphic cards are linked together to become one virtual graphics card. When this happens only one graphic card can be connected to the monitor(s), the other card is just used for extra processing power. The idea behind this that the work will be split between the two graphic cards. 

Using this feature requires that the driver have a good idea of what is going to happen every frame, so it knows how to schedule the work. This works well for video games since they perform the same render passes each frame (shader, main, post-process, for example). So each game has it's own profile built into the driver for it's particular usage pattern. This does not work well for TouchDesigner since every .toe will have a different usage pattern. Thus, there is no profile built into the drivers for TouchDesigner for SLI/Crossfire. We haven't done much testing to see if there are any benefits to using SLI configurations with TouchDesigner. If you want to try, we suggest using the Alternate Frame Rendering method of SLI, as opposed to the Split Frame Rendering method. To see any speed improvements you would first need to ensure that your project is GPU bottle-necked. See the [Optimize](<./Optimize.md> "Optimize") article for more information on determining bottlenecks. 

## Multiple GPUs used as-is

Without GPU Affinity/SLI Mosaic all the work for processes get sent to the first GPU the system lists to TouchDesigner, and only the final images are sent across to the other GPUs to get displayed on-screen. If the system has both dedicated and integrated GPUs, then the dedicated one will be chosen of an integrated one, even if the integrated one is listed first. This is similar to Multi-GPU Mosaic/EyeFinity, but the driver is set up in a less optimal mode. This way of working can have a large performance impact on your project and is not recommended, but may be appropriate in certain situations (if the performance meets requirements). 

See also [Multiple Monitors](<./Multiple_Monitors.md> "Multiple Monitors")
