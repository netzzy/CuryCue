# Cell Class

The Cell Class describes the contents of a single cell from a [DAT](<./DAT.md> "DAT") operator table. The [DAT Class](<./DAT_Class.md> "DAT Class") offers many ways of accessing its individual cells. [DAT](<./DAT.md> "DAT") cells are always internally stored as strings, but may be accessed as numeric values. 

**IMPORTANT** :`op('table1')[1,2]`is this python cell object which usually gets converted for you to the string in the cell. More safely use`op('table1')[1,2].val`which always gives you the string. 

## Members`valid`→`bool`**(Read Only)** : 

> True if the referenced cell currently exists, False if it has been deleted.`row`→`int`**(Read Only)** : 

> The numeric row of the cell.`col`→`int`**(Read Only)** : 

> The numeric column of the cell.`owner`→`OP`**(Read Only)** : 

> The [OP](<./OP_Class.md> "OP Class") to which this object belongs.`val`→`str`: 

> Get or set the cell contents, which are always stored as a string value.

## Methods`run(*args, endFrame=False, fromOP=None, asParameter=False, group=None, delayFrames=0, delayMilliSeconds=0, wallTime=False, delayRef=None)`→`td.Run`: 

> [Run](<./Run_Class.md> "Run Class") the contents of the cell as a script, returning a Run object which can be used to optionally modify its execution. 
> 
>   * endFrame - (Keyword, Optional) If set to True, the execution will be delayed until the end of the current frame.
>   * fromOP - (Keyword, Optional) Specifies an optional [operator](<./OP_Class.md> "OP Class") from which the execution will be run relative to.
>   * asParameter - (Keyword, Optional) When fromOP used, run relative to a parameter of fromOP.
>   * group - (Keyword, Optional) Can be used to specify a group label string. This label can then be used with the [td.runs](<./Runs_Class.md> "Runs Class") object to modify its execution.
>   * delayFrames - (Keyword, Optional) Can be used to delay the execution a specific amount of frames.
>   * delayMilliSeconds - (Keyword, Optional) Can be used to delay the execution a specific amount of milliseconds. This value is rounded to the nearest frame.
>   * wallTime - (Keyword, Optional) Setting this to True results in the delay options being based on actual elapsed time instead of elapsed frames.
>   * delayRef - (Keyword, Optional) Specifies an optional [operator](<./OP_Class.md> "OP Class") from which the delay time is derived. If none is provided, will use the cell owner.
>   * arg - (Optional) Arguments that will be made available to the script in a local tuple named args.
>`offset(r, c)`→`Cell | None`: 

> The cell offset to this cell by the specified amount, or None. 
> 
>   * r - The number of rows from the cell. Positive values count down, while negative values count up.
>   * c - The number of columns from the cell. Positive values count right, while negative values count left.
> 

[code]
>     c = op('table1')['March', 'Sales']
>     d = c.offset(-1, 2)  # one row up, two columns right of cell C
>     
[/code]

### Casting to a Value

The Cell Class implements all necessary methods to be treated as a number or a string, which in this case gets or sets its value. Therefore, an explicit call to get or set val is unnecessary when used in a parameter, or in an expression. For example, the following are equivalent in a numeric parameter: 
[code](float)n[1,2]
    n[1,2].val
    n[1,2]
    
[/code]

Or equivalently, for a string parameter: 
[code](str)n[1,2]
    n[1,2].val
    n[1,2]
    
[/code]

Similarly, expressions on Cells will autocast themselves automatically: 
[code] 
    n[1,2].val + 1 # string plus 1, error
    n[1,2] + 1 # autocasted value plus 1
    
[/code]

In the second case, the contents of the Cell are used to determine if numeric or string operations should be used. For example, if cell n[1,2] contains "3" then: 
[code] 
    n[1,2].val + n[1,2].val # will return "33" since .val is a string.
    
[/code]

However, 
[code] 
    n[1,2] + n[1,2] # will return 6 since the contents "3" are numeric.
    
[/code]

If n[1,2] contained a non-numeric value such as "a" then 
[code] 
    n[1,2] + n[1,2] # will return "aa"
    
[/code]

TouchDesigner Build: Latest\nwikieditorwikieditorwikieditor2025.300002022.241402021.100002018.28070before 2018.28070
