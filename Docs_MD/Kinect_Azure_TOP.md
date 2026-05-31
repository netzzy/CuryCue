# Kinect Azure TOP

##   
  
Summary

**NOTE**

**OS:** This operator is only supported under the **Microsoft Windows 10 April 2018 or newer** operating system.  


The Kinect Azure TOP can be used to configure and capture data from a Microsoft Kinect Azure camera or a Kinect compatible [Orbbec](<./Orbbec.md> "Orbbec") camera (Femto Mega, Femto Bolt, etc). 

The TOP can be used to configure the settings of the camera (resolution, frame rate, synchronization, etc) as well to retrieve captured images from either its color or depth cameras. Image data from one camera can be remapped (aligned) to the other camera in order to match color and depth information. Only one Kinect Azure TOP can be connected to a single Kinect camera. To retrieve additional images from the same camera, use a [Kinect Azure Select TOP](<./Kinect_Azure_Select_TOP.md> "Kinect Azure Select TOP"). 

The Kinect Azure can also extract body tracking information and skeleton positions using the depth camera image. To access this data, use a [Kinect Azure CHOP](<./Kinect_Azure_CHOP.md> "Kinect Azure CHOP") and set its Kinect TOP parameter to the primary Kinect Azure TOP that is connected to the device. **Note:** While both Microsoft and Orbbec hardware can be used in the same project, only one hardware type can have body tracking enabled at any one time. Body tracking is required for the Player Index image or to obtain skeleton data. If body tracking is not required from the Orbbec, it is recommended to use the native [Orbbec TOP](<./Orbbec_TOP.md> "Orbbec TOP") instead. 

