# NDI Out TOP

##   
  
Summary

The NDI Out TOP will send image and audio data over IP to other [Newtek NDI® (Network Data Interface)](<./NDI.md> "NDI") enabled applications. The [NDI®](<./NDI.md> "NDI") protocol is created by [Newtek](<http://www.newtek.com/ndi/applications/>). 

See also [NDI](<./NDI.md> "NDI"), [NDI In TOP](<./NDI_In_TOP.md> "NDI In TOP") and [NDI DAT](<./NDI_DAT.md> "NDI DAT"). 

**NOTE for Windows OS - If experiencing connection issues make sure Windows Firewall is disabled.**

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[ndioutTOP_Class](<./NdioutTOP_Class.md> "NdioutTOP Class")

## 

Parameters - NDI Out Page

Active`active`\- Makes itself available as a source and sends out image data when active. 

Source Name`name`\- Specify the name for this source. 

Failover Source Name`failovername`\- If this source fails while receivers are connected to it, they will instead try to connect to the specified Failover Source. This format of this should be`MACHINENAME (SourceName)`. This format is the same as you would see the source listed in the NDI In TOP. 

FPS`fps`\- Specify the frame rate to send at. Note that NDI uses the FPS partially as a guide to control how to compress the frames. The higher the FPS, the more compressed the frames will be. So for example sending at 1 FPS will result in higher image quality that sending at 30 FPS. 

Low-Performance Behavior`lowperformancebehavior`\- ⊞ \- When the NDI sending thread isn't able to keep up due to insufficient system resources (usually available CPU time), this controls the resulting behavior of the node. 
* Stall Main Thread`stallmainthread`\- The main thread will stall, giving up it's resources so the NDI sender can keep-up with the frames that are being sent. This will likely result in the main thread dropping frames.
* Skip Frames`skipframes`\- The main thread will not stall, and instead will not give the sender new frames until it has processed the ones it currently has. This can result in the NDI sender being starved of CPU time and running at a far lower FPS than the main thread.


Output Pixel Format`outputpixelformat`\- ⊞ \- Controls the pixel format the output is encoded into. 
* 8-bit`fixed8`\- 8-bits fixed per color channel.
* 16-bit`fixed16`\- 16-bit fixed per color channel.


Include Alpha`includealpha`\- Also sends the alpha channel when this is turned on. If this is off the alpha will be 1.0. 

Group Names Table`grouptable`\- Can be DAT table with a column with the header 'groups'. Each cell listed under that heading is added as one of the NDI groups this output annouces itself as part of. 

Audio CHOP`audiochop`\- Specify the [CHOP](<./CHOP.md> "CHOP") (containing audio data) to send out on the NDI stream. 

Metadata DAT`metadata`\- Specify the [DAT](<./DAT.md> "DAT") (containing the metadata in table format **or** valid XML format) to send out on the NDI stream. The metadata can be read in by the [NDI In TOP](<./NDI_In_TOP.md> "NDI In TOP") using an Info DAT. 

Output Color Space`outputcolorspace`\- ⊞ \- Controls what color space the data will be converted to before output. If the output (file/SDI/ST2110 etc) supports metadata, will also attempt to include the color space in that. Some output forms only support a limited number of color spaces in their metadata. If the color space is unknown to the output form, then no metadata will be included. 
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


Output Reference White`outputreferencewhite`\- ⊞ \- When converting the color values to the Working Color Space for output, this controls how they should be treated with respect to [Reference White](<./Color_Space.htm#Reference_White> "Color Space"). If the Working Color Space is the same Reference White, then no adjustment is done. If they are different, then the Reference White level (brightness) of the colors will be adjusted to the range expected by the Output Color Space. For example if the project is set to have a SDR Reference White of 120 nits, and the HDR Reference White is 80 nits, and the project Working Color Space is HDR while the Output Color Space is SDR: then a color of (1, 1, 1), which is 80 nits in the HDR color space, will be converted to be (0.66, 0.66, 0.66), which is 80 nits still in the SDR Output Color Space. 
* Default For Color Space`default`\- Will use either the SDR or the HDR Reference White, based on the color space detected/selected.
* Standard (SDR)`sdr`\- Will treat the Output Color Space as SDR for it's reference white value.
* High (HDR)`hdr`\- Will treat the Output Color Space as HDR for it's reference white value.

## 

Parameters - Common Page

Output Resolution`outputresolution`\- ⊞ \- quickly change the resolution of the TOP's data. 
* Use Input`useinput`\- Uses the input's resolution.
* Eighth`eighth`\- Multiply the input's resolution by that amount.
* Quarter`quarter`\- Multiply the input's resolution by that amount.
* Half`half`\- Multiply the input's resolution by that amount.
* 2X`2x`\- Multiply the input's resolution by that amount.
* 4X`4x`\- Multiply the input's resolution by that amount.
* 8X`8x`\- Multiply the input's resolution by that amount.
* Fit Resolution`fit`\- Fits the width and height to the resolution given below, while maintaining the aspect ratio.
* Limit Resolution`limit`\- The width and height are limited to the resolution given below. If one of the dimensions exceeds the given resolution, the width and height will be reduced to fit inside the given limits while maintaining the aspect ratio.
* Custom Resolution`custom`\- Enables the Resolution parameter below, giving direct control over width and height.


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
* Mipmap Pixels`mipmap`\- Uses [ mipmap](<./Mipmapping.md> "Mipmapping") filtering when scaling images. This can be used to reduce artifacts and sparkling in moving/scaling images that have lots of detail.


Passes`npasses`\- Duplicates the operation of the TOP the specified number of times. Making this larger than 1 is essentially the same as taking the output from each pass, and passing it into the first input of the node and repeating the process. Other inputs and parameters remain the same for each pass. 

Channel Mask`chanmask`\- Allows you to choose which channels (R, G, B, or A) the TOP will operate on. All channels are selected by default. 

Pixel Format`format`\- ⊞ \- Format used to store data for each channel in the image (ie. R, G, B, and A). Refer to [Pixel Formats](<./Pixel_Formats.md> "Pixel Formats") for more information. 
* Use Input`useinput`\- Uses the input's pixel format.
* 8-bit fixed (RGBA)`rgba8fixed`\- Uses 8-bit integer values for each channel.
* sRGB 8-bit fixed (RGBA)`srgba8fixed`\- Uses 8-bit integer values for each channel and stores color in sRGB colorspace.
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

## 

Operator Inputs
* Input 0:  -

## 

Info CHOP Channels

Extra Information for the NDI Out TOP can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). 

### 

Specific NDI Out TOP Info Channels
* num_connected \- The number of receivers connected to this source.
* last_send_time \- Amount of time the sending thread took to send the last frame, in milliseconds.
* skipped_frames \- The total number of frames produced by TouchDesigner that didnt get sent out.

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


  
TouchDesigner Build: Latest\nwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditor2025.300002021.100002018.28070before 2018.28070

TOPs   
---  
[Add ](<./Add_TOP.md> "Add TOP")• [Experimental:Add ](</index.php?title=Experimental:Add_TOP&action=edit&redlink=1> "Experimental:Add TOP \(page does not exist\)")• [Analyze ](<./Analyze_TOP.md> "Analyze TOP")• [Experimental:Analyze ](</index.php?title=Experimental:Analyze_TOP&action=edit&redlink=1> "Experimental:Analyze TOP \(page does not exist\)")• [Anti Alias ](<./Anti_Alias_TOP.md> "Anti Alias TOP")• [Blob Track ](<./Blob_Track_TOP.md> "Blob Track TOP")• [Bloom ](<./Bloom_TOP.md> "Bloom TOP")• [Blur ](<./Blur_TOP.md> "Blur TOP")• [Experimental:Blur ](</index.php?title=Experimental:Blur_TOP&action=edit&redlink=1> "Experimental:Blur TOP \(page does not exist\)")• [Cache Select ](<./Cache_Select_TOP.md> "Cache Select TOP")• [Cache ](<./Cache_TOP.md> "Cache TOP")• [Channel Mix ](<./Channel_Mix_TOP.md> "Channel Mix TOP")• [Experimental:Channel Mix ](</index.php?title=Experimental:Channel_Mix_TOP&action=edit&redlink=1> "Experimental:Channel Mix TOP \(page does not exist\)")• [CHOP to ](<./CHOP_to_TOP.md> "CHOP to TOP")• [Chroma Key ](<./Chroma_Key_TOP.md> "Chroma Key TOP")• [Experimental:Chroma Key ](</index.php?title=Experimental:Chroma_Key_TOP&action=edit&redlink=1> "Experimental:Chroma Key TOP \(page does not exist\)")• [Circle ](<./Circle_TOP.md> "Circle TOP")• [Composite ](<./Composite_TOP.md> "Composite TOP")• [Experimental:Composite ](</index.php?title=Experimental:Composite_TOP&action=edit&redlink=1> "Experimental:Composite TOP \(page does not exist\)")• [Constant ](<./Constant_TOP.md> "Constant TOP")• [Experimental:Constant ](</index.php?title=Experimental:Constant_TOP&action=edit&redlink=1> "Experimental:Constant TOP \(page does not exist\)")• [Convolve ](<./Convolve_TOP.md> "Convolve TOP")• [Experimental:Convolve ](</index.php?title=Experimental:Convolve_TOP&action=edit&redlink=1> "Experimental:Convolve TOP \(page does not exist\)")• [Corner Pin ](<./Corner_Pin_TOP.md> "Corner Pin TOP")• [Experimental:Corner Pin ](</index.php?title=Experimental:Corner_Pin_TOP&action=edit&redlink=1> "Experimental:Corner Pin TOP \(page does not exist\)")• [CPlusPlus ](<./CPlusPlus_TOP.md> "CPlusPlus TOP")• [Crop ](<./Crop_TOP.md> "Crop TOP")• [Cross ](<./Cross_TOP.md> "Cross TOP")• [Experimental:Cross ](</index.php?title=Experimental:Cross_TOP&action=edit&redlink=1> "Experimental:Cross TOP \(page does not exist\)")• [Cube Map ](<./Cube_Map_TOP.md> "Cube Map TOP")• [Depth ](<./Depth_TOP.md> "Depth TOP")• [Difference ](<./Difference_TOP.md> "Difference TOP")• [Experimental:Difference ](</index.php?title=Experimental:Difference_TOP&action=edit&redlink=1> "Experimental:Difference TOP \(page does not exist\)")• [Direct Display Out ](<./Direct_Display_Out_TOP.md> "Direct Display Out TOP")• [DirectX In ](<./DirectX_In_TOP.md> "DirectX In TOP")• [DirectX Out ](<./DirectX_Out_TOP.md> "DirectX Out TOP")• [Displace ](<./Displace_TOP.md> "Displace TOP")• [Experimental:Displace ](</index.php?title=Experimental:Displace_TOP&action=edit&redlink=1> "Experimental:Displace TOP \(page does not exist\)")• [Edge ](<./Edge_TOP.md> "Edge TOP")• [Experimental:Edge ](</index.php?title=Experimental:Edge_TOP&action=edit&redlink=1> "Experimental:Edge TOP \(page does not exist\)")• [Emboss ](<./Emboss_TOP.md> "Emboss TOP")• [Experimental:Emboss ](</index.php?title=Experimental:Emboss_TOP&action=edit&redlink=1> "Experimental:Emboss TOP \(page does not exist\)")• [Feedback ](<./Feedback_TOP.md> "Feedback TOP")• [Experimental:Feedback ](</index.php?title=Experimental:Feedback_TOP&action=edit&redlink=1> "Experimental:Feedback TOP \(page does not exist\)")• [Fit ](<./Fit_TOP.md> "Fit TOP")• [Flip ](<./Flip_TOP.md> "Flip TOP")• [Experimental:Flip ](</index.php?title=Experimental:Flip_TOP&action=edit&redlink=1> "Experimental:Flip TOP \(page does not exist\)")• [Function ](<./Function_TOP.md> "Function TOP")• [Experimental:Function ](</index.php?title=Experimental:Function_TOP&action=edit&redlink=1> "Experimental:Function TOP \(page does not exist\)")• [GLSL Multi ](<./GLSL_Multi_TOP.md> "GLSL Multi TOP")• [GLSL ](<./GLSL_TOP.md> "GLSL TOP")• [Experimental:GLSL ](</index.php?title=Experimental:GLSL_TOP&action=edit&redlink=1> "Experimental:GLSL TOP \(page does not exist\)")• [HSV Adjust ](<./HSV_Adjust_TOP.md> "HSV Adjust TOP")• [Experimental:HSV Adjust ](</index.php?title=Experimental:HSV_Adjust_TOP&action=edit&redlink=1> "Experimental:HSV Adjust TOP \(page does not exist\)")• [HSV to RGB ](<./HSV_to_RGB_TOP.md> "HSV to RGB TOP")• [Experimental:HSV to RGB ](</index.php?title=Experimental:HSV_to_RGB_TOP&action=edit&redlink=1> "Experimental:HSV to RGB TOP \(page does not exist\)")• [Import Select ](<./Import_Select_TOP.md> "Import Select TOP")• [In ](<./In_TOP.md> "In TOP")• [Inside ](<./Inside_TOP.md> "Inside TOP")• [Experimental:Inside ](</index.php?title=Experimental:Inside_TOP&action=edit&redlink=1> "Experimental:Inside TOP \(page does not exist\)")• [Introduction To s Vid ](<./Introduction_To_TOPs_Vid.md> "Introduction To TOPs Vid")• [Kinect Azure Select ](<./Kinect_Azure_Select_TOP.md> "Kinect Azure Select TOP")• [Kinect Azure ](<./Kinect_Azure_TOP.md> "Kinect Azure TOP")• [Kinect ](<./Kinect_TOP.md> "Kinect TOP")• [Experimental:Layer Mix ](</index.php?title=Experimental:Layer_Mix_TOP&action=edit&redlink=1> "Experimental:Layer Mix TOP \(page does not exist\)")• [Experimental:Layer ](</index.php?title=Experimental:Layer_TOP&action=edit&redlink=1> "Experimental:Layer TOP \(page does not exist\)")• [Layout ](<./Layout_TOP.md> "Layout TOP")• [Leap Motion ](<./Leap_Motion_TOP.md> "Leap Motion TOP")• [Lens Distort ](<./Lens_Distort_TOP.md> "Lens Distort TOP")• [Experimental:Lens Distort ](</index.php?title=Experimental:Lens_Distort_TOP&action=edit&redlink=1> "Experimental:Lens Distort TOP \(page does not exist\)")• [Level ](<./Level_TOP.md> "Level TOP")• [Experimental:Level ](</index.php?title=Experimental:Level_TOP&action=edit&redlink=1> "Experimental:Level TOP \(page does not exist\)")• [Limit ](<./Limit_TOP.md> "Limit TOP")• [Experimental:Limit ](</index.php?title=Experimental:Limit_TOP&action=edit&redlink=1> "Experimental:Limit TOP \(page does not exist\)")• [Lookup ](<./Lookup_TOP.md> "Lookup TOP")• [Experimental:Lookup ](</index.php?title=Experimental:Lookup_TOP&action=edit&redlink=1> "Experimental:Lookup TOP \(page does not exist\)")• [Luma Blur ](<./Luma_Blur_TOP.md> "Luma Blur TOP")• [Experimental:Luma Blur ](</index.php?title=Experimental:Luma_Blur_TOP&action=edit&redlink=1> "Experimental:Luma Blur TOP \(page does not exist\)")• [Luma Level ](<./Luma_Level_TOP.md> "Luma Level TOP")• [Experimental:Luma Level ](</index.php?title=Experimental:Luma_Level_TOP&action=edit&redlink=1> "Experimental:Luma Level TOP \(page does not exist\)")• [Math ](<./Math_TOP.md> "Math TOP")• [Experimental:Math ](</index.php?title=Experimental:Math_TOP&action=edit&redlink=1> "Experimental:Math TOP \(page does not exist\)")• [Matte ](<./Matte_TOP.md> "Matte TOP")• [Experimental:Matte ](</index.php?title=Experimental:Matte_TOP&action=edit&redlink=1> "Experimental:Matte TOP \(page does not exist\)")• [Mirror ](<./Mirror_TOP.md> "Mirror TOP")• [Experimental:Mirror ](</index.php?title=Experimental:Mirror_TOP&action=edit&redlink=1> "Experimental:Mirror TOP \(page does not exist\)")• [Monochrome ](<./Monochrome_TOP.md> "Monochrome TOP")• [Experimental:Monochrome ](</index.php?title=Experimental:Monochrome_TOP&action=edit&redlink=1> "Experimental:Monochrome TOP \(page does not exist\)")• [MoSys ](<./MoSys_TOP.md> "MoSys TOP")• [Movie File In ](<./Movie_File_In_TOP.md> "Movie File In TOP")• [Experimental:Movie File In ](</index.php?title=Experimental:Movie_File_In_TOP&action=edit&redlink=1> "Experimental:Movie File In TOP \(page does not exist\)")• [Movie File Out ](<./Movie_File_Out_TOP.md> "Movie File Out TOP")• [Experimental:Movie File Out ](</index.php?title=Experimental:Movie_File_Out_TOP&action=edit&redlink=1> "Experimental:Movie File Out TOP \(page does not exist\)")• [MPCDI ](<./MPCDI_TOP.md> "MPCDI TOP")• [Multiply ](<./Multiply_TOP.md> "Multiply TOP")• [Experimental:Multiply ](</index.php?title=Experimental:Multiply_TOP&action=edit&redlink=1> "Experimental:Multiply TOP \(page does not exist\)")• [Ncam ](<./Ncam_TOP.md> "Ncam TOP")• [NDI In ](<./NDI_In_TOP.md> "NDI In TOP")• [Experimental:NDI In ](</index.php?title=Experimental:NDI_In_TOP&action=edit&redlink=1> "Experimental:NDI In TOP \(page does not exist\)")• NDI Out • [Experimental:NDI Out ](</index.php?title=Experimental:NDI_Out_TOP&action=edit&redlink=1> "Experimental:NDI Out TOP \(page does not exist\)")• [Noise ](<./Noise_TOP.md> "Noise TOP")• [Experimental:Noise ](</index.php?title=Experimental:Noise_TOP&action=edit&redlink=1> "Experimental:Noise TOP \(page does not exist\)")• [Normal Map ](<./Normal_Map_TOP.md> "Normal Map TOP")• [Notch ](<./Notch_TOP.md> "Notch TOP")• [Null ](<./Null_TOP.md> "Null TOP")• [NVIDIA Background ](<./NVIDIA_Background_TOP.md> "NVIDIA Background TOP")• [Experimental:NVIDIA Background ](</index.php?title=Experimental:NVIDIA_Background_TOP&action=edit&redlink=1> "Experimental:NVIDIA Background TOP \(page does not exist\)")• [NVIDIA Denoise ](<./NVIDIA_Denoise_TOP.md> "NVIDIA Denoise TOP")• [Experimental:NVIDIA Denoise ](</index.php?title=Experimental:NVIDIA_Denoise_TOP&action=edit&redlink=1> "Experimental:NVIDIA Denoise TOP \(page does not exist\)")• [NVIDIA Flex ](<./NVIDIA_Flex_TOP.md> "NVIDIA Flex TOP")• [NVIDIA Flow ](<./NVIDIA_Flow_TOP.md> "NVIDIA Flow TOP")• [NVIDIA Upscaler ](<./NVIDIA_Upscaler_TOP.md> "NVIDIA Upscaler TOP")• [Experimental:NVIDIA Upscaler ](</index.php?title=Experimental:NVIDIA_Upscaler_TOP&action=edit&redlink=1> "Experimental:NVIDIA Upscaler TOP \(page does not exist\)")• [OAK Select ](<./OAK_Select_TOP.md> "OAK Select TOP")• [Oculus Rift ](<./Oculus_Rift_TOP.md> "Oculus Rift TOP")• [OP Viewer ](<./OP_Viewer_TOP.md> "OP Viewer TOP")• [OpenColorIO ](<./OpenColorIO_TOP.md> "OpenColorIO TOP")• [OpenVR ](<./OpenVR_TOP.md> "OpenVR TOP")• [Optical Flow ](<./Optical_Flow_TOP.md> "Optical Flow TOP")• [Orbbec Select ](<./Orbbec_Select_TOP.md> "Orbbec Select TOP")• [Orbbec ](<./Orbbec_TOP.md> "Orbbec TOP")• [Experimental:Orbbec ](</index.php?title=Experimental:Orbbec_TOP&action=edit&redlink=1> "Experimental:Orbbec TOP \(page does not exist\)")• [Ouster Select ](<./Ouster_Select_TOP.md> "Ouster Select TOP")• [Ouster ](<./Ouster_TOP.md> "Ouster TOP")• [Out ](<./Out_TOP.md> "Out TOP")• [Outside ](<./Outside_TOP.md> "Outside TOP")• [Experimental:Outside ](</index.php?title=Experimental:Outside_TOP&action=edit&redlink=1> "Experimental:Outside TOP \(page does not exist\)")• [Over ](<./Over_TOP.md> "Over TOP")• [Experimental:Over ](</index.php?title=Experimental:Over_TOP&action=edit&redlink=1> "Experimental:Over TOP \(page does not exist\)")• [Pack ](<./Pack_TOP.md> "Pack TOP")• [Experimental:Pack ](</index.php?title=Experimental:Pack_TOP&action=edit&redlink=1> "Experimental:Pack TOP \(page does not exist\)")• [Photoshop In ](<./Photoshop_In_TOP.md> "Photoshop In TOP")• [Point File In ](<./Point_File_In_TOP.md> "Point File In TOP")• [Point File Select ](<./Point_File_Select_TOP.md> "Point File Select TOP")• [Point Transform ](<./Point_Transform_TOP.md> "Point Transform TOP")• [Experimental:POP to ](</index.php?title=Experimental:POP_to_TOP&action=edit&redlink=1> "Experimental:POP to TOP \(page does not exist\)")• [PreFilter Map ](<./PreFilter_Map_TOP.md> "PreFilter Map TOP")• [Projection ](<./Projection_TOP.md> "Projection TOP")• [Ramp ](<./Ramp_TOP.md> "Ramp TOP")• [Experimental:Ramp ](</Experimental:Ramp_TOP> "Experimental:Ramp TOP")• [RealSense ](<./RealSense_TOP.md> "RealSense TOP")• [Rectangle ](<./Rectangle_TOP.md> "Rectangle TOP")• [Remap ](<./Remap_TOP.md> "Remap TOP")• [Experimental:Remap ](</Experimental:Remap_TOP> "Experimental:Remap TOP")• [Render Pass ](<./Render_Pass_TOP.md> "Render Pass TOP")• [Render Select ](<./Render_Select_TOP.md> "Render Select TOP")• [Experimental:Render Simple ](</Experimental:Render_Simple_TOP> "Experimental:Render Simple TOP")• [Render ](<./Render_TOP.md> "Render TOP")• [Experimental:Render ](</Experimental:Render_TOP> "Experimental:Render TOP")• [RenderStream In ](<./RenderStream_In_TOP.md> "RenderStream In TOP")• [RenderStream Out ](<./RenderStream_Out_TOP.md> "RenderStream Out TOP")• [Reorder ](<./Reorder_TOP.md> "Reorder TOP")• [Experimental:Reorder ](</Experimental:Reorder_TOP> "Experimental:Reorder TOP")• [Resolution ](<./Resolution_TOP.md> "Resolution TOP")• [RGB Key ](<./RGB_Key_TOP.md> "RGB Key TOP")• [RGB to HSV ](<./RGB_to_HSV_TOP.md> "RGB to HSV TOP")• [Scalable Display ](<./Scalable_Display_TOP.md> "Scalable Display TOP")• [Screen Grab ](<./Screen_Grab_TOP.md> "Screen Grab TOP")• [Screen ](<./Screen_TOP.md> "Screen TOP")• [Experimental:Screen ](</Experimental:Screen_TOP> "Experimental:Screen TOP")• [Script ](<./Script_TOP.md> "Script TOP")• [Experimental:Script ](</Experimental:Script_TOP> "Experimental:Script TOP")• [Select ](<./Select_TOP.md> "Select TOP")• [Shared Mem In ](<./Shared_Mem_In_TOP.md> "Shared Mem In TOP")• [Shared Mem Out ](<./Shared_Mem_Out_TOP.md> "Shared Mem Out TOP")• [SICK ](<./SICK_TOP.md> "SICK TOP")• [Slope ](<./Slope_TOP.md> "Slope TOP")• [Experimental:Slope ](</Experimental:Slope_TOP> "Experimental:Slope TOP")• [Spectrum ](<./Spectrum_TOP.md> "Spectrum TOP")• [SSAO ](<./SSAO_TOP.md> "SSAO TOP")• [Experimental:ST2110 In ](</Experimental:ST2110_In_TOP> "Experimental:ST2110 In TOP")• [Experimental:ST2110 Out ](</Experimental:ST2110_Out_TOP> "Experimental:ST2110 Out TOP")• [Stype ](<./Stype_TOP.md> "Stype TOP")• [Substance Select ](<./Substance_Select_TOP.md> "Substance Select TOP")• [Substance ](<./Substance_TOP.md> "Substance TOP")• [Subtract ](<./Subtract_TOP.md> "Subtract TOP")• [Experimental:Subtract ](</Experimental:Subtract_TOP> "Experimental:Subtract TOP")• [SVG ](<./SVG_TOP.md> "SVG TOP")• [Switch ](<./Switch_TOP.md> "Switch TOP")• [Syphon Spout In ](<./Syphon_Spout_In_TOP.md> "Syphon Spout In TOP")• [Syphon Spout Out ](<./Syphon_Spout_Out_TOP.md> "Syphon Spout Out TOP")• [Text ](<./Text_TOP.md> "Text TOP")• [Texture 3D ](<./Texture_3D_TOP.md> "Texture 3D TOP")• [Texture Sampling Parameters ](<./Texture_Sampling_Parameters.md> "Texture Sampling Parameters")• [Threshold ](<./Threshold_TOP.md> "Threshold TOP")• [Experimental:Threshold ](</Experimental:Threshold_TOP> "Experimental:Threshold TOP")• [Tile ](<./Tile_TOP.md> "Tile TOP")• [Time Machine ](<./Time_Machine_TOP.md> "Time Machine TOP")• [Experimental:Tone Map ](</Experimental:Tone_Map_TOP> "Experimental:Tone Map TOP")• [TOP ](<./TOP.md> "TOP")• [Experimental:TOP ](</Experimental:TOP> "Experimental:TOP")• [TOP Viewer ](<./TOP_Viewer.md> "TOP Viewer")• [Touch In ](<./Touch_In_TOP.md> "Touch In TOP")• [Touch Out ](<./Touch_Out_TOP.md> "Touch Out TOP")• [Transform ](<./Transform_TOP.md> "Transform TOP")• [Under ](<./Under_TOP.md> "Under TOP")• [Experimental:Under ](</Experimental:Under_TOP> "Experimental:Under TOP")• [Video Device In ](<./Video_Device_In_TOP.md> "Video Device In TOP")• [Experimental:Video Device In ](</Experimental:Video_Device_In_TOP> "Experimental:Video Device In TOP")• [Video Device Out ](<./Video_Device_Out_TOP.md> "Video Device Out TOP")• [Experimental:Video Device Out ](</Experimental:Video_Device_Out_TOP> "Experimental:Video Device Out TOP")• [Video Stream In ](<./Video_Stream_In_TOP.md> "Video Stream In TOP")• [Experimental:Video Stream In ](</Experimental:Video_Stream_In_TOP> "Experimental:Video Stream In TOP")• [Video Stream Out ](<./Video_Stream_Out_TOP.md> "Video Stream Out TOP")• [Experimental:Video Stream Out ](</Experimental:Video_Stream_Out_TOP> "Experimental:Video Stream Out TOP")• [Vioso ](<./Vioso_TOP.md> "Vioso TOP")• [Web Render ](<./Web_Render_TOP.md> "Web Render TOP")• [Experimental:Web Render ](</Experimental:Web_Render_TOP> "Experimental:Web Render TOP")• [Experimental:ZED Select ](</Experimental:ZED_Select_TOP> "Experimental:ZED Select TOP")• [ZED ](<./ZED_TOP.md> "ZED TOP")• [Experimental:ZED ](</Experimental:ZED_TOP> "Experimental:ZED TOP")
