# Camera COMP

##   
  
Summary

The Camera Component is a 3D object that behaves like a real-world camera. You view your scene through it and render from its point of view using a [Render TOP](<./Render_TOP.md> "Render TOP"). 

See [Geometry Viewer](<./Geometry_Viewer.md> "Geometry Viewer") to learn about how you can inspect a scene from a camera. 

See [cameraViewport](<./Palette-camera.md> "Palette:camera") in the Palette \- it's a powerful interactive camera that can be used in place of the basic Camera COMP. 

A Camera Component can be attached or linked to any other 3D Component in a [3D hierarchy](<./3D_Parenting.md> "3D Parenting"). 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[cameraCOMP_Class](<./CameraCOMP_Class.md> "CameraCOMP Class")

## 

Parameters - Xform Page

The Xform parameter page controls the object component's transform in world space. 

Transform Order`xord`\- ⊞ \- This allows you to specify the order in which the changes to your Component will take place. Changing the Transform Order will change where things go much the same way as going a block and turning east gets you to a different place than turning east and then going a block. In matrix math terms, if we use the 'multiply vector on the right' (column vector) convention, a transform order of Scale, Rotate, Translate would be written as`T * R * S * Position`. 
* Scale Rotate Translate`srt`-
* Scale Translate Rotate`str`-
* Rotate Scale Translate`rst`-
* Rotate Translate Scale`rts`-
* Translate Scale Rotate`tsr`-
* Translate Rotate Scale`trs`-


Rotate Order`rord`\- ⊞ \- This allows you to set the transform order for the Component's rotations. As with transform order (above), changing the order in which the Component's rotations take place will alter the Component's final position. A Rotation order of Rx Ry Rz would create the final rotation matrix as follows`R = Rz * Ry * Rx`* Rx Ry Rz`xyz`\-`R = Rz * Ry * Rx`* Rx Rz Ry`xzy`\-`R = Ry * Rz * Rx`* Ry Rx Rz`yxz`\-`R = Rz * Rx * Ry`* Ry Rz Rx`yzx`\-`R = Rx * Rz * Ry`* Rz Rx Ry`zxy`\-`R = Ry * Rx * Rz`* Rz Ry Rx`zyx`\-`R = Rx * Ry * Rz`Translate`t`\- ⊞ \- This allows you to specify the amount of movement along any of the three axes; the amount, in degrees, of rotation around any of the three axes; and a non-uniform scaling along the three axes. As an alternative to entering the values directly into these fields, you can modify the values by manipulating the Component in the Viewport with the Select & Transform state. 
* X`tx`-
* Y`ty`-
* Z`tz`-


Rotate`r`\- ⊞ \- Theis specifies the amount of movement along any of the three axes; the amount, in degrees, of rotation around any of the three axes; and a non-uniform scaling along the three axes. As an alternative to entering the values directly into these fields, you can modify the values by manipulating the Component in the Viewport with the Select & Transform state. 
* X`rx`-
* Y`ry`-
* Z`rz`-


Scale`s`\- ⊞ \- This specifies the amount of movement along any of the three axes; the amount, in degrees, of rotation around any of the three axes; and a non-uniform scaling along the three axes. As an alternative to entering the values directly into these fields, you can modify the values by manipulating the Component in the Viewport with the Select & Transform state. 
* X`sx`-
* Y`sy`-
* Z`sz`-


Pivot`p`\- ⊞ \- The Pivot point edit fields allow you to define the point about which a Component scales and rotates. Altering the pivot point of a Component produces different results depending on the transformation performed on the Component. 

For example, during a scaling operation, if the pivot point of an Component is located at`-1, -1, 0`and you wanted to scale the Component by`0.5`(reduce its size by 50%), the Component would scale toward the pivot point and appear to slide down and to the left. 

In the example above, rotations performed on an Component with different pivot points produce very different results. 
* X`px`-
* Y`py`-
* Z`pz`-


Uniform Scale`scale`\- This field allows you to change the size of an Component uniformly along the three axes. 

> **Note:** Scaling a camera's channels is not generally recommended. However, should you decide to do so, the rendered output will match the Viewport as closely as possible when scales are involved.

Parent Transform Source`parentxformsrc`\- ⊞ \- _**NOTE:** This parameter replaces the previous '**Constrain To'** parameter._ Use 'Parent Transform Source' and to specify what initial position is used for this object. Can be one of "Parent (Hierarchy)", "Specify Parent Object", or "World Origin". 
* From Parent Object (Hierarchy)`hierarchy`-
* Specify Parent Object`specify`-
* World Origin`worldorigin`-


Parent Object`parentobject`\- Allows the location of the object to be constrained to any other object whose path is specified in this parameter. 

Look At`lookat`\- Allows you to orient this Component by naming another 3D Component you would like it to Look At, or point to. Once you have designated this Component to look at, it will continue to face that Component, even if you move it. This is useful if, for instance, you want a camera to follow another Component's movements. The Look At parameter points the Component in question at the other Component's origin. 

> **Tip:** To designate a center of interest for the camera that doesn't appear in your scene, create a Null Component and disable its display flag. Then Parent the Camera to the newly created Null Component, and tell the camera to look at this Component using the Look At parameter. You can direct the attention of the camera by moving the Null Component with the Select state. If you want to see both the camera and the Null Component, enable the Null Component's display flag, and use the Select state in an additional Viewport by clicking one of the icons in the top-right corner of the TouchDesigner window.

