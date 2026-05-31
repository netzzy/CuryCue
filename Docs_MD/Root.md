# Root

TouchDesigner is a hierarchy of components. "Root" is the top-most network in the hierarchy. The [Network Path](<./Network_Path.md> "Network Path") or Path for root is simply`/`. A typical path is`/project1/moviein1`. 

Normally you work in components under`/`, like in`/project1`, but you can put all you want in`/`. 

Root also contains`/local`, which contains things line MIDI settings, [Layout](<./Layout.md> "Layout"), python modules that are accessible from anywhere, and [Variables](<./Variables.md> "Variables").`/local`is saved intact in the`.toe`file, and is reloaded from the`.toe`on restart. Parts of`/local`are controlled via dialogs like the MIDI mapper, but given a lot of`/local`is text files and tables, most things can be edited manually by the user. 

Other things that are commonly put in Root: 
* startup scripts (use [Execute DAT](<./Execute_DAT.md> "Execute DAT"))
  * [Window Components](<./Window_COMP.md> "Window COMP") to manage outputs to monitors
  * [Audio Device Out CHOPs](<./Audio_Device_Out_CHOP.md> "Audio Device Out CHOP") to output to audio devices from one place, if that is desired.
  * common libraries, components and scripts that you want to be accessible to all your parts of your project.


Root is actually a [Base COMP](<./Base_COMP.md> "Base COMP"). See if you can find a way to display its parameter dialog! There are at least two ways. 

For this reason, it is better to do most of your work in components like`/project1`, which makes the component exportable and share-able via [RMB](<./Mouse_Click.md> "Mouse Click")->Save Component.... 

In Root you normally have`/perform`, which is a Window Component. It is tied to the [Window Placement Dialog](<./Window_Placement_Dialog.md> "Window Placement Dialog") and is the default Window Component used for [Perform Mode](<./Perform_Mode.md> "Perform Mode").`/ui`and`/sys`are not saved in the`.toe`. They are reloaded when TouchDesigner starts. You can look inside`/ui`and`/sys`, but there is not much use in changing it.
