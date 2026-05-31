# Projection Mapping

Here are several forms and corresponding solutions of projection mapping with TouchDesigner. Most are in the Palette under Mapping, others are specific operator types in TouchDesigner. 

### Kantan Mapper

[Kantan Mapper](<./Palette-kantanMapper.md> "Palette:kantanMapper") is a projection mapping and masking tool where you define 2D polygons and bezier outlines in the field of view of a projector, then fills each shape with a selected image (TOP). 

#### Kantan UV Helper

[Kantan UV Helper](<./Palette-kantanUVHelper.md> "Palette:kantanUVHelper") is an additional tool for Kantan Mapper to make use of Kantan's second UV Map output. Using the Helper lightens the processing time as Kantan itself is not anymore part of the rendering process. 

### CamSchnappr

[CamSchnappr](<./Palette-camSchnappr.md> "Palette:camSchnappr") \- If you have a physical 3D structure plus a virtual 3D model of that structure, you can to project a rendered virtual model onto that physical structure perfectly-aligned, by choosing and moving 6 guide points in your projected image. It can do multiple projectors with blend regions. 

### Projector Blend

[projectorBlend](<./Palette-projectorBlend.md> "Palette:projectorBlend") \- a tool to smoothly blend NxM arrays of projectors. 

### Stoner

[Stoner](<./Palette-stoner.md> "Palette:stoner") \- An interactive corner-pin image warper plus a mesh warper for manually fitting an image on a physical 3D surface. 

### Corner Pin SOP

[CornerPinSOP](<./Palette-cornerPinSOP.md> "Palette:cornerPinSOP") \- This palette component is a brute force corner-pinning component for SOPs. Can be useful also when corner-pinning lasers. 

### Quad Reproject

[quadReproject](<./Palette-quadReproject.md> "Palette:quadReproject") \- QuadReproject is used for LED screens (or any pixel arrays) to render pixel-perfect images, rendered from any viewing location relative to the LED screen. 

### Vioso

[Vioso](<./Vioso.md> "Vioso") is integrated with TouchDesigner and lets you read in calibration data from the VIOSO Calibrator Software. Vioso's auto-alignment technology makes the setup of installations like multi-projector panorama displays, domes and multi-projector setups for projection mapping more automated and quick. 

### Scalable Dislays

[Scalable Displays](<./Scalable_Display_TOP.md> "Scalable Display TOP") \- The Scalable Display TOP lets you load calibration data retrieved from running the Scalable Display Calibration Software. 

### Sweet Spot

[sweetSpot](<./Palette-sweetSpot.md> "Palette:sweetSpot") is a technique better known as [Trompe-l'œil](<https://en.wikipedia.org/wiki/Trompe-l'%C5%93il>) where a scene is rendered from the position of the observer and re-projected onto a surface. Results created for large format projections, surround environments or tracked monitor setups will seem to be close to perspectively correct when viewed from the general area of the sweet spot. For a pixel-perfect perspective-correct result, more suitable for LED Screens in XR Stage environemnts also check the [Camera COMP's](<./Camera_COMP.md> "Camera COMP") [Quad Reprojection](<./Quad_Reprojection.md> "Quad Reprojection") feature. 

### Kinect Calibration

The [Kinect Calibration](<./Palette-kinectCalibration.md> "Palette:kinectCalibration") component is an example for calibrating a Kinect Camera to a projector with the help of checkerboards. It utilizes the same technique as camSchnappr due to the ability to fetch 3D coordinates from its pointcloud. 

### Corner Pin TOP

[Corner Pin TOP](<./Corner_Pin_TOP.md> "Corner Pin TOP") \- Elementary corner-pinning.
