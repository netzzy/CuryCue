# Color Space Workflows

## Overview  
  
First, make sure you've read the [Color Space](<./Color_Space.md> "Color Space") article to get a high-level overview of color space concepts. 

By default, TouchDesigner is not color space aware, and runs in a mode we now call Pass-Through. This means all colors are loaded in from files as-is, combined/composited as-is, and output to displays and files as-is. Without any other intervention this workflow is actually not correct, since the content being brought in will likely have a non-linear transfer function applied to it (such as sRGB), and lighting/compositing should only be done with a linear transfer function. Images and movies usually look correct on output though since they are loaded in with that transfer still applied, and then shown with the transfer, which usually matches the transfer of the monitor (at least when dealing with sRGB content). All builds prior to the 2025.30000 series suffered from this defect. 

To avoid breaking existing files, the new color-correct workflow requires an opt-in on a per-project basis. 

## Working Color Space

The working color space defines how all of the color values store within the project are held. This includes that colors for SOP and POP attributes, as well as colors held in TOPs. Regardless of what color space the source colors are defined in (most images will be in sRGB for example), they will all be converted to the working color space when loaded in. The project has a singular working color space to avoid confusion and errors that could occur when trying to combine one TOP that was in one color space and another that's in a different color space. 

### RGB Color Parameters

All color parameters will automatically be converted to the working color space when they are evaluated and used by the node. Parameters to control what color space to treat the values as are located on the Common page of the nodes that have color parameters. This is known as the Parameter Color Space. 

### TOP Texture Data

TOPs that bring in external data (Movie File In TOP, Video Device In TOP), will attempt to detect the color space of the source content, and convert it to the working color space when bringing in the data. If nothing can be detected then sRGB will be assumed, but there is a parameter to explicitly specify what color space to treat the input as. 

When outputting a TOP to a Movie File Out TOP, Video Device Out TOP etc, you will need to specify what color space you want the content converted to before output. If possible, the nodes will also tag the content as that color space (when the output protocol supports it). Some protocols such as SDI only support a very limited number of color spaces in their metadata. 

The GLSL nodes now have a new 'Colors' tab which differentiates those uniforms from regular Vector uniforms 

### POP Color Attribute Qualifier

POP attributes can be given a Color qualifier when they are created, which will cause parameters used to fill in their default values to convert that parameter from the Parameter Color Space to the Working Color Space. POP color attributes that are created from parameters will be converted into the working color space. Colors imported via external geometry formats will be converted to the working color space. 

## Turning on Color Space Workflows

Color Space correct workflows is an opt-in feature that is done per-project. This is to avoid changing the behavior of existing projects and components. However note that using .tox file that depend on the passthrough behavior may not work the same when used in a Color Space correct project. 

**You will need to save your.toe and restart it for color space changes to take effect.**

**NOTE:** You can use the [Preferences Dialog](<./Preferences.md> "Preferences") 'Color' tab or directly control these settings through the [Project Class](<./Project_Class.md> "Project Class") in python. 

### Working Color Space

The working color space is the color space that all images/movies and color values will be converted into before they are used in processing. All TOPs store their data in this color space. On output, the content will be converted to the correct color space as required by the output destination. 

To choose the working color space of the project, use 
[code] 
     project.workingColorSpace
    
[/code]

Which accepts the values 
[code] 
     WorkingColorSpace.PASS_THROUGH
     WorkingColorSpace.SRGB_LINEAR
     WorkingColorSpace.ACES_CG
     WorkingColorSpace.DCIP3_LINEAR
     WorkingColorSpace.REC_2020_LINEAR
    
[/code]

PASS_THROUGH is the default state for all projects, and matching the behavior of all builds released before 2025.30000 series. ACES_CG forces all TOPs to be 16-bit float, and all colors will be in the ACEScg color space with linear transfer. SRGB_LINEAR means all colors will be in the sRGB color space, and processed using a linear transfer function. However, any 8-bit RGBA texture will **store** their data using a sRGB transfer function. This is done to provide more detail for the darker colors. This does not mean you will see the colors changes like gamma has been applied to the images. It only means that color values that are brighter will get rounded to coarser steps of the 256 color steps that 8-bit can hold. 

### Editor Window Pixel Format

The pixel format used to output content to the OS determines both the bit-depth of content, as if the content is HDR capable or not. For Perform windows, this is selected in the [Window COMP](<./Window_COMP.md> "Window COMP"). For the main editor window though, since can be selected with 
[code] 
     project.editorWindowPixelFormat
    
[/code]

Which accepts the values: 
[code] 
     WindowPixelFormat.SDR8_FIXED
     WindowPixelFormat.SDR10_FIXED
     WindowPixelFormat.HDR10_FIXED
     WindowPixelFormat.HDR16_FLOAT
    
[/code]

If your editor window is set to a HDR format, but your monitor is not in HDR mode, then you may experience a mode change, as the OS flips it into HDR mode automaticlly. It is recommended that you have your monitor in HDR mode already when working HDR window pixel format. 

Note that this does not control what color space your monitor is running in directly, or what is sent across the wire to the monitor. This only controls what TouchDesigner sends to the OS. TouchDesigner and the OS will agree on color space to use for each of the pixel formats, and then the OS may do another conversion from that color space to what the monitor desires. Using 16-bit float, which will likely be supported by your GPU/OS, does not mean 16-bit float data will be sent to the monitor. 

The bit depth of the data sent to the monitor is usually controlled in the Driver Settings for your GPU.
