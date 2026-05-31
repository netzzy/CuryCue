# Release Notes/2023.10000/experimental

Current **Experimental** Build **2023.11220 - Nov 15 2023** \- [Download Here](<https://derivative.ca/download/experimental>)

Experimental builds include new features still in development and testing, features are subject to change or even be removed. For the stability and reliability required for performances and project deliveries, use the production ready [Official Builds](<../../Release_Notes.md> "Release Notes"). 

**Known Issues** and **Backward Compatibility** warnings below should be read carefully. 

⚠️ Project .toe **files saved in Experimental can not be loaded back in Official**. 

[Download Here](<https://derivative.ca/download/experimental>)

## Known Issues

Please report all issues to the **[Bugs Forum](<https://forum.derivative.ca/>)** , remember to include build number. 
* [Bloom TOP](<../../Bloom_TOP.md> "Bloom TOP") \- 'Bloom Alpha' does not calculate alpha correctly.
  * [Body Track CHOP](<../../Body_Track_CHOP.md> "Body Track CHOP") \- Can sometimes crash if parameters are manipulated too quickly.

## Backward Compatibility

**Change for keys on Windows systems**
* TouchDesigner's License System Codes are now generated differently to reduce the chance of a system code change when applying Windows Updates. **Old keys will work in this 2023.10k branch** , however, **new keys created in this 2023.10k branch will not work with older versions** of TouchDesigner.
  * We have released an update to 2022.20k branch so any builds released after July 10 2023 will also work with the new keys created in this 2023 version. **In summary - If you want to use 2022 and 2023 versions with the same key, either a) create your key using 2022 builds, or b) use a 2022 build released after July 10 2023** (yet to be released).


  
**File Compatibility**

Project .toe files saved in Experimental can not be loaded back in Official. 

  
**Backward Compatibility Changes**

We try to make upgrading to new TouchDesigner branches as painless as possible, but sometimes changes are made that are not compatible with the feature set in older builds. These are difficult decisions and we do not take them lightly, but we move forward with such changes when it is clear that they will benefit the TouchDesigner platform in the long term. 
* **BACKWARD COMPATIBILITY ISSUE** \- **tdu.match interprets spaces** in the pattern argument as separators.
* **BACKWARD COMPATIBILITY ISSUE** \- The **[Keyboard In DAT](<../../Keyboard_In_DAT.md> "Keyboard In DAT")'s 'key' column will no longer return special characters such as !@#$%^&*()**. These will now be 1234567890 for better consistency with other shortcut workflows.
* **BACKWARD COMPATIBILITY ISSUE** \- **Parameter expressions assigned to None in scripts will now be empty string** instead of the string 'None'.
* **BACKWARD COMPATIBILITY ISSUE** \- **When Python parameter expression is blank, return None** , not empty string.
* **BACKWARD COMPATIBILITY ISSUE** \- **Panel.interactMouse/interactTouch will respect a panel's 'Enable'** parameter toggle.
* **BACKWARD COMPATIBILITY ISSUE** \- [Optical Flow TOP](<../../Optical_Flow_TOP.md> "Optical Flow TOP") \- '**Cost Output' values are now normalized to 0-1** , instead of 0-255.
* **BACKWARD COMPATIBILITY ISSUE** \- [TDJSON](<../../TDJSON.md> "TDJSON") \- Including '**eval' in extraAttrs** argument list will now create a new "eval" entry in the JSON instead of replacing the value in "val".
* **BACKWARD COMPATIBILITY ISSUE** \- [Point File In TOP](<../../Point_File_In_TOP.md> "Point File In TOP") / [Point File Select TOP](<../../Point_File_Select_TOP.md> "Point File Select TOP") \- Altered **how the output texture size is determined** based on the number of points. Might result in different texture sizes than previous versions.
* **BACKWARD COMPATIBILITY ISSUE** \- [Point File In TOP](<../../Point_File_In_TOP.md> "Point File In TOP") / [Point File Select TOP](<../../Point_File_Select_TOP.md> "Point File Select TOP") \- **Field parameters are now stored as strings** rather than indices.
* **BACKWARD COMPATIBILITY ISSUE** \- [Sequence Class](<../../Sequence_Class.md> "Sequence Class").blocks - This now returns a list of [SequenceBlock Class](<../../SequenceBlock_Class.md> "SequenceBlock Class") not list of tuples of Pars. sequence[3] sequence.blocks[6] etc now returns a block, whose elements are now ParGroup objects, not Par objects.
* **BACKWARD COMPATIBILITY ISSUE** \- Several built-in parameters have been renamed for consistency, starting with index 0, etc. Older files will load correctly and get updated when saved, but note that **files saved in 2023.10k builds will cause issues if loaded into any previous builds.**
* **BACKWARD COMPATIBILITY ISSUE** \- [Texture SOP](<../../Texture_SOP.md> "Texture SOP") \- Fixed **UV stretching and shearing of 'Face' type mapping**. This changes the behaviour of 'Face' type option.
* **BACKWARD COMPATIBILITY ISSUE** \- **Parameter order gets overridden** when changing a Parameter's page member.

## Build 2023.11280 - Dec 03, 2023

### New Features
* [macOS](<../../MacOS.md> "MacOS") \- Added support for hardware decoding in the [Movie File In TOP](<../../Movie_File_In_TOP.md> "Movie File In TOP") and [Video Stream In TOP](<../../Video_Stream_In_TOP.md> "Video Stream In TOP"). To enable on the Movie File In TOP, turn on the 'Hardware Decode' parameter toggle on the Tune page. 
    * Supported codecs vary by hardware, potentially works for H.264, HEVC (H.265), P-JPEG, VP9, AV1, ProRes
    * When possible it does direct-to-texture decode - image memory is always on the GPU.
* [Spectrum TOP](<../../Spectrum_TOP.md> "Spectrum TOP") \- Revamped the Spectrum TOP to use Vulkan via the VkFFT library, deprecating the CUDA and OpenCV usage. It results in much faster performance and cross platform support for both Windows and macOS.
* [Audio Device In CHOP](<../../Audio_Device_In_CHOP.md> "Audio Device In CHOP") \- Added 'Rate Mode' parameter for ASIO devices that can pull the sample rate from the device rather than manually override it.
  * [Audio File In CHOP](<../../Audio_File_In_CHOP.md> "Audio File In CHOP") \- Added support for driving the audio file index with a timecode reference.


  
**Custom Sequential Parameters**
* [TouchEngine](<../../TouchEngine.md> "TouchEngine") and [Engine COMP](<../../Engine_COMP.md> "Engine COMP") \- Fully supports sequential parameters 
    * TouchEngine - Added a the new sequence parameter type, added a function to change sequence block count.
    * TouchEngine - For hosts using older library versions, expose sequences as a series of regular parameters.
    * Engine COMP \- Correctly display, edit and update parameter sequences, including changes to block count.

### New Python
* [AudiofileinCHOP Class](<../../AudiofileinCHOP_Class.md> "AudiofileinCHOP Class")`.timecode`\- Gets a timecode represenation of the audio file read index.
  * [MidiinCHOP Class](<../../MidiinCHOP_Class.md> "MidiinCHOP Class")`.timecode`\- A new getter that grabs the timecode representation of the last set of quarter frame messages.
* [OP Class](<../../OP_Class.md> "OP Class")`.seq`\- A new member which allows accessing sequences by name.


For example:`n.seq['Color'] # returns None if not found``n.seq.Color # raises exception if not found`* [OP Class](<../../OP_Class.md> "OP Class")`.curBlock`\- The SequenceBlock of the currently evaluated parameter.


For example:`me.curBlock.par.B # use in parameter A of each block`* [Project Class](<../../Project_Class.md> "Project Class").quit() - Added`exitCode`keyword argument, to manually specify an exit code on quitting.
* [Sequence Class](<../../Sequence_Class.md> "Sequence Class").blocks - This now returns a list of [SequenceBlock Class](<../../SequenceBlock_Class.md> "SequenceBlock Class") not list of tuples of Pars.


**BACKWARD COMPATIBILITY** sequence[3] sequence.blocks[6] etc now returns a block, whose elements are now ParGroup objects, not Par objects. 
* [Sequence Class](<../../Sequence_Class.md> "Sequence Class") \- New par and parGroup members which return a list (one from each block) or None.


For example:`n.seq.Info.parGroup.T # entire list``n.seq.Info.parGroup.T[3] # ParGroup from 4th block.``n.seq.Info.parGroup['T'] # None if not found, else entire list``n.seq.Info.par.Tx # entire list``n.seq.Info.par.Tx[3] # ParGroup from 4th block.`* [SequenceBlock Class](<../../SequenceBlock_Class.md> "SequenceBlock Class") \- For working with a block of parameters in a sequence.


Can be accessed via: 
* Sequence.blocks
  * Sequence[index]
  * Iterating through Sequence


  
Block members include .index .owner .sequence .par .parGroup 

For example:`for p in Block (iterating)``len(Block) (number of pars)``Block[index]`(each par) 
* [Timecode Class](<../../Timecode_Class.md> "Timecode Class").cycle - A new member for getting/setting whether the timecode will cycle once it reaches its max (default value: True)

### New Palette
* [Palette:camSchnappr](<../../Palette-camSchnappr.md> "Palette:camSchnappr") \- Inverted UI interaction: ctrl+LMB will add points and ctrl+RMB will remove them. Interaction directly with the mouse (using no modifier keys) will control the camera now.
* [Palette:kantanMapper](<../../Palette-kantanMapper.md> "Palette:kantanMapper") \- All wireframe materials use Topology mode now.
  * [Palette:materialDesignIcons](<../../Palette-materialDesignIcons.md> "Palette:materialDesignIcons") \- Fixed an internal shader issue.
  * [palette:particlesGpu](<../../Palette-particlesGpu.md> "Palette:particlesGpu") \- New default compositing setting (Discard Alpha) and fixed source only creating particles if source alpha greater 0.
  * [Palette:sickEngine](<../../Palette-sickEngine.md> "Palette:sickEngine") \- A new component to wrap the SICK TOP in an Engine COMP for connecting to more than one sensor in the same project.
  * [Palette:webBrowser](<../../Palette-webBrowser.md> "Palette:webBrowser") \- Multitouch usability enabled.

### Bug Fixes and Improvements

**COMP**
* [Engine COMP](<../../Engine_COMP.md> "Engine COMP") \- Fixed an issue which caused a Python error for old-style onInitialize callbacks which don't return a value.
  * [Text COMP](<../../Text_COMP.md> "Text COMP") \- Fixed a bug when loading custom font files and added a warning message when the font fails to load.


  
**TOP**
* [Noise TOP](<../../Noise_TOP.md> "Noise TOP") \- Fixed Simplex2D noise so that when the 'Derivative (Slope) parameter is toggled On, RGB channels get the XYZ noise derivatives.
  * [Normal Map TOP](<../../Normal_Map_TOP.md> "Normal Map TOP") \- Fixed bug that could case NaN output values when using inputs textures with values greater than 1.
  * [Nvidia Background TOP](<../../Nvidia_Background_TOP.md> "Nvidia Background TOP") / [Nvidia Denoise TOP](<../../Nvidia_Denoise_TOP.md> "Nvidia Denoise TOP") / [Nvidia Upscaler TOP](<../../Nvidia_Upscaler_TOP.md> "Nvidia Upscaler TOP") \- Fixed handling of 32-bit input textures. Note: output will still be 8 bit fixed.
  * [Point File In TOP](<../../Point_File_In_TOP.md> "Point File In TOP") / [Point File Select TOP](<../../Point_File_Select_TOP.md> "Point File Select TOP") \- **BACKWARD COMPATIBILITY ISSUE** \- Altered how the output texture size is determined based on the number of points. Might result in different texture sizes than previous versions.
  * [Video Stream In TOP](<../../Video_Stream_In_TOP.md> "Video Stream In TOP") \- Added 'Active' parameter.


**CHOP**
* [Audio Stream In CHOP](<../../Audio_Stream_In_CHOP.md> "Audio Stream In CHOP") \- Added an 'Active' parameter.
  * [Body Track CHOP](<../../Body_Track_CHOP.md> "Body Track CHOP") / [Face Track CHOP](<../../Face_Track_CHOP.md> "Face Track CHOP") \- Fixed tracking issues when using a floating point input texture.
* [Lag CHOP](<../../Lag_CHOP.md> "Lag CHOP") \- Clamp 'Lag' and 'Overshoot' parameters to never be less than zero
  * [Timecode CHOP](<../../Timecode_CHOP.md> "Timecode CHOP") \- Added 'Cycle' toggle.


**SOP**
* [Add SOP](<../../Add_SOP.md> "Add SOP") \- Fixed bug that prevented the point sequence parameters from working.


**DAT**

**Misc**
* Export Movie Dialog \- Fixed Codec dropdown not working.
  * [OAK-D](<../../OAK-D.md> "OAK-D") \- Example file added to Samples/OAK.

### Operator Snippets

### Backward Compatibility Changes
* **BACKWARD COMPATIBILITY ISSUE** \- [Point File In TOP](<../../Point_File_In_TOP.md> "Point File In TOP") / [Point File Select TOP](<../../Point_File_Select_TOP.md> "Point File Select TOP") \- Altered how the output texture size is determined based on the number of points. Might result in different texture sizes than previous versions.
  * **BACKWARD COMPATIBILITY ISSUE** \- [Sequence Class](<../../Sequence_Class.md> "Sequence Class").blocks - This now returns a list of [SequenceBlock Class](<../../SequenceBlock_Class.md> "SequenceBlock Class") not list of tuples of Pars. sequence[3] sequence.blocks[6] etc now returns a block, whose elements are now ParGroup objects, not Par objects.

## Build 2023.11220 - Nov 15, 2023

### New Features

**Custom Sequential Parameters**

Custom parameters now support user defined [Sequential Parameters](<../../Sequential_Parameters.md> "Sequential Parameters"). These can be defined directly with python or through the [Component Editor Dialog](<../../Component_Editor_Dialog.md> "Component Editor Dialog"). 

All Sequential parameter sequences (both built-in and custom) now **start with a new sequence parameter**. The name of this sequence parameter defines the prefix of all the following parameters in that sequence block. 

For example, let's look a the built-in sequential parameters in the Constant CHOP:`n.par.const`(New 'sequence' parameter)`n.par.const0name``n.par.const0value``n.par.const1name``n.par.const1value`etc 

Access to any [sequence object](<../../Sequence_Class.md> "Sequence Class") is handled through this new parameter:`n.par.const.sequence.blockSize`**To create Custom Sequential Parameters through python**:`n.customPages[0].appendSequence('S')`You can attach parameters to that sequence through python:`n.par.S.sequence.blockSize = 3`(connects next 3 parameters to it). 

**Alternatively use the Component Editor Dialog** and create a new parameter of 'Sequence' type. 

  
**BACKWARD COMPATIBILITY ISSUE** \- Several built-in parameters have been renamed for consistency, starting with index 0, etc. Older files will load correctly and get updated when saved, but note that **files saved in 2023.10k builds will cause issues if loaded into 2022 or previous builds.**

### New Python
* [App Class](<../../App_Class.md> "App Class").`tempFolder`\- New member which **reports the temporary files location**.
  * [COMP Class](<../../COMP_Class.md> "COMP Class").`delTD()`method is now properly called on extensions when operator is deleted.
* [Page Class](<../../Page_Class.md> "Page Class").`sort()`\- Allows Par and ParGroups as arguments (in addition to strings).
* [TOP Class](<../../TOP_Class.md> "TOP Class").`pixelFormat`\- New member that **returns the pixel format** as a string.

### New Palette
* [Palette:depthProjection ](<../../Palette-depthProjection.md> "Palette:depthProjection") \- Fixed the direction of the XY axes.
  * [Palette:logger](<../../Palette-logger.md> "Palette:logger") v2.2.5 - Many tweaks and fixes. 
    * The logger COMP now **follows the propagation rules of the python library**.
    * **A Stream Handler was added** to handle Textport log items. Therefore, when interacting with the logger COMP or the logger object directly, it will in most cases have an impact on both handlers (if used simultaneously). For example, when the setting changed is impacting the Logger object rather than an handler, such as the log level, or propagation. Status Bar is not using an handler.
    * Adding some missing **Help tooltip, docStrings and type hinting**.
    * Prevented logger from initializing when Active flag is off.
* [Palette:pointRender](<../../Palette-pointRender.md> "Palette:pointRender") \- Updated to use cloned cameraViewport.
  * [Palette:stoner](<../../Palette-stoner.md> "Palette:stoner") \- Fixed **Grid Warp mode not properly adjusting bezier** surface weights.
  * [Palette:webBrowser](<../../Palette-webBrowser.md> "Palette:webBrowser") \- **Added a Crop page** and parameters for an additional cropped output (new second TOP output called _Output 1_).
  * [WebRTC](<../../WebRTC.md> "WebRTC") \- Updated WebRTC and Signaling components to latest Logger v2.2.5.

### Bug Fixes and Improvements
* [ZED](<../../ZED.md> "ZED") \- Upgraded to ZED SDK 4.0.7.


**COMP**
* [Engine COMP](<../../Engine_COMP.md> "Engine COMP") \- Fixed an issue which could cause TouchDesigner to **hang when a component is loaded** in some circumstances.


**TOP**
* [Movie File In TOP](<../../Movie_File_In_TOP.md> "Movie File In TOP") \- Improved **performance of ProRes** on macOS.
  * [Optical Flow TOP](<../../Optical_Flow_TOP.md> "Optical Flow TOP") \- Adding new '**Pre-Shrink' parameter**.
  * [Point File In TOP](<../../Point_File_In_TOP.md> "Point File In TOP") / [Point File Select TOP](<../../Point_File_Select_TOP.md> "Point File Select TOP") \- **BACKWARD COMPATIBILITY ISSUE** \- **Field parameters are now stored as strings** rather than indices.


**CHOP**
* [Audio Device In CHOP](<../../Audio_Device_In_CHOP.md> "Audio Device In CHOP") \- Added the option to **select device by index** rather than name for ASIO and CoreAudio.
  * [Clock CHOP](<../../Clock_CHOP.md> "Clock CHOP") \- **Fixed 'Since Program Start'** mode having incorrect start time.
  * [Transform CHOP](<../../Transform_CHOP.md> "Transform CHOP") \- Fixed **Quaternion Lerp and Slerp** input blend behaviour.


**SOP**
* [Texture SOP](<../../Texture_SOP.md> "Texture SOP") \- **BACKWARD COMPATIBILITY ISSUE** \- Fixed **UV stretching and shearing of 'Face' type mapping**. This changes the behaviour of 'Face' type option.


**DAT**
* [Parameter DAT](<../../Parameter_DAT.md> "Parameter DAT") \- Added **page name filtering** and a toggle to output a column with the page that each parameter belongs to.


**Misc**
* [macOS](<../../MacOS.md> "MacOS") \- Fixed an issue which caused **edits to DAT contents in external editors** to be ignored.
  * Inproved the behavior of the **value ladder on Remote Desktop/VNC/Synergy/Parsec** etc.
  * Fixed dialog window (ie. colorpicker) **sizes slowly getting larger** when repeatedly opened.
  * Fixed a case where **unicode characters in a external file's filepath** could cause a crash.
  * Fixed **shortcut keys not working** in TOP viewers.
  * Stopped **auto-connecting of component inputs or outputs** when drag and dropping or pasting a component into the network editor.

### Operator Snippets

### Backward Compatibility Changes
* **BACKWARD COMPATIBILITY ISSUE** \- Several built-in parameters have been renamed for consistency, starting with index 0, etc. Older files will load correctly and get updated when saved, but note that **files saved in 2023.10k builds will cause issues if loaded into any previous builds.**
* **BACKWARD COMPATIBILITY ISSUE** \- [Texture SOP](<../../Texture_SOP.md> "Texture SOP") \- Fixed **UV stretching and shearing of 'Face' type mapping**. This changes the behaviour of 'Face' type option.
* **BACKWARD COMPATIBILITY ISSUE** \- [Point File In TOP](<../../Point_File_In_TOP.md> "Point File In TOP") / [Point File Select TOP](<../../Point_File_Select_TOP.md> "Point File Select TOP") \- **Field parameters are now stored as strings** rather than indices.
* **BACKWARD COMPATIBILITY ISSUE** \- **Parameter order gets overridden** when changing a Parameter's page member.

## Build 2023.11170 - Oct 24, 2023

### New Features
* [Audio Devices DAT](<../../Audio_Devices_DAT.md> "Audio Devices DAT") / [Video Devices DAT](<../../Video_Devices_DAT.md> "Video Devices DAT") \- Two new DATs which **list all input and output audio/video devices**. Callbacks are included to create actions when devices are added or removed.
  * [Text COMP](<../../Text_COMP.md> "Text COMP") \- Added new 'Drop Shadow' parameter to **draw a drop shadow under the text**.
* [Movie File In TOP](<../../Movie_File_In_TOP.md> "Movie File In TOP") / [Movie File Out TOP](<../../Movie_File_Out_TOP.md> "Movie File Out TOP") \- Added support for **ProRes decoding and encoding**.
  * [Movie File Out TOP](<../../Movie_File_Out_TOP.md> "Movie File Out TOP") \- Added a new 'Limit Length' parameter to automatically **stop recording when the output reaches a set length**.
* [Render TOP](<../../Render_TOP.md> "Render TOP") \- The '**Image Output' feature has been reworked**. Multiple can now be created, with custom names, array sizes and formats. This is found on the new 'Image' page.
* [FreeD In CHOP](<../../FreeD_In_CHOP.md> "FreeD In CHOP") \- Added 'Camera ID' parameter to allow **filtering of camera packets and receiving date from multiple cameras**.
  * [Leap Motion TOP](<../../Leap_Motion_TOP.md> "Leap Motion TOP") / [Leap Motion CHOP](<../../Leap_Motion_CHOP.md> "Leap Motion CHOP") \- Gemini v5 tracking is now supported on macOS Apple Silicon. Go to the [Leap Motion CHOP](<../../Leap_Motion_CHOP.md> "Leap Motion CHOP") help page to locate the downloads required and instructions for installation.
  * [Transform CHOP](<../../Transform_CHOP.md> "Transform CHOP") \- Added 'Xform Matrix/CHOP/DAT' parameter to **apply a matrix transform directly**.

### New Python
* [App Class](<../../App_Class.md> "App Class") \- Added **`processId`member**.
* [OP Class](<../../OP_Class.md> "OP Class"), [td Module](<../../Td_Module.md> "Td Module") \- **New`opex()`method** that works identically to`op()`, except it **will raise an exception if it fails to find the node** instead of returning`None`as`op()`does. **This is the new recommended way to get nodes in parameter expressions** , as the error will be more useful than 'NoneType has no attribute 'par', that is often seen when using op(), for example.
* [TDJSON](<../../TDJSON.md> "TDJSON") \- **BACKWARD COMPATIBILITY ISSUE** Including '**eval' in extraAttrs argument** list will now create a new "eval" entry in the JSON instead of replacing the value in "val".
* Optimized Expressions - Added **support for`DAT.text`**.

### New Palette
* [TDAbleton](<../../TDAbleton.md> "TDAbleton") v2.3 - **Added Change Global OP Shortcut feature** to allow multiple instances, which allows you to connect to multiple Ableton Lives in one project. 
    * v2.1.1 - Fixed defaults on the TDA package.
* [Palette:pointRender](<../../Palette-pointRender.md> "Palette:pointRender") \- version 1.2.2 - Updated to use the latest cameraViewport component.
  * [Palette:cameraViewport](<../../Palette-cameraViewport.md> "Palette:cameraViewport") \- version 0.39.0 - Added comments to help explain setup.
  * [Palette:kinectPointcloud](<../../Palette-kinectPointcloud.md> "Palette:kinectPointcloud") \- version 1.0.2 - Updated to use the latest pointRender and cameraViewport components.
  * [Palette:particlesGpu](<../../Palette-particlesGpu.md> "Palette:particlesGpu") \- Simulation stays stopped when timeline is paused and viewer tumbled.
  * [Palette:treeLister](<../../Palette-treeLister.md> "Palette:treeLister") \- **Optimized row selection and selection reporting**. Exposed more inner members: IDObjDict, ObjIDDict, GetObjectFromID, GetIDFromObj (see [Palette:treeLister](<../../Palette-treeLister.md> "Palette:treeLister") for details).
  * [palette:treeLister](<../../Palette-treeLister.md> "Palette:treeLister") \- **Added 'Alphabetize Tree' parameter** (default True) in case you don't want to alpahabetize, which was forced in previous versions. Also fixes a bug where treeLister could sometimes sort twice when it only needs to sort once.

### Bug Fixes and Improvements
* [OAK-D](<../../OAK-D.md> "OAK-D") \- Upgrade to DepthAI 2.22.0
  * [OpenCV](<../../OpenCV.md> "OpenCV") \- Upgrade to 4.8.0.
  * Upgrade to R3D SDK 8.4.0, used in the [Movie File In TOP](<../../Movie_File_In_TOP.md> "Movie File In TOP") for decoding RED Camera codec in .r3d file format.
  * [RealSense](<../../RealSense.md> "RealSense") \- Upgrade to SDK 2.54.2.
  * [Substance TOP](<../../Substance_TOP.md> "Substance TOP") \- Upgrade to SDK v9.0.1, this enables the use of E.6 Materials.
* [Annotate COMP](<../../Annotate_COMP.md> "Annotate COMP") \- New '**Utility' parameter access to utility flag** (when On, hides from searches).
  * [Camera Blend COMP](<../../Camera_Blend_COMP.md> "Camera Blend COMP") \- Fixed the [Line MAT](<../../Line_MAT.md> "Line MAT") using **incorrect aspect ratio** values when rendering with a blended camera.
  * [Engine COMP](<../../Engine_COMP.md> "Engine COMP") \- Tox files now have the **external tox settings disabled on load**.
  * [Slider COMP](<../../Slider_COMP.md> "Slider COMP") \- Fixed default component to **accept changes to u and v via script**.
  * [Text COMP](<../../Text_COMP.md> "Text COMP") \- Added a new parameter to **parse escape sequences** like '\n' and '\t' when using the Specification DAT. Also **fixed vertical alignment** when using the Specification DAT.
  * [Geo Text COMP](<../../Geo_Text_COMP.md> "Geo Text COMP") \- **Fixed 'Font Color'** not working.
* [GLSL TOP](<../../GLSL_TOP.md> "GLSL TOP") \- Added 'TOPs' parameter to **reference other inputs via parameter** instead of a wired input.
  * [Leap Motion TOP](<../../Leap_Motion_TOP.md> "Leap Motion TOP") / [Leap Motion CHOP](<../../Leap_Motion_CHOP.md> "Leap Motion CHOP") \- Updated Windows to SDK 5.13.2 and added SDK version to the info popup.
  * [Lookup TOP](<../../Lookup_TOP.md> "Lookup TOP") \- Dark/Light UV values will no longer be clamped at 0 on the low end.
  * [Movie File In TOP](<../../Movie_File_In_TOP.md> "Movie File In TOP") \- Fixed a new crash when loading sequences of EXRs.
* [Nvidia Background TOP](<../../Nvidia_Background_TOP.md> "Nvidia Background TOP") \- Fixed issue where input image was passed to the Nvidia model flipped, resulting in poor background removal.
  * [Optical Flow TOP](<../../Optical_Flow_TOP.md> "Optical Flow TOP") \- **BACKWARD COMPATIBILITY ISSUE** \- 'Cost Output' values are now normalized to 0-1, instead of 0-255.
  * [Substance TOP](<../../Substance_TOP.md> "Substance TOP") \- Improvements to parameter generation, specifically with menus.
  * [Video Device In TOP](<../../Video_Device_In_TOP.md> "Video Device In TOP") \- Improved AJA support to work with **dual UHD inputs for Kona HDMI devices**.
  * [Web Render TOP](<../../Web_Render_TOP.md> "Web Render TOP") \- Fixed a crash which could occur loading a project.
* [Body Track CHOP](<../../Body_Track_CHOP.md> "Body Track CHOP") \- Static input images are now reprocessed when the parameters change.
  * [DMX Out CHOP](<../../DMX_Out_CHOP.md> "DMX Out CHOP") \- Fixed bug with sACN/KiNET/ArtNet where **only the first channel might be sent in Packet Per Channel mode**.
  * [Face Track CHOP](<../../Face_Track_CHOP.md> "Face Track CHOP") \- **Face mesh is now included in the Config/Models folder** and the 'Mesh' parameter now defaults to the included mesh file.
  * [Face Track CHOP](<../../Face_Track_CHOP.md> "Face Track CHOP") \- Static input images are now reprocessed when parameters change.
  * [Info CHOP](<../../Info_CHOP.md> "Info CHOP") \- Fixed issue which resulted in **extra channels for the 'Timecode' Info Type** on some OPs.
  * [LTC Out CHOP](<../../LTC_Out_CHOP.md> "LTC Out CHOP") \- **Added 'High FPS Behavior' menu** with the options to cucle or duplicate frames for high frame rate scenarios.
  * [Timer CHOP](<../../Timer_CHOP.md> "Timer CHOP") \- Various Improvements 
    * Next Segment / Prev Segment now updates masterSeconds properly.
    * Stop resetting masterSeconds each cycle.
    * Fixed dropped pulse values.
* [Folder DAT](<../../Folder_DAT.md> "Folder DAT") \- **Improved performance by optimizing filesystem check** and fixed a crash which could occur loading a project. 
    * This optimization also improves performance when a file changes in any File In OPs.
  * [Point SOP](<../../Point_SOP.md> "Point SOP") \- Fixed **incorrect new attribute values** in some cases when an attribute is deleted.
* [Art-Net DAT](<../../Art-Net_DAT.md> "Art-Net DAT") \- **Removed local port parameter** because it is redundant and can conflict with the receiving socket.
  * [Render Pick DAT](<../../Render_Pick_DAT.md> "Render Pick DAT") \- **Now works without any DAT input connected**, so the Python`pick()`method can be used without a dummy input.
  * [Web Server DAT](<../../Web_Server_DAT.md> "Web Server DAT") \- **Fixed`onServerStop`callback** not triggered when 'Restart' parameter is pulsed. Furthermore, an optimization to shut down the web server when its parent component cooking is disabled was added.
* [Custom Operators](<../../Custom_Operators.md> "Custom Operators") \- **Added 'cookCount' member** to the OP_NodeInfo class.
* [Privacy](<../../Privacy.md> "Privacy") \- Improved support for **nested private components**. A private component's children now have access to their parents, even if those parents have their own privacy.
  * [Network Utilities: Comments, Network Boxes, Annotates](<../../Network_Utilities-_Comments,_Network_Boxes,_Annotates.md> "Network Utilities: Comments, Network Boxes, Annotates") \- Comments, Network Boxes and Annotates now have a '**Utility' parameter for turning on and off utility mode**.
* [TOP](<../../TOP.md> "TOP") \- Channel mask on the Common page now **works correctly for Mono and Alpha Textures**.
  * [TOP](<../../TOP.md> "TOP") \- Pixel inspector tool now gives **pixel-centered UV values**.
* Fixed **incomplete panel layouts** when parents employ children scaling.
* Tox files are now saved with the **external tox parameter turned off**.
  * Fixed being able to use backspace or delete in input boxes are are not editable.

### Operator Snippets
* New snippets for [Body Track CHOP](<../../Body_Track_CHOP.md> "Body Track CHOP"), [Timecode CHOP](<../../Timecode_CHOP.md> "Timecode CHOP"), [Bloom TOP](<../../Bloom_TOP.md> "Bloom TOP").

### Backward Compatibility Changes
* **BACKWARD COMPATIBILITY ISSUE** \- [Optical Flow TOP](<../../Optical_Flow_TOP.md> "Optical Flow TOP") \- 'Cost Output' values are now normalized to 0-1, instead of 0-255.
* **BACKWARD COMPATIBILITY ISSUE** \- [TDJSON](<../../TDJSON.md> "TDJSON") \- Including 'eval' in extraAttrs argument list will now create a new "eval" entry in the JSON instead of replacing the value in "val".

## Build 2023.10130 - Aug 16, 2023

### Key Highlights

#### OAK-D AI Sensors

**[OAK-D](<../../OAK-D.md> "OAK-D") cameras offer a range of high-resolution cameras with depth vision and on-chip machine learning**. OAK-D can run computer vision tasks on-device and send the processed images or data to TouchDesigner on both Windows and macOS. For example, an OAK camera can compute human skeleton landmarks for a live RGB image and send both the landmarks and image to TouchDesigner. OAK is short for the OpenCV AI Kit, which originated through online crowd-funding. [Luxonis](<https://www.luxonis.com/>) has expanded the line of OAK hardware and also released several open-source libraries such as DepthAI that run on the OAK. 

The aim of integrating TouchDesigner with OAK cameras is to facilitate novel interactions with the rest of the TouchDesigner environment while providing low-latency, high throughput performance with the OAK hardware. If you think a pure Python example that doesn't involve TouchDesigner is running faster than one which does, please let us know. For example, we aim for the frames-per-second of an OAK's RGB camera received in TouchDesigner to be at least as fast as what you would receive in pure Python with DepthAI and OpenCV. 

**Three new OAK-D operators work together to implement the OAK functionality** : The [OAK Device CHOP](<../../OAK_Device_CHOP.md> "OAK Device CHOP") is the main interface to the camera devices. The [OAK Select CHOP](<../../OAK_Select_CHOP.md> "OAK Select CHOP") extracts channel and dictionary data from the camera results of a OAK Device CHOP. The [OAK Select TOP](<../../OAK_Select_TOP.md> "OAK Select TOP") extracts processed images from the camera. Each DepthAI model running on each camera will have one OAK Device CHOP plus one or more of the OAK Select OPs. 

#### Machine Learning Features
* [Body Track CHOP](<../../Body_Track_CHOP.md> "Body Track CHOP") \- This new CHOP uses [Nvidia Maxine AR SDK](<https://developer.nvidia.com/maxine#ar-sdk>) to perform **body pose estimation** on any TOP video or camera input. It can track bounding boxes and 34 key points of one or more human bodies, with optional joint angles, in 2D or 3D.
* [ZED](<../../ZED.md> "ZED") \- Major overhaul including an SDK update and the addition of **body tracking support** in the [ZED CHOP](<../../ZED_CHOP.md> "ZED CHOP") and a '**Neural' depth camera mode** in the [ZED TOP](<../../ZED_TOP.md> "ZED TOP").
* [Nvidia Upscaler TOP](<../../Nvidia_Upscaler_TOP.md> "Nvidia Upscaler TOP") \- This new TOP used [Nvidia Maxine Video Effects SDK](<https://developer.nvidia.com/maxine#ve-sdk>) to upscale the resolution of an input video. The Upscale mode is faster and offers a 'Strength' parameter. The Super Resolution mode is higher quality and doesn't offer a Strength parameter, but it does have an optional 'Artifact Reduction' toggle.

#### Broadcast and Virtual Production
* [MoSys CHOP](<../../MoSys_CHOP.md> "MoSys CHOP") / [MoSys TOP](<../../MoSys_TOP.md> "MoSys TOP") \- The MoSys CHOP receives data from a **MoSys camera tracking system. The channels can be used to control a virtual camera and to implement lens distortion** via the MoSys TOP as part of a virtual production system.
* [Video Device Out TOP](<../../Video_Device_Out_TOP.md> "Video Device Out TOP") \- On [Deltacast](<../../Deltacast.md> "Deltacast") devices we added support for **12-bit output and custom resolution output** for HDMI/Displayport output.
* [OptiTrack In CHOP](<../../OptiTrack_In_CHOP.md> "OptiTrack In CHOP") \- Previously named the [NatNet In CHOP](<../../NatNet_In_CHOP.md> "NatNet In CHOP"), we renamed it for clarity.

#### Timecode Tools

Numerous [Timecode](<../../Timecode.md> "Timecode") tools has been woven into TouchDesigner. A new Timecode CHOP can create and manage SMTPE timecode and a large selection of OPs in TouchDesigner that deal with time have been updated to be driven by timecode or include a timecode member so they can all be managed effectively. For a full list of these operators, refer to the [Timecode](<../../Timecode.md> "Timecode") page. 
* [Timecode CHOP](<../../Timecode_CHOP.md> "Timecode CHOP") \- **A new CHOP for managing Timecode**
    * Added custom length parameters and extra countdown field to [Info DAT](<../../Info_DAT.md> "Info DAT").
    * Added countdown output channels.
    * Check out the new OP Snippets for this operator.
* [Timeline CHOP](<../../Timeline_CHOP.md> "Timeline CHOP") \- Added a new parameter to **drive timeline time with a timecode object**.
  * [LTC Out CHOP](<../../LTC_Out_CHOP.md> "LTC Out CHOP") \- Added a parameter to drive the LTC Out timecode with a Timecode Object/CHOP/DAT.
  * [Timer CHOP](<../../Timer_CHOP.md> "Timer CHOP") \- Added option in the 'Time Control' parameter to drive the Timer CHOP directly with timecode.
* [Timecode Class](<../../Timecode_Class.md> "Timecode Class") \- A new class to **access timecode features via python** throughout TouchDesigner.
* Many operators that can use timecode now have **new timecode members** to access their timecode directly via python.

#### Laser Control
* [Laser Device CHOP](<../../Laser_Device_CHOP.md> "Laser Device CHOP") \- The Laser Device CHOP can send **laser points to supported laser devices: EtherDream, Helios, and ShowNET**. ShowNET support comes to TouchDesigner for the first time! The devices can be connected to a laser using an ILDA cable, except in the case of ShowNET when an onboard DAC is used. Applications of the Laser Device CHOP include displaying computer-generated shape animations or other special effects of a light show. The Laser Device CHOP replaces the deprecated [EtherDream CHOP](<../../EtherDream_CHOP.md> "EtherDream CHOP") and [Helios DAC CHOP](<../../Helios_DAC_CHOP.md> "Helios DAC CHOP").
* [Laser CHOP](<../../Laser_CHOP.md> "Laser CHOP") \- Added **look-up CHOP for vertex hold min/max angles** and **added 'Blank State Channel'** for help with debugging.

#### New Operators
* [Bloom TOP](<../../Bloom_TOP.md> "Bloom TOP") \- The Bloom TOP creates a **glow effect around bright parts of the image**.
* [GLSL COMP](<../../GLSL_COMP.md> "GLSL COMP") \- The new GLSL COMP **uses GLSL shaders to render an image in a panel directly to the screen**. It is useful for rendering pixel accurate UIs as the resolution will automatically adapt to the DPI scaling of the screen it is displayed on.

#### Engine COMP Overhaul
* [Engine COMP](<../../Engine_COMP.md> "Engine COMP") \- New features and improvements. 
    * **Enabled OP Viewer parameter** on Common parameter page to show a selected viewer.
    * Added '**Asset Paths' parameter to make relative paths** based on the Project .toe file or the External .tox file.
    * Added **TouchEngine process parameters** on the Advanced parameter page. This allows you to quit or launch the process independently from loading your component.
    * Added '**On Engine COMP Load' parameter** which determines what happens when a .tox is loaded (also affects copy & paste).
    * **Errors** on the loaded component are **now reported in the pop-up info text** via middle-mouse button .
    * Added a new **onError() callback** to the Callback DAT.
    * Allow use of user selected operator colors (use color palette to set).
* **New Init Start parameter page** modelled after Init Start on Timer CHOP including a similar set of core control parameters. 
    * Added “Ready when” parameter to specify when the transition to Ready state happens.
    * Added onInitialize() callback.
    * Added 'Go To Done' parameter, and 'On Done' parameter to determine behavior, plus onDone() callback, plus "done" channel, plus "goToDone()" Python command.
    * Added 'Pre-Roll' parameter.
* **Added a docked[Info CHOP](<../../Info_CHOP.md> "Info CHOP") and [Info DAT](<../../Info_DAT.md> "Info DAT")**
    * More channels added in 'General' Info Type.
    * Added “Initialize Start” Info Type group of channels reporting on the Status of the Init Start features mentioned above.
    * Added 'TouchEngine Status' Info Type group of channels for process and component state to better understand the TouchEngine process lifetime.
    * Renamed Engine Perform to 'TouchEngine Perform'.
    * Added “engine_pid” to Info DAT
    * Added [Info CHOP](<../../Info_CHOP.md> "Info CHOP") channels output_cook_abs_frame, engine_absolute_frame, engine_absolute_seconds, and initialize_fail.

#### Lightweight Installer for Windows

**The best option for installing TouchDesigner on Windows is our new lightweight installer**. This installer packages the core elements of TouchDesigner into a much smaller download which lets you select the features of TouchDesigner you require and downloads them on-the-fly. If you don't own devices like Kinect Azure, ZED camera, or even an Nvidia GPU, save time by skipping these items in your install. The download size is smaller and faster, the installation goes more quickly, and TouchDesigner will use less space on your system. Only install what you need! 

**Add additional features after the initial installation** by going to Settings > Add or Remove Programs and locating your TouchDesigner application. Then select 'Modify' from the options menu on the app and the Modify installation dialog will open allowing you to select the additional features you'd like to download and install. 

We will always **continue to maintain a full installer** for those who want everything or need to install TouchDesigner later on machines where there is no internet connection. However, with the addition of more devices, large SDKs, and features using machine learning models, the full installer is now greater than 2.4GB and will continue to grow. The lightweight installer is a great option for anyone working with a reliable internet connection. 

#### More New Features
* **Python 3.11**
    * Python upgraded to 3.11 - Runs 10-60% faster for everything, better error messages, more new and shiny!
    * Full update details [What’s New In Python 3.11](<https://docs.python.org/3/whatsnew/3.11.html>) and [What’s New In Python 3.10](<https://docs.python.org/3/whatsnew/3.10.html>)
* **Working with External Files**
    * New parameters on the Common page of all Components offer better control of managing external file locations and paths.
    * New parameter 'Relative File Path Behavior' allows you to use relative paths that are local to the Project (.toe file) or to the location of the External COMP (.tox file).


Users are invited [to read our article](<https://derivative.ca/community-post/word-about-externals-202310k-builds/68166>) introducing some changes and new features. 
* **Nvidia 40-series GPUs**
    * The machine learning models for Nvidia operators using [Maxine SDKs](<https://developer.nvidia.com/maxine#ar-sdk>) have been updated to include models for the 40-series Geforce and Professional A-series Ada generation GPUs.
* [Noise TOP](<../../Noise_TOP.md> "Noise TOP") \- Added '**Derivative (slope)' toggle** to get the gradient of the noise in the RGB channels. Only works in monochrome mode.
* [Text COMP](<../../Text_COMP.md> "Text COMP") / [Text TOP](<../../Text_TOP.md> "Text TOP") \- New options for selecting fonts via a new '**Typeface' parameter** instead of the previous 'Bold' and 'Italics' parameters.
* [Audio VST CHOP](<../../Audio_VST_CHOP.md> "Audio VST CHOP") \- Added support for **custom bus layouts** and new parameters for controlling the VST plugin's playhead.
* [Bind CHOP](<../../Bind_CHOP.md> "Bind CHOP") \- New '**Exclusive Hold' parameter**. Locks out remaining inputs for this period when change detected.
* [Pattern CHOP](<../../Pattern_CHOP.md> "Pattern CHOP") \- Added a **new 'Cyclic Ramp' ramp** type.
  * [Pulse CHOP](<../../Pulse_CHOP.md> "Pulse CHOP") improvements 
    * Added a second input to **specify custom pulse indices**.
    * **Multiple channels** now supported.
    * Options to set **minimum spacing** values for pulses if they overlap.
    * **Pulse height** determined by the number of repeated indices.
    * Option to **specify units** for the pulse indices in samples, frames, or seconds.
    * Added '**Connect' option to Interpolate parameter** menu which gives true linear interpolation.
* [Timer CHOP](<../../Timer_CHOP.md> "Timer CHOP") \- Numerous improvements 
    * **Active toggle expanded** to: Never / Always / While Running / While Playing. 'While Playing' only cooks if any timers are active and 'Play' is enabled.
    * **New 'Defer Parm Changes' parameter** controls whether or not parameter changes take affect immediately or after the next init/start cycle.
* [Trigger CHOP](<../../Trigger_CHOP.md> "Trigger CHOP") \- Added menu **option 'Update once per Cycle'** to update trigger shape parameters only once each cycle.
* [Insert DAT](<../../Insert_DAT.md> "Insert DAT") \- Added rows and cols via cell expressions and added a new 'Replace if Duplicate Name' toggle to replace existing column/row names if new ones have the same name.
* [Keyboard In DAT](<../../Keyboard_In_DAT.md> "Keyboard In DAT") \- **Overhaul to how characters are handled** with the goal to improve international language support and offer a more consistent interface with keyboard input. 
    * **BACKWARDS COMPATIBILITY ISSUE** \- The 'key' column will no longer return special characters such as !@#$%^&*(). These will now be 1234567890 for better consistency with other shortcut workflows.
    * **New optional 'web_codes' column** , which matches the key code names that Chromium expects.
    * Reworked callback to take a namedtuple, add 'webCode' as a new value.

### New Python
* **Python updated to 3.11**
    * Python 3.11 - Runs 10-60% faster for everything!
    * Create better error messages with Exception.add_note().
    * [PEP 678: Exceptions can be enriched with notes](<https://docs.python.org/3/whatsnew/3.11.html#whatsnew311-pep678>)
    * Full update details here: [What’s New In Python 3.11](<https://docs.python.org/3/whatsnew/3.11.html>)
* Python 3.10 - New ["match" statements](<https://peps.python.org/pep-0636/>). Similar to "switch" in C++ and other languages. 
    * Full update details here: [What’s New In Python 3.10](<https://docs.python.org/3/whatsnew/3.10.html>)


**Reset parameters new python**
* [Par Class](<../../Par_Class.md> "Par Class") \- reset()
  * [ParGroup Class](<../../ParGroup_Class.md> "ParGroup Class") \- reset()
  * [Page Class](<../../Page_Class.md> "Page Class") \- resetPars()
  * [OP Class](<../../OP_Class.md> "OP Class") \- resetPars(parNames='*', parGroupNames='*', pageNames='*', includeBuiltin=True, includeCustom=True)


reset() -> bool - Resets the associated parameters to its default state, returns true if anything was changed. 
[code] 
           op('geo1').par.tx.reset()
           op('geo1').parGroup.t.reset()
           op('geo1').pages[0].resetPars()
           op('player').customPages['Setup'].resetPars()
           op('player').resetPars(includeBuiltin=False) # only reset custom
    
[/code]

**Default parameter new python**
* [Par Class](<../../Par_Class.md> "Par Class") / [ParGroup Class](<../../ParGroup_Class.md> "ParGroup Class").defaultBindExpr .defaultExpr - Get or set the default bind expression on custom parameters.


[code]
           n.par.Float1.defaultBindExpr = 'me.par.Float2'
           n.par.Float1.defaultExpr = 'me.time.frame'
    
[/code]
* [Par Class](<../../Par_Class.md> "Par Class") / [ParGroup Class](<../../ParGroup_Class.md> "ParGroup Class").defaultMode - For custom parameters get or set the default evaluation mode.


[code]
           n.par.Float1.defaultMode = ParMode.EXPRESSION - Resetting the parameter sets it to .defaultExpr expression, so using the previous example n.par.Float1.defaultExpr = 'me.time.frame', then the expression would be set to me.time.frame.
    
[/code]
* [Component Editor Dialog](<../../Component_Editor_Dialog.md> "Component Editor Dialog") \- Added features for default parameter modes.
  * [TDJSON](<../../TDJSON.md> "TDJSON") \- Updated to work with default parameter modes.


  
**General Python Additions and Improvements**
* [App Class](<../../App_Class.md> "App Class").systemFolder - A new member that contains the installation folder for TouchDesigner system files.
  * [ClockCHOP Class](<../../ClockCHOP_Class.md> "ClockCHOP Class") \- Added a new timecode member.
  * [DAT Class](<../../DAT_Class.md> "DAT Class") \- row(),col(),rows(),cols() have a new bool argument`val`.`val=True`returns list of just cell entries instead of list of cells.
  * [Dependency Class](<../../Dependency_Class.md> "Dependency Class").setVal(val, setInfo=None) .setInfo(Keyword, Optional) - Optional information passed to the modified callback. Allows users to give more specific information when setting a value.
  * [ListCOMP Class](<../../ListCOMP_Class.md> "ListCOMP Class") \- Added .dropRow .dropCol members. The current row/col about to be dropped over.
* [OakdeviceCHOP Class](<../../OakdeviceCHOP_Class.md> "OakdeviceCHOP Class") \- Changed masterTimecode/runningTimecode to return a tdu.Timecode rather than a string. Also added a timecode getter that simply returns masterTimecode, similar to the [Timer CHOP](<../../Timer_CHOP.md> "Timer CHOP").
  * [OakselectCHOP Class](<../../OakselectCHOP_Class.md> "OakselectCHOP Class") / [OakselectTOP Class](<../../OakselectTOP_Class.md> "OakselectTOP Class") \- Added a timecode member that returns the referenced OAK Device CHOP's master timecode.
* [OP Class](<../../OP_Class.md> "OP Class").checkSequence() -> list - Returns a (possibly empty) list of any [ParGroup](<../../ParGroup.md> "ParGroup") objects with unmatched sequence flags.
* [Page Class](<../../Page_Class.md> "Page Class").appendMenu(size=1) - Now supports up to 4 menus in a single ParGroup.
  * [Page Class](<../../Page_Class.md> "Page Class") / [Cell Class](<../../Cell_Class.md> "Cell Class") \- Comparisons to 'None' vs None now work properly.
* [PanelCOMP Class](<../../PanelCOMP_Class.md> "PanelCOMP Class") \- Added .dropReady The current state of the drop operation. True when the drop will be accepted.
  * [PanelCOMP Class](<../../PanelCOMP_Class.md> "PanelCOMP Class") \- **BACKWARDS COMPATIBLITY ISSUE** \- Panel.interactMouse/interactTouch will respect 'Enable' parameter toggle.
  * [Par Class](<../../Par_Class.md> "Par Class") \- Custom parameter order attribute is now a float and no longer limited to integers.
  * [Par_Class](<../../Par_Class.md> "Par Class") \- .defaultMode .mode undoable when changed in script.
* [Timecode Class](<../../Timecode_Class.md> "Timecode Class").setLength - A new method for setting a custom length.
  * [Timecode Class](<../../Timecode_Class.md> "Timecode Class").countdown - A new member of the Timecode object that is the difference between the current timecode value and the length.
* [TimerCHOP Class](<../../TimerCHOP_Class.md> "TimerCHOP Class").playingTimecode/cumulativeTimecode - Has been changed to return a tdu.Timecode object rather than a string
* [TOP Class](<../../TOP_Class.md> "TOP Class") \-`cudaMemory()`now supports a 'stream' keyword argument. Use this to make use of a cudaStream_t/CUstream stream to do the work on.
  * [TOP Class](<../../TOP_Class.md> "TOP Class") \- Added`newestSliceWOffset`member for use with [Texture 3D TOP](<../../Texture_3D_TOP.md> "Texture 3D TOP") generated textures in Python.
  * [scriptTOP Class](<../../ScriptTOP_Class.md> "ScriptTOP Class") \-`copyCUDAMemory()`now supports a 'stream' keyword argument. Use this to make use of a cudaStream_t/CUstream stream to do the work on.
* [run](<../../Run_Command_Examples.md> "Run Command Examples") function. The first argument can now be an optional function instead of a string. This can be easier to work with rather than constructing an executable line of code with embedded quotes.


[code]
           run( lambda: print('A') )
           run( lambda x: print(x), 'B' )
           run( print, 'C', 'D', 'E')
    
[/code]
* * run(func) now accepts keywords. ie. run( myfunc, 'C', a=1, stop=True)
* [tdu_Module](<../../Tdu_Module.md> "Tdu Module").match - **BACKWARDS COMPATIBILITY ISSUE** \- Now supports space separated patterns and single ^ terms properly. tdu.match interprets spaces in the pattern argument as separators.


eg: 
[code] 
           tdu.match( "^foo", ["bar"] )    # ["bar"] 
           tdu.match( "* foo", ["bar"] )    # ["bar"]
    
[/code]
* Parameter members .expr, .bindExpr, .defaultExpr, .defaultBindExpr assigned to None in scripts will now be empty string instead of the string 'None'. **BACKWARDS COMPATIBILITY ISSUE**
* When Python parameter expression is blank, return None, not empty string. **BACKWARDS COMPATIBILITY ISSUE**

###  New Palette
* [TDAbleton](<../../TDAbleton.md> "TDAbleton") \- 2.2.0 features of note 
    * Currently playing **arrangement clip info** is now reflected in abletonTrack parameters
    * RunRemoteCode extension functions will no longer work when Listen Only is set on tdaMaster component. This can be overridden with an "overrideListenOnly=True" argument.
    * Added **"Back To Arrangement" toggle** on abletonSong - return tracks to arrangement control
* [Palette:camSchnappr](<../../Palette-camSchnappr.md> "Palette:camSchnappr") \- Upgrading P, Cd etc. identifiers in shaders.
* [Palette:debugControl](<../../Palette-debugControl.md> "Palette:debugControl") \- Version 1.4.0 - Added ability to **print timestamp**.
* [Palette:kantanMapper](<../../Palette-kantanMapper.md> "Palette:kantanMapper") \- Removed tscript from Window COMP parameter.
  * [Palette:kantanMapper](<../../Palette-kantanMapper.md> "Palette:kantanMapper") \- KantanUVHelper, fixing typo in page name.
* [Palette:lister](<../../Palette-lister.md> "Palette:lister") \- Fixed a bug where reordering rows in lister can mangle a sync'd input table if not all tableDAT cols are displayed in lister.
  * [Palette:logger](<../../Palette-logger.md> "Palette:logger") \- v2.1.13 - A **new palette component** wrapping around the [Python Logging Library](<https://docs.python.org/3/library/logging.html>) and interface to add additional Loggers easily in your TouchDesigner projects.
* [Palette:particlesGpu](<../../Palette-particlesGpu.md> "Palette:particlesGpu")
    * **Life can be randomized** or derived of an Effector input. Particles with alpha=0 will not be rendered.
    * New '**Lifemodifier' parameter** to multiply remaining lifetime with effector value.
    * Fixed source interpolation disabled when source input provided.
    * Particles are not created from source points that have alpha 0.
* [Palette:popMenu](<../../Palette-popMenu.md> "Palette:popMenu") \- Fixed issue where title width wasn't incorporated into menu window width. Other cosmetics. Menu updates size when pars change.
  * [Palette:quadReproject](<../../Palette-quadReproject.md> "Palette:quadReproject") \- v0.1.7 - Added support for **multiple lights** in the 'Lights' parameter.
* [Palette:recorder](<../../Palette-recorder.md> "Palette:recorder") \- A **new folder called TDV** S for general video server components. The first component is the **recorder component** which wraps a [Movie File Out TOP](<../../Movie_File_Out_TOP.md> "Movie File Out TOP") for easier recording and encoding of videos.
* [Palette:searchReplace](<../../Palette-searchReplace.md> "Palette:searchReplace") \- Now searches the evaluated value of parameters as well as val, expr, bindExpr.
* [palette:lister](<../../Palette-lister.md> "Palette:lister") and [palette:treeLister](<../../Palette-treeLister.md> "Palette:treeLister") \- Bug fixes and improvements 
    * Added **defaultAutoColDefine** and exposed '**Word Wrap' parameter** in config components.
    * Fixed bug where SetCellLookName function would override striping.
* [palette:treeLister](<../../Palette-treeLister.md> "Palette:treeLister") \- Further improvements 
    * Added **scrollbar controls** to Tree parameter page.
    * Added '**Expand All' pulse button** and ExpandAll function to expose all tree nodes.
    * Fixed bug where FromPathsSelectRows would miss the first row.
    * Fixed bug where input mode with wirePath and parentPath columns would fail.
    * Fixed error messages on initial load.
* [Palette:webRTC](<../../Palette-webRTC.md> "Palette:webRTC") \- Fixes and tweaks to the [signaling components](<../../Palette-signalingServer.md> "Palette:signalingServer") and webRTC components. 
    * Internal loggers are all updated to the latest version of the Logger COMP.
* TransitMap removed (before eventual replacement).

### Bug Fixes and Improvements
* Updated Nvidia Optical Flow to 4.0.11
  * Updated Nvidia Video Effects to 0.7.2
  * Updated Nvidia AR SDK (Face Track) to 0.8.2
  * Updated JUCE v7.0.2
  * Updated Kinect Body Tracking SDK to 1.1.2
  * Ableton Link SDK v3.0.6
* [Container COMP](<../../Container_COMP.md> "Container COMP") \- Fixed a problem with the positioning of popup windows when panel opacity is below one.
  * [List COMP](<../../List_COMP.md> "List COMP") \- Don't edit cells if modifier (shift/ctrl/alt/etc) keys are used. Also fixed an out-of-bounds issue calling rollover with (max_row, max_col) instead of (-1,-1).
* [Text COMP](<../../Text_COMP.md> "Text COMP") \- Improvements and bug fixes 
    * Fixed an issue where **text members were out of date** if the view hadn't been displayed yet.
    * onTextEditEnd() callback is now inside the _Text Value Change_ undo block to allow additional events to be added to the undo step.
    * UI Events are now flushed before the [OP Viewer TOP](<../../OP_Viewer_TOP.md> "OP Viewer TOP") captures a panel viewer to ensure it is up to date with the latest cook which **fixed a case where Text COMP data might be a frame behind**.
* [CHOP to TOP](<../../CHOP_to_TOP.md> "CHOP to TOP") \- Fixed **16-bit float formats** not working.
  * [Kinect Azure TOP](<../../Kinect_Azure_TOP.md> "Kinect Azure TOP") / [Kinect Azure CHOP](<../../Kinect_Azure_CHOP.md> "Kinect Azure CHOP") \- Updated to Body Tracking SDK version 1.1.2
* [Movie File Out TOP](<../../Movie_File_Out_TOP.md> "Movie File Out TOP") \- [NotchLC](<../../NotchLC.md> "NotchLC") \- Fixed bug in **NotchLC encoder** that caused files to end up larger than expected.
  * [Nvidia Denoise TOP](<../../Nvidia_Denoise_TOP.md> "Nvidia Denoise TOP") / [Nvidia Background TOP](<../../Nvidia_Background_TOP.md> "Nvidia Background TOP") \- Updated to Nvidia Video Effects library version 0.7.2
  * [Video Device In TOP](<../../Video_Device_In_TOP.md> "Video Device In TOP") \- [Info DAT](<../../Info_DAT.md> "Info DAT") no longer includes output devices.
* [Audio VST CHOP](<../../Audio_VST_CHOP.md> "Audio VST CHOP") \- **Added timestamp argument** to onReceiveMidi() callback. 
    * [AudiovstCHOP Class](<../../AudiovstCHOP_Class.md> "AudiovstCHOP Class").send/sendExclusive - Added timestamp keyword argument.
* [Info CHOP](<../../Info_CHOP.md> "Info CHOP") \- **Added "All" info type** to display all info available.
* [Logic CHOP](<../../Logic_CHOP.md> "Logic CHOP") \- '**Convert Input'** menu indexing fixed.
  * [Lookup CHOP](<../../Lookup_CHOP.md> "Lookup CHOP") \- **Added 'Extend Condition' menus** with options for 'Use Input' and the standard extend options found elsewhere ie. (Hold, Cycle, etc).
* [MQTT Client DAT](<../../MQTT_Client_DAT.md> "MQTT Client DAT") \- **Added topic argument** to onPublish callback.
  * [OP Find DAT](<../../OP_Find_DAT.md> "OP Find DAT") \- 'Include Utility Off' no longer includes children of utility nodes.
  * [UDP In DAT](<../../UDP_In_DAT.md> "UDP In DAT") / [TCP/IP DAT](<../../TCP/IP_DAT.md> "TCP/IP DAT") / [Touch In DAT](<../../Touch_In_DAT.md> "Touch In DAT") / [Touch Out DAT](<../../Touch_Out_DAT.md> "Touch Out DAT") / [OSC In CHOP](<../../OSC_In_CHOP.md> "OSC In CHOP") \- Updated the way TCP and UDP sockets bind to ports. We now can **issue more warnings depending on the status of the port** and how the binding of the socket went, for exmaple, if the port is already in use or not. Windows only.
* [Line MAT](<../../Line_MAT.md> "Line MAT") \- Now **supports draw vectors** for point primitives.
* [SOP](<../../SOP.md> "SOP") operators now support directly saving contents as the following formats **dae, 3ds, dxf, obj** (in addtion to fbx).
  * [Blend SOP](<../../Blend_SOP.md> "Blend SOP") \- Fixed crash when blend weights reached 0.
  * [Text SOP](<../../Text_SOP.md> "Text SOP") \- Fixed crash in some cases when using a Font File.
* [Search / Replace Dialog](<../../SearchReplace_Dialog.md> "SearchReplace Dialog") now searches the evaluated value of parameters as well as val, expr, and bindExpr.
  * Improved accuracy of **GPU timing calculations**.
  * Fixed password dialog sometimes not opening on top of other windows.
  * Fixed floating network editors sometimes being always on top.
  * Fixed parameter dialog to not show default parmeters in non-default mode (eg: './help' and 'repositioncomp' in containers)
  * Fixed Global OP shortcuts not registering properly on external toxes.
  * Fixed spurious errors when using [Page](<../../Page_Class.md> "Page Class").appendPar()
  * TOP viewer pixel value picking (when viewer is active) now works correctly for 3D textures and Cube Map textures.
  * Added definitions for **media keys** i.e. AudioVolumeUp, BrowserBack, etc
  * Added drag and drop support for **FLAC audio files**.
  * dragEnd callback 'droppedOn' now distinguishes between Par and ParGroup.


  
**Sequential Parameters** [Sequential Parameters](<../../Sequential_Parameters.md> "Sequential Parameters") are sets of parameters in TouchDesigner that can be grown using the +/- buttons in the parameter dialog. **We have revamped the naming as follows**. 

The new naming format is:`<sequence name><block index><parName>`. 

Every sequence now has a "sequence name" which is added as a prefix to every parameter that is part of the sequence. This is followed by a "block index", which is the index of the block (set of associated parameters) within the sequence. 

For example, the name/value pars in constantCHOP used to be called name0/value0, name1/value1, etc. The new names are: const0name/const0value, const1name/const1value etc. Other notable examples are extensions (sequence name "ext") and internal operators (sequence name "iop") TouchDesigner will attempt to understand the old names as aliases, but there can still be backwards compatibility issues in some cases. 

  
**Licensing**
* On Windows, TouchDesigner's **License System Codes are now generated differently** to reduce the chance of a system code change when applying Windows Updates. Old keys will work in this 2023.10k branch, however, new keys created in this 2023.10k branch will not work with older versions of TouchDesigner. We also have release an update to 2022.20k branch so any builds released after July 10 2023 will also work with the new keys created in this 2023 version. **In summary - If you want to use 2022 and 2023 versions with the same key, either a) create your key using 2022 builds, or b) use a 2022 build released after July 10 2023**.
  * **Errors are now provided** when [Floating Cloud](<../../Floating_Cloud_Licenses.md> "Floating Cloud Licenses") and [Dongle](<../../License_Dongle.md> "License Dongle") licenses are expired for the current build.
  * **[Floating Cloud](<../../Floating_Cloud_Licenses.md> "Floating Cloud Licenses") licenses won't be consumed anymore** if a better [Dongle](<../../License_Dongle.md> "License Dongle") license is present on the system. Furthermore, floating cloud or dongle licenses won't be used if a higher level local license is installed through the [Key Manager Dialog](<../../Key_Manager_Dialog.md> "Key Manager Dialog").


  
**Panel Layout Optimization**
* Lots of work was done to **speed up internal panel layout code** resulting in many control panels performing significantly faster. If you discover regressions or control panels that are still extremely slow, please contact us via the [bugs forum](<https://forum.derivative.ca/>).
