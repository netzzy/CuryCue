# Channel Class

A Channel object describes a single [channel](<./Channel.md> "Channel") from a [CHOP](<./CHOP.md> "CHOP"). The [CHOP Class](<./CHOP_Class.md> "CHOP Class") provides many ways of accessing its individual channels. See [Working with CHOPs in Python](<./Working_with_CHOPs_in_Python.md> "Working with CHOPs in Python") for more examples of how to use this class. 

## Members`valid`→`bool`**(Read Only)** : 

> True if the referenced chanel value currently exists, False if it has been deleted.`index`→`int`**(Read Only)** : 

> The numeric index of the channel.`name`→`str`**(Read Only)** : 

> The name of the channel.`owner`→`OP`**(Read Only)** : 

> The [OP](<./OP_Class.md> "OP Class") to which this object belongs.`exports`→`list`**(Read Only)** : 

> The (possibly empty) list of [parameters](<./Par_Class.md> "Par Class") this channel currently exports to.`vals`→`list`: 

> Get or set the full list of Channel values. Modifying Channel values can only be done in Python within a [Script CHOP](<./ScriptCHOP_Class.md> "ScriptCHOP Class").

## Methods`[index]`→`float`: 

> Sample values may be easily accessed from a Channel using the [] subscript operator. 
> 
>   * index - Must be an numeric sample index. Wildcards are not supported.
> 

> 
> To get the third sample from the channel, assuming the channel has 3 or more samples: 
[code] 
>     n = op('pattern1')
>     c = n['chan1'][2] # the third sample
>     l = len(n['chan2']) # the total number of samples in the channel
>     
[/code]`eval(index)`→`float`: 

> Evaluate the channel at the specified index sample index. If no index is given, the current index based on the current time is used. 
> 
>   * index - (Optional) The sample index to evaluate at.
>`evalFrame(frame)`→`float`: 

> Evaluate the channel at the specified frame. If no frame is given, the current frame is used. 
> 
>   * frame - (Optional) The frame to evaluate at.
>`evalSeconds(secs)`→`float`: 

> Evaluate the channel at the specified seconds. If no time is given, the current time is used. 
> 
>   * secs - (Optional) The time in seconds to evaluate at.
>`numpyArray()`→`numpy.ndarray`: 

> Returns this channels data as a NumPy array with a length equal to the track length.`destroy()`→`None`: 

> Destroy and remove the actual Channel this object refers to. This operation is only valid when the channel belongs to a [ Script CHOP](<./ScriptCHOP_Class.md> "ScriptCHOP Class") or [OSC In CHOP](<./OscinCHOP_Class.md> "OscinCHOP Class") . Note: after this call, other existing Channel objects in this CHOP may no longer be valid.`average()`→`float`: 

> Returns the average value of all the channel samples.`min()`→`float`: 

> Returns the minimum value of all the channel samples.`max()`→`float`: 

> Returns the maximum value of all the channel samples.`copyNumpyArray(numpyArray)`→`None`: 

> Copies the contents of the numpyArray into the Channel sample values. 
> 
>   * numpyArray - The NumPy Array to copy. Must be shape(n), where n is the sample length of the CHOP. The data type must be float32. Modifying Channel values can only be done in Python within a [Script CHOP](<./Script_CHOP.md> "Script CHOP").
> 

### Casting to a Value

The Channel Class implements all necessary methods to be treated as a number, which in this case evaluates its current value. Therefore, an explicit call to eval() is unnecessary when used in a parameter, or in a numeric expression. 

For example, the following are equivalent in a channel: 
[code](float)n['chan1']
    n['chan1'].eval()
    
[/code]

The following are also equivalent, because the + 1 will implicitly cast the channel to a number: 
[code] 
    n['chan1'].eval() + 1
    n['chan1'] + 1
    
[/code]

TouchDesigner Build: Latest\nwikieditor2022.241402021.100002018.28070before 2018.28070
