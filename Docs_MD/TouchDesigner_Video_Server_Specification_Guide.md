# TouchDesigner Video Server Specification Guide

## Suggested Operating System

Windows 10/11 is the suggested windows operating system. 

## Processor
* For more detail go here: [Intel Processors and TouchDesigner](<./Intel_Processors_and_TouchDesigner.md> "Intel Processors and TouchDesigner")
  * Derivative recommends Intel processors.
  * We have successfully built desktop general use TouchDesigner systems (non pro video servers) using AMD Ryzen 7. These are great processors for TD with tremendous value - <https://www.amd.com/en/products/cpu/amd-ryzen-7-2700x>
  * We don't have experience with AMD Threadripper CPUs but we expect they work well. <https://www.amd.com/en/products/ryzen-threadripper>
  * The main TouchDesigner thread runs on a single core. Pick the highest clock speed available for your CPU class and price range.
  * Pick a CPU with enough lanes to support the specified PCIe expansion boards.
  * If you are getting a single CPU get a CORE CPU.
  * If you are getting more than one CPU you must go with XEON.

## Memory
* Consult your CPU and motherboard specs to choose the fastest memory available.

## Graphics Card
* For more detail go here: [Nvidia Geforce vs Quadro](<./Nvidia_Geforce_vs_Quadro.md> "Nvidia Geforce vs Quadro")
  * Derivative recommends Nvidia Graphics cards.
  * If you are playing back large format video directly from the graphics card use Quadro.
  * If you are playing video using SDI Expansion boards use Quadro.
  * If you are looking for good value on a personal workstation for TouchDesigner development use Geforce cards.

## Motherboard
* Ensure the motherboard supports the correct slot type for the chosen CPU(s).
  * Ensure there are enough PCIe slots of the correct bandwidth to support your video card(s).
  * Ensure the graphics cards are installed in the correct slots according to the motherboard manual.
  * Be aware of how many PCI Lanes are supported by the CPU and Motherboard.
  * NVMe drives often eat PCI Lanes and may effect motherboard lane availability when installed.

## Hard Drive
* For more detail go here: [Storage Technology and TouchDesigner](<./Storage_Technology_and_TouchDesigner.md> "Storage Technology and TouchDesigner")
  * This article by Thinkmate is a must read. <https://www.thinkmate.com/inside/articles/nvme>
  * Tom's Hardware has good coverage of NVMe technology. <https://www.tomshardware.com/reviews/intel-750-series-ssd,4096-2.html>
  * Use motherboard embedded M.2 slots with NVMe Drive for OS when possible.
  * Use NVMe technology over SATA or SAS where-ever possible.
  * Use NVMe RAID Controller Cards for larger drives at higher speeds.

## Codec Stats

The following section covers testing stats for video codecs. These tables will aid in calculating the speed and size of hard drives required to playback video in TouchDesigner. 

### Testing Platform

The following computer specification is the Derivative video server testing platform. Most of the codec and SDI playback research and analysis was performed using this system. 

<https://www.supermicro.com/products/system/1U/1028/SYS-1028U-TRT_.cfm>
* Supermicro Ultra SuperServer 1028U-TRT+ - 1U
  * Supermicro X10DRU-i+ motherboard
  * 2 x Six-Core Intel Xeon Processor E5-2643 v4 3.40GHz 20MB Cache (135W).
  * 8 x 4GB PC4-17000 2133 MHz DDR4 ECC Registered DIMM.
  * 128GB SATA 6.0Gb/s Disk on Module (MLC) (Vertical). (DOM)
  * 7 x 480GB Samsung PM863 Series 2.5 SATA 6.0Gb/s Solid State Drive.
  * Supermicro AOC-S3008L-L8i SAS 3.0 12Gb/s 8-Port Host Bus Adapter
  * SDI In/Out - AJA Corvid 88
  * 10x SATA - Dual 10-Gigabit Ethernet (RJ45)
  * 750W Redundant.

### HAPQ Codec Performance Stats

