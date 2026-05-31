# Ouster

[Ouster](<https://www.ouster.io>) makes LIDAR devices for scanning 3D environments with lasers. TouchDesigner supports real-time point cloud capture and recording with the Ouster LIDAR sensors running firmware 2.0+. (Firmware 3.x is not currently supported). Ouster data can be manipulated live with TouchDesigner’s procedural node-based tools and TouchDesigner features that support working with point cloud data on the GPU. 

[![](./images/thumb/1/13/OusterOS1.jpg/200px-OusterOS1.jpg)](</File:OusterOS1.jpg>)

[](</File:OusterOS1.jpg> "Enlarge")

Ouster OS1

### Ouster Features Supported in TouchDesigner
* TouchDesigner provides direct support for the full Ouster product line. Sensors must run firmware 2.0 or higher.
  * Capture formats include visual Panoramic and Scan Order formats.
  * X, Y, Z, Range, Intensity and Noise planes are flexibly mapped to RGBA image channels on the GPU.
  * Additional sensor data includes IMU (Inertial Measurement Unit gyroscope and accelerometer), packet counts and matrices.
  * Time Sync Mode supports multiple devices in the same area (Internal OSC, Sync Pulse In, PTP 1588). Auto startup features, window rejection mode are supported.

### Point Cloud Features in TouchDesigner Boost Data Manipulation
* TouchDesigner can capture in real-time all 7+ channels of the Ouster's 32-bit floating point data streams.
  * Buffer select operations provide an easy way to extract device channels and manipulate them on the GPU with procedural node-based tools that minimize or eliminate the need for coding.
  * The captured point data can be viewed as 3D point clouds or 2D arrays in any [TOP](<./TOP.md> "TOP") viewer.
  * RGBA Normalized viewer mode provides a way to see channel data in a normalized luminance space for easy viewing and inspecting of 32-bit data.
  * Points can be rendered with the [Line Material](<./Line_MAT.md> "Line MAT"), controlling point size based on distance to camera.
  * The enhancing instancing engine provides a method for directly mapping point cloud data from TOPs into 3D camera renders. The instancer accepts a different 32bit RGBA texture for each attribute class.
  * TouchDesigner can record Ouster streams as a sequence of OpenEXR files to storage in real-time. It can record unlimited channels of 32-bit floating point data along with customizable header data for storing IMU and other meta information. This can be played back in real-time.


See: [Ouster TOP](<./Ouster_TOP.md> "Ouster TOP"), [Ouster Select TOP](<./Ouster_Select_TOP.md> "Ouster Select TOP"), [Point File In TOP](<./Point_File_In_TOP.md> "Point File In TOP"), [Movie File Out TOP](<./Movie_File_Out_TOP.md> "Movie File Out TOP").
