# Meta VR

## Oculus Rift and Meta Quest

TouchDesigner supports several VR headsets from Meta including the Meta Quest and Oculus Rift through the [Oculus Rift TOP](<./Oculus_Rift_TOP.md> "Oculus Rift TOP") and [Oculus Rift CHOP](<./Oculus_Rift_CHOP.md> "Oculus Rift CHOP"). 

Download three demos files: [File:OculusRiftCV1Demos.zip](</File:OculusRiftCV1Demos.zip> "File:OculusRiftCV1Demos.zip")

### Meta VR support in TouchDesigner

TouchDesigner has built-in support for Meta headsets through the [Oculus Rift TOP](<./Oculus_Rift_TOP.md> "Oculus Rift TOP") and [Oculus Rift CHOP](<./Oculus_Rift_CHOP.md> "Oculus Rift CHOP"). Both operators have a **Device** parameter to support using multiple devices connected to one machine. 

**Requirements**
* [VR hardware](<https://www.meta.com/quest/>)
  * Setup headset device: [Setup Headset](<https://www.meta.com/quest/setup/>)


**Ways to interface with Meta headsets in TouchDesigner**
* [Oculus Rift CHOP](<./Oculus_Rift_CHOP.md> "Oculus Rift CHOP") \- Outputs several sets of channels such as orientation, left and right eye camera positions, acceleration and left and right eye projection matrices.
  * [Oculus Rift TOP](<./Oculus_Rift_TOP.md> "Oculus Rift TOP") \- Outputs the left and right images to the headset device.

### Getting Started

The demos list above are a good starting point for developing for Meta headsets. 

For Oculus devices, first ensure that the headset is configured to use the 'Extend Desktop to the HMD' display mode. This can be selected from the Oculus Configuration Utility under the Tools->Rift Display Mode menu. Direct HMD rendering is not supported for OpenGL applications yet. Once the Oculus is appearing as an extra monitor in your OS you need to ensure it has the correct orientation. By default it shows up as 'Portrait' but our tests have shown that the correct orientation is 'Landscape (Flipped)'. Use the 'Show Demo Scene' button in the Oculus Configuration Utility to test and ensure the display is setup correctly. Once the Oculus is working correctly for the demo scene in 'Extend Desktop Mode', it should also work correctly for TouchDesigner. 

For Meta Quest devices, enable PC Link. This can be done within the Quest headset by going to Settings -> Link -> Link toggle. You can connect your Quest device to your PC through a physical Link cable or Air Link which uses your local Wi-Fi network. If your PC is connected to your headset, you should see the PC under Settings -> Link -> Launch -> Available PCs. Once PC Link is enabled and a PC is connected to your headset, launch Link. 

#### Refresh Rate Issues

Most desktop monitors run at 60hz, but Meta headsets may run at a different refresh rate depending on the model. For example, the Oculus Rift S runs at 80hz and the Oculus Rift DV1 runs at 90hz. Windows may not feed the Oculus 80/90hz data if there are TouchDesigner windows redrawing on the 60hz monitor. If possible, set all your monitors to run at 90hz. However, many monitors don't support that. Going into perform mode with your window and ensuring the 'Redraw' parameter is off avoids this issue. In addition, V-Sync Mode in the perform Window COMP should be disabled. 

### Oculus Rift CHOP

The [Oculus Rift CHOP](<./Oculus_Rift_CHOP.md> "Oculus Rift CHOP") provides two main sets of data. Each eye's camera render position via a transform matrix as 16 CHOP channels. The other set of data is each eye's projection matrix also as 16 CHOP channels. These two matrices can be used directly in the Camera COMP using the CHOP/DAT Matrix parameters for the Pre-XForm and Projection Matrix. 

### Tips for Working with Meta headsets
* In [this video](<https://youtu.be/N9GoD_1FZ5I?t=7470>) Markus Heckmann walks through basic VR setup for Oculus including creating a scene, outputting to Oculus, and using 3D audio. Check the comments for a list of timestamps.
  * For additional support and troubleshooting refer to the [Meta Community forum](<https://communityforums.atmeta.com/>).
