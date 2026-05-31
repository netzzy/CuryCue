# TOP

## 

Summary

See also [Category:TOPs](<./Category-TOPs.md> "Category:TOPs") for a full list of articles related to TOPs. 

**Texture Operators** , also known as **TOPs** , are image operators that provide real-time, GPU-based compositing and image manipulation. All calculations for TOPs are performed on the system's GPU. TOPs can be used for preparing textures, compositing streams images and movies, building control panel elements, manipulation of 32-bit floating point data, and almost any other image task you might have. TOPs support many formats, including floating-point image formats for working with high-dynamic range (HDR) images. 

All renders and composites occur offscreen with TOPs. Data can be scaled to any resolution, limited only by the amount of graphics RAM and the maximum resolution of the graphics card. 

TOPs that are being used to hold point cloud data, where R G B holds 32-bit X Y Z data can be viewed as a 3D set of points by right-clicking on the viewer and selecting View as Points. 

**NOTE:** TouchDesigner Non-Commercial is limited to 1280x1280 resolution. 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[TOP Class](<./TOP_Class.md> "TOP Class")

## Sweet 16 TOPs

The following 16 TOPs are commonly used, we recommend familiarizing yourself with them. 

TOP | Purpose | Related TOP  
---|---|---  
[Movie File In](<./Movie_File_In_TOP.md> "Movie File In TOP") | Read movies, still images, or a sequence of still images. | [Video Device In](<./Video_Device_In_TOP.md> "Video Device In TOP"), [Movie File Out](<./Movie_File_Out_TOP.md> "Movie File Out TOP")  
[Ramp](<./Ramp_TOP.md> "Ramp TOP") | Create vertical, horizontal, radial, and circular ramps. | [Constant](<./Constant_TOP.md> "Constant TOP"), [Noise](<./Noise_TOP.md> "Noise TOP")  
[Level](<./Level_TOP.md> "Level TOP") | Adjust contrast, brightness, gamma, black level, color range, opacity. | [Luma Level](<./Luma_Level_TOP.md> "Luma Level TOP")  
[Transform](<./Transform_TOP.md> "Transform TOP") | Translate, scale, rotate, multi-repeat tile, background fill. | [Flip](<./Flip_TOP.md> "Flip TOP")  
[Over](<./Over_TOP.md> "Over TOP") | Place and shift one image over another based on the alpha of one image. | [Cross](<./Cross_TOP.md> "Cross TOP"), [Multiply](<./Multiply_TOP.md> "Multiply TOP")  
[Text](<./Text_TOP.md> "Text TOP") | Text generation with variety of fonts. |   
[Blur](<./Blur_TOP.md> "Blur TOP") | Blur. | [Luma Blur](<./Luma_Blur_TOP.md> "Luma Blur TOP")  
[Composite](<./Composite_TOP.md> "Composite TOP") | Combine multiple images with variety of operations like under, difference. |   
[Render](<./Render_TOP.md> "Render TOP") | Render 3D objects, lights and camera into an image. |   
[CHOP to](<./CHOP_to_TOP.md> "CHOP to TOP") | Convert CHOP channels into scanlines of an image. |   
[Resolution](<./Resolution_TOP.md> "Resolution TOP") | Change the resolution of an image and smooth-filter down. | all TOPs alter resolution   
[Crop](<./Crop_TOP.md> "Crop TOP") | Crop image to smaller resolution. | [Corner Pin](<./Corner_Pin_TOP.md> "Corner Pin TOP"), [Fit](<./Fit_TOP.md> "Fit TOP")  
[Select](<./Select_TOP.md> "Select TOP") | Selects an image from the same network or a different network. | [Switch](<./Switch_TOP.md> "Switch TOP")  
[Reorder](<./Reorder_TOP.md> "Reorder TOP") | Re-order the channels of an image. | [Channel Mix](<./Channel_Mix_TOP.md> "Channel Mix TOP")  
[Cache](<./Cache_TOP.md> "Cache TOP") | Hold a static or dynamic sequence of images and output one of them. | [Feedback](<./Feedback_TOP.md> "Feedback TOP")  
[Displace](<./Displace_TOP.md> "Displace TOP") | Use red-blue of one image to warp another image. | [Time Machine](<./Time_Machine_TOP.md> "Time Machine TOP")  
  
