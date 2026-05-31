# NDI Performance Testing

NDI is networking protocol that has quickly gained prominance in the video distribution and playback world. This document covers a session of NDI performance testing that occured in Oct 2019 which was conducted at Cocolabs Mexico with Derivative. The goal of the testing was to attempt to uncover maximum throughput of various computers and networking technologies and to address any issues with other networking technologies like the Dante audio protocol.   
  
For working with NDI and Dante over the same network infrastructure see Using Dante with NDI on the [Dante](<./Dante.md> "Dante") page. 

## Testing Platforms

##### Cocolabs - Coco1 - Price ~3500

Motherboard | 1 | Asus | WS C422 SAGE / 10G   
---|---|---|---  
CPU | 1 | Intel | Xeon W 2135 - (Skylake) - 6 cores - 12 threads - 3.7/4.5Ghz - 48 Lanes PCI   
Memory | 4 | Unknown | 4x8 = 32GB DDR 4 1330 MHz   
System Drive | 1 | Samsung | NVMe Samsung SSD 970   
Media Drive | 1 | Samsung | 860 Pro 512 - SSD - SATA III   
Graphics Card | 2 | Nvidia | Quadro P4000   
NIC | 2 | Intel | X550 - Ethernet 802.3   
  
## Network Technologies

The brands of network technologies used in this testing are as follows. 

Derivative LA Buffalo BS-MP2008 - 8 ports 

<https://www.buffalo-technology.com/productpage/switch-bs-mp2008/>

Derivative LA CISCO SYSTEMS Sg350-10P 10-Port Gigabit 

<https://www.cisco.com/c/en/us/support/switches/sg350-10p-10-port-gigabit-poe-managed-switch/model.html>

Cocolab NetGear XS716T - Smart Managed Pro Switch 16 ports. 

<https://www.netgear.com/business/products/switches/smart/XS716T.aspx#tab-overview>

Coco2 PCI Expansion Card - Expansion card for Coco1 Server ASUS XG-C100C 

<https://www.asus.com/us/Networking/XG-C100C/> <https://www.anandtech.com/show/11598/asus-launches-xgc100c-10-gbe-adapter-aquantia-aqc107-99>

Dante Hardware Focusite Pro - RedNet X2P Dante Master Clock / Audio Monitoring System / Analog I/O 

<https://pro.focusrite.com/category/audiooverip/item/rednet-x2p>

### Important Switch and NIC Configurations
* Ensure both sending and receiving hard drives are faster than 1.3 GB/s sustained read and write.
  * Ensure NICs are 10Gbe and that they are installed in the correct PCI Slot if they are expansion cards.
  * Generally this requires the slot supports x4.
  * Ensure computer Chipset and NIC drivers are up-to-date with the latest drivers. The latest drivers are often not found on the “brand” or “manufacturer” websites. For example to find the ASUS XG-C100C drivers you must go to the chip maker website located here <https://driverdownloads.aquantia.com/> and search for the Part Number AQC107 / choose OS etc.

## 10Gbe Network Switch Testing

Before embarking on testing network bandwith using NDI it was first important to establish how much a single 10 Gbe switch can be saturated with video data. What is the maximum load possible on the switch using standard benchmarks? Following this real-world test were performed. 

### Synthetic Test (Crystal Mark)

For all NICS and switches in the testing platform it was possible completely or very closely saturate the full 10 Gb/s ( 1.25GB/s ). To do this a hard drive that supports over 1.3 GB/s is required for both the sender and receiver. 

### Testing Network Bandwidth

The following simple test has proven itself reliable and easy to execute. It provides clear statistics and gave consistent results for determining the performance of switch settings and features. Therefore we recommend using CrystalDiskMark with the default settings for comparing your own analysis of your own network and computer hardware performance. 

<https://crystalmark.info/en/software/crystaldiskmark/>

Crystal Disk Mark can be used to test network bandwidth by performing a standard drive test using a shared network location that is on a drive supporting sustained read / write speeds above 1300 MB/s. 

The following section outlines how this benchmark was obtained. Two computers are required. One computer is a system with a fast hard drive. The second computer is a system that can access the fast hard drive through the Windows network either as a mounted drive or as a shared location. 

