# Introduction to SOPs Vid Notes

### What you are going to create

In this Tutorial you will first create a sphere with noise attached, You will then add a material to the sphere and composite it over a gradient and attach a fake shadow. 

### Inserting Geometry, Cameras and Lighting into a Project
* Open TouchDesigner and click the X at the top of the [palette](<./Palette.md> "Palette") browser on the left quarter of the screen.
  * Select the current nodes in the network by right clicking and dragging and then right clicking and selecting delete, or alternatively hit the delete key.
  * Double click the network editor and the [OP Create Dialog](<./OP_Create_Dialog.md> "OP Create Dialog") should appear (alternatively press the <tab> key). Under the COMP tab hold down shift and select a [Geometry COMP](<./Geometry_COMP.md> "Geometry COMP"), [Light COMP](<./Light_COMP.md> "Light COMP"), [Camera COMP](<./Camera_COMP.md> "Camera COMP") and then switch to the TOP tab and select a [Render TOP](<./Render_TOP.md> "Render TOP"). You should now have 4 nodes: geo1, cam1, light1 and render1 with dotted lines pointing from the first 3 to the [Render TOP](<./Render_TOP.md> "Render TOP"). These dotted lines indicate that the [Render TOP](<./Render_TOP.md> "Render TOP") is referencing those nodes for its own [parameters](</index.php?title=Parameters&action=edit&redlink=1> "Parameters \(page does not exist\)").

### Removing the default geometry and replacing it with your own
* Double click the [Geometry COMP](<./Geometry_COMP.md> "Geometry COMP") and delete the [Torus SOP](<./Torus_SOP.md> "Torus SOP") inside. (Right Click > Delete)
  * Double click the network and again whilst holding shift lay down a [Sphere SOP](<./Sphere_SOP.md> "Sphere SOP") followed by a [Noise SOP](<./Noise_SOP.md> "Noise SOP").
  * Under the Spheres parameters set the Primitive Type parameter to NURBS.
  * The two rightmost of the four circle icons underneath the viewer on the Noise SOP will set the particles to display and render (hover over the icons for a hint at what that icon represents). Select both of these parameters so they are highlighted.
  * Zoom out using your scroll wheel until back to the original project1 level or select _project1_ from the [path](<./Network_Path.md> "Network Path") bar at the top of the network editor.

### Adding a material to the geometry
* Double click the network and select from the MAT tab a [Phong MAT](<./Phong_MAT.md> "Phong MAT"). Place it above the [Geometry COMP](<./Geometry_COMP.md> "Geometry COMP").
  * Select the [Phong MAT](<./Phong_MAT.md> "Phong MAT") and drag it onto the [Geometry COMP](<./Geometry_COMP.md> "Geometry COMP"). A small dotted straight line should appear between the two to indicate that the material is applied. Your geometry should now also be much darker and shinier in the [Render TOP](<./Render_TOP.md> "Render TOP") [viewer](<./Viewer.md> "Viewer").
  * Click the [Phong MAT](<./Phong_MAT.md> "Phong MAT") and under its [parameters](</index.php?title=Parameters&action=edit&redlink=1> "Parameters \(page does not exist\)") set the Diffuse parameters values to 0.075, 0.075 and 0.075 for Red, Green and Blue. This should create a very dark grey.
  * Set the Specular to 1, 1 and 1 for R, G and B and then set the Shininess Parameter to 24.

### Modifying the Camera COMP and Light COMPs positions
* Select the [Camera COMP](<./Camera_COMP.md> "Camera COMP") and set its Translate Z [Parameter](<./Parameter.md> "Parameter") to 20 rather than the default (5).
  * Select the [Light COMP](<./Light_COMP.md> "Light COMP") and set the Translate Parameter to x: -50 y: 50 and z: 0. In the [Render TOP](<./Render_TOP.md> "Render TOP") [viewer](<./Viewer.md> "Viewer") the sphere should now be smaller and in the center with the lighting shining from above.

### Adding a Ramp TOP background and compositing the geometry over it
* Double click the network and under the TOP tab select a [Ramp TOP](<./Ramp_TOP.md> "Ramp TOP").
  * Under the Common tab in the [Ramp TOPs](<./Ramp_TOP.md> "Ramp TOP") [parameters](</index.php?title=Parameters&action=edit&redlink=1> "Parameters \(page does not exist\)") set the Custom Resolution to 1280x720
  * In the [Ramp TOPs](<./Ramp_TOP.md> "Ramp TOP") [parameters](</index.php?title=Parameters&action=edit&redlink=1> "Parameters \(page does not exist\)") click two new points on the Ramp Bar and place them very close to one another a third of the way up the screen.
  * Set the Value slider for each point by clicking the point you want to edit and then dragging the value slider. Create a ramp which looks like a floor, and wall behind with the floor meeting the wall a third of the way up.


