# Transparency

## The Short Answer  
  
There are two ways to render correct transparency:  
1\. By rendering your objects farthest to closest order and turning on blending (labor-intensive to set up). For sorting and rendering instances and individual polygons and other primitives, see the section Sorting and Blending below.  
2\. By using the "Order-Independent Transparency" feature in the [Render TOP](<./Render_TOP.md> "Render TOP") (easy but consumes more of your graphics processor). 

You can use a combination of these two (in two separate [Render TOP](<./Render_TOP.md> "Render TOP") and [Render Pass TOP](<./Render_Pass_TOP.md> "Render Pass TOP")) if the situation requires it. 

### Sorting Geometry Objects

To render multiple Geometry objects that have some transparency: 
* Turn on 'Blending' in the 'Common' page of the MATs for objects you want to be transparent.
  * Adjust the draw order of the transparent objects to ensure they are drawn in farthest to closest order. This is usually done on the 'Render' page of the [Geometry COMP](<./Geometry_COMP.md> "Geometry COMP") by adjusting the 'Draw Priority' parameter. A lower value means it will be drawn later, so closer objects should have a lower value than farther objects.


Draw all of your opaque geometry first in a [Render TOP](<./Render_TOP.md> "Render TOP") (or [Render Pass TOP](<./Render_Pass_TOP.md> "Render Pass TOP")). If you want maximum speed try and make sure these opaque objects are drawn in closest to farthest order. Then in another Render Pass TOP, draw all of your transparent objects in farthest to closest order, and turn on Alpha Blending in the Common page of all of their MATs (This is important!). If all of your geometry is transparent, then you can ignore the first render and just render all of your geometry in farthest to closest order in the first Render TOP. You can control the draw order of your geometry by using the "Draw Priority" parameter in the [Geometry COMP](<./Geometry_COMP.md> "Geometry COMP"). 

This technique is very fast but is labor intensive to set up. The simple case is when the position of the camera and geometry is static, however once the camera or geometry is moving then the Draw Priority parameters need to be set dynamically. The following file shows a number of scenarios 

**Example File :** [File:Transparency Sorting.toe](</File:Transparency_Sorting.toe> "File:Transparency Sorting.toe")
* _/sorting_static_ \- this network shows a simple statically sorted scene.
  * _/sorting_static_overlay_ \- this network shows incorrect sorting of geometry. Since the Draw Priority is static, when the blue pyramid goes from in-front to behind the other geometry it will disappear because it is not drawn before the other objects.
  * _/sorting_dynamic_overlay_ \- this network shows dynamically changing Draw Priority parameters calculated from the objects distance to the camera. This keeps the geometry draw order sorted properly at all times.

### Order-Independent Transparency

