# CPlusPlus TOP Upgrades For 2022.20000 Builds

CPlusPlus TOPs compiled against headers from builds before and including 2021.30000 won't work in builds 2022.20000 and onwards, due to the changeover to Vulkan. This page contains information for the essential changes to be made to compile your code against the newer headers.   
  
## Changes

  *`getOutputFormat()`is gone. You need to specify the output format from within`execute()`via`TOP_CUDAOutputInfo`for CUDA, and`TOP_UploadInfo`for CPU workflow. More flexibility offered this way.
  * Pixel format is set in`OP_TOPInputDownloadOptions::pixelFormat`, replacing`OP_TOPInputDownloadOptions::cpuMemPixelType`* The`TOP_Context`pointer isn't passed through`execute()`anymore. To get access to it, it is still passed in`CreateTOPInstance()`where you can store it in your TOP class during instantiation. This context can be used to create and work with a`TOP_Buffer`, to do CUDA operations, or work with python callbacks.
  * For CPU workflow specifics: 
    *`OP_Inputs::getTOPDataInCPUMemory()`is gone. To download texture from the input TOPs, Use`OP_TOPInput::downloadTexture()`, and specify the download options via`OP_TOPInputDownloadOptions`.
    *`OP_TOPInputDownloadType`is gone, and the option of either delaying downloading the frame, or instantly downloading the frame has to be done manually. Store the downloaded result`OP_TOPDownloadResult`as a member in your TOP class, then when you want to stall the thread to wait for the result, call`getData()`on it.
    *`TOP_OutputFormatSpecs`is gone. Use`TOP_Output`and`TOP_UploadInfo`.`TOP_UploadInfo`stores the format of the texture to be outputted.`TOP_Output`contains the methods for creating buffer via`TOP_Context::createOutputBuffer()`and uploading the texture to the GPU via`TOP_Output::uploadBuffer()`, offering lot more functionality.
* To use the CUDA workflow: 
    * Store a CUDA stream object`cudaStream_t`in the operator class. Instantiate it via`cudaStreamCreate()`, and destroy via`cudaStreamDestroy()`* To access the input data, populate an object of`OP_CUDAAcquireInfo`, then get the input into`OP_CUDAArrayInfo* inputArray`via`OP_TOPInput::getCUDAArray()`. Note that the acquired`inputArray->cudaArray`will be a nullptr until`beginCUDAOperations()`has been called, more on this later.
    * To give the CUDA output back, populate an object of`TOP_CUDAOutputInfo`, then call`TOP_Output::createCUDAArray()`to create`OP_CUDAArrayInfo* outputInfo`that will store the output`cudaArray`. Again,`outputInfo->cudaArray`will remain null until`beginCUDAOperations()`is called.
    * CUDA operations can only begin once`TOP_Context::beginCUDAOperations()`has been called. The relevant input and output`OP_CUDAArrayInfo::cudaArray`objects will get valid addresses after this method has been called. Once you're done with the operations, call`TOP_Context::endCUDAOperations()`.
    * Further, between`beginCUDAOperations()`and`endCUDAOperations()`, your`OP_Inputs`inputs object cannot be accessed, so call the`OP_Inputs`methods beforehand to get the values.


For a better understanding of all of these changes, refer to the examples in`Samples\CPlusPlus\`## See Also

[Write a CPlusPlus TOP](<./Write_a_CPlusPlus_TOP.md> "Write a CPlusPlus TOP")
