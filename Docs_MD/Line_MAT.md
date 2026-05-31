# Line MAT

##   
  
Summary

The Line MAT renders 3D line segments, dots and vectors. The line width and color can be varied based on distance to the camera, using two models: a 1/z dropoff (z = distance from camera), or a near-far distance rolloff model, where you set the width and color at the near and far distances, and you vary three rolloff controls. 

For lines it renders different types of end caps and hinge/joints (round, box, arrow). The light model is flat-shaded (no affect from scene lighting). It draws edges (like polygon edges), points and vectors from points. There are different parameters to control the desired shape, as explained in the Parameter sections. It renders several primitive types: polygons, meshes, NURBS, quads, etc. It also manages closed polygons / open polygons. 

You can render a dot at each point. You can render a vector at each point which uses any attribute, like Normal (N). The points or vectors can have their own colors and alpha. 

Line Width is a resolution-independent quantity. A line width of 1 will draw a line that is 1/1000 the width of the image. This is true when used with orthographic cameras and perspective cameras. 

To make the width of a line and its points vary per-point of a SOP, the width can be set by adding a point attribute`width`on the SOP being rendered. A value of 2 scales the width at that point by 2 times its normal width. New point attributes can be created with the [Point SOP](<./Point_SOP.md> "Point SOP") Custom page. To affect per-point width and not affect the line width, use the point attribute`pscale`. 

When you are animating Ortho Width or Field of View, you may want line widths to adjust more realistically. When the parameter "Width Affected by FOV/Ortho Width" is on, the behavior is different: For Ortho cameras, the drawn line width increases when Ortho Width drops below 1, (as if you are zooming into it), and decreases when Ortho Width increases above 1. For Perspective cameras, the drawn line width increases when Field of View drops below 90 degrees, and decreases when Field of View increases above 90 degrees. Note that when the parameter "Width Affected by FOV/Ortho Width" is on, lines are still resolution-independent. 

Intro article here from Interactive Immersive HQ: [new-superpowers-touchdesigners-line-mat/](<https://interactiveimmersive.io/blog/3d/new-superpowers-touchdesigners-line-mat/>)

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[lineMAT_Class](<./LineMAT_Class.md> "LineMAT Class")

## 

Parameters - Setup Page

This is a general setup page for globally control the shared features of Lines, Points, and Vectors. Every change in this page will affect all the three mentioned types. 

Depth Interpolation Model`depthinterpolationmodel`\- ⊞ \- Depth Interpolation Model depthmodel – a menu to select how the width of line items changes by their distance from the camera. 
* S Curve`scurve`\- a bounded range for the width between the near and far planes (Distance Near and Far) that uses S Curve for a more dramatic and yet smooth (referring to the continuity of the curve) changes. The curve shape can be controlled by Bias, Steepness, and Linearize parameters.
* Inverse Distance`inversedistance`\- uses the inverse distance weighting which provides a more visually accurate changes on the final width.


Inverse Distance Exponent`inversedistanceexponent`\- When the Depth Interpolation Model is Inverse Distance, this determines how fast the widths/sizes decrease with distance. If it is set to 1 (default), the width goes down at the rate of 1/r. If it set to 2, it goes down by 1/(r*r), meaning that for lines/dots at a distance r that have a width of w, that line/dot at a distance twice as far away (2r) are 1/4 the width/size as they are at distance r. 

Distance Near`distancenear`\- Specifies a near plane with a certain distance from the camera. 

Distance Far`distancefar`\- Specifies a far plane with a certain distance from the camera. 

Width Near`widthnear`\- Specifies a fixed width value when the distance from camera is less than or equal to Distance Near. See the Summary of this operator for an explantion of the treatment of line width. 

Width Far`widthfar`\- Specifies a fixed width value when the distance from the camera is equal or bigger than the Distance Far. Note when the Near-Far Range option is selected as the Depth Model, any point in between Distance Near and Distance Far will be calculated based on sine curve. 

Width Affected by FOV/OrthoWidth`widthaffectedbyfov`\- With this off (default), looking at a rendered image of a certain resolution, a line of with w will always be the same # of pixels wide as you change the field-of-view or ortho width. With this parameter on, a line of width w will be half the number of pixels wide if you double the field-of-view or double the ortho width. Relevant if you are animating camera zoom, for instance. 

Width Bias`widthbias`\- Moves the S Curve’s bias backward or forward for width interpolation (only S Curve depth model). 

Width Steepness`widthsteepness`\- Controls the steepness of the S Curve for width interpolation (only S Curve depth model). The higher the value of the steepness, you will notice more dramatic changes (higher slope) in the curve width. Also, with lower values of steepness, the curve transforms into a more linear form. 

Width Linearize`widthlinearize`\- Control the amount of curvature in the curve for width interpolation (only S Curve depth model). 

Color Bias`colorbias`\- Moves the S Curve’s bias backward or forward for color interpolation. 

Color Steepness`colorsteepness`\- Controls the steepness of the S Curve for color interpolation. 

Color Linearize`colorlinearize`\- Control the amount of curvature in the curve for color interpolation. 

Lift Direction`liftdirection`\- ⊞ \- If a line is being drawn on a polygon or its edge (the polygon being in another Geometry COMP \+ shader), and you need to lift it off the surface to be fully visible, this specifies whether to displace the line points toward the camera or along the line's normal (which can be the direction of the polygon's normal). 
* Along Camera Z Axis`alongcamerazaxis`\- displace the points along Camera Z axis.
* Along Normal`alongnormal`\- displace the points along point's Normal vector.
* Toward Camera`towardcamera`-


