# Optimized Python Expressions

## Overview

### Optimized Python Expressions

Starting with the 2018.20000 series of builds, a custom Python expression execution engine has been incorporated into TouchDesigner. This engine will parse Python expressions that are in parameters. Assuming the members and methods used in that expression fall into the range of members and methods the engine is aware of, it will evaluate the expression without having to use Python's engine. This generally results in a the expression evaluating in about 1/4 of the time than it does if it was evaluated through the regular Python engine. 

The goal of this feature isn't to evaluate every parameter expression using this engine, but to evaluate the most commonly used expressions. You can determine if an expression is evaluated using this engine by holding the mouse over the parameter name. It will show either **(Optimized)** or **(Unoptimized)** in the popup that will show up. The [Perform CHOP](<./Perform_CHOP.md> "Perform CHOP") has a parameter to monitor the number of optimized expressions. 

If an expression ever ends up causing an error, the engine will stop being used for that expression and the Python engine will be used instead. If the expression is changed, or on the next time the file is loaded, TouchDesigner will once again try to use the engine to evaluate the parameter. 

### Cached Python Expressions

In addition to optimized expressions, a new system that caches expression results will keep them from re-calculating every frame. The [Perform CHOP](<./Perform_CHOP.md> "Perform CHOP") has a parameters to monitor the number cached expressions. 

### What can the engine evaluate

When a Python expression is parsed it is broken up into tokens. A token can be for example a constant boolean value`True`or a constant string. Tokens are also the methods, members and variable names that are part of an expression. The engine has a set of tokens it recognizes, and if the expression contains only those tokens, then it can evaluate the expression. If there are any tokens it does not recognize in the expression, then it will not try to evaluate the expression and the regular Python engine will be used. 

As long as the expression contains only tokens recognized by the engine, the there is no limit to how large the expression and be or how complex the expression can be. 

For example this expression can be evaluated by the optimized expression engine: 
[code] 
     op(‘geo1’).par.tx + math.max(parent().par.tx + op(‘speed1’)[0], 10) / int(op('table1')['header', 5])
    
[/code]

The types of supported tokens are: 
* the`me`variable
* Constants: 
    * Strings
    * Booleans (`True`,`False`)
    * Integers
    * Floats
* Comparison operators: 
    *`==`*`!=`*`<`*`>`*`>=`*`<=`* Unary operators: 
    *`-`(negate)
    *`+`*`~`(invert)
* Boolean operators: 
    *`and`*`or`* Binary operators, for numerical and string operations: 
    *`+`*`-`*`*`*`/`*`%`(modulus)
    *`**`(power), as long as both arguments aren't integers.
    *`//`(floor division)
* single line if expressions
* Global [td module](<./Td_Module.md> "Td Module") functions: 
    *`op()`*`parent()`*`passive()`* [Tdu Module](<./Tdu_Module.md> "Tdu Module") functions: 
    *`remap()`*`rand()`* [AbsTime Class](<./AbsTime_Class.md> "AbsTime Class") methods and members: 
    *`frame`*`seconds`* [OP Class](<./OP_Class.md> "OP Class") methods and members: 
    *`name`*`par`*`digits`*`time`*`path`*`inputs`*`inputCOMPs`*`outputCOMPs`*`fetch()`, in some cases.
* [TimeCOMP Class](<./TimeCOMP_Class.md> "TimeCOMP Class") methods and members: 
    *`frame`*`seconds`*`rate`* [CHOP Class](<./CHOP_Class.md> "CHOP Class") methods and members: 
    *`rate`*`numSamples`*`start`*`end`*`[]`operator to access a [Channel Class](<./Channel_Class.md> "Channel Class") object.
* [DAT Class](<./DAT_Class.md> "DAT Class") methods and members: 
    *`[]`operator access a [Cell Class](<./Cell_Class.md> "Cell Class") object.
