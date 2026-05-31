# Metaball

Metaballs can be thought of as force fields whose surface is an implicit function defined at any point where the density of the force field equals a certain threshold. This field can currently be specified as an elliptical or super-quadric shape around a point. When two metaballs overlap in space, their field effects are added together. 

See also [Metaball SOP](<./Metaball_SOP.md> "Metaball SOP")

The field is specified by a weight and a kernel function. The kernel function results in a value of 0 at the outside edge of the metaball and a value of 1 at the center. The kernel function is scaled by the weight to shift the location of the surface closer or further away from the center. 

Because the density of the force field can be increased by the proximity of other metaball force fields, metaballs have the unique property that they change their shape to adapt and fuse with surrounding metaballs. This makes them very effective for modeling organic surfaces. 

For example, below we have a metaball. The surface of the metaball exists whenever the density of the metaball's field reaches a certain threshold: 

When two or more metaball force fields are combined, as in the illustration below, the resulting density of the force fields is added, and the surface extends to include that area where the force fields intersect and create density values with a value of one. 

Metaballs are defined by the parameters **Center x/y/z** , **Radius x/y/z** , **Exponent x/y/z** , and a 3×3 rotation matrix which determines the orientation. A metaball is known as a super-quadratic if either exponent is not equal to one. 

You can see a metaball's sphere of influence by turning on **Display Hulls** in a [Geometry Viewer](<./Geometry_Viewer.md> "Geometry Viewer")'s options dialog. 

In the SOP editor, a metaball can be selected only by its hull. 

## Pusher Metaballs

It is possible for metaballs to have negative Weights (_Pusher_ Metaballs). This allows holes to be created by effectively subtracting from the surface. 

## What does an Exponent do?

In the instance of metaballs, the XY and Z exponent determines the inflation towards "squarishness" or contraction towards "starishness" as described below: 
* Value > 1 - Results in metaballs that appear more like a "star".
  * Value < 1 - Results in metaballs that appear more "squarish".
  * Value = 1 - Results in metaballs that appear spherical.


In Touch, metaballs are often used as force fields for particle systems. You can create metaballs with a [Metaball SOP](<./Metaball_SOP.md> "Metaball SOP"), or in the SOP editor. 

## Metaball Model Types
* **Blinn Kernal** \- Always puts a sphere at the blob centre, even if the weight is less than 1.0. The Blinn model is the fastest and most stable of all the models.
* **Wyvill and Elendt Kernals** \- These models are very similar; only the weight distribution function is different.
* **Links Kernal** \- This is the slowest method, but provides a good compromise between the Blinn and Wyvill methods in terms of weight distribution.
