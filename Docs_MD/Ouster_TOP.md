# Ouster TOP

##   
  
Summary

**NOTE**

**License:** Only available in [TouchDesigner Educational](<./TouchDesigner_Educational.md> "TouchDesigner Educational"), [TouchDesigner Commercial](<./TouchDesigner_Commercial.md> "TouchDesigner Commercial") and [TouchDesigner Pro](<./TouchDesigner_Pro.md> "TouchDesigner Pro"). 

[Ouster](<./Ouster.md> "Ouster") makes LIDAR devices for scanning 3D environments. The Ouster TOP sends and receives data with an Ouster Imaging Lidar, converting to point cloud data on the GPU. For more information see the user guides at [Ouster.io](<https://www.ouster.io/resources>)

**Requirements:**
* The TOP currently supports Ouster devices using version 2.x firmware. Devices that require version 3 firmware are not currently supported.
  * Access to your local network to connect with the sensor device. Check your firewall settings if you have trouble accessing the device.
  * High resolution scanning modes require up to 130Mbps of bandwidth. Gigabit Ethernet hardware is required for full operation. Insufficient bandwidth will cause broken images and missing frames.


**Features include:**
* Additional sensor data like IMU (Inertial Measurement Unit - the gyroscope and accelerometer), packet counts, matrices via Info CHOP and Info DAT.
  * Visual Panoramic and Scan Order capture formats selectable in 'Image Layout' parameter.
  * Flexible X, Y, Z, Range, Intensity and Noise plane mapping to RGBA GPU Image Channels
  * Time Sync Mode for supporting multiple devices in the same area (Internal OSC, Sync Pulse In, PTP 1588)
  * Auto startup features


**Connection Instructions:**  
To connect to the sensor, you will need either the IP addressed assigned by the local DHCP server or the name of the device. The name is based on the serial number that is usually printed on the top of the sensor in the format "os-############". This name can be entered directly into the Device Address parameter (see parameter help below). You can also connect to the device through a web browser using the IP or name in the format`<http://os-###########/>`. The web interface allows you to check the status of the device and gives additional error information. 

Once the device is configured, it will continue to send output to the target IP address so it is not required to enter the device address again unless you need to change the configuration. 

Range data collected from the device is presented as 32bit floating point values in the RGBA channels of the output image. Output can be arranged either in chronological scan order or as a panoramic image using the Image Layout parameter. IMU data from the device can be accessed by connecting an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). If more than 4 output channels are needed, you can use a [Ouster Select TOP](<./Ouster_Select_TOP.md> "Ouster Select TOP") to create additional output images. 

**Note:** All 3D coordinates are transformed into TouchDesigner space where Y is up and X and Z represent the ground plane. This is different from the original coordinate space defined in the Ouster documentation. 

The lookup tables used to convert the range values into 3D points can be accessed with an [Info DAT](<./Info_DAT.md> "Info DAT"). 

See also: [Ouster Select TOP](<./Ouster_Select_TOP.md> "Ouster Select TOP")

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[ousterTOP_Class](<./OusterTOP_Class.md> "OusterTOP Class")

## 

Parameters - Connection Page

Active`active`\- Enables connections with the device. 

Device Address`deviceaddress`\- The IP address or the name of the Ouster device. The address is only required during configuraton. The device will request an address from the local DHCP server when it is connected to the network. The name of the device is printed on the top of the sensor in the format "os-#####", where ##### is the serial number e.g. "os-991900123456". You can determine the IP address using the ping command and the device name e.g. ping -4 os-991900123456. For more information see the Ouster User Guide at [Ouster.io](<https://www.ouster.io/downloads>). 

Lidar Port`lidarport`\- The UDP port number to receive lidar data. 

IMU Port`imuport`\- The UDP port number to receive data from the inertial measurement unit (IMU) on the device. The IMU data can be accessed by connecting the Ouster TOP to an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). 

Command Port`commandport`\- The TCP/IP port number to use to send configuration commands to the device. 

Target Address`targetaddress`\- The IP address where the sensor should send the lidar and IMU data to. If the parameter is blank, the address of the current machine will be used. This field should only be necessary if the sending machine has more than one IP address or if you wish to send the lidar data to a different machine than the one you are configuring it on. 

Local Address`localaddress`\- An IP address for the current machine that should be used to connect to the device with. If the address is left blank, the default network address will be used. 

