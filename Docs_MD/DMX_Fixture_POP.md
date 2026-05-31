# DMX Fixture POP

## 

Summary

The DMX Fixture POP constructs DMX universes from a POP input, and is used in conjunction with a [DMX Out POP](<./DMX_Out_POP.md> "DMX Out POP") to send DMX to a device. 

In the POP input, each primitive is analogous to a fixture. Each fixture is iterated over and the DMX profile defined on the Channels page is used to construct the DMX universes for each fixture. The fixture/primitives are iterated over in the order they're defined in the POP. 

The following primitive attributes, as unsigned integers, can be used to specify net, subnet, universe, channel, and netaddress, allowing for per-fixture customization without needing to use the Routing Table: 

  *`DMXFixtureNet`*`DMXFixtureSubnet`*`DMXFixtureUniverse`*`DMXFixtureChannel`*`DMXFixtureNetAddress`The [DMX Map DAT](<./DMX_Map_DAT.md> "DMX Map DAT") can be used to inspect the DMX universes created. 

### Creating the DMX Profile

The DMX Profile is defined by the Channel sequence on the DMX Profile page. 

DMX Channels are sequenced in the universe output in the same order they're defined on the DMX Profile page. 

For any given Channel sequence, all attribute components will be interleaved together. Eg. '`P`' will be interleaved as 'Px Py Pz'. If the DMX profile requires them to not be interleaved then they will instead need to be separated into their own Channel sequence blocks. 

Multiple attributes can be specified together: Eg. '`P Color`' will interleave P and Color together like so: 'Px Py Pz Colorr Colorg Colorb Colora'. If the interleaved components are of different resolutions, then they will need to be separated into their own Channel sequence blocks, but by enabling Merge with Above Block they can be interleaved together. 

For Point Value Types, all points will be iterated over before the next Channel Sequence. 

Individual attribute components can also be specified. Eg. '`P(0) P(1)`' to use just position x and y. 

Attribute components are interleaved by value unless Interleave Bytes is enabled for the attribute grouping. Example: Position attribute P with 16-bit resolution will be interleaved as`Px[0] Px[1] Py[0] Py[1] Pz[0] Pz[1] ...`when the Interleave Bytes toggle is disabled, but interleave as`Px[0] Py[0] Pz[0] Px[1] Py[1] Pz[1] ...`when the Interleave Bytes toggle is enabled. 

### Auto Layout Mode

The DMX Fixture POP is in Auto Layout mode when the Auto Layout toggle is enabled, or as a default when the toggle is disabled and no routing table is referenced, or the routing table has no rows. 

Auto Layout mode auto-increments channel and universe values from a defined starting point (using the net, subnet, universe, and channel parameters). Primitives are iterated over in primitive order (eg. prim 0 is first) and each primitive's points are iterated over in point order (eg. point 0 is first). 

The DMX Profile page defines the channel layout for each primitive. It is executed once per primitive, and then a channel gap is added (specified by parameter) between each primitive channel layout. 

If Quantize Universe is set to off, then the next primitive will begin immediately after the channel gap. But if Quantize Universe is set to By Fixture, it will first check to see if the next primitive (ie. fixture) can fit in the remaining channels of the universe, and if not, it will jump to the next universe at channel=1. Similarly, if Quantize Universe is set to By Components, and a multi-component DMX Channel entry on the DMX Profile page cannot fit all components in the remaining channels of the universe (eg.`P`has 3 components x y z so with 8-bit resolution would require 3 remaining channels), then it will jump to the next universe at channel=1. 

When the`DMXFixtureNetAddress`attribute is set, each specific net address value will have their own independently incrementing channel values. Eg. if there are 8 primitives each of exactly 512 channels, and there are 4 with`DMXFixtureNetAddress=192.168.0.1`and 4 with`DMXFixtureNetAddress=192.168.0.2`, then the resulting channel layout will be 4 universes [0-3] with`netaddress=192.168.0.1`and 4 universes [0-3] with`netaddress=192.168.0.2`. 

When the`DMXFixtureUniverse`attribute is set, the channel value is set to 1 for that universe, unless`DMXFixtureChannel`is also set. If the`DMXFixtureUniverse`is greater than 15 then the`DMXFixtureNet`and`DMXFixtureSubnet`attribute values will not be used if set. 

