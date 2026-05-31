# Palette:gal

gal (Gadget Library) is a collection 11 master components that are simple UI gadgets like sliders, buttons, radios, menus, fields. 

It is being superseded by [Widgets](<./Widgets.md> "Widgets") in the UI / Basic Widgets palette folder. gal has been up updated to 2021.30000 to help upgrade projects that use prior versions. 

The gadgets here are totally self-contained and independent - they don't need any data, image or operators from outside the gadget. 

The UI for gal lets you drag-drop any gadget into your network. Or go inside and copy/paste any gadgets into your project networks, and adjust their custom parameters. The current value is always stored in the parameter Value (Value 1 and Value 2 for`xyslider`) which you can export or bind to. 

There are only 11 "master" gadgets from which all the variants you see have been configured via their custom parameters. The masters are:`slider`,`sliderL`(light),`sliderxy`,`knob`,`binary`,`binaryB (lighter)`,`binaryC (lightest)`,`radio`,`menu`,`string`,`label`. 

If you put this`gal`component in`/`, the gadgets you copy/paste from here will all be clones of the ones in`/gal`should it exist - All gadgets you paste will be clones of a gadget in this component according to the Clone parameter. 

If you are upgrading from a version of`gal`before Version 33, pulse the Update parameter on the Gal page which will assure all top-level parameters are up to date. 

You can delete this component after you copy/paste gadgets from it. Or put new versions of`gal`in`/gal`to auto-update gadgets in your projects. 

Inside the component, the gadgets in each row are actually the same gadget (they are clones of the first gadget in the row). They only vary via the use of their custom parameters. 

The "value" of the gadget is always the parameter 'Value' - that's where the master value of the gadget is kept. The first output of the gadget, a CHOP (except for`string`and`label`), always contains the current value of the parameter, and is named according to the Channel Name parameter, starting with`v1`. 

The gadgets and their look here can be customized by you. They are designed to be resizable, operate well with touch screens, and be as dark and monochrome as possible (so the UI doesn't distort/distract from the colors/levels/impression of the video you are producing). 

To any slider, knob or button (binary), you can map MIDI or any other control signals coming is as CHOPs. See the`readMe`in`mapper/`. 

Read the other`readMe`DATs here for more info. It is instructive to look inside the gadgets at their design ... it uses custom parameters, a minimum of nodes, and internally builds export DAT tables that customize the look/feel of the gadgets. 

Extra page "Push Value to Source" parameter: This is obsoleted by [Binding](<./Binding.md> "Binding"), which gives same functionality but has better visual feedback. Left here for backward compatibility.