The HAPQ Codec is a codec that balances quality with performance. Instead of using the CPU to decode the image data, the HAPQ format is readily consumed and decompressed directly by the GPU. HAPQ supports both RGB and RGBA image formats. The testing platform has a drive array that supports a data read rate of 3,300 MB/s. 

Resolution | Format | FPS | MB/s | Max Streams | CPU% @ Max | GPU% @ Max | MB/s @ Max | Terabyte Per Hour   
---|---|---|---|---|---|---|---|---  
1920x1080 | RGB | 30 | 59 | 56 | 20% | 52% | 3,300 | 0.2124   
1920x1080 | RGBA | 30 | 87 | 40 | 20% | 50% | 3,300 | 0.3132   
1920x1080 | RGB | 60 | 118 | 28 | 20% | 53% | 3,300 | 0.4248   
1920x1080 | RGBA | 60 | 174 | 19 | 20% | 54% | 3,300 | 0.6264   
3840x2160 | RGB | 30 | 236 | 13 | 20% | 54% | 3,300 | 0.8496   
3840x2160 | RGBA | 30 | 384 | 8 | 20% | 54% | 3,300 | 1.3824   
3840x2160 | RGB | 60 | 500 | 7 | 26% | 54% | 3,500 | 1.8   
3840x2160 | RGBA | 60 | 696 | 4 | 20% | 54% | 3,300 | 2.5056   
  
### NotchLC Comparison Codec Performance Stats for 60FPS

NotchLC is a high quality codec that utilizes the GPU. While it requires more CPU and GPU resources than HAPQ, it's optimal compression setting is higher quality to HAPQ and argueably as good or better than Apple ProRes. 

The most clear conclusion we can draw from the NotchLC testing is that you will most likely not be able to saturate a high speed drive configuration as well as HAPQ can. Our HAPQ testing yeilds a playback breaking point that is very close to our testing platform's 3500 MB/s limit. NotchLC tends to start dropping frames well before the harddrive bandwidth capacity is reached suggesting the limiting factor is more CPU limitations. 

<https://notchlc.notch.one/>

Resolution | Format | FPS | MB/s | Max Streams | CPU% @ Max | GPU% @ Max | MB/s @ Max | Terabyte Per Hour   
---|---|---|---|---|---|---|---|---  
3840x2160 | RGB | 60 | 340 | 5 | 45% | 42% | 1,700 | 1.2124   
3840x2160 | RGBA | 60 | 395 | 5 | 45% | 45% | 1,700 | 1.2124   
  
### What's better? HAPQ or HotchLC

Both HAPQ and NotchLC are powerful codecs for playback and recoding high resolution real-time content. HAPQ is a constant bitrate codec that will generate the same file size independent of pixel content. The data is stored in a format that is immediately readable by the GPU so it uses very little CPU or GPU resource to decode. HAPQ is an 8bit codec and compression quality is good but depending on the content, you will see artifacts like banding in soft gradients. NotchLC is a pseudo 10bit Codec so it holds more color information. The NotchLC optimal setting yeilds very high quality file that can be used as an intermediate format for further processing and editing in a traditional visual effects or video production pipeline. NotchLC compression is variable based on the pixel content. The more noisey the content the less it will compress and therefore will yield larger file sizes. A standard live action video file in HAPQ with no secondary compression is approximately 5% smaller than NotchLC. The same file in HAQ with secondary compression is approximately 15% smaller. 

The main conclusion to draw from this comparison is that both codecs will require a similar harddrive configuration. Therefore design the harddrive configuration based on HAPQ requirements and the NotchLC playback and recording will be very happy on the same system. 

As mentioned earlier, NotchLC is more demanding on CPU and GPU, therefore higher clock speeds and more cores for the processors will increase bandwidth assuming the harddrive configuration has more headroom. A faster GPU is also a positive factor when considering NotchLC and HAPQ. 

### 4K Comparison Codec Performance Stats for 60FPS

