# Panel

A Panel, or Control Panel is a custom graphical user interface user control built within TouchDesigner. See [Panel Component](<./Panel_Component.md> "Panel Component"), which are used to create such user interfaces. 

The "look" of a panel is created using the [Text COMPs](<./Text_COMP.md> "Text COMP") and [TOPs](<./TOP.md> "TOP"). 

The "feel" or behavior is determined by the settings of the [Panel Components](<./Panel_Component.md> "Panel Component"), the [Panel Execute DAT](<./Panel_Execute_DAT.md> "Panel Execute DAT"), [Extensions](<./Extensions.md> "Extensions") in the panel, the panel member of the [panelCOMP Class](<./PanelCOMP_Class.md> "PanelCOMP Class"), and the use of the Panel CHOP which turns [Panel Values](<./Panel_Value.md> "Panel Value") into CHOP Channels. 

To display a panel in a floating or fixed-position window on your monitors, use the [Window COMP](<./Window_COMP.md> "Window COMP"). 

While editing, a panel can be viewed by 
* right-clicking on a [Panel Component](<./Panel_Component.md> "Panel Component") and selecting _View..._
  * changing [Pane](<./Pane.md> "Pane") type to _Panel_
  * clicking on the [Pane Bar](<./Pane_Bar.md> "Pane Bar") the square icon (Open Viewer) if you are working inside a Panel component
