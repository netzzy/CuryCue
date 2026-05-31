# ProgressiveUnloader Class

The`ProgressiveUnloader`class describes a specific instance of the`COMP.progressiveUnload()`[method](<./COMP_Class.htm#progressiveUnload> "COMP Class") of a [COMP](<./COMP_Class.md> "COMP Class"). Methods and members of this class are used to obtain progress information about the underway progressive unload operation, or modify it. 
[code] 
    n = op('comp1')
    
    # Check if comp1 is progressively unloading
    n.progressiveUnloader.active
    
    # Get the total number of frames since comp1 has been progressively unloading
    n.progressiveUnloader.elapsedFrames
    
    # Terminate comp1's progressive unloading
    n.progressiveUnloader.kill()
    
[/code]  
  
## Members`active`→`bool`**(Read Only)** : 

> Returns true if progressive unloading is underway`remainingNodes`→`float`**(Read Only)** : 

> Returns the remaining nodes to be unloaded. Returns 0 if`progressiveUnload()`has not been called at all for this component`nodesUnloaded`→`float`**(Read Only)** : 

> Returns the number of unloaded nodes. Returns 0 if`progressiveUnload()`has not been called at all for this component`lastFrameUnloadTime`→`float`**(Read Only)** : 

> Returns the unload time (in milliseconds) of the latest frame. Returns 0 if`progressiveUnload()`has not been called at all for this component`averageFrameUnloadTime`→`float`**(Read Only)** : 

> Returns the average unload time (in milliseconds) across all previous frames. Returns nan if`progressiveUnload()`has not been called at all for this component`gpuMemUnloaded`→`float`**(Read Only)** : 

> Returns the total gpuMemory (in MB) that has been unloaded. Returns 0 if`progressiveUnload()`has not been called at all for this component`elapsedFrames`→`float`**(Read Only)** : 

> Returns the elapsed frames since progressive unloading started. Returns 0 if`progressiveUnload()`has not been called at all for this component

## Methods`kill()`→`None`: 

> Terminate the progressive unloading operation.

TouchDesigner Build: Latest\nwikieditorwikieditor