Scan Mode`scanmode`\- ⊞ \- Select a scanning mode to set the sensor's horizontal resolution and number of revolutions per second. The vertical resolution is determined by the hardware e.g. an OS1-64 sensor has vertical resolution of 64 pixels (samples). 
* 512 x 10Hz`mode512x10`-
* 512 x 20Hz`mode512x20`-
* 1024 x 10Hz`mode1024x10`-
* 1024 x 20Hz`mode1024x20`-
* 2048 x 10Hz`mode2048x10`-


Configure Device`configdevice`\- Enable this toggle to have the Ouster TOP set the configuration properties of the device. If the device has already been configured to the correct mode and network connections than this can be disabled to save some processing time. 

## 

Parameters - Output Page

The Output page allows you to select what data is placed in the TOP's output image. Range, Intensity, Reflectivity and Noise are raw data channels coming from the sensor, while XYZ position values are calculated by using the range data and the look up table of beam azimuth and altitude angles. Range is measured in millimeters, while XYZ positions are in meters. If you need more than 4 channels of data, use a [Ouster Select TOP](<./Ouster_Select_TOP.md> "Ouster Select TOP") to create a second output image from the same sensor data. 

In addition to the sensor data, you can also assign a constant value of one or zero to a channel by selecting the corresponding entry from the menu. Selecting 'Active Mask' from the channel menu will output a one if the pixel represents valid sensor data or a zero if it is padding (when the image contains more pixels than there is available sensor data). The mask channel can be used in the [Geometry COMP](<./Geometry_COMP.md> "Geometry COMP") Active instance channel to control which points are used for instancing. 

Image Layout`layout`\- ⊞ \- Use this parameter to determine how data is arranged in the output image. The layout of data is generally not important when used as a point cloud. 
* Scan Order`pointcloud`\- Sensor data is arranged chronologically in a square texture according to when it was received by the scanner. If there are fewer points than pixels in the image, the remaining pixels are filled with the floating point value NaN.
* Panoramic`image`\- In panoramic mode, the samples are arranged to form a continuous picture of the area around the sensor.


Red`redchannel`\- ⊞ \- Select what sensor data will be placed into the red channel of the output image. 
* X`x`-
* Y`y`-
* Z`z`-
* Range`range`-
* Intensity`intensity`-
* Reflectivity`reflectivity`-
* Noise`noise`-


Green`greenchannel`\- ⊞ \- Select what sensor data will be placed into the green channel of the output image. 
* X`x`-
* Y`y`-
* Z`z`-
* Range`range`-
* Intensity`intensity`-
* Reflectivity`reflectivity`-
* Noise`noise`-


Blue`bluechannel`\- ⊞ \- Select what sensor data will be placed into the blue channel of the output image. 
* X`x`-
* Y`y`-
* Z`z`-
* Range`range`-
* Intensity`intensity`-
* Reflectivity`reflectivity`-
* Noise`noise`-


Alpha`alphachannel`\- ⊞ \- Select what sensor data will be placed into the alpha channel of the output image. 
* X`x`-
* Y`y`-
* Z`z`-
* Range`range`-
* Intensity`intensity`-
* Reflectivity`reflectivity`-
* Noise`noise`-

## 

Parameters - Timing Page

Time Sync Mode`timemode`\- ⊞ \- Select how the sensor generates timestamp information. 
* Internal OSC`internalosc`\- Timestamps are generated from an internal oscillator. This is the default setting.
* Sync Pulse In`syncpulsein`\- Timing is synced to pulses on the SYNC_PULSE_IN input.
* PTP 1588`ptp1588`\- Timing is synced to an external PTP master.


Sync Pulse In Polarity`pulseinpolarity`\- ⊞ \- The polarity of the SYNC_PULSE_IN signal to use. 
* Active Low`activelow`-
* Active High`activehigh`-


