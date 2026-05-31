# Parameter

Every operator in TouchDesigner has a set of control Parameters that can be integer or floating point numbers, menus, binary toggles, text strings or operator [paths](<./Network_Path.md> "Network Path"), which determine the output of the operator. 

The parameter dialog is normally at the top-right of the network editor. Pressing 'p' turns off and on the parameter dialog. The parameter dialog for any operator can be opened by right-clicking on the operator and selecting "Parameters...". 

Parameters in TouchDesigner only exist in [Operators](<./Operator.md> "Operator") (OPs or "nodes"). Parameter types include: 
* numbers, both integer and floating point
  * number pairs, triples or quadruples (e.g. width and height, XYZ position, RGBA color)
  * on-off flags (toggles)
  * menus
  * text strings
  * [paths](<./Network_Path.md> "Network Path") to other nodes in TouchDesigner networks
  * "pulse" buttons that initiate actions like running scripts
  * python objects - any python object that you can make using numbers, True/False values, strings, lists and dictionaries. The python object has to be self-contained - it cannot refer to other operators or parameters, for example.


See the [Component Editor](<./Component_Editor.md> "Component Editor") to create custom parameters and see the range of parameter types that are available. 

### Parameter Modes and Evaluation

Every Parameter can be in one of four modes: Constant Mode, [Expression](<./Expression.md> "Expression") Mode, [Export](<./Export.md> "Export") Mode or Bind ([Binding](<./Binding.md> "Binding")) Mode. An "**evaluated parameter** " is resulting value of the parameter based on its mode, expressions, exports or binds. 

Parameters can be driven by [Python](<./Category-Python.md> "Category:Python") expressions when the [Parameter Mode](<./Parameter_Mode.md> "Parameter Mode") is in Expression Mode. 

**TIP** : Pressing ctrl-e/Cmd+e with the cursor in a parameter brings up the current parameter’s expression in your text editor, making it easier to see and edit long expressions. 

Parameters can be driven by [CHOPs](<./CHOP.md> "CHOP") by [Exporting](<./Export.md> "Export") CHOP channels to a parameter, putting the parameter in [Export Mode](<./Parameter_Mode.md> "Parameter Mode"). In the example Parameter Dialog below, the Y-Translate parameter is being controlled via a CHOP channel export. This is indicated by the green color of the parameter in the dialog (think green for CHOPs!). 

Parameters can be bi-directionally synced to other parameters and CHOP channels using [Binding](<./Binding.md> "Binding"). The parameter will go into [Bind Mode](<./Parameter_Mode.md> "Parameter Mode"). 

**IMPORTANT** :`op('pattern1').par.phase`is the python [parameter object](<./Par_Class.md> "Par Class") which usually gets converted to an evaluated value for you, like when you use it in a parameter expression. More safely, especially when using a parameter in scripts, use`op('pattern1').par.phase.eval()`, which always gives you the final evaluated value. 

### Parameter Attributes

Parameters have numerous other attributes, some are parameter type-dependent. 
* name (internal python name you see when you roll over the parameter)
  * label
  * default value
  * minimum, maximum, clamp low, clamp high, clamp low value, clamp high value (for integers and floats)
  * menu entries
  * enable flag and enable expression (determines if you can access the parameter - usually means it it not relevant in the current state of other parameters)
  * read-only - the parameter is active and evaluating but you can't hand-edit it until you turn off read-only
  * section divider - in UI a line appears after the prior parameters

### Custom Parameters

Custom Parameters are user created parameters which can be added to [Components](<./Component.md> "Component"), [Custom Operators](<./Custom_Operators.md> "Custom Operators"), and Script Operators ([Script TOP](<./Script_TOP.md> "Script TOP") / [Script CHOP](<./Script_CHOP.md> "Script CHOP") / [Script SOP](<./Script_SOP.md> "Script SOP") / [Script DAT](<./Script_DAT.md> "Script DAT")). In the case of Components and Script Operators, you can create/edit/delete them in the [Component Editor](<./Component_Editor.md> "Component Editor"). 

For more information see [Custom Parameters](<./Custom_Parameters.md> "Custom Parameters"). 

### Internal Parameters

See [Internal Parameters](<./Internal_Parameters.md> "Internal Parameters")

### Sequential Parameters

See [Sequential Parameters](<./Sequential_Parameters.md> "Sequential Parameters")

See also: [Parameter Python Class](<./Par_Class.md> "Par Class"), [Parameter Dialog](<./Parameter_Dialog.md> "Parameter Dialog"), [Parameter Mode](<./Parameter_Mode.md> "Parameter Mode")
