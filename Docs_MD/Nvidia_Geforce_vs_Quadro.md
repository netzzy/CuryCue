# Nvidia Geforce vs Quadro

### Nvidia Product Lines and Generations  
  
For TouchDesigner system builders, the Nvidia ecosystem segments are essentially divided into two verticals. First is the gaming GPU line called Geforce and the second is Quadro which is the professional line. The Quadro line is focused on media production, large format video delivery, CAD and scientific visualization. 

For TouchDesigner video servers built for frame accurate professional video applications, the Quadro line should be used because it has a range of features specifc to high resolution multiple screen mapping as well as particular frame sync technologies. 

For most personal TouchDesigner development systems the Geforce line is preferable if for no other reason than price. The Geforce line is always significantly less expensive than the Quadro counterpart. As well, TouchDesigner plays very well with the game focused tuning of the Geforce line. 

Nvidia releases an entire generation of chips that cover all their lines. All products in the same generation use the same chip, whether its Geforce, Quadro or anything else. Various features are exposed or not in either Geforce or Quadro. As well the chips will be paired with a wide range of memory bandwidths, clock speeds, and other specialized IP cores that will impact performance. 

Models | Kepler | Maxwell | Pascal | Volta | Turing   
---|---|---|---|---|---  
Year Introduced | Q2 2012 | Q1 2014 | Q2 2016 | Q2 2017 | Q2 2018   
Geforce Base Model | 860 | 960 | 1060 |  | RTX 2060   
Geforce Premium Model | GTX 880 Ti | GTX 980 Ti | GTX 1080 Ti |  | RTX 2080 Ti   
Geforce Titan Model |  | Titan | Titan X / Xp | Titan V | TITAN RTX   
Quadro Series | K6000 | M6000 | P6000 |  | RTX6000   
Quadro G Series |  |  | GP100 | GV100 |   
  
## Geforce vs Geforce Ti vs Titan

The Geforce line is divided into a few subcategories which separate the “regular” models from the “premium” and “ultra premium”. As indicated below, the configuration of each GPU and card will affect overall performance. Over the passed 6 years Nvidia has close to doubling the overall performance of each subsequent GPU generation. Nvidia offers value oriented GPU boards with the 1060, 1070 and 1070 Ti, and premium models with the, 1080, 1080 Ti and Titan versions. 

The Ti versions of Geforce cards generally have more memory and greater performance specs like overall core counts. Ti stands for Titanium and apparently has no technical meaning, so it’s just marketing lingo that implies “premium” - and has no relationship to Titan in meaning. 

The Titan versions are the “ultra high end” of the Geforce line. This generally translates to a little more of everything over the for highest numbered Ti models, but Titan models will still be missing Quadro professional features. 

It’s worth noting here that Nvidia did skip releasing Volta based mid range Geforce and Quadro cards. Volta chips can be found only in the ultra premium models of each line, producing the Titan XV and Quadro GP100. 

## Quadro G Series GPUs

The Quadro GP100 (Pascal) and GV100 (Volta) are souped up cards with added features for running compute software, deep learning algorithms and other such things that are currently unsupported in TouchDesigner. They are missing important features that are required to run 3D apps, and will run TouchDesigner poorly. 

## Tesla GPUs

