# NDI

Newtek NDI® (Network Device Interface) is a network-based video and audio distribution protocol (video over IP on Ethernet-based LAN) developed by [NewTek](<https://www.newtek.com/>). NDI® is a registered trademark of NewTek, Inc. Detailed description of NDI and its benefits can be found on the [Official NDI page.](<http://NDI.NewTek.com/>) It can be used TouchDesigner-to-TouchDesigner or with numerous other software tools and hardware products that support NDI. 

[![NDI Logo.png](./images/3/37/NDI_Logo.png)](</File:NDI_Logo.png>)

[](</File:NDI_Logo.png> "Enlarge")

See [NDI In TOP](<./NDI_In_TOP.md> "NDI In TOP"), [NDI Out TOP](<./NDI_Out_TOP.md> "NDI Out TOP"), [NDI DAT](<./NDI_DAT.md> "NDI DAT") and [NDI Performance Testing](<./NDI_Performance_Testing.md> "NDI Performance Testing")

See also, for H.264 over IP [Video Stream In TOP](<./Video_Stream_In_TOP.md> "Video Stream In TOP"), [Video Stream Out TOP](<./Video_Stream_Out_TOP.md> "Video Stream Out TOP"), and for HAP over IP [Touch In TOP](<./Touch_In_TOP.md> "Touch In TOP") and [Touch Out TOP](<./Touch_Out_TOP.md> "Touch Out TOP"). 

Builds 2022.20000+ including 2025.Official use NDI 5.0  
Builds 2021.13790-2021.17000 use NDI version 4.6.1  
Builds 2020.24520-2021.13780 use NDI version 4.5.  
Builds 2020.20000-2020.24510 use NDI version 4.1. 

## Network

The NDI protocol automatically discovers NDI video sources using mDNS, which is a multi-cast service discovery protocol. If your NDI sources are on networks not reachable via multi-cast, you'll need to specify the IP of the source machines in the [NDI In TOPs](<./NDI_In_TOP.md> "NDI In TOP") parameters. 

## Latency

NDI offers a very low latency solution vs. RTSP / H264, at the cost of higher network bandwidth. 

## Video Format

Video sent over NDI is sent as YUV 4:2:2 format, and is compressed. The video can optionally include an alpha channel as well. Video can be 8-bit or 16-bit color depth. There are no limits to FPS or resolution, except for what the hardware can handle. Compression is done using the [SpeedHQ codec](<https://wiki.multimedia.cx/index.php/SpeedHQ>), which is CPU-based and very fast. NDI selects the compression level based on a few factors, including the FPS. It'll use a higher compression ratio when sending at a higher FPS, to ensure the bandwidth requirements don't become too high. 

## Audio

Audio sent over NDI is transmitted at the sample rate and number of channels in the audio CHOP that is passed to the [NDI Out TOP](<./NDI_Out_TOP.md> "NDI Out TOP"). 

## Metadata

NDI has the option to send metadata along with the video frame. Metadata sent over NDI must be formatted as XML. With a text input the text must already be formatted as XML, but in the case of a table input we convert the cells to XML using the following format: 
[code] 
    <?xml version="1.0" ?>
    <TouchDesignerFormat>
    	<HeaderInfo version=1 datatype="table" numrows=2 numcolumns=2 />
    	<Data>
    		<Row row=0>
    			<Column column=0>
    				<Cell value="A" />
    			</Column>
                <Column column=1>
    				<Cell value="B" />
    			</Column>
    		</Row>
    		<Row row=1>
    			<Column column=0>
    				<Cell value="C" />
    			</Column>
                <Column column=1>
    				<Cell value="D" />
    			</Column>
    		</Row>
    	</Data>
    </TouchDesignerFormat>
    
[/code]

## Multi-Cast

NDI can also use multi-cast to send its data. For help on how to enable multi-cast for NDI, refer to the NDI documentation. Control for multi-cast is done outside of TouchDesigner using the NDI Access Manager tool, which comes with the [Newtek NDI Tools](<https://www.newtek.com/ndi/tools/>). 

## Groups

NDI supports sources tagging themselves as being parts of one or more named 'groups'. When an NDI receiver searches for sources, it can specify groups it's interested in to reduce the number of sources it lists. 

## App

NDI provides a useful mobile application to stream NDI from phones. Search for Newtek NDI on the stores. 

## NDI Network Devices

For choosing a network switch and setting up a network: 

[https://docs.derivative.ca/images/4/46/NDI_Network_Guidelines_se_21_May_2018.pdf](<./images/4/46/NDI_Network_Guidelines_se_21_May_2018.pdf>)

[https://docs.derivative.ca/images/2/24/Adding-ndi-to-your-network.pdf](<./images/2/24/Adding-ndi-to-your-network.pdf>)

<https://support.newtek.com/hc/en-us/articles/217662768-NDI-Network-Interface-Settings>

## Network Performance Settings

On a few of our internal testing platforms it has been found that using the largest setting for Jumbo Frames on the network controller has generated very clear postive performance results with regard to remedying dropped frames at high resolutions on Gibabit NICs and switches. Not all switches support Jumbo Frames. A good switch that does is the Cisco SG300-12 and Cisco SG350-12 model. 

To set jumbo frames open the control panel and locate the Network Card properties and click the Configure button. 

In the NIC properties dialog locate the Advanced page and in the attribute lister located Jumbo Packet and set the value to 9014 Bytes. 

Your switch will have to support Jumbo Frames and it will most likely have to be turned on using the Switch managment tools... For example on our testing switch... 

## Performance Stats

1 4K RGB Noise signal is ~900 Mb/s so a single 4K signal can fully saturate and 1Gb/s switch. NDI uses massively variable compression so the Mb/s will depend on the content. When testing your bandwidth use RGB Randon Noise to be aware of your maximum requirements. 

## Trouble-Shooting Connection Issues
* Make sure all TouchDesigner senders and receivers are running the same version of TouchDesigner.
  * Try deactivating the firewall of problem computers. If this rememedies the issue then resolve the firewall issue before turning it back on.

## Trouble-Shooting Frame Drop Issues
* It has been found that other internet applications - most notably - Skype can interfere with NDI and cause frame drops. Its not clear why this is but we have clearly seen this happen - possibly due to collisions.


See also: [NDI and Dante Networks](<./NDI_and_Dante_Networks.md> "NDI and Dante Networks")
