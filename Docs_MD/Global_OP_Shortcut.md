# Global OP Shortcut

Global Operator Shortcuts help you get to any [component](<./COMP_Class.md> "COMP Class") from **any** [operator](<./OP_Class.md> "OP Class"). In large systems you may want to access components that are not a parent of the current operator, but located in arbitrary components. Thus [Parent Shortcuts](<./Parent_Shortcut.md> "Parent Shortcut") would not work in this case.   

### Example

You have a component`/myProject/mediaManager`that you want accessible everywhere.   
Set its **Global OP Shortcut** parameter to`MediaManager`.   
Then from any operator or script,`op.MediaManager`, will be equivalent to that component:`op('/myProject/mediaManager')`.   
A child movie operator`movie1`in that component can then be reached anywhere by`op.MediaManager.op('movie1')`.   

### Conflicts

An error will occur if two components have the same **Global OP Shortcut**. To handle this, either rename them individually, or name them sequentially.   
For example`/myProject/Player1`and`Player2`may have their shortcut parameters set with the expression:`'Player'+str(me.digits))`.   
This results in shortcuts`Player1`and`Player2`. 

For exact usage and details, see [OP Class#Members](<./OP_Class.htm#Members> "OP Class").   
See also:`parent()`in [Td_Module](<./Td_Module.md> "Td Module"), [Parent Shortcut](<./Parent_Shortcut.md> "Parent Shortcut").
