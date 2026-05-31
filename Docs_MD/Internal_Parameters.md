# Internal Parameters

[Parameters](<./Parameter.md> "Parameter") are a powerful way to hold data in TouchDesigner. But putting parameters on the top level of a [component](<./Component.md> "Component") that are only used inside makes the component messy. “Internal Parameters” provide a simple shortcut to parameter collections that you create within a component, accessible from anywhere in that component. They act like "persistent local variables". 

## Simplest Procedure

Most simply, right-click on a network background and select Create Internal Parameters.... You pick a shortcut`_Name_`. (By default it's the Parent Shortcut name, if it exists, or "`Local`".) When you press Apply it creates a Base COMP in your network (called`ipar _Name_`) where you can add a collection of custom parameters. When you add a parameter`_Parname_`to the Base COMP, then anywhere in your network you can refer to it with an expression like`ipar._Name_._Parname_`. 

(This is set it up on the Common page of the parent component where the shortcut name and the path to the Base COMP are found in Internal OP Shortcut 1 and Internal OP 1.)`ipar._Name_`searches up in the parent components' hierarchy until it finds a component with a matching Internal OP Shortcut name. From there it finds the Base COMP that holds the set of parameters. 

See also [Internal Operators](<./Internal_Operators.md> "Internal Operators"). 

## Manual Procedure

Go inside any component, say`/project1`of a default TouchDesigner. Create a [Base Component](<./Base_COMP.md> "Base COMP"), and name it`iparEffect`. 

On`iparEffect`create a Float [Custom Parameter](<./Custom_Parameters.md> "Custom Parameters") and name it`Size`. 

Go to the parameters of`/project1`, to the Common page. Name your internal shortcut by setting Internal OP Shortcut 1 to`Effect`. 

Give the path to the new Base Component by setting Internal OP 1 to`./iparEffect`. 

The base component's parameters are now easy to get and set within your component: 

Go back in`project1`and create a Circle SOP. In its Radius parameters put`ipar.Effect.Size`. 

Change the Size parameter on`iparEffect`. The expression on the Circle SOP updates correctly. 

To set the Size parameter in a python script, create a Text DAT and in it put:`ipar.Effect.Size = 1.7`On the Text DAT, turn off Viewer Active, and on the node rclick -> Run Script. The Size parameter on`iparEffect`will change to`1.7`. 

## Rationale

Holding values inside a component as parameters has advantages versus holding values in tables, Constant CHOPs, [Extensions](<./Extensions.md> "Extensions") or [Storage](<./Storage.md> "Storage"), as discussed in Pros and Cons below. Internal Parameters are simple to use, and can reduce or eliminate the need to write code in extensions. And by creating parameters inside your component, they are not needlessly exposed outside. See also [Internal Operators](<./Internal_Operators.md> "Internal Operators") or iOPs. 

## Recommendation

Name your internal parameter extension something meaningful. If it's a bin of movies, make the [Parent Shortcut](<./Parent_Shortcut.md> "Parent Shortcut") parameter be called`Bin`, and the internal parameter name be also`Bin`. 

Like any parameter, if an internal parameter is a path to an operator, you have to write, for example,`op(ipar.Effect.Oppath)`or`ipar.Effect.Oppath.eval()`. Otherwise you generally don't need`.eval()`. 

To easily see your evaluated parameters in the network, put a Parameter DAT in the Base COMP and put`./parameter1`in the Base COMP's OP Viewer parameter. The viewer will now show the Parameter DAT's table of parameters. 

To see where an internal parameter comes from when it appears in a parameter expression, select the text`ipar.Effect`and put your cursor over the parameter label. It will reveal its path. 

## Discussion - Where you can Hold and Modify Data in TouchDesigner

To review, there are already several ways to hold data internally in TouchDesigner: 
* text strings located in [Table DAT](<./Table_DAT.md> "Table DAT") cells and [Text DATs](<./Text_DAT.md> "Text DAT")
  * pre-existing parameters (on [Constant CHOP](<./Constant_CHOP.md> "Constant CHOP"), [Add SOP](<./Add_SOP.md> "Add SOP"), …)
  * [Custom Parameters](<./Custom_Parameters.md> "Custom Parameters") on the outside of components
  * CHOPs, SOPs and TOPs which are "[locked](<./Lock_Flag.md> "Lock Flag")" (and harder to modify)
  * TouchDesigner-python [Storage](<./Storage.md> "Storage") in any Operator
  * TouchDesigner-python [Extension](<./Extensions.md> "Extensions") “Properties”
  * Regular python variables in functions and scripts (these are not persistent after a script runs)
  * data held in [Script CHOP](<./Script_CHOP.md> "Script CHOP"), [Script DAT](<./Script_DAT.md> "Script DAT") and [Script SOP](<./Script_SOP.md> "Script SOP") that generate data
  * Dialogs -> Variables, where you can create variables and access them in python with`var('VARNAME')`. These are simply strings. These variables are not commonly used.
  * Internal Parameters

## Pros and Cons of Internal Parameters

### Benefits
* procedural (changing the parameter causes cooking downstream reliably)
  * easily hand-editable
  * gives good visual feedback - you can see values changing live
  * you can give them easy-to-understand labels
  * their values can be python expressions dependent on other data, and they get evaluated procedurally. These custom parameters can be driven with animated expressions.
  * you can export to them with animated channels
  * there is tight control over data integrity: they have default values, minimum and maximum ranges are imposed, and menus have specific values and labels
  * it can handle multiple data types (strings, True/False booleans, integers, floats, menus, operator paths, python lists)
  * with the new Python parameter type, a parameter can also hold a python list or dictionary, where the elements are simple strings, booleans, ints and floats. (as with all custom parameters, you create Python parameters in the [Component Editor](<./Component_Editor_Dialog.md> "Component Editor Dialog") under rclick -> Customize Component)
  * persistent - they are saved in a`.toe`or`.tox`as regular parameters
  * fewer syntax errors when developing
  * can be used in conjunction with extensions, sometimes replacing extensions
  * less coding, less to learn: You don't need to code python classes in a DAT to define anything.
  * are the same speed as parameters anywhere, and at least as fast as animated numbers in DAT cells.
  * are faster than python code in extensions or callbacks because they are compiled into an optimized executable format. (Roll over a parameter with an expression and you will likely see the word "Optimized" that indicates it is compiled into execution code.)

### Limitations
* In a parameter you cannot easily represent SOP data (points, polygons, primitives, attributes), non-trivial python structures.
  * It has not been possible to manage long lists or large arrays of 1D, 2D or 3D numbers, although now there is the Python parameter type that can hold simple lists, for example.
  * An internal parameter (any parameter) uses more memory than a DAT cell but is the same as any custom parameter.
* The syntax for parameters that are operators is:`op(ipar.Effect.Operatorpath)`. As stated above, in the case where the parameter is not a float, integer, boolean or string, but is an operator (like the path to some node), using`ipar.Effect.Operatorpath`in an expression somewhere may resolve to the parameter object and not the value you intend, so you need to put`op(ipar.Effect.Operatorpath)`. Same with a Python type parameter.

## Getting to ipar from Outside a Component

You may want to get the value of an`ipar`of another component, or you may want a parameter on a component to use an`ipar`of that component. 

Being "internal" this isn't possible with`ipar`. But you can use a member of the component to access it:`COMP.internalParameters[**Name**]`where`_Name_`is the`ipar`name you want.`COMP.internalParameters`is a dictionary of internal parameter shortcuts found on the component. 

See also [Internal Operators](<./Internal_Operators.md> "Internal Operators").
