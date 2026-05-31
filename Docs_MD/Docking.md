# Docking

Docking a node is a way to reduce clutter in a network by hiding an operator as a small dock icon on another node. This icon is color-coded to indicate the [Operator Family](<./Operator_Family.md> "Operator Family") of the docked node. Any node can be docked to another node. When a dock pa ent node is moved in the [Network Editor](<./Network_Editor.md> "Network Editor"), the docked node moves with it as well. 

Docking does not affect the nodes' behavior, only the look. 

A docked node is often docked to a related node to help with network organization, an example is the [Ramp TOP](<./Ramp_TOP.md> "Ramp TOP"). A new Ramp TOP is created with a docked [Table DAT](<./Table_DAT.md> "Table DAT") that stores the ramp color information. To view the Table DAT, click on the DAT-colored dock icon attached to the lower-right corner of the Ramp TOP. Click on the icon again to collapse the docked node back down to an icon. 

## Docking a Node

A node can be docked two different ways: 
* \- Right-clicking on the node to be docked and select **Dock to ...** , then click on the node you want to dock to.
  * \- Using`Op.dock`and`Op.docked`in python for the [Operator class](<./OP_Class.htm#Common_Flags> "OP Class").


[![](./images/9/9c/Docking.png)](</File:Docking.png>)

_ramp1_ with docked node collapsed, _ramp2_ with docked node exposed
