# Page Class

The Page Class describes the list of custom [parameters](<./Par_Class.md> "Par Class") contained on a page. Pages are created on components via the COMP Class. See also the guide [Custom Parameters](<./Custom_Parameters.md> "Custom Parameters").   
  
Methods that create parameters return a [ParGroup](<./ParGroup_Class.md> "ParGroup Class") that was created. 

To view individual attributes of each parameter such as default, min, max, etc, see the [Par Class](<./Par_Class.md> "Par Class") documentation. 

Pages can be accessed like a Python list of parameters: 
[code] 
    page = op('button1').pages[0]	# get the page object
    print(len(page))				# number of parameters on the page 
    debug(page[0])					# first parameter on the page
    for p in pages:
    	debug(m.description)		# print all the parameters on the page
    
[/code]

## Members`name`→`bool`: 

> Get or set the name of the page.`owner`→`OP`**(Read Only)** : 

> The [OP](<./OP_Class.md> "OP Class") to which this object belongs.`parGroups`→`list`**(Read Only)** : 

> A list of [parameter groups](<./ParGroup_Class.md> "ParGroup Class") on this page. A ParGroup is the set of parameters on one line.`pars`→`list`**(Read Only)** : 

> The list of [parameters](<./Par_Class.md> "Par Class") on this page.`index`→`int`**(Read Only)** : 

> The numeric index of this page.`isCustom`→`bool`**(Read Only)** : 

> Boolean for whether this page is custom or not.

## Methods`appendOP(name, label=None, order=None, replace=True)`→`ParGroup`: 

> Create a node reference type [parameter](<./Par_Class.md> "Par Class"). This parameter will accept references to any operator. 
> 
> Returns the created [parameter group](<./ParGroup_Class.md> "ParGroup Class") object. 
> 
>   * name - The name of the parameter.
>   * label - (Keyword, Optional) The displayed label of the parameter, default will use the name argument.
>   * order - (Keyword, Optional) Specify the display order of the parameter, default is highest.
>   * replace - (Keyword, Optional) By default, replaces parameter with fresh attributes. If False, it errors if the parameter already exists.
>`appendCOMP(name, label=None, order=None, replace=True)`→`ParGroup`: 

> Create a COMP node reference type [parameter](<./Par_Class.md> "Par Class"). This parameter will only accept references to COMPs, and will refuse operators of other families. 
> 
> Returns the created [parameter group](<./ParGroup_Class.md> "ParGroup Class") object. 
> 
>   * name - The name of the parameter.
>   * label - (Keyword, Optional) The displayed label of the parameter, default will use the name argument.
>   * order - (Keyword, Optional) Specify the display order of the parameter, default is highest.
>   * replace - (Keyword, Optional) By default, replaces parameter with fresh attributes. If False, it errors if the parameter already exists.
>`appendObject(name, label=None, order=None, replace=True)`→`ParGroup`: 

> Create a 3D Object COMP node reference type [parameter](<./Par_Class.md> "Par Class"). This parameter will only accept references to 3D Object COMPs, and will refuse operators of other families. 
> 
> Returns the created [parameter group](<./ParGroup_Class.md> "ParGroup Class") object. 
> 
>   * name - The name of the parameter.
>   * label - (Keyword, Optional) The displayed label of the parameter, default will use the name argument.
>   * order - (Keyword, Optional) Specify the display order of the parameter, default is highest.
>   * replace - (Keyword, Optional) By default, replaces parameter with fresh attributes. If False, it errors if the parameter already exists.
>`appendPanelCOMP(name, label=None, order=None, replace=True)`→`ParGroup`: 

> Create a Panel COMP node reference type [parameter](<./Par_Class.md> "Par Class"). This parameter will only accept references to Panel COMPs, and will refuse operators of other families. 
> 
> Returns the created [parameter group](<./ParGroup_Class.md> "ParGroup Class") object. 
> 
>   * name - The name of the parameter.
>   * label - (Keyword, Optional) The displayed label of the parameter, default will use the name argument.
>   * order - (Keyword, Optional) Specify the display order of the parameter, default is highest.
>   * replace - (Keyword, Optional) By default, replaces parameter with fresh attributes. If False, it errors if the parameter already exists.
>`appendTOP(name, label=None, order=None, replace=True)`→`ParGroup`: 

