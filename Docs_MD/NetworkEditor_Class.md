# NetworkEditor Class

The NetworkEditor class describes an instance of a [Network Editor](<./Network_Editor.md> "Network Editor"). They are subclasses of the [Pane Class](<./Pane_Class.md> "Pane Class"), which can be accessed from the [ui](<./UI_Class.md> "UI Class") object. 

## Members`showBackdropCHOPs`→`bool`: 

> Enable or disable [CHOP](<./CHOP.md> "CHOP") viewers as backdrops.`showBackdropGeometry`→`bool`: 

> Enable or disable [SOP](<./SOP.md> "SOP") and [Geometry object](</index.php?title=Geometry_Object&action=edit&redlink=1> "Geometry Object \(page does not exist\)") viewers as backdrops.`showBackdropTOPs`→`bool`: 

> Enable or disable [TOP](<./TOP.md> "TOP") viewers as backdrops.`showColorPalette`→`bool`: 

> Enable or disable display of the operator color palette selector.`showDataLinks`→`bool`: 

> Enable or disable operator data links.`showList`→`bool`: 

> Control display of operators as a list, or connected nodes.`showNetworkOverview`→`bool`: 

> Enable or disable display of the network overview.`showParameters`→`bool`: 

> Enable or disable display of the currently selected operator parameters.`straightLinks`→`bool`: 

> Control display of operator links as straight or curved.`x`→`float`: 

> Get or set the x coordinate of the network editor area, where 1 unit = 1 pixel when zoom = 1.`y`→`float`: 

> Get or set the y coordinate of the network editor area, where 1 unit = 1 pixel when zoom = 1.`zoom`→`float`: 

> Get or set the zoom factor of the network editor area, where a zoom factor of 1 draws each node at its unscaled resolution.

## Methods`fitWidth(width)`→`None`: 

> Fit the network area to specified width, specified in node units. This affects the zoom factor. 
> 
>   * width - The width to fit to.
>`fitHeight(height)`→`None`: 

> Fit the network area to specified height, specified in node units. This affects the zoom factor. 
> 
>   * height - The height to fit to.
>`home(zoom=True, op=None)`→`None`: 

> Home all operators in the network. 
> 
>   * zoom - (Keyword, Optional) When true, the view will be scaled accordingly, otherwise the nodes will only be re-centered.
>   * op - (Keyword, Optional) If an operator is specified, the network will be homed around its location.
> 

[code]
>     p = ui.panes['pane1']
>     n = op('/project1')
>     p.home(op=n)
>     p = ui.panes[2]
>     p.home(zoom=True)
>     
[/code]`homeSelected(zoom=True)`→`None`: 

> Home all selected operators in the network. 
> 
>   * zoom - (Keyword, Optional) When true, the view will be scaled accordingly, otherwise the nodes will only be re-centered.
>`placeOPs(listOfOPs, inputIndex=None, outputIndex=None, delOP=None, undoName='Operators')`→`None`: 

> Use the mouse to place the specified operators in the pane. 
> 
>   * listOfOps - The list of operators to be placed.
>   * inputIndex - If specified, which input index to connect to.
>   * outputIndex - If specified, which output index to connect to.
>   * delOP - If specified, deletes that operator immediately after placing the listOfOPs.
>   * undoName - Describes the [Undo](<./Undo.md> "Undo") operation.
> 

# Pane Class

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

TouchDesigner Build: Latest\nwikieditor2021.100002018.28070before 2018.28070
