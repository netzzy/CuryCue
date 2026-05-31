# Group Class

An Group describes groups lists of [Prim Class](<./Prim_Class.md> "Prim Class") or [Point Class](<./Point_Class.md> "Point Class"). 

A Group can be created with the [Group SOP](<./Group_SOP.md> "Group SOP") or using the`createPointGroup(str)`or`createPrimGroup(str)`methods of the [ScriptSOP Class](<./ScriptSOP_Class.md> "ScriptSOP Class"). 

## Members`default`→`tuple`**(Read Only)** : 

> The default values associated with this Group. It returns a tuple item of group points.`name`→`str`: 

> Set/gets the group name.`owner`→`OP`**(Read Only)** : 

> Gets the owner of this group.

## Methods`add(item : [Point](<./Point_Class.md> "Point Class") | [Prim](<./Prim_Class.md> "Prim Class") | int)`→`None`: 

> Adds a point/primitive to this group. The point or primitive to be added can be specified by a point, primitive object or the index of a point or primitive object.`discard(item : [Point](<./Point_Class.md> "Point Class") | [Prim](<./Prim_Class.md> "Prim Class") | int)`→`None`: 

> Removes a point/primitive from this group. The point or primitive to be removed can be specified by a point, primitive object or the index of a point or primitive object.`destroy()`→`None`: 

> Destroys the current point/primitive group.

TouchDesigner Build: Latest\nwikieditorwikieditor2021.10000before 2021.10000
