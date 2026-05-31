# Intel Processors and TouchDesigner

When considering the construction of a TouchDesigner powered media server, the first consideration is what graphics card and peripherals will be required to support the range of features to fulfill the purpose of the server. Once these choices are made a CPU may be chosen. The choice of CPU will then limit the alternatives for motherboard through CPU socket type as well as memory and PCI slot configurations. 

See also [TouchDesigner Video Server Specification Guide](<./TouchDesigner_Video_Server_Specification_Guide.md> "TouchDesigner Video Server Specification Guide"). 

### Intel Product Lines for TouchDesigner

TouchDesigner runs on any Intel Core or Xeon processor. These two processor types have an expansive range of generations and models. This document will cover CPU basics to make it easier to choose a processor for use with TouchDesigner. 
* Entire Core line of Processors - <https://ark.intel.com/content/www/us/en/ark.html#@PanelLabel122139>
  * Entire Xeon line of processors - <https://ark.intel.com/content/www/us/en/ark.html#@PanelLabel595>

### CPU Clock Speed - GHz

The main TouchDesigner application runs on a single thread. This means for a single instance of TouchDesigner, only one core will compute each operation in sequence. To run at 60 FPS, your TD application must be able to compute all operations within 1/60th of a second, or 16.666 ms. If your TD application has demanding processing requirements that are CPU bound, the only way to provide more processing power is with a higher clock speed when all things like CPU product, generation, etc are otherwise equal. 

Therefore, with all other things equal, the ideal CPU is the model that fits all of your requirements, and has the highest individual core speed possible. Individual core speed is reflected as the statistic Gigahertz or GHz. 

### Core Count

Among other things the TouchDesigner [Movie File In TOP](<./Movie_File_In_TOP.md> "Movie File In TOP") operator, which is responsible for streaming movie files and image sequences off disk, is threaded. This means each movie being decoded can have parallel access to CPU resources separate from the main TouchDesigner thread. The operating system automatically manages the assignment of threads to CPU cores. There are many factors that play a role in calculating the CPU model and number of CPUs required for a given video server use case. 

If the media server is to decode many streams of H.264 using the [Movie File In TOP](<./Movie_File_In_TOP.md> "Movie File In TOP"), then having many cores will matter in a CPU. As well Windows can run multiple separate TouchDesigner or TouchEngine processes in parallel so having the right number of cores to support the required number of threads is very important... 

### PCI Express Lanes

Understanding the basic function and nomenclature surrounding PCI-e lanes is critical when configuring a PC and choosing the right CPU for a TouchDesigner powered system. A PCIe lane is a data pathway to and from the CPU between expansion devices like the hard drives and graphics cards. An individual lane will have a particular bandwidth measured in bytes/s. The frequency at which the data travels along the pathway will determine the transfer rate. A single lane of PCIe 3.0 has a bandwidth of 1GB/s. PCIe ports on a motherboard are generally either x1, x4, 8x or x16 which will increase the bandwidth of the port by the expressed amount. 

PCI Express | Introduced | Transfer | Throughput |  |  |  |   
---|---|---|---|---|---|---|---  
version |  | rate | ×1 | ×2 | ×4 | ×8 | ×16   
1 | 2003 | 2.5 GT/s | 250 MB/s | 0.50 GB/s | 1.0 GB/s | 2.0 GB/s | 4.0 GB/s   
2 | 2007 | 5.0 GT/s | 500 MB/s | 1.0 GB/s | 2.0 GB/s | 4.0 GB/s | 8.0 GB/s   
3 | 2010 | 8.0 GT/s | 984.6 MB/s | 1.97 GB/s | 3.94 GB/s | 7.88 GB/s | 15.8 GB/s   
4 | 2017 | 16.0 GT/s | 1969 MB/s | 3.94 GB/s | 7.88 GB/s | 15.75 GB/s | 31.5 GB/s   
5 | expected in | 32.0 GT/s] | 3938 MB/s | 7.88 GB/s | 15.75 GB/s | 31.51 GB/s | 63.0 GB/s   
| Q2 2019] |  |  |  |  |  |   
  
A given CPU will support only a maximum number of PCIe lanes. A given PCIe expansion card will require a particular number of lanes, which in turn will require a specific PCIe slot that supports the required bandwidth. Therefore we first must consider the number of PCIe lanes that are required to support the graphics card and any other expansion boards before deciding on CPU and motherboard. 

