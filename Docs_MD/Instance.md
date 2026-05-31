# Instance

There are two kinds of Instancing in TouchDesigner: 

1\. Geometry instances in the [Geometry Component](<./Geometry_COMP.md> "Geometry COMP") are copies of the geometry object, which can be transformed independently. The Geometry COMP has an **Instance** parameter page to create instances. You can have one instance for every sample of a CHOP, row of a table, pixel of an image, or point of a SOP. Transformations of the instances can be made by supplying [CHOP](<./CHOP.md> "CHOP") channels with X, Y, and Z and other data, for example. 

2\. An instance is an [OP](<./Operator.md> "Operator") that doesn't actually have its own data, but rather just refers to an OP (or has an input) whose data it uses. This includes Null OPs, Select OPs and Switch OPs. In this context this is a reference to another OP's data.