Lift Scale`liftscale`\- For lines that are drawn on top of filled polygons or along their edges, they may be cut off because they are rendered in the same place. To make it look good, you want to lift the line toward the camera or along its normal away from the surface. This parameter scales how far you lift the line off the surface to make it look good without separating them too far. 

Num Points in Circle`numptsincircle`\- When drawing Points in Circle (Polygon) mode, or drawing end-caps, or elbows between edges, this determines how many points you would draw in a full-circle arc to simulate a circular shape. The lower the number, the faster it renders. 

## 

Parameters - Line Page

Draw Lines`drawlines`\- A toggle to draw the Line polygons. 

Line Joint Type`linejointtype`\- ⊞ \- A menu to select the joint type where two lines segments meet. 
* Round`round`\- a round joint.
* Miter`miter`\- a sharp miter joint.
* Bevel`bevel`\- a square shaped joint.


Miter Threshold (deg)`miterthreshold`\- Specifies a threshold value in degrees for the Miter joint which alters the joint shape to Bevel joint if the angle between each two lines segments is bigger than this value. 

Line Start Cap Type`linestartcaptype`\- ⊞ \- A menu to Specify the end cap type at the Line start. You can control the size of each end cap type in the Cap page. 
* Round`round`-
* Square`square`\- Square shaped end cap.
* Triangle`triangle`\- Triangle shaped end cap.
* Arrow`arrow`\- Arrow Shaped end cap.
* None`none`\- No end cap (flat shaped).


Line End Cap Type`lineendcaptype`\- ⊞ \- A menu to Specify the end cap type at the Line end. 
* Round`round`\- Refer to Line Start Cap Type
* Square`square`\- Refer to Line Start Cap Type
* Triangle`triangle`\- Refer to Line Start Cap Type
* Arrow`arrow`\- Refer to Line Start Cap Type
* None`none`\- Refer to Line Start Cap Type


Line End Taper Strength`lineendtaperstrength`\- 

Line Near Color`linenearcolor`\- ⊞ \- Specifies the color value for the Line at the Distance Near plane and any location closer to camera. 
* Red`linenearcolorr`-
* Green`linenearcolorg`-
* Blue`linenearcolorb`-


Line Near Alpha`linenearalpha`\- Specifies the alpha value for the Line at the Distance Near plane and any location closer to camera. 

