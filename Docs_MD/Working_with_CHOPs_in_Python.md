# Working with CHOPs in Python

The main documentation for the methods and classes you use to work with CHOPs are the [CHOP Class](<./CHOP_Class.md> "CHOP Class") and [Channel Class](<./Channel_Class.md> "Channel Class") articles. This article gives examples of using those methods and classes. 

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

  
Refer to [Working with OPs in Python](<./Working_with_OPs_in_Python.md> "Working with OPs in Python") for more details about this seciton. 

## Using CHOPs in scripts

To use a CHOP in a script you would first get a reference to the CHOP(s) you are interested in using`op()`. Ideally this would be assigned to a variable which you can use multiple times in the script without having to re-search for the OP every time you need it. Then you can use the`[]`s on the CHOP reference to refer to a specific channel. You can either use a channel name like this`['chan1']`or a channel index`[0]`to refer to a channel. For example this script gets the channel named 'chan1' from one CHOP, and the first channel of another CHOP, and adds them together. 
[code] 
     # get a reference to a CHOP named 'pattern1'
     n1 = op('pattern1')
     # get a reference to a CHOP named 'pattern2'
     n2 = op('pattern2') 
       
    
     # now get references to the two channels we are interested in
     c1 = n1['chan1']
     c2 = n2[0]
       
    
     # add them together. This will add the values at the current time, not all the samples in the channels
     total = c1 + c2
    
[/code]

To do an operation on every sample in a channel, you can use the [] operator on the channel. For example this script will add up all the samples in a channel: 
[code] 
     # get a reference to a CHOP named 'pattern1'
     n = op('pattern1')
       
    
     total = 0
     numSamps = n.numSamples
     c = n['chan1'] 
     for i in range(0, numSamps):
       total = total + c[i]
    
[/code]

Alternatively, you can use the channel's`vals`member, which is a list of all its values: 
[code] 
     for v in c.vals:
       total = total + v
    
[/code]

or more simply, using the builtin`sum()`expression: 
[code] 
      total = sum(c.vals)
    
[/code]

You can also get references to channels using the`chan()`method (which is just another form of the [] operator, but with searching capabilities) or the`chans()`method. The`chans()`allows you to get a list channels from a CHOP. If no argument are given to`chans()`then a list of all channels in the CHOP are returned. 

For example this should get a reference to a CHOP, then adds up all of the channels in it. 
[code] 
     # get a reference to a CHOP named 'pattern1'
     n = op('pattern1')
     # start our total at 0
     total = 0
       
    
     # for each channel in the CHOP
     for c in n.chans():
        # c is an instance of the Channel Class, and all the methods/members of that class can be used on it
        # add the channel's current value to the running total
        total = total + c
     print(total)
    
[/code]

To print the name of every channel in a CHOP you can do this: 
[code] 
     # get a reference to 'pattern1'
     n = op('pattern1')
     # start our total at 0
     total = 0
       
    
     # for each channel in the CHOP
     for c in n.chans():
        # c is an instance of the Channel Class, and all the methods/members of that class can be used on it
        print(c.name)
    
[/code]

To get a list of all the channels that start with 't' in a CHOP, you can simply do 
[code] 
     # get a reference to 'pattern1'
     n = op('pattern1')
     ts = n.chans('t*')
    
[/code]

## Casting Channels to a Value

## Using CHOPs in parameters

To reference a CHOP value in a parameter you first need to get a reference to the CHOP, and then use the [CHOP Class](<./CHOP_Class.md> "CHOP Class") to do something with that CHOP such as get a sample from one of its channels. 

For example, this would get the current sample from the channel named 'chan1' from the CHOP named 'pattern1', which is in the same network as the node whose parameters we are typing in 
[code] 
     op('pattern1')['chan1']
    
[/code]

We can also reference a CHOP by its channel index like this: 
[code] 
     op('pattern1')[1] # gets the 2nd channel in the CHOP
    
[/code]

You can get other information about the CHOP also, such as the number of channels 
[code] 
     op('pattern1').numChans
    
[/code]

Or the name of the 3rd channel 
[code] 
     op('pattern1')[2].name
    
[/code]

## Common Python tasks

### Expressions

Evaluate channel`chan1`at the current frame  |`op('pattern1')['chan1'].eval()`---|---  
_or if in parameter, simply:_ |`op('pattern1')['chan1']`Get sample 8 of channel`chan1`|`op('pattern1')['chan1'].eval(8)`Get the number of CHOP Channels  |`op('pattern1').numChans`Get the CHOP length  |`op('pattern1').numSamples`Get the third sample from the first channel  |`op('pattern1')[0][2]`Get the name of the 2nd channel  |`op('pattern1')[1].name`Get the channel index of channel`chan1`|`op('pattern1')['chan1'].index`
