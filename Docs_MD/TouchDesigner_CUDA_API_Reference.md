# TouchDesigner CUDA API Reference

## Overview

The API TouchDesigner uses to interface with a .dll you write is a call and answer mechanism. That is, TouchDesigner will call certain functions in your .dll and you should fill in these functions with code necessary to give TouchDesigner back the information it needs. A lot of information and comments will be in the TCUDA_Types.h file instead of this article to make sure the information is always up to date with changes in the API. 

## Enumerated Types

The API defines many enumerated types to make it easier to know what are the valid values for a entry in a structure. For example if a structure has a member of type`TCUDA_DataFormat`, then from TCUDA_Types.h we can see that valid values for this are TCUDA_DATA_FORMAT_UNSIGNED_BYTE and TCUDA_DATA_FORMAT_FLOAT.   
The different enumerated types won't be discussed here, you should look in TCUDA_Types.h for information on them. 

## Structures

The API uses structures as a way to send information from, and get information back from the .dll. 

The different structures won't be discussed here, you should look in TCUDA_Types.h for information on them. 

### Rules for filling in the structures

You will notice structures are declared like this (true structure is likely different): 
[code] 
     typedef struct
     {
       int reserved[9];
       union
       {
           struct
           {
               int         reserved[9];
           } param;
           struct
           {
               int         reserved[9];
           } chop;
           struct
           {
               TCUDA_DataFormat    dataFormat;
               int                 reserved[9];
           } top;
           struct
           {
               bool        interestedInTransforms;
               bool        interestedInParameters;
               union {
                   struct {
                       int projWidth;
                       int projHeight;
                   } cam;
               };
               int         reserved[6];
           } obj;
       } ;
     } TCUDA_ParamRequestResult;
    
[/code]

The first thing to notice that there are a lot of reserved* members declared. These are there to take up space so more features can be added to these structures later without breaking old CUDA .dlls. You should never write to these reserved* members. Second is that the structure has a union. Depending on what type of parameter you are writing to, you should only write to one piece of this union. If you don't know what a union is in C++ refer to [this page](<http://en.wikipedia.org/wiki/Union_type>)

For example if you are replying to a request for a camera object, and the structure was declared as 
[code] 
     TCUDA_ParamRequestResult *result;
    
[/code]

You'd write to various members of this structure like this 
[code] 
     result->obj.interestedInParameters = true
     result->obj.cam.projWidth = 512;
     result->obj.cam.projHeight = 512;
    
[/code]

It's important you don't write to structures that don't match the data type this parameter is. So you wouldn't write to the result->chop structure for an object. Or similarly if the subType of the Object wasn't a camera, you wouldn't write to result->obj.cam. 

## Functions

Each function gives and/or asks for specific information from the .dll. Some functions must be defined for the .dll to work, some don't. It's important that your function declarations match what the API expects exactly, or unexpected things will happen (like crashes). Parameters that are declared as`const`are information given to you to help you decide what to do, you must not change the data in these structures. A parameters that isn't declared as`const`is where you would fill in information to tell TouchDesigner what it wants to know. 

### Required Functions
[code] 
     int tCudaGetAPIVersion()
    
[/code]

This function must always return TCUDA_API_VERSION. This lets TouchDesigner know what version of the API the .dll was written against, allowing for backwards compatibility. 

**Parameters** : None 

**Return Value** :It must return TCUDA_API_VERSION, which is defined in TCUDA_Types.h. 
[code] 
     bool tCudaGetParamInfo(const TCUDA_NodeInfo *info, const TCUDA_ParamRequest *request, TCUDA_ParamRequestResult *reqResult)
    
[/code]

This function is called once for each potential parameter. It gives information about the parameter in the`request`, and any information you want to give back is set in the`reqResult`parameter. Returning from this true tells TouchDesigner that you are interested in this parameter, returning false tells TouchDesigner that you are not. 

**Parameters** :`info`\- This is a pointer to a TCUDA_NodeInfo structure that gives information about the node that is currently cooking.`request`\- This is a pointer to a TCUDA_ParamRequest structure that gives information about this particular parameter.`reqResult`\- This structure will contains options that lets you dictate how this parameter will be used. 

**Return Value** : return true if the parameter is going to be used, return false if it isn't. 
[code] 
     bool tCudaExecuteKernel(const TCUDA_NodeInfo *info, const int nparams, const TCUDA_ParamInfo **params, const TCUDA_ParamInfo *output)
    
[/code]

When TouchDesigner calls this function it's asking you to execute your CUDA kernel(s) using the given parameters, and witting the results to the data pointer given by the`output`structure. 

**Parameters** :`info`\- This is a pointer to a TCUDA_NodeInfo structure that gives information about the node that is currently cooking.`nparams`\- This is the number of entries in the`params>`array.`params`\- This is an array of pointers to the parameters that can be used as inputs to the CUDA kernel. The parameters listed in this array depend on what you return from tCudaGetParamInfo.`output`\- This is a pointer to the structure that contains information about where the kernel should write it's output to. The`data`member of this structure will be already allocated CUDA device memory that is big enough to store your output depending on what your output settings are (data format, resolution, number of channels etc.)  