Specify Line Far Color`specifylinefarcolor`\- A toggle to use the far color and interpolate the values between near and far color. 

Line Far Color`linefarcolor`\- ⊞ \- Specifies the color value for the Line at the Distance Far plane and beyond (farther from camera). 
* Red`linefarcolorr`-
* Green`linefarcolorg`-
* Blue`linefarcolorb`-


Line Far Alpha`linefaralpha`\- Specifies the alpha value for the Line at the Distance Far plane and beyond (farther from camera). 

## 

Parameters - Point Page

Draw Points`drawpoints`\- A toggle to draw the Points. 

Point Type`pointtype`\- ⊞ \- A menu to select the Point type. 
* Circle`circle`\- draws circle on each point of the geometry.
* Sphere`sphere`\- draws sphere on each point of the geometry.
* Circle (Sprite)`circlesprite`-
* Square`square`-
* Cone`cone`-


Point Size Multiplier`pointsizemultiplier`\- Specifies a scale coefficient to the size of the Point. By default, the point radius size equals to the width at the point’s location from the camera. 

Point Near Color`pointnearcolor`\- ⊞ \- Specifies the color value for the Point at the Distance Near plane and any location closer to camera. 
* Red`pointnearcolorr`-
* Green`pointnearcolorg`-
* Blue`pointnearcolorb`-


Point Near Alpha`pointnearalpha`\- Specifies the alpha value for the Point at the Distance Near plane and any location closer to camera. 

Specify Point Far Color`specifypointfarcolor`\- A toggle to use the far color and interpolate the values between near and far color. 

Point Far Color`pointfarcolor`\- ⊞ \- Specifies the color value for the Point at the Distance Far plane and beyond (farther from camera). 
* Red`pointfarcolorr`-
* Green`pointfarcolorg`-
* Blue`pointfarcolorb`-


Point Far Alpha`pointfaralpha`\- Specifies the alpha value for the Point at the Distance Far plane and beyond (farther from camera). 

Point Lift Direction`pointliftdirection`\- ⊞ \- A menu to select the the dirction to lift points. See parameter Lift Direction. 
* Toward Camera`towardcamera`-
* Along Normal`alongnormal`-


Point Lift Scale`pointliftscale`\- see parameter Lift Scale. 

## 

Parameters - Vector Page

Draw Vectors`drawvectors`\- A toggle to draw the Vectors at each point. 

Scale`scale`\- A scale value which applies on the length of the Vector. 

Vector Start Cap Type`vectorstartcaptype`\- ⊞ \- A menu to Specify the end cap type at the Vector start. You can control the size of each end cap type in the Cap page. 
* Round`round`-
* Square`square`-
* Triangle`triangle`-
* Arrow`arrow`-
* None`none`-


Vector End Cap Type`vectorendcaptype`\- ⊞ \- A menu to Specify the end cap type at the Vector end. You can control the size of each end cap type in the Cap page. 
* Round`round`-
* Square`square`-
* Triangle`triangle`-
* Arrow`arrow`-
* None`none`-


Vector Taper Strength`vectortaperstrength`\- : A coefficient to scale the width of end part of the Vector. 

Vector Near Color`vectornearcolor`\- ⊞ \- Specifies the color value for the Vector at the Distance Near plane and any location closer to camera. 
* Red`vectornearcolorr`-
* Green`vectornearcolorg`-
* Blue`vectornearcolorb`-


Vector Near Alpha`vectornearalpha`\- Specifies the alpha value for the Vector at the Distance Near plane and any location closer to camera. 

Specify Vector Far Color`specifyvectorfarcolor`\- A toggle to use the far color and interpolate the values between near and far color. 

Vector Far Color`vectorfarcolor`\- ⊞ \- Specifies the color value for the Vector at the Distance Far plane and beyond (farther from camera). 
* Red`vectorcolorfarr`-
* Green`vectorcolorfarg`-
* Blue`vectorcolorfarb`-
* Vector Far Color`vectorfarcolorr`-
* Vector Far Color`vectorfarcolorg`-
* Vector Far Color`vectorfarcolorb`-


