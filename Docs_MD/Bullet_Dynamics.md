# Bullet Dynamics

### 

What is Bullet?

Bullet is an open source real-time physics simulation API: <http://bulletphysics.org/wordpress/>

A Bullet simulation contains bodies, forces and constraints, and produces motion on the bodies. 

Bodies are much like physical objects in the real world and have many of the same physical properties: mass, size, kinetic friction etc. They also occupy space in the world, and no two physical objects can occupy the same space. When two physical objects attempt to occupy the same space in the world, they collide, and the same is true for the bodies in a Bullet simulation. Each body has a collision shape, which determines how it collides with other bodies. Examples of bodies: a brick wall, a baseball. 

In TouchDesigner all bodies are rigid, meaning they cannot deform based on collisions or other outside forces (as opposed to soft bodies). A body can be a whole geometry component, a SOP within a Geometry component, or one or more [instances](<./Instance.md> "Instance") of Geometry component. 

Forces are just like the forces we experience in the real world; they act on bodies by changing their velocity. In Bullet, forces can either be applied over time or as an impulse. For example: the wind is a force applied over time, and a cannon applies an impulse force to a cannon ball. 

At its core, what the Bullet API does is solve for the transformation and velocity of each body in the simulation. It handles all the math behind collisions of bodies, forces, friction, restitution, constraints etc. All the Bullet API needs is a set of forces and bodies with their respective properties and initial states, and it does the rest. One thing that the Bullet API does not do however, is calculate air resistance. 

See also: [Bullet Solver COMP](<./Bullet_Solver_COMP.md> "Bullet Solver COMP"), [Actor COMP](<./Actor_COMP.md> "Actor COMP"), [Force COMP](<./Force_COMP.md> "Force COMP"), [Impulse Force COMP](<./Impulse_Force_COMP.md> "Impulse Force COMP"), [Constraint COMP](<./Constraint_COMP.md> "Constraint COMP"), [Bullet Solver CHOP](<./Bullet_Solver_CHOP.md> "Bullet Solver CHOP"). 

There are a number of OP Snippets for Bullet. 

### 

What is possible with Bullet and TouchDesigner?

Bullet allows you to create realistic rigid body physics simulations in TouchDesigner, using the Bullet Dynamics operators. User interaction can be added to the simulation using the feedback parameter on the Bullet Solver COMP and Actor COMP, along with the Bullet Solver CHOP. Some examples of interactions you can add to a simulation: grabbing objects in VR or using a Leap Motion to create forces on objects. 

Using a feedbacking system, the [multiTouch](<./Palette-multiTouch.md> "Palette:multiTouch") example in the Palette implements user interaction with the discs. The MultiTouch example uses a [Render Pick DAT](<./Render_Pick_DAT.md> "Render Pick DAT") to determine if a disc is selected with the mouse. If the disc is selected, then the simulation data from the [Bullet Solver CHOP](<./Bullet_Solver_CHOP.md> "Bullet Solver CHOP") is overridden using a [Switch CHOP](<./Switch_CHOP.md> "Switch CHOP"). Once selected, the disc will follow the position of the touch/cursor input. This is done by modifying the velocity of the disc each frame based on the difference in touch/cursor positions from frame to frame. 

**NOTE:** When implementing a user interaction system, it is preferable to override the velocity of a body instead of directly overriding its position. This is because when overriding the position, the body will not have any momentum/inertia, so any collisions with other bodies while interacting with the body will be inaccurate. In the context of the simulation, if you are modifying the position of a body directly it interprets this as teleportation. 

### 

How to use Bullet in TouchDesigner

In TouchDesigner, the Bullet Solver COMP is the primary operator of any physics simulation. It is responsible for running the simulation and solving for the transformations and velocities of each body that is in the simulation. Actor COMPs represent the bodies in the simulation, and Impulse Force/Force COMPs represent the forces. 

In TouchDesigner and Bullet, units are typically referred to in meters. However, consistency of units is what's really important. It doesn't matter what units are used so long as the same units are used across all OPs in the simulation. This means that an entire simulation can be scaled up by 10 (all parameters including velocity/forces) and still have the same results. This is important to keep in mind because Bullet simulations will not perform as well (clipping, poor collision) for small objects (ie. below 10cm in size). The solution there is to simply scale everything up. 

