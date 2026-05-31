# Orbbec

[Orbbec](<https://www.orbbec.com/>) is a developer and manufacturer of 3D cameras and other sensors that can be used within TouchDesigner. Orbbec produces [multiple product lines](<https://www.orbbec.com/products/>) that rely on different 3D technologies such as stereo vision, structured light, or time of flight (TOF) to produce a depth maps and point clouds. Depending on the model, these cameras can use either USB or ethernet (include POE) and are supported on Windows and/or OSX. In [coordination with Microsoft](<https://www.orbbec.com/news/orbbec-announces-family-of-products-based-on-microsoft-itof-depth-technology/>), Orbbec also produces multiple cameras that include the same hardware sensors as the Kinect Azure and are compatible with the Microsoft body tracking system. 

### Orbbec TOP / Orbbec Select TOP

The [Orbbec TOP](<./Orbbec_TOP.md> "Orbbec TOP") and [Orbbec Select TOP](<./Orbbec_Select_TOP.md> "Orbbec Select TOP") can be used to stream video data (color, depth & point cloud) from a wide range of Orbbec cameras including the Femto, Gemini and Astra product lines. The TOPs use the Orbbec SDK and a complete list of compatible cameras can be found [here](<https://www.orbbec.com/developers/orbbec-sdk/>). Some models connect via USB, other models connect via PoE Ethernet. 

In TouchDesigner, the Orbbec TOP is used to connect to and configure the camera and can output one video stream. To obtain additional video streams, the [Orbbec Select TOP](<./Orbbec_Select_TOP.md> "Orbbec Select TOP") can be linked to the primary [Orbbec TOP](<./Orbbec_TOP.md> "Orbbec TOP"). An [Info CHOP](<./Info_CHOP.md> "Info CHOP") can also be connected to obtain IMU data on supported devices. 

### Kinect Azure TOP / Kinect Azure CHOP / Kinect Azure Select TOP

Compatible cameras (including the [Femto Mega](<https://www.orbbec.com/products/tof-camera/femto-mega/>) and [Femto Bolt](<https://www.orbbec.com/products/tof-camera/femto-bolt/>)) share internal hardware with the Microsoft Kinect Azure and can be used directly by the [Kinect Azure TOP](<./Kinect_Azure_TOP.md> "Kinect Azure TOP") and [Kinect Azure Select TOP](<./Kinect_Azure_Select_TOP.md> "Kinect Azure Select TOP") in place of original Microsoft devices. You can utilize these cameras by switching the 'Hardware' parameter on the Kinect Azure TOP to 'Orbbec'. By using the Kinect Azure node with the Orbbec camera, you can make use of the Microsoft body tracking library and obtain skeleton player index data. **Notes:** The Kinect Azure node does not automatically support the Femto Mega's ethernet connection; however, you can enable this feature by placing a config file alongside your toe file. See the [Orbbec docs](<https://www.orbbec.com/documentation-mega/k4a-access-femtomega-network-mode/>) for more info. Also note, using the Orbbec TOP and Kinect Azure TOP in the same project can cause instabilities. If you are only using the depth or color camera images, it is recommended to use the Orbbec TOP directly. 

### Usage Recommendations

It is not recommended to use the Kinect and native Orbbec nodes together in the same project. If you need to use skeleton tracking (player index or Kinect Azure CHOP), then you should only use Kinect Azure nodes to access the Orbbec cameras. If you do not need skeleton tracking, use the native Orbbec nodes.
