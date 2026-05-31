# Dependency

Dependency is the [Procedural](<./Procedural.md> "Procedural") mechanism in TouchDesigner, where if one piece of data changes, it automatically causes other operators and expressions to re-[Cook](<./Cook.md> "Cook"). This assures all data is consistent in a TouchDesigner process, and causes all the output displays, UIs, devices and protocols to update in realtime. 

#### Automatic Dependency

If there is a change in an operator's output data or parameter value, it causes other operators downstream from it to cook. Downstream means operators that are connected to the output of a changed node, and operators (or their parameters) that refer to the changed operator (often visible as the dashed-lines in a network). 

See [Cook](<./Cook.md> "Cook"). 

#### Python Data Dependency

Because Python does not inherently have a procedural mechanism, [Dependency Objects](<./Dependency_Class.md> "Dependency Class") in TouchDesigner allow python data to cause downstream cooking when that data is changed. 

See [Dependency_Class](<./Dependency_Class.md> "Dependency Class") for how to set up Python Dependency. To create recursively dependable Python collections, see [Deeply Dependable Collections](<./TDStoreTools.htm#Deeply_Dependable_Collections> "TDStoreTools").
