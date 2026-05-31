# Lister Custom COMP Examples

This page contains examples of how to set up a **lister** custom component. They assume a basic knowledge of TouchDesigner and Python.   
  
For full documentation of lister, see: [Lister Custom COMP](<./Palette-lister.md> "Palette:lister"). 

## Example 1 - File Lister

In this example, we will create a very simple lister using only parameters and wires. We will also use a couple of simple Python expressions in associated operators. The end result will be a lister that allows you to choose the file displayed in a movieFileInDAT. 

##### Creating a lister

To create a lister, drag one from the [Palette](<./Palette.md> "Palette") (Derivative>UI folder) into your network. 

##### Creating an input DAT

Any table can be used as an input into lister. For this example, we will use a [Folder DAT](<./Folder_DAT.md> "Folder DAT") because we are making a list of files. Create a Folder DAT in your network to the left of the lister. Change the DAT's Root Folder parameter expression to`app.samplesFolder + '/Map'`. It now contains a list of all the sample maps provided in TouchDesigner. Wire the output of the DAT to the input of the lister. Open a floating viewer of the lister by right-clicking on its node and selecting "View...". 

##### Ordering and selecting data

For this feature to work, you need to change a couple settings on the lister. First, let the lister know that the top row of the table is headers by turning on the Input Table Has Headers parameter. Next, enable column sorting and filtering by turning on the Clickable Header parameter. 

You can now sort rows by clicking on the column labels. Note that your original Folder DAT does not change when you do these things. The DAT is only used to create the original data. 

To select a row, click on it. You can select multiple rows using shift and ctrl clicks. If you turn on the Drag To Reorder Rows parameter, you can rearrange rows by selecting and dragging them. 

##### Filtering data

To filter the lister's data, you can enter a string into its Filter String parameter. It will now only display rows that contain that string in the currently filtered column. To select the filter column, click on the column label. 

##### Controlling a movieFileIn TOP using the lister

In this step, you will create a very simple file selector using the lister. For this example, first turn off a few features. Switch off the following toggle parameters in the lister: Clickable Header, Multiple Row Select, Drag To Reorder Rows. Also, remove any Filter String you have set. The lister data will now stay the same as the original table. 

Create a [Movie File In TOP](<./Movie_File_In_TOP.md> "Movie File In TOP") in your network. Change the TOP's File parameter expression to`op('folder1')[int(op('lister').par.Selectedrows), 1] if op('lister').par.Selectedrows else ''`. 

This little bit of Python selects a cell from the input table that corresponds to the lister's selected row. Select different rows to see this work. **NOTE:** The`if`clause at the end takes care of the case where no rows are selected. 

## Example 2 - Network Lister

In this example, we will create a lister using Python callbacks and the Column Definition (colDefine) table. The end result will be a lister that allows you to select operators in TouchDesigner's root network. 

##### Creating a lister

To create a lister, drag one from the [Palette](<./Palette.md> "Palette") (Derivative>UI folder) into your network. 

##### Populating the lister using onGetRawData callback

Open the lister's callback DAT for editing by clicking its Edit Callbacks parameter. The`onGetRawData`callback populates the lister's row data. It can handle a number of different kinds of data, but in this case we will be using a list of objects. Specifically, we will populate the raw data with an OP object for each row. Put the following code in the callback DAT: 
[code] 
    def onGetRawData(info):
    	return op('/').children
    
[/code]

This returns a list of the root operator's children. The lister will base each row on an item in the list, in this case a TouchDesigner [Operator](<./Operator.md> "Operator") object. Open a floating viewer of the lister by right-clicking its node and selecting "View...". You will see that the autodefine columns feature has created a column of "objects" with a string representation of each operator in the rows. Our next step is to manually define the columns that we want in our lister. 

##### Editing the Column Definition table

To open the Column Definition table, click the lister's Edit Column Definitions parameter. In this table, the first column contains labels and the following columns contain formatting information about each of the lister's columns. Change your table to contain this data: 

To see the effects of these changes, switch off the Autodefine Columns parameter in the lister. It is now using the colDefine table you just set up. Let's take a look at some of the features of this table... 

The **column** row contains a unique name for each column. The **columnLabel** row is the string that will appear above that column in the lister's header. The "*" in the _Operator_ column's _columnLabel_ means to use the _column_ name above. The empty columnLabels in _Select_ and _Delete_ indicate no column label. 

