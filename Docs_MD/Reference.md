# Reference

In a network, a grey dashed line between nodes is a **Reference** (or Link) that indicates one operator is getting data from another operator.   
  
A Reference is formed by either 
* a [Parameter Reference](<./Parameter_Reference.md> "Parameter Reference"), a parameter in an OP that is a name or path to another operator, or
  * a [Node Reference](</index.php?title=Node_Reference&action=edit&redlink=1> "Node Reference \(page does not exist\)"), an expression that contains the name or path of another operator. The expression can appear in a parameter, or in a DAT's python script.
  * a DAT Cell Reference
  * a CHOP Channel Reference


When a reference is in an expression, like`op('base1/pattern1').par.phase`, it specifies the location to retrieve a value from. 

When a reference is a parameter in an OP, such as`/project1/pattern1`, the data output from the source OP is passed to, or shared with the OP containing the reference. For example, if it's a reference to a TOP, the source image is used to generate the output of the OP. 

In some cases a parameter that is an OP reference is actually a reference to multiple OPs - the path to lultiple OPs is obtained by listing their paths or using wildcards to specify multiple OPs. See [Pattern Matching](<./Pattern_Matching.md> "Pattern Matching"). 

Examples of operators that have reference parameters: 
* [Select TOP](<./Select_TOP.md> "Select TOP"), [Select CHOP](<./Select_CHOP.md> "Select CHOP"), [Select DAT](<./Select_DAT.md> "Select DAT")
  * [Render TOP](<./Render_TOP.md> "Render TOP") the names of cameras, lights and geometry objects
  * [Composite TOP](<./Composite_TOP.md> "Composite TOP")
  * [Join CHOP](<./Join_CHOP.md> "Join CHOP")


**See also** : [Wire](<./Wire.md> "Wire"), [Hierarchy](<./Hierarchy.md> "Hierarchy")