See also: [DMX Out POP](<./DMX_Out_POP.md> "DMX Out POP"), [DMX Map DAT](<./DMX_Map_DAT.md> "DMX Map DAT"), [DMX](<./DMX.md> "DMX")

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[dmxfixturePOP_Class](<./DmxfixturePOP_Class.md> "DmxfixturePOP Class")

## 

Parameters - Fixture Page

Active`active`\- When enabled, will actively update the fixture and universe data, and if used in a DMX Out POP will be sent out to the device. If disabled, the DMX Out POP will not merge the DMX universes constructed by this POP for sending. 

Auto Layout`autolayout`\- When enabled, the universes will be constructed sequentially starting from net, subnet, universe, and channel specified in the parameters. For example, if starting a net=0, subnet=0, universe=1, channel=0, then the DMX Fixture POP will iterate through all 512 channels using the profile at which point it will move to universe 2. When disabled, a Routing Table must be used instead, and the universes manually assigned to a primindex. 

Routing Table`routingtable`\- Use a Routing Table to assign specific net, subnet, universe values to a fixture/primitive. Additionally, netaddress may optionally be specified to override those on the DMX Out POP. The routing table will override use of parameters, as well as any of the reserved attributes: DMXFixtureNet, DMXFixtureSubnet, DMXFixtureUniverse, DMXFixtureChannel, and DMXFixtureNetAddress. 

Net (0-127)`net`\- When using Auto Layout, specify the starting net value. 

Subnet (0-15)`subnet`\- When using Auto Layout, specify the starting subnet value. 

Universe`universe`\- When using Auto Layout, specify the starting universe value. 

Channel`channel`\- When using Auto Layout, specify the starting channel value. 

Channel Gap`changap`\- When using Auto Layout, specify the amount of channels between fixtures. Eg. if fixture 1 ends on channel 200 and there is a channel of 10, then fixture 2 will start on channel 211. 

Quantize Universe`quantizeuni`\- ⊞ \- Specify the level of quantizing to perform within a universe. It can either be set to be done By Fixture, or By Component. 
* Off`off`\- When set to Off, no quantizing is done, and both channels and fixtures can bridge universes.
* By Fixture`fixture`\- When set to By Fixture, fixtures cannot bridge universes (ie. have their channel range start in a different universe than it ends in), meaning that it must be a maximum of 512 channels. Also, if a fixture cannot fit in the remaining channels of a universe, then it will be moved to the next one.
* By Component`component`\- When set to By Component, multi-component DMX Channel entries (eg.`P`has 3 components x y z which requires 3 channels with 8-bit resolution) cannot bridge universes. If it cannot fit into the remaining channels of a universe, then it will be moved to the next one.

## 

Parameters - DMX Profile Page

DMX Channel`dmxchan`\- Start of Sequential Parameter Blocks used to define the DMX profile 

Name`dmxchan0name`\- Specify the unique DMX Channel identifier. 

Value Type`dmxchan0valuetype`\- ⊞ \- Specify how the channels values are iterated, and how the attributes are sourced. 
* Point`point`\- When using the Point value type, each point will be iterated over for this channel block and have their values interleaved, before moving on to the next channel.
* Primitive`primitive`\- When using the Primitive value type, the channel value will be interleaved from the value source only once per primitive/fixture, before moving on to the next channel.


Value Source`dmxchan0valuesource`\- ⊞ \- For the DMX channel value, gets it from an attribute or from a parameter. 
* Constant`constant`\- Set the channel values using a constant. Note: if Value Type is Point, each point will still be iterated over once and have their value set to the constant value. In other words, the number of channels used is still the same whether using a constant or attribute value source.
* Attribute`attribute`\- Set the values using an attribute. Multiple attributes can be specified together. They will be all be interleaved.


Group`dmxchan0group`\- Optionally select a point group. Only points within the group will be used for universe creation, rather than all points. 

Number of Components`dmxchan0numcomps`\- ⊞ \- Number of components of the new attribute. 
* 1`1`\- Number of constant components to use.
* 2`2`-
* 3`3`-
* 4`4`-


Value`dmxchan0value`\- ⊞ \- Set the constant value. 
* Value`dmxchan0valuer`-
* Value`dmxchan0valueg`-
* Value`dmxchan0valueb`-
* Value`dmxchan0valuea`-


Attribute`dmxchan0attr`\- Set the attributes to interleave. Multiple attributes can be specified together. 