Tesla GPUs are are designed for running compute type applications and virtualization workstation and are currently not compatible with TouchDesigner. Tesla GPUs are equipped with Tensor cores in addition to the standard Nvidia GPU, “Cuda Cores”. These generally drive up the price as can be seen with the Quadro G Series and the Volta Generation. Please let us know if you have an application for this technology. 
1. Nvidia Tesla [[[1]](<https://en.wikipedia.org/wiki/Nvidia_Tesla>)]

## GPU Features That Matter

There are wide range of GPU features that vary from card to card. This section isolates the most important stats for comparison. 

### Floating-Point Performance

FLOPs stands for “floating-point operations per second.” Floating-point performance is a measurement of the raw processing power of the GPU, and therefore has been a quick way to compare GPUs. With the introduction of Compute cores, Tesla cores and RTX cores, the FLOPs total is getting a massive boost in the general stats. However many of the technologies that boost the numbers are currently not utilized by TouchDesigner. Therefore it is increasingly difficult to compare the singular GFLOP numbers between for example the Maxwell and Pascal line vs the Volta and Turing lines that have these new core types and include the stats rolled into a single value. 

To compare direct floating point numbers use the statistic FP32 and FP64 instead. The total GFLOPs numbers are general adding together a range of different cores and therefore can be misleading. 

### Pixel Rate

The number of pixels that can be rendered to the screen every second. 

### Shading Processors (Units)

Shading units (or shading processors) are small processors within the graphics card that are responsible for processing different aspects of the image. You may also hear shading units referred to as “streaming cores” and “cuda cores”. 

### Texture Mapping Units (TMUS)

TMUs take textures and map them to the geometry of a 3D scene. More TMUs will typically mean that texture information is processed faster. 

### Texture Rate

The number of textured pixels that can be rendered to the screen every second. 

### Render Output Units (ROPs)

The ROPs are responsible for some of the final steps of the rendering process, writing the final pixel data to memory and carrying out other tasks such as anti-aliasing to improve the look of graphics. 

### RAM

This is the total GPU memory for the graphics card. 

### Memory Bus Width

A wider bus width means that it can carry more data per cycle. It is an important factor of memory performance, and therefore the general performance of the graphics card. 

### Version of DDR Memory

Newer versions of GDDR memory offer improvements such as higher transfer rates that give increased performance. 

### Output Types / HDMI / DisplayPort / DVI

The type of hardware video connectors on the GPU board. 

### High Color Depths

Most graphics support only 8bit color depth which is 256 levels of RGBA. Some Quadro cards support higher bit depths such as 10bit color. Generally this will require a modern DisplayPort type video port and must be connected using the correct cable and to a device that support the desired color depth. 

## General Features

The following section covers those features that are common across all lines of Nvidia GPU since the introduction of the Kepler family. 

### Nvidia NVENC

Nvidia NVENC is a technology that performs video encoding, freeing the CPU for other mission critical tasks - like for example running TouchDesigner. It was first introduced with the Kepler-based microarchitecture in March 2012, and since then has evolved over the generations to support more encoding technologies. 

When using the [Movie File Out TOP](<./Movie_File_Out_TOP.md> "Movie File Out TOP"), selecting any H264 or H265/HVEC codec will utilize the GPU based encoder. You can detect if the NVENC encoder is active by using the Windows Task Manager application. The Performance page of the Task Manager has a graph for the utilization of the Video Encode engine. 

GeForce graphics cards support no more than 2 simultaneously encoding video streams, regardless of the number of cards installed. Quadro cards support many (restricted only by available resources) simultaneous streams per card, depending on many factors like card model and compression quality. 

For more information on supported encoding video codecs refer to this support matrix… All supported video codecs in the follow support matrix are not necessarily supported by TouchDesigner. 

[https://developer.nvidia.com/video-encode-decode-gpu-support-matrix](<https://www.google.com/url?q=https://developer.nvidia.com/video-encode-decode-gpu-support-matrix&sa=D&ust=1552417247868000>)

### Nvidia PureVideo

[https://en.wikipedia.org/wiki/Nvidia_PureVideo](<https://www.google.com/url?q=https://en.wikipedia.org/wiki/Nvidia_PureVideo&sa=D&ust=1552417247870000>)

Nvidia PureVideo is a hardware SIP core that performs video decoding and should not be confused with NVENC. By default TouchDesigner video decoding is CPU based and managed directly by TouchDesigner. Video decoding in TouchDesigner is threaded across multiple CPUs, if the codec supports it. Nvidia PureVideo decoding can be enabled by turning on the 'Hardware Decode' parameter on the 'Tune' page of the [Movie File In TOP](<./Movie_File_In_TOP.md> "Movie File In TOP"). 

## Quadro Specific Features

This section describes the features only available with the professional Quadro line of graphics cards. 

### Faster GPU-to-CPU Memory Transfers

Quadro's offer faster GPU-to-GPU memory transfers, which are important for any video outputs that arn't going through the GPU's displayport/HDMI outputs. If your system is using other outputs such as [Video Device Out TOP](<./Video_Device_Out_TOP.md> "Video Device Out TOP"), [NDI Out TOP](<./NDI_Out_TOP.md> "NDI Out TOP"), [Video Stream Out TOP](<./Video_Stream_Out_TOP.md> "Video Stream Out TOP"), you may want to consider a Quadro if the total resolution being sent is high. 

### Support from Nvidia

Quadro's offer direct support from Nvidia for issues that are encountered, which isn't offered for Geforce cards. If an issue is reported that we think is related to the Nvidia software/driver, we have no avenue to get support if the issue is only reproduced on a Geforce device. 

### Settings Profiles

Quadro cards come with GPU driver settings that are tuned for particular use cases. 

### EDID Spoofing

Sometimes it’s necessary to hardcode the graphics cards to a particular device EDID to ensure that the screen configuration remains the same even when the graphics ports are disconnected. By default Windows will immediately reconfigure the screen layout based on what devices are connected. The driver will remember the last configuration based on the EDIDs that it finds. For installations with permanent connections its imperative that ports are hardcoded even when screens are disconnected. This is not possible with Geforce cards so an external hardware solution would be required for the same behavior. 

### Mosaic

<https://www.nvidia.com/en-us/design-visualization/solutions/nvidia-mosaic-technology>

There are various screen tearing and frame dropping artifacts present in the Windows 10 system. Removing all these artifacts can be difficult and is a bit of a black art. See [Perfect Playback](<./Perfect_Playback.md> "Perfect Playback") for more information. One feature that can be critical for perfectly smooth playback is to use Nvidia Mosaic technology to unify the windows desktop into a single desktop across up to all 4 display ports. Thus if each DisplayPort was sending a 3840x2160 output, the entire windows desktop would be 7680x4320. If all devices connected to the Display ports are the same model device, and Nvidia Mosaic is enabled then it’s possible playback and sync artifacts will be avoided. 

Along with the Nvidia Control Panel UI. Mosaic can also be configured on the command line using the [Mosaic Utility](<https://www.nvidia.com/en-us/drivers/mosaic-utility/>). 

Geforce cards have a similar but less powerful feature called 'Surround', which can also be used to achieve similar results though. 

### Quadro Sync

[Quadro Sync](<https://www.nvidia.com/en-us/design-visualization/solutions/quadro-sync/>)

[Quadro Sync Setup Guide ](<http://images.nvidia.com/content/quadro/product-literature/user-guides/Quadro-Sync-II-User-Guide.pdf>)

If a screen or projector array is run by more than one physical computer or a computer with multiple graphics cards, then a Quadro Sync expansion card can be used to synchronize all graphics cards to the same sync phase. Without this sync card the screens connected to one graphics card may be off in phase from other cards causing visual tearing of content between the displays. This may or may not be noticible depending on the content being shown. 

Quadro Sync is also required to use Hardware Framelock in the [Window COMP](<./Window_COMP.md> "Window COMP") or the [Direct Display Out TOP](<./Direct_Display_Out_TOP.md> "Direct Display Out TOP"). 

Along with the Nvidia Control Panel UI, it can be configured using the [QSync Utility](<https://www.nvidia.com/en-us/drivers/qsync-utility/>). 

Quadro Sync should not be confused with Nvidia G-sync which is a gaming technology for smoother game play in video games. Many years ago Quadro Sync was named G-Sync though. 

## Unsupported Nvidia Technology

The following section covers Nvidia technology that is not supported by TouchDesigner. 

### Quadro NVS

Quadro NVS cards should not be confused with regular Quadro cards. They are designed for business applications that require many large displays for viewing things like financial data for stock brokers etc. The GPUs found on these cards are not appropriate for demanding GPU applications like TouchDesigner. 

### Nvidia SLI

SLI is a gaming technology that permits multiple graphics cards to render a single raster of graphics by dividing and distributing across multiple GPUs. TouchDesigner is not compatible with SLI. The only way to take advantage of multiple graphics cards is to use [GPU Affinity](<./Using_Multiple_Graphic_Cards.htm#GPU_Affinity> "Using Multiple Graphic Cards"). 

Multiple cards in the same system will allow for addressing all the outs of each graphics card. However only a single GPU will be used for rendering and that GPU will not work optimally since there is overhead for the main GPU to manage communication with the other GPU output ports. 

Simply put, without GPU affinity, TouchDesigner runs optimally only with a single graphics card per computer.
