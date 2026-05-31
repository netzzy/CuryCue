# Kinect

This article contains information about the Kinect 2 device. See [Kinect1](<./Kinect1.md> "Kinect1") for the original Kinect.   
  
See the [Kinect Azure TOP](<./Kinect_Azure_TOP.md> "Kinect Azure TOP") for the latest functionality. 

Microsoft Kinect2 can be used as an input device in TouchDesigner on Windows OS using the [Kinect TOP](<./Kinect_TOP.md> "Kinect TOP") and the [Kinect CHOP](<./Kinect_CHOP.md> "Kinect CHOP"). 

Kinect is a motion sensor input device from Microsoft. The device includes an infrared depth sensing camera, a RGB color camera, and a microphone array for audio capture. The Microsoft Kinect SDK enables features such as skeleton tracking, hand interactions, and voice recognition. 

The Kinect2 was originally released for Microsoft's Xbox One gaming console in 2013. In 2014, Microsoft released **Kinect 2 for Windows** which included a Kinect SDK which works exclusively with new Kinect hardware for Windows operating systems. 

### 

Kinect 2 Support in TouchDesigner

TouchDesigner has built-in support for Kinect using Microsoft's official Kinect for Windows SDK. As such, only Kinect for Windows hardware is supported by TouchDesigner's built-in Kinect operators. 

  
**Requirements**
* Windows 8 or 10 operating system.
  * **Kinect for Windows** hardware device. Only compatible with Kinect for Xbox One devices if the extra compatibility dongle is purchased from Microsoft.
  * Install the [Kinect SDK 2.0](<http://www.microsoft.com/en-us/download/details.aspx?id=44561>)


  
**Ways to interface with Kinect in TouchDesigner**
* Depth camera - [Kinect TOP](<./Kinect_TOP.md> "Kinect TOP")
  * RGB camera - [Kinect TOP](<./Kinect_TOP.md> "Kinect TOP")
  * Infrared camera - [Kinect TOP](<./Kinect_TOP.md> "Kinect TOP")
  * Skeleton Point Tracking - [Kinect CHOP](<./Kinect_CHOP.md> "Kinect CHOP")
  * Hand Interaction - [Kinect CHOP](<./Kinect_CHOP.md> "Kinect CHOP")
  * Microphone Array Audio Capture - [Audio Device In CHOP](<./Audio_Device_In_CHOP.md> "Audio Device In CHOP")

### 

Tips for Working with Kinect Sensors
* As of the writing of this article, Microsoft has not added support for accessing multiple Kinect 2 devices on a the same system.
  * For additional support and troubleshooting refer to the [Kinect Support Community](<http://social.msdn.microsoft.com/Forums/en-US/home?category=kinectsdks>).
