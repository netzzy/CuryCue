# Video Device In TOP

## 

Summary

The Video Device In TOP can be used to capture video from an external camera, capture card, capture dongle, IP camera, or video decoder connected to the system. Multiple devices can simultaneously stream video into TouchDesigner by using multiple Device In TOPs. HD-SDI video can be streamed into TouchDesigner through capture cards such and those from [Blackmagic Design](<./Blackmagic_Design.md> "Blackmagic Design"), [AJA](<./AJA.md> "AJA") and [Deltacast](<./Deltacast.md> "Deltacast"). 

If the device does not seem to provide a video stream but it is visible in the Cameras parameter menu, make sure no other applications are currently using the device. 

**TIP** : Create an [Info DAT](<./Info_DAT.md> "Info DAT") and point it to the Video Device In TOP to see what devices are currently attached. The [Info CHOP](<./Info_CHOP.md> "Info CHOP") gives data for analyzing the performance of Video Device In and Out TOPs. Additionally, the [Info CHOP](<./Info_CHOP.md> "Info CHOP") can be used to obtain timecode embeded into the source signal on some device, as indicated in the below list. 

Major capture devices vendors currently supported: 
* [Blackmagic Design](<./Blackmagic_Design.md> "Blackmagic Design") \- Supports Timecode. Windows and macOS.
  * [AJA](<./AJA.md> "AJA") \- Supports Timecode. Windows only and macOS.
  * [Deltacast](<./Deltacast.md> "Deltacast") \- Supports Timecode. Windows only.
  * [Bluefish444](<./Bluefish444.md> "Bluefish444") \- Windows only.


Also supported with native drivers are some models from Datapath SDI, Allied Vision, Imaging Development Systems (IDS), FLIR/Point Grey, and Ximea. 

AJA and Blackmagic Design devices support 12-bit input and output formats, including AJA’s ability to capture at a full 12-bit RGB 4:4:4. 

