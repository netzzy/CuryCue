# 3D Parenting

## Summary

There are two methods of creating 3D objects in a Hierarchy, and they can be mixed together. 

### Parent-Child Node Connectors

The Object Component types (Geometry, Camera, Light, Null...) can be placed in a 3D "hierarchy" using the top and bottom connectors of the nodes in a network. The 3D hierarchy affects what you see in the Render TOP and in any of the 3D component type viewers. 

Below`geo1`and`geo2`are both a "child" of`null1`. The resulting transform of`geo1`is the transform of`null1`applied to the transform of`geo1`. For each 3D object, its transform is a 4x4 matrix that expresses its translate, rotate and scale, defined by the parameters on its Xform and Pre-Xform parameter pages. 

When you connect one Component to another via their top and bottom connectors, you create a "parenting" or "hierarchical" relationship. Moving a parent through its Transform page will move its children with it. 

Each Component can have only one parent. 

### Putting a 3D Component in the Network of Another 3D Component

Parenting is also done by putting an Object COMP type inside another Object COMP. This is the same as if you had wired them using the top/bottom connectors. If a COMP is wired to another COMP through its top connector, then that COMP is its transform parent. If it isn't wired to anything through its top connector, the the COMP it is located within is its transform parent. 

If, for example, you wanted to include as part of your scene the view on the world as seen from a particular camera, you could link the output of a Geometry Component to the input of a Camera Component. Defining a parenting relationship in this way means that any transformations you make to the geometry will include the camera as well. 

## Matrix Math

Using the vector on the right convention (column vectors), the transform of a parent is applied to the child's transform like this: 
[code] 
     parentXForm * xform
    
[/code]

See also: [Geometry COMP](<./Geometry_COMP.md> "Geometry COMP"), [Camera COMP](<./Camera_COMP.md> "Camera COMP"), [Light COMP](<./Light_COMP.md> "Light COMP")
