# Display Options

There are 3 ways to open the [Geometry Viewer](<./Geometry_Viewer.md> "Geometry Viewer")'s display options. 
* Press "p" keyboard shortcut (must be in **View** state if using the Geometry Viewer in a pane).
  * Right-click on the viewer and select Display Options (must be in **View** state if using the Geometry Viewer in a pane).
  * Click the "+" Display Options button in Geometry Viewer toolbar.

## Guides & Markers

This page can be used to control the display of point, vertex or primitive overlays for SOP geometry. For POPs, an expanded list of attribute overlays is available in the right-click [view options menu](<./Geometry_Viewer.md> "Geometry Viewer"). 

Rendering of the origin and grid can also be turned on and off from this page. 

## Misc

[![](./images/thumb/9/95/DisplayOptionsMisc.png/300px-DisplayOptionsMisc.png)](</File:DisplayOptionsMisc.png>)

[](</File:DisplayOptionsMisc.png> "Enlarge")

Display Options dialog Misc page
* Aspect Ratio - enable this option to force the viewer aspect to a specific ratio rather than using the dimensions of the node.
  * Scale Attribute Overlays - controls the size of all attribute overlays e.g. text, vectors, dots, etc. 1 is the default size and < 1 is smaller and > 1 is larger.
  * Scale in Screen Space - controls whether the overlays are scaled relative to the screen or world. In screen space, overlays will remain a constant size relative to the node viewer, whereas in world space the overlays will stay a fixed size relative to the geometry and will grow or shrink as you zoom in and out.
  * Thin Attribute Range - Enable this option to reduce the number of points, vertices or primitives whose overlays are displayed. Only those whose index falls between the given range will be drawn.
  * Thin Attribute Percentage - Reduce the number of points, vertices or primitives whose overlays are drawn as a percentage of the total. At 0, none of the points, vertices or primitives are thinned and all are displayed. At 1, everything is removed and nothing will be drawn.
