# DMX Out POP

##   
  
Summary

The DMX Out POP can send to DMX, Art-Net, sACN, [KiNET](<https://www.colorkinetics.com/global/learn/optics-matter>), or FTDI devices. 

The DMX Out POP merges the DMX universes from each of its [DMX Fixture POP](<./DMX_Fixture_POP.md> "DMX Fixture POP") inputs, and sends them to the device. It can merge any number of DMX Fixture POPs but conflicts may arise if multiple DMX Fixture POPs write to the same channel value of a DMX universe. A warning will be output in that case, and for debugging such conflicts the [DMX Map DAT](<./DMX_Map_DAT.md> "DMX Map DAT") is a useful tool. 

**Note:** every input must be a DMX Fixture POP, whether they are wired or by parameter OP reference. 

The DMX in TouchDesigner was developed on the [ENTTEC](<http://www.enttec.com>) device, namely their [DMX USB Pro](<http://www.enttec.com/?main_menu=Products&pn=70304>) and DMX over Ethernet devices, but it should work for many devices and software that support DMX/Art-Net/sACN/KiNET. 

A Routing Table can be provided in a DAT where network addresses can be specified by adding rows for each DMX512 universe and then specifying the net, subnet and universe values. 

**Tip** : You can use a single DMX Out POP to gather and serve any number of DMX Fixture POPs in your project because you can specify recursively from root`/*`the path of all DMX Fixture POPs to Search for in the DMX Fixture POPs parameter. You can use a [Folder DAT](<./Folder_DAT.md> "Folder DAT") to find all the DMX Fixture POPs in your project. 

**ENTTEC NOTE:** \- Use ENTTEC's [NMU (Node Management Utility)](<http://www.enttec.com/us/products/controls/dmx-over-ethernet/nmu/>) to configure and inspect the ENTTEC devices found on your network. 

**macOS NOTE:** \- ENTTEC USB Pro may not connect automatically, to enable it enter the following command in the Terminal:`sudo kextunload -b com.apple.driver.AppleUSBFTDI`**Tip** : Use [WireShark](<https://www.wireshark.org/>) to watch your DMX network traffic. 

See also: [Art-Net](<./Art-Net.md> "Art-Net"), [sACN](<./SACN.md> "SACN"), [DMX In CHOP](<./DMX_In_CHOP.md> "DMX In CHOP"), [DMX Out CHOP](<./DMX_Out_CHOP.md> "DMX Out CHOP"), [DMX](<./DMX.md> "DMX")

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[dmxoutPOP_Class](<./DmxoutPOP_Class.md> "DmxoutPOP Class")

## 

Parameters - DMX Page

Active`active`\- When enabled, will be actively sending to the device. 

Interface`interface`\- ⊞ \- Select the type of interface to connect to the device with. 
* Generic Serial`serial`\- Uses the operating system's serial calls to write data.
* Enttec USB Pro`enttecusbpro`-
* Enttec USB Pro Mk2`enttecusbpromk2`-
* Art-Net`artnet`\- Sets the interface to [Art-Net](<http://en.wikipedia.org/wiki/Art-Net>) protocol.
* sACN`sacn`\- Sets the interface to [sACN](<https://en.wikipedia.org/wiki/Architecture_for_Control_Networks>) protocol.
* KiNET`kinet`\- Sets the interface to [KiNET](<https://www.colorkinetics.com/global/learn/led-lighting-technology#KiNET>) protocol.


Rate`rate`\- How often data is sent to the device (per second). **WARNING: DMX512 devices have a maximum refresh rate of 44Hz. It is recommended that Rate <= 44 for reliable performance.**

## 

Parameters - Fixtures Page

Fixture`fixture`\- Start of Sequential Parameter Blocks for DMX Fixture POP inputs, either wired or referenced. 

Active`fixture0active`\- When active, this Fixture is merged and sent. 

DMX Fixture POPs`fixture0pop`\- A reference to one or more DMX Fixture POPs. The parameter is disabled if there is a corresponding wired input. 

## 

Parameters - Serial Page

Serial Port`serialport`\- ⊞ \- When the Interface parameter is set to Generic Serial this parameter lets you select which Serial (COM) port to use. 
* COM3`com3`-


DMXking Port`dmxkingport`\- ⊞ \- Select a DMXking port to send to. 
* Default`default`-


Device`device`\- ⊞ \- Select a DMX device from the menu. 
* *`*`-

## 

Parameters - Network Page

Multicast`multicast`\- Enable multicast for sACN. Multicast automatically builds the IP based on Net, Subnet, and Universe of the device. This allows for sending to multiple devices at once by specifying multiple universes. 

Network Address`netaddress`\- Specify the IP address to use. This address corresponds to the receiving device address. When the address is set to its default 255.255.255.255, the messages are instead broadcast to all devices on the network. The Net, Subnet and Universe of the receiving devices must still match those specified in the DMX Out POP in all cases. If a netaddress is specified in the Routing Table for a given net/subnet/universe then that will be used instead. 

Local Address`localaddress`\- ⊞ \- When the sending machine is equipped with multiple network adapters, this parameter can be used to choose which adapter to send the data from by specifying its IP address here. 
* 192.168.178.150`192.168.178.150`-
* 10.2.0.2`10.2.0.2`-


Local Port`localport`\- In rare cases it can be necessary to supply a custom port from which the data should be sent. The default of`-1`means the O/S assigned port is being used. 

Use Custom Port`customport`\- Enable the Network Port parameter to specify the port of the receiving hardware. When disabled, default port is 6454 for Art-Net, 5568 for sACN, and 6038 for KiNET. 

Network Port`netport`\- Specify the port of the receiving hardware. 

Priority`priority`\- The data priority, if there are multiple sources. Used with sACN and KiNET protocols. 

Send ArtSync`sendartsync`\- When enabled will send out ArtSync packets. ArtSync packets are used to synchronize multiple universes together. It will do this by waiting for all ArtDmx packets to finish sending, then follow up by sending an ArtSync packet. 

ArtSync Timeout`artsynctimeout`\- Specify the time in milliseconds that ArtSync will wait for all ArtDmx packets to complete sending, before sending the ArtSync packet. If they have not all been sent when the timeout is reached, then ArtSync will terminate and the ArtSync packet will not be sent. Additionally, a new frame of ArtDmx packets will be sent and a new ArtSync will be initiated. 

CID`cid`\- The unique ID of the sender. 

Source`source`\- User assigned name of source (for informative purposes). 

KiNET Version`kinetversion`\- ⊞ \- Select the version of the KiNET protocol to use. 
* DmxOut (v1)`v1`-
* PortOut (v2)`v2`-


Use Custom KiNET Port`customkinetport`\- When enabled, can specify a custom port for the KiNET v2 interface. When disabled, the port will be the broadcast port: 255. 

KiNET Port`kinetport`\- Specifies the port for KiNET v2 interface. 

Routing Table`routingtable`\- Use a Table DAT to specify netaddress, source, cid, priority, and kinetport values for specific universes. The net, subnet, universe columns must be filled in with valid values. Note: the [DMX Fixture POP](<./DMX_Fixture_POP.md> "DMX Fixture POP") can override the netaddress value with its own Routing Table. 

## 

Parameters - Multipliers Page

Use Multipliers`usemultipliers`\- Enable the use of multipliers, which apply a post-operation multiply [0-1] on specific named channels (ie. the name set using the Name parameter on a DMX Fixture POP). 

Multiplier`multiplier`\- Start of Sequential Parameter Blocks for a channel multipplier. If there are duplicate channel names the multipliers will be combined for that channel. 

DMX Channels`multiplier0dmxchannels`\- Select the DMX Channel names (derived from the Name parameters on the input DMX Fixture POPs). The accompanying menu has a list of all available channel names. One Multiplier sequence block can reference multiple channel names in a space delimited format: eg. "Dimmer RGB", where Dimmer and RGB are channel names. "*" can be used to apply the multiplier to every single channel. 

Multiplier Value`multiplier0value`\- The multiplier value from [0-1] to apply to any channel that matches the associated channel names specified in DMX Channels. 

## 

Parameters - Common Page

Bypass`bypass`\- Pass through the first input to the output unchanged. 

Free Extra GPU Memory`freeextragpumem`\- Free memory that has accumulated when output memory has grown and shrunk. 

Delete Input Attributes`delinputattrs`\- Only output which attributes you specify in this POP \- helps isolate attributes into a separate branch. 

## 

Operator Inputs
* Input 0:  -

## 

Info CHOP Channels

Extra Information for the DMX Out POP can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). __

### 

Common POP Info Channels

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


  
TouchDesigner Build: Latest\nwikieditorwikieditor2025.30000

POPs   
---  
[Accumulate ](<./Accumulate_POP.md> "Accumulate POP")• [Alembic In ](<./Alembic_In_POP.md> "Alembic In POP")• [Analyze ](<./Analyze_POP.md> "Analyze POP")• [Attribute Combine ](<./Attribute_Combine_POP.md> "Attribute Combine POP")• [Attribute Convert ](<./Attribute_Convert_POP.md> "Attribute Convert POP")• [Attribute ](<./Attribute_POP.md> "Attribute POP")• [Blend ](<./Blend_POP.md> "Blend POP")• [Box ](<./Box_POP.md> "Box POP")• [Cache Blend ](<./Cache_Blend_POP.md> "Cache Blend POP")• [Cache ](<./Cache_POP.md> "Cache POP")• [Cache Select ](<./Cache_Select_POP.md> "Cache Select POP")• [CHOP to ](<./CHOP_to_POP.md> "CHOP to POP")• [Circle ](<./Circle_POP.md> "Circle POP")• [Connectivity ](<./Connectivity_POP.md> "Connectivity POP")• [Convert ](<./Convert_POP.md> "Convert POP")• [Copy ](<./Copy_POP.md> "Copy POP")• [CPlusPlus ](<./CPlusPlus_POP.md> "CPlusPlus POP")• [Curve ](<./Curve_POP.md> "Curve POP")• [DAT to ](<./DAT_to_POP.md> "DAT to POP")• [Delete ](<./Delete_POP.md> "Delete POP")• [Dimension ](<./Dimension_POP.md> "Dimension POP")• [DMX Fixture ](<./DMX_Fixture_POP.md> "DMX Fixture POP")• DMX Out • [Extrude ](<./Extrude_POP.md> "Extrude POP")• [Facet ](<./Facet_POP.md> "Facet POP")• [Feedback ](<./Feedback_POP.md> "Feedback POP")• [Field ](<./Field_POP.md> "Field POP")• [File In ](<./File_In_POP.md> "File In POP")• [File Out ](<./File_Out_POP.md> "File Out POP")• [Force Radial ](<./Force_Radial_POP.md> "Force Radial POP")• [GLSL Advanced ](<./GLSL_Advanced_POP.md> "GLSL Advanced POP")• [GLSL Copy ](<./GLSL_Copy_POP.md> "GLSL Copy POP")• [GLSL Create ](<./GLSL_Create_POP.md> "GLSL Create POP")• [GLSL ](<./GLSL_POP.md> "GLSL POP")• [GLSL Select ](<./GLSL_Select_POP.md> "GLSL Select POP")• [Grid ](<./Grid_POP.md> "Grid POP")• [Group ](<./Group_POP.md> "Group POP")• [Histogram ](<./Histogram_POP.md> "Histogram POP")• [Import Select ](<./Import_Select_POP.md> "Import Select POP")• [In ](<./In_POP.md> "In POP")• [Limit ](<./Limit_POP.md> "Limit POP")• [Line Break ](<./Line_Break_POP.md> "Line Break POP")• [Line Divide ](<./Line_Divide_POP.md> "Line Divide POP")• [Line Metrics ](<./Line_Metrics_POP.md> "Line Metrics POP")• [Line ](<./Line_POP.md> "Line POP")• [Line Resample ](<./Line_Resample_POP.md> "Line Resample POP")• [Line Smooth ](<./Line_Smooth_POP.md> "Line Smooth POP")• [Line Thick ](<./Line_Thick_POP.md> "Line Thick POP")• [Lookup Attribute ](<./Lookup_Attribute_POP.md> "Lookup Attribute POP")• [Lookup Channel ](<./Lookup_Channel_POP.md> "Lookup Channel POP")• [Lookup Texture ](<./Lookup_Texture_POP.md> "Lookup Texture POP")• [Math Combine ](<./Math_Combine_POP.md> "Math Combine POP")• [Math Mix ](<./Math_Mix_POP.md> "Math Mix POP")• [Math ](<./Math_POP.md> "Math POP")• [Merge ](<./Merge_POP.md> "Merge POP")• [Neighbor ](<./Neighbor_POP.md> "Neighbor POP")• [Noise ](<./Noise_POP.md> "Noise POP")• [Normal ](<./Normal_POP.md> "Normal POP")• [Normalize ](<./Normalize_POP.md> "Normalize POP")• [Null ](<./Null_POP.md> "Null POP")• [OAK Select ](<./OAK_Select_POP.md> "OAK Select POP")• [Out ](<./Out_POP.md> "Out POP")• [Particle ](<./Particle_POP.md> "Particle POP")• [Pattern ](<./Pattern_POP.md> "Pattern POP")• [Phaser ](<./Phaser_POP.md> "Phaser POP")• [Plane ](<./Plane_POP.md> "Plane POP")• [Point File In ](<./Point_File_In_POP.md> "Point File In POP")• [Point Generator ](<./Point_Generator_POP.md> "Point Generator POP")• [Point ](<./Point_POP.md> "Point POP")• [Points, Vertices and Primitives in s ](<./Points,_Vertices_and_Primitives_in_POPs.md> "Points, Vertices and Primitives in POPs")• [Polygonize ](<./Polygonize_POP.md> "Polygonize POP")• [POP ](<./POP.md> "POP")• [Primitive ](<./Primitive_POP.md> "Primitive POP")• [Projection ](<./Projection_POP.md> "Projection POP")• [Proximity ](<./Proximity_POP.md> "Proximity POP")• [Quantize ](<./Quantize_POP.md> "Quantize POP")• [Random ](<./Random_POP.md> "Random POP")• [Ray ](<./Ray_POP.md> "Ray POP")• [Rectangle ](<./Rectangle_POP.md> "Rectangle POP")• [ReRange ](<./ReRange_POP.md> "ReRange POP")• [Revolve ](<./Revolve_POP.md> "Revolve POP")• [Select ](<./Select_POP.md> "Select POP")• [Skin Deform ](<./Skin_Deform_POP.md> "Skin Deform POP")• [Skin ](<./Skin_POP.md> "Skin POP")• [SOP to ](<./SOP_to_POP.md> "SOP to POP")• [Sort ](<./Sort_POP.md> "Sort POP")• [Sphere ](<./Sphere_POP.md> "Sphere POP")• [Sprinkle ](<./Sprinkle_POP.md> "Sprinkle POP")• [Subdivide ](<./Subdivide_POP.md> "Subdivide POP")• [Switch ](<./Switch_POP.md> "Switch POP")• [Texture Map ](<./Texture_Map_POP.md> "Texture Map POP")• [TOP to ](<./TOP_to_POP.md> "TOP to POP")• [Topology ](<./Topology_POP.md> "Topology POP")• [Torus ](<./Torus_POP.md> "Torus POP")• [Trail ](<./Trail_POP.md> "Trail POP")• [Transform ](<./Transform_POP.md> "Transform POP")• [Trig ](<./Trig_POP.md> "Trig POP")• [Tube ](<./Tube_POP.md> "Tube POP")• [Twist ](<./Twist_POP.md> "Twist POP")• [ZED ](<./ZED_POP.md> "ZED POP")
