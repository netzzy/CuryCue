# Particle POP

## 

Summary

The Particle POP is used for creating and controlling motion of "particles" for particle system simulations. A particle is simply a POP point with special attributes that are created by the Particle POP or added/modified manually by the user in a feedback-type loop, making it easy for customization. POPs are able to handle millions+ of points as they fully run on the GPU. 

Particles are created with an initial position (`P`) and a velocity (`PartVel`) as well as mass (`PartMass`) that derive from (1) the input POP's points, (2) Particle POP's parameters and (3) attributes feeding back (see below). Particles can be emitted based on a constant emission rate or can be emitted based on an input attribute. When emitting based on an input attribute, the Particle POP checks the emitting attribute for each input point and emits that many particles at that position every frame (the emission value is converted to an integer). The Map page serves to configure initial values for various particle properties, including life span (`PartLifeSpan`), drag (`PartDrag`), velocity (`PartVel`), and mass (`PartMass`). It also provides options for setting life span variance and applying velocity damping. 

The particle system is open and highly customizable. It is based on a feedback loop where the output is sent to standard POP nodes and the [Force POP](<./Force_POP.md> "Force POP") nodes that add forces, constrain points, change states to dying/etc, leading to a Null POP at the end of the chain. That Null POP is used by the Particle POP to retrieve the system's state for the next frame (specified by the Feedback parameter). The Particle POP looks for the attributes`PartForce`and`PartVel`to compute the positions for the current frame. 

The Particle POP is based on the features and behavior of the [Feedback POP](<./Feedback_POP.md> "Feedback POP"). To Initialize, Start, end, pause, speed, pre-roll the particle system, it uses the TouchDesigner "Initialize / Start" standard based on the [Timer CHOP](<./Timer_CHOP.md> "Timer CHOP"). It shares several of the same parameters, and if you attach an [Info CHOP](<./Info_CHOP.md> "Info CHOP") to the Particle POP, you will see the same state channels and timer channels as the Timer CHOP. 

You can Pre-Roll the simulation some number of seconds when you Initialize, so that when you press Start, the simulation will be already underway and not be adding its first particles. 

topic: attributes created / determined when the particle is created. Attributes created / modified every loop cycle. 

See examples in POP`Examples/`and`Overview.toe`See [Learning about POPs](</index.php?title=Experimental:POP&action=edit&redlink=1> "Experimental:POP \(page does not exist\)")

See also [Feedback POP](<./Feedback_POP.md> "Feedback POP")

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[particlePOP_Class](<./ParticlePOP_Class.md> "ParticlePOP Class")

### Attributes

Particles have various attributes that regular geometry do not have. These attributes must be carried with each point in order to carry out the simulation. These attributes are listed below 

Particle Attributes Attribute Name | Type | Description   
---|---|---  
PartId | uint | A unique id for the particle   
P | vec3 | The particle’s position   
PartVel | vec3 | The particle’s velocity in Units per second   
PartAge | float | The particle’s age (in seconds)   
PartLifeSpan | float | The particle’s lifespan (in seconds)   
PartForce | vec3 | The cumulative forces applied to the particle   
PartMass | float | Particle’s mass   
PartDrag | float | The drag factor applied to the particle causing it to decelerate.   
PartDeath | uint | Indicates if a particle should be removed from the simulation (optional attribute)   
  
During simulation, the position is updated based on the applied forces (F), the mass (m), the velocity (V), the position (P) and the delta time (dt). 

