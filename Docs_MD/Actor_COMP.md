# Actor COMP

## 

Summary

An Actor COMP is analogous to a body (or bodies) in a physics system. An Actor COMP must be used in conjunction with a physics solver: either a [Bullet Solver COMP](<./Bullet_Solver_COMP.md> "Bullet Solver COMP") or [Nvidia Flex Solver COMP](<./Nvidia_Flex_Solver_COMP.md> "Nvidia Flex Solver COMP"), which in turn is analogous to the world/simulation that the actors/bodies operate in. An Actor COMP can either be static, meaning it is not affected by any forces in the simulation and cannot move (ie. has infinite mass), or it can be dynamic, meaning it is moved by forces and collides with other bodies (either static or dynamic) in the world. 

See also: [Flex](<./Flex.md> "Flex"), [Bullet Dynamics](<./Bullet_Dynamics.md> "Bullet Dynamics"), [Bullet Solver COMP](<./Bullet_Solver_COMP.md> "Bullet Solver COMP"), [Force COMP](<./Force_COMP.md> "Force COMP"), [Constraint COMP](<./Constraint_COMP.md> "Constraint COMP"), [Bullet Solver CHOP](<./Bullet_Solver_CHOP.md> "Bullet Solver CHOP"), [Nvidia Flex Solver COMP](<./Nvidia_Flex_Solver_COMP.md> "Nvidia Flex Solver COMP"), [Nvidia Flex TOP](<./Nvidia_Flex_TOP.md> "Nvidia Flex TOP"). 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[actorCOMP_Class](<./ActorCOMP_Class.md> "ActorCOMP Class")

## 

Usage

### 

Actors in Bullet

Static bodies can be concave or convex, but dynamic bodies must be convex. However, dynamic collision shapes can be compound, meaning it is a collision shape made of other collision shapes. So, a concave collision shape can be created in the dynamic case by building it out of a group of convex shapes. This can be done using multiple SOPs. Each SOP must be convex, but combination of the SOPs does not need to be. If Automatic mode is selected, then a compound collision shape will be created from these SOPs. 

All bodies in an Actor COMP have a corresponding collision shape. The collision shape is what determines how objects will collide with one another, and it is important to note that what is seen in the viewer/render will not necessarily directly match the collision shape. 

Collision shapes are created using SOPs, either through the "Collision SOPs" parameter or by putting them inside the Actor COMP itself. If the "Collision SOPs" parameter is filled in, then the Actor COMP will create a single body from all the SOPs at that given paths (if the path is a COMP then it will recursively grab all the SOPs in the COMP). If there is nothing filled in for the "Collision SOPs" parameter, then the Actor COMP will instead recursively search inside itself for any SOPs that have both their display and render flags on. The Actor COMP will create a single body and corresponding collision shape from these SOPs. 

There are several options when it comes to creating a collision shape out of the SOPs. These options can be chosen from the "Collision Shape" parameter. For instance, the option "Oriented Bounding Box" will create a minimum volume bounding box around the selected SOPs. 

To create multiple bodies, use the instancing on the "Instance" page of the Actor COMP. This will create any number of identical bodies, each with their own identical collision shape. Currently there is no way to create multiple non-identical bodies in a single Actor COMP. 

Bodies are initialized using the "Initialize Actor" parameter, so if any changes are made to the SOPs that create the bodies, then the Actor COMP must be reinitialized. Bodies will automatically be re-initialized if the Kinematic State, Shape, or Center of Mass is changed. 

Transforms can be applied to an Actor COMP using the Xform and Pre-Xform pages, much like on a Geometry COMP or Camera COMP. The transforms on the Xform and Pre-Xform pages create the initial transform of the actor in the simulation, but they can also be used to modify the transform of an actor during a simulation. Changing scale on either page will require a reinitialization of the actor since it changes the collision shape itself. Modifying any of the transforms while instancing will automatically reinitialize the actor. 

Actor COMPs cannot be nested; however, Actor COMPs can be nested inside Geometry COMPs and vice versa. Geometry COMPs with a nested Actor COMPs cannot have any scale transform; however, Geometry COMPs nested inside an Actor COMP can have scale. An Actor COMP nested inside Geometry COMPs will use their transform only when it is initialized. Therefore, any changes to the transform of these Geometry COMPs will require a reinitialization of the Actor COMP. 

### 

Actors in Flex

[Flex](<./Flex.md> "Flex") actors can either be fluid particles, a fluid particle emitter, or a static shape. 

