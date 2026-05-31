# Kinect1

This article contains information about the Kinect Version 1 device, for the newer Version 2 model see [Kinect 2 article](<./Kinect.md> "Kinect"). 

Microsoft Kinect1 can be used as an input device in TouchDesigner on Windows OS using the Kinect TOP and the Kinect CHOP. 

Kinect is a motion sensor input device from Microsoft. The device includes an infrared depth sensing camera, a RGB color camera, and a microphone array for audio capture. The Microsoft Kinect SDK enables features such as skeleton tracking, hand interactions, and voice recognition. 

The Kinect was originally released for Microsoft's Xbox360 gaming console in 2010. On Feb 1 2012, Microsoft released **Kinect for Windows** which included a Kinect SDK which works exclusively with new Kinect hardware for Windows operating systems. 

### 

Kinect Support in TouchDesigner

TouchDesigner has built-in support for Kinect using Microsoft's official Kinect for Windows SDK. As such, only Kinect for Windows hardware is supported by TouchDesigner's built-in Kinect operators. (See Tips below for information on Xbox 360 Kinect sensors) 

  
**Requirements**
* **Kinect for Windows** hardware device model 1517 (no 'official support' for Kinect for Xbox360 devices models 1414 and 1473, see below)
  * Install the [Kinect Runtime 1.8](<http://www.microsoft.com/en-us/download/details.aspx?id=40277>) or [Kinect for Windows SDK 1.8](<http://www.microsoft.com/en-us/download/details.aspx?id=40278>)


  
**Ways to interface with Kinect in TouchDesigner**
* Depth camera - [Kinect TOP](<./Kinect_TOP.md> "Kinect TOP")
  * RGB camera - [Kinect TOP](<./Kinect_TOP.md> "Kinect TOP")
  * Infrared camera - [Kinect TOP](<./Kinect_TOP.md> "Kinect TOP")
  * Skeleton Point Tracking - [Kinect CHOP](<./Kinect_CHOP.md> "Kinect CHOP") **NOTE** : For joint orientation and bone hierarchy, see: [Kinect Hierarchy](<http://msdn.microsoft.com/en-us/library/hh973073.aspx>)
  * Hand Interaction - [Kinect CHOP](<./Kinect_CHOP.md> "Kinect CHOP")
  * Microphone Array Audio Capture - [Audio Device In CHOP](<./Audio_Device_In_CHOP.md> "Audio Device In CHOP")
  * To control the tilt of the camera, use the Tscript`kinecttilt`Command

### 

Tips for Working with Kinect Sensors
* Always connect the AC power supply that comes with the Kinect sensor. The green LED will light up under USB power, however the sensor will not function correctly unless the AC power supply is also connected.
  * Kinect V1 can be less stable on USB3.0 ports, try USB2.0 ports if you are experiencing problems connecting tot he device or the connection drops out after some time.
  * If using multiple Kinects, each Kinect sensor must be connected to its own USB controller. On some computers multiple USB ports will be on the same USB controller, this will cause problems if two Kinects are sharing that same controller. Refer to your computer's Device Manager to inspect which ports belong to each USB controller.
  * If you require USB extenders, we have successfully used these extenders with Kinect sensors and other USB cameras. [25M USB Active Extenders](<http://www.monoprice.com/products/product.asp?c_id=103&cp_id=10303&cs_id=1030312&p_id=7644&seq=1&format=2>) Note that these extenders do not work if you connect two together.
  * **Xbox360 (models 1414 and 1473)** , although not officially supported, usually work by installing the [Kinect for Windows SDK 1.8](<http://www.microsoft.com/en-us/download/details.aspx?id=40278>). The Kinect Runtime 1.8 will NOT work with the Xbox360 models and they will not be detected, the full SDK must be installed.
  * For additional support and troubleshooting refer to the [Kinect Support Community](<http://www.microsoft.com/en-us/kinectforwindows/develop/community_support.aspx>).

### 

Kinect Example Files

[File:Kinect.tox](</File:Kinect.tox> "File:Kinect.tox") \- This file uses the depth camera, color camera, and skeletal tracking features of Kinect.