In our tests at Derivative, the computer with the fastest drive is the video server testing platform named Galactus. To prepare for running the test CrystalDiskMark was installed on both the server and the secondary network computer which in our case is named Jupiter. The fast drive is shared on the network. All other NICs are disabled on both computers. 

Crystal Mark running local on Galactus shows the performance of the D video drive (7 disk SATA Raid 0 array running on a 12Gb/s SAS PCI expansion card). We can see the read/write performance for the first row test is 3633/3217 MB/s which is well above the maximum network switch bandwidth of 10 Gb/s or 1250 MB/s. 

Next the same test is performed on the same drive but running the test on another computer on the same 10G network. Use the Select Folder drop down menu to access a valid network location. 

As we can see the network-based benchmark scores much lower across all tests, with the first row test showing a read/write speed of 1185/1025. 

One of the first goals was to ensure the network switch and NIC cards were operating at their greatest capacities. There can be a wide array of factors that might contribute to suboptimal performance from a network switch. With this easy to use network-based benchmark setup, it can be straightforward to test network NIC and switch settings. The next few sections will take you through some important features to keep an eye on when setting up an Audio Video network. 

### MTU Size - Jumbo Frames / Jumbo Packets

MTU stands for maximum transmission unit, which is the size of the largest protocol data unit (PDU) that can be communicated in a single network layer transaction. 

<https://en.wikipedia.org/wiki/Maximum_transmission_unit>

Most managed switches and higher quality NIC cards will support a setting that will increase the MTU such that more data can be sent with less individual packets. This setting is generally referred to as Jumbo Frames or Jumbo Packets. 

To configure a NIC card use the NIC Properties dialog and click the “Configure…” button. (Control Panel > Network & Internet > Ethernet > Change Adapter Options > Ethernet Adaptor > Properties > Configure > Advanced) 

In the configuration dialog use the Advanced page to access the customizable settings. Every NIC Adaptor Advanced page configuration will be slightly different. Generally NICs will have Jumbo Packets disabled. 

If Jumbo Packets are to be used to increase network performance it is important that all NICs on the same network can work with the specified packet size. As well the maximum size must be supported by the network switch. 

A quick search for “Jumbo” in the switch manual for the BS-MP2008 yields the following. 

So we can see the NIC supports a maximum of 16348 bytes while the switch supports a maximum of only 9216 bytes. (The manual for the switch does say 9216 frames but that is a translation error.) 

Therefore the maximum setting for the NIC should be 9014 Bytes, while the setting for Jumbo Frames has to be activated using the switch configuration tool. Every switch is different so you will have to consult your switch documentation to explore the configuration options available. 

The Buffalo BS-MP2008 switch has a simple configuration panel that can be accessed using a web browser. 

Results are summarized in the following chart. We can see that in our synthetic test Jumbo Frames yields a significant boost in performance. 

Test | Jumbo Off | Jumbo On | % Difference   
---|---|---|---  
Read |  |  |   
Sequential Read 1MiB (Q= 8, T= 1) | 1185.64 | 1238.39 | 4.35%   
Sequential Read 1MiB (Q= 1, T= 1) | 400.19 | 662.63 | 49.39%   
Random Read 4KiB (Q= 32, T=16) | 680.46 | 944.95 | 32.54%   
Random Read 4KiB (Q= 1, T= 1) | 6.71 | 7.24 | 7.60%   
Write |  |  |   
Sequential Write 1MiB (Q= 8, T= 1) | 1024.41 | 1233.87 | 18.55%   
Sequential Write 1MiB (Q= 1, T= 1) | 467.04 | 581.38 | 21.81%   
Random Write 4KiB (Q= 32, T=16) | 502.32 | 933.02 | 60.01%   
Random Write 4KiB (Q= 1, T= 1) | 6.47 | 7.46 | 14.21%   
  
In addition to the increase in performance, activating Jumbo Frames gets a highest scoring Test1 1MiB(Q=8, T=1) which is much closer to the theoretical maximum for that test which should be around 1250 MB/s or 10,000 Gb/s. 

#### IEEE 802.3az

IEEE 802.3az is a networking standard for reducing power consumption during low network activity. The Dante documentation suggests that this setting be disabled in the network switch management panel. 

<https://www.audinate.com/sites/default/files/PDF/dante-network-blacklisted-eee-switches-audinate.pdf>

