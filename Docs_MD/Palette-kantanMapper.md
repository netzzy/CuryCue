# Palette:kantanMapper

簡単 (kantan) - japanese for easy, simple - **Kantan Mapper 2** is a new projection mapping and masking toolkit for TouchDesigner. The user defines 2D polygons and bezier outlines in the field of view of a projector, then fills each shape with a selected image (TOP) with tools to warp how the image fits into the shape.   
  
## Summary

Kantan Mapper is an interface overlaid on-top of an actual projection to enable the drawing, creation and placement of various shapes onto real life objects and the possibility to assign TOP Image Nodes to these shapes and masks. 

See also [Projection Mapping](<./Projection_Mapping.md> "Projection Mapping"), [Vioso](<./Vioso.md> "Vioso"), [Scalable Displays](<./Scalable_Display_TOP.md> "Scalable Display TOP"), [camSchnappr](<./Palette-camSchnappr.md> "Palette:camSchnappr"), [projectorBlend](<./Palette-projectorBlend.md> "Palette:projectorBlend"). 

## Getting Started

Kantan Mapper 2 is located in the Palette in 'Mapping' folder. To begin, open the [Palette](<./Palette.md> "Palette") and drag`kantanMapper`from Palette>Mapping onto your network pane. 

Error in [widget Vimeo](<./Widget-Vimeo.md> "Widget:Vimeo"): unable to write file /var/www/html/extensions/Widgets/compiled_templates/wrt6863cc6b810b11_09158699

Error in [widget Vimeo](<./Widget-Vimeo.md> "Widget:Vimeo"): unable to write file /var/www/html/extensions/Widgets/compiled_templates/wrt6863cc6b821a03_16870417

## Parameters - Kantan Page

Help`Help`\- Opens this page. 

Open Kantan Window`Open`\- Opens the Kantan Mapper Interface. 

Close Kantan Window`Close`\- Closes the Kantan Mapper Interface. 

## General Usage

After dragging kantanMapper from Palette>Tools onto your network pane, click the "Open Kantan Window" parameter pulse button to open the KantanMapper editing interface. 

### Create a Shape

To create a shape select either the [![Kantan-CreateRectangle.png](./images/9/94/Kantan-CreateRectangle.png)](</File:Kantan-CreateRectangle.png>) Create Quad or the [![Kantan-CreateFreeform.png](./images/d/d8/Kantan-CreateFreeform.png)](</File:Kantan-CreateFreeform.png>) Create Freeform tool. 

For quads click on the startpoint on the editing canvas and drag to the opposite endpoint of the quad. 

For freeform shapes, click on the canvas to create a key and drag out the edges. To close a shape, click back on the first key created. 

### Transform a Shape

With the Select Shape Tool selected, select a shape on the canvas. You can drag the shape to reposition or use the outer handles to scale and rotate the shape. 

### Modifying a Shape

With the Select Keys and Handles Tool selected, pick a shape on the canvas if a shape is not yet selected and move the keys or handles. 

### Assigning a Texture

Drag a TOP onto the Texture field in the Shape Settings section. 

### Duplicate Shapes

Select a shape and hold the Alt key when transforming the shape to create a copy. 

### Editing Textures

With a shape selected, click the Edit Texture Button to bring up the Texture Editor. Here, specify the area of the texture to apply to the shape or apply the shape as a mask to the texture.v 

## User Interface

### Project Settings

Resolution \- Specify the output Resolution of the full Canvas. This should match the resolution of the projector(s) used for this project. 

Window Options - Will open the [Window COMP](<./Window_COMP.md> "Window COMP") parameters for the output screen. 

Toogle Output - Will open/close the output window as set-up in the Window Options. 

Bg Mask - Specify a background mask by either dragging a TOP into the field or typing in the absolute path to the TOP. The button behind the field is used to enable or disable the mask. 

Bg Level - Control the level of the background mask when enabled. 

### Shapes Tree

The Shapes Tree Viewer is a list of shapes (quads and freeform) as well as groups in a collapsible display. 

Every row representing a shape or group can be hidden by clicking the eyeball icon [![Kantan-Eyeball.png](./images/e/e7/Kantan-Eyeball.png)](</File:Kantan-Eyeball.png>) in the last column of the tree. 

Shapes and groups can be reordered by dragging them. 

Shapes and groups can be nested by dragging them onto other groups. 

New Groups can be created with the "Add Group" button [![Kantan-AddGroup.png](./images/2/20/Kantan-AddGroup.png)](</File:Kantan-AddGroup.png>) on the top-left of the Shape Tree. 

### Editing Tools

The Editing Tools section of the UI holds the controls for selecting, creating and transforming shapes in KantanMapper. 

Select Shape Tool [![Kantan-SelectShape.png](./images/5/5a/Kantan-SelectShape.png)](</File:Kantan-SelectShape.png>) can select Shapes and exposes the shape transform handles for translation, scale and rotate. 