Multipurpose IO Mode`iomode`\- ⊞ \- Determines how the sensor uses the SYNC_PULSE_OUT signal. 
* Off`off`\- The signal is not used. This is the default setting.
* Input NMEA`inputnmea`\- The sensor will expect standard NMEA $GPRMC UART messages on the multipurpose IO port. See [here](<https://www.gpsworld.com/what-exactly-is-gps-nmea-data/>) for more information on GPS NMEA data.
* Output Internal OSC`outputinternalosc`\- Signal output is taken from the internal oscillator.
* Output Sync Pulse In`outputsyncpulsein`-
* Output PTP 1588`outputptp1588`-
* Output Encoder Angle`outputangle`\- Signal output is based on the angle of the encoder.


Sync Pulse Out Polarity`pulseoutpolarity`\- ⊞ \- Polarity of the output signal pulse. 
* Active Low`activelow`-
* Active High`activehigh`-


Sync Pulse Out Frequency`pulseoutfrequency`\- Frequency of the output pulse in Hz (must be greater than 0). 

Sync Pulse Out Angle`pulseoutangle`\- The encoder angle at which to output a signal pulse. Measured in degrees less than 360. 

Sync Pulse Out Width`pulseoutwidth`\- Width of the output signal pulse in mm. 

NMEA In Polarity`nmeainpolarity`\- ⊞ \- Sets the polarity of the NMEA URT input $GPRMC messages. Set to 'Active High' if UART is active high, idle low, and the start bit is after a falling edge. 
* Active Low`activelow`-
* Active High`activehigh`-


NMEA Ignore Valid Char`nmeaignorevalidchar`\- Turn off, if the NMEA UART input $GPRMC messages should be ignored if valid character is not set, and turn on if messages should be used for time syncing regardless of the valid character. 

NMEA Baud Rate`nmeabaudrate`\- ⊞ \- The baud rate for the incoming NMEA URT input $GPRMC messages. 
* Baud 9600`baud9600`-
* Baud 115200`baud115200`-


NMEA Leap Seconds`nmealeapseconds`\- An integer number of leap seconds that will be added to the UDP timestamp when calculating seconds since 00:00:00 Thursday, 1 Jan 1970. Set to 0 for Unix Epoch Time. 

## 

Parameters - Advanced Page

Auto Start`autostart`\- Tell the sensor to automatically begin sending data when it turns on. The default is On. 

## 

Parameters - Common Page

Output Resolution`outputresolution`\- ⊞ \- quickly change the resolution of the TOP's data. 
* Use Input`useinput`\- Uses the input's resolution
* Eighth`eighth`\- Multiply the input's resolution by that amount.
* Quarter`quarter`\- Multiply the input's resolution by that amount.
* Half`half`\- Multiply the input's resolution by that amount.
* 2X`2x`\- Multiply the input's resolution by that amount.
* 4X`4x`\- Multiply the input's resolution by that amount.
* 8X`8x`\- Multiply the input's resolution by that amount.
* Fit Resolution`fit`\- Grow or shrink the input resolution to fit this resolution, while keeping the aspect ratio the same.
* Limit Resolution`limit`\- Limit the input resolution to be not larger than this resolution, while keeping the aspect ratio the same.
* Custom Resolution`custom`\- Directly control the width and height.


Resolution`resolution`\- ⊞ \- Enabled only when the Resolution parameter is set to Custom Resolution. Some Generators like Constant and Ramp do not use inputs and only use this field to determine their size. The drop down menu on the right provides some commonly used resolutions. 
* W`resolutionw`-
* H`resolutionh`-


Resolution Menu`resmenu`\- A drop-down menu with some commonly used resolutions. 

Use Global Res Multiplier`resmult`\- Uses the Global Resolution Multiplier found in **Edit >Preferences>TOPs**. This multiplies all the TOPs resolutions by the set amount. This is handy when working on computers with different hardware specifications. If a project is designed on a desktop workstation with lots of graphics memory, a user on a laptop with only 64MB VRAM can set the Global Resolution Multiplier to a value of half or quarter so it runs at an acceptable speed. By checking this checkbox on, this TOP is affected by the global multiplier. 

Output Aspect`outputaspect`\- ⊞ \- Sets the image aspect ratio allowing any textures to be viewed in any size. Watch for unexpected results when compositing TOPs with different aspect ratios. (You can define images with non-square pixels using xres, yres, aspectx, aspecty where xres/yres != aspectx/aspecty.) 
* Use Input`useinput`\- Uses the input's aspect ratio.
* Resolution`resolution`\- Uses the aspect of the image's defined resolution (ie 512x256 would be 2:1), whereby each pixel is square.
* Custom Aspect`custom`\- Lets you explicitly define a custom aspect ratio in the Aspect parameter below.


Aspect`aspect`\- ⊞ \- Use when Output Aspect parameter is set to Custom Aspect. 
* Aspect1`aspect1`-
* Aspect2`aspect2`-


Aspect Menu`armenu`\- A drop-down menu with some commonly used aspect ratios. 

Input Smoothness`inputfiltertype`\- ⊞ \- This controls pixel filtering on the input image of the TOP. 
* Nearest Pixel`nearest`\- Uses nearest pixel or accurate image representation. Images will look jaggy when viewing at any zoom level other than Native Resolution.
* Interpolate Pixels`linear`\- Uses linear filtering between pixels. This is how you get TOP images in viewers to look good at various zoom levels, especially useful when using any Fill Viewer setting other than Native Resolution.
* Mipmap Pixels`mipmap`\- Uses [ mipmap](<./Mipmapping.md> "Mipmapping") filtering when scaling images. This can be used to reduce artifacts and sparkling in moving/scaling images that have lots of detail.


Fill Viewer`fillmode`\- ⊞ \- Determine how the TOP image is displayed in the viewer. 

**NOTE:** To get an understanding of how TOPs work with images, you will want to set this to **Native Resolution** as you lay down TOPs when starting out. This will let you see what is actually happening without any automatic viewer resizing. 
* Use Input`useinput`\- Uses the same Fill Viewer settings as it's input.
* Fill`fill`\- Stretches the image to fit the edges of the viewer.
* Fit Horizontal`width`\- Stretches image to fit viewer horizontally.
* Fit Vertical`height`\- Stretches image to fit viewer vertically.
* Fit Best`best`\- Stretches or squashes image so no part of image is cropped.
* Fit Outside`outside`\- Stretches or squashes image so image fills viewer while constraining it's proportions. This often leads to part of image getting cropped by viewer.
* Native Resolution`nativeres`\- Displays the native resolution of the image in the viewer.


Viewer Smoothness`filtertype`\- ⊞ \- This controls pixel filtering in the viewers. 
* Nearest Pixel`nearest`\- Uses nearest pixel or accurate image representation. Images will look jaggy when viewing at any zoom level other than Native Resolution.
* Interpolate Pixels`linear`\- Uses linear filtering between pixels. Use this to get TOP images in viewers to look good at various zoom levels, especially useful when using any Fill Viewer setting other than Native Resolution.
* Mipmap Pixels`mipmap`\- Uses [ mipmap](<./Mipmapping.md> "Mipmapping") filtering when scaling images. This can be used to reduce artifacts and sparkling in moving/scaling images that have lots of detail. When the input is 32-bit float format, only nearest filtering will be used (regardless of what is selected).


Passes`npasses`\- Duplicates the operation of the TOP the specified number of times. For every pass after the first it takes the result of the previous pass and replaces the node's first input with the result of the previous pass. One exception to this is the [GLSL TOP](<./GLSL_TOP.md> "GLSL TOP") when using compute shaders, where the input will continue to be the connected TOP's image. 

Channel Mask`chanmask`\- Allows you to choose which channels (R, G, B, or A) the TOP will operate on. All channels are selected by default. 

Pixel Format`format`\- ⊞ \- Format used to store data for each channel in the image (ie. R, G, B, and A). Refer to [Pixel Formats](<./Pixel_Formats.md> "Pixel Formats") for more information. 
* Use Input`useinput`\- Uses the input's pixel format.
* 8-bit fixed (RGBA)`rgba8fixed`\- Uses 8-bit integer values for each channel.
* sRGB 8-bit fixed (RGBA)`srgba8fixed`\- Uses 8-bit integer values for each channel and stores color in sRGB colorspace. Note that this does **not** apply an sRGB curve to the pixel values, it only stores them using an sRGB curve. This means more data is used for the darker values and less for the brighter values. When the values are read downstream they will be converted back to linear. For more information refer to [sRGB](<./SRGB.md> "SRGB").
* 16-bit float (RGBA)`rgba16float`\- Uses 16-bits per color channel, 64-bits per pixel.
* 32-bit float (RGBA)`rgba32float`\- Uses 32-bits per color channel, 128-bits per pixels.
* 10-bit RGB, 2-bit Alpha, fixed (RGBA)`rgb10a2fixed`\- Uses 10-bits per color channel and 2-bits for alpha, 32-bits total per pixel.
* 16-bit fixed (RGBA)`rgba16fixed`\- Uses 16-bits per color channel, 64-bits total per pixel.
* 11-bit float (RGB), Positive Values Only`rgba11float`\- A RGB floating point format that has 11 bits for the Red and Green channels, and 10-bits for the Blue Channel, 32-bits total per pixel (therefore the same memory usage as 8-bit RGBA). The Alpha channel in this format will always be 1. Values can go above one, but can't be negative. ie. the range is [0, infinite).
* 16-bit float (RGB)`rgb16float`-
* 32-bit float (RGB)`rgb32float`-
* 8-bit fixed (Mono)`mono8fixed`\- Single channel, where RGB will all have the same value, and Alpha will be 1.0. 8-bits per pixel.
* 16-bit fixed (Mono)`mono16fixed`\- Single channel, where RGB will all have the same value, and Alpha will be 1.0. 16-bits per pixel.
* 16-bit float (Mono)`mono16float`\- Single channel, where RGB will all have the same value, and Alpha will be 1.0. 16-bits per pixel.
* 32-bit float (Mono)`mono32float`\- Single channel, where RGB will all have the same value, and Alpha will be 1.0. 32-bits per pixel.
* 8-bit fixed (RG)`rg8fixed`\- A 2 channel format, R and G have values, while B is 0 always and Alpha is 1.0. 8-bits per channel, 16-bits total per pixel.
* 16-bit fixed (RG)`rg16fixed`\- A 2 channel format, R and G have values, while B is 0 always and Alpha is 1.0. 16-bits per channel, 32-bits total per pixel.
* 16-bit float (RG)`rg16float`\- A 2 channel format, R and G have values, while B is 0 always and Alpha is 1.0. 16-bits per channel, 32-bits total per pixel.
* 32-bit float (RG)`rg32float`\- A 2 channel format, R and G have values, while B is 0 always and Alpha is 1.0. 32-bits per channel, 64-bits total per pixel.
* 8-bit fixed (A)`a8fixed`\- An Alpha only format that has 8-bits per channel, 8-bits per pixel.
* 16-bit fixed (A)`a16fixed`\- An Alpha only format that has 16-bits per channel, 16-bits per pixel.
* 16-bit float (A)`a16float`\- An Alpha only format that has 16-bits per channel, 16-bits per pixel.
* 32-bit float (A)`a32float`\- An Alpha only format that has 32-bits per channel, 32-bits per pixel.
* 8-bit fixed (Mono+Alpha)`monoalpha8fixed`\- A 2 channel format, one value for RGB and one value for Alpha. 8-bits per channel, 16-bits per pixel.
* 16-bit fixed (Mono+Alpha)`monoalpha16fixed`\- A 2 channel format, one value for RGB and one value for Alpha. 16-bits per channel, 32-bits per pixel.
* 16-bit float (Mono+Alpha)`monoalpha16float`\- A 2 channel format, one value for RGB and one value for Alpha. 16-bits per channel, 32-bits per pixel.
* 32-bit float (Mono+Alpha)`monoalpha32float`\- A 2 channel format, one value for RGB and one value for Alpha. 32-bits per channel, 64-bits per pixel.

## 

Info CHOP Channels

Extra Information for the Ouster TOP can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). 

