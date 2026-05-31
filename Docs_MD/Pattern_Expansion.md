# Pattern Expansion

  
Pattern Expansion takes a short string and expands it to generate a longer string of individual elements. Example:`chan[1-3]`generates`chan1 chan2 chan3`.   
  
[Pattern Replacement](<./Pattern_Replacement.md> "Pattern Replacement") uses Pattern Expansion, along with having some of it's own syntax on-top of Pattern Expansion. Pattern Expansion is different from "[Pattern Matching](<./Pattern_Matching.md> "Pattern Matching")", in Pattern Expansion you are creating a list of strings, while in Pattern Matching you are looking for a pattern in a string or a set of strings. 

Expansion is done by using putting the data to expand into`[]`. Valid syntax is 

  *`[_alphaset_]`\- Where _alphaset_ is one or more letters (not numbers), each of which will be split out into it's own result. The [a-g] format is not currently supported, the characters must be listed as [abcdefg]
  *`[_int1_ -_int2_]`\- Where _int1_ and _int2_ form a range of numbers. A result will be created for each number in the range.
  *`[_int1_ -_int2_ :_increment_]`\- Similar to the previous one, but _increment_ allows for skipping numbers in the range.
  *`[_int1,int2,int3_]`\- Match the specific integers given


**Note** Each expansion will be expanded against every possible other expansion in the string. So one expansion with 2 results followed by one with 3 results, will result in a final result containing 6 results. The order the numbers and ranges appear in`[]`is the order they are generated. See examples below. 

### Examples`[tr][xyz]`| Starts expansion from right to left. Expands to`tx ty tz rx ry rz`---|---`chan[1-11:2]`| Starts expansion at chan1 to chan11 in increments of 2. Expands to`chan1 chan3 chan5 chan7 chan9 chan11``chan[1-3] pos[xyz]`| Starts expanding first term, and then the second. Expands to`chan1 chan2 chan3 posx posy posz`Pattern expansion occurs in: 
* [Rename CHOP](<./Rename_CHOP.md> "Rename CHOP"), [Select CHOP](<./Select_CHOP.md> "Select CHOP") and [Panel CHOP](<./Panel_CHOP.md> "Panel CHOP") \- where channels are renamed.
  * [Constant CHOP](<./Constant_CHOP.md> "Constant CHOP"), [Noise CHOP](<./Noise_CHOP.md> "Noise CHOP"), [Wave CHOP](<./Wave_CHOP.md> "Wave CHOP"), [LFO CHOP](<./LFO_CHOP.md> "LFO CHOP"), [Pulse CHOP](<./Pulse_CHOP.md> "Pulse CHOP") and [Joystick CHOP](<./Joystick_CHOP.md> "Joystick CHOP") \- where channels are created using patterns.
  * [Merge DAT](<./Merge_DAT.md> "Merge DAT") \- where DATs are selected for merging.


**Note** : See`[tdu.expand](<./TDU_Class.md> "TDU Class")()`**Note** : To expand a list of operators that is in a parameter type that is a list of operators, see`.evalOPs()`in [Par Class](<./Par_Class.md> "Par Class")

See also [Pattern Replacement](<./Pattern_Replacement.md> "Pattern Replacement"), [Pattern Matching](<./Pattern_Matching.md> "Pattern Matching").
