# ParGroup Class

The ParGroup class describes an instance of a single ParGroup. 

See also [Custom Parameters](<./Custom_Parameters.md> "Custom Parameters"). 

## Members`bindExpr`→`Tuple[str, ...]`: 

> Get or set expressions that return an object to bind to. This can be used to bind this parameter's constant values to the referenced object's value. 
> 
> Example: 
[code] 
>     p.bindExpr = ("op('geo1').par.tx", "op('geo1').par.ty", "op('geo1').par.tz")
>     
[/code]
> 
> Note the outside quotes, as bindExpr is an expression, not an object.`bindMaster`→`tuple`**(Read Only)** : 

> The objects to which this parameter is bound to, possibly None.`bindRange`→`bool`: 

> Get or set parameter's range binding state. If True, min, max, clampMin, clampMax, normMin, normMax, normVal values will be based on master bind parameter. Can only be set on Custom Parameters.`bindReferences`→`tuple`**(Read Only)** : 

> The (possibly empty) lists of objects which bind to this parameter.`clampMax`→`Tuple[float, ...]`: 

> Get or set the parameter's numerical clamping behaviors. If set to`clampMax = True`, the parameter will clamp on the upper end at the value specified in max Can only be set on Custom Parameters.`clampMin`→`Tuple[bool, ...]`: 

> Get or set the parameter's numerical clamping behaviors. If set to`clampMin = True`, the parameter will clamp on the lower end at the value specified in min Can only be set on Custom Parameters.`collapsable`→`bool`**(Read Only)** : 

> Returns True if the parameter is collapsable.`collapser`→`bool`**(Read Only)** : 

> Returns True if the parameter is a parent of collapsable parameters (ie. a collapser).`default`→`tuple`: 

> Get or set the parameter's default values. Can only be set on Custom Parameters.`defaultExpr`→`Tuple[str, ...]`: 

> Get or set the parameter's default expressions. Can only be set on Custom Parameters. 
[code]
>     # value defaults to this expression.
>     op('base1').parGroup.Size.defaultExpr = ('me.time.frame', 'me.time.frame', 'me.time.frame')
>     
[/code]`defaultBindExpr`→`Tuple[str, ...]`: 

> Get or set the parameter's default bind expressions. Can only be set on Custom Parameters. 
[code]
>     # value defaults to this expression.
>     op('base1').parGroup.Size.defaultBindExpr = ('me.par.tx', 'me.par.ty', 'me.par.tz')
>     
[/code]`defaultMode`→`Tuple[ParMode, ...]`: 