* [TOP Class](<./TOP_Class.md> "TOP Class") methods and members: 
    *`width`*`height`*`aspectWidth`*`aspectHeight`* [Panel Class](<./Panel_Class.md> "Panel Class") methods and members: 
    *`width`*`height`* [ParCollection Class](<./ParCollection_Class.md> "ParCollection Class") methods and members: 
    *`.`operator to get a [Par Class](<./Par_Class.md> "Par Class") object.
    *`[]`operator to get a [Par Class](<./Par_Class.md> "Par Class") object.
* [Par Class](<./Par_Class.md> "Par Class") methods and members: 
    *`eval()`*`evalNorm()`*`normVal`*`default`*`menuIndex`* automatic casting to int/float/string
* [Channel Class](<./Channel_Class.md> "Channel Class") methods and members: 
    *`eval()`*`[]`operator to get a single sample from a CHOP channel.
    * automatic casting
* [Cell Class](<./Cell_Class.md> "Cell Class") methods and members: 
    *`eval()`*`[r,c]`operator to get a cell from a DAT table.
    * automatic casting
* [Python list class](<https://docs.python.org/3.7/tutorial/datastructures.html>) methods and members: 
    *`[]`operator
    *`any(list)`*`len(list)`*`all(list)`* [Python math module](<https://docs.python.org/3.7/library/math.html>) functions: 
    *`abs()`*`max()`*`min()`*`round()`* [Python global functions](<https://docs.python.org/3.7/library/functions.html>): 
    *`pow()`*`int()`*`str()`*`bool()`*`float()`*`getattr()`(In limited cases)
* [Project Class](<./Project_Class.md> "Project Class") methods and members: 
    *`cookRate`(get only)
* [SOP Class](<./SOP_Class.md> "SOP Class") methods and members: 
    *`center`*`numPrims`*`numPoints`* [primitiveSOP Class](<./PrimitiveSOP_Class.md> "PrimitiveSOP Class") the`me.inputPrim`[Prim Class](<./Prim_Class.md> "Prim Class") has these members optimized: 
    *`me.inputPrim.index`*`me.inputPrim.center`*`me.inputPrim.direction`*`me.inputPrim.weight`*`me.inputPrim.normal`*`len(me.inputPrim)`* [pointSOP Class](<./PointSOP_Class.md> "PointSOP Class") has these special cases optimized: 
    * Includes inputPoint2, inputColor2, inputNormal2 and inputTexture2 as well.
    *`me.inputPoint.index`*`me.inputPoint.normP`*`me.inputPoint.P`*`me.inputPoint.x`*`me.inputPoint.y`*`me.inputPoint.z`*`me.inputPoint.normal`*`me.inputPoint.color`*`me.inputPoint.sopCenter`*`me.inputColor`(Deprecated)
    *`me.inputNormal`(Deprecated)
    *`me.inputTexture`* [Vector Class](<./Vector_Class.md> "Vector Class") : 
    *`[]`operator
    *`x, y and z`members
* [Position Class](<./Position_Class.md> "Position Class") : 
    *`[]`operator
    *`x, y and z`members
* [Color Class](<./Color_Class.md> "Color Class") : 
    *`[]`operator
    *`r, g, b and a`members
* [Panel Class](<./Panel_Class.md> "Panel Class") : 
    * Access to Panel Values.
* [PanelValue Class](<./PanelValue_Class.md> "PanelValue Class")
    * Automatic casting
    *`val`member
* [expressionCHOP Class](<./ExpressionCHOP_Class.md> "ExpressionCHOP Class") methods and members : 
    *`inputVal`*`chanIndex`*`sampleIndex`* [waveCHOP Class](<./WaveCHOP_Class.md> "WaveCHOP Class") methods and members : 
    *`chanIndex`*`sampleIndex`[Python Math Module constants and functions](<https://docs.python.org/3.5/library/math.html>) : 
* *`pi`*`sin()`*`cos()`*`tan()`*`asin()`*`acos()`*`ceil()`*`floor()`*`sqrt()`*`degrees()`*`radians()`