> Create a TOP node reference type [parameter](<./Par_Class.md> "Par Class"). This parameter will only accept references to TOPs, and will refuse operators of other families. 
> 
> Returns the created [parameter group](<./ParGroup_Class.md> "ParGroup Class") object. 
> 
>   * name - The name of the parameter.
>   * label - (Keyword, Optional) The displayed label of the parameter, default will use the name argument.
>   * order - (Keyword, Optional) Specify the display order of the parameter, default is highest.
>   * replace - (Keyword, Optional) By default, replaces parameter with fresh attributes. If False, it errors if the parameter already exists.
>`appendCHOP(name, label=None, order=None, replace=True)`→`ParGroup`: 

> Create a CHOP node reference type [parameter](<./Par_Class.md> "Par Class"). This parameter will only accept references to CHOPs, and will refuse operators of other families. 
> 
> Returns the created [parameter group](<./ParGroup_Class.md> "ParGroup Class") object. 
> 
>   * name - The name of the parameter.
>   * label - (Keyword, Optional) The displayed label of the parameter, default will use the name argument.
>   * order - (Keyword, Optional) Specify the display order of the parameter, default is highest.
>   * replace - (Keyword, Optional) By default, replaces parameter with fresh attributes. If False, it errors if the parameter already exists.
>`appendSOP(name, label=None, order=None, replace=True)`→`ParGroup`: 

> Create a SOP node reference type [parameter](<./Par_Class.md> "Par Class"). This parameter will only accept references to SOPs, and will refuse operators of other families. 
> 
> Returns the created [parameter group](<./ParGroup_Class.md> "ParGroup Class") object. 
> 
>   * name - The name of the parameter.
>   * label - (Keyword, Optional) The displayed label of the parameter, default will use the name argument.
>   * order - (Keyword, Optional) Specify the display order of the parameter, default is highest.
>   * replace - (Keyword, Optional) By default, replaces parameter with fresh attributes. If False, it errors if the parameter already exists.
>`appendPOP(name, label=None, order=None, replace=True)`→`ParGroup`: 

> Create a POP node reference type [parameter](<./Par_Class.md> "Par Class"). This parameter will only accept references to POPs, and will refuse operators of other families. 
> 
> Returns the created [parameter group](<./ParGroup_Class.md> "ParGroup Class") object. 
> 
>   * name - The name of the parameter.
>   * label - (Keyword, Optional) The displayed label of the parameter, default will use the name argument.
>   * order - (Keyword, Optional) Specify the display order of the parameter, default is highest.
>   * replace - (Keyword, Optional) By default, replaces parameter with fresh attributes. If False, it errors if the parameter already exists.
>`appendMAT(name, label=None, order=None, replace=True)`→`ParGroup`: 

> Create a MAT node reference type [parameter](<./Par_Class.md> "Par Class"). This parameter will only accept references to MATs, and will refuse operators of other families. 
> 
> Returns the created [parameter group](<./ParGroup_Class.md> "ParGroup Class") object. 
> 
>   * name - The name of the parameter.
>   * label - (Keyword, Optional) The displayed label of the parameter, default will use the name argument.
>   * order - (Keyword, Optional) Specify the display order of the parameter, default is highest.
>   * replace - (Keyword, Optional) By default, replaces parameter with fresh attributes. If False, it errors if the parameter already exists.
>`appendDAT(name, label=None, order=None, replace=True)`→`ParGroup`: 

> Create a DAT node reference type [parameter](<./Par_Class.md> "Par Class"). This parameter will only accept references to DATs, and will refuse operators of other families. 
> 
> Returns the created [parameter group](<./ParGroup_Class.md> "ParGroup Class") object. 
> 
>   * name - The name of the parameter.
>   * label - (Keyword, Optional) The displayed label of the parameter, default will use the name argument.
>   * order - (Keyword, Optional) Specify the display order of the parameter, default is highest.
>   * replace - (Keyword, Optional) By default, replaces parameter with fresh attributes. If False, it errors if the parameter already exists.
>`appendInt(name, label=None, size=1, order=None, replace=True)`→`ParGroup`: 

