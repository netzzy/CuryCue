# System Requirements

System requirements for [TouchDesigner](<./TouchDesigner_Products.md> "TouchDesigner Products") and [TouchPlayer](<./TouchPlayer.md> "TouchPlayer"). 

##### Basic Requirements

_Older than hereafter specified configurations might work but some features will not be available._

## Windows

**Operating System**
* Microsoft Windows 10 / Windows 11


**Hardware**
* A minimum of 4GB GPU memory, 8GB+ is recommended.
  * The most recent [Nvidia drivers](<http://www.nvidia.com/Download/index.aspx?lang=en-us>), [AMD drivers](<http://support.amd.com/us/gpudownload/Pages/index.aspx>) or Intel drivers are recommended.


TouchDesigner requires a GPU and drivers that support Vulkan 1.1. 

**Nvidia GPUs**
* Nvidia Geforce 1000-series or better.
  * Nvidia Quadro/RTX Pascal series or better.
  * Requires Driver 530.00 or newer. Driver 581.00 or later recommended.


**AMD GPUs**
* AMD Radeon 5000 series or better (RDNA architecture GPUs).


**Intel GPUs** NOTE: Not all features are supported on integrated video chipsets and there is a lower expectation on overall performance. 
* Intel 500 and newer GPUs (not the 5000, 6000 series). You can look for your GPU [here.](<https://www.intel.ca/content/www/ca/en/support/articles/000005524/graphics.html>)

## Apple Mac

**Operating System**
* Apple macOS 13 (Ventura) and up (See also [macOS](<./MacOS.md> "MacOS"))


**Hardware**
* Mac Pro / iMac / Mac Mini / MacBook Pro / MacBook Air 2020+
  * Your Mac must support macOS 13 or higher, but we recommend running the latest macOS. You can find a list of supported hardware [here](<https://en.wikipedia.org/wiki/MacOS_Monterey#Supported_hardware>).
  * We highly recommend a Mac with Apple Silicon for TouchDesigner. For Intel-based Macs we recommend a model with a discrete AMD GPU.

## Input Devices
* A three-button mouse with scroll-wheel is required.

## Feature Specific Requirements
* [Movie File In TOP](<./Movie_File_In_TOP.md> "Movie File In TOP") \- H.264 and H.265 hardware accelerated decoding 
    * On Windows Nvidia GPU only, or macOS for codecs the hardware supports.
  * [Movie File Out TOP](<./Movie_File_Out_TOP.md> "Movie File Out TOP") \- H.264 and H.265 encoding 
    * On Windows OS requires Nvidia GPU, also works on macOS.
  * [Video Stream Out TOP](<./Video_Stream_Out_TOP.md> "Video Stream Out TOP") \- Uses H.264 encoding 
    * Windows OS & Nvidia GPU only
  * [Syphon Spout In TOP](<./Syphon_Spout_In_TOP.md> "Syphon Spout In TOP") / [Syphon Spout Out TOP](<./Syphon_Spout_Out_TOP.md> "Syphon Spout Out TOP")
    * For Spout on Windows, Nvidia or AMD GPUs are required, Intel does not work.
  * [Face Track CHOP](<./Face_Track_CHOP.md> "Face Track CHOP") and [Face Track SOP](<./Face_Track_SOP.md> "Face Track SOP")
    * Windows OS & Nvidia RTX GPU only.
    * Mesh fitting using the Face Track SOP requires a compatible mesh file that can be downloaded from external sources.
  * [Nvidia Background TOP](<./Nvidia_Background_TOP.md> "Nvidia Background TOP")
    * Windows OS & Nvidia RTX GPU only.
  * [Nvidia Denoise TOP](<./Nvidia_Denoise_TOP.md> "Nvidia Denoise TOP")
    * Windows OS & Nvidia RTX GPU only.
  * [Nvidia Flex](<./Flex.md> "Flex")
    * Windows OS & Nvidia GPU only
  * [Nvidia Flow TOP](<./Nvidia_Flow_TOP.md> "Nvidia Flow TOP")
    * Windows OS & Nvidia GPU only
  * [Notch TOP](<./Notch_TOP.md> "Notch TOP") \- Playback Notch blocks 
    * Windows OS
  * [Optical Flow TOP](<./Optical_Flow_TOP.md> "Optical Flow TOP") \- detects patterns of motion in its input. 
    * Windows OS & Nvidia 3000 GPU or higher
  * [Scalable Display TOP](<./Scalable_Display_TOP.md> "Scalable Display TOP")
    * Windows OS
  * CUDA in [C++ TOP](<./CPlusPlus_TOP.md> "CPlusPlus TOP")
    * Windows OS & Nvidia GPU only
  * [DirectX In TOP](<./DirectX_In_TOP.md> "DirectX In TOP") and [DirectX Out TOP](<./DirectX_Out_TOP.md> "DirectX Out TOP")
    * Windows OS & DirectX 9.0 and higher
  * [Photoshop In TOP](<./Photoshop_In_TOP.md> "Photoshop In TOP")
    * Adobe Photoshop CS6 and up
  * [SVG TOP](<./SVG_TOP.md> "SVG TOP")
    * Windows OS & Nvidia GPU only
  * [Geometry COMP](<./Geometry_COMP.md> "Geometry COMP") Texture Instancing 
    * Windows OS & Nvidia GPU only
  * [Window COMP](<./Window_COMP.md> "Window COMP") Hardware Frame Lock 
    * Windows OS & Nvidia Quadro Sync or AMD S400 only
  * [Pangolin CHOP](<./Pangolin_CHOP.md> "Pangolin CHOP") \- Drive Pangolin lasers through their Beyond software. 
    * Windows OS
  * [RealSense CHOP](<./RealSense_CHOP.md> "RealSense CHOP") \- Skeleton and face tracking with old legacy RealSense devices. 
    * Windows OS
  * [Kinect](<./Kinect.md> "Kinect") 2 Support 
    * Windows OS - 8 or 10
    * dedicated USB 3.0 Controller
  * [Kinect Azure TOP](<./Kinect_Azure_TOP.md> "Kinect Azure TOP") / [Kinect Azure CHOP](<./Kinect_Azure_CHOP.md> "Kinect Azure CHOP") \- Body tracking and Player Index support 
    * Windows OS
    * Nvidia GPU is recommended, but AMD and Intel graphics cards are now supported. CPU-based option is too slow for most use cases.
  * [NatNet In CHOP](<./NatNet_In_CHOP.md> "NatNet In CHOP") \- Receives tracking data from OptiTrack systems. 
    * Windows OS
  * [Oculus Rift](<./Oculus_Rift.md> "Oculus Rift")
    * Windows OS
    * Oculus Rift DK2 or CV1
  * [OpenVR](<./OpenVR.md> "OpenVR") \- HTC Vive or other OpenVR supported HMDs. 
    * Windows OS
  * [ZED](<./ZED.md> "ZED") \- TOP, CHOP, POP and SOP that access ZED devices. 
    * Windows OS
