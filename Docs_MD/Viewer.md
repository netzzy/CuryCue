# Viewer

### Locations of Viewers

Viewers of TouchDesigner operators are found in three places: 
* in nodes - Viewers inside nodes are called to as [Node Viewers](<./Node_Viewer.md> "Node Viewer").
  * in floating windows - Opened from panes as floating dialogs (using Tear Off or Copy Pane), or opened by selecting **Viewer...** from a node's right-click menu.
  * in [Panes](<./Pane.md> "Pane")


**Note** : Moving content inside a node viewer does not affect its transforms or parameters. **Exception** : [Camera COMP](<./Camera_COMP.md> "Camera COMP")

### Styles of Viewers

There is a viewer style for every operator family. 

    [Geometry Viewer](<./Geometry_Viewer.md> "Geometry Viewer") \- A 3D viewport for viewing and manipulating 3D scenes or objects. You can tumble, pan, and zoom throughout the 3D scene. You can also edit the scene by translating, rotating, and scaling geometry, cameras, and lights at the [Object Component](<./Object_Component.md> "Object Component") level. These viewers are also found as Node Viewers in all 3D Components and SOPs.

    In the node viewers of Geometry COMPs and SOPs, the Adaptive Homing option will continually keep in-view the 3D geometry being displayed, even when the geometry changes shape, size and animated position. This can be turned off globally in Edit > Preferences > Geometry : Adaptive Homing by Default.

    Panel Viewer - Displays the view of [Panel Components](<./Panel_Component.md> "Panel Component") and allows for interactions with the control panels.

    [CHOP Viewer](<./CHOP_Viewer.md> "CHOP Viewer") \- A 2D viewer to inspecting and editing CHOP channel values. Time is on the x-axis, value (or amplitude) is on the y-axis. Also found as a Node Viewer in all CHOPs.

    [TOP Viewer](<./TOP_Viewer.md> "TOP Viewer") \- A 2D viewer for viewing TOP images. You can pan and zoom around the image. Also found as a Node Viewer in all TOPs.

    [SOP Editor](<./SOP_Editor.md> "SOP Editor") \- Similar to the Geometry Viewer but specialized for editing SOP geometry. Using SOP viewer **States** you can directly manipulate geometry or model new geometry from scratch. A SOP viewer can only be opened directly from SOPs by right-clicking on the SOP and selecting **Model Geometry...** from the menu.

    [DAT Viewer](<./DAT_Viewer.md> "DAT Viewer") \- Displays the text or table data of the DAT. This can be directly edited (in generator DATs) by making the viewer active. Note that the default node laguage for DATs is python and displayed in blue text, if the text is the same purple color as DATs then this node's language is set to Tscript.