The “CPU%” and “MB/s” columns represent the CPU utilization and storage read bandwidth required for a single stream of video. The “CPU% @ Max” and “MB/s @ Max” represent the utilization of the same resources when running the maximum number of streams without dropping from the required frame rate of 60FPS. This table gives an impression of the difference between supported codecs. 

Resolution | Codec | Bit Rate | Format | File Size Bytes | CPU% | MB/s | Max Streams | CPU% @ Max | MB/s @ Max | Terabyte Per Hour   
---|---|---|---|---|---|---|---|---|---|---  
4096x2160 | H264 | 8bit | RGB | 211,787 | 11.00% | 6 | 4 | 56.00% | 23 | 0.04   
4096x2160 | H265 | 8bit | RGB | 87,573 | 13.00% | 5 | 1 | 12% | 5 | 0.02   
4096x2160 | Cineform | 10bit | YUV | 881,805 | 9.00% | 48 | 3 | 50.00% | 150 | 0.18   
4096x2160 | Cineform | 12bit | RGBA | 2,008,283 | 18.00% | 70 | NA | NA | NA | 0.4   
4096x2160 | Animation | 8bit | RGB | 624,611 | 5.00% | 140 | NA | NA | NA | 0.12   
4096x2160 | HAPQ | 8bit | RGB | 9,331,214 | 2.00% | 515 | 6 | 14.00% | 3,000 | 1.87   
4096x2160 | HAPQ | 8bit | RGB | 3,889,233 | 5.00% | 215 | 6 | 42.00% | 1,300 | 0.78   
4096x2160 | HAPQA | 8bit | RGBA | 13,996,827 | 2.00% | 770 | 4 | 8.00% | 3,000 | 2.8   
4096x2160 | HAPQA | 8bit | RGBA | 4,118,246 | 5.00% | 230 | 5 | 37.00% | 1,100 | 0.82   
3840x2160 | HAPQ | 8bit | RGB | 34,992,052 | 2.00% | 475 | 7 | 17.00% | 3,300 | 1.75   
  
## Supported Video Data Input / Output Technology (SDI etc)

TouchDesigner supports the latest cards from the following manufacturers. 
* [AJA](<./AJA.md> "AJA") \- <https://www.aja.com/>
  * AJA Kona line is well tested - <https://www.aja.com/family/desktop-io>
  * AJA Corvid 88 is part of our video server testing platform - <https://www.aja.com/family/developer>
  * [Blackmagic Design](<./Blackmagic_Design.md> "Blackmagic Design") \- <https://www.blackmagicdesign.com/>
  * Blackmagic Decklink 8K Pro is well tested - <https://www.blackmagicdesign.com/products/decklink>
  * [Bluefish444](<./Bluefish444.md> "Bluefish444") \- <https://bluefish444.com/>
  * Datapath - <https://www.datapath.co.uk/>

## Supported IP Audio and Video Technology

TouchDesigner supports the follow IP based technologies for sending audio and video over networks. 
* [Dante](<./Dante.md> "Dante") \- <https://www.audinate.com/>
  * [NDI](<./NDI.md> "NDI") \- <https://www.newtek.com/ndi/>

## Recommended Product Links
* The Intel Ark website is a one stop shop for specifications covering the entire line of prodcuts made by Intel. <https://ark.intel.com/content/www/us/en/ark.html>
  * Nvidia Geforce for non professional / desktop / laptop GPUs. <https://www.nvidia.com/en-us/geforce/>
  * For professional video playback and SDI solutions we recommend Quadro. <https://www.nvidia.com/en-us/design-visualization/quadro/>
  * Supermicro Servers and Workstation Motherboards and Cases. <https://www.supermicro.com/index_home.cfm>
  * Thinkmate complete GPU based / NVMe server architectures. They built our testing platform and offer professional system design guidance. <https://www.thinkmate.com/>
  * For enterprise solutions / permanent installations we recommend HP. <https://www8.hp.com/us/en/workstations/overview.html>
