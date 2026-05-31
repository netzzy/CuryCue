# More Things to Know about TouchDesigner

This is a continuation of [First Things to Know about TouchDesigner](<./First_Things_to_Know_about_TouchDesigner.md> "First Things to Know about TouchDesigner").   
  
#### 36\. Exploring Other People's Components
* In any component, the square box at the top left of a pane brings up panel (or viewer) of the component you are in.
  * Use a Trail CHOP on CHOPs that animate to watch clearly their time-history.
  * Pressing the F10 or F9 keys with your cursor over any panel (click on the panel first) takes you to its source network in a floating window.

#### 37\. Output to Movie Files

TouchDesigner allows you to output the viewer contents of any operator to a movie file. You can use a [Movie File Out TOP](<./Movie_File_Out_TOP.md> "Movie File Out TOP") easily enough, but the following procedure is an alternative. First, start playing forward using the [Timeline](<./Timeline.md> "Timeline"). Right-click on the operator whose viewer you want to output. Select _Export Movie_ from the context menu that appears to bring up the [Export Movie Dialog](<./Export_Movie_Dialog.md> "Export Movie Dialog"). Select the output options for your movie such as resolution, codec and file name. Click on the _Start_ button to start recording to a QuickTime movie. To finish, click on the _Stop_ button. 

#### 38\. Connect MIDI Devices

See the [MIDI Device Mapper Dialog](<./MIDI_Device_Mapper_Dialog.md> "MIDI Device Mapper Dialog") to map a MIDI device to a MIDI device ID (not same as MIDI channel). 

The easiest way is to bringing a MIDI In CHOP, select your device, wiggle a control, and export that channel to a parameter or wherever you need it. 

#### 39\. Use Multiple Monitors for Output

See [Multiple Monitors](<./Multiple_Monitors.md> "Multiple Monitors") and you can use the convenient setup tool **windowCanvas** in the OP Snippets for [Window COMP](<./Window_COMP.md> "Window COMP"). 

#### 40\. Clones are Components kept in sync with a Master Clone

A [clone](<./Clone.md> "Clone") is a copy of a master component, with the additional feature that any time the master is changed (including the wiring and parameters of nodes inside it), all of its clones are changed to match it. 

Pick any component, like`container1`created above, put its name (`container1`) in the Clone parameter on the Common page, and copy/paste (Ctrl-C Ctrl-V, or via the network menu) the component twice. Make each clone's inputs different. You will see each clone's outputs are unique. 

All clone nodes and the nodes inside clones are darkened. See also [Clone](<./Clone.md> "Clone"), [Component](<./Component.md> "Component"). 

#### 41\. Simplify a Network by creating a new Component

You can select nodes, right-click on the network and select Collapse Selected. It will create a new [Base COMP](<./Base_COMP.md> "Base COMP") and the selected nodes will be placed inside it. Inputs and outputs to the component will be created and wired up to incoming and outgoing operators. 

If you want the new component to be a Container component, for example, right-click on the Base component and select Change OP Type. 

( Manually, the above can be accomplished as follows: First create a [Container COMP](<./Container_COMP.md> "Container COMP") in your network. Select the nodes you wish to to put in the container and copy them using Ctrl+C. Select the container and enter it by pressing "Enter" or "i" or by using the mouse scroll-wheel into the container. Once inside, paste the nodes into the container using Ctrl+V. If your nodes were originally wired to other nodes in the network, create In and Out CHOPs, TOPs, DATs, SOPs etc as necessary to establish inputs and outputs to the container. Then go back out the component and wire its inputs and outputs to the appropriate nodes. Then delete the nodes you originally copied. ) 

#### 42\. A Component Viewer shows the output of a Node inside - panel, polygon geometry or the Viewer of any OP

The viewer area of any component can contain a choice of things: Normally, [Panel Components](<./Panel_Component.md> "Panel Component") show their internal gadgets, and [Object](<./Object.md> "Object") viewers contain views of their 3D objects, which is the default. But in the component viewer you can put the viewer of any other operator, or the component's parameters, or an interactive view of the component's network. It's all managed with the Node View menu on the Common page of the component's parameters. 

#### 43\. Exporting using DATs

You can export from one DAT table to any number of parameters in any number of nodes, via [DAT Export](<./DAT_Export.md> "DAT Export"). The table needs 4 columns:`path`,`parameter`,`value`, and`enable`, and the DAT Export flag needs to be clicked On in the DAT. 

#### 44\. TouchDesigner crashes or hangs - what to do

Some day, TouchDesigner will crash or hang. If it crashes, it may prompt you to save the`CrashAutoSave.toe`file, which you can restart right away to get back to your work before the crash. The crash may ask you if you want a`.dmp`file, accept it and send the file to us. Don't bother sending the Microsoft crash files. If it hangs, on Windows, go to Task Manager, find the process, right click and save dump, then force quit the process. 

If TouchDesigner is full-screen with no borders, first try to press Esc with the cursor over the window. It may eliminate or shrink the window and allow you to save or restart. If you can get up the Task Manager, you can kill any TouchDesigner process there is in the Process section. If the Ctrl-Alt-Del key combination (or Ctrl-Shift-Esc ) doesn't give you the Task Manager or if nothing is killable, then you may need to reboot. 

Two (out of date) beginner videos: **[1](<./First_Things_to_Know_Part_1_Vid.md> "First Things to Know Part 1 Vid")** **[2](<./First_Things_to_Know_Part_2_Vid.md> "First Things to Know Part 2 Vid")**

  
**[Back to First Things](<./First_Things_to_Know_about_TouchDesigner.md> "First Things to Know about TouchDesigner")**