For Magewell HDMI-to-USB3 capture (highly recommended, no drivers, plug-and-play), see [Magewell](<http://www.magewell.com/usb-capture-hdmi>). 

**IP Cameras and USB3** include models from: 
* [Allied Vision](<https://www.alliedvision.com/en/products/cameras.html>) \- PvAPI SDK models only, not Vimba SDK. Prosilica Series and Manta cameras. Windows only.
  * [Point Grey FLIR Flycapture2 and Spinnaker](<https://www.ptgrey.com/>) \- Windows only.
  * [Imaging Development Systems (IDS)](<https://en.ids-imaging.com/>) \- TouchDesigner implements both the _uEye IDS Software Suite_ and the 'Peak' SDKs. _GigE Vision_ cameras are currently not supported.
  * [Ximea](<https://www.ximea.com/>) \- Windows only.


Only a small subset of cameras from each manufacturer has been tested in-house, however it's expected that any modern camera from the supported manufacturer should work. If any issues are encountered please contact`support@derivative.ca`. 

See also [Video Device Out TOP](<./Video_Device_Out_TOP.md> "Video Device Out TOP"). 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[videodeviceinTOP_Class](<./VideodeviceinTOP_Class.md> "VideodeviceinTOP Class")

## 

Parameters - Video In Page

Active`active`\- When set to one the TOP captures the image stream from the camera or decoder. 

Driver`driver`\- ⊞ \- Selects the library to use to interface with the cameras. 
* DirectShow (WDM)`directshow`-
* Media Foundation`mediafoundation`-
* Imaging Source - Not Supported`imagingsource`-
* DataPath (RGBEASY)`datapath`-
* Blackmagic`blackmagic`-
* Allied Vision (GigE)`alliedvisiongige`-
* Imaging Development Systems (IDS)`ids`-
* FLIR / Point Grey (FlyCapture2)`pointgreyflycapture`-
* FLIR / Point Grey (Spinnaker)`flirspinnaker`-
* AVFoundation (macOS)`avfoundation`-
* BlueFish444`bluefish444`-
* AJA`aja`-
* Ximea`ximea`-
* Deltacast`deltacast`-


Device`device`\- ⊞ \- Select which camera or decoder you want from this menu. 
* NDI Webcam Video 1`V1`-


Specify IP`specifyip`\- When using Allied Vision library allows you to specify the camera address by IP. 

IP`ip`\- The IP address used when Specify IP above is turned on. 

Options`options`\- Opens the options or control panel for the camera. NOTE: Only works when using DirectShow (WDM) cameras. 

Deinterlace`deinterlace`\- ⊞ \- Sets which fields to show. 
* Off`off`\- Shows the entire frame as one image without any deinterlacing.
* Even`even`\- Shows Even fields only. Line 1 is the top line of the frame. This will show lines 2, 4, 6, 8 etc, starting at the second from top line, and ending at the very bottom line.
* Odd`odd`\- Shows Odd fields only. Line 1 is the top line of the frame, so this will show lines 1, 3, 5, 7 etc, starting at the very top line.
* Bob (Split)`bob`\- Alternatively shows the even then odd fields, resulting in twice the framerate being shown, and removing the interlacing artifacts. Which field is shown first is controlled by the 'Field Precedence' parameter.


Field Precedence`precedence`\- ⊞ \- When using Bob (Split) deinterlacing, this selects which field is shown first for each frame. 
* Even`even`\- Shows the Even lines first, then the Odd ones. Line 1 is the top line of the frame. This will show lines 2, 4, 6, 8 etc first, then the next cook it will shows lines 1, 3, 5, 7 etc.
* Odd`odd`\- Shows the Odd lines first, then the Event ones. Line 1 is the top line of the frame. This will show lines 1, 3, 5, 7 etc first, then the next cook it will shows lines 2, 4, 6, 8 etc.


TV Channel`channel`\- Selects the TV channel if a TV tuner is used as the video input. 

Signal Format`signalformat`\- The signal format to capture input at. This is the resolution and the frame rate, as well as if the frames are progressive or interlaced. Note that when using an interlaced format, the rate refers to fields per second. 

Quad Link`quadlink`\- Used for cards that support quad-link formats. Quad-link esstenially takes 4 inputs and creates one single larger input out of them, for example 4 1080p inputs become a single 4K input. 

Input Pixel Format`inputpixelformat`\- ⊞ \- Some capture devices support pixel formats other than 8-bit. For supported devices (Blackmagic Design) this will make the node attempt to use that capability. 
* 8-bit`fixed8`\- 8-bit per channel precision.
* 10-bit`fixed10`\- 10-bit per channel precision. The texture pixel format will be set to RGB10A2.
* 16-bit`fixed16`\- 16-bit per channel precision. The texture pixel format will be set to RGBA16-Fixed.
* 12-bit`fixed12`-


Input Color Space`inputcolorspace`\- ⊞ \- Controls what color space the input data will be treated as. It will be converted to the Working [Color Space](<./Color_Space.md> "Color Space") when uploaded to the GPU. 
* Automatic`automatic`\- Automatically try to determine the input's color space based on color space metadata available from the input, if any. If no color space can be determined, it is assumed to be sRGB.
* sRGB`srgb`\- [sRGB](<https://en.wikipedia.org/wiki/SRGB>) color space, with sRGB transfer function. Considered an SDR color space with respect to Reference White.
* sRGB - Linear`srgblinear`\- [sRGB](<https://en.wikipedia.org/wiki/SRGB>) color space, with linear transfer function. Considered an SDR color space with respect to Reference White.
* Rec.601 (NTSC)`rec601ntsc`\- [Rec.601](<https://en.wikipedia.org/wiki/Rec._601>) with NTSC primaries color space, with Rec.601 transfer function. Considered an SDR color space with respect to Reference White.
* Rec.709`rec709`\- [Rec.709](<https://en.wikipedia.org/wiki/Rec._709>) color space, with Rec.709 (same as Rec.2020) transfer function. Considered an SDR color space with respect to Reference White.
* Rec.2020`rec2020`\- [Rec.2020](<https://en.wikipedia.org/wiki/Rec._2020>) color space, with Rec.2020 (same as Rec.709) transfer function. Considered an HDR color space with respect to Reference White.
* Rec.2020 ST2084PQ`rec2020st2084pq`\- [Rec.2020](<https://en.wikipedia.org/wiki/Rec._2020>) color space, with [Perceptual Quantizer](<https://en.wikipedia.org/wiki/Perceptual_quantizer>) transfer function. Considered an HDR color space with respect to Reference White.
* Rec.2020 HLG`rec2020hlg`\- [Rec.2020](<https://en.wikipedia.org/wiki/Rec._2020>) color space, with [Hybrid Log Gamma](<https://en.wikipedia.org/wiki/Hybrid_log%E2%80%93gamma>) transfer function. Considered an HDR color space with respect to Reference White.
* DCI-P3`dcip3`\- [DCI-P3](<https://en.wikipedia.org/wiki/DCI-P3>) color space, with D65 white point and 2.6 gamma transfer function. Considered an HDR color space with respect to Reference White.
* DCI-P3 (D60)`dcip3d60`\- [DCI-P3 "D60 sim"](<https://en.wikipedia.org/wiki/DCI-P3>) color space, with D60 white point, and 2.6 gamma transfer function. Considered an HDR color space with respect to Reference White.
* Display-P3 (D65)`displayp3d65`\- [Display-P3](<https://en.wikipedia.org/wiki/DCI-P3>) color space, with D65 white point, and sRGB gamma transfer function. Considered an HDR color space with respect to Reference White.
* Display-P3 (D65) - Linear`displayp3d65linear`\- [Display-P3](<https://en.wikipedia.org/wiki/DCI-P3>) color space, with D65 white point, and linear transfer function. Considered an HDR color space with respect to Reference White.
* ACES2065-1`aces2065-1`\- [ACES 2065-1](<https://en.wikipedia.org/wiki/Academy_Color_Encoding_System>) (also known as ACES AP0) color space, with a linear gamma transfer function. Considered an HDR color space with respect to Reference White.
* ACEScg`acescg`\- [ACEScg](<https://en.wikipedia.org/wiki/Academy_Color_Encoding_System>) (also known as ACES AP1) color space, with a linear gamma transfer function. Considered an HDR color space with respect to Reference White.
* ACESproxy`acesproxy`\- [ACESproxy](<https://en.wikipedia.org/wiki/Academy_Color_Encoding_System>) color space, which has a log transfer function. Considered an HDR color space with respect to Reference White.
* Passthrough`passthrough`\- When selected, the color values will be used as-is in the operation, without any modification or attempt to convert them into the Working Color Space.


Input Reference White`inputreferencewhite`\- ⊞ \- When converting the input color values to the Working Color Space, this controls how they should be treated with respect to [Reference White](<./Color_Space.htm#Reference_White> "Color Space"). If the Working Color Space is the same Reference White, then no adjustment is done. If they are different, then the Reference White level (brightness) of the colors will be adjusted to the range expected by the Working Color Space. For example if the project is set to have a SDR Reference White of 120 nits, and the HDR Reference White is 80 nits, then a color of (1, 1, 1), which is 120 nits in the SDR color space, will be converted to be (1.5, 1.5, 1.5), which is 120 nits still in the HDR Working Color Space. 
* Default For Color Space`default`\- Will use either the SDR or the HDR Reference White, based on the color space detected/selected.
* Standard (SDR)`sdr`\- Will treat the Input Color Space as SDR for it's reference white value.
* High (HDR)`hdr`\- Will treat the Input Color Space as HDR for it's reference white value.


Transfer Mode`transfermode`\- ⊞ \- Controls how the frames are transferred from the input device to CPU memory, and how they are transferred from CPU memory to the GPU. 
* Automatic`automatic`\- Will choose the best transfer mode for the components installed on the computer. In general this will be 'Pre-Upload'.
* Pre-Upload`preupload`\- Upload the frames to the GPU as they arrived. This ensures the data is already in GPU memory when the GPU wants to process it.
* On-Demand`ondemand`\- Only upload frames to the GPU if the TOP is going to display them for that cook. This reduces PCIe bandwidth between the GPU and CPU memory in cases where the TOP is showing less frames than what the input device is capturing. However this means the GPU may stall waiting for that frame to be uploaded.
* On-Demand, Sync to Frame Input`ondemandsync`\- This mode is currently only available for [AJA](<./AJA.md> "AJA") devices. This causes the whole TouchDesigner process to stall until right after a frame arrives on this input. Then the process will start executing and use that input frame for this nodes cook. This removes any latency from the capture input, but can result in worse performance. Real-time should turned off for the TouchDesigner process at the top of the UI, and only one node should be set to this mode in a single process.


Memory Mode`memorymode`\- ⊞ \- Controls the memory type used to transfer data between the capture card and the GPU. 
* Automatic`automatic`\- Will choose the best memory mode for the transfer. This will be 'Pinned' for capture cards that support it, and 'Regular' if not.
* Pinned`pinned`\- Pinned memory allows data to be transferred in 2 copies instead of three. Capture->Pinned CPU Memory, Pinned CPU Memory->GPU Memory.
* Regular`regular`\- The regular memory mode means 3 copies are required. Capture->Capture Writable Memory, Capture Writable Memory->GPU Readable Memory, GPU Readable Memory->GPU Memory.


Sync Inputs`syncinputs`\- Enabling syncing of multiple Video Device In TOPs. Syncing allows multiple nodes using multiple inputs and capture cards on a single system to ensure they are outputting frames in sync. Without this each node will be free running and will possible be outputting frames that came it at different times due to internal queuing. It's important the input sources are GenLocked to ensure all of their data arrives to all of the inputs at the same time, otherwise syncing will not work. This feature is currently supported for Blackmagic, DataPath, Deltacast and BlueFish devices. 

Sync Group Index`syncgroupindex`\- There can be multiple sync groups active in a .toe file. Nodes will only sync to other nodes that are part of the same sync group. 

Max Sync Offset (ms)`maxsyncoffset`\- Specified in milliseconds. The maximum difference in time two image could have arrived at be considered in-sync. Images that arrive at times more different than this offset will be considered to be part of different 'frame'. 

Sync Timeout (ms)`synctimeout`\- How much time to wait for all frames in a sync group to become available before giving up trying to sync. Expressed in milliseconds. If this timeout elapses when waiting for a frame from one or more sources in the sync group, all of the nodes in the sync group will keep their current image and not output a new image, even if some new images arrived on some of the inputs. 

Reset Stats`resetstats`\- A pulse to reset the statistics in an attached [Info CHOP](<./Info_CHOP.md> "Info CHOP"). 

## 

Parameters - Options Page

Currently all of these options are only available for [Ximea](</index.php?title=Ximea&action=edit&redlink=1> "Ximea \(page does not exist\)") cameras. 

Preset`preset`\- ⊞ \- 
* Externally Configured`externallyconfigured`-
* Custom`custom`-


Auto Gain/Exposure`autoge`\- 

Auto Gain/Exposure Bias`autogebias`\- 

Auto Gain/Exposure Level`autogelevel`\- 

Max Gain`maxgain`\- 

Max Exposure (ms)`maxexposure`\- 

Gain`gain`\- 

Exposure (ms)`exposure`\- 

Chromaticity Gamma`cgamma`\- 

Luminosity Gamma`lgamma`\- 

Limit FPS`limitfps`\- 

FPS`limitedfps`\- 

Capture`capture`\- 

Capture Pulse`capturepulse`\- 

Auto White-Balance`autowb`\- 

White-Balance Coeffs`wbcoeffs`\- ⊞ \- 
* White-Balance Coeffs`wbcoeffsr`-
* White-Balance Coeffs`wbcoeffsg`-
* White-Balance Coeffs`wbcoeffsb`-


Custom Bandwidth`custombandwidth`\- ⊞ \- 
* Default`default`-
* On`on`-
* Off`off`-


Bandwidth Limit (Mb/s)`bandwidthlimit`\- 

Camera Bit Depth`camerabitdepth`\- ⊞ \- 
* Automatic`automatic`-
* 8-Bit`8bit`-
* 10-Bit`10bit`-
* 12-Bit`12bit`-


GPU Demosaic`gpudemosaic`\- 

## 

Parameters - Common Page

Output Resolution`outputresolution`\- ⊞ \- quickly change the resolution of the TOP's data. 
* Use Input`useinput`\- Uses the input's resolution
* Eighth`eighth`\- Multiply the input's resolution by that amount.
* Quarter`quarter`\- Multiply the input's resolution by that amount.
* Half`half`\- Multiply the input's resolution by that amount.
* 2X`2x`\- Multiply the input's resolution by that amount.
* 4X`4x`\- Multiply the input's resolution by that amount.
* 8X`8x`\- Multiply the input's resolution by that amount.
* Fit Resolution`fit`\- Grow or shrink the input resolution to fit this resolution, while keeping the aspect ratio the same.
* Limit Resolution`limit`\- Limit the input resolution to be not larger than this resolution, while keeping the aspect ratio the same.
* Custom Resolution`custom`\- Directly control the width and height.


Resolution`resolution`\- ⊞ \- Enabled only when the Resolution parameter is set to Custom Resolution. Some Generators like Constant and Ramp do not use inputs and only use this field to determine their size. The drop down menu on the right provides some commonly used resolutions. 
* W`resolutionw`-
* H`resolutionh`-


Resolution Menu`resmenu`\- A drop-down menu with some commonly used resolutions. 

Use Global Res Multiplier`resmult`\- Uses the Global Resolution Multiplier found in **Edit >Preferences>TOPs**. This multiplies all the TOPs resolutions by the set amount. This is handy when working on computers with different hardware specifications. If a project is designed on a desktop workstation with lots of graphics memory, a user on a laptop with only 64MB VRAM can set the Global Resolution Multiplier to a value of half or quarter so it runs at an acceptable speed. By checking this checkbox on, this TOP is affected by the global multiplier. 

Output Aspect`outputaspect`\- ⊞ \- Sets the image aspect ratio allowing any textures to be viewed in any size. Watch for unexpected results when compositing TOPs with different aspect ratios. (You can define images with non-square pixels using xres, yres, aspectx, aspecty where xres/yres != aspectx/aspecty.) 
* Use Input`useinput`\- Uses the input's aspect ratio.
* Resolution`resolution`\- Uses the aspect of the image's defined resolution (ie 512x256 would be 2:1), whereby each pixel is square.
* Custom Aspect`custom`\- Lets you explicitly define a custom aspect ratio in the Aspect parameter below.


Aspect`aspect`\- ⊞ \- Use when Output Aspect parameter is set to Custom Aspect. 
* Aspect1`aspect1`-
* Aspect2`aspect2`-


Aspect Menu`armenu`\- A drop-down menu with some commonly used aspect ratios. 

Input Smoothness`inputfiltertype`\- ⊞ \- This controls pixel filtering on the input image of the TOP. 
* Nearest Pixel`nearest`\- Uses nearest pixel or accurate image representation. Images will look jaggy when viewing at any zoom level other than Native Resolution.
* Interpolate Pixels`linear`\- Uses linear filtering between pixels. This is how you get TOP images in viewers to look good at various zoom levels, especially useful when using any Fill Viewer setting other than Native Resolution.
* Mipmap Pixels`mipmap`\- Uses [ mipmap](<./Mipmapping.md> "Mipmapping") filtering when scaling images. This can be used to reduce artifacts and sparkling in moving/scaling images that have lots of detail.


Fill Viewer`fillmode`\- ⊞ \- Determine how the TOP image is displayed in the viewer. 

**NOTE:** To get an understanding of how TOPs work with images, you will want to set this to **Native Resolution** as you lay down TOPs when starting out. This will let you see what is actually happening without any automatic viewer resizing. 
* Use Input`useinput`\- Uses the same Fill Viewer settings as it's input.
* Fill`fill`\- Stretches the image to fit the edges of the viewer.
* Fit Horizontal`width`\- Stretches image to fit viewer horizontally.
* Fit Vertical`height`\- Stretches image to fit viewer vertically.
* Fit Best`best`\- Stretches or squashes image so no part of image is cropped.
* Fit Outside`outside`\- Stretches or squashes image so image fills viewer while constraining it's proportions. This often leads to part of image getting cropped by viewer.
* Native Resolution`nativeres`\- Displays the native resolution of the image in the viewer.


Viewer Smoothness`filtertype`\- ⊞ \- This controls pixel filtering in the viewers. 
* Nearest Pixel`nearest`\- Uses nearest pixel or accurate image representation. Images will look jaggy when viewing at any zoom level other than Native Resolution.
* Interpolate Pixels`linear`\- Uses linear filtering between pixels. Use this to get TOP images in viewers to look good at various zoom levels, especially useful when using any Fill Viewer setting other than Native Resolution.
* Mipmap Pixels`mipmap`\- Uses [ mipmap](<./Mipmapping.md> "Mipmapping") filtering when scaling images. This can be used to reduce artifacts and sparkling in moving/scaling images that have lots of detail. When the input is 32-bit float format, only nearest filtering will be used (regardless of what is selected).


Passes`npasses`\- Duplicates the operation of the TOP the specified number of times. For every pass after the first it takes the result of the previous pass and replaces the node's first input with the result of the previous pass. One exception to this is the [GLSL TOP](<./GLSL_TOP.md> "GLSL TOP") when using compute shaders, where the input will continue to be the connected TOP's image. 

Channel Mask`chanmask`\- Allows you to choose which channels (R, G, B, or A) the TOP will operate on. All channels are selected by default. 

Pixel Format`format`\- ⊞ \- Format used to store data for each channel in the image (ie. R, G, B, and A). Refer to [Pixel Formats](<./Pixel_Formats.md> "Pixel Formats") for more information. 
* Use Input`useinput`\- Uses the input's pixel format.
* 8-bit fixed (RGBA)`rgba8fixed`\- Uses 8-bit integer values for each channel.
* sRGB 8-bit fixed (RGBA)`srgba8fixed`\- Uses 8-bit integer values for each channel and stores color in sRGB colorspace. Note that this does **not** apply an sRGB curve to the pixel values, it only stores them using an sRGB curve. This means more data is used for the darker values and less for the brighter values. When the values are read downstream they will be converted back to linear. For more information refer to [sRGB](<./SRGB.md> "SRGB").
* 16-bit float (RGBA)`rgba16float`\- Uses 16-bits per color channel, 64-bits per pixel.
* 32-bit float (RGBA)`rgba32float`\- Uses 32-bits per color channel, 128-bits per pixels.
* 10-bit RGB, 2-bit Alpha, fixed (RGBA)`rgb10a2fixed`\- Uses 10-bits per color channel and 2-bits for alpha, 32-bits total per pixel.
* 16-bit fixed (RGBA)`rgba16fixed`\- Uses 16-bits per color channel, 64-bits total per pixel.
* 11-bit float (RGB), Positive Values Only`rgba11float`\- A RGB floating point format that has 11 bits for the Red and Green channels, and 10-bits for the Blue Channel, 32-bits total per pixel (therefore the same memory usage as 8-bit RGBA). The Alpha channel in this format will always be 1. Values can go above one, but can't be negative. ie. the range is [0, infinite).
* 16-bit float (RGB)`rgb16float`-
* 32-bit float (RGB)`rgb32float`-
* 8-bit fixed (Mono)`mono8fixed`\- Single channel, where RGB will all have the same value, and Alpha will be 1.0. 8-bits per pixel.
* 16-bit fixed (Mono)`mono16fixed`\- Single channel, where RGB will all have the same value, and Alpha will be 1.0. 16-bits per pixel.
* 16-bit float (Mono)`mono16float`\- Single channel, where RGB will all have the same value, and Alpha will be 1.0. 16-bits per pixel.
* 32-bit float (Mono)`mono32float`\- Single channel, where RGB will all have the same value, and Alpha will be 1.0. 32-bits per pixel.
* 8-bit fixed (RG)`rg8fixed`\- A 2 channel format, R and G have values, while B is 0 always and Alpha is 1.0. 8-bits per channel, 16-bits total per pixel.
* 16-bit fixed (RG)`rg16fixed`\- A 2 channel format, R and G have values, while B is 0 always and Alpha is 1.0. 16-bits per channel, 32-bits total per pixel.
* 16-bit float (RG)`rg16float`\- A 2 channel format, R and G have values, while B is 0 always and Alpha is 1.0. 16-bits per channel, 32-bits total per pixel.
* 32-bit float (RG)`rg32float`\- A 2 channel format, R and G have values, while B is 0 always and Alpha is 1.0. 32-bits per channel, 64-bits total per pixel.
* 8-bit fixed (A)`a8fixed`\- An Alpha only format that has 8-bits per channel, 8-bits per pixel.
* 16-bit fixed (A)`a16fixed`\- An Alpha only format that has 16-bits per channel, 16-bits per pixel.
* 16-bit float (A)`a16float`\- An Alpha only format that has 16-bits per channel, 16-bits per pixel.
* 32-bit float (A)`a32float`\- An Alpha only format that has 32-bits per channel, 32-bits per pixel.
* 8-bit fixed (Mono+Alpha)`monoalpha8fixed`\- A 2 channel format, one value for RGB and one value for Alpha. 8-bits per channel, 16-bits per pixel.
* 16-bit fixed (Mono+Alpha)`monoalpha16fixed`\- A 2 channel format, one value for RGB and one value for Alpha. 16-bits per channel, 32-bits per pixel.
* 16-bit float (Mono+Alpha)`monoalpha16float`\- A 2 channel format, one value for RGB and one value for Alpha. 16-bits per channel, 32-bits per pixel.
* 32-bit float (Mono+Alpha)`monoalpha32float`\- A 2 channel format, one value for RGB and one value for Alpha. 32-bits per channel, 64-bits per pixel.


Parameter Color Space`parmcolorspace`\- ⊞ \- Controls how all color parameters on this node are interpreted. The color values as treated as being in the selected color space, and are converted to the Working [Color Space](<./Color_Space.md> "Color Space") before they are used as part of the node's operation. Note that this does not change the color space of the node itself, as that is always in the Working Color Space. 
* sRGB`srgb`\- [sRGB](<https://en.wikipedia.org/wiki/SRGB>) color space, with sRGB transfer function. Considered an SDR color space with respect to Reference White.
* sRGB - Linear`srgblinear`\- [sRGB](<https://en.wikipedia.org/wiki/SRGB>) color space, with linear transfer function. Considered an SDR color space with respect to Reference White.
* Rec.601 (NTSC)`rec601ntsc`\- [Rec.601](<https://en.wikipedia.org/wiki/Rec._601>) with NTSC primaries color space, with Rec.601 transfer function. Considered an SDR color space with respect to Reference White.
* Rec.709`rec709`\- [Rec.709](<https://en.wikipedia.org/wiki/Rec._709>) color space, with Rec.709 (same as Rec.2020) transfer function. Considered an SDR color space with respect to Reference White.
* Rec.2020`rec2020`\- [Rec.2020](<https://en.wikipedia.org/wiki/Rec._2020>) color space, with Rec.2020 (same as Rec.709) transfer function. Considered an HDR color space with respect to Reference White.
* DCI-P3`dcip3`\- [DCI-P3](<https://en.wikipedia.org/wiki/DCI-P3>) color space, with D65 white point and 2.6 gamma transfer function. Considered an HDR color space with respect to Reference White.
* DCI-P3 (D60)`dcip3d60`\- [DCI-P3 "D60 sim"](<https://en.wikipedia.org/wiki/DCI-P3>) color space, with D60 white point, and 2.6 gamma transfer function. Considered an HDR color space with respect to Reference White.
* Display-P3 (D65)`displayp3d65`\- [Display-P3](<https://en.wikipedia.org/wiki/DCI-P3>) color space, with D65 white point, and sRGB gamma transfer function. Considered an HDR color space with respect to Reference White.
* ACES2065-1`aces2065-1`\- [ACES 2065-1](<https://en.wikipedia.org/wiki/Academy_Color_Encoding_System>) (also known as ACES AP0) color space, with a linear gamma transfer function. Considered an HDR color space with respect to Reference White.
* ACEScg`acescg`\- [ACEScg](<https://en.wikipedia.org/wiki/Academy_Color_Encoding_System>) (also known as ACES AP1) color space, with a linear gamma transfer function. Considered an HDR color space with respect to Reference White.
* Passthrough`passthrough`\- When selected, the color values will be used as-is in the operation, without any modification or attempt to convert them into the Working Color Space.


Parameter Reference White`parmreferencewhite`\- ⊞ \- When converting a parameter color value to the Working Color Space, this controls how it should be treated with respect to [Reference White](<./Color_Space.htm#Reference_White> "Color Space"). If the Working Color Space is the same Reference White, then no adjustment is done. If they are different, then the Reference White level (brightness) of this color will be adjusted to the range expected by the Working Color Space. For example if the project is set to have a SDR Reference White of 120 nits, and the HDR Reference White is 80 nits, then a color of (1, 1, 1), which is 120 nits in the SDR color space, will be converted to be (1.5, 1.5, 1.5), which is 120 nits still in the HDR Working Color Space. 
* Default For Color Space`default`\- Will use either the SDR or the HDR Reference White, based on the color space selected.
* Use Parent Panel`useparent`\- Will use the Reference White that the parent panel has selected. If the top-level panel also has 'Use Parent' selected, then 'UI Reference White' will be used.
* Standard (SDR)`sdr`\- Will treat the Parameter Color Space as SDR for it's reference white value.
* High (HDR)`hdr`\- Will treat the Parameter Color Space as HDR for it's reference white value.
* UI`ui`\- Will treat the Parameter Color Space as UI for it's reference white value. This uses the 'UI Reference White Nits' value for it's brightness.

## 

Info CHOP Channels

Extra Information for the Video Device In TOP can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). 

### 

Specific Video Device In TOP Info Channels
* connected \- 1 if the node is successfully connected to the device, 0 if not. This does not necessarily mean there is valid input coming to the device.
* sync_timeouts \- When using the 'Sync Group' feature, this counts how many times the group failed to all provide a frame with similar enough timestamps within the timeout period.
* last_sync_wait \- How long the node had to wait from the time it was ready for a new frame until all the inputs provided valid frames for a synced output.
* odd_field \- When de-interlacing an interlaced input, this will be 1 when the odd field is being shown and 0 when the even field is being shown.
* capture_fps \- The calculated number of frames per second that are being captured by the device. This does **not** map directly to the signal format rate. It won't show 59.97 for example. This is simply a count of how many frames were captured in the last 1000ms.
* capture_total \- The total number of frames that have been captured this capture began.
* frames_repeated \- How many times the node has shown the same frame more than once. It does not currently correct for if the repeats are expected, such as when capturing a 30hz signal but TouchDesigner is running at 60fps. In that case the channel will keep increasing since each captured frame will be shown twice.
* frames_dropped \- This counts how many frames were captured by the card, but never consumed by TouchDesigner's reading thread. This occurs if the capture is running faster than TouchDesigner is able to consume frames.
* frames_skipped \- This counts how many frames were consumed by TouchDesigner's reading thread, but never consumed by the node itself. This can occur if TouchDesigner isn't running at full frame rate.
* connection_changes \- Counts connection changes, not supported by all devices.
* temperature \- On supported devices, outputs the temperature of the device in celsius. Will be a very negative number for devices that don't support it.
* signal_fps \- The actual signal format FPS of the input signal. 0 if unknown.
* rgb_input \- Will be 1 if the input is detected as an RGB (such as RGB 4:4:4) format. 0 if it is a YUV/YCbCr based. -1 if it is unknown or not supported by the the library.
* frame_queue_length \- The number of receieved frames queued inside TouchDesigner.
* frame_hw_queue_length \- The number of frames still queued on the device that TouchDesigner has not yet read.
* last_dma_copy_time \- The number of milliseconds it took to copy the last frame from the device to the CPU. -1 if this is not measured.
* frame_timestamp \- Time in seconds of the last frame displayed. -1 if this is not provided by the device.

### 

Common TOP Info Channels
* resx \- Horizontal resolution of the TOP in pixels.
* resy \- Vertical resolution of the TOP in pixels.
* aspectx \- Horizontal aspect of the TOP.
* aspecty \- Vertical aspect of the TOP.
* depth \- Depth of 2D or 3D array if this TOP contains a 2D or 3D texture array.
* gpu_memory_used \- Total amount of texture memory used by this TOP.

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


  
TouchDesigner Build: Latest\nwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditormw-rollbackmw-revertedmw-manual-revert2025.300002022.241402021.100002020.200002018.28070before 2018.28070

TOPs   
---  
[Add ](<./Add_TOP.md> "Add TOP")• [Analyze ](<./Analyze_TOP.md> "Analyze TOP")• [Anti Alias ](<./Anti_Alias_TOP.md> "Anti Alias TOP")• [Blob Track ](<./Blob_Track_TOP.md> "Blob Track TOP")• [Bloom ](<./Bloom_TOP.md> "Bloom TOP")• [Blur ](<./Blur_TOP.md> "Blur TOP")• [Cache Select ](<./Cache_Select_TOP.md> "Cache Select TOP")• [Cache ](<./Cache_TOP.md> "Cache TOP")• [Channel Mix ](<./Channel_Mix_TOP.md> "Channel Mix TOP")• [CHOP to ](<./CHOP_to_TOP.md> "CHOP to TOP")• [Chroma Key ](<./Chroma_Key_TOP.md> "Chroma Key TOP")• [Circle ](<./Circle_TOP.md> "Circle TOP")• [Composite ](<./Composite_TOP.md> "Composite TOP")• [Constant ](<./Constant_TOP.md> "Constant TOP")• [Convolve ](<./Convolve_TOP.md> "Convolve TOP")• [Corner Pin ](<./Corner_Pin_TOP.md> "Corner Pin TOP")• [CPlusPlus ](<./CPlusPlus_TOP.md> "CPlusPlus TOP")• [Crop ](<./Crop_TOP.md> "Crop TOP")• [Cross ](<./Cross_TOP.md> "Cross TOP")• [Cube Map ](<./Cube_Map_TOP.md> "Cube Map TOP")• [Depth ](<./Depth_TOP.md> "Depth TOP")• [Difference ](<./Difference_TOP.md> "Difference TOP")• [Direct Display Out ](<./Direct_Display_Out_TOP.md> "Direct Display Out TOP")• [DirectX In ](<./DirectX_In_TOP.md> "DirectX In TOP")• [DirectX Out ](<./DirectX_Out_TOP.md> "DirectX Out TOP")• [Displace ](<./Displace_TOP.md> "Displace TOP")• [Edge ](<./Edge_TOP.md> "Edge TOP")• [Emboss ](<./Emboss_TOP.md> "Emboss TOP")• [Feedback ](<./Feedback_TOP.md> "Feedback TOP")• [Fit ](<./Fit_TOP.md> "Fit TOP")• [Flip ](<./Flip_TOP.md> "Flip TOP")• [Function ](<./Function_TOP.md> "Function TOP")• [GLSL Multi ](<./GLSL_Multi_TOP.md> "GLSL Multi TOP")• [GLSL ](<./GLSL_TOP.md> "GLSL TOP")• [HSV Adjust ](<./HSV_Adjust_TOP.md> "HSV Adjust TOP")• [HSV to RGB ](<./HSV_to_RGB_TOP.md> "HSV to RGB TOP")• [Import Select ](<./Import_Select_TOP.md> "Import Select TOP")• [In ](<./In_TOP.md> "In TOP")• [Inside ](<./Inside_TOP.md> "Inside TOP")• [Introduction To s Vid ](<./Introduction_To_TOPs_Vid.md> "Introduction To TOPs Vid")• [Kinect Azure Select ](<./Kinect_Azure_Select_TOP.md> "Kinect Azure Select TOP")• [Kinect Azure ](<./Kinect_Azure_TOP.md> "Kinect Azure TOP")• [Kinect ](<./Kinect_TOP.md> "Kinect TOP")• [Layer Mix ](<./Layer_Mix_TOP.md> "Layer Mix TOP")• [Layer ](<./Layer_TOP.md> "Layer TOP")• [Layout ](<./Layout_TOP.md> "Layout TOP")• [Leap Motion ](<./Leap_Motion_TOP.md> "Leap Motion TOP")• [Lens Distort ](<./Lens_Distort_TOP.md> "Lens Distort TOP")• [Level ](<./Level_TOP.md> "Level TOP")• [Limit ](<./Limit_TOP.md> "Limit TOP")• [Lookup ](<./Lookup_TOP.md> "Lookup TOP")• [Luma Blur ](<./Luma_Blur_TOP.md> "Luma Blur TOP")• [Luma Level ](<./Luma_Level_TOP.md> "Luma Level TOP")• [Math ](<./Math_TOP.md> "Math TOP")• [Matte ](<./Matte_TOP.md> "Matte TOP")• [Mirror ](<./Mirror_TOP.md> "Mirror TOP")• [Monochrome ](<./Monochrome_TOP.md> "Monochrome TOP")• [MoSys ](<./MoSys_TOP.md> "MoSys TOP")• [Movie File In ](<./Movie_File_In_TOP.md> "Movie File In TOP")• [Movie File Out ](<./Movie_File_Out_TOP.md> "Movie File Out TOP")• [MPCDI ](<./MPCDI_TOP.md> "MPCDI TOP")• [Multiply ](<./Multiply_TOP.md> "Multiply TOP")• [Ncam ](<./Ncam_TOP.md> "Ncam TOP")• [NDI In ](<./NDI_In_TOP.md> "NDI In TOP")• [NDI Out ](<./NDI_Out_TOP.md> "NDI Out TOP")• [Noise ](<./Noise_TOP.md> "Noise TOP")• [Normal Map ](<./Normal_Map_TOP.md> "Normal Map TOP")• [Notch ](<./Notch_TOP.md> "Notch TOP")• [Null ](<./Null_TOP.md> "Null TOP")• [NVIDIA Background ](<./NVIDIA_Background_TOP.md> "NVIDIA Background TOP")• [NVIDIA Denoise ](<./NVIDIA_Denoise_TOP.md> "NVIDIA Denoise TOP")• [NVIDIA Flex ](<./NVIDIA_Flex_TOP.md> "NVIDIA Flex TOP")• [NVIDIA Flow ](<./NVIDIA_Flow_TOP.md> "NVIDIA Flow TOP")• [NVIDIA Upscaler ](<./NVIDIA_Upscaler_TOP.md> "NVIDIA Upscaler TOP")• [OAK Select ](<./OAK_Select_TOP.md> "OAK Select TOP")• [Oculus Rift ](<./Oculus_Rift_TOP.md> "Oculus Rift TOP")• [OP Viewer ](<./OP_Viewer_TOP.md> "OP Viewer TOP")• [OpenColorIO ](<./OpenColorIO_TOP.md> "OpenColorIO TOP")• [OpenVR ](<./OpenVR_TOP.md> "OpenVR TOP")• [Optical Flow ](<./Optical_Flow_TOP.md> "Optical Flow TOP")• [Orbbec Select ](<./Orbbec_Select_TOP.md> "Orbbec Select TOP")• [Orbbec ](<./Orbbec_TOP.md> "Orbbec TOP")• [Ouster Select ](<./Ouster_Select_TOP.md> "Ouster Select TOP")• [Ouster ](<./Ouster_TOP.md> "Ouster TOP")• [Out ](<./Out_TOP.md> "Out TOP")• [Outside ](<./Outside_TOP.md> "Outside TOP")• [Over ](<./Over_TOP.md> "Over TOP")• [Pack ](<./Pack_TOP.md> "Pack TOP")• [Photoshop In ](<./Photoshop_In_TOP.md> "Photoshop In TOP")• [Point File In ](<./Point_File_In_TOP.md> "Point File In TOP")• [Point File Select ](<./Point_File_Select_TOP.md> "Point File Select TOP")• [Point Transform ](<./Point_Transform_TOP.md> "Point Transform TOP")• [POP to ](<./POP_to_TOP.md> "POP to TOP")• [PreFilter Map ](<./PreFilter_Map_TOP.md> "PreFilter Map TOP")• [Projection ](<./Projection_TOP.md> "Projection TOP")• [Ramp ](<./Ramp_TOP.md> "Ramp TOP")• [RealSense ](<./RealSense_TOP.md> "RealSense TOP")• [Rectangle ](<./Rectangle_TOP.md> "Rectangle TOP")• [Remap ](<./Remap_TOP.md> "Remap TOP")• [Render Pass ](<./Render_Pass_TOP.md> "Render Pass TOP")• [Render Select ](<./Render_Select_TOP.md> "Render Select TOP")• [Render Simple ](<./Render_Simple_TOP.md> "Render Simple TOP")• [Render ](<./Render_TOP.md> "Render TOP")• [RenderStream In ](<./RenderStream_In_TOP.md> "RenderStream In TOP")• [RenderStream Out ](<./RenderStream_Out_TOP.md> "RenderStream Out TOP")• [Reorder ](<./Reorder_TOP.md> "Reorder TOP")• [Resolution ](<./Resolution_TOP.md> "Resolution TOP")• [RGB Key ](<./RGB_Key_TOP.md> "RGB Key TOP")• [RGB to HSV ](<./RGB_to_HSV_TOP.md> "RGB to HSV TOP")• [Scalable Display ](<./Scalable_Display_TOP.md> "Scalable Display TOP")• [Screen Grab ](<./Screen_Grab_TOP.md> "Screen Grab TOP")• [Screen ](<./Screen_TOP.md> "Screen TOP")• [Script ](<./Script_TOP.md> "Script TOP")• [Select ](<./Select_TOP.md> "Select TOP")• [Shared Mem In ](<./Shared_Mem_In_TOP.md> "Shared Mem In TOP")• [Shared Mem Out ](<./Shared_Mem_Out_TOP.md> "Shared Mem Out TOP")• [SICK ](<./SICK_TOP.md> "SICK TOP")• [Slope ](<./Slope_TOP.md> "Slope TOP")• [Spectrum ](<./Spectrum_TOP.md> "Spectrum TOP")• [SSAO ](<./SSAO_TOP.md> "SSAO TOP")• [ST2110 In ](<./ST2110_In_TOP.md> "ST2110 In TOP")• [ST2110 Out ](<./ST2110_Out_TOP.md> "ST2110 Out TOP")• [Stype ](<./Stype_TOP.md> "Stype TOP")• [Substance Select ](<./Substance_Select_TOP.md> "Substance Select TOP")• [Substance ](<./Substance_TOP.md> "Substance TOP")• [Subtract ](<./Subtract_TOP.md> "Subtract TOP")• [SVG ](<./SVG_TOP.md> "SVG TOP")• [Switch ](<./Switch_TOP.md> "Switch TOP")• [Syphon Spout In ](<./Syphon_Spout_In_TOP.md> "Syphon Spout In TOP")• [Syphon Spout Out ](<./Syphon_Spout_Out_TOP.md> "Syphon Spout Out TOP")• [Text ](<./Text_TOP.md> "Text TOP")• [Texture 3D ](<./Texture_3D_TOP.md> "Texture 3D TOP")• [Texture Sampling Parameters ](<./Texture_Sampling_Parameters.md> "Texture Sampling Parameters")• [Threshold ](<./Threshold_TOP.md> "Threshold TOP")• [Tile ](<./Tile_TOP.md> "Tile TOP")• [Time Machine ](<./Time_Machine_TOP.md> "Time Machine TOP")• [Tone Map ](<./Tone_Map_TOP.md> "Tone Map TOP")• [TOP ](<./TOP.md> "TOP")• [TOP Viewer ](<./TOP_Viewer.md> "TOP Viewer")• [Touch In ](<./Touch_In_TOP.md> "Touch In TOP")• [Touch Out ](<./Touch_Out_TOP.md> "Touch Out TOP")• [Transform ](<./Transform_TOP.md> "Transform TOP")• [Under ](<./Under_TOP.md> "Under TOP")• Video Device In • [Video Device Out ](<./Video_Device_Out_TOP.md> "Video Device Out TOP")• [Video Stream In ](<./Video_Stream_In_TOP.md> "Video Stream In TOP")• [Video Stream Out ](<./Video_Stream_Out_TOP.md> "Video Stream Out TOP")• [Vioso ](<./Vioso_TOP.md> "Vioso TOP")• [Web Render ](<./Web_Render_TOP.md> "Web Render TOP")• [ZED Select ](<./ZED_Select_TOP.md> "ZED Select TOP")• [ZED ](<./ZED_TOP.md> "ZED TOP")
