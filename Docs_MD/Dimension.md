# Dimension

A POP’s point list may have an implied structure within it. For example, a [Grid POP](<./Grid_POP.md> "Grid POP") or [Plane POP](<./Plane_POP.md> "Plane POP") is a list of points implicitly arranged in columns and rows, thus having two dimensions. This information is passed to downstream POPs. The rows and columns are considered "dimensions". A Grid POP has two dimensions by default, and three dimensions if you increase its number of slices (default 1). When you pass a POP to another POP, you may want to preserve and use what is known about its structure.   
  
**Dimension** is the metadata that describes the structure of the point list, and is passed from POP to POP. 

Points are organized generally as N-dimensions, where each dimension has some number of elements. Dimensions compound: You get three dimensions by copying a circle (a [Circle POP](<./Circle_POP.md> "Circle POP") has a dimension of 1) onto each point of a 2-dimensional grid. 

When converting a [POP to TOP](<./POP_to_TOP.md> "POP to TOP"), you may want to create the corresponding width and height (and depth) of pixels in the TOP. The dimension is used for this. When converting a [TOP to POP](<./TOP_to_POP.md> "TOP to POP"), you will want to preserve its width and height resolutions, again generating the correct dimensions. 

Middle-click on a POP to see its popup info: You will see numbers for Dimension, for example, on a [Torus POP](<./Torus_POP.md> "Torus POP") : 
[code] 
    Dimension 20 40
    
[/code]

indicating a 20 x 40 point arrangement. If you multiply the dimension numbers you will always get the total number of points in the POP. In this example, in memory, the first 20 numbers are the first row, etc. 
[code] 
    Dimension 20 40 12
    
[/code]

indicates a 20 x 40 x 12 point arrangement (12 sets of 40 sets of 20 points) 

Some generator POPs are multi-dimensional (Torus (2 dimensions), Tube (2 dimensions), Grid (2 or 3), in some cases Sphere is 2 dimensions….). 

Some POPs always preserve the dimensions (like [Math POP](<./Math_POP.md> "Math POP") which only changes point values). Some POPs increase the number of dimensions ([Copy POP](<./Copy_POP.md> "Copy POP"), [Trail POP](<./Trail_POP.md> "Trail POP") and sometimes [Merge POP](<./Merge_POP.md> "Merge POP")) 

Some POPs destroy multi-dimensions ([Delete POP](<./Delete_POP.md> "Delete POP")). A Grid POP is no longer 2-dimensions if you, for example, delete one point. It becomes 1-dimension whose size simply is the total number of points. 

All POPs have at least 1 dimension with the number of dimension elements being the number of points, like the Circle POP. 

If a POP has N dimensiona nad any of the dimensions is 0, then the POP will have 0 points. 

NOTE: This replaces the concept of meshes in SOPs. 

### Built-In Attributes for Dimension

You can use the dimensions when working with attributes like in [Math Mix POP](<./Math_Mix_POP.md> "Math Mix POP") or [Lookup Channel POP](<./Lookup_Channel_POP.md> "Lookup Channel POP"), accessible on any attribute parameter menu: at the bottom of the attribute menu press the > submenu.`_NumDim`is the number of dimensions of the input.`_DimSize[0]`would be the number of columns in a grid or torus or tube.`_DimSize[1]`is the number of rows. etc,`_DimI[0]`is the column number of a point,`_Dim[1]`is the row number.`_DimU[0]`is the point’s column represented as a normalized number between 0 and 1.`_DimU[0]`is 1 for the last point in a grid column. These numbers are useful for all the Lookup* CHOPs. 

pro tip:`_DimCy[0]`is similar to`_DimU[0]`but is cyclic: The last column has`_DimU[0] == 1`, but the last column has`DimCy[0] == ( 1 - 1/numcols )`, so with 10 columns, the last column has`DimCy[0] == .9`,. Therefore if you give a Lookup POP an index value of`1`and it’s cyclic, it’s referring to the first point. 

Note: although built-in attributes for dimension are most convenient, you can also **extract the dimensions of any POP into a point attribute using the** [Analyze POP](<./Analyze_POP.md> "Analyze POP"). 

### Python for Dimension

In python,`POP.dimension`is the list of sizes of each dimension, for example`[10, 20, 8]`. It is the map of points arranged in memory.`len(POP.dimension)`is the number of dimensions,`3`in this case. Always the number of points in a POP is the product of all the dimensions. 

NOTE: The term “array” is not used with dimension. An attribute is an array if it is more than one float3 for instance. 

For the [Grid POP](<./Grid_POP.md> "Grid POP"), in python,`POP.dimension[0]`is the number of columns,`POP.dimension[1]`is number of rows,`POP.dimension[2]`is number of slices if there is more than 1 slice. 

And if you copy this 3D grid to points of a circle,`POP.dimension[4]`is the number of circle points you stamped to.`POP.numPoints = POP.dimension[0] * POP.dimension[1] * POP.dimension[2] * POP.dimension[3]`Attributes vs Python  | Attribute | Python   
---|---|---  
number of points |`_NumPoints`|`POP.numPoints()`dimension info object | - |`POP.dimension`number of dimensions |`_NumDim`|`len(POP.dimension)`elements in first dimension |`_DimSize[0]`|`POP.dimension[0]`index of point in first dimension |`_DimI[0]`| \-   
index of point in second dimension |`_DimI[1]`| \-   
normalized index of point in first dimension |`_DimU[0]`| \-   
cyclic normalized index of point in first dimension |`_DimCy[0`] | \-   
attribute value | _attributeName_ |`POP.points(_attributeName_)`
