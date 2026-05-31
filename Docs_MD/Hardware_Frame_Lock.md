# Hardware Frame Lock

## What is Hardware Frame-Lock?

Hardware Frame Lock is used to synchronize the GPU with the displays or projectors attached to them. This makes it possible to maintain frame-accurate sync across displays or projectors and across multiple graphics cards. Such sync is often required when content spans multiple outputs or when using multiple GPUs and/or multiple computers with multiple GPUs. It can also be used when displays or projectors need to be synced to an external timing source. 

There are two parts that make up Hardware Frame Lock. 

### Genlock

Genlock ensures the refresh intervals of all the displays are occuring at the same time (in phase with each other). The sync signal can be generated internally by one of the Quadros in the sync group, or by an external House-Sync signal plugged into the Quadro Sync cards. Without Genlock the displays may be refreshing at different intervals, resulting in visual tearing due to some displays starting to update their content before other displays. Genlock is obtained by setting up the Quadro Sync in the Nvidia Control Panel. It will function regardless of how the TouchDesigner project is setup (as long as V-Sync is on), and doesn't require a Pro license. It can alternatively be setup using the command line [QSync Utility](<https://www.nvidia.com/en-us/drivers/qsync-utility/>). 

### Hardware Frame-Lock

Hardware Frame-Lock is enabled in the [Window COMP](<./Window_COMP.md> "Window COMP") via the 'Hardware Frame-Lock' parameter. This feature also uses the Quadro Sync cards, and ensures all of the displays only update when they are all ready to update. This avoids cases where one process has a hiccup and isn't ready to output a new frame, but other processes go ahead and update anyways, resulting in the final canvas showing two different frames at the same time. All processes will stall and wait for the lagging process when a hiccup occurs. This mode also reduces overall render performance due to the overhead it requires, so it should only be used when absolutely necessary. Lots of content can be shown across multiple displays without Frame Lock, and look great. 

#### Frame Lock Limitations

The new [Direct Display Out TOP](<./Direct_Display_Out_TOP.md> "Direct Display Out TOP") is a much more robust way to use Frame Lock, as it avoids any interaction with the Windows Desktop compositor, that the [Window COMP](<./Window_COMP.md> "Window COMP") requires. This is the recommendd way to use Frame Lock in the 2025.30000 and later builds. Frame Lock is not fault tolerance. If one machine starts dropping frames then all of them need to drop frames. There is no mechanism for a poorly behaving machine to 'catch up' if it drops frames for a bit. Due to this, it's important that your [Sync Out CHOP](<./Sync_Out_CHOP.md> "Sync Out CHOP") and [Sync In CHOPs](<./Sync_In_CHOP.md> "Sync In CHOP") have very high timeouts. More information on this later. 

##### Direct Display Out TOP

The Direct Display Out TOP allows directly interfacing with the DisplaPort outputs of your GPU, without interacting witht the Windows Desktop compositor. This allows for a much more robust workflow with Frame Lock. 

##### Window COMP

In general Frame Lock isn't robust against windows changing places, chaging modes (going to Perform and then back to editor). When working with Frame Lock, you should launch your application directly into Perform Mode with the window at positioned full-screen borderless at the correct position on the correct monitor(s). 

#### Diagnosing Frame Lock

Nvidia has a few options for Frame Lock behavior, which can be configured using configureDriver.exe. Download the configureDriver.exe utility: <https://www.nvidia.com/en-us/drivers/driver-utility/>

And select "Enable the SwapGroupPresentIndicator for OpenGL and Vulkan" to turn on this feature. 

See also [Sync In CHOP](<./Sync_In_CHOP.md> "Sync In CHOP") and [Syncing Multiple Computers](<./Syncing_Multiple_Computers.md> "Syncing Multiple Computers"). 

## Nvidia Quadro Sync

The [Nvidia Quadro Sync](<http://www.nvidia.com/object/nvidia-sync-quadro-gsync.html>) hardware solution requires the use of specific Quadro cards with the appropriate Quadro Sync card for synchronization. Each computer system that will be synced requires its own sync card which is attached to the graphics card via a ribbon cable. 

### Requirements

**Quadro Sync**
* NVIDIA Quadro Sync Card
  * NVIDIA Quadro/RTX Profressional Graphics card.

### Multiple GPUs on a Single System

This is the most simple setup which will synchronize the output of multiple GPUs and displays on a single computer. 

There are some restrictions to consider when setting a system up for sync 
* All displays connected must run on the same EDID. The simplest way to do this is ensure they are the same type, manufacturer, and model.
  * Whenever using multiple GPUs with TouchDesigner, use [GPU Affinity](<./Using_Multiple_Graphic_Cards.md> "Using Multiple Graphic Cards") for optimum performance. This requires a separate process file for each GPU.


1) Make sure all connections and power are properly setup between the graphics cards and sync card. 

2) Make sure Vertical Sync setting in the Nvidia Control Panel is set to "On" or "Use the 3D application setting". 

3) To enable Frame Lock, open the Synchronize Displays section of the Nvidia Control Panel. 
1. Set the option for **The timing server is...** to _On this System_.
  2. Check the checkboxes for all required displays in the **Select displays to lock to the server:** section.


4) In your TouchDesigner`.toe`file, confirm the following: 
* Make sure [GPU Affinity](<./Using_Multiple_Graphic_Cards.md> "Using Multiple Graphic Cards") is properly setup for each .toe file that runs on each GPU, if you are using multiple GPUs on a single PC.
  * Start your process with the [Direct Display Out TOP](<./Direct_Display_Out_TOP.md> "Direct Display Out TOP")'s not active.
  * Turn on the **Hardware Frame-Lock** parameter in the [Direct Display Out TOP](<./Direct_Display_Out_TOP.md> "Direct Display Out TOP").
  * Use [Sync Out CHOP](<./Sync_Out_CHOP.md> "Sync Out CHOP") and [Sync In CHOP](<./Sync_In_CHOP.md> "Sync In CHOP") on your server and client machines.
  * Use a channel coming from the [Sync Out CHOP](<./Sync_Out_CHOP.md> "Sync Out CHOP") into the [Sync In CHOP](<./Sync_In_CHOP.md> "Sync In CHOP") to turn on the Direct Display Out TOPs on all outputs. This is required so that the swaps occur exactly in sync on processes. When this is happening the Timeouts for both the servers and the clients in their CHOPs should be 5 seconds. This ensure that all of the outputs can be opened and are ready to be used before any process starts moving forward.
  * Once playback has started, you can turn down the Timeout on the Server to somethign lower such as 1 second, so that interaction can occur with it incase things start to break. It should stay high on the clients though, since they should never timeout.
