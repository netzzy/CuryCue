# Quadrics

See [Quadrics](<http://en.wikipedia.org/wiki/Quadric>) for a complete definition of these surfaces. 

**Types of Quadrics**
* **Ellipse (Circle)**


These are circles whose X and Y radii are specified independently of each other. Ellipses are stored as primitives rather than as polygons, NURBS , or Bézier curves. They contain their own set of parameters: centre xyz, x-radius, y-radius, and a 3×3 rotation matrix which determines which direction the primitive faces. If both radii are equal, the ellipse is known as a circle. 
* **Ellipsoid (Sphere)**


Ellipsoids are the three-dimensional analogue of an ellipse. They are defined by the parameters centre xyz, x-radius, y-radius, z-radius, and a 3×3 rotation matrix which determines the orientation of the ellipsoid. The ellipsoid is known as a sphere if all three radii are equal. 
* **Tube (Cylinder)**


Tubes are primitive types which resemble cylinders, with the exception that the upper and lower diameter can be changed independently of each other. They also have the ability to have "Caps" - coverings over their end surfaces. Tubes are defined by a centre xyz, a top radius, a bottom radius, a height, and a 3×3 rotation matrix which determines the orientation of the tube. Tubes degenerate into cones if one of the radii is zero.
