# TDFunctions

The **TDFunctions** module provides a variety of Python utility functions for TouchDesigner. To use TDFunctions put the following line at the top of your Python script: 
[code] 
    import TDFunctions
    
[/code]

You can now use any of the following functions by calling: 
[code] 
    TDFunctions.<function name>(...)
    
[/code]

**Note:** older versions of TouchDesigner required this to import TDFunctions:`TDFunctions = op.TDModules.mod.TDFunctions`## Methods`clamp(value, inMin, inMax)`→`float`: 

> returns the value clamped between inMin and inMax. 
> 
>   * value - The value to be clamped.
>   * inMin - The minimum value.
>   * inMax - The maximum value.
>`parentLevel(parentOp, childOp)`→`OP or None`: 

> determines if parentOp is a parent of childOp at any depth. Returns None or the depth of parenthood. i.e. childOp.parent(<returnValue>) will yield parentOp. This method returns None if childOp is not a child of parentOp. 
> 
> **Note:** childOp.parent(<returnValue>) will error in that case. 
> 
>   * parentOp - The parent to be evaluated.
>   * childOp - The child to be evaluated.
>`sharedParent(op1, op2)`→`OP or None`: 

> Returns the nearest shared parent of op1 and op2. Returns None if root is result. 
> 
>   * op1 - The first operator.
>   * op2 - The second operator.
>`getShortcutPath(fromOp, toOp, toParName=None)`→`path expression`: 

> Return a shortcut path expression from fromOp to toOp. This expression is suitable for use in any OP parameter expression on fromOp. The expression will incorporate [Parent Shortcuts](<./Parent_Shortcut.md> "Parent Shortcut") and [Global OP Shortcuts](<./Global_OP_Shortcut.md> "Global OP Shortcut"). 
> 
> **Note:** because there are multiple ways to create a shortcut expression, the result of this function will always be a best guess. 
> 
>   * fromOp - the operator to generate expression from.
>   * toOp - the operator to generate expression to.
>   * toParName - (string) if provided, the shortcut will be to that parameter on toOp.
>`panelParentShortcut(panel, parentShortcut)`→`Panel COMP or None`: 

> Return the first panelParent of panel that has the provided [parentShortcut](<./Parent_Shortcut.md> "Parent Shortcut"). Returns None if no panelParent with shortcut is found. 
> 
>   * panel - the panel to start searching at.
>   * parentShortcut - the parent shortcut to look for.
>`parMenu(menuNames, menuLabels=None)`→`menuSource object`: 

> Returns an object suitable for menuSource property of [parameters](<./Par_Class.md> "Par Class"). This is also available as`tdu.ParMenu`. 
> 
>   * menuNames - A list of strings for menu values.
>   * menuLabels - (Optional) A list of strings for menu labels. Defaults to menuNames.
>`incrementStringDigits(string, min=1, suffixOnly=False)`→`string`: 

> Method for iterating a string with digits on the end, or adding digits if none are there. This simulates the automatic naming of duplicate operators. 
> 
>   * string - The string to add digits to.
>   * min - (Optional) The number to add if string doesn't have a number already.
>   * suffixOnl - (Optional) If True, only use digits at end of string
>`findNetworkEdges(comp, ignoreNodes=None)`→`dict or None`: 

> A utility for placing nodes in a network. Returns a dictionary of 'nodes' and 'positions' at extremes of network. Returns None if no nodes found. Dictionary keys are 'top', 'left', 'right', 'bottom'. 
> 
>   * comp - The network to analyze.
>   * ignoreNodes - (Optional) A list of nodes to ignore during analysis.
>`arrangeNode(node, position='bottom', spacing=20)`→`float`: 

> Place a node according to the other nodes in the network. 
> 
>   * node - The node to move.
>   * position - (Optional) Can be 'bottom', 'top', 'left' or 'right'. left, right will be placed parallel with top nodes. top, bottom will be placed parallel with left nodes.
>   * spacing - (Optional) Distance from network edge.
>`createProperty(classInstance, name, value=None, attributeName=None, readOnly=False, dependable=True)`→`None`: 

