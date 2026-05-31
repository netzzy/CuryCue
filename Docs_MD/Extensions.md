# Extensions

When creating a custom Component, it is often desirable to extend the component's functionality and data. This can be accomplished using Python **Extensions**. You can add local Python data and functionality, including data that will work with TouchDesigner's [procedural](<./Dependency.md> "Dependency") system. Extensions are specified as a list of Python objects on the Extensions page of a Component. Each of a Component's extensions can then be accessed by other operators, either directly (when **[Promoted](<#Promoting_Extensions>)**) or through the [`**ext**`object](<#The_ext_Object>). 

Creating extensions requires a basic understanding of the Python programming language. Some great learning resources: 
* [General Python tutorial](<http://docs.python.org/tutorial>)
  * [Introduction to Python in TouchDesigner](<./Introduction_to_Python_Tutorial.md> "Introduction to Python Tutorial")
  * [Matthew Ragan's tutorial: Understanding Extensions](<http://matthewragan.com/2015/07/05/touchdesigner-understanding-extensions/>)
  * Extension and other Python examples can be found in`Samples/Learn/PythonExamples.toe`of the TouchDesigner installation folder.

# Creating Extensions

The easiest and recommended way to create extensions is using the [Component Editor](<./Component_Editor_Dialog.md> "Component Editor Dialog"). You can also set up an extension directly using your custom Component's **Extension Parameters**. 

## Using The Component Editor To Create An Extension

To open the **[Component Editor](<./Component_Editor_Dialog.md> "Component Editor Dialog")** , select **Customize Component...** from the [RMB Menu](<./RMB_Menu.md> "RMB Menu") of your custom Component. Open the **Extension Code** section of the dialog. 

The Extension Code section of the Component Editor assists in creating extensions for your custom Component. To create a new extension, simply enter the name in the textbox and click **Add**. Once created, you can edit, reinitialize, or delete the extension using the buttons on the right. The **+** expands advanced features that let you create a custom definition and/or name for your extension, or turn Promotion on or off. For more info, see the [Extension Parameters](<#Extension_Parameters>) section below. 

**TIP:** It is standard in TouchDesigner to capitalize your extension name and add the suffix **`Ext`**. 

## Extension Parameters

**NOTE:** using the Component Editor automates this process. If you are using that method, you won't need to work directly with these Parameters. 

To create an extension directly, you must set up your custom Component's **Extension Parameters**. In most cases, you will also set up an associated DAT containing your extension code. 

Each of a Component's four available extensions has three parameters associated with it: 

#### Extension Object

The **Extension Object** Parameter contains a bit of Python code that must _**return a Python object when executed**_. A reference to this object will be stored as the given extension. In the image above, we see the most common usage: a class (`ExampleExt`) instantiated with the Component (`me`) as argument. The class is defined in a DAT, also named`ExampleExt`inside the Component. 

Expert Python users will note that the code in this Parameter can return any Python object, which has some creative uses, such as [Internal Parameters](<./Internal_Parameters.md> "Internal Parameters"). 

#### Extension Name

By default, an extension is referenced by the Python object's class name. In the above example, it would be called`ExampleExt`. The **Extension Name** parameter lets you give the extension a name of your choosing. So, in the above image, we see that`ExampleExt`will use the name`CustomNameExt`. 

#### Promote Extension

**Promoted Extensions** allow more direct access to their data and functionality. See [Promoting Extensions](<#Promoting_Extensions>). 

#### Re-Init Extensions

TouchDesigner will automatically re-initialize extensions when they change, but sometimes you will want to do this manually. The **Re-Init Extensions** Parameter will re-run the code in the Extension Object parameters and replace the Component's extensions with the results. 

# Writing Extension Code

In most cases, you will write extension code in a DAT within your custom Component. If you use the [Component Editor](<./Component_Editor_Dialog.md> "Component Editor Dialog") to create your extension, this is set up automatically for you. We will use the default extension that the Component Editor creates as an example in the following sections. 
[code] 
    from TDStoreTools import StorageManager
    import TDFunctions as TDF
    
    class DefaultExt:
    	"""
    	DefaultExt description
    	"""
    	def __init__(self, ownerComp):
    		# The component to which this extension is attached
    		self.ownerComp = ownerComp
    
    		# properties
    		TDF.createProperty(self, 'MyProperty', value=0, dependable=True,
    						   readOnly=False)
    
    		# attributes:
    		self.a = 0 # attribute
    		self.B = 1 # promoted attribute
    
    		# stored items (persistent across saves and re-initialization):
    		storedItems = [
    			# Only 'name' is required...
    			{'name': 'StoredProperty', 'default': None, 'readOnly': False,
    			 						'property': True, 'dependable': True},
    		]
    		# Uncomment the line below to store StoredProperty. To clear stored
    		# 	items, use the Storage section of the Component Editor
    		
    		# self.stored = StorageManager(self, ownerComp, storedItems)
    
    	def myFunction(self, v):
    		debug(v)
    
    	def PromotedFunction(self, v):
    		debug(v)
    
[/code]

## Importing Modules
[code] 
    from TDStoreTools import StorageManager
    import TDFunctions as TDF
    
[/code]

In the first two lines of the default extension we import a class and a module using standard Python import statements. For more info on this, see [Importing Modules](<./Introduction_to_Python_Tutorial.htm#Importing_Modules> "Introduction to Python Tutorial"). 

## Python Attributes

Python attributes are created using standard Python. After the class definition, we see the following code creating attributes: 
[code] 
    		# The component this extension is attached to
    		self.ownerComp = ownerComp
    
[/code]

and 
[code] 
    		# attributes:
    		self.a = 0 # attribute
    		self.B = 1 # promoted attribute
    
[/code]

The`ownerComp`attribute is standard and should be used in every extension. It is passed as an argument during extension creation and holds the Component that the extension is attached to. Next, two custom attributes are created,`a`and`B`. Because`B`is capitalized, it can be [promoted](<#Promoting_Extensions>). We'll explore what that means more below, but in general, promoted members can be accessed directly through the operator, like this:`op('myOperatorWithExtension').B`. 

## Python Properties

Python properties are like attributes but they have accessor functions. If you are not familiar with this concept, there are a number of tutorials online... [here](<https://www.programiz.com/python-programming/property>) is a good one. Properties can be created using standard Python methods, which we won't explore here. In this default extension, we use a utility function from the`[TDFunctions](<./TDFunctions.md> "TDFunctions")`module called`createProperty`. The example below is just like the one above, with the exception of`readOnly`being set to True. 
[code] 
    		TDF.createProperty(self, 'MyProperty', value=0, dependable=True,
    						   readOnly=True)
    
[/code]

This code creates a property called`MyProperty`which has a starting value of zero, is dependable (explained [below](<#Dependable_Values>)), and is read-only. You can read the value of this property directly:`value = self.MyProperty`. Because it is read-only and dependable, you set it like this:`self._MyProperty.val = newValue`(just prefix the name with an underscore). If it were not read-only, you would set it directly:`self.MyProperty = newValue`. 

All these features will be useful to advanced Python users, but less experienced programmers will more often use`createProperty`in a simpler way: 
[code] 
    		TDF.createProperty(self, 'MyProperty', value=0)
    
[/code]

This creates`MyProperty`with a starting value of zero, using the defaults of`dependable=True`and`readOnly=False`. 

## Storage Manager

All of the properties above are re-created when the extension initializes, which happens when a file is loaded, the Operator is cut/pasted, when the Re-Init Extensions button is pressed, etc. To store Python values in such a way that they are persistent during these events, use the **`StorageManager`** class. 

**Important:** in many cases it is better to use [Custom Parameters](<./Custom_Parameters.md> "Custom Parameters") for persistent values, because that gives users direct access to them on the Component's Parameter page. The best times to use`StorageManager`are when you want to hide values or save values on your component. 
[code] 
    		# stored items (persistent across saves and re-initialization):
    		storedItems = [
    			# Only 'name' is required...
    			{'name': 'StoredProperty', 'default': None, 'readOnly': False,
    			 						'property': True, 'dependable': True},
    		]
    		# Uncomment the line below to store StoredProperty. To clear stored
    		# 	items, use the Storage section of the Component Editor
    		
    		# self.stored = StorageManager(self, ownerComp, storedItems)
    
[/code]

You must uncomment that last line for this to take effect. It is commented out by default to avoid saving example data on the component. The use of the`StorageManager`object is explained in detail in the [StorageManager Class](<./StorageManager_Class.md> "StorageManager Class") wiki. 

## Extension Functions

Define functions in extensions exactly as you would in any Python class: 
[code] 
    	def myFunction(self, v):
    		debug(v)
    
    	def PromotedFunction(self, v):
    		debug(v)
    
[/code]

As with other attributes, capitalized function names will be accessible through [promotion](<#Promoting_Extensions>). Within extension functions, use`self.ownerComp`to accessed the Component that the extension is attached to. 

# Dependable Values

Often you'll want to reference extension properties in [Parameter Expressions](<./Parameter_Expression.md> "Parameter Expression") and have those expression values update automatically when the property value changes. This functionality can be created by using [Dependencies](<./Dependency_Class.md> "Dependency Class"). The easiest way to create dependable values is to use the`[createProperty](<#Python_Properties>)`function or`[StorageManager](<#Storage_Manager>)`class, as explained above. 

Python collections (lists, dictionaries, and sets) can be a bit more complicated to make dependable. For a full explanation of how to achieve this, see [Deeply Dependable Collections](<./TDStoreTools.htm#Deeply_Dependable_Collections> "TDStoreTools"). 

# Accessing Extensions

There are three ways to access the extensions on your Component. In order of most common usage to least, they are: **Promotion** , the`**ext**`member, and the **`extensions`** member. 

## Promoting Extensions

The simplest way to access attributes of an extension is to **Promote** it. If an extension is promoted, all its capitalized methods and members are available at the Component level. Using the above examples, and assuming the extension were on an Operator named`myCustomComp`, all of the following would work: 

    

  *`op('myCustomComp').B`*`op('myCustomComp').MyProperty`*`op('myCustomComp').StoredList`*`op('myCustomComp').PromotedFunction('test')`The following would not work, because they are not capitalized, and thus not promoted: 

    

  *`op('myCustomComp').a`*`op('myCustomComp').myFunction('test')`## The`ext`Member

Another powerful way to access extensions is the **`ext`** member. **All** Operators have an **`ext`** member that gives them access to extensions within them (or their parents, see below). Extensions are accessed via their class name, or, if it's not blank, the string in the associated Extension Name parameter. Attributes **don't have to be promoted** to be accessed through the`ext`member. Using a couple of the examples above, the following would work: 

    

  *`op('myCustomComp').ext.ExampleExt.B`*`op('myCustomComp').ext.ExampleExt.PromotedFunction('test')`*`op('myCustomComp').ext.ExampleExt.a`*`op('myCustomComp').ext.ExampleExt.myFunction('test')`Another important attribute of the`ext`member is that it exists on all Operators and will **search up the network hierarchy** for the named extension. This means that every Operator within`op('myCustomComp')`would be able to use the code:`me.ext.ExampleExt.myFunction('test')`. Technically, the`me`is not even required in most cases, so any Operator within`op('myCustomComp')`could use this in a script:`ext.ExampleExt.myFunction('test')`or this in a parameter expression:`ext.a`. 

## The`extensions`Member

In some rare cases, you may want to access a Component's extensions directly through its`extensions`member. This is a simple Python list containing a Component's four extension objects. Once again, using the above examples, you could access`ExampleExt`this way: 

    

  *`op('myCustomComp').extensions[0].myFunction('test')`# Extension Gotchas

When doing advanced Python programmimg in TouchDesigner, there are a couple sticky situations you can run into. This section attempts to address the common ones. **Note:** It is not necessary to understand these for basic Python programming. 

## Gotcha: "Cannot use an extension during its initialization" and other init timing issues - Solution: **`extensionsReady`** and **`onInitTD`**

Because of timing issues between Python and TouchDesigner, you may occasionally get a **"Cannot Use an extension during its initialization** error. This means that something is trying to access an extension while it is still running its`__init__`function. There are a couple ways to get around this. 
* **If the error occurs in a parameter expression** you can use the **extensionsReady** variable to make sure that the expression doesn't evaluate until all extensions are initialized. Generally, this looks something like this:`parent().MyExtensionProperty if parent().extensionsReady else 0 # or other default value`This will only attempt to evaluate and return`parent().MyExtensionProperty`if the extension is ready, otherwise it will return 0 (or whatever default value you place there). When the extension is initialized, the expression will re-evaluate and be set to`parent().MyExtensionProperty`.
* For other timing issues in extensions, you can define the **built-in`onInitTD`function** in your extension. This function will be called automatically by TouchDesigner at the end of the frame that your extension initialized. This can be very useful for situations when you want your extension to access its Component or other TouchDesigner objects that are not ready at`__init__`time. **Note:** if multiple extensions are initialized on the same frame, they will all run their`__init__`functions before any of their`onPostInit`functions are run.


As an example, you can just add this code to your extension: 

    

    
[code]
    	def onInitTD(self):
    		"""
    		Called at end of frame that this extension is initialized.
    		"""
    		debug('onInitTD')
    
[/code]

## Gotcha: extensions staying in memory - Solution: **`onDestroyTD`**

Because of the way Python garbage collection works, you can run into a situation where your old extensions stay in memory after a component has "re-inited" its extensions. This happens when another Python object holds a reference to the extension or something in the extension (like a function). When this happens, the extension's`__del__`function, the usual place to perform cleanup functions for Python objects, will not be called. 

In order to guarantee cleanup, when extensions are re-initialized, TouchDesigner will call the old extension's`onDestroyTD`function if it exists. This can be used much like Python's builtin`__del__`function. Here is an example extension: 

    

    
[code]
    class TestExt:
    	"""
    	TestExt description
    	"""
    	def __init__(self, ownerComp):
    		self.ownerComp = ownerComp
    
    		self.selfRef = self.__init__ 	# creates a self-reference
    										# keeping TestExt from being 
    										# garbage collected
    		debug('__init__', self)
    
    	def onDestroyTD(self):
    		self.selfRef = None # this line removes the self reference
    							# comment it out to see that onDestroyTD never gets
    							# called when "Reinit Extensions" is pulsed
    		debug('onDestroyTD', self)
    
    	def __del__(self):
    		debug('__del__', self)
    
[/code]

More features that prevent this sort of problem will be coming to TouchDesigner in the future. 

# Example Extension:`ColorExt`This section will describe an example Extension to illustrate many of the concepts on this page. It will be presented as a tutorial so that you can build the extension yourself. 

The`**ColorExt**`extension creates a system that stores a`baseColor`to be used as a background in panels inside the custom Component. The`baseColor`is not meant to be directly changeable, but can be incremented through a list of available base colors. 

**Note:** because Python errors are reported there, it is always worthwhile to keep a [Textport](<./Textport.md> "Textport") open when working with extensions. 

## Step 1: Create The`ColorExt`Extension

For starters, we will want an empty Component to customize. Create a [Container COMP](<./Container_COMP.md> "Container COMP") somewhere in your network. It's always a good idea to name your Operators, and this is especially true of custom Components, so rename it`colorExample`. Use the [Component Editor](<./Component_Editor_Dialog.md> "Component Editor Dialog") to add an extension named`ColorExt`. This creates a default extension in a DAT inside`colorExample`. It also sets up`colorExample`'s Extension Parameters to use the new extension. Click the "Edit" button in the Component Editor to edit`ColorExt`. 

## Step 2: Write The`ColorExt`Extension

The`ColorExt`extension will look a lot like the default because we are intentionally using many of the same features. Here is the code for you to enter or cut/paste: 
[code] 
    from TDStoreTools import StorageManager  # deeply dependable collections/storage
    TDF = op.TDModules.mod.TDFunctions  # utility functions
    
    class ColorExt:
    	"""
    	ColorExt stores a base color to be used by operators inside it.
    	"""
    
    	def __init__(self, ownerComp):
    		# The component this extension is attached to
    		self.ownerComp = ownerComp
    
    		# Attributes:
    		self.baseColorList = [
    			# [red, green, blue]
    			[1, 0, 0],
    			[0, 1, 0],
    			[0, 0, 1],
    			[1, 1, 1]
    		]
    
    		# stored items (persistent across saves and re-initialization):
    		storedItems = [
    			{'name': 'ColorIndex', 'default': 0, 'readOnly': True},
    		]
    		self.stored = StorageManager(self, ownerComp, storedItems)
    
    		# Properties
    		TDF.createProperty(self, 'BaseColor',
    				   value=self.baseColorList[self.ColorIndex],
    				   readOnly=True,
                       dependable=True)
    
    	def IncrementBaseColor(self):
    		"""
    		Promoted Function description.
    		"""
    		self.stored['ColorIndex'] += 1
    		if self.ColorIndex == len(self.baseColorList):
    			self.stored['ColorIndex'] = 0
    		self._BaseColor.val = self.baseColorList[self.ColorIndex]
    
[/code]

####`ColorExt`Attributes

We only need one attribute for`ColorExt`, which is the list of available base colors. Sensibly, we have named this`baseColorList`. Notice that it is not promoted because it starts with a lower case letter. Though there is no way to truly protect Python attributes from being changed from the outside, not promoting them generally indicates that they are not meant to be messed with except from within. 

####`ColorExt`Stored Items

We will store one item,`ColorIndex`, our index into`baseColorList`. This way, whichever base color is chosen won't be reset when the extension is reinitialized. By way of example, we _have_ promoted`ColorIndex`(by giving it a capitalized name) but we have once again discouraged changing it from the outside by setting it to read-only. We will see how to set it below in The IncrementBaseColor Function. 

**Note:** the positions of stored items and properties are switched in`ColorExt`because we need to use`ColorIndex`in our property. 

####`ColorExt`Properties

As described above, the purpose of`ColorExt`is to provide a base color that can be used by panels inside`colorExample`. The`BaseColor`property will provide that value. We make it a property so that it can be made dependable, which means that panels that use`BaseColor`in their expressions will be automatically updated when the value of`BaseColor`changes. Once again, we set the property to be read-only in order to discourage direct changes from the outside. 

### The`IncrementBaseColor`Function

The`**IncrementBaseColor**`function provides the main interface for changing`colorExample`'s base color. Because this function is our main intended interface from the outside, the function name is capitalized so that it will be promoted. Calling the function increments our stored`ColorIndex`and sets our`BaseColor`property to the appropriate item in`baseColorList`. 

Another thing worth noting in this function is how the read-only values are set. Stored read-only values are accessed through the Component's`StorageManager`object,`stored`, as defined in the`__init__`method. This object acts like a Python dictionary with stored items keyed by their name: 
[code] 
    		self.stored['ColorIndex'] += 1
    
[/code]

Properties, by default, store their values in a member with the name prefixed by an underscore. Dependable values, in addition must be accessed through their member's`val`attribute. Thus, we have: 
[code] 
    		self._BaseColor.val = self.baseColorList[self.ColorIndex]
    
[/code]

## Step 3: Using`ColorExt`Once this code is entered, the extension should be initialized automatically. If in doubt, you can always go to the Component's Extensions parameter page and press Re-Init Extensions. We can now use the new features we have added to`colorExample`. 

### Using`BaseColor`Our original goal was to create a base color that can be used by panels inside`colorExample`. To see this in action, go inside`colorExample`and create a [Container COMP](<./Container_COMP.md> "Container COMP"). Go to the new container's Look parameter page and enter the following into its Background Color expressions: [![BaseColorPars.PNG](./images/3/3e/BaseColorPars.png)](</File:BaseColorPars.PNG>)

The color should immediately turn to blue, which is item 0 (the`ColorIndex`default) in`baseColorList`. Notice that we use the`ext`method of accessing`ColorExt`. This will work for every Operator inside`colorExample`, because`ext`will search upwards until it finds the named extension. 

### Using`IncrementBaseColor`We have intentionally made it difficult to change the base color of`colorExample`. Instead, the user is meant to cycle through a list using our extension function,`IncrementBaseColor`. We will use the promotion system to run this function as if it were a method of the`colorExample`operator. 

In the textport, type the following code:`op("_< path to colorExample>_").IncrementBaseColor()`. Replace _< path to colorExample>_ with the appropriate path. **Tip:** if you drag`colorExample`into the textport, TouchDesigner will insert its path automatically. 

As you can see, this command increments the base color, and our inner container's background is updated automatically. This is so cool that you might want to run`IncrementBaseColor`a few more times to see the other options. 

## Wrapping Up

Although this example was an extremely simple illustration of the power of extensions, we have seen two of their most powerful uses. 
1. Using the`ext`object, you can provide custom data and functionality to every Operator in a custom Component.
  2. Using promoted extensions, you can provide custom data and functionality to the custom Component itself.


The extension system provides effectively limitless Component customization possibilities in TouchDesigner. One thing worth noting is that in many cases Python operates more slowly than Operators. When doing time-critical operations that require extensions, it will sometimes be worthwhile to use Operators in combination with your extensions and allow the Operators to do the heavy computing while extensions manage the system organization. 

Some examples of extremely customized Components that make heavy use of the extension system: [Lister Custom COMP](<./Palette-lister.md> "Palette:lister"), [PopMenu Custom COMP](<./Palette-popMenu.md> "Palette:popMenu"), [PopDialog Custom COMP](<./Palette-popDialog.md> "Palette:popDialog").
