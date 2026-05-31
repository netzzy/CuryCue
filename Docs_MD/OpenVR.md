# OpenVR

OpenVR is an open standard for VR that is implemented and supported by Valve, and is the protocol used on the [HTC Vive](<https://en.wikipedia.org/wiki/HTC_Vive>) VR system, part of Valve Corporation's SteamVR project. 

HTC Vive is the first (and currently only) device that has been tested throughly with TouchDesigner. 

The [OpenVR TOP](<./OpenVR_TOP.md> "OpenVR TOP") outputs the left and right rendered images to an OpenVR device. 

The [OpenVR CHOP](<./OpenVR_CHOP.md> "OpenVR CHOP") supplies data for head tracking as well as data from the Vive's highly-accurate and responsive dual [Controllers](<http://www.vive.com/ca/accessory/controller/>) (all its buttons, trackpad, and position/rotation values) and [Tracker](<http://www.vive.com/ca/vive-tracker/>) accessories. 

### 

OpenVR support in TouchDesigner

OpenVR devices are accessed through the [OpenVR CHOP](<./OpenVR_CHOP.md> "OpenVR CHOP"), [OpenVR TOP](<./OpenVR_TOP.md> "OpenVR TOP"), and the [OpenVR SOP](<./OpenVR_SOP.md> "OpenVR SOP"). 

**NOTE** : It is also possible to run the controllers without the headset. 

They implement <https://github.com/ValveSoftware/openvr>. 
* [OpenVR CHOP](<./OpenVR_CHOP.md> "OpenVR CHOP") \- outputs positional data from the OpenVR SDK. You can choose between Sensor extrinsic data: for use as a transform matrix in a [Camera COMP](<./Camera_COMP.md> "Camera COMP"), Sensor intrinsic data: for use as a projection matrix in a [Camera COMP](<./Camera_COMP.md> "Camera COMP") for left and right eye or Controller/Tracker data: for positional and interaction channels from external controllers/trackers.
  * [OpenVR TOP](<./OpenVR_TOP.md> "OpenVR TOP") \- outputs the left and right images to an OpenVR device.
  * [OpenVR SOP](<./OpenVR_SOP.md> "OpenVR SOP") \- Holds OpenVR driver dependent models ie. a the model for an controller.

### 

Examples

There is a Vive Section in the [Category:Palette](<./Category-Palette.md> "Category:Palette") with basic elements for a OpenVR environment as well as a simple complete setup which can be used as a starting point to develop OpenVR based projects: gestureDraw, openVRRender, viveController, viveSimple, geoControlPanel. 

Prior example .toe and .tox files available here: [File:OpenVRExamples.zip](</File:OpenVRExamples.zip> "File:OpenVRExamples.zip")

### Tips for Working with OpenVR
* In [this video](<https://youtu.be/N9GoD_1FZ5I?t=7470>) Markus Heckmann walks through basic VR setup for Oculus including creating a scene, outputting to Oculus, and using 3D audio. Check the comments for a list of timestamps. **Note:** The workflow for Oculus works in the same way for OpenVR, simply substitute OpenVR operators in place of Oculus Rift operators.
