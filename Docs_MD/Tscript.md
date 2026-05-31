# Tscript
* [Tscript Commands](<./Tscript_Commands.md> "Tscript Commands")
  * [Tscript Expressions](<./Tscript_Expressions.md> "Tscript Expressions")
  * [Python vs Tscript Equivalents](<./Python_vs_Tscript_Equivalents.md> "Python vs Tscript Equivalents")

## TouchDesigner Scripting Language

**Tscript** is TouchDesigner's original built in scripting language, now alongside the [Python](<./Python.md> "Python") language. A side-by-side list of common tasks in both languages can be found [here](<./Python_vs_Tscript_Equivalents.md> "Python vs Tscript Equivalents"). 

Tscript is similar to C-Shell in its syntax and structure. TouchDesigner's [Expression](<./Expression.md> "Expression") language is also used heavily in Tscript. As a result, when learning Tscript, don't focus solely on Tscript itself, but look at [Expressions](<./Expression.md> "Expression") too. 

[Tscript Commands](<./Tscript_Commands.md> "Tscript Commands") and [Tscript Expressionsis](<./Tscript_Expressions.md> "Tscript Expressions") a complete reference of Tscript. 

## The Order of Expansion

Expansion of a TouchDesigner command follows the C-shell expansion standards very closely. There are some subtle differences. 

### Lexical Structure