Static shapes in Flex are built in the same way that concave (ie. static) shapes are built in Bullet. Static shapes require a triangle mesh SOP to build up their collision shape. However, box/sphere collision shape options can also be used to create a bounding box/sphere of the collision shape SOP. 

Fluid particles behave much the same way as instancing on a Bullet actor. The number of fluid particles is equal to the number of instances created from an instance OP. The instance parameters are used to give the particle an initial transform, but once the simulation is running the transform is updated from the simulation results. 

One key difference of a fluid particle Actor COMP is that no SOP is needed to create a fluid particle since their size/behaviour is defined through the simulation parameters on the [Nvidia Flex Solver COMP](<./Nvidia_Flex_Solver_COMP.md> "Nvidia Flex Solver COMP"). A SOP in the Actor COMP can be used to the render/display the positions of the particles. Alternatively, the particle positions can be fetched using the [Nvidia Flex TOP](<./Nvidia_Flex_TOP.md> "Nvidia Flex TOP"). 

Fluid emitters add particles to the scene at the emission point (ie. the transform of the Actor COMP). Particles are added up until the emission maximum is reached, at which point emission particles will be recycled from already existing particles. 

### 

Using an Actor COMP

When creating an Actor COMP there are some important questions to consider: 
* **Will this Actor be in a Bullet or Flex simulation?** There are many commonalities between Bullet actors and Flex actors, however they do differ in their functionality, meaning that not all parameters overlap. For Bullet specific parameters see the Bullet page of the Actor COMP and for Flex specific parameters see the Flex page of the Actor COMP.
  * **Will the bodies move?** A moving body's Kinematic State must be dynamic. A static body can "move" by overriding its position, but this is not recommended since clipping can easily occur and and collisions will be incorrect (because the bodies won't have momentum).
  * **What SOPs will be used to create the collision shape?** Every Actor COMP has a corresponding collision shape that is created from SOPs. The SOPs can be set through the Collision SOPs parameter, or if that parameter is not set, through the display/render flags of SOPs inside the Actor COMP.
  * **What collision shape will be used?** The SOPs gathered in the previous stage are used to create the collision shape. Each collision shape has their own pros and cons, which are outlined on the [Bullet Dynamics](<./Bullet_Dynamics.md> "Bullet Dynamics") page. The collision shape is what determines how the body will interact with other bodies (ie. collide). The collision shape does not necessarily correspond with what is displayed/rendered. The collision shape can be shown using the Display Collision Shape toggle.
  * **Will the collision shape be concave?** If the collision shape is concave and static, simply select Concave from the drop-down menu. If the collision shape is to be concave and dynamic then there is an extra step: convex decomposition. The collision shape must be a Compound collision shape (ie. a group of convex collision shapes) where each part of the compound shape is convex, but combined together create a concave shape. Each part of the compound shape is represented using a single SOP. Consider the letter "T" as an example. "T" is concave so it will need to be split into two separate convex parts: the top line and the bottom line. 2 SOPs would be created (one for each line) for the collision shape that when combined together form the full concave "T". If the "T" were static however, it could remain as 1 SOP.

### 

Why are my bodies not colliding?

To understand why two bodies might not collide it is important to understand that Bullet simulates discretely. Speed, position, constraints, collisions are all calculated on a frame by frame basis, as opposed to continuously. In the case of Bullet, collisions are calculated at the beginning and the end of a frame. What this means is that if a body is moving a large distance every frame it can clip through other bodies, because it's not colliding with it at the beginning or the end of the frame when collision is calculated. In the same vein, if an object is very thin then other bodies will be able to clip through it easier than something with more depth because bodies won't have to move as far in a frame to completely jump over it. 

Continuous collision detection (see parameter) helps to fix this by performing collision detection along the movement vector (between start/end of frame) so that collisions happening between the start/end of frame will be caught. This helps significantly with high linear velocity bodies, but not so much high angular velocity bodies. 

A couple other things to consider changing to fix body "leaking": 
1. Manually limit the velocity of bodies, or lower the strength of the forces being applied.
  2. Add depth to very thin collision surfaces. If you're using a Grid SOP as a collision surface, consider using a Box SOP instead. Or, if you're using a Box SOP as the collision shape to contain other bodies inside, consider making the collision shape out of 6 individual Box SOPs (one for each side of the box) combined together.

## 

Parameters - General Page

Initialize Actor`initialize`\- Recreates the collision shapes for all the bodies in the Actor COMP. Also resets all velocities and position to their default state. Initialize Actor should be pulsed when any changes are made to the SOPs used for creating the collision shape, or for any changes to the instancing OP. 

