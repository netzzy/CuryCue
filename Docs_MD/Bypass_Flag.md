# Bypass Flag

[![](./images/c/ce/BypassOff.jpg)](</File:BypassOff.jpg>)  
  
[](</File:BypassOff.jpg> "Enlarge")

Bypass flag is off

[![](./images/1/1a/BypassOn.jpg)](</File:BypassOn.jpg>)

[](</File:BypassOn.jpg> "Enlarge")

Bypass flag is on

**Bypass** is one of the Operator state [Flags](<./Flag.md> "Flag") present on every [OP](<./Operator.md> "Operator") in a network. When an operator is bypassed, the operator acts as if it is not there - it's a pass-through. Regardless of how many inputs an operator has, the first input is passed through. Another way to think about it - when bypassed, the network will cook the same as if this operator were deleted. 

The bypass flag is useful for testing to see what the network would do with an operator removed without having to do any rewiring. 

Bypass on a component causes all nodes inside it to be bypassed. So it's possible that the output of the component will not be the same as the first input. 

To bypass an operator, click on the arrow shaped flag. Clicking on it again removes the bypass. OPs that have been bypassed are easily identifiable by the large red arrow that is superimposed on the operator's viewer. 

**Tip** : TOPs have a Passes parameter that has the same effect, and can be driven with an expression. 

See also [Flag](<./Flag.md> "Flag").