> Create a integer type [parameter](<./Par_Class.md> "Par Class"). Returns the created [parameter group](<./ParGroup_Class.md> "ParGroup Class") object. 
> 
>   * name - The name of the parameter.
>   * label - (Keyword, Optional) The displayed label of the parameter, default will use the name argument.
>   * size - (Keyword, Optional) Set the number of values associated with the parameter. When greater than 1, the parameter will be shown as multiple float fields without a slider and multiple parameters will be created with the index of the parameter appended to the parameter name, starting at 1.
>   * order - (Keyword, Optional) Specify the display order of the parameter, default is highest.
>   * replace - (Keyword, Optional) By default, replaces parameter with fresh attributes. If False, it errors if the parameter already exists.
>`appendFloat(name, label=None, size=1, order=None, replace=True)`→`ParGroup`: 

> Create a float type [parameter](<./Par_Class.md> "Par Class"). Returns the created [parameter group](<./ParGroup_Class.md> "ParGroup Class") object. 
> 
>   * name - The name of the parameter.
>   * label - (Keyword, Optional) The displayed label of the parameter, default will use the name argument.
>   * size - (Keyword, Optional) Set the number of values associated with the parameter. When greater than 1, the parameter will be shown as multiple float fields without a slider and multiple parameters will be created with the index of the parameter appended to the parameter name, starting at 1.
>   * order - (Keyword, Optional) Specify the display order of the parameter, default is highest.
>   * replace - (Keyword, Optional) By default, replaces parameter with fresh attributes. If False, it errors if the parameter already exists.
>`appendXY(name, label=None, order=None, replace=True)`→`ParGroup`: 

> Create a XY position type [parameter](<./Par_Class.md> "Par Class"). Similar to creating a float parameter with size=2, but with more appropriate default naming. 
> 
> Returns the created [parameter group](<./ParGroup_Class.md> "ParGroup Class") object. 
> 
>   * name - The name of the parameter.
>   * label - (Keyword, Optional) The displayed label of the parameter, default will use the name argument.
>   * order - (Keyword, Optional) Specify the display order of the parameter, default is highest.
>   * replace - (Keyword, Optional) By default, replaces parameter with fresh attributes. If False, it errors if the parameter already exists.
>`appendXYZ(name, label=None, order=None, replace=True)`→`ParGroup`: 

> Create a XYZ position type [parameter](<./Par_Class.md> "Par Class"). Similar to creating a float parameter with size=3, but with more appropriate default naming. 
> 
> Returns the created [parameter group](<./ParGroup_Class.md> "ParGroup Class") object. 
> 
>   * name - The name of the parameter.
>   * label - (Keyword, Optional) The displayed label of the parameter, default will use the name argument.
>   * order - (Keyword, Optional) Specify the display order of the parameter, default is highest.
>   * replace - (Keyword, Optional) By default, replaces parameter with fresh attributes. If False, it errors if the parameter already exists.
>`appendXYZW(name, label=None, order=None, replace=True)`→`ParGroup`: 

> Create a XYZW position type [parameter](<./Par_Class.md> "Par Class"). Similar to creating a float parameter with size=4, but with more appropriate default naming. 
> 
> Returns the created [parameter group](<./ParGroup_Class.md> "ParGroup Class") object. 
> 
>   * name - The name of the parameter.
>   * label - (Keyword, Optional) The displayed label of the parameter, default will use the name argument.
>   * order - (Keyword, Optional) Specify the display order of the parameter, default is highest.
>   * replace - (Keyword, Optional) By default, replaces parameter with fresh attributes. If False, it errors if the parameter already exists.
>`appendWH(name, label=None, order=None, replace=True)`→`ParGroup`: 

