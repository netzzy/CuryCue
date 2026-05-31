# Drag-and-Drop

TouchDesigner supports Drag-and-Drop functionality as a shortcut to complex import/export and copy/paste functionality. Drag-and-Drop functionality allows you to: 
* Import [TouchDesigner-readable files](<./File_Types.md> "File Types").
  * Export data from TouchDesigner nodes to external applications.
  * Copy and/or move nodes from one TouchDesigner network to another.
  * Add TouchDesigner-readable file(s), Panel components or TouchDesigner nodes to open control panels.


[Panel Components](<./Panel_Component.md> "Panel Component") have options for Drag and Drop on their _Drag/Drop_ page of parameters. These parameters can be used to inherit the Drag/Drop settings from the panel's parents, or to force Drag/Drop on or off. 

# Drag/Drop Callbacks

To create custom drag/drop systems for your UI, you can use Python Drag/Drop callbacks with all [Panel Components](<./Panel_Component.md> "Panel Component"). All parameters for this are on the **Drag/Drop parameter page**. Once you set your panel to`Use Drag/Drop Callbacks`in either the`**When Dragging This**`or the`**On Dropping Into**`parameter, you can press the **Add** button in the`Drag/Drop Callbacks`parameter to create a default callbacks DAT. Edit this DAT to set up your custom Drag/Drop behavior. These callbacks are called when the user drags or drops on the component's displayed panel, _not_ the component's network node, so to test in a network the node viewer must be active. 

To create a single Drag/Drop callbacks DAT for a network of panels, it is useful to note that the`Use Parent's Drag/Drop Settings`menu choices will cause panels to use the first Drag/Drop callbacks found above them in the hierarchy. Because the originating panel component that received a drag or drop operation is always passed in as an argument, different behaviors can be set up for different panels. 

[Click here for migration guide from pre-2020.46450 builds](<./Python_Drag/Drop_Experimental_Migration.md> "Python Drag/Drop Experimental Migration")

## Setting Up A Draggable Panel

To use the callback system to create a draggable panel, first be sure the`When Dragging This`parameter on your component is set to`Use Drag/Drop Callbacks`. Next, you will use the`onDragStartGetItems`callback to tell the system what item or items will be dragged when the user clicks and drags on the panel. After the drag is complete, you will receive an`onDragEnd`callback in which you can script any further actions to be taken. 

####`onDragStartGetItems(comp, info)`→`list of items to drag`Called when information about dragged items is required. 

  *`comp`\- the clicked-on panel
  *`info`\- A dictionary containing all info about drag


    **You must return a list of items from the callback to start a drag operation.** An item is whatever you want TouchDesigner to drag. Commonly this is an OP, a parameter, or a CHOP channel, but you can put any Python object you like in the item list.

    **Example`onDragStartGetItems`callback code**`return [comp]`drags the panel operator itself`return [comp.parent()]`drags the panel's parent`return [op('custom1'}, op('custom2')]`drags two operators`return [comp.par.x]`drags the panel's x parameter`return [op('myCHOP')['speed']]`drags a CHOP's`speed`channel.

####`onDragEnd(comp, info)`Called when a drag action ends. 

  *`comp`\- the clicked-on panel
  *`info`\- A dictionary containing all info about drag, including:


    accepted: True if the drag was accepted
    dropResults: a dict of drop results. This is the return value of onDropGetResults
    dragItems: a list of objects being dragged over comp

    This callback can be used if you need to take special actions after a drop has occurred.

## Setting Up A Panel As A Drop Target

To use the callback system to set up dropping onto a panel, start by making sure the`On Dropping Into`parameter on your component is set to`Use Drag/Drop Callbacks`. The first step in receiving a drop is determining whether the panel can accept the items being dragged over it (a.k.a. hovering) using the`onHoverStartGetAccept`callback. If an acceptable item is dropped onto the panel, you can then use the`onDropGetResults`callback to react to the drop. The`onHoverEnd`callback can be used to script any actions to be taken when items are dragged into _and then back out of_ the panel's area. This would most often be used to turn off any visual hover indicators. 

