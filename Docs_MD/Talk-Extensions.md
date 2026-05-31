# Legacy Docs:

When creating a component with specific functionality, it is often desirable to also extend the component's scripting options. For example, one may want to create a component to play back movie files. Extensions allow for extending the component with specific functions such as 'Preload all Movies' or 'Go to Movie Number 5' etc. 

Extensions also allow for extending the component with specific data and properties. You can add local python data and objects. See also the [Dependency Class](<./Dependency_Class.md> "Dependency Class") if you want your python data to procedurally affect other data. 

Any component in TouchDesigner can be extended in Python. This can be accomplished through the use of Extensions. 

Extensions are specified as a list of Python objects on the **Extensions** page of a component. Each of the extension objects can then be accessed by other operators, either directly or through an automatic search on the object's type. 

Examples can be found in`Samples/Learn/PythonExamples.toe`of the installation folder. 

**TIP** : Read Mathew Ragan's explanation of Extensions on his blog: [Mathew Ragan: Understanding Extensions](<http://matthewragan.com/2015/07/05/touchdesigner-understanding-extensions/>)

**ALSO SEE:** [StorageManager Class](<./StorageManager_Class.md> "StorageManager Class"), [TDFunctions](<./TDFunctions.md> "TDFunctions")

# Example

**TIP** : On the Customize Component... dialog found via the RMB menu on a component, is a tab called Extensions where you can automatically create the required extension nodes with some sample code in it. What you find below is a walk-through of doing the same thing. 

Create a new component called`base1`. In this component add a Text DAT called`text1`. In this DAT, define two classes by entering the following text:   

[code] 
    class MyClass1:
        def triple(self, v):
            return v*3
    
     class MyClass2:
        def triple(self, v):
            return v*3
    
[/code]

Normally these class definitions can be accessed as a [module](<./MOD_Class.md> "MOD Class") with expressions such as`mod.text1.MyClass1`and`mod.text1.MyClass2`. See: [Creating Internal Modules from DATs](<./Introduction_to_Python_Tutorial.htm#Creating_Internal_Modules_from_DAT> "Introduction to Python Tutorial") for more information. 

In this case however, specific instances of those classes will be created in a component extension. 

Create a [ Geometry Object Component](<./Geometry_COMP.md> "Geometry COMP") in`base1`named`geo1`. 

In two of`geo1`'s **Extension Objects** parameters, enter:`mod.text1.MyClass1()`and`mod.text1.MyClass2()`Click **Re-Init Extensions** to initialize these extensions in the component. 

Bringing up Operator popup info on`geo1`(middle clicking on the node) should now show`MyClass1`and`MyClass2`as extensions. 

Create a [Box SOP](<./Box_SOP.md> "Box SOP") inside of`geo1`. We wish to access the above methods in the SOP's parameters. There are a few ways to do this. 

Firstly, we can access the extension objects directly, if we know where they exactly are. In the box **tx** parameter enter:`[code]
    op('..').extensions[0].triple(0.33)
    
[/code]```This will look in parent`geo1`, use its first extension object to access the`triple()`method. More generally though, we will not know where an extension is located, but what type of extension we are looking for. 

Instead in parameter **tx** now enter:```[code]
    ext.MyClass1.triple(0.33)
    
[/code]```This will search upwards through all component parents, until it finds an extension object of type`MyClass1`, callings its`triple`method. 

Lastly, an extension may not live in a direct parent component, but in a sibling etc. In that case, the`ext`search may be started from any arbitrary location:`[code]
    op('/project1/base1/geo1').ext.MyClass1.triple(0.33)
    
[/code]```Like the first example, the above will search`geo1`**and all of its parents** until it finds an extension of type`MyClass1`. However one can specify any starting operator location. 

# Naming Extensions

By default,`ext._type_`searches for extension instances matching _type_ , example:`ext.MyClass`, however extensions can be named with the`Extension Name`parameters. Naming an extension, will then allow searching by that specific name instead. 

# Promoting Extensions

If an extension is promoted in a component, its methods and members are immediately available at the OP level. Each extension in a component can be individually promoted with its corresponding Promote Extension parameter on the Extensions page. 

**Note that to be promoted, methods and members must begin with a capital letter**. If you rename the function`triple()`in the previous example to`Triple()`, then you can use the following examples below once the extension is promoted: 

Example:`[code]
    op('../base2').Triple(12.3)
    
[/code]```instead of`[code]
    op('../base2').ext.MyClass1.Triple(12.3)
    
[/code]```# Dependencies

Often, when you work with Extensions, you'll want to reference properties or members or [storage](<./OP_Class.htm#Storage> "OP Class") and have any references to those values updated dynamically. This functionality can be created by using [Dependencies](<./Dependency_Class.md> "Dependency Class"). 

# Properties

Custom operator properties can be created using Extensions. Below is a simple example of creating a property named`FuelLevel`in an extension named`Car`: 
[code] 
    class Car:
        def __init__(self):
            self.FuelLevel = 100
    
[/code]

This basic example creates a class named`Car`and upon creation, it initializes with a property named`FuelLevel`. If you attach this extension to a [Base COMP](<./Base_COMP.md> "Base COMP") named`base1`, and wanted to query the value you could use the code below: 
[code] 
    op('base1').FuelLevel
    
[/code]

This would return the value 100. If you wanted to update this value, you could use the code below: 
[code] 
    op('base1').FuelLevel = 99
    
[/code]

In this implementation, these properties would not create dependencies for any operators referencing them. You can find an example of creating properties with dependencies on the [Dependencies](<./Dependency_Class.md> "Dependency Class") page. 

# Things to Note

Make sure to specify instances, and not class definitions. Example:`[code]
    me.mod.text1.MyClass()
    
[/code]```not:`[code]
    me.mod.text1.MyClass  # wrong, specifies a class, not an instance of one.
    
[/code]```
