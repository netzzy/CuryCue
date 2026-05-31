# Working with OPs in Python

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

### Examples

Place down a new [Text DAT](<./Text_DAT.md> "Text DAT"), ensure its parameter flag is set to Python, and enter the following script: 
[code] 
    n = op('/project1')
    m = n.ops('text*')
    for a in m:
    	print(a.name)
    
[/code]

After running the script,`n`is assigned the results of the global function, while`m`is assigned results relative to`n`. 

Some useful members and methods of an OP object, are: 

  *`name`*`path`*`children`*`parent()`These are described in [OP Class](<./OP_Class.md> "OP Class"). Notice the last attribute,`parent()`is a function. It takes an optional argument specifying how far up the parent chain to climb. To see how they are used in practice, put down a new Text DAT, ensure its Parameter Language parameter is set to Python and enter the following code: 
[code] 
    print('i am ', me)
    print('child of ', parent())
    print('grandchild of ', parent(2))
    
    print('root children:')
    k = root.children
    for r in k:
    	print(r)
    
[/code]

The resulting details will be found in the textport. 

## Common Python Tasks

### Expressions

| Python   
---|---  
Getting an OP's path  |`op('sphere1').path`Getting an OP's name  |`op('sphere1').name`Getting an OP's digits  |`op('sphere1').digits`Querying the value of an OP's parameter  |`op('sphere1').par.tx.eval()`or when it's constant`op('sphere1').par.tx`Querying a parameter in the same OP |`me.par.tx`Getting Info CHOP channels from an OP  
without cooking it  |`passive(op('moviein1')).width`Getting an OP's parent  |`parent()`Getting an OP's grand-parent  |`parent(2)`Getting an OP's name  |`me.name`Getting an OP's parent's name  |`parent().name`Getting digits of an OP's name from its parameters  |`me.digits`Getting digits of an OP's parent's  
name from its parameters  |`parent().digits`Getting an OP's type  |`# returns an OP object, not a string  
type(op('moviein1'))`getting a unique random number each frame  |`tdu.rand(absTime.frame+.1)`getting a unique random number per numbered operator  |`tdu.rand(me.digits+.17)`Checking for an OP's existence  |`if op('moviein1'):`or`bool(op('moviein1'))`Getting the number of children of a COMP |`len(op('geo1').children)`Getting the number of inputs of a multi-input OP |`len(op('switch1').inputs)`Getting [Info CHOP](<./Info_CHOP.md> "Info CHOP") channels from an OP, width is a member  |`op('moviein1').width`Conditional "if" in one line of a parameter  |`22 if me.time.frame<100 else 33`Conditional "if" alternative  |`[33,22][me.time.frame<100]`Convert space separated string to a list  |`tdu.split('Space separated string with "two word item"')`List comprehension  |`[c.name for c in root.children]`Conditional list comprehension  |`[c.name for c in root.children if c.name != 'perform']`Test operator type  |`type(root) == baseCOMP`Test operator family  |`isinstance(root, TOP)`### Time

"Absolute Time" is the time since you started your TouchDesigner process, not counting when your power button was off (top bar). 

| Python   
---|---  
Retrieving a node's local frame number  |`me.time.frame`Retrieving a node's local time in seconds  |`me.time.seconds`Retrieving absolute time in frames  |`absTime.frame`Retrieving absolute time in seconds  |`absTime.seconds`### Storage in Python

Storage is the preferred way to work with persistent global data in Python, since it can store anything data type. 

| Python   
---|---  
Setting a value in storage of a component`n`|`n.store('keyname', 0.0)`Getting a value from storage  |`n.fetch('keyname')`Directly access the storage dictionary  |`n.storage`Directly access a key in the storage dictionary  |`n.storage['keyname']`Test if a key exists in the storage dictionary  |`'keyname' in n.storage`### Commands

| Python   
---|---  
Creating an OP ([Sphere SOP](<./Sphere_SOP.md> "Sphere SOP"))  |`op('/project1').create(sphereSOP)`Creating a named OP |`op('/project1').create(sphereSOP, 'mysphere')`Copying OPs (Nodes)  |`op('/project1').copy(op('out1'), name='out2')`Deleting an OP |`op('mysphere').destroy()`Renaming an OP |`op('mysphere').name = 'thesphere'`Changing an OP's type  |`op('mysphere').changeType(boxSOP)`Changing multiple OPs' types  |`list = ops('*sphere*')  
[s.changeType(boxSOP) for s in list]`Setting an OP's comment  |`op('mysphere').comment = 'this is a sphere'`Changing an OP's parameter  |`op('mysphere').par.frequency = 10`Changing an OP's parameter  
with more than 1 value  |`s = op('mysphere')  
s.par.tx = 1  
s.par.ty = 2  
s.par.tz = 3`Pulsing a parameter value  |`op('moviein1').par.cue.pulse()`Cooking an OP |`op('mysphere').cook()`Saving an OP's data to a file  |`op('mysphere').save('sphere.tog')`Changing an OP's [Render](<./Render_Flag.md> "Render Flag") and [Display Flags](<./Display_Flag.md> "Display Flag") on  |`s = op('mysphere')  
s.render = True  
s.display = True`Loading a [.tox file](<./.md> ".tox") into a COMP |`op('/project1').loadTox('geo1.tox')`Wiring operators together  |`Refer to the [Connector Class](<./Connector_Class.md> "Connector Class")`Clicking gadgets (panel components)  |`op('slider1').click(.6, .7)`Timeline Play/Pause  |`me.time.play = True/False`[Run asynchronous or delayed Python code](<./Run_Command_Examples.md> "Run Command Examples") |`run('print("hello, world")', delayMilliSeconds=2000)`### Variables

Variables are always text strings. 

| Python   
---|---  
Setting a value  |`me.var('DESKTOP')`Setting a [Root Variable](<./Variables.htm#Root_Variables> "Variables") |`root.setVar('MEDIA', 'c:/MEDIA')`Setting a [Component Variable](<./Variables.htm#Component_Variables> "Variables")  
at the current component  |`parent().setVar('MEDIA', 'c:/MEDIA')`Setting a Component Variable  
at another component  |`op('/project1/geo1').setVar('MEDIA', 'c:/MEDIA')`Setting a [Path Variable](<./Variables.htm#Path_Variables> "Variables") | Set the Path Variable parameter of any parent component and use`me.var('name')`in the same way.
