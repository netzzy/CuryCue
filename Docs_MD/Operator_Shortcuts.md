# Operator Shortcuts

There are three ways to give shortcut names to operators in TouchDesigner: 

[Parent Shortcuts](<./Parent_Shortcut.md> "Parent Shortcut") access a higher level component from within that component. 

[Global OP Shortcuts](<./Global_OP_Shortcut.md> "Global OP Shortcut") access a unique component from anywhere in TouchDesigner. 

[Internal Operator Shortcuts](<./Internal_Operators.md> "Internal Operators") and the related [Internal Parameter Shortcuts](<./Internal_Parameters.md> "Internal Parameters") provide easy access from operators inside a component to other operators inside that same component. 

These should not be confused with [Keyboard Shortcuts](<./Keyboard_Shortcuts.md> "Keyboard Shortcuts"). 

## Python Shortcut Objects

There are a number of Python objects that facilitate the various operator shortcuts in TouchDesigner. They can be accessed in the global namespace through the [Td Module](<./Td_Module.md> "Td Module") and they can also be accessed relative to operators as members of the [OP Class](<./OP_Class.md> "OP Class"). For detailed usage instructions follow those links. A brief description of the objects themselves is below:`**Shortcut**`\- the parent object of all the other shortcut classes. 

  *`**OPShortcut**`\- the most commonly used shortcut, accessed through`op`. Returns an operator (or None if path not found) from a provided path (argument) or [Global OP Shortcut](<./Global_OP_Shortcut.md> "Global OP Shortcut") (member).
  *`**OPEXShortcut**`\- Works just like`OPShortcut`but raises an exception when an operator path is not found. Accessed through`opex`.
  *`**OPsShortcut**`\- Works similarly to`OPShortcut`but accepts multiple patterns, including wildcards, as arguments and returns a list of operators that match.
  *`**ParentShortcut**`\- Allows access to hierarchical parents of an operator. Returns an operator from a provided number of levels (argument) or [Parent Shortcut](<./Parent_Shortcut.md> "Parent Shortcut") name (member).
  *`**IOPShortcut**`\- Allows access to [Internal Operators](<./Internal_Operators.md> "Internal Operators") as defined in a components parameters. Returns an operator.
  *`**IparShortcut**`\- Allows access to [Internal Parameters](<./Internal_Parameters.md> "Internal Parameters") as defined in a components parameters. Returns a parameter. This is basically the same as IOPShortcut but returns the`par`member of the operator instead of the operator itself.
