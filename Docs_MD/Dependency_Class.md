# Dependency Class

A **[Dependency](<./Dependency.md> "Dependency")** object is a value that automatically causes any expression referencing it to update when the dependency value has changed. These objects eliminate the need to manually force cook operators referencing values in [Extensions](<./Extensions.md> "Extensions") or [Storage](<./OP_Class.htm#Storage> "OP Class") for example. For information about dependencies in mutable objects (lists, dicts, sets), see **[Deeply Dependable Collections](<./TDStoreTools.htm#Deeply_Dependable_Collections> "TDStoreTools")**

## Instantiators`TDU.Dependency(val = None)`→`TDU.Dependency`: 

> Create a new dependency object. 
> 
>   *`val`\- the starting value to be stored in the dependency object. Can be any Python object.
> 

## Members`val`→`Any`: 

> The value associated with this object. Referencing this value in an expression will cause the operator to become dependent on its value. Setting this value will cause those operators to be recooked as necessary.`peekVal`→`Any`**(Read Only)** : 

> This returns the same value as .val but does not create a dependency on the value.`callbacks`→`list`: 

> A modifiable list of functions. When the Dependency object is modified, it calls each function on the list. Each function is called with a single argument which is a dictionary containing the following: 
> 
>   * 'dependency'- The Dependency that was modified.
>   * 'prevVal' - The previous value if available.
>   * 'callback' - This callback function.
>`ops`→`list`**(Read Only)** : 

> A list of [operators](<./OP_Class.md> "OP Class") currently dependent on the object.`listAttributes`→`list`**(Read Only)** : 

> A list of [list attributes](<./ListAttribute_Class.md> "ListAttribute Class") currently dependent on the object.

## Methods`modified()`→`None`: 

> This call is needed when changing not the value itself, but a subcomponent. For example, if Dependency.val is a dictionary, setting any of the members will not notify the dependent operators. A call to modified is necessary.`setVal(val, setInfo=None)`→`None`: 

> Sets the value with optional information. 
> 
>   * val - The new value to be set.
>   * setInfo (Keyword, Optional) - Optional information passed to the modified callback.
>`[<index or key>]`→`collection value`: 

> **Only when the dependency wraps iterable or mapped data such as a list or dictionary** , you can use [] to access the items in the wrapped data. 
[code]
>     dep = TDU.Dependency({'fred': 33, 'wilma':39})
>     print(dep['fred']) # prints "33". The key to the dictionary works directly on the dependency object.
>     dep2 = TDU.Dependency(["a", "d", "g"])
>     print(dep[2]) # prints "g". The index to the list works directly on the dependency object.
>     
[/code]

### Usage

Consider the following module, used as an [extension](<./Extensions.md> "Extensions") in a component called`comp1`for example 
[code] 
    class MyClass:
    	def __init__(self):
    		self.Scale = 5
    
[/code]

Any expressions that reference`Scale`will not update when`Scale`is manually changed. For example, if either of these expressions was in the value field of a Constant CHOP, it would not be updated if the`Scale`value was updated. 

Example: 
[code] 
    # using a non-promoted extension
    op('comp1').ext.MyClass.Scale
    
    # using a promoted extension
    op('comp1').Scale
    
[/code]

If you need your references to dynamically update, you can create a`Dependency`. Start by defining a`TDU.Dependency`as below: 
[code] 
    class MyClass:
    	def __init__(self):
    		self.Scale = TDU.Dependency(5)
    
[/code]

Now there is a cook dependency created between the`Scale`value, and the Operator referencing it. There are two ways to reference the value. The first is similar to how we were referencing the value previous: 
[code] 
    # using a non-promoted extension
    op('comp1').ext.MyClass.Scale
    
    # using a promoted extension
    op('comp1').Scale
    
[/code]

and the other method is to explicitly call the`Scale`'s`val`: 
[code] 
    # use for non-promoted extension
    op('comp1').ext.MyClass.Scale.val
    
    # use for a promoted extension
    op('comp1').Scale.val
    
[/code]

Note the`.val`is often not required, as the Dependency object will cast itself to its underlying value in most cases. 

To update this value, you must reference the member's`val`. A`Dependency`value is a type in and of itself and writing the expression below would actually overwrite the`Dependency`value with a regular interger and remove the cook dependency from the references: 
[code] 
    # wrong way to update dependency of a promoted extension
    op('comp1').Scale = 5
    
[/code]

What you should do instead is assign the value to the`val`of the`Dependency`as below: 
[code] 
    # correct way to update dependency of a promoted extension
    op('comp1').Scale.val = 5
    
[/code]

Using this method will update the value of`Scale`while keeping the`Dependency`intact. 

Dictionaries, lists, sets, and other objects with changing contents are called "mutable" objects. **If the contents of a mutable object changes, a dependency wrapping it does not automatically register as being modified!** You must either use a **[deeply dependable collection](<./TDStoreTools.htm#Deeply_Dependable_Collections> "TDStoreTools")** or call the`.modified()`function manually as in the example below: 
[code] 
    op('comp1').Scale.val = [1,2,3]
    op('comp1').Scale.val[1] = 15 # changing the contents doesn't update dependency!
    op('comp1').Scale.modified() # this call notifies TouchDesigner that the value has changed
    
[/code]

You can create Python callbacks that are called when the dependency object changes: 
[code] 
    op('comp1').Scale.callbacks = [print]
    
    # adding a function requires getting the list, changing it, then re-setting it
    def prevPrint(info):
    	print(f'Previous value: {info['prevVal']})
        
    callbacks = op('comp1').Scale.callbacks
    callbacks.append(prevPrint)
    op('comp1').Scale.callbacks = callbacks
    
    # removing a callback works similarly
    callbacks = op('comp1').Scale.callbacks
    callbacks.remove(print)
    op('comp1').Scale.callbacks = callbacks
    
[/code]

TouchDesigner Build: Latest\nwikieditorwikieditor2025.300002022.241402021.100002018.28070before 2018.28070