Forward Direction`forwarddir`\- ⊞ \- Sets which axis and direction is considered the forward direction. 
* +X`posx`-
* -X`negx`-
* +Y`posy`-
* -Y`negy`-
* +Z`posz`-
* -Z`negz`-


Look At Up Vector`lookup`\- ⊞ \- When specifying a Look At, it is possible to specify an up vector for the lookat. Without using an up vector, it is possible to get poor animation when the lookat Component, for example, passes through the Y axis of the target Component. 
* Don't Use Up Vector \- Use this option if the look at Component does not pass through the Y axis of the target Component.
  * Use Up Vector \- This precisely defines the rotates on the Component doing the looking. The Up Vector specified should not be parallel to the look at direction. See Up Vector below.
  * Use Quaternions \- Quaternions are a mathematical representation of a 3D rotation. This method finds the most efficient means of moving from one point to another on a sphere.
* Don't use up vector`off`-
* Use up vector`on`-
* Use quaternions`quat`-
* Use Roll`roll`-


Path SOP`pathsop`\- Names the SOP that functions as the path you want this Component to move along. For instance, you can name a SOP that provides a path for the camera to follow. 

Roll`roll`\- Using the angle control you can specify a Component's rotation as it animates along the path. 

Position`pos`\- This parameter lets you specify the Position of the Component along the path. The values you can enter for this parameter range from`0`to`1`, where`0`equals the starting point and`1`equals the end point of the path. The value slider allows for values as high as`10`for multiple "passes" along the path. 

Orient along Path`pathorient`\- If this option is selected, the Component will be oriented along the path. The positive Z axis of the Component will be pointing down the path. 

Orient Up Vector`up`\- ⊞ \- When orienting a Component, the Up Vector is used to determine where the positive Y axis points. 
* X`upx`-
* Y`upy`-
* Z`upz`-


Auto-Bank Factor`bank`\- The Auto-Bank Factor rolls the Component based on the curvature of the path at its current position. To turn off auto-banking, set the bank scale to`0`. 

## 

Parameters - Pre-Xform Page

The Pre-Xform parameter page applies a transform to the object component the same way connecting another [Object](<./Object.md> "Object") as a parent of this node does. The transform is applied to the left of the [Xform](<./Object_COMP_Xform_Page.md> "Object COMP Xform Page") page's parameters. In terms of matrix math, if we use the 'multiply on the right' (column vector) convention, the equation would be`preXForm * xform * Position`. 

Apply Pre-Transform`pxform`\- Enables the transformation on this page. 

Transform Order`pxord`\- ⊞ \- Refer to the documentation on Xform page for more information. 
* Scale Rotate Translate`srt`-
* Scale Translate Rotate`str`-
* Rotate Scale Translate`rst`-
* Rotate Translate Scale`rts`-
* Translate Scale Rotate`tsr`-
* Translate Rotate Scale`trs`-


Rotate Order`prord`\- ⊞ \- Refer to the documentation on Xform page for more information. 
* Rx Ry Rz`xyz`-
* Rx Rz Ry`xzy`-
* Ry Rx Rz`yxz`-
* Ry Rz Rx`yzx`-
* Rz Rx Ry`zxy`-
* Rz Ry Rx`zyx`-


Translate`pt`\- ⊞ \- Refer to the documentation on Xform page for more information. 
* X`ptx`-
* Y`pty`-
* Z`ptz`-


Rotate`pr`\- ⊞ \- Refer to the documentation on Xform page for more information. 
* X`prx`-
* Y`pry`-
* Z`prz`-


Scale`ps`\- ⊞ \- Refer to the documentation on Xform page for more information. 
* X`psx`-
* Y`psy`-
* Z`psz`-


Pivot`pp`\- ⊞ \- Refer to the documentation on Xform page for more information. 
* X`ppx`-
* Y`ppy`-
* Z`ppz`-


Uniform Scale`pscale`\- Refer to the documentation on Xform page for more information. 

Reset Transform`preset`\- This button will reset this page's transform so it has no translate/rotate/scale. 

Commit to Main Transform`pcommit`\- This button will copy the transform from this page to the main Xform page, and reset this page's transform. 

Xform Matrix/CHOP/DAT`xformmatrixop`\- This parameter can be used to transform using a 4x4 matrix directly. For information on ways to specify a matrix directly, refer to the [Matrix Parameters](<./Matrix_Parameters.md> "Matrix Parameters") page. This transform will be applied after the regular Pre-Transform transformation. That is, it'll be applied in the oder XformMatrix * PreXForm * Position. 

## 

Parameters - View Page

Projection`projection`\- ⊞ \- A pop-up menu lets you choose from Perspective and Orthographic projection types. A third option Perpective to Ortho Blend enables the Projection Blend parameter below which can be used to blend between perspectives. A 4th option Custom Projection Matrix allows you to specify a custom 4x4 projection matrix using a tdu.Matrix, CHOP or a DAT. 
* Perspective`perspective`-
* Orthographic`ortho`-
* Perspective to Ortho Blend`persporthoblend`-
* Custom Projection Matrix`custommatrix`-


Projection Blend`projectionblend`\- Blends between perspective projection and orthographic projection when the Projection parameter is set to Perspective to Ortho Blend. 

Ortho Width`orthowidth`\- Only active if Orthographic is chosen from the Projection pop-up menu. This specifies the width of the orthographic projection. 

