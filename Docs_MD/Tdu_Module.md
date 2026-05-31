# TDU Class

The`TDU`class is a generic utility class containing all miscellaneous utility functions and members that don't refer specifically to TouchDesigner data structures. To access members and methods of this class use the default instance`tdu`. 

## Members`fileTypes`→`dict`**(Read Only)** : 

> A dictionary of all supported file types, organized by category. 
[code]
>     # example of various file types accepted by Movie File In TOP
>     tdu.fileTypes['movie']
>     tdu.fileTypes['image']
>     
[/code]
[code] 
>     # other file types
>     tdu.fileTypes['audio']
>     
[/code]
> 
> Note: Acceptable file types can be both uppercase and lowercase, so if`suffix`is a suffix string, you need to force it to lowercase by using`suffix.lower()`: 
[code] 
>     for suffix.lower() in tdu.fileTypes['movie']:
>     	print(suffix)
>     
[/code]`Matrix`→`TDU.Matrix`**(Read Only)** : 

> The [Matrix](<./Matrix_Class.md> "Matrix Class") definition class.`Position`→`TDU.Position`**(Read Only)** : 

> The [Position](<./Position_Class.md> "Position Class") definition class.`Vector`→`TDU.Vector`**(Read Only)** : 

> The [Vector](<./Vector_Class.md> "Vector Class") definition class.`Quaternion`→`TDU.Quaternion`**(Read Only)** : 

> The [Quaternion](<./Quaternion_Class.md> "Quaternion Class") definition class.`Color`→`TDU.Color`**(Read Only)** : 

> The [Color](<./Color_Class.md> "Color Class") definition class.`Dependency`→`TDU.Dependency`**(Read Only)** : 

> The [Dependency](<./Dependency_Class.md> "Dependency Class") definition class.`FileInfo`→`TDU.FileInfo`**(Read Only)** : 

> The FileInfo object takes a file path and has a few utility properties to provide additional information. It is derived from str, so will work as a Python string, but can be differentiated from a regular string by using`isinstance(tdu.FileInfo)`. 
> 
> Utility properties include: 
> 
>   * path: filepath string
>   * ext: string after and including "."
>   * fileType: the TD filetype (from tdu.fileTypes)
>   * absPath: the absolute path to filepath
>   * dir: the containing directory of filepath
>   * exists: exists in file-system
>   * isDir: is a directory in the file-system
>   * isFile: is a file in the file-system
>   * baseName: the name of the final element in the path
>`ArcBall`→`TDU.ArcBall`**(Read Only)** : 

> The [ArcBall](<./ArcBall_Class.md> "ArcBall Class") definition class.`Camera`→`tdu.Camera`**(Read Only)** : 

> The [Camera](<./Camera_Class.md> "Camera Class") definition class.`debug`→`module`**(Read Only)** : 

> Helper module for the builtin debug statement. [Documentation.](<./Debug_module.md> "Debug module")`Timecode`→`TDU.Timecode`**(Read Only)** : 

> The [Timecode](<./Timecode_Class.md> "Timecode Class") definition class.

## Methods`rand(seed)`→`float`: 

> Return a random value in the range [0.0, 1.0) given the input seed value. That is, it will never return 1.0, but it may return 0.0. For a given seed, it will always return the same random number. The seed does not need to be a number. If the seed is not numeric, it resolves it to its string representation to produce a unique value. In the case of OPs for example, its string representation is a constant path. Thus one can produce a unique random value for each OP which remains the same for that OP each time you reload TouchDesigner. 
[code]
>     tdu.rand(me) # return a specific random number based on path
>     tdu.rand(5) # return a specific random number
>     tdu.rand(absTime.frame) # return a different number every frame
>     
[/code]`clamp(inputVal, min, max)`→`float | int`: 

> Returns the input value clamped between min and max values. Arguments can be any type that can be compared (float, int, str, etc).`remap(inputVal, fromMin, fromMax, toMin, toMax)`→`float`: 

