# CUDAMemoryShape Class

Describes the shape of a CUDA memory segment. 

## Members`width`→`int`: 

> Get/Set the width in pixels of the memory.`height`→`int`: 

> Get/Set the height in pixels of the memory.`numComps`→`int`: 

> Get/Set the number of color components per pixel of the memory.`depth`→`int`: 

> Get/Set the depth in pixels of the memory.`isCube`→`bool`: 

> Get/Set whether this shape describes a cubemap. Depth must equal 6.`is3D`→`bool`: 

> Get/Set whether this shape describes a 3D texture. If this is false and depth > 1, then it's a 2D array.`dataType`→`numpy.dtype`: 

> Get/Set the data type of each color component, as a numpy data type. E.g numpy.uint8, numpy.float32. Note that for uint8 data types, the channel ordering will be BGRA for 4 component textures. It will be RGBA however for other data types.

## Methods

No operator specific methods. 

  
TouchDesigner Build:  Latest\nwikieditor 2025.30000 2022.24140 2021.10000