### Examples of testing`dragItems`in callbacks
[code] 
    	# test the number of drag items by testing the length (len)
    	if len(info['dragItems']) == 1:
    		debug('Received one dragged item only')
    
    	# test if the first drag item is an operator using isinstance
    	if isinstance(info['dragItems'][0], OP):
    		debug('First dragged item is an operator')
    	# useful classes to test:
    	#	OP: operator
    	#	COMP, TOP, CHOP, SOP, MAT, DAT: operator families
    	#	panelexecDAT, containerCOMP etc.: specific operator types
    	#	Channel: CHOP channel
    	#	Par: parameter
    	#	tdu.FileInfo: file
    
    	# test if the type of ALL drag items is DAT by using all, list comprehension, and isinstance
    	if all([isinstance(item, DAT) for item in info['dragItems']]):
    		debug('All dragged items are DATs')
    
[/code]

####`onHoverStartGetAccept(comp, info)`→`True if drag items are acceptable`Called when comp needs to know if dragItems are acceptable as a drop. You must return True if you want to accept`dragItems`for dropping. 

  *`comp`\- the dropped on panel
  *`info`\- A dictionary containing all info about hover, including:


    dragItems: a list of objects being dragged over comp

    The easiest way to see this in action is to use the following code in this callback and watch the textport when you drag various items over your panel:`debug('\nonHoverStartGetAccept', comp.path, '\n\t', info)`####`onHoverEnd(comp, info)`Called when dragItems leave comp's hover area. 

  *`comp`\- the dropped on panel
  *`info`\- A dictionary containing all info about hover, including:


    dragItems: a list of objects being dragged over comp

####`onDropGetResults(comp, info)`→`dict of results`Called when comp receives a drop of dragItems. This will only be called if onHoverStartGetAccept has returned True for these dragItems. 

  *`comp`\- the dropped on panel
  *`info`\- A dictionary containing all info about drop, including:


    dragItems: the list of objects being dropped on comp

    Returning a dictionary of items from this function is optional, but allows you to set up cross-communication between drag sources and drop targets. The dictionary should have results with descriptive keys. The following key/value pairs are standard and should be used when possible: 

  *`'createdOPs':[<list of created ops in order of corresponding drag item>]`## Getting Panel Location (u/v) of a Drop

If you want to know where exactly in a panel something was dropped, you can access`comp.panel.dragrollu`and`comp.panel.dragrollv`in the callbacks. You can also use a [Panel CHOP](<./Panel_CHOP.md> "Panel CHOP") to track these values continually. 

# Legacy Drag/Drop System

## How Component Drag-and-Drop Works
* Anything dropped into a network that Allows Drop will be handled by the Network's Drop Script, regardless of whether you are dropping onto a node viewer, a control panel view, or a network editor in either list view or node view. No menu will popup.
  * By default, Components **Do Not Allow Drop**.
  * If a Component Does Not Allow Drop, you will only be able to drop things into it via the network editor list or node view. A menu may popup to give you a list of options.
  * If the node being dropped has a Dropped Component or Drop Destination Script, then the Move option will not be available.
  * A node that has a Dropped Component or Drop Destination Script will still drop as itself if you drop it onto parameters or [Text DATs](<./Text_DAT.md> "Text DAT"). It will also save as a *.tox of itself if you drop it onto a windows desktop or folder.

## Drop Scripts - Text

A component's Drop Script would get run when you drop another component or an external file into that component. 

Each component network can be set to allow dragging-and-dropping. In a component's parameter dialog, there is a Drag tab where you can modify the settings. You can set a components to use its parents settings, or to use custom scripts. By default, the settings of the root folder for Dragging is **Do Not Allow Drag** and for Dropping **Do Not Allow Drop** , with the default Drop Script specified at`/sys/drop`. 