> Get or set the parameter's evaluation modes. 
[code]
>     op('geo1').parGroup.t.defaultMode = (ParMode.EXPRESSION, ParMode.EXPRESSION, ParMode.EXPRESSION)
>     
[/code]
> 
> The modes are one of: ParMode.CONSTANT, ParMode.EXPRESSION, or ParMode.EXPORT, or ParMode.BIND. 
> 
> See [Parameter_Dialog#Working_with_Parameter_Modes](<./Parameter_Dialog.htm#Working_with_Parameter_Modes> "Parameter Dialog") for more information.`enable`→`bool`: 

> Get or set the parameter group's enable state. Can only be set on [Custom Parameters](<./Custom_Parameters.md> "Custom Parameters"). This will also set the enable member of all individual parameters in the group.`enableExpr`→`str`: 

> Get or set an expression that controls the enable state for this parameter group. This member is shared by all parameters and the parameter group. 
[code]
>     p.enableExpr = "me.par.X.menuIndex == 5"
>     # Note the outside quotes, as this is an expression, not an object.
>     
[/code]
> 
> **TouchDesigner 2023.30000+**
> 
> If the expression is a lambda function, it will be called once for each parameter in the parameter group, with the index as an argument... 
[code] 
>     rgbaPar.enableExpr = "lambda parIndex: parIndex < 3" # enable first 3 elements
>     rgbaPar2.enableExpr = "lambda parIndex: parIndex >= 3" # enable 4th element
>     
[/code]`exportOP`→`Tuple[OP | None, ...]`**(Read Only)** : 

> The operators exporting to this parameter.`exportSource`→`Tuple[Cell | Channel | None, ...]`**(Read Only)** : 

> tuple of objects exporting to this parameter. Examples: Cell, Channel or None.`expr`→`Tuple[str, ...]`: 

> Get or set the non-evaluated expressions only. To get the parameter's current values, regardless of the Parameter Mode (constant, expression, export or bound), use the eval() method described below. 
[code]
>     op('geo1').parGroup.t.expr = ('absTime.frame', 'absTime.frame', 'absTime.frame')  
>     # set to match current frame
>     
[/code]
> 
> When setting this member, the parameter will also be placed in expression mode. See mode member below. 
> 
> **NOTE:** For convenience, the expression is placed in double-quotes so you can safely put in expressions containing single quotes. 'a' and "a" have the same effect of enclosing strings in python.`help`→`str`: 

> Get or set a custom parameter's help text. To see any parameter's help, rollover the parameter while holding the Alt key.`isDefault`→`bool`**(Read Only)** : 

> True when the parameter value, expression and mode are in their default settings.`isCustom`→`bool`**(Read Only)** : 

> True for Custom Parameters.`isFloat`→`bool`**(Read Only)** : 

> True for floating point numeric parameters.`isInt`→`bool`**(Read Only)** : 

> True for integer numeric parameters.`isMenu`→`bool`**(Read Only)** : 

> True for menu parameters.`isMomentary`→`bool`**(Read Only)** : 

> True for momentary parameters.`isNumber`→`bool`**(Read Only)** : 

> True for numeric parameters.`isOP`→`bool`**(Read Only)** : 

> True for OP parameters.`isPulse`→`bool`**(Read Only)** : 

> True for pulse parameters.`isPython`→`bool`**(Read Only)** : 

> True for python parameters.`isSequence`→`bool`**(Read Only)** : 

> True for sequence header parameters.`isString`→`bool`**(Read Only)** : 

> True for string parameters.`isToggle`→`bool`**(Read Only)** : 

> True for toggle parameters.`label`→`str`: 

> Get or set the parameter's label. 
[code]
>     op('myOperator').parGroup.Custompar.label = 'Translate'
>     
[/code]
> 
> Can only be set on Custom Parameters.`max`→`Tuple[float, ...]`: 

> Get or set the parameter's numerical maximum values. The parameter's values will be clamped at that maximum if`clampMax = True`. Can only be set on Custom Parameters.`menuIndex`→`Tuple[int, ...]`: 

> Get or set a tuple of menu constant values by their indices.`menuLabels`→`Tuple[list[str], ...]`: 

> Get or set a tuple of lists of all possible menu choice labels. In the case of non menu parameters, None(s) are returned. Can only be set on Custom Parameters.`menuNames`→`Tuple[list[str], ...]`: 

> Get or set a tuple of lists of all possible menu choice names. In the case of non menu parameters, None(s) are returned. Can only be set on Custom Parameters.`menuSource`→`Tuple[str, ...]`: 

> Get or set a tuple of expressions that returns objects with`.menuItems``.menuNames`members. This can be used to create a custom menu whose entries dynamically follow that of another menu for example.`min`→`Tuple[float, ...]`: 

> Get or set the parameter's numerical minimum values. The parameter's values will be clamped at that minimum if`clampMin = True`for the particular Par. Can only be set on Custom Parameters.`mode`→`Tuple[ParMode, ...]`: 

> Get or set the parameter's evaluation modes. 
[code]
>     op('geo1').parGroup.t.mode = (ParMode.EXPRESSION, ParMode.EXPRESSION, ParMode.EXPRESSION)
>     
[/code]
> 
> The modes are one of:`ParMode.CONSTANT`,`ParMode.EXPRESSION`, or`ParMode.EXPORT`, or`ParMode.BIND`. 
> 
> See [Parameter_Dialog#Working_with_Parameter_Modes](<./Parameter_Dialog.htm#Working_with_Parameter_Modes> "Parameter Dialog") for more information.`name`→`str`: 

> Get or set the parameter's unique name. 
[code]
>     op('myOperator').parGroup.Custompar.name = 'Translate'
>     
[/code]
> 
> Can only be set on Custom Parameters.`baseName`→`str`: 

> Get or set the parameter's base name. This excludes any sequence prefixes, sequence indices or name suffixes. Can only be set on Custom Parameters.`normMax`→`Tuple[float, ...]`: 

> Get or set the parameter's maximum slider values if the parameter is a numerical slider. Can only be set on Custom Parameters.`normMin`→`Tuple[float, ...]`: 

> Get or set the parameter's minimum slider values if the parameter is a numerical slider. Can only be set on Custom Parameters.`normVal`→`Tuple[float, ...]`: 

> Get or set the parameter's values as a normalized slider position. Can only be set on Custom Parameters.`order`→`int`: 

> Get or set the parameter's position on the parameter page. Can only be set on Custom Parameters.`owner`→`OP`**(Read Only)** : 

> The OP to which this object belongs.`page`→`Page`: 

> Get or set the parameter page the custom parameter is part of. Can only be set on Custom Parameters.`password`→`bool`: 

> Get or set the parameter's password mode. When True all text is rendered as asterisks. Can only be set on Custom string, int or float parameters. Custom Parameters.`prevMode`→`tuple`**(Read Only)** : 

> The parameter's previous evaluation modes.`readOnly`→`bool`: 

> Get or set the parameter's read only status. When True the parameter cannot be modified through the UI, only scripting.`startSection`→`bool`: 

> Get or set the parameter's separator status. When True a visible separator is drawn between this parameter and the ones preceding it. Can only be set on Custom Parameters.`style`→`str`**(Read Only)** : 

> Describes the behavior and contents of the custom parameter. Example 'Float', 'Int', 'Pulse', 'XYZ', etc.`subLabel`→`tuple`**(Read Only)** : 

> Returns the names of the sub-label.`val`→`tuple`: 

> Get or set the constant values of the parameter only. To get the parameter's current values, regardless of the Parameter Modes (`constant`,`expression`,`export`or`bound`), use the eval() method described below. 
[code]
>     op('geo1').parGroup.t.val   # the constant values 
>     op('geo1').parGroup.t.eval()   # the evaluated parameter
>     op('geo1').parGroup.t.val = (1,2,3)
>     op('geo1').parGroup.t = (1,2,3)  #equivalent to above, more concise form
>     
[/code]
> 
> When setting this member, the parameter will also be placed in constant mode. See mode member below. 
> 
> To set a menu value by its index, use the menuIndex member as described below.`valid`→`bool`**(Read Only)** : 

> True if the referenced parameter currently exists, False if it has been deleted.`index`→`int`**(Read Only)** : 

> The parameter's order in the list.`sequence`→`Sequence | None`**(Read Only)** : 

> The [Sequence](<./Sequence_Class.md> "Sequence Class") this parGroup is a part of. None if not in a sequence.`sequenceBlock`→`SequenceBlock | None`**(Read Only)** : 

> The [SequenceBlock](<./SequenceBlock_Class.md> "SequenceBlock Class") this parGroup belongs to. None if not in a sequence.`blockIndex`→`int`**(Read Only)** : 

> The index of the parGroup within its [SequenceBlock](<./SequenceBlock_Class.md> "SequenceBlock Class"). None if not in a sequence.`sequenceIndex`→`int`**(Read Only)** : 

> The index of the parGroup's [SequenceBlock](<./SequenceBlock_Class.md> "SequenceBlock Class") in its [Sequence](<./Sequence_Class.md> "Sequence Class"). None if not in a sequence.`size`→`int`: 

> Get or set the parameter's vector size.`maxSize`→`int`**(Read Only)** : 

> Returns the maximum number of [Par](<./Par_Class.md> "Par Class") elements for this ParGroup`defaultSize`→`int`**(Read Only)** : 

> Returns the default number of [Par](<./Par_Class.md> "Par Class") elements for this ParGroup.`suffixes`→`list`**(Read Only)** : 

> Returns a list of suffixes used to name the [Par](<./Par_Class.md> "Par Class") elements of this ParGroup.

## Methods`copy(ParGroup)`→`None`: 

> Copy the specified parameter. 
> 
>   * ParGroup \- The parameter to copy.
> 

[code]
>     op('geo1').parGroup.t.copy( op('geo2').parGroup.t )
>     
[/code]`destroy()`→`None`: 

> Destroy the parameter referenced by this ParGroup. An exception will be raised if the parameter has already been destroyed. Only custom and sequential parameters can be destroyed. Destroying a sequential parameter will destroy its entire block. Note: When any parameter is destroyed, any existing parameter objects will be invalid and should be re-fetched.`eval()`→`tuple`: 

> Evaluate a parameter group. This value may be derived by the parameter group's constant value, expression, or export, dependent on its mode. 
[code]
>     a = op('geo1').parGroup.t.eval()
>     
[/code]`evalExport()`→`tuple`: 

> Evaluate the export portions of a parameter, if it contains any. This will ignore any expressions, etc. 
[code]
>     a = op('geo1').parGroup.t.evalExport()
>     
[/code]`evalExpression()`→`tuple`: 

> Evaluate the expression portions of a parameter, if it contains any. This will ignore any exports, etc. 
[code]
>     a = op('geo1').parGroup.t.evalExpression()
>     
[/code]
> 
> To evaluate an arbitrary expression string, that is not inside a parameter, see [OP.evalExpression](<./OP_Class.htm#evalExpression> "OP Class").`evalNorm()`→`Tuple[float, ...]`: 

> Similar to eval() but the returns the normalized slider values.`evalOPs()`→`Tuple[list[op], ...]`: 

> Evaluate each parameter as a series of operators. This is useful for a custom parameter that specifies a list of operator paths for example. 
[code]
>     a = op('base1').parGroup.Paths.evalOPs()
>     
[/code]`pars(pattern)`→`list`: 

> Returns a (possibly empty) list of parameter objects that match the pattern. 
> 
>   * pattern - Is a string following the Pattern Matching rules, specifying which parameters to return.
> 

[code]
>     # translate parameters
>     newlist = op('geo1').parGroup.t.pars('t?')
>     
[/code]`reset()`→`bool`: 

> Resets the parameter group to its default state. 
> 
> Returns true if anything was changed. 
[code] 
>     op('geo1').parGroup.t.reset()
>     
[/code]`isSameParGroup(parGroup : ParGroup)`→`bool`: 

> True if the provided parGroup is the same ParGroup on the same operator. Because`op('container1').parGroup.x == op('container2').parGroup.x`compares values and`op('container1').parGroup.x is op('container1').parGroup.x`is always False (because of TouchDesigner internals), you must use`isParGroup`to compare ParGroup objects. Similarly`op('container2').par.Myfloat in op('container2').customPars`will return unreliable results. 
> 
>   * parGroup - The ParGroup to compare identity with.
> 


TouchDesigner Build: Latest\nwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditormw-rollbackmw-revertedmw-revertedmw-revertedmw-reverted2025.300002023.112802022.24140before 2022.24140
