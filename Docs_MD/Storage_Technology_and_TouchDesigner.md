# Storage Technology and TouchDesigner

### Overview

Understanding storage technology can be daunting because there are a wide range of compatible and incompatible systems, some software, some hardware, some combinations of both. There are hardware interfaces, software protocols, cables and connectors, form factors, and media types. Some of the systems overlap, others are phasing out and yet others are catching on. 

Today’s storage landscape is changing quickly, and is likely an area where errors will are made when assembling choices for a media server. 

The following chart outlines the key technologies in storage for building a modern server. The scope is limited to “inside the box” so we will not cover network based NAS systems that stream data over a network or external drives that connect via USB 3 or Thunderbolt. 

From a high level, its important to have familiarity with the following technologies. 

#### Storage Technology Chart

Technology | Type | Intro Date | Prevalence | Life Cycle   
---|---|---|---|---  
HHD Magnetic | Storage Media | 1956! | Ubiquitous | Standard   
NAND | Storage Media | 1984 | Ubiquitous | Standard   
SSD | Storage Media | 1991 | Ubiquitous | Standard   
RAID | Technology | 1987 | Ubiquitous | Standard   
SATA-III | Interface / Bus | 2008 | Ubiquitous | Twilight   
PCI Express 3.0 | Bus | 2010 | Ubiquitous | Standard   
SAS | Protocol / Interface | 2010 | Enterprise / Pro | Old Standard   
mSATA | Interface | Recent | Mobile Only | Old Standard   
M.2 | Interface | Recent | Ubiquitous | New Standard   
NVMe | Protocol |  | Growing | New Standard   
U.2 | Interface |  | Growing | New Standard   
PCI Express 4.0 | Bus |  | Growing | New Standard   
  
# Storage Media

Storage media refers to the place where data is physically stored. When considering mass storage devices for a TouchDesigner server there are two broad choices. In general, server data can be stored on magnetic spinning disks or it can be stored on nonvolatile solid-state flash memory which has the ability to store data when not powered. 

A magnetic spinning disk is know as a hard-drive. Non volatile solid state flash memory is know as NAND or v-NAND. 

# Storage Media Form Factors

Today magnetic disks are generally referred to as hard-drives or HHD. Form factors are generally specified in inches, and for most TouchDesigner applications there will be only 3.5 inch drives for consideration. 

SSD media comes in an array of formats that work on a wide range of interfaces like USB, SATA, PCI boards and M.2 slots etc. SSD drives also work with both the SATA protocol and NVMe protocol. 

## HHD vs SSD

### HHD

HHD’s work with spinning platters and read-write heads that can move to any location at tremendous speeds. The speed at which the platters rotate is measured in RPMs and larger numbers usually mean faster performance. Because HHD’s are partially a physical machine there are limits to the maximum possible speeds and as such hard drive technology has plateaued in the context of how quickly data can be retrieved or stored. 

Capacities of HHD drives have grown well over 10TB and therefore HHD storage media is still very competitive for offline storage in video servers. Offline storage can contain large video files, rendered raw footage etc, cloud data images etc. 

HHD drives can be found with interfaces for both SATA and SAS interfaces. Recommended speeds start at 7200 RPMs with suggested cache sizes above 64 MBs. 

Modern HHD drives are generally fast enough to write and store H.264 or H.265 live encoded video so if you are building a video recording system, a large capacity HHD system configured in a variety of possible RAID setups might be the best option. 

### SSD

SSD storage media is the standard for modern high performance storage. An SSD (solid-state drive) is a configuration of v-NAND, form factor, flash controller, interface and protocol. The architectural configuration of the SSD controller is optimized to deliver high read and write performance for both sequential and random data requests. SSDs are sometimes referred to as flash drives or solid-state disks. 

Because SSD drives are just arrays of fast memory, the interfaces and protocols that were developed specifically for HHD technology, namely SATA and SAS protocols are now antiquated for SSD architectures. 

You can still find SSD drives configured with SATA or SAS interfaces but these are quickly becoming a thing of the past. The following section covers a range of interfaces and protocols that are available today. 

# Interfaces, Protocols, Controllers and Busses

Before the turn of the millenium, there were a range of protocols, interfaces and buses that permitted computers to connect with peripherals like printers, disk drives and scanners. One of the most widely integrated technologies was called SCSI or Small Computer System Interface. There were others like AT Attachment (ATA) and subsequently Parallel ATA or (PATA). 

