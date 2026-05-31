# Link

A Link or Reference is a grey dashed line between nodes that that indicates one operator is getting data from another operator. In contrast, a colored [Wire](<./Wire.md> "Wire") connects the output of one node to an input of another node in the same [Operator Family](<./Operator_Family.md> "Operator Family"). 

Reference / Link types include: 
1. a parameter in an OP that is a name or path to another operator - node paths where a node fetches the data of another node, as in the [Select TOP](<./Select_TOP.md> "Select TOP") and [Select CHOP](<./Select_CHOP.md> "Select CHOP").
  2. a [Python](<./Python.md> "Python") expression in a [Parameters](<./Parameter.md> "Parameter") or a DAT script that contains: 
     1. the name or path of another operator
     2. data from the output of another parameter:`op('pattern1')['chan1'][5]`3. a parameter of another operator:`op('pattern1').par.phase`4. a python member of another operator, like`op('pattern1').numSamples`3. a CHOP [Exporting](<./Export.md> "Export") where a CHOP channel is sent to an operator [Parameter](<./Parameter.md> "Parameter").
  4. s [DAT Export](<./DAT_Export.md> "DAT Export") where a row of a table DAT is sent to an operator [Parameter](<./Parameter.md> "Parameter").
  5. a DAT operator executing its content on changes in another node, as in the [CHOP Execute DAT](<./CHOP_Execute_DAT.md> "CHOP Execute DAT").


When a reference is in an expression, like`op('base1/pattern1').par.phase`, it specifies the location to retrieve a value from. for example`op('table1')[3,4]`from a table cell or`op{'pattern1')['chan1']`from a CHOP's output channel. 

When a reference is a parameter in an OP, such as`/project1/pattern1`, the data output from the source OP is passed to, or shared with the OP containing the reference. For example, if it's a reference to a TOP, the source image is not copied but is used to generate the output of the OP. 

In some cases a parameter that is an OP reference is actually a reference to multiple OPs - the path to multiple OPs is obtained by listing their paths or using wildcards to specify multiple OPs. See [Pattern Matching](<./Pattern_Matching.md> "Pattern Matching"). 

Examples of operators that have reference parameters: 
* [Select TOP](<./Select_TOP.md> "Select TOP"), [Select CHOP](<./Select_CHOP.md> "Select CHOP"), [Select DAT](<./Select_DAT.md> "Select DAT")
  * [Render TOP](<./Render_TOP.md> "Render TOP") the names of cameras, lights and geometry objects
  * [Composite TOP](<./Composite_TOP.md> "Composite TOP")
  * [Join CHOP](<./Join_CHOP.md> "Join CHOP")

## See also

[Wire](<./Wire.md> "Wire"), [Reference](<./Reference.md> "Reference"), [Parameter Reference](<./Parameter_Reference.md> "Parameter Reference"), [Connector](<./Connector.md> "Connector"), [Node](<./Node.md> "Node"), [Operator](<./Operator.md> "Operator")
