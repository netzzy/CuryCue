# errorDAT Class

  
This class inherits from the [ DAT class](<./DAT_Class.md> "DAT Class"). It references a specific [Error DAT](<./Error_DAT.md> "Error DAT"). 

## Members

No operator specific members. 

## Methods

No operator specific methods. 

## Callbacks

The following python callbacks are associated with this operator. 
[code] 
    # me - this DAT.
    # 
    # dat - the DAT that received the error
    # rowIndex - the row number the error was placed into
    # message - the error message
    # absFrame - the absolute frame at which the error occured
    # frame - the local frame at which the error occured
    # severity - describes the level of error (0=info, 1=warning, 2=error, 3=fatal)
    # type - describes the family of error
    # source - the operator that generated the error
    
    def onError(dat, rowIndex, message, absFrame, frame, severity, type, source):
    	return
    
[/code]

# DAT Class

## Members`export`→`bool`: 

> Get or set [Export Flag](<./Export_Flag.md> "Export Flag")`module`→`'module'`**(Read Only)** : 

> Retrieve the contents of the DAT as a module. This allows for functions in the module to be called directly. E.g n.module.function(arg1, arg2)`numRows`→`int`**(Read Only)** : 

> Number of rows in the DAT table.`numCols`→`int`**(Read Only)** : 

> Number of columns in the DAT table.`text`→`str`: 

> Get or set contents. Tables are treated as tab delimited columns, newline delimited rows. **Note:** newlines will be removed from cell contents in this format, so multi-line text in cells is not supported. Use the`csv`member below instead.`csv`→`str`: 

