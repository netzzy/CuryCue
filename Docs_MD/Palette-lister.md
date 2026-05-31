# Summary

The **lister** custom Component builds on [List COMP](<./List_COMP.md> "List COMP") to make a multi-featured tool for listing complex data. Formatting of the lister is set up in the **config** Component, which starts out docked to the lister. Data can be provided via Python, parameter or table. Complex data and effects can be achieved using **callbacks**. **NOTE:** Many of lister's features require a basic knowledge of Python. 

You can find **lister** in the [Palette](<./Palette.md> "Palette") under the folder Derivative>UI. Drag and drop the component from the [Palette](<./Palette.md> "Palette") into your network. 

For examples of how to set up a lister, see **[Lister Custom COMP Examples](<./Lister_Custom_COMP_Examples.md> "Lister Custom COMP Examples")**. There is also an extensive [tutorial here](<https://forum.derivative.ca/t/the-big-bad-lister-part-1-3-2020-10-26-10-58/156312>). 

# Custom Parameters

Many of lister's features are set up using custom parameters. 

## Lister Page

This is the parameter page with all basic lister settings. 
* * *

**Refresh**`Refresh`\- Manually refresh the lister. **NOTE:** This re-analyzes raw data for lister, so dynamically added lister data might disappear! 

**Edit Config Comp**`Editconfigcomp`\- Open a network editor window for the Lister's Config Component. 

**Edit Column Definitions**`Editcoldefine`\- Open the lister's colDefine table. (Only available when Auto-define Columns is off) 

**Edit Callbacks**`Editcallbacks`\- Open a text editor for the Lister's callbacks. 

**Print Callbacks**`Printcallbacks`\- Enables debug prints of all callbacks (whether found or not) to the textport. 
* * *

**Input Table DAT**`Inputtabledat`\- Table used as input to the lister. Wired input will override this. 

**Refresh On Input Change**`Refreshoninputchange`\- When on, lister will be automatically refreshed when wired`inputTable`changes. 

**Input Table Has Headers**`Inputtablehasheaders`\- If True, the first row of the input table will be treated as column headers. **For this to work, every column must have a non-blank header.**

**Auto-sync Input Table**`Autosyncinputtable`\- If True, changes to the lister will be mirrored back to Input Table DAT automatically. This only works for columns with the following sourceDataModes:`int`,`float`,`string`,`version`,`blank`,`color`. Only available when Input Table DAT is defined via parameter and Input Table Has Headers is True. 

**Source Index In Output**`Sourceindexinoutput`\- If True, adds a column to the output DATs that holds the original index of the row data, from the input source. Useful for referring back to source tables after data is sorted or rearranged. 
* * *

**Autodefine Columns**`Autodefinecols`\- Enables automatic generation of table columns. 

**Recreate Auto-columns**`Recreateautocolumns`\- Re-analyzes raw data to create automatic column definitions. This will resize column widths, among other things. 

**Copy Auto Cols To Config**`Copyautocolstoconfig`\- Pressing this button copies the column settings created by Autodefine Columns into the lister's custom colDefine table. This is useful for creating a starting point based on Autodefine settings. **WARNING:** this will destroy all current custom column settings. 
* * *

**Header**`Header`\- Enables the table header. 

**Sizeable Cols**`Sizeablecols`\- Enables sizeable columns. Drag header edges to size. A few notes: 
* Works best with 0 or 1`stretch`column. See [colDefine Table](<#colDefine_Table>) below.
  * When there is no`stretch`column, the left column must be`sizeable`. If there is one, the left and right columns must be`sizeable`.
  * For older versions of lister,`sizeable`defaults to off, and you may want to update the _header_ operator in the Config Comp to display header borders. Coloring the Right Border is recommended.


**Save Col Resizes**`Savecolresizes`\- When using Sizeable Cols, save the sized column widths into the colDefine table. This will restore sizes on reload and copy/pastes. This is not available with Auto-Defined Columns. 

**Clickable Header**`Clickableheader`\- Enables click-to-sort columns feature. 

**Selectable Rows**`Selectablerows`\- Enables selection of rows. 

**Multiple Row Select**`Multiplerowselect`\- Enables selection of multiple rows using shift and ctrl keys. Only available when Selectable Rows is on. 

**Drag To Reorder Rows**`Dragtoreorderrows`\- Enables drag to reorder feature. Only available when Selectable Rows is on (rows must be selected to reorder). 

**Arrow Keys**`Arrowkeys`\- Enables moving the row selection using arrow keys. Only available when Selectable Rows is on. 

**Delete Key**`Deletekey`\- Enables selected row deletion using Delete key. Only available when Selectable Rows is on. 

**Highlight Rollover**`Highlightrollover`\- When on, rows will be highlighted when rolled over with the mouse. See Config Component inside for highlight colors. 

**Row Striping**`Rowstriping`\- Striping behavior 
* _Striping_ : uses background color of rowStripeOverlay TOP in config COMP to color every other row.
  * _Dividing Lines_ : uses color set in define table in config COMP to create an underline for each row.


**Drop Highlight**`Drophighlight`\- Defines preview when an external object is dragged into lister and defined as an acceptable drop (see onDropHover callback in [Basic Callbacks](<#Basic_Callbacks>)). The color of the line or highlight will be defined by the`dragDropLineColor`or`dragDropOverlayColor`rows in the [define table](<#define_table>), respectively. 
* _Above Row_ : draw a line above the row being hovered over.
  * _Below Row_ : draw a line below the row being hovered over.
  * _Row_ : draw a highlight over the row being hovered over.
  * _Cell_ : draw a highlight over the cell being hovered over.

## Select/Sort/Filter Page

### Select

**Save Selected Rows**`Saveselectedrows`\- If True, save selection state between loads and when copying/cutting/pasting component. 

**Save Sel. On Input Change**`Saveseloninputchange`\- If input table changes, save selected rows by number even if row objects are different. 

**Allow Empty Selection**`Allowemptyselection`\- When Off, select the first row if no other row is selected 

**Selected Output**`Selectedoutput`\- Determines contents of the out_selected component output. 
* * *

**Selected Rows**`Selectedrows`\- Always contains a space delimited list of the currently selected rows. 
* * *

### Sort

**Save Sort**`Savesort`\- If True, save sort state between loads and when copying/cutting/pasting component. 

**Use Sort Indicator Chars**`Usesortindicatorchars`\- If True, display the following characters in sorted column headers to indicate sort direction 

**Sort Char**`Sortchar`\- If list is sorted by a column, display this in column header after label 

**Sort Reverse Char**`Sortreversechar`\- If list is reverse sorted by a column, display this in column header after label 
* * *

**Sort Columns**`Sortcols`\- A space delimited list of columns to sort by. Note that this is set automatically when Clickable Header is set to True. 

**Sort Reverse**`Sortreverse`\- When True, sort order is reversed. 
* * *

### Filter

**Save Filter**`Savefilter`\- If True, save filter state between loads and when copying/cutting/pasting component. 

**Filter String**`Filterstring`\- In order to be displayed, rows must contain the filter string in one or more of the filter columns. 
* * *

**Filter Columns**`Filtercols`\- A space delimited list of columns to apply the filter to. If this is blank, no filter will be applied. 
* * *

## Advanced Page

This parameter page contains advanced user features for lister. 

**Allow Undo**`Allowundo`\- Enables Undo features when user edits cells and moves rows. 

**Do Advanced Callbacks**`Advancedcallbacks`\- Enables advanced callback features. See inside the internal Docs component for more information. 

**Linked Table DAT**`Linkedtable`\- The lister's contents will be locked to the contents of this DAT. Changes to the DAT will be reflected in Lister and vice-versa. 

**Raw Data**`Rawdata`\- This is a versatile parameter that is useful for quick tests and examples. It can contain a python list, a python list of lists, or a python list of dictionaries. Useful for testing different kinds of input. In previous version, this par could hold a table or path to a table; that functionality is now deprecated and the Input Table DAT parameter should be used instead. 

**Lock Configs**`Lockconfigs`\- Turn off to allow changes to the following two parameters... 

**Config Comp**`Configcomp`\- The Lister's Config Component containing format information. 

**Callback DAT**`Callbackdat`\- The DAT containing the Lister's custom callbacks. Normally this is located in the Config Component. 

**Legacy Drag/Drop**`Legacydragdrop`\- If True, use the old drag/drop callbacks in the lister Callback DAT. Otherwise, use the new standard Drag/Drop Callbacks ([docs.derivative.ca/List_COMP#Drag.2FDrop](<./List_COMP.htm#Drag.2FDrop> "List COMP")). 

# Config Comp

The **config** Comp is where columns, colors, and other set-up is defined. When you create a lister, the config is docked to the component. For easy sharing, you can make the config comp clone immune and put it inside the lister as well. 

## colDefine Table

The **colDefine** table sets up the data definitions and look. The **Autodefine Columns** parameter can be set to True for simple set-ups, and turning it on and off will reset the auto-definitions, but for more complex set-ups, you'll want to define your own columns. **TIP:** for easy access to the colDefine table, pulse the **Edit Column Definitions** parameter on the Lister parameter page. 

The rows inside colDefine are as follows: 
* **column** : the internal name of the column. The names "rowData" and "sourceIndex" are reserved. Use only letters and numbers, and start with a letter.
  * **columnLabel** : the header label for the column. "*" uses the column name.
  * **sourceData** : if`sourceDataMode`is 'constant', this value will be put in each cell. If lister is populated with dictionaries, this value is the key where data for this column is found. If lister is populated with objects, this value is the name of an object's member. If lister is populated with lists, this is the index in the list. In the case of lists, the index is optional, and the list's order will be used if`sourceData`is left blank.
  * **sourceDataMode** : the type of data stored in the column cells. In addition to formatting, this mode defines the way sorts are performed. Anything besides the following values will result in`str(<sourceData>)`.


    

  *`**int**`,`**float**`,`**string**`, or`**version**`fetches values via`sourceData`. The`version`option sorts using [Python's distutils LooseVersion](<http://epydoc.sourceforge.net/stdlib/distutils.version.LooseVersion-class.html>) function.
  *`**constant**`uses the literal`sourceData`string in the colDefine table.
  * **`color`** uses`sourceData`and takes a list of [r, g, b, a] or [r, g, b, a, "text"] (anything else will be treated as text with no color)
  * **`blank`** does not display any text, no matter what the value is, but keeps the value in the lister's`Data`list. This can be useful with the`<topPath>*`mode below.
  * **`repr`** displays`[repr](<http://docs.python.org/3.5/library/functions.html#repr>)``(sourceData)`* **`eval`** treats`sourceData`as an expression to evaluate, with the row object available as`rowObject`. For example, to get the objects class name, you could set`sourceData`to`rowObject.__class__.__name__`.
  * **`rowNum`** displays the lister row number. (`sourceData`is ignored)
  * **`sourceIndex`** displays the source index of the original row info, i.e. the table row if the lister is using an input table
* **textFormat** : final processing of the string displayed in the lister cell. The`textFormat`uses [f-string](<./Python_f-strings.md> "Python f-strings") features to change the displayed string and has no effect on the original data in the table. The following variables are available in the f-string:


    

  *`rowObject`: the full rowObject
  *`text`: cell's text
  *`val`the numeric value of the cell if`sourceDataMode`is`float`or`int`.


    If the format string begins with a`*`, formatting errors will be ignored and the text will appear unchanged if an error occurs.
* **cellLook** : used to reference the tops in config Comp. Make a <cellLook> TOP, a <cellLook>Roll TOP (optional) and a <cellLook>Press TOP (optional).
  * **topPath** : path to top with graphic to display in cells. Paths are relative to this config comp. To make a top that changes on roll and press, create tops with names`<topPath>Roll`and`<topPath>Press`. If the path ends with`*`, the text value of the cell will be added to the path. This is useful for buttons with different states, such as toggles. For example, a topPath of`switch`would look for`switchTrue`or`switchFalse`if the cell held a bool value.`Roll`and`Press`will then be appended to those names for roll and press states. Setting`sourceDataMode`to`blank`is often helpful when using`topPath`with the`*`feature.
  * **help** : the default popup help for the column.`*`will put the value of the cell in the tooltip, which is useful for long data like paths.`*`followed by an expression will evaluate that expression and use the result for the popuphelp; in this mode, the keyword`rowObject`holds the rowObject for the cell and`text`holds the cell's text.
  * **width** : pixel width of column (used as minimum for stretch columns)
  * **stretch** : (1 or 0) If 1, this column stretches.
  * **sizeable** : (1 or 0) If 1, this column is sizeable by dragging the header edges. See the [Sizeable Cols](<#Lister_Page>) parameter above for more info.
  * **editable** : (0-2) text is editable. Row objects will automatically be updated. Other effects can be written in onEdit callback. If the value is 1, single-click to edit. If the value is 2, double-click.
  * **clickOnDrag** : (1 or 0) if 1, pressing a cell in this column causes a click event and dragging the mouse across other cells in this column will cause clicks as each new cell is entered.
  * **draggable** : (1 or 0) if 1, this column's cells are draggable
  * **selectRow** : (1 or 0) If 1, clicking this column selects the row when row selection features are active
  * **justify** : text justification. Can be 'TOPLEFT', 'TOPCENTER', 'TOPRIGHT', 'CENTERLEFT', 'CENTER', 'CENTERRIGHT', 'BOTTOMLEFT', 'BOTTOMCENTER', or 'BOTTOMRIGHT'. Defaults to 'CENTERLEFT'. If blank, defaults to master [look](<#Format_OPs_and_Looks>) or`cellLook`.
  * **fontBold** : when no`cellLook`is defined, use this to control font bold. If blank, defaults to master [look](<#Format_OPs_and_Looks>).
  * **fontItalic** : when no`cellLook`is defined, use this to control font italic. If blank, defaults to master [look](<#Format_OPs_and_Looks>).

## autoColDefineDefaults Table

The **autoColDefineDefaults** table is similar to the colDefine table but has only labels and a single column of data. These are the default settings that will be use for each column when **Auto-define Columns** is on. If you want the width of the lister columns to be based on the size of the text in the column, put the string`auto`in the width cell. 

## define Table

The **define** table holds extra definitions for lister. Each definition has a Description with info about its effects. 

## Format OPs and Looks

Any unlocked textTOPs or textCOMPs in the Config Comp will create "Looks" in the lister's extension (available through the "Look" dict). The looks define the attributes for the table, rows, columns, and cells in various states. The button____ textCOMPs are an example of a user-defined look. The btnImage____ textCOMPs are an example of graphics to be displayed in cells. 

Older versions of lister used textTOPS to define Looks, but it is highly recommended to convert these to textCOMPs in modern versions. Examples can be found in the default Config Comp on the lister in the palette>UI. 

The following table shows the correspondence between the textTOPs, the textCOMPs, and the listCOMP's attrib members: 

textTOP parameter(s) | textCOMP parameter(s) | listCOMP attrib   
---|---|---  
font | font | fontFace   
fontfile | fontfile | fontFile   
fontsizex | fontsize | fontSizeX   
(fontcolorr, fontcolorg, fontcolorb, fontalpha) | (fontcolorr, fontcolorg, fontcolorb, fontalpha) | textColor   
(bgcolorr, bgcolorg, bgcolorb, bgalpha) | (bgcolorr, bgcolorg, bgcolorb, bgalpha) | bgColor   
wordwrap | wordwrap | wordWrap   
bold | bold | fontBold   
italic | italic | fontItalic   
position1 | textoffsetx | textOffsetX   
position2 | textoffsety | textOffsetY   
(alignx, aligny) | (alignx, aligny) | textJustify   
resolution2 | h | rowHeight   
  
In addition, all border settings from textTOPs will be applied to the attributes (`<side>Border<location>Color`) 

## Callbacks DAT

The **callbacks** DAT contains the lister's custom callbacks. The location of this DAT can be changed via the lister's parameters. For more information, see below. 

# Custom Callbacks

**Custom callbacks** facilitate complex Python tasks within the lister. Callbacks always take a single argument, an **info dictionary** of values relevant to the callback. Print this dictionary to see what is being passed. The keys will explain what each item is. 

The info dictionary always contains an "ownerComp" key. It will often contain an "about" key, describing the callback, and will always contain this key if a return value is expected. Generally, callbacks are called AFTER the internal method they are associated with, to allow over-riding of whatever that method does. 

Callbacks marked with (c), called **Cell Callbacks** , can be named in two ways... 
* Callback<Column name> for specific columns (e.g. onClickNetwork, onClickName)
  * Callback for all cells (e.g. onClick)


**Note** : the Callback<Column name> format uses the`column`setting from the [colDefine table](</index.php?title=ColDefine_table&action=edit&redlink=1> "ColDefine table \(page does not exist\)") up to the first space. 

If you want to see all callbacks being called, turn on the **Print Callbacks** switch in the lister parameters. Callbacks will now be printed to textport. 

## Callback Gotchas

### Off-Cell Callbacks

In order to receive callbacks for **the area in the lister that does not have any cells** , the **Off Cell Callbacks** parameter on the **List** page must be set to True. The row and column for off cell callbacks is -1. 

## Basic Callbacks
* **onInit** : When extension is re-initialized, but before initial refresh and auto-column set up
  * **onPostInit** : Called one frame after initialization.
  * **onRefresh** : Whenever list data is changed, a refresh is called. The following four callbacks all happen within every Refresh call.
  * **onGetRawData** : This is where the list of raw data is set up. For example, this could be a list of comps. Lister can currently analyze a list of lists, a list of tuples, a list of dicts, a list of objects, or a table operator. If a source table is provided in Lister parameters or through wiring, info["data"] will be pre-filled with the data from that table. **Return a raw data list.**
  * **onConvertData** : Turn the raw data into a workingData, a list of strings to be used in the table cells. Note that the object from rawdata is always appended to this list! Lister automates this to a large degree. **Return a converted data list.**
  * **onFilter** : Filter out elements of workingData as desired. Lister automates this to a large degree. **Return a filtered data list.**
  * **onSort** : Sort workingData as desired. Lister automates this to a large degree. **Return a sorted data list.**
* **onClick, onClickRight, onClickMiddle** : (c) mouse pressed and released on a cell
  * **onClickHeader, onClickHeaderRight, onClickHeaderMiddle** : (c) mouse pressed and released on header row cell
  * **onDoubleClick** : (c) Left mouse double-click on cell
  * **onDoubleClickHeader** : (c) Left mouse double-click on header row cell
  * **onEditEnd** : (c) Cell text has been edited
  * **onChangeCellText** : (c) A cell's text has been changed
  * **onMouseDown, onMouseRightDown, onMouseMiddleDown** : (c) Mouse pressed down on cell
  * **onMouseUp, onMouseRightUp, onMouseMiddleUp** : (c) Mouse released down on cell
  * **onMouseHold** : (c) The mouse has been held down on a cell for a full second
  * **onMouseDrag, onMouseRightDrag, onMouseMiddleDrag** : Button down and dragged
  * **onSelectRow** : A row has been selected
  * **onDeselectRow** : a row has been deselected
  * **onRemovedSelectedRow** : a row that was selected was removed during Refresh
  * **onSelectColumn** : A header column has been selected by click (mouse press-release)
  * **onDataChanged** : The main data list has been altered. This callback is called BEFORE the listCOMP is reset.
  * **onMoveRows** : Rows have been rearranged
  * **onDeleteRows** : Rows have been deleted
  * **onKeyPressed** : A key has been pushed down
  * **onKeyReleased** : A key has been released
  * **onAddRow** : a row has been added to the lister via the`AddRow`method, or Undo/Redo.
  * **onSetupAutoColDefine** : the autoColDefine definitions have been recreated. Use this callback to customize the autoColDefine table.

## Advanced Callbacks

The following callbacks will only be called if the **Do Advanced Callbacks** parameter is set to True. Generally, these callbacks will be called more often when active and are separated for the sake of speed. 
* **onSetCellLook** : (c) Called whenever a look is applied to a cell.
  * **onSetCellText** : (c) A cell's text is being set
  * **onSetHeaderLook** : Called when a look is applied to a header cell.
  * **onSetRowLook** : Called when a look is applied to a row
  * **onInitCell** : (c) Called when a cell is initialized, which happens after each Refresh
  * **onInitHeader** : Called when header row is initialized.
  * **onInitRow** : Called when row is initialized
  * **onRollover** : Mouse is rolling over the list.
  * **onPressCell** : (c) A cell is being pressed like a button, but has not been released. This can happen multiple times if the user presses and drags mouse on and off cell. Used in association with the "press" looks for buttons...
  * **onRowObjectToWorkingData** : called after a row is converted from a raw object to a list of data for the lister.
  * **onSortDataRows** : called after a set of rows are sorted by the lister.

# Drag/Drop

Lister uses standard [List COMP drag/drop callbacks](<./List_COMP.htm#Drag.2FDrop> "List COMP"). 

**Note:** you can set a lister column to be draggable in the column definition table. You can also set listCOMP draggable attributes directly. 

The following old callbacks are now deprecated: 
* **onDropHover** : (c) Something is being dragged onto lister. Return true if interested. If True is not returned, no **onDrop** callback will be received.
  * **onDrop** : (c) Something is being dropped onto lister. If the drop is from another Lister, info['fromListerInfo'] will contain the source cell. Otherwise, that value will be None. You won't get this if the return value of the previous onDropHover call was False. Callbacks will not be recieved if the Drop parameter in the Drag/Drop page is set to Do Not Allow Drops.

# Inputs

Input 1`inputTable`: A table of data to be used in the lister. This data can be filtered or sorted within the lister. 

# Outputs

Output 1`out_table`: A duplicate of the lister's data in text form. Output 2`out_selected`: Info from selected rows 

# ListerExt Extension Class

The **`ListerExt`** extension provides extended functionality for working with lister. Frequently used members and methods are listed here. A full list can be found using the Python`help()`function. 

## Members`**Data**`| A list of Python dictionaries, keyed by column names + a 'sourceIndex' key containing the original data index and a 'rowObject' key containing the original raw data for the lister. This is where you will find all data used to generate the list.   
---|---`**ColumnDict**`| **(Read Only)** A dictionary of column name: column number.`**ColNumDict**`| **(Read Only)** A dictionary of column number: column name.`**SelectedRowObjects**`| **(Read Only)** A list of all rowObjects in selected rows.   
  
## Methods

**`Refresh()`**

    Re-init table, refreshing all data and formatting all cells.

**`DeleteRows(rows)`**

    Delete a list of rows. 

  *`rows`\- A python list of row numbers.


**`DataChanged(selectionObjects=None)`**

    Call this when you change the Lister's Data. Refreshes text and size. Does not get raw data, convert data, sort or filter. 

  *`selectionObjects`**(Optional)** \- a list of objects that will be selected if present in rowObjects.


**`GetObjectRowNum(object)`→`row number of object`**

    Returns the row number of the provided object. 

  *`object`\- the raw data row object used to populate the lister.


**`SelectRow(row, addRow=False)`**

    Set selected row. Set row to None and addRow to False to remove all selections. 

  *`row`\- the row number to select.
  *`addRow`\- **(Keyword, Optional)** Set to True to add row to current selection.


**`DeselectRow(row)`**

    Deselect a row. 

  *`row`\- the row number to deselect.


**`SetCellLookName(row, col, lookName)`**

    Set the individual cell look name. Generally, this should be called in the onInitCell (individual cell) or onInitTable (whole table) callbacks 

  *`row`\- cell row number
  *`col`\- cell col number
  *`lookName`\- name of look (see textTOPs in config comp). Use`None`to unset individual cell look (goes back to col look). Use`""`to remove column look and unset individual cell look.


**`SortDataRows(dataRows, keyList=None)`**

    Sort a list of row data in place. This will sort using the columns set by the lister's Sort Columns parameter. 

  *`dataRows`\- a list of data rows.
  *`keyList`\- **(Keyword, Optional)** A list of sort keys to apply to their corresponding columns. These will override standard sort methods. A value of`None`in the list means to use standard sort.


**`AddRow(rowNumber=None, rowData=None, rowObject='__no__object__', rowDict=None, addUndo=True, sourceIndex=None)`→`rowData`**

    Add a row to lister data. 

  *`rowNumber`\- where to insert the row. None (default) appends it.
  *`rowData`\- a full row data dictionary including all cols and 'rowObject' key
  *`rowObject`\- a rowObject to be processed by RowObjectToDataRow. Ignored if rowData is provided.
  *`rowDict`\- a dictionary of colName:data to fill row. Missing columns will be blank. None (default) will create a blank row. Ignored if rowObject or rowData is provided.
  *`addUndo`\- if True, add an undo step for this
  *`sourceIndex`\- used to reference back to original data order. Probably unnecessary if rows are being added manually.


**`RowObjectToDataRow(rowObject, sourceIndex=None)`→`dict formatted for Data list`**

    Convert a rowObject to a dict keyed by column names. The final items will be the sourceIndex and rowObject. 

  *`rowObject`\- any valid row object (list, dict, or Python object)
  *`sourceIndex`\- used to reference back to original data order. Probably unnecessary if rows are being added manually.


**`WorkingDataToDataRow(workingData, sourceIndex=None)`→`dict formatted for Data list`**

    Convert a list of data to a Dict keyed by column names. The final items will be the sourceIndex and rowObject. If you don't need to alter the data in the columns, use RowObjectToDataRow instead. 

  *`workingData`\- a list of data corresponding to each column of the lister, followed by the original row object.
  *`sourceIndex`\- used to reference back to original data order. Probably unnecessary if rows are being added manually.

## Overlay System

The extensions implement an overlay system that allows background color manipulation for different areas in the lister. These functions will generally be called from callbacks, depending on if they are in reaction to events (call in`on<Event>`callbacks) or whenever lister data is refreshed (call in`onRefresh`callback). There are certain situation where you may have to use advanced callbacks`onSet<location>Look`to get this to work. The overlays are defined by **overColor** s, which are a standard r, g, b, a list with an optional **overLayer** number at the end. The overLayer defines the layer of the overlay, which affects transparency operations. There can only be one overlay per overlayer, so later settings to the same overLayer will replace previous settings. 

All overlay functions return a **removeArgs** tuple that can be passed back to the setter function to remove that overlay. For example: 
[code] 
    # set column 3 red:
    removeArgs = myLister.SetColOverlay(3, [1,0,0,1])
    
    # remove red overlay from column 3:
    myLister.SetColOverlay(*removeArgs)
    
[/code]

**`SetColOverlay(col, overColor, apply=True)`→`removeArgs tuple`**

    Apply (or remove) overlay to a column. 

  *`col`col to overlay
  *`overColor`overColor for overlay. If None, remove all overlays. Default overlayer is 40.
  *`apply`if True the overlay will be applied. If False, the overlay will be removed if found


**`SetRowOverlay(row, overColor, apply=True)`→`removeArgs tuple`**

    Apply (or remove) overlay to a row. 

  *`row`row to overlay
  *`overColor`overColor for overlay. If None, remove all overlays. Default overlayer is 45.
  *`apply`if True the overlay will be applied. If False, the overlay will be removed if found


**`SetCellOverlay(row, col, overColor, apply=True)`→`removeArgs tuple`**

    Apply (or remove) overlay to a cell. 

  *`row`row of cell
  *`col`col of cell
  *`overColor`overColor for overlay. If None, remove all overlays. Default overlayer is 50.
  *`apply`if True the overlay will be applied. If False, the overlay will be removed if found


**`SetRangeOverlay(row, col, height, width, overColor, apply=True)`→`removeArgs tuple`**

    Apply (or remove) overlay to a rectangle of cells. 

  *`row`row of top left corner
  *`col`col of top left corner
  *`height`height of overlay rectangle
  *`width`width of overlay rectangle
  *`overColor`overColor for overlay. If None, remove all overlays. Default overlayer is 100.
  *`apply`if True the overlay will be applied. If False, the overlay will be removed if found
