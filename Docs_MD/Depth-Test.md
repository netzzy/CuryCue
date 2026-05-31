# Depth-Test

## Overview

The Depth-Test is how OpenGL determines if one object is in front of another object, regardless of the order the objects are drawn in. Every time an object is drawn it writes a depth for each of its pixels into something called the Depth Buffer. The Depth Buffer is buffer that holds values ranging between 0 and 1. Objects that are located at the near plane of the camera will have a depth value of 0. Object located at the far plane of the camera will have a depth value of 1. Every time a pixel is drawn, the [GPU](<./GPU.md> "GPU") will compare the incoming pixel's depth value with the values that's currently in the Depth Buffer for that pixel on the image. If the depth value of the incoming pixel is less than or equal to the current pixel's, the incoming pixel will get drawn over the current pixel, and the incoming pixel's depth value will be written to the Depth Buffer. If the incoming pixel's depth value is higher than the current pixel's, then the incoming pixel will be discarded. A empty scene will have all depth values of 1. 

You can control some of the behavior of the Depth-Test by changing parameters on the [Common page of the MAT](<./MAT_Common_Page.md> "MAT Common Page") applied to your geometry. 

## Depth-Test Function

The Depth-Test Function is selected in the Common page of any MAT. The Depth-Test Function controls how the incoming pixel's depth value is compared to the current pixel's depth value. By default the compare is "Less than or Equal" (as in the above example). This means if the incoming pixel's depth value is less than or equal to the current pixel's value, the incoming pixel passes the Depth-Test, and will be drawn. If it's greater than the current pixel's depth value then it fails the Depth-Test, and will be discarded. 

## Writing Depth Values

In the [MAT](<./MAT.md> "MAT") options you can choose to write or not write depth values. A material that doesn't write depth values will still be subject to the depth test, but regardless of if it passes or fails the test, it will never write its values to the Depth Buffer. Its color will be still drawn though. This is useful if you have geometry that you want to render, but don't really care if something else draws over it. Some particle systems for example. If the Depth-Test is disabled, depth values will never be written to the Depth Buffer. 

## Obtaining the values of the Depth Buffer

You can obtain the values of the Depth Buffer by using the [Depth TOP](<./Depth_TOP.md> "Depth TOP"). These values will be 24-bit precision initially. If you plan to modify these values using other [TOPs](<./TOP.md> "TOP"), it's advisable to use a 16 or 32-bit pixel format for any downstream TOPs to avoid losing precision.
