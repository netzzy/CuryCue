# Pane Bar

At the top of every [Pane](<./Pane.md> "Pane") resides the Pane Bar. Here you can access pane options and navigate networks in TouchDesigner. 

  
The address bar in the center of the Pane Bar tells you which network you are currently working in. You can click inside the address bar and manually enter a path to any network in the project. Alternatively, you can navigate networks by clicking on one of the slashes ("/") in the address bar. When clicked, a drop down menu will contain a list of all available networks at that level of the project's hierarchy. 

Beside the address bar, there are a number of buttons in the Pane Bar, they are described below. 

  
[![PaneTypeIcon.png](./images/7/7d/PaneTypeIcon.png)](</File:PaneTypeIcon.png>) \- Selects the type of pane. 

  
[![PaneViewerIcon.png](./images/5/5e/PaneViewerIcon.png)](</File:PaneViewerIcon.png>) \- Opens the viewer of the parent component (ie. viewer for the current network). 

  
[![PaneBackIcon.png](./images/a/a8/PaneBackIcon.png)](</File:PaneBackIcon.png>) \- Analogous to a webbrowser's back button, takes you to the previously visited network address for this pane. 

  
[![PaneForwardIcon.png](./images/6/67/PaneForwardIcon.png)](</File:PaneForwardIcon.png>) \- Analogous to a webbrowser's forward button, takes you to the next visited network address after using the "Back" button above. 

  
[![PaneBookmarkIcon.png](./images/0/04/PaneBookmarkIcon.png)](</File:PaneBookmarkIcon.png>) \- Opens a drop down menu listing all bookmarks and gives the option of bookmarking the address in the current pane or opening the [Bookmarks Dialog](<./Bookmarks_Dialog.md> "Bookmarks Dialog"). Below is an exampe of the drop-down bookmark menu. 

  
[![PaneRootIcon.png](./images/c/c0/PaneRootIcon.png)](</File:PaneRootIcon.png>) \- Takes you to the root network, path = / 

  
[![PaneLinkIcon.png](./images/c/ca/PaneLinkIcon.png)](</File:PaneLinkIcon.png>) \- Lets you link panes by setting numerous panes to the same number in this drop down menu. 

  
[![PaneMaximizeIcon.png](./images/0/0a/PaneMaximizeIcon.png)](</File:PaneMaximizeIcon.png>) \- Maximizes the pane to fill the work area (only has an effect when using multiple panes). 

  
[![PaneOptionsIcon.png](./images/c/ce/PaneOptionsIcon.png)](</File:PaneOptionsIcon.png>) \- A menu of auxiliary options for the pane. This menu also contains the "name" of the pane at the top. This is useful for scripting and expressions that manipulate your panes and layout. 
* Split Left/Right - splits the pane into 2 panes left and right.
  * Split Top/Bottom - splits the pane into 2 panes top and bottom.
  * Duplicate Pane - creates a floating (separate window) copy of the pane.
  * Floating Copy - when using multiple panes, this will tear off the selected pane and place it in a floating window. Once that floating window pane is closed, the pane will reappear in the TouchDesigner layout.
  * Maximize - Maximizes the pane to fill the work area (only has an effect when using multiple panes).
  * Close - closes the pane.