Value Resolution`dmxchan0valueres`\- ⊞ \- The value resolution. Note: one DMX channel is 8-bit (ie. one byte and 0-255), so if a value is greater than 8-bit, it will use more than one channel: Eg. 16-bit uses 2 channels. 
* 8-bit`b8`-
* 16-bit`b16`-
* 24-bit`b24`-
* 32-bit`b32`-


Value is Normalized`dmxchan0normalized`\- When enabled, values of 0-1 are expected, and they will be scaled to the appropriate range for the resolution (ie. 0-255 for 8-bit). When disabled, the values will be output as-is. Clamping is done in both cases. 

Merge with Above Block`dmxchan0merge`\- When enabled, will interleave channel values with the above block. The blocks must be of the same value type and value source. This feature is useful if needing to interleave values of different resolutions. 

Interleave Bytes`dmxchan0interleavebytes`\- When enabled, attribute component values will be interleaved by byte order, instead of value order. Example: Position attribute P with 16-bit resolution will be interleaved as`Px[0] Px[1] Py[0] Py[1] Pz[0] Pz[1] ...`when the toggle is disabled, but interleave as`Px[0] Py[0] Pz[0] Px[1] Py[1] Pz[1] ...`when the Interleave Bytes toggle is enabled. This also means that if the components have an 8-bit value resolution, then the toggle will have no effect. Interleave Bytes can only be enabled at the root (ie. top) DMX Channel in the case where multiple DMX Channel blocks are merged together with Merge Above Block. 

## 

Parameters - Common Page

Bypass`bypass`\- Pass through the first input to the output unchanged. 

Free Extra GPU Memory`freeextragpumem`\- Free memory that has accumulated when output memory has grown and shrunk. 

Delete Input Attributes`delinputattrs`\- Only output which attributes you specify in this POP \- helps isolate attributes into a separate branch. 

