# Palette:opBrowser
1. Path  
  2. Control buttons
  3. Tree pane
  4. Viewer pane
  5. Parameters pane

## 

Summary

The **opBrowser** Custom Component provides a range of network browsing, viewing, and parameter editing capabilities. It can be used as a standalone browser or embedded into other UI's. All configuration features are controlled by custom parameters and can be made accessible or not in the browser UI. 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[Palette/opBrowser Ext](</index.php?title=Palette/opBrowser_Ext&action=edit&redlink=1> "Palette/opBrowser Ext \(page does not exist\)")

## 

Parameters - Browser Page

These parameters are general options for the Browser and Tree 

Component`Component`\- The root component to browse. 

Include Component`Includecomponent`\- Show the`Component`in the browser tree. Otherwise, the top level will be`Component`'s children 

Include Wire Hierarchy`Includewirehierarchy`\- Organize the OP tree using hierarchy created by grey Component wires as well as depth. 

Include Result Parents`Includeresultparents`\- Include the top level OPs in the tree. 

Limit Max Depth`Limitmaxdepth`\- Use maximum depth settings for browser tree. 

Maximum Depth`Maxdepth`\- Maximum component depth in the browser tree. 

Open Window`Openwindow`\- Open browser window 

Close Window`Closewindow`\- Close browser window 

Help`Help`\- Open this help page 

Version`Version`**(Read Only)** \- Browser version (for internal use) 

## 

Parameters - Filters Page

These filters apply to the browser tree and generally duplicate those in [OP Find DAT](<./OP_Find_DAT.md> "OP Find DAT"). Uses TouchDesigner style [pattern matching](<./Pattern_Matching.md> "Pattern Matching"). Lists are space delimited and strings with spaces should be in quotes. 

Filter Roots Only`Filterrootsonly`\- Apply filter only to browser tree roots. Otherwise, apply to all roots and branches. 

Object COMPs`Objects`\- Show Object COMPs in browser tree 

Panel COMPs`Panels`\- Show Panel COMPs in browser tree 

Other COMPs`Other`\- Show other COMPs in browser tree 

TOPs`Tops`\- Show TOPs in browser tree 

CHOPs`Chops`\- Show CHOPs in browser tree 

SOPs`Sops`\- Show SOPs in browser tree 

MATs`Mats`\- Show MATs in browser tree 

DATs`Dats`\- Show DATs in browser tree 

Case Sensitive`Casesensitive`\- Filters will be case sensitive. 

Combine Filters`Combinefilters`\- ⊞ \- Defines how the filters on this page are combined 
* All`all`\- All filters must be true 
* Any`any`\- Any filter must be true


Name`Namefilter`\- OPs with this name 

Type`Typefilter`\- OPs of this type (use Python class name) 

Tags`Tagsfilter`\- OPs with one or more of these tags 

DAT Text`Textfilter`\- DATs containing this text 

Par Name`Parnamefilter`\- OPs with parameters that have one of these names. Use Python parameter names. 

Par Value`Parvaluefilter`\- OPs with parameters that have one of these values. 

Par Expression`Parexpressionfilter`\- OPs with this string in their expressions 

Par Non-Default Only`Parnondefaultonly`\- Ps with non-default parameters only 

Lambda Filter Key`Lambdafilterkey`\- A Python lambda filter method, whose argument is the OP to be filtered out or not. For example, to get all OPs whose name starts with "A":`lambda x: x.name.startswith('A')`## 

Parameters - Tree Page

Settings for the browser tree 

Right Click Menu`Rightclickmenu`\- Bring up standard network context menu for OPs on RMB 

Multiple Row Select`Multiplerowselect`\- Allow multiple rows to be selected in tree 

Double Click To Set Component`Doubleclicktosetcomponent`\- Double-click a COMP in the tree to make it the new root Component

Path Column`Pathcolumn`\- Show Path column in tree 

Tags Column`Tagscolumn`\- Show Tags column in tree 

Type Column`Typecolumn`\- Set Type Column to display OP type abbreviations or full OP type name. Turning the column off is also an option. 

Type Column Width`Typecolumnwidth`\- Width of Type column in pixels. 

Viewer Button`Viewerbutton`\- Show Viewer button column in tree 

Parameters Button`Parametersbutton`\- Show Parameters button column in tree 

Network Button`Networkbutton`\- Show Network button column in tree 