Viewing Angle Method`viewanglemethod`\- ⊞ \- This menu determines which method is used to define the camera's angle of view. 
* Horizontal FOV`horzfov`\- Uses the FOV Angle parameter below to set the camera's angle of view horizontally.
* Vertical FOV`vertfov`\- Uses the FOV Angle parameter below to set the camera's angle of view vertically.
* Focal Length and Aperture`focalaperture`\- Uses the Focal Length and Aperture parameters below to define the camera's angle of view.


FOV Angle`fov`\- The field of view (FOV) angle is the angular extend of the scene imaged by the camera. 

**Useful Equations**

Field of View and Throw Angle: The FOV would be: 

    FOV = arctan( (screenWidth / 2) / (distanceToScreen) ) * 2
    FOV = arctan( 0.5 * (screenWidth / distanceToScreen) ) * 2

Throw is: 

    Throw = distanceToScreen / screenWidth
    1/Throw = screenWidth / distanceToScreen

In terms of throw, it's 

    FOV = arctan(0.5 * (1/Throw)) * 2
    FOV = arctan(0.5 / Throw) * 2

**FOV calculations in x and y**

The above equations can be used to determine FOV_x and FOV_y (ie. horizontally and vertically) using Comera COMP parameters focal and aperture. In TouchDesigner's Camera COMP, screenWidth = aperture parameter and distanceToScreen = focal parameter (assuming infinity focus), from this 

    FOV_x = arctan( (aperture / 2) / focal) * 2

Furthermore, as mentioned above aperture parameter = aperture_x and if given the resolution in x and y of the rendered view (ie. aspect ratio) 

    aperture_y = resy/resx * aperture_x

From this 

    FOV_y = arctan( (aperture_y / 2) / focal ) * 2

Focal Length`focal`\- The parameter sets the focal length of the lens, zooming in and out. Perspective is flattened or exaggerated depending on focal length. See FOV Angle parameter for relation of aperture, focal length and field of view angle. Some interesting distortion effects can be acheived with this parameter. 

Aperture`aperture`\- This value relates to the area through which light can pass for the camera. 

Near`near`\- This control allows you to designate the near clipping planes. Geometry closer from the lens than these distances will not be visible. 

**NOTE:** If geometry in your scene is producing z-depth artifacts, increase the resolution of the camera's z-depth buffer. To do this, decrease the difference between near and far clipping planes, starting with the near plane. __

Far`far`\- This control allows you to designate the far clipping planes. Geometry further away from the lens than these distances will not be visible. 

**NOTE:** If geometry in your scene is producing z-depth artifacts, increase the resolution of the camera's z-depth buffer. To do this, decrease the difference between near and far clipping planes, starting with the near plane. __

Window Roll Pivot`winrollpivot`\- ⊞ \- 
* Viewport Origin`viewport`-
* Camera Origin`camera`-
* Legacy Behavior`legacy`-


Window X/Y`win`\- ⊞ \- These parameters define the center of the window during the rendering process. The window parameter takes the view and expands it to fit the camera's field of vision. It is important to note that this action is independent of perspective. In other words, it acts as though you are panning the camera without actually moving the camera. The units for this parameter are normalized. That is a Window X of -0.5 will move the previous center of the image to the left edge of the render. 
* X`winx`-
* Y`winy`-


Window Size`winsize`\- The Window Size parameter specifies the dimensions for expanding the view. Similar to Window X / Y, this parameter creates a zoom effect by scaling the screen before rendering to the viewport. 

Window Roll`winroll`\- This parameter sets the amount, in degrees, the window area rolls. This can be set as a static value or as an aspect that changes over the course of the animation. The roll occurs about the centre of the window. 

IPD Shift`ipdshift`\- This is the Interpupillary Distance which applies a translation on the X axis. It is separate from the other translations because when doing things such as a Cube Map rendering, the shift needs to occur after the rotation to the other cube face. If you apply the shift directly in the X translate parameter the cameras will be in the incorrect spot for many of the cube faces. 

To use the IPD with 2 cameras, the right eye camera should be set with +IPD/2 and the left eye camera to -IPD/2. __

Proj Matrix/CHOP/DAT`projmatrixop`\- When Custom Projection Matrix is selected, this parameters should be filled in a custom 4x4 projection matrix. For ways to specify a matrix in a parameter, refer to the [Matrix Parameters](<./Matrix_Parameters.md> "Matrix Parameters") article. The projection matrix should generate depth values in Vulkan depth clip range [0,1], not OpenGL clip range [-1,1]. 

Custom Projection GLSL DAT`customproj`\- Takes a DAT containing a GLSL shader to specify custom projection functions. You must provide one functions in this shader. As a starting point, here are the definitions for the function that is used when custom ones are not provided. This will only be used when the Render TOP is rendering a 2D output, not cubemaps or fisheye renders. Note that projection works using Vulkan depth clip range [0,1], not OpenGL's [-1,1]. So the position will be clipped when z is outside the range 0 <= z <= w. 
[code]
     vec4 UserWorldToProj(vec4 worldSpaceVertPosition, int cameraIndex)			
     {			
         vec4 projP = uTDMats[cameraIndex].camProj * worldSpaceVertPosition;			
         return projP;			
     }			
    
[/code]`vec3 TDWorldToProj()`will automatically call this at the appropriate point. You can use uniforms/samplers in this shader code by declaring them here and providing them in the GLSL page of the [Render TOP](<./Render_TOP.md> "Render TOP"). __

