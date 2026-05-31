# MacOS

## macOS Version Support  
  
**NOTE: Always apply all macOS updates for the version of macOS you are on. For example, if you are on macOS 12, make sure to update to the lastest macOS 12.x.x**
* macOS 12 Monterey or newer is required for TouchDesigner 2025 builds.
  * macOS 10.15 or newer is required for TouchDesigner 2023 builds.
  * macOS 10.14 or newer is required for TouchDesigner 2022 builds.
  * macOS 10.12 can also be used on TouchDesigner builds 2021 and older. See [Previous Official Builds](<https://derivative.ca/download/archive>)

## Differences with TouchDesigner on macOS
* In most cases where one would use the "ctrl" modifier key on Windows, macOS uses the "cmd" key.
  * Common main menu items and macOS system wide shortcuts are respected where possible. For example, the location and keyboard shortcut for **TouchDesigner Preferences...** is 'macOS-like'.
  * The scroll wheel actions are inverted compared to Windows (by default), but this can be set in macOS with System Preferences > Mouse > Scroll Direction: Natural
  * TouchPlayer is distributed using a separate installer on macOS. You can find the TouchPlayer downloads in the dropdown menu for macOS here [Download Official Builds](<https://derivative.ca/download>)
  * CodeMeter Runtime for [USB Licensing Dongles](<./License_Dongle.md> "License Dongle") is a separate installer on macOS. Download it here [Download macOS CodeMeter](<https://www.wibu.com/support/user/user-software.html>) and use Codemeter Control Center version 7.40b
* You can use ctrl+c to interrupt Python scripts in macOS. Try it for hangs.
  * You can run multiple builds of TouchDesigner easily on macOS by simply putting the TouchDesigner application in a different folder or by renaming the TouchDesigner.app file (so it doesn't overwrite the existing build).

## Limitations and Known Issues
* Make sure to apply all OS updates within your macOS version. For example, if you are on macOS 12, make sure to update to the lastest macOS 12.x.x
* Nvidia specific features that use CUDA or Hardware Encoding/Decoding will not work. These include: 
    * Nvidia specifc SDKs such as Nvidia Flex and Nvidia Flow
    * Review the complete list of [Nvidia specific features](<./System_Requirements.htm#Feature_Specific_Requirements> "System Requirements")
* Line Width parameter on common page in Materials (MATs) has no effect.

#### macOS Apple Silicon Build Specific
* The following operators have not been ported yet
  * [Movie File In TOP](<./Movie_File_In_TOP.md> "Movie File In TOP") / [Movie File Out TOP](<./Movie_File_Out_TOP.md> "Movie File Out TOP") \- The [Cineform](<./GoPro_Cineform.md> "GoPro Cineform") codec SDK does not look like it will be updated for Apple Silicon, so it is not an option to add to these builds.
  * [RealSense TOP](<./RealSense_TOP.md> "RealSense TOP") / [RealSense CHOP](<./RealSense_CHOP.md> "RealSense CHOP") \- The [librealsense SDK v2.50.0](<https://github.com/IntelRealSense/librealsense/releases>) does not look like it will be updated for Apple Silicon, so it is not an option to add to these builds.

## Operators not supported
* DirectX TOPs - Microsoft SDK
  * Kinect OPs / Kinect Azure OPs - Microsoft SDK
  * NatNet CHOP \- Windows only SDK
  * Notch TOP \- Windows only SDK
  * Nvidia Flex OPs - Nvidia CUDA SDK
  * Nvidia Flow OPs - Nvidia SDK
  * Oculus Rift OPs - Windows only SDK
  * OpenVR OPs - Windows only SDK
  * Pangolin CHOP \- Windows only SDK
  * RealSense CHOP \- Windows only SDK
  * Scalable Display TOP \- Windows only SDK
  * SVG TOP \- Nvidia SDK
  * Video Stream Out TOP \- Nvidia Hardware Encoding
  * ZED TOP / ZED CHOP / ZED SOP \- Windows only SDK

## Crash Reports

You can find the crash reports via Applications->Utilities->Console. Look for a TouchDesigner crash reports under 'Crash Reports' 

To force a crash report when TouchDesigner is hanging, open up Terminal`ps -A | grep TouchDesigner`That should give you output with the process id of the hanging TouchDesigner, as follows:`<process-id> ?? 1:09.97 /Applications/TouchDesigner.app/Contents/MacOS/TouchDesigner`Run the following command to kill the process and force a crash report.`kill -3 <process-id>`## Spin Reports

If TouchDesigner freezes, a spin report might be generated during a hang and would appear in the Spin Reports section of Applications->Utilities->Console. If there are none you can open Applications->Utilities->Activity Monitor, select TouchDesigner and from the "..." item in the toolbar select Spindump to force a report. 

  
See [Troubleshooting in TouchDesigner](<./Troubleshooting_in_TouchDesigner.md> "Troubleshooting in TouchDesigner").
