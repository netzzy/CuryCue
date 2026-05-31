# Points Class

The Points class describes the set of [point objects](<./Point_Class.md> "Point Class") owned by one [SOP](<./SOP_Class.md> "SOP Class"). 

## Members`owner`→`OP`**(Read Only)** : 

> The [OP](<./OP_Class.md> "OP Class") to which this object belongs.

## Methods

No operator specific methods. 

### Special Functions`len(Points)`→`int`: 

> Returns the total number of points. 
[code]
>     a = len(op('box1').points)
>     
[/code]`[index]`→`td.Point`: 

> Get a specific point given an integer index. 
[code]
>     n = op('box1').points[0]
>     
[/code]`Iterator`→`td.Point`: 

> Iterate over each point. 
[code]
>     for m in op('box1').points:
>     	# do something with m, which is a Point
>     
[/code]

  
TouchDesigner Build: Latest\n2021.100002018.28070before 2018.28070
