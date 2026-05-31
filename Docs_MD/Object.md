# Object

Object Components (or`3D Objects`) are a sub-[Family](<./Operator_Family.md> "Operator Family") of all [Components](<./Component.md> "Component") and are used to define and render 3D scenes with the [Render TOP](<./Render_TOP.md> "Render TOP"). The most common object types are the [Geometry Component](<./Geometry_COMP.md> "Geometry COMP") which contain the 3D shapes defined by [SOPs](<./SOP.md> "SOP") to render, and the [Camera](<./Camera_COMP.md> "Camera COMP"), [Light](<./Light_COMP.md> "Light COMP") and [Null](<./Null_COMP.md> "Null COMP") components. 

There are sixteen 3D Object component types, found in the left column of the Components page of the OP Create menu: 
* [Ambient Light COMP](<./Ambient_Light_COMP.md> "Ambient Light COMP")
  * [Blend COMP](<./Blend_COMP.md> "Blend COMP")
  * [Bone COMP](<./Bone_COMP.md> "Bone COMP")
  * [Camera COMP](<./Camera_COMP.md> "Camera COMP")
  * [Camera Blend COMP](<./Camera_Blend_COMP.md> "Camera Blend COMP") \- multi-camera interpolation
  * [Environment Light COMP](<./Environment_Light_COMP.md> "Environment Light COMP") \- light source from a spherical environment around your scene, contributing to reflections
  * [Geometry COMP](<./Geometry_COMP.md> "Geometry COMP") \- holds the [SOPs](<./SOP.md> "SOP") that are rendered
  * [Geo Text COMP](<./Geo_Text_COMP.md> "Geo Text COMP") \- 3D text
  * [Handle COMP](<./Handle_COMP.md> "Handle COMP")
  * [Light COMP](<./Light_COMP.md> "Light COMP")
  * [Null COMP](<./Null_COMP.md> "Null COMP") \- serves only to transform 3D objects in a hierarchy
  * [Nvidia Flow Emitter COMP](<./Nvidia_Flow_Emitter_COMP.md> "Nvidia Flow Emitter COMP") \- emits fluid for the [Nvidia Flow TOP](<./Nvidia_Flow_TOP.md> "Nvidia Flow TOP")
  * [Shared Mem Out COMP](<./Shared_Mem_Out_COMP.md> "Shared Mem Out COMP"), [Shared Mem In COMP](<./Shared_Mem_In_COMP.md> "Shared Mem In COMP")
  * [FBX COMP](<./FBX_COMP.md> "FBX COMP") \- imports geometry, motion, textures from`.fbx`files
  * [USD COMP](<./USD_COMP.md> "USD COMP") \- imports geometry, motion, textures from`.usd`and`.usdc`files


"**Object Space** " refers to geometry (points in SOPs and other 3D objects) relative to a certain object, like where a point of a SOP is located relative to a camera. For this, the [Object Merge SOP](<./Object_Merge_SOP.md> "Object Merge SOP") and [Object CHOP](<./Object_CHOP.md> "Object CHOP") and is useful. A "point in Object Space" is an XYZ position expressed in a reference frame relative to the origin of a certain 3D object. 

### Python Objects

Separately, the term "Objects" is used in the context of Python scripting in TouchDesigner.
