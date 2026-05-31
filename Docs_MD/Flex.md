# Flex

See also: [Bullet Dynamics](<./Bullet_Dynamics.md> "Bullet Dynamics"), [Nvidia Flex Solver COMP](<./Nvidia_Flex_Solver_COMP.md> "Nvidia Flex Solver COMP"), [Nvidia Flex TOP](<./Nvidia_Flex_TOP.md> "Nvidia Flex TOP"), [Actor COMP](<./Actor_COMP.md> "Actor COMP"), [Force COMP](<./Force_COMP.md> "Force COMP")

### 

What is Nvidia Flex?

[Nvidia Flex](<https://developer.nvidia.com/flex>) is a particle-based physics simulator. Flex uses a unified particle representation for all object types. All bodies in a simulation (with the exception of static shapes/surfaces) are composed of particles, and their behaviour in the simulation will be defined by what type of substance: rigid, soft, fluid, rope, cloth. Because all bodies in a Flex simulation are represented by particles, all substances can be simulated together seamlessly without the need for multiple solvers. 

### 

Nvidia Flex in TouchDesigner

Nvidia Flex simulation is done through the Nvidia Flex Solver COMP. The Nvidia Flex Solver COMP is responsible for running the simulation and updating the transforms of all bodies in the simulation. The [Nvidia Flex Solver COMP](<./Nvidia_Flex_Solver_COMP.md> "Nvidia Flex Solver COMP") has all the global parameters, such as particle radius and friction. Bodies can be added to the Nvidia Flex Solver COMP's simulation via the [Actor COMP](<./Actor_COMP.md> "Actor COMP"). The Actor COMP currently only supports fluid substances and static shapes. 

Fluids are created either from instancing or emission. With instancing, the number of particles is determined by the number of input instances (ie. resolution of a TOP, number of points in a SOP), and their initial transforms are calculated from the instance input parameters (see also: [Actor COMP](<./Actor_COMP.md> "Actor COMP")). With emission, the maximum number of particles is set explicitly via a parameter. The Actor COMP starts with 0 fluid particles, but fluid particles are added to the simulation from the emitter. A SOP is not needed for creating a particle. Particle collision boundaries are simply defined by a radius (on the Nvidia Flex Solver COMP), so the SOP that is inside the Actor COMP is irrelevant outside of rendering. Naturally, a sphere SOP with the same radius as the collision particle will be the most accurate. A low-poly sphere can be used for improved performance. 

Nvidia Flex Solver COMP only works on systems running Windows OS. 

### 

What is possible with Flex in TouchDesigner?

Flex allows you to create realistic fluid particle simulations in TouchDesigner. Fluid emission is also supported. In addition to fluids, TouchDesigner also supports static shapes/surfaces. 

### 

Flex vs. Bullet

The [Nvidia Flex Solver COMP](<./Nvidia_Flex_Solver_COMP.md> "Nvidia Flex Solver COMP") exists as an alternative to the [Bullet Solver COMP](<./Bullet_Solver_COMP.md> "Bullet Solver COMP"). Both of these physics simulators use the Actor COMP to add bodies to the simulation. 

The key difference is Flex is a particle simulator and Bullet is a rigid body simulator. Bullet does not have a particle simulator; it is only a rigid body simulator. Flex also supports rigid body simulation but currently in TouchDesigner Flex only supports fluid particle simulations. Because Flex leverages the GPU (ie. CUDA), its simulations can support many more bodies than Bullet. 

The [Nvidia Flex Solver COMP](<./Nvidia_Flex_Solver_COMP.md> "Nvidia Flex Solver COMP") is a more closed simulation than the [Bullet Solver COMP](<./Bullet_Solver_COMP.md> "Bullet Solver COMP"). When it comes to user interaction and fetching simulation info, Bullet is the superior choice. This is primarily because of the [Bullet Solver CHOP](<./Bullet_Solver_CHOP.md> "Bullet Solver CHOP"), which allows simulation info such as transform and velocity to be retrieved, and is a key part of the feedbacking system in Bullet. Bullet in TouchDesigner also has better support in python (see [Body Class](<./Body_Class.md> "Body Class")). Additionally, Bullet provides a collision callback mechanism. 

Bullet supports impulse and continuous linear/angular forces. These forces can either be global or local ([Actor COMP](<./Actor_COMP.md> "Actor COMP") specific). Flex only support force fields. Force fields can either push outward (positive strength) or pull inward (negative strength), with an option for linear falloff from the force field center. 

Flex comes built in with simulation boundaries, in the form of planes. A maximum of 6 planes are provided in the form of parameters on the [Nvidia Flex Solver COMP](<./Nvidia_Flex_Solver_COMP.md> "Nvidia Flex Solver COMP"). The default plane is an +Z XY-plane, meaning particles are constrained to the +Z side of the plane. 

### 

How to use Flex in TouchDesigner

For completed examples on how to use Flex in TouchDesigner, please refer to the [Nvidia Flex Solver COMP](<./Nvidia_Flex_Solver_COMP.md> "Nvidia Flex Solver COMP") Snippets under Help > Operator Snippets. 

See also: [https://docs.derivative.ca/Bullet_Dynamics#How_to_use_Bullet_in_TouchDesigner](<./Bullet_Dynamics.htm#How_to_use_Bullet_in_TouchDesigner>)

In TouchDesigner, the [Nvidia Flex Solver COMP](<./Nvidia_Flex_Solver_COMP.md> "Nvidia Flex Solver COMP") is the primary operator of the physics simulation. It is responsible for running the simulation and solving for the transformations and velocities of each body that is in the simulation. Actor COMPs represent the bodies in the simulation, and force fields can be added using the [Force COMP](<./Force_COMP.md> "Force COMP"). 

To create a simple fluid emitter simulation: 
1. Create an [Nvidia Flex Solver COMP](<./Nvidia_Flex_Solver_COMP.md> "Nvidia Flex Solver COMP")
  2. Enable planes. Rotate the plane to be a +Y XZ-plane. In order to do this, rotate the plane 90 degrees around the X-axis.
  3. Create an Actor COMP and reference it on the [Nvidia Flex Solver COMP](<./Nvidia_Flex_Solver_COMP.md> "Nvidia Flex Solver COMP") so that it will be added to the simulation.
  4. This Actor COMP will be a fluid emitter. So, change the kinematic state of the [Actor COMP](<./Actor_COMP.md> "Actor COMP") to dynamic. Then, on the Flex page, change the Flex Type to be Fluid Emitter
  5. Choose emission transform. The Fluid Emitter transform is calculated from the transform of the [Actor COMP](<./Actor_COMP.md> "Actor COMP") (Xform and Pre-Xform page). Instancing is enabled automatically and instances will be created automatically, so parameters on the instance pages will have no effect.
  6. Choose the emission speed and dimension.
  7. Choose the maximum number of emission particles. The fluid emitter will create new fluid particles up until the maximum, at which point it will begin to recycle existing fluid particles within the Actor COMP.
  8. Start the simulation using the "Start Sim" parameter on the [Nvidia Flex Solver COMP](<./Nvidia_Flex_Solver_COMP.md> "Nvidia Flex Solver COMP").
