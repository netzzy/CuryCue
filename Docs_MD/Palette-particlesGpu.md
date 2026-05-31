# Palette:particlesGpu

##   
  
Summary

particlesGpu is a compute shader based particle system. 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[Palette:particlesGpu Ext](<./Palette-particlesGpu_Ext.md> "Palette:particlesGpu Ext")

## 

Parameters - ParticlesGPU Page

Create`Create`\- ⊞ \- Specify how particles are being created. You can either create a certain number of particles all at once or create a certain number of particles on a per frame basis. 
* By Total Number of Particles`numParticles`\- Specify the total number of particles that should be simulated in this system. All the particles are spawned at the exact same time.
* By Particles per Frame`perFrame`\- Specify how many particles should be created per frame. The total number of particles will be a function between the number in`Birth`multiplied by the specified`Life`(in seconds) and the`Lifevariance`(also in seconds)


Particles`Particles`\- The total number of particles being simulated in the system. Only available when the`Create`parameter is set to "By Total Number of Particles". 

Birth`Birth`\- The number of particles spawned each frame. Only available when the`Create`parameter is set to "By Particles per Frame". 

Life`Life`\- The number of seconds a particle will be alive. 

Lifevariance`Lifevariance`\- A delta number of seconds that will be added or subtracted from the expected lifetime, specified in the`Life`parameter, of a particle. 

Size Type`Sizetype`\- ⊞ \- Select how the particle size is being determined. While the types "Constant" and "Random" are specified with below`Particle Size Min`and`Particle Size Max`parameters, the remaining options take particle attributes like "Age" or "Velocity" to lookup the size via a CHOP specified in the`Size Lookup`parameter. When choosing any of the four "Effector" types, the index into the lookup will be fetched from the "Effector" input to the particle system. 
* Constant`constant`\- The size of the particle is being set via the`Particle Size Min`parameter.
* Random`random`\- The size of the particle is a random value between the`Particle Size Min`and`Particle Size Max`parameters.
* Age`age`\- The size of the particle is determined by the CHOP referenced in the`Size Lookup`parameter with the particle's age as a normalized index into the CHOP.
* Velocity`velocity`\- The size of the particle is determined by the CHOP referenced in the`Size Lookup`parameter with the particle's velocity as a normalized index into the CHOP. Use the`Velocity Remap`parameter to scale velocity to a unit value.
* Effector R`er`\- The size of the particle is determined by the CHOP referenced in the`Size Lookup`parameter with the value of the "effector" input texture's red channel at the particles index position as a normalized index into the CHOP.
* Effector G`eg`\- The size of the particle is determined by the CHOP referenced in the`Size Lookup`parameter with the value of the "effector" input texture's green channel at the particles index position as a normalized index into the CHOP.
* Effector B`eb`\- The size of the particle is determined by the CHOP referenced in the`Size Lookup`parameter with the value of the "effector" input texture's blue channel at the particles index position as a normalized index into the CHOP.
* Effector A`ea`\- The size of the particle is determined by the CHOP referenced in the`Size Lookup`parameter with the value of the "effector" input texture's alpha channel at the particles index position as a normalized index into the CHOP.


Particle Size Min`Particlesizemin`\- Specify the Size of the particle. Only available when the`Size Type`parameter is set to "Constant" or "Random". 

Particle Size Max`Particlesizemax`\- Specify the maximum size of the particle. Only available when the`Size Type`parameter is set to "Random". 

Size Lookup (CHOP)`Sizelookup`\- A reference to a CHOP containing a single channel called "size" which is used as a lookup when the`Size Type`parameter is set to "Age", "Velocity" or one of the "Effector"s. 

Pos Limit Plane`Limitpos`\- ⊞ \- The`Pos Limit Plane`and`Neg Limit Plane`parameters describe a bounding box used for the`Hit Behaviour`of the particle. 
* Pos Limit Plane`Limitposx`-
* Pos Limit Plane`Limitposy`-
* Pos Limit Plane`Limitposz`-


Neg Limit Plane`Limitneg`\- ⊞ \- The`Neg Limit Plane`and`Pos Limit Plane`parameters describe a bounding box used for the`Hit Behaviour`of the particle. 
* Neg Limit Plane`Limitnegx`-
* Neg Limit Plane`Limitnegy`-
* Neg Limit Plane`Limitnegz`-


Hit Behaviour`Hit`\- ⊞ \- Specify what the particle should do when leaving the bounding box described via the`Pos Limit Plane`and`Neg Limit Plane`parameters. 
* None`none`\- The bounding box is ignored.
* Die on Contact`die`\- The particle dies at the moment it leaves the bounding box.
* Bounce on Contact`bounce`\- The particle bounces when trying to leave the bounding box.
* Avoid Bounds`avoid`\- The particle tries to avoid the edges of the bounding box.
* Stick`stick`\- The particle will stick on the bounding box.


Avoid Factor`Avoidfactor`\- Only available when the`Hit Behaviour`parameter is set to "Avoid Bounds". This currently controls how much the particle will try to avoid the bounds. Note: This will be deprecated. 

Display Bounds`Displaybounds`\- When set to "On" will render the bounding box in the final render. 

Mass`Mass`\- The particle's mass which has an influence on the forces. Currently not implemented. 

