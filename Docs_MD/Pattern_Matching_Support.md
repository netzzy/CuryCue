# Pattern Matching Support

## Group Name Expansion

**Note** : Operator Patterns support the`@groupname`pattern expansion. 

## COMP

Node | Parameter Name | Pattern Type | Supports Set Matching   
---|---|---|---  
[Actor COMP](<./Actor_COMP.md> "Actor COMP") | Forces | Operator | ✅   
Collision SOPs | Operator | ✅   
Light Mask | Operator | ✅   
[Blend COMP](<./Blend_COMP.md> "Blend COMP") | Light Mask | Operator | ✅   
[Bone COMP](<./Bone_COMP.md> "Bone COMP") | Light Mask | Operator | ✅   
[Bullet Solver COMP](<./Bullet_Solver_COMP.md> "Bullet Solver COMP") | Actors | Operator | ✅   
Global Forces | Operator | ✅   
[Camera COMP](<./Camera_COMP.md> "Camera COMP") | Camera Light Mask | Operator | ✅   
[Constraint COMP](<./Constraint_COMP.md> "Constraint COMP") | Actor Bodies | Index | ✅   
[Geo Text COMP](<./Geo_Text_COMP.md> "Geo Text COMP") | Light Mask | Operator | ✅   
[Geometry COMP](<./Geometry_COMP.md> "Geometry COMP") | Instance Textures | Operator | ✅   
Light Mask | Operator | ✅   
[Handle COMP](<./Handle_COMP.md> "Handle COMP") | Light Mask | Operator | ✅   
[Light COMP](<./Light_COMP.md> "Light COMP") | Shadow Casters | Operator | ✅   
[NVIDIA Flex Solver COMP](<./NVIDIA_Flex_Solver_COMP.md> "NVIDIA Flex Solver COMP") | Actors | Operator | ✅   
Global Forces | Operator | ✅   
Light Mask | Operator | ✅   
[NVIDIA Flow Emitter COMP](<./NVIDIA_Flow_Emitter_COMP.md> "NVIDIA Flow Emitter COMP") | Light Mask | Operator | ✅   
  
## POP