As of Q4 2018 the only PCI Express version to be concerned with is PCI Express 3.0. The entire line of Intel Core and Xeon chips support only 3.0. This means when looking at CPU, graphics, video and hard drive controller expansion board specifications, “number of lanes” will generally be referring to the number of PCI Express 3.0 lanes. 

Consider the Intel® Core™ i7-5930K Processor, which has the following specification. 

<https://ark.intel.com/products/82931/Intel-Core-i7-5930K-Processor-15M-Cache-up-to-3-70-GHz->

A web page search for “lanes” at the above address will provide the following subsection. 

Here we see the CPU will support 40 lanes of PCI. This means with two Quadro P6000 cards - which both require 16 PCIe lanes each, that this computer will have only 8 lanes left. If the system needs to capture video as well, for example with the Datapath VisionHD4 card, the number of PCI lanes need to be considered from the board spec. 

<https://www.datapath.co.uk/datapath-products/video-capture-cards/visionav-range/vision-hd4>

The spec page indicates an 8 Lane PCI Express Gen.3 bus is required. Looking closer, only 4 PCIe lanes will actually be used by the card. With a total of 8 lanes remaining the CPU could support two of these cards, even with two Quadro P6000 cards taking up 32 lanes. This example illustrates how decisions on expansion boards can drive the choice of CPU and visa versa. Decisions on GPU, storage and expansion PCIe boards (like video capture and output) will all affect the total number of lanes required. Decisions on all these components should be made, and a total count of lanes should be calculated before finalizing a CPU choice. 

### Comparing Systems 8 Lanes vs 16 Lanes - Do PCI Lanes Always Matter?

In October of 2019 we set up a case study in cooperation with Cocolabs Mexico City. We had the opportunity to compare performance between 2 system configurations. The systems were designated as Coco1 and Coco2. 

Coco1 system was using a Xeon processor with 48 lanes of PCI. Coco2 had an i7 providing only 16 lanes of PCI. As well, Coco1's motherboard has built-in dual 10G NIC, and a faster NVMe Samsung SSD. Coco2 is less expensive. 

Both systems are using the same dual Quadro P4000 cards. Each P4000 Quadro card can utilize 16 lanes of PCI each. Because Coco2 has only 16 lanes on the CPU, using both cards will force the PCI lanes to run in 8x mode, effectively halving the total bandwidth for pushing data to and from the card over the PCI bus. 

With these differences in mind, a comparison of synthetic performance benchmarks between these 3 system configurations is quite interesting. Note that Coco2-1 and Coco2-2 are matching systems but Coco2-1 has a single GPU running at x16 and Coco2-2 has a single GPU running at x8. 

##### Coco1 System Config: Price ~ 3500

Part Type | QTY | Brand | Model   
---|---|---|---  
Motherboard | 1 | Asus | WS C422 SAGE / 10G   
CPU | 1 | Intel | Xeon W 2135 - (Skylake) - 6 cores - 12 threads - 3.7/4.5Ghz - 48 Lanes PCI   
Memory | 4 |  | 4x8 = 32GB DDR 4 1330 MHz   
System Drive | 1 | Samsung | NVMe Samsung SSD 970   
Media Drive | 1 | Samsung | 860 Pro 512 - SSD - SATA III   
Graphics Card | 2 | Nvidia | Quadro P4000   
NIC | 2 | Intel | X550 - Ethernet 802.3   
  
##### Coco2 System Config: Price ~ 2500

Part Type | QTY | Brand | Model   
---|---|---|---  
Motherboard | 1 | Asus ROG Maximus | XI Hero (WIFI)   
CPU | 1 | Intel | 8700K (Coffee Lake) - 6 cores - 12 threads - 3.7 / 4.7 GHz - 16 Lanes PCI   
Memory | 1 | Corsair |   
System Drive | 1 | Gammix | NVMe 512 - S5 Read 2100MB/s Write 1500 MB/s   
Media Drive | 1 | Western Digital | WDC WDS240G2G0A-00JH30 - 512 MB - SATA   
Graphics Card | 2 | Nvidia | Quadro P4000   
NIC | 1 | Asus | ASUS XG-C100C 10G PCI-E - Aquantic650 - Ethernet 802.3   
  
##### Synthetic Test Results