**Note:** The Orbbec Femto Mega does not automatically support ethernet connections using the Kinect Azure TOP or CHOP. However, you can enable detection of ethernet devices using an external configuration file places alongside your toe file. Ethernet connections only support depth and IR images, color video is only supported over USB. For further information on the file see the [Orbbec documentaion](<https://www.orbbec.com/documentation-mega/k4a-access-femtomega-network-mode/>). 

**Warning:** When working with Orbbec hardware, using both Kinect Azure and Orbbec nodes in the same project may lead to instability. It is recommended to use either all Kinect Azure or all Orbbec nodes depending on project requirements. 

**TIP:** See Elburz' video on using KinectAzure's point clouds and a bunch of Azure general tips. [Kinect Azure Point Cloud in TouchDesigner Tutorial](<https://www.youtube.com/watch?v=P_PjAr2Yzao>) on the Interactive and Immersive HQ. 

See also [Kinect Azure CHOP](<./Kinect_Azure_CHOP.md> "Kinect Azure CHOP"), [Kinect Azure Select TOP](<./Kinect_Azure_Select_TOP.md> "Kinect Azure Select TOP"), [Palette:pointRender](<./Palette-pointRender.md> "Palette:pointRender"), [Palette:kinectCalibration](<./Palette-kinectCalibration.md> "Palette:kinectCalibration"), [Palette:kinectRecorder](</index.php?title=Palette:kinectRecorder&action=edit&redlink=1> "Palette:kinectRecorder \(page does not exist\)"), [Palette:kinectPointcloud](<./Palette-kinectPointcloud.md> "Palette:kinectPointcloud"). 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[kinectazureTOP_Class](<./KinectazureTOP_Class.md> "KinectazureTOP Class")

## 

Parameters - Kinect Azure Page

Active`active`\- Enable or disable the camera. **Note** Disabling this TOP will also disable any other operators ([Kinect Azure Select TOP](<./Kinect_Azure_Select_TOP.md> "Kinect Azure Select TOP") or [Kinect Azure CHOP](<./Kinect_Azure_CHOP.md> "Kinect Azure CHOP")) that rely on it. 

Hardware Type`library`\- ⊞ \- Choose whether you are using Microsoft Kinect Azure hardware or a Kinect compatible Orbbec camera (Femto Mega, Femto Bolt, etc). Both camera types can be used together in the same project, but only one hardware type can enable body tracking at any one time. 
* Microsoft Kinect Azure`microsoft`\- Select this option if you are using an original Microsoft Kinect Azure camera.
* Orrbec Compatible (Femto Mega, Femto Bolt, ...)`orbbec`\- Selection this option for a Kinect compatible Orbbec camera e.g. Femto Mega, Femto Bolt, etc. Not all Orbbec cameras are compatible with the Kinect Azure. For general Orbbec support use an [Orbbec TOP](<./Orbbec_TOP.md> "Orbbec TOP").


Sensor`sensor`\- The serial number of the connected Kinect Azure camera. The TOP will automatically fill the list with all available cameras. Note: Only one Kinect Azure TOP should be connected to a single camera. 

Camera FPS`fps`\- ⊞ \- Controls the frame rate of both the color and depth cameras. Some higher camera resolutions are not supported when running at 30FPS. Lower framerates can produce brighter color images in low light conditions. 
* 5 FPS`fps5`-
* 15 FPS`fps15`-
* 30 FPS`fps30`-


Color Resolution`colorres`\- ⊞ \- The resolution of images captured by the color camera. Different resolutions may have different aspect ratios. Note: 4096 x 3072 is not supported at 30 FPS. 
* 1280 x 720 (16:9)`1280x720`-
* 1920 x 1080 (16:9)`1920x1080`-
* 2560 x 1440 (16:9)`2560x1440`-
* 2048 x 1536 (4:3)`2048x1536`-
* 3840 x 2160 (16x9)`3840x2160`-
* 4096 x 3072 (4x3)`4096x3072`\- Note: This resolution is not supported when operating at 30FPS. Reduce the framerate to 15 or 5 FPS to use this setting.


Depth Mode`depthmode`\- ⊞ \- The depth mode controls which of the Kinect's two depth cameras (Wide or Narrow FOV) are used to produce the depth image and whether any 'binning' is used to process the data. In 'binned' modes, 2x2 blocks of pixels are combined to produce a filter, lower resolution image. Note: Body tracking is not supported when using the Passive IR depth mode. 
* Narrow FOV - Unbinned (640x576)`narrowunbinned`-
* Wide FOV - 2x2 Binned (512x512)`widebinned`-
* Narrow FOV - 2x2 Binned (320x288)`narrowbinned`\- Note: This mode is not recommended for use with body tracking.
* Wide FOV - Unbinned (1024x1024)`wideunbinned`\- Note: This mode is not supported at 30FPS and is not recommended for use with body tracking.
* Passive IR (1024x1024)`passiveir`\- Note: This mode does not support body tracking.


Body Tracking Model`modelpath`\- The file path to the ONNX model that performs body tracking features. TouchDesigner includes the regular and lite models that are part of the Kinect Azure SDK. 

Body Tracking Processing Mode`proccessingmode`\- ⊞ \- Determines how the body tracking model is processed. The default mode runs mostly on the GPU (supports Nvidia, AMD and Intel), but this can also be switched to a CPU mode when a compatible GPU is not available. 
* GPU Default`gpudefault`\- The default processing mode. It is equivalent to DirectML when running on Windows.
* CPU`cpu`\- The AI model will run on the CPU instead of the graphics cards. This is notably slower and not recommended for production release.
* DirectML`directml`\- Equivalent to the default mode when running on Windows. The AI model will run on the GPU. This is compatible with Nvidia, AMD and Intel GPUs.


Body Tracking GPU Device`gpu`\- The device number of the GPU to use when there are multiple GPUs in the system. The ordering system may be dependent on the GPU manufacturer. 

Sensor Orientation`orientation`\- ⊞ \- Used to indicate when the camera is mounted in a non-upright position. This can help improve body-tracking results. 
* Default`default`-
* Clockwise 90 Degrees`cw90`-
* Counterclockwise 90 Degrees`ccw90`-
* Flipped 180 Degrees`flipped`-


Image`image`\- ⊞ \- A list of available image types to capture from the device and display in this TOP. All image types have a second version that is mapped (aligned) to the image space of the other camera so that color and depth image data can be matched. The resolution of the image is controlled by the Color Resolution or Depth Mode parameters depending on the type of image selected. Use a [Kinect Azure Select TOP](<./Kinect_Azure_Select_TOP.md> "Kinect Azure Select TOP") to access additional image types from the same camera. 
* Color`color`\- An 8-bit RGBA image from the color camera.
* Color aligned to Depth`colorremap`\- The color camera image remapped to align with the current depth camera image. The resolution is determined by the Depth Mode.
* Depth`depth`\- A single channel 32bit floating point depth image where pixel values measure the distance in meters from the camera. Resolution and field of view are determined by the Depth Mode parameter.
* Depth aligned to Color`depthremap`\- The depth image remapped to align with the current color camera image. The resolution is determined by the Color Resolution parameter.
* IR`ir`\- A 16-bit integer infrared image captured by the depth camera. Resolution and field of view are determined by the Depth Mode.
* IR aligned to Color`irremap`\- The infrared image remapped to align the current color camera image. The resolution is determined by the Color Resolution parameter.
* Player Index`playerindex`\- An 8-bit single channel image that maps pixels to players that have been identified by the body tracking system. Pixel values represent the body id multiplied by 25 to improve contrast. Note: The player index map may have additional hardware requirements (CUDA capable graphics card) and may not synchronize with the color or depth images depending on current settings. The resolution is determined by the current Depth Mode.
* Player Index aligned to Color`playerindexremap`\- The player index map remapped to align with the current color image. The resolution is determined by the Color Resolution parameter.
* Point Cloud`pointcloud`\- A 32bit floating point RGBA image where the depth information has been converted into XYZ positions that are stored in the RGB channels. Position data is represented in meters and the resolution and field of view are determined by the Depth Mode. The Point Cloud image can be viewed in 3D by activating the TOP and selecting 'View as Points' in the right-click menu, or by using the TOP as an instance source in the Geometry COMP.
* Point Cloud aligned to Color`pointcloudremap`\- The point cloud image remapped to align with the current color image. Note: Remapping the image can create gaps and artifacts when view the points in 3D.


Align Image to Other Camera`remapimage`\- When enabled, the current image will be remapped to align with images from the other camera. For example, use this feature to create a color camera image that maps to the pixels of the depth camera. 

The current depth mode and color resolution will be used to do the remapping. Note: Remapping the point cloud image can create artifacts in the distribution of points due to gaps in the remapping algorithm. __

Sync Image to Body Tracking`bodyimage`\- When enabled, the image produced will be delayed so that it corresponds to the most recent data in the body tracking system. The amount of delay may fluctuate based on the power of the processor doing the body tracking and the complexity of the scene. A [Kinect Azure Select TOP](<./Kinect_Azure_Select_TOP.md> "Kinect Azure Select TOP") can be used at the same time to retrieve the real-time image stream. 

Mirror Image`mirrorimage`\- Flip the image in the horizontal axis. 

CPU Body Tracking`cpu`\- When enabled, body tracking calculations will be done on the CPU rather than on the graphics card. This method is much slower, but does not require a high-powered graphics card to function. 

## 

Parameters - Color Page

Use the controls on the Color page to adjust the output of the color camera. 

Reset Color Controls`resetcolors`\- Reset all of the color controls to the camera's defaults. These vary per camera and may be different than the parameter defaults. 

Enable Color Controls`enablecolors`\- Turn on to enable adjustment controls for the color camera. When disabled, the previous color settings will remain in place. Use the Reset Color Controls button to switch the camera back to its default settings. 

Manual Exposure`manualexposure`\- Enable to allow setting the exposure time manually. When disabled, the camera will automatically choose an exposure based on the light levels and frame rate. 

Note: This feature may not work correctly due to issues in the current Kinect SDK. __

Exposure Time`exposure`\- Adjust the exposure time of the color image measured in microseconds. The time must be less than one frame. 

Note: This feature may not work correctly due to issues in the current Kinect SDK. __

Manual White Balance`manualwhitebalance`\- Enable to allow setting the camera white balance manually. 

White Balance`whitebalance`\- Select the temperature in degrees Kelvin used to set the white balance of the image. The value is rounded to the nearest 10 degrees. 

Brightness`brightness`\- Used to adjust the brightness of the image from 0 to 255. 128 is the default. 

Contrast`contrast`\- Conrtols the contrast of the color image. 

Saturation`saturation`\- Controls the saturation of the color image. 

Sharpness`sharpness`\- Adjusts the sharpness of the color image. 

Gain`gain`\- The gain of the color image. 

Backlight Compensation`backlight`\- Enables compensation for bright back lighting in a scene. 

Powerline Frequency`powerfreq`\- ⊞ \- Select the frequency of the power supply for use in the cameras noise cancellation system. 
* 50Hz`50hz`-
* 60Hz`60hz`-

## 

Parameters - Timing Page

Depth Image Delay`depthdelay`\- A delay in microseconds between when the depth and color images are captured. The delay must be less than one frame in length based on the current framerate. 

Wired Sync Mode`syncmode`\- ⊞ \- When using more than one Kinect Azure camera, this setting can be used to determine which unit is the master and which are subordinates. 
* Standalone`standalone`-
* Master`master`-
* Subordinate`subordinate`-


Subordinate Delay`subdelay`\- A delay in microseconds between when the master unit captures an image and when this device captures an image. (Only applicable for subordinate devices). 

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

Extra Information for the Kinect Azure TOP can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). 

### 

Specific Kinect Azure TOP Info Channels
* image_frame \- The number of image frames processed by the camera.
* bodytracking_frame \- The number of body tracking frames processed by the camera.
* color_timestamp \- The camera timestamp in microseconds of the latest frame from the color camera.
* depth_timestamp \- The camera timestamp in microseconds of the latest frame from the depth camera.
* bodytracking_timestamp \- The timestamp in microseconds of the frame used to calculate body tracking data.
* image_errors \- The total number of errors produced by the image system.
* bodytracking_errors \- The total number of errors procuded by the body tracking system.

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


  
TouchDesigner Build: Latest\nwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditor2023.112802021.100002020.20000before 2020.20000

TOPs   
---  
[Add ](<./Add_TOP.md> "Add TOP")• [Analyze ](<./Analyze_TOP.md> "Analyze TOP")• [Anti Alias ](<./Anti_Alias_TOP.md> "Anti Alias TOP")• [Blob Track ](<./Blob_Track_TOP.md> "Blob Track TOP")• [Bloom ](<./Bloom_TOP.md> "Bloom TOP")• [Blur ](<./Blur_TOP.md> "Blur TOP")• [Cache Select ](<./Cache_Select_TOP.md> "Cache Select TOP")• [Cache ](<./Cache_TOP.md> "Cache TOP")• [Channel Mix ](<./Channel_Mix_TOP.md> "Channel Mix TOP")• [CHOP to ](<./CHOP_to_TOP.md> "CHOP to TOP")• [Chroma Key ](<./Chroma_Key_TOP.md> "Chroma Key TOP")• [Circle ](<./Circle_TOP.md> "Circle TOP")• [Composite ](<./Composite_TOP.md> "Composite TOP")• [Constant ](<./Constant_TOP.md> "Constant TOP")• [Convolve ](<./Convolve_TOP.md> "Convolve TOP")• [Corner Pin ](<./Corner_Pin_TOP.md> "Corner Pin TOP")• [CPlusPlus ](<./CPlusPlus_TOP.md> "CPlusPlus TOP")• [Crop ](<./Crop_TOP.md> "Crop TOP")• [Cross ](<./Cross_TOP.md> "Cross TOP")• [Cube Map ](<./Cube_Map_TOP.md> "Cube Map TOP")• [Depth ](<./Depth_TOP.md> "Depth TOP")• [Difference ](<./Difference_TOP.md> "Difference TOP")• [Direct Display Out ](<./Direct_Display_Out_TOP.md> "Direct Display Out TOP")• [DirectX In ](<./DirectX_In_TOP.md> "DirectX In TOP")• [DirectX Out ](<./DirectX_Out_TOP.md> "DirectX Out TOP")• [Displace ](<./Displace_TOP.md> "Displace TOP")• [Edge ](<./Edge_TOP.md> "Edge TOP")• [Emboss ](<./Emboss_TOP.md> "Emboss TOP")• [Feedback ](<./Feedback_TOP.md> "Feedback TOP")• [Fit ](<./Fit_TOP.md> "Fit TOP")• [Flip ](<./Flip_TOP.md> "Flip TOP")• [Function ](<./Function_TOP.md> "Function TOP")• [GLSL Multi ](<./GLSL_Multi_TOP.md> "GLSL Multi TOP")• [GLSL ](<./GLSL_TOP.md> "GLSL TOP")• [HSV Adjust ](<./HSV_Adjust_TOP.md> "HSV Adjust TOP")• [HSV to RGB ](<./HSV_to_RGB_TOP.md> "HSV to RGB TOP")• [Import Select ](<./Import_Select_TOP.md> "Import Select TOP")• [In ](<./In_TOP.md> "In TOP")• [Inside ](<./Inside_TOP.md> "Inside TOP")• [Introduction To s Vid ](<./Introduction_To_TOPs_Vid.md> "Introduction To TOPs Vid")• [Kinect Azure Select ](<./Kinect_Azure_Select_TOP.md> "Kinect Azure Select TOP")• Kinect Azure • [Kinect ](<./Kinect_TOP.md> "Kinect TOP")• [Layer Mix ](<./Layer_Mix_TOP.md> "Layer Mix TOP")• [Layer ](<./Layer_TOP.md> "Layer TOP")• [Layout ](<./Layout_TOP.md> "Layout TOP")• [Leap Motion ](<./Leap_Motion_TOP.md> "Leap Motion TOP")• [Lens Distort ](<./Lens_Distort_TOP.md> "Lens Distort TOP")• [Level ](<./Level_TOP.md> "Level TOP")• [Limit ](<./Limit_TOP.md> "Limit TOP")• [Lookup ](<./Lookup_TOP.md> "Lookup TOP")• [Luma Blur ](<./Luma_Blur_TOP.md> "Luma Blur TOP")• [Luma Level ](<./Luma_Level_TOP.md> "Luma Level TOP")• [Math ](<./Math_TOP.md> "Math TOP")• [Matte ](<./Matte_TOP.md> "Matte TOP")• [Mirror ](<./Mirror_TOP.md> "Mirror TOP")• [Monochrome ](<./Monochrome_TOP.md> "Monochrome TOP")• [MoSys ](<./MoSys_TOP.md> "MoSys TOP")• [Movie File In ](<./Movie_File_In_TOP.md> "Movie File In TOP")• [Movie File Out ](<./Movie_File_Out_TOP.md> "Movie File Out TOP")• [MPCDI ](<./MPCDI_TOP.md> "MPCDI TOP")• [Multiply ](<./Multiply_TOP.md> "Multiply TOP")• [Ncam ](<./Ncam_TOP.md> "Ncam TOP")• [NDI In ](<./NDI_In_TOP.md> "NDI In TOP")• [NDI Out ](<./NDI_Out_TOP.md> "NDI Out TOP")• [Noise ](<./Noise_TOP.md> "Noise TOP")• [Normal Map ](<./Normal_Map_TOP.md> "Normal Map TOP")• [Notch ](<./Notch_TOP.md> "Notch TOP")• [Null ](<./Null_TOP.md> "Null TOP")• [NVIDIA Background ](<./NVIDIA_Background_TOP.md> "NVIDIA Background TOP")• [NVIDIA Denoise ](<./NVIDIA_Denoise_TOP.md> "NVIDIA Denoise TOP")• [NVIDIA Flex ](<./NVIDIA_Flex_TOP.md> "NVIDIA Flex TOP")• [NVIDIA Flow ](<./NVIDIA_Flow_TOP.md> "NVIDIA Flow TOP")• [NVIDIA Upscaler ](<./NVIDIA_Upscaler_TOP.md> "NVIDIA Upscaler TOP")• [OAK Select ](<./OAK_Select_TOP.md> "OAK Select TOP")• [Oculus Rift ](<./Oculus_Rift_TOP.md> "Oculus Rift TOP")• [OP Viewer ](<./OP_Viewer_TOP.md> "OP Viewer TOP")• [OpenColorIO ](<./OpenColorIO_TOP.md> "OpenColorIO TOP")• [OpenVR ](<./OpenVR_TOP.md> "OpenVR TOP")• [Optical Flow ](<./Optical_Flow_TOP.md> "Optical Flow TOP")• [Orbbec Select ](<./Orbbec_Select_TOP.md> "Orbbec Select TOP")• [Orbbec ](<./Orbbec_TOP.md> "Orbbec TOP")• [Ouster Select ](<./Ouster_Select_TOP.md> "Ouster Select TOP")• [Ouster ](<./Ouster_TOP.md> "Ouster TOP")• [Out ](<./Out_TOP.md> "Out TOP")• [Outside ](<./Outside_TOP.md> "Outside TOP")• [Over ](<./Over_TOP.md> "Over TOP")• [Pack ](<./Pack_TOP.md> "Pack TOP")• [Photoshop In ](<./Photoshop_In_TOP.md> "Photoshop In TOP")• [Point File In ](<./Point_File_In_TOP.md> "Point File In TOP")• [Point File Select ](<./Point_File_Select_TOP.md> "Point File Select TOP")• [Point Transform ](<./Point_Transform_TOP.md> "Point Transform TOP")• [POP to ](<./POP_to_TOP.md> "POP to TOP")• [PreFilter Map ](<./PreFilter_Map_TOP.md> "PreFilter Map TOP")• [Projection ](<./Projection_TOP.md> "Projection TOP")• [Ramp ](<./Ramp_TOP.md> "Ramp TOP")• [RealSense ](<./RealSense_TOP.md> "RealSense TOP")• [Rectangle ](<./Rectangle_TOP.md> "Rectangle TOP")• [Remap ](<./Remap_TOP.md> "Remap TOP")• [Render Pass ](<./Render_Pass_TOP.md> "Render Pass TOP")• [Render Select ](<./Render_Select_TOP.md> "Render Select TOP")• [Render Simple ](<./Render_Simple_TOP.md> "Render Simple TOP")• [Render ](<./Render_TOP.md> "Render TOP")• [RenderStream In ](<./RenderStream_In_TOP.md> "RenderStream In TOP")• [RenderStream Out ](<./RenderStream_Out_TOP.md> "RenderStream Out TOP")• [Reorder ](<./Reorder_TOP.md> "Reorder TOP")• [Resolution ](<./Resolution_TOP.md> "Resolution TOP")• [RGB Key ](<./RGB_Key_TOP.md> "RGB Key TOP")• [RGB to HSV ](<./RGB_to_HSV_TOP.md> "RGB to HSV TOP")• [Scalable Display ](<./Scalable_Display_TOP.md> "Scalable Display TOP")• [Screen Grab ](<./Screen_Grab_TOP.md> "Screen Grab TOP")• [Screen ](<./Screen_TOP.md> "Screen TOP")• [Script ](<./Script_TOP.md> "Script TOP")• [Select ](<./Select_TOP.md> "Select TOP")• [Shared Mem In ](<./Shared_Mem_In_TOP.md> "Shared Mem In TOP")• [Shared Mem Out ](<./Shared_Mem_Out_TOP.md> "Shared Mem Out TOP")• [SICK ](<./SICK_TOP.md> "SICK TOP")• [Slope ](<./Slope_TOP.md> "Slope TOP")• [Spectrum ](<./Spectrum_TOP.md> "Spectrum TOP")• [SSAO ](<./SSAO_TOP.md> "SSAO TOP")• [ST2110 In ](<./ST2110_In_TOP.md> "ST2110 In TOP")• [ST2110 Out ](<./ST2110_Out_TOP.md> "ST2110 Out TOP")• [Stype ](<./Stype_TOP.md> "Stype TOP")• [Substance Select ](<./Substance_Select_TOP.md> "Substance Select TOP")• [Substance ](<./Substance_TOP.md> "Substance TOP")• [Subtract ](<./Subtract_TOP.md> "Subtract TOP")• [SVG ](<./SVG_TOP.md> "SVG TOP")• [Switch ](<./Switch_TOP.md> "Switch TOP")• [Syphon Spout In ](<./Syphon_Spout_In_TOP.md> "Syphon Spout In TOP")• [Syphon Spout Out ](<./Syphon_Spout_Out_TOP.md> "Syphon Spout Out TOP")• [Text ](<./Text_TOP.md> "Text TOP")• [Texture 3D ](<./Texture_3D_TOP.md> "Texture 3D TOP")• [Texture Sampling Parameters ](<./Texture_Sampling_Parameters.md> "Texture Sampling Parameters")• [Threshold ](<./Threshold_TOP.md> "Threshold TOP")• [Tile ](<./Tile_TOP.md> "Tile TOP")• [Time Machine ](<./Time_Machine_TOP.md> "Time Machine TOP")• [Tone Map ](<./Tone_Map_TOP.md> "Tone Map TOP")• [TOP ](<./TOP.md> "TOP")• [TOP Viewer ](<./TOP_Viewer.md> "TOP Viewer")• [Touch In ](<./Touch_In_TOP.md> "Touch In TOP")• [Touch Out ](<./Touch_Out_TOP.md> "Touch Out TOP")• [Transform ](<./Transform_TOP.md> "Transform TOP")• [Under ](<./Under_TOP.md> "Under TOP")• [Video Device In ](<./Video_Device_In_TOP.md> "Video Device In TOP")• [Video Device Out ](<./Video_Device_Out_TOP.md> "Video Device Out TOP")• [Video Stream In ](<./Video_Stream_In_TOP.md> "Video Stream In TOP")• [Video Stream Out ](<./Video_Stream_Out_TOP.md> "Video Stream Out TOP")• [Vioso ](<./Vioso_TOP.md> "Vioso TOP")• [Web Render ](<./Web_Render_TOP.md> "Web Render TOP")• [ZED Select ](<./ZED_Select_TOP.md> "ZED Select TOP")• [ZED ](<./ZED_TOP.md> "ZED TOP")