[insert image here] 
* Double click the network and select a [Composite TOP](<./Composite_TOP.md> "Composite TOP"). Place the [TOP](<./TOP.md> "TOP") to the right of the [Render TOP](<./Render_TOP.md> "Render TOP") and [Ramp TOPs](<./Ramp_TOP.md> "Ramp TOP").
  * Left click the [Render TOPs](<./Render_TOP.md> "Render TOP") output and wire it into the [Composite TOP](<./Composite_TOP.md> "Composite TOP") by left clicking the [Composite TOPs](<./Composite_TOP.md> "Composite TOP") input.
  * Wire the [Ramp TOP](<./Ramp_TOP.md> "Ramp TOP") into the [Composite TOPs](<./Composite_TOP.md> "Composite TOP") input too.
  * Select the [Composite TOP](<./Composite_TOP.md> "Composite TOP") and in its [parameters](</index.php?title=Parameters&action=edit&redlink=1> "Parameters \(page does not exist\)") set the Operand [parameter](<./Parameter.md> "Parameter") to Over.

### Insert a fake shadow effect using a Ramp TOP and Transform TOPs
* Create a new [Ramp TOP](<./Ramp_TOP.md> "Ramp TOP") between the [Render TOP](<./Render_TOP.md> "Render TOP") and first [Ramp TOP](<./Ramp_TOP.md> "Ramp TOP").
  * Again set the [Ramp TOPs](<./Ramp_TOP.md> "Ramp TOP") resolution to 1280x768 under the Common tab in the parameters.
  * Switching back to the Ramp tab, set the Type to Circular, Phase to 0.8 and the Period to 0.4.
  * Add a new point to the middle of the Ramp Bar.
  * Set all of the 3 Ramp Bar values to 0 and the middle and far right Ramp Bars Alphas to 0.
  * You should now have a black spot with fading edges and a checkerboard background. If the spot is too big for the [viewer](<./Viewer.md> "Viewer") you can drag the middle value in the Ramp Bar to the left to choke the ramp.
  * Right click the [Ramp TOPs](<./Ramp_TOP.md> "Ramp TOP") output and whilst holding shift select a [Transform TOP](<./Transform_TOP.md> "Transform TOP"), a [Blur TOP](<./Blur_TOP.md> "Blur TOP") and letting go of shift select a [Level TOP](<./Level_TOP.md> "Level TOP").
  * Select the [Transform TOP](<./Transform_TOP.md> "Transform TOP") and set its Translate [parameter](<./Parameter.md> "Parameter") to x: 0 and y: -0.25.
  * Select the Scale parameter and set x: 0.4 and y: 0.08.
  * Switch to the [Blur TOP](<./Blur_TOP.md> "Blur TOP") and set the Pre-Shrink parameter to 5 and the Filter Size to 16.
  * Select the [Level TOP](<./Level_TOP.md> "Level TOP") and under to Post tab set the Opacity parameter to 0.3.
  * Finally wire the [Level TOPs](<./Level_TOP.md> "Level TOP") output into the [Composite TOPs](<./Composite_TOP.md> "Composite TOP") input, you will notice that there is no difference in the [Composite TOPs](<./Composite_TOP.md> "Composite TOP") viewer. This is due to how the [Composite TOP](<./Composite_TOP.md> "Composite TOP") layers its inputs. Inputs placed after one another are placed behind the previous layer.
  * Select the [Composite TOP](<./Composite_TOP.md> "Composite TOP") and you will see in the parameters an Input OP parameter. Click the up arrow icon next to the [Level TOP](<./Level_TOP.md> "Level TOP") in the list.
  * In the [Composite TOPs](<./Composite_TOP.md> "Composite TOP") [viewer](<./Viewer.md> "Viewer") the shadow should now be visible beneath the morphing Sphere.

### Set the Project up to be displayed in Perform Mode
* Right click the [Composite TOP](<./Composite_TOP.md> "Composite TOP") and select an [Out TOP](<./Out_TOP.md> "Out TOP") from the [TOP](<./TOP.md> "TOP") tab.
  * Zoom out of the [network](<./Network.md> "Network") until you see project1 or click the / in the Path Bar above the [Network](<./Network.md> "Network") Editor.
  * Select project1 and under the Layout tab in project1's parameters set the Width to 1280 and the Height to 720.
  * Click the ^ at the top left of the screen above the [Network](<./Network.md> "Network") Editor to switch to [Perform Mode](<./Perform_Mode.md> "Perform Mode"). You can press the Escape Key to then close [Perform Mode](<./Perform_Mode.md> "Perform Mode").
