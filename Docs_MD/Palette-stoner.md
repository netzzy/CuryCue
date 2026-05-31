# Palette:stoner

Stoner is a grid-warping and upscale 'keystoner' tool. It has two levels of warping. First is a 4-point corner-pin. Within that is a mesh warper where for each point of the mesh you can adjust position and curvature using bezier handles. Stoner has 2 outputs: 
* the final warped image and
  * a displacement map which can be used in conjunction with the [Remap TOP](<./Remap_TOP.md> "Remap TOP")


On the Stoner custom parameter page you can also specify a custom COMP (usually a [Base COMP](<./Base_COMP.md> "Base COMP") will be perfect) where the displacement data and the displacement map are stored. 

**Note:** Stoner is intended to be used to create the displacement map and then to be removed from the file with only the necessary data inside the COMP defined in the "Project" custom parameter staying behind. This will increase performance quite a lot and let you use one centralized Stoner instead of many. 

See also [Projection Mapping](<./Projection_Mapping.md> "Projection Mapping"). 

## Getting Started

You can find Stoner in the [Palette](<./Palette.md> "Palette") under the folder Derivative>Mapping. 

Drag and drop the component from the [Palette](<./Palette.md> "Palette") into your network. 

Connect a TOP to the input of the Stoner component. 

Open the Stoner interface by clicking the "Open Stoner Window" custom parameter on the node's Stoner parameter page. 

## General Interface Controls

You can re-size the interface by dragging any of the windows edges. 

Switch between Modes via the Mode Buttons or by hitting keys: 

    g - for grid-warp mode
    k - for keystone mode

Undo and redo can be accessed via Ctrl+z and Ctrl+y. 

Zoom in and out of the viewer by using the mouse wheel. 

Drag the grid in the viewer by click and drag via the middle mouse button. 

Hit "h" to reset the viewer. 

Changing the Rows and Columns by number will reset the grid. 

## Grid Warp

The grid can be warped using Bezier or Linear mode. 

Select Points to move by clicking on them in the viewer. 

You can select multiple points by holding down the Ctrl key. 

You can select a whole row or column by holding down "Ctrl+r" or "Ctrl+c". 

Add a row or column by switching into "Add Row" or "Add Column" Mode and selecting the point of creation in the viewer. A red line will indicate where a new row or column is created. Selecting a point also enables deleting the row or the column this point belongs to by clicking "Delete Row" or "Delete Column" 

Move points by dragging them with the mouse. Alternatively, use the arrow keys to move selected points and hold the "Ctrl" key to increase step size. 

Selecting points will reveal additional Bezier control handles. Hitting the "l" key will toggle between locked and unlocked state. 

## Keystone

The Image can be mapped Perspectively or in Bilinear mode. 

Select Points to move by clicking on them in the viewer. Alternatively, use the arrow keys to move selected points and hold the "Ctrl" key to increase step size. 

Reset selected Keystone points by clicking "Reset Selected" 

TouchDesigner Build: Latest\n2021.100002020.236802018.28070before 2018.28070