Select Key & Handle Tool [![Kantan-SelectKeys.png](./images/d/d9/Kantan-SelectKeys.png)](</File:Kantan-SelectKeys.png>) enables the selection and transform of a shapes keys and handles. 

To add a quad use the Create Quad Tool [![Kantan-CreateRectangle.png](./images/9/94/Kantan-CreateRectangle.png)](</File:Kantan-CreateRectangle.png>). After selecting the tool click and drag on the canvas to create a quad shape. 

To add a freeform shape use the Create Freeform Tool [![Kantan-CreateFreeform.png](./images/d/d8/Kantan-CreateFreeform.png)](</File:Kantan-CreateFreeform.png>). After selecting the tool, click and drag on the canvas to create a key and it's handles. repeat and finish the shape by clicking on the first key created. 

If a shape is selected and the "Select Key & Handle" tool is active, shape specific tools become available: 

Common to all shapes is the key and handle selector [![Kantan-KeyHandleTransform.png](./images/b/bf/Kantan-KeyHandleTransform.png)](</File:Kantan-KeyHandleTransform.png>). Keys and Handles can be translated when selected. A red line shows 

For Quads: 
* [![Kantan-Gridwarp.png](./images/a/af/Kantan-Gridwarp.png)](</File:Kantan-Gridwarp.png>) enables the gridwarp mode of the selected quad. This enables the transformation of grid points and handles. Also rows and columns can be removed by selecting them and clicking the keyboard delete key.
  * [![Kantan-AddRow.png](./images/8/80/Kantan-AddRow.png)](</File:Kantan-AddRow.png>) add a row to the gridwarp mesh by selecting the insert point on the grid directly.
  * [![Kantan-AddCol.png](./images/d/d3/Kantan-AddCol.png)](</File:Kantan-AddCol.png>) add a column to the gridwarp mesh by selecting the insert point on the grid directly.


For Freeform Shapes: 
* [![Kantan-AddKey.png](./images/3/3d/Kantan-AddKey.png)](</File:Kantan-AddKey.png>) enables adding keys inline the selected shape.
  * [![Kantan-ConvertKey.png](./images/f/f9/Kantan-ConvertKey.png)](</File:Kantan-ConvertKey.png>) collapses the handles of a bezier key when selecting the key and enables resizing of the handles by dragging them from the key.

### Shape Settings

Name - Change the name of the shape as shown in the Shapes Tree. 

Color - Change the color of the shape. The color is shown if no texture is assigned to the shape or the texture is disabled. 

Texture - Assign a texture to the shape by dragging a TOP onto the field and enabling it by clicking the [![Kantan-Disable.png](./images/1/1d/Kantan-Disable.png)](</File:Kantan-Disable.png>) button behind it. 

Orientation - Change the orientation of the assigned texture or flip it. 

Edit Texture - Open the Texture Editor. 

Softedge - Apply softedge to the shape. While softedge on the quad is done via a basic shader, the softedge on the freeform is a bit more of an experiment using the [Extrude SOP](<./Extrude_SOP.md> "Extrude SOP") and [Skin SOP](<./Skin_SOP.md> "Skin SOP"). To see it's inner workings, navigate to .../kantanMapper/project/allShapes/item*. 

Lock Handle - Locks and unlocks the gridwarp handles of the quad and the key handles of the freeform shape. 

### Transform Tools

Transformation can be applied to single or multiple shapes. When using the fields or buttons, the middle mouse wheel can be used to increase or decrease the current value. 

Scale - Change the scale of the selected shapes around the selected pivot. 

Rotate - Change the rotation of the selected shapes around the selected pivot. 

Translate - Move the selected shapes in tx and ty. 

Pivot - Pick the pivot to apply the transform around. 

Free Pivot - If "Free" is selected in Pivot, change the position of the pivot point. 

### Shape Tools

The available Tools depend on the selected shape. 

#### Quad

[![Kantan-RectangleTools.png](./images/1/13/Kantan-RectangleTools.png)](</File:Kantan-RectangleTools.png>) Rows / Cols - Change the number of rows and columns in the quad. **Warning:** this will reset the Gridwarp. To remove a row or column without loosing the previously applied deform, select the row or column when in grid warp mode. 

Warping - Change the warping mode of the quad. Options are: 
* Bezier: The grid can be warped with keys and handles.
  * Linear: only the grid points can be transformed and are connected linearly.


Mapping - Choose how a texture is mapped onto the quad: 
* Perspective
  * Bilinear


Reset Keystone - Reset the transformation on the corner points of the quad. 

Reset Warp - Reset the transformation on all grid points of the quad. 

#### Freeform

Detail - change the resolution of the edges between keys on the freeform shape. 

## Texture Editor

TouchDesigner Build: Latest\n2021.100002020.236802018.28070before 2018.28070