Vt+1=Vt+Fm⋅dt{\displaystyle V_{t+1}=V_{t}+{\frac {F}{m}}\cdot dt}![{\\displaystyle V_{t+1}=V_{t}+{\\frac {F}{m}}\\cdot dt}](https://wikimedia.org/api/rest_v1/media/math/render/svg/1dc971fb4366b9b7583c11ba3b9c69468a32b9dc)

Pt+1=Pt+Vt+1⋅dt{\displaystyle P_{t+1}=P_{t}+V_{t+1}\cdot dt}![{\\displaystyle P_{t+1}=P_{t}+V_{t+1}\\cdot dt}](https://wikimedia.org/api/rest_v1/media/math/render/svg/4a077629a18c7c1c19287ef8d769261214eb6012)

The`PartDrag`attribute (D) is used to compute a force (FD{\displaystyle F_{D}}![{\\displaystyle F_{D}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/ac0e98e9397b14b2f9399967a0c2154fa2c14d69)) acting on the particles in the direction opposite to their motion (V). 

FD=D⋅V2{\displaystyle F_{D}=D\cdot V^{2}}![{\\displaystyle F_{D}=D\\cdot V^{2}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/bd66380e5a0e3398d48068800b38a16eb671012d)

The Velocity Damping parameter simply attenuates the velocity (V) over time using a damping factor (VD{\displaystyle V_{D}}![{\\displaystyle V_{D}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/499c0305c10b57061914df97a42583a302f79994)). 

Vt+1=Vt+1⋅(1−VD)⇒VD∈[0,1]{\displaystyle V_{t+1}=V_{t+1}\cdot (1-V_{D})\Rightarrow V_{D}\in [0,1]}![{\\displaystyle V_{t+1}=V_{t+1}\\cdot \(1-V_{D}\)\\Rightarrow V_{D}\\in \[0,1\]}](https://wikimedia.org/api/rest_v1/media/math/render/svg/43c1f39b66f1b2e8c7ac1010f76b7363f40d1b6b)

Particles can carry additional attributes. These attributes can be copied from the input POP are created with an initial value. 

### Extending the Particle Simulation

By default, the particle simulation is very basic. The particles positions are updated based on the`PartVel`velocity attribute and`PartForce`force attribute. 

Particles that reach their lifespan are removed from the simulation. 

To inject forces in the simulation and affect the particles velocities, for example, the particle system has to be extended. 

A POP node downstream in the network, typically a [Null POP](<./Null_POP.md> "Null POP") has to be referenced in the Target Particles Update POP parameter. This reference will cause a feedback loop and re-injects the particles next frame with updated attributes in the Particle POP simulation. With this mechanism, it’s possible to extend the simulation to control particles forces, spatial limits, collisions, etc. 

This extending mechanism has some limitations. The number of particles reinjected in the Particle POP has to be the same. Points can’t be added or removed downstream and reinjected back. **The Particle POP is responsible for creating and removing particles**, but it’s possible to control birth with input emission attributes and death with the optional`PartDeath`attribute. Another limitation is that the reinjected points need to carry the particles' reserved attributes. 

## 

Parameters - Particles Page

Target Particles Update POP`targetpop`\- A reference to a POP node downstream in the network. This reference will cause a feedback loop and re-injects the particles next frame 

Create Point Primitives`createpointprim`\- Enable creating point primitives 

Point Id Reuse`pointidreuse`\- ⊞ \- Point Id recycling mode. 
* Reuse Point Ids in Loop`loop`-
* Reuse First Available Point Id`unused`-
* Don't Reuse Point Ids`none`-


Maximum Particles`maxparticles`\- Sets the maximum number of particles. 

Emission from`emissionmode`\- ⊞ \- Determines how particles are emitted 
* Birth Rate`rate`-
* Birth Attribute`attr`\- Name of sequential block to create new attributes.


Birth Rate`birthrate`\- ⊞ \- Number of particles born each unit of time 
* Birth Rate`birthrate`-
* Birth Rate Unit`birthrateunit`\- Unit for birth rate.


Input Birth Attribute`birthattr`\- Input attribute to specify birth rate. 

Randomize Input Points`rndinputpts`\- Enable source points shuffling. 

Life Expect`life`\- ⊞ \- Life Expectancy average time. 
* Life Expect`life`-
* Life Expect Unit`lifeunit`\- Unit for the life expectancy of the particles.


Life Variance (Fraction)`lifevariance`\- Life Expectancy variation as fractoin of life expectancy. 

Random Seed`randomseed`\- Life variance and source position random seed. 

Initial Velocity`initvelocity`\- ⊞ \- Determines the particle's initial velocity in Units per second. 
* Initial Velocity`initvelocityx`-
* Initial Velocity`initvelocityy`-
* Initial Velocity`initvelocityz`-


Initial Mass`initmass`\- Determines the particle's mass. 

Initial Drag`initdrag`\- Determines the drag factor applied to the particle causing it to decelerate. 

Velocity Damping`damping`\- Sets a multiplicative coefficient applied each frame to the particle's velocity to reduce its speed over time. It scales velocity down each frame exponentially. 

Initialize`initializepulse`\- Initializes the POP from its input and parameters, it indicates it’s ready by turning on the ready channel in an attached Info CHOP, awaiting a Start pulse. 

Start`startpulse`\- Start the particle simulation. 

Play`play`\- ⊞ \- Pause or play the feedback loop. 
* Play`play`-
* Step Pulse`steppulse`\- Help Not Available.


Speed`speed`\- Simulation speed. 

Pre-Roll`preroll`\- ⊞ \- Run the loop for this time before it is ready during initialization.. 
* Pre-Roll`preroll`-
* Pre-Roll Unit`prerollunit`\- Warm-up stage time units.


Go to Done`donepulse`\- Will immediately go to the done state. 

## 

Parameters - Attributes Page

In Attributes`attrs`\- ⊞ \- Input attributes to copy to new particles. 
* *`*`-


Rename to`renameto`\- Change the input attributes to a new name. 

Use Death Attribute`usedeathattr`\- Enable using the Death Attribute to force-kill particles. 

New Attribute`attr`\- Name of sequential block to create new attributes. 

New Attribute Name`attr0name`\- ⊞ \- Choose to create a predefined attribute or a custom attribute. 
* New Attribute Name`attr0name`-
* Custom Name`attr0customname`\- The name of the new cutom attribute.


Attribute Type`attr0type`\- ⊞ \- Determines the type. 
* Attribute Type`attr0type`-
* Components`attr0numcomps`\- The number of components in the new custom attribute.


Default Value`attr0value`\- ⊞ \- Default values of the attribute components. 
* Default Value`attr0value0`\- Attribute value(s).
* Default Value`attr0value1`\- Attribute value(s).
* Default Value`attr0value2`\- Attribute value(s).
* Default Value`attr0value3`\- Attribute value(s).

## 

Parameters - Map Page

Mapping`map`\- Start of Sequential Parameter Blocks for attribute-to-parameter mapping. 

OP`map0op`\- Source OP for parameter mapping. The default of _in0 means the input POP. 

Element`map0element`\- The attribute (or component of an attribute) that will be mapped to a parameter per-point. 

Parameter`map0parm`\- ⊞ \- Parameter on the current POP that will be mapped from the Element (the attribute). 
* life (Life Expect)`life`-
* lifevariance (Life Variance (Fraction))`lifevariance`-
* damping (Velocity Damping)`damping`-
* initvelocity (Initial Velocity)`initvelocity`-
* initvelocityx`initvelocityx`-
* initvelocityy`initvelocityy`-
* initvelocityz`initvelocityz`-
* initmass (Initial Mass)`initmass`-
* initdrag (Initial Drag)`initdrag`-


Combine Operation`map0combineop`\- ⊞ \- Combine operation for attribute value with parameter value. 
* Set`set`-
* Multiply`mult`-
* Add`add`-

## 

Parameters - Common Page

Bypass`bypass`\- Pass through the first input to the output unchanged. 

Free Extra GPU Memory`freeextragpumem`\- Free memory that has accumulated when output memory has grown and shrunk. 

Delete Input Attributes`delinputattrs`\- Only output which attributes you specify in this POP \- helps isolate attributes into a separate branch. 

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

Operator Inputs
* Input 0:  -

## 

Info CHOP Channels

Extra Information for the Particle POP can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). __

### 

Common POP Info Channels

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


  
TouchDesigner Build: Latest\nwikieditor2025.30000

POPs   
---  
[Accumulate ](<./Accumulate_POP.md> "Accumulate POP")• [Alembic In ](<./Alembic_In_POP.md> "Alembic In POP")• [Analyze ](<./Analyze_POP.md> "Analyze POP")• [Attribute Combine ](<./Attribute_Combine_POP.md> "Attribute Combine POP")• [Attribute Convert ](<./Attribute_Convert_POP.md> "Attribute Convert POP")• [Attribute ](<./Attribute_POP.md> "Attribute POP")• [Blend ](<./Blend_POP.md> "Blend POP")• [Box ](<./Box_POP.md> "Box POP")• [Cache Blend ](<./Cache_Blend_POP.md> "Cache Blend POP")• [Cache ](<./Cache_POP.md> "Cache POP")• [Cache Select ](<./Cache_Select_POP.md> "Cache Select POP")• [CHOP to ](<./CHOP_to_POP.md> "CHOP to POP")• [Circle ](<./Circle_POP.md> "Circle POP")• [Connectivity ](<./Connectivity_POP.md> "Connectivity POP")• [Convert ](<./Convert_POP.md> "Convert POP")• [Copy ](<./Copy_POP.md> "Copy POP")• [CPlusPlus ](<./CPlusPlus_POP.md> "CPlusPlus POP")• [Curve ](<./Curve_POP.md> "Curve POP")• [DAT to ](<./DAT_to_POP.md> "DAT to POP")• [Delete ](<./Delete_POP.md> "Delete POP")• [Dimension ](<./Dimension_POP.md> "Dimension POP")• [DMX Fixture ](<./DMX_Fixture_POP.md> "DMX Fixture POP")• [DMX Out ](<./DMX_Out_POP.md> "DMX Out POP")• [Extrude ](<./Extrude_POP.md> "Extrude POP")• [Facet ](<./Facet_POP.md> "Facet POP")• [Feedback ](<./Feedback_POP.md> "Feedback POP")• [Field ](<./Field_POP.md> "Field POP")• [File In ](<./File_In_POP.md> "File In POP")• [File Out ](<./File_Out_POP.md> "File Out POP")• [Force Radial ](<./Force_Radial_POP.md> "Force Radial POP")• [GLSL Advanced ](<./GLSL_Advanced_POP.md> "GLSL Advanced POP")• [GLSL Copy ](<./GLSL_Copy_POP.md> "GLSL Copy POP")• [GLSL Create ](<./GLSL_Create_POP.md> "GLSL Create POP")• [GLSL ](<./GLSL_POP.md> "GLSL POP")• [GLSL Select ](<./GLSL_Select_POP.md> "GLSL Select POP")• [Grid ](<./Grid_POP.md> "Grid POP")• [Group ](<./Group_POP.md> "Group POP")• [Histogram ](<./Histogram_POP.md> "Histogram POP")• [Import Select ](<./Import_Select_POP.md> "Import Select POP")• [In ](<./In_POP.md> "In POP")• [Limit ](<./Limit_POP.md> "Limit POP")• [Line Break ](<./Line_Break_POP.md> "Line Break POP")• [Line Divide ](<./Line_Divide_POP.md> "Line Divide POP")• [Line Metrics ](<./Line_Metrics_POP.md> "Line Metrics POP")• [Line ](<./Line_POP.md> "Line POP")• [Line Resample ](<./Line_Resample_POP.md> "Line Resample POP")• [Line Smooth ](<./Line_Smooth_POP.md> "Line Smooth POP")• [Line Thick ](<./Line_Thick_POP.md> "Line Thick POP")• [Lookup Attribute ](<./Lookup_Attribute_POP.md> "Lookup Attribute POP")• [Lookup Channel ](<./Lookup_Channel_POP.md> "Lookup Channel POP")• [Lookup Texture ](<./Lookup_Texture_POP.md> "Lookup Texture POP")• [Math Combine ](<./Math_Combine_POP.md> "Math Combine POP")• [Math Mix ](<./Math_Mix_POP.md> "Math Mix POP")• [Math ](<./Math_POP.md> "Math POP")• [Merge ](<./Merge_POP.md> "Merge POP")• [Neighbor ](<./Neighbor_POP.md> "Neighbor POP")• [Noise ](<./Noise_POP.md> "Noise POP")• [Normal ](<./Normal_POP.md> "Normal POP")• [Normalize ](<./Normalize_POP.md> "Normalize POP")• [Null ](<./Null_POP.md> "Null POP")• [OAK Select ](<./OAK_Select_POP.md> "OAK Select POP")• [Out ](<./Out_POP.md> "Out POP")• Particle • [Pattern ](<./Pattern_POP.md> "Pattern POP")• [Phaser ](<./Phaser_POP.md> "Phaser POP")• [Plane ](<./Plane_POP.md> "Plane POP")• [Point File In ](<./Point_File_In_POP.md> "Point File In POP")• [Point Generator ](<./Point_Generator_POP.md> "Point Generator POP")• [Point ](<./Point_POP.md> "Point POP")• [Points, Vertices and Primitives in s ](<./Points,_Vertices_and_Primitives_in_POPs.md> "Points, Vertices and Primitives in POPs")• [Polygonize ](<./Polygonize_POP.md> "Polygonize POP")• [POP ](<./POP.md> "POP")• [Primitive ](<./Primitive_POP.md> "Primitive POP")• [Projection ](<./Projection_POP.md> "Projection POP")• [Proximity ](<./Proximity_POP.md> "Proximity POP")• [Quantize ](<./Quantize_POP.md> "Quantize POP")• [Random ](<./Random_POP.md> "Random POP")• [Ray ](<./Ray_POP.md> "Ray POP")• [Rectangle ](<./Rectangle_POP.md> "Rectangle POP")• [ReRange ](<./ReRange_POP.md> "ReRange POP")• [Revolve ](<./Revolve_POP.md> "Revolve POP")• [Select ](<./Select_POP.md> "Select POP")• [Skin Deform ](<./Skin_Deform_POP.md> "Skin Deform POP")• [Skin ](<./Skin_POP.md> "Skin POP")• [SOP to ](<./SOP_to_POP.md> "SOP to POP")• [Sort ](<./Sort_POP.md> "Sort POP")• [Sphere ](<./Sphere_POP.md> "Sphere POP")• [Sprinkle ](<./Sprinkle_POP.md> "Sprinkle POP")• [Subdivide ](<./Subdivide_POP.md> "Subdivide POP")• [Switch ](<./Switch_POP.md> "Switch POP")• [Texture Map ](<./Texture_Map_POP.md> "Texture Map POP")• [TOP to ](<./TOP_to_POP.md> "TOP to POP")• [Topology ](<./Topology_POP.md> "Topology POP")• [Torus ](<./Torus_POP.md> "Torus POP")• [Trail ](<./Trail_POP.md> "Trail POP")• [Transform ](<./Transform_POP.md> "Transform POP")• [Trig ](<./Trig_POP.md> "Trig POP")• [Tube ](<./Tube_POP.md> "Tube POP")• [Twist ](<./Twist_POP.md> "Twist POP")• [ZED ](<./ZED_POP.md> "ZED POP")