Drag`Drag`\- Drag describes the loss of velocity over time for a particle. 

Max Velocity`Maxvelocity`\- Clamp the maximum velocity of a particle. 

System Max Velocity`Systemmaxvelocity`\- The current maximum velocity of any particle in the system. This is read only and can be used in the`Velocity Remap`parameter. 

Velocity Remap`Remapvelocity`\- ⊞ \- When using a particle's velocity in conjunction with lookup curves for the size, color or forces attributes, the remap parameter can help to normalize the velocity value for lookups into the curves. One would look at the`System Max Velocity`parameter and use it in the second parameter to normalize all particles velocities. 
* Velocity Remap`Remapvelocity1`-
* Velocity Remap`Remapvelocity2`-


Speed`Speed`\- Can be used to speed up or slow down the simulation. This can have unwanted effects when driving parameters with time dependent values. 

Reset`Reset`\- Reset the particle system. 

## 

Parameters - Forces Page

Inital Velocity`Inital`\- ⊞ \- The contribution of the initial velocity to the particle's velocity when spawned. The initial velocity is derived from the Particle Source or "particleVelocity" input to the component. 
* Inital Velocity`Initalx`-
* Inital Velocity`Initaly`-
* Inital Velocity`Initalz`-


Initial Magnitude`Initialmagnitude`\- A multiplier to the`Initial Velocity`parameter. 

Initial Turbulence`Initialturbulence`\- Adds turbulence to the initial velocity. 

External Type`Externaltype`\- ⊞ \- Select how the external force is being determined. While the type "Constant" is specified with below parameters, the remaining options take particle attributes like "Age" or "Velocity" to lookup these values via a CHOP specified in the`External Lookup`parameter. When choosing any of the four "Effector" types, the index into the lookup will be fetched from the "Effector" input to the particle system. See the`External Lookup`parameter below for more information on the required CHOP channels. 
* Constant`constant`\- The external force is being calculated using the`External`,`External Magnitude`, and`External Variance`parameters.
* Age`age`\- The external force is determined by the CHOP referenced in the`External Lookup`parameter with the particle's age as a normalized index into the CHOP.
* Velocity`velocity`\- The external force is determined by the CHOP referenced in the`External Lookup`parameter with the particle's velocity as a normalized index into the CHOP. Use the`Velocity Remap`parameter to scale velocity to a unit value.
* Effector R`er`\- The external force is determined by the CHOP referenced in the`External Lookup`parameter with the value of the "effector" input texture's red channel at the particles index position as a normalized index into the CHOP.
* Effector G`eg`\- The external force is determined by the CHOP referenced in the`External Lookup`parameter with the value of the "effector" input texture's green channel at the particles index position as a normalized index into the CHOP.
* Effector B`eb`\- The external force is determined by the CHOP referenced in the`External Lookup`parameter with the value of the "effector" input texture's blue channel at the particles index position as a normalized index into the CHOP.
* Effector A`ea`\- The external force is determined by the CHOP referenced in the`External Lookup`parameter with the value of the "effector" input texture's alpha channel at the particles index position as a normalized index into the CHOP.


External`External`\- ⊞ \- The contribution of the external force to the particle's velocity. An External Force is a constant increase in velocity per frame, not unlike gravity. 
* External Force`Externalx`-
* External Force`Externaly`-
* External Force`Externalz`-


External Magnitude`Externalmag`\- A multiplier to the`External Force`parameter. 

External Variance`Externalvariance`\- An additional turbulence to the External Force. 

External Lookup (CHOP)`Externallookup`\- A reference to a CHOP containing 5 channels that represent the forces values: "externalx", "externaly", "externalz", "externalmag", and "externalvariance". Any missing channel will be assumed to have the value 0. 

Wind Type`Windtype`\- ⊞ \- Select how the wind force is being determined. While the type "Constant" is specified with below parameters, the remaining options take particle attributes like "Age" or "Velocity" to lookup these values via a CHOP specified in the`Wind Lookup`parameter. When choosing any of the four "Effector" types, the index into the lookup will be fetched from the "Effector" input to the particle system. See the`Wind Lookup`parameter below for more information on the required CHOP channels. 
* Constant`constant`\- The wind force is being calculated using the`Wind`,`Wind Magnitude`, and`Wind Variance`parameters.
* Age`age`\- The wind force is determined by the CHOP referenced in the`Wind Lookup`parameter with the particle's age as a normalized index into the CHOP.
* Velocity`velocity`\- The wind force is determined by the CHOP referenced in the`Wind Lookup`parameter with the particle's velocity as a normalized index into the CHOP. Use the`Velocity Remap`parameter to scale velocity to a unit value.
* Effector R`er`\- The wind force is determined by the CHOP referenced in the`Wind Lookup`parameter with the value of the "effector" input texture's red channel at the particles index position as a normalized index into the CHOP.
* Effector G`eg`\- The wind force is determined by the CHOP referenced in the`Wind Lookup`parameter with the value of the "effector" input texture's green channel at the particles index position as a normalized index into the CHOP.
* Effector B`eb`\- The wind force is determined by the CHOP referenced in the`Wind Lookup`parameter with the value of the "effector" input texture's blue channel at the particles index position as a normalized index into the CHOP.
* Effector A`ea`\- The wind force is determined by the CHOP referenced in the`Wind Lookup`parameter with the value of the "effector" input texture's alpha channel at the particles index position as a normalized index into the CHOP.


