# Write a Shared Memory TOP

  
In the TouchDesigner installation directory, under`Samples/SharedMem/TOP`there is the header defined in`TOP_SharedMemHeader.h`that needs to be filled in at the start of the shared memory buffer. The memory buffer should have this header, followed by the image data. 

**NOTE: The 'Shared Mem Type' parameter in the TOP must be set to 'Local' for your app to be able interface with it.**

## Creating a Shared Memory Buffer

Refer to the article [Using Shared Memory in TouchDesigner](<./Using_Shared_Memory_in_TouchDesigner.md> "Using Shared Memory in TouchDesigner") to learn how to create a shared memory buffer. If you are the sender, you need to create a buffer whose size will accommodate both the header, and the image data. Get the size of the header simply with 
[code] 
     sizeof(TOP_SharedMemHeader)
    
[/code]

The size of the image data depends on the number of channels, the resolution and the dataType. In general it's 
[code] 
     width * height * number of channels * number_of_bytes_per_channel
    
[/code]

Where`number_of_bytes_per_channel`is`1`for dataType`GL_UNSIGNED_BYTE`and`4`for`GL_FLOAT`. 

Once you have a pointer to the memory, you can do the next step. 

## Writing/Reading the Header

You can get the header file used to describe the data that is sent through a Shared Mem TOP in`touch/SharedMem/TOP`(Under the directory where TouchDesigner is installed). The file is called`TOP_SharedMemHeader.h`. 

The header is the first thing that appears in the shared memory. So you can cast the pointer you get from`UT_SharedMem`to`TOP_SharedMemHeader`. 
[code] 
     TOP_SharedMemHeader *header = (TOP_SharedMemHeader*)shm->getMemory();
    
[/code]

If you are the sender, fill in all of the fields in this header. Refer to the header for more details one each field you need to fill in. 

**If you are the sender, make sure you do this, otherwise the receiver won't know where the image is.**
[code] 
     header->dataOffset = sizeof(TOP_SharedMemHeader);
    
[/code]

  
Most of the members of the header are self-explanatory, except for`dataFormat`,`dataType`and`pixelFormat`. The valid values for these are listed at the top of`TOP_SharedMemHeader.h`. The values are OpenGL constants but I'll provide their actual values (in hexadecimal) in case you aren't using OpenGL at all in your app.`dataFormat`: This is the format of your image in memory. For example if you don't have an alpha channel and your image data's pixel format is RGB, you specify`GL_RGB`.`dataType`: This is the data type of your image data. If it's stored an unsigned char's use`GL_UNSIGNED_BYTE`(8-bits per channel), if it's stored as floats use`GL_FLOAT`(32-bits per channel).`pixelFormat`: This is the format of the texture you want to be created in the Shared Mem In TOP. The`pixelFormat`doesn't need to match the`dataType`. For example you can create a`GL_RGBA16F_ARB`(16 bit float) texture from 8-bits unsigned char data, or vice versa, if you want. Don't confuse the RGBA here with a`dataFormat`as above, the RGBA doesn't imply that's the channel order, it just implies that's the channels present, they could be ordered BGRA if you want. 

  
If you are the receiver, use the the information from the header however you see fit. 

## Reading/Writing the Image

Get a pointer to where you should read/write the image by simply using the`getImage()`call in the header: 
[code] 
     unsigned char *image = (unsigned char*)header->getImage(); // For 8-bit
    
[/code]

or 
[code] 
     float *image = (float*)header->getImage(); // For floating point data
    
[/code]

Now read/write the image data depending on the format.
