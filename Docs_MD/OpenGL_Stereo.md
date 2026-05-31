# OpenGL Stereo

## **THIS FEATURE IS NO LONGER SUPPORTED AS OF THE 2022.20000 SERIES OF BUILDS**

Also known an Quad Buffered Stereo, OpenGL native stereo is a way of providing the GPU driver with the left and right eye images and allowing it to present them to the users in it's own way, based on the driver settings and PC setup. This is different then other methods of outputting stereo such as placing the left/right images side-by-side at a double-wide output resolution, or using two outputs; one for left and one for right. 

One example of this is Nvidia's 3D Vision system where a monitor outputs images at 120hz (60hz per eye) and uses shutter glasses such as [these](<http://www.nvidia.ca/object/3d-vision-main.html>) to control what each eye sees. 

## Setup

To get OpenGL Stereo working you first need to set it up in your GPU's driver settings. Refer to the documentation of your GPU manufacturer for detailed information. For the Nvidia case you'll want to use the 'Set up Stereoscopic 3D' section of the Nvidia Control Panel first. Then ensure that 'Stereo - Enable' = On is set in the 'Manage 3D settings' section. Also make sure you have selected the correct 'Stereo - Display mode' based on the display technology you are using. 

Next, to make TouchDesigner start up using Stereo enabled windows, set the Windows environment variable TOUCH_STEREO=1. A dialog box will be displayed on startup if TOUCH_STEREO=1 is set but TouchDesigner is unable to setup stereo windows. 

## Rendering

Rendering stereo images requires using two cameras that are offset from each other slightly, as well as asymmetric projection frustum. An article that goes into detail about that is located [here.](<http://www.nvidia.com/content/GTC-2010/pdfs/2010_GTC2010.pdf>)

A new method`projectionStereo()`is provided in the [Matrix Class](<./Matrix_Class.md> "Matrix Class") to help with this. This function will create a projection matrix for the left and right eyes which you can use as a Custom Projection in the [Camera COMP](<./Camera_COMP.md> "Camera COMP"). Along with the custom projection, you'll also want to offset the two cameras by -IPD/2.0 (left eye) and +IPD/2.0 (right eye) in the X axis. IPD is the Interpupillary distance also given to the`projectionStereo()`function, specified in centimeters. 

## Example

Here example file with rendering setup using the python script (via custom parameters in the stereoWindow COMP): [File:StereoRenderExample.toe](</File:StereoRenderExample.toe> "File:StereoRenderExample.toe")
