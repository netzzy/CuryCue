# Using Rim Lights

This article will walk through how to use rim lights in a 3D scene. You may follow along by loading [Media:3D_render.toe](<./images/9/98/3D_render.bin> "3D render.toe") in TouchDesigner. 

### 1 - Prepare the geometry

Rim lights are applied through the [Phong MAT](<./Phong_MAT.md> "Phong MAT") material. All geometry you wish to use with rim lights must have a Phong MAT applied. 

Make sure the geometry has [Normals](<./Normals.md> "Normals") and [Texture Coordinates](</index.php?title=Point_Attributes&action=edit&redlink=1> "Point Attributes \(page does not exist\)"). You can confirm this by inspecting the info on the SOP that is rendering (SOPs with their [Render Flag](<./Render_Flag.md> "Render Flag") on). Hold the middle-mouse button down on this SOP to preview its info, there should be attributes N[3] for normals and attributes uv[3] for texture coordinates. 

### 2 - Enable Rim Lights

On the **Rim** parameter page of the Phong MAT, there are parameters to control two separate rim lights. Turn on the checkbox for **Enable Rim Light 1**. 

At first the light effect might not be visible due to the angle the light is coming from. The **Rim Center** parameter specifies which direction the rim light is coming from. In this example, set **phong1'** s Rim Center to 0, this will make the rim light appear to come from the right side of the geometry. 

The effect might still be subtle. The **Rim Strength** parameter multiplies the effect of the rim light. Set Rim Strength = 2, the rim light should now be easily visible on the right side of the geometry. 

**Enable Rim Light 2** will turn on the second rim light. Leave it off for this example. 

### 3 - Rim Light Settings

Now that the rim light is clearly visible, play with the Rim Center parameter and watch the direction of the light change. 

The **Rim Width** parameter adjusts how 'wide' the rim light effect is on the geometry. Larger widths make the rim light cover more of the geometry, smaller widths tighten the effect of the light. Try a very small Rim Width = 0.25 and high Rim Strength = 5.0 for a strong rim light effect in this example. 

### 4 - Rim Light Color

You can adjust the main color of the rim light using the **Rim Color** parameter. 

The **Rim Color Map** can be used to get more control over the color of the rim light by using a TOP image as a color map. This Rim Color Map is applied to the geometry using the texture coordinates specified in the **Rim Map Coord** parameter. 

Remember, as with all lights in Touch, the value of the color or color map will effect the intensity of the light as well ( 50% gray (0.5,0.5,0.5) will be half the intensity of 100% white (1,1,1,) ). 

### 5 - Using the Rim Strength Ramp

The **Rim Strength Ramp** parameter can be used to gain detailed control over the strength of the rim light. The ramp needs to be a horizontal ramp image, and can be just 1 pixel in height (the ramp is sampled in u). If the ramp is more than 1 pixel in height, then the middle row of pixels is used. 

The TOP ramp assigned to Rim Strength Ramp is mapped such that the left side of the ramp (u=0) controls rim light strength where the geometry normals are facing the camera. The right side of the ramp (u=1) is the strength where normals are perpendicular to the camera.