> Returns the input value remapped from the first range to the second. 
[code]
>     tdu.remap(0.5, 0, 1,  -180, 180)  #remap slider value to angle range
>     
[/code]`base(str)`→`str`: 

> Returns the beginning portion of the string occurring before any digits. The search begins after the last slash if any are present. 
> 
>   * str - The string to extract the base name from.
> 

[code]
>     tdu.base('arm123') # returns 'arm'
>     tdu.base('arm123/leg456') # returns 'leg'
>     
[/code]
> 
> Note this method will work on any string, but when given a specific operator, its more efficient to use its local base member: 
[code] 
>     n = op('arm123/leg456')
>     b = n.base #returns 'leg'
>     
[/code]`digits(str)`→`int | None`: 

> Returns the numeric value of the last consecutive group of digits in the string, or None if not found. The search begins after the last slash if any are present. The digits do not nessearily need to be at the end of the string. 
[code]
>     tdu.digits('arm123') # returns 123
>     tdu.digits('arm123/leg456') # returns 456
>     tdu.digits('arm123/leg') # returns None, searching is only done after the last /
>     tdu.digits('arm123/456leg') # returns 456
>     
[/code]
> 
> Note this method will work on any string, but when given a specific operator, its more efficient to use its local digits member: 
[code] 
>     n = op('arm123/leg456')
>     d = n.digits # returns 456
>     
[/code]`validName(str)`→`str`: 

> Returns a version of the string suitable for an operator name. Converts illegal characters to underscores. 
> 
> Slashes are converted to underscores. To preserve forward slashes, use validPath() instead. 
[code] 
>     tdu.validName('a#bc def') # returns 'a_bc_def'
>     
[/code]`validPath(str)`→`str`: 

> Returns a version of the string suitable for an operator path, including slashes. Converts illegal characters to underscores. 
[code]
>     tdu.validPath('/a#bc d/ef') # returns '/a_bc_d/ef'
>     
[/code]`expand(pattern)`→`list`: 

> Return a list of the expanded items, following the rules of [Pattern Expansion](<./Pattern_Expansion.md> "Pattern Expansion"). 
[code]
>     tdu.expand('A[1-3] B[xyz]') # return ['A1', 'A2', 'A3', 'Bx', 'By', 'Bz']
>     
[/code]`expandPath(path)`→`str`: 

> Expand the file path, using project.paths, the current folder, and any other relevant information. 
[code]
>     tdu.expandPath('movies:/test.bmp') # looks at project.paths for 'movies' entry.
>     
[/code]`collapsePath(path, asExpression=False)`→`str`: 

> Collapse the file path, using project.paths, the current folder, and any other relevant information. 
[code]
>     tdu.collapsePath('C:/downloads/test.bmp') # looks at project.paths for any entries matching the path, and removes current folder from prefix.
>     
[/code]
> 
>   * path - The path to be shortened.
>   * asExpression - (Keyword, Optional) If True, result can be used as an expression, including [App Class](<./App_Class.md> "App Class") members and quoted strings.
>`split(string, eval=False)`→`list`: 

> Return a list from a space separated string, allowing quote delimiters. 
> 
>   * string - Any Python object, as it will be evaluated as str(string). Parameters will work.
>   * eval - (Keyword, Optional) If True convert any valid Python literal structures: strings, numbers, tuples, lists, dicts, booleans, and None.
> 

[code]
>     split('1 2.3 None fred "one \'2\'" "[1,2]"') #yields ['1', '2.3', 'None', 'fred', "one '2'", '[1, 2]']
>     split('1 2.3 None fred "one \'2\'" "[1,2]"', True) #yields [1, 2.3, None, 'fred', "one '2'", [1, 2]]
>     
[/code]`match(pattern, inputList, caseSensitive=True)`→`list`: 

