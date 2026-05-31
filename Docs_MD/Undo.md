# Undo

Undo and redo operations are supported in two ways. Most of the support is for the design mode (editing networks in TouchDesigner), with limited support in perform mode.   
  
In design mode where you are editing netwoks, user interactions such as creating or deleting nodes, changing node parameters etc, can be reverted via the Edit->Undo menu or Ctrl-Z (Cmd-Z for macOS). Edit->Redo or Ctrl-Y (Cmd-Shift-Z for macOS) will redo any undos. 

## Undo in Scripts and Textports

By default, scripts will not create undo actions. To create undo steps in scripts, use the [Undo Class](<./Undo_Class.md> "Undo Class"). 

## Supported Operations
* Node operations - create, delete, placement, flag changes, wiring and un-wiring, renaming.
  * Node parameter changes via user interaction or scripting. (including multi-node parameter changes via selecting nodes)
  * Copy and paste - including duplicating nodes and text editing
  * DAT text and table editing, via DAT editors or external editors.
  * Keyframe animation editing.

## Unsupported Operations
* Undo in geometry editing is pending.
  * Changing node selection.
  * [Text COMP](<./Text_COMP.md> "Text COMP") has a multi-step local undo system while editing, and will also create an undo step for the final result.
  * [Field COMP](<./Field_COMP.md> "Field COMP") only uses a local one-step undo, which is not tied to the main undo/redo queue. This component is deprecated, use [Text COMP](<./Text_COMP.md> "Text COMP") instead.

## Perform Mode

Undo in perform mode works only on items that would work in the Editor. Most things in Perform mode will require scripts if you want to create undo steps. See [Undo Class](<./Undo_Class.md> "Undo Class") for info.
