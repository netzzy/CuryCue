# UI Class

The UI class describes access to the UI elements of the application, found in the automatically imported [td module](<./Td_Module.md> "Td Module").   
  
To access members and methods of this class use the default instance`ui`. 

For Example: 
[code] 
    # open the Midi Device Mapper Dialog
    ui.openMIDIDeviceMapper()
    
[/code]

## Members`clipboard`→`str`: 

> Get or set the operating system clipboard text contents.`colors`→`Colors`**(Read Only)** : 

> Access to the application [colors](<./Colors_Class.md> "Colors Class").`dpiBiCubicFilter`→`bool`: 

> Get or set the global DPI scale filtering mode of TouchDesigner windows. True means bi-cubic, False means linear.`masterVolume`→`float`: 

> Get or set the master audio output volume. A value of 0 is no output, while a value of 1 is full output.`options`→`Options`**(Read Only)** : 

> Access to the application [options](<./Options_Class.md> "Options Class").`panes`→`Panes`**(Read Only)** : 

> Access to the set of all [panes](<./Panes_Class.md> "Panes Class").`performMode`→`bool`: 

> Get or set [Perform Mode](<./Perform_Mode.md> "Perform Mode"). Set to True to go into Perform Mode, False to go into [Designer Mode](<./Designer_Mode.md> "Designer Mode").`preferences`→`Preferences`**(Read Only)** : 

> Access to the application [preferences](<./Preferences_Class.md> "Preferences Class"), which can also be access through the [Preferences Dialog](<./Dialogs-Preferences_Dialog.md> "Dialogs:Preferences Dialog").`redrawMainWindow`→`bool`: 

> Get or set whether the main window should redraw. The main window is either the main network editor, or the perform window.`rolloverOp`→`OP | None`**(Read Only)** : 

> Operator currently under the mouse in a network editor.`rolloverPar`→`Par | None`**(Read Only)** : 

> Parameter currently under the mouse in a parameter dialog.`rolloverParGroup`→`ParGroup | None`**(Read Only)** : 

> ParGroup currently under the mouse in a parameter dialog.`rolloverPanel`→`PanelCOMP | None`**(Read Only)** : 

> returns the panel currently under the mouse.`rolloverPage`→`Page | None`**(Read Only)** : 

> returns the Page currently under the mouse in a parameter dialog.`rollover`→`Par | ParGroup | Page | OP | PanelCOMP | None`**(Read Only)** : 

> combines the other rollover members into one test, reporting the TD object under the mouse. Because there is some overlap, priority is in the following order: Par | ParGroup | Page | OP | Panel. **Note:** Panel and OP tests both return a PanelCOMP, so to tell the difference between rolling over a PanelCOMP operator in a network and rolling over an active Panel, you may have to use the specific`rolloverPanel`or`rolloverOP`methods.`lastChopChannelSelected`→`Channel`**(Read Only)** : 

> Last [CHOP channel](<./Channel.md> "Channel") selected via mouse.`showPaletteBrowser`→`bool`: 

> Get or set display of the palette browser.`status`→`str`: 

> Get or set the status message. 
[code]
>     ui.status = 'Operation Complete'
>     
[/code]`undo`→`Undo`**(Read Only)** : 

> The [Undo](<./Undo_Class.md> "Undo Class") object, which provides access to application undo functions.`windowWidth`→`int`**(Read Only)** : 

> Get the app window width.`windowHeight`→`int`**(Read Only)** : 

> Get the app window height.`windowX`→`int`**(Read Only)** : 

> Get the app window X position.`windowY`→`int`**(Read Only)** : 

> Get the app window Y position.

## Methods`copyOPs(listOfOPs)`→`None`: 

> Copy a list of operators to the operator clipboard. All operators must be children of the same component. 
> 
>   * listOfOPs - A list containing one or more OPs to be copied.
> 

[code]
>     ui.copyOPs( op('geo1').selected )
>     
[/code]`pasteOPs(COMP, x=None, y=None)`→`None`: 

> Copy the contents of the operator clipboard into the specified component. 
> 
>   * COMP \- The destination to receive the operators.
>   * x - Optional network coordinates at which to paste the operators.
>   * y - see x
> 

[code]
>     l = ui.pasteOPs( op('geo2') )
>     
[/code]`messageBox(title, message, buttons=['Ok'])`→`int`: 

> This method will open a message dialog box with the specified message. Returns the index of the button clicked. 
> 
>   * title - Specifies the window title.
>   * message - Specifies the content of the dialog.
>   * buttons - (Keyword, Optional) Specifies a list button labels to show in the dialog.
> 

[code]
>     # basic usage
>     ui.messageBox('Warning', 'Have a nice day.')
>     # specify options and report result
>     a = ui.messageBox('Please select:', 'Buttons:', buttons=['a', 'b', 'c'])
>     ui.messageBox('Results', 'You selected item: ' + str(a))
>     # pick a node from their paths
>     ui.messageBox('Please select:', 'Nodes:', buttons=parent().children)
>     # pick a node from their first names (list comprehension)
>     ui.messageBox('Please select:', 'Nodes:', buttons=[x.name for x in parent().children])
>     # pick a cell
>     ui.messageBox('Please select:', 'Cells:', buttons=op('table1').cells('*','*'))
>     
[/code]`refresh()`→`None`: 

> Update and redraw all viewports, nodes, UI elements etc immediately. This update is otherwise done once per frame at the end of all script executions. For example, if the current frame is manually changed during a script, a call to refresh will cause all dependent data to update immediately. 
[code]
>     for i in range(100):
>     	ui.status = str(i)
>     	ui.refresh()
>     
[/code]`chooseFile(load=True, start=None, fileTypes=None, title=None, asExpression=False)`→`str | None`: 

