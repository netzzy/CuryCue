# Binding

Binding is a [Parameter Mode](<./Parameter_Mode.md> "Parameter Mode") that ties two or more parameters' values together, where changing the value of any one of the bound parameters changes all of them. The actual value is stored in one place, whichever value is at the top of the bind chain, called the **bind master**. Parameters can be **bind references** , bind masters, or both.   
  
**Table cells** , **[Bind CHOP](<./Bind_CHOP.md> "Bind CHOP") channels**, [Panel Values](<./Panel_Value.md> "Panel Value"), and [Dependency objects](<./Dependency_Class.md> "Dependency Class") can also be bound with parameters, but can only be bind masters because they have no place to set a bind expression. 

A **bind chain** is a tree of interconnected values that are linked by binding. A bind master can have multiple bind references, each of which can also be the bind master for other parameters. In other words, you can have one or more bind references bound to one bind master, and you can also set up a chain where parameter C is the bind reference of parameter B, which is the bind reference of parameter A. 

A **bind reference** is a parameter in a fourth "Bind" [Parameter Mode](<./Parameter_Mode.md> "Parameter Mode"), and will show up as purple text in parameter dialogs. A bind reference's **bind expression** will resolve to its master. It can only be changed via its UI, its`val`property, or its bind master. A bind reference does not use its constant, expression or export parameter modes. 

The **bind master** is at the top of the bind chain and holds the current value. A **Bind master parameter** can have exports and expressions and generally works like any other parameter, but its value can also be changed indirectly by the bind references. **Note:** If a bind master parameter is changed by its references, it will enter Constant [Parameter Mode](<./Parameter_Mode.md> "Parameter Mode"). 

**Bind master table cells** can be changed by changing the cell value or bind reference parameter values. **Bind master channels** , only available on the [Bind CHOP](<./Bind_CHOP.md> "Bind CHOP"), can be changed by changing the CHOP's channel inputs or by changing the bind reference parameter values. 

To **bind to a Text DAT'**s body of text see "Binding Other Object Attributes" below. 

## Setting Up by Using Bind Expressions

To set up bind references, set a parameter's [Parameter Mode](<./Parameter_Mode.md> "Parameter Mode") to Bind, then add a **bind expression** that points to the bind master, like`op('lfo1').par.phase`. The bind expression is accessed by expanding the parameter and typing into the lower entry field. The upper text entry area (available in some parameters) is used for changing the parameter's actual value, similar to constant mode. Setting up binding to **table cells** or **bindCHOP channels** is similar. Enter an expression to the object in the bind expression, e.g.`op('table1')[0,0]`or`op('bind1')['chan1']`. 

You can also set the bind expression using python:`Par.bindExpr = string`## Setting Up by Dragging

You can also set up binding between parameters by dragging. To bind parameters using the mouse, always drag the **bind master** to the **bind reference**. Drag the parameter name from the bind master's parameter dialog into the parameter name or entry field of the bind reference parameter. In the case of multi-value parameters, drag the name of the bind master onto the name of the bind reference. Once you have done this, select **Bind** from the popup menu that appears. 

## Binding Custom Menu Parameters

When binding a custom menu parameter to another menu parameter, you will usually want to duplicate the options in the other menu. This is easily achieved using the`menuSource`member. Using the [Component Editor Dialog](<./Component_Editor_Dialog.md> "Component Editor Dialog") (or Python), write an expression in the custom parameter's`menuSource`that points to the parameter whose menu you want to duplicate. **Note:** this is done automatically when you drag a menu parameter into the Component Editor's parameter area and choose a bind or reference option in the pop-up menu. 

## Binding Other Object Attributes and Properties (bind tuples)

You can also bind to **named object attributes** like the text of a [Text DAT](<./Text_DAT.md> "Text DAT"). The expression format is a 2 part tuple, called a bind tuple, in the format:`(object, attribute)`for example:`(op('text1'), 'text')`, or`(op('box1'), 'nodeY')`. 

An advanced feature of this type of binding is that it will use **Python property** setter functions properly. If you use a Python property to return a dependable object (like a parameter or a tdu.Dependency object), using dot notation in the bind expression will skip the property accessor and change the returned object directly when a change is made to the parameter. Using the bind tuple notation will use the property's setter function when the bind value changes. 

**Note:** this only works bi-directionally with attributes that are [Dependable](<./Dependency.md> "Dependency"). If you find a TouchDesigner attribute you need to bind to that is not dependable, please post in the forums. 

## Binding to`None`When bind expressions evaluate to None they always return None. This can help to deal with certain difficult error states. For example, if you want to bind to`/geo1`'s`tx`parameter but you aren't sure that`/geo1`exists, you could use this bind expression:`op('geo1').par.tx if op('geo1') else None`. 

## Chained Binds Example

In this image, the`Text`parameter on a textTOP is bound to a cell in table1. The constantCHOP's`name0`parameter is then bound to the textCOMP's`text`parameter, creating a chain of binds. Changing any of these values will change all of them. 

## Many-To-One Binds Example

In this image, all of the constantTOP's`color`parameters are bound to the bindCHOP's single channel. The lfoCHOP's`frequency`parameter is also bound to the bindCHOP's channel. This creates a many-to-one binding. Again, changing any of these values will change all of them.
