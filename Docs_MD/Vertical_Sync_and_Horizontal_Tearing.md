# Perfect Playback

## Overview  
  
The word 'image' used in this article refers to the full contents of a window. It doesn't refer to the content of a single TOP, as the content of a TOP is only visible when it's drawn to a window. 

The majority of the information on this page is related to the Windows operating system, as we don't have much experience running shows on macOS devices. 

Although many shows/projects are fine with random dropped frames/stutters, some forms of content are particularly unacceptable with them. Slow, smooth motion is a common example. To obtain perfect playback a few requirements must be met. TouchDesigner needs to be generating images fast enough to provide a new one for every refresh of the output device. It must also not be running at a different rate than the output device. For a 60hz monitor, TouchDesigner must be running at 60FPS and not dropping any frames. If your output device is something else such as an SDI card, then TouchDesigner must be running at the same rate as the SDI signal (29.97Hz, for example). 

These images need to be shown in their entirety, not partially updated. For monitor output this is achieved via Vertical Sync. For SDI and other outputs types this is not an issue. 

For monitor outputs, the OS must be actually presenting the images to the screen and not silently dropping them. This is achieved through 'Exclusive' access to the desktop. More information is [here](<./Perfect_Playback.htm#Running_in_Exclusive_Access_Mode> "Perfect Playback"). 

## Perfect Playback for Monitor Outputs

These are outputs that are connected to your desktop, which you display images to using a [Window COMP](<./Window_COMP.md> "Window COMP"). 

### Quick Answer

Do all of the below: 
* Ensure your TouchDesigner is set to run at the same FPS as your monitor. Use the [Monitors DAT](<./Monitors_DAT.md> "Monitors DAT") to verify this.
  * Ensure all of your monitors are running at the same refresh rate. Use the [Monitors DAT](<./Monitors_DAT.md> "Monitors DAT") to verify this.
  * If using movie content, ensure it is authored at a FPS that is equal to or exactly divides your monitor's refresh rate.

#### Using Window COMP and the Desktop
* Combine all of your monitor outputs into a single monitor output by combining all active outputs together into a single virtual monitor, and optionally splitting those outputs across even more monitors using a [splitter device](<./Multiple_Monitors.htm#Output_to_Multiple_Monitors> "Multiple Monitors").
  * Ensure the Desktop scaling for Windows is set to 100%.
  * Ensure Vertical Sync is enabled in the [Window COMP](<./Window_COMP.md> "Window COMP").
  * Use [Perform Mode](<./Perform_Mode.md> "Perform Mode").
  * Disable Borders in your [Window COMP](<./Window_COMP.md> "Window COMP").
  * Do not have any extra [Window COMPs](<./Window_COMP.md> "Window COMP") open. Your perform window should be the only open window coming from TouchDesigner.
  * Ensure your Perform Window has gotten full-screen exclusive access to the desktop, more information [here](<./Perfect_Playback.htm#Running_in_Exclusive_Access_Mode> "Perfect Playback").


**OR**

#### Direct Display Out
* Alternatively, the issues that arise from using the Window COMP and the desktop go away when using the [Direct Display Out TOP](<./Direct_Display_Out_TOP.md> "Direct Display Out TOP"). Consider using that when possible.

### Monitor Refresh Rate and Project FPS

Use the [Monitors DAT](<./Monitors_DAT.md> "Monitors DAT") to see what refresh rate your monitors are precisely running at. The other dialogs in Windows often round the refresh rate to 60 or 30, when the actual rate is 59.94 or 29.97. Running a 59.94Hz monitor when you are targeting 60FPS will result in a regular dropped frame in your playback. 

There is an option in the [Window COMP](<./Window_COMP.md> "Window COMP") under 'V-Sync Mode' called 'FPS is Half Monitor Rate'. In builds before 2022.20000 series (pre-Vulkan), this would allow you to run your project at 30FPS on a 60Hz monitor, but ensuring every image is shown for exactly 2 refreshes. Without this option an image may be shown for 1 or 3 refreshes, which makes the content look like it is stuttering. Currently this feature is not functional in the 2022.20000+ series of builds, but we hope to re-add support when Vulkan adds support for it. 

### Movie Content FPS

If you are playing back movie content, that content needs to have been authored at that same rate, or at least a rate that perfectly divides the monitor refresh rate (30FPS content on a 60Hz monitor, for example). Running 29.97FPS video on a 60Hz monitor will result in a regular repeated frame in your content, which can look like a stutter for slow smooth motion. 

### Running in Exclusive Access Mode

Starting with Windows 8, windows on the desktop are managed by the 'Desktop Window Manager (DWM)'. This manager controls how different windows are updated on the desktop, does compositing between them etc. Unfortunately, even if TouchDesigner is providing images to the OS at the required refresh rate, the DWM may not end up displaying a image to the desktop. The only known solution to DWM randomly dropping frames is to ensure that the application has 'exclusive access' to the GPU. You can tell if TouchDesigner is obtaining exclusive access by a fullscreen flicker that occurs on the displays as it enters perform mode, or if you click on a different window than the perform window, causing the perform window to lose focus. 

There are two ways to enter exclusive mode. The first is to have a fullscreen borderless window that covers the entire desktop, and ensure the desktop is only a single monitor. If there is extra monitor connected to the GPU that isn't used as part of the output (say for controlling the OS, or running another application) this stops TouchDesigner from gaining full control of the desktop. When in this mode you can click off the window to leave exclusive mode, and click back onto it to get back into exclusive mode again. You should see a flicker each time. 

The second option is new in the [Window COMP](<./Window_COMP.md> "Window COMP"), under 'Opening Size', select 'Single Monitor Exclusive'. This allows the perform window to only target a single monitor, and other monitors can still be connected to the desktop. You should see a flicker in this mode as well, however if you click-off the window, you won't be able to re-enter exclusive mode. You'll need to leave and re-enter perform mode. 

A useful tool for seeing that your Windows's flipping/blitting behavior is is [PresentMon](<https://github.com/GameTechDev/PresentMon>)

#### Pop-up Menus

Since only one window can have exclusive access to the driver, something like a popup/dropdown menu that opens another window ontop of your UI will cause the perform window to drop out of exclusive access and cause a flicker. If this behavior is less desirable than the possible frame drops that can occur from a regular window, then you may need to make your window 1 pixel less in width or height than the desktop, to ensure it doesn't enter exclusive access mode. 

### Combine Multiple Monitors Into a Single Virtual Monitor

To obtain exclusive mode you can only be targeting a single monitor. Most projects require multiple monitor outputs though, so you'll want to combine them into a single virtual monitor using Nvidia Mosaic, Nvidia Surround or AMD EyeFinity. Refer to [Multiple Monitors](<./Multiple_Monitors.md> "Multiple Monitors") for more information. 

### Use Perform Mode and Avoid Multiple Windows

Ensure you are using [Perform Mode](<./Perform_Mode.md> "Perform Mode"), and ensure Vertical Sync is enabled on the [Window COMP](<./Window_COMP.md> "Window COMP") (altough, it is enabled by default). 

When you have multiple windows drawing at the same time, this can cut your frame rate down significantly. This GPU driver has to sync up multiple buffer swaps with a single monitor, resulting in large slowdowns. For this reason you should place all of your content in a single window. Use the Perform Panel to do this, or open a single large [Window COMP](<./Window_COMP.md> "Window COMP") with its Perform parameter turned on. 

## Perfect Playback for Non-Monitor Outputs

Examples of Non-Monitor outputs include using [Video Device Out TOP](<./Video_Device_Out_TOP.md> "Video Device Out TOP") (although it can be used to drive a monitor behind the scenes) and the [NDI Out TOP](<./NDI_Out_TOP.md> "NDI Out TOP"). 

### Quick Answer
* Ensure your TouchDesigner is set to run at the same FPS as your output device's desired FPS.
  * If using movie content, ensure it is authored at a FPS that is equal to or exactly divides your monitor's refresh rate.
  * Use [Perform Mode](<./Perform_Mode.md> "Perform Mode") with either Vertical Sync disabled, or the 'Draw Window' option disabled.

### Movie Content FPS

Refer to [Perfect_Playback#Movie_Content_FPS](<./Perfect_Playback.htm#Movie_Content_FPS> "Perfect Playback"). 

### Perform Mode Sync with your Desktop Monitor

By default the [Window COMP](<./Window_COMP.md> "Window COMP")'s settings will have the perform window attempt to vertical sync with the monitor connected to your desktop. When outputting to a different output device, you will likely be targeting a different refresh rate than what you're monitor is running at. This will cause TouchDesigner to be incorrectly syncing to the monitor's refresh rate, even if your project FPS is set to the different value that is correct for your desired output. To avoid this either turn off 'Vertical Sync' in the [Window COMP](<./Window_COMP.md> "Window COMP") for your perform window, or turn off drawing altogether using the 'Draw Window' parameter in the [Window COMP](<./Window_COMP.md> "Window COMP"). There is currently no way to avoid sync when in Designer Mode, so frame drops/performance should only be assessed when in Perform Mode. 

## See Also
