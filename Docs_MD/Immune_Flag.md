# Immune Flag

[![](./images/6/68/ImmuneFlag.png)](</File:ImmuneFlag.png>)

[](</File:ImmuneFlag.png> "Enlarge")

Immune Flag is off

[![](./images/1/11/ImmuneFlagOn.png)](</File:ImmuneFlagOn.png>)

[](</File:ImmuneFlagOn.png> "Enlarge")

Node Immune Flag is on

[![](./images/4/47/ImmuneFlagNetworkOn.png)](</File:ImmuneFlagNetworkOn.png>)

[](</File:ImmuneFlagNetworkOn.png> "Enlarge")

Network Immune Flag is on

Every non-component node has an [Immune](<./Immune.md> "Immune") 2-state [Flag](<./Flag.md> "Flag"), also known as Clone Immune Flag. If the Immune flag is On for a node in a [Clone](<./Clone.md> "Clone"), it is not affected by changes made to the equivalent node in the master clone. You can use the Immune flag to customize parameters of operators, or to add extra operators and additional data that does not exist in the Clone's Master Component. bi-state The Immune flag on non-components is a 2-state flag. 
* [![ImmuneFlagOffIcon.png](./images/9/91/ImmuneFlagOffIcon.png)](</File:ImmuneFlagOffIcon.png>) Off
  * [![ImmuneFlagOnIcon.png](./images/2/28/ImmuneFlagOnIcon.png)](</File:ImmuneFlagOnIcon.png>) On - This node is made immune.


For example, Table DATs in clones are often made immune to make the table unique in each clone. 

What is kept immune: the parameters, the wiring coming to the inputs of the node, and, if the node is a panel, all its [Panel Values](<./Panel_Value.md> "Panel Value") like`state`,`u`and`v`. The data of Table DATs and the data of [Locked](</index.php?title=Lock&action=edit&redlink=1> "Lock \(page does not exist\)") nodes are also kept immune. 

**WARNING** : If you add a new node in a Clone and make the new node's Immune flag On, you may also have to make the Immune flag On of the nodes its output is connected to, since wiring information is held with the inputs of a node. 

#### Immune on Components

Every component node has an [Immune](<./Immune.md> "Immune") 3-state [Flag](<./Flag.md> "Flag"), also known as Clone Immune Flag. 

The Immune flag on components is a 3-state flag. 
* [![ImmuneFlagOffIcon.png](./images/9/91/ImmuneFlagOffIcon.png)](</File:ImmuneFlagOffIcon.png>) Off
  * [![ImmuneFlagOnIcon.png](./images/2/28/ImmuneFlagOnIcon.png)](</File:ImmuneFlagOnIcon.png>) On - This node is made immune.
  * [![ImmuneFlagNetworkOnIcon.png](./images/6/67/ImmuneFlagNetworkOnIcon.png)](</File:ImmuneFlagNetworkOnIcon.png>) On Including Children - This node is made immune plus (if the node is a [Component](<./Component.md> "Component")) all nodes inside the component (recursively) are immune.


If a node is inside a [Clone](<./Clone.md> "Clone") component and the node's Immune flag is On, it is not affected by changes made to the equivalent node in the master clone. 

Thus entire [Components](<./Component.md> "Component") can be made immune using On Including Children, where all the nodes inside the component's network are immune as well. 

The 3-state flag is on the tiles and also in the network editor's list mode (use shift+t to switch modes). 

When a`.toe`or`.tox`file is saved, all cloned nodes are NOT saved in the`.toe`except for immune nodes. Immune nodes in clones are saved since they are not defined in the master clone. Otherwise, nodes in clones are not expected to be saved in the file. 

  
See [Clone](<./Clone.md> "Clone") for additional information. 

See also [Flag](<./Flag.md> "Flag"). 

#### Immune by Python

See`cloneImmune`in [OP_Class](<./OP_Class.md> "OP Class"). 

For components, see`componentCloneImmune`in [COMP_Class](<./COMP_Class.md> "COMP Class"). When`componentCloneImmune`is True, everything inside the clone is immune. When`componentCloneImmune`is False, it uses the [OP_Class](<./OP_Class.md> "OP Class")`cloneImmune`member to determine if just the component is immune (its parameters etc, but not the component's network inside).
