# Release Notes/Experimental

This branch is now available as 2025 Official Builds **2025.31500 - Oct 29 2025** \- [Download Here](<https://derivative.ca/release/202531500/73152>)

[Download old Experimental Builds here](<https://derivative.ca/download/experimental>)

Experimental builds include new features still in development and testing, features are subject to change or even be removed. For the stability and reliability required for performances and project deliveries, use the production ready [Official Builds](<../Release_Notes.md> "Release Notes"). 

**Known Issues** and **Backward Compatibility** warnings below should be read carefully. 

[Download POPs Sample Package here](<https://www.dropbox.com/scl/fo/0e1hsc1isbhg7o2hd7vnm/ALXKQfGHE0paETnPpWvo7VQ?rlkey=4ih7bxgmcnrdau3ue7xxnee10&st=r9oi2joy&dl=0>)

## Known Issues
* When using HDR Window Pixel Formats (see [Color Space](<../Color_Space.md> "Color Space")), displaying HDR content as TOP backdrop can result in parts of the network editor being hard to view due to bad alpha blending. Turning off TOP backdrop display avoids this issue.


Please report all issues to the **[Bugs Forum](<https://forum.derivative.ca/c/bugs/8>)** , remember to include build number. 

[![](../images/thumb/0/09/ExperimentalTab.png/250px-ExperimentalTab.png)](</File:ExperimentalTab.png>)

[](</File:ExperimentalTab.png> "Enlarge")

Check the Experimental tabs in wiki
* Experimental Documentation - While we are far along in documentation, there are still numerous features and new operators that are awaiting documentation. Note that when you are reading the wiki, if there is documentation for Experimental Builds it will be found in the articles "Experimental" tab.

## Backward Compatibility

We try to make upgrading to new TouchDesigner branches as painless as possible, but sometimes changes are made that are not compatible with the features in older builds. Please review these changes as preparation for moving your projects to 2025.30000. 
* **BACKWARD COMPATIBILITY ISSUE** \- [File In CHOP](<../File_In_CHOP.md> "File In CHOP") \- .chan files now preserve channel names instead of always defaulting to chan1, chan2, chan3, ...
  * **BACKWARD COMPATIBILITY ISSUE** \- [Timer CHOP](<../Timer_CHOP.md> "Timer CHOP") \- The first segment was always one sample short, this has now been fixed.
  * **BACKWARD COMPATIBILITY ISSUE** \- [ZED CHOP](<../ZED_CHOP.md> "ZED CHOP") \- Now needs to point to a [ZED TOP](<../ZED_TOP.md> "ZED TOP") to select it's camera source.
  * **BACKWARD COMPATIBILITY ISSUE** \- [ZED SOP](<../ZED_SOP.md> "ZED SOP") \- Now needs to point to a [ZED TOP](<../ZED_TOP.md> "ZED TOP") to select it's camera source.
  * **BACKWARD COMPATIBILITY ISSUE** \- [ZED](<../ZED.md> "ZED") \- Upgraded to ZED SDK 5.0.1, this update means Pascal GPUs are no longer supported with ZED.
  * **BACKWARD COMPATIBILITY ISSUE** \- [Par Class](<../Par_Class.md> "Par Class") \- Comparisons now use parameter evaluations in all cases. par1 == par2 would previously only return true if it were the same parameter object, now it compares their evaluation results.
  * **BACKWARD COMPATIBILITY ISSUE** \- [ParGroup](<../ParGroup.md> "ParGroup")`.enable`and`.readOnly`members now returns a tuple of values instead of a single bool value, as Par's are now individually enable-able.
  * **BACKWARD COMPATIBILITY ISSUE** \- [Par Class](<../Par_Class.md> "Par Class") / [ParGroup Class](<../ParGroup_Class.md> "ParGroup Class") \-`.readOnly`can now be set per Par, not just the entire ParGroup as a whole.
  * **BACKWARD COMPATIBILITY ISSUE** \- 'me' context no longer wrongly set to root in some cases. When executing a run() command, in some cases 'me' value was set to root instead of the location the run command originated from. This could lead to permission errors trying to access neighbouring content within a private component for example.
  * **BACKWARD COMPATIBILITY WARNING** \- [DMX Fixture POP](<../DMX_Fixture_POP.md> "DMX Fixture POP") / [DMX Map DAT](<../DMX_Map_DAT.md> "DMX Map DAT") \- Changed channel values to go from range 1-512 rather than 0-511 to match the DMX512 addressing standard.
  * **BACKWARD COMPATIBILITY WARNING** \- [MIDI In CHOP](<../MIDI_In_CHOP.md> "MIDI In CHOP") \- While using the CHOP with 'Simplified Output' = Off (ie. using non-simplified output, 1-based Index parameter was fixed for Note type midi messages by adding 1 to the index of the note, controller, velocity, aftertouch. This doesn't affect the channel number. When loading older files, channel index for Note midi messages may be incremented by one if the 1 Based Index parameter was saved toggled to On in those older files.
  * **BACKWARD COMPATIBILITY WARNING** \- [DMX Fixture POP](<../DMX_Fixture_POP.md> "DMX Fixture POP") \- DMX Channel Names _must not include spaces_ now.
  * **BACKWARD COMPATIBILITY WARNING** \- [POP](<../POP.md> "POP") \- A number of POP parameters were renamed and extended in size. This may affect loaded values or expressions in previous toe or tox files.  
For example some Random POP parameters (Amplitude, A, B, etc) were extended to have per-axis parameters (controlled by the size parameter), similar to the Noise POP. This required updating the RoyTimWorkshop file in the Examples folder. Please redownload the examples or be aware of these changes.
  * **BACKWARD COMPATIBILITY WARNING** \- [TDFunctions](<../TDFunctions.md> "TDFunctions") \- Improved error messaging and behavior of`createProperty`. However, using delattr to delete a property created by`createProperty`will now only set the value to None.
  * **BACKWARD COMPATIBILITY WARNING** \-`ui.rolloverPanel`now reverts back to None when no panel is currently being rolled over. Previously it would remain pointing to the last panel.

## Official Build 2025.31500 Oct 29, 2025

**NOTE: This build was promoted to Official 2025**

### New Python
* [OP Class](<../OP_Class.md> "OP Class").`asType(<OP class> class, checkType=False)`-> OP
    * A new wrapper function overridden in TDI type checking. Returns itself.
    * class - Expected type of this operator.
    * checkType - (Optional) If True, raise an exception if this operator is not a member or subtype of class.
  * [Optimized Python Expressions](<../Optimized_Python_Expressions.md> "Optimized Python Expressions") \- Optimized [Pattern CHOP](<../Pattern_CHOP.md> "Pattern CHOP")'s`.chanIndex`and`.sampleIndex`.

### New Palette
* [Palette:multiLevel](<../Palette-multiLevel.md> "Palette:multiLevel") \- Converted to use POPs.
  * [Palette:tdPyEnvManager](<../Palette-tdPyEnvManager.md> "Palette:tdPyEnvManager") \- v1.2.10 - Samples update. Fixed a case where a vEnv could be created in the wrong folder if the .toe file was not saved first before adding COMP to project.
  * [Palette:tdPyEnvManager](<../Palette-tdPyEnvManager.md> "Palette:tdPyEnvManager") \- v1.2.9 - Fixed a case where the COMP status could be marked as linked and ready when no vEnv was present.
  * [TDAbleton](<../TDAbleton.md> "TDAbleton") \- 2.6.3 - Fixed a single frame error on abletonTrack when going from arrangement clip to none. Increased OSC buffer size and improved log messages.

### Bug Fixes and Improvements

**COMP**
* [Engine COMP](<../Engine_COMP.md> "Engine COMP") / [TouchEngine](<../TouchEngine.md> "TouchEngine") \- Fixed issues which could cause unexpected behaviour or crashes.


**POP**
* [Alembic In POP](<../Alembic_In_POP.md> "Alembic In POP") \- Added 64-bit attribute support and more attribute types (eg. Point, Quat, Box, M33).


**TOP**
* [GLSL TOP](<../GLSL_TOP.md> "GLSL TOP") \- Improved errors when array uniforms are incorrectly assigned on the 'Vectors' page.
  * [Movie File Out TOP](<../Movie_File_Out_TOP.md> "Movie File Out TOP") \- Added support for Opus audio codec.
* [Scalable Display TOP](<../Scalable_Display_TOP.md> "Scalable Display TOP") \- Added new parameter 'Apply Camera Offset' to use the camera offsets in [Scalable Atlas](<https://www.scalabledisplay.com/products/scalable-atlas/>) files.
  * [Video Stream Out TOP](<../Video_Stream_Out_TOP.md> "Video Stream Out TOP") \- Fixed cases where 'Keyframe Interval' and 'B-Frame' parameters were ignored.
  * [Video Stream Out TOP](<../Video_Stream_Out_TOP.md> "Video Stream Out TOP") \- New 'Ultra High Quality' option in the 'Quality' menu.
  * [Video Stream Out TOP](<../Video_Stream_Out_TOP.md> "Video Stream Out TOP") \- Added support for H265/HEVC codec for Enhanced RTMP.
  * [Video Stream Out TOP](<../Video_Stream_Out_TOP.md> "Video Stream Out TOP") \- Added support for Opus audio codec when using SRT output.


**CHOP**
* [CPlusPlus CHOP](<../CPlusPlus_CHOP.md> "CPlusPlus CHOP") \- Fixed the OP_TimeInfo structure not having useful deltaFrames when in non-timeslice mode.
  * [Laser CHOP](<../Laser_CHOP.md> "Laser CHOP") \- Fixed a bug where 'Closed Shape Overlap' could create a gap at the start/end of a closed shape.
  * [Laser Device CHOP](<../Laser_Device_CHOP.md> "Laser Device CHOP") \- Fixed flickering bug when sending to **Helios** devices.
  * [Laser Device CHOP](<../Laser_Device_CHOP.md> "Laser Device CHOP") \- For Helios devices, added an [Info CHOP](<../Info_CHOP.md> "Info CHOP") channel that reports whether the device supports extended frames (ie. with user channels and 16-bit color)
* [Noise CHOP](<../Noise_CHOP.md> "Noise CHOP") \- Reset parameters now affects Random and Brownian ('Num of Integrals' = 0) modes as expected.


**DAT**
* [Execute DAT](<../Execute_DAT.md> "Execute DAT") \-`onStart`now called after other initializing scripts during load.
  * [Video Devices DAT](<../Video_Devices_DAT.md> "Video Devices DAT") \- Fixed output not working for some drivers.
  * [Web Client DAT](<../Web_Client_DAT.md> "Web Client DAT") \- In the`onResponse`callback, change "set-cookies" in the header to be a list instead of a single value.


**MAT**
* [GLSL MAT](<../GLSL_MAT.md> "GLSL MAT") \- Improved errors when array uniforms are incorrectly assigned on the 'Vectors' page.

## Build 2025.31310 Oct 8, 2025

### New Features
* [Alembic In POP](<../Alembic_In_POP.md> "Alembic In POP") \- A new POP for loading alembic file sequences into POPs
  * [File Out POP](<../File_Out_POP.md> "File Out POP") \- The File Out POP allows you to write out POP contents to different file types. This includes point, geometry and scene file types. You can record a sequence of .obj or .exr files by setting the 'Type' parameter to 'File Sequence'. Some file formats have fixed attributes that File Out POP look for such as the .spz and .obj file formats. While other files allow arbitrary attribute writing such as .exr and .ply formats.
  * [Layer Mix TOP](<../Layer_Mix_TOP.md> "Layer Mix TOP") \- The new Layer Mix TOP lets you composite unlimited image layers in a layer stack, and gives you individual adjustment controls over each layer. To avoid clutter and unneeded parameters, you can select only the adjustments you want to use by enabling them. You can also specify a background plate to composite your layers over.
  * [Color Space](<../Color_Space.md> "Color Space") \- Added 'ACES2065_1' as a working color space option.
  * [Color Space](<../Color_Space.md> "Color Space") \- Added 'UI Reference White' as another control for TouchDesigner's interface and more generally Panel COMPs to set their reference white brightness.

### New Python
* These Python [preferences](<../Preferences.md> "Preferences") are now off by default. 
    * Add Externally Installed Python Site-Packages to Search Path
    * Add Python User Site-Packages to Search Path
  * [ProgressiveUnloader Class](<../ProgressiveUnloader_Class.md> "ProgressiveUnloader Class") \- Renamed from 'Progressive Unload Class'.
  * [Color Class](<../Color_Class.md> "Color Class") \- Added`colorSpacePrimaries`query.
  * [COMP Class](<../COMP_Class.md> "COMP Class")`.progressiveUnload()`\- Now errors if no argument provided for splitting the unload over multiple frames.
  * [COMP Class](<../COMP_Class.md> "COMP Class")`.progressiveUnloader`\- This member is of type ProgressiveUnloader Class now (renamed from ProgressiveUnload).
  * [COMP Class](<../COMP_Class.md> "COMP Class")`.findChildren()`now updates properly when searching by value.
  * [Page Class](<../Page_Class.md> "Page Class")`.appendParGroup(name, parGroup=p)`\- Fixed a crash that could occur.
  * [TOP Class](<../TOP_Class.md> "TOP Class")`.pixelFormatName`member added to get the pixel format menuName. For all python handling and parameter interactions this should be used instead of`pixelFormat`.
  * [TOP Class](<../TOP_Class.md> "TOP Class")`.save()`now returns`FileSaveStatus`python object which has methods and members for querying info regarding the save task. In particular,`isCompleted()`returns true if saving finished, useful for asynchronous mode.
  * [UI Class](<../UI_Class.md> "UI Class") \- New rollover members return the object currently being rolled over. One of:`ui.rolloverPar`,`ui.rolloverParGroup`,`ui.rolloverPage`,`ui.rolloverOp`,`ui.rolloverPanel`in that order.

### New Palette
* [Palette:autoMediaPlayer](<../Palette-autoMediaPlayer.md> "Palette:autoMediaPlayer") \- Fix for repeating the last movie and better randomization in selection.
  * [Palette:domeViewer](<../Palette-domeViewer.md> "Palette:domeViewer") \- v0.5.0 - Added toggle 'Render Dome FLoor' to control floor rendering, and added a toggle for 'Render North Pointer (Arrow)'. Renamed the 'Update POV / Reset To' parameter.
  * [Palette:logger](<../Palette-logger.md> "Palette:logger") \- v2.6.4 - Fixed a potential issue where the logger would not be recreated when a specific configuration change required full reset of the logger object.
  * [Palette:searchReplace](<../Palette-searchReplace.md> "Palette:searchReplace") \- Fixed 'whole words' mode for search strings with special characters.
  * [TDAbleton](<../TDAbleton.md> "TDAbleton") \- 2.6.2 - Added separate MPE MIDI devices. The abletonMIDI component now has a default pitchbend channel option. Minor bug fixes.
  * [Palette:tdPyEnvManager](<../Palette-tdPyEnvManager.md> "Palette:tdPyEnvManager") \- v1.2.8 - The`Helper`class is now loaded during TouchDesigner startup. If a`TDPyEnvManagerContext.json`file is present next to the`.toe`file and the registered environment is valid, it will be added to the Python module search path during startup. This ensures that Python extensions depending on third-party libraries initialize properly. More details on the [Helper documentation.](<../TDPyEnvManagerHelper.md> "TDPyEnvManagerHelper")
    * Numerous additional improvements for stability, logging, and some updates to the samples.

### Bug Fixes and Improvements
* [Orbbec](<../Orbbec.md> "Orbbec") \- Updated to SDK 1.10.16, this is compatible with Orbbec Femto Mega firmware v1.3.0+.
  * [RealSense](<../RealSense.md> "RealSense") \- Updated to SDK v2.56.5


  
**COMP**
* [Engine COMP](<../Engine_COMP.md> "Engine COMP") \- Fixed a potential hang or crash when some errors occurred.
  * [Engine COMP](<../Engine_COMP.md> "Engine COMP") / [TouchEngine](<../TouchEngine.md> "TouchEngine") \- Fixed an issue which could cause TouchEngine to crash when using POP In or Out on macOS.
  * [Geometry COMP](<../Geometry_COMP.md> "Geometry COMP") \- Fixed a crash which could happen when the parent's Geometry COMP was being disabled. Additionally fixed a crash related to the viewer bounding box and instancing.
  * [Geo Text COMP](<../Geo_Text_COMP.md> "Geo Text COMP") \- Fixed top and bottom text padding when using a Specification DAT/CHOP.
  * [Panel Component](<../Panel_Component.md> "Panel Component") \- Fixed 'Opacity' giving in darker results than 2023.10000 Official builds.
  * [Text COMP](<../Text_COMP.md> "Text COMP") \- Fixed a bug selecting strings using python in single line mode.
  * [Window COMP](<../Window_COMP.md> "Window COMP") \- Added parameter to control 'Output Color Space' when [Working Color Space](<../Color_Space.md> "Color Space") is set to a Color Space other than 'Passthrough'.


**POP**
* [POP](<../POP.md> "POP") \- [macOS](<../MacOS.md> "MacOS") Intel machines will now work with POPs. Please note new minimum [System Requirements](<../System_Requirements.md> "System Requirements") for Macs.
  * [POP](<../POP.md> "POP") \- Fixed issue which caused crashes and corrupt output on Macs with AMD GPUs.
  * [POP](<../POP.md> "POP") \- Fixed issue on [macOS](<../MacOS.md> "MacOS") where using too many attributes would cause unexpected behavior. You will notice most POP Guide samples and example file work better on macOS now.
  * [Box POP](<../Box_POP.md> "Box POP") \- Fixed Box and Face mapping modes on rounded corner boxes.
  * [CPlusPlus POP](<../CPlusPlus_POP.md> "CPlusPlus POP") \- Disabling parameters now works correctly.
  * [CPlusPlus POP](<../CPlusPlus_POP.md> "CPlusPlus POP") \- Restrict when createBuffer/getAttribute can be used with CUDA memory. Also reduced memory allocations when using CUDA buffers.
  * [Force Radial POP](<../Force_Radial_POP.md> "Force Radial POP") \- Renamed from [Force POP](<../Force_POP.md> "Force POP")
    * Positive strength values on planar force now pull the particles away from the plane.
    * Rearranged and renamed some parameters and changed the logic and behavior of falloff controls.
  * [Random POP](<../Random_POP.md> "Random POP") \- New attribute size is now based on 'Random Size' parameter (When Combine is Set and a new attribute name is in the output scope).


**TOP**
* [GLSL TOP](<../GLSL_TOP.md> "GLSL TOP") \- Fixed an issue where changing the texture dimension of the input didn't trigger the shader to recompile.
  * [Movie File Out TOP](<../Movie_File_Out_TOP.md> "Movie File Out TOP") \- Added support for encoding AV1 codec video (on newer NVIDIA GPUs).
  * [NVIDIA RTX Video TOP](<../NVIDIA_RTX_Video_TOP.md> "NVIDIA RTX Video TOP") \- Added support for more input pixel formats and fixed swapped color channels in some cases.
  * [OpenColorIO TOP](<../OpenColorIO_TOP.md> "OpenColorIO TOP") \- Fixed crash that occured when choosing 'Working Color Space' but no Working Color Space was set in the project.
  * [POP to TOP](<../POP_to_TOP.md> "POP to TOP") \- Added new layout modes.
  * [Render Simple TOP](<../Render_Simple_TOP.md> "Render Simple TOP") \- Added new 'Normalize View' and 'Normalize Geo' parameters. Fixed an issue where the first render may be blank.
  * [Video Stream Out TOP](<../Video_Stream_Out_TOP.md> "Video Stream Out TOP") \- Added support for AV1 codec for RTMP output.


**CHOP**
* [Audio Render CHOP](<../Audio_Render_CHOP.md> "Audio Render CHOP") \- Crashes and bugs fixed, performance improved. 
    * Added 'Baked Data Variation' parameter to switch simulation modes between 'Static Listener' and 'Static Source', where baked reflection data is calculated in reference to whichever objects are set to be static.
    * Added parameters for attenuation (this only works when reflections are disabled).
  * [Render Pick CHOP](<../Render_Pick_CHOP.md> "Render Pick CHOP") \- Added 'Name Format' and 'Type Suffix' parameters to provide POP friendly naming.


**DAT**
* [Null DAT](<../Null_DAT.md> "Null DAT") \- Fixed a bug that could cause text to disappear from read-only text DATs after clicking inside to select text.
  * [Render Pick DAT](<../Render_Pick_DAT.md> "Render Pick DAT") \- Added 'Name Format' and 'Type Suffix' parameters to provide POP friendly naming.


**SOP**
* [Alembic SOP](<../Alembic_SOP.md> "Alembic SOP") \- Fixed velocity attribute import for point primitives and fixed a crash that could occur dealing with velocities.


**Misc**
* [Orbbec](<../Orbbec.md> "Orbbec") \- Upgraded SDK 
    * Upgraded Orbbec SDK to 1.10.16, this is compatible with Orbbec Femto Mega firmware v1.3.0+.
    * Upgraded Kinect Azure wrapper (K4A) to 1.10.3.
    * Orbbec SDK now has support for Intel-based Macs, previously it was for Apple Silicon only.
  * [Custom Operators](<../Custom_Operators.md> "Custom Operators") \- Added query for working color space primaries.`TD::getWorkingColorSpacePrimaries()`.
  * TouchDesigner and TouchPlayer now always begin with the timeline playing *unless* it is explicitly stopped in a startup script.
  * Fixed negative GPU memory counting in POPs that occurred in some cases.
  * New Touch Tips added.

### Operator Snippets

Introducing OP Snippets for POPs and more. There are snippets for almost all POPs and related inter-family operators, along with a bunch of new ones for other parts of TouchDesigner. 

Recall there are three way to get to Snippets \- rclick on names in the OP Create dialog, rclick -> Operator Snippets on any node, and the top menu bar Help -> Operator Snippets. 

The`Overview.toe`file in the POPs`Examples`folder still has a lot of examples explaining the numerous concepts of POPs, like attributes and dimension, so you can continue to explore in`Overview.toe`. The other folders in`Examples`continue to be very useful, including Darien Brito's`POPGuide`plus`RoyTimWorkshop`. 

The`Examples`continue to be at [Dropbox Link for POPs Examples folder](<https://www.dropbox.com/scl/fo/0e1hsc1isbhg7o2hd7vnm/ALXKQfGHE0paETnPpWvo7VQ?rlkey=4ih7bxgmcnrdau3ue7xxnee10&e=1&st=r9oi2joy&dl=0>). 

### Backward Compatibility Changes

**BACKWARD COMPATIBILITY ISSUE**
* **BACKWARD COMPATIBILITY WARNING** \-`ui.rolloverPanel`now reverts back to None when no panel is currently being rolled over. Previously it would remain pointing to the last panel.

## Build 2025.30960 Sep 09, 2025

### New Features
* [Force POP](<../Force_POP.md> "Force POP") overhaul - Local forces have been broken into separate controls so one Force POP can apply Radial, Axial, Spiral, or Planar forces at once. Additional falloff controls have been added. This is a work in progress and will be tweaked further. We'd be happy to hear your feedback.
* Composite TOPs can now use Justify Horizontal and/or Justify Vertical parameters when 'Pre-Fit Overlay' is set to Fit Vertical, Fit Horizontal or Fit Best modes. Which justify parameters are enabled depends on the mode selected, for example Fit Vertical can only be justified horizontally and Fit Horizontal can only be justified vertically. This has been added to the following TOPs: [Composite TOP](<../Composite_TOP.md> "Composite TOP") / [Over TOP](<../Over_TOP.md> "Over TOP") / [Cross TOP](<../Cross_TOP.md> "Cross TOP") / [Difference TOP](<../Difference_TOP.md> "Difference TOP") / [Add TOP](<../Add_TOP.md> "Add TOP") / [Inside TOP](<../Inside_TOP.md> "Inside TOP") / [Multiply TOP](<../Multiply_TOP.md> "Multiply TOP") / [Screen TOP](<../Screen_TOP.md> "Screen TOP") / [Subtract TOP](<../Subtract_TOP.md> "Subtract TOP") / [Under TOP](<../Under_TOP.md> "Under TOP") / [Outside TOP](<../Outside_TOP.md> "Outside TOP")

### New Python
* Fixed hang when executing help() or other python commands that waited on user input to continue.
  * Fixed parent() expressions not updating on renames.
* [TDStoreTools](<../TDStoreTools.md> "TDStoreTools") \- Improved error messaging and behavior of`DependList`and`DependDict`* [TDFunctions](<../TDFunctions.md> "TDFunctions") \- Improved error messaging and behavior of`createProperty`. **Backwards Compatibility** \- using delattr to delete a property created by`createProperty`will now only set the value to None

### New Palette
* [Palette:domeViewer](<../Palette-domeViewer.md> "Palette:domeViewer") \- v0.4.1 - Initial release. A new COMP inspired from Fred Tretout's InsideDome. Can be used to previz content for domes as well as easily generate the dome POP to design content with.
* [TDAbleton](<../TDAbleton.md> "TDAbleton") \- v.2.6.1 Bug fix - MIDI m4l devices now work with MPE.
* [Palette:tdPyEnvManager](<../Palette-tdPyEnvManager.md> "Palette:tdPyEnvManager") \- v1.0.11 - Removed helper env name length restriction.

### Bug Fixes and Improvements
* [Deltacast](<../Deltacast.md> "Deltacast") \- Upgraded to SDK 6.31.1.


**COMP**
* [Engine COMP](<../Engine_COMP.md> "Engine COMP") \- Change to [Info CHOP](<../Info_CHOP.md> "Info CHOP") channels so`component_none`is 0 when`component_error`is 1 (eg after a failed load).
  * [Engine COMP](<../Engine_COMP.md> "Engine COMP") \- Fixed 'Ready When' = 'Component Running' mode so the output is updated when in the ready state.
  * [Engine COMP](<../Engine_COMP.md> "Engine COMP") \- Fixed issue which could leave an Engine COMP in an error state after loading a .tox failed.


**POP**
* [DMX Fixture POP](<../DMX_Fixture_POP.md> "DMX Fixture POP") \- Fixed setting of universe values > 15 via DMXFixtureUniverse attribute.
  * [DMX Out POP](<../DMX_Out_POP.md> "DMX Out POP") \- Added 'ArtSync Timeout' parameter to specify the time in milliseconds that ArtSync will wait for all ArtDmx packets to complete sending before sending the ArtSync packet. If they have not all been sent when the timeout is reached, then ArtSync will terminate and the ArtSync packet will not be sent. Additionally, a new frame of ArtDmx packets will be sent and a new ArtSync will be initiated.
  * [DMX Out POP](<../DMX_Out_POP.md> "DMX Out POP") \- Fixed some ArtSync latency.


**TOP**
* [Deltacast](<../Deltacast.md> "Deltacast") \- Enumerate boards that can't input and output from the same connectors correctly.
  * [Deltacast](<../Deltacast.md> "Deltacast") \- Added support for cards that don't have bi-directional connectors.
  * [Movie File In TOP](<../Movie_File_In_TOP.md> "Movie File In TOP") \- Added 'HLG Peak Nits' parameter to control the peak nits for HLG encoded content.
* [Movie File Out TOP](<../Movie_File_Out_TOP.md> "Movie File Out TOP") \- Added support for encoding AAC audio.
  * [Noise TOP](<../Noise_TOP.md> "Noise TOP") \- Fixed this node always using it's input Pixel Format.
  * [Render Simple TOP](<../Render_Simple_TOP.md> "Render Simple TOP") \- Renamed from [Simple Render TOP](<../Simple_Render_TOP.md> "Simple Render TOP").
* [Video Device In TOP](<../Video_Device_In_TOP.md> "Video Device In TOP") \- Fixed some issues with 8192x4320 resolution capture on [Deltacast](<../Deltacast.md> "Deltacast") cards.
  * [Video Device Out TOP](<../Video_Device_Out_TOP.md> "Video Device Out TOP") \- Fixed [Deltacast](<../Deltacast.md> "Deltacast") output not working correctly, including issues with 8K output.


**CHOP**
* [Copy CHOP](<../Copy_CHOP.md> "Copy CHOP") \- Fixed overcooking and crashing issues when copy/stamping parameters.
  * [DMX Out CHOP](<../DMX_Out_CHOP.md> "DMX Out CHOP") \- Added 'ArtSync Timeout' parameter to specify the time in milliseconds that ArtSync will wait for all ArtDmx packets to complete sending before sending the ArtSync packet. If they have not all been sent when the timeout is reached, then ArtSync will terminate and the ArtSync packet will not be sent. Additionally, a new frame of ArtDmx packets will be sent and a new ArtSync will be initiated.
  * [Hokuyo CHOP](<../Hokuyo_CHOP.md> "Hokuyo CHOP") \- Added new 'Local Address' parameter, helpful for when a system has multiple network interface cards.


**DAT**
* [Folder DAT](<../Folder_DAT.md> "Folder DAT") \- Fixed issue which caused files in subdirectories to be missed in some circumstances.
  * [Media File Info DAT](<../Media_File_Info_DAT.md> "Media File Info DAT") \- Added 'Pixel Aspect Ratio' to the list of information.
  * [WebSocket DAT](<../WebSocket_DAT.md> "WebSocket DAT") \- Fixed a crash when a message is received but there is no 'Callbacks DAT' referenced.


**MAT**
* [GLSL MAT](<../GLSL_MAT.md> "GLSL MAT") \- Added new`TDImageStore_*()`/`TDImageLoad_*()`functions to work with Image Outputs from the [Render TOP](<../Render_TOP.md> "Render TOP"). Required for color correct values when using a working [Color Space](<../Color_Space.md> "Color Space").
  * [Line MAT](<../Line_MAT.md> "Line MAT") \- New auto-cleanup of memory used by the Line MAT when it's not used for a while.


**SOP**
* [Copy SOP](<../Copy_SOP.md> "Copy SOP") / [LSystem SOP](<../LSystem_SOP.md> "LSystem SOP") \- Fixed overcooking and crashing issues when copy/stamping parameters.
  * [Skin SOP](<../Skin_SOP.md> "Skin SOP") \- Fixed a crash when input is invalid.


**Misc**
* [Timecode](<../Timecode.md> "Timecode") \- On macOS, fixed setting timecode from string when there are leading zeroes (eg. '08:08:08:08').
  * [Custom Operators](<../Custom_Operators.md> "Custom Operators") \- Fixed issue with Custom Operators loading. POP plugins now are loaded as Custom Operators too.
  * Fixed an issue where a python expression error in the 'Clone Master' parameter would prevent saving a component.
  * Fixed a bug that caused the 'Active Viewer' button to disappear on POPs and SOPs at certain zoom levels.

### Backward Compatibility Changes
* **BACKWARD COMPATIBILITY WARNING** \- [TDFunctions](<../TDFunctions.md> "TDFunctions") \- Improved error messaging and behavior of`createProperty`. However, using delattr to delete a property created by`createProperty`will now only set the value to None.

## Build 2025.30770 Aug 09, 2025

### New Features
* [Color Space Workflows](<../Color_Space_Workflows.md> "Color Space Workflows") \- A new 'Color' tab in the Preferences Dialog exposes [Color Space](<../Color_Space.md> "Color Space") controls and workflows. _These settings are saved per-project_ , so a change in any settings on this page requires saving the project.toe file and restarting the project. See articles [Color Space](<../Color_Space.md> "Color Space") and [Color Space Workflows](<../Color_Space_Workflows.md> "Color Space Workflows") for details and usage. 
    * Set the project's working color space between sRGB, ACEScg, Rec 2020 Linear, or DCI-P3 Linear
    * Set the Window Pixel format to SDR 8-bit, SDR 10-bit, HDR 10-bit, or HDR 16-bit Float.
    * Separate controls for Reference White Nits for both SDR and HDR.
    * **Note:** Known issues remain where some color adjustments of the user interface are requirement in some working modes. This will be fixed in an upcoming version.
  * Three new POPs have been added [Line Resample POP](<../Line_Resample_POP.md> "Line Resample POP"), [Plane POP](<../Plane_POP.md> "Plane POP"), and [ZED POP](<../ZED_POP.md> "ZED POP"). See the POPs section below.
  * New console for Windows and macOS which captures low level messages more reliably, including error messages and output from subprocesses. The [Environment Variable](<../Variables.md> "Variables") TOUCH_TEXT_CONSOLE no longer needed except to display messages before the TouchDesigner editor launches.
  * [Audio Render CHOP](<../Audio_Render_CHOP.md> "Audio Render CHOP") \- Added 'Auto' mode for baking reflections which will automatically rebake when any parameter change occurs that necessitates it.

### New Python
* Added pygdft and pymvr Python packages to TouchDesigner.
* [OP Class](<../OP_Class.md> "OP Class").`enclosedBy`\- List of all [Annotate COMPs](<../Annotate_COMP.md> "Annotate COMP") enclosing this operator.
  * [POP Class](<../POP_Class.md> "POP Class").save() - Method added for saving POP geometry, similar to SOP.save().
  * [SequenceCollection Class](<../SequenceCollection_Class.md> "SequenceCollection Class") \- Is now iterable. For example`[s for s in op('geo1').seq]`to iterate through all sequences of a particular OP.
  * [TDFunctions](<../TDFunctions.md> "TDFunctions") \- Fixed an issue with`applyParInfo`when source has a bind expression. Added`raiseExceptions`argument to that and`applyParDefaults`.
  * [Tdu Module](<../Tdu_Module.md> "Tdu Module").`parSummary(opType)`\- Outputs a detailed summary of the built-in parameters.
  * [Timecode Class](<../Timecode_Class.md> "Timecode Class")`.setLength`\- Fixed setting by tdu.Timecode so it accounts for potential differences in FPS.

### New Palette
* [Palette:callbacksHelper](<../Palette-callbacksHelper.md> "Palette:callbacksHelper") \- A new component in the Tools folder, simply drop this into your custom component to easily create a callback system for it.
  * [Palette:cameraViewport](<../Palette-cameraViewport.md> "Palette:cameraViewport") \- Version 1.2.2 - New parameter to externalize the transform into a DAT so it can be immune from cloning. 
    * New preset sequences and a button to stop auto rotation.
    * Added 'Go' pulse button to jump to preset position. Removed unneeded reference to numpy.
  * Added fix for transform DAT being overwritten by storage on load.
  * Updated built-in lights and helpers to use POPs.
  * Fixed a bug with updating the external camera transform.
* [TDAbleton](<../TDAbleton.md> "TDAbleton") \- Version 2.6.0 
    * Better arrangement clip information in abletonTrack Component output CHOP.
    * Added 'Arm for Recording' toggle to abletonTrack
    * Added looping info to clips
    * Fixed lingering errors when using "Update All Components"
    * Fixed long cooks in abletonTrack when a Live set has a long arrangement
    * Fixed demo to use "Auto Filter Legacy"
  * [Widgets](<../Widgets.md> "Widgets") \- v2.2.6 
    * New masterRadioMenu widget. Similar the Radio button but is a menu base type and operates with string values. Also includes ability to disable and hide items.

### Bug Fixes and Improvements
* [OpenVR](<../OpenVR.md> "OpenVR") \- Upgrade to OpenVR 2.5.1.


**COMP**
* [Engine COMP](<../Engine_COMP.md> "Engine COMP") \- Added new "Allow UI" parameter to control the ability of loaded components to open windows (Window COMPs).
  * [FBX COMP](<../FBX_COMP.md> "FBX COMP") \- Fixed [Info CHOP](<../Info_CHOP.md> "Info CHOP") not cooking when using an animation, unless 'Children Cook Time' was enabled.
  * [FBX COMP](<../FBX_COMP.md> "FBX COMP") \- Fixed a bug where animation would not play forward when 'Extend Left' set to "Hold".


**POP**
* [POP](<../POP.md> "POP") \- 'Save Geometry...' option added for all POP nodes, same file formats available as in [SOPs](<../SOP.md> "SOP").
  * Generator POPs now have more consistent parameters.
  * [Connectivity POP](<../Connectivity_POP.md> "Connectivity POP") \- Changes the way points in meshes (dimensions) are connected. There are now more connectivity types, closed dimensions, and a more simple interface.
  * [DMX Fixture POP](<../DMX_Fixture_POP.md> "DMX Fixture POP") \- When creating a new DMX Fixture POP, make the first sequence block expanded by default.
  * [DMX Fixture POP](<../DMX_Fixture_POP.md> "DMX Fixture POP") \- **BACKWARD COMPATIBILITY ISSUE** \- DMX Channel Names _must not include spaces_ now.
  * [DMX Out POP](<../DMX_Out_POP.md> "DMX Out POP") \- Added a 'Multipliers' page for creating multipliers [0-1] using channel name identifiers.
  * [DMX Out POP](<../DMX_Out_POP.md> "DMX Out POP") \- Fixed aggregation of the same universes from different [DMX Fixture POPs](<../DMX_Fixture_POP.md> "DMX Fixture POP") with different destination network addresses.
  * [DMX Out POP](<../DMX_Out_POP.md> "DMX Out POP") \- Fixed issue where no packets would be created if the referenced [DMX Fixture POP](<../DMX_Fixture_POP.md> "DMX Fixture POP") has 'Active' toggle re-enabled.
  * [Feedback POP](<../Feedback_POP.md> "Feedback POP") \- Fixed the initialization not working with 'Play' parameter disabled.
  * [Feedback POP](<../Feedback_POP.md> "Feedback POP") / [Particle POP](<../Particle_POP.md> "Particle POP") \- Can now step forward by single frames.
  * [Field POP](<../Field_POP.md> "Field POP") \- Can now combine weight with another attributes. When using a 'Specification POP', Field can output an array attribute with one value per field.
  * [Line Resample POP](<../Line_Resample_POP.md> "Line Resample POP") \- A new POP offering curvature-based resampling of lines.
  * [Line Smooth POP](<../Line_Smooth_POP.md> "Line Smooth POP") \- This POP was revamped.
  * [Noise POP](<../Noise_POP.md> "Noise POP") \- Output noise attributes can now be single components ie. Color.rb P(1)
  * [Particle POP](<../Particle_POP.md> "Particle POP") \- Fixed a bug that caused the attribute overlays to flicker.
  * [Plane POP](<../Plane_POP.md> "Plane POP") \- A new POP which is a 2D grid (similar to [Grid SOP](<../Grid_SOP.md> "Grid SOP")). Use the Plane POP when you just need a simple 2D plane and use the [Grid POP](<../Grid_POP.md> "Grid POP") when you need 3D grids and more advanced features.
  * [Random POP](<../Random_POP.md> "Random POP") \- Now more consistent with the Noise POP. The default output now has 3 components (ie. float3) as determined by the 'Noise Size' parameter, which now is 1, 2, 3 or 4. 'Parameter Size' added to adjust X Y and Z separately.
  * [Revolve POP](<../Revolve_POP.md> "Revolve POP") \- Now revolves using first-and-last points of line strips as an axis.
  * [Simple Render TOP](<../Simple_Render_TOP.md> "Simple Render TOP") \- Fixed crash that occurs when the target POP is deleted.
  * [ZED POP](<../ZED_POP.md> "ZED POP") \- Creates point clouds with a [ZED](<../ZED.md> "ZED") camera, does what the [ZED SOP](<../ZED_SOP.md> "ZED SOP") used to do but now in POPs.


**TOP**
* [Blur TOP](<../Blur_TOP.md> "Blur TOP") \- Fixed mipmaps not getting re-generated when it cooks.
  * [Direct Display Out TOP](<../Direct_Display_Out_TOP.md> "Direct Display Out TOP") \- Fixed this node not working in experimental builds.
  * [Level TOP](<../Level_TOP.md> "Level TOP") \- Fixed recent bug where 'Gamma' on 'Post' page would not work.
  * [Math TOP](<../Math_TOP.md> "Math TOP") \- 'Fix Invalid Values' menu added to handle bad pixel values. Allows for conversion of NaNs to Zero and Infs to One.
  * [Noise TOP](<../Noise_TOP.md> "Noise TOP") \- 'Derivative' parameter renamed to 'Gradient'.
  * [OpenVR TOP](<../OpenVR_TOP.md> "OpenVR TOP") \- Added color space support.
  * [Point File In TOP](<../Point_File_In_TOP.md> "Point File In TOP") \- Is now [Color Space](<../Color_Space.md> "Color Space") aware when used in a project with working color space set.
  * [Video Device In TOP](<../Video_Device_In_TOP.md> "Video Device In TOP") \- Fixed case where some input formats would not be converted correctly to RGBA.
  * [Video Device Out TOP](<../Video_Device_Out_TOP.md> "Video Device Out TOP") \- Fixed hang that occurs when turning on 'Sync Group' for [Blackmagic Design](<../Blackmagic_Design.md> "Blackmagic Design") devices and fixed older Blackmagic devices not working correctly.
  * [Video Device Out TOP](<../Video_Device_Out_TOP.md> "Video Device Out TOP") \- Fixed [Deltacast](<../Deltacast.md> "Deltacast") device output not working correctly.
  * [Video Stream In TOP](<../Video_Stream_In_TOP.md> "Video Stream In TOP") \- Fixed a bug that caused extra frame drops in some cases.
  * [Video Stream Out TOP](<../Video_Stream_Out_TOP.md> "Video Stream Out TOP") \- Reduce audio dropouts when connection is unstable.


**CHOP**
* [Audio Device In CHOP](<../Audio_Device_In_CHOP.md> "Audio Device In CHOP") \- Reduce pitch-shifts that this node can produce in the audio.
  * [Audio Render CHOP](<../Audio_Render_CHOP.md> "Audio Render CHOP") \- Improved baking warnings and an 'Auto' mode tht bakes after each parameter change that requires re-baking. Also fixed a possible crash with Audio Render CHOP.
  * [Audio Render CHOP](<../Audio_Render_CHOP.md> "Audio Render CHOP") \- Static 'Mesh SOPs' parameter now supports multiple SOPs.
  * [ST2110 Device CHOP](<../ST2110_Device_CHOP.md> "ST2110 Device CHOP") \- Fixed a problem where Blackmagic IP cards would not be found if other Blackmagic cards are installed in the system.
  * [Timecode CHOP](<../Timecode_CHOP.md> "Timecode CHOP") \- Added an option to set custom length from a [Timecode Class](<../Timecode_Class.md> "Timecode Class") object.
  * [Timecode CHOP](<../Timecode_CHOP.md> "Timecode CHOP") \- Added 'Extend Left' parameter and changed Cycle toggle to be a menu named 'Extend Right'.


**Misc**
* [Color Space](<../Color_Space.md> "Color Space") \- Added Rec.2020 and DCI-P3 as options for the working [color space](<../Color_Space.md> "Color Space").
  * [Custom Operators](<../Custom_Operators.md> "Custom Operators") \- Fixed new crash that will occur if a custom operator is loaded from ProjectDir/Plugins.
  * [Custom Operators](<../Custom_Operators.md> "Custom Operators") / [CPlusPlus TOP](<../CPlusPlus_TOP.md> "CPlusPlus TOP") / [CPlusPlus DAT](<../CPlusPlus_DAT.md> "CPlusPlus DAT") / [CPlusPlus SOP](<../CPlusPlus_SOP.md> "CPlusPlus SOP") / [CPlusPlus CHOP](<../CPlusPlus_CHOP.md> "CPlusPlus CHOP") \- New`opHelpURL`string member exposed, allowing the operator help page to point to a custom website
  * Oculus Rift folder and components in the [Palette](<../Palette.md> "Palette") renamed to use MetaQuest as base name.

### Backward Compatibility Changes

**BACKWARD COMPATIBILITY ISSUE**
* **BACKWARD COMPATIBILITY WARNING** \- [DMX Fixture POP](<../DMX_Fixture_POP.md> "DMX Fixture POP") \- DMX Channel Names _must not include spaces_ now.
  * **BACKWARD COMPATIBILITY WARNING** \- [POP](<../POP.md> "POP") \- A number of POP parameters were renamed and extended in size. This may affect loaded values or expressions in previous toe or tox files.  
For example some Random POP parameters (Amplitude, A, B, etc) were extended to have per-axis parameters (controlled by the size parameter), similar to the Noise POP. This required updating the RoyTimWorkshop file in the Examples folder. Please redownload the examples or be aware of these changes.

## Build 2025.30280 - Jun 30, 2025

### New Features
* [Nvidia Background TOP](<../Nvidia_Background_TOP.md> "Nvidia Background TOP") / [Nvidia Denoise TOP](<../Nvidia_Denoise_TOP.md> "Nvidia Denoise TOP") / [Nvidia Upscaler TOP](<../Nvidia_Upscaler_TOP.md> "Nvidia Upscaler TOP") \- Upgraded to latest version of Nvidia Maxine. Adds support for Blackwell GPUs ie. 50-series Geforce GPUs. Requires runtime dependencies to be installed from <https://www.nvidia.com/en-us/geforce/broadcasting/broadcast-sdk/resources/>.
* [ZED](<../ZED.md> "ZED") \- Updated the SDK to 5.0.2 and added access to a number of new features. 
    * [ZED TOP](<../ZED_TOP.md> "ZED TOP") \- Support for new image type called 'Mask', that provides a single mask from detection bodies with tracking ID as pixel value.
    * [ZED TOP](<../ZED_TOP.md> "ZED TOP") \- Added a new toggle parameter 'Disable Self Calibration' that disables automatic self-calibration process that occurs when opening the camera by default.
    * [ZED CHOP](<../ZED_CHOP.md> "ZED CHOP") \- Added support for 38 joint body tracking.
    * [ZED CHOP](<../ZED_CHOP.md> "ZED CHOP") \- Support for 2D, 3D and head 3D bounding boxes in ZED CHOP by turnon in the 'Bounding Boxes' toggle.

### New Python
* [geotextCOMP Class](<../GeotextCOMP_Class.md> "GeotextCOMP Class")`.layoutText()`\- This function now creates a dependency so that OPs using it will automatically recook when the Geo Text COMP changes.
  * [geotextCOMP Class](<../GeotextCOMP_Class.md> "GeotextCOMP Class")`.layoutText()`\- Returned positions now include vertical alignment and padding.
  * [WebclientDAT Class](<../WebclientDAT_Class.md> "WebclientDAT Class").request - Added formParts keyword argument that accepts a list of WebFormPart namedtuples. formParts enables construction of a MIME-formatted request, allowing for multipart and form requests.

### New Palette
* [Palette:tdPyEnvManager](<../Palette-tdPyEnvManager.md> "Palette:tdPyEnvManager") \- v1.0.8 - In Conda mode, when no environment name is specified a generic environment name is used and set in the Environment parameter.
  * [Palette:tdPyEnvManager](<../Palette-tdPyEnvManager.md> "Palette:tdPyEnvManager") \- v1.0.9 - Spinning animation does not show as often anymore. Some other tweaks around status and UI / icon.
  * [Palette:tdPyEnvManager](<../Palette-tdPyEnvManager.md> "Palette:tdPyEnvManager") \- v1.0.10 - Temporary fix to prevent the creation of empty shells that could open when creating conda environments or Python vEnvs.
  * [Widgets](<../Widgets.md> "Widgets") \- v2.2.5 
    * Button widget now uses Text COMP multiline mode offering better support for button names that require 2 lines.

### Bug Fixes and Improvements
* [NDI](<../NDI.md> "NDI") \- Upgraded to NDI SDK 6.2.0.
  * [ZED](<../ZED.md> "ZED") \- Upgraded to SDK 5.0.2.
  * Upgraded to latest version of Nvidia Maxine. Adds support for Blackwell GPUs ie. 50-series Geforce GPUs. Requires runtime dependencies to be installed from <https://www.nvidia.com/en-us/geforce/broadcasting/broadcast-sdk/resources/>.


  
**COMP**
* [Geo Text COMP](<../Geo_Text_COMP.md> "Geo Text COMP") \- Added warnings when Specification DAT append mode is used with incompatible features.


**POP**
* [CPlusPlus POP](<../CPlusPlus_POP.md> "CPlusPlus POP") \- Added the ability to create POP [Custom Operators](<../Custom_Operators.md> "Custom Operators") including using CUDA to process the data.
  * [DMX Fixture POP](<../DMX_Fixture_POP.md> "DMX Fixture POP") \- Fixed a crash when using an input that has a subset of total points (ie. Delete POP).
  * [DMX Fixture POP](<../DMX_Fixture_POP.md> "DMX Fixture POP") / [DMX Out POP](<../DMX_Out_POP.md> "DMX Out POP") \- Added`num_universes`[Info CHOP](<../Info_CHOP.md> "Info CHOP") channel.
  * [DMX Fixture POP](<../DMX_Fixture_POP.md> "DMX Fixture POP") / [DMX Map DAT](<../DMX_Map_DAT.md> "DMX Map DAT") \- **BACKWARD COMPATIBILITY ISSUE** \- Changed channel values to go from range 1-512 rather than 0-511 to match the DMX512 addressing standard.
  * [Noise POP](<../Noise_POP.md> "Noise POP") \- The default output of Noise now has 3 components (ie. float3), as determined by the 'Noise Size' parameter, which now is 1, 2, 3 or 4. This was previously set by the 'Parameter Size' and the 'Combine Operation' parameters.


**TOP**
* [Blackmagic Design](<../Blackmagic_Design.md> "Blackmagic Design") \- Added support for Timecode over HDMI.
  * [Blur TOP](<../Blur_TOP.md> "Blur TOP") \- Fixed an issue that broke output when the output resolution was different than the input. Also fixes Bloom COMP in the palette not working due to that.
  * [CHOP to TOP](<../CHOP_to_TOP.md> "CHOP to TOP") \- Fixed recent bug that caused pixel format to incorrectly be 8-bit in many cases.
  * [Convolve TOP](<../Convolve_TOP.md> "Convolve TOP") \- A Coefficients DAT has been docked for ease of use.
  * [CPlusPlus TOP](<../CPlusPlus_TOP.md> "CPlusPlus TOP") \- Added`TOP_Output::getSuggestedOutputDesc()`to help decide what resolution the node should output based on the 'Common' page parameters.
  * [Displace TOP](<../Displace_TOP.md> "Displace TOP") \- New 'Aspect Correct' parameter added for mapping the displace weights to be aspect correct.
  * [Movie File Out TOP](<../Movie_File_Out_TOP.md> "Movie File Out TOP") \- Fixed GPU memory leak when using the Nvidia H.264 and HEVC/H.265 encoders.¥
  * [NDI In TOP](<../NDI_In_TOP.md> "NDI In TOP") / [NDI Out TOP](<../NDI_Out_TOP.md> "NDI Out TOP") \- Upgraded to NDI 6.2.0.
  * [Nvidia Background TOP](<../Nvidia_Background_TOP.md> "Nvidia Background TOP") / [Nvidia Denoise TOP](<../Nvidia_Denoise_TOP.md> "Nvidia Denoise TOP") / [Nvidia Upscaler TOP](<../Nvidia_Upscaler_TOP.md> "Nvidia Upscaler TOP") \- Upgraded to latest version of Nvidia Maxine. Adds support for Blackwell GPUs ie. 50-series Geforce GPUs. Requires runtime dependencies to be installed from <https://www.nvidia.com/en-us/geforce/broadcasting/broadcast-sdk/resources/>.
  * [NVIDIA RTX Video TOP](<../NVIDIA_RTX_Video_TOP.md> "NVIDIA RTX Video TOP") \- A new TOP that leverages the Nvidia RTX Video SDK for AI-enhanced video processing. This custom TOP enables RTX Video Super Resolution and RTX Video HDR effects to improve sharpness, clarity, and automatically convert SDR video to HDR within TouchDesigner workflows.
  * [Render TOP](<../Render_TOP.md> "Render TOP") \- Fixed issue where 'Image Outputs' were not working.
  * [Simple Render TOP](<../Simple_Render_TOP.md> "Simple Render TOP") \- New basic operator to render geometry without needing extra COMPs (cameras / lights, etc.)
  * [Video Stream Out TOP](<../Video_Stream_Out_TOP.md> "Video Stream Out TOP") \- Fixed a new issue with stream constantly restarting in some cases.
  * [ZED TOP](<../ZED_TOP.md> "ZED TOP") \- Support for new image type called 'Mask', that provides a single mask from detection bodies with tracking ID as pixel value.
  * [ZED TOP](<../ZED_TOP.md> "ZED TOP") \- Added a new toggle parameter 'Disable Self Calibration' that disables automatic self-calibration process that occurs when opening the camera by default.


**CHOP**
* Added menu with toggling behavior to CHOP Viewer scope tools.
  * [Audio NDI CHOP](<../Audio_NDI_CHOP.md> "Audio NDI CHOP") \- Fixed this node not getting data if the referenced [NDI In TOP](<../NDI_In_TOP.md> "NDI In TOP") hasn't been used anywhere.
  * [Count CHOP](<../Count_CHOP.md> "Count CHOP") \- Momentary 'Count Up', 'Count Down' buttons still supported when inputs connected (OR'd to incoming value).
  * [Laser CHOP](<../Laser_CHOP.md> "Laser CHOP") \- Fixed a crash when using a POP input that has a subset of total points (ie. Delete POP).
  * [MIDI In CHOP](<../MIDI_In_CHOP.md> "MIDI In CHOP") \- While using the CHOP with 'Simplified Output' = Off (ie. using non-simplified output, 1-based Index parameter was fixed for Note type midi messages by adding 1 to the index of the note, controller, velocity, aftertouch. This doesn't affect the channel number.**Backward Compatibility** \- When loading older files, channel index for Note midi messages may be incremented by one if the 1 Based Index parameter was saved toggled to On in those older files.
  * [Pangolin CHOP](<../Pangolin_CHOP.md> "Pangolin CHOP") \- Fixed a crash when using an input that has a subset of total points (ie. Delete POP).
  * [TOP to CHOP](<../TOP_to_CHOP.md> "TOP to CHOP") \- Fixed 'Output as Single Channel Set' not working.
  * [ZED CHOP](<../ZED_CHOP.md> "ZED CHOP") \- Added support for 38 joint body tracking.
  * [ZED CHOP](<../ZED_CHOP.md> "ZED CHOP") \- Support for 2D, 3D and head 3D bounding boxes in ZED CHOP by turnon in the 'Bounding Boxes' toggle.


**DAT**
* Fixed multiple issues with the cursor position in DATs after pressing shift-TAB.
  * [DMX Map DAT](<../DMX_Map_DAT.md> "DMX Map DAT") \- Added`universe_num`column for the full/expanded universe value.
  * [DMX Map DAT](<../DMX_Map_DAT.md> "DMX Map DAT") \- Fixed incorrect`netaddress`column value when using sACN multicast.
  * [NDI DAT](<../NDI_DAT.md> "NDI DAT") \- Fixed a crash when used with cloning.
  * [Web Client DAT](<../Web_Client_DAT.md> "Web Client DAT") \- Added 'Web Form' toggle that enables construction of MIME-formatted request, similar to using mimeParts in [WebclientDAT Class](<../WebclientDAT_Class.md> "WebclientDAT Class").request. When enabled, the second input will be interpreted as MIME parts rather than the request body.


**MAT**
* [GLSL MAT](<../GLSL_MAT.md> "GLSL MAT") \- Fixed issue where 'Image Outputs' were not working.


**Misc**
* [Custom Operators](<../Custom_Operators.md> "Custom Operators") \- Now support requesting TOP data on the CPU in different color spaces, when there is a working color space defined.
  * Horizontal camera tumble direction is now correctly flipped when the camera is upside down. This applies to built-in viewers, tdu.Camera class and the cameraViewport component.

### Backward Compatibility Changes

**BACKWARD COMPATIBILITY ISSUE**
* **BACKWARD COMPATIBILITY WARNING** \- [DMX Fixture POP](<../DMX_Fixture_POP.md> "DMX Fixture POP") / [DMX Map DAT](<../DMX_Map_DAT.md> "DMX Map DAT") \- Changed channel values to go from range 1-512 rather than 0-511 to match the DMX512 addressing standard.
  * **BACKWARD COMPATIBILITY WARNING** \- [MIDI In CHOP](<../MIDI_In_CHOP.md> "MIDI In CHOP") \- While using the CHOP with 'Simplified Output' = Off (ie. using non-simplified output, 1-based Index parameter was fixed for Note type midi messages by adding 1 to the index of the note, controller, velocity, aftertouch. This doesn't affect the channel number. When loading older files, channel index for Note midi messages may be incremented by one if the 1 Based Index parameter was saved toggled to On in those older files.

## Build 2025.30060 - Jun 06, 2024

### Key Highlights

#### Point Operators \- POPs

Introducing [POPs](<../POP.md> "POP"), aka Point Operators! POPs are a new family of operators that run on the GPU and create or modify 3D data. Points are the building blocks of polygons, lines, line strips, spline curves, point clouds, particle systems, any 3D geometrical shape and any form of data points. 

Every POP contains a set of points with a set of Point Attributes. The most common attribute is Position (`P`), the position in 3D space of the points. The POP may have other attributes like Color (`Color`\- always with a red, green, blue and alpha component) and Normal (`N`\- a direction vector with 3 components). The points can also have extra user-defined attributes or can get attributes automatically-generated from certain POP operators. 

To learn about POPs, please visit our **[Learning About POPs](<https://www.notion.so/3f7645a368a043f99cd143e2382b8ab0?pvs=25>)** article here for an in-depth look at what's behind this exciting new OP family. Download the [POPs Examples Package](<https://www.dropbox.com/scl/fo/0e1hsc1isbhg7o2hd7vnm/ALXKQfGHE0paETnPpWvo7VQ?rlkey=4ih7bxgmcnrdau3ue7xxnee10&st=r9oi2joy&dl=0>) to learn and try out a bunch of examples. 

#### New DMX Workflows with POPs

Data can also flow from POPs directly to other operator families, like Channel Operators (CHOPs) and then on to lasers, DMX or other external systems. While DMX was previously handled in TouchDesigner exclusively by the DMX In and Out CHOPs, we have introduced a set of new DMX POP operators enabling powerful new workflows for lighting, LEDs and anything operating on DMX. 

First we introduce the [DMX Fixture POP](<../DMX_Fixture_POP.md> "DMX Fixture POP") which lets you setup all the channels in your fixture's profile. Each point and primitive in the DMX Fixture POP's input will represent a copy of this fixture, inherently giving you a position in 3D space for every fixture in your setup. From here, the DMX Fixture POP will construct all the channels and universes required to address all your fixtures. Second, the new [DMX Out POP](<../DMX_Out_POP.md> "DMX Out POP") takes one or more DMX Fixture POPs, merges all the universes and sends the data out to your DMX, Art-Net, sACN, KiNET, or FTDI devices. A third new operator, the [DMX Map DAT](<../DMX_Map_DAT.md> "DMX Map DAT"), is useful for visualizing DMX universe and channel layouts and can be helpful for troubleshooting channel conflicts between DMX fixtures. You'll find a DMX Map DAT docked to every DMX Out POP ready to help debug any such conflicts. 

Last but not least, a new [Pan Tilt CHOP](<../Pan_Tilt_CHOP.md> "Pan Tilt CHOP") has been introduced to make it easier to control lighting fixture's pan and tilt controls, something that previously wasn't trivial using raw rotational values in CHOPs. 

#### Hardware Device Operators

##### Laser Upgrades
* [Laser CHOP](<../Laser_CHOP.md> "Laser CHOP") \- For this release the laser point generation process was overhauled, with improvements to blanking calculations, image sharpness/uniformity, point repeating, general stability, and taking input directly from POPs. The CHOP was developed with the help of [LaserAnimation Sollinger](<https://laseranimation.com/en/>) who guided us in speccing and implementing the necessary parameters, especially in regards of the blanking timing settings. 
    * The new Laser CHOP introduces the notion of Corner Points. Previously, everything could've been considered a "Corner Point", but now with the use of input attributes/channels (`LasCorner`and`lascorner`), corner points can be selected. In contrast, all non-Corner Points are considered Guide Points. Corner Points are repeatable to enable sharper and more defined lines. Guide Points are never repeated and only serve to guide the laser along a desired path, while at the same time not consuming extra points from the laser device's point buffer because they do not follow the same repeating rules as Corner Points.
    * Additionally, there are extra input attributes/channels that allow for extra per-Corner Point control on point repeating: "`LasCornerHoldAdd`" (SOP/POP) or "`lascornerholdadd`" (CHOP) and "`LasCornerHoldLookupFactor`" (SOP/POP) or "`lascornerholdlookupfactor`" (CHOP)
    * New 'Closed Shape Overlap' parameter which adds overlapping points at the start/end of a shape to create a more uniform shape by removing hot-spots (like those introduced by start point hold time for example) via color interpolation.
    * New 'Interpolate Colors' parameter enables color interpolation between points.

##### ST2110
* [ST2110 In TOP](<../ST2110_In_TOP.md> "ST2110 In TOP") / [ST2110 Out TOP](<../ST2110_Out_TOP.md> "ST2110 Out TOP") \- New TOPs for ST2110 devices such as the Blackmagic IP range and Deltacast DELTA-ip-ST2110.
  * [ST2110 Device CHOP](<../ST2110_Device_CHOP.md> "ST2110 Device CHOP") \- A new CHOP used to configure the ST2110 NIC (DHCP/IP Settings). The ST2110 TOPs reference this node to determine the available channels to send data out of the configured NIC.

##### Other Devices
* [Serial Devices DAT](<../Serial_Devices_DAT.md> "Serial Devices DAT") \- New DAT that lists the available serial ports and identifies if a port is in use or not.
* [ZED](<../ZED.md> "ZED") \- Overhaul - CHOP and SOP now point to ZED TOP, etc.

#### 3D Texture Support
* Most TOPs now natively support 3D Textures. Feeding a 3D TOPs a source with 3D Texture format will now perform the operation on the 3D Texture. 
    * List of TOPs - Add, Blur, Channel Mix, Chroma Key, Composite, Constant, Corner Pin, Cross, Difference, Displace, Emboss, Flip, Function, HSV Adjust, HSV to RGB, Inside, Lens Distort, Level, Limit, Luma Blur, Level Level, Math, Matte, Mirror, Mono, Multiply, Noise, Outside, Over, Remap, Screen, Subtract, Screen, Slope, Reorder, Threshold
  * [TOP to CHOP](<../TOP_to_CHOP.md> "TOP to CHOP") and [TOP to POP](<../TOP_to_POP.md> "TOP to POP") \- works with 3D Textures or 2D Arrays.

#### Metadata support
* [Movie File Out TOP](<../Movie_File_Out_TOP.md> "Movie File Out TOP") \- Added support for Exif metadata writing for .png, .jpeg and .tiff file formats.
  * [Audio File Out CHOP](<../Audio_File_Out_CHOP.md> "Audio File Out CHOP") \- Added support for writing metadata to .wav, .mp3, .ogg, .aiff audio file formats.
  * [Media File Info DAT](<../Media_File_Info_DAT.md> "Media File Info DAT") \- Added support to read Exif metadata.
  * Added new member`.metadata`to [Media File Info DAT](<../Media_File_Info_DAT.md> "Media File Info DAT"), [Movie File In TOP](<../Movie_File_In_TOP.md> "Movie File In TOP") and [Audio File In CHOP](<../Audio_File_In_CHOP.md> "Audio File In CHOP").

#### Pattern Matching

Some parameters in TouchDesigner are used to specify multiple operators, multiple channels, multiple points, etc. For example, the Render TOP allows for multiple lights, geometry COMPs and cameras. The Join CHOP and Composite TOP accept multiple CHOPs and TOPs respectively. A parameter that is a "pattern" allows you to specify several names and/or specify "wild cards" which will match all or parts of the names of operators, channels, point indexes etc. Some examples, 1)`r[xyz]`matches channels rx, ry and rz, 2)`*foot*`matches each channel that has "foot" in it, with anything or nothing before or after it. 

We are introducing an new update to [Pattern Matching](<../Pattern_Matching.md> "Pattern Matching") that is consistent throughout the product. Refer to the [Pattern Matching](<../Pattern_Matching.md> "Pattern Matching") documentation for details on the usage. Note: There is a 'Legacy Features' section below. Some uses of it are obsolete but we have legacy modes that allow older patterns and files to continue to work as-is. 

The new Pattern Matching includes many improvements outlined here: 
* **String patterns**
    * Now all string patterns use the same pattern matching so you get consistent results. Previously, some nodes would be able to match`geo[2-3,5]`while others couldn't (ie. [Render TOP](<../Render_TOP.md> "Render TOP")), now they all can.
    * Any string pattern can now use Set Notation for matching (if shown as supported [this table](<../Pattern_Matching_Support.md> "Pattern Matching Support")). 
      * Now _space separated patterns_ are consistently treated as OR, whereas previously these was different for different parameters.
      * **Recommended:** Use "`&`" and "`|`" symbols for more explicit syntax, for example:`^fit5 & ^fit5`and`^fit5 | ^fit6`are more explicit and preferred versus`^fit5 ^fit6`* **Index patterns** \- Functionally index pattern matching works similar to the previous notation except ranges are now surrounded by a brackets, _not_ should use ^, improvements to take notation, and now supports set matching for non ordered. 
    * Index patterns used to be differentiated by not having any square brackets, i.e.`0-10:2,3`. Now they also use brackets which is more consistent with string patterns, ie.`[0-10:2]`would be valid for both a new index and string pattern.
    * Using ^ instead of ! for _not_ so`^5`versus`!5`(in SOPs you were even able to use ! and ^ together, i.e.`^!50-70`, not possible in new matching).
    * 'Take' notation has changed. We used to say`0-15:2,3`for "Take the first 2 of every 3 points, i.e. 0,1,3,4,6,7...), now we use`[0-15:2:4]`* Take notation now supports`[*:2]`notation, take every second entry from "*" which ranges from 0-maximum number of points (similarly for ordered ranges from 0-10 in that order).
    * POPs indices exclusively use the new syntax. Set matching is supported for non ordered ranges (such as those in [Primitive POP](<../Primitive_POP.md> "Primitive POP")).
* **Set Matching** \- The pattern matching rules above can be used in conjunction with [set operator notation](<../Pattern_Matching.htm#Set_Operator_Notation> "Pattern Matching") for more expressive selection. Basic, Operator and Index Patterns (i.e.`/project/geo1`,`t?`,`chan*`,`blend[2-6:2]`) create sets and |, &, ~ can apply set operations between them.
* **Additional Notes**
    * Any string pattern should have been updated (except those that were old/deprecated).
    * POPs all use the new index pattern matching described above.
    * The [Delete CHOP](<../Delete_CHOP.md> "Delete CHOP"), [Reorder CHOP](<../Reorder_CHOP.md> "Reorder CHOP") and [Sort CHOP](<../Sort_CHOP.md> "Sort CHOP") have a 'Legacy Pattern Matching' toggle for using older style index pattern matching for backward compatibility.
    * SOPs Index pattern matching have been left unchanged.

#### Color Space Workflow

_**Coming soon in the next release!**_ The color space settings are not exposed yet but will become available in our next build in a couple of weeks time. For now you can disregard the new color space parameters you'll find, mostly in TOPs and other operators that have a color parameter. 

#### Operator New Features
* All Out operators now have an optional 'Select' parameter as an alternative to wired input.

##### COMP Features
* [Button COMP](<../Button_COMP.md> "Button COMP") \- New parameters to adjust the text on the button's label, including 'Scale Text to Fit', 'Font Size', 'Line Spacing', and 'Text Padding'.
  * [Geo Text COMP](<../Geo_Text_COMP.md> "Geo Text COMP") \- Added 'Face Camera' parm to make text face the camera regardless of orientation. 
    * Added depth-based scaling parameters (similar to the [Line MAT](<../Line_MAT.md> "Line MAT")) to control text scaling based on distance from the camera.
    * Added 'Width Affected by FOV/OrthoWidth' parameter (similar to the Line MAT) to make sizing field-of-view independent.
    * All of the above new features work independently for each camera. For example, with the 'Face Camera' parameter toggled on, the text will face each camera it is viewer from.
  * [List COMP](<../List_COMP.md> "List COMP") \- New attribute`topFill`controls the way a background TOP will fill:`fillMode.STRETCH`,`HORIZONTAL`,`VERTICAL`,`BEST`,`NATIVE`,`OUTSIDE`For example 
[code] 
    def onInitRow(comp, row, attribs):
    	attribs.top = op('out1')
    	if (row%2 == 0):
    		attribs.topFill = FillMode.VERTICAL
    	else:
    		attribs.topFill = FillMode.HORIZONTAL
    	return
    
[/code]
* [Panel COMPs](<../Panel_Component.md> "Panel Component") \- All Panel Components received these updates. 
    * On the Look parameter page, a new 'TOP Fill' option 'Fill Outside' fills the available area by cropping rather than stretching the image.
    * On the Drag/Drop parameter page you'll find: 
      * In the 'When Dragging This' parameter menu there is now an option to 'Fill Custom Parameter' to easily fill a single parameter without need of setting up a callback.
      * 'Built-In Drop Options' toggle controls whether or not built-in options are included when dropping onto this node.
  * [Text COMP](<../Text_COMP.md> "Text COMP") \- Added 'Placeholder Text' that is displayed when the text contents are empty.
  * [Window COMP](<../Window_COMP.md> "Window COMP") \- A new 'Prevent Display Sleep' toggle parameter has been added to keep your display from going to sleep regardless of power saving modes set on the system.

##### TOP Features
* [Movie File In TOP](<../Movie_File_In_TOP.md> "Movie File In TOP") \- New features. 
    * Allow 'Index' parameter to be a negative number. When negative the index will cycle back through the movie.
    * Added 'Pre-Download HTTP Addresses' parameter. This was the default behavior before, but now can be turned off.
    * Added support for reading some forms of`.ktx`files.
  * [Movie File Out TOP](<../Movie_File_Out_TOP.md> "Movie File Out TOP") \- New features. 
    * Added support for VVC (Versatile Video Coding), also known as H.266.
    * Added 'Stereo Mode' and 'Spherical Mode' parameters to write out metadata for stereo and spherical video content.
    * Added 'Leading Zeros Digits' parameter to specify the minimum number of suffix digits that the filename will have. If the sequence number is less than this number, then leading zeros are appended so that the total number of suffix digits is at least this value.
  * [Script TOP](<../Script_TOP.md> "Script TOP") \- Added parameter 'Modify Outside of Cook' which when 'On' allows the TOP's output to be updated by an external script.
  * [Video Device In TOP](<../Video_Device_In_TOP.md> "Video Device In TOP") \- Extended device support and improvements. 
    * Added support for the IDS Peak SDK, to support newer [IDS cameras](<https://en.ids-imaging.com/>).
    * [AJA](<../AJA.md> "AJA") devices can now use the 'Sync to Input Frame' with multiple inputs.
    * Now possible to capture up to 16 audio channels for [Deltacast](<../Deltacast.md> "Deltacast") devices.
    * Added support for 10-bit output on [Bluefish444](<../Bluefish444.md> "Bluefish444") devices, you'll also find this support in the [Video Device Out TOP](<../Video_Device_Out_TOP.md> "Video Device Out TOP").
    * Added 'frames_displayed' [Info CHOP](<../Info_CHOP.md> "Info CHOP") channel.
    * Improved performance when using 'Media Foundation' library and the pixel format of the data stream is NV12.
  * [Video Device Out TOP](<../Video_Device_Out_TOP.md> "Video Device Out TOP") \- Improved device support. 
    * Added support for synchronized output for [Blackmagic Design](<../Blackmagic_Design.md> "Blackmagic Design") devices.
    * Added support for 10-bit output on [Bluefish444](<../Bluefish444.md> "Bluefish444") devices.
    * Device selection is now more portable between machines, using a device index if the exact device can't be found.
  * [Video Stream Out TOP](<../Video_Stream_Out_TOP.md> "Video Stream Out TOP") \- AAC audio, some tuning parameters and improvements. 
    * Added support for AAC audio for RTMP and SRT modes, as such, the default audio codec has been changed to AAC.
    * Added parameters to force the Mux Size and the VBV Buffer Size.

##### CHOP Features
* [Audio Render CHOP](<../Audio_Render_CHOP.md> "Audio Render CHOP") \- Added added a new 'Simulation' mode that supports multiple sources, scene meshes, and reflection.
  * [Clock CHOP](<../Clock_CHOP.md> "Clock CHOP") \- Added 'Countdown' mode. For the first input, any missing values are assumed to be midnight January 1st of specified year. The second input is entirely optional, missing values are taken from current time.
  * [DMX Out CHOP](<../DMX_Out_CHOP.md> "DMX Out CHOP") \- Better support for serial and DMXKing devices.
  * [Script CHOP](<../Script_CHOP.md> "Script CHOP") \- Added parameter 'Modify Outside of Cook' which when 'On' allows the CHOP's output to be updated by an external script.
  * [Trigger CHOP](<../Trigger_CHOP.md> "Trigger CHOP") \- Added 'Enable Remap Length' and 'Remap Length' parameters which will re-time the total length of the envelope to the specified length. Note that 'held sustain' length is not remapped, only Delay, Attack, Peak, and Release lengths are remapped.

##### DAT Features
* [Multi Touch In DAT](<../Multi_Touch_In_DAT.md> "Multi Touch In DAT") \- New features 
    * New parameter 'Occlude Panels by Hierarchy' - Enable filtering out multitouch events by Panel Depth Layer.
    * New parameter 'Occlude Panels by Depth Layer' - Only children of the specified panel will receive multitouch events. Touches on parent and sibling panels are ignored.
    * New parameter 'Occlude Panels Above Depth' - Multitouch events from panels with a Depth Layer larger than this value will be ignored.
  * [Table DAT](<../Table_DAT.md> "Table DAT") \- Performance optimizations to make large tables cook significantly faster.
  * [Table DAT](<../Table_DAT.md> "Table DAT") \- In the DAT viewer's right-click menu, there is now an option to toggle the 'Auto Resize Columns' behavior on/off.

##### MAT Features
* **TriPlanar texturing** ... 
    * [PBR MAT](<../PBR_MAT.md> "PBR MAT") / [Phong MAT](<../Phong_MAT.md> "Phong MAT") \- Added new menu 'Texture Sampling Mode' to PBR MAT and Phong MAT with options Regular, Screen Space Coordinates and Triplanar.
    * For backward compatibility, the 'Screen Space Coordinates' option previous found under the 'Texture Coord' menu is now located in the new 'Texture Sampling Mode' menu.
    * Triplanar texture mapping can be selected using the 'Triplanar Mapping' option in the new mode menu. When using this mode, first triplanar texture attributes need to be generated via the [Texture Map POP](<../Texture_Map_POP.md> "Texture Map POP").
    * [Texture Map POP](<../Texture_Map_POP.md> "Texture Map POP") \- The option 'Triplanar Coordinates (Point)' found in the 'Texture Type' menu will generate triplanar texture attributes on the geometry for use with triplanar mapping in the MATs above.

#### Operating System Specific
* [macOS](<../MacOS.md> "MacOS") \- Minimum requirements now macOS 12.0 Monterey.
  * [macOS](<../MacOS.md> "MacOS") \- Added support for hardware accelerated H.264 and HEVC/H.265 encoding with the [Movie File Out TOP](<../Movie_File_Out_TOP.md> "Movie File Out TOP").
  * Windows and macOS - A minimum of 4GB GPU memory is required, we recommend 8GB or more.

#### Python Tools
* TouchDesigner's Python version has been updated to **3.11.10**

#####  Python Autocomplete and Help in VScode
* [TDI Library](<../TDI_Library.md> "TDI Library") \- The TDI Library enables popup help and code-completion when working with python in Microsoft Visual Studio Code (VS Code). It contains the help documentation and Python description of all built-in TouchDesigner objects, classes and functions. In addition to help and auto-completion, using TDI library will eliminate error and warning indicators when using VS Code to edit TouchDesigner Python.

##### Tool Components for working with Python in TouchDesigner
* [Thread Manager](<../Thread_Manager.md> "Thread Manager") \- A new system component and a set of palette components designed to facilitate Python threading in TouchDesigner. 
    * Read our [Introduction to the Thread Manager](<https://derivative.ca/community-post/enhancing-your-python-toolbox-touchdesigner%E2%80%99s-thread-manager/72022>) for a walkthrough.
* [Palette:tdPyEnvManager](<../Palette-tdPyEnvManager.md> "Palette:tdPyEnvManager") \- A component to sideload and manage python virtual environments, conda environments, and third-party packages and libraries. 
    * Read our [Introduction to the Python Environment Manager](<https://derivative.ca/community-post/introducing-touchdesigner-python-environment-manager-tdpyenvmanager/72024>) here.
* Depth Anything V2 Tutorial - Depth Anything V2 is a machine learning library that can create depth information for images and videos. Check out [this tutorial](<https://derivative.ca/community-post/custom-integration-thread-manager-support-third-party-python-library/72023>) which uses both the _ThreadManager_ and the _TDPyEnvManager_ to get Depth Anything V2 running in TouchDesigner.
* [Palette:logger](<../Palette-logger.md> "Palette:logger") \- v2.6.1 - Major overall. Improved by always initializing a Logger object reducing initialization issues and now including a QueueHandler to work in conjunction with the [Thread Manager](<../Thread_Manager.md> "Thread Manager") mentioned above.

### New Python
* Python version updated to 3.11.10 
    * Updated all extra Python packages we ship with to the latest versions.
    * Upgraded to NumPy 2.1.2.
* Added [box python package](<https://pypi.org/project/python-box/>).
  * Added [tzdata python package](<https://pypi.org/project/tzdata/>) so the 'zoneinfo' package works correctly out of the box.
* Individual parameter disabling within a [ParGroup](<../ParGroup.md> "ParGroup")
  * [AbsTime Class](<../AbsTime_Class.md> "AbsTime Class") \-`.frame``.seconds`now pause with main timeline.
  * [Camera Class](<../Camera_Class.md> "Camera Class")`.frameBounds`\- Added a new 'padding' keyword expressed as a fraction of the viewport height e.g. 0.1 puts a minimum 10% padding around all sides.
  * [Camera Class](<../Camera_Class.md> "Camera Class") / [ArcBall Class](<../ArcBall_Class.md> "ArcBall Class") \- Added errors for unexpected arguments and keywords.
  * [COMP Class](<../COMP_Class.md> "COMP Class")`.layout(ops, horizontal=False, vertical=False, gridRows=0)`\- Added a method to automatically layout operators.
  * [COMP Class](<../COMP_Class.md> "COMP Class")`.findChildren(renamed=True)`\- Returns a list of children whose names have been edited, ie. any non-default name.
  * [COMP Class](<../COMP_Class.md> "COMP Class")`.collapseSelected()`returns a reference to the created Base COMP.
  * [COMP Class](<../COMP_Class.md> "COMP Class")`.progressiveUnload()`\- A new method to progressively unload the COMP's children over multiple frames. All 'PerFrame' options can be specified together. Unloading will move to next frame when one of the criteria gets met. 
    * Additionally a [COMP Class](<../COMP_Class.md> "COMP Class")`.progressiveUnloader`member has been added to query the progress of the progressiveUnload operation. See [ProgressiveUnload Class](</index.php?title=ProgressiveUnload_Class&action=edit&redlink=1> "ProgressiveUnload Class \(page does not exist\)") below.
    * [ProgressiveUnload Class](</index.php?title=ProgressiveUnload_Class&action=edit&redlink=1> "ProgressiveUnload Class \(page does not exist\)") \- This new class describes a specific instance of the`COMP.progressiveUnload()`method. Methods and members of this class are used to obtain progress information about the underway progressive unload operation, or modify it.
* [geometryCOMP Class](<../GeometryCOMP_Class.md> "GeometryCOMP Class")`.bounds`/ [SOP_Class](<../SOP_Class.md> "SOP Class")`.bounds`\- New functions for returning the bounds of the contained geometry. The 'render' and 'display' now default to False in contrast to the legacy`computeBounds`function. For example, calling`OP.bounds()`with no keywords will now always return bounds regardless of the state of the render. The legacy computeBounds function has been deprecated.
  * [geometryCOMP Class](<../GeometryCOMP_Class.md> "GeometryCOMP Class")`.computeBounds`\- COMPs that are not 3D Objects (ie. Base COMP, Panel COMPs, etc) are no longer included in bounds when the recurse keyword is used.
* [Custom Operators](<../Custom_Operators.md> "Custom Operators") / [CPlusPlus TOP](<../CPlusPlus_TOP.md> "CPlusPlus TOP") / [CPlusPlus DAT](<../CPlusPlus_DAT.md> "CPlusPlus DAT") / [CPlusPlus SOP](<../CPlusPlus_SOP.md> "CPlusPlus SOP") / [CPlusPlus CHOP](<../CPlusPlus_CHOP.md> "CPlusPlus CHOP").`opHelpURL`\- New string member exposed allowing the operator's help page to point to a custom website URL.
* [DAT Class](<../DAT_Class.md> "DAT Class")`.csv`\- Get or set the contents as csv format. Unlike`.text`format,`.csv`supports newlines in cells.
  * [DAT Class](<../DAT_Class.md> "DAT Class") \- Removed`textFormat`member from DAT class and moved to [textDAT Class](<../TextDAT_Class.md> "TextDAT Class") and [scriptDAT Class](<../ScriptDAT_Class.md> "ScriptDAT Class").
* [datexecuteDAT Class](<../DatexecuteDAT_Class.md> "DatexecuteDAT Class").`sizeChanged`\- Added to info argument.
  * [datexecuteDAT Class](<../DatexecuteDAT_Class.md> "DatexecuteDAT Class").`onRow(Col)HeadersChange`\- NMow provides _prevDAT_.
  * [datexecuteDAT Class](<../DatexecuteDAT_Class.md> "DatexecuteDAT Class").`onTableChanged(dat, prevDAT, info)`\- Now includes DAT in its previous state as well as a description of which rows/columns were removed/added.
  * [datexecuteDAT Class](<../DatexecuteDAT_Class.md> "DatexecuteDAT Class").`onTableChanged()`info argument now contains:


[code]
      rowsChanged - a list of row indices with different contents
      rowsAdded   - the list of added *header* indices (in dat)
      rowsRemoved - the list of removed *header* indices (in prevDAT)
      colsChanged - a list of col indices with different contents
      colsAdded   - the list of added *header* indices (in dat)
      colsRemoved - the list of removed *header* indices (in prevDAT)
      cellsChanged - the list of cells that have changed content
      sizeChanged - bool, true if number of rows or columns changed
    
[/code]
* [Dependency Class](<../Dependency_Class.md> "Dependency Class") \- Using deepcopy on a`tdu.Dependency()`will now also copy over its`.callbacks`member.
* [listCOMP Class](<../ListCOMP_Class.md> "ListCOMP Class") \- Rolling outside cells now shows popup help defined in table attribute.
  * [listCOMP Class](<../ListCOMP_Class.md> "ListCOMP Class") \- New members`displayColWidth`and`displayRowHeight`that return the actual row or height of a cell including any resizing.
* [mediafileinfoDAT Class](<../MediafileinfoDAT_Class.md> "MediafileinfoDAT Class")`.metadata`\- Returns a dictionary of the metadata key value entries.
* [Monitor Class](<../Monitor_Class.md> "Monitor Class") \- Added new`.connectedGPUName`and`.connectedGPUIndex`members.
* [Page Class](<../Page_Class.md> "Page Class") / [Cell Class](<../Cell_Class.md> "Cell Class") \- Comparisons to 'None' vs None now work properly.
* [Par Class](<../Par_Class.md> "Par Class") \- Comparisons now use parameter evaluations in all cases. **BACKWARD COMPATIBILITY** par1 == par2 would previously only return true if it were the same parameter object, now it compares their evaluation results.
* [Par Class](<../Par_Class.md> "Par Class")`.enablePar`\- Get or set the single parameter's enable state within the [ParGroup](<../ParGroup.md> "ParGroup"). For the entire ParGroup use ParGroup.enable or Par.enable. Can only be set on [Custom Parameters](<../Custom_Parameters.md> "Custom Parameters").
  * [ParGroup](<../ParGroup.md> "ParGroup")`.enableExpr`\- Now supports lambda format to enable individual parameter enabling within the ParGroup. Example:`n.parGroup.enableExpr = 'lambda x: x==2'`. #only enables third component
* [ParGroup](<../ParGroup.md> "ParGroup")`.enable`\- This member now returns a tuple of values instead of a single value, as parameters are now individually enable-able. 
    * **BACKWARD COMPATIBILITY** \- The return type of`ParGroup.enable`is now a tuple, not a single bool.
* [Par Class](<../Par_Class.md> "Par Class") / [ParGroup Class](<../ParGroup_Class.md> "ParGroup Class")`.readOnly`\- This member can now be set per parameter, not just the entire ParGroup as a whole. 
    * **BACKWARD COMPATIBILITY** \- ParGroup.readOnly now returns a tuple of individual values, not a single bool.
* [Par Class](<../Par_Class.md> "Par Class")`.isSamePar(x)`/ [ParGroup Class](<../ParGroup_Class.md> "ParGroup Class")`.isSameParGroup(x)`\- Returns True if argument passed refers to same parameter as object does. For example:`n.par.tx.isSamePar(p)`returns True if`p`is the same parameter as`n.par.tx`. Note this is different from using`==`which compares the parameter's evaluated values.
  * [ParGroup Class](<../ParGroup_Class.md> "ParGroup Class")`.maxSize`\- Returns the maximum number of parameter elements for this ParGroup.
  * [ParGroup](<../ParGroup.md> "ParGroup")`.defaultSize`\- Returns default number of parameter elements for this ParGroup.
  * [ParGroup](<../ParGroup.md> "ParGroup")`.suffixes`\- Returns a list of suffixes used to name the parameter elements of this ParGroup.
* isPar, isParGroup renamed to isSamePar, isSameParGroup
* [Par Class](<../Par_Class.md> "Par Class") / [ParGroup Class](<../ParGroup_Class.md> "ParGroup Class")`.sequenceBlock`\- Returns the [sequenceBlock Class](<../SequenceBlock_Class.md> "SequenceBlock Class") the object belongs to, or None.
* [Run Class](<../Run_Class.md> "Run Class") when executed from a DAT, Cell, or td, now remains persistent. Allows you to check the state after its completed.
* Properly setup context '`me`', when executing a`run()`command. In some cases '`me`' value was set to root instead of the location the`run`command originated from. This could lead to permission errors trying to access neighboring content within a private component for example. **BACKWARD COMPATIBILITY** \- '`me`' context no longer wrongly set to root in some cases.
* [ParCollection Class](<../ParCollection_Class.md> "ParCollection Class") / [ParGroupCollection Class](<../ParGroupCollection_Class.md> "ParGroupCollection Class") is now iterable. You can iterate through all the parameters of an operator, a sequence or even a block:


[code]
       debug(list(n.par))
       debug(list(n.par.S.sequence.blockPars))
       debug(list(n.par.S.sequence[1].par))
       debug(list(n.parGroup))
       debug(list(n.par.S.sequence.blockParGroups))
       debug(list(n.par.S.sequence[1].parGroup))
    
[/code]
* [Sequence Class](<../Sequence_Class.md> "Sequence Class")`.reorderBlocks(index1, index2..)`\- Reorder the specified blocks leaving the rest in place.
  * [Sequence Class](<../Sequence_Class.md> "Sequence Class")`.sortBlocks(key=lambda block: (`block.namePar`or`block[0]).eval()`, baseName=_, reverse=False)_`* key - A function that is passed to every block in the sequence to return a sortable value. By default it evaluates the block's main name parameters, if defined, else the first parameter of the block.
    * baseName - If specified, uses the parameter of each block with that baseName as the sort value.
    * reverse - If True, reverses the order of the sort.


[code]
    For Example:
     .sortBlocks(baseName='value', reverse=True)  # sort on reverse *value parameters in the sequence
     .sortBlocks(key=lambda block: block.par.value)  # same as above
     .sortBlocks(key=lambda block: block.par.x + block.par.y)  # sort on combined x+y value of each block
    
[/code]
* [Sequence Class](<../Sequence_Class.md> "Sequence Class")`.blockName`\- Gets the basename of the parameter used to name each block. By default this would be 'Blockname'
  * [sequenceBlock Class](<../SequenceBlock_Class.md> "SequenceBlock Class")`.name`\- Get the name of a particular block. This is the value of the parameter in the block with basename 'Blockname'. When blocks are added this parameter gets automatically updated with a unique value. This means, in addition to accessing a block by index (example:`n.seq.MySequence[3]`) you can also access it by name (example:`n.seq.MySequence['SectorJ']`).
  * [SequenceBlock Class](<../SequenceBlock_Class.md> "SequenceBlock Class")`.namePar`\- Returns parameter defining name of block, or None. (As opposed to .name which returns that parameter's value).
  * [Sequence Class](<../Sequence_Class.md> "Sequence Class")`.Sequence[name or index]`\- Finds a block by its position or block name as described above.
  * [Sequence Class](<../Sequence_Class.md> "Sequence Class")`.moveBlock`\- Now takes optional keyword '`num`', describing number of blocks to move.
  * [Sequence Class](<../Sequence_Class.md> "Sequence Class") \- moveBlock, insertBlock arguments can be names, integers, or SequenceBlock objects.
  * [sequence Class](<../Sequence_Class.md> "Sequence Class")`.moveBlock(blockFromIndex, blockToIndex, num=1)`\- Moves the specified blocks.
  * [SequenceBlock Class](<../SequenceBlock_Class.md> "SequenceBlock Class")`.destroy()`replaces [Sequence Class](<../Sequence_Class.md> "Sequence Class")`.destroyBlock(index)`which is now deprecated.
* [SysInfo Class](<../SysInfo_Class.md> "SysInfo Class") \- Added new members`.GPUName`,`.GPUID`, and`.GPUPlatformID`.
* [td Module](<../Td_Module.md> "Td Module") / [DAT Class](<../DAT_Class.md> "DAT Class") / [Cell Class](<../Cell_Class.md> "Cell Class") \- Added boolean option _`wallTime`_ to`.run()`method to specify if the delay options are to be based on elapsed frames or elapsed time.
  * [Tdu Module](<../Tdu_Module.md> "Tdu Module").`tdu.isPointCloudFile()`\- Added to identify if a file is a point cloud file.
* [textCOMP Class](<../TextCOMP_Class.md> "TextCOMP Class")`.evalTextSize`now takes optional keywords _wordWrap_ and _pageWidth_ that can override the parameter values during this call.
  * [TOP Class](<../TOP_Class.md> "TOP Class") \- Improvements for 3D texture support. 
    * Added support for`.numpyArray()`to download 3D textures.
    *`.numpyArray()`now downloads full Cube Maps.
    *`.cudaMemory()`now supports outputting data from 3D/2DArray/Cube textures.
  * [UI Class](<../UI_Class.md> "UI Class")`.messageBox()`\- No longer is called recursively from [Execute DAT](<../Execute_DAT.md> "Execute DAT") Frame Start/End callbacks.
  * [UI Class](<../UI_Class.md> "UI Class")`.rolloverPage`\- Returns the parameter dialog 'page' currently under the mouse, or None. Similar to UI.rolloverParGroup below.
  * [UI Class](<../UI_Class.md> "UI Class")`.rolloverParGroup`\- Returns ParGroup currently under the mouse, including parameter labels.
* Optional keyword argument _alwaysOnTop_ added to several UI elements


[code]
       OP.openViewer(alwaysOnTop=False)
       OP.openParameters(alwaysOnTop=False)
       UI.openBookmarks(alwaysOnTop=False)
       UI.openTextport(alwaysOnTop=False)
       UI.openWindowPlacement(alwaysOnTop=False)
       UI.openPaletteBrowser(alwaysOnTop=False)
       UI.openMIDIDeviceMapper(alwaysOnTop=False)
       UI.openNewProject(alwaysOnTop=False)
       UI.openKeyManager(alwaysOnTop=False)
       UI.openErrors(alwaysOnTop=False)
       UI.openVersion(alwaysOnTop=False)
       UI.openPreferences(alwaysOnTop=False)
       UI.openBeat(alwaysOnTop=False)
    
[/code]
* Extension changes 
    *`onDestroyTD`called instead of __delTD__ when extension destroyed (still backward compatible).
    *`onPostInit`renamed to`onInitTD`### New Palette
* [Palette:cameraViewport](<../Palette-cameraViewport.md> "Palette:cameraViewport") \- Improvements 
    * Added instance Id and custom attributes to pick callback.
    * New parameter to add padding around an object when framing.
    * Callback return value can now be used to indicate the event was handled and camera movement should not be initiated.
    * Pivot position is now saved to file. Fixed the 'Pivot Distance' parameter default.
    * Nodes [tagged](<../Tag.md> "Tag") with 'cameraViewportExcludeBounds' are now excluded from bounding box calculations used for framing and homing.
    * New parameters to set the homing bounds manually.
* [Palette:cornerPinPOP](<../Palette-cornerPinPOP.md> "Palette:cornerPinPOP") \- A new component mirroring the functionality of [Palette:cornerPinSOP](<../Palette-cornerPinSOP.md> "Palette:cornerPinSOP") but using POPs instead.
* [Palette:cppParsTemplateGen](<../Palette-cppParsTemplateGen.md> "Palette:cppParsTemplateGen") \- 0.1.2 - Fixed namespace issue that was occurring with the latest CPlusPlus Custom OPs API.
  * [Palette:cppParsTemplateGen](<../Palette-cppParsTemplateGen.md> "Palette:cppParsTemplateGen") \- v0.1.3 - Fixed parameter variable name formatting when parameter name uses numbers or symbols.
* [Palette:gestureCapture](<../Palette-gestureCapture.md> "Palette:gestureCapture") \- v10.0.0 - Converted to use and output POPs.
* [Palette:lister](<../Palette-lister.md> "Palette:lister") \- Added drag-to-size column headers. 
    * Controlled by Sizeable Cols and Save Col Resizes parameters.
    * colDefine now has a "sizeable" row for every column.
    * Works best with a maximum of 1 stretchy column.
    * Includes a cleanup of the Select/Sort/Filter parameter page.
    * **sizeable** : old listers will require setting the "sizeable" row in the colDefine table for this feature to work.
    * **Column border** : listers using old listerConfig components will not have a border between column headers. This is controlled by the border settings on the _header_ component in listerConfig. Change _Right Border_ to Border A, then set color on _Border A_. Gray 0.4 is the default.
  * [Palette:lister](<../Palette-lister.md> "Palette:lister") \- colDefine and look OPs now use "topFill" to define how TOPs in cells fill the cell.
  * [Palette:lister](<../Palette-lister.md> "Palette:lister") \- Fixed an issue where column headers didn't use justify setting provided in the colDefine table.
* [Palette:logger](<../Palette-logger.md> "Palette:logger") \- v2.6.1 - Major overall. 
    * The logger object (self.Logger) is now always initialized. This prevents possible error where logging would fail because the logger was not initialized. This can however cause cases of silent logging, where the messages are added to a queue and not dequeued. See following point.
    * The logger is now initialized with a QueueHandler. The QueueHandler allow for messages to be queued and dequeued overtime. Messages can be queued safely from additional threads, and dequeued on the main TouchDesigner thread. When dequeued, messages are eventually passed to the extra handlers such as the StreamHandler (textport) or FileHandler.
    * A new dictionnary ExtraHandler is holding the handlers managed by the Logger COMP. When any of the managed handlers is updated, a new QueueListener is created to handle the future log messages and changes.
    * New methods to Add or Remove Extra Handlers are exposed. They should be used when a user want to add a custom handler and the log messages should be passed to this handler when dequeued.
    * New defaults and measures to avoid a case where a new Logger COMP reuse a logger instance caused by a perfect name match in the Logger name and hierarchy. This could happen in the past if a Logger was named “ABC” and pointing to a parent “project1”. The resulting logger name would be “project1.ABC” and this match could exist in another component when using multiple loggers. This should be mitigated by new defaults, but this is not entirely avoidable. Try to name your loggers without generic names.
    * Adding support for File rotation settings.
    * Code cleanup, removing unnecessary methods, various fixes.
* [Palette:operatorPath](<../Palette-operatorPath.md> "Palette:operatorPath") \- 1.4.0 - Added 'Font File' parameter.
* [Palette:particlesGpu](<../Palette-particlesGpu.md> "Palette:particlesGpu") \- Looping time to avoid bad distribution of hash function upwards of 24 hour runtime.
  * [Palette:pointRender](<../Palette-pointRender.md> "Palette:pointRender") \- v2.0.0 - Updated to POPs workflow.
  * [Palette:popDialog](<../Palette-popDialog.md> "Palette:popDialog") \- Added text entry modes including password, float, and int. Available in parameters or Open command.
  * [Palette:popMenu](<../Palette-popMenu.md> "Palette:popMenu") 1.3.1 - Submenus will now work when timeline is paused.
  * [Palette:quadReproject](<../Palette-quadReproject.md> "Palette:quadReproject") \- v1.0.0 - Complete rework. Component is now almost exclusively relying on parSequences and expressions.
* [TDAbleton](<../TDAbleton.md> "TDAbleton") \- 2.5.3 
    * Ableton Component's sendOSC functions no longer work when 'Connect' parameter is off. If you need to override this in script, call sendOSC directly on the TDAbleton master component.
    * Firing an empty clip slot (from abletonClipSlot component) on a record-armed track will start recording a new clip.
* [Palette:tdPyEnvManager](<../Palette-tdPyEnvManager.md> "Palette:tdPyEnvManager") \- Initial release. A component to sideload and manage third-party python and conda environments.
* [Thread Manager](<../Thread_Manager.md> "Thread Manager") \- First public release. A new system component and a set of palette components designed to facilitate Python threading in TouchDesigner.
  * [Palette:threadManagerClient](<../Palette-threadManagerClient.md> "Palette:threadManagerClient") \- A component which works with the Thread Manager COMP, the ThreadManagerClient is designed around it's callback DAT. Users should review the template code and adapt it to their own cases. The customized methods implemented in the ThreadManagerClient Callback are generating a TDTask that gets passed to the Thread Manager TDTask queue. While experienced developers can rely on the Thread Manager directly using`op.TDResources.ThreadManager`, users not familiar with threading should consider using the ThreadManager Client instead.
* [Palette:treeLister](<../Palette-treeLister.md> "Palette:treeLister") \- Has the new lister topFill and sizable columns features.
  * [Palette:webBrowser](<../Palette-webBrowser.md> "Palette:webBrowser") \- Better support for inputing unicode characters in languages like German and Japanese.

### Bug Fixes and Improvements
* Upgraded to Blackmagic SDK 14.4. - [Blackmagic Design](<../Blackmagic_Design.md> "Blackmagic Design")
  * Upgraded to Deltacast SDK/Driver 6.24.1. - [Deltacast](<../Deltacast.md> "Deltacast")
  * Upgraded to depthai 2.30.0. - [OAK-D](<../OAK-D.md> "OAK-D")
  * Upgraded to OpenCV 4.10.0. - [OpenCV](<../OpenCV.md> "OpenCV")
  * Upgraded to RenderStream 2.0. - [RenderStream](<../RenderStream.md> "RenderStream")
  * Upgraded to slugLibrary 7.2 - [Text COMP](<../Text_COMP.md> "Text COMP"), [Text TOP](<../Text_TOP.md> "Text TOP"), DAT viewers, etc.
  * Upgraded to Spout SDK 2.007.014 - [Syphon Spout In TOP](<../Syphon_Spout_In_TOP.md> "Syphon Spout In TOP") / [Syphon Spout Out TOP](<../Syphon_Spout_Out_TOP.md> "Syphon Spout Out TOP")
  * Upgraded to ZED SDK 5.0.1. Pascal GPUs are no longer supported with ZED. - [ZED](<../ZED.md> "ZED")
  * Upgraded to Helios SDK v11.0 with IDN adapter support - [Laser Device CHOP](<../Laser_Device_CHOP.md> "Laser Device CHOP") \- [Helios](<https://bitlasers.com/helios-laser-dac/>)


  
**COMP**
* [Engine COMP](<../Engine_COMP.md> "Engine COMP") \- Improvements and bug fixes. 
    * Improved the performance of TOP outputs.
    * Fixed connected multi-input OPs (eg Merge) losing connections during reload.
    * Fixed options for the 'Asset Paths' parameter functioning the wrong way around.
    * Fixed crash which could occur under GPU resource starvation.
* [FBX COMP](<../FBX_COMP.md> "FBX COMP") / [USD COMP](<../USD_COMP.md> "USD COMP") \- Added 'Import POPs' parameter which will use POPs in place of SOPs when importing.
  * [FBX COMP](<../FBX_COMP.md> "FBX COMP") \- Normalize bone weights of the imported assets.
* [Geo Text COMP](<../Geo_Text_COMP.md> "Geo Text COMP") \- New 'Face Camera' functionality. 
    * 'Face Camera' behaviour changed such that it rotates about the anchor point of the layout box.
    * 'Width Affected by 'FOV' and 'Lift Towards Cam' parameter now works with Orthographic camera type.
    * Added 'Lift Towards Camera' parameter.
    * Make 'Depth Scale S Curve' parameter independent from 'Face Camera'.
    * Fixed 'Face Camera' and 'Depth Scaling' to work for all align modes and anchorUVs.
    * Fixed 'Face Camera' relative orientation of appended blocks.
    * 'Face Camera' parameter works properly with the 'Specification DAT's 'append' flag.
* [Panel COMPs](<../Panel_Component.md> "Panel Component") \- Fixed an issue with the 'Use Vertical' option in 'Fixed Aspect' menu parameter. Also addressed aligning a row of children with simultaneous Fill and Fixed Aspect ratios.
* [Parameter COMP](<../Parameter_COMP.md> "Parameter COMP") \- 'Labels' toggle to turn on/off parameter labels leaving only the active part of the parameter to the right of the label ie. the slider, toggle, button, field, etc.
* [Text COMP](<../Text_COMP.md> "Text COMP") \- Improvements and bug fixes. 
    * Improved layout of text when both 'Scale Text to Fit' and 'Word Wrap' are enabled together.
    * Copying text when in 'Select Only' mode no longer includes hidden formatting directives.
    * Fixed cursor movement and selection with formatting directives when using 'Select Only' mode.
    * Fixed a bug that removed leading line breaks in multi-line mode.
* [Window COMP](<../Window_COMP.md> "Window COMP") \- New features and improvements. 
    * A new 'Prevent Display Sleep' toggle parameter has been added to keep your display from going to sleep.
    * Renamed "monitor" to "display" in parameters, menus and warnings.
    * Added a warning if the specified monitor doesn't exist while the window is opened in perform mode.
    * Fixed issue which could cause the wrong OP to be used in [Perform Mode](<../Perform_Mode.md> "Perform Mode") after using Open as Perform Window from a [Window COMP](<../Window_COMP.md> "Window COMP")'s parameter dialog.
    * On macOS, when a window is sized to exactly fill one or all monitors and has no borders, it will open as a full-screen window, matching behaviour on Windows.
    * Removed notion of 'Stereo' from Window COMP and underlaying classes.


  
**TOP**
* [Cache TOP](<../Cache_TOP.md> "Cache TOP") \- Bug fixes 
    * Fixed a case where 'Reset' would create a (0,0,0,1) texture instead of (0,0,0,0).
    * Fixed 'Output Index' not returning correct index if the cache isn't full due to 'Replace Single' being used.
    * Fixed 'Pre-Fill' sometimes filling the wrong resolution.
* [Chroma Key TOP](<../Chroma_Key_TOP.md> "Chroma Key TOP") \- Fixed a hang that can occur with this operator.
  * [Corner Pin TOP](<../Corner_Pin_TOP.md> "Corner Pin TOP") \- Added 'Mapping' parameter to the 'Extract' page for option between Bilinear and Perspective extraction.
  * [Displace TOP](<../Displace_TOP.md> "Displace TOP") \- 'Vertical Source' parameter default value changed to Green.
* [Movie File In TOP](<../Movie_File_In_TOP.md> "Movie File In TOP") \- Bug fixes. 
    * Fixed issue that can occur with 2 channel .exr files.
    * Fixed some cases where compressed format .dds files wouldn't be read properly.
* [Movie File Out TOP](<../Movie_File_Out_TOP.md> "Movie File Out TOP") \- Bug fixes. 
    * Header DAT parameter is now disabled for formats that don't support it.
    * Fixed H264/H265 files producing artifacts when seeking.
    * Fixed an issue which prevented some third-party applications from recognizing the alpha channel in exported ProRes 4444.
    * Selecting YUV 4:4:4 (10-Bit) when exporting ProRes 4444 correctly allows the encoder to discard the alpha channel on macOS 13 and above.
* [Movie File In TOP](<../Movie_File_In_TOP.md> "Movie File In TOP") / [Video Stream In TOP](<../Video_Stream_In_TOP.md> "Video Stream In TOP") \- 'Hardware Decode' now defaults to On.
* [Noise TOP](<../Noise_TOP.md> "Noise TOP") \- 'Derivative' now supported for Simplex 4D and Perlin 4D noise. For derivatives of 4D noise types, the 'Alpha' parameter will be disabled and the alpha channel will have the 4th component of the derivative.
* [OP Viewer TOP](<../OP_Viewer_TOP.md> "OP Viewer TOP") \- Fixed cook dependency warnings when appending anything to an OP Viewer TOP.
  * [Render TOP](<../Render_TOP.md> "Render TOP") \- A few new parameters have been added. 
    * Added a new 'Render' pulse parameter to render one frame when the 'Render' toggle parameter is turned off.
    * Added a new 'Background Color' parameter, which is combined with the [Camera COMP](<../Camera_COMP.md> "Camera COMP")'s Background Color to determine the final Background Color of the render.
    * For working with UV Unwrap workflows with POPs, a new 'UV Unwrap POP Coord Attribute' parameter has been added.
  * [Render Pass TOP](<../Render_Pass_TOP.md> "Render Pass TOP") \- Can no longer have a different pixel format than the [Render TOP](<../Render_TOP.md> "Render TOP") it's downstream from.
  * [Render Select TOP](<../Render_Select_TOP.md> "Render Select TOP") \- Fixed crash that can occur when deleting this node in some cases.
  * [Resolution TOP](<../Resolution_TOP.md> "Resolution TOP") \- Don't allow mipmap filtering on the input when 'High Quality Resize' is used.
* [Script TOP](<../Script_TOP.md> "Script TOP") \-`copyNumpyArray`and`cudaCUDAMemory()`now support 3D, 2D Texture Array and Cube Map textures.
  * [Slope TOP](<../Slope_TOP.md> "Slope TOP") \- Default for 'Green' parameter changed to 'Vertical Luminance' and default for 'Blue' parameter changed to 'Neutral'.
  * [Syphon Spout In TOP](<../Syphon_Spout_In_TOP.md> "Syphon Spout In TOP") / [Syphon Spout Out TOP](<../Syphon_Spout_Out_TOP.md> "Syphon Spout Out TOP")\- Upgrade to SDK 2.007.014. Addws support for Sender FPS in [Info CHOP](<../Info_CHOP.md> "Info CHOP") when enabled in the Spout Settings dialog.
* [Video Stream In TOP](<../Video_Stream_In_TOP.md> "Video Stream In TOP") \- Improvements 
    * Improved re-buffering behavior and added a new 'Force Re-buffer' pulse parameter to be able to force a re-buffer.
    * Avoid truncating the end of the file when streaming a non-realtime file source (ie. a complete file not a live-stream).
    * Added 'sample_rate' and 'true_length' [Info CHOP](<../Info_CHOP.md> "Info CHOP") channels.
* [Web Render TOP](<../Web_Render_TOP.md> "Web Render TOP") \- updates and improvements. 
    * Updated to Chromium 132.0
    * The option to 'Use Shared Textures' in chromium (cef) on windows is back.
    * New parameter for 'DPI Scaling'.
    * New parameter to specify a table to 'Modify Request Headers'.
    * **Backward Compatibility Issue** \- Using the same cache with 2 Web Render TOPs is no longer supported, the second one will error.
* [ZED TOP](<../ZED_TOP.md> "ZED TOP") \- Added both support for SVO2 playback and support for network streaming data from another machine using ZED native streaming.
  * [ZED Select TOP](<../ZED_Select_TOP.md> "ZED Select TOP") \- Added this new operator to select different images from a [ZED TOP](<../ZED_TOP.md> "ZED TOP").


**CHOP**
* [CHOP](<../CHOP.md> "CHOP") = Simplified CHOP Viewer 'Scope Tools' to a single string field for scope. Supports [Pattern Matching](<../Pattern_Matching.md> "Pattern Matching").
* [Audio Device In CHOP](<../Audio_Device_In_CHOP.md> "Audio Device In CHOP") / [Audio Movie CHOP](<../Audio_Movie_CHOP.md> "Audio Movie CHOP") / [Audio Stream In CHOP](<../Audio_Stream_In_CHOP.md> "Audio Stream In CHOP") / [Audio Web Render CHOP](<../Audio_Web_Render_CHOP.md> "Audio Web Render CHOP") \- Default stereo channels are now output when the CHOP is in error state (ie. no device selected, no source found, etc.) to avoid network errors downstream.
  * [Audio File Out CHOP](<../Audio_File_Out_CHOP.md> "Audio File Out CHOP") \- Added support for big-endian .aiff formats.
  * [Audio Movie CHOP](<../Audio_Movie_CHOP.md> "Audio Movie CHOP") \- Added a 'Volume' parameter to be more inline with other audio sources.
* [Blob Track CHOP](<../Blob_Track_CHOP.md> "Blob Track CHOP") \- Internal ID counting behavior improved. The final effect is that IDs ramp up in a much more controlled manner.
* [Count CHOP](<../Count_CHOP.md> "Count CHOP") \- Added 'Count Up' and 'Count Down' momentary parameters to allow counting with no input connected.
  * [Count CHOP](<../Count_CHOP.md> "Count CHOP") \- Non-timesliced mode now uses all channels of the Increment input, not just the first. This allows you to specify separate count increments for channels on the first input by supplying multiple channels into the Increment input.
* [Delay CHOP](<../Delay_CHOP.md> "Delay CHOP") \- Better queueing behavior when frames skipped / max delay setup incorrectly.
  * [DMX Out CHOP](<../DMX_Out_CHOP.md> "DMX Out CHOP") / [DMX In CHOP](<../DMX_In_CHOP.md> "DMX In CHOP") \- Added better support for DMXking devices, re-categorized parameters.
  * [Feedback CHOP](<../Feedback_CHOP.md> "Feedback CHOP") \- Reset on startup/initial cook similar to [Feedback TOP](<../Feedback_TOP.md> "Feedback TOP").
  * [File In CHOP](<../File_In_CHOP.md> "File In CHOP") \- Channel names now preserved when reading a .chan file into a CHOP. **** BACKWARD COMPATIBILITY **** Chan files now preserve channel names instead of always defaulting to chan1, chan2, chan3, ...
  * [Info CHOP](<../Info_CHOP.md> "Info CHOP") \- Now updates more accurately when monitoring nodes controlled by scripts.
  * [Join CHOP](<../Join_CHOP.md> "Join CHOP") \- Changed behaviour such that the first input to the CHOP doesn't need to be non-empty for the rest of the inputs to be joined.
  * [Laser Device CHOP](<../Laser_Device_CHOP.md> "Laser Device CHOP") \- Helios - Added support for full 16-bit color and position, as well up to 4 optional user channels (user1, user2, user3, user4).
  * [Pangolin CHOP](<../Pangolin_CHOP.md> "Pangolin CHOP") \- Added support for using POPs an an input. Also added 'Zone' attribute override for POP inputs.
* [Parameter CHOP](<../Parameter_CHOP.md> "Parameter CHOP") \- New features and bug fixes. 
    * Added 'Sequences' parameter to better parse [Sequential Parameters](<../Sequential_Parameters.md> "Sequential Parameters").
    * Fixed 'Rename' parameter menu issue where the menu would display names inconsistent with actual channel names.
    * Fixed 'pageindex' not returning a label nor updating on change.
* [Render Pick CHOP](<../Render_Pick_CHOP.md> "Render Pick CHOP") \- Fixed a bug in the render pick event that caused a crash in the callback.
  * [RenderStream In CHOP](<../RenderStream_In_CHOP.md> "RenderStream In CHOP") \- Added support for multiple Scenes and Schemas.
  * [Resample CHOP](<../Resample_CHOP.md> "Resample CHOP") \- Added new parameter 'Use Last Frame Only' to trim to the input's last frame and perform the resample on that.
* [Speed CHOP](<../Speed_CHOP.md> "Speed CHOP") \- New 'Speed' parameter that allows generating values when no inputs are connected.
* [Stretch CHOP](<../Stretch_CHOP.md> "Stretch CHOP") / [Resample CHOP](<../Resample_CHOP.md> "Resample CHOP") \- New interpolation method 'Repeat Samples' that provides better spaced results when lengths are integer multiples of original.
* [Timer CHOP](<../Timer_CHOP.md> "Timer CHOP") \- Improvements and bug fixes.\ 
    * New 'Run Values' parameter controls a subtle behavior of what the counters are on the frame when Start is pulsed and the`running`channel goes from 0 to 1. If the menu is set to Zero, the channels`timer_frames`,`timer_samples`and`timer_fraction`will be 0 when Start is pulsed. If set to One,`timer_frames`and`timer_samples`will be at one frame, and`timer_fraction`will also have stepped forward by a frame. These channels are always 0 when you Initialize.
* * Better spacing of Timer CHOP output in first timeslice to work better with non-timesliced OPs (such as the [Movie File Out TOP](<../Movie_File_Out_TOP.md> "Movie File Out TOP")).
    * Fixed bug where Timer CHOP's python object didn't update after reaching the done state and returning to zero.
    * Fixed bad behavior when spaces were in [Info DAT](<../Info_DAT.md> "Info DAT") names.
    * Fixed growing cook delays when external time runs past timer length.
    * 'Defer Par Changes' now defaults to off.
    * Round values to the nearest sample when units are seconds. (Fixes cases of 1 2/3 seconds not being over 100 frames).
    * [Timer CHOP](<../Timer_CHOP.md> "Timer CHOP") \- **BACKWARD COMPATIBILITY** \- The first segment was always one sample short, but has now been fixed.
* [Touch In CHOP](<../Touch_In_CHOP.md> "Touch In CHOP") / [Touch Out CHOP](<../Touch_Out_CHOP.md> "Touch Out CHOP") \- The Touch In and Touch Out CHOPs work in non-timeslice mode now, sending multisample data.
* [ZED CHOP](<../ZED_CHOP.md> "ZED CHOP") \- Added a backwards compatibility warning for ZED on startup for older projects - **BACKWARDS COMPATIBILITY ISSUE** \- [ZED CHOP](<../ZED_CHOP.md> "ZED CHOP") \- Now needs to point to a [ZED TOP](<../ZED_TOP.md> "ZED TOP") to select it's camera source.


**DAT**
* [DATs](<../DAT.md> "DAT") \- Since newlines are supported in DAT cells, display them as symbols and allow them to be selected/deleted/copied etc.
* [Audio Devices DAT](<../Audio_Devices_DAT.md> "Audio Devices DAT") / [Video Devices DAT](<../Video_Devices_DAT.md> "Video Devices DAT") \- Now refreshes properly with fewer redundant intermediate callbacks.
  * [DAT Execute DAT](<../DAT_Execute_DAT.md> "DAT Execute DAT") \- A new`onTableChange`method does everything now, the other 4 legacy methods (`onRowChange`,`onColChange`,`onCellChange`, and`onSizeChange`) are now deprecated.
  * [Folder DAT](<../Folder_DAT.md> "Folder DAT") \- When "All Extensions" is off, an empty value in the "Extensions" parameter matches files with no extension.
* [Media File Info DAT](<../Media_File_Info_DAT.md> "Media File Info DAT") \- 'valid' row added to indicate if the entries in the value columns are valid. Also added python members for 'seconds' row and 'valid' row.
  * [OP Find DAT](<../OP_Find_DAT.md> "OP Find DAT") \- Now supports different aliases for toggle values (on/1/True off/0/False).
  * [Parameter DAT](<../Parameter_DAT.md> "Parameter DAT") \- Fixed 'pageindex' not returning a label nor updating on change.
  * [Perform DAT](<../Perform_DAT.md> "Perform DAT") \- Added 'Clear' parameter that lets you clear the DAT contents.
  * [Web Server DAT](<../Web_Server_DAT.md> "Web Server DAT") \- Fixed`onWebSocketClose`callback not triggered on server de-activation or restart and also made a fix to WebSocket closing so that it correctly sends a 'Close Frame' to the client.
  * [Web Server DAT](<../Web_Server_DAT.md> "Web Server DAT") \- Fixed a hang using 'Restart' pulse with active WebSocket connections. Also fixed onWebSocketClose callback not being triggered in some cases.


**SOP**
* [Sphere SOP](<../Sphere_SOP.md> "Sphere SOP") \- The w texture coordinate is now zero when creating Equirectangular coordinates.
* [ZED SOP](<../ZED_SOP.md> "ZED SOP") \- Added a backwards compatibility warning for ZED on startup for older projects - **BACKWARDS COMPATIBILITY ISSUE** \- [ZED SOP](<../ZED_SOP.md> "ZED SOP") \- Now needs to point to a [ZED TOP](<../ZED_TOP.md> "ZED TOP") to select it's camera source.


  
**MAT**
* [MAT](<../MAT.md> "MAT") \- All MAT operators now have a bypass flag.
* [MAT](<../MAT.md> "MAT") \- New 'Texture Sample Mode' menu found in all texture map's extended parameters to select between regular texture coordinates, screen space coordinates, or the new tri-planar mapping coordinates. 
    * Added 'Texture Sampling Mode' menu to PBR MAT Metallic map, Roughness map, Ambient Occlusion map
    * Added 'Texture Sampling Mode' menu to PBR MAT Specular Level map
    * Added 'Texture Sampling Mode' menu to Alpha map
    * Added 'Texture Sampling Mode' menu to Height maps, Emit maps, Darkness Emit maps
    * Added 'Texture Sampling Mode' menu to Diffuse maps, Specular maps, Normal maps
    * Added parameter disabling for 'Texture Sampling Mode' menu of Multi-Texturing map.
  * [Point Sprite MAT](<../Point_Sprite_MAT.md> "Point Sprite MAT") \- New menu 'Sizing Model' allows the depth based scaling of the sprites to be either via the Constant/Attenuate parameters, or Perspective Correct scaling like most geo objects. 
    * Added 'Size Affected by FOV/OrthoWidth' parameter to make scaling FOV independent or dependent.


**Misc**
* [Geometry Viewer](<../Geometry_Viewer.md> "Geometry Viewer") \- A number of new display options have been added for working with POPs. These options can be found in the viewer's right-click menu. 
    * Toggle Hilite Dot Per Point - Displays an overlay dot for each point in the scene (POPs only).
    * Display Attribute Text - Display attribute data or indices as text overlayed on the geometry (POPs only).
    * Display Attribute Vector - Display multi-dimension attribute data as vector arrows overlayed on the geometry (POPs only). If the selected attribute is less than 3 dimensions, the missing dimensions will be assumed as 0. Attribute values are normalized so that vectors with smaller magnitudes will appear as smaller arrows.
    * Display Attribute Dots - Display single dimension attributes as a colored dot with a ring of blue relative to the magnitude of the value. The smallest value in the scene appears as a solid red dot and the largest as a solid blue dot.
    * Display Attribute Colors - Display multi-dimension attribute data as a colored dot (POPs only). The attribute is not normalized to preserve the color value which means attributes greater than one will appear solid white on most monitors.
    * The [Display Options](<../Display_Options.md> "Display Options") dialog also has new options on the 'Misc' page. Here you'll now find settings for Scale Attribute Overlays, Scale in Screen Space, Thin Attribute Range, and Thin Attribute Percentage.
  * [ZED](<../ZED.md> "ZED") \- Now supports Blackwell GPUs (Geforce 5xxx), no longer supports Pascal GPUs (Geforce 1xxx, P-series Quadros).
  * Script Operators [Script CHOP](<../Script_CHOP.md> "Script CHOP") / [Script DAT](<../Script_DAT.md> "Script DAT") / [Script TOP](<../Script_TOP.md> "Script TOP") / [Script SOP](<../Script_SOP.md> "Script SOP") \- New callback`onGetCookLevel`added to manually specify the cook behaviour of the operator.
  * Script Operators - Allow setting parameter values in the onSetupParameters() callback.
  * [GLSL](<../GLSL.md> "GLSL") \-`TDCreateRotMatrix()`is now available in all GLSL shaders.
  * [Custom Operators](<../Custom_Operators.md> "Custom Operators") \- XYZW par type now supported.
  * Some changes to how .dmp files are created to obtain more information.
  * All In operators now have an optional 'OP' parameter as an alternative to wired input.
  * Fixed re-opening a minimized parameter dialog, view etc, instead of doing nothing.
  * Fixed bug where Undo shortcuts were blocked when the mouse was over an active DAT, CHOP or TOP.
  * Fixed problem displaying UTF8 characters in the [Textport](<../Textport.md> "Textport") when it is closed.
  * [macOS](<../MacOS.md> "MacOS") \- Stop playback during system sleep.
  * [macOS](<../MacOS.md> "MacOS") \- Folder parameters and ui.chooseFolder() now display a 'New Folder' button in the open dialog.
  * sys.executable now points to the included python executable, not TouchDesigner.

### Operator Snippets
* POPs Snippets coming soon!

### Backward Compatibility Changes
* **BACKWARD COMPATIBILITY ISSUE** \- [File In CHOP](<../File_In_CHOP.md> "File In CHOP") \- .chan files now preserve channel names instead of always defaulting to chan1, chan2, chan3, ...
  * **BACKWARD COMPATIBILITY ISSUE** \- [Timer CHOP](<../Timer_CHOP.md> "Timer CHOP") \- The first segment was always one sample short, this has now been fixed.
  * **BACKWARD COMPATIBILITY ISSUE** \- [ZED CHOP](<../ZED_CHOP.md> "ZED CHOP") \- Now needs to point to a [ZED TOP](<../ZED_TOP.md> "ZED TOP") to select it's camera source.
  * **BACKWARD COMPATIBILITY ISSUE** \- [ZED SOP](<../ZED_SOP.md> "ZED SOP") \- Now needs to point to a [ZED TOP](<../ZED_TOP.md> "ZED TOP") to select it's camera source.
  * **BACKWARD COMPATIBILITY ISSUE** \- [ZED](<../ZED.md> "ZED") \- Upgraded to ZED SDK 5.0.1, this update means Pascal GPUs are no longer supported with ZED.
  * **BACKWARD COMPATIBILITY ISSUE** \- [Par Class](<../Par_Class.md> "Par Class") \- Comparisons now use parameter evaluations in all cases. par1 == par2 would previously only return true if it were the same parameter object, now it compares their evaluation results.
  * **BACKWARD COMPATIBILITY ISSUE** \- [ParGroup](<../ParGroup.md> "ParGroup")`.enable`and`.readOnly`members now returns a tuple of values instead of a single bool value, as Par's are now individually enable-able.
  * **BACKWARD COMPATIBILITY ISSUE** \- [Par Class](<../Par_Class.md> "Par Class") / [ParGroup Class](<../ParGroup_Class.md> "ParGroup Class") \-`.readOnly`can now be set per Par, not just the entire ParGroup as a whole.
* **BACKWARD COMPATIBILITY ISSUE** \- 'me' context no longer wrongly set to root in some cases. When executing a run() command, in some cases 'me' value was set to root instead of the location the run command originated from. This could lead to permission errors trying to access neighbouring content within a private component for example.