Node | Parameter Name | Pattern Type | Supports Set Matching   
---|---|---|---  
[Analyze POP](<./Analyze_POP.md> "Analyze POP") | Input Attributes | Basic | ✅   
[Attribute Combine POP](<./Attribute_Combine_POP.md> "Attribute Combine POP") | In POP(s) | Operator | ✅   
In Attributes | Basic | ✅   
[Attribute Convert POP](<./Attribute_Convert_POP.md> "Attribute Convert POP") | Attribute Name | Basic | ✅   
[Attribute POP](<./Attribute_POP.md> "Attribute POP") | Delete Point Attributes | Basic | ✅   
Delete Vertex Attributes | Basic | ✅   
Delete Primitive Attributes | Basic | ✅   
[Blend POP](<./Blend_POP.md> "Blend POP") | In POP(s) | Operator | ✅   
Point Attribute Scope | Basic | ✅   
Primitive Attribute Scope | Basic | ✅   
Vertex Attribute Scope | Basic | ✅   
[Copy POP](<./Copy_POP.md> "Copy POP") | Names | Basic | ✅   
[Curve POP](<./Curve_POP.md> "Curve POP") | Lookup Index Attribute | Basic | ✅   
[Delete POP](<./Delete_POP.md> "Delete POP") | Pattern | Index | ✅   
[DMX Out POP](<./DMX_Out_POP.md> "DMX Out POP") | DMX Fixture POPs | Operator | ✅   
Local IP Pattern | Basic |   
[GLSL Advanced POP](<./GLSL_Advanced_POP.md> "GLSL Advanced POP") | In POPs | Operator | ✅   
Point Output Attributes | Basic | ✅   
Prim Output Attributes | Basic | ✅   
Vert Output Attributes | Basic | ✅   
[GLSL Copy POP](<./GLSL_Copy_POP.md> "GLSL Copy POP") | Point Output Attributes | Basic | ✅   
Vert Ouput Attributes | Basic | ✅   
Prim Output Attributes | Basic | ✅   
[GLSL POP](<./GLSL_POP.md> "GLSL POP") | In POPs | Operator | ✅   
Output Attributes | Basic | ✅   
[Group POP](<./Group_POP.md> "Group POP") | Pattern | Index | ✅   
[Lookup Attribute POP](<./Lookup_Attribute_POP.md> "Lookup Attribute POP") | Lookup Index Attribute(s) | Basic | ✅   
[Math Combine POP](<./Math_Combine_POP.md> "Math Combine POP") | In POP(s) | Operator | ✅   
[Merge POP](<./Merge_POP.md> "Merge POP") | In POP(s) | Operator | ✅   
[Neighbor POP](<./Neighbor_POP.md> "Neighbor POP") | Neighbor Point Attributes | Basic | ✅   
[Particle POP](<./Particle_POP.md> "Particle POP") | In Attributes | Basic | ✅   
[Primitive POP](<./Primitive_POP.md> "Primitive POP") | Point Index Pattern | Index (Ordered) |   
[Ray POP](<./Ray_POP.md> "Ray POP") | Hit Point Attr Scope | Basic | ✅   
Hit Primitive Attr Scope | Basic | ✅   
Hit Vertex Attr Scope | Basic | ✅   
[Select POP](<./Select_POP.md> "Select POP") | Point Attribute Scope | Basic | ✅   
Primitive Attribute Scope | Basic | ✅   
Vertex Attribute Scope | Basic | ✅   
[Sprinkle POP](<./Sprinkle_POP.md> "Sprinkle POP") | Point Attribute Scope | Basic | ✅   
Primitive Attribute Scope | Basic | ✅   
Vertex Attribute Scope | Basic | ✅   
[Switch POP](<./Switch_POP.md> "Switch POP") | In POP(s) | Operator | ✅   
Point Attribute Scope | Basic | ✅   
Primitive Attribute Scope | Basic | ✅   
Vertex Attribute Scope | Basic | ✅   
  
## DAT