Wind`Wind`\- ⊞ \- The contribution of the wind force to the particle's velocity. A Wind Force is a constant increase in velocity per frame until the wind's velocity has been reached. 
* Wind`Windx`-
* Wind`Windy`-
* Wind`Windz`-


Wind Magnitude`Windmag`\- A multiplier to the`Wind`parameter. 

Wind Variance`Windvariance`\- An additional turbulence to the Wind Force. 

Wind Lookup (CHOP)`Windlookup`\- A reference to a CHOP containing 5 channels that represent the forces values: "windx", "windy", "windz", "windmag", and "windvariance". Any missing channel will be assumed to have the value 0. 

Turbulence Type`Turbtype`\- ⊞ \- Select how the turbulence force is being determined. While the type "Constant" is specified with below parameters, the remaining options take particle attributes like "Age" or "Velocity" to lookup these values via a CHOP specified in the`Turbulence Lookup`parameter. When choosing any of the four "Effector" types, the index into the lookup will be fetched from the "Effector" input to the particle system. See the`Turbulence Lookup`parameter below for more information on the required CHOP channels. 
* Constant`constant`\- The turbulence is being calculated using the`Turbulence`,`Turbulence Magnitude`,`Turbulence Period`,`Turbulence Seed`, and`Turbulence Speed`parameters.
* Age`age`\- The turbulence is determined by the CHOP referenced in the`Turbulence Lookup`parameter with the particle's age as a normalized index into the CHOP.
* Velocity`velocity`\- The turbulence is determined by the CHOP referenced in the`Turbulence Lookup`parameter with the particle's velocity as a normalized index into the CHOP. Use the`Velocity Remap`parameter to scale velocity to a unit value.
* Effector R`er`\- The turbulence is determined by the CHOP referenced in the`Turbulence Lookup`parameter with the value of the "effector" input texture's red channel at the particles index position as a normalized index into the CHOP.
* Effector G`eg`\- The turbulence is determined by the CHOP referenced in the`Turbulence Lookup`parameter with the value of the "effector" input texture's green channel at the particles index position as a normalized index into the CHOP.
* Effector B`eb`\- The turbulence is determined by the CHOP referenced in the`Turbulence Lookup`parameter with the value of the "effector" input texture's blue channel at the particles index position as a normalized index into the CHOP.
* Effector A`ea`\- The turbulence is determined by the CHOP referenced in the`Turbulence Lookup`parameter with the value of the "effector" input texture's alpha channel at the particles index position as a normalized index into the CHOP.


Turbulence`Turb`\- ⊞ \- The contribution of the turbulence to the particle's velocity. A turbulence is a position based lookup into a threedimensional noisefield defined with below parameters. 
* Turbulence`Turbx`-
* Turbulence`Turby`-
* Turbulence`Turbz`-


Turbulence Magnitude`Turbmag`\- A multiplier to the`Turbulence`parameter. 

Turbulence Period`Turbperiod`\- The period of the noise function. 

Turbulence Seed`Turbseed`\- The seed of the noise function. 

Turbulence Speed`Turbtrans`\- ⊞ \- This is currently an offset of the xyz lookup position in the noise field. When specifying a constant number the noise will be constant as well. 
* Turbulence Speed`Turbtransx`-
* Turbulence Speed`Turbtransy`-
* Turbulence Speed`Turbtransz`-


Turbulence Lookup (CHOP)`Turblookup`\- A reference to a CHOP containing 9 channels that represent the force values: "turbx", "turby", "turbz", "turbmag", "turbperiod", "turbseed", "turbtransx", "turbtransy", and "turbtransz". Any missing channel will be assumed to have the value 0. 

Extra Forces (CHOP)`Extraforceschop`\- Via a CHOP containing 9 channels, multiple positional forces of the types "Radial", "Axial", "Vortex", and "Spiral" can be defined. These forces try to mimick the behaviour of the [Force SOP](<./Force_SOP.md> "Force SOP") with some differences: The original SOP takes a [Metaball](<./Metaball.md> "Metaball") as an input and can apply all 4 forces at the same position with "Vortex" and "Spiral" interacting with each other. This implementation treats the force source as a wyvill type metaball and "Vortex" and "Spiral" do not interact but are calculated seperately. 

Multiple forces can be specified with a multisample CHOP where each sample represents a unique force field. 

The 9 required channels are: "forceposx", "forceposy", "forceposz", "forceradius", "forceamount", "forcetype", "forcedirx", "forcediry", and "forcedirz". The value of "forcetype" can be one of: 
* 0: Radial force
  * 1: Axial force
  * 2: Vortex force and
  * 3: Spiral force


The "forcedir*" channels are only required for the directional forces "Axial", "Vortex", and "Spiral". See the [Force SOP](<./Force_SOP.md> "Force SOP") for more information on these different force types. Any missing channel will be assumed to have the value 0. __

Display Extra Forces`Displayextraforces`\- Displays a wireframe sphere in place of any of the extra forces whose "forceAmount" value is greater than 0. 

