# Rendering Shadows

This article will walk through how to render shadows in a 3D scene. You may follow along by loading [Media:3D_render.toe](<./images/9/98/3D_render.bin> "3D render.toe") in TouchDesigner. Jump to the end of the article for the completed shadow example. 

### Step 1 - Turn on Shadows

In the light1, go to it's 'Shadows' parameter page and change the Shadow Type to 'Hard, 2D Mapped'. You'll see shadows but they don't quite look right. This is because geometry from the light/camera is casting a shadow. Change the 'Shadow Casters' parameter to be just geo1 instead of * and only the objects in geo1 will cast a shadow. 

### Step 2 - Removing Shadow Artifacts

Sometimes there is a "moire" effect artifact covering the geometry with the default settings for the shadows. There won't be in this case, but you can see them if you change the Polygon Offset Factor in the light's shadow parameter to something lower. If you experience these artifacts you will need to adjust the polygon offset values until they go away. 

### Step 3 - Shadow Detail

Shadow detail can be optimized by adjusting the shadow map to use its resolution most effectively. Using the light's **Focal Length** and **Aperture** parameters (or FOV), try to fill as much of the depth map as possible with the geometry. 

You can visualize what the shadow map looks like by pointing a [Depth TOP](<./Depth_TOP.md> "Depth TOP") at the light. The shadow map may be very faint, too faint to see the geometry (the depth data is still valid, but the floating point values may be too hard to see visually in the image). Increase the light's **Near** parameter until the geometry is visible. For _light1_ , a value of 2 works in this example. 

Now adjust Focal Length and/or Aperture until the geometry fills the maximum amount of the depth map. While adjusting these parameters, watch the viewer of the _depth1_ TOP and inspect the shadow's detail. Go as far as possible without clipping the shadows. Return _light1'_ s Near parameter to the previous value when done. 

TIP: Double-check animated scenes when changing these settings. 

### Step 4 - Tweaking other Shadow Parameters

On`phong1`'s **Advanced** parameter page, experiment with the **Shadow Strength** and **Shadow Color** parameters. Notice this only effects the shadows on that material, and the shadows that are cast on the floor do not change with`phong1`. To change those, adjust the material at`/3D_render/stage/mat_floor`[Media:Shadow_example.toe](<./images/7/7f/Shadow_example.bin> "Shadow example.toe") \- the example file with shadows.
