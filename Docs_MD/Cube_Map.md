# Cube Map

A Cube Map is a texture that is sampled using 3 texture coordinates. It is composed of 6 2D texture, each mapping to one 'side' of a unit cube (+X, -X, +Y, -Y, +Z, -Z). The 3 texture coordinates are treated as a vector coming from a point in the middle of the cube, and whatever point on one the cube faces the vector hits, thats the texel that sampled. So depending on which direction the vector is pointing one of the cube sides are selected, and from there it decides which texel on the side's 2D texture to return.   
  
You can create a Cube Map using the [Cube Map TOP](<./Cube_Map_TOP.md> "Cube Map TOP"). 

Cube maps are useful for many advanced lighting techniques, as well as reflections in the [Phong MAT](<./Phong_MAT.md> "Phong MAT"). 

This example file shows a Cube Map TOP being used for the Environment Map of a Phong MAT to simulate reflections. [File:Cubemap.tox](</File:Cubemap.tox> "File:Cubemap.tox")

ATI has created free tool for working with CubeMaps: [CubeMapGen](<http://developer.amd.com/gpu/cubemapgen/Pages/default.aspx>).
