# Attribute Class

An [Attribute](<./Attribute.md> "Attribute") describes a general geometric Attribute, associated with a [Prim Class](<./Prim_Class.md> "Prim Class"), [Point Class](<./Point_Class.md> "Point Class"), or [Vertex Class](<./Vertex_Class.md> "Vertex Class"). Specific values for each Prim, Point or Vertex are described with the [AttributeData Class](<./AttributeData_Class.md> "AttributeData Class"). Lists of attributes for the [SOP](<./SOP_Class.md> "SOP Class") are described with the [Attributes Class](<./Attributes_Class.md> "Attributes Class").   
  
## Members`owner`→`OP`**(Read Only)** : 

> The [OP](<./OP_Class.md> "OP Class") to which this object belongs.`name`→`str`**(Read Only)** : 

> The name of this attribute.`size`→`int`**(Read Only)** : 

> The number of values associated with this attribute. For example, a normal attribute has a size of 3.`type`→`float | int | str | tuple | [TDU.Position](<./Position_Class.md> "Position Class") | [TDU.Vector](<./Vector_Class.md> "Vector Class")`**(Read Only)** : 

> The type associated with this attribute: float, integer, string, tuple, [Position](<./Position_Class.md> "Position Class"), or [Vector](<./Vector_Class.md> "Vector Class").`default`→`float | int | str | tuple | [TDU.Position](<./Position_Class.md> "Position Class") | [TDU.Vector](<./Vector_Class.md> "Vector Class")`**(Read Only)** : 

> The default values associated with this attribute. Dependent on the type of attribute, it may return a float, integer, string, tuple, [Position](<./Position_Class.md> "Position Class"), or [Vector](<./Vector_Class.md> "Vector Class").`isArray`→`bool`**(Read Only)** : 

> True if the attribute is an an array.`arraySize`→`int`**(Read Only)** : 

> The size of the array for array attributes, 0 otherwise.`numMatCols`→`int`**(Read Only)** : 

> The number of columns for matrix attributes, 0 otherwise.`numMatRows`→`int`**(Read Only)** : 

> The number of rows for matrix attributes, 0 otherwise.

## Methods`destroy()`→`None`: 

> Destroy the attribute referenced by this object. 
[code]
>     n = scriptOP.pointAttribs['N'].destroy()
>     
[/code]`vals(delayed=False)`→`list`: 

> Returns the attribute values as a list. 
> 
>   * delayed - (Keyword, Optional) If set to True, the download results will be delayed until the next call to vals(), avoiding stalling the GPU waiting for the result immediately.
> 

### Accessing Attributes

See [Attributes](<./Attributes_Class.md> "Attributes Class") for examples on how to access individual attributes. 

  
TouchDesigner Build: Latest\nwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditor2025.300002022.241402021.100002018.28070before 2018.28070
