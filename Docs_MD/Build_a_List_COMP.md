# Build a List COMP

## Overview  
  
This document explains the finer points of building a [List COMP](<./List_COMP.md> "List COMP"). It is assumed the reader already has an understanding of the [Python](<./Python.md> "Python") language. [List COMP](<./List_COMP.md> "List COMP") is controlled by callbacks, which can be found in the DAT that is docked to it on creation. 

## Callbacks Stages

The [List COMP](<./List_COMP.md> "List COMP") runs its init callbacks when the Reset parameter is pulsed or on load. These init functions are in place to let the user assign Table, Row, Col or Cell specific attributes which determine the layout and look of the List. The four init functions are called in this order: 

  *`onInitTable(comp, attribs)`*`onInitCol(comp, col, attribs)`*`onInitRow(comp, row, attribs)`*`onInitCell(comp, row, col, attribs)`Once initialized the following callback functions are run on specific events: 

  *`onRollover(comp, row, col, coords, prevRow, prevCol, prevCoords)`is called when a mouse rolls over a cell
  *`onSelect(comp, startRow, startCol, startCoords, endRow, endCol, endCoords, start, end)`is called when a mouse is clicked while over a cell
  *`onRadio(comp, row, col, prevRow, prevCol)`*`onFocus(comp, row, col, prevRow, prevCol)`*`onEdit(comp, row, col, val)`## Building a simple [List COMP](<./List_COMP.md> "List COMP") with a [Folder DAT](<./Folder_DAT.md> "Folder DAT") as content source

Lets assume you want to display the content of a [Folder DAT](<./Folder_DAT.md> "Folder DAT") with the ability to highlight rows you are rolling over. Lets also assume that clicking on a row will change the rows layout as well and run a custom script which takes the row and column as an argument. As a requirement, the first row should act as a header row with a different layout then the rest. For this example it is assumed that the [Folder DAT](<./Folder_DAT.md> "Folder DAT") is 5 columns wide and located parallel to the [List COMP](<./List_COMP.md> "List COMP"). 

