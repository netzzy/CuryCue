# Orbbec TOP

##   
  
Summary

The Orbbec TOP can be used to retrieve video streams and IMU data from an [Orbbec camera](<./Orbbec.md> "Orbbec"). The available video streams depend on the connected camera, but typically include color, depth, IR and point cloud data. This node uses the Orbbec SDK and a list of [compatible camera models](<https://github.com/orbbec/OrbbecSDK>) can be found on the project's Github page. 

The camera may be connected either by USB or ethernet depending on the model. 

**Note:** Obtaining color video images over ethernet may not be supported for older firmware. We recommend you update your camera firmware to the latest version that is compatible with the Orbbec SDK that your TouchDesigner build is using. 

**MacOS:** Connecting to Orbbec cameras on Mac OS systems requires root privileges. You can launch TouchDesigner with root privileges by opening a Terminal window and using the sudo command i.e.`sudo "/Applications/TouchDesigner.app/contents/MacOS/TouchDesigner"`To obtain more than one video stream from a camera, you can use one or more [Orbbec Select TOPs](<./Orbbec_Select_TOP.md> "Orbbec Select TOP") linked to the primary Orbbec TOP. All resolution and configuration is handled by the primary Orbbec TOP. 

Skeleton tracking data can also be obtained from compatible Kinect Orbbec cameras (Femto Mega, Femto Bolt, etc) using the [Kinect Azure TOP](<./Kinect_Azure_TOP.md> "Kinect Azure TOP") and [Kinect Azure CHOP](<./Kinect_Azure_CHOP.md> "Kinect Azure CHOP"). **Note:** if using the Kinect Azure nodes with Orbbec hardware, you should not use the Orbbec TOP in the same project or it could lead to instabilities. 

An [Info CHOP](<./Info_CHOP.md> "Info CHOP") can be used to view the current value of each supported camera property, and an [Info DAT](<./Info_DAT.md> "Info DAT") can be used to see the minimum, maximum, and default value of each supported camera property. 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[orbbecTOP_Class](<./OrbbecTOP_Class.md> "OrbbecTOP Class")

## 

Parameters - Orbbec Page

Active`active`\- Turn this parameter off to disable communication with the camera. This will also stop any [Orbbec Select TOPs](<./Orbbec_Select_TOP.md> "Orbbec Select TOP") that rely on this TOP. 

Device Source`devicesource`\- ⊞ \- Specifies which mode to use to connect to a camera. **Note:** We generally recommend users to connect to cameras through the Device menu parameter instead of specifying the IP address. 
* Auto-Detect`auto`\- Connect to enumerated cameras through the Device menu.
* IP Address`ipaddress`\- Connect to cameras by specifying their IP addresses.


Device`device`\- Use this parameter to select the serial number of the camera you wish to connect to. Only one Orbbec TOP can connect to any camera at one time. Use an [Orbbec Select TOP](<./Orbbec_Select_TOP.md> "Orbbec Select TOP") to obtain additional video streams from the same camera. Both USB and ethernet connected cameras are discoverable by this menu. Cameras connected through this menu can automatically reconnect after unplugging and replugging. **Note:** It can take up to 30s for a camera to appear after it has been plugged in. 

IP`ip`\- The IP address of the camera to connect to. 

Color Resolution`colorres`\- ⊞ \- Select the resolution of the sensor's color camera. Every camera has a default resolution that it will use automatically. Additional options will appear in the menu depending on the camera model. Not all frame rates (FPS) will be available for all camera resolutions. 
* Default`default`\- Use the default resolution for the camera.


Color FPS`colorfps`\- ⊞ \- Set the frame rate in frames-per-second for the color camera. The camera will assume a default frame rate automatically, but additional rates will appear in this list depending on the camera model. Not all frame rates may be supported by the current camera resolution. 
* Default`default`\- The default frame rate for the sensor's color camera.


Depth Resolution`depthres`\- ⊞ \- Select the resolution of the sensor's depth camera. Every camera has a default resolution that it will use automatically. Additional options will appear in the menu depending on the camera model. Not all frame rates (FPS) will be available for all camera resolutions. 
* Default`default`\- The default resolution rate for the sensor's depth camera.


Depth FPS`depthfps`\- ⊞ \- Set the frame rate in frames-per-second for the depth camera. The camera will assume a default frame rate automatically, but additional rates will appear in this list depending on the camera model. Not all frame rates may be supported by the current camera resolution. 
* Default`default`\- The default frame rate for the sensor's depth camera.


Depth Align Mode`depthalignmode`\- ⊞ \- This parameter can be used to transform the depth image to match the resolution of the color camera. This may be done in either hardware or software depending on the camera model. Some resolutions may not be supported. The node will display an error if the current depth and color resolutions are not compatible. 
* Disabled`disabled`\- The depth image will be displayed in its native resolution.
* Hardware`hardware`\- The depth image will be transformed to the color camera's resolution using hardware remapping.
* Software`software`\- The depth image will be transformed to the color camera's resolution using software remapping.


Image`image`\- ⊞ \- Select which of the camera's video streams to display in the node's output image. Additional streams can be obtained for the same camera using the [Orbbec Select TOP](<./Orbbec_Select_TOP.md> "Orbbec Select TOP"). 
* Color`color`\- The video stream for the color camera. This is usually an 8-bit RGBA image.
* Depth`depth`\- The video stream for the depth camera. This is a 32-bit floating point texture where each pixel measures the depth in meters.
* IR`ir`\- The raw IR image from the depth camera. The resolution and frame rate are based on the depth camera settings.
* Point Cloud`pointcloud`\- A 3D point cloud where the x, y and z positions are stored in meters in the red, blue and green channels of a 32 bit floating point image.


Enable Gyro Sensor`gyro`\- Enable rotational IMU data from the gyro sensor if it is available on the current camera. The data is measured in degrees/sec and accessible as CHOP channels by attaching an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). 

