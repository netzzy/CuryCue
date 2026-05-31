# Pane Class

The Pane class describes an instance of a [pane](<./Pane.md> "Pane") interface. It can be accessed through the [ui.panes](<./Panes_Class.md> "Panes Class") object. It is the parent class of the [NetworkEditor Class](<./NetworkEditor_Class.md> "NetworkEditor Class"). 

## Members`owner`→`COMP`: 

> Get or set the [component](<./COMP_Class.md> "COMP Class") this pane points to.`id`→`int`**(Read Only)** : 

> A unique numeric identifier.`link`→`int`: 

> Get or set the numeric link index.`enable`→`bool`: 

> Get or set mouse and keyboard interactivity on the pane.`maximize`→`bool`: 

> Enable or disable the pane maximize state.`name`→`str`: 

> Get or set the pane name.`ratio`→`float`: 

> Get or set the split proportion of the pane, if the pane was previously split.`bottomLeft`→`Coords`**(Read Only)** : 

> The coordinates of the bottom left corner, expressed as both x/y and u/v in a named tuple.`topRight`→`Coords`**(Read Only)** : 

> The coordinates of the top right corner, expressed as both x/y and u/v in a named tuple.`open`→`bool`**(Read Only)** : 

> Returns True if the Pane is currently open.`type`→`PaneType`**(Read Only)** : 

> The enumerated type of the pane. Example: NetworkEditor. 
> 
> The enumeration is called PaneType and consists of: 
> 
>   * PaneType.NETWORKEDITOR
>   * PaneType.PANEL
>   * PaneType.GEOMETRYVIEWER
>   * PaneType.TOPVIEWER
>   * PaneType.CHOPVIEWER
>   * PaneType.ANIMATIONEDITOR
>   * PaneType.PARAMETERS
>   * PaneType.TEXTPORT
> 

## Methods`changeType(paneType)`→`td.Pane`: 

> Change the pane to the specified type. Will return a new Pane object that represents the Pane. After being called, the current Pane instance will no longer be valid. 
> 
>   * paneType - The type of pane to change this pane to.
> 

[code]
>     p = ui.panes[0]
>     p = p.changeType(PaneType.TOPVIEWER)  # note: must re-assign p to new object.
>     
[/code]`close()`→`None`: 

> Close the pane.`floatingCopy()`→`td.Pane`: 

> Return a floating copy of the pane.`splitBottom()`→`td.Pane`: 

> Split the bottom portion of the pane into a new pane.`splitLeft()`→`td.Pane`: 

> Split the left portion of the pane into a new pane.`splitRight()`→`td.Pane`: 

> Split the right portion of the pane into a new pane.`splitTop()`→`td.Pane`: 

> Split the top portion of the pane into a new pane.`tearAway()`→`bool`: 

> Detach the pane into a floating window. Returns True if successful.

TouchDesigner Build: Latest\nwikieditor2025.300002021.100002020.200002018.28070before 2018.28070
