# RenderStream

## Overview  
  
[RenderStream](<https://www.disguise.one/en/products/renderstream/>) is a proprietary protocol by [Disguise](<https://www.disguise.one/en/>) for controlling third party realtime render engines from the Disguise software. It allows one to split up a large realtime render task among an arbitrary number of render PCs. Because it is entirely network-based, Renderstream can scale very flexibly, and is not as limited by hardware outputs or routing complexities that can arise with, for example, video standards like HDMI, DP, or SDI. 

In TouchDesigner 2022.28040 and later, support for RenderStream r22 and later is found in the [RenderStream In CHOP](<./RenderStream_In_CHOP.md> "RenderStream In CHOP"), [RenderStream In TOP](<./RenderStream_In_TOP.md> "RenderStream In TOP"), and [RenderStream Out TOP](<./RenderStream_Out_TOP.md> "RenderStream Out TOP"). 

Enabling these nodes requires a TouchDesigner Pro or TouchPlayer Pro license. 

It allows you to send values/images to TouchDesigner, generate content in TouchDesigner using those values/images, and then send the images back to D3, all in sync. 

TouchDesigner`.toe`project files are loaded in, animated and driven using the standard RenderStream UI. RenderStream invokes TouchDesigner’s plugin, TouchEngine to load and run the components. Any TouchDesigner component that generates visuals can be augmented to conform to the RenderStream -TouchDesigner API. Images and controls flow from RenderStream into TouchDesigner via the RenderStream In TOP and CHOP, and data flows out to RenderStream via the [RenderStream Out TOP](<./RenderStream_Out_TOP.md> "RenderStream Out TOP"). 

## Disguise

Some video documentation is available at the [Disguise YouTube Channel.](<https://www.youtube.com/watch?v=DfLjy7ZIcpQ>)

More details (must read) on how to setup your Disguise RenderStream project are available at the following [Disguise RenderStream GitHub repository](<https://github.com/disguise-one/RenderStream#known-filetypes>). 

## TouchDesigner

Every frame that a TouchDesigner component is called by Disguise to generate a frame, it receives a set of parameters, camera transforms, current frame number and other data. TouchDesigner generates one or more images and returns them via [RenderStream Out TOPs](<./RenderStream_Out_TOP.md> "RenderStream Out TOP"). At the same time, the TouchDesigner component can be receiving, processing and sending data to devices, protocols or other software tools. 

### Rendering Setup

There are a few pieces in your TouchDesigner project that need to be setup to get your project to render as RenderStream is requesting: 

#### Camera COMP

The [Camera COMP](<./Camera_COMP.md> "Camera COMP") needs to be setup to position the camera using the correct transform, and use the correct projection matrix. The matrices needed to do this are obtaind from the [RenderStream In CHOP](<./RenderStream_In_CHOP.md> "RenderStream In CHOP") via 2 Python methods. The below instrunctions assume that CHOP is named`renderstreamin1`: 1\. On the 'XForm' page, set the Z translate to 0, which defaults to 5 on a new Camera COMP. 2\. On the 'Pre-Xform' page, fill the 'Xform Matrix/CHOP/DAT' parameter with the expression`op('renderstreamin1').cameraTransform`. You'll need to turn on the 'Apply Pre-Transform' toggle to access that parameter. 3\. On the 'View' page, change the 'Projection' menu to 'Custom Projection Matrix', and fill the 'Proj Matrix/CHOP/DAT' parameter with the expression`op('renderstreamin1').projection`. 

### Render TOP

The [RenderStream In CHOP](<./RenderStream_In_CHOP.md> "RenderStream In CHOP") also contains 'width' and 'height' channels, which you'll want to use to drive the Resolution of your [Render TOP](<./Render_TOP.md> "Render TOP"). Now renferece the [Camera COMP](<./Camera_COMP.md> "Camera COMP") you've setup in the in the 'Camera' parameter of the Render TOP. 

### Schema

To prepare a component for use in the Disguise system, you edit a table DAT on the [RenderStream In CHOP](<./RenderStream_In_CHOP.md> "RenderStream In CHOP") in your TouchDesigner component to define a RenderStream Schema, which exposes parameters to Disguise that can be driven through Disguise’s UI. At run-time values are fed back through the RenderStream In CHOP in TouchDesigner.
