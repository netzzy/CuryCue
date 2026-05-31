# Bezier Class

A Bezier describes an instance of a single geometry Bezier primitive (containing a set of connected Bezier curves). It is an instance of a [Prim Class](<./Prim_Class.md> "Prim Class"). It can be created from either a [Model SOP](<./ModelSOP_Class.md> "ModelSOP Class") or [Script SOP](<./ScriptSOP_Class.md> "ScriptSOP Class"). Each curve is described by a set of segments, where each segment is a list of [vertices](<./Vertex_Class.md> "Vertex Class"). The first and last vertex of each segment is an anchor position, while its neighboring vertices describe tangent handles. 

The members and methods below allow modification of the Bezier in a modelling context, however the Bezier can also be modified by direction manipulation of its vertices. See [Prim Class](<./Prim_Class.md> "Prim Class") for more details. 

## Members`anchors`→`list`**(Read Only)** : 

> Returns the list of anchor [vertices](<./Vertex_Class.md> "Vertex Class").`basis`→`list`**(Read Only)** : 

> Return the bezier basis as a list of float values.`closed`→`bool`: 

> Get or set whether the curve is closed or open.`order`→`float`**(Read Only)** : 

> Return the bezier order. The order is one more than the degree.`segments`→`list`**(Read Only)** : 

> Returns a list of segments, where each segment is a list of [vertices](<./Vertex_Class.md> "Vertex Class").`tangents`→`list`**(Read Only)** : 

> Returns the tangents as a list of [vertex](<./Vertex_Class.md> "Vertex Class") pairs.

## Methods`insertAnchor(u)`→`Vertex`: 

> inserts anchor at given position (u from 0..1) and returns anchor vertex.`updateAnchor(anchorIndex, targetPosition, tangents=True)`→`tdu.Position`: 

> Modify the anchor vertex to the new [position](<./Position_Class.md> "Position Class"). If tangents is True, modify neighboring tangent vertices as well. Returns resulting position.`appendAnchor(targetPosition, preserveShape=True)`→`Vertex`: 

> Appends a set of vertices, creating a new segment on the curve, ending with the targetPosition. 
> 
> Returns final anchor vertex. 
> 
>   * preserveShape - (Keyword, Optional) Specifies whether the new tangent will align with the previous segment or not.
>`updateTangent(tangentIndex, targetPosition, rotate=True, scale=True, rotateLock=True, scaleLock=True)`→`tdu.Position`: 

> Modify the vertex vertex to the new [position](<./Position_Class.md> "Position Class"), constraining either rotation or scale. Locked controls matching tangent. Returns resulting position.`deleteAnchor(anchorIndex)`→`None`: 

> Deletes the anchor and its neighbouring tangents.

TouchDesigner Build: Latest\n2022.241402021.100002018.28070before 2018.28070
