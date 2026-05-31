# Point Transform TOP

##   
  
Summary

The Point Transform TOP treats the RGB values of the input image as a point cloud of XYZ positions or vectors and performs 3D transformations and alignments. When the input type is set to 'Vector', translations are ignored and only rotation and scaling operations are performed. The alpha channel, if present, is passed along to the output image unchanged. 

Transformations can be defined directly on the Transform page, taken from an input CHOP (see [Transform CHOP](<./Transform_CHOP.md> "Transform CHOP")), using the Look At parameter, or as a combination of any of those methods. 

The Align page allows you to move or scale the point cloud relative to the origin, a 1x1x1 cube, or to a reference object. For example, you can scale the cloud to fit inside another point cloud or piece of geometry, or you can align the point cloud to sit on the XZ plane, or directly beside another cloud. 

The second input can optionally be used as a weight map to control how much of the transformation is applied to each individual point. 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[pointtransformTOP_Class](</PointtransformTOP_Class> "PointtransformTOP Class")

## 

Parameters - Transform Page

Input Type`inputtype`\- ⊞ \- Choose if the RGB channels of the input texture should be treated as positions or vectors. Vectors will not have the translation portion of the transform applied to them, and can be normalized before and/or after the transformation is applied. 
* Position`position`\- The RGB values represent XYZ positions.
* Vector`vector`\- The RGB values represent XYZ directions.


Normalize Input`innormalize`\- RGB input vectors are rescaled to a length of one before they are transformed. 

Normalize Output`outnormalize`\- RGB vectors are rescaled to a length of one after they are transformed. 

Transform Order`xord`\- ⊞ \- Changes the order that the translate, rotate and scale operations are performed on the input. Analogous to how you would end up in different locations if you were to move a block and turn east, versus turning east and then moving a block. In matrix math terms, if we use the 'multiply vector on the right' (column vector) convention, a transform order of Scale, Rotate, Translate would be written as T * R * S * Position 
* Scale Rotate Translate`srt`-
* Scale Translate Rotate`str`-
* Rotate Scale Translate`rst`-
* Rotate Translate Scale`rts`-
* Translate Scale Rotate`tsr`-
* Translate Rotate Scale`trs`-


Rotate Order`rord`\- ⊞ \- As with transform order (above), changing the order in which the rotations take place will alter the final position and orientation. A Rotation order of Rx Ry Rz would create the final rotation matrix as follows R = Rz * Ry * Rx 
* Rx Ry Rz`xyz`-
* Rx Rz Ry`xzy`-
* Ry Rx Rz`yxz`-
* Ry Rz Rx`yzx`-
* Rz Rx Ry`zxy`-
* Rz Ry Rx`zyx`-


Translate`t`\- ⊞ \- Move the input positions in the X, Y and Z axes. If the input is set to 'Vector', the translate values will have no effect. 
* Translate`tx`-
* Translate`ty`-
* Translate`tz`-


Rotate`r`\- ⊞ \- Rotate the input RGB values around the corresponding X, Y and Z axes. Angles are given in degrees. 
* Rotate`rx`-
* Rotate`ry`-
* Rotate`rz`-


Scale`s`\- ⊞ \- Scale the input RGB values in the corresponding X, Y and Z axes. If 'Normalize Output' is on, then all output values will be rescaled to a length of one regardless of the scale values. 
* Scale`sx`-
* Scale`sy`-
* Scale`sz`-


Pivot`p`\- ⊞ \- The pivot is the point about which the input points or vectors are scaled and rotated. Altering the pivot point produces different results depending on the transformation performed on the object. 
* Pivot`px`-
* Pivot`py`-
* Pivot`pz`-


Uniform Scale`scale`\- Scale the input values along all axes simultaneously. 

Invert`invert`\- Invert the transformation i.e. preform the reverse movements. 

Look At`lookat`\- Allows you to orient your input points by naming the object you would like them to Look At, or point to. Once you have designated this object to look at, it will continue to face that object, even if you move it. 

Up Vector`upvector`\- ⊞ \- When orienting an object towards the 'Look At' target, the Up Vector is used to determine where the positive Y axis points. 
* Up Vector`upvectorx`-
* Up Vector`upvectory`-
* Up Vector`upvectorz`-