Update Collision Shape`updatecs`\- If enabled the Actor COMP will automatically update collision shapes. This will occur when the "Collision SOPs" or "Collision Shape" parameters are changes or the underlying SOPs used to create the collision shape are changed (ie. when their cook count increases). 

Update Collision Shape`updatecspulse`\- When clicked this will instantly update the collosion shape. 

Active`active`\- Toggle the actor on/off. If the actor is active, then it will be updated as the simulation progress. However, if it is inactive, then it will be removed from the simulation and no longer collide with any of the other actors/bodies. As a result, it's transform will also no longer be updated. 

Kinematic State`kinstate`\- ⊞ \- The kinematic state defines the Actor COMPs ability to move from external forces. If an object is dynamic, then it is moveable in the simulation, but if it static then it is not. 
* Static (Infinite Mass)`static`\- The bodies in this COMP cannot be moved in the simulation.
* Dynamic (Finite Mass)`dynamic`\- The bodies in this COMP can move.


Collision SOPs`sops`\- Specifies SOPs or COMPs to use for the collision shape. If a SOP is referenced, then just that SOP will be used for the collision shape. But if a COMP is selected then all SOPs inside of that (recursive) will be used for the collision shape. If this parameter is left blank, then the SOPs selected will be all SOPs inside the Actor COMP with display and render flags on. 

