# Back-Face Culling

**Back-Face Culling** is a performance optimization that avoids drawing [polygons](<./Polygon.md> "Polygon") that are determined to be facing away from the camera. A back-facing polygon is defined as a polygon who's vertices have a clockwise winding. What this means is if you are looking at a polygon (a triangle for example) and you look at the position of vertices 0, 1 and 2, if they make a clockwise loop, then you are looking at the back face of the polygon. If they make a counter-clockwise loop than you are looking at the front face of the polygon. 

**NOTE:** If you are looking at your geometry in a [Geometry Viewer](<./Geometry_Viewer.md> "Geometry Viewer"), be sure to use the Vertex Number, and not the Point Number, to figure out which side of your polygons is the front face. 

An easy mistake to make is to assume that the polygon's Normal defines which of it's side is the front face. This is untrue, the normal has no bearing on which side is the front face. For lighting to work correctly though it's important the normal is on the front face of the polygon (the face that has a counter-clockwise vertex winding). 

Back-Face Culling can be turned on in each [MATs](<./MAT.md> "MAT") common page, or more globally in the [Render TOPs](<./Render_TOP.md> "Render TOP").
