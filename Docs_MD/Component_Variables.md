# Component Variables

## Component Variables

Component [variables](<./Variables.md> "Variables") are created local to any component, are usable anywhere in the component, and only in that component. 

They are usually used with [Tscript](<./Tscript.md> "Tscript") but can be used with Python, though in Python, properties in [Extensions](<./Extensions.md> "Extensions") are more flexible. 

In Python, you would use the`var('VARNAME')`expression to fetch a component variable. Setting them in python is difficult, something like`op('../../local/set_variables')['varname',1] = value`. 

In Tscript, use the TScript:`cvar`command to create, list and delete component variables. Component variables for any component can be viewed in the [Variables Dialog](<./Variables_Dialog.md> "Variables Dialog"): Drag the component you want and drop it on the Variables dialog, this will create a tab displaying the component's local variables if any exist. 

Component variables are evaluated hierarchically in TouchDesigner's networks. If a component variable is referenced and it is not defined in the local component, then it will search the parent component for the variable. This will continue until the variable is found or it reaches the top of the network hierarchy,`/`, the root. 

How component variables work internally: Component variables are stored inside a [Base COMP](<./Base_COMP.md> "Base COMP") called`local`inside the component. The variables are defined inside`local`in a table DAT named`variables`. This DAT is fed by a [Table DAT](<./Table_DAT.md> "Table DAT") called`set_variables`, which is the DAT that the commands (TScript:`cvar`,`rvar`) use to insert variables in. This allows tables of other variables to be merged into`variables`. The TScript: **`cvar`** command can be used to list, set, or unset component variables. 

NOTE: Root variables are simply component variables set at the root of the hierarchy,`/`.
