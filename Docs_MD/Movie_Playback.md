# Movie Playback

## Overview  
  
This article will describe the stages of data transfer and processing required to playback a movie. It describes more in depth what the [Movie File In TOP](<./Movie_File_In_TOP.md> "Movie File In TOP") does to get a frame on the GPU in a TOP. 

There are three stages: The first stage of playing back a movie is reading the file data from disk, unmodified, into CPU memory. Once the file data is in CPU memory it needs to be decoded into a raster image. The final stage of playback occurs when the frame is uploaded from the pre-read cache of CPU memory to GPU memory where it can be used by all TOPs downstream on the GPU. 

## Reading from Disk

The first stage of playing back a movie is reading the file data from disk. This data needs to be read into CPU memory so it can be decompressed into uncompressed RGBA or YUV image data. 

The [Info CHOP](<./Info_CHOP.md> "Info CHOP")'s`"last_frame_hd_read_time`channel says how long the last frame took to read from the hard drive/SSD. This value is in milliseconds. 

### Bit-rate

The bit-rate of a movie is the amount of data per second that needs to be read from disk to play the file. This number is given in bits-per-second usually. Drive speed is usually given in bytes-per-second though, so be sure you are using the correct units when determining if you have the required read speed to playback your movie. Bytes are usually denoted with a capital 'B', while bits are denoted with a lower case 'b'. There are 8 bits in 1 byte, so a file that has a bit-rate of 80Mbits/sec will consume disk read bandwidth of 10MBytes/s. 

The [Info CHOP](<./Info_CHOP.md> "Info CHOP")'s`"disk_read_mbit_rate`channel says the average disk read rate in mega-bits a second. 

### Buffered/Cached Reading

By default all files read in the operating system are read using what is called Buffered/Cached reading. What this means is that data from the file is first copied to CPU memory owned by the OS, and then copied over to TouchDesigner's CPU memory. The OS is free to keep its copy of the file in its memory for as long as it wants. The OS will only discard that file data if it needs to, for example if that CPU memory is needed for other reasons. The data kept by the OS in it's memory is the compressed file data, not uncompressed RGB/YUV frames. 

If you are playing back files that total 4GB in size, and you have 16GB of CPU RAM. Unless you have applications eat up that other RAM it's entirely possible the files will only be read from disk once and the rest of the time the data in the OS's CPU memory will be read from instead. File data is cached as it gets read so a file won't be entirely cached until you've played through the entire file once. Check your disk usage to know if your playback is reading from the disk or using cached data. 

The memory that is being used to cache the movie file's data is not recorded anywhere. You will not see it show up as CPU memory usage by TouchDesigne, nor as general memory consumed in the system as a whole. This is because the memory is entirely disposable, and the OS can discard the cached data at any time for any reason. 

**Note** \- If you have content that plays back poorly the first run through but fast the second time, this likely means your disk cannot deliver the data at the required rate, and playback is only possible from the cached data. This can be a dangerous state to be in unless you have enough RAM, because you have no control of when/if the OS will drop cached data out of it's RAM. 

Unless you are playing back files that have very high data-rate (uncompressed data, HAP, lossless H264 etc.), this is usually the mode you want to playback in. 

### High-Performance Read (Unbuffered Reading)

The High-Performance Read parameter in the [Movie File In TOP](<./Movie_File_In_TOP.md> "Movie File In TOP") turned off buffered/cached file reading. Data is read directly from the disk into TouchDesigner's CPU memory. This is faster because it avoids a memory copy operation. There is also other algorithmic optimizations done specific to TouchDesigner in this mode that allows for extremely high data-rate playback. When using this mode the disk will be constantly in use during playback and it will show the true rate playback of your content. 

This mode should be used when very high read data-rates are required, such as high resolution Hap, lossless H264/H265. 

## Decoding Frames

Once the file data is in CPU memory it needs to be decoded into an image. This image is usually uncompressed RGB or YUV data. Most forms of YUV will be converted to RGB once the data gets to the GPU, but some will be converted on the CPU. This can be seen with the 'hardware_yuv_to_rgb' channel in the [Info CHOP](<./Info_CHOP.md> "Info CHOP"). 

Some codecs will make use of multiple threads to decode the data. This is controllable by the 'Max Decode CPUs' parameter in the Movie File In TOP. 

Decompressed frames are placed into to the Pre-Read cache of the Movie File In TOP. The size of this cache is controlled by the 'Pre-Read Frames' parameter. The`preload()`method on the Movie File In TOP is a way to fill the 'Pre-Read Frames' with minimal impact on playback of the rest of the file. 

The [Info CHOP](<./Info_CHOP.md> "Info CHOP")'s`last_frame_decode_time`channel say show long the last frame took to decode on the CPU. This value is in milliseconds. 

### Hap decoding

Codecs such as Hap have a very light CPU decompression stage, while codecs like H264 have a very heavy CPU decompression stage. A very high resolution Hap file will still result in a significate CPU decode time though, so using chunked encoding for Hap as well as having cores to decode those chunks may be needed to play back high resolution Hap files. 

Although a portion of Hap is decoded on the GPU, there is still a CPU cost. By default it has a lossless CPU compression that is applied which will take time. If this compression is disabled when encoding the cost will be greatly reduced, but there are still memory copies that will take some time. 

### Nvidia Hardware Decoding

Decoding using Nvidia's hardware decoder is supported. This feature is enable on the Tune page of the Movie File In TOP's parameters. Information about supported codecs for Nvidia GPUs can be found [here](<https://developer.nvidia.com/nvidia-video-codec-sdk>). In this mode the data is uploaded to the GPU before any decoding is done, the frames are decoded into RGBA on the GPU, and remain there to be used by TOPs. If a file is unable to be decoded using the GPU, it will fall back t using the regular CPU decoding. The [Info CHOP](<./Info_CHOP.md> "Info CHOP")'s`hardware_decode`channel will be 1 if hardware decoding is being used and 0 if not. 

### Pre-Read Cache

Once a frame's CPU decode work as completed, it is added to the pre-read cache, ready to be uploaded to the GPU when that frame is requested to be shown. You can see how many frames are pre-read by looking at the [Info CHOP](<./Info_CHOP.md> "Info CHOP")'s`num_pre_read_frames`channel. 

## Uploading to the GPU

The final stage of playback occurs when the Movie File In TOP needs to output a particular frame. The frame is uploaded from the pre-read cache to GPU memory where it can be used by all TOPs downstream on the GPU. If the frame isn't already in the pre-read cache, possibly due to cueing the movie to a new index, a pre-read miss will occur which will force the Movie File In TOP to wait until that frame is read and decompressed.