This feature is enabled in the parameter page of the [Render TOP](<./Render_TOP.md> "Render TOP"). The draw order of your geometry does not matter when this feature is enabled. You should also *not* have Alpha Blending turned on in your [MATs](<./Phong_MAT.htm#Parameters_-_Common_Page> "Phong MAT"). The number of transparency passes controls the quality of the result (more complex geometry will need more passes to be visually correct), but more passes will result in slower rendering speed. This process is multi-pass. For every pixel the closest surface is rendered in the first pass, the second closest surface second, up to the number of passes specified by the Transparency Passes parameter below. Turning this option on will disable some advanced features in the Render TOP, as well as anti-aliasing. You can use the [Anti Alias TOP](<./Anti_Alias_TOP.md> "Anti Alias TOP") instead to anti-alias your scene afterwards. 

It uses a technique called Depth Peeling. First you render the normal frame. On your next render you peel away all of the pixels you saw in the first frame, and reveal the pixels underneath them. The next frame you do the same, peeling away the pixels you could see from the 2nd render. And so on. Once all of the renders are done, you re composite each layer Over the other, starting at the farthest back layer. 

If you take a sphere for example, you'll need to do 2 passes, the first one for the front of the sphere, and then 2nd will be the inside of the sphere. 

If you have 10 spheres, one behind the other. You'll need 19-20 passes to get the correct image. 

If you have 10 spheres, each next to each other across the screen, you'll only need 2 passes. 

In reality though you will only need 3-5 passes to get an image that's acceptable. It may not be 100% correct, but it'll look pretty close to correct. Each pass is a full render, so each pass adds significant overhead. 

The following file shows a number of Order-Independent scenarios: 

**Example File :** [File:Transparency Order Independant.toe](</File:Transparency_Order_Independant.toe> "File:Transparency Order Independant.toe")
* _/order_independant_transparency_ \- a simple example, toggle the **Transparency** parameter from **Order Independent-Transparency** to **Sorted Draw with Blending** and back [Render TOP](<./Render_TOP.md> "Render TOP") to see the effect enabled and disabled..
  * _/order_indpt_trans_passes2_ \- in this network, only 2 transparency passes are required. Since none of the objects overlap, a pass is required only for the front face and the back face of the transparent objects.
  * _/order_indpt_trans_passes5_ \- in this network the transparent objects are overlapping such that at times there are 5 polygon faces displayed a certain pixels. For this reason, the transparency passes must be turned up to 5 to achieve proper transparency rendering. Adjust the number of passes and the effect of of this parameter will become obvious in this example. More complex scenes can quickly become very taxing on the GPU using this method and a high number of passes.

### Alpha-to-Coverage

Alpha-to-coverage is a hacky way of getting fake transparency in very busy scenes. When this is enabled the alpha value of rendered pixels will control how many sub-samples of the antialiasing buffer will be used to generate a pixels final color. For example when using an 8x antialias there are 8 possible sub-samples per pixel used to build up it's final color. With alpha to coverage an output alpha of 0.5 means only up to 4 of those pixels will get used, if the geometry covers all 8 sub-samples. It's situational when this mode of transparency works, usually just with very busy particles systems. 

## The Complete Answer

A common misconception about OpenGL is that it supports transparency by simply applying alpha to geometry. This is incorrect as there is no feature in OpenGL that implicitly does transparency. 

Transparency in OpenGL is created using a feature called Alpha-Blending. It is essentially using the alpha of the rendered geometry as a blend factor to blend with other geometry in the scene. Transparency is blending the color of objects farther away with the color of objects that are closer. To do this correctly the farther away objects need to be drawn already, so the closer objects have that color available to blend with. If done correctly this makes the objects look transparent (or translucent if so desired). 

What makes transparency tricky in OpenGL is the [Depth-Test](<./Depth-Test.md> "Depth-Test"). The [Depth-Test](<./Depth-Test.md> "Depth-Test") is how OpenGL makes geometry that is closer to the camera occlude geometry that is farther from the camera, regardless of which geometry is drawn first. If an object that is close to the camera has been drawn, and then one that is farther away (and behind the already drawn one) gets drawn, the Depth-Test will not draw pixels of the 2nd object that is occluded by the 1st object. 

What this means for transparency is you need to draw your farthest geometry first. By drawing in farthest to closest order, it ensures that every pixel gets drawn so when the closer geometry is drawn, it has color information from the farther geometry to blend with. You can think of transparency as a bunch of Over composite operations. 

An example of what happens with blending when geometry aren't drawn in the correct order: Lets say you are drawing the closer geometry first with an alpha of 0.0. The geometry will get rendered and blended with what’s currently drawn. 

Let's say it's a red background. So the result will be 100% red. Next you draw the farther geometry. Since the closer geometry has already being drawn, its depth values are already in the depth buffer. The farther geometry won’t get rendered because the GPU will determine that it is occluded by the closer geometry. 

## Setting Alpha Values

### Controlling Alpha

The alpha value for geometry is the 4th component of the Cd attribute. (This is different than [Houdini](<http://sidefx.com>), which uses a separate attribute called 'Alpha' for its alpha. Geometry imported from Houdini that has an Alpha attribute will be automatically converted to TouchDesigner's alpha format.) 

You can control the alpha of your geometry in many places. 
* [Primitive SOP](<./Primitive_SOP.md> "Primitive SOP") \- The primitive attribute SOP where you can set alpha per primitive.
  * [Point SOP](<./Point_SOP.md> "Point SOP") \- The point attribute SOP where you can set alpha point-by-point.
  * [Vertex SOP](<./Vertex_SOP.md> "Vertex SOP") \- The vertex attribute SOP where you can set alpha vertex-by-vertex.


Along with geometric alpha, alpha can also be applied using: 
* Various Maps in your Materials.
  * Alpha parameters in your Materials (The Alpha Page in the Phong MAT for example)


See [MATs](<./MAT.md> "MAT") for a list of Material operators. 

The various sources of alpha will all be multiplied together to obtain the geometry's final alpha (this is done per-pixel when rendering). 

The following example demonstrates the various methods to set geomtery's alpha [File:Controlling alpha.tox](</File:Controlling_alpha.tox> "File:Controlling alpha.tox")

## Sorting and Blending

### OpenGL Rendering and Alpha

The sorting of primitives within a SOP and sorting the draw order of Components is critical for controlling alpha blending. Sorting primitives is important when the SOP's geometry needs to be blended correctly with itself. A transparent box or sphere where you want to see both the near and far sides for example. It may not be possible to correctly sort some primitives. For example, a long curving mesh is a single primitive and may be impossible to render correctly with blending if it curves back onto itself. Sorting of Components is important when one SOP need to be blended with another SOP. This is the more common case. 

### Draw Order

Geometry is passed to the OpenGL render pipeline based on the following order. First, based on which Components the SOPs reside in (and the Draw Priority of those Components) geometry is rendered one SOP at a time. Within that SOP, the primitives are rendered based on their primitive order, lower primitive numbers are rendered first. 

#### Sorting SOPs in Geometry Objects (Draw Priority)

In TouchDesigner, a Component's "Draw Priority" parameter allows you to set the drawing order. Objects with higher Draw Priority values are drawn first. 

The priority can automatically be set by exporting the TZ channel of an [Object CHOP](<./Object_CHOP.md> "Object CHOP"), where the camera is the Reference Object and your transparent objects are the Target Objects. Since in TouchDesigner you can have Components within Components, draw priority works in a hierarchical manner. This means starting at the top level, for each Component listed in the Render TOP's Geometry parameter, each Component's draw priority is compared with the other Components listed in the Geometry parameter, and they are dealt with in order. 

If there are other Components within each Component, their draw priorities are compared and they in turn are dealt with in order. **IMPORTANT** : Essentially Draw Priority will control how a Component is rendered versus its siblings. It doesn't control how that Component is rendered versus other Component in the scene that are located in other components. 

So for example if you have two trees of Objects you are rendering, one located in`/character1/geo`and one located in`/character2/geo`, and you have them listed in the Render TOP as '`/character1/geo /character2/geo`' this is what happens: 

Lets say`/character1/geo`has a draw priority of 1 and`/character2/geo`has a draw priority of 0. In this case everything inside of`/character1/geo`will get rendered first, followed by everything inside`/character2/geo`. 

The Components that are inside both '`geo`' components will also have draw priorities, but regardless of their value, it's not possible for something inside`/character2/geo/`to be drawn before`/character1/geo/`because *everything* inside`/character1/geo`will get drawn first, since it has a higher draw priority than`/character2/geo`. 

#### Sorting Primitives in a SOP

The sorting inside a SOP is controlled by the primitive number. Lower numbered primitives are rendered first. The [Sort SOP](<./Sort_SOP.md> "Sort SOP") is the key to controlling the order primitives rendered. The Sort SOP can sort primitives by depth, relative to a selectable camera, among other options. This technique is also slow so it's not advisable to have this node cooking every frame. 

As mentioned earlier primitive sorting doesn't work for well meshes, NURBS, Beziers or other patches, which creates problems with rotating spherical patches like a NURBs sphere. 

Often transparency within a SOP is unnecessary, so rendering artifacts caused by enabling blending and rendering a SOP can be solved by turning on [Back-Face Culling](<./Back-Face_Culling.md> "Back-Face Culling")

#### Sorting Instances in a Geometry Object

A set of instances will all be rendered in one draw call, so they will all be rendered before or after other SOPs in the file. To sort instances relative to each other, use a [Sort CHOP](<./Sort_CHOP.md> "Sort CHOP") or [Sort DAT](<./Sort_DAT.md> "Sort DAT") on the CHOP or DAT that is specifying the instance data. If your camera is looking down -Z, you can sort by the`tz`coordinate, and sort by increasing values (lowest value first). 

Since all the instances are rendered in one call, other geometry that is in front of some instances but behind other ones will not be sorted properly for transparency. 

So if instances are sorted, you don't need to do Order-Independent Transparency for that object. 

### Performance Considerations

While drawing geometry in farthest to closest order is necessary for transparency, it is the slowest way to draw geometry. Huge performance gains can be made by drawing geometry from closest to farthest. This is due to a feature available on modern graphics hardware called [Early Depth-Test](<./Early_Depth-Test.md> "Early Depth-Test"). So care must be taken that farthest to closest rendering is only used when necessary. 

## Order Independent Transparency

When using Order Independent Transparency, the results will only be seen in the Render TOP. They will not be visible in the Geometry Viewer/Geometry Viewport. 

Sorting geometry/primitives does not help when using this feature, so that work can be avoided. 

## Alpha Blend Function Revealed

These settings are available on all [MAT's common page](<./MAT_Common_Page.md> "MAT Common Page"). 

These settings aren't very easy to understand, but if you are patient and read the descriptions and examples for each factor, you will fully grasp how to use them. This documentation gives you a basis for experimentation, while the examples show some usable results. 

With the OpenGL blending function, pixels can be drawn using a function that blends the incoming (source) RGBA values with the RGBA values that are already in the frame buffer (the destination values). Therefore, it is important to know how TouchDesigner determines what order polygons are sent through the render pipeline, and how the already rendered pixel information is combined with incoming geometry, material attributes and texture maps, to create the final pixel color. 

The OpenGL blend function provides for different ways to combine the rendered colors with what colors are already present in the buffer. Different factors can determine what the final source color and the final destination color are. Then the modified source and destination values are added together to form the new color. To understand how to use these factors, it is important to understand the components of this function. They are as follows. 
* **(Rs, Gs, Bs, As) Source Color** \- comes from the material parameter settings and the texture map colors.
  * **(Rd, Gd, Bd, Ad) Destination Color** \- is the current color held in the buffer, and eventually combined and replaced as the final color of the pixel.
  * **(Sr,Sg,Sb,Sa) Source Factor** \- is determined by the Source Blend menu.
  * **(Dr,Dg,Db,Da) Destination Factor** \- is determined by the Dest Blend menu.


The blended function holds together as follows. 
[code] 
    R = (Rs * Sr) + (Rd * Dr)
    G = (Gs * Sg) + (Gd * Dg)
    B = (Bs * Sb) + (Bd * Db)
    A = (As * Sa) + (Ad * Da)
    
[/code]

Or more simply 
[code](Source Color * Source Factor) + (Current Destination Color * Destination Factor) = Final Destination Color
    
[/code]

## Source Blend Factors

All of the source blend factors are multiplied by the RGBA of the source color, regardless of which option is chosen. For example if Dest Alpha is chosen the RGB and A of the color color will be multiplied by the Dest Alpha. 

### One - (Default)

The source blend factor is set to one. 

The source color that comes from the material and texture map is multiplied by one. 

Standard transparency is best implemented using this blend function with primitives sorted from farthest to nearest. This is the default setting because our MATs by default will post-multiply the source color by it's own alpha at the end of the shader. If you turn off this feature in the MAT (Like in the Alpha page of the Phong MAT), or are using a shader that doesn't do this, you'll want to use Source Alpha as your Source Factor. 

### Zero

The source blend factor is set to zero. 

The Source Color (Rs,Gs,Bs,As) is multiplied by (0,0,0,0). This effectively removes any source color from the alpha blend function, leaving only the Destination Color and Destination Factor for creating a final pixel color. 

### Dest Color

The source blend factor is set to the destination color value. 

The Source Color (Rs,Gs,Bs,As) is multiplied by (Rd,Gd,Bd,Ad). 

### One Minus Dest Color

The source blend factor is set to one minus the destination alpha value. 

The Source Color (Rs,Gs,Bs,As) is multiplied by (1 - Rd, 1 - Gd, 1 - Bd, 1 - Ad). 

### Src Alpha

The source blend factor is set to the alpha of the source color. 

The Source Color (Rs,Gs,Bs,As) is multiplied by (As,As,As,As) 

### One Minus Src Alpha

The source blend factor is set to the alpha of the source color and then subtracted from one. 

The Source Color (Rs,Gs,Bs,As) is multiplied by (1 - As, 1 - As, 1 - As, 1 - As) 

### Dest Alpha

The source blend factor is set to the destination alpha value. 

The Source Color (Rs,Gs,Bs,As) is multiplied by (Ad,Ad,Ad,Ad) 

### One Minus Dest Alpha

The source blend factor is set to the destination alpha value subtracted from one. 

The Source Color (Rs,Gs,Bs,As) is multiplied by (1 - Ad, 1 - Ad, 1 - Ad, 1 - Ad) 

## Destination Blend Factors

### One

The destination blend factor is set to one. 

The destination color (Rd,Gd,Bd,Ad) is multiplied by (1,1,1,1). 

### Src Color

The destination blend factor is set to the source color. 

The destination color (Rd,Gd,Bd,Ad) is multiplied by (Rs,Gs,Bs,As). 

### One Minus Src Color

The destination blend factor is set to the source color subtracted from one. 

The destination color (Rd,Gd,Bd,Ad) is multiplied by (1 - Rs, 1 - Gs, 1 - Bs, 1 - As). 

### Src Alpha

The destination blend factor is set to the source alpha. 

The destination color (Rd,Gd,Bd,Ad) is multiplied by (As,As,As,As). 

### One Minus Src Alpha - (Default)

The destination blend factor is set to the source alpha subtracted from one. 

The destination color (Rd,Gd,Bd,Ad) is multiplied by (1 - As, 1 - As, 1 - As, 1 - As). 

Standard transparency is best implemented using this blend function with primitives sorted from farthest to nearest. 

### Dest Alpha

The destination blend factor is set to the destination alpha value. 

The destination color (Rd,Gd,Bd,Ad) is multiplied by (Ad,Ad,Ad,Ad). 

### One Minus Dest Alpha

The destination blend factor is set to the destination alpha value subtracted from one. 

The destination color (Rd,Gd,Bd,Ad) is multiplied by (1 - Ad, 1 - Ad, 1 - Ad, 1 - Ad). 

### Zero

The destination blend factor is set to zero. 

The Destination Color (Rd,Gd,Bd,Ad) is multiplied by (0,0,0,0). 

This effectively replaces all of the pixel values from the current buffer and replaces them with black.