Vector Far Alpha`vectorfaralpha`\- Specifies the alpha value for the Vector at the Distance Far plane and beyond (farther from camera). 

## 

Parameters - Caps Page

Round Width`roundwidth`\- Specifies a scale to the width of Round end caps. 

Round Height`roundheight`\- Specifies a scale to the height of Round end caps. 

Square Width`squarewidth`\- Specifies a scale to the width of Square end caps. 

Square Height`squareheight`\- Specifies a scale to the height of Square end caps. 

Triangle Width`trianglewidth`\- Specifies a scale to the width of Triangle end caps. 

Triangle Height`triangleheight`\- Specifies a scale to the height of Triangle end caps. 

Arrow Width`arrowwidth`\- Specifies a scale to the width of Arrow end caps. 

Arrow Height`arrowheight`\- Specifies a scale to the height (from the base of arrow to the head) of Arrow end caps. 

Arrow Tail Length`arrowtaillength`\- Specifies a scale to the tail length of Arrow end caps (the longer the tail the sharper it will look like). 

End Cap Width Multiplier`endcapwidthmultiplier`\- Normally end caps are the same width as the line. This parameter lets you make the cap wider/narrower than the line. 

End Cap Height Multiplier`endcapheightmultiplier`\- Normally the end caps extend farther than the end of the line by half of the width (making the end cap a half-circle, and similarly for square, triangular and arrow endcape). This parameter lets you push the end cap out farther or closer. 

Start Caps Pullback`startcappullback`\- By default (0), the start cap goes beyond the start point of the line so that the center of a circular startcap is right at the start point. Setting this to 1 makes the tip of the end cap positioned exactly at the start point. 

End Caps Pullback`endcappullback`\- By default (0), the end cap goes beyond the end point of the line so that the center of a circular endcap is right at the end point. Setting this to 1 makes the tip of the end cap positioned exactly at the end point. 

## 

Parameters - Attributes Page

Line Position Attribute`lineposatt`\- 

Line Width Attribute`linewidthatt`\- 

Line Color Attribute`linecoloratt`\- 

Point Position Attribute`pointposatt`\- 

Point Size Attribute`pointsizeatt`\- 

Point Color Attribute`pointcoloratt`\- 

Vector Attribute Type`vectoratttype`\- ⊞ \- When drawing a vector at each point, this determines where to get the XYZ of the vector. By default it gets it from an attribute of the SOP, the point normal by default. But when instancing is used, you can get it from an instance attribute from an Instance OP. The vector can be represented in world space or in the reference frame of the Geometry COMP. 
* SOP Attribute`sopattrib`-
* Instance Custom Attribute (SOP Space)`instanceattribsop`-
* Instance Custom Attribute (World Space)`instanceattribworld`-


Vector Attribute`vectoratt`\- ⊞ \- Specify the geometry [Attribute](<./Attribute.md> "Attribute") to use to render the Vector. Some standard attribute are: N, P, Cd, uv, however it is possible to specify a custom attribute. Note that this value is case sensitive, ensure that the it matches with the name of the attribute for that point/vector. 
* N (Point Normal X, Y, Z)`N`-
* P (Point Position X, Y, Z)`P`-
* Cd (Point Color red, green, blue, alpha)`Cd`-
* uv (Point Texture Coordinates U,V,W)`uv`-


Vector Instance Custom Attribute Index`vectorcusattribidx`\- When instancing is used, you can get the XYZ vector from an instance attribute. This is the index of the X value in the Instance OP. 

## 

Parameters - Deform Page

Refer to the [ Deform Article](<./Deforming_Geometry_\(Skinning\).md> "Deforming Geometry \(Skinning\)") for more information on doing deforms in TouchDesigner. 

Deform`dodeform`\- Enables deforms on this material. 

