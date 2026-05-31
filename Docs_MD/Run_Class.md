# Run Class

The Run class describes a single instance of a delayed script execution. See [Run Command Examples](<./Run_Command_Examples.md> "Run Command Examples") for more info. They can be accessed from the [runs](<./Runs_Class.md> "Runs Class") object. Scripts can be executed with delays with the following methods: 
[code] 
    DAT.run()
    Cell.run()
    td.run()
    
[/code]

## Members`active`→`bool`: 

> Get or set whether or not this script will execute once its target frame is reached.`group`→`str`: 

> Get or set the group label associated with this script.`isCell`→`bool`**(Read Only)** : 

> Returns true when the source is a [cell](<./Cell_Class.md> "Cell Class"), from a Cell.run() call.`isDAT`→`bool`**(Read Only)** : 

> Returns true when the source is a [DAT](<./DAT_Class.md> "DAT Class"), from a DAT.run() call.`isString`→`bool`**(Read Only)** : 

> Returns true when the source is a string, from a td module run() call`path`→`OP`**(Read Only)** : 

> The [operator](<./OP_Class.md> "OP Class") location from which this script will execute.`remainingFrames`→`int`: 

> Get or set the remaining number of frames before the execution will occur.`remainingMilliseconds`→`int`: 

> Get or set the remaining number of milliseconds before the execution will occur.`source`→`DAT | Cell | str`**(Read Only)** : 

> The source of the run. It will be either a [DAT](<./DAT_Class.md> "DAT Class"), [cell](<./Cell_Class.md> "Cell Class"), or string.

## Methods`kill()`→`None`: 

> Kill this run before it executes, and remove it from the global runs list, located in the [td Module](<./Td_Module.md> "Td Module").

TouchDesigner Build: Latest\nwikieditor2021.100002018.28070before 2018.28070
