# Working with DATs in Python

The main documentation for the methods and classes you use to work with DATs are the [DAT Class](<./DAT_Class.md> "DAT Class") and [Cell Class](<./Cell_Class.md> "Cell Class") articles. This article gives examples of using those methods and classes.   
  
## Getting Started

The main class type describing any [Operator](<./Operator.md> "Operator") is the base [OP Class](<./OP_Class.md> "OP Class"). You will need a reference to one of these to do anything. There are two global operator objects are always available (except for in the [Textport](<./Textport.md> "Textport")): 

  *`me`refers to the operator that is currently being evaluated or executed. For example, when executing a script,`me`refers to the containing DAT. When evaluating an expression,`me`refers to the containing operator.
  *`root`refers to the top level component`/`.


To get references to other OPs (for example, a node named`'pattern1'`sitting next to the node`'constant1'`) the most common functions to use are:`op()`and`ops()`, for example`op('pattern1')`.`op()`returns a single OP object, while`ops`returns a (possibly empty) list of OPs. They are described in [td Module](<./Td_Module.md> "Td Module"). 

These functions search for operators from the current component, so both relative and absolute paths are supported. The current component is defined as: The OP that`me`is inside. 

Note that the [OP Class](<./OP_Class.md> "OP Class") itself, also contains an`op()`and`ops()`method. In this case, nodes are searched from the OP. 

For example:`me.op('..')`will always return its own parent, while`op('..')`will return the parent of the current component. 

If you are typing a Python expression in a parameter of a node`'constant1'`, and you wish to get a reference to`'pattern1'`, you would type 
[code] 
    op('pattern1')
    
[/code]

If you are in a script you can assign this reference to a variable for easier repeated access. 
[code] 
    n = op('pattern1')
    
[/code]

In this case`op()`will search relative to the DAT that is executing the script. 

An OP also has a`parent()`method that can be use to get the parent [COMP](<./Component.md> "Component") of it. 
[code] 
    parent()
    
[/code]

If you are putting a Python statement in a parameter of a COMP and want to refer to a child of that COMP, you can use the`op()`method for the OP, which is available as`me`in the parameters. 
[code] 
    me.op('achildnode')
    
[/code]

**TIP:** To find out quickly what members and methods you have access to for any node, select that node and on its parameter dialog, click the Python Help icon. You will go the wiki for the python classes for that node. There you can find out what info you can get about a node, and what methods are available for it. The documentation can also be arrived at by right clicking on the node and selecting "Python Help..." from the menu. 

  
Refer to [Working with OPs in Python](<./Working_with_OPs_in_Python.md> "Working with OPs in Python") for more details about this section. 

## Using DATs in scripts

To use a DAT in a script you would first get a reference to the DAT(s) you are interested in using`op()`. Ideally this would be assigned to a variable which you can use multiple times in the script without having to re-search for the OP every time you need it. Then you can use the`[]`s on the DAT reference to refer to a specific cell. You can use either labels or indices to refer to a cell. For example this script copies cells from one table to another. 
[code] 
     # get a reference to a DAT named 'table1'
     n1 = op('table1')
     # get a reference to a DAT named 'table2'
     n2 = op('table2') 
       
    
     # now get references to the two cells we are interested in
     c1 = n1['month', 'sales']   #Get cell in row labelled 'month' and column labelled 'sales'
     c2 = n2[3,6] # Get row 3 and column 6. (Note indices start at 0, not 1). 
       
    
     # Concatenate them as strings and update the cell with the new value
     total = c1 + c2
     n2[3,6] = total
    
[/code]

## Common Python Tasks

### Expressions

Get a cell value by index  |`op('table1')[2,3]`---|---  
Get a cell value by label  |`op('table1')['r1', 'c1']`Get a cell value by row index, col label  |`op('table1')[2, 'product']`Cast cell to integer and float  |`int(op('table1')['month', 3])  
float(op('table1')['speed', 4])`Get the number of table rows  |`op('table1').numRows`Get the number of table columns  |`op('table1').numCols`Set a cell value by indeces or labels  |`op('table1')[3,4] = 'hello'  
op('table1')[2, 'answer'] = 'hello'  
op('table1')['month', 3] = 'july'`Set a cell value by label  |`op('table1')['r1', 'c1'] = 'abc'`Copy a table to another table  |`op('table1').copy(op('fromTable'))`Append a row to a table  |`op('table1').appendRow(['s1','s2', num])`Append a column to a table  |`op('table1').appendCol(['s1','s2', num])`Access current cell in an [Evaluate DAT](<./Evaluate_DAT.md> "Evaluate DAT") |`me.inputCell`Access neighboring cells in an Evaluate DAT |`me.inputCell.offset(1,2)`
