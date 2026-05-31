# Particle

A particle system is a type of [Primitive](<./Primitive.md> "Primitive") of a [SOP](<./SOP.md> "SOP") that consists of a group of discrete particles which change over time. Each particle has its own attributes controlling size, position, velocity, etc. Particles can generate new attributes depending on their age, or they may die. Assigning values discretely to each particle enables realistic modeling of systems involving turbulence such as: smoke, wind, fire, dust, and hair. 

### Particles on the CPU

Any point or set of [points](<./Point.md> "Point") can be used as the basis for the particles in a particle system. [Grid SOPs](<./Grid_SOP.md> "Grid SOP") or [Sphere SOPs](<./Sphere_SOP.md> "Sphere SOP") are often employed for this purpose. A particle system can be created in SOPs by using a [Particle SOP](<./Particle_SOP.md> "Particle SOP"), particles will be emitted from the points of the geometry connected to the Particle SOP's first input. 

Any point or set of points can also be converted into particles using a [Convert SOP](<./Convert_SOP.md> "Convert SOP"). 

### Particles on the GPU

Particles can be simulated on the GPU by treating each pixel in a TOP as a particle, and instancing them through the Instancing pages of a [Geometry COMP](<./Geometry_COMP.md> "Geometry COMP"). TOPs that facilitate this include the [Point File In TOP](<./Point_File_In_TOP.md> "Point File In TOP"), [Math TOP](<./Math_TOP.md> "Math TOP"), [Limit TOP](<./Limit_TOP.md> "Limit TOP"), [Slope TOP](<./Slope_TOP.md> "Slope TOP"), [Feedback TOP]], [Reorder TOP](<./Reorder_TOP.md> "Reorder TOP"). In the Palette are several examples under Point Clouds and particlesGPU. 

See also [Point Sprite MAT](<./Point_Sprite_MAT.md> "Point Sprite MAT").