Optical Flow Magnitude`Optflowmag`\- A multiplier to the force values retrieved from the Optical Flow input. 

Optical Flow Remap`Optflowremap`\- ⊞ \- Remap Size parameter for the Optical Flow input. To sample from the Optical Flow texture, the x and y positions of the particles are used. As these most likely extend beyond 0-1, specify here the maximum bounds of the particles in either direction. For example for a particle system where some particles are located at x=-10, y=5, set the remap parameter to 10 and 5 respectively. This means that any particle's position in the range of x: -10 to 10 and y: -5 to 5 will be remapped to 0 to 1 as a lookup into the Optical Flow texture. 
* Inputsize Remap`Inputsizeremapx`-
* Inputsize Remap`Inputsizeremapy`-


Rotation Type`Rotationtype`\- ⊞ \- Select what kind of rotation the particles are subjected to. Note: this only has an effect on Materials choosed on the "Material" paramter page, that are not of the [Line MAT](<./Line_MAT.md> "Line MAT") type. 
* None`none`\- There is no rotation. The particles will be oriented to the XY plane.
* Velocity`velocity`\- The particles are oriented towards the velocity vector of the particle. Especially in conjunction with a phong material, this can give the impression of shading.
* Face Camera`billboard`\- All particles are rotated towards the camera.
* Continous`continous`\- Particles are rotating continiously.


Rotation Speed`Rotationspeed`\- ⊞ \- Specify the speed at which particles are rotating. A speed of 1 will rotate the partice by one degree per frame. 
* Rotation Speed`Rotationspeedx`-
* Rotation Speed`Rotationspeedy`-
* Rotation Speed`Rotationspeedz`-


Randomize Initial Rotation`Rotationrandom`\- Toggle on to have the particles spawned with a random rotation. 

Rotation Init`Rotationinit`\- ⊞ \- Specify the rotation of spawned particles. The rotation is represented as a vector. 
* Rotation Init`Rotationinitx`-
* Rotation Init`Rotationinity`-
* Rotation Init`Rotationinitz`-

## 

Parameters - Render Page

Resolution`Resolution`\- ⊞ \- Specify the resolution of the final render of the particle system. 
* Resolution`Resolutionw`-
* Resolution`Resolutionh`-


Fade In`Fadein`\- Specify the time in seconds a particle fades in after being spawned. 

Fade Out`Fadeout`\- Specify the time in seconds a particle fades out before dying. 

Color Type`Colortype`\- ⊞ \- Select how the particle color is being determined. While the types "Constant" and "Random" are specified with below`Color 1`and`Color 2`parameters, and "Velocity" as well as "Turbulence" are driven by the respective particle attributes, the remaining options take particle attributes like "Age" or "Velocity" to lookup the size via a CHOP specified in the`Color Lookup`parameter. When choosing any of the four "Effector" types, the index into the lookup will be fetched from the "Effector" input to the particle system. 
* Constant`constant`\- The particle's color is specified via the`Color 1`parameter.
* Random`random`\- The particle's color is randomly picked between the`Color 1`and`Color2`parameters.
* Velocity`velocity`\- The particle's color is the same value as the particles velocity.
* Turbulence`turb`\- The particle's color is the same as the value of the turbulence force it might be traversing.
* Age (Lookup)`ageL`\- The color of the particle is determined by the CHOP referenced in the`Color Lookup`parameter with the particle's age as a normalized index into the CHOP.
* Velocity (Lookup)`velocityL`\- The color of the particle is determined by the CHOP referenced in the`Color Lookup`parameter with the particle's velocity as a normalized index into the CHOP. Use the`Velocity Remap`parameter to scale velocity to a unit value.
* Effector R`er`\- The color of the particle is determined by the CHOP referenced in the`Color Lookup`parameter with the value of the "effector" input texture's red channel at the particles index position as a normalized index into the CHOP.
* Effector G`eg`\- The color of the particle is determined by the CHOP referenced in the`Color Lookup`parameter with the value of the "effector" input texture's green channel at the particles index position as a normalized index into the CHOP.
* Effector B`eb`\- The color of the particle is determined by the CHOP referenced in the`Color Lookup`parameter with the value of the "effector" input texture's blue channel at the particles index position as a normalized index into the CHOP.
* Effector A`ea`\- The color of the particle is determined by the CHOP referenced in the`Color Lookup`parameter with the value of the "effector" input texture's alpha channel at the particles index position as a normalized index into the CHOP.


Color 1`Color1`\- ⊞ \- The color of the particle if`Color Type`is set to "Constant" or "Random" 
* Color 1`Color1r`-
* Color 1`Color1g`-
* Color 1`Color1b`-
* Color 1`Color1a`-


Color 2`Color2`\- ⊞ \- If`Color Type`is set to "Random", the particle's color will be a random value between`Color 1`and this parameter. 
* Color 2`Color2r`-
* Color 2`Color2g`-
* Color 2`Color2b`-
* Color 2`Color2a`-


Color Lookup (CHOP)`Colorlookup`\- A reference to a CHOP containing 3 channels that represent the color values: "r", "g", "b", and "a". Any missing channel will be assumed to have the value 1. 

Camera`Camera`\- Specify a custom [Camera COMP](<./Camera_COMP.md> "Camera COMP") to render the particle system. 

