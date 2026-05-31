# 

Summary

The **popMenu** custom Component builds on [Container COMP](<./Container_COMP.md> "Container COMP") to make an easy-to-use pop-up menu that can be used as a context menu, in dropdown controls, or for other menu needs. The dialog can be set up using parameters or script. Multi-level menus can be created through scripting. Custom formatting of popMenu is set up in the internal **config** Component. A **callback** system is provided for more complex needs. 

There is a system`popMenu`available in`op.TDResources`, so for many needs a call to`op.TDResources.PopMenu.Open(...)`is all that is needed to create a menu. The system`popMenu`has two levels of submenu attached to it to facilitate multi-level context menus. 

Just as the system popMenu can be used for many different purposes (as long as only one is open at a time) it is highly recommended to reuse a custom popMenu as much as possible. That is, once you have configured a popMenu to your liking, use Python to open that same one from different places if possible, for example, from a [Panel Execute DAT](<./Panel_Execute_DAT.md> "Panel Execute DAT") in a Container COMP. This saves memory, creates a uniform menu style, and minimizes [Window Components](<./Window_COMP.md> "Window COMP"). 

For examples of how to set up a popMenu, see **[PopMenu Custom COMP Examples](<./PopMenu_Custom_COMP_Examples.md> "PopMenu Custom COMP Examples")**. 

**TIP:** if your popMenu configuration is dependent on rapidly changing values, turning off its viewer will cause it to consume less time when not in use. 

# Custom Parameters - Pop Menu Page

Help Page`Helppage`\- Open this wiki page in a browser. 

Open`Open`\- Open the pop-up menu. 

Close`Close`\- Close the pop-up menu 

Input Table`Inputtable`\- Choose the input table format with this menu. 
* _Include All Rows, Column 0 is Items_ : uses all rows in table with the first column as menu items.
  * _First Row is Labels, Column 0 is Items_ : uses first row of table as labels, with the first column of all following rows as menu items.
  * _First Row is Labels, Column "name" is Items_ : uses first row of table as labels, and the column labeled "name" of all following rows as menu items.
* * *

Items`Items`\- A python list of menu item strings, in the order they are to appear. 

Highlighted Items`Highlighteditems`\- A python list of visually highlighted items from Items parameter. 

Disabled Items`Disableditems`\- A python list of disabled items from Items parameter. 

Dividers After Items`Dividersafteritems`\- These items will have a line drawn under them. 

Checked Items`Checkeditems`\- A list or dictionary of items with check marks after them. If a dictionary is used, the format is`{'<item name>': True/False}`. False items will have an empty checkbox. 

Shortcuts`Shortcuts`\- A dictionary of keyboard shortcuts in the form`{'<item name>': '<shortcut>'}`. This does not implement the keyboard shortcut, it is only informational. 

Title`Title`\- Display this string at top of menu. 

Columns`Columns`\- The number of columns in the popMenu. All columns will be of equal width, and items will be listed from top to bottom then left to right. If there is more than one column, dividers, submenus, and checked item features will not be available. 

Max Height Mode`Maxheightmode`\- Selects whether the _Max Height_ parameter (below) is defined in pixels or rows. 

Max Height`Maxheight`\- If the menu is taller than this, a scrollbar will be used. 

Scale`Scale`\- Scale the entire menu by this factor. 

Auto Close`Autoclose`\- If true, the menu will be closed when a choice is made. 

Borders`Borders`\- Display menu borders. 
* * *

Horizontal Align`Horizontalalign`\- Defines the horizontal anchor point of the menu when it is opened. 

Vertical Align`Verticalalign`\- Defines the vertical anchor point of the menu when it is opened. 

Align Offset`Alignoffset`\- Offset from the anchor point when menu is opened. 
* * *

Button Comp`Buttoncomp`\- A component that the menu is displayed relative to. If this is not a valid comp, menu will be displayed relative to mouse. 

Horizontal Attach`Horizontalattach`\- The horizontal location on Button Comp the menu is attached to. 

Vertical Attach`Verticalattach`\- The horizontal location on Button Comp the menu is attached to. 

# Custom Parameters - Advanced Page

Edit Callbacks`Editcallbacks`\- Edit the callbacks DAT. 