> Use this method to add a property to a class. 
> 
> **WARNING:** the property is added to the class of instance, so all objects of instance's class will now have this property. 
> 
>   * classInstance - An instance of the class to add a property to. This is usually 'self' in the __init__ method of the class.
>   * name - The name of the property. Must be a valid Python object name.
>   * value - (Optional) The starting value of the property.
>   * attributeName - (Optional) The attribute name used to store the value of the property. Defaults to _<name>.
>   * readOnly - (Optional) If True, the property will be read only. A read only property can be changed via the attributeName. If the property is dependable, use attributeName.val.
>   * dependable - (Optional) If True, the value will be dependable. If set to "deep", collections will be deeply dependable.
>`makeDeepDependable(value)`→`dependency object`: 

> Returns a [deeply dependable](<./TDStoreTools.htm#Deeply_Dependable_Collections> "TDStoreTools") object out of the provided python object. Deeply dependable collections will cause cooks when their contents change. 
> 
>   * value - The value of the deep dependable object.
>`forceCookNonDatOps(comp)`→`None`: 

> Recursively force cook op and all children of comp, unless they are DATs`showInPane(operator, pane='Floating', inside=False)`→`None`: 

> Open an operator for viewing in a chosen editor pane. The pane will be focused on the chosen operator unless inside is True, in which case it will show the inside if possible. 
> 
>   * operator - The operator to view.
>   * pane - (Optional) A ui.pane or 'Floating' for a new floating pane.
>   * inside - (Optional) If inside is True, try to show view inside comps.
>`tScript(cmd)`→`float`: 

> Run a tscript command. This is slow because it creates and destroys an operator. If you need this to be faster, build an optimized network with its own tscript DAT. 
> 
>   * cmd - tScript command to run.
>`parStringToIntList(parString)`→`list of ints`: 

> Convert a space delimited string to a list of ints. 
> 
>   * parString - Space delimited list of ints.
>`listToParString(l)`→`space delimited string list`: 

> Convert a list to a space delimited string. 
> 
>   * l - A python list.
>`replaceOp(dest, source=None)`→`None`: 

> Replace dest with an exact copy of source. If source is None and dest is a comp, try to use dest's clone parameter. 
> 
>   * dest - The OP to be replaced.
>   * source - (Optional) The OP to replace with. If None, use dest's clone source.
>`setParDefaultsToCurrent(parList, setState=True, allowUndo=True)`→`dict`: 

> Attempt to set parameters' default settings to the parameters' current value or state. If application fails, no exception will be raised. 
> 
> Returns: {'changed': [list of pars that were changed], 'unchanged': [list of pars that were unchanged], 'error': [list of pars that errored]} 
> 
>   * parList - list of parameters to set.
>   * setState - (Optional) If True set default to current mode, otherwise set default to current constant value. Python pars always consider this arg to be True. Defaults to True.
>   * allowUndo - (Optional) If True create an undo step.
>`getParInfo(sourceOp, pattern='*', names=None, includeCustom=True, includeNonCustom=True)`→`dict`: 

> Returns a parInfo dict for sourceOp. The format of a parInfo dict is`{<parName>:(par.val, par.expr, par.mode string, par.bindExpr, par.default)...}`> 
>   * sourceOp - The operator to look for pars on.
>   * pattern - (Optional) A pattern match string for par names.
>   * names - (Optional) A list of specific names to include. None means include all.
>   * includeCustom - (Optional) Include custom parameters.
>   * includeNonCustom - (Optional) Include non-custom parameters.
>`applyParDefaults(targetOp, parInfo, raiseExceptions=False)`→`list`: 

> Attempt to apply par defaults from parInfo dict to targetOp. Ignores pageindex par. If this fails, no exception will be raised unless raiseExceptions is True! This sets the default, defaultExpr, and defaultBindExpr, not values. 
> 
>   * targetOp - The operator to apply values to.
>   * parInfo - The parInfo dict. The format of a parInfo dict is`{<parName>:(par.val, par.expr, par.mode string, par.bindExpr, par.default, par.defaultExpr, par.defaultBindExpr, par.defaultMode string)...}`>   * raiseExceptions: if True, raise an exception if any par fails to apply
>`applyParInfo(targetOp, parInfo, setDefaults=False, raiseExceptions=False)`→`list`: 

> Attempt to apply par values, expressions, and modes from parInfo dict to targetOp. Ignores pageindex par. If application fails, no exception will be raised unless raiseExceptions is True! 
> 
>   * targetOp - The operator to apply values to.
>   * parInfo - The parInfo dict. The format of a parInfo dict is`{<parName>:(par.val, par.expr, par.mode string, par.bindExpr, par.default, par.defaultExpr, par.defaultBindExpr, par.defaultMode string)...}`>   * setDefaults - if True, set the par.default as well
>   * raiseExceptions: if True, raise an exception if any par fails to apply
>`panelParentShortcut(panel, parentShortcut)`→`COMP with provided shortcut or None`: 

> return the first panelParent of panel that has the provided parentShortcut. Returns None if no panelParent with shortcut is found. 
> 
>   * panel - The panel to search from.
>   * parentShortuct - The shortcut to look for.
>`getMenuLabel(menuPar)`→`label string`: 

> Return menuPar's currently selected menu item's label 
> 
>   * menuPar - a menu style parameter
>`setMenuLabel(menuPar, label)`→`None`: 

> Sets menuPar's selected menu item to the item with menuLabel == label 
> 
>   * menuPar - a menu style parameter
>   * label - label to set menu entry to
>`messageDialog(text, title)`→`None`: 

> Open a popup dialog (after one frame delay), with just an OK button 
> 
>   * text - text of dialog
>   * title - title of dialog
>`bindChain(par, parsOnly=False)`→`list of [par, par's bind master, ...]`: 

> Return a list of parameters, starting with par, followed by its bind master, if available, followed by it's master's master if available etc. 
> 
>   * par - the parameter to start the chain search
>   * parsOnly - if True, only return parameters in the chain
>`unbindReferences(par, modeOnly=False)`→`list of references that were changed`: 

> Erase bind strings or change modes for all bindReferences of a parameter 
> 
>   * par - the bindMaster parameter
>   * modeOnly - if True, just change the references modes to prevMode
>`getCustomPage(comp, name)`→`Page object or None if name not found`: 

> Get a custom page object by name 
> 
>   * comp - comp with custom page
>   * name - page name
>`changeParStyle(p, style, size=1, includeValueData=True)`→`A list of newly created parameters`: 

> Change a parameter's style 
> 
>   * p - The parameter to change
>   * style - The style string for the parameter (e.g. 'Int', 'Float', 'Menu' etc.)
>   * size - For multivalue pars (e.g. 'Int', 'Float') the number of values 1-4
>   * includeValueData - If True, include all val, expr, bind settings
>`multiMatch(patterns, inputList, caseSensitive=True, useMinus=True)`→`list`: 

> Return a subset of`inputList`that matches`patterns`, which is similar to what you would put in a pattern matching parameter. 
> 
>   * patterns - space separate list of pattern-match strings to check
>   * inputList - list of strings to check
>   * caseSensitive - True to check case
>   * useMinus - if True, allow "-" to precede an entry in patterns to exclude from results anything that matches the entry. If False, ignore any pattern preceded by "-"
>`formatString(format, dataDict=None)`→`formatted string`: 

> format a string using f-string formatting. 
> 
> Uses an f-string style format string and a dictionary of data to return a formatted string. For more info, search "Python f-strings" or look [here](<https://realpython.com/python-f-strings/#f-strings-a-new-and-improved-way-to-format-strings-in-python>). Example usage:`formatString('{num} red balloons', {'num': 99})`... returns '99 red balloons' 
> 
>   * format (string) - the f-string to use for formatting
>   * dataDict (dict, optional) - dictionary of values available to the format string. Defaults to {}.
>
