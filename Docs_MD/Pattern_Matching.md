# Pattern Matching

  
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
