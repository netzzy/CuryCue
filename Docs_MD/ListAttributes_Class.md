# ListAttributes Class

The ListAttributes class describes a set of [list attribute objects](<./ListAttribute_Class.md> "ListAttribute Class") for cells, rows, columns or table. It can be accessed from a [List Component](<./ListCOMP_Class.md> "ListCOMP Class"). 

Access to individual List Attributes depends on what type: row, col, or cell: 
[code] 
    rowAttribs = op('list1').rowAttribs		# get the ListAttributes object for rows
    print(len(rowAttribs))					# number of rows 
    print(rowAttribs[0].bgColor)			# rows are accessed by row #. 
    										# This prints the background color settings for the first row
    
    colAttribs = op('list1').colAttribs		# get the ListAttributes object for columns
    print(len(colAttribs))					# number of columns 
    print(colAttribs[0].bgColor)			# cols are accessed by column #. 
    										# This prints the background color settings for the first column
    
    cellAttribs = op('list1').cellAttribs	# get the ListAttributes object for columns
    print(len(cellAttribs))					# total number of cells 
    print(colAttribs[0,2].bgColor)			# cells are accessed by [row, col]. 
    										# This prints the background color settings for the cell in the first row, third column
    
[/code]

**Note:** The attributes above are the settings for List Component's hierarchical layout technique. This means that cell settings override row settings, which override column settings, which override table settings. If you want to know the final value in a given cell, use`listCOMP.displayAttribs[row, col]`. 

## Members

No operator specific members. 

## Methods

No operator specific methods. 

  
TouchDesigner Build: Latest\n2021.100002018.28070before 2018.28070
