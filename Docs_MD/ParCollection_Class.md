# ParCollection Class

The ParCollection class can be used to access [Parameters](<./Par_Class.md> "Par Class"). To access a parameter you need to use its internal name, which you can obtain by hovering your mouse over the parameter name, and looking at the popup that will come up. See also [Par Class](<./Par_Class.md> "Par Class"). An operator's instance of this can be found in`OP.par`. 

## Members

This object contains a member for each parameter in the component. You can both read the value using: 
[code] 
    a = op('geo1').par.tx
    
[/code]

You can also change the value using 
[code] 
    a = op('geo1').par.tx = 4
    a = op('geo1').par.lookat = 'null1'
    
[/code]`owner`→`OP`**(Read Only)** : 

> The [OP](<./OP_Class.md> "OP Class") to which this object belongs.

## Methods`[name]`→`Par`: 

> [Parameters](<./Par_Class.md> "Par Class") may be easily accessed using the [] subscript and assignment operators. 
> 
>   * name - Must be an exact string name. Wildcards are not supported. If not found None is returned.
> 

[code]
>     p = op('base1').par['Myfloat5']
>     
[/code]

TouchDesigner Build: Latest\n2021.100002020.230602018.28070before 2018.28070