> Return a subset of inputList, in which each element matches the pattern. Wildcards are supported. 
[code]
>     tdu.match('foo*', ['foo', 'bar']) # return ['foo']
>     tdu.match('ba?', ['foo', 'bar']) # return ['bar']
>     
[/code]`forceCrash()`→`None`: 

> forces a crash for debugging and crash recovery purposes`tryExcept(func1 : Callable, func2val : Any)`→`Any`: 

> Evaluate the first function (func1). If an exception is raised, return second argument instead. Second argument can be either a function, which will be called, or a final result. **Note:** If the second argument is a function, it is only called if the first function fails. 
> 
>   * func1: the function that will be "tried"
>   * func2val: a value (returned if func1 fails) or a function (return result if func1 fails)
> 

> 
> This is a one-liner try/except function for use in parameter expressions to handle simple errors. **Tip:** always be careful when hiding errors with try/except, because it can make real problems in your code/network invisible. 
[code] 
>         tdu.tryExcept(lambda: 1/me.par.w, 0.0) # second argument is simply 0.0
>         tdu.tryExcept(lambda: 1/me.par.w, me.GetDefaultValue)   # Good:  me.GetDefaultValue not called until needed.
>         tdu.tryExcept(lambda: 1/me.par.w, me.GetDefaultValue()) # >> INCORRECT <<.  Always calls second function even if not needed.
>     
[/code]`ParMenu(menuNames, menuLabels=None)`→`TDU.MenuObject`: 

> This method uses a list of strings to create an object meant to be used as a [parameter](<./Par_Class.md> "Par Class") menu source. 
> 
>   * menuNames - A list of strings for menu values.
>   * menuLabels - (Optional) A list of strings for menu labels. Defaults to menuNames.
>`TableMenu(table, nameCol=0, labelCol=None, includeFirstRow=False)`→`TDU.MenuObject`: 

> Create a parameter menu source object based on a DAT table. 
> 
> This method uses a table to create an object meant to be used as a [parameter](<./Par_Class.md> "Par Class") menu source. 
> 
>   * table - a DAT table to get the menu information from
>   * nameCol - (Keyword, Optional) Column name or number for menuNames. Defaults to 0.
>   * labelCol - (Keyword, Optional) Column name or number for menuLabels. Defaults to None, which means to use names as labels.
>   * includeFirstRow - (Keyword, Optional) if True, include first row of table in menu entries. Defaults to False.
> 

> 
> Generally you will use this in the menuSource field in the Component Editor as follows 
[code] 
>         tdu.TableMenu(op('table1')) # use the first column of table1 as a list of menu names and labels 
>         tdu.TableMenu(op('table2'), nameCol='names', labelCol='labels') # from table2, use the column labeled 'names' as menu names, and the column labeled 'labels' as menu names
>         tdu.TableMenu(op('table3'), labelCol=1, includeFirstRow=True) # from table3, use the first column as menu names and the second column as menu labels. Include the first row of the table in those lists
>     
[/code]`isPointCloudFile(path)`→`bool`: 

> Check if the input file is a point cloud file. For .exr, the channel headers are checked. Returns true if channels ending in X,Y,Z or x,y,z are found, or if the file was saved out using Movie File Out TOP with "Save as Point Cloud" set. 
> 
> For all other types, only the file extension is checked. 
> 
>   * path - Path to the input file.
>`parSummary(OPType)`→`dict`: 

> Returns a dictionary describing the builtin parameters of the OP class provided. 
> 
>   * OPType - The OP type to describe.
> 

[code]
>     tdu.parSummary(mathCHOP) # Works on td.OP types or strings, not actual operator instances.
>     
[/code]

TouchDesigner Build: Latest\nwikieditorwikieditorwikieditorwikieditorwikieditormw-revertedmw-new-redirectmw-manual-revert2025.300002023.112802022.241402021.100002020.200002018.28070before 2018.28070