| Coco1 | Coco2-1 | Coco2-2   
---|---|---|---  
Unigine SuperPosition Direct X 1920x1080 Extreme | 3070 | 2936 | 3000   
Unigine SuperPosition OpenGL 4K Optimized | 4193 | 3973 | 4016   
Unigine SuperPosition OpenGL 8K Optimized | 1718 | 1637 | 1665   
Cinebench | 3292 | 3375 | 3291   
  
Examining the table above shows that pushing the GPU does not mean you are utilizing or require more than 8 lanes of PCI. All the numbers are very close which means having dual graphics cards running on only 8 lanes of PCI each can be a good way to generate value for real-world applications when compared with a more expensive motherboard and CPU supporting what amounts to simply more PCI lanes with the same GPU and CPU power. 

## Intel Core

The Intel Core line of processors are the most widely used processor for building TouchDesigner development rigs. These are the most versatile chips for gaming, computer graphics design, programming and ideal for audio visual systems. 

### Core Generation

Within the Intel Core product line there is a notion of generation. The Core processor has been around for many years, and therefore has passed through many generations and microarchitectures. All generations of Core processors work well with TouchDesigner. Subsequent generations come with a range of modifications that affect TouchDesigner performance. There are a litany of feature shuffles and architecture modifications that might go into a new generation. 

<https://www.anandtech.com/show/13400/intel-9th-gen-core-i9-9900k-i7-9700k-i5-9600k-review>

Intel's Core Architecture Cadence  Core Generation | Microarchitecture | Process Node | Release Year   
---|---|---|---  
2nd | Sandy Bridge | 32nm | 2011   
3rd | Ivy Bridge | 22nm | 2012   
4th | Haswell | 22nm | 2013   
5th | Broadwell | 14nm | 2014   
6th | Skylake | 14nm | 2015   
7th | Kaby Lake | 14nm+ | 2016   
8th | Kaby Lake-R | 14nm+ | 2017   
| Coffee Lake-S | 14nm++ | 2017-2018   
| Kaby Lake-G | 14nm+ | 2018   
| Coffee Lake-U/H | 14nm++ | 2018   
| Whiskey Lake-U | 14nm++ | 2018   
| Amber Lake-Y | 14nm+ | 2018   
| Cannon Lake-U | 10nm | 2017*   
9th | Coffee Lake Refresh | 14nm** | 2018   
Unknown | Ice Lake (Consumer) | 10nm? | 2019?   
| Cascade Lake (Server) | 14nm** | 2018   
| Cooper Lake (Server) | 14nm** | 2019   
| Ice Lake (Server) | 10nm | 2020   
* Single CPU For Revenue |  |  |   
** Intel '14nm Class' |  |  |   
  
### Hyper-Threading

Hyper-Threading is a technology that provides scheduling of CPU cycles for sharing a single core more efficiently between two seperate threads. Hyper-Threading has been around for many years so the majority of usage of TouchDesigner over the last 10 years has been done on CPUs with support for Hyper-Threading. Intel has produced a range of modern 9th generation processors with no Hyper-Threading so it’s worth taking note of the difference. 

Because TouchDesigner runs on a single thread, there will be no performance hit for the main TouchDesigner application on CPUs that don’t support Hyper-Threading. When looking at processor specs, if the number of threads is 2x the number of cores, the processor supports Hyper-Threading. If the number of cores matches the number of threads it does not. 

### Turbo Boost

Turbo Boost is a feature that will automatically raise the processor operating frequency when demanding applications like TouchDesigner are running. However this feature will only burst at the higher frequency for a limited period of time so both the base clock and turbo clock frequency are important considerations. Turbo boost allows the CPU core to run at a more energy efficient and cooler temperature when it isn't under demand. When TouchDesigner is running the Intel processor will generally boost up to it’s higher supported clock frequency. 

The base clock is the guarenteed base speed for the specified CPU. Operating temperature and cooling can impact what the sustained operating frequency is for a particular configuration. 

CPU-z allows for monitoring each core’s operating frequency. Download for free here… 

<https://www.cpuid.com/softwares/cpu-z.html>

When looking at processor specs, if the processor has a Base Frequency and Max Turbo Frequency then the processor supports Turbo Boost. If there is only a Base Frequency then it does not. 

### Memory

CPU and motherboard will generally determine what memory must be used. It’s generally recommended to purchase the fastest memory supported by the CPU. 