> Create a WH size type [parameter](<./Par_Class.md> "Par Class"). Similar to creating a float parameter with size=2, but with more appropriate default naming. 
> 
> Returns the created [parameter group](<./ParGroup_Class.md> "ParGroup Class") object. 
> 
>   * name - The name of the parameter.
>   * label - (Keyword, Optional) The displayed label of the parameter, default will use the name argument.
>   * order - (Keyword, Optional) Specify the display order of the parameter, default is highest.
>   * replace - (Keyword, Optional) By default, replaces parameter with fresh attributes. If False, it errors if the parameter already exists.
>`appendUV(name, label=None, order=None, replace=True)`→`ParGroup`: 

> Create a UV 2D texture type [parameter](<./Par_Class.md> "Par Class"). Similar to creating a float parameter with size=2, but with more appropriate default naming. 
> 
> Returns the created [parameter group](<./ParGroup_Class.md> "ParGroup Class") object. 
> 
>   * name - The name of the parameter.
>   * label - (Keyword, Optional) The displayed label of the parameter, default will use the name argument.
>   * order - (Keyword, Optional) Specify the display order of the parameter, default is highest.
>   * replace - (Keyword, Optional) By default, replaces parameter with fresh attributes. If False, it errors if the parameter already exists.
>`appendUVW(name, label=None, order=None, replace=True)`→`ParGroup`: 

> Create a UVW 3D texture type [parameter](<./Par_Class.md> "Par Class"). Similar to creating a float parameter with size=3, but with more appropriate default naming. 
> 
> Returns the created [parameter group](<./ParGroup_Class.md> "ParGroup Class") object. 
> 
>   * name - The name of the parameter.
>   * label - (Keyword, Optional) The displayed label of the parameter, default will use the name argument.
>   * order - (Keyword, Optional) Specify the display order of the parameter, default is highest.
>   * replace - (Keyword, Optional) By default, replaces parameter with fresh attributes. If False, it errors if the parameter already exists.
>`appendRGB(name, label=None, order=None, replace=True)`→`ParGroup`: 

> Create a RGB color type [parameter](<./Par_Class.md> "Par Class"). Similar to creating a float parameter with size=3, but with more appropriate default naming. 
> 
> Returns the created [parameter group](<./ParGroup_Class.md> "ParGroup Class") object. 
> 
>   * name - The name of the parameter.
>   * label - (Keyword, Optional) The displayed label of the parameter, default will use the name argument.
>   * order - (Keyword, Optional) Specify the display order of the parameter, default is highest.
>   * replace - (Keyword, Optional) By default, replaces parameter with fresh attributes. If False, it errors if the parameter already exists.
>`appendRGBA(name, label=None, order=None, replace=True)`→`ParGroup`: 

> Create a RGBA color type [parameter](<./Par_Class.md> "Par Class"). Similar to creating a float parameter with size=4, but with more appropriate default naming. 
> 
> Returns the created [parameter group](<./ParGroup_Class.md> "ParGroup Class") object. 
> 
>   * name - The name of the parameter.
>   * label - (Keyword, Optional) The displayed label of the parameter, default will use the name argument.
>   * order - (Keyword, Optional) Specify the display order of the parameter, default is highest.
>   * replace - (Keyword, Optional) By default, replaces parameter with fresh attributes. If False, it errors if the parameter already exists.
>`appendStr(name, label=None, order=None, replace=True)`→`ParGroup`: 

> Create a string type [parameter](<./Par_Class.md> "Par Class"). Returns the created [parameter group](<./ParGroup_Class.md> "ParGroup Class") object. 
> 
>   * name - The name of the parameter.
>   * label - (Keyword, Optional) The displayed label of the parameter, default will use the name argument.
>   * order - (Keyword, Optional) Specify the display order of the parameter, default is highest.
>   * replace - (Keyword, Optional) By default, replaces parameter with fresh attributes. If False, it errors if the parameter already exists.
>`appendStrMenu(name, label=None, order=None, replace=True)`→`ParGroup`: 