### 

Specific Ouster TOP Info Channels
* num_lidar_packets \- The number of lidar packets received by the TOP. Each packet contains 16 vertical columns of samples.
* missing_lidar_packets \- The number of lidar packets that were missing if a new frame is detected before the last frame was complete.
* skipped_lidar_packets \- The number of lidar packets that were skipped if a packet is not the next expected one in the sequence.
* num_imu_packets \- The number of IMU packets received by the TOP. Each packet contains one set of gyro and accelerometer readings.
* num_command_packets \- The number of configuration packets received from the device. Command packets are used to set parameters and to check the device's status.
* command_state \- The internal state of the Ouster TOP used for debugging. 0 is offline, 1 is connected, 4 is error.
* frame_id \- This number increases by 1 each time the sensor completes a full revolution.
* frame_start_time \- The time frame started in nanoseconds since the device was booted.
* beam_angles_state \- 1 if the TOP has received a complete set of beam altitude and azimuth angles from the device. Defaults to 0.
* imu_transform_state \- 1 if the TOP has received a complete IMU transform from the device. Defaults to 0.
* lidar_transform_state \- 1 if the TOP has received a complete lidar transform from the device. Defaults to 0.
* imu_read_time \- The time the measurement was take in nanoseconds since the device was booted.
* accel_read_time \- The time the accelerometer measurement was take in nanoseconds relative to the current timestamp mode (see Ouster User Guide).
* gyro_read_time \- The time the gyroscope measurement was take in nanoseconds relative to the current timestamp mode (see Ouster User Guide)
* accel_tx \- Acceleration in the x-axis (g)
* accel_ty \- Acceleration in the y-axis (g)
* accel_tz \- Acceleration in the z-axis (g)
* vel_rx \- Angular velocity around the x-axis (deg per sec)
* vel_ry \- Angular velocity around the y-axis (deg per sec)
* vel_rz \- Angular velocity around the z-axis (deg per sec)
* lidar_m00 -
* lidar_m10 -
* lidar_m20 -
* lidar_m30 -
* lidar_m01 -
* lidar_m11 -
* lidar_m21 -
* lidar_m31 -
* lidar_m02 -
* lidar_m12 -
* lidar_m22 -
* lidar_m32 -
* lidar_m03 -
* lidar_m13 -
* lidar_m23 -
* lidar_m33 -
* imu_m00 -
* imu_m10 -
* imu_m20 -
* imu_m30 -
* imu_m01 -
* imu_m11 -
* imu_m21 -
* imu_m31 -
* imu_m02 -
* imu_m12 -
* imu_m22 -
* imu_m32 -
* imu_m03 -
* imu_m13 -
* imu_m23 -
* imu_m33 -