Quad Reproject SOP`quadreprojsop`\- [Quad Reprojection](<./Quad_Reprojection.md> "Quad Reprojection") is a feature that allows reprojection an arbitrary quad in the scene so that portion of the render where it ends up will be blown up to fill the output of the render. Refer to the [Quad Reprojection](<./Quad_Reprojection.md> "Quad Reprojection") article for more information about this feature. 

Quad Reproject Points`quadreprojpts`\- ⊞ \- Specifies 4 point indices in the SOP referenced by Quad Reproject SOP that make up the quad that determines the region to be reprojected. The indices should be listed in bottom left, bottom right, top left, top right order, as viewed from the camera. The SOP that is referenced should be in the COMP that is being rendered, so the world transform that will be applied to is can be taken into account. 
* Quad Reproject Points 1`quadreprojpts1`-
* Quad Reproject Points 2`quadreprojpts2`-
* Quad Reproject Points 3`quadreprojpts3`-
* Quad Reproject Points 4`quadreprojpts4`-

## 

Parameters - Settings Page

Background Color`bgcolor`\- ⊞ \- Sets the background color and alpha of the camera's view. 
* Red`bgcolorr`-
* Green`bgcolorg`-
* Blue`bgcolorb`-
* Alpha`bgcolora`-


Pre-Multiply RGB by Alpha`premultrgbbyalpha`\- This option allows the Background Color to be pre-multiplied by alpha. 

Fog`fog`\- ⊞ \- This menu determines the type of fog rendered in the viewport: **Linear** fog uses the following equation: 

**Exponential** fog uses the following equation: 

**Squared Exponential** fog uses the following equation: 
* Off`off`-
* Linear`linear`-
* Exponential`exp`-
* Squared Exponential`exp2`-


Fog Density`fogdensity`\- A value that specifies density or thickness, used in both exponential fog types. Only non-negative densities are accepted. 

Fog Near`fognear`\- The starting distance of the fog. If geometry is closer to the camera than this distance, fog will not be calculated in the color of the geometry. Used in the linear fog equation. 

Fog Far`fogfar`\- The far distance used in the linear fog equation. 

Fog Color`fogcolor`\- ⊞ \- The color of the fog. 
* Red`fogcolorr`-
* Green`fogcolorg`-
* Blue`fogcolorb`-


Fog Alpha`fogalpha`\- Used to control the background opacity of the scene. 

Fog Map`fogmap`\- Use a TOP texture as a color map for the fog. 

Camera Light Mask`camlightmask`\- Allows only specific [lights](<./Light_COMP.md> "Light COMP") to be used by this camera. This is used in conjunction with the Lights parameter in the Render TOP to determine what lights are used to illuminate the geometry. When this parameter is left blank, all lights specified in the Render TOP will be used. Lights specified in this parameter will limit the geometry's lighting with this camera to the light(s)specified assuming the light(s) is also listed in the Render TOP. 

## 

Parameters - Render Page

The Display parameter page controls the component's [material](</index.php?title=Material&action=edit&redlink=1> "Material \(page does not exist\)") and [rendering](<./Rendering.md> "Rendering") settings. 

Material`material`\- Selects a [MAT](<./MAT.md> "MAT") to apply to the geometry inside. 

Render`render`\- Whether the Component's geometry is visible in the [Render TOP](<./Render_TOP.md> "Render TOP"). This parameter works in conjunction (logical AND) with the Component's [Render Flag](<./Render_Flag.md> "Render Flag"). 

Draw Priority`drawpriority`\- Determines the order in which the Components are drawn. Smaller values get drawn after larger values. The value is compared with other Components in the same parent Component, or if the Component is the top level one listed in the Render TOP's 'Geometry' parameter, then against other top-level Components listed there. This value is most often used to help with [Transparency](<./Transparency.md> "Transparency"). 

Pick Priority`pickpriority`\- When using a [Render Pick CHOP](<./Render_Pick_CHOP.md> "Render Pick CHOP") or a [Render Pick DAT](<./Render_Pick_DAT.md> "Render Pick DAT"), there is an option to have a 'Search Area'. If multiple objects are found within the search area, the pick priority can be used to select one object over another. A higher value will get picked over a lower value. This does not affect draw order, or objects that are drawn over each other on the same pixel. Only one will be visible for a pick per pixel. 

Wireframe Color`wcolor`\- ⊞ \- Use the R, G, and B fields to set the Component's color when displayed in wireframe shading mode. 
* Red`wcolorr`-
* Green`wcolorg`-
* Blue`wcolorb`-


Light Mask`lightmask`\- By default all lights used in the [Render TOP](<./Render_TOP.md> "Render TOP") will affect geometry renderer. This parameter can be used to specify a sub-set of lights to be used for this particular geometry. The lights must be listed in the [Render TOP](<./Render_TOP.md> "Render TOP") as well as this parameter to be used. 

## 

Parameters - Extensions Page

The Extensions parameter page sets the component's python extensions. Please see [extensions](<./Extensions.md> "Extensions") for more information. 

Re-Init Extensions`reinitextensions`\- Recompile all extension objects. Normally extension objects are compiled only when they are referenced and their definitions have changed. 

Init Extensions On Start`initextonstart`\- Perform a Re-Init automatically when TouchDEsigner Starts 

Extension`ext`\- Sequence of info for creating extensions on this component 