> Create a menu type [parameter](<./Par_Class.md> "Par Class"). Returns the created [parameter group](<./ParGroup_Class.md> "ParGroup Class") object. 
> 
>   * name - The name of the parameter.
>   * label - (Keyword, Optional) The displayed label of the parameter, default will use the name argument.
>   * order - (Keyword, Optional) Specify the display order of the parameter, default is highest.
>   * replace - (Keyword, Optional) By default, replaces parameter with fresh attributes. If False, it errors if the parameter already exists.
>`appendMenu(name, label=None, order=None, replace=True)`→`ParGroup`: 

> Create a menu type [parameter](<./Par_Class.md> "Par Class"). Returns the created [parameter group](<./ParGroup_Class.md> "ParGroup Class") object. 
> 
> To set the actual menu entries, use the [Par](<./Par_Class.md> "Par Class") members: .menuNames and .menuLabels. 
> 
>   * name - The name of the parameter.
>   * label - (Keyword, Optional) The displayed label of the parameter, default will use the name argument.
>   * order - (Keyword, Optional) Specify the display order of the parameter, default is highest.
>   * replace - (Keyword, Optional) By default, replaces parameter with fresh attributes. If False, it errors if the parameter already exists.
>`appendFile(name, label=None, order=None, replace=True)`→`ParGroup`: 

> Create a file reference type [parameter](<./Par_Class.md> "Par Class"). Has built-in functionality to open a new file picker window. 
> 
> Returns the created [parameter group](<./ParGroup_Class.md> "ParGroup Class") object. 
> 
>   * name - The name of the parameter.
>   * label - (Keyword, Optional) The displayed label of the parameter, default will use the name argument.
>   * order - (Keyword, Optional) Specify the display order of the parameter, default is highest.
>   * replace - (Keyword, Optional) By default, replaces parameter with fresh attributes. If False, it errors if the parameter already exists.
>`appendFileSave(name, label=None, order=None, replace=True)`→`ParGroup`: 

> Create a file save reference type parameter. Has built-in functionality to open a new file picker window. 
> 
> Returns the created parameter objects. 
> 
>   * name - The name of the parameter.
>   * label - (Keyword, Optional) The displayed label of the parameter, default will use the name argument.
>   * order - (Keyword, Optional) Specify the display order of the parameter, default is highest.
>   * replace - (Keyword, Optional) By default, replaces parameter with fresh attributes. If False, it errors if the parameter already exists.
>`appendFolder(name, label=None, order=None, replace=True)`→`ParGroup`: 

> Create a folder reference type [parameter](<./Par_Class.md> "Par Class"). Has built-in functionality to open a new folder picker window. 
> 
> Returns the created [parameter group](<./ParGroup_Class.md> "ParGroup Class") object. 
> 
>   * name - The name of the parameter.
>   * label - (Keyword, Optional) The displayed label of the parameter, default will use the name argument.
>   * order - (Keyword, Optional) Specify the display order of the parameter, default is highest.
>   * replace - (Keyword, Optional) By default, replaces parameter with fresh attributes. If False, it errors if the parameter already exists.
>`appendPulse(name, label=None, order=None, replace=True)`→`ParGroup`: 

> Create a pulse button type [parameter](<./Par_Class.md> "Par Class"). Returns the created [parameter group](<./ParGroup_Class.md> "ParGroup Class") object. 
> 
>   * name - The name of the parameter.
>   * label - (Keyword, Optional) The displayed label of the parameter, default will use the name argument.
>   * order - (Keyword, Optional) Specify the display order of the parameter, default is highest.
>   * replace - (Keyword, Optional) By default, replaces parameter with fresh attributes. If False, it errors if the parameter already exists.
>`appendMomentary(name, label=None, order=None, replace=True)`→`ParGroup`: 

> Create a momentary button type [parameter](<./Par_Class.md> "Par Class"). Returns the created [parameter group](<./ParGroup_Class.md> "ParGroup Class") object. 
> 
>   * name - The name of the parameter.
>   * label - (Keyword, Optional) The displayed label of the parameter, default will use the name argument.
>   * order - (Keyword, Optional) Specify the display order of the parameter, default is highest.
>   * replace - (Keyword, Optional) By default, replaces parameter with fresh attributes. If False, it errors if the parameter already exists.
>`appendToggle(name, label=None, order=None, replace=True)`→`ParGroup`: 

