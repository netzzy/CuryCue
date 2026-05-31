# Level TOP

## 

Summary

The Level TOP adjusts image contrast, brightness, gamma, black level, color range, quantization, opacity and more. See also the [Luma Level TOP](<./Luma_Level_TOP.md> "Luma Level TOP") which preserves hue and saturation more accurately, but is slower. 

The Level TOP's features have been built into one TOP to maximize performance in a single pass. It takes all its parameters to make a lookup table on the CPU, so animating parameters in the Level TOP will decrease its performance as the lookup table is recreated each frame that a parameter changes. 

**Note:** This TOP supports 3D Textures and 2D Texture Arrays. 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[levelTOP_Class](<./LevelTOP_Class.md> "LevelTOP Class")

## 

Parameters - Pre Page

Clamp Input`clampinput`\- ⊞ \- This option will clamp pixel values in between 0 and 1. When using higher bit depth floating pixel formats, it is recommended to set it to Unclamped to allow the full range of values to be operated on. Auto should detect the pixel format as set accordingly. 
* Automatic`automatic`\- Detects pixel format and clamps if 8-bit fixed or leaves unclamped for floating point pixel formats.
* Clamp [0-1]`clamp`\- Clamps data to values between 0 and 1. Recommended for 8-bit fixed default pixel format for better performance.
* Unclamped`unclamped`\- No clamping of data, use for higher bit-depth pixel formats.


Invert`invert`\- Inverts the colors in the image. Black becomes white, white becomes black. Colors invert across the color wheel, so red becomes cyan, blue becomes yellow, green becomes magenta, and so on. 

Black Level`blacklevel`\- Any pixel with a value less than or equal to this will be black. 

Brightness 1`brightness1`\- Increases or decreases the brightness of an image. Brightness can be considered the arithmetic mean of the RGB channels. The Brightness parameter adds or subtracts an offset into the R, G, and B channels. Low brightness will result in dark tones, while high brightness will wash the color out towards white. 

Gamma 1`gamma1`\- The Gamma parameter applies a gamma correction to the image. Gamma is the relationship between the brightness of a pixel as it appears on the screen, and the numerical value of that pixel. This is often represented by a gamma curve. The difference between brightness and gamma is that gamma also affects the ratio of red to green to blue. A straight, linear gamma curve with a value of 1 means no change. 

Contrast`contrast`\- Contrast applies a scale factor (gain) to the RGB channels. Increasing contrast will brighten the light areas and darken the dark areas of the image, making the difference between the light and dark areas of the image stronger. 

## 

Parameters - Range Page

In Low`inlow`\- Any pixel below this value appears black. 

In High`inhigh`\- Any pixel above this value appears white. 

Out Low`outlow`\- Clamps pixel values to this value or higher. 

Out High`outhigh`\- Clamps pixel values to this value or lower. 

## 

Parameters - RGBA Page

Low R`lowr`\- Clamps the minimum level of the red channel. 

High R`highr`\- Clamps the maximum level of the red channel. 

Low G`lowg`\- Clamps the minimum level of the green channel. 

High G`highg`\- Clamps the maximum level of the green channel. 

Low B`lowb`\- Clamps the minimum level of the blue channel. 

High B`highb`\- Clamps the maximum level of the blue channel. 

Low A`lowa`\- Clamps the minimum level of the alpha channel. 

High A`higha`\- Clamps the maximum level of the alpha channel. 

## 

Parameters - Step Page

Apply Stepping`stepping`\- Turns on stepping (posterizing) and enables the parameters below. 

Step Size`stepsize`\- Posterizes the image into bands or stripes. Number of bands equal to the inverse of this parameter (i.e., 0.25 = 4 bands). Use a default Ramp TOP to easily see this parameter's effect. 

Threshold`threshold`\- Offsets the position of the step boundaries. 

Clamp Low`clamplow`\- Clamps the image's minimum value. (_value_ as in hue, saturation, and _value_) 

Clamp High`clamphigh`\- Clamps the image's maximum value. (_value_ as in hue, saturation, and _value_) 

Soften`soften`\- Softens or blends the boundaries between steps. 

## 

