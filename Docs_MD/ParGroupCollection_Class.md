# ParGroupCollection Class

The ParGroupCollection class can be used to access [ParGroups](<./ParGroup_Class.md> "ParGroup Class"). To access a parGroup you need to use its internal name, which you can obtain by hovering your mouse over the parameter name, and looking at the popup that will come up. See also [ParGroup Class](<./ParGroup_Class.md> "ParGroup Class"). An operator's instance of this can be found in`OP.parGroup`. 

## Members

This object contains a member for each parGroup in the component. You can both read the value using: 
[code] 
    a = op('geo1').par.t
    
[/code]

You can also change the value using 
[code] 
    a = op('geo1').parGroup.tx = (1,1,1) # transform has 3 values
    a = op('geo1').parGroup.lookat = 'null1'
    
[/code]`owner`→`OP`**(Read Only)** : 

> The [OP](<./OP_Class.md> "OP Class") to which this object belongs.

## Methods`[name]`→`Par`: 

> [ParGroups](<./ParGroup_Class.md> "ParGroup Class") may be easily accessed using the [] subscript and assignment operators. 
> 
>   * name - Must be an exact string name. Wildcards are not supported. If not found None is returned.
> 

[code]
>     p = op('base1').parGroup['Myfloat5']
>     
[/code]

TouchDesigner Build: Latest\nwikieditorbefore wikieditor
