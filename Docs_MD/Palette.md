# Palette

The Palette is a collection of useful [Components](<./Component.md> "Component") that you can drag-drop on to your [network](<./Network.md> "Network"). It is opened/closed via the [![PaletteIcon.jpg](./images/c/c0/PaletteIcon.jpg)](</File:PaletteIcon.jpg>) icon at the top-left of the UI.   
  
See [Category:Palette](<./Category-Palette.md> "Category:Palette") for some of the individual palette components. 

## Opening the Palette Browser

The Palette Browser can be accessed: 
* by selecting Dialogs -> Palette Browser from the main menu bar.
  * by clicking on the **Open Palette** button, found to the left of the Pane Layout options, underneath the File menu.
  * use python [UI Class](<./UI_Class.md> "UI Class") to open`ui.openPaletteBrowser()`## The Interface

Clicking on a Folder will display its in the Component section immediately below the folder section. When clicking on a Component, a preview window appears at the bottom of the interface giving you an icon preview and additional information. 

## Loading Palette Elements into TouchDesigner

To load a file from a palette, select the file from the browser and [Drag-and-Drop](<./Drag-and-Drop.md> "Drag-and-Drop") it into any TouchDesigner network. In addition, the file Preview can also selected and dropped into a network. 

## Adding Items to a Palette
* To add a component to a palette, drag the component onto a sub-folder under the "My Components" folder section.
  * To create a new sub-folder in My Components 
    1. Right-click on My Components or any sub-folder under My Components.
    2. Select “Add Folder” from the contect menu.
    3. Type the name of your new folder in the dialog that comes up.

## Removing Components or Folders from a Palette

To remove previously added components or folders, right click on it and select “Delete”. 

**Note:** Items from the default Palette or that are a part of the initial creation of a personal palette can not be deleted in this way. 

## Updating a Palette

When adding files to a folder that contains a Palette, these files are not automatically loaded into the Palette structure. To have them included, right click on the folder and select "Refresh Folder". The new components will now be displayed in the Palette.