When building a desktop, aside from the Graphics Card (GPU), the CPU is generally the first choice. Once a CPU has been selected you may refer to the motherboard section of this document. With a motherboard selected you can refer to the motherboard specification or the motherboard's qualified vendors list (QVL) to choose the right memory. 

### Intel Integrated Graphics

Many CPUs from Intel come with a built-in GPU. These GPUs will often work with TouchDesigner but they are much lower power than Nvidia GPUs and likely not appropriate for demanding TouchDesigner video server applications. However they can likely play back simple video streams and perform other simple tasks which make embedded Intel GPUs candidates for light use cases. 

The HDMI ports built-in to the motherboards main IO backpanel will run on the Intel GPUs. Be careful to check the Motherboard specs when decding if you are interested in using these ports now or down the road. HDMI 1.4 will only support 4K @ 30hz, whereas HDMI 2.0 will support 4K @ 60Hz and higher. The displayport will generally support 4K @ 60Hz. 

## Core Families

### Core-i3

The Core i3 processor is the budget line for the Core family and over most of the last decade have only supported 2 cores. However with the release of the 8th and 9th generation, 4 core models are now available. These processors are inexpensive and are well equipped with respectable clock speeds. These value processors are certainly candidates for low power, small form-factor basic video server / kiosk type applications. 

Note the i3 family does not support Hyper Threading or Turbo Boost. This means these CPUs are locked to a single operating frequency, and you must have enough cores to run TouchDesigner as well as the operating system and other tasks. For value based applications it is still recommended that a minimum of 4 cores be available, especially if there is any video decoding. 

As well the maximum number of PCI Express lanes is 16 so you will be limited to a single high powered GPU or only a couple of 8x PCI boards. 

As an example, the i3-8350K processor supports 4 cores with an operating frequency of 4Ghz. This CPU will likely yield respectable TouchDesigner performance with enough cores to manage other parallel threads like video decoding or secondary audio processes etc. The price lists well under $200 USD and is therefore certainly worth a look. 

### Core-i5

For TouchDesigner system builders, the i5 has certainly taken a back seat to the supreme i7 family. However in the last few generations the i5 has been endowed with extremely attractive core counts and higher clock speeds. Often the i5 of a newer generation has comparable power to the same category i7 from the previous generation. Now that we are entering the 9th generation, there are a wide array of very strong i5 processors for creating TouchDesigner based servers. 

If the video server application is clearly defined and for example, a 6 core CPU with no hyperthreading will support the required video decoding and other requirements. If so, then an 8th generation Intel® Core™ i5-8600K will be a fine option listing well under $300. 

Most i5 processors support Turbo Boost while most do not support Hyper-Threading. Like the i3, the maximum number of PCI Express lanes is limited to 16 lanes. 

The 8th generation onwards i5 processor is a very capable processor for a wide array of video server applications. The main limiting factor for this category will be the number of cores and for most processors, a lack of Hyper-Threading. If 6 cores alone are enough there are savings to be had here. 

### Core-i7

The i7 CPU has been the standard CPU choice for most TouchDesigner applications. Most i7 processors support Hyper-Threading, Turbo Boost and overclocking. With the 9th generation i7 top clocks speeds are crossing the 4Ghz ceiling, along with larger cache sizes, but in some cases they have also lost Hyperthreading. 

The i7 processor is certainly the ideal processor for TouchDesigner workstations, as well as most video serving use cases that do not require a large number of PCI Express lanes. 

The entire line of i7 (non X-Series) processors max out at 16 lanes of PCI express on the chip. 

Generally the i7 and now i9 in the same generation will support the highest clock speeds and most number of cores. You will be paying the premium price to get access to the maximum performance available today - reflected in the i7 and i9 Series. Unlike the i3, the i5, i7 and i9 generally support overclocking. 

### Core-i9

There is nothing architectural that can clearly differentiate an i9 from it’s i7 predecessor. Both are based on the same Skylake microarchitecture. The i9 family will be getting the higher core counts while the i7 Series will likely max out at 8 cores with the i7-7820x. As well, the i9 in a few cases will end up with a few more PCI Express lanes in some cases, and certainly higher clock speeds. However there is currently a tendency for 9th generation i7 processors not to support Hyper-Threading, so this is another feature to be on the lookout for when going through the specs. 

### Core-X

[![Core X processors.png](./images/thumb/f/f0/Core_X_processors.png/300px-Core_X_processors.png)](</File:Core_X_processors.png>)

[](</File:Core_X_processors.png> "Enlarge")

