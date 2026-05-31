# Why is My Render Black

Often, your [Render TOP](<./Render_TOP.md> "Render TOP") is all black, though you expect to see something there. Here's are things to try to find out why you don't see what you expect. 
* Check to see if anything is being rendered: Go to Edit -> Preferences on the TOPs page, the Viewer Background is set to show Checker Board as the background (vs Black). 
    * Then in your Render TOP, if you see all-checkerboard, then there is indeed nothing rendering there. If it has black, there there is something rendering but isn't getting lit.
    * Add a light, and make sure it is in front of the geometry.
    * Change the material of the object to have Emit color, or Ambient color. Or change the Material to a [Constant MAT](<./Constant_MAT.md> "Constant MAT") with a default white color.
  * Maybe the geometry is outside the field of view of the camera. Change the Render TOP's Render Mode parameter to Cube Map. Here you see in all directions. If you see nothing in the Cube Map render....
  * The next thing to look at is Near and Far clipping planes of the camera. In your [Camera COMP](<./Camera_COMP.md> "Camera COMP"), is your Near and Far parameter set to reasonable values that bound your 3D geometry? For large scenes witeh cameras at distances over 1000, your geometry may be outside the near/far clipping planes.
  * Next it's time to check what's rendering...
  * Check the Geometry parameter of the Render TOP. It should have a pattern to all your expected objects to render. To make sure you catch everything, put "*" into the Geometry parameter. If you still see nothing.... 
    * Check that you are rendering Geometry components. On the Geometry components you expect to see, make sure their Render flag is on (purple).
    * That's not enough. The Geometry components also have a Render parameter. Make sure the Render parameter is on.
    * And that is not enough. For each [Geometry COMP](<./Geometry_COMP.md> "Geometry COMP"), inside the component, make sure, for all the SOPs in your network that you expecting to render, that the Render flag is on at the bottom of the node.
    * If you have done all that and you still see nothing, check the SOP that you expect to see: 
      * Middle mouse click to see the info on the SOP. Is the bounding box what you expect? 
        * Check to see if there is point or vertex color, in particular, make sure alpha is not set to 0. Or it's all black.
        * One way to see the numbers in your SOP is to attach the SOP to a "[SOP to DAT](<./SOP_to_DAT.md> "SOP to DAT")" operator and look at the different columns. Sometimes Normals that are 0 will give black results.
      * If you still see nothing, put a Sphere SOP in your network and turn on its Render flag (and Display flag, so you can see it in a camera viewer).
* For lights to have an effect, the display flag in the lights needs to be on.
  * Make sure Materials of your objects have a non-0 Alpha parameter setting.
  * Make sure Materials that have texture maps contain textures with non-0 alpha. Replace your textures with white Constant TOPs.
  * Lights/cameras cannot be nested in [Base COMPs](<./Base_COMP.md> "Base COMP"), as a base will exclude them from the [Geometry Viewer](<./Geometry_Viewer.md> "Geometry Viewer").
  * It might also be the case that the network path of the geometry viewer is not at a level from where all lights are visible.
* You may want to replace the Camera that the Render TOP is using with a default Camera COMP.
  * Try creating a new empty Render TOP, then adding in the objects / cameras that you expect to see. Try creating a default GeometryCOMP, default Light COMP.
  * Other things ... [Back-Face Culling](<./Back-Face_Culling.md> "Back-Face Culling"), Blend Modes on Render TOP (though unlikely)