Forward Direction`forwarddir`\- ⊞ \- Sets which axis and direction is considered the forward direction. 
* +X`posx`-
* -X`negx`-
* +Y`posy`-
* -Y`negy`-
* +Z`posz`-
* -Z`negz`-


Transform CHOP`chopinput`\- Path to a CHOP node with channels describing a 3D transformation. These channels may come from a [Transform CHOP](<./Transform_CHOP.md> "Transform CHOP") or another CHOP with the correct channels defined. 

Multiply Order`multiplyorder`\- ⊞ \- Controls whether the transformation from the given CHOP is applied to the input values before or after the transformation describe by this node. 
* Input, then Transform Page`inputxformpage`-
* Transform Page, then Input`xformpageinput`-

## 

Parameters - Weights Page

Weight Channel`weightchannel`\- ⊞ \- Select how to use the colors of the second input image as weights for transforming the points of the first input. 
* Luminance`luminance`-
* Red`red`-
* Green`green`-
* Blue`blue`-
* Alpha`alpha`-
* RGB Average`rgbaverage`-
* RGBA Average`average`-
* RGB Maximum`rgbmax`-
* RGBA Maximum`max`-
* RGBA Independent`independent`-


Weight Range`weightrange`\- ⊞ \- Set the range of weight values used to control how much of the transformation is applied to a point. Points with the minimum weight will **not** be transformed, while points with the maximum weight will be **fully** transformed. A linear interpolation is applied to points with weights that fall between the minimum and maximum. 
* Weight Range`weightrange1`-
* Weight Range`weightrange2`-

## 

Parameters - Align Page

These operations allow you to align the input points to the origin or to another reference object before or after the transformation has been applied. For example, you can recenter the transformed point cloud on the origin or position it directly next to another point cloud. **Note:** Align operations incur additional performance costs because they must calculate the dimensions of all points in the input. 

Align Transform Order`alignxformorder`\- ⊞ \- Determines the order that align operations are performed on the input points. **Note** : Unlike Scaling on the transform page, the alignment scale is always done relative to the center of the point cloud so that the point cloud's center does not change. 
* Transform, then Align`transformalign`-
* Align, then Transform`aligntransform`-


Reference Node`alignref`\- A path to a TOP or SOP node used to align the input points after the transformation. **Note** Using another point cloud TOP as a reference will incur additional performance costs because of the need to calculate the dimensions of the reference points. 

Align Operation Order`alignopord`\- ⊞ \- Set the order in which scale and transform is applied when aligning. 
* Scale Translate`st`-
* Translate Scale`ts`-


Align Translate X`aligntx`\- ⊞ \- Determines the final position of points along the X axis i.e. shifts values in the red channel. 
* Off`off`\- X values are not moved.
* Origin`origin`\- X values are aligned relative to the origin i.e. zero.
* Reference Input`reference`\- X values are aligned relative to the X position of the reference node.


From Input`fromx`\- ⊞ \- Determines how the points are aligned relative to the dimensions of the input points. 
* Min`min`\- Points are aligned relative to the lowest X value.
* Center`center`\- Points are aligned relative to the center of the X values.
* Max`max`\- Points are aligned relative to the highest X value.


To Reference`tox`\- ⊞ \- Determines how the final points are aligned relative to the reference node. 
* Min`min`\- Points are aligned with the lowest X value in the reference node.
* Center`center`\- Points are aligned with the center of the X values in the reference node.
* Max`max`\- Points are aligned with the highest X value in the reference node.


Align Translate Y`alignty`\- ⊞ \- Determines the final position of points along the Y axis i.e. shifts values in the green channel. 
* Off`off`\- Y values are not moved.
* Origin`origin`\- Y values are aligned relative to the origin i.e. zero.
* Reference Input`reference`\- Y values are aligned relative to the X position of the reference node.


From Input`fromy`\- ⊞ \- Determines how the points are aligned relative to the dimensions of the input points. 
* Min`min`\- Points are aligned relative to the lowest Y value.
* Center`center`\- Points are aligned relative to the center of the Y values.
* Max`max`\- Points are aligned relative to the highest Y value.