> Open a dialog box for loading or saving a file. Returns the filename selected or None if the dialog is cancelled. 
> 
>   * load - (Keyword, Optional) If set to True, the dialog will be a Load dialog, otherwise it's a Save dialog.
>   * start - (Keyword, Optional) If provided, specifies an initial folder location and/or filename selection.
>   * fileTypes - (Keyword, Optional) If provided, specifies a list of file extensions that can be used as filters. Otherwise '*.*' is the only filter.
>   * asExpression - (Keyword, Optional) If set to true, the results are provided as an expression, suitable for a [Parameter](<./Par_Class.md> "Par Class") expression or as input to an eval() call. [App Class](<./App_Class.md> "App Class") member constants such as samplesFolder may be included in the result.
>   * title (Keyword, Optional) If provided, will override the default window title.
> 

[code]
>     a = ui.chooseFile(start='python_examples.toe', fileTypes=['toe'], title='Select a toe') # specify extension
>     a = ui.chooseFile(fileTypes=tdu.fileTypes['image'], title='Select an image') # any support image extension
>     path = ui.chooseFile(load=False,fileTypes=['txt'],title='Save table as:')
>     if (path):
>     	op('table1').save(path)
>     
[/code]`chooseFolder(title='Select Folder', start=None, asExpression=False)`→`str | None`: 

> Open a dialog box for selecting a folder. Returns the folder selected or None if the dialog is cancelled. 
> 
>   * title - (Keyword, Optional) If provided, specifies the window title.
>   * start - (Keyword, Optional) If provided, specifies an initial folder location and/or filename selection.
>   * asExpression - (Keyword, Optional) If set to true, the results are provided as an expression, suitable for a [Parameter](<./Par_Class.md> "Par Class") expression or as input to an eval() call. [App Class](<./App_Class.md> "App Class") member constants such as samplesFolder may be included in the result.
> 

[code]
>     a = ui.chooseFolder()
>     a = ui.chooseFolder(title='Select a folder location.')
>     
[/code]`viewFile(URL_or_path, showInFolder=False)`→`None`: 

> View a URL or file in the default external application. You can use`ui.viewFile()`to open a folder/directory in Windows Explorer or macOS Finder. 
> 
>   * URL_or_path - URL or path to launch.
> 

[code]
>     a = ui.viewFile('output.txt')
>     
[/code]
> 
>   * showInFolder - Show file as selected in Explorer or macOS Finder instead of launching an external application.
> 

[code]
>     a = ui.viewFile('output.txt', showInFolder=True)
>     
[/code]`openBeat()`→`None`: 

> Open the [Beat Dialog](<./Beat_Dialog.md> "Beat Dialog").`openBookmarks()`→`None`: 

> Open the [Bookmarks Dialog](<./Bookmarks_Dialog.md> "Bookmarks Dialog").`openCOMPEditor(path)`→`None`: 

> Open component editor for the specific operator. 
> 
>   * path - Specifies the path to the operator. An OP can be passed in as well.
>`openConsole()`→`None`: 

> Open the [Console Window](</index.php?title=Console_Window&action=edit&redlink=1> "Console Window \(page does not exist\)").`openDialogHelp(title)`→`None`: 

> Open help page for the specific dialog. 
> 
>   * title - Specifies the help page to open.
> 

[code]
>     ui.openDialogHelp('Window Placement Dialog')
>     
[/code]`openErrors()`→`None`: 

> Open the [Errors Dialog](<./Errors_Dialog.md> "Errors Dialog").`openExplorer()`→`None`: 

> Open an Explorer window.`openExportMovie(path)`→`None`: 

> Open the [Export Movie Dialog](<./Export_Movie_Dialog.md> "Export Movie Dialog"). 
> 
>   * path - Specifies the operator content to export, optional.
> 

[code]
>     ui.openExportMovie('/project1/out1')
>     
[/code]`openImportFile()`→`None`: 

> Open the [Import File Dialog](<./Import_File_Dialog.md> "Import File Dialog").`openKeyManager()`→`None`: 

> Open the [Key Manager Dialog](<./Key_Manager_Dialog.md> "Key Manager Dialog").`openMIDIDeviceMapper()`→`None`: 

> Open the [MIDI Device Mapper Dialog](<./MIDI_Device_Mapper_Dialog.md> "MIDI Device Mapper Dialog").`openNewProject()`→`None`: 

> Open the [New Project Dialog](<./New_Project_Dialog.md> "New Project Dialog").`openOperatorSnippets(family=None, type=None, example=None)`→`None`: 

> Open the Operator Snippets window.`openPaletteBrowser()`→`None`: 

> Open the [Palette](<./Palette.md> "Palette").`openPerformanceMonitor()`→`None`: 

> Open the [Performance Monitor Dialog](<./Performance_Monitor_Dialog.md> "Performance Monitor Dialog").`openPreferences()`→`None`: 

> Open the [Preferences Dialog](<./Dialogs-Preferences_Dialog.md> "Dialogs:Preferences Dialog").`openSearch()`→`None`: 

> Open the [Search Replace Dialog](<./Search_Replace_Dialog.md> "Search Replace Dialog").`openTextport()`→`None`: 

> Open the [Textport](<./Textport.md> "Textport").`openVersion()`→`None`: 

> Open a dialog displaying current version information. See also: [App.version](<./App_Class.md> "App Class")`openWindowPlacement()`→`None`: 

> Open the [Window Placement Dialog](<./Window_Placement_Dialog.md> "Window Placement Dialog").`findEditDAT(filename)`→`DAT | None`: 

> Given an external filename, finds the corresponding DAT thats update from this filename if any..

TouchDesigner Build: Latest\nwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditor2025.300002022.241402021.100002018.28070before 2018.28070