To set up your own Drop Script, set your component's parameter Drop to Allow Drop, and enter the path for the [DAT](<./DAT.md> "DAT") specifying your Drop Script onto the Drop Script parameter. This DAT will be executed whenever something is dropped onto this component. The parameters passed to the Drop Script in Python are: 

  *`args[0]`\- dropped node name, CHOP channel or file name, depending on what is dropped
  *`args[1]`\- x position in network coordinates when the mouse was released
  *`args[2]`\- y position in network coordinates when the mouse was released
  *`args[3]`\- the number of the item being dropped
  *`args[4]`\- the total number of items being dropped
  *`args[5]`\- the operator type or file extension
  *`args[6]`\- the fullpath of the network or node the node or channel was dragged from, or the parent directory
  *`args[7]`\- the network accepting this drop

## Drop Script \- Tables

If you want to process individual node types or file types, you can use a drop table. Specify a Table DAT in the drop script field. TouchDesigner will automatically look for 2 columns in the table. The first column should indicate the data type and the second should indicate the Text DAT that holds the script to process that data type. TouchDesigner will call the script for each data and with the above parameters. Here is a sample drop table: 
[code] 
     chop      chop_script        handle CHOP nodes
     sop       sop_script         handle SOP nodes
     channel   channel_script     handle channel data
     cmd       cmd_script         runs a .cmd file
     tox       tox_script         loads a .tox file
    
[/code]

Columns are not limited to two, but only the first two columns will be used to process drops. 

## Drag Scripts

You can specify whether a component is allowed to be dragged. The default settings for root is Do Not Allow Drag. This means that you cannot click on the control panel view of a component and drag it to a network you can drop in. However, you will still be able to drag the Node View of that component and drop it. 

The parameters passed to the Drag Script in Python are: 

  *`args[0]`\- dragged operator name
  *`args[1]`\- the index of the operator dragged
  *`args[2]`\- the total number of operators being dragged
  *`args[3]`\- operator type
  *`args[4]`\- parent path of dragged operator


There are a couple of ways to modify what operator will be dropped when you drag a Component. The Dropped Component parameter is the easiest way to specify an alternative operator to drop. Note that this alternative operator must exist, otherwise the component itself will be dropped. The alternative is only used when dropping onto a network or control panel. Text pasted via dragging and dropping, or files saved via dropping onto the desktop, will still use the original. 

## Drop Destination Scripts

A more flexible way to specify alternatives to drop, is to use the Drop Destination Script. If a Drop Destination Script is specified, a temporary network is created and the component (or the alternative operator specified in Dropped Component) is copied to this network. You can add or modify operators in this network. 

Then _**echo**_ a list of paths. TouchDesigner will look at the list of paths output by this script, and will copy them to the dropped network. A node path is specified relative to the current component when the script exits. If a node cannot be found for a string, TouchDesigner will assume that it is a file and dropped the string as a file into the drop network. 

The arguments for the Destination Drop Script are: 

  *`arg[0]`\- full path of script
  *`arg[1]`\- copy of component (or alternative operator specified in parameter Dropped Component)
  *`arg[2]`\- full path of temporary network (in /sys)
  *`arg[3]`\- name of component (or alternative operator specified in parameter Dropped Component)
  *`arg[4]`\- full path of component parent (where the drag came from) (or alternative operator parent)
  *`arg[5]`\- operator type of copy

## Drop Types

By default, dragging a component drops operators or file paths. If a drop destination script is specified, you can also add a DAT table with a list of return types that the drop destination script will provide. Return types can be one of the op types ([COMP](<./Component.md> "Component"),[TOP](<./TOP.md> "TOP"),[CHOP](<./CHOP.md> "CHOP"),[SOP](<./SOP.md> "SOP"),[MAT](<./MAT.md> "MAT"),[DAT](<./DAT.md> "DAT")), channel, or supported [filetypes](<./File_Types.md> "File Types"). For example, a DAT table containing just 
[code] 
     jpg
     tiff
     top
    
[/code]

will only let the component being dropped into know that it will only provide those 3 types. If the component being dropped into has a table of types and corresponding scripts, then you will only be able to drop if there is a matching type. i.e., if the drop script table looks like this: 
[code] 
     top      top_script
    
[/code]

then only tops supplied by the drop destination script will be accepted by the component. 

See also [File Types](<./File_Types.md> "File Types")
