# InputPoint Class

A Input Point is a special case of a [Point](<./Point_Class.md> "Point Class") object, only available in the [Point SOP's](<./Point_SOP.md> "Point SOP") parameters. 

The members below are unique to Input Point. See [Point Class](<./Point_Class.md> "Point Class") for other members and more information. 

## Members`color`→`[TDU.Color](<./Color_Class.md> "Color Class")`**(Read Only)** : 

> The color for this point. This is different from the Cd attribute, since it can come from a Vertex if there is no color on the inputPoint itself.`normal`→`[TDU.Vector](<./Vector_Class.md> "Vector Class")`**(Read Only)** : 

> The normal for this point. This is different from the N attribute, since it can come from a Vertex or from the destination point, if there is no normal on the inputPoint itself.`sopCenter`→`[TDU.Position](<./Position_Class.md> "Position Class")`**(Read Only)** : 

> Get the barycentric coordinate of the geometry the inputPoint is a part of. This is faster than other methods to get the center of a SOP's geometry due to internal optimizations. It is expressed as a tdu.Position.

## Methods

No operator specific methods. 

  
TouchDesigner Build: Latest\nwikieditorwikieditorwikieditorwikieditorwikieditor2021.100002018.28070before 2018.28070
