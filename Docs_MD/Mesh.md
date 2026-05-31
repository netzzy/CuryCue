# Mesh

Meshes are a collection of edges and vertices that can be represented as having a number of rows and columns based on a UV co-ordinate system. They can be modified into various shapes such as tubes and spheres by changing the point coordinates and/or closing the mesh in U or V, while maintaining their row/column-like topology.   
  
For example, below right is a mesh modified into a sphere by wrapping the mesh in U. Both primitives have the same m x n point topology, only the point coordinates are different. What looks like individual polygons in the above figure are actually intrinsic parts of the primitive. 

A figure that doesn't have an m × n topology cannot be a primitive mesh. The mesh below-left is not a primitive mesh, it does not have an m x n topology. The mesh below-right is a 5x4 primitive mesh.