All TOPs are documented in the [Category:TOPs](<./Category-TOPs.md> "Category:TOPs"). 

## TOP Flags

The lower right corner contains only 2 flags, the TOP’s [Display Flag](<./Display_Flag.md> "Display Flag") and [Viewer Active Flag](<./Viewer_Active_Flag.md> "Viewer Active Flag"). Turning on the display flag displays the TOP as a background in the current [Network Pane](<./Network_Editor.md> "Network Editor"). Turning on multiple TOP Display Flags will display a tiled sequence of multiple TOP outputs as the background of the network pane. 

## TOP Viewers

All TOP operators have interactive [Node Viewers](<./Node_Viewer.md> "Node Viewer"). To interact with it, turn on the TOP's [Viewer Active Flag](<./Viewer_Active_Flag.md> "Viewer Active Flag") to make the viewer active. 

A gray checkerboard background will be displayed in images where an alpha channel is present. This can be turned off by opening [Preferences](<./Dialogs-Preferences_Dialog.md> "Dialogs:Preferences Dialog") in the **Edit** menu. In preferences you can choose to use checkerboard or black as you alpha background. 

Use [LMB](<./Mouse_Click.md> "Mouse Click") to move the image around. Use [MMB](<./Mouse_Click.md> "Mouse Click") to zoom in and out of the image. Re-center the image by using the home shortcut "**h** ". 

Clicking the [RMB](<./Mouse_Click.md> "Mouse Click") will open the viewer options menu. Keyboard shortcuts are listed beside each entry in the menu. 

**Home** \- Re-centers and scales the image to fit in the viewer. 

**Display Pixel Values** \- Displays pixel information over the image. The [Timeline](<./Timeline.md> "Timeline") should be playing forward for the values to properly update. 

The following is displayed: 
* cursor uv coordinates
  * cursor xy pixel coordinates
  * RGB values 0-255
  * RGB values 0-1


**Display Field Guide** \- Displays a 24x24 field guide over the image. The guide also displays the action safe zone and title safe zone for the image. 

**Display Mode** \- The display mode options give the option of viewing certain channels of the image. 

The following display modes are available: 
* Color - Display all RGB channles.
  * Red/Green/Blue/Alpha - Display the Red/Green/Blue/Alpha channel respectively.
  * Mono - Display the image in monochrome.
  * Normalize Split - Displays each channel in the image at the same time normalized from 0-1. Excellent for viewing floating point and point cloud data.


**View as Points** \- Displays the data in the TOP as 3D points for each pixel assuming red = x, green = y, and blue = z. Useful for viewing point cloud data. 

Point cloud data displayed 3 modes: 1) Color 2) Normalized Split 3) View as Points 
* [![TOP operators](./images/thumb/5/55/Opcreate_TOP.jpg/95px-Opcreate_TOP.jpg.png)](</File:Opcreate_TOP.jpg> "TOP operators")

TOP operators 
* [![A TOP network](./images/thumb/c/c3/TOPexample.jpg/144px-TOPexample.jpg)](</File:TOPexample.jpg> "A TOP network")

A TOP network 
* [![TOP viewer options](./images/thumb/b/bb/TOPviewer.jpg/144px-TOPviewer.jpg)](</File:TOPviewer.jpg> "TOP viewer options")

[TOP viewer options](<./TOP_Viewer.md> "TOP Viewer")
* [![Composite with Feedback](./images/7/7a/TOPexample2.jpg)](</File:TOPexample2.jpg> "Composite with Feedback")

Composite with Feedback 

## Using TOPs
* 2D image data, everything processed on GPU, generators and filters, real-time compositing
  * Import: Movie File In TOP, Video Device In TOP
  * Export: right-click menu, Movie File Out TOP, Export Movie Dialog

## See also

[Category:TOPs](<./Category-TOPs.md> "Category:TOPs")  
[Mipmapping](<./Mipmapping.md> "Mipmapping") and [Texture Filtering](<./Texture_Filtering.md> "Texture Filtering")  
[TOP Generator Common Page](<./TOP_Generator_Common_Page.md> "TOP Generator Common Page") and [TOP Filter Common Page](<./TOP_Filter_Common_Page.md> "TOP Filter Common Page")  
[Pixel Formats](<./Pixel_Formats.md> "Pixel Formats")

