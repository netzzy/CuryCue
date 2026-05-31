# Force Field

Force fields can be used to affect the [Particle SOP](<./Particle_SOP.md> "Particle SOP") or [Spring SOP](<./Spring_SOP.md> "Spring SOP"). The force field is defined by one or more [Metaball](<./Metaball.md> "Metaball") primitives that have been fed into the [Force SOP](<./Force_SOP.md> "Force SOP"). The attractor output is then fed into the third input of the Particle or Spring SOP.   
  
See also [Metaball SOP](<./Metaball_SOP.md> "Metaball SOP"). 

A metaball defines a field of effect. The meta-surface is the point in the field where the value of the field is 1. Thus when two metaballs are merged, their fields get added. When metaballs are used for attractors, the fields are also added together. 

**Types of Forces**

When a single metaball is used as an attractor, there are four types of forces which can be added to the force field. These are: 
* **Radial Force** \- A force pulling particles to the center of the force field. If the force is negative, the particles will be repelled from the center.
  * **Axial Force** \- A force which pulls particles along the axis specified.
  * **Vortex Force** \- A tangential force which causes the particles to spiral around the axis specified.
  * **Spiral Force** \- A force which pulls particles toward the axis specified. If the force is negative, the particles will be repulsed from the axis.


**Other Notes**

The axis specified is in relation to the space of the metaball. Thus, if the metaball is rotated by using a [Transform SOP](<./Transform_SOP.md> "Transform SOP"), the axis specified will also be rotated. This allows for different metaballs to push particles in different directions. 

When multiple metaballs are merged together as attractors, each metaball acts independently on the particle in question. However, the forces of all metaballs are cumulative, causing the particle to be affected by all the different attractors. 

Outside the hull of a metaball (visible as a guide geometry in the Particle SOP, or by turning on display of hulls in the viewport), the attractor will have no effect. At the center of the metaball, the scale of the forces will be whatever the weight of the metaball is set to. By adjusting the weight and kernel type of each metaball, different force field types can be generated.
