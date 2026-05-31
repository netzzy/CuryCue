# USD In TouchDesigner

**Summary**  
  
The USD stands for Universal Scene Description which is a pipeline for defining, composing and reading hierarchical scene description. It was developed by Pixar and is the core of its 3D graphics pipeline. It provides a scene description of models and shots to be consumed by all Pixar’s rendering application systems as well as other third-party applications. 

USD facilitates the collaboration of multiple artists or content creators to work on the same scene and assets. This means that they have the capability to make their own assemblies, packaging, edit their assets and data, or define variant sets to a have switchable discrete set of alternatives of scene tree. 

For detailed description of USD features and API refer to <https://graphics.pixar.com/usd/docs/>

TouchDesigner currently reads USD file and does not write USD files. 

See also [USD COMP](<./USD_COMP.md> "USD COMP"), [USD](<./USD.md> "USD"). 

  
**Importing USD File**

In TouchDesigner the USD COMP node is used to import the USD files. Once the file is loaded in TouchDesigner, a hierarchical tree of nodes will be created. The type of the nodes depends on what is available in the imported USD file, but at the minimum it is expected to see [Geometry COMP](<./Geometry_COMP.md> "Geometry COMP")/[Null COMP](<./Null_COMP.md> "Null COMP") to represent the transformation operators (i.e. Xforms prim type within USD file) or Scope prim and [Import Select SOP](<./Import_Select_SOP.md> "Import Select SOP") nodes for geometric primitives. Other common types of nodes are [Camera COMP](<./Camera_COMP.md> "Camera COMP") and [Import Select CHOP](<./Import_Select_CHOP.md> "Import Select CHOP") for animated transformation or to represent PointInstancer which will be explained shortly, [Import Select TOP](<./Import_Select_TOP.md> "Import Select TOP") for uv texture assets, and MAT nodes. 

By default, the hierarchy of nodes in TouchDesigner is mostly the same as the USD file hierarchy of primitives, however in some cases extra nodes are added in the path for better compatibilities or some special nodes moved around. An example of these cases is adding a [Geometry COMP](<./Geometry_COMP.md> "Geometry COMP") for any geometry type primitives such as meshes that have their own animated transformation, while in the USD file there are not defined as transform primitives. This helps users to be able to observe the transformation changes as the time changes. 

**Supported Geometries**

The supported USD geometric primitive schemas in TouchDesigner are meshes, geomsubsets, points, basis curves (currently Bezier curves is supported and for other types of curves such as B-Splines, Hermite, etc. the interpolation is treated like the linear curves), NURBS Curves, and NURBS surfaces. Each of these primitives are represented in their own ImportSelect SOP and recognized by their unique internal hierarchy path within the original USD file (i.e.`SdfPath`). Nevertheless, in each [Import Select SOP](<./Import_Select_SOP.md> "Import Select SOP"), it is also possible to select another primitive just by clicking the path menu and choose and replace the current primitive by the selected primitive. For large USD files with lots of geometric primitives, it is recommended to keep track of what has been replaced with the original primitive. 

  
**USD-TouchDesigner Attribute Conversions**