TOPs   
---  
[Add ](<./Add_TOP.md> "Add TOP")• [Analyze ](<./Analyze_TOP.md> "Analyze TOP")• [Anti Alias ](<./Anti_Alias_TOP.md> "Anti Alias TOP")• [Blob Track ](<./Blob_Track_TOP.md> "Blob Track TOP")• [Bloom ](<./Bloom_TOP.md> "Bloom TOP")• [Blur ](<./Blur_TOP.md> "Blur TOP")• [Cache Select ](<./Cache_Select_TOP.md> "Cache Select TOP")• [Cache ](<./Cache_TOP.md> "Cache TOP")• [Channel Mix ](<./Channel_Mix_TOP.md> "Channel Mix TOP")• [CHOP to ](<./CHOP_to_TOP.md> "CHOP to TOP")• [Chroma Key ](<./Chroma_Key_TOP.md> "Chroma Key TOP")• [Circle ](<./Circle_TOP.md> "Circle TOP")• [Composite ](<./Composite_TOP.md> "Composite TOP")• [Constant ](<./Constant_TOP.md> "Constant TOP")• [Convolve ](<./Convolve_TOP.md> "Convolve TOP")• [Corner Pin ](<./Corner_Pin_TOP.md> "Corner Pin TOP")• [CPlusPlus ](<./CPlusPlus_TOP.md> "CPlusPlus TOP")• [Crop ](<./Crop_TOP.md> "Crop TOP")• [Cross ](<./Cross_TOP.md> "Cross TOP")• [Cube Map ](<./Cube_Map_TOP.md> "Cube Map TOP")• [Depth ](<./Depth_TOP.md> "Depth TOP")• [Difference ](<./Difference_TOP.md> "Difference TOP")• [Direct Display Out ](<./Direct_Display_Out_TOP.md> "Direct Display Out TOP")• [DirectX In ](<./DirectX_In_TOP.md> "DirectX In TOP")• [DirectX Out ](<./DirectX_Out_TOP.md> "DirectX Out TOP")• [Displace ](<./Displace_TOP.md> "Displace TOP")• [Edge ](<./Edge_TOP.md> "Edge TOP")• [Emboss ](<./Emboss_TOP.md> "Emboss TOP")• [Feedback ](<./Feedback_TOP.md> "Feedback TOP")• [Fit ](<./Fit_TOP.md> "Fit TOP")• [Flip ](<./Flip_TOP.md> "Flip TOP")• [Function ](<./Function_TOP.md> "Function TOP")• [GLSL Multi ](<./GLSL_Multi_TOP.md> "GLSL Multi TOP")• [GLSL ](<./GLSL_TOP.md> "GLSL TOP")• [HSV Adjust ](<./HSV_Adjust_TOP.md> "HSV Adjust TOP")• [HSV to RGB ](<./HSV_to_RGB_TOP.md> "HSV to RGB TOP")• [Import Select ](<./Import_Select_TOP.md> "Import Select TOP")• [In ](<./In_TOP.md> "In TOP")• [Inside ](<./Inside_TOP.md> "Inside TOP")• [Introduction To s Vid ](<./Introduction_To_TOPs_Vid.md> "Introduction To TOPs Vid")• [Kinect Azure Select ](<./Kinect_Azure_Select_TOP.md> "Kinect Azure Select TOP")• [Kinect Azure ](<./Kinect_Azure_TOP.md> "Kinect Azure TOP")• [Kinect ](<./Kinect_TOP.md> "Kinect TOP")• [Layer Mix ](<./Layer_Mix_TOP.md> "Layer Mix TOP")• [Layer ](<./Layer_TOP.md> "Layer TOP")• [Layout ](<./Layout_TOP.md> "Layout TOP")• [Leap Motion ](<./Leap_Motion_TOP.md> "Leap Motion TOP")• [Lens Distort ](<./Lens_Distort_TOP.md> "Lens Distort TOP")• [Level ](<./Level_TOP.md> "Level TOP")• [Limit ](<./Limit_TOP.md> "Limit TOP")• [Lookup ](<./Lookup_TOP.md> "Lookup TOP")• [Luma Blur ](<./Luma_Blur_TOP.md> "Luma Blur TOP")• [Luma Level ](<./Luma_Level_TOP.md> "Luma Level TOP")• [Math ](<./Math_TOP.md> "Math TOP")• [Matte ](<./Matte_TOP.md> "Matte TOP")• [Mirror ](<./Mirror_TOP.md> "Mirror TOP")• [Monochrome ](<./Monochrome_TOP.md> "Monochrome TOP")• [MoSys ](<./MoSys_TOP.md> "MoSys TOP")• [Movie File In ](<./Movie_File_In_TOP.md> "Movie File In TOP")• [Movie File Out ](<./Movie_File_Out_TOP.md> "Movie File Out TOP")• [MPCDI ](<./MPCDI_TOP.md> "MPCDI TOP")• [Multiply ](<./Multiply_TOP.md> "Multiply TOP")• [Ncam ](<./Ncam_TOP.md> "Ncam TOP")• [NDI In ](<./NDI_In_TOP.md> "NDI In TOP")• [NDI Out ](<./NDI_Out_TOP.md> "NDI Out TOP")• [Noise ](<./Noise_TOP.md> "Noise TOP")• [Normal Map ](<./Normal_Map_TOP.md> "Normal Map TOP")• [Notch ](<./Notch_TOP.md> "Notch TOP")• [Null ](<./Null_TOP.md> "Null TOP")• [NVIDIA Background ](<./NVIDIA_Background_TOP.md> "NVIDIA Background TOP")• [NVIDIA Denoise ](<./NVIDIA_Denoise_TOP.md> "NVIDIA Denoise TOP")• [NVIDIA Flex ](<./NVIDIA_Flex_TOP.md> "NVIDIA Flex TOP")• [NVIDIA Flow ](<./NVIDIA_Flow_TOP.md> "NVIDIA Flow TOP")• [NVIDIA Upscaler ](<./NVIDIA_Upscaler_TOP.md> "NVIDIA Upscaler TOP")• [OAK Select ](<./OAK_Select_TOP.md> "OAK Select TOP")• [Oculus Rift ](<./Oculus_Rift_TOP.md> "Oculus Rift TOP")• [OP Viewer ](<./OP_Viewer_TOP.md> "OP Viewer TOP")• [OpenColorIO ](<./OpenColorIO_TOP.md> "OpenColorIO TOP")• [OpenVR ](<./OpenVR_TOP.md> "OpenVR TOP")• [Optical Flow ](<./Optical_Flow_TOP.md> "Optical Flow TOP")• [Orbbec Select ](<./Orbbec_Select_TOP.md> "Orbbec Select TOP")• [Orbbec ](<./Orbbec_TOP.md> "Orbbec TOP")• [Ouster Select ](<./Ouster_Select_TOP.md> "Ouster Select TOP")• [Ouster ](<./Ouster_TOP.md> "Ouster TOP")• [Out ](<./Out_TOP.md> "Out TOP")• [Outside ](<./Outside_TOP.md> "Outside TOP")• [Over ](<./Over_TOP.md> "Over TOP")• [Pack ](<./Pack_TOP.md> "Pack TOP")• [Photoshop In ](<./Photoshop_In_TOP.md> "Photoshop In TOP")• [Point File In ](<./Point_File_In_TOP.md> "Point File In TOP")• [Point File Select ](<./Point_File_Select_TOP.md> "Point File Select TOP")• [Point Transform ](<./Point_Transform_TOP.md> "Point Transform TOP")• [POP to ](<./POP_to_TOP.md> "POP to TOP")• [PreFilter Map ](<./PreFilter_Map_TOP.md> "PreFilter Map TOP")• [Projection ](<./Projection_TOP.md> "Projection TOP")• [Ramp ](<./Ramp_TOP.md> "Ramp TOP")• [RealSense ](<./RealSense_TOP.md> "RealSense TOP")• [Rectangle ](<./Rectangle_TOP.md> "Rectangle TOP")• [Remap ](<./Remap_TOP.md> "Remap TOP")• [Render Pass ](<./Render_Pass_TOP.md> "Render Pass TOP")• [Render Select ](<./Render_Select_TOP.md> "Render Select TOP")• [Render Simple ](<./Render_Simple_TOP.md> "Render Simple TOP")• [Render ](<./Render_TOP.md> "Render TOP")• [RenderStream In ](<./RenderStream_In_TOP.md> "RenderStream In TOP")• [RenderStream Out ](<./RenderStream_Out_TOP.md> "RenderStream Out TOP")• [Reorder ](<./Reorder_TOP.md> "Reorder TOP")• [Resolution ](<./Resolution_TOP.md> "Resolution TOP")• [RGB Key ](<./RGB_Key_TOP.md> "RGB Key TOP")• [RGB to HSV ](<./RGB_to_HSV_TOP.md> "RGB to HSV TOP")• [Scalable Display ](<./Scalable_Display_TOP.md> "Scalable Display TOP")• [Screen Grab ](<./Screen_Grab_TOP.md> "Screen Grab TOP")• [Screen ](<./Screen_TOP.md> "Screen TOP")• [Script ](<./Script_TOP.md> "Script TOP")• [Select ](<./Select_TOP.md> "Select TOP")• [Shared Mem In ](<./Shared_Mem_In_TOP.md> "Shared Mem In TOP")• [Shared Mem Out ](<./Shared_Mem_Out_TOP.md> "Shared Mem Out TOP")• [SICK ](<./SICK_TOP.md> "SICK TOP")• [Slope ](<./Slope_TOP.md> "Slope TOP")• [Spectrum ](<./Spectrum_TOP.md> "Spectrum TOP")• [SSAO ](<./SSAO_TOP.md> "SSAO TOP")• [ST2110 In ](<./ST2110_In_TOP.md> "ST2110 In TOP")• [ST2110 Out ](<./ST2110_Out_TOP.md> "ST2110 Out TOP")• [Stype ](<./Stype_TOP.md> "Stype TOP")• [Substance Select ](<./Substance_Select_TOP.md> "Substance Select TOP")• [Substance ](<./Substance_TOP.md> "Substance TOP")• [Subtract ](<./Subtract_TOP.md> "Subtract TOP")• [SVG ](<./SVG_TOP.md> "SVG TOP")• [Switch ](<./Switch_TOP.md> "Switch TOP")• [Syphon Spout In ](<./Syphon_Spout_In_TOP.md> "Syphon Spout In TOP")• [Syphon Spout Out ](<./Syphon_Spout_Out_TOP.md> "Syphon Spout Out TOP")• [Text ](<./Text_TOP.md> "Text TOP")• [Texture 3D ](<./Texture_3D_TOP.md> "Texture 3D TOP")• [Texture Sampling Parameters ](<./Texture_Sampling_Parameters.md> "Texture Sampling Parameters")• [Threshold ](<./Threshold_TOP.md> "Threshold TOP")• [Tile ](<./Tile_TOP.md> "Tile TOP")• [Time Machine ](<./Time_Machine_TOP.md> "Time Machine TOP")• [Tone Map ](<./Tone_Map_TOP.md> "Tone Map TOP")• TOP • [TOP Viewer ](<./TOP_Viewer.md> "TOP Viewer")• [Touch In ](<./Touch_In_TOP.md> "Touch In TOP")• [Touch Out ](<./Touch_Out_TOP.md> "Touch Out TOP")• [Transform ](<./Transform_TOP.md> "Transform TOP")• [Under ](<./Under_TOP.md> "Under TOP")• [Video Device In ](<./Video_Device_In_TOP.md> "Video Device In TOP")• [Video Device Out ](<./Video_Device_Out_TOP.md> "Video Device Out TOP")• [Video Stream In ](<./Video_Stream_In_TOP.md> "Video Stream In TOP")• [Video Stream Out ](<./Video_Stream_Out_TOP.md> "Video Stream Out TOP")• [Vioso ](<./Vioso_TOP.md> "Vioso TOP")• [Web Render ](<./Web_Render_TOP.md> "Web Render TOP")• [ZED Select ](<./ZED_Select_TOP.md> "ZED Select TOP")• [ZED ](<./ZED_TOP.md> "ZED TOP")