Parameter Color Space`parmcolorspace`\- ⊞ \- Controls how all color parameters on this node are interpreted. The color values as treated as being in the selected color space, and are converted to the Working [Color Space](<./Color_Space.md> "Color Space") before they are used as part of the node's operation. Note that this does not change the color space of the node itself, as that is always in the Working Color Space. 
* sRGB`srgb`\- [sRGB](<https://en.wikipedia.org/wiki/SRGB>) color space, with sRGB transfer function. Considered an SDR color space with respect to Reference White.
* sRGB - Linear`srgblinear`\- [sRGB](<https://en.wikipedia.org/wiki/SRGB>) color space, with linear transfer function. Considered an SDR color space with respect to Reference White.
* Rec.601 (NTSC)`rec601ntsc`\- [Rec.601](<https://en.wikipedia.org/wiki/Rec._601>) with NTSC primaries color space, with Rec.601 transfer function. Considered an SDR color space with respect to Reference White.
* Rec.709`rec709`\- [Rec.709](<https://en.wikipedia.org/wiki/Rec._709>) color space, with Rec.709 (same as Rec.2020) transfer function. Considered an SDR color space with respect to Reference White.
* Rec.2020`rec2020`\- [Rec.2020](<https://en.wikipedia.org/wiki/Rec._2020>) color space, with Rec.2020 (same as Rec.709) transfer function. Considered an HDR color space with respect to Reference White.
* DCI-P3`dcip3`\- [DCI-P3](<https://en.wikipedia.org/wiki/DCI-P3>) color space, with D65 white point and 2.6 gamma transfer function. Considered an HDR color space with respect to Reference White.
* DCI-P3 (D60)`dcip3d60`\- [DCI-P3 "D60 sim"](<https://en.wikipedia.org/wiki/DCI-P3>) color space, with D60 white point, and 2.6 gamma transfer function. Considered an HDR color space with respect to Reference White.
* Display-P3 (D65)`displayp3d65`\- [Display-P3](<https://en.wikipedia.org/wiki/DCI-P3>) color space, with D65 white point, and sRGB gamma transfer function. Considered an HDR color space with respect to Reference White.
* ACES2065-1`aces2065-1`\- [ACES 2065-1](<https://en.wikipedia.org/wiki/Academy_Color_Encoding_System>) (also known as ACES AP0) color space, with a linear gamma transfer function. Considered an HDR color space with respect to Reference White.
* ACEScg`acescg`\- [ACEScg](<https://en.wikipedia.org/wiki/Academy_Color_Encoding_System>) (also known as ACES AP1) color space, with a linear gamma transfer function. Considered an HDR color space with respect to Reference White.
* Passthrough`passthrough`\- When selected, the color values will be used as-is in the operation, without any modification or attempt to convert them into the Working Color Space.


Parameter Reference White`parmreferencewhite`\- ⊞ \- When converting a parameter color value to the Working Color Space, this controls how it should be treated with respect to [Reference White](<./Color_Space.htm#Reference_White> "Color Space"). If the Working Color Space is the same Reference White, then no adjustment is done. If they are different, then the Reference White level (brightness) of this color will be adjusted to the range expected by the Working Color Space. For example if the project is set to have a SDR Reference White of 120 nits, and the HDR Reference White is 80 nits, then a color of (1, 1, 1), which is 120 nits in the SDR color space, will be converted to be (1.5, 1.5, 1.5), which is 120 nits still in the HDR Working Color Space. 
* Default For Color Space`default`\- Will use either the SDR or the HDR Reference White, based on the color space selected.
* Use Parent Panel`useparent`\- Will use the Reference White that the parent panel has selected. If the top-level panel also has 'Use Parent' selected, then 'UI Reference White' will be used.
* Standard (SDR)`sdr`\- Will treat the Parameter Color Space as SDR for it's reference white value.
* High (HDR)`hdr`\- Will treat the Parameter Color Space as HDR for it's reference white value.
* UI`ui`\- Will treat the Parameter Color Space as UI for it's reference white value. This uses the 'UI Reference White Nits' value for it's brightness.

## 

Operator Inputs
* Input 0:  -

## 

Info CHOP Channels

Extra Information for the DMX Fixture POP can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). __

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


  
TouchDesigner Build: Latest\nwikieditor2025.30000

POPs   
---  
[Accumulate ](<./Accumulate_POP.md> "Accumulate POP")• [Alembic In ](<./Alembic_In_POP.md> "Alembic In POP")• [Analyze ](<./Analyze_POP.md> "Analyze POP")• [Attribute Combine ](<./Attribute_Combine_POP.md> "Attribute Combine POP")• [Attribute Convert ](<./Attribute_Convert_POP.md> "Attribute Convert POP")• [Attribute ](<./Attribute_POP.md> "Attribute POP")• [Blend ](<./Blend_POP.md> "Blend POP")• [Box ](<./Box_POP.md> "Box POP")• [Cache Blend ](<./Cache_Blend_POP.md> "Cache Blend POP")• [Cache ](<./Cache_POP.md> "Cache POP")• [Cache Select ](<./Cache_Select_POP.md> "Cache Select POP")• [CHOP to ](<./CHOP_to_POP.md> "CHOP to POP")• [Circle ](<./Circle_POP.md> "Circle POP")• [Connectivity ](<./Connectivity_POP.md> "Connectivity POP")• [Convert ](<./Convert_POP.md> "Convert POP")• [Copy ](<./Copy_POP.md> "Copy POP")• [CPlusPlus ](<./CPlusPlus_POP.md> "CPlusPlus POP")• [Curve ](<./Curve_POP.md> "Curve POP")• [DAT to ](<./DAT_to_POP.md> "DAT to POP")• [Delete ](<./Delete_POP.md> "Delete POP")• [Dimension ](<./Dimension_POP.md> "Dimension POP")• DMX Fixture • [DMX Out ](<./DMX_Out_POP.md> "DMX Out POP")• [Extrude ](<./Extrude_POP.md> "Extrude POP")• [Facet ](<./Facet_POP.md> "Facet POP")• [Feedback ](<./Feedback_POP.md> "Feedback POP")• [Field ](<./Field_POP.md> "Field POP")• [File In ](<./File_In_POP.md> "File In POP")• [File Out ](<./File_Out_POP.md> "File Out POP")• [Force Radial ](<./Force_Radial_POP.md> "Force Radial POP")• [GLSL Advanced ](<./GLSL_Advanced_POP.md> "GLSL Advanced POP")• [GLSL Copy ](<./GLSL_Copy_POP.md> "GLSL Copy POP")• [GLSL Create ](<./GLSL_Create_POP.md> "GLSL Create POP")• [GLSL ](<./GLSL_POP.md> "GLSL POP")• [GLSL Select ](<./GLSL_Select_POP.md> "GLSL Select POP")• [Grid ](<./Grid_POP.md> "Grid POP")• [Group ](<./Group_POP.md> "Group POP")• [Histogram ](<./Histogram_POP.md> "Histogram POP")• [Import Select ](<./Import_Select_POP.md> "Import Select POP")• [In ](<./In_POP.md> "In POP")• [Limit ](<./Limit_POP.md> "Limit POP")• [Line Break ](<./Line_Break_POP.md> "Line Break POP")• [Line Divide ](<./Line_Divide_POP.md> "Line Divide POP")• [Line Metrics ](<./Line_Metrics_POP.md> "Line Metrics POP")• [Line ](<./Line_POP.md> "Line POP")• [Line Resample ](<./Line_Resample_POP.md> "Line Resample POP")• [Line Smooth ](<./Line_Smooth_POP.md> "Line Smooth POP")• [Line Thick ](<./Line_Thick_POP.md> "Line Thick POP")• [Lookup Attribute ](<./Lookup_Attribute_POP.md> "Lookup Attribute POP")• [Lookup Channel ](<./Lookup_Channel_POP.md> "Lookup Channel POP")• [Lookup Texture ](<./Lookup_Texture_POP.md> "Lookup Texture POP")• [Math Combine ](<./Math_Combine_POP.md> "Math Combine POP")• [Math Mix ](<./Math_Mix_POP.md> "Math Mix POP")• [Math ](<./Math_POP.md> "Math POP")• [Merge ](<./Merge_POP.md> "Merge POP")• [Neighbor ](<./Neighbor_POP.md> "Neighbor POP")• [Noise ](<./Noise_POP.md> "Noise POP")• [Normal ](<./Normal_POP.md> "Normal POP")• [Normalize ](<./Normalize_POP.md> "Normalize POP")• [Null ](<./Null_POP.md> "Null POP")• [OAK Select ](<./OAK_Select_POP.md> "OAK Select POP")• [Out ](<./Out_POP.md> "Out POP")• [Particle ](<./Particle_POP.md> "Particle POP")• [Pattern ](<./Pattern_POP.md> "Pattern POP")• [Phaser ](<./Phaser_POP.md> "Phaser POP")• [Plane ](<./Plane_POP.md> "Plane POP")• [Point File In ](<./Point_File_In_POP.md> "Point File In POP")• [Point Generator ](<./Point_Generator_POP.md> "Point Generator POP")• [Point ](<./Point_POP.md> "Point POP")• [Points, Vertices and Primitives in s ](<./Points,_Vertices_and_Primitives_in_POPs.md> "Points, Vertices and Primitives in POPs")• [Polygonize ](<./Polygonize_POP.md> "Polygonize POP")• [POP ](<./POP.md> "POP")• [Primitive ](<./Primitive_POP.md> "Primitive POP")• [Projection ](<./Projection_POP.md> "Projection POP")• [Proximity ](<./Proximity_POP.md> "Proximity POP")• [Quantize ](<./Quantize_POP.md> "Quantize POP")• [Random ](<./Random_POP.md> "Random POP")• [Ray ](<./Ray_POP.md> "Ray POP")• [Rectangle ](<./Rectangle_POP.md> "Rectangle POP")• [ReRange ](<./ReRange_POP.md> "ReRange POP")• [Revolve ](<./Revolve_POP.md> "Revolve POP")• [Select ](<./Select_POP.md> "Select POP")• [Skin Deform ](<./Skin_Deform_POP.md> "Skin Deform POP")• [Skin ](<./Skin_POP.md> "Skin POP")• [SOP to ](<./SOP_to_POP.md> "SOP to POP")• [Sort ](<./Sort_POP.md> "Sort POP")• [Sphere ](<./Sphere_POP.md> "Sphere POP")• [Sprinkle ](<./Sprinkle_POP.md> "Sprinkle POP")• [Subdivide ](<./Subdivide_POP.md> "Subdivide POP")• [Switch ](<./Switch_POP.md> "Switch POP")• [Texture Map ](<./Texture_Map_POP.md> "Texture Map POP")• [TOP to ](<./TOP_to_POP.md> "TOP to POP")• [Topology ](<./Topology_POP.md> "Topology POP")• [Torus ](<./Torus_POP.md> "Torus POP")• [Trail ](<./Trail_POP.md> "Trail POP")• [Transform ](<./Transform_POP.md> "Transform POP")• [Trig ](<./Trig_POP.md> "Trig POP")• [Tube ](<./Tube_POP.md> "Tube POP")• [Twist ](<./Twist_POP.md> "Twist POP")• [ZED ](<./ZED_POP.md> "ZED POP")
