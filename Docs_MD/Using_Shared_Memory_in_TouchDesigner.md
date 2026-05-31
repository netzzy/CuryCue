# Using Shared Memory in TouchDesigner

## Overview

Various OPs in TouchDesigner are able to send and receive data via shared memory, which is a fast way to send data between two different processes. This guide will help you make your own app that can send or receive data from TouchDesigner. This guide gives the basics on how to setup and use shared memory. More specific articles for each OP type will tell you how to write/read from this shared memory so that the processes can talk to each other correctly. 

**NOTE:** You need to have TouchDesigner Commercial or Pro to have access to the Shared Memory nodes. 

## Source Files

C++ source code is supplied to make this task much easier. You can get the source files from`Samples/SharedMem`in your TouchDesigner Install directory. 

### UT_SharedMem

This class does everything that needs to be done to manage shared memory. If you are the sender you need to create the shared memory by also specifying the size of the shared memory. This size needs to be big enough to hold all of the data you need to write. The amount of data depends on the type of OP you are working with. Refer to that OPs article for more information. If you are the receiver, you only specify the name of the shared memory. This name matches the name that you give the parameter in the shared memory OP. Create a shared memory to send data like this 
[code] 
     UT_SharedMem *shm = new UT_SharedMem(ShmString(L"mymemoryname"), myRequiredSize); // figure out the size based on the OP
    
[/code]

or for the receiver 
[code] 
     UT_SharedMem *shm = new UT_SharedMem(ShmString(L"mymemoryname"));
    
[/code]

Check the state of the shared memory using 
[code] 
     UT_SharedMemError err = shm->getErrorState();
     if (err != UT_SHM_ERR_NONE)
     { 
        // an error occured 
     }
    
[/code]

  
Before you read or write to the memory, you need to lock it. If it's able to lock the memory then you can get the pointer to the memory and use it. Once you have this pointer, what you do with it depends on the type of OP you are communicating with. Finally, unlock once done read/writing the data. 
[code] 
     if (!shm->lock())
     {
         // error
     }
     else
     {
         void *data = shm->getMemory();
         
         // Use the data here
         
         // Unlock it when done
         shm->unlock();
     }
    
[/code]

### UT_Mutex`UT_Mutex`is a class to lock/unlock the shared memory segment to make sure two processes aren't accessing it at the same time. You don't need to use this class yourself, it'll be used by`UT_SharedMem`though, so make sure to include and compile it in your project. 

## Compile Issues and Considerations

### Unicode

In the 2018.20000 builds and earlier, the UT_SharedMem class is not written with Unicode support. If you get errors involving LPCWSTR types or other Unicode types, it means you are compiling with Unicode support turned on, but using the older source/header files from 2018.20000 and earlier builds. Go to the project properties, 'General' page, and for 'Character Set' select 'Not Set'. If you require Unicode support, use the header files from 2019.10000 series of builds, or later. 

This has been changed in the 2019.10000 series of builds, and the class is written to be unicode compliant. 

## Related Articles

[Write a Shared Memory TOP](<./Write_a_Shared_Memory_TOP.md> "Write a Shared Memory TOP")

[Write a Shared Memory CHOP](<./Write_a_Shared_Memory_CHOP.md> "Write a Shared Memory CHOP")
