# RealSense

RealSense is a tracking device from Intel. TouchDesigner acquires multiple data streams from Intel RealSense devices using the [RealSense TOP](<./RealSense_TOP.md> "RealSense TOP") and [RealSense CHOP](<./RealSense_CHOP.md> "RealSense CHOP").   
  
The [RealSense TOP](<./RealSense_TOP.md> "RealSense TOP") uses the [Intel librealsense API](<https://github.com/IntelRealSense/librealsense>), which provides cross platform support for all camera models. The [RealSense CHOP](<./RealSense_CHOP.md> "RealSense CHOP") uses the [Cubemos RealSense Skeleton Tracking API](<https://www.intelrealsense.com/skeleton-tracking/>) to provide skeleton tracking data. **Note:** the RealSense CHOP is now deprecated as licenses for the skeleton tracking SDK are no longer available from Cubemos. 

**NOTE:** The [librealsense SDK v2.50.0](<https://github.com/IntelRealSense/librealsense/releases>) does not look like it will be updated for Apple Silicon, so it is not an option to add to these builds. 

## RealSense TOP

The [RealSense TOP](<./RealSense_TOP.md> "RealSense TOP") node outputs color, depth and IR data in various forms. 

Various data streams can be captured by the RealSense TOP: 
1. **Color** , which is the video from the RealSense camera color sensor.
  2. **Depth** , a calculation of the depth of each pixel. 0 means the pixel is 0 meters from the camera and 1 means the pixel is the maximum distance or more from the camera.
  3. **Raw Depth** , values taken directly from the RealSense camera SDK. Once again 0 means 1 meter from the camera and 1 is the maximum range or more away from the camera.
  4. **Visualized Depth** , a gray scale image from the RealSense SDK which can help you visualize the depth but it cannot be used to actually determine a pixel’s exact distance from the camera.
  5. **Depth To Color UV Map** , the UV values from a 32 bit floating RG texture (note, no blue) that are needed to remap the depth image to line up with the color image. You can use the Remap TOP node to align the images to match.
  6. **Color To Depth UV Map** , the UV values from a 32 bit floating RG texture (note, no blue) that are needed to remap the color image to line up with the depth image. You can use the Remap TOP node to align the two.
  7. **Infrared** , the raw video from the infrared sensor of the RealSense camera.
  8. **Point cloud** , literally a cloud of points in 3d space (X, Y, Z coordinates) or data points created by the scanner of the RealSense Camera.
  9. **Point Cloud Color UVs** which can be used to get each point’s color from the Color image stream.
  10. **Segmented Color (with Alpha)** which outputs masked color image of the detected person in front of the camera.
  11. **IMU/SLAM Tracking** With the T265 model, the positional data of where the camera is in space can be retrieved using the [Info CHOP](<./Info_CHOP.md> "Info CHOP").


See the point cloud sample at: [http://www.derivative.ca/Forum/viewtopic.php?f=22&t=7977](<http://www.derivative.ca/Forum/viewtopic.php?f=22&t=7977>)

### Supported Devices

Currently the [RealSense TOP](<./RealSense_TOP.md> "RealSense TOP") supports the following RealSense devices: 
* F200
  * R200
  * ZR300
  * SR300
  * D405
  * D415
  * D435
  * D435i
  * D455
  * D455f
  * D456
  * D555

## RealSense CHOP

**DEPRECATED:** Skeleton tracking features no longer licensable by Cubemos. 

The [RealSense CHOP](<./RealSense_CHOP.md> "RealSense CHOP") references a [RealSense TOP](<./RealSense_TOP.md> "RealSense TOP") via parameter. The RealSense CHOP supports skeleton tracking on Windows. 

**Skeleton Tracking:** Performs [skeleton tracking](<https://www.intelrealsense.com/skeleton-tracking/>) using the referenced RealSense TOP's camera. Skeleton Tracking must be enabled on the RealSense TOP. 

The [RealSense CHOP](<./RealSense_CHOP.md> "RealSense CHOP") supports skeleton tracking through the [Cubemos RealSense Skeleton Tracking API](<https://www.intelrealsense.com/skeleton-tracking/>). The API requires a license to use in TouchDesigner. A full license can be purchased [here](<https://www.intelrealsense.com/skeleton-tracking>); a trial license is also available. Installing the SDK is required to setup the license file. After installation of the SDK, the license can be setup with the`post_installation.bat`script in the Cubemos/SkeletonTracking/scripts directory. A model file (`.cubemos`) is also required for the skeleton tracking, two of which are packaged with the Cubemos Skeleton Tracking SDK, located in the`Cubemos/SkeletonTracking/models/skeleton-tracking`folder. 

## Installing Required Software

#### Camera Firmware

The [RealSense TOP](<./RealSense_TOP.md> "RealSense TOP") does *not* require drivers to be installed, but does require that the correct firmware is installed on the device. You can do this by installing the RealSense SDK from here: <https://github.com/IntelRealSense/librealsense/releases> Then use the Camera Viewer tool to update the firmware to the recommended version. 

The firmware downloads are available here: <https://dev.intelrealsense.com/docs/firmware-releases>

The 2025.30000 series uses SDK version 2.56.5. <https://github.com/IntelRealSense/librealsense/releases/tag/v2.56.5>

  
See [RealSense CHOP](<./RealSense_CHOP.md> "RealSense CHOP"), [RealSense TOP](<./RealSense_TOP.md> "RealSense TOP")
