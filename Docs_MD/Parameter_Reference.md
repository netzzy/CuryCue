# Parameter Reference

A parameter reference can be setup between any two parameters by putting an expression in one parameter that refers to another parameter. This creates a [Link](<./Link.md> "Link") between the two parameters such that when one changes, the other will change automatically. A Parameter reference is a type of [Link](<./Link.md> "Link"), known in other software as a "constraint". 

**Source Parameter** \- this parameter is being referenced by another parameter. 

**Reference Parameter** \- this parameter's value is linked (referenced) to the source parameter and contains an expression. 

Any change in the source parameter's value will change the referenced parameter's value. 

## Making a Parameter Reference

**Using right-click menus**

1) Right click on any parameter and select _Yank Parameter_. This will be the source parameter. 

2) Go to the parameter you wish to be referenced, right-click and select _Put Yanked References_

  
**Using expressions**

Use a Python expression like`op('pattern1').par.phase * 20.`in the parameter.
