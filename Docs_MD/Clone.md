# Clone

**Clones** are TouchDesigner's mechanism to assure many components match the structure and behavior of a master clone. As the master component is edited, all its clones are changed automatically to match.   
  
A clone is a component whose **Clone Master** parameter is set to a path to another component, its "clone master". A component is not a clone if the Clone Master parameter is blank or points to a non-existent component, or if its Clone Enable parameter is off, or if the clone master's Clone Enable is off. 

**Common among all Clones** : What a clone has in common with its master: 
* All top-level custom parameters and pages on the clone master are re-created on the clones. The parameter definitions are the same, but the values are not mirrored - the values of all top-level parameters of the clones are independent of the master. (On a parameter in the master, rclick -> Copy to all Clones to manually propagate a changed value to the clones.)
  * Inside the clones, all clones will be forced to contain the same children operators (nodes) inside the component. This includes the wiring between the nodes, the layout of the nodes, the parameter values, and the flags of the nodes, like bypass, lock and viewer state.


**Unique to each Clone** : Clones can be made to cook and output differently: 
* **component inputs** \- CHOPs, SOPs, TOPs and DATs that feed into the clone via the inputs may have differing data. Therefore the data output from nodes in the clone will often be different, as will the data output from the clone itself.
  * **top-level component parameter values** as noted above.
  * **expressions** \- Expressions on the clone or on nodes inside the clone that use`parent().name`(operator parent's name) and`parent().digits`(digits in operator's parent's name) can be used to differentiate between clones. For example, the clone's name's digits can be used to look up values in tables externally (`op('table1')[parent().digits, 'columnname']`). Therefore parameters may have the same expressions, but the expressions may evaluate to different values.
  * **immune nodes** \- Nodes that are inside the clone and are set to be "immune" (flag on the node) are untouchable and unique. Nodes that have their immune flag set are not forced to match the master of the clones. For example, you may put an immune Table DAT inside a clone that makes it unique, encapsulated and portable.

### Making a Parameter of All Clones have Same Value

Right-click on any parameter that is the master of any number of clones and select “Copy to all Clones”. This finds all the clones and make the values all the same. 

### Clone Immunity and the Immune Flag

Immunity allows (1) a node inside a clone to be not updated from the clone master, and (2) a node to exist in a clone that does not exist in the clone master. 

If you turn on the [Immunity](<./Immune.md> "Immune") flag on a node in a clone, and you change that node in the clone master, the node in the clone will remain the same. A typical example is using Clone Immune to keep personalized [DAT](<./DAT.md> "DAT") tables inside clones: these tables can contain different data in each clone. 

You can add any number new nodes in a clone and turn on their Immunity flag. These nodes will not be deleted or changed by cloning. 

In a clone master component, if you turn in the Immune flag of any node, then that Immune flag is turne on in all clones. If you turn off the Immune flag on a node in the clone master, TouchDesigner will ask you if you want to turn the flag off in all the clones. 

If you paster a Clone Immune node in the Master Clone, then that Immune node will be created in each clone. If you delete an immune node in the clone master, it will delete it in the clones unless you hae gone to the clones and manually set teh clone immune flag. 

See [Immunity](<./Immune.md> "Immune") for more behaviors. 

## See also

[Immune](<./Immune.md> "Immune"), [Replicator Component](<./Replicator_COMP.md> "Replicator COMP")
