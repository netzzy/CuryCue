# Quad Reprojection

## Overview  
  
Quad Reprojection renders pixel-perfect perspective-correct images for flat TVs and LED panels hung at any orientation. It is an alternative method to map content onto quads in a perspective-correct manner. For example take a physcal setup that has a bunch of white panels hanging in the air with arbitrary orientations and sizes. The goal is to make these panels show a coherent overall image between them all, in a perspective-correct manner from a particular point in the room, often know as the Sweet Spot. If you are using a projector to map content onto those panels you would use [Palette:camSchnappr](<./Palette-camSchnappr.md> "Palette:camSchnappr") using a virtual copy of the panels in the same orientations/sizes relative to a virtual projector. Render out the scene and then send that out the projector. If the viewer is standing at the correct point in the room, the rendered content would look like it's floating behind/through the panels. 

However, if the panels are TVs or LED panels instead this technique won't work. Each TV needs to have its content fed through its own signal. A quick approach would be to use the same technique as with a projector, but pulling out each TV's section of the rendered output using corner-pinning so that each TV can be fed its own section of the output. This would work, but will suffer from resolution and filtering issues. For example, if the 1920x1080 TV only takes up 10% of the rendered image width, you would need to render at 19200 pixels wide to feed that TV content which has a similar resolution to its native resolution. If the TV is rotated in any way then filtering will be applied to the rendered image's pixels when generating the content for that TV. Quad reprojection allows the content to be created for each TV/Panel in a pixel-perfect manner, directly at render time. No post corner pinning is needed, so it will produce a surperior image as well as reduce GPU load, which may be caused by having to over-render the resolution of the rendered image. 

An example of using Quad Reproject is available here: 

[File:QuadReproject.toe](</File:QuadReproject.toe> "File:QuadReproject.toe")

Alternatively, you can find in the palette the [Palette:quadReproject](<./Palette-quadReproject.md> "Palette:quadReproject") COMP which is can be used to quickly setup multiple outputs using the Quad Reproject features of the [Camera COMP](<./Camera_COMP.md> "Camera COMP"). It will output pixel perfect textures for one or multiple screens. 

## Usage

To use`QuadReproject.toe`, first create geometry that matches the physical panels you want to map onto. Place this geometry relative to a camera that is positioned where you want the Sweet Spot to be. For each of the panels create a new Camera COMP which will be responsible for rendering the content in a perspective-correct manner for that panel. Point the 'Quad Reproject SOP' parameter in the [Camera COMP](<./Camera_COMP.md> "Camera COMP") to the SOP that contains the geometry for that panel. The SOP should be located in a COMP that is used to position it in the world, as its world position will be taken into account. Fill the 'Quad Reproject Points' parameter with the 4 point indices of the corners of the panel, as they are in the SOP you pointed to. The points should be specified in bottom left, bottom right, top left, top right order. 

This will cause the camera to render the scene as if it is zooming in/corner pinning the area the quad covers in the scene so that it fills its entire output. This operation occurs in the vertex shader which means each pixel is calculated after the zooming has occured, so every pixel is calcuated for the output natively. The output of the render from each camera can then be sent directly to the TVs/panels without further processing. 

## Caveats

Since this trick is done in the vertex shader, some artifacts can occur. In particular when the quad is at a sharp angle from the camera, artifacts can show up. Also rendered geometry (the 'scene') should be tessellated enough so single polygons aren't taking up a large percentage of the rendered output. 

### Non-rectangular Quads

This technique has not be tried on panels that aren't rectangular or squares. In theory it should work, but we haven't been able to verify that yet. Note that previsualization of non-rectangular panels will not look correct inside TouchDesigner due to the way the GPU interpolates texture coordinates for non-parallelogram quads.