Get Bone Data:`deformdata`\- ⊞ \- Specifies where the deform bone data will be obtained. 
* From a SOP`sop`-
* From another MAT`mat`-
* From a DeformIn MAT`deformin`-


SOP with Capture Data`targetsop`\- Specifies the SOP that contains the deform capture attributes. 

pCaptPath Attrib`pcaptpath`\- Specifies the name of the pCaptPath attribute to use. When your geometry has been put through a [Bone Group SOP](<./Bone_Group_SOP.md> "Bone Group SOP"), the attributes will be split into names like pCaptPath0, pCaptPath1. You can only render 1 bone group at a time, so this should match the group you are rendering with this material. 

pCaptData Attrib`pcaptdata`\- Much like pCaptPath Attrib. 

Skeleton Root Path`skelrootpath`\- Specifies the path to the COMP where the root of the skeleton is located. 

MAT`mat`\- When obtaining deform data from a MAT or a Deform In MAT, this is where that MAT is specified. 

## 

Parameters - Common Page

### 

Blending

[Blending](<./Blending.md> "Blending") is summing the color value of the pixel being drawn and the pixel currently present in the Color-Buffer. Blending is typically used to simulate [Transparency](<./Transparency.md> "Transparency"). The blending equation is:`Final Pixel Value = (Source Blend * Source Color) + (Dest Blend * Destination Color)`Blending (Transparency)`blending`\- This toggle enables and disables blending. However see the wiki article [Transparency](<./Transparency.md> "Transparency"). 

Blend Operation`blendop`\- ⊞ \- 
* Add`add`-
* Subtract`subtract`-
* Reverse Subtract`revsubtract`-
* Minimum`minimum`-
* Maximum`maximum`-


Source Color *`srcblend`\- ⊞ \- This value is multiplied by the color value of the pixel that is being written to the Color-Buffer (also know as the Source Color). 
* Zero`zero`-
* Dest Color`dcol`-
* One Minus Dest Color`omdcol`-
* Source Alpha`sa`-
* One Minus Source Alpha`omsa`-
* Dest Alpha`da`-
* One Minus Dest Alpha`omda`-
* Source Alpha Saturate`sas`-
* One`one`-
* Constant Color`constantcol`-
* One Minus Constant Color`omconstantcol`-
* Constant Alpha`constanta`-
* One Minus Constant Alpha`omconstanta`-


Destination Color *`destblend`\- ⊞ \- This value is multiplied by the color value of the pixel currently in the Color-Buffer (also known as the Destination Color). 
* One`one`-
* Src Color`scol`-
* One Minus Src Color`omscol`-
* Source Alpha`sa`-
* One Minus Source Alpha`omsa`-
* Dest Alpha`da`-
* One Minus Dest Alpha`omda`-
* Zero`zero`-
* Dest Color`dcol`-
* One Minus Dest Color`omdcol`-
* Source Alpha Saturate`sas`-
* Constant Color`constantcol`-
* One Minus Constant Color`omconstantcol`-
* Constant Alpha`constanta`-
* One Minus Constant Alpha`omconstanta`-


Separate Alpha Function`separatealphafunc`\- This toggle enables and disables separate blending options for the alpha values. 

Alpha Blend Operation`blendopa`\- ⊞ \- 
* Add`add`-
* Subtract`subtract`-
* Reverse Subtract`revsubtract`-
* Minimum`minimum`-
* Maximum`maximum`-


Source Alpha *`srcblenda`\- ⊞ \- This value is multiplied by the alpha value of the pixel that is being written to the Color-Buffer (also know as the Source Alpha). 
* Zero`zero`-
* Dest Color`dcol`-
* One Minus Dest Color`omdcol`-
* Source Alpha`sa`-
* One Minus Source Alpha`omsa`-
* Dest Alpha`da`-
* One Minus Dest Alpha`omda`-
* Source Alpha Saturate`sas`-
* One`one`-
* Constant Color`constantcol`-
* One Minus Constant Color`omconstantcol`-
* Constant Alpha`constanta`-
* One Minus Constant Alpha`omconstanta`-