To Reference`toy`\- ⊞ \- Determines how the final points are aligned relative to the reference node. 
* Min`min`\- Points are aligned with the lowest Y value in the reference node.
* Center`center`\- Points are aligned with the center of the Y values in the reference node.
* Max`max`\- Points are aligned with the highest Y value in the reference node.


Align Translate Z`aligntz`\- ⊞ \- Determines the final position of points along the Z axis i.e. shifts values in the blue channel. 
* Off`off`\- Z values are not moved.
* Origin`origin`\- Z values are aligned relative to the origin i.e. zero.
* Reference Input`reference`\- Z values are aligned relative to the X position of the reference node.


From Input`fromz`\- ⊞ \- Determines how the points are aligned relative to the dimensions of the input points. 
* Min`min`\- Points are aligned relative to the lowest Z value.
* Center`center`\- Points are aligned relative to the center of the Z values.
* Max`max`\- Points are aligned relative to the highest Z value.


To Reference`toz`\- ⊞ \- Determines how the final points are aligned relative to the reference node. 
* Min`min`\- Points are aligned relative to the lowest Z value.
* Center`center`\- Points are aligned relative to the center of the Z values.
* Max`max`\- Points are aligned relative to the highest Z value.


Align Scale`alignscale`\- ⊞ \- The Align Scale can be used to resize the point cloud to fit inside the given bounds. Scaling can be done per axis (maintaining proportions or stretching), or on all axes. 
* Per Axis`peraxis`\- Scaling is controlled separately per-axis using the parameters below. **Note:** It is possible to have conflicting scales when setting limits on multiple axes.
* Unity`unity`\- The point cloud is resized to fit within a 1x1x1 cube. Proportions are maintained so that the largest dimension will have a length of 1.
* Reference`reference`\- The point cloud is resized to fit within the dimensions of the reference object. Proportions are maintained.


Align Scale X`alignscalex`\- ⊞ \- The point cloud is resized based on its width in the X axis. 
* Off`off`\- No scaling is done based on the X axis.
* Unity`unity`\- The point cloud is resized along the X axis so that the total width is 1. This does not affect the other axes and will distort the overall shape of the cloud.
* Reference Input`reference`\- The point cloud is resized along the X axis to the width of the reference object. This does not affect the other axes and will distort the overall shape of the cloud.
* Unity Proportional`unityprop`\- The point cloud is resized so that the total width in the X axis is 1. Other axes are scaled accordingly to maintain proportions.
* Reference Proportional`referenceprop`\- The point cloud is resized to match the width of the reference object. Other axes are scaled accordingly to maintain proportions.
* Unity Proportional`unityprop`-


Align Scale Y`alignscaley`\- ⊞ \- The point cloud is resized based on its height in the Y axis. 
* Off`off`\- No scaling is done based on the Y axis.
* Unity`unity`\- The point cloud is resized along the Y axis so that the total height is 1. This does not affect the other axes and will distort the overall shape of the cloud.
* Reference Input`reference`\- The point cloud is resized along the Y axis to the height of the reference object. This does not affect the other axes and will distort the overall shape of the cloud.
* Unity Proportional`unityprop`\- The point cloud is resized so that the total height in the Y axis is 1. Other axes are scaled accordingly to maintain proportions.
* Reference Proportional`referenceprop`\- The point cloud is resized to match the height of the reference object. Other axes are scaled accordingly to maintain proportions.


Align Scale Z`alignscalez`\- ⊞ \- The point cloud is resized based on its depth in the Z axis. 
* Off`off`\- No scaling is done based on the Z axis.
* Unity`unity`\- The point cloud is resized along the Z axis so that the total depth is 1. This does not affect the other axes and will distort the overall shape of the cloud.
* Reference Input`reference`\- The point cloud is resized along the Z axis to the depth of the reference object. This does not affect the other axes and will distort the overall shape of the cloud.
* Unity Proportional`unityprop`\- The point cloud is resized so that the total depth in the Z axis is 1. Other axes are scaled accordingly to maintain proportions.
* Reference Proportional`referenceprop`\- The point cloud is resized to match the depth of the reference object. Other axes are scaled accordingly to maintain proportions.

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
* Input 0: points \- The first input contains the position data of the points represented in the red, green, and blue channels.,
* Input 1: weights \- The second input contains an optional weight map that controls how much of the transformation is applied to each point. The weight channel and weight range parameters control how the color channels of the image are converted into weights.