Compositing`Compositing`\- ⊞ \- 
* Alpha To Coverage`coverage`-
* Discard Alpha`discard`-
* Order-Independent Transparency`independent`-
* No Depth Test`nodepth`-


Transparancy Layers`Transparancylayers`\- 

Alpha Threshold`Alphathreshold`\- 

## 

Parameters - Material Page

Material`Material`\- ⊞ \- Select which material type should be used for the particle system render. For the types "Constant" and "Phong" a texture can be selected or specified. 
* Constant`constant`\- The particle system is rendered with a [Constant MAT](<./Constant_MAT.md> "Constant MAT")
* Phong`phong`\- The particle system is rendered with a [Phong MAT](<./Phong_MAT.md> "Phong MAT")
* Line`line`\- The particle system is rendered with a [Line MAT](<./Line_MAT.md> "Line MAT")
* custom`custom`\- A custom material can be specified via the`Custom Material`parameter.


Custom Material`Custommaterial`\- Reference to a [MAT](<./MAT.md> "MAT") to be used as the material for rendering the particle system. 

Texture`Texture`\- ⊞ \- In case of selecting a "Constant" or "Phong" material, a texture can be selected that will be used for shading the particle. 
* Square`square`\- A simple square resulting in a constant color.
* Circle`circle`\- A circle texture.
* Snow`snow`\- a snowflake image.
* Leaf`leaf`\- A 2D Texture Array of 5 different leafs.
* Character`char`\- A 2D Texture Array of 60 different charachters.
* Custom`custom`\- Specify a custom texture in the`Particle Texture Map`parameter which can also be of the type 2D Texture Array.


Particle Texture Map`Particlemap`\- A reference to a TOP containing the texture to be used on the particles. 

## 

Parameters - Particle Source Page

Interpolate Source Point Position`Interpolatepoint`\- When using a low resolution source object, toggling this parameter will spawn particles from interpolated positions of the original source. 

Num Points`Numpoints`\- Specify the number of points the source shape should have. 

Shape`Shape`\- ⊞ \- Select what type of shape the source should be. 
* Sphere`sphere`\- A sphere volume.
* Box`box`\- A box volume.
* Torus`torus`\- A torus volume.
* Sphere Surface`spheresurf`\- A sphere surface.
* Box Surface`boxsurf`\- A box surface.
* Torus Surface`torussurf`\- A torus surface.
* Rectangle`rectangle`\- A rectangle.
* Circle`circle`\- A circle. (Only points along the circle are created.)
* Disc`disc`\- A disc. (There are also points inside the circle.)
* Line`line`\- A line defined by a start and an endpoint.


Orientation`Orientation`\- ⊞ \- 
* XY Plane`xy`\- Specifies the orientation of the shape. This is useful for type: "Torus", "Torus Surface", "Rectangle", "Circle", and "Disc".
* YZ Plane`yz`-
* ZX Plane`zx`-


Size`Shapesize`\- ⊞ \- The size of the generated shape when type is "Box", "Box Surface", or "Rectangle". 
* Size`Shapesizex`-
* Size`Shapesizey`-
* Size`Shapesizez`-


Radius`Radius`\- ⊞ \- The radius of the generated shape when type is "Sphere", "Torus", "Sphere Surface", "Torus Surface", "Circle", or "Disc" 
* Radius`Radiusx`-
* Radius`Radiusy`-
* Radius`Radiusz`-


Point A`Pa`\- ⊞ \- Starting point of a shape if type is "Line". 
* Point A`Pax`-
* Point A`Pay`-
* Point A`Paz`-


Point B`Pb`\- ⊞ \- End point of a shape if type is "Line". 
* Point B`Pbx`-
* Point B`Pby`-
* Point B`Pbz`-


Random Seed`Randomseed`\- Random seed of the point order. 

Transform`Transform`\- 

Transform Order`Xord`\- ⊞ \- 
* Scale Rotate Translate`srt`-
* Scale Translate Rotate`str`-
* Rotate Scale Translate`rst`-
* Rotate Translate Scale`rts`-
* Translate Scale Rotate`tsr`-
* Translate Rotate Scale`trs`-


Rotate Order`Rord`\- ⊞ \- 
* Rx Ry Rz`xyz`-
* Rx Rz Ry`xzy`-
* Ry Rx Rz`yxz`-
* Ry Rz Rx`yzx`-
* Rz Rx Ry`zxy`-
* Rz Ry Rx`zyx`-


Translate`T`\- ⊞ \- 
* Translate`Tx`-
* Translate`Ty`-
* Translate`Tz`-


Rotate`R`\- ⊞ \- 
* Rotate`Rx`-
* Rotate`Ry`-
* Rotate`Rz`-


Scale`S`\- ⊞ \- 
* Scale`Sx`-
* Scale`Sy`-
* Scale`Sz`-


Pivot`P`\- ⊞ \- 
* Pivot`Px`-
* Pivot`Py`-
* Pivot`Pz`-


Show Emitter Source`Showsource`\- 

## 

Parameters - About Page

Help`Help`\- 

Version`Version`\- 

## 

