# AttributeData Class

An AttributeData contains specific geometric [Attribute](<./Attribute.md> "Attribute") values, associated with a [Prim Class](<./Prim_Class.md> "Prim Class"), [Point Class](<./Point_Class.md> "Point Class"), or [Vertex Class](<./Vertex_Class.md> "Vertex Class"). Each value of the attribute must be of the same type, and can be one of float, string or integer. For example, a point or vertex normal attribute data, consists of 3 float values. 

## Members`owner`→`OP`**(Read Only)** : 

> The [OP](<./OP_Class.md> "OP Class") to which this object belongs.`val`→`float | int | str | tuple | [TDU.Position](<./Position_Class.md> "Position Class") | [TDU.Vector](<./Vector_Class.md> "Vector Class")`**(Read Only)** : 

> The set of values contained within this object. Dependent on the type of attribute, it may return a float, integer, string, tuple, [Position](<./Position_Class.md> "Position Class"), or [Vector](<./Vector_Class.md> "Vector Class"). For example Normal attribute data is expressed as a [Vector](<./Vector_Class.md> "Vector Class"), while [Position](<./Position_Class.md> "Position Class") attribute data is expressed as a Position.

## Methods

No operator specific methods. 

  
TouchDesigner Build: Latest\nwikieditorwikieditorwikieditor2022.241402021.100002018.28070before 2018.28070