Edit Column Definitions`Editcolumndefinitions`\- Open the column definitions table for the browser. See [Lister - column definition table](<./Palette-lister.htm#colDefine_table> "Palette:lister") for more info. 

## 

Parameters - Panes Page

Pane and layout controls. 

Pane Order`Paneorder`\- ⊞ \- Defines the order of panes in the browser. 
* Tree Viewer Parameters`Tree_Viewer_Parameters`\- 
* Tree Parameters Viewer`Tree_Parameters_Viewer`-
* Viewer Tree Parameters`Viewer_Tree_Parameters`-
* Viewer Parameters Tree`Viewer_Parameters_Tree`-
* Parameters Tree Viewer`Parameters_Tree_Viewer`-
* Parameters Viewer Tree`Parameters_Viewer_Tree`-


Pane Configuration`Paneconfiguration`\- ⊞ \- Defines the layout of the browser. 
* Horizontal`Horizontal`\- Left to right 
* Vertical`Vertical`\- Top to bottom
* Split Left`Split_Left`\- Top to bottom on left side, last pane on right
* Split Right`Split_Right`\- First pane on left, then top to bottom on right side
* Split Bottom`Split_Bottom`\- First pane on top, then left to right on bottom
* Split Top`Split_Top`\- Left to right on top, then last pane on bottom


Show Header`Showheader`\- Show the header with Path and control buttons 

Show Viewer`Showviewer`\- Show viewer pane 

Show Parameters`Showparameters`\- Show parameter pane 

Show OP Tree`Showtree`\- Show tree pane 

Show Viewer Button`Showviewerbutton`\- Show viewer display button in header 

Show Parameters Button`Showparametersbutton`\- Show parameter display button in header 

Show OP Tree Button`Showtreebutton`\- Show tree display button in header 

Sizeable Main Orientation`Sizeablemainorientation`\- Show handle for sizing primary orientation 

Sizeable Split Orientation`Sizeablesplitorientation`\- Show handle for sizing secondary orientation 

Knob Size`Knobsize`\- Size of sizing handles 

Tree Min Size`Treeminsize`\- ⊞ \- 

Tree Min Size`Treeminsizew`\- Minimum width and height of tree pane Tree Min Size`Treeminsizeh`-

Viewer Min Size`Viewerminsize`\- ⊞ \- 

Viewer Min Size`Viewerminsizew`\- Minimum width and height of viewer pane Viewer Min Size`Viewerminsizeh`-

Parameters Min Size`Parametersminsize`\- ⊞ \- 

Parameters Min Size`Parametersminsizew`\- Minimum width and height of parameter pane Parameters Min Size`Parametersminsizeh`-

## 

Parameters - Options Page

Other options for the browser 

Edit Settings`Editsettings`\- Open the edit settings window 

Edit Settings Button`Editsettingsbutton`\- Show edit settings button in header 

Allow Viewer Interaction`Allowviewerinteraction`\- Allow interaction in the viewer pane 

Viewer Interaction Button`Viewerinteractionbutton`\- Show allow interaction button in viewer UI 

Path Right Click Menu`Pathrightclickmenu`\- Bring up network context menu when you right-click in Path items 

Set Component With Drop`Setcomponentwithdrop`\- Set`Component`by dropping a COMP onto Path in browser UI 

# 

BrowserExt Extension Class

The **`BrowserExt`** extension provides extended functionality for working with opBrowser. Frequently used promoted members and methods are listed here. A full list can be found using the Python`help()`function. 

## Members`**Component**`| The root component to browse. Same as the`Component`parameter.   
---|---`**CurrentOP**`| The main selected operator. This is the operator that is shown in the Viewer and Parameter panes.`**SelectedPaths**`| A list of the OP paths currently selected in the tree.`**TreeLister**`| **(Read Only)** The [Tree Lister](<./Palette-treeLister.md> "Palette:treeLister") custom component used in the opBrowser.   
  
## Methods

**`OpenToPath(path, doRefresh=True)`→`True if successful, root opened in if already open, otherwise None.`**

    Open tree to the provided path. 

  *`path`: The path to open to
  *`doRefresh`: **(Optional)** \- If True, call Refresh() after expanding items..


**`FromPathGetRowNum(path, startRow)`→`Row number or None if row object is not currently visible.`**

    Get tree lister row number of chosen path. 

  *`path`: The object's path
  *`startRow`: **(Optional)** \- Start the search at this row. Default: 0.


**`FromPathsSelectRows(paths, addSelection)`→`list of paths that were not found`**

    Select the rows with the provided paths. Tree will be expanded to selected paths. Any paths not found will be ignored. 

  *`paths`: a list of path strings matching paths in the input table
  *`addSelection`: **(Optional)** \- if True, add to current selection. Default: False.