Destination Alpha *`destblenda`\- ⊞ \- This value is multiplied by the alpha value of the pixel currently in the Color-Buffer (also known as the Destination Alpha). 
* One`one`-
* Src Color`scol`-
* One Minus Src Color`omscol`-
* Source Alpha`sa`-
* One Minus Source Alpha`omsa`-
* Dest Alpha`da`-
* One Minus Dest Alpha`omda`-
* Zero`zero`-
* Dest Color`dcol`-
* One Minus Dest Color`omdcol`-
* Source Alpha Saturate`sas`-
* Constant Color`constantcol`-
* One Minus Constant Color`omconstantcol`-
* Constant Alpha`constanta`-
* One Minus Constant Alpha`omconstanta`-


Blend Constant Color`blendconstant`\- ⊞ \- 
* Blend Constant Color`blendconstantr`-
* Blend Constant Color`blendconstantg`-
* Blend Constant Color`blendconstantb`-


Blend Constant Alpha`blendconstanta`\- 

Legacy Alpha Behavior`legacyalphabehavior`\- 

Post-Mult Color by Alpha`postmultalpha`\- Multiplies the color by alpha after all other operations have taken place. 

Point Color Pre-Multiply`pointcolorpremult`\- ⊞ \- 
* Already Pre-Multiplied By Alpha`alreadypremult`-
* Pre-Multiply By Alpha in Shader`premultinshader`-


Depth Test`depthtest`\- Enables and disables the Depth-Test. If the depth-test is disabled, depths values aren't written to the Depth-Buffer. 

Depth Test Function`depthfunc`\- ⊞ \- The depth value of the pixel being drawn is compared to the depth value currently in the depth-buffer using this function. If the test passes then the pixel is drawn to the Frame-Buffer. If the test fails the pixel is discarded and no changes are made to the Frame-Buffer. 
* Less Than`less`-
* Less Than or Equal`lessorequal`-
* Equal`equal`-
* Greater Than`greater`-
* Greater Than or Equal`greaterorequal`-
* Not Equal`notequal`-
* Always`always`-

### 

Depth Test

Depth-Testing is comparing the depth value of the pixel being drawn with the pixel currently in the [Frame-Buffer](</index.php?title=Frame-Buffer&action=edit&redlink=1> "Frame-Buffer \(page does not exist\)"). A pixel that is determined to be in-front of the pixel currently in the Frame-Buffer will be drawn over it. Pixels that are determined to be behind the pixel currently in the Frame-Buffer will not be drawn. Depth-Testing allows geometry in a 3D scene to occlude geometry behind it, and be occluded by geometry in-front of it regardless of the order the geometry was drawn. 

For a more detailed description of Depth-Testing, refer to the [Depth-Test](<./Depth-Test.md> "Depth-Test") article. 

Write Depth Values`depthwriting`\- If Write Depth Values is on, pixels that pass the depth-test will write their depth value to the Depth-Buffer. If this isn't on then no changes will be made to the Depth-Buffer, regardless of if the pixels drawn pass or fail the depth-test. 

Discard Pixels Based on Alpha`alphatest`\- This enables or disables the pixel alpha test. 

Keep Pixels with Alpha`alphafunc`\- ⊞ \- This menu works in conjunction with the Alpha Threshold parameter below in determining which pixels to keep based on their alpha value. 
* Less Than`less`-
* Less Than or Equal`lessorequal`-
* Greater Than`greater`-
* Greater Than or Equal`greaterorequal`-


Alpha Threshold`alphathreshold`\- This value is what the pixel's alpha is compared to to determine if the pixel should be drawn. Pixels with alpha greater than the Alpha Threshold will be drawn. Pixels with alpha less than or equal to the Alpha Threshold will not be drawn. 