Enable Accel Sensor`accel`\- Enable linear acceleration IMU data from the accel sensor if it is available on the current camera. The data is measured in m/s^2 and accessible as CHOP channels by attaching an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). 

Properties CHOP`propschop`\- The path of the properties CHOP being referenced. Each channel of the CHOP represents an [OBPropertyID](<https://orbbec.github.io/OrbbecSDK/doc/api/English/Property_8h.html#a9e7aac1ea041c8958ea8c6e3aa53bbab>) which can be used to control camera settings. The channel name must be all lowercase and cannot include the 'OB_PROP_' prefix. For example, a valid channel name for 'OB_PROP_COLOR_MIRROR_BOOL' would be 'color_mirror_bool'. Supported properties differ between each Orbbec camera model. The current value of each supported property can be viewed in an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). The minimum, maximum, and default values of each supported property can be viewed in an [Info DAT](<./Info_DAT.md> "Info DAT"). 

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

## 

Info CHOP Channels

Extra Information for the Orbbec TOP can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). __

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


  
TouchDesigner Build: Latest\nwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditor2025.300002023.11280

TOPs   
---  
[Add ](<./Add_TOP.md> "Add TOP")• [Analyze ](<./Analyze_TOP.md> "Analyze TOP")• [Anti Alias ](<./Anti_Alias_TOP.md> "Anti Alias TOP")• [Blob Track ](<./Blob_Track_TOP.md> "Blob Track TOP")• [Bloom ](<./Bloom_TOP.md> "Bloom TOP")• [Blur ](<./Blur_TOP.md> "Blur TOP")• [Cache Select ](<./Cache_Select_TOP.md> "Cache Select TOP")• [Cache ](<./Cache_TOP.md> "Cache TOP")• [Channel Mix ](<./Channel_Mix_TOP.md> "Channel Mix TOP")• [CHOP to ](<./CHOP_to_TOP.md> "CHOP to TOP")• [Chroma Key ](<./Chroma_Key_TOP.md> "Chroma Key TOP")• [Circle ](<./Circle_TOP.md> "Circle TOP")• [Composite ](<./Composite_TOP.md> "Composite TOP")• [Constant ](<./Constant_TOP.md> "Constant TOP")• [Convolve ](<./Convolve_TOP.md> "Convolve TOP")• [Corner Pin ](<./Corner_Pin_TOP.md> "Corner Pin TOP")• [CPlusPlus ](<./CPlusPlus_TOP.md> "CPlusPlus TOP")• [Crop ](<./Crop_TOP.md> "Crop TOP")• [Cross ](<./Cross_TOP.md> "Cross TOP")• [Cube Map ](<./Cube_Map_TOP.md> "Cube Map TOP")• [Depth ](<./Depth_TOP.md> "Depth TOP")• [Difference ](<./Difference_TOP.md> "Difference TOP")• [Direct Display Out ](<./Direct_Display_Out_TOP.md> "Direct Display Out TOP")• [DirectX In ](<./DirectX_In_TOP.md> "DirectX In TOP")• [DirectX Out ](<./DirectX_Out_TOP.md> "DirectX Out TOP")• [Displace ](<./Displace_TOP.md> "Displace TOP")• [Edge ](<./Edge_TOP.md> "Edge TOP")• [Emboss ](<./Emboss_TOP.md> "Emboss TOP")• [Feedback ](<./Feedback_TOP.md> "Feedback TOP")• [Fit ](<./Fit_TOP.md> "Fit TOP")• [Flip ](<./Flip_TOP.md> "Flip TOP")• [Function ](<./Function_TOP.md> "Function TOP")• [GLSL Multi ](<./GLSL_Multi_TOP.md> "GLSL Multi TOP")• [GLSL ](<./GLSL_TOP.md> "GLSL TOP")• [HSV Adjust ](<./HSV_Adjust_TOP.md> "HSV Adjust TOP")• [HSV to RGB ](<./HSV_to_RGB_TOP.md> "HSV to RGB TOP")• [Import Select ](<./Import_Select_TOP.md> "Import Select TOP")• [In ](<./In_TOP.md> "In TOP")• [Inside ](<./Inside_TOP.md> "Inside TOP")• [Introduction To s Vid ](<./Introduction_To_TOPs_Vid.md> "Introduction To TOPs Vid")• [Kinect Azure Select ](<./Kinect_Azure_Select_TOP.md> "Kinect Azure Select TOP")• [Kinect Azure ](<./Kinect_Azure_TOP.md> "Kinect Azure TOP")• [Kinect ](<./Kinect_TOP.md> "Kinect TOP")• [Layer Mix ](<./Layer_Mix_TOP.md> "Layer Mix TOP")• [Layer ](<./Layer_TOP.md> "Layer TOP")• [Layout ](<./Layout_TOP.md> "Layout TOP")• [Leap Motion ](<./Leap_Motion_TOP.md> "Leap Motion TOP")• [Lens Distort ](<./Lens_Distort_TOP.md> "Lens Distort TOP")• [Level ](<./Level_TOP.md> "Level TOP")• [Limit ](<./Limit_TOP.md> "Limit TOP")• [Lookup ](<./Lookup_TOP.md> "Lookup TOP")• [Luma Blur ](<./Luma_Blur_TOP.md> "Luma Blur TOP")• [Luma Level ](<./Luma_Level_TOP.md> "Luma Level TOP")• [Math ](<./Math_TOP.md> "Math TOP")• [Matte ](<./Matte_TOP.md> "Matte TOP")• [Mirror ](<./Mirror_TOP.md> "Mirror TOP")• [Monochrome ](<./Monochrome_TOP.md> "Monochrome TOP")• [MoSys ](<./MoSys_TOP.md> "MoSys TOP")• [Movie File In ](<./Movie_File_In_TOP.md> "Movie File In TOP")• [Movie File Out ](<./Movie_File_Out_TOP.md> "Movie File Out TOP")• [MPCDI ](<./MPCDI_TOP.md> "MPCDI TOP")• [Multiply ](<./Multiply_TOP.md> "Multiply TOP")• [Ncam ](<./Ncam_TOP.md> "Ncam TOP")• [NDI In ](<./NDI_In_TOP.md> "NDI In TOP")• [NDI Out ](<./NDI_Out_TOP.md> "NDI Out TOP")• [Noise ](<./Noise_TOP.md> "Noise TOP")• [Normal Map ](<./Normal_Map_TOP.md> "Normal Map TOP")• [Notch ](<./Notch_TOP.md> "Notch TOP")• [Null ](<./Null_TOP.md> "Null TOP")• [NVIDIA Background ](<./NVIDIA_Background_TOP.md> "NVIDIA Background TOP")• [NVIDIA Denoise ](<./NVIDIA_Denoise_TOP.md> "NVIDIA Denoise TOP")• [NVIDIA Flex ](<./NVIDIA_Flex_TOP.md> "NVIDIA Flex TOP")• [NVIDIA Flow ](<./NVIDIA_Flow_TOP.md> "NVIDIA Flow TOP")• [NVIDIA Upscaler ](<./NVIDIA_Upscaler_TOP.md> "NVIDIA Upscaler TOP")• [OAK Select ](<./OAK_Select_TOP.md> "OAK Select TOP")• [Oculus Rift ](<./Oculus_Rift_TOP.md> "Oculus Rift TOP")• [OP Viewer ](<./OP_Viewer_TOP.md> "OP Viewer TOP")• [OpenColorIO ](<./OpenColorIO_TOP.md> "OpenColorIO TOP")• [OpenVR ](<./OpenVR_TOP.md> "OpenVR TOP")• [Optical Flow ](<./Optical_Flow_TOP.md> "Optical Flow TOP")• [Orbbec Select ](<./Orbbec_Select_TOP.md> "Orbbec Select TOP")• Orbbec • [Ouster Select ](<./Ouster_Select_TOP.md> "Ouster Select TOP")• [Ouster ](<./Ouster_TOP.md> "Ouster TOP")• [Out ](<./Out_TOP.md> "Out TOP")• [Outside ](<./Outside_TOP.md> "Outside TOP")• [Over ](<./Over_TOP.md> "Over TOP")• [Pack ](<./Pack_TOP.md> "Pack TOP")• [Photoshop In ](<./Photoshop_In_TOP.md> "Photoshop In TOP")• [Point File In ](<./Point_File_In_TOP.md> "Point File In TOP")• [Point File Select ](<./Point_File_Select_TOP.md> "Point File Select TOP")• [Point Transform ](<./Point_Transform_TOP.md> "Point Transform TOP")• [POP to ](<./POP_to_TOP.md> "POP to TOP")• [PreFilter Map ](<./PreFilter_Map_TOP.md> "PreFilter Map TOP")• [Projection ](<./Projection_TOP.md> "Projection TOP")• [Ramp ](<./Ramp_TOP.md> "Ramp TOP")• [RealSense ](<./RealSense_TOP.md> "RealSense TOP")• [Rectangle ](<./Rectangle_TOP.md> "Rectangle TOP")• [Remap ](<./Remap_TOP.md> "Remap TOP")• [Render Pass ](<./Render_Pass_TOP.md> "Render Pass TOP")• [Render Select ](<./Render_Select_TOP.md> "Render Select TOP")• [Render Simple ](<./Render_Simple_TOP.md> "Render Simple TOP")• [Render ](<./Render_TOP.md> "Render TOP")• [RenderStream In ](<./RenderStream_In_TOP.md> "RenderStream In TOP")• [RenderStream Out ](<./RenderStream_Out_TOP.md> "RenderStream Out TOP")• [Reorder ](<./Reorder_TOP.md> "Reorder TOP")• [Resolution ](<./Resolution_TOP.md> "Resolution TOP")• [RGB Key ](<./RGB_Key_TOP.md> "RGB Key TOP")• [RGB to HSV ](<./RGB_to_HSV_TOP.md> "RGB to HSV TOP")• [Scalable Display ](<./Scalable_Display_TOP.md> "Scalable Display TOP")• [Screen Grab ](<./Screen_Grab_TOP.md> "Screen Grab TOP")• [Screen ](<./Screen_TOP.md> "Screen TOP")• [Script ](<./Script_TOP.md> "Script TOP")• [Select ](<./Select_TOP.md> "Select TOP")• [Shared Mem In ](<./Shared_Mem_In_TOP.md> "Shared Mem In TOP")• [Shared Mem Out ](<./Shared_Mem_Out_TOP.md> "Shared Mem Out TOP")• [SICK ](<./SICK_TOP.md> "SICK TOP")• [Slope ](<./Slope_TOP.md> "Slope TOP")• [Spectrum ](<./Spectrum_TOP.md> "Spectrum TOP")• [SSAO ](<./SSAO_TOP.md> "SSAO TOP")• [ST2110 In ](<./ST2110_In_TOP.md> "ST2110 In TOP")• [ST2110 Out ](<./ST2110_Out_TOP.md> "ST2110 Out TOP")• [Stype ](<./Stype_TOP.md> "Stype TOP")• [Substance Select ](<./Substance_Select_TOP.md> "Substance Select TOP")• [Substance ](<./Substance_TOP.md> "Substance TOP")• [Subtract ](<./Subtract_TOP.md> "Subtract TOP")• [SVG ](<./SVG_TOP.md> "SVG TOP")• [Switch ](<./Switch_TOP.md> "Switch TOP")• [Syphon Spout In ](<./Syphon_Spout_In_TOP.md> "Syphon Spout In TOP")• [Syphon Spout Out ](<./Syphon_Spout_Out_TOP.md> "Syphon Spout Out TOP")• [Text ](<./Text_TOP.md> "Text TOP")• [Texture 3D ](<./Texture_3D_TOP.md> "Texture 3D TOP")• [Texture Sampling Parameters ](<./Texture_Sampling_Parameters.md> "Texture Sampling Parameters")• [Threshold ](<./Threshold_TOP.md> "Threshold TOP")• [Tile ](<./Tile_TOP.md> "Tile TOP")• [Time Machine ](<./Time_Machine_TOP.md> "Time Machine TOP")• [Tone Map ](<./Tone_Map_TOP.md> "Tone Map TOP")• [TOP ](<./TOP.md> "TOP")• [TOP Viewer ](<./TOP_Viewer.md> "TOP Viewer")• [Touch In ](<./Touch_In_TOP.md> "Touch In TOP")• [Touch Out ](<./Touch_Out_TOP.md> "Touch Out TOP")• [Transform ](<./Transform_TOP.md> "Transform TOP")• [Under ](<./Under_TOP.md> "Under TOP")• [Video Device In ](<./Video_Device_In_TOP.md> "Video Device In TOP")• [Video Device Out ](<./Video_Device_Out_TOP.md> "Video Device Out TOP")• [Video Stream In ](<./Video_Stream_In_TOP.md> "Video Stream In TOP")• [Video Stream Out ](<./Video_Stream_Out_TOP.md> "Video Stream Out TOP")• [Vioso ](<./Vioso_TOP.md> "Vioso TOP")• [Web Render ](<./Web_Render_TOP.md> "Web Render TOP")• [ZED Select ](<./ZED_Select_TOP.md> "ZED Select TOP")• [ZED ](<./ZED_TOP.md> "ZED TOP")