Collision Shape`shape`\- ⊞ \- The type of collision shape to make from the selected SOPs. Collision shapes can be viewed using a guide in the Actor COMP's viewer 
* Concave (Static only)`concave`\- Creates a concave collision shape out of all the SOPs. Should only be used for static Actor COMPs. The SOPs used for creating the concave collisions shape should only have polygons with either 3 or 4 vertices. If this mode is selected for a dynamic Actor COMP then a compound shape will be created instead.
* Convex Hull`convex`\- Creates a convex hull out of all the SOPs. A convex hull is a set of points that encloses all other points (in this case, the points from the SOPs), and the shape created from these points is convex. The points of the convex hull will be points from the original set of points (ie. the ones from the SOPs)
* Oriented Bounding Box`obb`\- Creates a bounding box around the SOPs that is oriented to minimize volume.
* Axis-Aligned Bounding Box`aabb`\- Creates a bounding box around the SOPs that has its axis aligned with XYZ (so it's not rotated).
* Bounding Ellipsoid`bellipsoid`\- Creates a minimum volume bounding ellipsoid around the SOP.
* Bounding Sphere`bsphere`\- creates a minimum volume bounding sphere around the SOPs. The difference between this and bounding ellipsoid is that all radii are the same (XYZ).
* Compound`compound`\- A compound collision shape is a collision shape composed of other collision shapes. If the Actor COMP is static then this has the same result as a concave shape. If the Actor COMP is dynamic then each SOP will be created into its own convex hull, then these will all be subsequently merged together into a single compound collision shape. This mode allows you to create concave collision shapes for dynamic bodies using multiple convex SOPs.


Ellipsoid Tolerance`elltol`\- The tolerance of the minimum volume bounding ellipsoid. In other words, how close to the optimal solution it is. 

Infinite Mass`infinitemass`\- Give the actor infinite mass. If the object is dynamic this will make it unmovable and static. Toggling infinite mass on or off will not require recreation of the collision shape, unlike changing the Kinematic State parameter. 

Mass`mass`\- The mass in kilograms of the actor. 

Cue Velocity`cuevel`\- Holds the linear and angular velocity and values given by linvel and angvel. The object will still collide with any other bodies in the simulation. 

Cue Pulse`cuevelpulse`\- Pulse the linear and angular velocity to values given by linvel and angvel. This will set the velocity to the given value at the beginning of the next frame. 

Linear Velocity`linvel`\- ⊞ \- The initial linear velocity of the actor in m/s. This parameter can also be used to modify an actor's linear velocity during a simulation. Additionally, it is used in conjunction with the "Cue Velocity" and "Cue Velocity Pulse" parameters. 
* Linear Velocity`linvelx`-
* Linear Velocity`linvely`-
* Linear Velocity`linvelz`-


Angular Velocity`angvel`\- ⊞ \- The initial angular velocity of the actor in degrees per second in m/s. This parameter can also be used to modify the actor's angular velocity during a simulation. Additionally, it is used in conjunction with the "Cue Velocity" and "Cue Velocity Pulse" parameters. 
* Angular Velocity`angvelx`-
* Angular Velocity`angvely`-
* Angular Velocity`angvelz`-

## 

Parameters - Bullet Page

Forces`forces`\- A list of local forces, meaning forces (ie. Force COMPs) that will only be applied to this actor. 

Use Global Gravity`globalgrav`\- Toggle for whether to use the Bullet Solver COMP's gravity (global), or its own local gravity. 

Gravitational Acceleration`gravity`\- ⊞ \- Actor's local gravity in m/s^2. Will only be applied if the actor is not using the Bullet Solver COMP's global gravity ie. the "Use Global Gravity" parameter above is turned off. 
* Gravitational Acceleration`gravityx`-
* Gravitational Acceleration`gravityy`-
* Gravitational Acceleration`gravityz`-


Friction`friction`\- The kinetic friction of the actor. It is the resistance between two bodies rubbing/sliding. The overall friction is the product of the two bodies touching. For example, if one body has 0 friction and the other has 1, then the overall friction between the two bodies is 0. 

Rolling Friction`rollfric`\- The rolling friction of the actor. It is the resistance/drag of one body (such as a sphere or cone) rolling on another. 

Restitution`rest`\- The coefficient of restitution of the actor. The coefficient of restitution is the ratio of the final to initial relative between two bodies/actors when they collide. In other words, restitution is the fraction of kinetic energy preserved after a collision. If two objects collide with 100% (ie. 1) restitution, then, both bodies will bounce off each other at the same speed at which they collided. 

Continuous Collision Detection`ccd`\- Toggles continuous collision detection on/off for this actor. Typically, collision detection is done discretely, meaning that collision is verified at the beginning/end of a frame. However, if a body is going too fast it will move too far in a single frame and therefore clip through any surfaces (ie. No collision detected). Continuous collision detection improves upon this by performing collision detection at intervals between the body's initial and final positions within a frame. Continuous collision detection can affect performance, so even if the parameter is toggled on it will not be used all the time. It will only be used for bodies moving above a velocity threshold. 

Display Guide`dispguide`\- Toggles on the display for the collision shape in the COMP viewer. 

Center of Mass`com`\- ⊞ \- Specifies the center of mass of the collision shape. The center of mass is the point around which the body will rotate. Center of mass can be viewed using a guide in the Actor COMP's viewer. It is shown as a red axis. 
* Center of Mass`comx`-
* Center of Mass`comy`-
* Center of Mass`comz`-


Bullet Feedback CHOP`bulletfb`\- A reference to a CHOP from which to feedback. The Actor COMP will read transformation and velocity data (in the correct format, see Bullet Solver CHOP for more information) from the CHOP, and overwrite the current values at the beginning of the next frame. A feedback loop can be created with this parameter and the Bullet Solver CHOP. See Bullet Solver CHOP. NOTE: scale cannot be feedbacked. force[xyz] and torque[xyz] can be used to apply forces to specific bodies. 

## 

Parameters - Flex Page

Triangle Collision Direction`tricolldir`\- ⊞ \- 
* Outward`outward`-
* Inward`inward`-
* Both`both`-


Flex Type`flextype`\- ⊞ \- The type of dynamic Flex actor. 
* Fluid`fluid`\- A fluid actor. The number of particles will be determined by the instance input count.
* Fluid Emitter`fluidemit`\- A fluid emitter actor. The number of particles will increase at a rate proportional to emission size and speed. Once the maximum is reached particles will be recycled from existing particles.


Enable Emission`emit`\- When enabled, the Actor COMP will actively emit particles. 

Emission Size`emitsize`\- ⊞ \- The size of the 2D emission grid. The size represents the number of particles on each side of the emission grid. For example, a 2x5 emission size will emit a grid 2 particles wide and 5 particles high. 
* Emission Size`emitsizex`-
* Emission Size`emitsizey`-


Emission Speed`emitspeed`\- The speed the particles come out of the emitter. 

Max Emission Particles`emitmax`\- Sets the maximum number of particles in the Actor COMP. Once this number is reached, emission will be done by recycling existing particles in the Actor COMP. 

Position Feedback TOP`flexposfb`\- A reference to a TOP to feedback position. The TOP should be encoded with the position data that will be used to override position in the simulation. The texture data will be read to correspond with the Flex TOP's position texture. 

Velocity Feedback TOP`flexvelfb`\- A reference to a TOP to feedback velocity. The TOP should be encoded with the velocity data that will be used to override velocity in the simulation. The texture data will be read to correspond with the Flex TOP's velocity texture. 

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

Parameters - Instance Page

The Instance parameter page provides the ability to create hardware instances of geometry. Each instance has an instance ID which can be passed into a [MAT](<./MAT.md> "MAT") shader via a uniform value. The instance ID can be retrieved by the [Render Pick CHOP](<./Render_Pick_CHOP.md> "Render Pick CHOP"). Any code in a vertex shader can customize the instance based on the instance ID. 

Instance's attributes can be individually driven by the data from any type of OP. When the instance data is supplied by a TOP, the TOP's RGBA channels are assigned to instance attributes, when data is supplied by a CHOP, the CHOP's channels are assigned to instance attributes, when from a SOP then the SOP's attributes are assigned to instance attributes, and when a DAT is used then a column is assigned to the instances attributes. The mapping of operator data to instance attributes is setup on the parameters below and on the Instance 2 and Instance 3 parameter pages. 

Instancing`instancing`\- Turns on instancing for the Geometry Component. 

Instance Count Mode`instancecountmode`\- ⊞ \- Two modes to determine how many instances will be created. 
* Manual`manual`\- Use the Num Instances parameter below to set the number of instances.
* Instance OP(s) Length`oplength`\- The number of CHOP samples/DAT rows in the Instance CHOP/DAT determines the number of instances.


Num Instances`numinstances`\- When using the Manual mode for Instance Count, this parameter set the number of instances. 

Default Instance OP`instanceop`\- Specify a path to a CHOP or DAT used to transform the instances. Number of samples/rows in this CHOP or DAT determines the number of instances when using the CHOP Length/DAT Num Rows mode for Instance Count. 

First Row is`instancefirstrow`\- ⊞ \- What to do with the first row of a table DAT when using DAT rows for Instance Count. 
* Ignored`ignored`\- The first row is ignored and it's values won't be used as part of an instance. Indices must be used to select the columns to use for instance attributes.
* Names`names`\- The first row contains column names which can be used to select which columns to use from the table.
* Values`values`\- The first row is considered to contain values for the first instance. Indices must be used to select the columns to use for instance attributes.


Transform Order`instxord`\- ⊞ \- Controls the order the transform operations will be applied to each instance. Refer to the documentation for the Xform page for more details. 
* Scale Rotate Translate`srt`-
* Scale Translate Rotate`str`-
* Rotate Scale Translate`rst`-
* Rotate Translate Scale`rts`-
* Translate Scale Rotate`tsr`-
* Translate Rotate Scale`trs`-


Rotate Order`instrord`\- ⊞ \- The rotational matrix presented when you click on this option allows you to set the transform order for the Component's rotations. As with transform order (above), changing the order in which the Component's rotations take place will alter the Component's final position. 
* Rx Ry Rz`xyz`-
* Rx Rz Ry`xzy`-
* Ry Rx Rz`yxz`-
* Ry Rz Rx`yzx`-
* Rz Rx Ry`zxy`-
* Rz Ry Rx`zyx`-


Translate OP`instancetop`\- Select a specific operator to get data from for the Translate instance attributes below. If not specified, the the operator specified in the 'Default Instance OP' on the Instance parameter page can be used. 

Active`instanceactive`\- Select the data channel that will be used to control which instances are rendered. Only instances with a non-zero value in this channel will be rendered; instances with a zero active channel value will be skipped. If no data is assigned to this channel then all instances are rendered. Use the drop-down menu on the right to easily select from the available options. 

Translate X`instancetx`\- Select what data to use to translate instances, use the drop-down menu on the right to easily select from the available options. 

Translate Y`instancety`\- Select what data to use to translate instances, use the drop-down menu on the right to easily select from the available options. 

Translate Z`instancetz`\- Select what data to use to translate instances, use the drop-down menu on the right to easily select from the available options. 

Rotate OP`instancerop`\- Select a specific operator to get data from for the Rotate instance attributes below. If not specified, the the operator specified in the 'Default Instance OP' on the Instance parameter page can be used. 

Rotate X`instancerx`\- Select what data to use to rotate instances, use the drop-down menu on the right to easily select from the available options. 

Rotate Y`instancery`\- Select what data to use to rotate instances, use the drop-down menu on the right to easily select from the available options. 

Rotate Z`instancerz`\- Select what data to use to rotate instances, use the drop-down menu on the right to easily select from the available options. 

Scale OP`instancesop`\- Select a specific operator to get data from for the Scale instance attributes below. If not specified, the the operator specified in the 'Default Instance OP' on the Instance parameter page can be used. 

Scale X`instancesx`\- Select what data to use to scale instances, use the drop-down menu on the right to easily select from the available options. 

Scale Y`instancesy`\- Select what data to use to scale instances, use the drop-down menu on the right to easily select from the available options. 

Scale Z`instancesz`\- Select what data to use to scale instances, use the drop-down menu on the right to easily select from the available options. 

Pivot OP`instancepop`\- Select a specific operator to get data from for the Pivot instance attributes below. If not specified, the the operator specified in the 'Default Instance OP' on the Instance parameter page can be used. 

Pivot X`instancepx`\- Select what data to use for the pivot of the instances, use the drop-down menu on the right to easily select from the available options. 

Pivot Y`instancepy`\- Select what data to use for the pivot of the instances, use the drop-down menu on the right to easily select from the available options. 

Pivot Z`instancepz`\- Select what data to use for the pivot of the instances, use the drop-down menu on the right to easily select from the available options. 

## 

Parameters - Instance 2 Page

When the instance data is supplied by a TOP, the TOP's RGBA channels are assigned to instance attributes; when data is supplied by a CHOP, the CHOP's channels are assigned to instance attributes; when from a SOP then the SOP's attributes are assigned to instance attributes; and when a DAT is used then a column is assigned to the instances attributes. 

Rotate to Vector: Order`instancerottoorder`\- ⊞ \- Controls where in the transform equation the Rotate To Vector operation is applied. 
* Default`default`\- The Rotate to Vector operation will be applied before all other transform operations (except the pivot offset), regardless of their order of operation. E.g`T * R * S * (RotToVector) * Position`,`R * S * T * (RotToVector) * Position`.
* Pre-Rot`prerot`\- The Rotate To Vector operation will be applied after the main rotation as part of the TRS order. I.e`T * (RotToVector * R) * S * Position`,`(RotToVector * R) * S * T * Position`.
* Post-Rot`postrot`\- The Rotate To Vector operation will be applied before the main rotation as part of the TRS order. I.e`T * (R * RotToVector) * S * Position`,`(R * RotToVector) * S * T * Position`.


Rotate to Vector: Forward Direction`instancerottoforward`\- ⊞ \- Determine which axis for the geometry original orientation is considered 'forward'. That is, it'll treat the part of the geometry that is looking down that axis as the front and rotate it so it's aligned with the rotate to vector direction. 
* +X`posx`-
* -X`negx`-
* +Y`posy`-
* -Y`negy`-
* +Z`posz`-
* -Z`negz`-


Rotate to OP`instancerottoop`\- Select a specific operator to get data from for the Rotate to Vector instance attributes below. If not specified, the the operator specified in the 'Default Instance OP' on the Instance parameter page can be used. 

Rotate to Vector X`instancerottox`\- Select what data to use to rotate to vector instances, use the drop-down menu on the right to easily select from the available options. 

Rotate to Vector Y`instancerottoy`\- Select what data to use to rotate to vector instances, use the drop-down menu on the right to easily select from the available options. 

Rotate to Vector Z`instancerottoz`\- Select what data to use to rotate to vector instances, use the drop-down menu on the right to easily select from the available options. 

Rotate Up OP`instancerotupop`\- Select a specific operator to get data from for the Rotate Up instance attributes below. If not specified, the the operator specified in the 'Default Instance OP' on the Instance parameter page can be used. 

Rotate Up X`instancerotupx`\- Select what data to use to rotate up instances, use the drop-down menu on the right to easily select from the available options. 

Rotate Up Y`instancerotupy`\- Select what data to use to rotate up instances, use the drop-down menu on the right to easily select from the available options 

Rotate Up Z`instancerotupz`\- Select what data to use to rotate up instances, use the drop-down menu on the right to easily select from the available options 

Instance Order`instanceorder`\- ⊞ \- Sets how transforms are applied to the instances. 
* Instance, then World Transform`instanceworld`\- Use the individual instance transforms first, then apply the world transform (i.e. Xform and Pre-Xform parameter pages).`worldXform * instanceXForm * Position`* World Transform, then Instance`worldinstance`\- Use the world transform first, then apply the individual instance transforms.`instanceXForm * worldXForm * Position`Texture Mode`instancetexmode`\- ⊞ \- Set how the texture coordinates are applied to the instances. 
* Replace`replace`\- Replaces texture coordinates.
* Transform`transform`\- Offsets texture coordinates.


Tex Coord OP`instancetexcoordop`\- Select a specific operator to get data from for the Texture Coord instance attributes below. If not specified, the the operator specified in the 'Default Instance OP' on the Instance parameter page can be used. 

U`instanceu`\- Select what data to apply to texture coordinates of the instances, use the drop-down menu on the right to easily select from the available options. This interacts with the first texture layer [uv[0] attributes](<./Attribute.md> "Attribute") coming from the SOP. 

V`instancev`\- Select what data to apply to texture coordinates of the instances, use the drop-down menu on the right to easily select from the available options. This interacts with the first texture layer [uv[0] attributes](<./Attribute.md> "Attribute") coming from the SOP. 

W`instancew`\- Select what data to apply to texture coordinates of the instances, use the drop-down menu on the right to easily select from the available options. This interacts with the first texture layer [uv[0] attributes](<./Attribute.md> "Attribute") coming from the SOP. 

Color Mode`instancecolormode`\- ⊞ \- Controls how the instance color values interact with the SOPs ['Cd' (diffuse color)](<./Attribute.md> "Attribute") attribute. If the SOP doesn't have a 'Cd' attribute, then it will behave as if its 'Cd' is (1, 1, 1, 1). 
* Replace`replace`-
* Multiply`multiply`-
* Add`add`-
* Subtract`subtract`-


Color OP`instancecolorop`\- Select a specific operator to get data from for the Color instance attributes below. If not specified, the the operator specified in the 'Default Instance OP' on the Instance parameter page can be used. 

R`instancer`\- Select what data to apply to the diffuse color of the instances, use the drop-down menu on the right to easily select from the available options. These parameters will be combined/replaced with the SOPs 'Cd' attribute, as chosen by the Color Mode parameter. 

G`instanceg`\- Select what data to apply to the diffuse color of the instances, use the drop-down menu on the right to easily select from the available options. These parameters will be combined/replaced with the SOPs 'Cd' attribute, as chosen by the Color Mode parameter. 

B`instanceb`\- Select what data to apply to the diffuse color of the instances, use the drop-down menu on the right to easily select from the available options. These parameters will be combined/replaced with the SOPs 'Cd' attribute, as chosen by the Color Mode parameter. 

A`instancea`\- Select what data to apply to the diffuse color of the instances, use the drop-down menu on the right to easily select from the available options. These parameters will be combined/replaced with the SOPs 'Cd' attribute, as chosen by the Color Mode parameter. 

Instance Textures`instancetexs`\- ⊞ \- Specify the paths one or more TOP containing the textures to use with the instances. Wildcards and pattern matching is supported. 

Extend U`instancetexextendu`\- ⊞ \- 
* Hold`hold`-
* Zero`zero`-
* Repeat`repeat`-
* Mirror`mirror`-


Extend V`instancetexextendv`\- ⊞ \- 
* Hold`hold`-
* Zero`zero`-
* Repeat`repeat`-
* Mirror`mirror`-


Extend W`instancetexextendw`\- ⊞ \- 
* Hold`hold`-
* Zero`zero`-
* Repeat`repeat`-
* Mirror`mirror`-


Filter`instancetexfilter`\- ⊞ \- 
* Nearest`nearest`-
* Linear`linear`-
* Mipmap Linear`mipmaplinear`-


Anisotropic Filter`instancetexanisotropy`\- ⊞ \- 
* Off`off`-
* 2x`2x`-
* 4x`4x`-
* 8x`8x`-
* 16x`16x`-

### 

Instance Texturing

This feature allows for arbitrary textures to be applied to instances. The textures do not need to be the same resolution, and they don't need to be combined into an grouped format such as a 3D Texture or a 2D Texture array. Multiple TOPs can be specified using the "Instance Textures" parameter, and the texture that is applied per-instance is specified using the channel chosen in the "Texture Index" parameter. This is different from a 3D Texture or 2D Texture Array, which would use the W texture coordinate to select a texture from within a single texture. By default this texture will be used as the "Base Color Map" texture for a [PBR MAT](<./PBR_MAT.md> "PBR MAT"), and the Color Map for all other materials such as the [Phong MAT](<./Phong_MAT.md> "Phong MAT"). For materials that support more than one map, the map that this this feature replaces can be chosen in the material's parameters. Currently on Windows at most 16384 textures can be used at once, and on macOS at most 128 textures can be used at once. These numbers are reduced by other textures that are used by the render such as other maps, cone light lookup map etc. 

Tex Index OP`instancetexindexop`\- Select a specific operator to get data from for the Texture Index instance attribute below. If not specified, the the operator specified in the 'Default Instance OP' on the Instance parameter page can be used. 

Texture Index`instancetexindex`\- Select what data to select which texture to use for the instances, use the drop-down menu on the right to easily select from the available options. 

## 

Parameters - Instance 3 Page

Custom attributes allow arbitrary attributes to be assigned to instances, usable in a [GLSL MAT](<./GLSL_MAT.md> "GLSL MAT"). They can be accessed using`TDInstanceCustomAttrib0()`,`TDInstanceCustomAttrib1()`etc. For more information refer to [Write a GLSL Material](<./Write_a_GLSL_Material.md> "Write a GLSL Material"). These attributes will be ignored in other materials such as the [PBR MAT](<./PBR_MAT.md> "PBR MAT"). 

Below you can add more parameters as you require more custom attributes. Different GPUs will have a different number of maximum custom attributes supported. 

Custom Instance`instance`\- Sequence of arbitrary attributes to be assigned to instances 

OP`instance0customop`\- Select a specific operator to get data from for the instance attributes below. If not specified, the the operator specified in the 'Default Instance OP' on the Instance parameter page can be used. 

X`instance0customx`\- Select what data to use for this instance attribute, use the drop-down menu on the right to easily select from the available options. 

Y`instance0customy`\- Select what data to use for this instance attribute, use the drop-down menu on the right to easily select from the available options. 

Z`instance0customz`\- Select what data to use for this instance attribute, use the drop-down menu on the right to easily select from the available options. 

W`instance0customw`\- Select what data to use for this instance attribute, use the drop-down menu on the right to easily select from the available options. 

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

## 

Info CHOP Channels

Extra Information for the Actor COMP can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). 

