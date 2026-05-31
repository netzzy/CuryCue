# Movie File In TOP

## 

Summary

The Movie File In TOP loads movies, still images, or a sequence of still images into TOPs. It will read images in`.jpg`,`.gif`,`.tif`, or`.bmp`format. It will read movies in QuickTime's`.mov`format,`.mp4`,`.mpg`,`.mpeg`,`.avi`,`.wmv`,`.dpx`, [Cineform](<./GoPro_Cineform.md> "GoPro Cineform") and [Hap](<./Hap.md> "Hap") Q formats (including Hap Q with Alpha). 

It also supports the [NotchLC](<./NotchLC.md> "NotchLC") codec, [EXR](<./EXR.md> "EXR") files (`.exr`) and some`.swf`and`.flv`Flash files as well as DXT1/3/5 and RG compressed`.dds`files. Images and movies can also be fetched from the web by using`http://`to specify a URL. 

Access the hardware decoder on Nvidia GPUs with the Hardware Decode parameter on the 'Tune' page. This supports 10 and 12-bit H264/H265s and YUV 444 files on supporting hardware, converted into 16-bit pixel channels. Other codecs that this also decodes include VP8, VP9, JPEG, AV1, VC1. More information [here.](<https://developer.nvidia.com/video-encode-and-decode-gpu-support-matrix-new>)

When reading file formats that support higher bit depths such as 10-bit/16-bit/32-bit, an appropriate pixel format will be automatically used as long as the 'Pixel Format' menu on the Common page is left as 'Use Input'. i.e. a 16-bit file will cause each pixel to have 16-bits per color channel automatically. 

For a complete list, see [File Types](<./File_Types.md> "File Types"). 

Examine the state of a Movie File In TOP by attaching an [Info CHOP](<./Info_CHOP.md> "Info CHOP") to it (see below on Info CHOP). This will show info like movie length, resolution, the number of images per second (the`sample_rate`channel), and whether there is audio in the file. It also shows dynamic information like movie open status, current frame, readahead frames and queue size, dropped frame count, CPU decode time and GPU upload time. 

Note that a movie's "images per second" (sample_rate) may be different than the timeline's frames per second. When referring to the movie's "index", it's in reference to the sequence of images in the movie file, not related to the global project frame rate. 

See also the page on Movie File In TOP optimizations [Movie Playback](<./Movie_Playback.md> "Movie Playback"), plus [Hap](<./Hap.md> "Hap"), [Movie File Out TOP](<./Movie_File_Out_TOP.md> "Movie File Out TOP"), [Cineform](<./GoPro_Cineform.md> "GoPro Cineform") and [Video Stream In TOP](<./Video_Stream_In_TOP.md> "Video Stream In TOP"). 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[moviefileinTOP_Class](<./MoviefileinTOP_Class.md> "MoviefileinTOP Class")

## 

Parameters - Play Page

File`file`\- The path and name of the image or movie file to load. Image and movie formats are those found in [File Types](<./File_Types.md> "File Types"). You can specify files on the internet using`http://`... 

To treat a folder of images as if they are one movie, specify the folder containing the images instead of a filename. All the files must be the same resolution. It will treat all stills/movies in that folder as if each is a frame in one movie. The order of the images is the alphanumeric. By default the first image has an index of 0, second is 1, etc, regardless of their file names. Overriding the sample rate on the Trim parameter page will let you playback the image sequence at any frame rate. 

Using an`info.xml`file in the directory containing a sequence of images allows you to specify the frames per second and an audio file to be used with the sequence of images. Example xml file: 
[code] 
    <?xml version="1.0" encoding="ISO-8859-1" standalone="yes" ?>
      <Settings>
          <attributes fps="30.0" />
          <audio filename="audio.wav" />
      </Settings>
    
[/code]

URLs can be used to fetch images and movies. The image or movie is downloaded to the user's Derivative temp directory and is read into the Movie File In TOP. __

Reload`reload`\- Change from 0 to 1 to force the image to reload, useful when the file changes or did not exist at first. 

Reload Pulse`reloadpulse`\- Instantly reloads the file. 

Play Mode`playmode`\- ⊞ \- Specifies the method used to play the movie, there are 3 options. 
* Locked to Timeline`locked`\- This mode locks the movie position to the timeline. Scrubbing or jumping in the timeline will change the movie position accordingly. The parameters Play, Reset, Speed, and Index are disabled in this mode since the timeline is directly tied to movie position.
* Specify Index`specify`\- This mode allows the user to specify a particular position in the movie using the Index parameter below. Use this mode for random access to any location in the movie.
* Sequential`sequential`\- This mode continually plays regardless of the timeline position (the Index parameter is disabled). Reset and Speed parameters below are enabled to allow some control.
* Timecode Object/CHOP/DAT`timecodeop`\- This mode allows the user to set the movie index by reference to a timecode in the form of either a CHOP, DAT, or [Timecode Class](<./Timecode_Class.md> "Timecode Class") object.


Play`play`\- Movie plays when 1, movie stops when 0. 

Speed`speed`\- This is a speed multiplier which only works when Play Mode is _Sequential_. A value of 1 is the default playback speed. A value of 2 is double speed, 0.5 is half speed and so on. Negative values will play the movie backwards. 

Cue`cue`\- Jumps to Cue Point when set to 1. Only available when Play Mode is Sequential. 

Cue Pulse`cuepulse`\- Instantly jumps to the Cue Point position in the movie. 

Cue Point`cuepoint`\- Set any index in the movie as a point to jump to. 

Cue Point Unit`cuepointunit`\- ⊞ \- Select the units for this parameter from Index, Frames, Seconds, and Fraction (percentage). 
* I`indices`-
* F`frames`-
* S`seconds`-
* %`fraction`-


Cue Behavior`cuebehavior`\- ⊞ \- Customize the Cue parameter's behavior. 
* On Release, Repeat Cued Frame`repeat`\- When releasing the Cue parameter, immediately play the next frame.
* On Release, Play Next Frame`play`\- When releasing the Cue parameter, first play the cued frame before continuing to play the next frame.


Index`index`\- This parameter explicitly sets the movie position when Play Mode is set to Specify Index. The units menu on the right lets you specify the index in the following units: Index, Frames, Seconds, and Fraction (percentage). For example, assume you have a movie that internally is 25 fps, and the timeline that is 60 fps. If you set Units to Index and the parameter value to 25, you get the image that is 1 second into the movie. If you set the Units to Frames and set the value to 60 you get the same image at 1 second into the movie. When this number is negative the index will cycle back through the movie. 

Index Unit`indexunit`\- ⊞ \- Select the units for this parameter from Index, Frames, Seconds, and Fraction (percentage). 
* I`indices`-
* F`frames`-
* S`seconds`-
* %`fraction`-


Loop Crossfade`loopcrossfade`\- Crossfades the beginning and end of the movie together to create a smooth transition when looping. If the movie uses Trim options, it will crossfade Trim Start with Trim End positions. 

Loop Crossfade Unit`loopcrossfadeunit`\- ⊞ \- Select the units for this parameter from Index, Frames, Seconds, and Fraction (percentage). 
* I`indices`-
* F`frames`-
* S`seconds`-
* %`fraction`-


Step Size`stepsize`\- Sets how many frames to skip before displaying next frame. For example, a StepSize of 30 will display every 30th frame. This timing of movie playback does not change, so with a Step Size of 30 and a sample rate of 30, a new frame will be displayed every second. 

Audio Loop`audioloop`\- ⊞ \- This menu helps you determine how to treat the audio as the end of a movie approaches. This is needed because of all the cases of playing a movie, like when driving with an index, the TOP will not know if you intend to loop it or not. 
* Silence`silence`\- Audio will go silent when movie ends.
* Fade`fade`\- Audio will fade out when movie ends.
* Match Start to End`match`-


Image Sequence Indexing`imageindexing`\- ⊞ \- Determines how an image sequence is ordered. 
* Zero Based`zero`\- Index the sequence of images starting at 0, after sorting them alphanumerically.
* Filename Based`filename`\- Index the sequence of images using the numbers on the end of the filenames. I.e a file named flower400.tiff will be frame index 400, regardless of if there are other files in the directory before it.


Timecode Mode`timecodemode`\- ⊞ \- 
* Absolute`absolute`-
* Use to File Timecode`usefiletimecode`-


Timecode Object/CHOP/DAT`timecodeop`\- Set the movie index with a reference to a timecode. Should be a reference to either a CHOP with channels 'hour', 'second', 'minute', 'frame', a DAT with a timecode string in its first cell, or a [Timecode Class](<./Timecode_Class.md> "Timecode Class") object. 

## 

Parameters - Image Page

Interpolate Frames`interp`\- Interpolates between frames based based on exact time. For example, if the index (in frames) is 1.5, then frames 1 and 2 will be blended 50-50. If the index is 1.7 then 30% of frame 1 is blended with 70% of frame 2 and so on. 

Deinterlace`deinterlace`\- ⊞ \- For movies that are stored as fields, where each image is made of two images interleaved together. A 30-frame per second movie would contain 60 fields per second. For each image, the even scanlines of the first field are interleaved with the odd scanlines of the second field. The Movie File In TOP has several ways of dealing with this: 
* Off`off`\- Output the movie images unchanged.
* Even`even`\- Take only the even scanlines of the file's images and create the odd scanlines by interpolating between the even scanlines. (For historic reasons, scanline 0 is at the top of the images for the purpose of the deinterlacing.)
* Odd`odd`-
* Bob (Split)`bob`-


Field Precedence`precedence`\- ⊞ \- Where fields are extracted one field at a time, this will extract the Even field first by default, otehrwise it will extract the odd field first. The video industry has not standardized on one or the other. 
* Even`even`\- When the disk files are fragmented. The Movie File In TOP will read frames of the movie into memory before they are used, this can eliminate pops or stutters in playback that occur from fragmented files, other resources accessing the hard drive, or movie looping.
* Odd`odd`-


Bottom Half is Alpha (AAA)`bottomhalfalpha`\- If enabled, the image/movie will have it's height halved, and the R channel from the pixels on the bottom half will be treated as if they were the alpha channel for the top half. Useful for cases where the image format does not support alpha natively. 

Multiply RGB by Alpha`multalpha`\- ⊞ \- Premultiplies the image. 
* Off`off`-
* On`on`-
* Automatic`automatic`-


Pre-Multiply RGB by Alpha`premultrgbbyalpha`\- ⊞ \- Premultiplies the image. 
* Off`off`-
* On`on`-
* Automatic`automatic`-


Input Color Space`inputcolorspace`\- ⊞ \- Controls what color space the input data will be treated as. It will be converted to the Working [Color Space](<./Color_Space.md> "Color Space") when uploaded to the GPU. 
* Automatic`automatic`\- Automatically try to determine the input's color space based on color space metadata available from the input, if any. If no color space can be determined, it is assumed to be sRGB.
* sRGB`srgb`\- [sRGB](<https://en.wikipedia.org/wiki/SRGB>) color space, with sRGB transfer function. Considered an SDR color space with respect to Reference White.
* sRGB - Linear`srgblinear`\- [sRGB](<https://en.wikipedia.org/wiki/SRGB>) color space, with linear transfer function. Considered an SDR color space with respect to Reference White.
* Rec.601 (NTSC)`rec601ntsc`\- [Rec.601](<https://en.wikipedia.org/wiki/Rec._601>) with NTSC primaries color space, with Rec.601 transfer function. Considered an SDR color space with respect to Reference White.
* Rec.709`rec709`\- [Rec.709](<https://en.wikipedia.org/wiki/Rec._709>) color space, with Rec.709 (same as Rec.2020) transfer function. Considered an SDR color space with respect to Reference White.
* Rec.2020`rec2020`\- [Rec.2020](<https://en.wikipedia.org/wiki/Rec._2020>) color space, with Rec.2020 (same as Rec.709) transfer function. Considered an HDR color space with respect to Reference White.
* Rec.2020 ST2084PQ`rec2020st2084pq`\- [Rec.2020](<https://en.wikipedia.org/wiki/Rec._2020>) color space, with [Perceptual Quantizer](<https://en.wikipedia.org/wiki/Perceptual_quantizer>) transfer function. Considered an HDR color space with respect to Reference White.
* Rec.2020 HLG`rec2020hlg`\- [Rec.2020](<https://en.wikipedia.org/wiki/Rec._2020>) color space, with [Hybrid Log Gamma](<https://en.wikipedia.org/wiki/Hybrid_log%E2%80%93gamma>) transfer function. Considered an HDR color space with respect to Reference White.
* DCI-P3`dcip3`\- [DCI-P3](<https://en.wikipedia.org/wiki/DCI-P3>) color space, with D65 white point and 2.6 gamma transfer function. Considered an HDR color space with respect to Reference White.
* DCI-P3 (D60)`dcip3d60`\- [DCI-P3 "D60 sim"](<https://en.wikipedia.org/wiki/DCI-P3>) color space, with D60 white point, and 2.6 gamma transfer function. Considered an HDR color space with respect to Reference White.
* Display-P3 (D65)`displayp3d65`\- [Display-P3](<https://en.wikipedia.org/wiki/DCI-P3>) color space, with D65 white point, and sRGB gamma transfer function. Considered an HDR color space with respect to Reference White.
* Display-P3 (D65) - Linear`displayp3d65linear`\- [Display-P3](<https://en.wikipedia.org/wiki/DCI-P3>) color space, with D65 white point, and linear transfer function. Considered an HDR color space with respect to Reference White.
* ACES2065-1`aces2065-1`\- [ACES 2065-1](<https://en.wikipedia.org/wiki/Academy_Color_Encoding_System>) (also known as ACES AP0) color space, with a linear gamma transfer function. Considered an HDR color space with respect to Reference White.
* ACEScg`acescg`\- [ACEScg](<https://en.wikipedia.org/wiki/Academy_Color_Encoding_System>) (also known as ACES AP1) color space, with a linear gamma transfer function. Considered an HDR color space with respect to Reference White.
* ACESproxy`acesproxy`\- [ACESproxy](<https://en.wikipedia.org/wiki/Academy_Color_Encoding_System>) color space, which has a log transfer function. Considered an HDR color space with respect to Reference White.
* Passthrough`passthrough`\- When selected, the color values will be used as-is in the operation, without any modification or attempt to convert them into the Working Color Space.


Input Reference White`inputreferencewhite`\- ⊞ \- When converting the input color values to the Working Color Space, this controls how they should be treated with respect to [Reference White](<./Color_Space.htm#Reference_White> "Color Space"). If the Working Color Space is the same Reference White, then no adjustment is done. If they are different, then the Reference White level (brightness) of the colors will be adjusted to the range expected by the Working Color Space. For example if the project is set to have a SDR Reference White of 120 nits, and the HDR Reference White is 80 nits, then a color of (1, 1, 1), which is 120 nits in the SDR color space, will be converted to be (1.5, 1.5, 1.5), which is 120 nits still in the HDR Working Color Space. 
* Default For Color Space`default`\- Will use either the SDR or the HDR Reference White, based on the color space detected/selected.
* Standard (SDR)`sdr`\- Will treat the Input Color Space as SDR for it's reference white value.
* High (HDR)`hdr`\- Will treat the Input Color Space as HDR for it's reference white value.


Loading/Error Image`loadingerrorimage`\- ⊞ \- When the file can not be loaded for some reason, select what to display instead. 
* Colored Bottom Right Square`coloredbottomright`\- Show a colored square in the bottom right. Red means failed to load, grey means still loading.
* Zero`zero`\- Show a blank frame.


Decode Pixel Format`decodepixelformat`\- ⊞ \- 
* Fastest`fastest`-
* Best`best`-

## 

Parameters - Trim Page

Trim`trim`\- Enables the parameters below to set trim in and out points. 

Trim Start`tstart`\- Trim the starting point of the movie. 

Trim Start Unit`tstartunit`\- ⊞ \- Select the units for this parameter from Index, Frames, Seconds, and Fraction (percentage). 
* I`indices`-
* F`frames`-
* S`seconds`-
* %`fraction`-


Trim End`tend`\- Trim the ending point of the movie. 

Trim End Unit`tendunit`\- ⊞ \- Select the units for this parameter from Index, Frames, Seconds, and Fraction (percentage). 
* I`indices`-
* F`frames`-
* S`seconds`-
* %`fraction`-


Extend Left`textendleft`\- ⊞ \- Determines how the Movie File In TOP handles movie positions that lie before the Trim Start position. For example, if Trim Start is set to 1, and the movie's current index is -10, the Extend Left menu determines how the movie position is calculated. 
* Hold`hold`\- Displays the first frame in the movie range (the frame specified by Trim Start) for any position before Trim Start.
* Cycle`cycle`\- Loops the movie range continuously.
* Mirror`mirror`\- Loops the movie range in a zig-zag pattern. For example, playing backwards from Trim Start the movie will index will climb towards Trim End, at which point is will decend down towards Trim Start again and continue to zig-zag (or mirror) the further the movie plays backwards.
* Black`black`\- Displays black frame for any movie position before Trim Start.
* Zero`zero`-


Extend Right`textendright`\- ⊞ \- Determines how the Movie File In TOP handles movie positions that lie after the Trim End position. For example, if Trim End is set to 20, and the movie's current index is 25, the Extend Right menu determines how the movie position is calculated. 
* Hold`hold`\- Displays the last frame in the movie range (the frame specified by Trim End) for any position after Trim End.
* Cycle`cycle`\- Loops the movie range continuously.
* Mirror`mirror`\- Loops the movie range in a zig-zag pattern. For example, playing forwards from Trim End the movie will index will start decending towards Trim Start, at which point is will start climbing towards Trim End and continue to zig-zag (or mirror) the further the movie plays.
* Black`black`\- Displays black frame for any movie position after Trim End.
* Zero`zero`-


Override Sample Rate`overridesample`\- Turn On to change the sample rate of the movie. When loading an image sequence, use these parameters to set the playback speed for the sequence. 

Sample Rate`samplerate`\- Set the sample rate for playback when 'Override Sample Rate' above is On. 

## 

Parameters - Tune Page

Pre-Read Frames`prereadframes`\- Sets how many video frames TouchDesigner reads ahead and stores in memory. The Movie File In TOP will read and decode frames of the movie into CPU memory before they are used, this can eliminate pops or stutters in playback that occur from some frames taking too long to decode, other resources accessing the hard drive, or movie looping. When reading a sequence of image, having more Pre Read Frames will allow multiple images to be decode at the same time. This allows playback of heavy file formats such as .exr in real-time, assuming the machine has enough CPU cores. 

Frame Read Timeout`frametimeout`\- The time (in milliseconds) TouchDesigner will wait for a frame from the hard drive before giving up. If the Disk Read Timeout time is reached, that frame is simply skipped. This also works for network files that are downloaded via http://. 

Frame Timeout Strategy`frametimeoutstrat`\- ⊞ \- When on, if the Disk Read Timeout is reached TouchDesigner will use the latest available frame in place of the skipped frame. 
* Keep Frame`keep`\- Keep showing the same frame that is currently being output.
* Best for Playback`playback`\- Try to pick the best frame for playback. This may be a newer frame that what is shown, but not quite the frame that is requested.
* Best for Seeking`seeking`\- Try to show any frame, either before or after the target frame. Good for when seeking the movie via a shuttle widget in a UI.


Always Load Initial Frame`alwaysloadinitial`\- If this parameter is turned on, then for the first loaded frame the Frame Read Timeout will be ignored, and it will always wait for the first frame to ensure the node always starts up with a valid image. 

File Open Timeout`opentimeout`\- The time (in milliseconds) TouchDesigner will wait for a movie to open. If the Disk Open Timout is reached, the Movie File In TOP will stop waiting and make its image all black, with a grey square in the bottom right corner. If the file still isn't opened the next time the TOP cooks, it'll wait again, and do the same. It'll keep doing this until the file is opened, or the open fails. 

On Timeout, use Latest Avail`uselatestontimeout`\- When on, if the Disk Read Timeout is reached TouchDesigner will use the latest available frame in place of the skipped frame. 

Pre-Download HTTP Addresses`predownloadhttp`\- When On, the file will be fully downloaded before playing. When Off, the file will be streamed from its currently URL. 

Update Image`updateimage`\- Image will not update when set to 0. Movie index will continue to move forward but the output image will not update. This is useful when you are using a Movie Audio CHOP to get audio from the movie, but you don't care about the video. 

Max Decode CPUs`maxdecodecpus`\- Limit the maximum number of CPUs that will be used to decode certain video codecs that are capable of multi-CPU decoding, such as H264/H265 and Cineform. Note that this does not affect multi-threaded decoding for image sequence playback, which is instead controlled by increasing the Pre-Read Frame parameter. 

High Performance Read`highperfread`\- This option should be used when playing back files that require very high SSD read speeds such as high resolution (4K+) HAP Q files. It greatly improves read performance in those cases. It should not be used for low resolution or low data rate files such as 1080p H264 files. 

High Performance Read Factor`highperfreadfactor`\- When doing high performance reads, this parameter controls the size of the read operations that are done on disk. Whatever the largest operation the codec asks to be done, this is multiplied by the read factor and all subsequent reads will read that much data instead. This can result in higher throughput depending on the drives. For example if a request is made to read 1MB and the factor is set to 3, then instead the operations will read 3MB from the disk and the extra 2MB read will be ready for the next frame and will likely already have the next 2 frames available in CPU RAM. 

Hardware Decode`hwdecode`\- Controls if this node should use hardware decoding via the Nvidia hardware decoder chip. You can check if hardware decoding is being used using the Info CHOP, 'hardware_decode' channel. This parameter does nothing for Hap and NotchLC codecs, which are always hardware decoded. 

Async Upload to GPU`asyncupload`\- When enabled, this will use OpenGL features to upload movie images to the GPU asynchronously. This will reduce the cook time of the Movie File In TOP considerably (in the performance monitor the lines that say "Uploading Image to GPU" will go down to almost nothing). There is a GPU memory cost to using this feature however. It uses up another (Width * Height * 4 * Read Ahead Size) bytes of GPU memory. If you are having poor results with this feature, make sure your graphics drivers are up to date. 

## 

Parameters - Common Page

Output Resolution`outputresolution`\- ⊞ \- quickly change the resolution of the TOP's data. 
* Use Input`useinput`\- Uses the input's resolution
* Eighth`eighth`\- Multiply the input's resolution by that amount.
* Quarter`quarter`\- Multiply the input's resolution by that amount.
* Half`half`\- Multiply the input's resolution by that amount.
* 2X`2x`\- Multiply the input's resolution by that amount.
* 4X`4x`\- Multiply the input's resolution by that amount.
* 8X`8x`\- Multiply the input's resolution by that amount.
* Fit Resolution`fit`\- Grow or shrink the input resolution to fit this resolution, while keeping the aspect ratio the same.
* Limit Resolution`limit`\- Limit the input resolution to be not larger than this resolution, while keeping the aspect ratio the same.
* Custom Resolution`custom`\- Directly control the width and height.


Resolution`resolution`\- ⊞ \- Enabled only when the Resolution parameter is set to Custom Resolution. Some Generators like Constant and Ramp do not use inputs and only use this field to determine their size. The drop down menu on the right provides some commonly used resolutions. 
* W`resolutionw`-
* H`resolutionh`-


Resolution Menu`resmenu`\- A drop-down menu with some commonly used resolutions. 

Use Global Res Multiplier`resmult`\- Uses the Global Resolution Multiplier found in **Edit >Preferences>TOPs**. This multiplies all the TOPs resolutions by the set amount. This is handy when working on computers with different hardware specifications. If a project is designed on a desktop workstation with lots of graphics memory, a user on a laptop with only 64MB VRAM can set the Global Resolution Multiplier to a value of half or quarter so it runs at an acceptable speed. By checking this checkbox on, this TOP is affected by the global multiplier. 

Output Aspect`outputaspect`\- ⊞ \- Sets the image aspect ratio allowing any textures to be viewed in any size. Watch for unexpected results when compositing TOPs with different aspect ratios. (You can define images with non-square pixels using xres, yres, aspectx, aspecty where xres/yres != aspectx/aspecty.) 
* Use Input`useinput`\- Uses the input's aspect ratio.
* Resolution`resolution`\- Uses the aspect of the image's defined resolution (ie 512x256 would be 2:1), whereby each pixel is square.
* Custom Aspect`custom`\- Lets you explicitly define a custom aspect ratio in the Aspect parameter below.


Aspect`aspect`\- ⊞ \- Use when Output Aspect parameter is set to Custom Aspect. 
* Aspect1`aspect1`-
* Aspect2`aspect2`-


Aspect Menu`armenu`\- A drop-down menu with some commonly used aspect ratios. 

Input Smoothness`inputfiltertype`\- ⊞ \- This controls pixel filtering on the input image of the TOP. 
* Nearest Pixel`nearest`\- Uses nearest pixel or accurate image representation. Images will look jaggy when viewing at any zoom level other than Native Resolution.
* Interpolate Pixels`linear`\- Uses linear filtering between pixels. This is how you get TOP images in viewers to look good at various zoom levels, especially useful when using any Fill Viewer setting other than Native Resolution.
* Mipmap Pixels`mipmap`\- Uses [ mipmap](<./Mipmapping.md> "Mipmapping") filtering when scaling images. This can be used to reduce artifacts and sparkling in moving/scaling images that have lots of detail.


Fill Viewer`fillmode`\- ⊞ \- Determine how the TOP image is displayed in the viewer. 

**NOTE:** To get an understanding of how TOPs work with images, you will want to set this to **Native Resolution** as you lay down TOPs when starting out. This will let you see what is actually happening without any automatic viewer resizing. 
* Use Input`useinput`\- Uses the same Fill Viewer settings as it's input.
* Fill`fill`\- Stretches the image to fit the edges of the viewer.
* Fit Horizontal`width`\- Stretches image to fit viewer horizontally.
* Fit Vertical`height`\- Stretches image to fit viewer vertically.
* Fit Best`best`\- Stretches or squashes image so no part of image is cropped.
* Fit Outside`outside`\- Stretches or squashes image so image fills viewer while constraining it's proportions. This often leads to part of image getting cropped by viewer.
* Native Resolution`nativeres`\- Displays the native resolution of the image in the viewer.


Viewer Smoothness`filtertype`\- ⊞ \- This controls pixel filtering in the viewers. 
* Nearest Pixel`nearest`\- Uses nearest pixel or accurate image representation. Images will look jaggy when viewing at any zoom level other than Native Resolution.
* Interpolate Pixels`linear`\- Uses linear filtering between pixels. Use this to get TOP images in viewers to look good at various zoom levels, especially useful when using any Fill Viewer setting other than Native Resolution.
* Mipmap Pixels`mipmap`\- Uses [ mipmap](<./Mipmapping.md> "Mipmapping") filtering when scaling images. This can be used to reduce artifacts and sparkling in moving/scaling images that have lots of detail. When the input is 32-bit float format, only nearest filtering will be used (regardless of what is selected).


Passes`npasses`\- Duplicates the operation of the TOP the specified number of times. For every pass after the first it takes the result of the previous pass and replaces the node's first input with the result of the previous pass. One exception to this is the [GLSL TOP](<./GLSL_TOP.md> "GLSL TOP") when using compute shaders, where the input will continue to be the connected TOP's image. 

Channel Mask`chanmask`\- Allows you to choose which channels (R, G, B, or A) the TOP will operate on. All channels are selected by default. 

Pixel Format`format`\- ⊞ \- Format used to store data for each channel in the image (ie. R, G, B, and A). Refer to [Pixel Formats](<./Pixel_Formats.md> "Pixel Formats") for more information. 
* Use Input`useinput`\- Uses the input's pixel format.
* 8-bit fixed (RGBA)`rgba8fixed`\- Uses 8-bit integer values for each channel.
* sRGB 8-bit fixed (RGBA)`srgba8fixed`\- Uses 8-bit integer values for each channel and stores color in sRGB colorspace. Note that this does **not** apply an sRGB curve to the pixel values, it only stores them using an sRGB curve. This means more data is used for the darker values and less for the brighter values. When the values are read downstream they will be converted back to linear. For more information refer to [sRGB](<./SRGB.md> "SRGB").
* 16-bit float (RGBA)`rgba16float`\- Uses 16-bits per color channel, 64-bits per pixel.
* 32-bit float (RGBA)`rgba32float`\- Uses 32-bits per color channel, 128-bits per pixels.
* 10-bit RGB, 2-bit Alpha, fixed (RGBA)`rgb10a2fixed`\- Uses 10-bits per color channel and 2-bits for alpha, 32-bits total per pixel.
* 16-bit fixed (RGBA)`rgba16fixed`\- Uses 16-bits per color channel, 64-bits total per pixel.
* 11-bit float (RGB), Positive Values Only`rgba11float`\- A RGB floating point format that has 11 bits for the Red and Green channels, and 10-bits for the Blue Channel, 32-bits total per pixel (therefore the same memory usage as 8-bit RGBA). The Alpha channel in this format will always be 1. Values can go above one, but can't be negative. ie. the range is [0, infinite).
* 16-bit float (RGB)`rgb16float`-
* 32-bit float (RGB)`rgb32float`-
* 8-bit fixed (Mono)`mono8fixed`\- Single channel, where RGB will all have the same value, and Alpha will be 1.0. 8-bits per pixel.
* 16-bit fixed (Mono)`mono16fixed`\- Single channel, where RGB will all have the same value, and Alpha will be 1.0. 16-bits per pixel.
* 16-bit float (Mono)`mono16float`\- Single channel, where RGB will all have the same value, and Alpha will be 1.0. 16-bits per pixel.
* 32-bit float (Mono)`mono32float`\- Single channel, where RGB will all have the same value, and Alpha will be 1.0. 32-bits per pixel.
* 8-bit fixed (RG)`rg8fixed`\- A 2 channel format, R and G have values, while B is 0 always and Alpha is 1.0. 8-bits per channel, 16-bits total per pixel.
* 16-bit fixed (RG)`rg16fixed`\- A 2 channel format, R and G have values, while B is 0 always and Alpha is 1.0. 16-bits per channel, 32-bits total per pixel.
* 16-bit float (RG)`rg16float`\- A 2 channel format, R and G have values, while B is 0 always and Alpha is 1.0. 16-bits per channel, 32-bits total per pixel.
* 32-bit float (RG)`rg32float`\- A 2 channel format, R and G have values, while B is 0 always and Alpha is 1.0. 32-bits per channel, 64-bits total per pixel.
* 8-bit fixed (A)`a8fixed`\- An Alpha only format that has 8-bits per channel, 8-bits per pixel.
* 16-bit fixed (A)`a16fixed`\- An Alpha only format that has 16-bits per channel, 16-bits per pixel.
* 16-bit float (A)`a16float`\- An Alpha only format that has 16-bits per channel, 16-bits per pixel.
* 32-bit float (A)`a32float`\- An Alpha only format that has 32-bits per channel, 32-bits per pixel.
* 8-bit fixed (Mono+Alpha)`monoalpha8fixed`\- A 2 channel format, one value for RGB and one value for Alpha. 8-bits per channel, 16-bits per pixel.
* 16-bit fixed (Mono+Alpha)`monoalpha16fixed`\- A 2 channel format, one value for RGB and one value for Alpha. 16-bits per channel, 32-bits per pixel.
* 16-bit float (Mono+Alpha)`monoalpha16float`\- A 2 channel format, one value for RGB and one value for Alpha. 16-bits per channel, 32-bits per pixel.
* 32-bit float (Mono+Alpha)`monoalpha32float`\- A 2 channel format, one value for RGB and one value for Alpha. 32-bits per channel, 64-bits per pixel.

## 

Info CHOP Channels

Extra Information for the Movie File In TOP can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). 

### 

Specific Movie File In TOP Info Channels
* index \- The current frame index being shown. This is in the FPS of the movie file, not in timeline frames.
* true_index \- When the movie has a Trim applied to it, this will show the actually frame index within the movie being shown.
* index_fraction \- Normalized index value going from 0-1 from start to the end of the movie.
* file_resx \- The width of the movie in pixels.
* file_resy \- The height of the movie in pixels.
* start \- Unused currently.
* length \- The length of the movie, in movie frames.
* sample_rate \- The FPS of the movie.
* last_index_uploaded \- The last movie frame uploaded to the GPU.
* mv_has_audio \- 1 if the movie has an audio track, 0 if not.
* preloading \- 1 if the movie is currently preloading via the preload() Python method.
* odd_field \- When deinterlacing using Bob (split), 1 means the odd field is being shown, 0 means the even field is being shown.
* last_frame \- 1 if the last frame of the movie is currently being shown, 0 if not. Note that if a frame is dropped the last frame may never get shown, if the movie is looping.
* loop_frame \- 1 if the movie has just looped.
* pre_read_misses \- Counts how many times the node wanted to show a frame, but that frame wasn't already ready in the Pre-Read Cache.
* last_pre_read_miss_wait \- The amount of time the node last waited for a pre_read_misses frame to be read, in milliseconds.
* hard_drive_timeouts \- The number of times the node gave up reading a frame due to it not reading fast enough. The amount of time it will wait is controlled by the 'Frame Read Timeout' parameter.
* num_pre_read_frames \- The number of frames that have been pre-read, decoded, and are ready to be shown.
* first_index_to_read \- The frame index of the first index in the Pre-Read cache.
* last_frame_hd_read_time \- The amount of time spent reading the last frame from the hard-drive, in milliseconds.
* last_frame_decode_time \- The amount of time spent decoding/decompression the last frame on the CPU, in milliseconds. This does not account for time spent decoding on the GPU for codecs such as NotchLC, or Hardware Decoded codecs.
* open \- 1 if the movie's file is open.
* opening \- 1 if the movie's file is in the process of opening, but not open yet.
* open_failed \- 1 if opening the movie failed.
* fully_pre_read \- 1 if the Pre-Read Cache of the movie is filled with already decoded frames.
* true_length \- The true length of the movie, ignoring any trimming.
* hardware_yuv_to_rgb \- 1 if the YUV format the movie was encoded in is being converted to RGB on the GPU.
* has_non_av_track \- 1 if the movie file has a track that is not video or audio, such as a subtitle track.
* pre_read_fails \- The number of times pre-reading a frame failed.
* disk_read_mbit_rate \- The amount of data being read per second off of the hard drive, in mega-bits.
* has_decode_errors \- 1 if the file is suffering from decode errors.
* num_decode_chunks \- For Hap codecs, how many chunks the file was encoded as.
* hardrware_decode \- If the Hardware Decode parameter is on, this will be 1 if the GPU is able to hardware decode the movie's codec.

### 

Common TOP Info Channels
* resx \- Horizontal resolution of the TOP in pixels.
* resy \- Vertical resolution of the TOP in pixels.
* aspectx \- Horizontal aspect of the TOP.
* aspecty \- Vertical aspect of the TOP.
* depth \- Depth of 2D or 3D array if this TOP contains a 2D or 3D texture array.
* gpu_memory_used \- Total amount of texture memory used by this TOP.

### 

Common Operator Info Channels
* total_cooks \- Number of times the operator has cooked since the process started.
* cook_time \- Duration of the last cook in milliseconds.
* cook_frame \- Frame number when this operator was last cooked relative to the component timeline.
* cook_abs_frame \- Frame number when this operator was last cooked relative to the absolute time.
* cook_start_time \- Time in milliseconds at which the operator started cooking in the frame it was cooked.
* cook_end_time \- Time in milliseconds at which the operator finished cooking in the frame it was cooked.
* cooked_this_frame \- 1 if operator was cooked this frame.
* warnings \- Number of warnings in this operator if any.
* errors \- Number of errors in this operator if any.


  
TouchDesigner Build: Latest\nwikieditorwikieditorwikieditorwikieditor2025.300002023.112802022.241402021.100002018.28070before 2018.28070

TOPs   
---  
[Add ](<./Add_TOP.md> "Add TOP")• [Analyze ](<./Analyze_TOP.md> "Analyze TOP")• [Anti Alias ](<./Anti_Alias_TOP.md> "Anti Alias TOP")• [Blob Track ](<./Blob_Track_TOP.md> "Blob Track TOP")• [Bloom ](<./Bloom_TOP.md> "Bloom TOP")• [Blur ](<./Blur_TOP.md> "Blur TOP")• [Cache Select ](<./Cache_Select_TOP.md> "Cache Select TOP")• [Cache ](<./Cache_TOP.md> "Cache TOP")• [Channel Mix ](<./Channel_Mix_TOP.md> "Channel Mix TOP")• [CHOP to ](<./CHOP_to_TOP.md> "CHOP to TOP")• [Chroma Key ](<./Chroma_Key_TOP.md> "Chroma Key TOP")• [Circle ](<./Circle_TOP.md> "Circle TOP")• [Composite ](<./Composite_TOP.md> "Composite TOP")• [Constant ](<./Constant_TOP.md> "Constant TOP")• [Convolve ](<./Convolve_TOP.md> "Convolve TOP")• [Corner Pin ](<./Corner_Pin_TOP.md> "Corner Pin TOP")• [CPlusPlus ](<./CPlusPlus_TOP.md> "CPlusPlus TOP")• [Crop ](<./Crop_TOP.md> "Crop TOP")• [Cross ](<./Cross_TOP.md> "Cross TOP")• [Cube Map ](<./Cube_Map_TOP.md> "Cube Map TOP")• [Depth ](<./Depth_TOP.md> "Depth TOP")• [Difference ](<./Difference_TOP.md> "Difference TOP")• [Direct Display Out ](<./Direct_Display_Out_TOP.md> "Direct Display Out TOP")• [DirectX In ](<./DirectX_In_TOP.md> "DirectX In TOP")• [DirectX Out ](<./DirectX_Out_TOP.md> "DirectX Out TOP")• [Displace ](<./Displace_TOP.md> "Displace TOP")• [Edge ](<./Edge_TOP.md> "Edge TOP")• [Emboss ](<./Emboss_TOP.md> "Emboss TOP")• [Feedback ](<./Feedback_TOP.md> "Feedback TOP")• [Fit ](<./Fit_TOP.md> "Fit TOP")• [Flip ](<./Flip_TOP.md> "Flip TOP")• [Function ](<./Function_TOP.md> "Function TOP")• [GLSL Multi ](<./GLSL_Multi_TOP.md> "GLSL Multi TOP")• [GLSL ](<./GLSL_TOP.md> "GLSL TOP")• [HSV Adjust ](<./HSV_Adjust_TOP.md> "HSV Adjust TOP")• [HSV to RGB ](<./HSV_to_RGB_TOP.md> "HSV to RGB TOP")• [Import Select ](<./Import_Select_TOP.md> "Import Select TOP")• [In ](<./In_TOP.md> "In TOP")• [Inside ](<./Inside_TOP.md> "Inside TOP")• [Introduction To s Vid ](<./Introduction_To_TOPs_Vid.md> "Introduction To TOPs Vid")• [Kinect Azure Select ](<./Kinect_Azure_Select_TOP.md> "Kinect Azure Select TOP")• [Kinect Azure ](<./Kinect_Azure_TOP.md> "Kinect Azure TOP")• [Kinect ](<./Kinect_TOP.md> "Kinect TOP")• [Layer Mix ](<./Layer_Mix_TOP.md> "Layer Mix TOP")• [Layer ](<./Layer_TOP.md> "Layer TOP")• [Layout ](<./Layout_TOP.md> "Layout TOP")• [Leap Motion ](<./Leap_Motion_TOP.md> "Leap Motion TOP")• [Lens Distort ](<./Lens_Distort_TOP.md> "Lens Distort TOP")• [Level ](<./Level_TOP.md> "Level TOP")• [Limit ](<./Limit_TOP.md> "Limit TOP")• [Lookup ](<./Lookup_TOP.md> "Lookup TOP")• [Luma Blur ](<./Luma_Blur_TOP.md> "Luma Blur TOP")• [Luma Level ](<./Luma_Level_TOP.md> "Luma Level TOP")• [Math ](<./Math_TOP.md> "Math TOP")• [Matte ](<./Matte_TOP.md> "Matte TOP")• [Mirror ](<./Mirror_TOP.md> "Mirror TOP")• [Monochrome ](<./Monochrome_TOP.md> "Monochrome TOP")• [MoSys ](<./MoSys_TOP.md> "MoSys TOP")• Movie File In • [Movie File Out ](<./Movie_File_Out_TOP.md> "Movie File Out TOP")• [MPCDI ](<./MPCDI_TOP.md> "MPCDI TOP")• [Multiply ](<./Multiply_TOP.md> "Multiply TOP")• [Ncam ](<./Ncam_TOP.md> "Ncam TOP")• [NDI In ](<./NDI_In_TOP.md> "NDI In TOP")• [NDI Out ](<./NDI_Out_TOP.md> "NDI Out TOP")• [Noise ](<./Noise_TOP.md> "Noise TOP")• [Normal Map ](<./Normal_Map_TOP.md> "Normal Map TOP")• [Notch ](<./Notch_TOP.md> "Notch TOP")• [Null ](<./Null_TOP.md> "Null TOP")• [NVIDIA Background ](<./NVIDIA_Background_TOP.md> "NVIDIA Background TOP")• [NVIDIA Denoise ](<./NVIDIA_Denoise_TOP.md> "NVIDIA Denoise TOP")• [NVIDIA Flex ](<./NVIDIA_Flex_TOP.md> "NVIDIA Flex TOP")• [NVIDIA Flow ](<./NVIDIA_Flow_TOP.md> "NVIDIA Flow TOP")• [NVIDIA Upscaler ](<./NVIDIA_Upscaler_TOP.md> "NVIDIA Upscaler TOP")• [OAK Select ](<./OAK_Select_TOP.md> "OAK Select TOP")• [Oculus Rift ](<./Oculus_Rift_TOP.md> "Oculus Rift TOP")• [OP Viewer ](<./OP_Viewer_TOP.md> "OP Viewer TOP")• [OpenColorIO ](<./OpenColorIO_TOP.md> "OpenColorIO TOP")• [OpenVR ](<./OpenVR_TOP.md> "OpenVR TOP")• [Optical Flow ](<./Optical_Flow_TOP.md> "Optical Flow TOP")• [Orbbec Select ](<./Orbbec_Select_TOP.md> "Orbbec Select TOP")• [Orbbec ](<./Orbbec_TOP.md> "Orbbec TOP")• [Ouster Select ](<./Ouster_Select_TOP.md> "Ouster Select TOP")• [Ouster ](<./Ouster_TOP.md> "Ouster TOP")• [Out ](<./Out_TOP.md> "Out TOP")• [Outside ](<./Outside_TOP.md> "Outside TOP")• [Over ](<./Over_TOP.md> "Over TOP")• [Pack ](<./Pack_TOP.md> "Pack TOP")• [Photoshop In ](<./Photoshop_In_TOP.md> "Photoshop In TOP")• [Point File In ](<./Point_File_In_TOP.md> "Point File In TOP")• [Point File Select ](<./Point_File_Select_TOP.md> "Point File Select TOP")• [Point Transform ](<./Point_Transform_TOP.md> "Point Transform TOP")• [POP to ](<./POP_to_TOP.md> "POP to TOP")• [PreFilter Map ](<./PreFilter_Map_TOP.md> "PreFilter Map TOP")• [Projection ](<./Projection_TOP.md> "Projection TOP")• [Ramp ](<./Ramp_TOP.md> "Ramp TOP")• [RealSense ](<./RealSense_TOP.md> "RealSense TOP")• [Rectangle ](<./Rectangle_TOP.md> "Rectangle TOP")• [Remap ](<./Remap_TOP.md> "Remap TOP")• [Render Pass ](<./Render_Pass_TOP.md> "Render Pass TOP")• [Render Select ](<./Render_Select_TOP.md> "Render Select TOP")• [Render Simple ](<./Render_Simple_TOP.md> "Render Simple TOP")• [Render ](<./Render_TOP.md> "Render TOP")• [RenderStream In ](<./RenderStream_In_TOP.md> "RenderStream In TOP")• [RenderStream Out ](<./RenderStream_Out_TOP.md> "RenderStream Out TOP")• [Reorder ](<./Reorder_TOP.md> "Reorder TOP")• [Resolution ](<./Resolution_TOP.md> "Resolution TOP")• [RGB Key ](<./RGB_Key_TOP.md> "RGB Key TOP")• [RGB to HSV ](<./RGB_to_HSV_TOP.md> "RGB to HSV TOP")• [Scalable Display ](<./Scalable_Display_TOP.md> "Scalable Display TOP")• [Screen Grab ](<./Screen_Grab_TOP.md> "Screen Grab TOP")• [Screen ](<./Screen_TOP.md> "Screen TOP")• [Script ](<./Script_TOP.md> "Script TOP")• [Select ](<./Select_TOP.md> "Select TOP")• [Shared Mem In ](<./Shared_Mem_In_TOP.md> "Shared Mem In TOP")• [Shared Mem Out ](<./Shared_Mem_Out_TOP.md> "Shared Mem Out TOP")• [SICK ](<./SICK_TOP.md> "SICK TOP")• [Slope ](<./Slope_TOP.md> "Slope TOP")• [Spectrum ](<./Spectrum_TOP.md> "Spectrum TOP")• [SSAO ](<./SSAO_TOP.md> "SSAO TOP")• [ST2110 In ](<./ST2110_In_TOP.md> "ST2110 In TOP")• [ST2110 Out ](<./ST2110_Out_TOP.md> "ST2110 Out TOP")• [Stype ](<./Stype_TOP.md> "Stype TOP")• [Substance Select ](<./Substance_Select_TOP.md> "Substance Select TOP")• [Substance ](<./Substance_TOP.md> "Substance TOP")• [Subtract ](<./Subtract_TOP.md> "Subtract TOP")• [SVG ](<./SVG_TOP.md> "SVG TOP")• [Switch ](<./Switch_TOP.md> "Switch TOP")• [Syphon Spout In ](<./Syphon_Spout_In_TOP.md> "Syphon Spout In TOP")• [Syphon Spout Out ](<./Syphon_Spout_Out_TOP.md> "Syphon Spout Out TOP")• [Text ](<./Text_TOP.md> "Text TOP")• [Texture 3D ](<./Texture_3D_TOP.md> "Texture 3D TOP")• [Texture Sampling Parameters ](<./Texture_Sampling_Parameters.md> "Texture Sampling Parameters")• [Threshold ](<./Threshold_TOP.md> "Threshold TOP")• [Tile ](<./Tile_TOP.md> "Tile TOP")• [Time Machine ](<./Time_Machine_TOP.md> "Time Machine TOP")• [Tone Map ](<./Tone_Map_TOP.md> "Tone Map TOP")• [TOP ](<./TOP.md> "TOP")• [TOP Viewer ](<./TOP_Viewer.md> "TOP Viewer")• [Touch In ](<./Touch_In_TOP.md> "Touch In TOP")• [Touch Out ](<./Touch_Out_TOP.md> "Touch Out TOP")• [Transform ](<./Transform_TOP.md> "Transform TOP")• [Under ](<./Under_TOP.md> "Under TOP")• [Video Device In ](<./Video_Device_In_TOP.md> "Video Device In TOP")• [Video Device Out ](<./Video_Device_Out_TOP.md> "Video Device Out TOP")• [Video Stream In ](<./Video_Stream_In_TOP.md> "Video Stream In TOP")• [Video Stream Out ](<./Video_Stream_Out_TOP.md> "Video Stream Out TOP")• [Vioso ](<./Vioso_TOP.md> "Vioso TOP")• [Web Render ](<./Web_Render_TOP.md> "Web Render TOP")• [ZED Select ](<./ZED_Select_TOP.md> "ZED Select TOP")• [ZED ](<./ZED_TOP.md> "ZED TOP")
