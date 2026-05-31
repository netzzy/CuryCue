# Palette:treeLister

The **treeLister** custom Component provides a powerful and easy way to make tree controls for displaying hierarchical data. It is derived from the [lister custom component](<./Palette-lister.md> "Palette:lister"), so many of its features are documented in that Component's wiki pages. **Note:** many of treeLister's features require a basic knowledge of Python.   
  
You can find **treeLister** in the [Palette](<./Palette.md> "Palette") under the folder Derivative>UI. Drag and drop the component from the [Palette](<./Palette.md> "Palette") into your network. 

**See Also:**[Palette:lister](<./Palette-lister.md> "Palette:lister"), [Lister Custom COMP Examples](<./Lister_Custom_COMP_Examples.md> "Lister Custom COMP Examples")

# 

Quick Start

There are three main ways to input data into a treeLister. They correspond to the options in the **Input Mode** parameter. Be sure the appropriate option is selected there when using the following methods... 

### Callbacks Only

This method is useful for data objects that already have a hierarchical structure, such as file directories and TouchDesigner networks. To use callbacks to dynamically generate tree data, you must: 
* define the following callbacks:`getObjectFromID`,`getIDFromObject`,`getObjectChildren`. See [Basic Callbacks](<#Basic_Callbacks>) below for information about each one. To edit treeLister's callbacks, click the Edit Callbacks parameter on the Lister parameter page.
  * define tree roots in the [Roots parameter](<#Settings>) and/or define the treeLister's`DefaultRoots`member in the`[onInit](<./Palette-lister.htm#Basic_Callbacks> "Palette:lister") callback`.`DefaultRoots`will be used if the Roots parameter is blank.

### JSON

For this method, wire a DAT containing a valid JSON text object into the treeLister's input. The JSON object will be represented in tree form. 

The row objects that are automatically created from JSON have the following members: 

    

  *`**key**`: The object's key in it's parent container. This is a key string for objects in dicts and an index integer for objects in lists.
  *`**id**`: The tree ID used for the object. This is a tuple of keys leading to the object from the root.
  *`**type**`: The type of the object.
  *`**value**`: The value of the object if it does not hold a container.
  *`**children**`: The object's children if it holds a container.

### Table with "path" col

For this method, wire a table DAT with column headers and a "path" column into the treeLister's input. The path should be unique for every row of the table. If necessary, set the Path Separator parameter. Example DATs for use with this method: [OP Find DAT](<./OP_Find_DAT.md> "OP Find DAT") and [Folder DAT](<./Folder_DAT.md> "Folder DAT"). 

### Table with "path", "wirepath", and "parentpath" cols

For this method, wire a table DAT with column headers and "path", "wirepath", and "parentpath" columns into the treeLister's input. This is for use with the [OP Find DAT](<./OP_Find_DAT.md> "OP Find DAT") to create tree data from TouchDesigner networks that include grey wired hierarchies. 

## Column Definitions

To verify your data and get the basics of your tree set up, turn on the **Autodefine Columns** parameter on the Lister page. 

Ultimately you will probably want to create your own column definitions for a tree lister. For information about that, see [Lister Custom COMP: colDefine table](<./Palette-lister.htm#colDefine_table> "Palette:lister"). For full tutorials, see: [Lister Custom COMP Examples](<./Lister_Custom_COMP_Examples.md> "Lister Custom COMP Examples"). **Note:** you should always keep the first two columns for indent and expander button. The third column should be stretchy to absorb each row's indent. 

# 

Custom Parameters

Basic treeLister functionality is set up with parameters. 

## Tree Page

### Tools

Collapse All`Collapseall`\- Collapse all branches of the tree. 

Reload Input`Reloadinput`\- Reload input table or JSON. 

### Settings

Input Table`Treeinputtabledat`\- Table used for input (alternative to wiring in). 

Input Mode`Inputmode`\- Select the mode for the Component's input. 
* **Callbacks Only** : Use the callback system to build the tree dynamically. Requires that the following callbacks are defined:`getObjectFromID`,`getIDFromObject`,`getObjectChildren`.
  * **JSON** : Input provided through text DAT wired to input. The DAT must contain a valid JSON text object.
  * **Table with "path" col** : Input provided through table DAT wired to input. The DAT must have a "path" column that contains a unique path for each row. These paths will be used to define the tree hierarchy.


Path Separator`Pathseparator`\- The separator used in the "path" column for the _Table with "path" col_ input mode. 

Numeric Path`Numericpath`\- If True, treat the elements between path separators as numbers. Useful for IP-like paths. 

Use Default Roots`Usedefaultroots`\- If True, use the tops of provided data structure as the roots. 

Roots`Roots`\- A Python list of tree ID's to be used as the root objects in the tree. 

Show Roots`Showroots`\- If off, the tree will start at the defined roots, but will start displaying at the roots' children. For example, this can be used to show every file in a folder without displaying a node for the folder itself. 

Click Corner To Refresh`Clickcornertorefresh`\- When on, treeLister will display a refresh button in the top-left of the tree. This is useful for manually refreshing data that has changed. 

# 

Config Comp

The internal **config** Comp is where columns, colors, and other set-up is defined. All the features of [Lister's Config Comp](<./Palette-lister.htm#Config_Comp> "Palette:lister") are available. Only the changes and additions will be described here. 

## colDefine table

The **colDefine** table sets up the data definitions and look. For detailed info, see [Lister Custom COMP: colDefine table](<./Palette-lister.htm#colDefine_table> "Palette:lister"). 

##### Required Columns

TreeLister has two required columns: **`Indent`** and **`Expando`**. These are set up for you in the default treeLister, and you will generally not have to change them. The`Indent`column is the empty space before a row, and the`Expando`column contains the button to expand and collapse tree branches. In the column definition`textFormat`row is the characters used for open and closed branches. 

The third column should be set to`stretch`to absorb each row's indent. **Tip:** the`width`entry sets the minimum width for stretchable columns, so set that to a number large enough to display your tree labels. 

##### Changes To`sourceData`and`sourceDataMode`TreeLister adds a new **`sourceDataMode`** to lister's choices: "**`id`** " will display a row object's tree ID. 

When treeLister is using **Table with "path" col** Input Mode,`sourceData`refers to the column label in the input table. In this mode, the special`sourceData`entry`__row__`will also be available to display the source row of the input table. **Tip:**`"__row__"`is also available as a key in the row object of each lister`Data`row. 

## define table

The **define** table holds extra definitions for a lister. The treeLister adds: 
* **`indentWidth`** \- defines the number of pixels to indent each level of the tree.
  * **`refreshChar`** \- the character used in the corner when _Click Corner to Refresh_ is on.

## Look OPs

The various textCOMPs (older version use textTOPs) define the attributes for the table, rows, columns, and cells in various states. The treeLister adds a few of these, most important of which are the **expando*** textCOMPs. These define the way the expando button looks in the treeLister. The characters used in expando are found in the [colDefine table](<#colDefine_table>),`textFormat`row. There is also an **indent** textCOMP defining how the indent area looks. **In general there is no need to change these OPs.**

# 

Custom Callbacks

**Custom callbacks** facilitate complex Python tasks within the treeLister. Callbacks always take a single argument, an **info dictionary** of values relevant to the callback. Print this dictionary to see what is being passed. The keys will explain what each item is. 

All the [callbacks from lister](<./Palette-lister.htm#Custom_Callbacks> "Palette:lister") are available in treeLister. 

In addition, the following are new callbacks added to treeLister: 

## Basic Callbacks
* **getObjectFromID** : Every row object in a treeLister must have a unique ID, which is often the "path" to the object. This callback must return the row object. The info dictionary provides:
* **id** : the ID used to identify the object
  * **jsonObject** : if the tree has an associated JSON hierarchy, this is the object returned by that hierarchy for the given ID.
* **getIDFromObject** : This is the reverse of`getObjectFromID`. This callback must return the ID. The info dictionary provides:
* **object** : the row object
  * **jsonID** : if the tree has an associated JSON hierarchy, this is the ID returned by that hierarchy for the given object.
* **getObjectChildren** : This callback must return a list of child objects for the provided tree row object. The info dictionary provides:
* **object** : the row object
  * **jsonChildren** : if the tree has an associated JSON hierarchy, this is a list of`object`'s child objects in that hierarchy.

## Advanced Callbacks
* **onReloadInput** : Called after input JSON or table data is reloaded into tree.
  * **onBuildTreeData** : Called after the tree builds its working data for all rows.
  * **onTreeInitRow** : Called after the tree initializes a data row, including setting its rowIndent attribute.

# 

TreeListerExt Extension Class

The **`TreeListerExt`** extension provides extended functionality for working with treeLister. Frequently used promoted members and methods are listed here. A full list can be found using the Python`help()`function. 

**Note:** The`TreeListerExt`class uses`ownerComp`in an unusual way, to refer to its internal [Lister custom Component](<./Palette-lister.md> "Palette:lister"). The treeLister itself is stored in its`treeListerComp`member. 

## Members`**Lister**`| The internal [Lister custom Component](<./Palette-lister.md> "Palette:lister"). **Note:** this is also`ownerComp`, for inheritance reasons.   
---|---`**TreeLister**`| The TreeLister component itself. **Note:** this is **not**`ownerComp`, for inheritance reasons.`**DefaultRoots**`| A set of tree IDs to be used as the default roots, if the Root parameter is empty.`**Roots**`| **(Read Only)** The IDs of the tree's root objects.`**SelectedPaths**`| **(Read Only)** All selected paths. Only works in "path" col modes.`**IDObjDict**`| **(Read Only)** A dictionary of tree objects indexed by ID. This doesn't use the getObjectFromID callback.`**ObjIDDict**`| **(Read Only)** A dictionary of IDs indexed by tree object. This doesn't use the getIDFromObject callback.   
  
## Methods

**`ReloadInput()`**

    Reload input JSON or table.

**`OpenToPath(path, doRefresh=True)`→`True if successful, root opened in if already open, otherwise None.`**

    Open tree to the provided path. Only works in "path" col modes. 

  *`path`: The path to open to
  *`doRefresh`: **(Optional)** \- If True, call Refresh() after expanding items..


**`FromPathGetRowNum(path, startRow)`→`Row number or None if row object is not currently visible.`**

    Only works in "path" col modes. 

  *`path`: The object's path
  *`startRow`: **(Optional)** \- Start the search at this row. Default: 0.


**`FromPathsSelectRows(paths, addSelection)`→`list of paths that were not found`**

    Select the rows with the provided paths. Tree will be expanded to selected paths. Only works in "path" col modes. Any paths not found will be ignored. 

  *`paths`: a list of path strings matching paths in the input table
  *`addSelection`: **(Optional)** \- if True, add to current selection. Default: False.


**`CollapseAll(refresh=False)`**

    Set all tree branches to be collapsed.

  *`refresh`: if True,`Refresh`will be run automatically afterward. Otherwise, you must call this function manually to see the effects.


**`ExpandAll(refresh=False)`**

    Set all tree branches to be expanded.

  *`refresh`: if True,`Refresh`will be run automatically afterward. Otherwise, you must call this function manually to see the effects.


**`ToggleExpand(_ID, value=None, root=None_)`**

    Switch the expanded setting of a tree ID branch. Requires a manual`Refresh()`call to update tree. 

  *`ID`: object ID
  *`value`: **(Optional)** \- if provided, switch to that value. Otherwise, toggle value.
  *`root`: **(Optional)** \- for trees with overlapping roots displayed, you can specify which root to expand the given ID in with this argument. Otherwise, ID will toggle in ALL roots.


**`CreateJSONObject(_roots=None_)`→`[OrderedDict](<http://docs.python.org/3.5/library/collections.html?highlight=ordereddict#collections.OrderedDict>)`**

    Create a JSON compatible Python object from tree data, starting at the given roots. **Note:** this only works in JSON Input Mode. 

  *`roots`**(Optional)** \- a list of IDs that will be the root nodes of the Python object. If not provided, the entire tree will be used.


**`CreateJSONText(_roots=None_)`→`JSON text`**

    Create JSON text from tree data, starting at the given roots. **Note:** this only works in JSON Input Mode. 

  *`roots`**(Optional)** \- a list of IDs that will be the root nodes of the JSON text object. If not provided, the entire tree will be used.


**`GetObjectFromID(_ID_)`→`row object`**

    Get row object. This method does use the getObjectFromID callback. 

  *`ID`**(Optional)** \- the unique object identifier used by treeLister (often a path).


**`GetIDFromObject(_obj_)`→`ID`**

    Get ID. This method does use the getIDFromObject callback. 

  *`obj`**(Optional)** \- the row object held by the treeLister.

# Drag/Drop

The treeLister uses standard [List COMP drag/drop callbacks](<./List_COMP.htm#Drag.2FDrop> "List COMP").