### 

Common TOP Info Channels
* resx \- Horizontal resolution of the TOP in pixels.
* resy \- Vertical resolution of the TOP in pixels.
* aspectx \- Horizontal aspect of the TOP.
* aspecty \- Vertical aspect of the TOP.
* depth \- Depth of 2D or 3D array if this TOP contains a 2D or 3D texture array.
* gpu_memory_used \- Total amount of texture memory used by this TOP.

### 

Common Operator Info Channels
* total_cooks \- Number of times the operator has cooked since the process started.
* cook_time \- Duration of the last cook in milliseconds.
* cook_frame \- Frame number when this operator was last cooked relative to the component timeline.
* cook_abs_frame \- Frame number when this operator was last cooked relative to the absolute time.
* cook_start_time \- Time in milliseconds at which the operator started cooking in the frame it was cooked.
* cook_end_time \- Time in milliseconds at which the operator finished cooking in the frame it was cooked.
* cooked_this_frame \- 1 if operator was cooked this frame.
* warnings \- Number of warnings in this operator if any.
* errors \- Number of errors in this operator if any.


  
TouchDesigner Build: Latest\nwikieditorwikieditor2022.241402021.100002020.20000before 2020.20000

TOPs   
---  
[Add ](<./Add_TOP.md> "Add TOP")• [Analyze ](<./Analyze_TOP.md> "Analyze TOP")• [Anti Alias ](<./Anti_Alias_TOP.md> "Anti Alias TOP")• [Blob Track ](<./Blob_Track_TOP.md> "Blob Track TOP")• [Bloom ](<./Bloom_TOP.md> "Bloom TOP")• [Blur ](<./Blur_TOP.md> "Blur TOP")• [Cache Select ](<./Cache_Select_TOP.md> "Cache Select TOP")• [Cache ](<./Cache_TOP.md> "Cache TOP")• [Channel Mix ](<./Channel_Mix_TOP.md> "Channel Mix TOP")• [CHOP to ](<./CHOP_to_TOP.md> "CHOP to TOP")• [Chroma Key ](<./Chroma_Key_TOP.md> "Chroma Key TOP")• [Circle ](<./Circle_TOP.md> "Circle TOP")• [Composite ](<./Composite_TOP.md> "Composite TOP")• [Constant ](<./Constant_TOP.md> "Constant TOP")• [Convolve ](<./Convolve_TOP.md> "Convolve TOP")• [Corner Pin ](<./Corner_Pin_TOP.md> "Corner Pin TOP")• [CPlusPlus ](<./CPlusPlus_TOP.md> "CPlusPlus TOP")• [Crop ](<./Crop_TOP.md> "Crop TOP")• [Cross ](<./Cross_TOP.md> "Cross TOP")• [Cube Map ](<./Cube_Map_TOP.md> "Cube Map TOP")• [Depth ](<./Depth_TOP.md> "Depth TOP")• [Difference ](<./Difference_TOP.md> "Difference TOP")• [Direct Display Out ](<./Direct_Display_Out_TOP.md> "Direct Display Out TOP")• [DirectX In ](<./DirectX_In_TOP.md> "DirectX In TOP")• [DirectX Out ](<./DirectX_Out_TOP.md> "DirectX Out TOP")• [Displace ](<./Displace_TOP.md> "Displace TOP")• [Edge ](<./Edge_TOP.md> "Edge TOP")• [Emboss ](<./Emboss_TOP.md> "Emboss TOP")• [Feedback ](<./Feedback_TOP.md> "Feedback TOP")• [Fit ](<./Fit_TOP.md> "Fit TOP")• [Flip ](<./Flip_TOP.md> "Flip TOP")• [Function ](<./Function_TOP.md> "Function TOP")• [GLSL Multi ](<./GLSL_Multi_TOP.md> "GLSL Multi TOP")• [GLSL ](<./GLSL_TOP.md> "GLSL TOP")• [HSV Adjust ](<./HSV_Adjust_TOP.md> "HSV Adjust TOP")• [HSV to RGB ](<./HSV_to_RGB_TOP.md> "HSV to RGB TOP")• [Import Select ](<./Import_Select_TOP.md> "Import Select TOP")• [In ](<./In_TOP.md> "In TOP")• [Inside ](<./Inside_TOP.md> "Inside TOP")• [Introduction To s Vid ](<./Introduction_To_TOPs_Vid.md> "Introduction To TOPs Vid")• [Kinect Azure Select ](<./Kinect_Azure_Select_TOP.md> "Kinect Azure Select TOP")• [Kinect Azure ](<./Kinect_Azure_TOP.md> "Kinect Azure TOP")• [Kinect ](<./Kinect_TOP.md> "Kinect TOP")• [Layer Mix ](<./Layer_Mix_TOP.md> "Layer Mix TOP")• [Layer ](<./Layer_TOP.md> "Layer TOP")• [Layout ](<./Layout_TOP.md> "Layout TOP")• [Leap Motion ](<./Leap_Motion_TOP.md> "Leap Motion TOP")• [Lens Distort ](<./Lens_Distort_TOP.md> "Lens Distort TOP")• [Level ](<./Level_TOP.md> "Level TOP")• [Limit ](<./Limit_TOP.md> "Limit TOP")• [Lookup ](<./Lookup_TOP.md> "Lookup TOP")• [Luma Blur ](<./Luma_Blur_TOP.md> "Luma Blur TOP")• [Luma Level ](<./Luma_Level_TOP.md> "Luma Level TOP")• [Math ](<./Math_TOP.md> "Math TOP")• [Matte ](<./Matte_TOP.md> "Matte TOP")• [Mirror ](<./Mirror_TOP.md> "Mirror TOP")• [Monochrome ](<./Monochrome_TOP.md> "Monochrome TOP")• [MoSys ](<./MoSys_TOP.md> "MoSys TOP")• [Movie File In ](<./Movie_File_In_TOP.md> "Movie File In TOP")• [Movie File Out ](<./Movie_File_Out_TOP.md> "Movie File Out TOP")• [MPCDI ](<./MPCDI_TOP.md> "MPCDI TOP")• [Multiply ](<./Multiply_TOP.md> "Multiply TOP")• [Ncam ](<./Ncam_TOP.md> "Ncam TOP")• [NDI In ](<./NDI_In_TOP.md> "NDI In TOP")• [NDI Out ](<./NDI_Out_TOP.md> "NDI Out TOP")• [Noise ](<./Noise_TOP.md> "Noise TOP")• [Normal Map ](<./Normal_Map_TOP.md> "Normal Map TOP")• [Notch ](<./Notch_TOP.md> "Notch TOP")• [Null ](<./Null_TOP.md> "Null TOP")• [NVIDIA Background ](<./NVIDIA_Background_TOP.md> "NVIDIA Background TOP")• [NVIDIA Denoise ](<./NVIDIA_Denoise_TOP.md> "NVIDIA Denoise TOP")• [NVIDIA Flex ](<./NVIDIA_Flex_TOP.md> "NVIDIA Flex TOP")• [NVIDIA Flow ](<./NVIDIA_Flow_TOP.md> "NVIDIA Flow TOP")• [NVIDIA Upscaler ](<./NVIDIA_Upscaler_TOP.md> "NVIDIA Upscaler TOP")• [OAK Select ](<./OAK_Select_TOP.md> "OAK Select TOP")• [Oculus Rift ](<./Oculus_Rift_TOP.md> "Oculus Rift TOP")• [OP Viewer ](<./OP_Viewer_TOP.md> "OP Viewer TOP")• [OpenColorIO ](<./OpenColorIO_TOP.md> "OpenColorIO TOP")• [OpenVR ](<./OpenVR_TOP.md> "OpenVR TOP")• [Optical Flow ](<./Optical_Flow_TOP.md> "Optical Flow TOP")• [Orbbec Select ](<./Orbbec_Select_TOP.md> "Orbbec Select TOP")• [Orbbec ](<./Orbbec_TOP.md> "Orbbec TOP")• [Ouster Select ](<./Ouster_Select_TOP.md> "Ouster Select TOP")• Ouster • [Out ](<./Out_TOP.md> "Out TOP")• [Outside ](<./Outside_TOP.md> "Outside TOP")• [Over ](<./Over_TOP.md> "Over TOP")• [Pack ](<./Pack_TOP.md> "Pack TOP")• [Photoshop In ](<./Photoshop_In_TOP.md> "Photoshop In TOP")• [Point File In ](<./Point_File_In_TOP.md> "Point File In TOP")• [Point File Select ](<./Point_File_Select_TOP.md> "Point File Select TOP")• [Point Transform ](<./Point_Transform_TOP.md> "Point Transform TOP")• [POP to ](<./POP_to_TOP.md> "POP to TOP")• [PreFilter Map ](<./PreFilter_Map_TOP.md> "PreFilter Map TOP")• [Projection ](<./Projection_TOP.md> "Projection TOP")• [Ramp ](<./Ramp_TOP.md> "Ramp TOP")• [RealSense ](<./RealSense_TOP.md> "RealSense TOP")• [Rectangle ](<./Rectangle_TOP.md> "Rectangle TOP")• [Remap ](<./Remap_TOP.md> "Remap TOP")• [Render Pass ](<./Render_Pass_TOP.md> "Render Pass TOP")• [Render Select ](<./Render_Select_TOP.md> "Render Select TOP")• [Render Simple ](<./Render_Simple_TOP.md> "Render Simple TOP")• [Render ](<./Render_TOP.md> "Render TOP")• [RenderStream In ](<./RenderStream_In_TOP.md> "RenderStream In TOP")• [RenderStream Out ](<./RenderStream_Out_TOP.md> "RenderStream Out TOP")• [Reorder ](<./Reorder_TOP.md> "Reorder TOP")• [Resolution ](<./Resolution_TOP.md> "Resolution TOP")• [RGB Key ](<./RGB_Key_TOP.md> "RGB Key TOP")• [RGB to HSV ](<./RGB_to_HSV_TOP.md> "RGB to HSV TOP")• [Scalable Display ](<./Scalable_Display_TOP.md> "Scalable Display TOP")• [Screen Grab ](<./Screen_Grab_TOP.md> "Screen Grab TOP")• [Screen ](<./Screen_TOP.md> "Screen TOP")• [Script ](<./Script_TOP.md> "Script TOP")• [Select ](<./Select_TOP.md> "Select TOP")• [Shared Mem In ](<./Shared_Mem_In_TOP.md> "Shared Mem In TOP")• [Shared Mem Out ](<./Shared_Mem_Out_TOP.md> "Shared Mem Out TOP")• [SICK ](<./SICK_TOP.md> "SICK TOP")• [Slope ](<./Slope_TOP.md> "Slope TOP")• [Spectrum ](<./Spectrum_TOP.md> "Spectrum TOP")• [SSAO ](<./SSAO_TOP.md> "SSAO TOP")• [ST2110 In ](<./ST2110_In_TOP.md> "ST2110 In TOP")• [ST2110 Out ](<./ST2110_Out_TOP.md> "ST2110 Out TOP")• [Stype ](<./Stype_TOP.md> "Stype TOP")• [Substance Select ](<./Substance_Select_TOP.md> "Substance Select TOP")• [Substance ](<./Substance_TOP.md> "Substance TOP")• [Subtract ](<./Subtract_TOP.md> "Subtract TOP")• [SVG ](<./SVG_TOP.md> "SVG TOP")• [Switch ](<./Switch_TOP.md> "Switch TOP")• [Syphon Spout In ](<./Syphon_Spout_In_TOP.md> "Syphon Spout In TOP")• [Syphon Spout Out ](<./Syphon_Spout_Out_TOP.md> "Syphon Spout Out TOP")• [Text ](<./Text_TOP.md> "Text TOP")• [Texture 3D ](<./Texture_3D_TOP.md> "Texture 3D TOP")• [Texture Sampling Parameters ](<./Texture_Sampling_Parameters.md> "Texture Sampling Parameters")• [Threshold ](<./Threshold_TOP.md> "Threshold TOP")• [Tile ](<./Tile_TOP.md> "Tile TOP")• [Time Machine ](<./Time_Machine_TOP.md> "Time Machine TOP")• [Tone Map ](<./Tone_Map_TOP.md> "Tone Map TOP")• [TOP ](<./TOP.md> "TOP")• [TOP Viewer ](<./TOP_Viewer.md> "TOP Viewer")• [Touch In ](<./Touch_In_TOP.md> "Touch In TOP")• [Touch Out ](<./Touch_Out_TOP.md> "Touch Out TOP")• [Transform ](<./Transform_TOP.md> "Transform TOP")• [Under ](<./Under_TOP.md> "Under TOP")• [Video Device In ](<./Video_Device_In_TOP.md> "Video Device In TOP")• [Video Device Out ](<./Video_Device_Out_TOP.md> "Video Device Out TOP")• [Video Stream In ](<./Video_Stream_In_TOP.md> "Video Stream In TOP")• [Video Stream Out ](<./Video_Stream_Out_TOP.md> "Video Stream Out TOP")• [Vioso ](<./Vioso_TOP.md> "Vioso TOP")• [Web Render ](<./Web_Render_TOP.md> "Web Render TOP")• [ZED Select ](<./ZED_Select_TOP.md> "ZED Select TOP")• [ZED ](<./ZED_TOP.md> "ZED TOP")