**These processors are great for general purpose TouchDesigner applications.**

The X series of processors actually span the i5, i7 and i9 families. With every generation, there are X series processors that are equipped with features that generally put these processors at the top of the market in performance. When using ark.intel.com, the Core CPUs with the greatest numbers of cores, highest clock speeds and advanced features like larger caches can be found in the Core X-series section. You might also find them missing from the generic sections if you are looking for processor by product code. 

These prosumer level processors are designed for demanding applications like TouchDesigner and therefore have more cores, higher clock speeds, larger memory caches and in some cases many more lanes of PCIe. 

All X-series processors do not have on-chip Intel GPUs, which will not be missed by anyone building a TouchDesigner server with a graphics card. These processors always support Hyper-Threading and Turbo Boost. 

For those building single CPU high demand, high resolution TouchDesigner servers, you should be looking here for the top of the line, state of the art CPUs. Any processor in this category will perform well if it meets the performance requirements and works in the budget. 

## Intel Xeon

The Xeon processor is designed for servers and high performance workstations. Over the past 10 years the Xeon processor platform was widely used by TouchDesigner system builders to provide the maximum number of cores and greatest number of PCI Lanes, for scenarios that required systems to run round the clock for long periods of time, often measured in years. 

The Xeon processor in also designed to work with multiple processors per board. All Core processors will only work with a single CPU per motherboard. From the perspective of a TouchDesigner server, the total number of cores is the most important factor when choosing between Xeon and for example a top of the line Core X processor with comparable max clock speeds. If a use case requires more CPU cores than are physically required on a single Core CPU, the choice of Xeon may be forced. 

In the last year with the Core i9 X processor line, the per CPU core count has skyrocketed up to 18 physical cores from a maximum of only 8 cores in 2017. This is a game changer for TouchDesigner servers that require high clock speeds and maximum core counts, and therefore makes the need for a fresh comparison between Xeon and Core evermore relevant. 

Let’s first look at the features the Xeon series has over the Core X family before doing a direct comparison. 

### Multiprocessor Support

A big advantage with Xeon is support for multiple CPUs per motherboard. (excluding some like the E3 family - check individual specs to be sure) 

### Higher PCI Express Lane Counts

Xeon processors typically support a higher number of PCI-Express lanes for supporting things like Hardware Raid Controllers, Video IO cards, and other expansion boards. 

### Support for ECC RAM

Error correcting code memory, or ECC memory, automatically detects and repairs single-bit errors on-the-fly to keep workstation applications running reliably and free of data corruption. ECC RAM is an important feature for high demand, mission critical media server sceneios with TouchDesigner. 

### No Overclocking

Many i5 and most i7 processors are designed to be overclocked. Xeons can not be. 

### L3 cache

The CPU cache holds recently retrieved data in memory in case it is required again. For many data searching use cases this can enhance performance greatly. Most TouchDesigner applications will benefit little from an extremely large level 3 cache, though this extra cache is one reason why Xeon’s can be so much faster at high demand applications than i7. 

### Endurance - Up Time

Xeon processors are qualified to handle heavier, more intensive loads day in and day out. For the serious workstation user, this can translate to better longevity over i7 counterparts. If the TouchDesigner server use case requires the system to run for 5+ years in an always on state, then it might be worth considering a Xeon CPU for this reason alone. 

### Hyper-Threading

Most if not all Xeon CPUs support Hyper-Threading. However all Core-X series processors do as well. 

### Xeon Families and Model Numbers

As of Q4 2018, Intel has a newly re-branded set of Xeon processors under the Scalable moniker. The best way to isolate the right Xeon processor, is to use the the ARK webpage and sort by “Max Turbo Frequency” column. Once you have isolated the CPU with the highest clock speeds you can work backwards to find the right number of cores etc. 

<https://ark.intel.com/products/series/125191/Intel-Xeon-Scalable-Processors>

For more details on this product line read this article from Thinkmate.com. 

<https://www.thinkmate.com/inside/articles/intel-xeon-scalable>

### Core vs Xeon

The choice between Core and Xeon is hopefully now more straight forward. If you get enough PCI lanes from a single CPU in the Core X line, then it’s probably the best way to go. If you need many more lanes than available on any single Core processor then you will be forced to go with a Xeon dual CPU ( or more ) configuration. And if you are worried about crashing, then you need ECC memory and therefore Xeon.