By today’s standards the SCSI and ATA/PATA protocols and interfaces are outdated. The following section describes the interfaces and protocols that have been developed over the last 18+ years that were designed to overcome the limitations of these protocols while looking into recent trends to distill how each of the technologies might benefit a TouchDesigner powered server architecture. 

## RAID - Redundant Array of Independent Disks

RAID technology has been around and evolving for many decades. In a nutshell, RAID is a specification for combining multiple disks in arrays to either increase capacity, speed or redundancy or all 3 together. All three storage communication protocols covered in this document; SATA, SAS and NVMe, support RAID configurations. RAID is very big topic and if you are unfamiliar with this technology please refer to the internet. Wikipedia has very adequate coverage here… 

[https://en.wikipedia.org/wiki/RAID](<https://www.google.com/url?q=https://en.wikipedia.org/wiki/RAID&sa=D&ust=1552662376770000>)

## SATA-I, II, III

The most successful and now widely available technology that replaced the SCSI and PATA protocols is SATA or Serial ATA. SATA is actually the evolution of the PATA interface standard. Serial ATA industry compatibility specifications originate from the Serial ATA International Organization (SATA-IO). 

SATA is a computer bus interface that connects a compatible hard drive to a host bus adaptor. The host bus adaptor is usually found as a chip on the motherboard that will manage connected devices, permitting communication with the other subsystems including the CPU. 

A SATA III bus has a maximum throughput of 6 Gb/s (Gigabits) per hard drive. There is a theoretical maximum bandwidth of 600 MB/s, which in the real world ends up closer to 550 MBs maximum per drive. 

##### 8 SATA-III ports (interface) on Motherboard

SATA-III is the latest version of SATA and has already been around for over a decade. SATA-III is the most widely supported bus interface found on today’s motherboards. 

The SATA-III interface is supported by a wide range of both SSD and HHD storage media. 

##### SSD and HDD with SATA-III Interface

## AHCI Protocol ( Advanced Host Controller Interface )

AHCI is a standard and protocol. It was defined by Intel and was developed to improve how the computer operated with the SATA host controllers. 

When the SATA controller was introduced, there were various proprietary protocols that required specific drivers and suffered from a range of inadequacies. AHCI provided a single standard that is now widely adopted by motherboard manufacturers, BIOS developers and operating systems. 

Most SATA controllers can run in either “legacy mode” (also known as “IDE”) or AHCI mode. When building a TouchDesigner server where the operating system will be installed on a SATA drive, it’s important to first ensure that the BIOS has that SATA controller set to AHCI mode. 

When a SATA host controller is in AHCI mode, the controller is able to support a larger number of drive ports, supporting up to 32 devices over the legacy mode which is likely 4 devices. 

SATA + AHCI has been the industry standard for personal computer hard drive solutions for many years. When using SATA drives not configured in RAID ( RAID is explained briefly in next section ), AHCI should be used. 

For more information consult your motherboard guide for your particular BIOS configuration. 

It is highly recommended that the Operating System is installed onto an M.2 NVMe drive or similar. ACHI and SATA system disks should be avoided where possible. 

## SAS - Serial Attached SCSI

Serial Attached SCSI is an alternative protocol for moving data from storage devices to the computer. SAS is designed and maintained by the International Committee for Information Technology Standard (INCITS). 

Unlike SATA, SAS controllers are generally installed as PCIe SAS expansion boards although embedded SAS controllers can be found on enterprise server motherboards as well. 

The most widely available SAS controllers today are SAS-3 which support 12 Gbit/s and have been available since 2013. However the SAS-4 standard was completed in 2017 and is known as 24G, sporting a much faster 22.5 Gbit/s bus - something to keep an eye open for. 

Because SAS-3 controllers are faster than SATA3 they are more well suited for larger size (more drives) RAID configurations either as RAID 0 for greater speed and capacity or other configurations to support data redundancy. A SAS-3 RAID PCI board will generally support multiples of 4 drive ports. An 8 port card will be fitted with two small MiniSAS ports, with each port supporting 4 SAS lanes each, which can be attached to 4 different drives with the correct cable. 

## SAS Drives vs SATA Drives

SATA drives may be connected to SAS controllers with the correct cables. For example a RAID0 configuration of 8 SATA SSD drives would perform better, and closer to its theoretical maximum of 4400MB/s (8x 550MB/s), on a dedicated SAS-3 RAID Controller PCI expansion board than whatever might be found embedded on the motherboard for SATA ports. SATA Controllers on motherboards have much lower bandwidth with the limiting factor being the embedded Host Bus Adaptor, which does not share the superior PCI bus bandwidths. 

SAS drives require a compatible SAS controller card. SAS drives have a wide range of benefits with regard to data integrity, reliability that are beyond the scope of this document. In the context of TouchDesigner serving video, SAS drives come in both 6Gbit/s and 12Gbit/s models, and with enough drives can max out a PCI3.0 x8 bus at around 6400MB/s. 

For more information on SAS bandwidth limitations please consult this whitepaper by LSI (Broadcom). 

[12/Gb/s SAS: Busting Through the Storage Performance Bottlenecks](<https://docs.broadcom.com/docs/12353459>)

## NVM Express (NVMe)

With the popularity of SSD drives exploding it was determined that a new protocol was required to better take advantage of the maximum bandwith of NAND. SATA and even SAS impose bottlenecks that can be avoided by direct communication with the PCI bus. The new specification introduced in 2013 was called the Non-Volatile Memory Host Controller Interface or NVM Express. The express designation is an indication of where it runs - on PCIe. Instead of using the antiquated SATA controller, or slower SAS lane, the much faster PCI Express lane would be leveraged to dramatically increase the bandwidth at which data could flow from the controller to the CPU. 

As well the new NVMe specification included new ways to communicate with the arrays of NAND flash memory increasing limits on simultaneous instructions of AHCI’s maximum of 32 to a theoretical maximum of 64,000. 

Over the last few years the advancement of storage speeds running on NVMe technology have been extremely impressive. There are a variety of media and methods through which NVMe technology is delivered. A discussion of these technologies follow. 

### NVMe Interfaces and Form Factors

If you want an SSD drive you will have to decide on an interface and form factor. This section will introduce you to the options. 

##### mSATA

mSATA does not support NVMe however its worth introducing this little drive because its available for small form factor server ideas. The mSATA standard was developed to support thin notebooks and tablets. mSATA technology is limited to very small boards which don’t have room for many SSD V-NAND chips so the upper capacity for a single drive is very limited. Like SATA III, mSATA drives are also limited by the same 600 MB/s bandwidth limit. 

#### HHHL (CEM3.0) (PCI Expansion Board)

The HHHL formfactor for NVMe drives look much like any other PCI expansion board. These PCI expansion boards can be fitted with respectibly large capacities of NAND and can run at very high speeds, close to the maximum theoretical bandwidth of the PCI bus they are slotted in to. The majority of cards avaiable at the time of writing run in x4 PCI3.0 slots but x8 etc are appearing. 

Search google for "HHHL SSD Drives" for modern results. 

#### M.2

M.2 was designed to serve the same small formfactor of mSATA but overcome the capacity and speed limitations. In most cases it has already become the desired replacement for the mSATA standard because its thinner and can sustain more v-NAND chips. M.2 devices can be connected to SATA ports or directly the to PCI Express 3.0 lanes, completely circumventing the bandwidth limiting SATA protocol. 

In cases where the M.2 slot is connect the SATA controller it will have the same limitations. When the M.2 slot is connected to the PCI bus it will have access to much higher speeds and will be using the NVMe standard. Beware of the difference when purchasing and M.2 drive. Check if it is NVMe or SATA. As well check the supported MB/s which can vary greatly. 

M.2 Modules can come in longer lengths like 42, 60 and 80mm. Longer modules fit more NAND chips and therefore can support greater capacities. 

The M.2 slot is a formfactor for a slot with a hardware connection to the motherboard. It simply defines a connector and a length for device manufacturers to comply with. Motherboards have M.2 slots that work with a variety of technologies and protocols and therefore you will need to distinguish between them and read the motherboard specicifications carefully. 

Search google for "M.2 NVMe" for modern results. 

#### U.2

The U.2 interface has been developed to connect SSD drives directly the PCI Express bus. Currently each u.2 interface can work directly on a PCI 3.0 x4 bus for a theoretical maximum bandwidth of 4 GB/s per drive. The advantage of the U.2 Controller is that the port format is based on a wire connection and looks similar to the SAS Controller connector. 

This means you can connect a 2.5” SSD using a cable and place the SSD drive into hot swappable drive bays for easy access. Similar to SAS, U.2 NVMe harddrives must be connected to a U.2 Hardware RAID controller card and may be configured in RAID scenerios. 

Search google for "U.2 SDD" or "U.2 RAID Card" for modern results.
