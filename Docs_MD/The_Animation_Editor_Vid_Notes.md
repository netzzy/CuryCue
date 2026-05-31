# The Animation Editor Vid Notes

### Setting up the Geometry
* At the bottom of the screen in the [timeline](<./Timeline.md> "Timeline") set the End and Rend [parameters](</index.php?title=Parameters&action=edit&redlink=1> "Parameters \(page does not exist\)") on the left to 400.
  * Double click the [network](<./Network.md> "Network") and under the [COMP](<./Component.md> "Component") tab whilst holding <ctrl> select a [Camera COMP](<./Camera_COMP.md> "Camera COMP"), a [Geometry COMP](<./Geometry_COMP.md> "Geometry COMP"), a [Light COMP](<./Light_COMP.md> "Light COMP") and a [Render TOP](<./Render_TOP.md> "Render TOP").
  * Double click on the [Geometry COMP](<./Geometry_COMP.md> "Geometry COMP") and delete the [Torus SOP](<./Torus_SOP.md> "Torus SOP") inside.
  * Double click the network and from the [SOP](<./SOP.md> "SOP") tab select a [Sphere SOP](<./Sphere_SOP.md> "Sphere SOP").
  * Select the Sphere SOP and set its Radius parameter to 0.1 in x, y, and z.
  * Right click the Sphere SOP and select a [Transform SOP](<./Transform_SOP.md> "Transform SOP").
  * Copy and paste the Transform SOP you just created twice.

### Creating the [Animation COMP](<./Animation_COMP.md> "Animation COMP") and keyframing [CHOP](<./CHOP.md> "CHOP") [channels](<./Channel.md> "Channel")
* Double click the [network](<./Network.md> "Network") and select from the [COMP](<./Component.md> "Component") tab an [Animation COMP](<./Animation_COMP.md> "Animation COMP"), place it above the [SOPs](<./SOP.md> "SOP").
  * Right click the [Animation COMP](<./Animation_COMP.md> "Animation COMP") and select Edit Animation. The animation editor should appear in the lower half of the screen.
  * On the left hand side of the [Animation Editor](<./Animation_Editor.md> "Animation Editor") there is a parameter called **Names**. Here you can enter t[xy] and then click the **Add Channels** button below to add two new channels named tx and ty to the timeline. Typing tx ty would also work.
  * The objective is to make the sphere move in a square. This would require it to move from x: 0 y: 0 to x: 1 y: 0 to x: 1 y: 1 then y 1: x: 0 before heading back to x: 0 y: 0 again.
  * Click the tx button on the left hand side of the editor to select that channel to edit. The tx channel already has 2 [keyframes](<./Keyframe.md> "Keyframe") at the beginning and end of the timeline. To add the extra 3 keyframes that will be needed alt left-click 3 times on the colored line.
  * Right click and drag to select the second keyframe in the timeline of the 5.
  * At the top of the graph there are F V S and A parameters. Set F (frame) to 100 and V (value) to 1.
  * Select the second keyframe and set F to 200 and V to 1.
  * Select the third keyframe and set F to 300 and V to 0.
  * To the right of the F, V, S and A parameters is a **Function** parameter. The Function controls how the keyframes are joined. Select the [wire](<./Wire.md> "Wire") between two keyframes by right clicking and dragging without dragging over a keyframe. You can then shift select the other wires in the channel and set their Function to be linear. The animation curve should now have straight segments.
  * On the left hand side select ty and then repeat the process only with the following values. The first keyframe should be 0 at 0 frames, the second 0 at 100 frames, the third 1 at 200 frames, the fourth 1 at 300 frames and finally the fifth 0 at 400 frames.

### Exporting the Channels to the Spheres translate parameter
* Exit the Animation Editor. Right-click the output of the Animation COMP and select a [Null CHOP](<./Null_CHOP.md> "Null CHOP").
  * Activate the viewer of the Null CHOP and drag the tx channel onto the first Transform SOPs translate x parameter (tx parameter). Drag the ty channel onto the first Transform SOPs translate y parameter (ty parameter).
  * The sphere should now be moving in a square.

### Timeline Independent Animation COMPS and Cloning
* Double click the network and under the COMP tab select an Animation COMP. Repeat this so that you have two empty Animation COMPs, place them underneath the initial Animation COMP that was placed down.
  * Select the first new empty Animation COMP and in its parameters under the Common tab there is a [Clone](<./Clone.md> "Clone") parameter. Drag the first Animation Component to this parameter and the Animation COMP should become a darkened version of itself. This indicates that this COMP is a clone of the above. A clone is a COMP which has the same contents as a master node but can have different inputs.
  * Clone the second empty Animation COMP too.
  * Like with the first Animation COMP wire these into two Null CHOPs and then export those Null CHOP channels to the second and third Sphere SOPs.

### Controlling an Animation Component with a Beat CHOP
* Double click the network to the left of the second Animation COMP and holding shift insert a [Beat CHOP](<./Beat_CHOP.md> "Beat CHOP") and a [Math CHOP](<./Math_CHOP.md> "Math CHOP").
  * Select the Math CHOP and under the Range tab set it to be **From Range** 0 to 1 and **To Range** 0 to 400.
  * Wire the Math CHOP into the first cloned Animation COMP's input.
  * Select the first cloned Animation COMP and under the Animation tab set the **Play Mode** parameter to Use Input Index. This Animation COMP is now being controlled by the Beat CHOP's **Period** parameter rather than the timeline.

### Controlling an Animation Component with a Constant CHOPs Play and Speed Channel
* Double click the network to the left of the third Animation COMP and holding shift insert a [Constant CHOP](<./Constant_CHOP.md> "Constant CHOP") and a Null CHOP.
  * Select the Constant CHOP and under the 0 tab add two new channels called _play_ and _speed_. Set play to 1 and speed to 0.5.
  * Activate the viewer of the Null CHOP and drag the play channel to the second cloned Animation COMP's **Play** parameter under the Animation tab. Export the speed channel to the **Speed** parameter.
  * Finally in the second cloned Animation COMP, set the **Play Mode** parameter to Sequential in the Animation tab.

### Finishing off, TOP Compositing
* Zoom out of the Geometry Component or click _project1_ in the path bar at the top of the network editor.
  * Right click the Render TOP's output and select an [Over TOP](<./Over_TOP.md> "Over TOP") from the TOP tab.
  * Double click the network editor and place a Constant TOP below the Render TOP.
  * Change the Constant TOP's **Color** to black and under the Common tab set the **Custom Resolution** to 1280x720.
  * Wire the output of the Constant TOP into the second input of the Over TOP.
  * Select _project1_ and under the layout tab in the parameter window set the **Width** parameter to 1280 and the **Height** parameter to 720.
