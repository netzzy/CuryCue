# OpenEXR

[OpenEXR](<https://en.wikipedia.org/wiki/OpenEXR>) is a high dynamic range raster file format, released as an open standard along with a set of software tools created by Industrial Light & Magic (ILM), under a free software license similar to the BSD license.   
  
A full technical introduction of the format is available on [openexr.org](<http://openexr.org>). The currently-supported version is OpenEXR 2.3. 

Advantages of the EXR format are its support for up to 32-bit floating-point data (see TOP's Pixel Format parameter on the Common parameter page) and the ability to store an arbitrary number of channels. 

The EXR files can be loaded into TouchDesigner with the [Movie File In TOP](<./Movie_File_In_TOP.md> "Movie File In TOP") which reads the first 4 channels as RGBA and the [Point File In TOP](<./Point_File_In_TOP.md> "Point File In TOP") which reads EXR files with any number of channels and custom channel mapping options. 

EXR images can be saved out from TouchDesigner with (1) the **Save Image...** menu on TOPs, (2) the`.save()`python method on TOPs, and (3) the [Movie File Out TOP](<./Movie_File_Out_TOP.md> "Movie File Out TOP") with Type "Image" or "Image Sequence". 

### Improving Playback for EXR sequences

EXR sequences are heavy on both the SSD read speed, as well as CPU decode time. To achieve smooth playback of high resolution EXR images you will need both a fast SSD (NVMe M.2 ideally) as well as enough CPU cores to decode many EXRs are the same time. Multiple frames are decoded at the same time via the 'Pre-Read Frames' parameter. The default 3 means that at most 3 will be decoded at the same time. EXR frames can take a long time to decode, so you need to ensure you have enough Pre-Read Frames to have playback keep-up, and additionally you need to make sure that the initial set of frames is pre-read before you start playback. This can be checked via the`isFullyPreRead`member in the [Movie File In TOP](<./Movie_File_In_TOP.md> "Movie File In TOP"). 

As an example, as each frame takes 200ms to decode, and you are trying to play the sequence at 60FPS. Since new frames become available 200ms after they start decoding, there needs to be at least 200ms of frames 'pre-read', so by the time the last frame is read, the new one is ready. This means 'Pre-Read Frames' should be at least 6 in this case, and you'll need at 6 CPU cores available to focus on decoding. Having some padding is good though, so likely 7 or 8 is a better choice here.