Object`ext0object`\- A number of class instances that can be attached to the component. 

Name`ext0name`\- Optional name to search by, instead of the instance class name. 

Promote`ext0promote`\- Controls whether or not the extensions are visible directly at the component level, or must be accessed through the`.ext`member. Example:`n.Somefunction`vs`n.ext.Somefunction`## 

Parameters - Common Page

The Common parameter page sets the component's [node viewer](<./Node_Viewer.md> "Node Viewer") and [clone](<./Clone.md> "Clone") relationships. 

Parent Shortcut`parentshortcut`\- Specifies a name you can use anywhere inside the component as the path to that component. See [Parent Shortcut](<./Parent_Shortcut.md> "Parent Shortcut"). 

Global OP Shortcut`opshortcut`\- Specifies a name you can use anywhere at all as the path to that component. See [Global OP Shortcut](<./Global_OP_Shortcut.md> "Global OP Shortcut"). 

Internal OP`iop`\- Sequence header for internal operators. 

Shortcut`iop0shortcut`\- Specifies a name you can use anywhere inside the component as a path to "Internal OP" below. See [Internal Operators](<./Internal_Operators.md> "Internal Operators"). 

OP`iop0op`\- The path to the Internal OP inside this component. See [Internal Operators](<./Internal_Operators.md> "Internal Operators"). 

Node View`nodeview`\- ⊞ \- Determines what is displayed in the node viewer, also known as the [Node Viewer](<./Node_Viewer.md> "Node Viewer"). Some options will not be available depending on the Component type ([Object Component](<./Object_Component.md> "Object Component"), [Panel Component](<./Panel_Component.md> "Panel Component"), Misc.) 
* Default Viewer`default`\- Displays the default viewer for the component type, a 3D Viewer for Object COMPS and a Control Panel Viewer for Panel COMPs.
* Operator Viewer`opviewer`\- Displays the node viewer from any operator specified in the Operator Viewer parameter below.


Operator Viewer`opviewer`\- Select which operator's node viewer to use when the Node View parameter above is set to Operator Viewer. 

Enable Cloning`enablecloning`\- Control if the OP should be actively cloneing. Turning this off causes this node to stop cloning it's 'Clone Master'. 

Enable Cloning Pulse`enablecloningpulse`\- Instantaneously clone the contents. 

Clone Master`clone`\- Path to a component used as the Master [Clone](<./Clone.md> "Clone"). 

Load on Demand`loadondemand`\- Loads the component into memory only when required. Good to use for components that are not always used in the project. 

Enable External .tox`enableexternaltox`\- When on (default), the external .tox file will be loaded when the .toe starts and the contents of the COMP will match that of the external .tox. This can be turned off to avoid loading from the referenced external .tox on startup if desired (the contents of the COMP are instead loaded from the .toe file). Useful if you wish to have a COMP reference an external .tox but not always load from it unless you specifically push the Re-Init Network parameter button. 

Enable External .tox Pulse`enableexternaltoxpulse`\- This button will re-load from the external`.tox`file (if present). 

External .tox Path`externaltox`\- Path to a`.tox`file on disk which will source the component's contents upon start of a`.toe`. This allows for components to contain networks that can be updated independently. If the`.tox`file can not be found, whatever the`.toe`file was saved with will be loaded. 

Reload Custom Parameters`reloadcustom`\- When this checkbox is enabled, the values of the component's [Custom Parameters](<./Custom_Parameters.md> "Custom Parameters") are reloaded when the [.tox](<./.md> ".tox") is reloaded. This only affects top-level parameters on the component, all parameters on nodes inside the component are always reloaded with the [.tox](<./.md> ".tox"). 

Reload Built-In Parameters`reloadbuiltin`\- When this checkbox is enabled, the values of the component's built-in parameters are reloaded when the [.tox](<./.md> ".tox") is reloaded. This only affects top-level parameters on the component, all parameters on nodes inside the component are always reloaded with the [.tox](<./.md> ".tox"). 

Save Backup of External`savebackup`\- When this checkbox is enabled, a backup copy of the component specified by the External`.tox`parameter is saved in the`.toe`file. This backup copy will be used if the External`.tox`can not be found. This may happen if the`.tox`was renamed, deleted, or the`.toe`file is running on another computer that is missing component media. 

Sub-Component to Load`subcompname`\- When loading from an External`.tox`file, this option allows you to reach into the`.tox`and pull out a COMP and make that the top-level COMP, ignoring everything else in the file (except for the contents of that COMP). For example if a`.tox`file named`project1.tox`contains`project1/geo1`, putting`geo1`as the Sub-Component to Load, will result in`geo1`being loaded in place of the current COMP. If this parameter is blank, it just loads the`.tox`file normally using the top level COMP in the file. 

Relative File Path Behavior`relpath`\- ⊞ \- Set whether the child file paths within this COMP are relative to the .toe itself or the .tox, or inherit from parent. 
* Use Parent's Behavior`inherit`\- Inherit setting from parent.
* Relative to Project File (.toe)`project`\- The path, when specified as a relative path, will be relative to the .toe file.
* Relative to External COMP File (.tox)`externaltox`\- The path, when specified as a relative path, will be relative to the .tox file. When no external COMP file is specified, or when Enable External .tox is not toggled on, this doesn't have any impact.