TouchDesigner splits input lines into words at space characters, except as noted below. The characters`; < > ( ) =`form separate words and TouchDesigner will insert spaces around these characters except as noted below. By preceding a special character by a backslash (`\`), its special meaning can be suppressed. 

#### Evaluation of Quotes

Strings enclosed in a matched pair of quotes forms a partial word. Within double quotes (`"`), expansion will occur. Within single quotes (`'`) expansion will not be done. Within back-quotes (```) the enclosed string will be evaluated as a TouchDesigner expression and the result will be considered to be a partial word. Inside a matched pair of quotes, the quote character may be protected by preceding the slash with a backslash. 

Backquotes are evaluated with a higher priority than double quotes. This means that if a double-quoted argument encloses a back-quoted string, the back-quoted string may contain double quotes without terminating the initial double quote delimiter. For example, the string: 
[code] 
    foo'ch("/obj/geo1/tx")'
    
[/code]

will be parsed as a single argument. 

**Note:** As a general rule, do not include spaces between your "back" quotation marks and what lies between them. TouchDesigner may not evaluate them if there are extra spaces. 

#### Comments

The character`#`introduces a comment which continues to the end of the line. This character can be protected by a backslash (`\`) or by enclosing the character in quotes. 

#### Multiple Commands

Multiple commands can be specified on the same line by separating them with semicolons (`;`). 

### Expansion

Expansion is done in the following order: History substitution, [Macro](<./Macro.md> "Macro") expansion, [Variable](<./Variables.md> "Variables") & [Expression](<./Expression.md> "Expression") expansion. 

History substitution is not as sophisticated as the csh history mechanism. The supported substitutions are: 

  *`!!`\- Repeat last command
  *`!str`\- Repeat last command matching str
  *`!num`\- Repeat command "`num`" from the history list
  *`!-5`\- Repeat the command run five commands previous


With the`!!`substitution, characters following the`!!`are appended to the command. The resulting command is displayed in the Textport before the command is run. 

Variable and expression evaluation are done at the same time and have equal precedence. Variables are delimited by a dollar sign (`$`) followed by the variable name. A variable name must begin with letter or an underscore (`_`) followed by any number of letters, numbers or underscores. As well, the variable name may be delimited by curly braces (`{}`) in which case the contents of the curly braces is expanded before the variable name is resolved. This allows for pseudo array operations on variables. 

For example: 
[code] 
    touch -> set foo1 = bob 
    touch -> set foo2 = sue 
    touch -> for i = 1 to 2 
    > echo ${foo${i}} 
    > end 
    bob 
    sue 
    
[/code]

Expression evaluation is done on the string contained within matching backquotes (```). Inside the backquotes, expression expansion is performed as opposed to command line expansion. The expression is evaluated, and the resulting string is used to replace the expression on the command line. If the expression evaluates to a type other than a string, the result is cast to a string and this is the value used. 

### Command Expressions

These differ from general TouchDesigner expressions, though TouchDesigner expressions can be used inside of command expressions. The command expressions are used in the "`while`" and "`if`" commands. The order of operations in a command expression is as follows: 

  *`()`\- Parentheses
  *`== != < > <= >=`\- Equal, Not Equal, Less Than, Greater Than, Less Than or Equal, Greater Than or Equal
  *`&& ||`\- Logical AND and Logical OR


Expressions can be enclosed in parentheses for clarity, but this is not necessary. 

## Variables

There are many types of [Variables](<./Variables.md> "Variables") in TouchDesigner. Script variables are variables that are set within a script using the`set`command. They are local to the script and exist only for the duration of the script. When the script terminates, these variables will automatically be unset. 

All variables created by loops are considered local script variables (i.e. the "`for`" loop will use script variables). 

## Pattern Matching

**Note** : _With TouchDesigner 2025 we are transitioning to a new pattern matching that is consistent throughout the product. Some uses of it are obsolete but we have legacy modes that allow older patterns and files to continue to work as-is. With POPs being a new operator family, only the new pattern matching works. See Legacy Features below. Please report any difficulties you may be having._

Some parameters in TouchDesigner are used to specify multiple operators, multiple channels, multiple points, etc. For example, the [Render TOP](<./Render_TOP.md> "Render TOP") allows for multiple lights, geometry COMPs and cameras. The [Join CHOP](<./Join_CHOP.md> "Join CHOP") and [Composite TOP](<./Composite_TOP.md> "Composite TOP") accept multiple CHOPs and TOPs respectively. 

A parameter that is a "pattern" allows you to specify several names and/or specify "wild cards" which will match all or parts of the names of operators, channels, point indexes etc. Patterns are also used in some Python methods such as`ops()`which allows you to specify more than one OP using a single string. 

## Basic Patterns

Basic Pattern matching is also often used to match channel names. It uses the following kinds of patterns to select existing channels in an input CHOP, used in CHOPs like the [Select CHOP](<./Select_CHOP.md> "Select CHOP") and the [Math CHOP](<./Math_CHOP.md> "Math CHOP")'s Scope parameter, where you only want to affect certain channels and leave the rest as-is. 

  *`_pattern_`\- Match string exactly
  *`*`\- A "wild card" that matches any sequence of characters
  *`?`\- A "wild card" that matches any single character
  *`^`\- Do not match
  *`[_alphaset_]`\- Match any one of alphabetic characters enclosed in the square brackets. In TouchDesigner, the`[a-g]`format is not currently supported, the characters must be listed as`[abcdefg]`*`[_int1_ -_int2_]`or`[_int1_ -_int2_ :_increment_]`\- Match any integer numbers enclosed in the number range, with the optional increment
  *`[_int1,int2,int3_]`\- Match the specific integers given
  *`"pattern"`\- Match pattern ignoring whitespace as separators


**Note:** There should be no spaces within the ranges, i.e. do`[1,3,0-10:2]`not`[1, 3, 0-10:2]`### Examples`chan2`| Matches a single channel name   
---|---`chan3 tx ty tz`| Matches four channel names, each name is separated by spaces`chan*`| Matches each channel that starts with "`chan`" and ends with anything`*foot*`| Matches each channel that has "`foot`" in it, with anything or nothing before or after`t?`| The`?`matches a single character.`t?`matches two-character channels starting with`t`, like the translate channels`tx`,`ty`and`tz``r[xyz]`| Matches channels`rx`,`ry`and`rz`. that is, "`r`" followed by any character between the [ ]`blend[3-5]`| Matches number range giving`blend3`,`blend4`, and`blend5`.`blend[3-7:2]`| Matches number ranges giving`blend3`,`blend5`, and`blend7`. (3 to 7 in steps of 2)`blend[2-3,5,13]`| Matches channels`blend2`,`blend3`,`blend5`,`blend13``t[uvwxyz]`| [`uvwxyz`] matches characters between`u`and`z`, giving channels`tu`,`tv`,`tw`,`tx`,`ty`and`tz``"Instance 3"`| Matches the string "Instance 3" exactly, NOT matching Instance and 3.`"run -exec test[0-5]"`| Matches the string "run -exec test0" to "run -exec test5" exactly. Useful for matching Page names in [Parameter DAT](<./Parameter_DAT.md> "Parameter DAT") or entries in a [Table DAT](<./Table_DAT.md> "Table DAT")  
  
Some node parameters also support expanding component group names before matching. 

  *`@groupname`\- Expands all the items in the group. Since each group belongs to a network, you can specify a path before the @groupname identifier.

### Examples`container1/@lights1`| Matches members of the`lights1`group defined inside`container1`.   
---|---  
  
## Operator Patterns

Some parameters accept Node paths such as [Render TOPs](<./Render_TOP.md> "Render TOP") Geometry or Lights parameter. Pattern matching in this case can make selecting multiple nodes fast and easy. 

  *`_pattern_`\- Searches the current network and matches any node with the Basic Pattern`_pattern_`.
  *`/_subpattern1_ /_subpattern2_ /_subpattern3_ /_pattern_`\- Searches each sub-path according to it's sub-pattern and matches any nodes with the Basic Pattern`_pattern_`###  Examples`geo*`| Matches all nodes whose names start with "`geo`" in the current network   
---|---`/project1/geo*`| Matches all nodes in`/project1`whose names start with "`geo`"`/project[1-3]/geo*`| Matches all nodes in`/project1`,`/project2`, and`/project3`whose names start with "`geo`"   
  
## Index Patterns

Some parameters only match over indices, usually CHOPs and POPs (see below for SOPs), which is why there is a slightly modified syntax. There is always an implied range of points that the pattern will be matching on, either the number of channels, points, etc. 

  *`_number_`\- Matches any index with the number exactly
  *`*`\- Match all numbers
  *`^`\- Do not match
  *`[_int1_ -_int2_]`or`[_int1_ -_int2_ :_increment_]`\- Match any integer numbers enclosed in the number range, with the optional increment
  *`[_int1_ -_int2_ :_take_ :_increment_]`\- Match the first _take_ numbers every _increment_ enclosed in the number range. See example below.
  *`[*:_increment_]`or`[*:_take_ :_increment_]`\- Same as above except the range is all numbers taken from 0 to the maximum.
  *`[_int1,int2,int3_]`\- Match the specific integers given

### Examples`^20`| All indices except 20 are included   
---|---`[3-15]`| All indices from 3 to 15 are included`^[100-200]`| Every index <100 and >200 is included`[0-15:2]`| Every second point from 0 to 15 is included`[0-15:2:5]`| Take the first 2 numbers, every increment of 5, from 0 to 15, this selects 0,1,5,6,10,11,15`[*:3]`| From 0 to the maximum index, every multiple of three is included. For example with 10 points, this selects 0,3,6,9   
  
### Ordered Index Patterns

Some nodes such as the [Primitive POP](<./Primitive_POP.md> "Primitive POP") allow orderings within index selection with the following rules 

  *`*`acts as a range from`0-max`* Entries in ranges are selected in order in which they appear in the range
  * Entries in negated ranges are selected from`0-max`minus the indices specified by the range`[9-0]`| This selects 9,8,7,6,5,4,3,2,1,0 in that order   
---|---`[9-0:2]`| This selects 9,7,5,3,1 in that order`[0-10:4,3,7]`| This selects 0,4,8,3,7 in that order`[15-0:2:5]`| This selects 15,14,10,9,5,4,0 in that order`^[*:3]`| With a maximum value of 10, this selects 1,2,4,5,7,8,10 in that order   
  
**Note:** Ordered Index Patterns do not support set operator notation 

## Set Operator Notation

Some pattern matching rules (see [Pattern Matching Support](<./Pattern_Matching_Support.md> "Pattern Matching Support")) can be used in conjunction with set operator notation for more expressive selection. Basic, Operator and Index Patterns (i.e.`/project/geo1`,`t?`,`chan*`,`blend[2-6:2]`) create sets and`|`,`&`,`~`can apply the following set operations between them. The pattern will match any element in the final resulting set. 

  *`|`represents the **Union** of two sets
  *`&`represents the **Intersection** of two sets
  *`~`represents the **Set Difference** of two sets
  *`( )`groups set operations and treats the result as one set


The order of precedence of these operations goes`()`, and then the set operations from left to right in the pattern. **NOTE:** The`|`,`&`,`~`operators have equal precedence. This means for example 

  *`A | B & C`**IS** equal to`B & C | A`### Examples`* ~ chan[1,5,6]`| Matches everything except`chan1`,`chan5`, and`chan6`---|---`(* ~ geo*) | geo3`| Matches everything except things that starts with "`geo`" and ends with anything unless its`geo3``./mygeos/geo* ~ ./mygeos/geo[3-5]`| Matches every node in`./mygeos`that starts with "`geo`" and ends with anything except`geo3`,`geo4`, and`geo5``blend* ~ blend[0-9]*`| Matches everything that starts with`blend`except anything with a digit after`blend`, for example it would not match`blend0_light`,`blend2_dark`but would match`blend_light`and`blend_dark`.   
  
## Legacy Features
* **Prefer using`|`set operator notation instead**
    * Example: use`tx | nx`instead of`tx nx`* Previously for most nodes space and comma separated patterns implied patterns will be ORed together. This logic is still true for pattern not containing the new set operations for backwards compatibility. The set operator makes it more explicit
  * **Prefer using the updated index pattern syntax that is consistent with basic pattern matching**
    * Example: use`[100-120:2] ~ [0-9]`instead of`100-120:2 !0-9`* Old index matching notation for CHOPs will be a legacy toggle that is now off by default for newly placed nodes. When on the new set operator notation will not be available. It is recommended to instead use the new syntax that is more consistent with existing pattern matching
  * **Prefer using`/path/to/node`instead of`op:/path/to/node`**
    * Example: use`/project1/geo`instead of`op:/project1/geo`* Mainstay of old path names

### Old Index Notation

SOPs still use the old style of index notation, and does not support the new set operator syntax. For Examples and rough documentation: see parameter documentation for [Group SOP](<./Group_SOP.md> "Group SOP") or [Add SOP](<./Add_SOP.md> "Add SOP")

## See Also
* [Pattern Expansion](<./Pattern_Expansion.md> "Pattern Expansion"), [Pattern Replacement](<./Pattern_Replacement.md> "Pattern Replacement"), [Pattern Matching Support](<./Pattern_Matching_Support.md> "Pattern Matching Support")

## Command Loops

There are three different looping constructs in Tscript: 

**for**
[code] 
    for _variable_ = _start_ to _end_ [step _increment_] 
    ... 
    end 
    
[/code]

**foreach**
[code] 
    foreach _variable_ ( _element_list_ ) 
    ... 
    end 
    
[/code]

**while**
[code] 
    while ( _expression_ ) 
    ... 
    end 
    
[/code]

The`for`loop will loop from the`start`, up to and including the`end`. 

The`foreach`loop will cycle through every element in the`element_list`assigning the variable value to be a different element each iteration through the loop. 

All variables in the`for`and`foreach`loops are local variables. To export the variable to other scripts simply set a global variable using the`rvar`or the`cvar`Command inside the loop. 

**Example**

You can use a loop to perform repetitive tasks for you. For example, if you wanted to wanted to merge 255 SOPs, it would be faster to write a short script than to do all that wiring manually. 

For example, if you named your SOPs consistently, like:`model_0`,`model_1`,`model_2`...`model_255`, then you could execute the following script in a Textport: 
[code] 
    for i = 0 to 255 
    opwire model_$i -$i merge1 
    end 
    
[/code]

If you haven't been consistent with naming, you could also do it with a`foreach`. 

## Terminating a Long or Endless Script

**If TouchDesigner looks like it is hanging, you may have scripted an endless loop by mistake and may want to kill the script.** In this case, you can hit Ctrl-Break to interrupt, halt and terminate script execution. It may take a few seconds for TouchDesigner to respond, break from the script and stop processing. You can view messages on which scripts were stopped in the [Textport](<./Textport.md> "Textport"). 

## Conditional Statements

The "`if`" command provides the ability for a script to check a condition and then execute one set of commands if the condition is true or an alternate set of commands if the condition is false. It should have an`endif`to signify the end. 
[code] 
    if ( expr ) [then] 
    ... 
    else if (expr2) [then] 
    ... 
    else 
    ... 
    endif
    
[/code]

## Arithmetic Expressions

**Arithmetic Operations**
[code] 
    ^ - not
    + - add
    - - subtract
    * - multiply
    / - divide
    % - mod
    
[/code]

  
**Logical Operations**
[code] 
    == - equal to
    != - not equal to
    <  - less than
    <= - less than or equal to
    >  - greater than
    >= - greater than or equal to
    
[/code]
[code] 
    && = AND
    || = OR
    !  = NOT
    
[/code]

## Macros and Multiple Commands

Some frequently used commands can be represented with a single word, a [Macro](<./Macro.md> "Macro"). 

**Example**
[code] 
    touch-> macro greet echo hello world 
    touch-> greet 
    hello world 
    touch-> macro mine "opset -d off * ; opset -d on geo1" 
    touch-> mine 
    
[/code]

This will execute the string attached to the macro "`mine`" and turn off the display of all the objects then turn on object`geo1`. 

The next two commands list, then undefine, a macro: 
[code] 
    touch-> macro 
    greet hello world 
    mine opset -d off * ; opset -d on geo1 
    touch-> macro -u greet 
    
    
[/code]

TouchDesigner accepts several commands on the same command line separated by a semicolon (`;`). This does not apply to semicolons embedded in quotes. Macros can contain commands embedded in quotes. 

## Redirecting Command Output to DATs

Redirect to a DAT (clearing the DAT first) with the`echo`Command: 
[code] 
    echo "abc" > text1
    
[/code]

appending a line to the DAT: 
[code] 
    echo "abc" >> text1
    
[/code]

If the DAT does not exist, TouchDesigner will create a Text DAT and place the new text in it. 

It doesn't matter if there is a space after the`>`or`>>`. 

You can append to a pre-existing table, which adds a new row to the table. 

There are two syntax forms to put things in different columns. First by putting`\t`in your text string: 
[code] 
    echo abc\tdef\tghi >> table1
    
[/code]

and with quotes around it you need to put actual tab characters in the string: 
[code] 
    echo "abc   def  ghi" >> table1
    
[/code]

where the spaces above are actual tab characters (not`\t`). 

## Redirecting Command Output to Files

To redirect the output to a file in the filesystem, use`FILE:`as a destination prefix. Examples: 
[code] 
    echo "hello world" > FILE:abc.txt          # relative to current disk folder on current drive
    echo "hello world" > FILE:Map/README.txt   # relative path, into subfolder Map
    echo "hello world" > FILE:C:/abc.txt       # absolute path
    echo "hello world" > FILE:$TOUCH/test.txt  # new file using Built-in [Variable](<./Variables.md> "Variables") for the path to your project.
    echo "hello world" >> FILE:$TOUCH/test.txt # this appends text
    
[/code]

Note the quotes are optional in the above examples. Also note`>>`can be used to append to existing text, instead of replacing it. If no prefix is given, a DAT node path is assumed. This can also be specified with the`DAT:`prefix, though this is redundant. 

## Using Arguments in Scripts

When calling a script with Tscript`run`or`include`Command, arguments can be passed to the script. These arguments are set to TouchDesigner script variables so that they can be used by the script. 

**Example** Assuming the current TouchDesigner component contains`repeatscript`(see Tscript`pc`and`cc`Command): 
[code] 
    touch-> run repeatscript 1 10 2 blockhead
    
[/code]

where`_repeatscript_`contains: 
[code] 
    echo Hello, my name is $arg4 
    for i = $arg1 to $arg2 step $arg3 
    echo I said, my name is $arg4 
    end 
    
[/code]

Note that there are four variables in the script:`arg1`,`arg2`,`arg3`and`arg4`. These are set to the arguments`1`,`10`,`2`and`blockhead`respectively. 

  *`$arg0`\- name of the script


You can get the name of the script being run from`$arg0`. 

For example: run myscript 1 4.5 7 balloon will come into the script with 

  *`$argc`=`5`*`$arg0`=`myscript`*`$arg1`=`1`*`$arg2`=`4.5`*`$arg3`=`7`*`$arg4`=`balloon`This allows usages such as: 
[code] 
    if $argc != 5 then 
    echo USAGE: cmdread $arg0 numclowns clownsize numtoys toytype 
    exit 
    endif 
    
[/code]

  *`$argc`\- number of arguments passed to script


The number of arguments passed to the script can be retrieved with the variable`$argc`. 

For example, from the lookat script: 
[code] 
    # USAGE: lookat eyeobject focusobject 
    if $argc!= 2 then 
    echo USAGE: source lookat eyeobject focusobject 
    exit 
    endif
    
[/code]

## Examples

**Question:** How would I get all the container level parameters of the master component and reapply them to a [clone](<./Clone.md> "Clone")? 
[code] 
     set master = $arg1 
     set clone = $arg2
     opparm $clone`run("parmls /$master")`[/code]

The problem is that you will loose spaces, so any`par("tx")`will end up as`par(tx)`, which produces an error. The following script seems to work better, but hasn't been tested very much. 
[code] 
     set master = $arg1 
     set clone = $arg2
     foreach p (`noevals(run("parmls $master"))`)
        if (`arg("$p",1)`!="")
           opparm $clone $p
        else
           opparm $op`arg("$p",0)`""
        endif
        print ""
      end
    
[/code]
* * *
* * *
