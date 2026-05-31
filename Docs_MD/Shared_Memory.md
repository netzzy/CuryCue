# Shared Memory

Shared Memory can be used between multiple TouchDesigner processes or between TouchDesigner and other 3rd party applications.   
  
The following operators use shared memory and are available in TouchDesigner Educational, Commercial and Pro. 

**Shared Memory Inputs**
* [Shared Mem In TOP](<./Shared_Mem_In_TOP.md> "Shared Mem In TOP")
  * [Shared Mem In CHOP](<./Shared_Mem_In_CHOP.md> "Shared Mem In CHOP")
  * [Shared Mem In COMP](<./Shared_Mem_In_COMP.md> "Shared Mem In COMP")


**Shared Memory Outputs**
* [Shared Mem Out TOP](<./Shared_Mem_Out_TOP.md> "Shared Mem Out TOP")
  * [Shared Mem Out CHOP](<./Shared_Mem_Out_CHOP.md> "Shared Mem Out CHOP")
  * [Shared Mem Out COMP](<./Shared_Mem_Out_COMP.md> "Shared Mem Out COMP")

## Global Shared Memory

For some nodes that use shared memory such as the [Shared Mem Out CHOP](<./Shared_Mem_Out_CHOP.md> "Shared Mem Out CHOP") and [Shared Mem Out TOP](<./Shared_Mem_Out_TOP.md> "Shared Mem Out TOP"), there is a second mode of operation that can be used for how the memory is shared. Normally each node will create it's own memory using the given name, and the data will be updated and retrieved when the node cooks. This means that data can arrive at nodes from different frames, due to them cooking at different times during the frame. 

However sometimes sync is desired between the data is desired. Using Global shared memory allows for this. Under the hood a single large shared memory segment is created by the *Out process, and all of the *Out nodes that send out data will put their data into this segment. On the *In side, that memory is read once per frame, and the data is served out to all the *In nodes. This way all of the *In nodes will always recieve data from the same frame coming from the *Out process. 

Since a global shared memory segment is used, only one *Out process on a machine can be using Global shared memory, since it uses a custom name that will conflict with another process if that other process also tries to use Global shared memory.