> Get or set contents using [csv](<https://en.wikipedia.org/wiki/Comma-separated%20values>) file format. Unlike the`text`member, this does support multi-line text in cells.`editingFile`→`str`**(Read Only)** : 

> The path to the current file used by external editors.`isTable`→`bool`**(Read Only)** : 

> True if the DAT contains table formatted data.`isText`→`bool`**(Read Only)** : 

> True if the DAT contains text formatted data. (ie, not table formatted).`isEditable`→`bool`**(Read Only)** : 

> True if the DAT contents can be edited (Text DATs, Table DATs, locked DATs etc).`locals`→`dict`**(Read Only)** : 

> Local dictionary used during python execution of scripts in this DAT. The dictionary attribute is read only, but not its contents. Its contents may be manipulated directly with scripts, or with an [Examine DAT](<./Examine_DAT.md> "Examine DAT").`jsonObject`→`dict`**(Read Only)** : 

> Parses the DAT as json and returns a python object.`flush()`→`None`: 

> Dummy function required to redirect stdout to DATs.`isatty()`→`False`: 

> Required to redirect stdout to DATs.

## Methods`run(*args, endFrame=False, fromOP=None, asParameter=False, group=None, delayFrames=0, delayMilliSeconds=0, wallTime=False, delayRef=None)`→`td.Run`: 

> [Run](<./Run_Class.md> "Run Class") the contents of the DAT as a script, returning a Run object which can be used to optionally modify its execution. 
> 
>   * args - (Optional) Any number of arguments that will be made available to the script in a local tuple named args.
>   * endFrame - (Keyword, Optional) If set to True, the execution will be delayed until the end of the current frame.
>   * fromOP - (Keyword, Optional) Specifies an optional [operator](<./OP_Class.md> "OP Class") from which the execution will be run relative to.
>   * asParameter - (Keyword, Optional) When fromOP used, run relative to a parameter of fromOP.
>   * group - (Keyword, Optional) Can be used to specify a group label string. This label can then be used with the [td.runs](<./Runs_Class.md> "Runs Class") object to modify its execution.
>   * delayFrames - (Keyword, Optional) Can be used to delay the execution a specific amount of frames.
>   * delayMilliSeconds - (Keyword, Optional) Can be used to delay the execution a specific amount of milliseconds. This value is rounded to the nearest frame.
>   * wallTime - (Keyword, Optional) Setting this to True results in the delay options being based on actual elapsed time instead of elapsed frames.
>   * delayRef - (Keyword, Optional) Specifies an optional [operator](<./OP_Class.md> "OP Class") which is controlled by a different [Time Component](<./Time_COMP.md> "Time COMP"). If your own local timeline is paused, you can point to another timeline to ensure this script will still execute for example. If no delayRef is provided, this DAT will be used.
> 

[code] 
    # grab DAT
    n = op('text1')
    # run the DAT
    n.run()
    # run the data with some arguments
    r.run('firstArgIsString', secondArgIsVariable)
    
[/code]`save(filepath, append=False, createFolders=False)`→`str`: 

> Saves the content of the DAT to the file system. Returns the file path that it was saved to. 
> 
>   * filepath - (Optional) The path and filename to save the file to. If this is not given then a default named file will be saved to project.folder
>   * append - (Keyword, Optional) If set to True and the format is txt, then the contents are appended to the existing file.
>   * createFolders - (Keyword, Optional) If True, it creates the not existent directories provided by the filepath.
> 

[code]
>     name = n.save() #save in native format with default name
>     n.save('output.txt') #human readable format without channel names
>     n.save('C:/Desktop/myFolder/output.txt', createFolders=True)  # supply file path and createFolder flag
>     
[/code]`write(args)`→`str`: 

> Append content to this DAT. Can also be used to implement DAT printing functions. 
[code]
>     # grab DAT
>     n = op('text1')
>     # append message directly to DAT
>     n.write('Hello World')
>     # use print method
>     print('Hello World', file=n)
>     
[/code]`detectLanguage(setLanguage=False)`→`str`: 

> Returns the result of attempting to auto-detect the programming language in the DAT based on the contained text. 
> 
>   * setLanguage - (Keyword, Optional) If True sets the language parameters on the DAT appropriately
> 

### Modifying Content

The following methods can be used to modify the contents of a DAT. This can be done when the DAT is a [Text DAT](<./Text_DAT.md> "Text DAT"), or [Script DAT](<./Script_DAT.md> "Script DAT") for example, or a DAT that is [Locked](</index.php?title=Lock&action=edit&redlink=1> "Lock \(page does not exist\)").`clear(keepSize=False, keepFirstRow=False, keepFirstCol=False)`→`None`: 

> Remove all rows and columns from the table. 
> 
>   * keepSize - (Keyword, Optional) If set to True, size is unchanged, but entries will be set to blank, dependent on other options below.
>   * keepFirstRow - (Keyword, Optional) If set to True, the first row of cells are retained.
>   * keepFirstCol - (Keyword, Optional) If set to True, the first column of cells are retained.
> 

[code]
>     n.clear() #remove all rows and columns
>     n.clear(keepSize=True) #set all table cells to blank
>     n.clear(keepFirstRow=True) #remove all rows, but keep the first
>     n.clear(keepFirstRow=True, keepFirstCol=True) #keep the first row, first column, and set remaining cells to blank
>     
[/code]`copy(DAT)`→`None`: 

> Copy the text or table from the specified [DAT](<./DAT.md> "DAT") operator. 
> 
>   * OP - The DAT operator whose contents should be copied into the DAT.
> 

### Modifying Text Content

When the DAT is not a table, but a block of text, its contents can be simply accessed through its text member. 
[code] 
    t = op('merge1').text
    op('text2').text = 'merge1 contains:' + t
    
    op('text3').text = "Hello there!"
    
[/code]

### Modifying a Single Cell of a Table

Using`DAT[_row_ , _column_]`where _``row`,`column``_ specifies which cell to modify. The row and column may be integer numbers starting at 0, or strings which are the column names or row names (in row 0 or column 0 respectively): 
[code] 
    op('table1')['Monday',1] = 'day1'
    
    tab = op('table1')
    tab[0,0] = 'corner'
    tab[1,'select'] = 'yes'
    tab['Monday',1] = 'day1'
    
[/code]

### Modifying Table Content

The following methods can be used to modify the contents of a table type DAT containing rows and columns. This can be done when the DAT is a basic [Table DAT](<./Table_DAT.md> "Table DAT"), or [Script DAT](<./Script_DAT.md> "Script DAT"). It can also be used to append rows to FIFO-style DATs such as the [Serial DAT](<./Serial_DAT.md> "Serial DAT").`appendRow(vals, nameOrIndex, sort=None)`→`int`: 

> Append a row to the end of the table, or after the specified row name/index. Returns the integer index of the new row. 
> 
>   * vals - (Optional) If specified, will fill the row with the given values. It should be a list of items that can be expressed as strings. Each item will be copied to one [cell](<./Cell_Class.md> "Cell Class").
>   * nameOrIndex - (Optional) If specified will determine where the new row will be appended. If it's a numeric value it represents the numeric index of the row. If it is a string it represents a row label.
>   * sort - (Keyword, Optional) If specified will determine the column to keep sorted after the insertion. If it's a numeric value it represents the numeric index of the column. If it is a string it represents a column label.
> 

[code]
>     n.appendRow()
>     n.appendRow( [1,2,3], 'January' )  #append with values (1,2,3) after the row labelled 'January'
>     n.appendRow( [1,2,3], 5 )  #append row with values (1,2,3) after the row 5.
>     n.appendRow( [1,2,3], sort='Month' )  #append row with values (1,2,3) keeping column 'Month' sorted.
>     
[/code]`appendRows(vals, nameOrIndex, sort=None)`→`int`: 

> Append rows to the end of the table, or after the specified row name/index. Returns the integer of the last row appended. 
> 
>   * vals - (Optional) If specified, will fill the rows with the given values. It should be a list of lists of items that can be expressed as strings. Each item will be copied to one cell.
>   * nameOrIndex - (Optional) If specified will determine where the new row will be appended. If it's a numeric value it represents the numeric index of the row. If it is a string it represents a row label.
>   * sort - (Keyword, Optional) If specified will determine the column to keep sorted after the insertion. If it's a numeric value it represents the numeric index of the column. If it is a string it represents a column label.
> 

[code]
>     n.appendRows()
>     n.appendRows( [[1,2,3],[4,5,6,7]], 'January' )  #after the row labelled 'January append 2 rows: first one with values (1,2,3), then one with values (4,5,6,7)
>     n.appendRows( [[1,2,3]], 5 )  # after row 5 append one row with values (1,2,3).
>     n.appendRows( [1,2,3] )  # append 3 rows with values 1, 2, 3 respectively.
>     
[/code]`appendCol(vals, nameOrIndex, sort=None)`→`int`: 

> Append a column to the end of the table. See appendRow for similar usage.`appendCols(vals, nameOrIndex, sort=None)`→`int`: 

> Append columns to the end of the table. See appendRows for similar usage.`insertRow(vals, nameOrIndex, sort=None)`→`int`: 

> Insert a row to the beginning of the table or before the specified row name/index. See DAT.appendRow() for similar usage.`insertCol(vals, nameOrIndex, sort=None)`→`int`: 

> Insert a column to the beginning of the table or before the specified row name/index. See DAT.appendRow() for similar usage.`replaceRow(nameOrIndex, vals, entireRow=True)`→`int`: 

> Replaces the contents of an existing row. 
> 
>   * nameOrIndex - Specifies the row that will be replaced. If it's a numeric value it represents the numeric index of the row. If it is a string it represents a row label.
>   * vals - (Optional) If specified, will overwrite the row with the given values. It should be a list of lists of items that can be expressed as strings. Each item will be copied to one cell.
>   * entireRow - (Keyword, Optional) If True, overwrites every cell in the specified row. If False, will only overwrite as many cells in the row as there are items in vals.
> 

[code]
>     n.replaceRow(0) # will empty all the cells in row 0 (ie. replaced with nothing)
>     n.replaceRow('January', ['January', 1,2,3])  # the row 'January' will be replaced with the list of 4 items.
>     n.replaceRow(2, [1,2,3], entireRow=False)  # at row 2 the 3 items will replace the first 3 items in the row.
>     
[/code]`replaceCol(nameOrIndex, vals, entireCol=True)`→`int`: 

> Replaces the contents of an existing column. See DAT.replaceRow for similar usage.`deleteRow(nameOrIndex)`→`None`: 

> Delete a single row at the specified row name or index. 
> 
>   * nameOrIndex - May be a string for a row name, or numeric index for rowindex.
>`deleteRows(vals)`→`None`: 

> Deletes multiple rows at the row names or indices specified in vals. 
> 
>   * vals - If specified, will delete each row given. It should be a list of items that can be expressed as strings. If no vals is provided deleteRows does nothing.
>`deleteCol(nameOrIndex)`→`None`: 

> Delete a single column at the specified column name or index. 
> 
>   * nameOrIndex - May be a string for a column name, or numeric index for column index.
>`deleteCols(vals)`→`None`: 

> Deletes multiple columns at the column names or indices specified in vals. 
> 
>   * vals - If specified, will delete each column given. It should be a list of items that can be expressed as strings. If no vals is provided deleteCols does nothing.
>`setSize(numrows, numcols)`→`None`: 

> Set the exact size of the table. 
> 
>   * numrows - The number of rows the table should have.
>   * numcols - The number of columns the table should have.
>`scroll(row, col)`→`None`: 

> Bring current DAT viewers to the specified row and column 
> 
>   * row - Row to scroll to.
>   * col - (Optional) Column to scroll to for tables.
> 

### Accessing Table Content`[rowNameOrIndex, colNameOrIndex]`→`td.Cell`: 

> [cells](<./Cell_Class.md> "Cell Class") in a table may be accessed with the`[]`subscript operator. 
> 
> The NameOrIndex may be an exact string name, or it may be a numeric index value. [Pattern Matching](<./Pattern_Matching.md> "Pattern Matching") is _not_ supported. 
> 
>   * rowNameOrIndex - If a string it specifies a row name, if it's numeric it specifies a row index.
>   * colNameOrIndex - If a string it specifies a column name, if it's numeric it specifies a column index.
> 

[code]
>     c = n[4, 'June']
>     c = n[3, 4]
>     
[/code]`cell(rowNameOrIndex, colNameOrIndex, caseSensitive=True, val=False)`→`td.Cell | str | None`: 

> Find a single [cell](<./Cell_Class.md> "Cell Class") in the table, or None if none are found. 
> 
>   * rowNameOrIndex/colNameOrIndex - If a string it specifies a row/column name. If it's numeric it specifies a row/column index. [Pattern Matching](<./Pattern_Matching.md> "Pattern Matching") is supported for strings.
>   * caseSensitive - (Optional) Specifies whether or not case sensitivity is used.
>   * val - (Keyword, Optional) If set to true, returns list of cell item strings instead of list of Cell Class items.
> 

[code]
>     c = n.cell(5, 'June') #Return a cell under row 5, column 'June'.
>     c = n.cell('A*', 2) #Find a cell under any row beginning with an A, in column 2.
>     c = n.cell('A*', 2, val=True) #Return the str type of the found cell
>     
[/code]`cells(rowNameOrIndex, colNameOrIndex, caseSensitive=True, val=False)`→`list`: 

> Returns a (possibly empty) list of [cells](<./Cell_Class.md> "Cell Class") that match the given row/column names or indices. See DAT.cell method for similar usage.`findCell(pattern, rows=None, cols=None, valuePattern=True, rowPattern=True, colPattern=True, caseSensitive=False, val=False)`→`Cell | str | None`: 

> Returns a cell that matches the given pattern and row/column names or indices or None if no match is found. 
> 
>   * pattern - The pattern to match a cell.
>   * rows (Keyword, Optional) - If specified, looks for cell only in the specified rows. Must be specified as a list.
>   * cols (Keyword, Optional) - If specified, looks for cell only in the specified columns. Must be specified as a list.
>   * valuePattern, rowPattern, colPattern(Keyword, Optional) - If specified and set to False, disables pattern matching for a cell, rows or columns.
>   * caseSensitive(Keyword, Optional) - Cell matching is case sensitive if set to true.
>   * val - (Keyword, Optional) If set to true, returns list of cell item strings instead of list of Cell Class items.
> 

[code]
>     # given a table "table1":
>     # # id # fruit      # color  #
>     # # 0  # Strawberry # Red    #
>     # # 1  # Banana     # Yellow #
>     # # 2  # Cucumber   # Green  #
>     # # 3  # Blueberry  # Blue   #
>     # # 4  # Clementine # Orange #
>     # # 5  # *Fruit     # Green  #
>     
>     # t is the reference to a table DAT
>     t = op('/project1/table1')
>     
>     # search for any cell with the value 'Red'
>     # will return type:Cell cell:(1, 2) owner:/project1/table1 value:Red
>     t.findCell('Red')
>     
>     # search for any cell in the column 'fruit' with a value starting with 'blue'
>     # will return type:Cell cell:(4, 1) owner:/project1/table1 value:Blueberry
>     t.findCell('blue*',cols=['fruit'])
>     
>     # search for any cell in the column 'fruit' with a value starting with 'blue'
>     # with case-sensitive search enabled
>     # will return None
>     t.findCell('blue*',cols=['fruit'], caseSensitive=True)
>     
>     # will return type:Cell cell:(0, 1) owner:/project1/table1 value:fruit
>     # as the '*' in the search pattern will be used to pattern match, the 
>     # first row of the second column is matched
>     t.findCell('*Fruit')
>     
>     # will return type:Cell cell:(6, 1) owner:/project1/table1 value:*Fruit
>     # as pattern matching for the search pattern is disabled
>     # hence the '*' is not interpreted as a pattern but a string to look for
>     t.findCell('*Fruit', valuePattern=False)
>     
>     # search for any cell with the pattern '*Fruit'
>     # will return the str of the found cell, say 'SweetFruit'
>     t.findCell('*Fruit', val=True)
>     
[/code]`findCells(pattern, rows=None, cols=None, valuePattern=True, rowPattern=True, colPattern=True, val=False)`→`list`: 

> Returns a (possibly empty) list of cells that match the given patterns and row/column names or indices. 
> 
>   * pattern - The pattern to match cells.
>   * rows (Keyword, Optional) - If specified, looks for cells only in the specified rows.
>   * cols (Keyword, Optional) - If specified, looks for cells only in the specified columns.
>   * valuePattern, rowPattern, colPattern(Keyword, Optional) - If specified, overrides pattern matching for cells, rows or columns.
>   * caseSensitive(Keyword, Optional) - Cell matching is case sensitive if set to true.
>   * val - (Keyword, Optional) If set to true, returns list of cell item strings instead of list of Cell Class items.
>`row(*nameOrIndexes, caseSensitive=True, val=False)`→`List[Cell]`: 

> Returns a list of [cells](<./Cell_Class.md> "Cell Class") from the first row matching the name/index, or None if nothing is found. 
> 
>   * nameOrIndexes - Include any number of these. If a string it specifies a row name, if it's numeric it specifies a row index. [Pattern Matching](<./Pattern_Matching.md> "Pattern Matching") is supported.
>   * caseSensitive - (Optional) Specifies whether or not case sensitivity is used.
>   * val - (Optional) If set to true, returns list of cell item strings instead of list of Cell Class items.
> 

> 
> See DAT.col() for similar usage. 
[code] 
>     r = op('table1').row(3, caseSensitive=False)
>     r = op('table1').row('June')
>     r = op('table1').row('A*', 'B*') #returns first row beginning with A or B
>     r = op('table1').row('June', val=True) #returns list of all strings stored under the row 'June'
>     
[/code]`rows(*nameOrIndexes, caseSensitive=True, val=False)`→`List[List[Cell]]`: 

> Returns a (possibly empty) list of rows (each row being a list of cells). If no arguments are given it returns all rows in the table. 
> 
>   * nameOrIndexes - (Optional) Include any number of these. If a string it specifies a row name, if it's numeric it specifies a row index. [Pattern Matching](<./Pattern_Matching.md> "Pattern Matching") is supported.
>   * caseSensitive - (Optional) Specifies whether or not case sensitivity is used.
>   * val - (Optional) If set to true, returns list of cell item strings instead of list of Cell Class items.
> 

> 
> See DAT.rows() for similar usage. 
[code] 
>     for r in op('table1').rows():
>     	# do something with row 'r'
>     
>     for r in op('table1').rows(val=True):
>         # do something with the strings values of the row 'r'
>     
[/code]`col(*nameOrIndexes, caseSensitive=True, val=False)`→`list`: 

> Returns a list of [cells](<./Cell_Class.md> "Cell Class") from the first col matching the name/index, or None if nothing is found. 
> 
>   * nameOrIndexes - Include any number of these. If a string it specifies a column name, if it's numeric it specifies a column index. [Pattern Matching](<./Pattern_Matching.md> "Pattern Matching") is supported.
>   * caseSensitive - (Optional) Specifies whether or not case sensitivity is used.
>   * val - (Optional) If set to true, returns list of cell item strings instead of list of Cell Class items.
> 

[code]
>     r = op('table1').col(3, caseSensitive=False)
>     r = op('table1').col('June')
>     r = op('table1').col('A*', 'B*') #returns first column beginning with A or B
>     r = op('table1').col('June', val=True) #returns list of all strings stored under the column 'June'
>     
[/code]`cols(*nameOrIndexes, caseSensitive=True, val=False)`→`List[List[Cell]]`: 

> Returns a (possibly empty) list of columns (each being a list themselves). If no arguments are given then all columns in the table are returned. 
> 
>   * nameOrIndexes - (Optional) Include any number of these. If a string it specifies a column name, if it's numeric it specifies a column index. [Pattern Matching](<./Pattern_Matching.md> "Pattern Matching") is supported.
>   * caseSensitive - (Optional) Specifies whether or not case sensitivity is used.
>   * val - (Optional) If set to true, returns list of cell item strings instead of list of Cell Class items.
> 

[code]
>     for c in op('table1').cols():
>     	# do something with each column 'c'
>     
>     for c in op('table1').cols(val=True):
>         # do something with the string values in each column 'c'
>     
[/code]

# OP Class

## Members

### General`valid`→`bool`**(Read Only)** : 

> True if the referenced operator currently exists, False if it has been deleted.`id`→`int`**(Read Only)** : 

> Unique id for the operator. This id can also be passed to the op() and ops() shortcuts. Id's are not consistent when a file is re-opened, and will change if the OP is copied/pasted, changes OP types, deleted/undone. The id will not change if the OP is renamed though. Its data type is integer.`supported`→`bool`**(Read Only)** : 

> True if supported on the current Operating System.`name`→`str`: 

> Get or set the operator name.`path`→`str`**(Read Only)** : 

> Full path to the operator.`digits`→`int`**(Read Only)** : 

> Returns the numeric value of the last consecutive group of digits in the name, or None if not found. The digits can be in the middle of the name if there are none at the end of the name.`base`→`str`**(Read Only)** : 

> Returns the beginning portion of the name occurring before any digits.`par`→`ParCollection`**(Read Only)** : 

> An intermediate [parameter collection](<./ParCollection_Class.md> "ParCollection Class") object, from which a specific [parameter](<./Par_Class.md> "Par Class") can be found. 
[code]
>     n.par.tx
>     # or
>     n.par['tx']
>     
[/code]`parGroup`→`ParGroupCollection`**(Read Only)** : 

> An intermediate [parameter collection](<./ParGroupCollection_Class.md> "ParGroupCollection Class") object, from which a specific [parameter group](<./ParGroup_Class.md> "ParGroup Class") can be found. 
[code]
>     n.parGroup.t
>     # or
>     n.parGroup['t']
>     
[/code]`ext`→`Ext`**(Read Only)** : 

> Object that searches for parent [extensions](<./Extensions.md> "Extensions"). 
[code]
>     me.ext.MyClass
>     
[/code]`passive`→`bool`**(Read Only)** : 

> If true, operator will not cook before its access methods are called. To use a passive version of an operator n, use passive(n).`curPar`→`Par`**(Read Only)** : 

> The parameter currently being evaluated. Can be used in a parameter expression to reference itself. An easy way to see this is to put the expression`curPar.name`in any string parameter.`curBlock`→`SequenceBlock`**(Read Only)** : 

> The SequenceBlock of the parameter currently being evaluated. Can be used in a parameter expression to reference itself.`curSeq`→`Sequence`**(Read Only)** : 

> The Sequence of the parameter currently being evaluated. Can be used in a parameter expression to reference itself.`time`→`OP`**(Read Only)** : 

> [Time Component](<./TimeCOMP_Class.md> "TimeCOMP Class") that defines the operator's time reference.`fileFolder`→`str`**(Read Only)** : 

> Returns the folder where this node is saved.`filePath`→`str`**(Read Only)** : 

> Returns the file location of this node.`mod`→`MOD`**(Read Only)** : 

> Get a [module on demand](<./MOD_Class.md> "MOD Class") object that searches for DAT modules relative to this operator.`pages`→`List[Page]`**(Read Only)** : 

> A list of all built-in pages.`seq`→`SequenceCollection`**(Read Only)** : 

> An intermediate [sequence collection](<./SequenceCollection_Class.md> "SequenceCollection Class") object, from which a specific [sequence](</index.php?title=Sequence&action=edit&redlink=1> "Sequence \(page does not exist\)") can be found. 
[code]
>     comp.seq.ext
>     # or
>     comp.seq['ext']
>     
[/code]`builtinPars`→`List[Par]`**(Read Only)** : 

> A list of all [built-in parameters](<./Par_Class.md> "Par Class").`customParGroups`→`List[ParGroup]`**(Read Only)** : 

> A list of all [ParGroups](<./ParGroup_Class.md> "ParGroup Class"), where a ParGroup is a set of parameters all drawn on the same line of a dialog, sharing the same label.`customPars`→`List[Par]`**(Read Only)** : 

> A list of all [custom parameters](<./Par_Class.md> "Par Class").`customPages`→`List[Page]`**(Read Only)** : 

> A list of all [custom pages](<./Page_Class.md> "Page Class").`replicator`→`OP`**(Read Only)** : 

> The [replicatorCOMP](<./ReplicatorCOMP_Class.md> "ReplicatorCOMP Class") that created this operator, if any.`storage`→`dict`**(Read Only)** : 

> [Storage](<./Storage.md> "Storage") is dictionary associated with this operator. Values stored in this dictionary are persistent, and saved with the operator. The dictionary attribute is read only, but not its contents. Its contents may be manipulated directly with methods such as OP.fetch() or OP.store() described below, or examined with an [Examine DAT](<./Examine_DAT.md> "Examine DAT").`tags`→`set`: 

> Get or set a set of user defined strings. [Tags](<./Tag.md> "Tag") can be searched using OP.findChildren() and the [OP Find DAT](<./OP_Find_DAT.md> "OP Find DAT"). 
> 
> The set is a regular python set, and can be accessed accordingly: 
[code] 
>     n.tags = ['effect', 'image filter']
>     n.tags.add('darken')
>     
[/code]`children`→`List[OP]`**(Read Only)** : 

> A list of [operators](<./OP_Class.md> "OP Class") contained within this operator. Only [component](<./COMP_Class.md> "COMP Class") operators have children, otherwise an empty list is returned.`numChildren`→`int`**(Read Only)** : 

> Returns the number of children contained within the operator. Only [component](<./COMP_Class.md> "COMP Class") operators have children.`numChildrenRecursive`→`int`**(Read Only)** : 

> Returns the number of operators contained recursively within this operator. Only [component](<./COMP_Class.md> "COMP Class") operators have children.`op`→`OPShortcut`**(Read Only)** : 

> The operator finder object, for accessing operators through paths or shortcuts. **Note:** a version of this method that searches relative to '/' is also in the global [td module](<./Td_Module.md> "Td Module"). 
> 
>`**op(pattern1, pattern2..., includeUtility=False)**`→`[OP](<./OP_Class.md> "OP Class") or None`>
>> Returns the first OP whose path matches the given pattern, relative to the inside of this operator. Will return None if nothing is found. Multiple patterns may be specified which are all added to the search. Numeric OP ids may also be used. 
>> 
>>   *`pattern`\- Can be string following the [Pattern Matching](<./Pattern_Matching.md> "Pattern Matching") rules, specifying which OP to return, or an integer, which must be an OP Id. Multiple patterns can be given, the first matching OP will be returned.
>>   *`includeUtility`**(Optional)** \- if True, allow [Utility nodes](<./Network_Utilities-_Comments,_Network_Boxes,_Annotates.md> "Network Utilities: Comments, Network Boxes, Annotates") to be returned. If False, Utility operators will be ignored.
>> 

[code]
>>     b = op('project1')
>>     b = op('foot*', 'hand*') #comma separated
>>     b = op('foot* hand*')  #space separated
>>     b = op(154)
>>     
[/code]
> 
>`**op.shortcut**`→`OP`>
>>     An operator specified with by a [Global OP Shortcut](<./Global_OP_Shortcut.md> "Global OP Shortcut"). If no operator exists an exception is raised. These shortcuts are global, and must be unique. That is, cutting and pasting an operator with a Global OP Shortcut specified will lead to a name conflict. One shortcut must be renamed in that case. Furthermore, only components can be given Global OP Shortcuts. 
>> 
>>   *`shortcut`\- Corresponds to the Global OP Shortcut parameter specified in the target operator.
>> 

[code]
>>     b = op.Videoplayer
>>     
[/code]
>> 
>> To list all Global OP Shortcuts: 
[code] 
>>     for x in op:
>>     	print(x)
>>     
[/code]`opex`→`OPEXShortcut`**(Read Only)** : 

> An operator finder object, for accessing operators through paths or shortcuts. Works like the op() shortcut method, except it will raise an exception if it fails to find the node instead of returning None as op() does. This is now the recommended way to get nodes in parameter expressions, as the error will be more useful than, for example,`NoneType has no attribute "par"`, that is often seen when using op(). **Note:** a version of this method that searches relative to '/' is also in the global [td module](<./Td_Module.md> "Td Module"). 
> 
>`**op(pattern1, pattern2..., includeUtility=False)**`→`[OP](<./OP_Class.md> "OP Class")`>
>> Returns the first OP whose path matches the given pattern, relative to the inside of this operator. Will return None if nothing is found. Multiple patterns may be specified which are all added to the search. Numeric OP ids may also be used. 
>> 
>>   *`pattern`\- Can be string following the [Pattern Matching](<./Pattern_Matching.md> "Pattern Matching") rules, specifying which OP to return, or an integer, which must be an OP Id. Multiple patterns can be given, the first matching OP will be returned.
>>   *`includeUtility`**(Optional)** \- if True, allow [Utility nodes](<./Network_Utilities-_Comments,_Network_Boxes,_Annotates.md> "Network Utilities: Comments, Network Boxes, Annotates") to be returned. If False, Utility operators will be ignored.
>>`parent`→`ParentShortcut`**(Read Only)** : 

> The [Parent Shortcut](<./Parent_Shortcut.md> "Parent Shortcut") object, for accessing parent components through indices or shortcuts. 
> 
> **Note:** _a version of this method that searches relative to the current operator is also in the global[td module](<./Td_Module.md> "Td Module")._
> 
>`parent(n)`→`OP or None`>
>> The nth parent of this operator. If n not specified, returns the parent. If n = 2, returns the parent of the parent, etc. If no parent exists at that level, None is returned. 
>> 
>>   * n - (Optional) n is the number of levels up to climb. When n = 1 it will return the operator's parent.
>> 

[code]
>>     p = parent(2) #grandfather
>>     
[/code]
> 
>`parent.shortcut`→`OP`>
>> A parent component specified with a shortcut. If no parent exists an exception is raised. 
>> 
>>   * shortcut - Corresponds to the [Parent Shortcut](<./Parent_Shortcut.md> "Parent Shortcut") parameter specified in the target parent.
>> 

[code]
>>     n = parent.Videoplayer
>>     
[/code]
>> 
>> See also Parent Shortcut for more examples.`iop`→`IOPShortcut`**(Read Only)** : 

> The Internal Operator Shortcut object, for accessing internal shortcuts. See also [Internal Operators](<./Internal_Operators.md> "Internal Operators"). **Note:** a version of this method that searches relative to the current operator is also in the global [td Module](<./Td_Module.md> "Td Module").`ipar`→`IparShortcut`**(Read Only)** : 

> The Internal Operator Parameter Shortcut object, for accessing internal shortcuts. See also [Internal Parameters](<./Internal_Parameters.md> "Internal Parameters"). **Note:** a version of this method that searches relative to the current operator is also in the global [td Module](<./Td_Module.md> "Td Module").`currentPage`→`[Page](<./Page_Class.md> "Page Class")`: 

> Get or set the currently displayed parameter page. It can be set by setting it to another page or a string label. 
[code]
>     n.currentPage = 'Common'
>     
[/code]`enclosedBy`→`List[annotateCOMP]`**(Read Only)** : 

> The (possibly empty) list of Annotate operators enclosing this node. See also [AnnotateCOMP.enclosedOPs](<./AnnotateCOMP_Class.md> "AnnotateCOMP Class").

### Common Flags

The following methods get or set specific operator [Flags](<./Flag.md> "Flag"). Note specific operators may contain other flags not in this section.`activeViewer`→`bool`: 

> Get or set [Viewer Active Flag](<./Viewer_Active_Flag.md> "Viewer Active Flag").`allowCooking`→`bool`: 

> Get or set [Cooking Flag](<./Cooking_Flag.md> "Cooking Flag"). Only COMPs can disable this flag.`bypass`→`bool`: 

> Get or set [Bypass Flag](<./Bypass_Flag.md> "Bypass Flag").`cloneImmune`→`bool`: 

> Get or set [Clone Immune Flag](<./Immune_Flag.md> "Immune Flag").`current`→`bool`: 

> Get or set [Current Flag](<./Current_Flag.md> "Current Flag").`display`→`bool`: 

> Get or set [Display Flag](<./Display_Flag.md> "Display Flag").`expose`→`bool`: 

> Get or set the [Expose Flag](<./Expose_Flag.md> "Expose Flag") which hides a node from view in a network.`lock`→`bool`: 

> Get or set [Lock Flag](<./Lock_Flag.md> "Lock Flag").`selected`→`bool`: 

> Get or set [Selected Flag](<./Selected_Flag.md> "Selected Flag"). This controls if the node is part of the network selection. (yellow box around it).`python`→`bool`: 

> Get or set parameter expression language as python.`render`→`bool`: 

> Get or set [Render Flag](<./Render_Flag.md> "Render Flag").`showCustomOnly`→`bool`: 

> Get or set the Show Custom Only Flag which controls whether or not non custom parameters are display in[ parameter dialogs](<./Parameter_Dialog.md> "Parameter Dialog").`showDocked`→`bool`: 

> Get or set [Show Docked Flag](<./Docking.md> "Docking"). This controls whether this node is visible or hidden when it is docked to another node.`viewer`→`bool`: 

> Get or set [Viewer Flag](<./Viewer_Flag.md> "Viewer Flag").

### Appearance`color`→`tuple[float, float, float]`: 

> Get or set color value, expressed as a 3-tuple, representing its red, green, blue values. To convert between color spaces, use the built in colorsys module.`comment`→`str`: 

> Get or set comment string.`nodeHeight`→`int`: 

> Get or set node height, expressed in [network editor](<./NetworkEditor_Class.md> "NetworkEditor Class") units.`nodeWidth`→`int`: 

> Get or set node width, expressed in [network editor](<./NetworkEditor_Class.md> "NetworkEditor Class") units.`nodeX`→`int`: 

> Get or set node X value, expressed in [network editor](<./NetworkEditor_Class.md> "NetworkEditor Class") units, measured from its left edge.`nodeY`→`int`: 

> Get or set node Y value, expressed in [network editor](<./NetworkEditor_Class.md> "NetworkEditor Class") units, measured from its bottom edge.`nodeCenterX`→`int`: 

> Get or set node X value, expressed in [network editor](<./NetworkEditor_Class.md> "NetworkEditor Class") units, measured from its center.`nodeCenterY`→`int`: 

> Get or set node Y value, expressed in [network editor](<./NetworkEditor_Class.md> "NetworkEditor Class") units, measured from its center.`dock`→`OP`: 

> Get or set the [operator](<./OP_Class.md> "OP Class") this operator is docked to. To clear docking, set this member to None.`docked`→`List[OP]`**(Read Only)** : 

> The (possibly empty) list of [operators](<./OP_Class.md> "OP Class") docked to this node.

### Connection

See also the`OP.parent`methods. To connect components together see [COMP_Class#Connection](<./COMP_Class.htm#Connection> "COMP Class") section.`inputs`→`List[OP]`**(Read Only)** : 

> List of input [operators](<./OP_Class.md> "OP Class") (via left side connectors) to this operator. To get the number of inputs, use len(OP.inputs).`outputs`→`List[OP]`**(Read Only)** : 

> List of output [operators](<./OP_Class.md> "OP Class") (via right side connectors) from this operator.`inputConnectors`→`List[Connector]`**(Read Only)** : 

> List of input [connectors](<./Connector_Class.md> "Connector Class") (on the left side) associated with this operator.`outputConnectors`→`List[Connector]`**(Read Only)** : 

> List of output [connectors](<./Connector_Class.md> "Connector Class") (on the right side) associated with this operator.

### Cook Information`cookFrame`→`float`**(Read Only)** : 

> Last frame at which this operator cooked.`cookTime`→`float`**(Read Only)** : 

> **Deprecated** Duration of the last measured cook (in milliseconds).`cpuCookTime`→`float`**(Read Only)** : 

> Duration of the last measured cook in CPU time (in milliseconds).`cookAbsFrame`→`float`**(Read Only)** : 

> Last absolute frame at which this operator cooked.`cookStartTime`→`float`**(Read Only)** : 

> Last offset from frame start at which this operator cook began, expressed in milliseconds.`cookEndTime`→`float`**(Read Only)** : 

> Last offset from frame start at which this operator cook ended, expressed in milliseconds. Other operators may have cooked between the start and end time. See the cookTime member for this operator's specific cook duration.`cookedThisFrame`→`bool`**(Read Only)** : 

> True when this operator has cooked this frame.`cookedPreviousFrame`→`bool`**(Read Only)** : 

> True when this operator has cooked the previous frame.`childrenCookTime`→`float`**(Read Only)** : 

> **Deprecated** The total accumulated cook time of all children of this operator during the last frame. Zero if the operator is not a [COMP](<./COMP_Class.md> "COMP Class") and/or has no children.`childrenCPUCookTime`→`float`**(Read Only)** : 

> The total accumulated cook time of all children of this operator during the last frame. Zero if the operator is not a [COMP](<./COMP_Class.md> "COMP Class") and/or has no children.`childrenCookAbsFrame`→`float`**(Read Only)** : 

> **Deprecated** The absolute frame on which childrenCookTime is based.`childrenCPUCookAbsFrame`→`float`**(Read Only)** : 

> The absolute frame on which childrenCPUCookTime is based.`gpuCookTime`→`float`**(Read Only)** : 

> Duration of GPU operations during the last measured cook (in milliseconds).`childrenGPUCookTime`→`float`**(Read Only)** : 

> The total accumulated GPU cook time of all children of this operator during the last frame. Zero if the operator is not a COMP and/or has no children.`childrenGPUCookAbsFrame`→`float`**(Read Only)** : 

> The absolute frame on which childrenGPUCookTime is based.`totalCooks`→`int`**(Read Only)** : 

> Number of times the operator has cooked.`cpuMemory`→`int`**(Read Only)** : 

> The approximate amount of CPU memory this Operator is using, in bytes.`gpuMemory`→`int`**(Read Only)** : 

> The amount of GPU memory this OP is using, in bytes.

### Type`type`→`str`**(Read Only)** : 

> Operator type as a string. Example: 'oscin'.`subType`→`str`**(Read Only)** : 

> Operator subtype. Currently only implemented for [components](<./Component.md> "Component"). May be one of: 'panel', 'object', or empty string in the case of base components.`opType`→`str`**(Read Only)** : 

> Python operator class type, as a string. Example: 'oscinCHOP'. Can be used with COMP.create() method.`label`→`str`**(Read Only)** : 

> Operator type label. Example: 'OSC In'.`icon`→`str`**(Read Only)** : 

> Get the letters used to create the operator's icon.`family`→`str`**(Read Only)** : 

> Operator family. Example: CHOP. Use the global dictionary families for a list of each operator type.`isFilter`→`bool`**(Read Only)** : 

> True if operator is a filter, false if it is a generator.`minInputs`→`int`**(Read Only)** : 

> Minimum number of inputs to the operator.`maxInputs`→`int`**(Read Only)** : 

> Maximum number of inputs to the operator.`isMultiInputs`→`bool`**(Read Only)** : 

> True if inputs are ordered, false otherwise. Operators with an arbitrary number of inputs have unordered inputs, example [Merge CHOP](<./Merge_CHOP.md> "Merge CHOP").`visibleLevel`→`int`**(Read Only)** : 

> Visibility level of the operator. For example, expert operators have visibility level 1, regular operators have visibility level 0.`isBase`→`bool`**(Read Only)** : 

> True if the operator is a Base (miscellaneous) [component](<./Component.md> "Component").`isCHOP`→`bool`**(Read Only)** : 

> True if the operator is a [CHOP](<./CHOP.md> "CHOP").`isCOMP`→`bool`**(Read Only)** : 

> True if the operator is a [component](<./Component.md> "Component").`isDAT`→`bool`**(Read Only)** : 

> True if the operator is a [DAT](<./DAT.md> "DAT").`isMAT`→`bool`**(Read Only)** : 

> True if the operator is a [Material](<./MAT.md> "MAT").`isObject`→`bool`**(Read Only)** : 

> True if the operator is an [object](<./Object.md> "Object").`isPanel`→`bool`**(Read Only)** : 

> True if the operator is a [Panel](<./Panel.md> "Panel").`isSOP`→`bool`**(Read Only)** : 

> True if the operator is a [SOP](<./SOP.md> "SOP").`isTOP`→`bool`**(Read Only)** : 

> True if the operators is a [TOP](<./TOP.md> "TOP").`isPOP`→`bool`**(Read Only)** : 

> True if the operators is a [POP](<./POP.md> "POP").`isCustom`→`bool`**(Read Only)** : 

> True if the operators is a [Custom Operator](<./Custom_Operators.md> "Custom Operators").`licenseType`→`str`**(Read Only)** : 

> Type of [License](<./License_Class.md> "License Class") required for the operator.

## Methods

### General

**NOTE** :`create()`,`copy()`and`copyOPs()`is done by the parent operator (a component). For more information see [COMP.create, COMP.copy and COMP.copyOPs methods](<./COMP_Class.htm#Methods> "COMP Class").`pars(pattern)`→`list[Par]`: 

> Returns a (possibly empty) list of [parameter objects](<./Par_Class.md> "Par Class") that match the pattern. 
> 
>   * pattern - Is a string following the [Pattern Matching](<./Pattern_Matching.md> "Pattern Matching") rules, specifying which parameters to return.
> 

[code]
>     newlist = op('geo1').pars('t?', 'r?', 's?') #translate/rotate/scale parameters
>     
[/code]
> 
> Note: If searching for a single parameter given a name, it's much more efficient to use the subscript operator. For example:
[code]
>     name = 'MyName1'
>     op('geo1').par[name]
>     
[/code]`parGroups(pattern)`→`list[Par]`: 

> Returns a (possibly empty) list of [parGroup objects](<./ParGroup_Class.md> "ParGroup Class") that match the pattern. 
> 
>   * pattern - Is a string following the [Pattern Matching](<./Pattern_Matching.md> "Pattern Matching") rules, specifying which parameters to return.
> 

[code]
>     debug(op('geo1').parGroups('p*'))
>     
[/code]
> 
> **Note:** If searching for a single ParGroup given a name, it's much more efficient to use the subscript operator. For example: 
[code] 
>     name = 'MyColor'
>     op('geo1').parGroup[name]
>     
[/code]
> 
> or even: 
[code] 
>     op('geo1').parGroup.MyColor
>     
[/code]`ops(*patterns, includeUtility=False)`→`List[OP]`: 

> Returns a (possibly empty) list of OPs that match the patterns, relative to the inside of this OP. 
> 
> Multiple patterns may be provided. Numeric OP ids may also be used. The`ops`member is technically a Python Shortcut Object, not a true method. 
> 
>   *`pattern`\- Can be string following the [Pattern Matching](<./Pattern_Matching.md> "Pattern Matching") rules, specifying which OPs to return, or an integer, which must be an OP Id. Multiple patterns can be given and all matched OPs will be returned.
>   *`includeUtility`\- (Keyword, Optional) If specified, controls whether or not utility components (eg Comments) are included in the results.
> 

> 
> **Note:** a version of this method that searches relative to '/' is also in the global [td module](<./Td_Module.md> "Td Module"). 
[code] 
>     newlist = n.ops('arm*', 'leg*', 'leg5/foot*')
>     
[/code]`cook(force=False, recurse=False, includeUtility=False)`→`None`: 

> Cook the contents of the operator if required. 
> 
>   * force - (Keyword, Optional) If True, the operator will always cook, even if it wouldn't under normal circumstances.
>   * recurse - (Keyword, Optional) If True, all children and sub-children of the operator will be cooked.
>   * includeUtility - (Keyword, Optional) If specified, controls whether or not utility components (eg Comments) are included in the results.
>`copyParameters(OP, custom=True, builtin=True)`→`None`: 

> Copy all of the parameters from the specified [operator](<./OP_Class.md> "OP Class"). Both operators should be the same type. 
> 
>   * OP - The operator to copy.
>   * custom - (Keyword, Optional) When True, custom parameters will be copied.
>   * builtin - (Keyword, Optional) When True, built in parameters will be copied.
> 

[code]
>     op('geo1').copyParameters( op('geo2') )
>     
[/code]`changeType(OPtype)`→`OP`: 

> Change referenced operator to a new operator type. After this call, this OP object should no longer be referenced. Instead use the returned OP object. 
> 
>   * OPtype - The python class name of the operator type you want to change this operator to. This is not a string, but instead is a class defined in the global [td module](<./Td_Module.md> "Td Module").
> 

[code]
>     n = op('wave1').changeType(nullCHOP) #changes 'wave1' into a Null CHOP
>     n = op('text1').changeType(tcpipDAT) #changes 'text1' operator into a TCPIP DAT
>     
[/code]`dependenciesTo(OP)`→`list`: 

> Returns a (possibly empty) list of operator dependency paths between this operator and the specified operator. Multiple paths may be found.`evalExpression(str)`→`Any`: 

> Evaluate the expression from the context of this OP. Can be used to evaluate arbitrary snippets of code from arbitrary locations. 
> 
>   * str - The expression to evaluate.
> 

[code]
>     op('wave1').evalExpression('me.digits')  #returns 1
>     
[/code]
> 
> If the expression already resides in a parameter, use that parameters [evalExpression()](<./Par_Class.md> "Par Class") method instead.`destroy()`→`None`: 

> Destroy the operator referenced by this OP. An exception will be raised if the OP's operator has already been destroyed.`var(name, search=True)`→`str`: 

> Evaluate a[ variable](<./Variables.md> "Variables"). This will return the empty string, if not found. Most information obtained from variables (except for Root and Component variables) are accessible through other means in Python, usually in the global [td module](<./Td_Module.md> "Td Module"). 
> 
>   * name - The variable name to search for.
>   * search - (Keyword, Optional) If set to True (which is default) the operator hierarchy is searched until a variable matching that name is found. If false, the search is constrained to the operator.
>`openMenu(x=None, y=None)`→`None`: 

> Open a node menu for the operator at x, y. Opens at mouse if x & y are not specified. 
> 
>   * x - (Keyword, Optional) The X coordinate of the menu, measured in screen pixels.
>   * y - (Keyword, Optional) The Y coordinate of the menu, measured in screen pixels.
>`relativePath(OP)`→`str`: 

> Returns the relative path from this operator to the OP that is passed as the argument. See OP.shortcutPath for a version using expressions.`setInputs(listOfOPs)`→`None`: 

> Set all the operator inputs to the specified list. 
> 
>   * listOfOPs - A list containing one or more OPs. Entries in the list can be None to disconnect specific inputs. An empty list disconnects all inputs.
>`shortcutPath(OP, toParName=None)`→`str`: 

> Returns an expression from this operator to the OP that is passed as the argument. See OP.relativePath for a version using relative path constants. 
> 
>   * toParName - (Keyword, Optional) Return an expression to this parameter instead of its operator.
>`resetPars(parNames='*', parGroupNames='*', pageNames='*', includeBuiltin=True, includeCustom=True)`→`bool`: 

> Resets the specified parameters in the operator. 
> 
> Returns true if anything was changed. 
> 
>   * parNames (Keyword, Optional) - Specify parameters by Par name.
>   * parGroupNames (Keyword, Optional) - Specify parameters by ParGroup name.
>   * pageNames (Keyword, Optional) - Specify parameters by page name.
>   * includeBuiltin (Keyword, Optional) - Include builtin parameters.
>   * includeCustom (Keyword, Optional) - Include custom parameters.
> 

[code]
>     op('player').resetPars(includeBuiltin=False) # only reset custom
>     
[/code]`unload(cacheMemory=False)`→`None`: 

> Unloads CPU and GPU for the node. The memory will be realloted next time the node cooks, so make sure nothing is still using it to keep it released. 
> 
>   * cacheMemory - (Keyword, Optional) Currently only supported by the [Movie File In TOP](<./Movie_File_In_TOP.md> "Movie File In TOP"). If you are preloading into a Movie File In TOP that already has video, and the video format/resolution is the same, you can use the cacheMemory option to first unload the original movie and cache its memory, avoiding a reallocation when the`preload()`occurs. If True the memory (textures, upload buffers) of the movie will be cached for use by another movie later on. Useful if you are opening/closing many movies with the same codec and resolution.>
>`asType(opType, checkType=False)`→`OP`: 

> Casts this OP to the given type for editor code analysis. Returns the OP. 
> 
>   * opType - The type to cast this OP to.
>   * checkType: (Optional) If True, will check that this OP is of the given asType, and raise an exception if not.
> 

### Errors`addScriptError(msg)`→`None`: 

> Adds a script error to a node. 
> 
>   * msg - The error to add.
>`addError(msg)`→`None`: 

> Adds an error to an operator. Only valid if added while the operator is cooking. (Example Script SOP, CHOP, DAT). 
> 
>   * msg - The error to add.
>`addWarning(msg)`→`None`: 

> Adds a warning to an operator. Only valid if added while the operator is cooking. (Example Script SOP, CHOP, DAT). 
> 
>   * msg - The error to add.
>`errors(recurse=False)`→`str`: 

> Get error messages associated with this OP. 
> 
>   * recurse - Get errors in any children or subchildren as well.
>`warnings(recurse=False)`→`str`: 

> Get warning messages associated with this OP. 
> 
>   * recurse - Get warnings in any children or subchildren as well.
>`scriptErrors(recurse=False)`→`str`: 

> Get script error messages associated with this OP. 
> 
>   * recurse - Get errors in any children or subchildren as well.
>`clearScriptErrors(recurse=False, error='*')`→`None`: 

> Clear any errors generated during script execution. These may be generated during execution of DATs, Script Nodes, Replicator COMP callbacks, etc. 
> 
>   * recurse - Clear script errors in any children or subchildren as well.
>   * error - Pattern to match when clearing errors
> 

[code]
>     op('/project1').clearScriptErrors(recurse=True)
>     
[/code]`childrenCPUMemory()`→`int`: 

> Returns the total CPU memory usage for all the children from this COMP.`childrenGPUMemory()`→`int`: 

> Returns the total GPU memory usage for all the children from this COMP.

### Appearance`resetNodeSize()`→`None`: 

> Reset the node tile size to its default width and height.

### Viewers`closeViewer(topMost=False)`→`None`: 

> Close the floating content viewers of the OP. 
> 
>   * topMost - (Keyword, Optional) If True, any viewer window containing any parent of this OP is closed instead.
> 

[code]
>     op('wave1').closeViewer()
>     op('wave1').closeViewer(topMost=True) # any viewer that contains 'wave1' will be closed.
>     
[/code]`openViewer(unique=False, borders=True)`→`None`: 

> Open a floating content viewer for the OP. 
> 
>   * unique - (Keyword, Optional) If False, any existing viewer for this OP will be re-used and popped to the foreground. If unique is True, a new window is created each time instead.
>   * borders - (Keyword, Optional) If true, the floating window containing the viewer will have borders.
> 

[code]
>     op('geo1').openViewer(unique=True, borders=False) # opens a new borderless viewer window for 'geo1'
>     
[/code]`resetViewer(recurse=False)`→`None`: 

> Reset the OP content viewer to default view settings. 
> 
>   * recurse - (Keyword, Optional) If True, this is done for all children and sub-children as well.
> 

[code]
>     op('/').resetViewer(recurse=True) # reset the viewer for all operators in the entire file.
>     
[/code]`openParameters()`→`None`: 

> Open a floating dialog containing the operator parameters.

### Storage

[Storage](<./Storage.md> "Storage") can be used to keep data within components. Storage is implemented as one python dictionary per node. 

When an element of storage is changed by using`n.store()`as explained below, expressions and operators that depend on it will automatically re-cook. It is retrieved with the`n.fetch()`function. 

Storage is saved in`.toe`and`.tox`files and restored on startup. 

Storage can hold any python object type (not just strings as in Tscript variables). Storage elements can also have optional startup values, specified separately. Use these startup values for example, to avoid saving and loading some session specific object, and instead save or load a well defined object like`None`. 

See the [Examine DAT](<./Examine_DAT.md> "Examine DAT") for procedurally viewing the contents of storage.`fetch(key, default, search=True, storeDefault=False)`→`Any`: 

> Return an object from the OP storage dictionary. If the item is not found, and a default it supplied, it will be returned instead. 
> 
>   * key - The name of the entry to retrieve.
>   * default - (Optional) If provided and no item is found then the passed value/object is returned instead.
>   * storeDefault - (Keyword, Optional) If True, and the key is not found, the default is stored as well.
>   * search - (Keyword, Optional) If True, the parent of each OP is searched recursively until a match is found
> 

[code]
>     v = n.fetch('sales5', 0.0)
>     
[/code]`fetchOwner(key)`→`OP`: 

> Return the operator which contains the stored key, or None if not found. 
> 
>   * key - The key to the stored entry you are looking for.
> 

[code]
>     who = n.fetchOwner('sales5') #find the OP that has a storage entry called 'sales5'
>     
[/code]`store(key, value)`→`Any`: 

> Add the key/value pair to the OP's storage dictionary, or replace it if it already exists. If this value is not intended to be saved and loaded in the toe file, it can be be given an alternate value for saving and loading, by using the method storeStartupValue described below. 
> 
>   * key - A string name for the storage entry. Use this name to retrieve the value using fetch().
>   * value - The value/object to store.
> 

[code]
>     n.store('sales5', 34.5) # stores a floating point value 34.5.
>     n.store('moviebank', op('/project1/movies')) # stores an OP for easy access later on.
>     
[/code]`unstore(*keys)`→`None`: 

> For each key, remove it from the OP's storage dictionary. Pattern Matching is supported as well. 
> 
>   * keys - The name or pattern defining which key/value pairs to remove from the storage dictionary.
> 

[code]
>     n.unstore('sales*') # removes all entries from this OPs storage that start with 'sales'
>     
[/code]`storeStartupValue(key, value)`→`None`: 

> Add the key/value pair to the OP's storage startup dictionary. The storage element will take on this value when the file starts up. 
> 
>   * key - A string name for the storage startup entry.
>   * value - The startup value/object to store.
> 

[code]
>     n.storeStartupValue('sales5', 1) # 'sales5' will have a value of 1 when the file starts up.
>     
[/code]`unstoreStartupValue(*keys)`→`None`: 

> For key, remove it from the OP's storage startup dictionary. Pattern Matching is supported as well. This does not affect the stored value, just its startup value. 
> 
>   * keys - The name or pattern defining which key/value pairs to remove from the storage startup dictionary.
> 

[code]
>     n.unstoreStartupValue('sales*') # removes all entries from this OPs storage startup that start with 'sales'
>     
[/code]

### Miscellaneous`__getstate__()`→`dict`: 

> Returns a dictionary with persistent data about the object suitable for pickling and deep copies.`__setstate__()`→`dict`: 

> Reads the dictionary to update persistent details about the object, suitable for unpickling and deep copies.

TouchDesigner Build: Latest\n2022.241402021.100002018.28070before 2018.28070
