# Python Drag/Drop Experimental Migration

In TouchDesigner 2020.40k, a new Python drag/drop system was released. During the course of the experimental development, the callback system changed in a non-backwards-compatible manner. 

**This is a guide to moving from the Python Drag/Drop system previous to 2020.46450 experimental release.**

## The Change is in the Callback Arguments

All callback arguments are now in the form **`(comp, info)`**. The`comp`argument is unchanged, but the`info`argument is now a dictionary that contains all the arguments that were previously provided. This allows us to leave the arguments as is and still add useful information to these callbacks as the system becomes more advanced. 

## Steps to Migration

Migrating from the original experimental system is fairly simple. The arguments need to be changed on the functions, and then the info needs to be pulled out of them. 

### 1) Change the arguments

This is simply a matter of replacing the argument text in the function definition with`(comp, info)`. For example: 
[code] 
    def onDropGetResults(comp, info):
    
[/code]

. 

### 2) Get the information out of the`info`dict

This will be different for each callback. The general process is to put the information from the dictionary into their own variables as if they were passed as arguments. Putting in these lines _before any other code_ will make your older callback work again: 
* **`onHoverStartGetAccept`**`dragItems = info['dragItems']`* **`onHoverEnd`**`dragItems = info['dragItems']`* **`onDropGetResults`**`dragItems = info['dragItems']`* **`onDragStartGetItems`**


    

     No code necessary.
* **`onDragEnd`**`accepted = info['accepted']``dropResults = info['dropResults']``dragItems = info['dragItems']`
