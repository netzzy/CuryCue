# Write a CPlusPlus POP

## Overview

**Make sure you've read through[Write a CPlusPlus Plugin](<./Write_a_CPlusPlus_Plugin.md> "Write a CPlusPlus Plugin") first for general information about writing a plugin for a CPlusPlus POP**. 

The CPlusPlus POP allows the creation of POP geometry either by specifying buffers on the CPU, or via buffers created on the GPU through CUDA (Windows with NVIDIA GPUs only). Buffers of data are used to provide data for point, vertex and primtive attributes. Then an Index Buffer is used to specify how the points are tied together create triangles, quads, line strips, line and points. Finally, there is also some meta-information about the topology that may or may not be requried to be specified to help further refine the information for POP processing. 

A sample plugin that works using CPU memory is located in the installation folder under: Samples/CPlusPlus/SimpleShapesPOP and one using the CUDA workflow is under: Samples/CPlusPlus/CudaPOP 

Unlike the CPlusPlus TOP, there is no TOP_ExecuteMode choice the plugin needs to made. It can freely mix CPU data and CUDA workflows as it sees fit, assuming CUDA is supported on the system. 

## Generating POP data

### Creating Buffers

Buffers of memory are created using the`POP_Context::createBuffer()`function. The returned buffer can be queried to obtain it's true memory address using`getBuffer()`on it. These buffers can be used to specify attributes, index buffers, and other meta-information buffers. Although these buffers are smart-reference counted using OP_SmartRef, they should not be used once given back to TouchDesigner via calls to`setIndexBuffer(), setAttribute()`etc. CUDA buffers must be created before`beginCUDAOperations()`is called. CPU buffers can be created at any time in any thread. 

Data in buffers is assumed to always be tightly packed. 

### Creating Attributes

Once a buffer has been filled with data, it can be given to the`POP_Output`via`POP_Output::setAttribute`. The type, number of components, name etc. of the attribute is given by filling out a`POP_AttributeInfo`class, and providing that along with the buffer to`setAttribute`. The number of attribute of each given attribute class (point, vertices, primitives), will be implicitly known by the size of the smallest buffer of the attribute class provided. 

### Creating the Index Buffer

Each POP only has a single index buffer. An index buffer is an array of`uint32_t`indices that reference the point attribute index that each vertex refers to. For example an index buffer with entries [0, 1, 3, 2, 0, 1], refers to the 4 point attribute indexed at 0-3. This index buffer is specifying 6 vertices total, and the index of the vertex attributes they will use (if any are specified), will be [0, 1, 2, 3, 4, 5]. If this index buffer is specifying 2 triangles, that mean the primitive indices will be [0, 1]. 