Attributes in USD are property type of primitives that have one of the standard types (<https://graphics.pixar.com/usd/docs/api/_usd__page__datatypes.html>) and can have a default and uniform value or various values at each time sample. Most of the standard attribute types are supported in TouchDesigner. The Primvars or Primitive Variables are special kinds of attributes dedicated for geometric primitives that can have different interpolation types for the values of the attributes over the surface of a primitive. The Primvars in USD are considered as custom attributes in TouchDesigner and their interpolations types will be converted as of the standard types in TouchDesigner (i.e. Point, Vertex, and Primitive). 

  
**Materials and Shading**

Materials in USD is a container primitive that includes Shading nodes for a renderer. Each geometry specifies a binding to a material prim. It is possible that the geometry is split into several geometries where each geometry is a`UsdGeomSubset`which is this case each subset expresses its own binding to a material. There is an attribute for each subset that is called “`familyName`” and this value has to be “`materialBind`”, otherwise the binding material will be ignored. 

The materials can also have different variants (variant-set) where each variant can have different parameter values or shader network. Each material can be referenced to another asset, so in this case it is like copying the material along with its network to that asset. 

There are three types of “terminal” outputs for each material: surface, displacement, and volume. The material prim can have any number of these outputs and each output points to a shader node within the material network. Currently we support the “surface” output type which is directly applied to the surface of a geometry. 

In TouchDesigner, the material types are either a [PBR MAT](<./PBR_MAT.md> "PBR MAT") or [Phong MAT](<./Phong_MAT.md> "Phong MAT") nodes, and the asset files such as normal maps, uv texture and so forth are loaded as [Import Select TOP](<./Import_Select_TOP.md> "Import Select TOP") nodes which will be at the same level of the MAT node. The location of MAT node corresponds to its path within USD file, meaning that if a material is defined inside a Scope prim at the root level, the material should be found at that location. For the performance purpose, if a mesh prim doesn’t have an xform parent, we add an extra Geometry COMP for that mesh primitive and reference the binding MAT to its new COMP parent. 

The Material shader network is handled internally, meaning that the output of each shader node is passed to the next node and the results are reflected to a one single MAT node, therefore you may not find a specific node for the shaders. The`UsdGeomSubset`in TouchDesigner does not have a new SOP type, and since at each time one MAT node can be applied to a geometry, we split the parent mesh into multiple [Import Select SOP](<./Import_Select_SOP.md> "Import Select SOP") nodes. These new SOP nodes cannot be merged together via Merge Geometry parameter if they have different material bindings. This applies to all the SOPs within the USD network as well, that two SOP nodes are unmergeable if each have different material binding. 

  
**Other Supported USD Features**

In TouchDesigner, the USD **PointIntancer** is represented as a [Geometry COMP](<./Geometry_COMP.md> "Geometry COMP") with the Instancing parameter set to be ON. The PointInstancer in USD is a vectorized instancing of multiple prototypes which can be a prim or subtree in a USD stage. It is designed to scale billions of instances and can be used for masking/pruning of instances base on an integer id. In other words, each PointInstancer can represent any number of instances (prototypes) from one primitive and each integer id is a per instance index (protoIndex) relationship that identifies which geometry must be rendered for this instance. If authored, the transformation operators and orientation vectors of the PointInstacer are shown as separate tracks within [Import Select CHOP](<./Import_Select_CHOP.md> "Import Select CHOP") where each point on the track shows per-instance transformation (translation, rotation, and scale) and orientation value. This CHOP node is referenced in the [Geometry COMP](<./Geometry_COMP.md> "Geometry COMP"). If velocity is authored, it can affect the interpolation of the positions of each instance. The same for angular velocities that affects the instances orientations. 

The USD **Relationship** is a namespace pointer that can target (express interests in) one or more primitives, properties and relationships in a scene graph. 

TouchDesigner supports **SubLayering** and override features of a USD file. Perhaps one of the most powerful features of USD is the **Composition Arcs** operators that allows assembling of multiple layers togethers and relate them as a list-editing layers that can be resolved in a strength-order (from most to least order) to avoid conflicts of different artists working together simultaneously on a same file where each can have their own layer <https://graphics.pixar.com/usd/docs/USD-Glossary.html#USDGlossary-LayerStack>. Sublayering is a composition arc to create LayerStack of a layer. Another type of the Composition Arcs is **Variant-Sets** which allows to have a switch between various primitives or properties. A variant can contain a subtree of prims and basically have any scene descriptions. 

After Layering, the next most important composition mechanism is a **Reference**. It allows external scene descriptions layers to be instantiated in another scene description without copying the content of the referenced scene. This is comparable in certain respects to pointers, or header include files in C++, including their recursive nature. 

**Instancing** is another USD feature that provides the ability of having many instances of one object sharing the same representation within a stage. This feature helps with improving the performance in both memory and speed. To leverage this performance gain, in TouchDesigner, for all geometric instances of each “master” primitive, only the path of one of the instances is used and all other instances re-used the same geometry while keeping their own individual transformation. 

  
**Merging**

The **Merging** feature is a way to increase the performance of the USD COMP and helps to have less nodes within network hierarchy. By turning on the merging feature we merge the mergeable SOPs and Geometry COMPs, so each node can be merged with its compatible operator. We divide the nodes within TouchDesginer USD network into mergeable and unmergeable. The mergeable SOPs depends on whether they are animated or static, have PointInstancer type parent, have same binding material, or have the same parent or not. The animated SOPs are merged together and the same goes for static SOPs. The SOPs that have the PointInstancer type parent are unmergeable. If two SOPs do not have the same parent, they cannot be merged together as well. The merging has another attribute or parameter called merging level. The merging level defines ideally how far from the root node of the USD network we expect the nodes merge together. We call it ideally because some nodes are flagged as unmergeable, therefore their subtree may not reach to the specified level that is desired. The merging starts from the bottom of the network, however once the USD is created each node has a level number starting from 1 which is the root node and the level value increases for the children of each node by 1. Note that all children of one node within the hierarchy have the same level number and this value is the same for the children of sibling of their parent. 

The merging of the Geometry or Null COMPs is essentially multiplication of their transformation values from their xform tab. The unmergeable [Geometry COMPs](<./Geometry_COMP.md> "Geometry COMP") are those that have animated transformation. The other unmergeable nodes are the [Import Select CHOP](<./Import_Select_CHOP.md> "Import Select CHOP") node(s) that represents the animated COMPs, and the [Import Select CHOPs](<./Import_Select_CHOP.md> "Import Select CHOP") that are used for PointInstancer types. 

  
**Glossary**

**SdfPath** : assigns unique paths within a USD file for each of the objects in a namespace hierarchy. 

**xform** : is a short form of USD transformation which is a`UsdGeomXformable`schema. This Xformable is essentially a set of ordered sequenced transformation ops of the type UsdAttribute that together make up a transformation prim. 

**PointInstancer** : The PointInstancer primitive in USD is a vectorized instancing of multiple prototypes which can be a prim or subtree in a USD stage. It is designed to scale billions of instances and can be used for masking/pruning of instances base on an integer id. In other words, each PointInstancer can represent any number of instances (prototypes) from one primitive and each integer id is a per instance index (protoIndex) relationship that identifies which geometry must be rendered for this instance. If authored, the transformation operators and orientation vectors of the PointInstacer are shown as separate tracks within an [Import Select CHOP](<./Import_Select_CHOP.md> "Import Select CHOP") where each point on the track shows its per-instance transformation (translation, rotation, and scale) and orientation value. 

**Prototype** : is any geometry throughout the file that is used for instancing in any number by PointInstancer. An animated geometry that is used as prototype stays animated after instancing by PointInstancer. Also, a prototype can contain another PointInstancer. 

**Protoindex** : is an integer ID per instance into prototypes relationship which specifies which instance must be rendered. 

**Layer** : is the basic content container inside a USD file. It can contain 1 or more PrimSpecs. Layers generally correspond to individual files (or a file insize a usdz archive). 

**Sub-layering** : 

**Attribute** : is a property type of primitives that have one of the standard types (<https://graphics.pixar.com/usd/docs/api/_usd__page__datatypes.html>) and can have a default and uniform value or various values at each time sample. 

**Opinion** : If there are variant sets to override the current composition arc, there must be a way to rule out which definitions will be ignored, and which ones stays alive. Usually within a layer the local opinions are stronger than Variant sets or inherits one. 

**Stage** : the stage is the USD abstraction for a scenegraph derived from a root USD file, and all of the referenced/layered files it composes. A stage always presents the composed view of the scene description that backs it. 

For a complete glossary, visit the official documentation site at [pixar.com](<https://graphics.pixar.com/usd/docs/USD-Glossary.html#USDGlossary-Opinions>)