Wire Frame`wireframe`\- ⊞ \- Enables and disables wire-frame rendering with the option of OpenGL Tesselated or Topology based wireframes. 
* Off`off`-
* OpenGL Tesselated Wire Frame`tesselated`-
* Topology Wire Frame`topology`-

### 

Alpha Test

Alpha-testing allows you to choose to draw or not draw a pixel based on its alpha value. 

Line Width`wirewidth`\- This value is the width that the wires will be. This value is in pixels. 

Cull Face`cullface`\- ⊞ \- Selects which faces to render. 
* Use Render Setting`userender`\- Use the render settings found in the Render or Render Pass TOP.
* Neither`neither`\- Do not cull any faces, render everything.
* Back Faces`backfaces`\- Cull back faces, render front faces.
* Front Faces`frontfaces`\- Cull front faces, render back faces.
* Both Faces`bothfaces`\- Cull both faces, render nothing.


Polygon Depth Offset`polygonoffset`\- Turns on the polygon offset feature. 

Offset Factor`polygonoffsetfactor`\- 

Offset Units`polygonoffsetunits`\- 

### 

Wire Frame

The wire-frame feature will render the geometry as wire-frame, using the actual primitive type used in the render. What this means is surfaces like Metaballs, NURBs and Beziers will become a wire-frame of the triangles/triangle-strips used to render them (since these types of primitives can't be natively rendered in OpenGL). 

### 

Cull Face

The cull face parameter will cull faces from the render output. This can be used as an optimization or sometimes to remove artifacts. See [Back-Face Culling](<./Back-Face_Culling.md> "Back-Face Culling") for more infomation. 

### 

Polygon Depth Offset

This feature pushes the polygons back into space a tiny fraction. This is useful when you are rendering two polygons directly on-top of each other and are experiencing [Z-Fighting](<./Z-Fighting.md> "Z-Fighting"). Refer to [Polygon Depth Offset](<./Polygon_Depth_Offset.md> "Polygon Depth Offset") for more information. This is also an important feature when doing [shadows](<./Shadows.md> "Shadows"). 

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

Extra Information for the Line MAT can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). __

### 

Common MAT Info Channels

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


  
TouchDesigner Build: Latest\nwikieditorwikieditor2021.100002019.146502018.28070

MATs   
---  
[Constant ](<./Constant_MAT.md> "Constant MAT")• [Experimental:Constant ](</Experimental:Constant_MAT> "Experimental:Constant MAT")• [Depth ](<./Depth_MAT.md> "Depth MAT")• [GLSL ](<./GLSL_MAT.md> "GLSL MAT")• [Experimental:GLSL ](</Experimental:GLSL_MAT> "Experimental:GLSL MAT")• [In ](<./In_MAT.md> "In MAT")• Line • [MAT ](<./MAT.md> "MAT")• [Experimental:MAT ](</Experimental:MAT> "Experimental:MAT")• [MAT Common Page ](<./MAT_Common_Page.md> "MAT Common Page")• [Null ](<./Null_MAT.md> "Null MAT")• [Out ](<./Out_MAT.md> "Out MAT")• [PBR ](<./PBR_MAT.md> "PBR MAT")• [Experimental:PBR ](</Experimental:PBR_MAT> "Experimental:PBR MAT")• [Phong ](<./Phong_MAT.md> "Phong MAT")• [Experimental:Phong ](</Experimental:Phong_MAT> "Experimental:Phong MAT")• [Point Sprite ](<./Point_Sprite_MAT.md> "Point Sprite MAT")• [Experimental:Point Sprite ](</Experimental:Point_Sprite_MAT> "Experimental:Point Sprite MAT")• [Select ](<./Select_MAT.md> "Select MAT")• [Switch ](<./Switch_MAT.md> "Switch MAT")• [Texture Sampling Parameters ](<./Texture_Sampling_Parameters.md> "Texture Sampling Parameters")• [Wireframe ](<./Wireframe_MAT.md> "Wireframe MAT")