We can see this feature is available for deactivation in the Buffalo switch configuration tool and most managed switches will provide this setting. It will be on by default most likely. 

Once this setting has been deactivated we can simply perform another test. The results are summarized in the following chart and we can see the difference is small enough to indicate the setting has an insignificant impact on this kind of test. 

IEEE 802.3az Off On - Jumbo On |  |  |   
---|---|---|---  
Test | IEEE Off | IEEE On | % Difference   
Read |  |  |   
Sequential Read 1MiB (Q= 8, T= 1) | 1238.39 | 1238.39 | 0.00%   
Sequential Read 1MiB (Q= 1, T= 1) | 662.6 | 656.35 | -0.95%   
Random Read 4KiB (Q= 32, T=16) | 944.9 | 872.9 | -7.92%   
Random Read 4KiB (Q= 1, T= 1) | 7.24 | 7.39 | 2.05%   
Write |  |  |   
Sequential Write 1MiB (Q= 8, T= 1) | 1233.87 | 1185.5 | 0.06%   
Sequential Write 1MiB (Q= 1, T= 1) | 399.48 | 416.29 | 4.12%   
Random Write 4KiB (Q= 32, T=16) | 691.64 | 696.15 | 0.65%   
Random Write 4KiB (Q= 1, T= 1) | 6.87 | 6.82 | -0.73%   
IEEE 802.3az Off On - Jumbo Off |  |  |   
---|---|---|---  
Test | IEEE Off | IEEE On | % Difference   
Read |  |  |   
Sequential Read 1MiB (Q= 8, T= 1) | 1184.84 | 1185.5 | 0.06   
Sequential Read 1MiB (Q= 1, T= 1) | 399.48 | 416.2 | 4.12%   
Random Read 4KiB (Q= 32, T=16) | 691.64 | 696.15 | 0.65%   
Random Read 4KiB (Q= 1, T= 1) | 6.87 | 6.82 | -0.73%   
Write |  |  |   
Sequential Write 1MiB (Q= 8, T= 1) | 1036.15 | 1053.26 | 1.64%   
Sequential Write 1MiB (Q= 1, T= 1) | 466.41 | 468.48 | 0.44%   
Random Write 4KiB (Q= 32, T=16) | 557.08 | 536.2 | -3.82%   
Random Write 4KiB (Q= 1, T= 1) | 6.51 | 6.46 | -0.77%   
  
#### Final Remarks on Testing Network Features

This was the most expedient method we found to test, retest, and double check system / network performance against our real-world tests. We encourage others to try the same thing and compare your results with ours. 

## NDI Testing

To date we have conducted NDI 3.8 and NDI 4.1 testing. The testing was quite exhaustive, at times confusing and along the way we have found a variety of issues, some of which have been resolved while others are still outstanding. 

### Performance Evaluation

When discussing performance we are mainly focused on how the playback is “looking”. We still have no digital metric to measure how many frames we have received or dropped or missed etc. The only way to test was to visually watch the signal on the sender and receiver and judge playback rate by watching for dropped frames using a “White Line Test”. 

#### What is a White Line Test?

A “White Line Test” is a method for using human eyes to evaluate playback quality. With a vertical line scanning back and forth - from left to right with linear motion it is easy for the eye to catch even a single frame drop or any other artifact like a horizontal tear from an out of sync scanline. 

### NDI Testing Results and Analysis

Reading the following charts we can look at the CPU, GPU and Network load for each new stream that is sent. Row 0 starts with the sender running a TouchDesigner file that is streaming a single HAPQ movie off disk and passing through a “White Line Test” component. No NDI stream is active and so this establishes the baseline loads. 

The windows task manager is used to measure the maximum CPU / GPU / Network load value over the span of approximately 1 minute. This is completed by watching the graphs of the task manager while also paying attention to the white line playback. 

The frame drops values are determined using a best guess based on the tester’s experience looking at video that drops frames. Anything above 1-2 drops every 2 seconds would be considered unacceptable for many cases though certainly acceptable for others. For the sake of clarity we will assume any frequent frame dropping is a failure when compared with a properly configured Displayport or SDI video feed, as the attempt in this test is to achieve flawless playback. 