**Return Value** : true if kernel was executed that the OP should update it's data from the output, false if nothing was done (and therefore the OP shouldn't bother updating it's data from the output). 

### Optional Functions

You can choose not to define these functions if you wish. For functions that can return information, TouchDesigner will assume some defaults for functions that aren't defined. 
[code] 
     void tCudaNodeAttached (const TCUDA_NodeInfo *info)
    
[/code]

This function is called the first time a node attaches itself to the .dll. 

**Parameters** :`info`\- This is a pointer to a TCUDA_NodeInfo structure that gives information about the node that attaching itself to this .dll.   


**Return Value** : None 
[code] 
      void tCudaNodeDetached(const TCUDA_NodeInfo *info)
    
[/code]

This function is called when a node deattached itself from the .dll. This happens when the node is deleted, or it loads a different .dll. 

**Parameters** :`info`\- This is a pointer to a TCUDA_NodeInfo structure that gives information about the node that attaching itself to this .dll.   


**Return Value** : None 
[code] 
      void tCudaGetGeneralInfo(const TCUDA_NodeInfo *info, TCUDA_GeneralInfo *ginfo)
    
[/code]

This function asks the .dll for some general information that it can choose to fill in.`ginfo`will contain default values that you can choose to change depending on how you want the OP to behave. 

**Parameters** :`info`\- This is a pointer to a TCUDA_NodeInfo structure that gives information about the node that is currently cooking.`ginfo`\- A pointer to a TCUDA_GeneralInfo structure, you can fill in values in this structure with information if you want. 

**Return Value** : None 
[code] 
      bool tCudaGetTOPOutputInfo(const TCUDA_NodeInfo *info, TCUDA_TOPOutputInfo *oinfo)
    
[/code]

**Only called if the OP is a TOP.** This function allows you to specify the TOPs output in code, instead of doing it in the Common page, or relying on an input TOP's settings. 

**Parameters** :`info`\- This is a pointer to a TCUDA_NodeInfo structure that gives information about the node that is currently cooking.`oinfo`\- fill this parameter in with information about the desire output of the TOP, like the resolution and pixel format. 

**Return Value** : Return true if you want TouchDesigner to use these settings, return false if you want it to use the Common page to decide on the output settings. Returning false is the same as not defining this function at all. 
[code] 
     void tCudaGetTOPKernelOutputInfo(const TCUDA_NodeInfo *info, TCUDA_TOPKernelOutputInfo *oinfo)
    
[/code]

**Only called if the OP is a TOP.** This function allows you to specify options about how the kernel data will be outputted, like the channel order or the data format. If this function isn't defined default settings are used (BGRA, 8-bit unsigned byte etc.) 

**Parameters** :`info`\- This is a pointer to a TCUDA_NodeInfo structure that gives information about the node that is currently cooking.`oinfo`\- fill this parameter in with information about the desire output of the kernel, like the channel order and data format. 

**Return Value** : None 

## Other Important Concepts

### Host Memory vs. Device Memory

The CUDA documentation defines what host and device memory are. To sum it up quickly, host memory is memory that the CPU can access. This is memory you can read/write to in any C++ function. All of the structures that are passed to and returned from tCuda* functions are in host memory. Device memory is memory that CUDA can access. You can only read/write device memory inside a CUDA kernel. Attempting to read/write to a device memory pointer anywhere outside a CUDA kernel will result in a crash. Similarly trying to read/write a host memory pointer in a CUDA kernel will results in the kernel failing to run correctly. 

When TouchDesigner gives you pointers to memory they will declared as`void*`. Along with this pointer the structure will also have a`dataLocation`member that tells you if the pointer points to memory in host memory or device memory. Its up to you to cast these pointers to the correct type and use them correctly. For example in`tCudaExecuteKernel`the`output`structure contains a member called`data`. This pointer will always point to a location in device memory where the CUDA kernel should write it's results. You should pass this pointer into the CUDA kernel well you call it. 

When you are given a host memory pointer, you'll first need to cast it to the correct type. For example if the type is TCUDA_DATA_TYPE_FLOAT, you'd cast the data pointer from the first parameter like this 
[code] 
     float *flts = (float*)(params[0]->data);
    
[/code]

Then you can access the values like this 
[code] 
     float addition = flts[0] + flts[1]; // Add the first and second value.
    
[/code]

When passing these values to the CUDA kernel you need to pass them one value at a time. You can't simply pass`flts`since thats pointer, and CUDA will assume its a pointer to device memory. 

### RGBA vs. BGRA

When working in TOPs you will notice things like pixel formats are written like`TCUDA_PIXEL_FORMAT_RGBA8`, but then there is something called channel order, which is usually`TCUDA_CHAN_BGRA`. RGBA8 simply says that there are R, G, B and A channels, but doesn't imply what their order is. The channel order tells what the channel order will be. We only allow work to be done in BGRA (and not RGBA) channel order because that's the channel order that GPUs naively store data, and it results it better performance.