> Create a toggle button type [parameter](<./Par_Class.md> "Par Class"). Returns the created [parameter group](<./ParGroup_Class.md> "ParGroup Class") object. 
> 
>   * name - The name of the parameter.
>   * label - (Keyword, Optional) The displayed label of the parameter, default will use the name argument.
>   * order - (Keyword, Optional) Specify the display order of the parameter, default is highest.
>   * replace - (Keyword, Optional) By default, replaces parameter with fresh attributes. If False, it errors if the parameter already exists.
>`appendPython(name, label=None, order=None, replace=True)`→`ParGroup`: 

> Create a python expression [parameter](<./Par_Class.md> "Par Class"). Returns the created [parameter group](<./ParGroup_Class.md> "ParGroup Class") object. 
> 
>   * name - The name of the parameter.
>   * label - (Keyword, Optional) The displayed label of the parameter, default will use the name argument.
>   * order - (Keyword, Optional) Specify the display order of the parameter, default is highest.
>   * replace - (Keyword, Optional) By default, replaces parameter with fresh attributes. If False, it errors if the parameter already exists.
>`appendParGroup(name, parGroup=None, label=None, order=None, replace=True)`→`ParGroup`: 

> Create a parGroup with attributes copied from an existing parameter. Returns the created [parameter group](<./ParGroup_Class.md> "ParGroup Class") object. 
> 
>   * name - The name of the parameter. Built-in names can be used as they will be automatically adjusted to match proper custom name casing (begin with uppercase letter followed by lowercase letters and numbers only).
>   * parGroup - (Keyword, Optional) The parameter group to copy attributes from. If none specified, a default parameter created.
>   * label - (Keyword, Optional) The displayed label of the parameter, default will use the name argument.
>   * order - (Keyword, Optional) Specify the display order of the parameter, default is highest.
>   * replace - (Keyword, Optional) By default, replaces parameter with fresh attributes. If False, it errors if the parameter already exists.
>`appendHeader(name, label=None, order=None, replace=True)`→`ParGroup`: 

> Create a header parameter. Returns the created [parameter group](<./ParGroup_Class.md> "ParGroup Class") object. Only the value will be shown, not its label. 
> 
>   * name - The name of the parameter.
>   * label - (Keyword, Optional) The displayed label of the parameter, default will use the name argument.
>   * order - (Keyword, Optional) Specify the display order of the parameter, default is highest.
>   * replace - (Keyword, Optional) By default, replaces parameter with fresh attributes. If False, it errors if the parameter already exists.
>`appendSequence(name, label=None, order=None, replace=True)`→`ParGroup`: 

> Create a Sequence header parameter. Returns the created [parameter group](<./ParGroup_Class.md> "ParGroup Class") object. 
> 
>   * name - The name of the parameter.
>   * label - (Keyword, Optional) The displayed label of the parameter, default will use the name argument.
>   * order - (Keyword, Optional) Specify the display order of the parameter, default is highest.
>   * replace - (Keyword, Optional) By default, replaces parameter with fresh attributes. If False, it errors if the parameter already exists.
>`destroy()`→`None`: 

> Destroy the page this object refers to, and all its parameters.`sort(*pars)`→`None`: 

> Reorder custom parameter groups or parameters in specified order. 
[code]
>     n = op('base1')
>     page = n.appendCustomPage('Custom1')
>     page.appendFloat('Value')
>     page.appendFloat('Speed')
>     page.appendFloat('Color')
>     page.sort('Speed','Color','Value')
>     
[/code]`resetPars()`→`bool`: 

> Resets all the parameters in the page. 
> 
> Returns true if anything was changed. 
[code] 
>     op('geo1').pages[0].resetPars() 
>     op('player').customPages['Setup'].resetPars()
>     
[/code]

TouchDesigner Build: Latest\nwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditormw-revertedmw-manual-revert2025.300002023.112802021.100002020.200002018.28070before 2018.28070