Parameters - Post Page

Gamma 2`gamma2`\- A second gamma correction that is added after the Range, RGBA, and Step page adjustments have been applied. 

Opacity`opacity`\- Adjust the opacity, or transparency, of the image. 

Brightness 2`brightness2`\- A second brightness adjustment that is added after the Range, RGBA, and Step page adjustments have been applied. 

Clamp`clamp`\- Clamps pixel values to this value or lower. 

Clamp Low`clamplow2`\- Clamps the image's minimum value. (_value_ as in hue, saturation, and _value_) 

Clamp High`clamphigh2`\- Clamps the image's maximum value. (_value_ as in hue, saturation, and _value_) 

Pre-Multiply RGB by Alpha`premultrgbbyalpha`\- This option makes the color channels pre-multiplied by alpha. 

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

Extra Information for the Level TOP can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). __

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


  
TouchDesigner Build: Latest\nwikieditor2025.300002022.241402021.100002018.28070before 2018.28070

TOPs   
---  
[Add ](<./Add_TOP.md> "Add TOP")• [Experimental:Add ](</index.php?title=Experimental:Add_TOP&action=edit&redlink=1> "Experimental:Add TOP \(page does not exist\)")• [Analyze ](<./Analyze_TOP.md> "Analyze TOP")• [Experimental:Analyze ](</index.php?title=Experimental:Analyze_TOP&action=edit&redlink=1> "Experimental:Analyze TOP \(page does not exist\)")• [Anti Alias ](<./Anti_Alias_TOP.md> "Anti Alias TOP")• [Blob Track ](<./Blob_Track_TOP.md> "Blob Track TOP")• [Bloom ](<./Bloom_TOP.md> "Bloom TOP")• [Blur ](<./Blur_TOP.md> "Blur TOP")• [Experimental:Blur ](</index.php?title=Experimental:Blur_TOP&action=edit&redlink=1> "Experimental:Blur TOP \(page does not exist\)")• [Cache Select ](<./Cache_Select_TOP.md> "Cache Select TOP")• [Cache ](<./Cache_TOP.md> "Cache TOP")• [Channel Mix ](<./Channel_Mix_TOP.md> "Channel Mix TOP")• [Experimental:Channel Mix ](</index.php?title=Experimental:Channel_Mix_TOP&action=edit&redlink=1> "Experimental:Channel Mix TOP \(page does not exist\)")• [CHOP to ](<./CHOP_to_TOP.md> "CHOP to TOP")• [Chroma Key ](<./Chroma_Key_TOP.md> "Chroma Key TOP")• [Experimental:Chroma Key ](</index.php?title=Experimental:Chroma_Key_TOP&action=edit&redlink=1> "Experimental:Chroma Key TOP \(page does not exist\)")• [Circle ](<./Circle_TOP.md> "Circle TOP")• [Composite ](<./Composite_TOP.md> "Composite TOP")• [Experimental:Composite ](</index.php?title=Experimental:Composite_TOP&action=edit&redlink=1> "Experimental:Composite TOP \(page does not exist\)")• [Constant ](<./Constant_TOP.md> "Constant TOP")• [Experimental:Constant ](</index.php?title=Experimental:Constant_TOP&action=edit&redlink=1> "Experimental:Constant TOP \(page does not exist\)")• [Convolve ](<./Convolve_TOP.md> "Convolve TOP")• [Experimental:Convolve ](</index.php?title=Experimental:Convolve_TOP&action=edit&redlink=1> "Experimental:Convolve TOP \(page does not exist\)")• [Corner Pin ](<./Corner_Pin_TOP.md> "Corner Pin TOP")• [Experimental:Corner Pin ](</index.php?title=Experimental:Corner_Pin_TOP&action=edit&redlink=1> "Experimental:Corner Pin TOP \(page does not exist\)")• [CPlusPlus ](<./CPlusPlus_TOP.md> "CPlusPlus TOP")• [Crop ](<./Crop_TOP.md> "Crop TOP")• [Cross ](<./Cross_TOP.md> "Cross TOP")• [Experimental:Cross ](</index.php?title=Experimental:Cross_TOP&action=edit&redlink=1> "Experimental:Cross TOP \(page does not exist\)")• [Cube Map ](<./Cube_Map_TOP.md> "Cube Map TOP")• [Depth ](<./Depth_TOP.md> "Depth TOP")• [Difference ](<./Difference_TOP.md> "Difference TOP")• [Experimental:Difference ](</index.php?title=Experimental:Difference_TOP&action=edit&redlink=1> "Experimental:Difference TOP \(page does not exist\)")• [Direct Display Out ](<./Direct_Display_Out_TOP.md> "Direct Display Out TOP")• [DirectX In ](<./DirectX_In_TOP.md> "DirectX In TOP")• [DirectX Out ](<./DirectX_Out_TOP.md> "DirectX Out TOP")• [Displace ](<./Displace_TOP.md> "Displace TOP")• [Experimental:Displace ](</index.php?title=Experimental:Displace_TOP&action=edit&redlink=1> "Experimental:Displace TOP \(page does not exist\)")• [Edge ](<./Edge_TOP.md> "Edge TOP")• [Experimental:Edge ](</index.php?title=Experimental:Edge_TOP&action=edit&redlink=1> "Experimental:Edge TOP \(page does not exist\)")• [Emboss ](<./Emboss_TOP.md> "Emboss TOP")• [Experimental:Emboss ](</index.php?title=Experimental:Emboss_TOP&action=edit&redlink=1> "Experimental:Emboss TOP \(page does not exist\)")• [Feedback ](<./Feedback_TOP.md> "Feedback TOP")• [Experimental:Feedback ](</index.php?title=Experimental:Feedback_TOP&action=edit&redlink=1> "Experimental:Feedback TOP \(page does not exist\)")• [Fit ](<./Fit_TOP.md> "Fit TOP")• [Flip ](<./Flip_TOP.md> "Flip TOP")• [Experimental:Flip ](</index.php?title=Experimental:Flip_TOP&action=edit&redlink=1> "Experimental:Flip TOP \(page does not exist\)")• [Function ](<./Function_TOP.md> "Function TOP")• [Experimental:Function ](</index.php?title=Experimental:Function_TOP&action=edit&redlink=1> "Experimental:Function TOP \(page does not exist\)")• [GLSL Multi ](<./GLSL_Multi_TOP.md> "GLSL Multi TOP")• [GLSL ](<./GLSL_TOP.md> "GLSL TOP")• [Experimental:GLSL ](</index.php?title=Experimental:GLSL_TOP&action=edit&redlink=1> "Experimental:GLSL TOP \(page does not exist\)")• [HSV Adjust ](<./HSV_Adjust_TOP.md> "HSV Adjust TOP")• [Experimental:HSV Adjust ](</index.php?title=Experimental:HSV_Adjust_TOP&action=edit&redlink=1> "Experimental:HSV Adjust TOP \(page does not exist\)")• [HSV to RGB ](<./HSV_to_RGB_TOP.md> "HSV to RGB TOP")• [Experimental:HSV to RGB ](</index.php?title=Experimental:HSV_to_RGB_TOP&action=edit&redlink=1> "Experimental:HSV to RGB TOP \(page does not exist\)")• [Import Select ](<./Import_Select_TOP.md> "Import Select TOP")• [In ](<./In_TOP.md> "In TOP")• [Inside ](<./Inside_TOP.md> "Inside TOP")• [Experimental:Inside ](</index.php?title=Experimental:Inside_TOP&action=edit&redlink=1> "Experimental:Inside TOP \(page does not exist\)")• [Introduction To s Vid ](<./Introduction_To_TOPs_Vid.md> "Introduction To TOPs Vid")• [Kinect Azure Select ](<./Kinect_Azure_Select_TOP.md> "Kinect Azure Select TOP")• [Kinect Azure ](<./Kinect_Azure_TOP.md> "Kinect Azure TOP")• [Kinect ](<./Kinect_TOP.md> "Kinect TOP")• [Experimental:Layer Mix ](</index.php?title=Experimental:Layer_Mix_TOP&action=edit&redlink=1> "Experimental:Layer Mix TOP \(page does not exist\)")• [Experimental:Layer ](</index.php?title=Experimental:Layer_TOP&action=edit&redlink=1> "Experimental:Layer TOP \(page does not exist\)")• [Layout ](<./Layout_TOP.md> "Layout TOP")• [Leap Motion ](<./Leap_Motion_TOP.md> "Leap Motion TOP")• [Lens Distort ](<./Lens_Distort_TOP.md> "Lens Distort TOP")• [Experimental:Lens Distort ](</index.php?title=Experimental:Lens_Distort_TOP&action=edit&redlink=1> "Experimental:Lens Distort TOP \(page does not exist\)")• Level • [Experimental:Level ](</index.php?title=Experimental:Level_TOP&action=edit&redlink=1> "Experimental:Level TOP \(page does not exist\)")• [Limit ](<./Limit_TOP.md> "Limit TOP")• [Experimental:Limit ](</index.php?title=Experimental:Limit_TOP&action=edit&redlink=1> "Experimental:Limit TOP \(page does not exist\)")• [Lookup ](<./Lookup_TOP.md> "Lookup TOP")• [Experimental:Lookup ](</index.php?title=Experimental:Lookup_TOP&action=edit&redlink=1> "Experimental:Lookup TOP \(page does not exist\)")• [Luma Blur ](<./Luma_Blur_TOP.md> "Luma Blur TOP")• [Experimental:Luma Blur ](</index.php?title=Experimental:Luma_Blur_TOP&action=edit&redlink=1> "Experimental:Luma Blur TOP \(page does not exist\)")• [Luma Level ](<./Luma_Level_TOP.md> "Luma Level TOP")• [Experimental:Luma Level ](</index.php?title=Experimental:Luma_Level_TOP&action=edit&redlink=1> "Experimental:Luma Level TOP \(page does not exist\)")• [Math ](<./Math_TOP.md> "Math TOP")• [Experimental:Math ](</index.php?title=Experimental:Math_TOP&action=edit&redlink=1> "Experimental:Math TOP \(page does not exist\)")• [Matte ](<./Matte_TOP.md> "Matte TOP")• [Experimental:Matte ](</index.php?title=Experimental:Matte_TOP&action=edit&redlink=1> "Experimental:Matte TOP \(page does not exist\)")• [Mirror ](<./Mirror_TOP.md> "Mirror TOP")• [Experimental:Mirror ](</index.php?title=Experimental:Mirror_TOP&action=edit&redlink=1> "Experimental:Mirror TOP \(page does not exist\)")• [Monochrome ](<./Monochrome_TOP.md> "Monochrome TOP")• [Experimental:Monochrome ](</index.php?title=Experimental:Monochrome_TOP&action=edit&redlink=1> "Experimental:Monochrome TOP \(page does not exist\)")• [MoSys ](<./MoSys_TOP.md> "MoSys TOP")• [Movie File In ](<./Movie_File_In_TOP.md> "Movie File In TOP")• [Experimental:Movie File In ](</index.php?title=Experimental:Movie_File_In_TOP&action=edit&redlink=1> "Experimental:Movie File In TOP \(page does not exist\)")• [Movie File Out ](<./Movie_File_Out_TOP.md> "Movie File Out TOP")• [Experimental:Movie File Out ](</index.php?title=Experimental:Movie_File_Out_TOP&action=edit&redlink=1> "Experimental:Movie File Out TOP \(page does not exist\)")• [MPCDI ](<./MPCDI_TOP.md> "MPCDI TOP")• [Multiply ](<./Multiply_TOP.md> "Multiply TOP")• [Experimental:Multiply ](</index.php?title=Experimental:Multiply_TOP&action=edit&redlink=1> "Experimental:Multiply TOP \(page does not exist\)")• [Ncam ](<./Ncam_TOP.md> "Ncam TOP")• [NDI In ](<./NDI_In_TOP.md> "NDI In TOP")• [Experimental:NDI In ](</index.php?title=Experimental:NDI_In_TOP&action=edit&redlink=1> "Experimental:NDI In TOP \(page does not exist\)")• [NDI Out ](<./NDI_Out_TOP.md> "NDI Out TOP")• [Experimental:NDI Out ](</index.php?title=Experimental:NDI_Out_TOP&action=edit&redlink=1> "Experimental:NDI Out TOP \(page does not exist\)")• [Noise ](<./Noise_TOP.md> "Noise TOP")• [Experimental:Noise ](</index.php?title=Experimental:Noise_TOP&action=edit&redlink=1> "Experimental:Noise TOP \(page does not exist\)")• [Normal Map ](<./Normal_Map_TOP.md> "Normal Map TOP")• [Notch ](<./Notch_TOP.md> "Notch TOP")• [Null ](<./Null_TOP.md> "Null TOP")• [NVIDIA Background ](<./NVIDIA_Background_TOP.md> "NVIDIA Background TOP")• [Experimental:NVIDIA Background ](</index.php?title=Experimental:NVIDIA_Background_TOP&action=edit&redlink=1> "Experimental:NVIDIA Background TOP \(page does not exist\)")• [NVIDIA Denoise ](<./NVIDIA_Denoise_TOP.md> "NVIDIA Denoise TOP")• [Experimental:NVIDIA Denoise ](</index.php?title=Experimental:NVIDIA_Denoise_TOP&action=edit&redlink=1> "Experimental:NVIDIA Denoise TOP \(page does not exist\)")• [NVIDIA Flex ](<./NVIDIA_Flex_TOP.md> "NVIDIA Flex TOP")• [NVIDIA Flow ](<./NVIDIA_Flow_TOP.md> "NVIDIA Flow TOP")• [NVIDIA Upscaler ](<./NVIDIA_Upscaler_TOP.md> "NVIDIA Upscaler TOP")• [Experimental:NVIDIA Upscaler ](</index.php?title=Experimental:NVIDIA_Upscaler_TOP&action=edit&redlink=1> "Experimental:NVIDIA Upscaler TOP \(page does not exist\)")• [OAK Select ](<./OAK_Select_TOP.md> "OAK Select TOP")• [Oculus Rift ](<./Oculus_Rift_TOP.md> "Oculus Rift TOP")• [OP Viewer ](<./OP_Viewer_TOP.md> "OP Viewer TOP")• [OpenColorIO ](<./OpenColorIO_TOP.md> "OpenColorIO TOP")• [OpenVR ](<./OpenVR_TOP.md> "OpenVR TOP")• [Optical Flow ](<./Optical_Flow_TOP.md> "Optical Flow TOP")• [Orbbec Select ](<./Orbbec_Select_TOP.md> "Orbbec Select TOP")• [Orbbec ](<./Orbbec_TOP.md> "Orbbec TOP")• [Experimental:Orbbec ](</index.php?title=Experimental:Orbbec_TOP&action=edit&redlink=1> "Experimental:Orbbec TOP \(page does not exist\)")• [Ouster Select ](<./Ouster_Select_TOP.md> "Ouster Select TOP")• [Ouster ](<./Ouster_TOP.md> "Ouster TOP")• [Out ](<./Out_TOP.md> "Out TOP")• [Outside ](<./Outside_TOP.md> "Outside TOP")• [Experimental:Outside ](</index.php?title=Experimental:Outside_TOP&action=edit&redlink=1> "Experimental:Outside TOP \(page does not exist\)")• [Over ](<./Over_TOP.md> "Over TOP")• [Experimental:Over ](</index.php?title=Experimental:Over_TOP&action=edit&redlink=1> "Experimental:Over TOP \(page does not exist\)")• [Pack ](<./Pack_TOP.md> "Pack TOP")• [Experimental:Pack ](</index.php?title=Experimental:Pack_TOP&action=edit&redlink=1> "Experimental:Pack TOP \(page does not exist\)")• [Photoshop In ](<./Photoshop_In_TOP.md> "Photoshop In TOP")• [Point File In ](<./Point_File_In_TOP.md> "Point File In TOP")• [Point File Select ](<./Point_File_Select_TOP.md> "Point File Select TOP")• [Point Transform ](<./Point_Transform_TOP.md> "Point Transform TOP")• [Experimental:POP to ](</index.php?title=Experimental:POP_to_TOP&action=edit&redlink=1> "Experimental:POP to TOP \(page does not exist\)")• [PreFilter Map ](<./PreFilter_Map_TOP.md> "PreFilter Map TOP")• [Projection ](<./Projection_TOP.md> "Projection TOP")• [Ramp ](<./Ramp_TOP.md> "Ramp TOP")• [Experimental:Ramp ](</index.php?title=Experimental:Ramp_TOP&action=edit&redlink=1> "Experimental:Ramp TOP \(page does not exist\)")• [RealSense ](<./RealSense_TOP.md> "RealSense TOP")• [Rectangle ](<./Rectangle_TOP.md> "Rectangle TOP")• [Remap ](<./Remap_TOP.md> "Remap TOP")• [Experimental:Remap ](</index.php?title=Experimental:Remap_TOP&action=edit&redlink=1> "Experimental:Remap TOP \(page does not exist\)")• [Render Pass ](<./Render_Pass_TOP.md> "Render Pass TOP")• [Render Select ](<./Render_Select_TOP.md> "Render Select TOP")• [Experimental:Render Simple ](</index.php?title=Experimental:Render_Simple_TOP&action=edit&redlink=1> "Experimental:Render Simple TOP \(page does not exist\)")• [Render ](<./Render_TOP.md> "Render TOP")• [Experimental:Render ](</index.php?title=Experimental:Render_TOP&action=edit&redlink=1> "Experimental:Render TOP \(page does not exist\)")• [RenderStream In ](<./RenderStream_In_TOP.md> "RenderStream In TOP")• [RenderStream Out ](<./RenderStream_Out_TOP.md> "RenderStream Out TOP")• [Reorder ](<./Reorder_TOP.md> "Reorder TOP")• [Experimental:Reorder ](</index.php?title=Experimental:Reorder_TOP&action=edit&redlink=1> "Experimental:Reorder TOP \(page does not exist\)")• [Resolution ](<./Resolution_TOP.md> "Resolution TOP")• [RGB Key ](<./RGB_Key_TOP.md> "RGB Key TOP")• [RGB to HSV ](<./RGB_to_HSV_TOP.md> "RGB to HSV TOP")• [Scalable Display ](<./Scalable_Display_TOP.md> "Scalable Display TOP")• [Screen Grab ](<./Screen_Grab_TOP.md> "Screen Grab TOP")• [Screen ](<./Screen_TOP.md> "Screen TOP")• [Experimental:Screen ](</index.php?title=Experimental:Screen_TOP&action=edit&redlink=1> "Experimental:Screen TOP \(page does not exist\)")• [Script ](<./Script_TOP.md> "Script TOP")• [Experimental:Script ](</index.php?title=Experimental:Script_TOP&action=edit&redlink=1> "Experimental:Script TOP \(page does not exist\)")• [Select ](<./Select_TOP.md> "Select TOP")• [Shared Mem In ](<./Shared_Mem_In_TOP.md> "Shared Mem In TOP")• [Shared Mem Out ](<./Shared_Mem_Out_TOP.md> "Shared Mem Out TOP")• [SICK ](<./SICK_TOP.md> "SICK TOP")• [Slope ](<./Slope_TOP.md> "Slope TOP")• [Experimental:Slope ](</index.php?title=Experimental:Slope_TOP&action=edit&redlink=1> "Experimental:Slope TOP \(page does not exist\)")• [Spectrum ](<./Spectrum_TOP.md> "Spectrum TOP")• [SSAO ](<./SSAO_TOP.md> "SSAO TOP")• [Experimental:ST2110 In ](</index.php?title=Experimental:ST2110_In_TOP&action=edit&redlink=1> "Experimental:ST2110 In TOP \(page does not exist\)")• [Experimental:ST2110 Out ](</index.php?title=Experimental:ST2110_Out_TOP&action=edit&redlink=1> "Experimental:ST2110 Out TOP \(page does not exist\)")• [Stype ](<./Stype_TOP.md> "Stype TOP")• [Substance Select ](<./Substance_Select_TOP.md> "Substance Select TOP")• [Substance ](<./Substance_TOP.md> "Substance TOP")• [Subtract ](<./Subtract_TOP.md> "Subtract TOP")• [Experimental:Subtract ](</index.php?title=Experimental:Subtract_TOP&action=edit&redlink=1> "Experimental:Subtract TOP \(page does not exist\)")• [SVG ](<./SVG_TOP.md> "SVG TOP")• [Switch ](<./Switch_TOP.md> "Switch TOP")• [Syphon Spout In ](<./Syphon_Spout_In_TOP.md> "Syphon Spout In TOP")• [Syphon Spout Out ](<./Syphon_Spout_Out_TOP.md> "Syphon Spout Out TOP")• [Text ](<./Text_TOP.md> "Text TOP")• [Texture 3D ](<./Texture_3D_TOP.md> "Texture 3D TOP")• [Texture Sampling Parameters ](<./Texture_Sampling_Parameters.md> "Texture Sampling Parameters")• [Threshold ](<./Threshold_TOP.md> "Threshold TOP")• [Experimental:Threshold ](</index.php?title=Experimental:Threshold_TOP&action=edit&redlink=1> "Experimental:Threshold TOP \(page does not exist\)")• [Tile ](<./Tile_TOP.md> "Tile TOP")• [Time Machine ](<./Time_Machine_TOP.md> "Time Machine TOP")• [Experimental:Tone Map ](</index.php?title=Experimental:Tone_Map_TOP&action=edit&redlink=1> "Experimental:Tone Map TOP \(page does not exist\)")• [TOP ](<./TOP.md> "TOP")• [Experimental:TOP ](</index.php?title=Experimental:TOP&action=edit&redlink=1> "Experimental:TOP \(page does not exist\)")• [TOP Viewer ](<./TOP_Viewer.md> "TOP Viewer")• [Touch In ](<./Touch_In_TOP.md> "Touch In TOP")• [Touch Out ](<./Touch_Out_TOP.md> "Touch Out TOP")• [Transform ](<./Transform_TOP.md> "Transform TOP")• [Under ](<./Under_TOP.md> "Under TOP")• [Experimental:Under ](</index.php?title=Experimental:Under_TOP&action=edit&redlink=1> "Experimental:Under TOP \(page does not exist\)")• [Video Device In ](<./Video_Device_In_TOP.md> "Video Device In TOP")• [Experimental:Video Device In ](</index.php?title=Experimental:Video_Device_In_TOP&action=edit&redlink=1> "Experimental:Video Device In TOP \(page does not exist\)")• [Video Device Out ](<./Video_Device_Out_TOP.md> "Video Device Out TOP")• [Experimental:Video Device Out ](</index.php?title=Experimental:Video_Device_Out_TOP&action=edit&redlink=1> "Experimental:Video Device Out TOP \(page does not exist\)")• [Video Stream In ](<./Video_Stream_In_TOP.md> "Video Stream In TOP")• [Experimental:Video Stream In ](</index.php?title=Experimental:Video_Stream_In_TOP&action=edit&redlink=1> "Experimental:Video Stream In TOP \(page does not exist\)")• [Video Stream Out ](<./Video_Stream_Out_TOP.md> "Video Stream Out TOP")• [Experimental:Video Stream Out ](</index.php?title=Experimental:Video_Stream_Out_TOP&action=edit&redlink=1> "Experimental:Video Stream Out TOP \(page does not exist\)")• [Vioso ](<./Vioso_TOP.md> "Vioso TOP")• [Web Render ](<./Web_Render_TOP.md> "Web Render TOP")• [Experimental:Web Render ](</index.php?title=Experimental:Web_Render_TOP&action=edit&redlink=1> "Experimental:Web Render TOP \(page does not exist\)")• [Experimental:ZED Select ](</index.php?title=Experimental:ZED_Select_TOP&action=edit&redlink=1> "Experimental:ZED Select TOP \(page does not exist\)")• [ZED ](<./ZED_TOP.md> "ZED TOP")• [Experimental:ZED ](</index.php?title=Experimental:ZED_TOP&action=edit&redlink=1> "Experimental:ZED TOP \(page does not exist\)")
