# Layout

The TouchDesigner window is made of a menu bar at the top, a [Timeline](<./Timeline.md> "Timeline") at the bottom, plus one of a choice of pane Layouts in the middle. A Layout is made of one or more panes, each pane can contain a Network Editor, Viewer, Panel, etc.. See [Panes](<./Pane.md> "Pane") for additional information on using panes. 

## The Layout Strip

Layouts can be saved and recalled using the **Layout Strip** which is directly below the menu bar at the top of the TouchDesigner window. 

To the left there is a collection of default pane layouts. There are 5 to choose; single, quad, vertical split, horizontal split, and tri split. Click on the appropriate icon to load the layout. 

## Saving Custom Layouts

You can also save your own custom layouts by clicking the add layout button. 

For example, if a layout is added while the TouchDesigner interface is split into 2 vertical panes, all that pane information (including pane's type and path) is saved in a custom layout and added to the layout strip. Layouts for a project are saved in the [.toe](<./.md> ".toe") file so that they are accessible each time the project is re-opened. Layouts are saved as layout components in`/local/layouts`. 

## Loading Custom Layouts

Clicking on the custom Layout will load the panes in the configuration that they were saved in as well as loading the saved network path for each pane. 

## Renaming and Deleting Custom Layouts

Right-clicking on a layout will open a menu with options to rename or delete the selected layout.