Parameter Color Space`parmcolorspace`\- ⊞ \- Controls how all color parameters on this node are interpreted. The color values as treated as being in the selected color space, and are converted to the Working [Color Space](<./Color_Space.md> "Color Space") before they are used as part of the node's operation. Note that this does not change the color space of the node itself, as that is always in the Working Color Space. 
* sRGB`srgb`\- [sRGB](<https://en.wikipedia.org/wiki/SRGB>) color space, with sRGB transfer function. Considered an SDR color space with respect to Reference White.
* sRGB - Linear`srgblinear`\- [sRGB](<https://en.wikipedia.org/wiki/SRGB>) color space, with linear transfer function. Considered an SDR color space with respect to Reference White.
* Rec.601 (NTSC)`rec601ntsc`\- [Rec.601](<https://en.wikipedia.org/wiki/Rec._601>) with NTSC primaries color space, with Rec.601 transfer function. Considered an SDR color space with respect to Reference White.
* Rec.709`rec709`\- [Rec.709](<https://en.wikipedia.org/wiki/Rec._709>) color space, with Rec.709 (same as Rec.2020) transfer function. Considered an SDR color space with respect to Reference White.
* Rec.2020`rec2020`\- [Rec.2020](<https://en.wikipedia.org/wiki/Rec._2020>) color space, with Rec.2020 (same as Rec.709) transfer function. Considered an HDR color space with respect to Reference White.
* DCI-P3`dcip3`\- [DCI-P3](<https://en.wikipedia.org/wiki/DCI-P3>) color space, with D65 white point and 2.6 gamma transfer function. Considered an HDR color space with respect to Reference White.
* DCI-P3 (D60)`dcip3d60`\- [DCI-P3 "D60 sim"](<https://en.wikipedia.org/wiki/DCI-P3>) color space, with D60 white point, and 2.6 gamma transfer function. Considered an HDR color space with respect to Reference White.
* Display-P3 (D65)`displayp3d65`\- [Display-P3](<https://en.wikipedia.org/wiki/DCI-P3>) color space, with D65 white point, and sRGB gamma transfer function. Considered an HDR color space with respect to Reference White.
* ACES2065-1`aces2065-1`\- [ACES 2065-1](<https://en.wikipedia.org/wiki/Academy_Color_Encoding_System>) (also known as ACES AP0) color space, with a linear gamma transfer function. Considered an HDR color space with respect to Reference White.
* ACEScg`acescg`\- [ACEScg](<https://en.wikipedia.org/wiki/Academy_Color_Encoding_System>) (also known as ACES AP1) color space, with a linear gamma transfer function. Considered an HDR color space with respect to Reference White.
* Passthrough`passthrough`\- When selected, the color values will be used as-is in the operation, without any modification or attempt to convert them into the Working Color Space.


Parameter Reference White`parmreferencewhite`\- ⊞ \- When converting a parameter color value to the Working Color Space, this controls how it should be treated with respect to [Reference White](<./Color_Space.htm#Reference_White> "Color Space"). If the Working Color Space is the same Reference White, then no adjustment is done. If they are different, then the Reference White level (brightness) of this color will be adjusted to the range expected by the Working Color Space. For example if the project is set to have a SDR Reference White of 120 nits, and the HDR Reference White is 80 nits, then a color of (1, 1, 1), which is 120 nits in the SDR color space, will be converted to be (1.5, 1.5, 1.5), which is 120 nits still in the HDR Working Color Space. 
* Default For Color Space`default`\- Will use either the SDR or the HDR Reference White, based on the color space selected.
* Use Parent Panel`useparent`\- Will use the Reference White that the parent panel has selected. If the top-level panel also has 'Use Parent' selected, then 'UI Reference White' will be used.
* Standard (SDR)`sdr`\- Will treat the Parameter Color Space as SDR for it's reference white value.
* High (HDR)`hdr`\- Will treat the Parameter Color Space as HDR for it's reference white value.
* UI`ui`\- Will treat the Parameter Color Space as UI for it's reference white value. This uses the 'UI Reference White Nits' value for it's brightness.


Parameter Color Space`parmcolorspace`\- ⊞ \- Controls how all color parameters on this node are interpreted. The color values as treated as being in the selected color space, and are converted to the Working [Color Space](<./Color_Space.md> "Color Space") before they are used as part of the node's operation. Note that this does not change the color space of the node itself, as that is always in the Working Color Space. 
* sRGB`srgb`\- [sRGB](<https://en.wikipedia.org/wiki/SRGB>) color space, with sRGB transfer function. Considered an SDR color space with respect to Reference White.
* sRGB - Linear`srgblinear`\- [sRGB](<https://en.wikipedia.org/wiki/SRGB>) color space, with linear transfer function. Considered an SDR color space with respect to Reference White.
* Rec.601 (NTSC)`rec601ntsc`\- [Rec.601](<https://en.wikipedia.org/wiki/Rec._601>) with NTSC primaries color space, with Rec.601 transfer function. Considered an SDR color space with respect to Reference White.
* Rec.709`rec709`\- [Rec.709](<https://en.wikipedia.org/wiki/Rec._709>) color space, with Rec.709 (same as Rec.2020) transfer function. Considered an SDR color space with respect to Reference White.
* Rec.2020`rec2020`\- [Rec.2020](<https://en.wikipedia.org/wiki/Rec._2020>) color space, with Rec.2020 (same as Rec.709) transfer function. Considered an HDR color space with respect to Reference White.
* DCI-P3`dcip3`\- [DCI-P3](<https://en.wikipedia.org/wiki/DCI-P3>) color space, with D65 white point and 2.6 gamma transfer function. Considered an HDR color space with respect to Reference White.
* DCI-P3 (D60)`dcip3d60`\- [DCI-P3 "D60 sim"](<https://en.wikipedia.org/wiki/DCI-P3>) color space, with D60 white point, and 2.6 gamma transfer function. Considered an HDR color space with respect to Reference White.
* Display-P3 (D65)`displayp3d65`\- [Display-P3](<https://en.wikipedia.org/wiki/DCI-P3>) color space, with D65 white point, and sRGB gamma transfer function. Considered an HDR color space with respect to Reference White.
* ACES2065-1`aces2065-1`\- [ACES 2065-1](<https://en.wikipedia.org/wiki/Academy_Color_Encoding_System>) (also known as ACES AP0) color space, with a linear gamma transfer function. Considered an HDR color space with respect to Reference White.
* ACEScg`acescg`\- [ACEScg](<https://en.wikipedia.org/wiki/Academy_Color_Encoding_System>) (also known as ACES AP1) color space, with a linear gamma transfer function. Considered an HDR color space with respect to Reference White.
* Passthrough`passthrough`\- When selected, the color values will be used as-is in the operation, without any modification or attempt to convert them into the Working Color Space.


Parameter Reference White`parmreferencewhite`\- ⊞ \- When converting a parameter color value to the Working Color Space, this controls how it should be treated with respect to [Reference White](<./Color_Space.htm#Reference_White> "Color Space"). If the Working Color Space is the same Reference White, then no adjustment is done. If they are different, then the Reference White level (brightness) of this color will be adjusted to the range expected by the Working Color Space. For example if the project is set to have a SDR Reference White of 120 nits, and the HDR Reference White is 80 nits, then a color of (1, 1, 1), which is 120 nits in the SDR color space, will be converted to be (1.5, 1.5, 1.5), which is 120 nits still in the HDR Working Color Space. 
* Default For Color Space`default`\- Will use either the SDR or the HDR Reference White, based on the color space selected.
* Use Parent Panel`useparent`\- Will use the Reference White that the parent panel has selected. If the top-level panel also has 'Use Parent' selected, then 'UI Reference White' will be used.
* Standard (SDR)`sdr`\- Will treat the Parameter Color Space as SDR for it's reference white value.
* High (HDR)`hdr`\- Will treat the Parameter Color Space as HDR for it's reference white value.
* UI`ui`\- Will treat the Parameter Color Space as UI for it's reference white value. This uses the 'UI Reference White Nits' value for it's brightness.


Parameter Color Space`parmcolorspace`\- ⊞ \- Controls how all color parameters on this node are interpreted. The color values as treated as being in the selected color space, and are converted to the Working [Color Space](<./Color_Space.md> "Color Space") before they are used as part of the node's operation. Note that this does not change the color space of the node itself, as that is always in the Working Color Space. 
* sRGB`srgb`\- [sRGB](<https://en.wikipedia.org/wiki/SRGB>) color space, with sRGB transfer function. Considered an SDR color space with respect to Reference White.
* sRGB - Linear`srgblinear`\- [sRGB](<https://en.wikipedia.org/wiki/SRGB>) color space, with linear transfer function. Considered an SDR color space with respect to Reference White.
* Rec.601 (NTSC)`rec601ntsc`\- [Rec.601](<https://en.wikipedia.org/wiki/Rec._601>) with NTSC primaries color space, with Rec.601 transfer function. Considered an SDR color space with respect to Reference White.
* Rec.709`rec709`\- [Rec.709](<https://en.wikipedia.org/wiki/Rec._709>) color space, with Rec.709 (same as Rec.2020) transfer function. Considered an SDR color space with respect to Reference White.
* Rec.2020`rec2020`\- [Rec.2020](<https://en.wikipedia.org/wiki/Rec._2020>) color space, with Rec.2020 (same as Rec.709) transfer function. Considered an HDR color space with respect to Reference White.
* DCI-P3`dcip3`\- [DCI-P3](<https://en.wikipedia.org/wiki/DCI-P3>) color space, with D65 white point and 2.6 gamma transfer function. Considered an HDR color space with respect to Reference White.
* DCI-P3 (D60)`dcip3d60`\- [DCI-P3 "D60 sim"](<https://en.wikipedia.org/wiki/DCI-P3>) color space, with D60 white point, and 2.6 gamma transfer function. Considered an HDR color space with respect to Reference White.
* Display-P3 (D65)`displayp3d65`\- [Display-P3](<https://en.wikipedia.org/wiki/DCI-P3>) color space, with D65 white point, and sRGB gamma transfer function. Considered an HDR color space with respect to Reference White.
* ACES2065-1`aces2065-1`\- [ACES 2065-1](<https://en.wikipedia.org/wiki/Academy_Color_Encoding_System>) (also known as ACES AP0) color space, with a linear gamma transfer function. Considered an HDR color space with respect to Reference White.
* ACEScg`acescg`\- [ACEScg](<https://en.wikipedia.org/wiki/Academy_Color_Encoding_System>) (also known as ACES AP1) color space, with a linear gamma transfer function. Considered an HDR color space with respect to Reference White.
* Passthrough`passthrough`\- When selected, the color values will be used as-is in the operation, without any modification or attempt to convert them into the Working Color Space.


Parameter Reference White`parmreferencewhite`\- ⊞ \- When converting a parameter color value to the Working Color Space, this controls how it should be treated with respect to [Reference White](<./Color_Space.htm#Reference_White> "Color Space"). If the Working Color Space is the same Reference White, then no adjustment is done. If they are different, then the Reference White level (brightness) of this color will be adjusted to the range expected by the Working Color Space. For example if the project is set to have a SDR Reference White of 120 nits, and the HDR Reference White is 80 nits, then a color of (1, 1, 1), which is 120 nits in the SDR color space, will be converted to be (1.5, 1.5, 1.5), which is 120 nits still in the HDR Working Color Space. 
* Default For Color Space`default`\- Will use either the SDR or the HDR Reference White, based on the color space selected.
* Use Parent Panel`useparent`\- Will use the Reference White that the parent panel has selected. If the top-level panel also has 'Use Parent' selected, then 'UI Reference White' will be used.
* Standard (SDR)`sdr`\- Will treat the Parameter Color Space as SDR for it's reference white value.
* High (HDR)`hdr`\- Will treat the Parameter Color Space as HDR for it's reference white value.
* UI`ui`\- Will treat the Parameter Color Space as UI for it's reference white value. This uses the 'UI Reference White Nits' value for it's brightness.

## 

Info CHOP Channels

Extra Information for the Camera COMP can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). __

### 

Common COMP Info Channels
* num_children \- Number of children in this component.

### 

Common Operator Info Channels
* total_cooks \- Number of times the operator has cooked since the process started.
* cook_time \- Duration of the last cook in milliseconds.
* cook_frame \- Frame number when this operator was last cooked relative to the component timeline.
* cook_abs_frame \- Frame number when this operator was last cooked relative to the absolute time.
* cook_start_time \- Time in milliseconds at which the operator started cooking in the frame it was cooked.
* cook_end_time \- Time in milliseconds at which the operator finished cooking in the frame it was cooked.
* cooked_this_frame \- 1 if operator was cooked this frame.
* warnings \- Number of warnings in this operator if any.
* errors \- Number of errors in this operator if any.


  
TouchDesigner Build: Latest\nwikieditorwikieditor2022.241402021.100002018.28070before 2018.28070

COMPs   
---  
[Actor ](<./Actor_COMP.md> "Actor COMP")• [Ambient Light ](<./Ambient_Light_COMP.md> "Ambient Light COMP")• [Animation ](<./Animation_COMP.md> "Animation COMP")• [Annotate ](<./Annotate_COMP.md> "Annotate COMP")• [Base ](<./Base_COMP.md> "Base COMP")• [Blend ](<./Blend_COMP.md> "Blend COMP")• [Bone ](<./Bone_COMP.md> "Bone COMP")• [Bullet Solver ](<./Bullet_Solver_COMP.md> "Bullet Solver COMP")• [Button ](<./Button_COMP.md> "Button COMP")• [Camera Blend ](<./Camera_Blend_COMP.md> "Camera Blend COMP")• Camera • [MediaWiki:Common.js ](<./MediaWiki-Common.md> "MediaWiki:Common.js")• [COMP ](<./COMP.md> "COMP")• [Component ](<./Component.md> "Component")• [Constraint ](<./Constraint_COMP.md> "Constraint COMP")• [Container ](<./Container_COMP.md> "Container COMP")• [Engine ](<./Engine_COMP.md> "Engine COMP")• [Environment Light ](<./Environment_Light_COMP.md> "Environment Light COMP")• [FBX ](<./FBX_COMP.md> "FBX COMP")• [Field ](<./Field_COMP.md> "Field COMP")• [Force ](<./Force_COMP.md> "Force COMP")• [Geo Text ](<./Geo_Text_COMP.md> "Geo Text COMP")• [Geometry ](<./Geometry_COMP.md> "Geometry COMP")• [GLSL ](<./GLSL_COMP.md> "GLSL COMP")• [Handle ](<./Handle_COMP.md> "Handle COMP")• [Impulse Force ](<./Impulse_Force_COMP.md> "Impulse Force COMP")• [Light ](<./Light_COMP.md> "Light COMP")• [List ](<./List_COMP.md> "List COMP")• [Null ](<./Null_COMP.md> "Null COMP")• [NVIDIA Flex Solver ](<./NVIDIA_Flex_Solver_COMP.md> "NVIDIA Flex Solver COMP")• [NVIDIA Flow Emitter ](<./NVIDIA_Flow_Emitter_COMP.md> "NVIDIA Flow Emitter COMP")• [OP Viewer ](<./OP_Viewer_COMP.md> "OP Viewer COMP")• [Parameter ](<./Parameter_COMP.md> "Parameter COMP")• [Replicator ](<./Replicator_COMP.md> "Replicator COMP")• [Select ](<./Select_COMP.md> "Select COMP")• [Shared Mem In ](<./Shared_Mem_In_COMP.md> "Shared Mem In COMP")• [Shared Mem Out ](<./Shared_Mem_Out_COMP.md> "Shared Mem Out COMP")• [Slider ](<./Slider_COMP.md> "Slider COMP")• [Table ](<./Table_COMP.md> "Table COMP")• [Text ](<./Text_COMP.md> "Text COMP")• [Time ](<./Time_COMP.md> "Time COMP")• [USD ](<./USD_COMP.md> "USD COMP")• [Widget ](<./Widget_COMP.md> "Widget COMP")• [Window ](<./Window_COMP.md> "Window COMP")
