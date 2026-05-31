# Write a CPlusPlus TOP

## Overview

**Make sure you've read through[Write a CPlusPlus Plugin](<./Write_a_CPlusPlus_Plugin.md> "Write a CPlusPlus Plugin") first for general information about writing a plugin for a CPlusPlus TOP**. 

The CPlusPlus TOP allows you to write C++ code to create a TOP that can output multiple textures. Currently you can create your output by filling a CPU memory buffer (`TOP_ExecuteMode::CPUMem`) or by filling a`cudaArray`buffer (`TOP_ExecuteMode::CUDA`). 

Most of the documentation is held in the header files for the C++ API. The samples also contain a lot of comments about the workflow. 

For upgrading your CPlusPlus TOP compiled using headers from TouchDesigner builds before and including 2021.10000 to work in builds 2022.20000 and after, refer to [CPlusPlus TOP Upgrades For 2022.20000 Builds](<./CPlusPlus_TOP_Upgrades_For_2022.md> "CPlusPlus TOP Upgrades For 2022.20000 Builds")

## CUDA

The [CPlusPlus TOP](<./CPlusPlus_TOP.md> "CPlusPlus TOP") can be used with [CUDA](<./CUDA.md> "CUDA"). See the CudaTOP example project included with the TouchDesigner installation for an example. Note that any CUDA operations that occur in your C++ code must occur on the main thread, between calls to`OP_Context::beginCUDAOperations()`and`OP_Context::endCUDAOperations()`. 

## See Also

[Write a CPlusPlus Plugin](<./Write_a_CPlusPlus_Plugin.md> "Write a CPlusPlus Plugin")  
[Write a CPlusPlus CHOP](<./Write_a_CPlusPlus_CHOP.md> "Write a CPlusPlus CHOP")  
[CPlusPlus TOP Upgrades For 2022.20000 Builds](<./CPlusPlus_TOP_Upgrades_For_2022.md> "CPlusPlus TOP Upgrades For 2022.20000 Builds")  
[CPlusPlus TOP](<./CPlusPlus_TOP.md> "CPlusPlus TOP")  
[CPlusPlus CHOP](<./CPlusPlus_CHOP.md> "CPlusPlus CHOP")