Here are the basic steps for creating a physics simulation in TouchDesigner: 
1. Create a Bullet Solver COMP operator, this is your Bullet simulation engine. It will contain all bodies/forces.
  2. Create the desired amount of bodies you want in the simulation by creating Actor COMPs inside the Bullet Solver COMP. Ensure that all Actor COMPs are referenced in the "Actors" parameter on the Bullet Solver COMP. If the bodies are copies of each other, then instancing can be used instead of using multiple Actor COMPs. Ensure the display flag of each Actor COMP is on so it can be seen in the Bullet Solver COMP viewer.
  3. Choose the Kinematic State of each Actor.
  4. Create a collision shape for the Actor using the "Collision SOPs" path. This is a reference to SOPs that will be used to create the collision shape. Turn the display parameter on so it can be seen inside the Actor COMP viewer.
  5. Choose what shape the collision shape of the SOPs will be using the "Collision Shape" parameter.
  6. Set the initial transform of the Actor on the Xform and Pre-Xform pages.
  7. Set any additional properties of the Actor, such as mass, friction, initial velocity etc.
  8. Press the "Initialize Actor" pulse on each Actor COMP
  9. Create the desired amount of forces you want in the simulation. There are currently two types of forces available, the Force COMP, and the Impulse Force COMP. They can either be referenced by the Bullet Solver COMP as a global force, or individually by an Actor COMP as a local force.
  10. Press the "Start Sim" pulse on the Bullet Solver COMP to begin running the simulation. This will begin to modify the transformations and velocities of any bodies.

### 

Collision Shapes

There are 7 available collision shape methods to choose from, each with their own pros and cons. 

**Concave and Compound** – These methods create a collision shape that is as accurate as possible. For static shapes, this means creating a concave shape out of the given SOPs. For dynamic shapes a convex hull will be created for each SOP, and then each convex hull will be combined into a single compound collision shape. With this method dynamic concave shapes can be created, but each individual SOP can still only be convex. 

**Convex Hull** – This method creates a convex hull of the SOPs. The resulting collision shape is reasonably accurate; however, it will not be completely accurate for any very concave SOPs. This may be desired though. For instance, if you have an open jar, but you do not want anything to go inside of it, then selecting convex hull will put an invisible lid on the top. Convex hull collision detection can be slow, especially if the hull has a lot of points. For this reason, it might not be best to use a convex hull for SOPs with large amounts of "exterior" points. 

**Oriented Bounding Box** – This method creates a bounding box around the SOPs, oriented to minimize volume. Collision detection between boxes is generally much quicker than convex hulls, however accuracy is sacrificed with bounding boxes. In some cases, the minimum volume oriented bounding box can be very inaccurate, so whether a bounding box is suitable as the collision shape depends highly on the SOPs being used. For example, a bounding box around a sphere will leave large gaps at the corners. 

**Axis-Aligned Bounding Box** – This method creates a minimum volume bounding box aligned with the XYZ axes (ie. No rotation) around the SOPs. This method has the same benefits as an oriented bounding box, but it also suffers from the same problems. Because it must be aligned with the axes, an axis-aligned bounding box will generally be less accurate than an oriented bounding box, except in simple cases such as a sphere, or any other uniform convex shape. 

**Bounding Ellipsoid** – This method creates a minimum volume bounding ellipsoid around the SOPs, within a certain tolerance. The bounding ellipsoid is reasonably accurate and can be as close in accuracy to the convex hull in certain cases. Collision detection on bounding ellipsoids is faster than on convex hulls because they will generally have fewer points. Bounding ellipsoids have a constant 49 points. However, the algorithm for creating the minimum volume bounding ellipsoid can be slow for SOPs with large amounts of points. The "Ellipsoid Tolerance" parameter helps to mitigate this. The Ellipsoid tolerance parameter is an accuracy tolerance that defines how close the bounding ellipsoid will be to the optimal solution. 

**Bounding Sphere** – This method creates a bounding sphere around the SOPs. Collision detection for spheres is the fastest of all the options available. Bounding spheres are reasonably accurate for uniform SOPs (ie. XYZ extents are close). However, bounding spheres can be terribly inaccurate for certain SOPs, mainly when there is a large discrepancy in the XYZ extents. For instance, if you create a bounding sphere of a 100x100 XY plane, then the result will have a sphere with a very large radius in order to enclose the XY extents of the plane, even though the SOPs Z extent is very small.
