# Network Editor

The **Network Editor** is a pane type in TouchDesigner that is used to create and modify [Operators](<./Operator.md> "Operator"). The Network Editor is the default pane type for TouchDesigner and is visible when the program is launched. Navigating in the Network Editor is an important skill to learn early in TouchDesigner. Mastery of the Network Editor allows you to more easily modify and update your networks over time. The primary tool for network navigation is the mouse, although some operations have menu or keyboard equivalents. Each mouse button manipulates the Network Editor interface in a different way. 

## Network Navigation

### Node Selection

Use the left mouse button [LMB](<./Mouse_Click.md> "Mouse Click") to select nodes. To box-select multiple nodes hold shift while dragging with LMB or use the [RMB](<./Mouse_Click.md> "Mouse Click"). Alternatively, you can hold down the _Ctrl_ key and left-click on each individual node you want to add to the selection. To move a node, select it and keep the LMB depressed to drag it around the Network Editor. 

### Moving Around the Network

The left mouse button (LMB) navigates networks without changing the zoom level. Drag using the LMB in any empty area in the network to pan around the network. A scale 'overview' representation of the Network can be toggled on and off with the "**o** " key. 

### Zooming

The middle mouse button [MMB](<./Mouse_Click.md> "Mouse Click") controls the zoom level, hold MMB and drag right or left to zoom in or out. To return to **Unity Zoom** (zoom level of 1), use the keyboard shortcut "**f** " for **Unity Frame All**. 

If the middle mouse button is also a scroll wheel on your mouse, scroll forwards to zoom in and scroll backwards to zoom out. 

You can also box zoom by holding down the Ctrl button while using the MMB. To zoom in, hold down Ctrl and draw a box from left to right with the MMB. To zoom out, draw the box from right to left. 

### Moving Between Networks

There are several ways to move in and out of Component networks. 

To enter a network (go inside a component): 
* double-click on a component to go inside its network
  * use the scroll wheel to zoom up close to a component and keep zooming in to go inside its network
  * select the component and then press <Enter> key to go inside its network
  * select the component and then press the < i > key to go inside its network
  * select the component and then press the 'double arrow' in the [network path](<./Network_Path.md> "Network Path") found at the top of the [pane](<./Pane.md> "Pane")
  * on the component click [RMB](<./Mouse_Click.md> "Mouse Click") and select **Enter Component** from the menu


When inside a Component, to go up a level: 
* press the`u`key
  * use the scroll wheel to zoom out
  * in the [network path](<./Network_Path.md> "Network Path") found at the top of the [pane](<./Pane.md> "Pane"), click on the component’s name you want to see. For example, if the path is /project1/scene1/geo2 and you want to go /project1, simply click on the word "project1".
  * you may find the **Back** and **Forward** buttons in the top [pane bar](<./Pane_Bar.md> "Pane Bar") handy to navigate in and out of Components.

## Interacting with Operators

Here are some other interactions you can perform in the Network Editor. 
* Resize nodes by grabbing the edge of the node with LMB and dragging
  * Grid snapping is on by default, adjust grid options in [Preferences](<./Dialogs-Preferences_Dialog.md> "Dialogs:Preferences Dialog") (Edit > Preferences > Network)
  * Layout and Display options are found in the Network Editor's RMB menu
  * [Node Viewers](<./Node_Viewer.md> "Node Viewer") can go into [Viewer Active](<./Viewer_Active.md> "Viewer Active") mode (interactive mode) by clicking on the [Viewer Active](<./Viewer_Active.md> "Viewer Active") flag found in the lower-right corner.
  * Middle-clicking on node will open the operator info popup.
  * [Flags](<./Flag.md> "Flag") on the operators can be used to toggle their state (display state, render state, pickable state, etc)
  * Animated [Wires](<./Wire.md> "Wire") indicate data flow between operators.
  * The Network Editor can be toggled to **list mode** by pressing the shift+t keyboard shortcut or by selecting if from the right-click menu.

## See also
* [Network](<./Network.md> "Network")
  * [Zoomable User Interface](<./Zoomable_User_Interface.md> "Zoomable User Interface")
