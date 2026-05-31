# SICK

[SICK](<https://www.sick.com/ca/en/catalog/products/lidar-and-radar-sensors/>) makes lidar sensors, primarily for industrial automation applications, and is global provider of intelligent sensors and solutions for industrial automation technology. 

Communication with SICK LIDAR sensors is done over an Ethernet connection. 

The [SICK TOP](<./SICK_TOP.md> "SICK TOP") sets up the connection and receives a standard TouchDesigner point cloud as an array of pixels where the pixel's R G B values by default contain a point's X Y Z position expressed as 32-bit floating point numbers. 

Derivative has tested a limited set of models. The entire [range of LIDARs](<https://github.com/SICKAG/sick_scan_xd/blob/master/REQUIREMENTS.md>) run using the same SDK, so other models may work but you would have to determine usability yourself. TouchDesigner currently uses version 3.0.x of the SDK.