Node | Parameter Name | Pattern Type | Supports Set Matching   
---|---|---|---  
[Art-Net DAT](<./Art-Net_DAT.md> "Art-Net DAT") | Local IP Pattern | Basic |   
[CHOP Execute DAT](<./CHOP_Execute_DAT.md> "CHOP Execute DAT") | CHOPs | Operator | ✅   
[Clip DAT](<./Clip_DAT.md> "Clip DAT") | Component | Operator | ✅   
[DAT Execute DAT](<./DAT_Execute_DAT.md> "DAT Execute DAT") | DATs | Operator | ✅   
[DMX Map DAT](<./DMX_Map_DAT.md> "DMX Map DAT") | Net Filter | Basic |   
Subnet Filter | Basic |   
Universe Filter | Basic |   
Network Address Filter | Basic |   
[Evaluate DAT](<./Evaluate_DAT.md> "Evaluate DAT") | Row Select Values | Basic | ✅   
Col Select Values | Basic | ✅   
[Keyboard In DAT](<./Keyboard_In_DAT.md> "Keyboard In DAT") | Panels | Operator | ✅   
[Merge DAT](<./Merge_DAT.md> "Merge DAT") | DATs | Operator | ✅   
[OP Execute DAT](<./OP_Execute_DAT.md> "OP Execute DAT") | Monitor OPs | Operator | ✅   
[OP Find DAT](<./OP_Find_DAT.md> "OP Find DAT") | Name | Basic |   
Type | Basic |   
Parent Shortcut | Basic |   
OP Shortcut | Basic |   
Path | Basic |   
Parent Path (relative) | Basic |   
Wire Path | Basic |   
Comment | Basic |   
Tags | Basic |   
DAT Text | Basic |   
Par Name | Basic |   
Par Value | Basic |   
Par Expression | Basic |   
[OSC In DAT](<./OSC_In_DAT.md> "OSC In DAT") | Local IP Pattern | Basic |   
[OSC Out DAT](<./OSC_Out_DAT.md> "OSC Out DAT") | Local IP Pattern | Basic |   
[Panel Execute DAT](<./Panel_Execute_DAT.md> "Panel Execute DAT") | Panels | Operator | ✅   
[Parameter DAT](<./Parameter_DAT.md> "Parameter DAT") | Operators | Operator | ✅   
[Parameter Execute DAT](<./Parameter_Execute_DAT.md> "Parameter Execute DAT") | OPs | Operator | ✅   
[ParGroup Execute DAT](<./ParGroup_Execute_DAT.md> "ParGroup Execute DAT") | OPs | Operator | ✅   
[POP to DAT](<./POP_to_DAT.md> "POP to DAT") | Attributes | Basic | ✅   
[Select DAT](<./Select_DAT.md> "Select DAT") | Row Select Values | Basic | ✅   
Col Select Values | Basic | ✅   
[SOP to DAT](<./SOP_to_DAT.md> "SOP to DAT") | Attributes | Basic | ✅   
[Substitute DAT](<./Substitute_DAT.md> "Substitute DAT") | Row Select Values | Basic | ✅   
Col Select Values | Basic | ✅   
[TCP/IP DAT](<./TCP/IP_DAT.md> "TCP/IP DAT") | Local IP Pattern | Basic |   
[Touch In DAT](<./Touch_In_DAT.md> "Touch In DAT") | Local IP Pattern | Basic |   
[Touch Out DAT](<./Touch_Out_DAT.md> "Touch Out DAT") | Local IP PatternF | Basic |   
[UDP In DAT](<./UDP_In_DAT.md> "UDP In DAT") | Local IP Pattern | Basic |   
[UDP Out DAT](<./UDP_Out_DAT.md> "UDP Out DAT") | Local IP Pattern | Basic | ✅   
  
## CHOP