When dealing with the [List COMP](<./List_COMP.md> "List COMP") you have to be aware of the fact that its flexibility comes with a responsibility of the creator to manage states as well. This means that while [List COMP](<./List_COMP.md> "List COMP") is running callbacks as mentioned earlier, you will have to make sure that you save the Lists current state in appropriate ways. For example when a row changes its layout on rollover, the callbacks will have to make sure to change the layout back to its default look once the mouse leaves the row. Its proven very useful to save the required states in Python lists or dictionaries as [Storage](<http://www.derivative.ca/wiki088/index.php?title=OP_Class#Storage>)

In the [List COMP](<./List_COMP.md> "List COMP") parameters on the List page, change the Rows and Columns parameter to reflect the [Folder DAT](<./Folder_DAT.md> "Folder DAT") size and enable the Lock First Row parameter. On the Layout parameter page, change the Width parameter to 900. 

Open the docked callbacks [Text DAT](<./Text_DAT.md> "Text DAT") for editing. For the`initRow`function enter this to specify each rows`bgColor`and hit the [List COMP](<./List_COMP.md> "List COMP") Reset parameter to see the changes: 
[code] 
    def onInitRow(comp, row, attribs):
    	# if this is the first row make the background slightly red, otherwise keep it grey
    	if row == 0:
    		bgColor = [0.4,0.2,0.2,1]
    	else:
    		bgColor = [0.2,0.2,0.2,1]
    
    	# assign the bgColor to the rows attributes
    	attribs.bgColor = bgColor
    
    	return
    
[/code]

Now in the`initCell`function we will specify each cells content and hit the [List COMP](<./List_COMP.md> "List COMP") Reset parameter to see the changes: 
[code] 
    def onInitCell(comp, row, col, attribs):
    	# grab the cell content from the Folder DAT
    	cellContent = op('../folder1')[row,col].val
    
    	# assign the text from the Folder DAT to the cell attribute
    	attribs.text = cellContent
    
    	return
    
[/code]

Right away we see the need to appropriately size the column width which we can do in the initCol function. Additionally we'll set the first column to be able to stretch, so that when we increase the [List COMP](<./List_COMP.md> "List COMP") width, the first column will adjust to that size while the rest of the columns stay the same. The initial width given to the stretchy column serves as it's minimal width. After editing hit the [List COMP](<./List_COMP.md> "List COMP") Reset parameter to see the changes. 
[code] 
    def onInitCol(comp, col, attribs):
    	# specify each columns width in a list
    	colWidth = [150,150,250,90,90]
    
    	# specify which column is stretchable in a list
    	stretch = [1,0,0,0,0]
    
    	# assign the width and stretch to the column attributes
    	attribs.colWidth = colWidth[col]
    	attribs.colStretch = stretch[col]
    
    	return
    
[/code]

We can add further formatting to the [List COMP](<./List_COMP.md> "List COMP") in a general way via the`initTable`function and hit the [List COMP](<./List_COMP.md> "List COMP") Reset parameter to see the changes: 
[code] 
    def onInitTable(comp, attribs):
    	# set every cells justify to be center left
    	attribs.textJustify = JustifyType.CENTERLEFT
    
    	# set every cells bottom border to a slight blue
    	attribs.bottomBorderOutColor = [0.2,0.2,0.6,1]
    
    	return
    
[/code]

To change the look of a row when rolling over, edit the rollover callback function. The rollover callback function is called on and while your mouse is moving over a cell. Therefor when changing the layout of a row we should in this case compare the previous with the current rollover row and only change the bgColor when they are different. When rolling out of or into a [List COMP](<./List_COMP.md> "List COMP") the arguments for row, col, prevrow and prevcol will be -1 respectively. 
[code] 
    def onRollover(comp, row, col, coords, prevRow, prevCol, prevCoords):
    	# make sure to only change the layout if row and prevRow are different
    	if row != prevRow:
    
    		# we don't want to change the header row so test for row being larger then 0
    		# this also takes care of when rolling out of the List where row would return -1
    		if row > 0:
    			rowAttribs = comp.rowAttribs[row]
    			rowAttribs.bgColor = [0.2,0.4,0.2,1]
    
    		# same as before, we check that prevRow is not the header row and
    		# we are not entering the List from the outside
    		if prevRow > 0:
    			rowAttribs = comp.rowAttribs[prevRow]
    			rowAttribs.bgColor = [0.2,0.2,0.2,1]
    
    	return
    
[/code]

To achieve a momentary click layout change on the [List COMP](<./List_COMP.md> "List COMP") we can use the select callback in a similar way as we used the rollover callback. The select callback additionally receives a start and end argument with start being True on mouse down and end being True on mouse up. As your mouse can move around the [List COMP](<./List_COMP.md> "List COMP") while the mouse is down, you also receive start and end row/col information. As we have no information on which row was previously selected, we will have to save the selected row in storage: 
[code] 
    def onSelect(comp, startRow, startCol, startCoords, endRow, endCol, endCoords, start, end):
    	# execute this on mouse down
    	if start and startRow > 0:
    		# get the row attributes for the clicked on row
    		# and change the bgColor
    		rowAttribs = comp.rowAttribs[startRow]
    		rowAttribs.bgColor = [0.2,0.6,0.4,1]
    
    		# save the startRow in storage so we can revert the layout changes on mouse up
    		comp.store('prevSelect',startRow)
    
    		# run a script and pass row and column as an argument
    		op('../myScript').run(startRow, startCol)
    	
    	# execute this on mouse up
    	elif end:
    		# get the previous selected row from storage
    		prevSelRow = comp.fetch('prevSelect',None)
    
    		# if there is a previously selected row change the layout back to default
    		if prevSelRow:
    			rowAttribs = comp.rowAttribs[prevSelRow]
    
    			# if my mouse is still over the previously selected row, change it's layout to the rollover bg
    			# else change it to the default look
    			if startRow == endRow:
    				bgColor = [0.2,0.4,0.2,1]
    			else:
    				bgColor = [0.2,0.2,0.2,1]
    
    			# assign the color to the rows bgColor attribute
    			rowAttribs.bgColor = bgColor
    
    		# remove the previously selected row from storage
    		comp.unstore('prevSelect')
    
    	return
    
[/code]

## Using a Python Dictionary as content for the [List COMP](<./List_COMP.md> "List COMP")

With the cell text content being assigned via the text attribute, we can also get data from structures like Lists or Dictionaries. For this example we will assume that our content dictionary has following structure: 
[code] 
    myDict = {
    	'header':[
    		{'id':'name','label':'Name'},
    		{'id':'extension','label':'Extension'},
    		{'id':'type','label':'Type'},
    		{'id':'size','label':'Size'}
    	],
    	'content':[
    		{'name':'MyList.toe','extension':'toe','type':'TouchDesigner File','size':184666},
    		{'name':'MyImage.jpg','extension':'jpg','type':'Image File','size':184326},
    		{'name':'MyList1.toe','extension':'toe','type':'TouchDesigner File','size':184632},
    		{'name':'MyList2.toe','extension':'toe','type':'TouchDesigner File','size':184536}
    	]
    }
    
[/code]

The header key holds the information for the first row while the content key holds all other rows text. In order to gain access to the dictionary from the [List COMP](<./List_COMP.md> "List COMP") we will store this dictionary as an [Dependency Class](<./Dependency_Class.md> "Dependency Class") object to the [List COMP](<./List_COMP.md> "List COMP"). 
[code] 
    import TDStoreTools # see below
    
    myListCOMP = op('/project1/myListCOMP')
    myListCOMP.store('contentDict', TDStoreTools.DependDict(myDict))
    
[/code]

To display as many Rows as there are items in the stored Dictionary, we'll change the [List COMPs](<./List_COMP.md> "List COMP") Row parameter to: 
[code] 
    len(me.fetch('contentDict',{'content':[]}))+1
    
[/code]

Similarly for the Columns we will look at the size of the header dictionary: 
[code] 
    len(me.fetch('contentDict',{'header':[]}))
    
[/code]

The second argument to the fetch Method is the default which will be returned in case the stored item is not found. 

For the cells to display the correct content, we will need to fetch the stored dictionary in the initCell callback function and depending on row and column fetch the right entry from the content dictionary: 
[code] 
    def onInitCell(comp, row, col, attribs):
    	contentDict = comp.fetch('contentDict',None)
    	if contentDict:
    		header = contentDict['header'][col]
    		if row == 0:
    			attribs.text = header['Label']
    		else:
    			id = header['id']
    			rowContent = contentDict[row-1]
    			attribs.text = rowContent[id]
    
    	return
    
[/code]

As we are using a [Dependable Collection](<./TDStoreTools.htm#Deeply_Dependable_Collections> "TDStoreTools") object, with every update we make to the dictionary, the change will also be shown in the [List COMP](<./List_COMP.md> "List COMP")
[code] 
    myListCOMP = op('/project1/myListCOMP')
    contentDict = myListCOMP.fetch('contentDict',None)
    newItem = {'name':'someFile.toe','extension':'toe','type':'TouchDesigner File','size':932753}
    contentDict['content'].append(newItem)
    
[/code]
