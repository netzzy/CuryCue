# Tscript Expressions

  
Expressions in TouchDesigner are functions where you pass it data (string, float, vector etc.) and it returns data (not necessarily the same type as the data passed in). 

The expressions here are part of TouchDesigner's [Tscript](<./Tscript.md> "Tscript") scripting language. 

Examples: 

  *`sqrt(16)`takes a number and returns a number,`4`.
  *`strlen("hello")`takes a string and returns a number,`5`.
  *`base("flower42")`is a "string expression" - takes a string and returns a string,`flower`.
  *`if($F>10,2,3)`takes numbers and returns a number.
  *`ifs($F>10,"high","low")`takes a mix of numbers and strings, returning a string.
  *`tab("guests",2,3)`gets the string in the third row, 4th column of the table`guests`.
  *`chop("/project1/constant1/chan1")`gets the channel named`chan1`in the CHOP`/project1/constant1`.


Expressions are used in [Parameters](<./Parameter.md> "Parameter"), [DATs](<./DAT.md> "DAT") (especially the [Evaluate DAT](<./Evaluate_DAT.md> "Evaluate DAT")), [Commands](<./Tscript_Commands.md> "Tscript Commands") and [Scripts](<./Script.md> "Script"). 

A complete listing of all expressions is [below](<#Alphabetical_List>). 

Alternately type`exhelp`Command in the [textport](<./Textport.md> "Textport"). 

## Back-quotes

An important concept to understand when using expressions is when to use back-quotes (`). The back-quote key is same key as the Tilde (~) key. It's usually found in the upper-left corner of the keyboard. 

Placing something in backquotes tells TouchDesigner that the enclosed string is an expression that should be evaluated. 
[code]`expression(parameter)`[/code]

You need to place back-quotes around an expression if it's being used in a place where TouchDesigner is usually expecting a string. For example an expression in a string parameter like the Text TOP's Text parameter needs to be enclosed in back-quotes. However an expression in a numeric parameter like the Geometry object's Translate parameter does not need back-quotes, because TouchDesigner expects either a number, or an expression in that parameter. 

You must always enclose expressions in scripts and when entering commands in the textport. E.g 
[code] 
    echo sine of 45 degrees is`sin(45)`[/code]

## Sweet Sixteen Expressions

Expression | Purpose | Related Expression  
---|---|---  
[chop()](<#chop\(\)>) | Get a value from a CHOP channel. | [chopci()](<#chopci\(\)>)  
[tab()](<#tab\(\)>) | Get a value from a DAT table cell. | [tabrc()](<#tabrc\(\)>)  
[point()](<#point\(\)>) | Get a value from a SOP point. |   
[panel()](<#panel\(\)>) | Get information from a control panel. |   
[par()](<#par\(\)>) | Get the current value of a parameter. |   
[opdigits()](<#opdigits\(\)>) | Get the digits at the end of a node name. | [opexists()](<#opexists\(\)>)  
[opname()](<#opname\(\)>) | Get the name of a node. | [opexists()](<#opexists\(\)>)  
[opfullpath()](<#opfullpath\(\)>) | Get the full path of a node. |   
[strcmp()](<#strcmp\(\)>) | String manipulation expressions. | [strlen()](<#strlen\(\)>)  
[substr()](<#substr\(\)>) | String manipulation expressions. | [substitute()](<#substitute\(\)>)  
[index()](<#index\(\)>) | String manipulation expressions. | [strcat()](<#strcat\(\)>)  
[rand()](<#rand\(\)>) | Generate random numbers. |   
[execute()](<#execute\(\)>) | Execute the string as a Tscript command. |   
[smooth()](<#smooth\(\)>) | Interpolate between two values. |   
[varexists()](<#varexists\(\)>) | Check if a variable exists. |   
[expand()](<#expand\(\)>) | Expand variables in a string. | [eval()](<#eval\(\)>)  
  
## Alphabetical List

## 

abs(number)

This is a mathematical function used to express the absolute value of the number. 
[code] 
    abs(-2.6) = 2.6
    set A =`abs(-2.6)`[/code]

## 

acos(number)

This is a trigonometric mathematical function used to express the arccosine value of the number. 
[code] 
    acos(0)=90
    set A =`acos(90)`[/code]

## 

arclen(SOP, prim_num, ustart, ustop)

Computes the length of the curve specified by prim_num in the range [ustart, ustop]. ustart and ustop are unit values, defined in the [0,1] interval. Note: the primitive must be either a NURBS curve or a Bezier curve. 
[code] 
    # Will compute the length of the entire curve whose index is 12:
    arclen("/obj/geo1/model1", 12, 0, 1)
    
[/code]

    **See Also:**[surflen](<#surflen>) [normal](<#normal>) [curvature](<#curvature>) [unituv](<#unituv>)

## 

arg(line, argNum)

This function will parse and extract an argument from a line. Negative values count from the end. 
[code] 
    arg("apple banana carrot", 1) = "banana"
    arg("apple banana carrot", -1)= "carrot"
    
[/code]

    **See Also:**[argc](<#argc>) [argf](<#argf>) [argfx](<#argfx>) [argx](<#argx>) [argxc](<#argxc>)

## 

argc(line)

Returns the number of arguments in the line. Standard parsing is done, no variable expansion is done on the line. 
[code] 
    argc("This has four arguments")=4
    
[/code]

    **See Also:**[arg](<#arg>) [argf](<#argf>) [argfx](<#argfx>) [argx](<#argx>) [argxc](<#argxc>)

## 

argf(line, token)

This function returns the index of the argument on a line. 
[code] 
    argf("apple, banana, carrot", "carrot") = 2
    argf("apple, banana, carrot", "donut") = -1
    
[/code]

    **See Also:**[arg](<#arg>) [argc](<#argc>) [argfx](<#argfx>) [argx](<#argx>) [argxc](<#argxc>)

## 

argfx(line, token, separators)

This function returns the index of the argument on a line, given a string of separators. 
[code] 
    argfx("apple, banana, carrot", "banana", " ,") = 1
    argfx("/a/b/c/d", "e", "/") = -1
    
[/code]

    **See Also:**[arg](<#arg>) [argc](<#argc>) [argf](<#argf>) [argx](<#argx>) [argxc](<#argxc>)

## 

argx(line, argNum, separators)

This function will parse and extract an argument from a line, given a string of separators. Negative values count from the end. 
[code] 
    argx("apple, banana, carrot", 1, " ,")= "banana"
    argx("/a/b/c/d", -1, "/") = "d"
    
[/code]

    **See Also:**[arg](<#arg>) [argc](<#argc>) [argf](<#argf>) [argfx](<#argfx>) [argxc](<#argxc>)

## 

argxc(line, separators)

Returns the number of arguments in the line, given a string of separators. Standard parsing is done, no variable expansion is done on the line. 
[code] 
    argxc("apple; banana; carrot", "; ")=3
    
[/code]

    **See Also:**[arg](<#arg>) [argc](<#argc>) [argf](<#argf>) [argfx](<#argfx>) [argx](<#argx>)

## 

arm(sop_path, ret_type)

This function will extract inverse kinematic rotations from an arm sop. This is useful for creating hierarchical systems that mimic the arm. The sop_path is the full path of the arm sop. The ret_type is one of: srx, sry, arx, ury, hrx, hry, hrz, Hrx, Hry, Hrz, Htx, Hty, Htz The ret_type is the returned rotation, where: s=shoulder, a=humerus, u=ulna, h=hand, H=hand relative to shoulder 
[code] 
    arm ("/obj/geo1/arm1", "arx")
    # Note: the shoulder oxorder should be yx, hand should be xyz
    
[/code]

## 

asin(number)

This is a trigonometric mathematical function used to express the arcsine value of the number. 
[code] 
    asin (.866025)=60
    
[/code]

    **See Also:**[acos](<#acos>) [atan](<#atan>) [atan2](<#atan2>) [cos](<#cos>) [cosh](<#cosh>) [sin](<#sin>) [sinh](<#sinh>) [tan](<#tan>) [tanh](<#tanh>)

## 

atan(number)

This is a trigonometric mathematical function used to express the arctangent value of the number. 
[code] 
    atan(1.73205)=60
    
[/code]

    **See Also:**[acos](<#acos>) [asin](<#asin>) [atan2](<#atan2>) [cos](<#cos>) [cosh](<#cosh>) [sin](<#sin>) [sinh](<#sinh>) [tan](<#tan>) [tanh](<#tanh>)

## 

atan2(y, x)

Compute the arctangent of y/x. This is more stable than atan since it can use the signs of y and x to determine the quadrant the angle is in. It also handles the case where x is zero correctly, returning 90 or -90. 
[code] 
    atan2(1, 0) = 90
    atan2(0, 1) = 0
    atan2(0, -1) = 180
    
[/code]

    **See Also:**[acos](<#acos>) [asin](<#asin>) [atan](<#atan>) [cos](<#cos>) [cosh](<#cosh>) [sin](<#sin>) [sinh](<#sinh>) [tan](<#tan>) [tanh](<#tanh>)

## 

atof(source)

Will forcibly convert a string into a float. 

    **See Also:**[ctof](<#ctof>) [ftoc](<#ftoc>) [ftoa](<#ftoa>)

## 

backslash(string)

This will substitute all slashes in a string to backslashes. Remember to use the noevals expression to ignore escaped sequences. 
[code] 
    set a =`noevals(backslash($a))`[/code]

    **See Also:**[forwardslash](<#forwardslash>) [noevals](<#noevals>)

## 

base(string)

This function will return the non-numeric portion of a string. 
[code] 
    base("chan123")  = "chan"
    
[/code]

    **See Also:**[digits](<#digits>) [opdigits](<#opdigits>) [opbase](<#opbase>)

## 

bbox(SOP, type)

This function will return bounding box information for a SOP. The type can be one of D_XMIN, D_YMIN, D_ZMIN, D_XMAX, D_YMAX, or D_ZMAX for the corresponding values of the bounding box. 
[code] 
    bbox("sopname", "D_XMIN")
    
[/code]

## 

bezier()

This is a channel expression that yields a Bezier interpolation spline. 

## 

boneangle(bone1, bone2)

This function will return the angle between the negative Z axis of bone1 and the negative Z axis of bone2. Since bones are oriented along their negative Z axes, this can be used as the angle between two bones. 

## 

ceil(, float)

Returns the smallest integer not less than the value passed in. Also the Math CHOP has a Ceiling option in its Integer parameter. 

    **See Also:**[format](<#format>) [floor](<#floor>) [round](<#round>) [int](<#int>)

## 

centroid(, SOP, type)

This function will return centroid information for a SOP. The type can be one of D_X, D_Y, D_Z for the corresponding components of the centroid. 

## 

chop(channel)

Evaluates the channel within a CHOP at the current time. 
[code] 
    chop("/ch/ch1/wave1/chan1")
    
[/code]

    **See Also:**[chopi](<#chopi>) [chopt](<#chopt>) [chopf](<#chopf>) [chopstr](<#chopstr>)

## 

chopcf(CHOP, channel_index, frame)

Evaluates the channel at index channel_index within the specified CHOP at the specified frame. 
[code] 
    chopcf("/ch/ch1/wave1", 0, 11)
    
[/code]

    **See Also:**[chop](<#chop>) [chopf](<#chopf>) [chopct](<#chopct>) [chopci](<#chopci>)

## 

chopci(CHOP, channel_index, index)

Evaluates the channel at index channel_index within the specified CHOP at the specified sample index. 
[code] 
    chopci("/ch/ch1/wave1", 0, 10)
    
[/code]

    **See Also:**[chop](<#chop>) [chopi](<#chopi>) [chopct](<#chopct>) [chopcf](<#chopcf>)

## 

chopct(CHOP, channel_index, time)

Evaluates the channel at index channel_index within the specified CHOP at the specified time. 
[code] 
    chopct("/ch/ch1/wave1", 0, 0.5)
    
[/code]

    **See Also:**[chop](<#chop>) [chopt](<#chopt>) [chopcf](<#chopcf>) [chopci](<#chopci>)

## 

chope(CHOP)

Returns the end index of the channels in the specified CHOP. 
[code] 
    chope("/ch/ch1/wave1")
    
[/code]

    **See Also:**[chops](<#chops>) [chopl](<#chopl>) [chopn](<#chopn>) [chopname](<#chopname>) [chopr](<#chopr>)

## 

chopf(channel, frame)

Evaluates the channel within a CHOP with at the specified frame. 
[code] 
    chopf("/ch/ch1/wave1/chan1", 1)
    
[/code]

    **See Also:**[chopi](<#chopi>) [chopt](<#chopt>) [chop](<#chop>)

## 

chopi(channel, index)

Evaluates the channel within a CHOP with at the specified sample index. 
[code] 
    chopi("/ch/ch1/wave1/chan1", 10)
    
[/code]

    **See Also:**[chopf](<#chopf>) [chopt](<#chopt>) [chop](<#chop>)

## 

chopindex(channel)

Return the position of a channel within a CHOP
[code] 
    chopindex("/ch/ch1/wave1/chan3")
    
[/code]

    **See Also:**[chops](<#chops>) [chope](<#chope>) [chopl](<#chopl>) [chopn](<#chopn>) [chopr](<#chopr>) [chopname](<#chopname>)

## 

chopl(CHOP)

Returns the length of the channels in the specified CHOP, in samples. 
[code] 
    chopl("/ch/ch1/wave1")
    
[/code]

    **See Also:**[chops](<#chops>) [chope](<#chope>) [chopn](<#chopn>) [chopname](<#chopname>) [chopr](<#chopr>)

## 

chopn(CHOP)

Returns the number of data channels within the specified CHOP. 
[code] 
    chopn("/ch/ch1/wave1")
    
[/code]

    **See Also:**[chops](<#chops>) [chope](<#chope>) [chopl](<#chopl>) [chopr](<#chopr>)

## 

chopname(, CHOP, index)

Returns the name of a channel given a CHOP and an index 
[code] 
    chopname("/ch/ch1/wave1", 2)
    
[/code]

    **See Also:**[chops](<#chops>) [chope](<#chope>) [chopl](<#chopl>) [chopn](<#chopn>) [chopr](<#chopr>) [chopindex](<#chopindex>)

## 

chopr(CHOP)

Returns the sample rate of the specified CHOP. 
[code] 
    chopr("/ch/ch1/wave1")
    
[/code]

    **See Also:**[chops](<#chops>) [chope](<#chope>) [chopl](<#chopl>) [chopn](<#chopn>) [chopname](<#chopname>)

## 

chops(CHOP)

Returns the start index of the specified CHOP. 
[code] 
    chops("/ch/ch1/wave1")
    
[/code]

    **See Also:**[chops](<#chops>) [chope](<#chope>) [chopl](<#chopl>) [chopn](<#chopn>) [chopname](<#chopname>) [chopr](<#chopr>)

## 

chopstr(channel)

Returns the value of the channel within a CHOP at the current time as a text string. 
[code] 
    chopstr("/ch/ch1/wave1/chan1")
    
[/code]

    **See Also:**[chop](<#chop>) [chopf](<#chopf>) [chopt](<#chopt>) [chopi](<#chopi>)

## 

chopt(channel, time)

Returns the value of the channel within a CHOP at the time specified. 
[code] 
    chopt("/ch/ch1/wave1/chan1", 0.5)
    
[/code]

    **See Also:**[chopct](<#chopct>) [chopi](<#chopi>) [chopf](<#chopf>)

## 

chopts(channel, index)

Evaluates the channel within a CHOP with at the specified sample index. This expression is similar to chopi except the index parameter is adjusted to the beginning of the input time slice. For example index=0 is always the first sample of the input, regardless of its starting position. This expression can be used to modify timeslices with expressions without losing any samples. 
[code] 
    chopts("/ch/ch1/wave1/chan1", 10)
    
[/code]

## 

clamp(, value, minimum, maximum)

This is a Touch expression function that will clamp the value between the minimum and maximum numbers. It is used to prevent the value from going outside the specified range. 
[code] 
    # This will return 10 since the value is larger than the maximum number specified.
    clamp(12,2,10)
    # This will return 2 since the value is lesser than the minimum number specified.
    clamp(1,2,10)
    
[/code]

## 

clamptosphere(x, y, z, min_radius, max_radius, constant_type)

This function computes a vector R that is parallel to the given (x,y,z) vector. R is adjusted so that its magnitude is always between the min and max radii (i.e min_radius <= |R <= max_radius) This function returns one of the components of the vector R according to the value of constant_type: X, Y or Z. 

## 

collapsepathwith(collapsepathfromsource)

Returns a string whose prefix is replaced by any matching variables in the current component, any of its parents, as well as any global and system variables. Script variables will not be used. To collapse disk filenames use collapsepath(), collapsepathwith(). 
[code] 
    # Return $A/ghi:
    set A = "abc/def"
    echo`collapse("abc/def/ghi")`[/code]

    **See Also:**[collapsewith](<#collapsewith>) [collapsefromsource](<#collapsefromsource>) [collapsepath](<#collapsepath>)

## 

collapsepathfromsource()

Returns a string whose prefix is replaced by any matching variables in the given node, any of its parents, as well as any global and system variables. Script variables will not be used. If opnode is blank, no component variables will be used. 
[code] 
    # Return matching vars defined in /project1
    cvar B = "abc/def"
    echo`collapsefromsource($B, "/project1")`[/code]

    **See Also:**[collapse](<#collapse>) [collapsewith](<#collapsewith>) [collapsepath](<#collapsepath>) [collapsepathwith](<#collapsepathwith>)

## 

collapsepathwith(collapsepathfromsource)

Returns a path whose prefix is replaced by any matching variables in the current component, any of its parents, as well as any global and system variables. Script variables will not be used. 
[code] 
    # May return $DESKTOP/a.txt:
    collapsepath("C:/Documents and Settings/Admin1/Desktop/a.txt")
    
[/code]

    **See Also:**[collapse](<#collapse>) [collapsewith](<#collapsewith>) [collapsefromsource](<#collapsefromsource>)

## 

collapsepathwith()

Returns a path whose prefix is replaced by any matching variables in the given node, any of its parents, as well as any global and system variables. Script variables will not be used. If opnode is blank, no component variables will be used. 
[code] 
    # Return matching vars defined in /project1
    cvar B = "abc/def"
    echo`collapsefromsource($B, "/project1")`[/code]

    **See Also:**[collapse](<#collapse>) [collapsewith](<#collapsewith>) [collapsefromsource](<#collapsefromsource>) [collapsepath](<#collapsepath>)

## 

collapsepathfromsource()

Returns a path whose prefix is replaced by any matching variables in the current component, any of its parents, as well as any global and system variables. Script variables will not be used. Preference is first given to the given variable if it fits. Note: the variable parameter must not include the leading $ symbol. Also note: the replacement variable must replace whole words between lashes, not partial strings. 
[code] 
    # May return $MY_JOB_DIR/a.txt
    collapsepathwith("C:/jobs/a.txt", "MY_JOB_DIR")
    
[/code]

    **See Also:**[collapse](<#collapse>) [collapsewith](<#collapsewith>) [collapsepath](<#collapsepath>) [collapsefromsource](<#collapsefromsource>)

## 

collapsepathwith(collapsepathfromsource)

Returns a string whose prefix is replaced by any matching variables in the current component, any of its parents, as well as any global and system variables. Script variables will not be used. Preference is first given to the given variable if it fits. Note: the variable parameter must not include the leading $ symbol. Also note: the replacement variable must replace whole words between slashes, not partial strings. To collapse disk filenames use collapsepath(), collapsepathwith(). 
[code] 
    # Would return $A/def:
    set A = "abc"
    set B = "abc/def"
    echo`collapsewith($B, A)`[/code]

    **See Also:**[collapse](<#collapse>) [collapsefromsource](<#collapsefromsource>) [collapsepath](<#collapsepath>)

## 

constant()

This is a channel expression for a constant values. 

## 

convertbase(number)

Converts a number from one base to another. 
[code] 
    convertbase("255", 10, 16) = "FF"
    convertbase("111", 2, 10) = "7"
    convertbase("1F", 16, 10) = "31"
    convertbase("10", 16, 2) = "10000"
    
[/code]

    **See Also:**[format](<#format>)

## 

monitorcount()

Will return the monitor that the coordinates x and y lay within. If no monitor contains those coordinates, -1 will be returned. 

    **See Also:**[monitorright](<#monitorright>) [monitortop](<#monitortop>) [monitorleft](<#monitorleft>) [monitorbottom](<#monitorbottom>)

## 

cos(number)

This is a trigonometric mathematical function used to express the cosine value of the number. 
[code] 
    cos(60)=0.5
    
[/code]

## 

cosh(number)

This is a mathematical function used to express the hyperbolic cosine value of the number. 
[code] 
    cosh(2) = 3.7622
    
[/code]

## 

cross(v1, v2)

Computes the cross product between v1 and v2 

## 

ctof(source)

Will convert a character into a number. 
[code] 
    ctof("a") = 65
    
[/code]

    **See Also:**[ftoc](<#ftoc>) [atof](<#atof>) [ftoa](<#ftoa>)

## 

cubic()

A channel interpolation function which uses the slopes at either end to solve the differential equation to give a smooth curve between the end points. 

## 

curvature(, SOP, prim_num, u, v)

Evaluates the curvature of the surface at the parametric (u,v) location. u and v are unit values, defined in the [0,1] interval. Note: if the primitive is a mesh, u and v are defined in terms its number of rows and columns. 

    **See Also:**[unituv](<#unituv>) [primuv](<#primuv>) [primduv](<#primduv>) [normal](<#normal>)

## 

cvar(, variable, path)

This expression will return a component variable as evaluated from a specific path. The variable may reside in the path, or may reside in a containing component further up the hierarchy. 
[code] 
    cvar("A", "/project1")
    cvar("TOUCHTIME", "/")
    
[/code]

## 

deg(radians)

Converts the radians value to a value measured in degrees. 

    **See Also:**[rad](<#rad>)

## 

degree(, SOP, prim_num, D_U

Returns the degree of the polynomial defining the face or hull whose primitive number is specified. Polygons and meshes are expressed as linear functions, so their degree is 1. Spline types -- NURBS and Bezier curves and surfaces -- have degrees ranging from 1 to 10. Note: If the primitive is a polygon or a curve, D_U and D_V are irrelevant. 

## 

determinant(mat)

Returns the determinant of the matrix specified. This is only valid if the matrix is a 4x4 or 3x3 matrix. If the matrix is larger than 4x4, the 4x4 determinant will be returned. If the matrix is smaller than 3x3, the matrix will be converted to a 3x3 before the determinant is computed. The results of the upward conversion are not guaranteed. 

## 

digits(string)

This function will return the numeric value of the last set of consecutive digits in a string. 
[code] 
    digits("chan123") = 123
    
[/code]

    **See Also:**[base](<#base>) [opdigits](<#opdigits>) [opbase](<#opbase>)

## 

dihedral(v0, v1)

Computes the dihedral matrix between v0 and v1. This is a rotation matrix which will rotate vector v0 to vector v1. 

## 

distance(, x1, y1, z1, x2, y2, z2)

Returns sqrt(x_2-x_1)^2 + (y_2-y_1)^2 + (z_2-z_1)^2, the distance between the given points. 

    **See Also:**[pointdist](<#pointdist>) [uvdist](<#uvdist>)

## 

dot(v0, v1)

Computes the dot product between two vectors. 

## 

ease(number)

This is a channel expression function which will slowly ease in to and out of any change. It will start at rest and slowly increase the amount of change then, near the end of the function gradually reduce the amount of change until it is at rest. 

## 

ease(number)

This is a channel expression function which will slowly ease in to any change. 

## 

easeinp(number)

This is a channel expression function which will slowly increase the motion of the model to its maximum value. This is similar to the motion of an object accelerating due to gravity. 

## 

easeout(number)

This is a channel expression function which will slowly ease out of any change and come to rest. 

## 

easeoutp(, number)

This is a channel expression function which is similar to the easeinp expression only reversed. The change starts rapidly and begins to slow until it comes to rest. The number determines the inflection point of the curve. Increasing the number will shift the inflection point to the right. Fractional numbers will towards zero will shift the inflection point to the right. 

## 

easep(number)

This is a channel expression which will gradually ease in to the motion and gradually ease out. The ease out is faster than the ease in. 

## 

eval(expression)

This function will evaluate the string passed in as an expression. It's primary use is for evaluating variables which contain more complex expressions. This function returns a floating point value. 
[code] 
    set foo = 1+2
    echo`eval($foo)`[/code]

    **See Also:**[evals](<#evals>)

## 

evals(expression)

This function will evaluate the string passed in as an expression. It's primary use is for evaluating variables which contain more complex expressions. This function returns a string value. 
[code] 
    set foo = system("ls")
    echo`evals($foo)`[/code]

    **See Also:**[eval](<#eval>)

## 

execute(command)

This expression will execute the given TouchDesigner Tscript command (enclosed in quotes), and return the output of the command. 
[code] 
    # This will set the variable to the operators in the current working component.
    set foo = execute("lc -d")
    
[/code]

## 

exp(number)

This is a logarithmic exponentiation function. 
[code] 
    exp(2)= 7.3338906
    
[/code]

## 

expand(string)

This expression will recursively expand all variables in a string. 
[code] 
    touch -> set A=apple
    touch -> set B=\$A\$A
    touch -> echo $B
    $A$A
    touch -> echo`expand($B)`appleapple
    
[/code]

## 

expandpattern(string)

This expression will expand patterns in a string. 
[code] 
    touch -> echo`expandpattern("t[xyz]")`tx ty tz
    touch -> echo`expandpattern("t[5-13:2]")`t5 t7 t9 t11 t13
    touch -> echo`expandpattern("[tr][xyz]")`tx ty tz rx ry rz
    
[/code]

## 

explodematrix(mat, trs, xyz, component)

This function will extract a specific channel of information from a matrix. For example it can extract the X rotation (RX), or the Y scale (SY). These values can be plugged directly into Transform parameters for the various types of nodes that have a set transform parameters. <mat> is the matrix to explode, it can be a 3x3 or 4x4 matrix. <trs> is a string representing the transform order. It contains any combination of S, R and T. For example SRT signifies a scale, rotate, translate order. Or TRS indicates a translate, rotate, scale order. <xyz> is the rotation order, it's a string with any combination of X, Y and Z. For example YXZ means the rotation order is Y, then X, then Z. <component> is which channel you want to extract. It's a string starting with one of S, R or T, and followed by one of X, Y, or Z. For example RZ means extract the Z rotation channel. 
[code] 
    explodematrix(mlookat(vector("[1,0,0]"),vector("[0,1,0]")),"RST", "XYZ", "RZ")
    
[/code]

    **See Also:**[explodematrixp](<#explodematrixp>)

## 

explodematrixp(mat, pivot, trs, xyz, component)

This function is the same as explodematrix(), except it accepts a pivot vector in the <pivot> parameter. Refer to the help for explodematrix() for more information. 
[code] 
    explodematrixp(mlookat(vector("[1,0,0]"), vector("[0,1,0]")), vector("[0.5, 0, 1]"), "RST", "XYZ", "RZ")
    
[/code]

    **See Also:**[explodematrix](<#explodematrix>)

## 

filetype(filename)

This function will return the type of the file specified. It returns one of three strings: folder, file, or error. 
[code] 
    filetype("C:/autoexec.bat")
    filetype("C:/")
    
[/code]

## 

fit(num, oldmin, oldmax, newmin, newmax)

Return a number between newmin and newmax that is relative to num in the range between oldmin and oldmax. 
[code] 
    fit(3,1,4,5,20)=15
    
[/code]

## 

float(arg)

Returns the argument converted to a floating point number. Useful when mixing strings and numbers in an expression. 
[code] 
    float(2.5)=2.5
    float("2.5")=2.5
    float("12") + 3 = 15   (Note:  "12" + 3 = "123")
    
[/code]

    **See Also:**[ceil](<#ceil>) [floor](<#floor>) [format](<#format>) [int](<#int>) [round](<#round>) [trunc](<#trunc>)

## 

floor(number)

Returns the largest integer not greater than the number. Also the Math CHOP has a Floor option in its Integer parameter. 
[code] 
    floor(10.2)=10
    floor(-10.2)=-11
    
[/code]

    **See Also:**[ceil](<#ceil>) [float](<#float>) [format](<#format>) [int](<#int>) [round](<#round>) [trunc](<#trunc>)

## 

format(value, mindigits, decimals)

Formats a numeric value, where: min_digits is the minimum number of digits to the left of the decimal point decimals is the number of digits after the decimal point. Values are right justified and padded with zeros. 
[code] 
    format(3.1234, 3, 2) = 003.12
    
[/code]

    **See Also:**[ceil](<#ceil>) [floor](<#floor>) [int](<#int>) [round](<#round>) [trunc](<#trunc>)

## 

forwardslash(string)

This will substitute all slashes in a string to forwardslashes. Remember to use the noevals expression to ignore escaped sequences. 
[code] 
    set a =`noevals(forwardslash($a))`[/code]

    **See Also:**[backslash](<#backslash>) [noevals](<#noevals>)

## 

ff(represents, frames, in, the, range, 1, to, fps.)

Given a frame value and a frames per second value, this expression will return a timecode in the format: hh:mm:ss.ff where hh represents hours, 
[code] 
    frametotimecode(12345, 30) 		# returns "00:06:51.15"
    timecodetoframe("00:06:51.15", 30)	# returns 12345	
    timecodetoframe("06:51.15", 30)		# returns 12345
    
[/code]

    **See Also:**[timecodetoframe](<#timecodetoframe>)

## 

ftoa(number)

This expression will convert a number to a string. Type conversion is usually done automatically, however, you may wish to use this to force the conversion. 

    **See Also:**[ctof](<#ctof>) [ftoc](<#ftoc>) [atof](<#atof>)

## 

ftoc(number)

This expression will convert a number to a character. 
[code] 
    ftoc(65) = "a"
    
[/code]

    **See Also:**[ctof](<#ctof>) [atof](<#atof>) [ftoa](<#ftoa>)

## 

haspoint(, group_name, sop, point_num)

This function can be used to determine whether a given point is a member of a given group. 
[code] 
    haspoint("ears", "/obj/geo1/facet1", 4)
    # Will return 1 if the group "ears" contains point number 4, otherwise it will return 0.
    # The function will return 0 if the group specified is a primitive group.
    
[/code]

    **See Also:**[hasprim](<#hasprim>) [pointlist](<#pointlist>) [primlist](<#primlist>)

## 

hasprim(group_name, sop, prim_num)

This function can be used to determine whether a given primitive is a member of a given group. 
[code] 
    hasprim("ears", "/obj/geo1/facet1", 3)
    # Will return 1 if the group "ears" contains primitive number 3, otherwise it will return 0.
    # The function will return 0 if the group specified is a point group.
    
[/code]

    **See Also:**[haspoint](<#haspoint>) [pointlist](<#pointlist>) [primlist](<#primlist>)

## 

hsv(red, green, blue, component)

Converts the RGB value to one of the HSV values based on component specified. The component should be one of h, s or v. 
[code] 
    hsv(.3, .6, .4, "h")
    
[/code]

    **See Also:**[rgb](<#rgb>)

## 

ic(input_index, channel_index, index)

Evaluates a CHOP's input channel at the specified index. 
[code] 
    ic(0, 2, 10)
    
[/code]

    **See Also:**[ics](<#ics>) [ice](<#ice>) [icr](<#icr>) [icn](<#icn>) [icmin](<#icmin>) [icmax](<#icmax>) [icl](<#icl>) [oc](<#oc>)

## 

ice(input_index)

Returns the end index of a CHOP's input. 
[code] 
    ice(0)
    
[/code]

    **See Also:**[ics](<#ics>) [ic](<#ic>) [icr](<#icr>) [icn](<#icn>) [icmin](<#icmin>) [icmax](<#icmax>) [icl](<#icl>) [oc](<#oc>)

## 

icl(input_index)

Returns the length of a CHOP's input, in samples. 
[code] 
    icl(0)
    
[/code]

    **See Also:**[ics](<#ics>) [ic](<#ic>) [ice](<#ice>) [icr](<#icr>) [icn](<#icn>) [icmin](<#icmin>) [icmax](<#icmax>) [oc](<#oc>)

## 

icmax(input_index, channel_index)

Evaluates a CHOP's input channel's maximum value. 
[code] 
    icmax(0, 2)
    
[/code]

    **See Also:**[ics](<#ics>) [ic](<#ic>) [ice](<#ice>) [icr](<#icr>) [icn](<#icn>) [icmin](<#icmin>) [icl](<#icl>) [oc](<#oc>)

## 

icmin(input_index, channel_index)

Evaluates a CHOP's input channel's minimum value. 
[code] 
    icmin(0, 2)
    
[/code]

    **See Also:**[ics](<#ics>) [ic](<#ic>) [ice](<#ice>) [icr](<#icr>) [icn](<#icn>) [icmax](<#icmax>) [icl](<#icl>) [oc](<#oc>)

## 

icn(input_index)

Returns the number of channels in a CHOP's input. 
[code] 
    icn(0)
    
[/code]

    **See Also:**[ics](<#ics>) [ic](<#ic>) [ice](<#ice>) [icr](<#icr>) [icmin](<#icmin>) [icmax](<#icmax>) [icl](<#icl>) [oc](<#oc>)

## 

icr(input_index)

Returns the sample rate of a CHOP's input. 
[code] 
    icr(0)
    
[/code]

    **See Also:**[ics](<#ics>) [ic](<#ic>) [ice](<#ice>) [icn](<#icn>) [icmin](<#icmin>) [icmax](<#icmax>) [icl](<#icl>) [oc](<#oc>)

## 

ics(input_index)

Returns the start index of a CHOP's input. 
[code] 
    ics(0)
    
[/code]

    **See Also:**[ics](<#ics>) [ic](<#ic>) [ice](<#ice>) [icr](<#icr>) [icn](<#icn>) [icmin](<#icmin>) [icmax](<#icmax>) [icl](<#icl>) [oc](<#oc>)

## 

identity(size)

Creates an identity matrix of the size specified. That is, the resulting matrix will have size rows and size columns. 

## 

if(expression, true_value, false_value)

If the expression is true, the function evaluates to the true_value, otherwise the false_value is returned. The following example shows that if the frame number is less than 12, the resulting number equals the frame number. When the frame number reaches 12 or greater, the resulting number is always 75. 
[code] 
    if ($F<12, $F, 75)
    if (!strcmp("pos",$V), 1, -1)
    
[/code]

    **See Also:**[ifs](<#ifs>)

## 

ifs(expression, true_string, false_string)

If the expression is true, the function evaluates to the true_string, otherwise the false_string is returned. The following example shows that if the frame number is less than 12, the resulting string is the frame number. When the frame number reaches 12 or greater, the resulting string is "limit reached". 
[code] 
    ifs($F<12, "$F", "limit reached")
    ifs(!strcmp("A",$V), "Match", "No Match")
    
[/code]

    **See Also:**[if](<#if>)

## 

index(source, pattern)

Finds the first occurrence of pattern in source and returns the number of characters before the pattern occurs. If the pattern is not found -1 is returned. 
[code] 
    touch -> echo`index("Testing index", "sting")`2
    touch -> echo`index("Testing index", "i")`4
    
[/code]

    **See Also:**[rindex](<#rindex>)

## 

insideface(SOP, prim_num, x, y, z)

Returns one if point(x,y,z) is inside the specified primitive. 
[code] 
    # Will return 1 if point(1,2,3) is inside the first primitive of add1.
    insideface("/obj/geo1/add1", 0, 1,2,3)
    
[/code]

    **See Also:**[primdist](<#primdist>) [pointdist](<#pointdist>)

## 

int(number)

The integer value of the number by truncating the fractional parts off. 
[code] 
    int(2.501)=2
    int(-2.501)=-2
    int(0.2)=0
    int(-.2)=0
    
[/code]

    **See Also:**[ceil](<#ceil>) [float](<#float>) [floor](<#floor>) [format](<#format>) [round](<#round>) [trunc](<#trunc>)

## 

invert(mat)

Inverts the matrix given. This is only valid if the matrix is a 4x4 or 3x3 matrix. If the matrix is larger than 4x4, the matrix will be converted to a 4x4 matrix before it is inverted. If the matrix is smaller than 3x3, the matrix will be enlarged to a 3x3 matrix before it is inverted. The results of enlarging the matrix to a 3x3 are not guaranteed. 

## 

opnoutputs()

Returns the relative path to n'th wired parent of the currently evaluated node. For example ip(1) would return the node immediately wired to the first input. ip(2) would return the first input's input, etc. This expression should only exist within a parameter. 

    **See Also:**[ipf](<#ipf>) [opinput](<#opinput>) [opinputf](<#opinputf>) [opoutput](<#opoutput>) [opoutputf](<#opoutputf>) [opninputs](<#opninputs>)

## 

opnoutputs()

Returns the full path to n'th wired parent of the currently evaluated node. For example ipf(1) would return the node immediately wired to the first input. ipf(2) would return the first input's input, etc. This expression should only exist within a parameter. 

    **See Also:**[ip](<#ip>) [opinput](<#opinput>) [opinputf](<#opinputf>) [opoutput](<#opoutput>) [opoutputf](<#opoutputf>) [opninputs](<#opninputs>)

## 

iscollided(sopname, pointnumber)

Returns 1 if the point specified has collided with something 
[code] 
    iscollided("../particle1", $PT)
    
[/code]

## 

isnumber(text)

This function will return 1 (true) if the given string represents a number and 0 (false) if it does not 
[code] 
    isnumber("10") = isnumber("0") = 1
    isnumber("abc") = isnumber("10abc") = 0
    
[/code]

## 

isspline(SOP, prim_num)

Returns 1 if the primitive is a spline, i.e. a NURBS or Bezier curve or surface. Otherwise, the value returned is 0. 

## 

isstuck(sopname, pointnumber)

Will return if the point specified is used by a particle system and the point is stuck. Warning, this function can be slow. 
[code] 
    isstuck("../particle1", $PT)
    
[/code]

## 

F1(through, F12)

This function will return the current state of the key. Return values are 1 or 0, with 1 meaning the key is pressed, 0 meaning it is not. key can be: A through Z, and a through z Note: All parameters to this function are case insensitive. For example keystate("a") always returns the same value as keystate("A"). 
[code] 
    keystate("K")
    keystate("shift")
    keystate("F7")
    
[/code]

    **See Also:**[mouse](<#mouse>)

## 

length(x, y, z)

Returns sqrt(x*x + y*y + z*z), the length of the vector 

## 

linear()

This is a channel interpolation function which will do linear interpolation of the end points. 

## 

log(number)

This is the natural logarithm of the number. 
[code] 
    log(2.718281828)= 1
    
[/code]

    **See Also:**[log10](<#log10>)

## 

log10(number)

This is the logarithm base 10 of the number. 
[code] 
    log10(10) = 1
    log10(100) = 2
    
[/code]

    **See Also:**[log](<#log>)

## 

matrix(pattern)

Converts a string pattern to a matrix. The pattern should start with a square bracket, followed by a series of rows (specified as vector patterns - see the vector() function), followed by a trailing square bracket. 
[code] 
    matrix("")
    
[/code]

## 

max(value1, value2)

Returns the larger of value1 or value2. 
[code] 
    max(5,3)=5
    
[/code]

    **See Also:**[min](<#min>)

## 

mcols(mat)

Returns the number of columns in a matrix 

## 

min(value1, value2)

Returns the smaller of value1 or value2. 
[code] 
    min(5,3)=3
    
[/code]

    **See Also:**[max](<#max>)

## 

mindist(SOP, point_num, SOP, prim_num, return_type)

Given a point and a primitive, this function will find the distance between the point and the closest spot on the primitive. This expression is an alias for pointdist(). 

    **See Also:**[pointdist](<#pointdist>) [primdist](<#primdist>) [distance](<#distance>) [uvdist](<#uvdist>)

## 

mlookat(from, to)

Computes a transform matrix specifying a lookat from the from point to he to point. The from and to vectors are converted to 3 vectors for this computation. The resulting matrix will be a 3x3 matrix. 

## 

mlookatup(from, to, up)

Computes a transform matrix specifying a lookat from the from point to the to point. The from and to vectors are converted to 3 vectors for this computation. up is the up vector used in the calculation. The resulting matrix will be a 3x3 matrix. 

## 

modblend(val1, val2, length, weight)

Blends the two modular values. This function can be used to correctly blend two angles or other cyclic values. 
[code] 
    # will evaluate to 0. Simple linearly blending of the two values would result in an incorrect value of 180.
    modblend(355, 5, 360, 0.5)
    
[/code]

## 

monitorcount()

Will return the coordinate of the bottom bounds of the monitor. monitorindex is a 0-based index. 

    **See Also:**[coordtomonitor](<#coordtomonitor>) [monitorright](<#monitorright>) [monitortop](<#monitortop>) [monitorleft](<#monitorleft>)

## 

monitorcount()

Will return the number of monitors Touch can access. 

    **See Also:**[monitorwidth](<#monitorwidth>) [monitorheight](<#monitorheight>) [coordtomonitor](<#coordtomonitor>)

## 

monitorbottom(monitorcount, coordtomonitor)

Will return the height of the monitor. monitorindex is a 0-based index. 

    **See Also:**[monitorw](<#monitorw>) [monitorright](<#monitorright>) [monitortop](<#monitortop>) [monitorleft](<#monitorleft>)

## 

monitorleft(monitorindex)

Will return the coordinate of the left bounds of the monitor. monitorindex is a 0-based index. 

    **See Also:**[monitortop](<#monitortop>) [monitorbottom](<#monitorbottom>) [monitorright](<#monitorright>) [monitorcount](<#monitorcount>)

## 

monitorright(monitorindex)

Will return the coordinate of the right bounds of the monitor. monitorindex is a 0-based index. 

    **See Also:**[monitortop](<#monitortop>) [monitorbottom](<#monitorbottom>) [monitorleft](<#monitorleft>) [monitorcount](<#monitorcount>)

## 

monitortop(monitorindex)

Will return the coordinate of the top bounds of the monitor. monitorindex is a 0-based index. 

    **See Also:**[monitorright](<#monitorright>) [monitorbottom](<#monitorbottom>) [monitorleft](<#monitorleft>) [monitorcount](<#monitorcount>)

## 

monitorbottom(monitorcount)

Will return the width of the monitor. monitorindex is a 0-based index. 

    **See Also:**[monitorh](<#monitorh>) [monitorright](<#monitorright>) [monitortop](<#monitortop>) [monitorleft](<#monitorleft>)

## 

mouse(attribute)

This function returns the current state of the mouse. Return values are 0 or 1. Attribute can be: 
* x returns the X position
  * y returns the Y position
  * l returns the left button state.
  * m returns the middle button state.
  * r returns the right button state.


[code]
    mouse("x")
    mouse("m")
    
[/code]

    **See Also:**[keystate](<#keystate>)

## 

mrows(mat)

Returns the number of rows in a matrix 

## 

mzero(mat)

Sets all values of the matrix to 0. 

## 

noevals(expression)

This function will return as string passed in as a form that will not be expanded. It's primary use is for returning raw results from commands. This function returns a string value. 
[code] 
    echo`noevals(tab("table1", 0, 0))`[/code]

## 

noise(X, Y, Z)

This function can be used to apply noise to geometry. 
[code] 
    # To make a bumpy grid you could append a point SOP and use the following in the pos Z field:
    noise($TX, $TY, $TZ)
    
[/code]

    **See Also:**[snoise](<#snoise>) [turb](<#turb>) [sturb](<#sturb>)

## 

normal(SOP, prim_num, u, v, index)

Evaluates the X, Y, or Z component of the surface normal at the parametric (u,v) location. u and v are unit values, defined in the [0,1] interval. Note: if the primitive is a mesh, u and v are defined in terms its number of rows and columns. 

    **See Also:**[unituv](<#unituv>) [primuv](<#primuv>) [primduv](<#primduv>) [curvature](<#curvature>)

## 

normalize(v)

Returns the normalized vector 

## 

npointgroups(name)

This function returns the number of point groups in the SOP. 

    **See Also:**[npoints](<#npoints>) [nprims](<#nprims>) [nprimgroups](<#nprimgroups>)

## 

npoints(name)

This function returns the number of points in the SOP. 

    **See Also:**[nprims](<#nprims>) [nprimgroups](<#nprimgroups>) [npointgroups](<#npointgroups>)

## 

nprimgroups(name)

This function returns the number of primtive groups in the SOP. -1 is returned if the SOP cannot be cooked. 

    **See Also:**[npoints](<#npoints>) [nprims](<#nprims>) [npointgroups](<#npointgroups>)

## 

nprims(name)

This function returns the number of primtives in the SOP. -1 is returned if the SOP cannot be cooked. 

    **See Also:**[npoints](<#npoints>) [nprimgroups](<#nprimgroups>) [npointgroups](<#npointgroups>)

## 

objdist(comp1, comp2)

This function will return the distance between the origins of the components. 

    **See Also:**[origin](<#origin>) [vorigin](<#vorigin>) [vtorigin](<#vtorigin>) [vrorigin](<#vrorigin>) [originoffset](<#originoffset>)

## 

oc(output_channel_index, index)

Returns the value of a CHOP's output at the specified sample index. 
[code] 
    oc(0, 10)
    
[/code]

    **See Also:**[ics](<#ics>) [ic](<#ic>) [ice](<#ice>) [icr](<#icr>) [icn](<#icn>) [icmin](<#icmin>) [icmax](<#icmax>) [icl](<#icl>)

## 

opbase(name)

This function will return the non-numeric portion of a node's name. It is used when building several similar networks. 
[code] 
    opbase("/obj/ramp12") = "ramp"
    opbase("..") = "geo"	# (if the parent is geo1)
    
[/code]

    **See Also:**[digits](<#digits>) [base](<#base>) [opdigits](<#opdigits>)

## 

opcompinput(name, index)

Will return the name of the operator that is connected to the Component input of the given index. 

    **See Also:**[opcompinputf](<#opcompinputf>) [opncompinputs](<#opncompinputs>) [opcompoutput](<#opcompoutput>) [opncompoutputs](<#opncompoutputs>)

## 

opcompinputf(name, index)

Will return the full path of the operator that is connected to the Component input of the given index. 

    **See Also:**[opcompinput](<#opcompinput>) [opncompinputs](<#opncompinputs>) [opcompoutput](<#opcompoutput>) [opncompoutputs](<#opncompoutputs>)

## 

opcompoutput(name, compindex, outindex)

Will return the name of the operator which connects to the given node. compindex is the index of the Component output on the COMP. outindex is the index of the node connected to the output (in the case where multiple nodes are connected to the same output) 

    **See Also:**[opcompinput](<#opcompinput>) [opncompinputs](<#opncompinputs>) [opncompoutputs](<#opncompoutputs>)

## 

opcompoutputf(name, compindex, outindex)

Will print the full path of the operator which connects to the given node. 
* compindex is the index of the Component output on the COMP.
  * outindex is the index of the node connected to the output (in the case where multiple nodes are connected to the same output)


    **See Also:**[opcompinput](<#opcompinput>) [opncompinputs](<#opncompinputs>) [opcompoutput](<#opcompoutput>) [opncompoutputs](<#opncompoutputs>)

## 

opcurrent(, network)

This function returns the name of the current node in a network, or an empty string it the network has no children. The same value may be obtained by the $CURRENT variable, when used within a component. 
[code] 
    ->echo`opcurrent("/project1")`moviein1
    
[/code]

    **See Also:**[opflag](<#opflag>) [opflags](<#opflags>) [opselect](<#opselect>)

## 

opdigits(name)

This function will return the numeric value of the last set of consecutive digits in a node's name. It is used when building several similar networks. This expression expects a path to a node, if the node doesn't exist, it will return 0. opdigits(".") means the digits of the node that the expression is in. Tip: It is the same as the variable $OD. opdigits("..") means the digits of the parent of the node. Tip: It is the same as the variable $OPD. opdigits("../..") is the digits of the parent of the parent. 
[code] 
    opdigits("/obj/geo22")  = 22
    opdigits("..") = 7	# (if the current component is named geo7 for example)
    
[/code]

    **See Also:**[opname](<#opname>) [digits](<#digits>) [opbase](<#opbase>) [base](<#base>) [opfullpath](<#opfullpath>)

## 

opexists(op)

This function will return 1 if the operator exists. 

## 

opflag(node, flag)

This function returns the state of the specified flag. Currently the flags recognized are: 
* d Display Flag
  * r Render Flag
  * v Preview Flag
  * l Locked Flag
  * p Picked Flag
  * C Current Flag
  * t Template Flag
  * o Export Flag
  * b Bypass Flag
  * e Expose Flag
  * k Pickable Flag
  * c Allow Cooking Flag (recursive)
  * i Immune to Cloning Flag
  * n Component and Contents Immune to Cloning Flag (Network Clone Immune)
  * Y Parameters to be Displayed
  * y Parameters to be Displayed Minimized


[code]
    # Return the display state
    touch -> echo`opflag("/geo1", "d")`# Return the render state
    touch -> echo`opflag("/comp/blur1", "r")`[/code]

    **See Also:**[opflags](<#opflags>) [opselect](<#opselect>)

## 

opflags(component, flag)

This function builds a string of all the nodes which have the particular flag set. Currently these flags recognized are: 
* d Display Flag
  * r Render Flag
  * v Preview Flag
  * l Locked Flag
  * p Picked Flag
  * C Current Flag
  * t Template Flag
  * o Export Flag
  * b Bypass Flag
  * e Expose Flag
  * k Pickable Flag
  * x Axis Flag
  * i Immune to Cloning Flag
  * Y Parameters to be Displayed
  * y Parameters to be Displayed Minimized


[code]
    # List all rendered objects
    touch -> echo`opflags("/obj", "d")`# List all locked SOPs in object geo1
    touch -> echo`opflags("/obj/geo1", "l")`[/code]

    **See Also:**[opflag](<#opflag>) [opselect](<#opselect>)

## 

opfullpath(op)

This function will return the full path to the operator specified. 

    **See Also:**[opname](<#opname>) [oprelpath](<#oprelpath>) [parrelpath](<#parrelpath>)

## 

opidtopath(op)

This function will return the path of the node with the unique ID 
[code] 
    opidtopath(39)
    
[/code]

    **See Also:**[oppathtoid](<#oppathtoid>)

## 

opinfo(OP, infoname)

This expression is used to retrieve the same information about an OP that is available in an Info CHOP pointed at that OP. infoname should be the name of a channel available in the Info CHOP for that OP. 
[code] 
    opinfo("/moviein1", "resx")
    
[/code]

## 

opinfop(OP, infoname)

The same as the opinfo() expression except this version is passive and therefor will not cook the node specified. 
[code] 
    opinfop("/moviein1", "resx")
    
[/code]

## 

opinput(name, index)

Will print the name of the operator that is connected to the input of the given index. 

    **See Also:**[opinputf](<#opinputf>) [opninputs](<#opninputs>) [opoutput](<#opoutput>) [opnoutputs](<#opnoutputs>) [ip](<#ip>) [ipf](<#ipf>)

## 

opinputf(name, index)

Will print the full path of the operator that is connected to the input of the given index. 

    **See Also:**[opinput](<#opinput>) [opninputs](<#opninputs>) [opoutput](<#opoutput>) [opnoutputs](<#opnoutputs>) [ip](<#ip>) [ipf](<#ipf>)

## 

oplegalname(string)

Returns the string, with all characters that are illegal for a node path changed to _. A relative path, absolute path, or single node name may be given. 
[code] 
    oplegalname("/project1/bad-name!") = "/project1/bad_name_"
    
[/code]

## 

opname(name)

This function will print the name of the node given. It's main use is to find out the name of the network containing the node. For example, if used in a SOP, opname("..") will give the name of the object containing the SOP. opname(".") means the name of the node that the expression is in. Tip: It is the same as the variable $ON. opname("..") means the name of the parent of the node. Tip: It is the same as the variable $OPN. opname("../..") is the name of the parent of the parent. 
[code] 
    opname("/obj/geo22") = geo22
    opname("..") = obj	# (if the expression is in the component is named /obj/geo22)
    
[/code]

    **See Also:**[opfullpath](<#opfullpath>) [opdigits](<#opdigits>)

## 

opncompoutputs()

Returns the number of Component inputs that the COMP has with nodes connected to them. 

    **See Also:**[opcompinput](<#opcompinput>) [opcompinputf](<#opcompinputf>) [opcompoutput](<#opcompoutput>) [opcompoutputf](<#opcompoutputf>)

## 

opncompinputs()

Returns the number of nodes connected to the Component output specified by compindex. 

    **See Also:**[opcompinput](<#opcompinput>) [opcompinputf](<#opcompinputf>) [opcompoutput](<#opcompoutput>) [opcompoutputf](<#opcompoutputf>)

## 

opninputs(name)

Returns the maximum number of inputs that the node has connected. It is possible to have blank inputs (i.e. that aren't connected). 

    **See Also:**[opinput](<#opinput>) [opinputf](<#opinputf>) [opoutput](<#opoutput>) [opoutputf](<#opoutputf>) [opnoutputs](<#opnoutputs>) [ip](<#ip>) [ipf](<#ipf>)

## 

opnoutputs(name)

Returns the number of nodes which are connected to the output of the specified node. 

    **See Also:**[opinput](<#opinput>) [opinputf](<#opinputf>) [opoutput](<#opoutput>) [opoutputf](<#opoutputf>) [opninputs](<#opninputs>) [ip](<#ip>) [ipf](<#ipf>)

## 

opnumchildren(name)

This function will return the number of children a COMP has. This includes all node types, TOPs, SOPs, other COMPs etc. If the given node can't be found or is not a COMP, this function will return 0 
[code] 
    opnumchildren("/project1")  = 1
    
[/code]

## 

opnumchildrentype(name, type)

This function will return the number of children of a particular type a COMP has. Legal values for type are COMP, PANEL, OBJ, TOP, CHOP, DAT, MAT and ANY. ANY is the same as using opnumchildren. If the given node can't be found or is not a COMP, this function will return 0 
[code] 
    opnumchildrentype("/project1", "TOP")  = 1
    
[/code]

## 

opoutput(name, index)

Will print the name of the operator which connects to the given node. 

    **See Also:**[opinput](<#opinput>) [opninputs](<#opninputs>) [opoutputf](<#opoutputf>) [opnoutputs](<#opnoutputs>) [ip](<#ip>) [ipf](<#ipf>)

## 

opoutputf(name, index)

Will print the full path of the operator which connects to the given node. 

    **See Also:**[opinput](<#opinput>) [opninputs](<#opninputs>) [opoutput](<#opoutput>) [opnoutputs](<#opnoutputs>) [ip](<#ip>) [ipf](<#ipf>)

## 

opnoutputs()

Returns the relative path to the n'th parent of the specified node. For example opparent(".", 0) would return the containing component of the current node. opparent(".", 1) would return that component's parent, etc. In the case of Panel Components, parents may also be wired input connections. 

    **See Also:**[opparentf](<#opparentf>) [opinput](<#opinput>) [opinputf](<#opinputf>) [opoutput](<#opoutput>) [opoutputf](<#opoutputf>) [opninputs](<#opninputs>)

## 

opnoutputs()

Returns the full path to the n'th parent of the specified node. For example opparentf(".", 0) would return the containing component of the current node. opparentf(".", 1) would return that component's parent, etc. In the case of Panel Components, parents may also be wired input connections. 

    **See Also:**[opparent](<#opparent>) [opinput](<#opinput>) [opinputf](<#opinputf>) [opoutput](<#opoutput>) [opoutputf](<#opoutputf>) [opninputs](<#opninputs>)

## 

opparinfo(path, parameter, type)

This will return details from a specified parameter. Type may be one of: 
* e return the enable state.
  * d return the default state.
  * x return the expression.
  * s return the string value.
  * o return the override information.


[code]
    opparinfo("/project1", "tx", "x")
    
[/code]

## 

oppathtoid(op)

This function will return the unique ID of the specified operator. 
[code] 
    oppathtoid("/project1/moviein1")
    
[/code]

    **See Also:**[opidtopath](<#opidtopath>)

## 

oppwf()

This is a short cut for execute("oppwf"). 

    **See Also:**[execute](<#execute>)

## 

oprelpath(op, string)

This function will return the relative path between the specified operators. 
[code] 
    oprelpath("/project1/geo1", "/project1/geo1") = "."
    oprelpath("/project1/geo1", "/project1/geo2") = "geo2"
    
[/code]

    **See Also:**[opname](<#opname>) [opfullpath](<#opfullpath>) [parrelpath](<#parrelpath>)

## 

opparent(opparentf, oprootf)

Will return the path of the root node of the hierarchy containing the specified path. 

    **See Also:**[opinput](<#opinput>) [opninputs](<#opninputs>) [opoutput](<#opoutput>) [opnoutputs](<#opnoutputs>) [opcompinputf](<#opcompinputf>)

## 

opparent(opparentf, oproot)

Will return the full path of the root node of the hierarchy containing the specified path. 

    **See Also:**[opinput](<#opinput>) [opninputs](<#opninputs>) [opoutput](<#opoutput>) [opnoutputs](<#opnoutputs>) [opcompinputf](<#opcompinputf>)

## 

opselect(network)

This function returns a string of all the selected nodes in a network. The same value may be obtained by the $SELECT variable, when used within a component. 
[code] 
    -> echo`opselect("/project1")`out1 moviein1
    
[/code]

    **See Also:**[opflag](<#opflag>) [opflags](<#opflags>) [opcurrent](<#opcurrent>)

## 

opsinfo(string, string)

This will return the value associated with the operator. If the info associated with the node is text only, all the text will be returned. If the info is table based, the cells from the second column on will be concatenated together with tabs. 
[code] 
    opsinfo("/text1", "selected_text")
    
[/code]

## 

opsinfop(string, string)

This will return the value associated with the operator. If the info associated with the node is text only, all the text will be returned. If the info is table based, the cells from the second column on will be concatenated together with tabs. Contrary to the opsinfo() expression, this is passive and therefor will not cook the node specified. 
[code] 
    opsinfop("/text1", "selected_text")
    
[/code]

## 

opsubtype(, name)

This function will return the subtype of the specified operator. 
[code] 
    # Will return "object" indicating that node geo1 is a type of object component.
    opsubtype("/obj/geo1")
    
[/code]

    **See Also:**[optype](<#optype>)

## 

optransform(object_name)

Returns the matrix specifying the transform of the object at the current time. 

## 

optype(name)

This function will print the family and type of operator that the node specified is. 
[code] 
    # Will return COMP:geo, indicating that object geo1 is a Geo COMP.
    optype("/obj/geo1")
    
[/code]

    **See Also:**[opsubtype](<#opsubtype>)

## 

origin(, obj1, obj2, constant_type)

This function will return one of TX, TY, TZ, RX, RY, RZ, SX, SY, SZ value necessary to transform obj1 to obj2, depending on the type argument ("TX", "TY", "TZ", "RX", "RY", "RZ", "SX", "SY", "SZ"). This can also be thought of as the position of obj2 relative to obj1. It will compute the position of obj1 relative to obj2 and returns one of TX, TY, TZ, RX, RY, RZ, SX, SY, SZ based on the type argument If obj1 is the emptry string "", then the world space position of obj2 is returned. 

    **See Also:**[objdist](<#objdist>) [vorigin](<#vorigin>) [vtorigin](<#vtorigin>) [vrorigin](<#vrorigin>) [originoffset](<#originoffset>)

## 

originoffset(obj1, pos1, obj2, pos2, constant_type)

This function will return one of TX, TY, TZ, RX, RY, RZ, SX, SY, SZ value necessary to transform the point pos1 in the space of object obj1 to point pos2 in the space of object obj2, depending on the type argument ("TX", "TY", "TZ", "RX", "RY", "RZ", "SX", "SY", "SZ"). This can also be thought of as the position of pos2 in obj2 relative to pos1 in obj1. If obj1 is the emptry string "", then the world space position of obj2 is returned. 

    **See Also:**[objdist](<#objdist>) [origin](<#origin>) [vorigin](<#vorigin>) [vtorigin](<#vtorigin>) [vrorigin](<#vrorigin>)

## 

padzero(number, value)

Returns a string containing value preceded by enough zeros to make up number digits 
[code] 
    padzero(5, 126) = 00126
    padzerp(5, 23) = 00023
    padzero(1, 23) = 23
    
[/code]

    **See Also:**[format](<#format>)

## 

panel(path, panelvaluename)

Returns a panel value from a component. The panelvaluename is one of the panel value names found in the Panel Value list, such as rollover. The path is the location of the panel component, where .. is the parent of the node that panel() is located in. 
[code] 
    panel("/button1", "state")
    panel("/field1", "field")
    
[/code]

    **See Also:**[panelstr](<#panelstr>) [panelstrp](<#panelstrp>) [panelp](<#panelp>)

## 

panellocate(path, parent_path, vector_index)

Returns the bottom left location of the panel specified by path relative to the parent panel in the window under the mouse If the parent_path isn't specified then the top most panel is assumed. Returns 0 if no panel pointed to by path can be found in the window. vector_index can be one of x,y or 0,1. 
[code] 
    panellocate("/container1/button1", "", "0")
    panellocate("/container1/field1", "/container1", "y")
    
[/code]

## 

panelmouse(path, vector_index)

Returns the current mouse location relative to a panel in the window under the mouse. Returns 0 if no panel pointed to by path can be found in the window. vector_index can be one of x, y, u, v or 0, 1, 2, 3. 
[code] 
    panelmouse("/container1/button1", "x")
    panelmouse("/container1/field1", 0)
    
[/code]

## 

panelp(path, varname)

Returns a panel value from a component. This is the passive version of panel() which does not cook the component first. Use this to avoid infinite recursion dependencies. 
[code] 
    panelp("/button1", "state")
    panelp("/field1", "field")
    
[/code]

    **See Also:**[panelstr](<#panelstr>) [panelstrp](<#panelstrp>) [panel](<#panel>)

## 

panelscreen(path, vector_index)

Returns the bottom left location of the panel specified by path relative to the screen. Vector_index can be one of x,y,0,1 for panel under mouse. Returns 0 if no panel found in the window under the mouse. Vector_index can be one of l,r,b,t for the left, right, bottom and top coords of a panel. The panel is searched in the window under the mouse first, and if it is not found, searched for in other windows. Will return 0 if no panel exists for the path. 
[code] 
    panelscreen("/container1/button1", "x")
    
[/code]

## 

panelstr(path, varname)

Returns a panel value from a component as a text string. 
[code] 
    panelstr("/button1", "state")
    panelstr("/field1", "field")
    
[/code]

    **See Also:**[panel](<#panel>) [panelstrp](<#panelstrp>) [panelp](<#panelp>)

## 

panelstrp(, path, varname)

Returns a panel value from a component as a text string. This is the passive version of panelstr() which does not cook the component first. Use this to avoid infinite recursion dependencies. 
[code] 
    panelstrp("/button1", "state")
    panelstrp("/field1", "field")
    
[/code]

    **See Also:**[panel](<#panel>) [panelstr](<#panelstr>) [panelp](<#panelp>)

## 

par(, parameter, path, parameter)

Will evaluate the parameter specified. The second form includes a path to the parameter. 
[code] 
    # Return panelw of node /project1:
    par("/project1:panelw")
    # Get panelw from the parent node:
    par("..:panelw")
    # Return ty in the node that the expression is in:
    par("ty")
    # And older form allows a / instead of ::
    par("/project1/panelw")
    
[/code]

    **See Also:**[pars](<#pars>) [parsraw](<#parsraw>)

## 

param(token, value)

Returns the global parameter value associated with the token, or value if not defined. This function is used with stamping operators (eg. Copy SOP, LSystem SOP). 
[code] 
    param("sides", 5)
    param("fuzzy", 0.5
    
[/code]

## 

parevalpath(parameter)

Will evaluate the parameter as an operator path. This is useful for evaluating parameters with relative paths. The string will be expanded automatically by this function (at the current time). 

    **See Also:**[par](<#par>) [parf](<#parf>) [part](<#part>) [parsraw](<#parsraw>) [pars](<#pars>)

## 

parmlsvar(string, string)

## 

parrelpath(op, string, string)

This function will return the relative path between the specified operators. 
[code] 
    parrelpath("/project1/geo1", "/project1/geo1", "tx") = "tx"
    parrelpath("/project1/geo1", "/project1/geo2", "tx") = "geo2/tx"
    
[/code]

    **See Also:**[opname](<#opname>) [opfullpath](<#opfullpath>) [oprelpath](<#oprelpath>)

## 

pars(parameter)

Will evaluate the parameter as a string. This is useful for evaluating filenames in parameters. The string will be expanded automatically by this function (at the current time). 

    **See Also:**[par](<#par>) [parsraw](<#parsraw>)

## 

parsraw(parameter)

Will return the unevaluated parameter as a string. This is useful for obtaining the raw expression of a parameter. 

    **See Also:**[par](<#par>) [pars](<#pars>)

## 

point(SOP, point_number, attribute, index)

This function will extract information from a point in a SOP. The attribute parameter is the name of the attribute (eg. Cd for diffuse color). Two special attributes exist, P and Pw, which represent the position of the point in space (Pw allows you to access the W component of the position, index is ignored in this case). P with an index of 3 is the same as Pw. See Geometry Detail, SOP, Primitive. 
[code] 
    # Will return the X component of point 3 of the facet1 SOP in geo1.
    point("/obj/geo1/facet1", 3, "P", 0)
    # Will return the Z component of the normal attribute of point 3 in the facet1 SOP of object geo1.
    point("/obj/geo1/facet1", 3, "N", 2)
    # Note: This function will interpolate between point values if the point number is fractional, such as 3.35.
    
[/code]

## 

pointavg(SOP, attribute, index)

This function works much like the point function, except that it returns the average value of the attribute for all points in the specified sop. attribute The attribute name to get, use P for the position index 

The index of component of the attribute you want to get for example with attribute N (normals), ) will be the X component, 1 will be the Y component and 2 will be the Z component 
[code] 
    pointavg("project1/sphere1", "P", 1)
    
[/code]

## 

pointdist(SOP, point_num, SOP, prim_num, return_type)

Given a point and a primitive, this function finds the distance between the point and the closest spot on the primitive. 
* return_type 0 yields the minimum distance.
  * return_type 1 yields the u parametric value at the point of minimum distance.
  * return_type 2 yields the v parametric value at the point of minimum distance.


[code]
    # Will return the distance between point 0 of add1 and the closest spot from the surface of grid1 primitive number 0. 
    # If the return_type were 1, the u parametric value that is closest to the point would be returned:
    pointdist("/obj/geo1/add1", 0, "/obj/geo1/grid1", 0, 0)
    
[/code]

    **See Also:**[primdist](<#primdist>)

## 

pointlist(sop, group_name)

This function returns a string containing all the points in the point group specified. The string is a space separated list of numbers. 

    **See Also:**[haspoint](<#haspoint>) [hasprim](<#hasprim>) [primlist](<#primlist>)

## 

points(SOP, point_number, attribute)

This function will return the value of a string attribute for a given point of a SOP. 
[code] 
    # Will return the string associated with the string attribute "instance" for point 3 in the facet1 SOP in geo1:
    points("/obj/geo1/facet1", 3, "instance")
    
[/code]

## 

pow(base, exponent)

This computes the base to the power given. 
[code] 
    pow(2, 3) = 8
    
[/code]

## 

prim(SOP, prim_num, attrib_name, attrib_index)

This function can be used to get information about a specified primitive. When given the P or Pw attribute, the centroid of the primitive will be returned. When using Pw the index is ignored. P with an index of 3 is the same as Pw. 
[code] 
    # Will evaluate the X component of the centroid of primitive 3 in the sop specified.
    prim("/obj/geo1/facet1", 3, "P", 0)
    # Will evaluate the green color of the Cd attribute of primitive 3.
    prim("/obj/geo1/facet1", 3, "Cd", 1)
    
[/code]

    **See Also:**[primuv](<#primuv>) [point](<#point>)

## 

primdist(SOP, prim1_num, SOP, prim2_num, return_type)

This expression finds the minimum distance between two primitives. 
* return_type 0 yields the minimum distance.
  * return_type 1 yields prim1's u value at the point of minimum distance.
  * return_type 2 yields prim1's v value at the point of minimum distance.
  * return_type 3 yields prim2's u value at the point of minimum distance.
  * return_type 4 yields prim2's v value at the point of minimum distance.


Currently, primdist() will return 0 unless given face types (polygons and/or curves) or spline surfaces. 
[code] 
    # Will return the distance between the first primitives in both sphere1 and grid1.
    primdist("/obj/geo1/sphere1", 0, "/obj/geo1/grid1", 0, 0)
    
[/code]

    **See Also:**[pointdist](<#pointdist>)

## 

primduv(SOP, prim_num, attrib_name, attrib_index, u, v, du, dv)

Evaluates the (partial) derivatives of a face or hull attribute at a parametric (u,v) position. u and v are unit values, defined in the [0,1] interval. When given the P or Pw attribute, the positional derivative of (u,v)'s image on the primitive will be returned. If the primitive is a face type, v and dv are ignored. If both du and dv are 0, primduv becomes equivalent to primuv(). 

Note: if the primitive is a polygon or a mesh, u and v are defined in terms of the number of vertices, or rows or columns respectively. 
[code] 
    # Will evaluate the Z component of the first-order partial derivative of primitive 12 with respect to u, at the parametric location (0.4,0.5).
    primduv("/obj/geo1/tube1", 12, "P", 2, 0.4, 0.5, 1, 0)
    
[/code]

    **See Also:**[primuv](<#primuv>) [normal](<#normal>) [curvature](<#curvature>) [unituv](<#unituv>)

## 

primlist(sop, group_name)

This function returns a string containing all the primitives in the primitive group specified. The string is a space separated list of numbers. 

    **See Also:**[haspoint](<#haspoint>) [hasprim](<#hasprim>) [pointlist](<#pointlist>)

## 

prims(SOP, primitive_number, attribute)

This function will return the value of a string attribute for a given primitive in a SOP. 
[code] 
    # Will return the string associated with the string attribute texturemap for primitive 3 in the facet1 SOP in geo1.
    prims("/obj/geo1/facet1", 3, "texturemap")
    
[/code]

## 

primuv(SOP, prim_num, attrib_name, attrib_index, u, v)

Evaluates the specified attribute at a parametric (u,v) position on the primitive. u and v are unit values, defined in the [0,1] interval. When given the P or Pw attribute, the x, y, z or weight image of the (u,v) domain point will be returned. If the primitive is a face type or a circle, v is ignored. 

Note: if the primitive is a polygon or a mesh, u and v are defined in terms of the number of vertices, or rows or columns respectively. Currently, only the positional attribute of quadric primitives can be evaluated. 
[code] 
    # Will evaluate the Green component of the diffuse color attribute at a location on primitive 0 given by the parametric coordinates (0.7,0.3).
    primuv("/obj/geo1/tube1", 0, "Cd", 1, 0.7, 0.3)
    
[/code]

    **See Also:**[primduv](<#primduv>) [normal](<#normal>) [curvature](<#curvature>) [unituv](<#unituv>)

## 

print(label, value)

Prints the label into the textport and returns the value. This can be used to diagnose parameter expressions. 

## 

pulse(value, start, end)

This function creates an on/off pulse. If the value is less than start or greater than end, pulse returns a 0. Otherwise, it returns 1. Frequently, start and end are frame numbers and val is the current frame, $F. 

## 

quintic()

A channel interpolation function which uses the slopes and accelerations to smoothly interpolate the segment. 

## 

rad(number)

Converts the number to radians assuming that the number is measured in degrees. 
[code] 
    rad(180)=3.1415926
    
[/code]

## 

rand(value)

Gives a pseudo-random number between 0 and 1 depending on the value. If the same value is used the same number will result each time. A different number is returned if fractional values are different. NOTE: It is a good idea to use non-integer values as the argument to rand() 
[code] 
    rand(12.1)
    
[/code]

## 

raw()

This is a channel interpolation function for raw channels. 

## 

realuv(SOP, prim_num, uv_unit, D_U

Returns the real u or v parametric value, given the unit value of the same parameter. The unit value is defined in the [0,1] interval. The real value is defined in the valid interval of the primitive's domain if the primitive is a spline type. If the primitive is a polygon or a mesh, the size of its domain is given by the number of vertices, or rows or columns respectively. If the primitive is a polygon or a curve, D_U and D_V are irrelevant. Note: the result is undefined if the primitive is neither a face nor a hull. 

    **See Also:**[unituv](<#unituv>)

## 

repeat(f1, f2)

A channel interpolation function which repeats the motion between frames f1 and f2. 

    **See Also:**[repeatt](<#repeatt>)

## 

repeatt(t1, t2)

A channel interpolation function which repeats the motion between timest1 and t2. 

    **See Also:**[repeat](<#repeat>)

## 

rgb(hue, saturation, value, component)

Converts the color specified by hue, saturation, value to RGB. The component is a string which should be one of r, g or b. 
[code] 
    rgb(270, .5, 1, "b")
    
[/code]

    **See Also:**[hsv](<#hsv>)

## 

rindex(source, pattern)

Finds the last occurrence of pattern in source and returns the number of characters before the pattern occurs. If the pattern is not found -1 is returned. 
[code] 
    # Will return 2:
    touch -> echo`rindex("Testing rindex", "sting")`# Will return 9:
    touch -> echo`rindex("Testing rindex", "i")`[/code]

    **See Also:**[index](<#index>)

## 

rint()

Will round to the nearest integer. When the fractional component is .5 exactly, the function will round to the nearest even integer. 

    **See Also:**[round](<#round>)

## 

rotate(angle, axis)

Computes a 4x4 rotation matrix of a rotation specified by the angle (in degrees) around an axis. The axis should be a string which is one of x, y or z. 

    **See Also:**[rotaxis](<#rotaxis>) [scale](<#scale>) [translate](<#translate>)

## 

rotaxis(angle, axis)

Computes a 4x4 rotation matrix of a rotation specified by the angle around the axis specified by the vector. The vector is converted to a 3 vector for the purposes of this computation. 

    **See Also:**[rotate](<#rotate>) [scale](<#scale>) [translate](<#translate>)

## 

round(float)

Rounds to the nearest integer. When the fractional component is .5 exactly, the function will round to the nearest even integer. Also the Math CHOP has a Round option in its Integer parameter. 
[code] 
    round(2.501)=3
    round(-2.501)=-3
    round(0.2)=0
    round(-.2)=0
    
[/code]

    **See Also:**[format](<#format>) [trunc](<#trunc>) [float](<#float>) [int](<#int>) [ceil](<#ceil>) [floor](<#floor>)

## 

run(command)

This is a short form for the execute function. The command specified will be executed and string returned will be the output of the command. The command is a touch command. 

## 

scale(sx, sy, sz)

Computes a scale matrix given by the three scale values. 

    **See Also:**[rotate](<#rotate>) [rotaxis](<#rotaxis>) [translate](<#translate>)

## 

sign(value)

The sign of the value. For example, it returns 1 if the value is any positive number, -1 if the value is a negative number and 0 if the value is 0. 

## 

sin(float)

This is a trigonometric mathematical function used to express the sine value of the number. 
[code] 
    sin(60) = 0.866025
    
[/code]

## 

sinh(number)

The hyperbolic sine of the number. 

## 

smooth(value, minimum, maximum)

The return value is a smooth interpolation between 0 and 1. When the value is less than the minimum, the return value is 0. If the value is greater than the maximum, the return value is 1. 
[code] 
    # This will generate an ease-type curve between values 0 and 1, starting at frame 12 and ending at frame 55.
    smooth ($F, 12, 55)
    
[/code]

## 

snoise(X, Y, Z)

This function applies noise based on sparse convolution. 
[code] 
    noise($TX, $TY, $TZ)
    
[/code]

    **See Also:**[noise](<#noise>) [turb](<#turb>) [sturb](<#sturb>)

## 

spknot(SOP, prim_num, knot_index, D_U, D_V)

This spline-specific function returns the floating-point knot value, given the knot_index in the U or V knot sequence. The first valid knot_index is 0. If the primitive is a Bezier curve or surface, the values returned are those of its breakpoints. If the primitive is a curve, D_U and D_V are irrelevant. 

## 

spline(t1, t2, tension)

A channel interpolation function which runs a spline through the timemarks specified by t1 and t2 (including all the timemarks between t1 and t2). The tension specifies the tension of the spline. 

## 

sqrt(number)

The Square root of the number. 
[code] 
    sqrt(144)=12
    
[/code]

## 

strcasecmp(s1, s2)

String comparison which ignores case of string. Return codes are: 
* negative if s1 < s2
  * positive if s1 > s2
  * zero if s1 == s2

## 

strcasematch(pattern, s)

Does pattern matching comparison for a string ignoring case sensitivity. If the pattern matches the string, the return code will be 1 otherwise, the return code will be 0. Multiple patterns may be specified using a comma separated list. 
[code] 
    # Will return 1:
    strcasematch("FOO*", "foobar")
    # Will return 0:
    strcasematch("?baR", "fred")
    # Will return 1:
    strcasematch("FoO*,bAr*, "bar")
    
[/code]

    **See Also:**[strcmp](<#strcmp>) [strcasecmp](<#strcasecmp>)

## 

strcat(s1, s2)

This will concatenate two strings. 
[code] 
    # Will return Current motion file is job1.bmot:
    strcat("Current motion file is; ", $MOTNAME)
    
[/code]

## 

strcmp(s1, s2)

Returns a negative number if s1 is lexicographically less than s2 Returns a positive number if s1 is lexicographically greater than s2 Returns a zero if s1 is equal to s2 
[code] 
    strcmp("abc", "xyz")=-1
    strcmp("xyz, "abc")=1
    strcmp("abc", "abc")=0
    
[/code]

## 

stripmatrix(mat)

This function will strip out all non-essential characters from the string representation of a matrix or vector. This is useful when you want to interpret the values of the matrix (i.e. to pass to a VEX function). A string containing the floating point numbers (and only the numbers) which make up the matrix will be returned. 
[code] 
    stripmatrix(identity(3)) = "1 0 0  0 1 0  0 0 1"
    stripmatrix(vector3(1,2,3) = "1 2 3"
    
[/code]

## 

strlen(string)

Returns the number of characters in the string. 
[code] 
    strlen("abcde")=5
    
[/code]

## 

strmatch(pattern, s)

Does pattern matching comparison for a string. If the string matches the pattern, then the return code will be 1, otherwise it will be 0. Multiple patterns may be specified using a comma or space separated list. 
[code] 
    # Will return 1:
    strmatch("foo*", "foobar")
    # Will return 0:
    strmatch("?bar", "fred")
    # Will return 1:
    strmatch("foo*,bar*", "bar")
    
[/code]

    **See Also:**[strcmp](<#strcmp>) [strcasecmp](<#strcasecmp>) [strcasematch](<#strcasematch>)

## 

strrstr(string1, string2)

This function will return the offset in string1 of the last occurance of string2. If no occurance is found, it returns -1. This expression is identical to rindex() 
[code] 
    strstr("defdefghi", "def") = 3
    strstr("abcdefghi", "xyz") = -1
    
[/code]

## 

strstr(string1, string2)

This function will return the offset in string1 of the first occurance of string2. If no occurance is found, it returns -1. This expression is identical with index() 
[code] 
    strstr("abcdefghi", "def") = 3
    strstr("abcdefghi", "xyz") = -1
    
[/code]

## 

sturb(X, Y, Z, depth)

This function generates spatially coherent noise based on sparse convolution. The depth passed in is the amount of "fractalization" which is done to the noise. 

    **See Also:**[turb](<#turb>) [noise](<#noise>) [snoise](<#snoise>)

## 

substitute(original, find, replace)

Replaces every occurance of find in the original string with replace. See also the Substitute DAT. 
[code] 
    # Would return heLLo feLLow:
    substitute("hello fellow", "ll", "LL")
    
[/code]

## 

substr()

This will extract a sub-string of the first argument. The second argument is the index of the first character to extract (first index is 0). If you give a negative number for the second argument then it refers to the index counting backwards from the end of the string. The third argument is the number of characters to extract. 
[code] 
    # Note:  The first character is specified by a start of 0
    # Would return defg:
    tscript-> echo`substr("abcdefghijklm", 3, 4)`# Would return jk:
    tscript-> echo`substr("abcdefghijklm", -4, 2)`[/code]

## 

surflen(SOP, prim_num, ustart, vstart, ustop, vstop)

Given a surface and two parametric points in its domain ( [ustart,vstart] and [ustop,vstop] ) surflen() computes the length of the 3D curve that stretches between the two points. This curve is the 3D image of the line in the surface domain, whose end-points are [ustart,vstart] and [ustop,vstop]. If either u or v is kept constant, the 3D curve coincides with an isoparm. All four uv numbers are unit values, defined in the [0,1] interval. Note: the primitive must be either a NURBS surface or a Bezier surface. A polygonal mesh can be simulated by a bi-linear Bezier surface (u and v order 2). 
[code] 
    # Will compute the length of the curve on surface #12, defined parametrically by the surface domain points [0,1] and [0.2, 0.8]:
    surflen("/obj/geo1/grid1", 12, 0, 1, 0.2, 0.8)
    
[/code]

    **See Also:**[arclen](<#arclen>) [normal](<#normal>) [curvature](<#curvature>) [unituv](<#unituv>)

## 

tab(path, rowidx, colidx)

Returns a table entry within a DAT. The row and column are specified by index. 
[code] 
    tab("/dats/table1", 2, 3)
    
[/code]

    **See Also:**[tabr](<#tabr>) [tabc](<#tabc>) [tabrc](<#tabrc>) [tabnr](<#tabnr>) [tabnc](<#tabnc>)

## 

tabc(path, rowidx, colpattern)

Returns the first matching table entry within a DAT. The row is specified by index and the column is specified by name. 
[code] 
    tabc("/dats/table1", 2, "product")
    
[/code]

    **See Also:**[tab](<#tab>) [tabr](<#tabr>) [tabmc](<#tabmc>) [tabrc](<#tabrc>) [tabnr](<#tabnr>) [tabnc](<#tabnc>)

## 

tabfind(DAT, pattern, start, type, direction)

This function will search a DAT table, returning the index of the cell that matches the criteria. A start index of -1 represents the first/last cell entry. 
[code] 
    # Find the first row containing A* beginning from row 0:
    tabfind("/table1", "A*", 0, "row", "forward")
    # Find the last column containing A* beginning from column 9:
    tabfind("/table1", "A*", 9, "col", "reverse")
    # Find the last column containing A* searching from the end:
    tabfind("/table1", "A*", -1, "col", "reverse")
    
[/code]

    **See Also:**[tabfindinrow](<#tabfindinrow>) [tabfindincol](<#tabfindincol>)

## 

tabfindincol(DAT, pattern, indexorname, rowstart, searchcol, direction)

This function will search a column in a DAT table, returning the index of the row that matches the pattern. indexorname can be one of rc, Rc, rC, RC. A capital C indicates the column will be specified by name, while a captital R indicates the row will be specified by name. A start index of -1 represents the first/last cell entry. 
[code] 
    # Find the first cell in column 2 containing A* beginning from row 1:
    tabfindincol("/table1", "A*", "rc", 1, 2, "forward")
    # Find the first cell in the column named Weasels containing the word Ferret beginning from the row Comman Name:
    tabfindincol("/table1", "Ferret", "Rc", "Common Name", "Weasels", "forward")
    # Find the last cell in the last column containing Ott* beginning from row Zebra:
    tabfindincol("/table1", "Ott*", "rC", "Zebras", -1, "reverse")
    
[/code]

    **See Also:**[tabfind](<#tabfind>) [tabfindinrow](<#tabfindinrow>)

## 

tabfindinrow(DAT, pattern, indexorname, searchrow, colstart, direction)

This function will search a row in a DAT table, returning the index of the column that matches the pattern. indexorname can be one of rc, Rc, rC, RC. A capital R indicates the row will be specified by name, while a captital C indicates the column will be specified by name. A start index of -1 represents the first/last cell entry. 
[code] 
    # Find the first cell in row 2 containing A* beginning from column 1:
    tabfindinrow("/table1", "A*", "rc", 2, 1, "forward")
    # Find the first cell in the row named Weasels containing the word Ferret beginning from the column Comman Name:
    tabfindinrow("/table1", "Ferret", "Rc", "Weasels", "Common Name", "forward")
    # Find the last cell in the last row containing Ott* beginning from column Zebra:
    tabfindinrow("/table1", "Ott*", "rC", -1, "Zebras", "reverse")
    
[/code]

    **See Also:**[tabfind](<#tabfind>) [tabfindincol](<#tabfindincol>)

## 

tabmc(path, rowidx, colpattern)

Returns multiple table entries within a DAT. The row is specified by index and the column is specified by name. Multiple columns can be specified with a pattern. 
[code] 
    tabmc("/dats/table1", 2, "product")
    tabmc("/dats/table1", 2, "*")
    
[/code]

    **See Also:**[tab](<#tab>) [tabr](<#tabr>) [tabc](<#tabc>) [tabrc](<#tabrc>) [tabnr](<#tabnr>) [tabnc](<#tabnc>)

## 

tabmr(path, rowpattern, colidx)

Returns multiple table entries within a DAT. The row is specified by name and the column is specified by index. Multiple rows can be specified with a pattern. 
[code] 
    tabmr("/dats/table1", "month", 3)
    tabmr("/dats/table1", "*", 3)
    
[/code]

    **See Also:**[tab](<#tab>) [tabc](<#tabc>) [tabr](<#tabr>) [tabrc](<#tabrc>) [tabnr](<#tabnr>) [tabnc](<#tabnc>)

## 

tabnc(path)

Returns the number of columns in a table. 
[code] 
    tabnc("/dats/table1")
    
[/code]

    **See Also:**[tab](<#tab>) [tabr](<#tabr>) [tabc](<#tabc>) [tabrc](<#tabrc>) [tabnr](<#tabnr>)

## 

tabnr(path)

Returns the number of rows in a table. 
[code] 
    tabnr("/dats/table1")
    
[/code]

    **See Also:**[tab](<#tab>) [tabr](<#tabr>) [tabc](<#tabc>) [tabrc](<#tabrc>) [tabnc](<#tabnc>)

## 

tabr(path, rowpattern, colidx)

Returns the first matching table entry within a DAT. The row is specified by name and the column is specified by index. 
[code] 
    tabr("/dats/table1", "month", 3)
    
[/code]

    **See Also:**[tab](<#tab>) [tabc](<#tabc>) [tabmr](<#tabmr>) [tabrc](<#tabrc>) [tabnr](<#tabnr>) [tabnc](<#tabnc>)

## 

tabrc(path, rowname, colname)

Returns a table entry within a DAT. The row and column are specified by name. 
[code] 
    tabrc("/dats/table1", "month", "product")
    
[/code]

    **See Also:**[tab](<#tab>) [tabr](<#tabr>) [tabc](<#tabc>) [tabnr](<#tabnr>) [tabnc](<#tabnc>)

## 

tan(float)

This is a trigonometric mathematical function used to express the tangent value of the number. 
[code] 
    tan (60)=1.73205
    
[/code]

## 

tanh(number)

The hyperbolic tangent of the number. 

## 

text(TOP, attribute)

This function will extract text information from a Text TOP. attribute parameter can be w, width, 0 for width of Text TOP data, h, height, 1 for height of Text TOP data. To get the information without cooking the TOP, getting the last rendered text info (excludes auto sizing, borders and position), use ws, widthstatic, for width and hs, heightstatic for height. Since the static versions do not cook the Text TOP and can be used in the resolution parameters of the same TOP. 
[code] 
    # Returns width of the text string based on the settings of the Text TOP:
    text("/project1/field1/text", "width")
    text("/project1/field1/text", 0)
    # Returns height of the text string based on the settings of the Text TOP:
    text("/project1/field1/text", "height")
    text("/project1/field1/text", 1)
    # Returns width of the text string based on the static font settings (disregards options like auto-sizing, borders, and position) of the Text TOP:
    text("/project1/field1/text", "ws")
    # Returns height of the text string based on the static font settings (disregards options like auto-sizing, borders, and position) of the Text TOP:
    text("/project1/field1/text", "hs")
    
[/code]

## 

textstr(TOP, string, attribute)

This function will extract information from a Text TOP and calculate the width or height of a given string based on the settings. Text wrapping and auto sizing is ignored. The attribute parameter can be w, width, 0 for width, h, height, 1 for height, or ws, widthstatic, and hs, heightstatic for calculation without the borders. The static version of this function does not cook the Text TOP and can be used in the resolution parameters of the same TOP. 
[code] 
    # Returns width of the text string based on the settings of the Text TOP:
    textstr("/project1/field1/text", "derivative", "width")
    textstr("/project1/field1/text", "derivative", 0")
    # Returns height of the text string based on the settings of the Text TOP:
    textstr("/project1/field1/text", "derivative", "height")
    textstr("/project1/field1/text", "derivative", 1")
    # Returns width of the text string based on the font settings of the Text TOP:
    textstr("/project1/field1/text", "derivative", "ws")
    # Returns height of the text string based on the font settings of the Text TOP:
    textstr("/project1/field1/text", "derivative", "hs")
    
[/code]

    **See Also:**[text](<#text>)

## 

timecodetoframe(timecode, float)

Given a timecode and a frames per second value, this expression will return a frame. 

The timecode should be in the format: hh:mm:ss.ff where: 
* hh represents hours
  * mm represents minutes
  * ss represents seconds
  * ff represents frames in the range 1 to fps.


The hour and minute and frame portions of the timecode string are optional. 
[code] 
    # Returns 12345:
    timecodetoframe("00:06:51.15", 30)
    # Returns 12345:
    timecodetoframe("06:51.15", 30)
    
[/code]

    **See Also:**[frametotimecode](<#frametotimecode>)

## 

timepath(path)

This function will return the path to component defining time for the specified path. 
[code] 
    timepath("/project1")
    
[/code]

## 

todouble(number)

converts a 32-bit floating point number to 64-bit double precision. 

    **See Also:**[tofloat](<#tofloat>)

## 

floor(number)

Helps with precision problems when dealing with CHOP sample values, etc. Example: You set a Constant CHOP to .1 (a number that doesn't have an exact binary digital representation, not matter how many bits). CHOPs are stored as 32-bit, expressions compute at 64-bit. chop() converts from 32-bit to 64-bit which gives .10000000149012. tofloat(chop()) gives .1, which gives intelligent rounding. 
[code] 
    tofloat(.1000000014) = .1
    
[/code]

    **See Also:**[todouble](<#todouble>) [chop](<#chop>) [format](<#format>) [int](<#int>) [round](<#round>) [trunc](<#trunc>)

## 

tolower(s)

Converts all the characters in the string to lower case 

    **See Also:**[toupper](<#toupper>)

## 

toupper(s)

Converts all the characters in the string to upper case 

    **See Also:**[tolower](<#tolower>)

## 

translate(tx, ty, tz)

Computes a translation matrix given the three translate values. 

    **See Also:**[rotate](<#rotate>) [rotaxis](<#rotaxis>) [scale](<#scale>)

## 

transpose(mat)

Computes the transpose of the matrix specified. 

## 

trim(string)

Return the string with all leading and trailing space removed. 
[code] 
    trim(" abc   ")  = "abc"
    
[/code]

## 

trunc(number)

The integer value of the number by truncating the number. The number is rounded toward 0. That is, for positive numbers, the largest integer less than the number will be returned. For negative numbers, the smallest integer greater than the number will be returned. 
[code] 
    trunc(2.6)=2
    trunc(-2.6)=-2
    
[/code]

    **See Also:**[format](<#format>) [int](<#int>) [float](<#float>) [floor](<#floor>) [ceil](<#ceil>) [round](<#round>)

## 

turb(X, Y, Z, depth)

This function generates spatially coherent noise (i.e. random numbers which are close to each other when the X, Y, Z points are close to each other). The depth passed in is the amount of "fractalization" which is done to the noise. 

    **See Also:**[sturb](<#sturb>) [noise](<#noise>) [snoise](<#snoise>)

## 

unituv(SOP, prim_num, uv_real, D_U, D_V)

Returns the unit u or v parametric value, given the real_value of the same parameter. The unit value is defined in the [0,1] interval. The real_value is defined in the valid interval of the primitive's domain if the primitive is a spline type. If the primitive is a polygon or a mesh, the size of its domain is given by the number of vertices, or rows or columns respectively. If the primitive is a polygon or a curve, D_U and D_V are irrelevant. Note: the result is undefined if the primitive is neither a face nor a hull. 

    **See Also:**[realuv](<#realuv>)

## 

uvdist(SOP, prim1_num, u1, v1, SOP, prim2_num, u2, v2)

This expression finds the distance between two primitives at two parametric locations. Valid u and v values are between 0 and 1. Any primitive type is allowed. 
[code] 
    # Will return the distance between point (0.1, 0.8) on the first primitive in sphere1 and point (1, 0.5) on the third primitive in grid1:
    uvdist("/obj/geo1/sphere1", 0, 0.1, 0.8, "/obj/geo1/grid1", 2, 1, 0.5)
    
[/code]

    **See Also:**[distance](<#distance>) [primdist](<#primdist>) [pointdist](<#pointdist>) [unituv](<#unituv>)

## 

v(row_index, column_index)

Only usable inside DATs. This expression will look at the DAT's input 0 for the source table, then return the cell data of the specified row index and column index. 
[code] 
    v(2, 10)
    
[/code]

    **See Also:**[vr](<#vr>) [vc](<#vc>) [vrc](<#vrc>) [vs](<#vs>) [vsr](<#vsr>) [vsc](<#vsc>) [vsrc](<#vsrc>)

## 

vangle(v0, v1)

Returns the angle between the two vectors specified. 

## 

var(path, variable_name)

Returns the value of the variable from the context of the given path. If the path is a COMP, then Component variables within that COMP will be searched for a match, as well a the COMPs Path Variable. The variable may be any type of variable that is visible to the node, not just a locally defined component variable. 
[code] 
    # Evaluates $F as seen by /project1 though $F itself may be defined above it.
    var("/project1", "F")
    # Evaluates $TOUCHBUILD as seen by the root component.
    var("/", "TOUCHBUILD")
    
[/code]

## 

varexists(varname)

Returns 1 if the variable exists relative to the current evaluation location, 0 if not. Do not prefix the variable name with $ in this expression. 
[code] 
    # Returns 1:
    varexists("TOUCHBUILD")
    
[/code]

    **See Also:**[vartype](<#vartype>) [varpath](<#varpath>)

## 

varpath(varname)

Returns the path to the COMP where the variable is defined. Only returns a path for Root, Component and Path Variables. For undefined variables it will return undefined. For variable types that don't have a path, returns nopath. 
[code] 
    # Returns /:
    varpath("TOUCHBUILD")
    # Returns /project1:
    varpath("project")
    
[/code]

    **See Also:**[varexists](<#varexists>) [vartype](<#vartype>)

## 

vartype(varname)

Returns a string which indicates the type of variable varname is. The type of variable is determined by where the variable is defined. Possible returned values are: 
* undefined Variable is not defined
  * script Script Variable
  * operator Operator Variable (includes Operator Specific Variables)
  * path Path Variable
  * component Component Variable
  * root Root Variable
  * builtin Built-In Variable
  * system System Variable


For a more detailed description of each of these variable types, refer to the [Variables](<./Variables.md> "Variables") article. Do not prefix the variable name with $ in this expression. 
[code] 
    # Returns root:
    vartype("TOUCHBUILD")
    # Returns builtin:
    vartype("CUR_TOUCHBUILD")
    # Returns operator:
    vartype("OD")
    
[/code]

    **See Also:**[varexists](<#varexists>) [varpath](<#varpath>)

## 

vc(row_index, column_name)

Only usable inside DATs. This expression will look at the DAT's input 0 for the source table, then return the cell data of the specified row index and column name. 
[code] 
    vc(2, "carnivore")
    
[/code]

    **See Also:**[v](<#v>) [vr](<#vr>) [vrc](<#vrc>) [vs](<#vs>) [vsr](<#vsr>) [vsc](<#vsc>) [vsrc](<#vsrc>)

## 

vector(pattern)

The pattern passed in will be converted to a vector. The pattern should consist of a leading square bracket followed by a comma separated list of values and a closing square bracket. 
[code] 
    vector("[1,2,3,4,5]")
    
[/code]

## 

vector3(x, y, z)

Creates a 3 vector with the x, y, and z components specified. 

## 

vector4(x, y, z, w)

Creates a 4 vector with the x, y, z, and w components specified. 

## 

vertex(SOP, primitive_number, vertex_number, attribute, index)

This function will extract information from a vertex of a primitive in a sop. The attribute parameter is the name of the attribute (eg. Cd for diffuse color). Two special attributes exist P and Pw which represent the position of the point in space (Pw allows you to access the W component of the position, index is ignored in this case). P with an index of 3 is the same as Pw. 
[code] 
    # Will return the X component of vertex 3 of primitive2 in the facet1 SOP of geo1:
    vertex("/obj/geo1/facet1", 2, 3, "P", 0)
    # Will return the Z component of the color attribute of vertex 3 of primitive 2 in the facet1 SOP of object geo1.
    point("/obj/geo1/facet1", 2, 3, "Cd", 2)
    Note: This function will interpolate between point values if the vertex number is fractional, such as 3.35
    
[/code]

## 

vertexs(SOP, primitive_number, vertex_number, attribute)

This function will return the value of a string attribute for a given vertex (of a given primitive) in a SOP. 
[code] 
    # Will return the string associated with the string attribute instance for vertex 3 of primitive 0 in the facet1 SOP in geo1:
    vertexs("/obj/geo1/facet1", 1, 3, "instance")
    
[/code]

## 

vlength(vec)

Computes the length of the vector specified. This is equivalent to: sqrt(dot(vec, vec)) 

## 

vlength2(vec)

Compute the square of the length of the vector specified. This is equivalent to: dot(vec, vec) 

## 

vorigin(obj1, obj2)

This function will return a vector with 6 values in it. The values are set to [TX, TY, TZ, RX, RY, RZ] for the position of obj1 relative to obj2. If obj1 is the emptry string (""), then the world space position of obj2 is returned. 

    **See Also:**[objdist](<#objdist>) [origin](<#origin>) [vtorigin](<#vtorigin>) [vrorigin](<#vrorigin>) [originoffset](<#originoffset>)

## 

vr(row_name, column_index)

Only usable inside DATs. This expression will look at the DAT's input 0 for the source table, then return the cell data of the specified row name and column index. 
[code] 
    vr("furo", 10)
    
[/code]

    **See Also:**[v](<#v>) [vc](<#vc>) [vrc](<#vrc>) [vs](<#vs>) [vsr](<#vsr>) [vsc](<#vsc>) [vsrc](<#vsrc>)

## 

vrc(row_name, column_name)

Only usable inside DATs. This expression will look at the DAT's input 0 for the source table, then return the cell data of the specified row name and column name. 
[code] 
    vrc("latin", "carnivore")
    
[/code]

    **See Also:**[v](<#v>) [vr](<#vr>) [vc](<#vc>) [vs](<#vs>) [vsr](<#vsr>) [vsc](<#vsc>) [vsrc](<#vsrc>)

## 

vrorigin(obj1, obj2)

This function will return a vector containing the rotates required to transform obj1 to the space of obj2. If obj1 is the emptry string "", then the world space position of obj2 is returned. 

    **See Also:**[objdist](<#objdist>) [origin](<#origin>) [vorigin](<#vorigin>) [vtorigin](<#vtorigin>) [originoffset](<#originoffset>)

## 

vs(row_index, column_index)

Only usable inside DATs. This expression will look at the DAT's input 0 for the source table, then return the cell data of the specified row name and column name. 
[code] 
    vs(2, 10)
    
[/code]

    **See Also:**[v](<#v>) [vr](<#vr>) [vc](<#vc>) [vrc](<#vrc>) [vsr](<#vsr>) [vsc](<#vsc>) [vsrc](<#vsrc>)

## 

vsc(row_index, column_name)

Only usable inside DATs. This expression will look at the DAT's input 0 for the source table, then return the cell data of the specified row index and column name. 
[code] 
    vsc(2, "carnivore")
    
[/code]

    **See Also:**[v](<#v>) [vr](<#vr>) [vc](<#vc>) [vrc](<#vrc>) [vs](<#vs>) [vsr](<#vsr>) [vsrc](<#vsrc>)

## 

vscale(vec, scale)

Multiplies the vector by the scale. This is equivalent to vec*scale 

## 

vset(size, value)

Creates a vector of the size specified. Each component of the vector will be set to the value given. 

## 

vsize(vec)

Returns the number of elements in the vector 

## 

vsr(row_name, column_index)

Only usable inside DATs. This expression will look at the DAT's input 0 for the source table, then return the cell data of the specified row name and column index. 
[code] 
    vsr("furo", 10)
    
[/code]

    **See Also:**[v](<#v>) [vr](<#vr>) [vc](<#vc>) [vrc](<#vrc>) [vs](<#vs>) [vsc](<#vsc>) [vsrc](<#vsrc>)

## 

vsrc(row_name, column_name)

Only usable inside DATs. This expression will look at the DAT's input 0 for the source table, then return the cell data of the specified row name and column name. 
[code] 
    vsrc("latin", "carnivore")
    
[/code]

    **See Also:**[v](<#v>) [vr](<#vr>) [vc](<#vc>) [vrc](<#vrc>) [vs](<#vs>) [vsr](<#vsr>) [vsc](<#vsc>)

## 

vtorigin(obj1, obj2)

This function will return a vector containing the translates required to transform obj1 to the space of obj2. If obj1 is the emptry string "", then the world space position of obj2 is returned. 

    **See Also:**[objdist](<#objdist>) [origin](<#origin>) [vorigin](<#vorigin>) [vrorigin](<#vrorigin>) [originoffset](<#originoffset>)

## 

wrap()

Similar to the clamp expression in that the resulting value will always fall between the specified minimum and maximum value. It will, however, create a sawtooth wave for continuously increasing or decreasing values of the value. 
[code] 
    # This will create a sawtooth function between 5 and 10.
    wrap($F, 5, 10)
    
[/code]