Operator Inputs
* Input 0: particleSource \- TOP containing all positions of the particle source. R, G, B channels correspond to X, Y, Z positions respectively.
  * Input 1: particleSourceColor \- TOP containing color values of the particle source.
  * Input 2: particleVelocity \- TOP containing the initial velocity values for each particle. R, G, B channels correspond to the velocity in X, Y, Z respectively.
  * Input 2: opticalFlow \- TOP containing a texture where the values in the red and green channels are interpreted as force vectors in for the particles in the x and y directions respectively. A source can be an optical flow operator.
  * Input 3: effector \- Input for a texture used in any of the Size, Force or Color Lookups. For example the z component of the particleGPU's position output, could be used as a lookup for the particle color.

## 

Operator Outputs
* Output 0 \- The render output of the particle system.
* Output 1 \- The positions of all particles.
* Output 2 \- The channels of the included Initialize / Start Component.


TouchDesigner Build: Latest\nwikieditorwikieditorwikieditorwikieditor2022.241402021.100002018.28070before 2018.28070

Palette  
---  
[Palette ](<./Palette.md> "Palette")• [Palette:arcBallCamera ](<./Palette-arcBallCamera.md> "Palette:arcBallCamera")• [Palette:arcBallGeometry ](<./Palette-arcBallGeometry.md> "Palette:arcBallGeometry")• [Palette:audioAnalysis ](<./Palette-audioAnalysis.md> "Palette:audioAnalysis")• [Palette:audioSet ](<./Palette-audioSet.md> "Palette:audioSet")• [Palette:autoMediaPlayer ](<./Palette-autoMediaPlayer.md> "Palette:autoMediaPlayer")• [Palette:battery ](<./Palette-battery.md> "Palette:battery")• [Palette:bitwigClip ](<./Palette-bitwigClip.md> "Palette:bitwigClip")• [Palette:bitwigClipSlot ](<./Palette-bitwigClipSlot.md> "Palette:bitwigClipSlot")• [Palette:bitwigDeviceRemotes ](<./Palette-bitwigDeviceRemotes.md> "Palette:bitwigDeviceRemotes")• [Palette:bitwigMain ](<./Palette-bitwigMain.md> "Palette:bitwigMain")• [Palette:bitwigNote ](<./Palette-bitwigNote.md> "Palette:bitwigNote")• [Palette:bitwigProjectRemotes ](<./Palette-bitwigProjectRemotes.md> "Palette:bitwigProjectRemotes")• [Palette:bitwigRemotesDevice ](<./Palette-bitwigRemotesDevice.md> "Palette:bitwigRemotesDevice")• [Palette:bitwigRemotesProject ](<./Palette-bitwigRemotesProject.md> "Palette:bitwigRemotesProject")• [Palette:bitwigRemotesTrack ](<./Palette-bitwigRemotesTrack.md> "Palette:bitwigRemotesTrack")• [Palette:bitwigSelect ](<./Palette-bitwigSelect.md> "Palette:bitwigSelect")• [Palette:bitwigSong ](<./Palette-bitwigSong.md> "Palette:bitwigSong")• [Palette:bitwigTrack ](<./Palette-bitwigTrack.md> "Palette:bitwigTrack")• [Palette:bitwigTrackRemotes ](<./Palette-bitwigTrackRemotes.md> "Palette:bitwigTrackRemotes")• [Palette:blendModes ](<./Palette-blendModes.md> "Palette:blendModes")• [Palette:bloom ](<./Palette-bloom.md> "Palette:bloom")• [Palette:camera ](<./Palette-camera.md> "Palette:camera")• [Palette:cameraBrowser ](<./Palette-cameraBrowser.md> "Palette:cameraBrowser")• [Palette:cameraViewport ](<./Palette-cameraViewport.md> "Palette:cameraViewport")• [Palette:camSchnappr ](<./Palette-camSchnappr.md> "Palette:camSchnappr")• [Palette:changeColor ](<./Palette-changeColor.md> "Palette:changeColor")• [Palette:changeToColor ](<./Palette-changeToColor.md> "Palette:changeToColor")• [Palette:checker ](<./Palette-checker.md> "Palette:checker")• [Palette:chromaKey ](<./Palette-chromaKey.md> "Palette:chromaKey")• [Palette:colorThreshold ](<./Palette-colorThreshold.md> "Palette:colorThreshold")• [Palette:compareComp ](<./Palette-compareComp.md> "Palette:compareComp")• [Palette:convolve ](<./Palette-convolve.md> "Palette:convolve")• [Experimental:Palette:cornerPinPOP ](</index.php?title=Experimental:Palette:cornerPinPOP&action=edit&redlink=1> "Experimental:Palette:cornerPinPOP \(page does not exist\)")• [Palette:cornerPinSOP ](<./Palette-cornerPinSOP.md> "Palette:cornerPinSOP")• [Palette:cppParsTemplateGen ](<./Palette-cppParsTemplateGen.md> "Palette:cppParsTemplateGen")• [Palette:customAttributes ](<./Palette-customAttributes.md> "Palette:customAttributes")• [Palette:debugControl ](<./Palette-debugControl.md> "Palette:debugControl")• [Palette:dent ](<./Palette-dent.md> "Palette:dent")• [Palette:depthExtract ](<./Palette-depthExtract.md> "Palette:depthExtract")• [Palette:depthProjection ](<./Palette-depthProjection.md> "Palette:depthProjection")• [Palette:dilate ](<./Palette-dilate.md> "Palette:dilate")• [Experimental:Palette:domeViewer ](</index.php?title=Experimental:Palette:domeViewer&action=edit&redlink=1> "Experimental:Palette:domeViewer \(page does not exist\)")• [Palette:encoder ](<./Palette-encoder.md> "Palette:encoder")• [Palette:equalizer ](<./Palette-equalizer.md> "Palette:equalizer")• [Palette:feedback ](<./Palette-feedback.md> "Palette:feedback")• [Palette:feedbackEdge ](<./Palette-feedbackEdge.md> "Palette:feedbackEdge")• [Palette:firmata ](<./Palette-firmata.md> "Palette:firmata")• [Palette:gal ](<./Palette-gal.md> "Palette:gal")• [Palette:geoPanel ](<./Palette-geoPanel.md> "Palette:geoPanel")• [Palette:gestureCapture ](<./Palette-gestureCapture.md> "Palette:gestureCapture")• [Palette:graphPlot ](<./Palette-graphPlot.md> "Palette:graphPlot")• [Palette:histogram ](<./Palette-histogram.md> "Palette:histogram")• [Palette:hsvBlur ](<./Palette-hsvBlur.md> "Palette:hsvBlur")• [Palette:imageSearch ](<./Palette-imageSearch.md> "Palette:imageSearch")• [Palette:julia ](<./Palette-julia.md> "Palette:julia")• [Palette:kantanMapper ](<./Palette-kantanMapper.md> "Palette:kantanMapper")• [Palette:kinectCalibration ](<./Palette-kinectCalibration.md> "Palette:kinectCalibration")• [Palette:kinectPointcloud ](<./Palette-kinectPointcloud.md> "Palette:kinectPointcloud")• [Palette:leapPaint ](<./Palette-leapPaint.md> "Palette:leapPaint")• [Palette:lightTunnel ](<./Palette-lightTunnel.md> "Palette:lightTunnel")• [Palette:logger ](<./Palette-logger.md> "Palette:logger")• [Experimental:Palette:logger ](</index.php?title=Experimental:Palette:logger&action=edit&redlink=1> "Experimental:Palette:logger \(page does not exist\)")• [Palette:mandelbrot ](<./Palette-mandelbrot.md> "Palette:mandelbrot")• [Palette:materialDesignIcons ](<./Palette-materialDesignIcons.md> "Palette:materialDesignIcons")• [Palette:mesh ](<./Palette-mesh.md> "Palette:mesh")• [Palette:monochrome ](<./Palette-monochrome.md> "Palette:monochrome")• [Palette:motionSense ](<./Palette-motionSense.md> "Palette:motionSense")• [Palette:movieEngine ](<./Palette-movieEngine.md> "Palette:movieEngine")• [Palette:moviePlayer ](<./Palette-moviePlayer.md> "Palette:moviePlayer")• [Palette:moviePlaylist ](<./Palette-moviePlaylist.md> "Palette:moviePlaylist")• [Palette:multiLevel ](<./Palette-multiLevel.md> "Palette:multiLevel")• [Palette:multiMix ](<./Palette-multiMix.md> "Palette:multiMix")• [Palette:noise ](<./Palette-noise.md> "Palette:noise")• [Palette:onScreenKeyboard ](<./Palette-onScreenKeyboard.md> "Palette:onScreenKeyboard")• [Palette:operatorPath ](<./Palette-operatorPath.md> "Palette:operatorPath")• [Palette:opticalFlow ](<./Palette-opticalFlow.md> "Palette:opticalFlow")• Palette:particlesGpu • [Palette:pixelate ](<./Palette-pixelate.md> "Palette:pixelate")• [Palette:pixelRelocator ](<./Palette-pixelRelocator.md> "Palette:pixelRelocator")• [Palette:pointGenerator ](<./Palette-pointGenerator.md> "Palette:pointGenerator")• [Palette:pointillize ](<./Palette-pointillize.md> "Palette:pointillize")• [Palette:pointMerge ](<./Palette-pointMerge.md> "Palette:pointMerge")• [Palette:pointRender ](<./Palette-pointRender.md> "Palette:pointRender")• [Palette:pointRepack ](<./Palette-pointRepack.md> "Palette:pointRepack")• [Palette:pointTransform ](<./Palette-pointTransform.md> "Palette:pointTransform")• [Palette:pointWeight ](<./Palette-pointWeight.md> "Palette:pointWeight")• [Palette:popDialog ](<./Palette-popDialog.md> "Palette:popDialog")• [Experimental:Palette:popDialog ](</index.php?title=Experimental:Palette:popDialog&action=edit&redlink=1> "Experimental:Palette:popDialog \(page does not exist\)")• [Palette:probe ](<./Palette-probe.md> "Palette:probe")• [Palette:projectorBlend ](<./Palette-projectorBlend.md> "Palette:projectorBlend")• [Palette:pushPins ](<./Palette-pushPins.md> "Palette:pushPins")• [Palette:puzzle ](<./Palette-puzzle.md> "Palette:puzzle")• [Palette:quadReproject ](<./Palette-quadReproject.md> "Palette:quadReproject")• [Palette:radialBlur ](<./Palette-radialBlur.md> "Palette:radialBlur")• [Palette:recorder ](<./Palette-recorder.md> "Palette:recorder")• [Experimental:Palette:recorder ](</index.php?title=Experimental:Palette:recorder&action=edit&redlink=1> "Experimental:Palette:recorder \(page does not exist\)")• [Palette:remotePanel ](<./Palette-remotePanel.md> "Palette:remotePanel")• [Palette:rgbaBlur ](<./Palette-rgbaBlur.md> "Palette:rgbaBlur")• [Palette:rgbaDelay ](<./Palette-rgbaDelay.md> "Palette:rgbaDelay")• [Palette:rgbContrast ](<./Palette-rgbContrast.md> "Palette:rgbContrast")• [Palette:sceneChanger ](<./Palette-sceneChanger.md> "Palette:sceneChanger")• [Palette:search ](<./Palette-search.md> "Palette:search")• [Palette:searchReplace ](<./Palette-searchReplace.md> "Palette:searchReplace")• [Palette:sharpen ](<./Palette-sharpen.md> "Palette:sharpen")• [Palette:sickEngine ](<./Palette-sickEngine.md> "Palette:sickEngine")• [Palette:signalingClient ](<./Palette-signalingClient.md> "Palette:signalingClient")• [Palette:signalingServer ](<./Palette-signalingServer.md> "Palette:signalingServer")• [Palette:softenAlpha ](<./Palette-softenAlpha.md> "Palette:softenAlpha")• [Palette:solarize ](<./Palette-solarize.md> "Palette:solarize")• [Palette:sopRender ](<./Palette-sopRender.md> "Palette:sopRender")• [Palette:splitter ](<./Palette-splitter.md> "Palette:splitter")• [Palette:stitcher ](<./Palette-stitcher.md> "Palette:stitcher")• [Palette:stoner ](<./Palette-stoner.md> "Palette:stoner")• [Palette:superFormula ](<./Palette-superFormula.md> "Palette:superFormula")• [Palette:SVG ](<./Palette-SVG.md> "Palette:SVG")• [Palette:sweetSpot ](<./Palette-sweetSpot.md> "Palette:sweetSpot")• [Palette:sweetSpotPreviz ](<./Palette-sweetSpotPreviz.md> "Palette:sweetSpotPreviz")• [Palette:synchroCache ](<./Palette-synchroCache.md> "Palette:synchroCache")• [Palette:synchroClient ](<./Palette-synchroClient.md> "Palette:synchroClient")• [Palette:synchroFrameIn ](<./Palette-synchroFrameIn.md> "Palette:synchroFrameIn")• [Palette:synchroFrameOut ](<./Palette-synchroFrameOut.md> "Palette:synchroFrameOut")• [Palette:synchroNDIIn ](<./Palette-synchroNDIIn.md> "Palette:synchroNDIIn")• [Palette:synchroSDIIn ](<./Palette-synchroSDIIn.md> "Palette:synchroSDIIn")• [Palette:synchroVideoOut ](<./Palette-synchroVideoOut.md> "Palette:synchroVideoOut")• [Palette:tdBitwigPackage ](<./Palette-tdBitwigPackage.md> "Palette:tdBitwigPackage")• [Experimental:Palette:tdPyEnvManager ](</index.php?title=Experimental:Palette:tdPyEnvManager&action=edit&redlink=1> "Experimental:Palette:tdPyEnvManager \(page does not exist\)")• [Palette:TDVR ](<./Palette-TDVR.md> "Palette:TDVR")• [Palette:testGrid ](<./Palette-testGrid.md> "Palette:testGrid")• [Experimental:Palette:threadManagerClient ](</index.php?title=Experimental:Palette:threadManagerClient&action=edit&redlink=1> "Experimental:Palette:threadManagerClient \(page does not exist\)")• [Experimental:Palette:threadsMonitor ](</index.php?title=Experimental:Palette:threadsMonitor&action=edit&redlink=1> "Experimental:Palette:threadsMonitor \(page does not exist\)")• [Palette:transitMap ](<./Palette-transitMap.md> "Palette:transitMap")• [Palette:twirl ](<./Palette-twirl.md> "Palette:twirl")• [Palette:vectorScope ](<./Palette-vectorScope.md> "Palette:vectorScope")• [Palette:virtualFile ](<./Palette-virtualFile.md> "Palette:virtualFile")• [Palette:waveformMonitor ](<./Palette-waveformMonitor.md> "Palette:waveformMonitor")• [Palette:webBrowser ](<./Palette-webBrowser.md> "Palette:webBrowser")• [Palette:webRTC ](<./Palette-webRTC.md> "Palette:webRTC")• [Palette:webRTCPanel ](<./Palette-webRTCPanel.md> "Palette:webRTCPanel")• [Palette:webRTCPanelRcv ](<./Palette-webRTCPanelRcv.md> "Palette:webRTCPanelRcv")• [Palette:xyScope ](<./Palette-xyScope.md> "Palette:xyScope")• [Experimental:Thread Manager ](</index.php?title=Experimental:Thread_Manager&action=edit&redlink=1> "Experimental:Thread Manager \(page does not exist\)")