All this testing is performed with a single video file called Flares.mov. This file was selected from a set of 6 videos generated by the Cocolab design team to represent the type of content they will generate for their real-world use cases. This particular video was selected from the 6 because it has the most “noisey” content and therefore possibly the most challenging for the NDI compression engine. It’s worth mentioning here that it is quite easy to completely break the NDI compressor and therefore it’s important to read the “Breaking NDI Compression” section. 

Each row is another added stream and as more streams are added we can see how the CPU, GPU and network bandwidth loads up for both the Send and Receive computers. The final red row is where TouchDesigner itself starts to drop frames because the load is more than TouchDesigner can handle. 

We can see here NDI 3.8 is generally dropping a frame or two once you go above a single stream. Once you are above 3 streams the frame dropping gets to an unacceptable level. The load on the sender computer is quite minimal as you increase stream count. This is good news for those who want to centralize render power and stream signal to servers dedicated to display / projection. 

During the process of writing this paper NDI 4.0 was released and was playing back very poorly, dropping many frames per second even with a single stream. NDI 4.1 has clearly improved with regard to playback quality. We are happy to see this latest release has addressed the issue greatly. 

It’s also very clear from these stats that the load on the CPU and GPU has greatly increased. NDI 3.8 had a receiver load of CPU 25% and GPU 33% while NDI 4.1 is CPU 30% and GPU 66%. Meanwhile the network load has slightly decreased from 653 to 523 Mb/s. 

The compression visual quality has also greatly improved from 3.8 to 4.1. Please see the compression quality section for greater detail. 

### Adding More Receivers

NDI only starts sending data when a connection is made. Adding another receiver NDI TOP In that is connected to the same NDI TOP Out has the same effect on the bandwidth as a receiver connected to a different NDI Out. The bandwidth will essentially double. Adding more receivers adds a small load to the sender computer as well as increasing the sender outbound network by another full stream of bandwidth. 

## Compression Quality

NDI is essentially settingless. However it also increases the compression as the resolution increases. A higher resolution image will be compressed more. A lower resolution image looks better. In the image below a secondary crop of the same video is composited over the main 3840x2160 feed. The NDI 4.1 crop is 330x198. The compression quality is much cleaner on the cropped version. 

HAPQ generally looks much better than NDI, but it takes up a lot more bandwidth. For the compression test cases filed a single stream of 3840x2160 @60Hz takes 260 Mb/s of bandwidth using NDI while HAPQ requires roughly 6 times more at 1.8 Gb/s. 

#### Delay / Latency

On our testing platforms NDI seems to naturally sit around 10 frames behind TouchIn/Out. So there is greater latency with NDI over TouchIn and TouchOut 

### NDI Does Not Work Well With Some Content

As with any compression code beware that is can be fairly easy in TouchDesigner to create content that doesn't compress well. Things like particles, pixel shaders and things that have a lot of noise will not always compress well when compared with things like live action. The testing process was focused around a single piece of content - which was the Flares.mov file. NDI performance varies wildly depending on what kind of content is thrown at it. Included in the AV testing kit are a range of signals that can cause or atleast has caused NDI to fail - resulting in an increase in dropped frames or other artifacts like a solid green output. You should familiarize yourself with these cases and be wary of content that might push NDI into these performance bottlenecks. 

### Do Jumbo Frames Matter for NDI?

We saw no indication that having Jumbo frames either on or off made any difference in our visual playback analysis. Therefore we have no recommendation either way. 

### NDI Troubleshooting
* After changing network topology it can be useful to reboot all computers - especially the sender. It seems the mDNS gets tied up and thinks it has a connection when it really is looking at an old IP address and therefore the discovery magic doesn't seem to happen. We have seen NDI get very confused and only a reboot after checking firewall settings was all that could be done to fix it.
  * NDI will often get into a state where the receiving TOPs info reports they are connected but no video is being received. Using the NDI Monitor App yields a black image with a green and red bar at the top of the image. When in this state also when sending a test pattern from their Test Pattern app the NDI Monitor receives only black. It can see the signal in the menu but nothing comes through. When in this state the NDI streams are still detected on the receiver side even though they are no longer active on the sender side. The only way we have found to fix this state is to reboot the sender computer. Rebooting the clients doesn’t help. This generally happens when making modifications to network settings.
  * The only sure way to get a single 4K stream to play smoothly is for it to be the only stream. A second stream will often lead to dropped frames on both inputs.
