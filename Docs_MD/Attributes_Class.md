# Attributes Class

An Attributes object describes a set of [Prim](<./Prim_Class.md> "Prim Class") Class, [Point](<./Point_Class.md> "Point Class") Class, or [Vertex Class](<./Vertex_Class.md> "Vertex Class") [attributes](<./Attribute.md> "Attribute"), contained within a [SOP](<./SOP_Class.md> "SOP Class"). 

## Members`owner`→`OP`**(Read Only)** : 

> The [OP](<./OP_Class.md> "OP Class") to which this object belongs.

## Methods`[name]`→`Attribute`: 

> [Attributes](<./Attribute_Class.md> "Attribute Class") can be accessed using the [] subscript operator. 
> 
>   * name - The name of the attribute.
> 

[code]
>     attribs = scriptOP.pointAttribs # get the Attributes object
>     normals = attribs['N']
>     
[/code]`create(name, default)`→`Attribute`: 

> Create a new [Attribute](<./Attribute_Class.md> "Attribute Class"). 
> 
>   * name - The name of the attribute.
>   * default - (Optional) Specify default values for custom attributes. For standard attributes, default values are implied.
> 

> 
> Standard attributes are: N (normal), uv (texture), T (tangent), v (velocity), Cd (diffuse color). 
[code] 
>     # create a Normal attribute with implied defaults.
>     n = scriptOP.pointAttribs.create('N')
>     
>     # set the X component of the first point's Normal attribute.
>     scriptOp.points[0].N[0] = 0.3 
>     
>     # Create a Vertex Attribute called custom1 with defaults set to (0.0, 0.0)
>     n = scriptOP.vertexAttribs.create('custom1', (0.0, 0.0) )
>     
>     # Create a Primitive Attribute called custom2 defaulting to 1
>     n = scriptOP.primAttribs.create('custom2', 1 )
>     
[/code]

TouchDesigner Build: Latest\nwikieditor2022.241402021.100002018.28070before 2018.28070