The **sourceData** and **sourceDataMode** rows define what data will be put in this column. The lister is based on a list of OP objects, so the`name`in the Operator column indicates that the lister will use each OP's _name_ member, which is a string, as indicated by the _sourceDataMode_ setting. Both _Select_ and _Delete_ have a`constant`_sourceDataMode_ , so those rows will contain the literal contents of _sourceData_. 

For more details about the various settings in the table, see [colDefine table](<./Palette-lister.htm#colDefine_table> "Palette:lister"). 

##### Creating special looks in the Config COMP

The _Select_ and _Delete_ columns illustrate two ways to create special looks in your lister. Notice that the _Select_ column has a bitmap button and the _Delete_ column has a text button with a differentiated color. Try rolling over and clicking on these columns to see more of their looks. 

In the colDefine table, these unique cell looks are set in the **cellLook** and **topPath**. To see what they refer to, open the **Config COMP** by clicking the lister's Edit Config COMP parameter. In this COMP you will find many customizable features for lister. Among other things, the colDefine table, callbacks DAT, and TOPs that define cell looks are located here. The button, buttonRoll, and buttonPress TOPs define the button look for the _Delete_ column. The btnImage, btnImageRoll, and btnImagePress TOPs define the image to be displayed in the _Select_ column. You can create as many of these custom cell looks and images as you like, using this naming convention. 

For details about the various settings available through the look TOPs, see [Config TOPs](<./Palette-lister.htm#TOPs> "Palette:lister"). 

##### Writing button callbacks

The functionality for buttons is created using Python callbacks. To set this up, open the lister's callbacks DAT. Create the **Select** button's click functionality by adding the following text: 
[code] 
    def onClickSelect(info):
    	op = info['rowData']['rowObject']
    	op.current = True
    
[/code]

The name`onClick`followed by the lister's column name defines the callback for clicks on that column. The 'rowData' item in the info dictionary contains a Python [Ordered Dict](<http://www.blog.pythonlibrary.org/2016/03/24/python-201-ordereddict/>) with items for each column followed by a 'rowObject' item which is the original object provided as raw data for the lister. In this case, 'rowObject' contains the [Operator](<./Operator.md> "Operator") for this row. Setting that operator's`current`member to True selects the operator in the network as if it were clicked on. Open up the root network and click on the Select buttons in the lister to see this effect. Because the _clickOnDrag_ setting is set to on in the colDefine for this column, you can drag the mouse across it with the button down to select different operators as you drag. 

For the **Delete** buttons, enter the following code to illustrate a different approach: 
[code] 
    def onClick(info):
    	if info['col'] == 2:
    		info['ownerComp'].DeleteRows([info['row']])
    
[/code]

In addition to the`onClick<columnName>`callbacks, there is a general`onClick`callback which is called when any cell is clicked. In order to use this for the Delete button, we must first check that it is in that column by testing`info['col']`. If our column is 2, we delete the row from the lister by using its`DeleteRows`method. As you can see, the lister itself is stored in`info['ownerComp']`. Notice that for the sake of a safe example, the Delete button is set up to delete the row from the lister, not to delete the operator from the network. 

For a full list of available lister callbacks, see: [Custom Callbacks](<./Palette-lister.htm#Custom_Callbacks> "Palette:lister"). 

##### Advanced Callbacks and custom pop-up help

The last feature to add to the Network Lister is a pop-up help string showing the path to each operator. This needs to be set up in the`onInitCell`advanced callback. These callbacks are off by default because they are called more often, reducing speed slightly and cluttering the textport when the Print Callbacks parameter is on. Switch on the **Do Advanced Callbacks** parameter on the lister's Advanced page to activate them. Then add the following code to the callbacks DAT: 
[code] 
    def onInitCellOperator(info):
    	if info['row'] > 0:
    		operator = info['rowData']['rowObject']
    		attribs = info['attribs']
    		attribs.help = operator.path
    
[/code]

Here we are again using the column callback technique by appending`Operator`to the`onInitCell`callback name. The first line of the callback checks that the row number is greater than 0 because header rows also get an`onInitCell`callback. If we are not in the header row, we alter the cell's`attribs.help`member to hold the operator's path. For info about the many things that can be set in attribs, see: [ListCOMP Class](<./ListCOMP_Class.htm#Callbacks> "ListCOMP Class").