Print Callbacks`Printcallbacks`\- Debug messages for callbacks. See [Callbacks](<#Python_Callback_System>). 

Callback DAT`Callbackdat`\- DAT containing callback definitions. See [Callbacks](<#Python_Callback_System>). 

Config Comp`Configcomp`\- This popMenu's config Component. See [Config Comp](<#Config_Comp>). 

Refresh Look Config`Refreshlookconfig`\- Manually refresh the look after changes. See [Config Comp](<#Config_Comp>). 

Window Comp`Windowcomp`\- This popMenu's Window Component. **Note** : the internal window component is not clone immune, so to safely customize, create an external one or switch the internal one's clone immune flag on. 

DPI Scaling`Dpiscaling`\- The internal Window Component's DPI scaling mode. 

Include in Placement Dialog`Includedialog`\- Show the internal Window Component in the [Window Placement Dialog](<./Window_Placement_Dialog.md> "Window Placement Dialog")

SubMenu`Submenu`\- Another popMenu that opens as a submenu to this one. 

Allow Sticky SubMenus`Allowstickysubmenus`\- If True, clicking on a submenu entry will set it to stay open when an item is selected. 

# Inputs

inputTable - A table of items and, optionally, other information. Formatted as defined in the _Input Table_ parameter. 

# Outputs

selected - A CHOP containing the currently selected Item index, or -1 if the menu is open but nothing has been selected. 

selectedRow - A table containing the currently selected Item or nothing if menu is open but nothing has been selected. When using an input table, this will contain that table's labels and all columns from the selected row 

# PopMenu Extension Class

The **PopMenuExt** extension provides script functionality for working with popMenu. Frequently used members and methods are listed here. A full list can be found using the Python`help()`function. Note that within the extension, a each clickable Item area is called a **cell**. The cell number is the same as the Item index. A cell number of -1 is sometimes used to mean "no cell". 

## Members`**OptimalWidth**`| **(Read Only)** The best width for the menu to display all cells. Generally used by the width parameter.   
---|---`**OptimalHeight**`| **(Read Only)** The best width for the menu to display all cells. Generally used by the height parameter.`**Items**`| **(Read Only)** The list of items in the pop menu.   
  
## Methods

**`Open(items=None, callback=None, callbackDetails=None, disabledItems=None, dividersAfterItems=None, checkedItems=None, subMenuItems=None, autoClose=None, rolloverCallback=None)`**

    Opens the menu. Usually, a call to this method and a callback (provided in argument here or defined in Callback DAT) is all that is needed to use popMenu. If`items`argument is set to None, all other arguments set to None will use the values set in the popMenu's parameters. If`items`argument is provided, other arguments will have default values described below. 

  *`items`\- a list of item strings for the menu. If this is None or not provided, the default is to use the Items set up in parameters. If provided, these options will replace the ones in the Items parameter, and other Item parameters will be ignored (e.g. Disabled Items).
  *`callback`\- a method that will be called when a selection is made.
  *`callbackDetails`\- will be passed to callbacks in addition to item chosen.
  *`disabledItems`\- list of strings for greyed out, unselectable items. If`items`argument is provided, default = [].
  *`dividersAfterItems`\- list of strings for items with dividers below them. If`items`argument is provided, default = [].
  *`checkedItems`\- list of strings for items with check marks next to them. Will show the 'check' graphic in configComp. Also accepts a dict of strings with 'item': bool. Will show the 'checkOn' or 'checkOff' graphic depending on bool. Also accepts a string which will be used as an EXPRESSION to continually evaluate. If`items`argument is provided, default = [].
  *`subMenuItems`\- list of strings for items with indicator and will select on rollOver instead of click. Always use OpenSubMenu in handler function. Set SubMenu parameter to another popMenu comp. Default is []... no parameter available for submenus. If`items`argument is provided, default = [].
  *`autoClose`\- will close after selection or click away. If`items`argument is provided, default = True.
  *`rolloverCallback`\- will be called when a cell is rolledOver. A callback with cell -1 will be called when mouse leaves menu or menu closes. Uses same callbackDetails as selection callback.


**`OpenSubMenu(items=None, callback=None, callbackDetails=None, disabledItems=None, dividersAfterItems=None, checkedItems=None, subMenuItems=None, autoClose=None, rolloverCallback=None)`**

    Opens the menu's sub-menu. All arguments are exactly as in the`Open`method above. For all sub-menu items, this method must be called from the selection callback.

**`SetPlacement(hAlign='Left', vAlign='Top', alignOffset=(0,0), buttonComp=None, hAttach='Left', vAttach='Bottom', matchWidth=False)`**

    Set up placement parameters for the popMenu. This is a convenience function for reusing popMenu as a dropdown menu in multiple places 

  *`hAlign`\- set Horizontal Align.
  *`vAlign`\- set Vertical Align.
  *`alignOffset`\- set Align Offset.
  *`buttonComp`\- set Button COMP.
  *`hAttach`\- set Horizontal Attach.
  *`vAttach`\- set Vertical Attach.
  *`matchWidth`\- True = match width of menu to width of button Comp, False = optimal width, number = specific width.


**`Close()`**

    Close the menu. The selection callback will not be called.

**`OnSelect(cell, doautoClose=True)`**

    Simulates a click of the provided cell. 

  *`cell`\- the cell number to simulate a click on.
  *`doautoClose`\- **(Optional)** if False, skip all auto close functionality.

# Python Callback System

The **CallbackExt** extension provides Python callback functionality to custom components. All callbacks will be passed a single argument containing an **info dictionary**. Callbacks can be defined in the DAT named in the **Callback DAT** parameter. To report all callbacks to the textport, turn on the **Print Callbacks** toggle parameter. The Callback DAT and Print Callbacks parameters are often found on the Callbacks parameter page, but their location can be customized. 

The info dictionary always contains an "ownerComp" key. It will also have a "callbackName" key holding the callback name. It will sometimes contain an "about" key, describing the callback, and should always contain this key if a return value is expected. Generally, callbacks are called AFTER the internal method they are associated with, to allow over-riding of whatever that method does. 

TouchDesigner's Python callback system uses the [CallbacksExt Extension](<./CallbacksExt_Extension.md> "CallbacksExt Extension"). 

## PopMenu Callbacks
* **onSelect** : A selection has been made in the dialog. This is another way to achieve the effect of providing a callback via the`Open`method. The data provided in the info dictionary is as follows:
* **index** : The index in the menu's list of items.
  * **item** : The label in the menu's list of items.
  * **row** : The full row of info from the wired-in table of items, if there is one. Otherwise,`None`.
  * **details** : Callback details, as provided in the`Open`method.
  * **menu** : The popMenu itself.
* **onRollover** : A cell has been rolled over. The data provided in the info dictionary is the same as for the`onSelect`callback, however the cell can be -1, meaning that the mouse is not over any cell.
* **onOpen** : Called when popMenu is opened. The`details`and`menu`are provided as described above.
* **onClose** : Called when popMenu is closed. The`details`and`menu`are provided as described above.
* **onMouseUp** : The mouse has been released. The data provided in the info dictionary is the same as for the`onSelect`callback, however the cell can be -1, meaning that the mouse is not over any cell.
* **onMouseDown** : The mouse has been pressed. The data provided in the info dictionary is the same as for the`onSelect`callback, however the cell can be -1, meaning that the mouse is not over any cell.
* **onClick** : The mouse has been pressed and released on the same cell. The data provided in the info dictionary is the same as for the`onSelect`callback, however the cell can be -1, meaning that the mouse is not over any cell.
* **onLostFocus** : The popMenu has lost focus.

# Config Comp

The docked **config** Comp is where the colors, fonts, and graphics for popMenu are set up. 

## colDefine table

The **colDefine** table in popMenu's config Comp is only used to define the symbol column for subMenus and check boxes. In almost every case, the only thing that should be changed is the 'width' value. 

## textCOMPs

The textCOMPs are used to define the icons and cell looks in the popMenu. The **subMenu** , **check** , **checkOff** , and **checkOn** textCOMPs hold icon look and placement info. The **master** , **title** , **button** , **buttonRoll** , **buttonPress** , **buttonDisabled** , and **buttonHighlighted** textCOMPs define the various item looks. 

## TOPs

The **dividerColor** TOP defines the color of dividers as declared in the "Dividers After Items" parameter or argument. 

Older versions of popMenu used a different system for defining icons. The **subMenu** , **checkOn** , and **checkOff** TOPs are the graphics used for these elements in the popMenu. The various textTOPs define the cell format for list elements.
