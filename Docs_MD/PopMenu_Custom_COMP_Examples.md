# PopMenu Custom COMP Examples

This page contains examples of how to set up a **popMenu** custom component. They assume a basic knowledge of TouchDesigner and Python. 

For full documentation of popMenu, see: [PopMenu Custom COMP](<./Palette-popMenu.md> "Palette:popMenu"). 

## Example 1 - Menu Parameters

In this example we will explore the features available via the popMenu parameters. For more details, see [popMenu parameters](<./Palette-popMenu.htm#Custom_Parameters_-_Pop_Menu_Page> "Palette:popMenu"). 

##### Creating a popMenu

To create a popMenu, drag one from the [Palette](<./Palette.md> "Palette") (Derivative>UI folder) into your network. To test the popMenu, click the Open parameter. You can click the Close parameter or press _esc_ to close the menu. **Note:** the view in the menu node is not always an accurate depiction of the popMenu window, so it is good to open it while testing. 

##### List Item Parameters

To add list items to the popMenu, simply add them to the Python list in the **Items** parameter. To disable items in the list, add them to the Python list in the **Disabled Items** parameter. Disabled items must match those in the Items list exactly. **Highlighted Items** works exactly like Disabled Items, but the item has a highlight color and remains enabled. To create a dividing line after an item, add it to the Python List in the **Dividers After Items** parameters. 

There are a couple options for creating checked items in the popMenu using the **Checked Items** parameter. If you enter a Python list, items in the list will have checks next to them. This method does not allow for creating empty checkboxes, however. For that, use a Python dictionary with keys matching list Items and values of 1 (checked) or 0 (unchecked). 

##### Align and Format Parameters

To adjust the position that the popMenu appears relative to the mouse, use the **Horizontal Align** and **Vertical Align** parameters. The **Align Offset** parameters let you enter a pixel offset to the alignment. 

There are a few basic formatting parameters available as well. The **Columns** parameter can be used to create a multi-column menu. **Note:** if you have more than one column, Dividers After Items, Checked Items, and SubMenus (see examples below) will not be available. The **Borders** parameter turns on and off the outer border of the menu, and the **Max Height** parameter sets the size at which the menu will display a scrollbar. 

## Example 2 - A popMenu Network

In this example, we'll set up a simple network that opens a popMenu above a button when it is pressed. 

##### Creating a popMenu

To create a popMenu, drag one from the [Palette](<./Palette.md> "Palette") (Derivative>UI folder) into your network. For this example, make sure the name of it is _popMenu_. 

##### PopMenu Inputs and Outputs

Setting up a popMenu based on a table is easy. Simply wire it into the input of popMenu. The first column of the table will be used as the popMenu's list items. Other columns will be ignored. To create the example menu, make a single-column [Table DAT](<./Table_DAT.md> "Table DAT") with 4 rows containing: "Test", "Demo", "Trial", "Example". Wire the table into a popMenu. Press the Open parameter to see your menu in action. **TIP:** You can use different Input Table parameter settings for multi-column and labeled input tables. 

  
To get the popMenu's results using a CHOP, wire a [Null CHOP](<./Null_CHOP.md> "Null CHOP") into the popMenu's CHOP output. When the popMenu is opened, before a selection is made, the selected_cell channel's value will be -1. When a selection is made, selected_cell will be the selected item's index. Use the same technique with a [Table DAT](<./Table_DAT.md> "Table DAT") and the popMenu's DAT output to get the selected Item text. The table will be empty before a selection is made. 

##### Opening and Reacting to a popMenu Using a Button

First you'll need a button. Create a [Button COMP](<./Button_COMP.md> "Button COMP") in your network. Change its Width parameter to`100`and its Button Type parameter to`Momentary`. To make the button open your popMenu, create a [Panel Execute DAT](<./Panel_Execute_DAT.md> "Panel Execute DAT") and set its Panel parameter to the new button. Next, enter the following code into the DAT, creating the new`onMenuChoice`function and replacing the default`offToOn`function: 
[code] 
    def onMenuChoice(info):
    	debug(info)
    	debug(info['item'])
    
    def offToOn(panelValue):
    	op('popMenu').Open(callback=onMenuChoice)
    	return
    
[/code]

The`offToOn`callback opens the menu and sets the selection callback to`onMenuChoice`. The`onMenuChoice`function prints all the info sent to the callback, then prints just the most commonly used part of that info, the item string that was selected. For more info about callbacks, see: **[popMenu Callback System](<./Palette-popMenu.htm#Python_Callback_System> "Palette:popMenu")**. 

To test the button menu, open a floating viewer to the button and click it. You will want to use a floating viewer because the node view stretches the button and creates unpredictable menu placement. Your menu opens, but it opens at the mouse location instead of attached to the button. Let's fix that... 

##### Attaching a popMenu to a Button

To attach the popMenu to the button, use the parameters at the bottom of the menu's Pop Menu parameter page. First, set the **Button Comp** parameter to your button. **Note:** although the parameter is called Button Comp because that is its most common use, it can be any panel component. Next, set the **Horizontal Attach** parameter to`Left`and the **Vertical Attach** parameter to`Top`. These define where the menu's align point will be attached. We want to match that op the bottom left of the popMenu, so set the **Vertical Align** parameter to`Bottom`. 

Test the button again. Looks good except it would be nicer if the menu size matched the button's size. Go to the menu's Width parameter and notice that it contains the expression`me.OptimalWidth`. That **OptimalWidth** member contains the size to wrap the menu's text exactly. Just change the Width to 100 to match the button's width. Testing now will give the same result as the image at the top of this example. 

## Example 3 - Simple Selection popMenu Created with Script

In this example we will create a pop-up context menu that lets you select the current node in a TouchDesigner network. Unlike the previous examples, we will create this menu using only script. 

##### The System popMenu

For context pop-up menus, you will generally want to create and open the menu entirely from script. You can use your own popMenu COMP for this, or you can use the **system popMenu** provided in TouchDesigner. If you use the system popMenu, it should be for context menus and other things that will disappear immediately after use, because it can be invoked by other TouchDesigner features. This system popMenu is located at:`**op.TDResources.PopMenu**`##### Creating the Simple Selection Menu

To begin, create a [Text DAT](<./Text_DAT.md> "Text DAT") in a network with some other operators. Enter the following text into it: 
[code] 
    def menuChoice(info):
    	op(info['item']).current = True
    
    menuItems = [child.name for child in parent().children]
    
    op.TDResources.PopMenu.Open(
    		items=menuItems,
    		callback=menuChoice,
    		disabledItems=[me.name],
    	)
    
[/code]

The`**menuChoice**`function is what will be called when a menu selection is made. It simply sets the chosen operator to be the current node in the network. 

The`**menuItems**`list is a list of names of all the nodes in the network with your textDAT. It is created using a Python list comprehension. If you're not familiar with this syntax, there is a good tutorial here: [Python List Comprehension With Examples](<https://www.analyticsvidhya.com/blog/2016/01/python-tutorial-list-comprehension-examples/>). 

The last part of the script opens the actual pop-up menu. It is a call to the **Open** method of the system popMenu. You will recognize most of the arguments as parallels of the parameters on the popMenu COMP. The`**items**`argument holds the list items for the menu. In this case we put the list of names we created in the line above,`menuItems`. The`**callback**`argument takes a Python function that will be used as a callback when a choice is made from the menu. In this case, we want to use the`menuChoice`function at the top of the script. The`disabledItems`argument corresponds to the Disabled Items parameter, and as an example we provide a list with one element, the name of the script operator. For information on other arguments of popMenu's`Open`method, see [popMenu Methods](<./Palette-popMenu.htm#Methods> "Palette:popMenu"). 

To test the script, zoom out to where you can see other nodes in the script's network, then right-click on the textDAT and choose _Run Script_. When you choose an Operator name from the menu, a green box will appear around that Operator, indicating that it is the "current" node. 

## Example 4 - Advanced Selection popMenu

In this example we will expand the previous example to create a pop-up context menu that not only selects a node in a network, but also uses advanced popMenu features to show which node is being rolled over in the menu and which node is currently selected. 

##### Creating the Advanced Selection popMenu Script

Create a [Text DAT](<./Text_DAT.md> "Text DAT") in a network with some other operators. Enter the following text into it: 
[code] 
    def onMenuChoice(info):
    	if info['item'] == 'Close Menu':
    		info['menu'].Close()
    	else:
    		op(info['item']).current = True
    
    def onRollover(info):
    	for child in parent().selectedChildren:
    		child.selected = False
    	if info['item'] == 'Close Menu' or info['item'] is None:
    		return
    	op(info['item']).selected=True
    
    menuItems = [child.name for child in parent().children]
    lastChild = menuItems[-1]
    menuItems.append('Close Menu')
    op.TDResources.PopMenu.Open(
    		items=menuItems,
    		callback=onMenuChoice,
    		disabledItems=[me.name],
    		dividersAfterItems=[lastChild],
    		checkedItems='{child.name: child.current for child in op("' \
    						+ parent().path + '").children}',
    		autoClose=False,
    		rolloverCallback=onRollover
    	)
    
[/code]

Test the code by right-clicking on the textDAT and selecting _Run Script_. Notice that a yellow selection box appears around nodes when you roll over their names in the menu. When you click a node name, it becomes the current node and its name is checked. Click _Close Menu_ to (you guessed it) close the menu. 

This script is a lot to take in, so let's take it in sections... 

##### Selection and Rollover Callbacks
[code] 
    def onMenuChoice(info):
    	if info['item'] == 'Close Menu':
    		info['menu'].Close()
    	else:
    		op(info['item']).current = True
    
[/code]

The`onMenuChoice`function is similar to the one in the previous example, except it adds the _Close Menu_ option. As you can see, creating specific actions for menu choices is as simple as an if/else clause. 
[code] 
    def onRollover(info):
    	for child in parent().selectedChildren:
    		child.selected = False
    	if info['item'] == 'Close Menu' or info['item'] is None:
    		return
    	op(info['item']).selected=True
    
[/code]

The`onRollover`callback uses Operators' _selected_ member to create the yellow box you see around nodes when you roll over menu choices. The`for`loop deselects all the nodes in the network. We then check to make sure we aren't over the _Close Menu_ item or no item at all. Rollover callbacks will be called when the mouse leaves the popMenu, so the item can be`None`! Finally, if the mouse is over a valid item, set the corresponding Operator's`selected`member to True. 

##### Advanced Selection popMenu Setup and Checked Items Expression
[code] 
    menuItems = [child.name for child in parent().children]
    lastChild = menuItems[-1]
    menuItems.append('Close Menu')
    op.TDResources.PopMenu.Open(
    		items=menuItems,
    		callback=onMenuChoice,
    		disabledItems=[me.name],
    		dividersAfterItems=[lastChild],
    		checkedItems='{child.name: child.current for child in op("' \
    						+ parent().path + '").children}',
    		autoClose=False,
    		rolloverCallback=onRollover
    	)
    
[/code]

This part of the script creates the actual menu. As in the previous example, we create a`menuItems`list containing all the sibling nodes of the script. We then store the last member of that list in`lastChild`for use in the`Open`method. Finally, we append "Close Menu" to the list to create that option. 

In the **`Open`** method, we use`menuItems`as the list items. We use the`lastChild`we stored in the`**dividersAfterItems**`argument to create a line between the choices and the _Close Menu_ option. 

The`**checkedItems**`argument contains an expression which will continuously update the checkboxes in the menu. It uses a Python Dictionary comprehension (which you can learn about [here](<http://intermediatepythonista.com/python-comprehensions>)) to create a dictionary keyed by Operator name with data equal to the Operator's`current`member. This has the result of creating an empty checkbox by every Operator name except the "current" operator, which will have a check. **Note:** the`checkedItems`argument will accept a literal dictionary or list as well, but providing an expression causes it to update in real-time. 

The **`autoClose`** argument is False for this menu because it is meant to stay open until _Close Menu_ is selected. Finally, we set the`**rolloverCallback**`argument to the onRollover function we created above. 

## Example 5 - Color Selector popMenu with Sub-Menus

In this example we will create a popMenu with sub-menus that let you choose black or white for the node colors in your network. 

##### Creating the Color Selector popMenu Script

Create a [Text DAT](<./Text_DAT.md> "Text DAT") in a network with some other operators. Enter the following text into it: 
[code] 
    def onMainMenuChoice(info):
    	info['menu'].OpenSubMenu(
    			items=['white', 'black'],
    			callback=onSubMenuChoice,
    			callbackDetails=info['item'],
    		)
    
    def onSubMenuChoice(info):
    	menuOp = op(info['details'])
    	if info['item'] == 'white':
    		menuOp.color = (1,1,1)
    	elif info['item'] == 'black':
    		menuOp.color = (0,0,0)
    
    menuItems = [child.name for child in parent().children]
    op.TDResources.PopMenu.Open(
    		items=menuItems,
    		callback=onMainMenuChoice,
    		subMenuItems=menuItems,
    		autoClose=True,
    		allowStickySubMenus=True
    	)
    
[/code]

Test the code by right-clicking on the textDAT and selecting _Run Script_. When you roll over an Operator name, a sub-menu appears with _black_ and _white_ options. Selecting one of those will change the Operator's color in the network. 

In this example, we have activated the **sticky sub-menus** feature of popMenu. This allows you to click on a sub-menu item (in this case an Operator name) to force the sub-menu to "stick" open. This allows you to click on the sub-menu choices without the menu closing. Try that now. You will see that the Operator name is displayed in a bold font when the sub-menu is set to sticky. You can now switch between black and white without having to re-open the popMenu. You can click on the name again to turn of stickiness. The menu will still close if it loses focus, even if a sub-menu is sticky. 

Let's examine each the script in sections... 

##### The onMainMenuChoice Callback
[code] 
    def onMainMenuChoice(info):
    	info['menu'].OpenSubMenu(
    			items=['white', 'black'],
    			callback=onSubMenuChoice,
    			callbackDetails=info['item'],
    		)
    
[/code]

This is the most important part of creating a sub-menu. It is in the regular selection callback of the parent menu that you define all sub-menu settings. The`**OpenSubMenu**`method is basically identical to the`Open`method used for opening popMenus. The difference is that you call it from within a selection callback on`info['menu']`, which holds the parent popMenu. 

Notice that we set up all item callbacks just as described in previous examples, and we have a separate selection callback,`**onSubMenuChoice**`, to deal with selections from the sub-menu. The other new feature we use here is the`**details**`argument. You can use`details`to pass any extra info you need to the selection callback. In this case, we need to know which main menu item generated the sub-menu, so we pass`info['item']`. 

##### The onSubMenuChoice Callback
[code] 
    def subMenuChoice(info):
    	menuOp = op(info['details'])
    	if info['item'] == 'white':
    		menuOp.color = (1,1,1)
    	elif info['item'] == 'black':
    		menuOp.color = (0,0,0)
    
[/code]

The`**onSubMenuChoice**`callback is fairly simple. First, we fetch the Operator to affect from the`info['details']`received from the`onMainMenuChoice`callback. We then do a simple check against the selected`info['item']`to determine what color to set the operator to. 

##### Color Selector popMenu Setup
[code] 
    menuItems = [child.name for child in parent().children]
    op.TDResources.PopMenu.Open(
    		items=menuItems,
    		callback=onMainMenuChoice,
    		subMenuItems=menuItems,
    		allowStickySubMenus=True
    	)
    
[/code]

The main setup for this popMenu will look familiar to you from the previous examples. The only new thing to notice here is the`**allowStickySubMenus**`argument. This enables sticky sub-menus, which are described [above](<#Example_5_-_Color_Selector_popMenu_with_Sub-Menus>). 

**Important Note:** the system popMenu in`op.TDResources`provides two levels of sub-menus. If you need more than that you will have to create your own set of popMenus. That said, menus with more than two levels of sub-menus tend to be confusing.