### 

Specific Actor COMP Info Channels
* num_bodies -
* num_active_bodies -

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


  
TouchDesigner Build: Latest\nwikieditorwikieditorwikieditorwikieditormw-undo2022.241402021.100002020.236802020.200002019.146502018.28070

COMPs   
---  
Actor • [Ambient Light ](<./Ambient_Light_COMP.md> "Ambient Light COMP")• [Animation ](<./Animation_COMP.md> "Animation COMP")• [Annotate ](<./Annotate_COMP.md> "Annotate COMP")• [Base ](<./Base_COMP.md> "Base COMP")• [Blend ](<./Blend_COMP.md> "Blend COMP")• [Bone ](<./Bone_COMP.md> "Bone COMP")• [Bullet Solver ](<./Bullet_Solver_COMP.md> "Bullet Solver COMP")• [Button ](<./Button_COMP.md> "Button COMP")• [Camera Blend ](<./Camera_Blend_COMP.md> "Camera Blend COMP")• [Camera ](<./Camera_COMP.md> "Camera COMP")• [MediaWiki:Common.js ](<./MediaWiki-Common.md> "MediaWiki:Common.js")• [COMP ](<./COMP.md> "COMP")• [Component ](<./Component.md> "Component")• [Constraint ](<./Constraint_COMP.md> "Constraint COMP")• [Container ](<./Container_COMP.md> "Container COMP")• [Engine ](<./Engine_COMP.md> "Engine COMP")• [Environment Light ](<./Environment_Light_COMP.md> "Environment Light COMP")• [FBX ](<./FBX_COMP.md> "FBX COMP")• [Field ](<./Field_COMP.md> "Field COMP")• [Force ](<./Force_COMP.md> "Force COMP")• [Geo Text ](<./Geo_Text_COMP.md> "Geo Text COMP")• [Geometry ](<./Geometry_COMP.md> "Geometry COMP")• [GLSL ](<./GLSL_COMP.md> "GLSL COMP")• [Handle ](<./Handle_COMP.md> "Handle COMP")• [Impulse Force ](<./Impulse_Force_COMP.md> "Impulse Force COMP")• [Light ](<./Light_COMP.md> "Light COMP")• [List ](<./List_COMP.md> "List COMP")• [Null ](<./Null_COMP.md> "Null COMP")• [NVIDIA Flex Solver ](<./NVIDIA_Flex_Solver_COMP.md> "NVIDIA Flex Solver COMP")• [NVIDIA Flow Emitter ](<./NVIDIA_Flow_Emitter_COMP.md> "NVIDIA Flow Emitter COMP")• [OP Viewer ](<./OP_Viewer_COMP.md> "OP Viewer COMP")• [Parameter ](<./Parameter_COMP.md> "Parameter COMP")• [Replicator ](<./Replicator_COMP.md> "Replicator COMP")• [Select ](<./Select_COMP.md> "Select COMP")• [Shared Mem In ](<./Shared_Mem_In_COMP.md> "Shared Mem In COMP")• [Shared Mem Out ](<./Shared_Mem_Out_COMP.md> "Shared Mem Out COMP")• [Slider ](<./Slider_COMP.md> "Slider COMP")• [Table ](<./Table_COMP.md> "Table COMP")• [Text ](<./Text_COMP.md> "Text COMP")• [Time ](<./Time_COMP.md> "Time COMP")• [USD ](<./USD_COMP.md> "USD COMP")• [Widget ](<./Widget_COMP.md> "Widget COMP")• [Window ](<./Window_COMP.md> "Window COMP")
