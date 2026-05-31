# Custom Parameters

Custom parameters enable you to create a variety of [parameters](</index.php?title=Parameters&action=edit&redlink=1> "Parameters \(page does not exist\)") on user-defined [Parameter Pages](<./Parameter_Dialog.htm#Parameter_Pages> "Parameter Dialog") of the [Parameter Dialog](<./Parameter_Dialog.md> "Parameter Dialog"). 

You can create custom parameters in three ways: 
* on [Components](<./Component.md> "Component") as described below.
  * on script operators like the [Script SOP](<./Script_SOP.md> "Script SOP"), [Script CHOP](<./Script_CHOP.md> "Script CHOP") and [Script DAT](<./Script_DAT.md> "Script DAT"), described below.
  * on [C++ operators](<./Category-C++.md> "Category:C++"). Please refer to the [Write a CPlusPlus Plugin](<./Write_a_CPlusPlus_Plugin.md> "Write a CPlusPlus Plugin") page.


The **easiest way to see and edit parameters of components** is through the [Component Editor Dialog](<./Component_Editor_Dialog.md> "Component Editor Dialog"): right-click on a component node and select Customize... 

See also: [Internal Parameters](<./Internal_Parameters.md> "Internal Parameters")

## Naming Conventions

A custom parameter is distinguished from a built-in parameter by the capitalization of the first letter of its otherwise lower-case name (example:`Divisions`) versus all built-in parameters which are fully lowercase (example:`brightness`), and the custom parameter's appearance under the second row of pages on the Parameters Dialog. The standard to follow is to capitalize the first letter while having all remaining letters of the name in lower case. If the first letter of the custom parameter is not uppercase, the creation will fail and an error is returned. Also all parameter names contain no underscores. 

Examples: 
1. A string parameter for a search term:`Searchterm`2. A distance value:`Distance`Keep the number of of characters in custom parameter names below 12, preferably 10, as they are unreadable if you open up the parameter with the + icon by the parameter name. 

Labels for parameters are of the form: Rotate to X Axis, where words are capitalized except those between nouns, verbs, adjectives, adverbs, such as from, if, and, to. 

## Creating Custom Parameters on COMPs

**QUICK START** : Custom parameters are most easily created and managed using the RMB -> Customize... dialog on any component or Script Operator. First you add a new custom page by providing a page name and pressing Add Page. Then select that page under Pages and enter a parameter name (upper case first letter, lower case remaining characters, no spaces, such as "Speed") and parameter type (such as Float), then click Add Par to create the parameter. Then you can change the label that appears on the parameter dialog, the default value and more. Inside the component you can access the parameter using in this example`parent().par.Speed`. 

Creating custom parameters on a component is a two-stage process. The first step is creating the parameter. The second step is defining its behavior. Custom Parameters will exist as a part of the Component until they are explicitly deleted, and the code to create them only needs to be run once. 

A list of all the available parameter types and their arguments are available at the [Page Class](<./Page_Class.md> "Page Class") page. 

Internally, custom parameters are created and managed with python functions. What follows is the python equivalent to working with the Customize dialog. 

The following code will create a pulse type button on a [Parameter Page](<./Parameter_Dialog.htm#Parameter_Pages> "Parameter Dialog") called 'Controls' with a scripting name of 'Startsearch' and the label 'Click to Start Search'. The following code can be entered in a [Text DAT](<./Text_DAT.md> "Text DAT") in the same Network as a [Base COMP](<./Base_COMP.md> "Base COMP") named`base1`or it can also be entered in the [Textport](<./Textport.md> "Textport") if`base1`is created at the root (`/`) level: 
[code] 
    # create a pulse button parameter on the Base COMP node called base1
    baseOp = op('base1')
    newPage = baseOp.appendCustomPage('Controls')
    
    # create a tuplet containing one pulse parameter
    newTuplet = newPage.appendPulse('Startsearch', label='Click to Start Search')
    
[/code]

A tuplet is a list of related parameters that will appear on one row of the parameter interface. You can interact with the Pulse button above just as you would with any other pulse parameter: 
[code] 
    baseOp.par.Startsearch.pulse()
    
[/code]

  
The following code will create a float slider type parameter on a [Parameter Page](<./Parameter_Dialog.htm#Parameter_Pages> "Parameter Dialog") called 'Car Controls' with a label of 'Speed of Car' and a scripting name 'Speed'. It will have a slider minimum value of -2 and a maximum value of 2. The parameter will be clamped at a minimum of -10 and a maximum of 10 preventing the entry of lower and higher values. (These values are initially 0 and 1.) 
[code] 
    # create a float parameter on the Base COMP node called base1
    baseOp = op('base1')
    newPage = baseOp.appendCustomPage('Car Controls')
    newTuplet = newPage.appendFloat('Speed', label='Speed of Car', size=1)
    # get the first (and only) parameter of this tuplet
    p = newTuplet[0]
    
    # define attributes of the newly created parameter
    
    # normMin member defines the slider minimum value
    p.normMin = -2
    
    # normMax member defines the slider maximum value
    p.normMax = 2
    
    # default member defines the default value of the parameter
    p.default = 0.1
    
    # min member defines the absolute minimum value of the parameter
    # clampMin member prevents lower values than set in min
    p.min = -10
    p.clampMin = True
    
    # max member defines the absolute maximum value of the parameter
    # clampMax member prevents higher values than set in max
    p.max = 10
    p.clampMax = True
    
[/code]

  
You can also create multi-value parameters either by specifying the size keyword for integer or float type parameters. This is useful for creating parameters which, for example, have multiple facets to a single parameter. There are a number of pre-built multi-value parameter types that come with a more convenient naming schemes for regularly used arrays, such as RGB, RGBA, XYZ, and more. 

The method to create these parameters will return a tuple of [parameter instances](<./Par_Class.md> "Par Class") which can be used to define the parameters' attributes. In the following example the created parameter names will use the name as specified plus an index indicating the parameters order in the list, here 'Vector1', 'Vector2' and 'Vector3'. The maximum size for any parameter is 4. A for loop is used to iterate through all the vectors and set their parameters quickly. 
[code] 
    # create 3 float parameters on the Base COMP node called base1
    baseOp = op('base1')
    newPage = baseOp.appendCustomPage('Car Controls')
    newTuplet = newPage.appendFloat('Vector', label='Movement Vector', size=3)
    
    # define attributes of the newly created parameters
    for p in newTuplet:
    	#normMin member defines the sliders minimum value
    	p.normMin = 0
    
    	#normMax member defines the sliders maximum value
    	p.normMax = 1
    
    	#default member defines the default value of the parameter
    	p.default = 0.1
    
    	#min member defines the absolute minimum value of the parameter
    	#clampMin member prevents lower values than set in min
    	p.min = 0
    	p.clampMin = True
    
    	#max member defines the absolute maximum value of the parameter
    	#clampMax member prevents higher values than set in max
    	p.max = 10
    	p.clampMax = True
    
[/code]

For a complete overview of custom parameter types, please refer to the [Custom Parameter section of the COMP Class](<./COMP_Class.htm#Custom_Parameters> "COMP Class"). 

## Creating Custom Parameters on Script OPs

Similar to custom parameters on [COMPs](<./Component.md> "Component"), Script OPs like the [Script CHOP](<./Script_CHOP.md> "Script CHOP"), [Script SOP](<./Script_SOP.md> "Script SOP") or [Script DAT](<./Script_DAT.md> "Script DAT") let you define custom parameters via the Script OPs callbacks: 
[code] 
    def setupParameters(scriptOp):
    	page = scriptOp.appendCustomPage('Custom')
    	page.appendFloat('Valuea', label='Value A')
    	page.appendFloat('Valueb', label='Value B')
    	return
    
[/code]

After modifying the`setupParameters()`callback function, pulse the Script OPs 'Setup Parameters' parameter to execute the parameter creation. 

Custom parameter names must begin with a capital letter, and be followed by lowercase letters, numbers or underscores only. 

## Accessing Custom Parameters on Script OPs

Parameters in the Script OPs can be accessed a number of ways. The first is to access button type parameters through the`onPulse()`callback. In the example below, the Script OP has two custom pulse buttons. The`onPulse()`callback prints the name of the button that is pressed. 
[code] 
    # press 'Setup Parameters' in the OP to call this function to re-create the parameters.
    def setupParameters(scriptOp):
    	page = scriptOp.appendCustomPage('Custom')
    	page.appendPulse('Buttona')
    	page.appendPulse('Buttonb')
    	return
    
    # called whenever custom pulse parameter is pushed
    def onPulse(par):
    	print(par.name)
    	return
    
[/code]

Accessing the value of sliders is done by calling the parameter by its scripting name. In the example below two sliders are defined, and their values are accessed on every cook by adding the`print()`functions to the`cook()`callback: 
[code] 
    # press 'Setup Parameters' in the OP to call this function to re-create the parameters.
    def setupParameters(scriptOp):
    	page = scriptOp.appendCustomPage('Custom')
    	page.appendFloat('Slidera')
    	page.appendFloat('Sliderb')
    	return
    
    def cook(scriptOP):
    	scriptOp.clear()
    	print(scriptOp.par.Slidera)
    	print(scriptOp.par.Sliderb)
    	return
    
[/code]

## Editing Custom Parameters

Custom parameters are instances of the [Par Class](<./Par_Class.md> "Par Class") and as such can be modified using the [Par Class Members](<./Par_Class.htm#Members> "Par Class"). 

For example, the following script is used to create 2 float parameter sliders with the labels 'Value0' and 'Value1': 
[code] 
    #create 2 float parameters on the Base COMP node called base1
    baseOp = op('base1')
    newPage = baseOp.appendCustomPage('Custom')
    newPar = newPage.appendFloat('Valuea', label='Value A')
    newPar = newPage.appendFloat('Valueb', label='Value B')
    
[/code]

  
All the attributes of the parameters are editable after the fact by accesing the [Par Class](<./Par_Class.md> "Par Class"). For example, the script below changes the labels of the two float parameter sliders to 'Float Slider 1' and 'Float Slider 2': 
[code] 
    # edit the labels on the 2 float parameters on the Base COMP node called base1
    baseOp = op('base1')
    baseOp.par.Valuea.label = 'Float Slider A'
    baseOp.par.Valueb.label = 'Float Slider B'
    
[/code]

  
The scripting names assigned to the parameters can be changed to 'Floatsliderx' and 'Floatslidery', as well using the script below: 
[code] 
    #edit the labels on the 2 float parameters on the Base COMP node called base1
    baseOp = op('base1')
    baseOp.par.Valuea.name = 'Floatsliderx'
    baseOp.par.Valueb.name = 'Floatslidery'
    
[/code]

## Deleting Custom Parameters

Custom parameters can be removed by calling the parameters destroy method as such: 
[code] 
    # this will remove the custom parameter called 'Speed' from the Base COMP 'base1'
    baseOp = op('base1')
    baseOp.par.Speed.destroy()
    
[/code]

or by removing all custom parameters from an [Operator](<./Operator.md> "Operator"): 
[code] 
    # this will remove all custom parameters from the Base COMP 'base1'
    baseOp = op('base1')
    baseOp.destroyCustomPars()
    
[/code]

## Enabling and Disabling Custom Parameters

Custom Parameters can be set to an Enabled or Disabled state using the following script: 
[code] 
    # create a pulse button parameter on the Base COMP node called base1
    baseOp = op('base1')
    newPage = baseOp.appendCustomPage('Controls')
    newPar = newPage.appendPulse('Startsearch', label='Click to start search')
    
    # disable the pulse button
    baseOp.par.Startsearch.enable = False
    
    # enable the pulse button
    baseOp.par.Startsearch.enable = True
    
[/code]

You can use a Parameter Execute DAT to watch another parameter, and when it changes, alter the enable state of the parameter. 

## Sorting Custom Parameters

Custom parameters can be reordered on one [Parameter Page](<./Parameter_Dialog.htm#Parameter_Pages> "Parameter Dialog") as follows: 
[code] 
    # assuming the Base COMP 'base1' has 3 custom parameters displayed in this order 'Color', 'Speed', 'Value'
    baseOp = op('base1')
    page = baseOp.customPages[0]  #assume on first page
    page.sort('Speed','Color','Value')
    
[/code]

If the parameters are not on the same page, the order will not be affected. 

## Moving Parameters between Pages

Custom parameters can be moved between [Parameter Pages](<./Parameter_Dialog.htm#Parameter_Pages> "Parameter Dialog") by just assigning a new value to their`page`member. The moved parameter preserves all of its attrbutes, including all of its members, such as`min`,`max`, and`default`values. All parameters in a tuplet are displayed on the same page. 
[code] 
    #create a parameter on page 'Car Controls'
    baseOp = op('base1')
    p = baseOp.par.Size
    p.page = 'Car Spec'  #other parameters in tuplet will follow.
    
[/code]

## Deleting Custom Parameter Pages

A custom [Parameter Page](<./Parameter_Dialog.htm#Parameter_Pages> "Parameter Dialog") is deleted when by calling its destroy method directly. 
[code] 
    baseOp = op('base1')
    page = baseOp.customPages[0]
    page.destroy()
    
[/code]

## Reordering Custom Parameter Pages

Custom [Parameter Pages](<./Parameter_Dialog.htm#Parameter_Pages> "Parameter Dialog") can be reordered by specifying the new order: 
[code] 
    baseOp = op('base1')
    baseOp.sortCustomPages('Car Controls', 'Car Spec')
    
[/code]

## List Custom Parameters

A list of all [Custom Parameters](<./COMP_Class.htm#Custom_Parameters> "COMP Class") added to an Operator can be returned using the method`customPars`. The list is ordered by their appearance in the [Parameter Dialog](<./Parameter_Dialog.md> "Parameter Dialog"): 
[code] 
    baseOp = op('base1')
    baseOp.customPars
    
[/code]

## List Custom Parameter Pages

A list of all [Custom Parameters](<./COMP_Class.htm#Custom_Parameters> "COMP Class") Pages added to an Operator can be returned using the method`customPages`. The list is ordered by their appearance in the [Parameter Dialog](<./Parameter_Dialog.md> "Parameter Dialog"): 
[code] 
    baseOp = op('base1')
    baseOp.customPages
    
[/code]

## Access Custom Parameters from Inside Network

When in a component containing custom parameters, right-click on the network and select Open Parent Parameters. 

## Using Custom Parameter Values

Once created, Custom Parameters function the same as any built-in parameter of the same type. There are a number of ways to access the values of a parameter, including Custom Parameters. 

The first is directly, within a component, with an expression like`parent().par.Length`. 

The second is through the use of the [Parameter CHOP](<./Parameter_CHOP.md> "Parameter CHOP"). The [Parameter CHOP](<./Parameter_CHOP.md> "Parameter CHOP") will fetch custom parameters and standard parameters by category or name patterns from the Component being referenced. This will create a CHOP channel from each parameter selected. 

The third method is through the use of the [Parameter Execute DAT](<./Parameter_Execute_DAT.md> "Parameter Execute DAT"). This DAT provides Python callback functions for the parameters referenced by it. 

## Custom Parameter in Clones

We are referring here to parameters on the clones of components that have their Clone parameter set, not parameters inside these clones. 

Normally, custom parameter attributes, like label, default value, max/min and menu entries, propagate to all clones. This feature can be turned off by setting a custom parameter's **`styleCloneImmune`** property to True. 

Parameters' current value and their [Parameter Mode](<./Parameter_Mode.md> "Parameter Mode") **do not** propagate to all clones. They remain unique for each clone, like any other parameter or [Flag](<./Flag.md> "Flag") of the master node. 

The parameter order propagates to clones automatically. The page order propagates to clones automatically. 

## References

For a list of parameter attributes (members) and settings: [Par Class Members](<./Par_Class.htm#Members> "Par Class")

For a list of parameter types and their arguments: [Page Class](<./Page_Class.md> "Page Class")

**Tip: See also** [Internal Parameters](<./Internal_Parameters.md> "Internal Parameters").