## 

Info CHOP Channels

Extra Information for the Point Transform TOP can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). __

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


  
TouchDesigner Build: Latest\nwikieditorwikieditor2021.10000before 2021.10000

TOPs   
---  
[Add ](<./Add_TOP.md> "Add TOP")• [Analyze ](<./Analyze_TOP.md> "Analyze TOP")• [Anti Alias ](<./Anti_Alias_TOP.md> "Anti Alias TOP")• [Blob Track ](<./Blob_Track_TOP.md> "Blob Track TOP")• [Bloom ](<./Bloom_TOP.md> "Bloom TOP")• [Blur ](<./Blur_TOP.md> "Blur TOP")• [Cache Select ](<./Cache_Select_TOP.md> "Cache Select TOP")• [Cache ](<./Cache_TOP.md> "Cache TOP")• [Channel Mix ](<./Channel_Mix_TOP.md> "Channel Mix TOP")• [CHOP to ](<./CHOP_to_TOP.md> "CHOP to TOP")• [Chroma Key ](<./Chroma_Key_TOP.md> "Chroma Key TOP")• [Circle ](<./Circle_TOP.md> "Circle TOP")• [Composite ](<./Composite_TOP.md> "Composite TOP")• [Constant ](<./Constant_TOP.md> "Constant TOP")• [Convolve ](<./Convolve_TOP.md> "Convolve TOP")• [Corner Pin ](<./Corner_Pin_TOP.md> "Corner Pin TOP")• [CPlusPlus ](<./CPlusPlus_TOP.md> "CPlusPlus TOP")• [Crop ](<./Crop_TOP.md> "Crop TOP")• [Cross ](<./Cross_TOP.md> "Cross TOP")• [Cube Map ](<./Cube_Map_TOP.md> "Cube Map TOP")• [Depth ](<./Depth_TOP.md> "Depth TOP")• [Difference ](<./Difference_TOP.md> "Difference TOP")• [Direct Display Out ](<./Direct_Display_Out_TOP.md> "Direct Display Out TOP")• [DirectX In ](<./DirectX_In_TOP.md> "DirectX In TOP")• [DirectX Out ](<./DirectX_Out_TOP.md> "DirectX Out TOP")• [Displace ](<./Displace_TOP.md> "Displace TOP")• [Edge ](<./Edge_TOP.md> "Edge TOP")• [Emboss ](<./Emboss_TOP.md> "Emboss TOP")• [Feedback ](<./Feedback_TOP.md> "Feedback TOP")• [Fit ](<./Fit_TOP.md> "Fit TOP")• [Flip ](<./Flip_TOP.md> "Flip TOP")• [Function ](<./Function_TOP.md> "Function TOP")• [GLSL Multi ](<./GLSL_Multi_TOP.md> "GLSL Multi TOP")• [GLSL ](<./GLSL_TOP.md> "GLSL TOP")• [HSV Adjust ](<./HSV_Adjust_TOP.md> "HSV Adjust TOP")• [HSV to RGB ](<./HSV_to_RGB_TOP.md> "HSV to RGB TOP")• [Import Select ](<./Import_Select_TOP.md> "Import Select TOP")• [In ](<./In_TOP.md> "In TOP")• [Inside ](<./Inside_TOP.md> "Inside TOP")• [Introduction To s Vid ](<./Introduction_To_TOPs_Vid.md> "Introduction To TOPs Vid")• [Kinect Azure Select ](<./Kinect_Azure_Select_TOP.md> "Kinect Azure Select TOP")• [Kinect Azure ](<./Kinect_Azure_TOP.md> "Kinect Azure TOP")• [Kinect ](<./Kinect_TOP.md> "Kinect TOP")• [Layer Mix ](<./Layer_Mix_TOP.md> "Layer Mix TOP")• [Layer ](<./Layer_TOP.md> "Layer TOP")• [Layout ](<./Layout_TOP.md> "Layout TOP")• [Leap Motion ](<./Leap_Motion_TOP.md> "Leap Motion TOP")• [Lens Distort ](<./Lens_Distort_TOP.md> "Lens Distort TOP")• [Level ](<./Level_TOP.md> "Level TOP")• [Limit ](<./Limit_TOP.md> "Limit TOP")• [Lookup ](<./Lookup_TOP.md> "Lookup TOP")• [Luma Blur ](<./Luma_Blur_TOP.md> "Luma Blur TOP")• [Luma Level ](<./Luma_Level_TOP.md> "Luma Level TOP")• [Math ](<./Math_TOP.md> "Math TOP")• [Matte ](<./Matte_TOP.md> "Matte TOP")• [Mirror ](<./Mirror_TOP.md> "Mirror TOP")• [Monochrome ](<./Monochrome_TOP.md> "Monochrome TOP")• [MoSys ](<./MoSys_TOP.md> "MoSys TOP")• [Movie File In ](<./Movie_File_In_TOP.md> "Movie File In TOP")• [Movie File Out ](<./Movie_File_Out_TOP.md> "Movie File Out TOP")• [MPCDI ](<./MPCDI_TOP.md> "MPCDI TOP")• [Multiply ](<./Multiply_TOP.md> "Multiply TOP")• [Ncam ](<./Ncam_TOP.md> "Ncam TOP")• [NDI In ](<./NDI_In_TOP.md> "NDI In TOP")• [NDI Out ](<./NDI_Out_TOP.md> "NDI Out TOP")• [Noise ](<./Noise_TOP.md> "Noise TOP")• [Normal Map ](<./Normal_Map_TOP.md> "Normal Map TOP")• [Notch ](<./Notch_TOP.md> "Notch TOP")• [Null ](<./Null_TOP.md> "Null TOP")• [NVIDIA Background ](<./NVIDIA_Background_TOP.md> "NVIDIA Background TOP")• [NVIDIA Denoise ](<./NVIDIA_Denoise_TOP.md> "NVIDIA Denoise TOP")• [NVIDIA Flex ](<./NVIDIA_Flex_TOP.md> "NVIDIA Flex TOP")• [NVIDIA Flow ](<./NVIDIA_Flow_TOP.md> "NVIDIA Flow TOP")• [NVIDIA Upscaler ](<./NVIDIA_Upscaler_TOP.md> "NVIDIA Upscaler TOP")• [OAK Select ](<./OAK_Select_TOP.md> "OAK Select TOP")• [Oculus Rift ](<./Oculus_Rift_TOP.md> "Oculus Rift TOP")• [OP Viewer ](<./OP_Viewer_TOP.md> "OP Viewer TOP")• [OpenColorIO ](<./OpenColorIO_TOP.md> "OpenColorIO TOP")• [OpenVR ](<./OpenVR_TOP.md> "OpenVR TOP")• [Optical Flow ](<./Optical_Flow_TOP.md> "Optical Flow TOP")• [Orbbec Select ](<./Orbbec_Select_TOP.md> "Orbbec Select TOP")• [Orbbec ](<./Orbbec_TOP.md> "Orbbec TOP")• [Ouster Select ](<./Ouster_Select_TOP.md> "Ouster Select TOP")• [Ouster ](<./Ouster_TOP.md> "Ouster TOP")• [Out ](<./Out_TOP.md> "Out TOP")• [Outside ](<./Outside_TOP.md> "Outside TOP")• [Over ](<./Over_TOP.md> "Over TOP")• [Pack ](<./Pack_TOP.md> "Pack TOP")• [Photoshop In ](<./Photoshop_In_TOP.md> "Photoshop In TOP")• [Point File In ](<./Point_File_In_TOP.md> "Point File In TOP")• [Point File Select ](<./Point_File_Select_TOP.md> "Point File Select TOP")• Point Transform • [POP to ](<./POP_to_TOP.md> "POP to TOP")• [PreFilter Map ](<./PreFilter_Map_TOP.md> "PreFilter Map TOP")• [Projection ](<./Projection_TOP.md> "Projection TOP")• [Ramp ](<./Ramp_TOP.md> "Ramp TOP")• [RealSense ](<./RealSense_TOP.md> "RealSense TOP")• [Rectangle ](<./Rectangle_TOP.md> "Rectangle TOP")• [Remap ](<./Remap_TOP.md> "Remap TOP")• [Render Pass ](<./Render_Pass_TOP.md> "Render Pass TOP")• [Render Select ](<./Render_Select_TOP.md> "Render Select TOP")• [Render Simple ](<./Render_Simple_TOP.md> "Render Simple TOP")• [Render ](<./Render_TOP.md> "Render TOP")• [RenderStream In ](<./RenderStream_In_TOP.md> "RenderStream In TOP")• [RenderStream Out ](<./RenderStream_Out_TOP.md> "RenderStream Out TOP")• [Reorder ](<./Reorder_TOP.md> "Reorder TOP")• [Resolution ](<./Resolution_TOP.md> "Resolution TOP")• [RGB Key ](<./RGB_Key_TOP.md> "RGB Key TOP")• [RGB to HSV ](<./RGB_to_HSV_TOP.md> "RGB to HSV TOP")• [Scalable Display ](<./Scalable_Display_TOP.md> "Scalable Display TOP")• [Screen Grab ](<./Screen_Grab_TOP.md> "Screen Grab TOP")• [Screen ](<./Screen_TOP.md> "Screen TOP")• [Script ](<./Script_TOP.md> "Script TOP")• [Select ](<./Select_TOP.md> "Select TOP")• [Shared Mem In ](<./Shared_Mem_In_TOP.md> "Shared Mem In TOP")• [Shared Mem Out ](<./Shared_Mem_Out_TOP.md> "Shared Mem Out TOP")• [SICK ](<./SICK_TOP.md> "SICK TOP")• [Slope ](<./Slope_TOP.md> "Slope TOP")• [Spectrum ](<./Spectrum_TOP.md> "Spectrum TOP")• [SSAO ](<./SSAO_TOP.md> "SSAO TOP")• [ST2110 In ](<./ST2110_In_TOP.md> "ST2110 In TOP")• [ST2110 Out ](<./ST2110_Out_TOP.md> "ST2110 Out TOP")• [Stype ](<./Stype_TOP.md> "Stype TOP")• [Substance Select ](<./Substance_Select_TOP.md> "Substance Select TOP")• [Substance ](<./Substance_TOP.md> "Substance TOP")• [Subtract ](<./Subtract_TOP.md> "Subtract TOP")• [SVG ](<./SVG_TOP.md> "SVG TOP")• [Switch ](<./Switch_TOP.md> "Switch TOP")• [Syphon Spout In ](<./Syphon_Spout_In_TOP.md> "Syphon Spout In TOP")• [Syphon Spout Out ](<./Syphon_Spout_Out_TOP.md> "Syphon Spout Out TOP")• [Text ](<./Text_TOP.md> "Text TOP")• [Texture 3D ](<./Texture_3D_TOP.md> "Texture 3D TOP")• [Texture Sampling Parameters ](<./Texture_Sampling_Parameters.md> "Texture Sampling Parameters")• [Threshold ](<./Threshold_TOP.md> "Threshold TOP")• [Tile ](<./Tile_TOP.md> "Tile TOP")• [Time Machine ](<./Time_Machine_TOP.md> "Time Machine TOP")• [Tone Map ](<./Tone_Map_TOP.md> "Tone Map TOP")• [TOP ](<./TOP.md> "TOP")• [TOP Viewer ](<./TOP_Viewer.md> "TOP Viewer")• [Touch In ](<./Touch_In_TOP.md> "Touch In TOP")• [Touch Out ](<./Touch_Out_TOP.md> "Touch Out TOP")• [Transform ](<./Transform_TOP.md> "Transform TOP")• [Under ](<./Under_TOP.md> "Under TOP")• [Video Device In ](<./Video_Device_In_TOP.md> "Video Device In TOP")• [Video Device Out ](<./Video_Device_Out_TOP.md> "Video Device Out TOP")• [Video Stream In ](<./Video_Stream_In_TOP.md> "Video Stream In TOP")• [Video Stream Out ](<./Video_Stream_Out_TOP.md> "Video Stream Out TOP")• [Vioso ](<./Vioso_TOP.md> "Vioso TOP")• [Web Render ](<./Web_Render_TOP.md> "Web Render TOP")• [ZED Select ](<./ZED_Select_TOP.md> "ZED Select TOP")• [ZED ](<./ZED_TOP.md> "ZED TOP")
