# Prims Class

The Prims class describes the set of [prim objects](<./Prim_Class.md> "Prim Class") (primitives) owned by one [SOP](<./SOP_Class.md> "SOP Class").   
  
## Members`owner`→`OP`**(Read Only)** : 

> The [OP](<./OP_Class.md> "OP Class") to which this object belongs.

## Methods

No operator specific methods. 

### Special Functions`len(Prims)`→`int`: 

> Returns the total number of prims. 
[code]
>     a = len(op('box1').prims)
>     
[/code]`[index]`→`td.Prim`: 

> Get a specific prim given an integer index. 
[code]
>     n = op('box1').prims[0]
>     
[/code]`Iterator`→`td.Prim`: 

> Iterate over each prim. 
[code]
>     for m in op('box1').prims:
>     	# do something with m, which is a Prim
>     
[/code]

  
TouchDesigner Build: Latest\n2021.100002018.28070before 2018.28070