Node | Parameter Name | Pattern Type | Supports Set Matching   
---|---|---|---  
[Audio Render CHOP](<./Audio_Render_CHOP.md> "Audio Render CHOP") | Mesh SOPs | Operator | ✅   
[DAT to CHOP](<./DAT_to_CHOP.md> "DAT to CHOP") | Row Select Values | Basic |   
Col Select Values | Basic |   
[Delete CHOP](<./Delete_CHOP.md> "Delete CHOP") | Channel Names | Basic | ✅   
Channel Numbers | Index | ✅   
[DMX In CHOP](<./DMX_In_CHOP.md> "DMX In CHOP") | Local IP Pattern | Basic |   
Start Codes | Basic |   
[DMX Out CHOP](<./DMX_Out_CHOP.md> "DMX Out CHOP") | Local IP Pattern | Basic |   
[EtherDream CHOP](<./EtherDream_CHOP.md> "EtherDream CHOP") | Local IP Pattern | Basic |   
[FreeD CHOP](<./FreeD_CHOP.md> "FreeD CHOP") | Local IP Pattern | Basic |   
[FreeD Out CHOP](<./FreeD_Out_CHOP.md> "FreeD Out CHOP") | Local IP Pattern | Basic |   
[Join CHOP](<./Join_CHOP.md> "Join CHOP") | CHOPs | Operator | ✅   
[Keyboard In CHOP](<./Keyboard_In_CHOP.md> "Keyboard In CHOP") | Panels | Operator | ✅   
[MIDI In CHOP](<./MIDI_In_CHOP.md> "MIDI In CHOP") | Note Scope | Index | ✅   
Controller Index | Index | ✅   
MIDI Channels | Index | ✅   
[MIDI In Map CHOP](<./MIDI_In_Map_CHOP.md> "MIDI In Map CHOP") | Sliders | Basic | ✅   
Buttons | Basic | ✅   
[MoSys CHOP](<./MoSys_CHOP.md> "MoSys CHOP") | Local IP Pattern | Basic |   
[Mouse In CHOP](<./Mouse_In_CHOP.md> "Mouse In CHOP") | Panels | Operator | ✅   
[Ncam CHOP](<./Ncam_CHOP.md> "Ncam CHOP") | Local IP Pattern | Basic |   
[OptiTrack In CHOP](<./OptiTrack_In_CHOP.md> "OptiTrack In CHOP") | Local IP Pattern | Basic |   
[OSC In CHOP](<./OSC_In_CHOP.md> "OSC In CHOP") | Local IP Pattern | Basic |   
[OSC Out CHOP](<./OSC_Out_CHOP.md> "OSC Out CHOP") | Local IP Pattern | Basic |   
[Parameter CHOP](<./Parameter_CHOP.md> "Parameter CHOP") | Operators | Operator | ✅   
Rename From | Basic |   
Sequences | Basic |   
ParGroups | Basic |   
Parameters | Basic |   
[PosiStageNet CHOP](<./PosiStageNet_CHOP.md> "PosiStageNet CHOP") | Local IP Pattern | Basic |   
[Reorder CHOP](<./Reorder_CHOP.md> "Reorder CHOP") | Character Pattern | Basic |   
Numeric Pattern | Index | ✅   
[Select CHOP](<./Select_CHOP.md> "Select CHOP") | CHOPs | Operator | ✅   
Channel Names | Basic | ✅   
Rename From | Basic |   
[Sequencer CHOP](<./Sequencer_CHOP.md> "Sequencer CHOP") | Add Scope | Basic |   
Blend Scope | Basic |   
[Sort CHOP](<./Sort_CHOP.md> "Sort CHOP") | Channel Names | Basic |   
Channel Indices | Index | ✅   
[Stype CHOP](<./Stype_CHOP.md> "Stype CHOP") | Local IP Pattern | Basic |   
[Stype Out CHOP](<./Stype_Out_CHOP.md> "Stype Out CHOP") | Local IP Pattern | Basic |   
[Sync In CHOP](<./Sync_In_CHOP.md> "Sync In CHOP") | Local IP Pattern | Basic |   
[Sync Out CHOP](<./Sync_Out_CHOP.md> "Sync Out CHOP") | Local IP Pattern | Basic |   
  
## TOP

Node | Parameter Name | Pattern Type | Supports Set Matching   
---|---|---|---  
[Composite TOP](<./Composite_TOP.md> "Composite TOP") | TOPs | Operator | ✅   
[GLSL TOP](<./GLSL_TOP.md> "GLSL TOP") | TOPs | Operator | ✅   
[Layout TOP](<./Layout_TOP.md> "Layout TOP") | TOPs | Operator | ✅   
[NVIDIA Flow TOP](<./NVIDIA_Flow_TOP.md> "NVIDIA Flow TOP") | Flow Emitters | Operator | ✅   
[Ouster TOP](<./Ouster_TOP.md> "Ouster TOP") | Local IP Pattern | Basic |   
[Render TOP](<./Render_TOP.md> "Render TOP") | Geometry | Operator | ✅   
Lights | Operator | ✅   
Cameras | Operator | ✅   
  
## SOP

Node | Parameter Name | Pattern Type | Supports Set Matching   
---|---|---|---  
[DAT to SOP](<./DAT_to_SOP.md> "DAT to SOP") | Add Float Attributes | Basic | ✅   
Add Int Attributes | Basic | ✅   
Add String Attributes | Basic | ✅   
[Merge SOP](<./Merge_SOP.md> "Merge SOP") | SOPs | Operator | ✅   
[Object Merge SOP](<./Object_Merge_SOP.md> "Object Merge SOP") | SOP | Operator | ✅   
[Select SOP](<./Select_SOP.md> "Select SOP") | SOPs | Operator | ✅   
  
## See Also
* [Pattern Expansion](<./Pattern_Expansion.md> "Pattern Expansion"), [Pattern Replacement](<./Pattern_Replacement.md> "Pattern Replacement"), Pattern Matching Support