POPs support 5 different primitive types: triangles, quads, line strips (connected lines with N vertices), lines (2 vertex lines), and point primitives (such as point clouds, or particles). Primitives of each type must be grouped together in the index buffer, and appear in the same order listed above (which is also the order the information is listed in the`POP_TopologyInfo`. This is required so rendering the primitives can be done quickly, by doing each primitive type once in large batches. 

Note that although the primitives need to appear in this order in the Index Buffer, the points attibutes do not need to be ordered like this. Point attributes can be randomly distributed within the buffer. 

#### Line Strips

Other primitive types are quite simple, since the number of vertices in each primitive is known (3 for triangles, 4 for quads, 1 for point primitives). It is known when one primitive ends and the next starts based on the number of vertices encoutered. Line Strips however are more complex, since they can be of arbitrary length. To denote when a line strip ends an index of 0xFFFFFFFF should be written into the index buffer. This is called the primitive restart index. The first vertex of the next line strip can then follow that one. Be sure to allocate enough vertices to include these primitive restart indices, depending on how many line strips you plan to output. 

### Info Buffers

There are a few different info buffers that can be specified. Some are required, some are optional depending on the primitive types used, or if the data is provided in CPU memory or CUDA memory. These are specified by creating and setting buffers in a`POP_InfoBuffers`class. 

#### Point Info

Given by a buffer formatted as a`POP_PointInfo`class. This specifies the number of points that are actually present. All of the point attribute buffers must be at least large enough to hold this number of points. This buffer can be given either on the CPU or with CUDA memory. If it's specified using CUDA memory, then the Max Info buffer also needs to be provided. 

#### Topology Info

Given by a buffer formatted as a`POP_TopologyInfo`class. This specifies the number of primitives of each type, and the offset within the index buffer where the primitives of that type start. Line strips include extra information here than the other primitive types, since we can't infer the number of line strips in the index buffer purely by knowing the number of line strip vertices. This can be specified on either the CPU or in CUDA memory. If it's specified using CUDA memory, then the Max Info buffer also needs to be provided. 

#### Max Info

If Point or Topology Info is provided via CUDA, then the CPU does not actually know how many primitives and points there may be in the buffers. The CPU needs to know this information for memory allocations in downstream POPs, as well as for rendering the geometry. The maximum number of possible primitives of each type must be specified here. This buffer is always on the CPU, and does not need to be allocated using createBuffer(). The`maxInfo`member be be written to in-place in the`POP_InfoBuffers`class. 

#### Line Strips Info

When line strips are processed by other POPs, extra meta-information is needed to quickly find the start/end of each line strip. This buffer must be at least`2 * sizeof(uint32_t) * lineStripsCount`in size. It can be allocated on the CPU or as CUDA memory. For each line strip, it contains a pair of integers that denote { lineStripStartIndex, lineStripNumVertices }. The lineStripStartIndex is a 0-based index that starts where the line strips first show up in the index buffer (it doesn't matter how many triangles/quads appear earlier in the index buffer, 0 is the first line strip index. For example a 5 vertex line strip followed by a 10 vertex line strip would have the entries: [0, 5, 5, 10], since the first line strip start at index is 0 and it has 5 vertices, and then the second one starts at 5 and has 10 vertices. 

This must be provided if your topology includes line strips. 

#### Line Strips Prim Indices

This is a second buffer required to aid in the workflows with line strips. This buffer should be`sizeof(uint32_t) * lineStripsNumVertices`in size. It can be allocated on the CPU or as CUDA memory. Each entry should be the line strip primitive index that index buffer entry matches up with Restart index entries should be incldued as well. E.g A 3 point line strip followed by a 4 point line strip would be [0, 0, 0, 0, 1, 1, 1, 1, 1]. 

This must be provided if your topology includes line strips. 

#### Grid Info

Grid info is extra meta-information to describe how a field of points related to each other. Some POPs use this information in their operations. The buffer for this should be allocated using`POP_GridInfo::getRequiredSize(uint32_t numDims)`to determine the required buffer size. The buffer should always be allocated on the CPU. This class uses a workflow calls 'flexible arrays', that allows the last entry in a class to be an array, and despite it being only defined as [1] in size, you can write beyond that if you've allocated enough space to hold the extra entries. 

## Reading Buffers from a POP Input

A POP connected as an input to your CPlusPlus node can have all of it's individual attribute, index and meta-information buffers read. You can request these buffers on the CPU, as CUDA memory, or state you accept them either on the CPUOrCUDA, which allows the memory to remain where it is (CPU or GPU memory). Attributes and index buffers will always be on the GPU, but the meta-information buffers could be in either location. See the example code in the SimpleShapesPOP, and the documentation in the headers for more details about the functions available for this. 

Currently the CUDA buffers returned from POPs are copies of the data, so you are free to modify them as you wish, and they can be passed as an output buffer back to the POP at the end of the operation. CUDA buffers must be obtained before`beginCUDAOperations()`is called. 

## CUDA

Any operation that reads or writes CUDA memory that is known to TouchDesigner should occur between calls to`POP_Context::beginCUDAOperations()`and`POP_Context::endCUDAOperations()`. A`cudaStream_t`should be used for all operations and provided to the create*/get*/set* calls so GPU synchronization can be achieved.
