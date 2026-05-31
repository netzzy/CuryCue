# Panes Class

The Panes class describes the list of all [pane objects](<./Pane_Class.md> "Pane Class"). It can be accessed from [ui.panes](<./UI_Class.md> "UI Class"). 

## Members`current`→`td.Pane`**(Read Only)** : 

> The currently selected [pane](<./Pane_Class.md> "Pane Class").

## Methods`createFloating(type=None, name=None, maxWidth=1920, maxHeight=1080, monitorSpanWidth=0.9, monitorSpanHeight=0.9)`→`Pane`: 

> Return a floating pane. 
> 
>   * type - (Keyword, Optional) Type of pane created. See [Pane](<./Pane_Class.md> "Pane Class") for examples. Defaults to Network Editor.
>   * name - (Keyword, Optional) Name of the pane. This value can be used to find the pane in ui.panes.
>   * maxWidth - (Keyword, Optional) Upper limit on the width of the created window. Specified in pixels.
>   * maxHeight - (Keyword, Optional) Upper limit on the height of the created window. Specified in pixels.
>   * monitorSpanWidth - (Keyword, Optional) Specifies window width as a portion of the monitor width.
>   * monitorSpanHeight - (Keyword, Optional) Specifies window height as a portion of the monitor height.
> 

> 
> Example 
[code] 
>         p = ui.panes.createFloating(type=PaneType.NETWORKEDITOR, name="Output")
>         p.owner = op('/project1/base1')
>     
[/code]

### Special Functions`len(Panes)`→`int`: 

> Returns the total number of panes. 
[code]
>     a = len(ui.panes)
>     
[/code]`[index]`→`td.Pane`: 

> Get specific pane, referenced by string or index. 
[code]
>     p = ui.panes[0]
>     p = ui.panes['pane1']
>     
[/code]`Iterator`→`td.Pane`: 

> Iterate over each pane. 
[code]
>     for n in ui.panes:
>     	# do something with n
>     
[/code]

  
TouchDesigner Build: Latest\nwikieditorwikieditor2021.100002018.28070before 2018.28070
