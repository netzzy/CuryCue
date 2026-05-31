# Palette:geoPanel

This example shows you how to put any 2D panels into a 3D scene with lighting and operate them as you would in 2D. 

This is in the [Palette](<./Palette.md> "Palette") under Techniques. 

You create a bunch of Panel Components as you would in 2D normally, and instead of displaying them in a 2D [Container COMP](<./Container_COMP.md> "Container COMP"), they are used in a 3D render by connecting each gadget (a 2D panel, see`geoPanel/geopanel1`) inside a customized [Geometry component](<./Geometry_COMP.md> "Geometry COMP") with custom parameters. The Render Pick DAT and the Render TOP are set up to operate the panels virtually. 

You can use a mouse with this, single-finger multitouch works as well, and multi-finger. 

A [tag](<./Tag.md> "Tag") '`geopanel`' on the`geo_*`components causes the Render Pick DAT callback to treat Geometry components to be treated in this way. All other 3D objects are ignored by the callback. 

**WARNING** : It's important that the Display flag is Off for all panels being displayed in 3D. That is, they should not also be displayed as 2D panels in the container of the 3D interaction. 

Discussion here: [https://www.derivative.ca/Forum/viewtopic.php?f=22&t=8027](<https://www.derivative.ca/Forum/viewtopic.php?f=22&t=8027>)

### Flow – How it Works
* You mouse click on the`geoPanel`container which only uses a 3D rendered image as the background. The click/drag/release events drives a [Multi Touch In DAT](<./Multi_Touch_In_DAT.md> "Multi Touch In DAT") that is pointing to`geoPanel`.
  * The [Multi Touch In DAT](<./Multi_Touch_In_DAT.md> "Multi Touch In DAT") is passed to the Render Pick DAT that is also connected to the 3D render. Render Pick gets back an event list in its callback that identifies which 3D objects were hit and where.
  * The [Render Pick DAT](<./Render_Pick_DAT.md> "Render Pick DAT") sends`interactTouch()`events to individual gadgets (panels) in`geoPanel`to operate them virtually.

### Family of 3D Gadgets in geoPanel/geoGadget

In`geoPanel/geoGadget`there are a bunch of template components.`geoGadget/geopanel`is the most generic in that you provide it a panel/gadget external to the component - in that example it's`button1`, but you can switch it to any gadget or any panel you've made. 

The rest of the components in`geoGadget`are slight mods of each other`**Bold text**`\- they all contain a generic gadget -`geoslider`contains`slider`,`geobinary`contains`binary`,`georadio`contains`radio`,`geomenu`contains`menu`, etc. so you don't need to provide your own gadget. Each of these is a master clone with unique parameters. Obviously you can adapt your own, but make sure you change the Clone parameter to a new name. 

On the right in`geoPanel`are the instances that are rendered in the Render TOP. 

Note that the customer parameters on the geogadgets like`geoslider`,`geobinary`, etc have parameters that are pulled inside, for example a`slider`gadget using refererence expressions inside the`geogadget`. These particular geogadgets use`gal`gadgets which have the added feature of pushing values back up to the custom parameters when you operate the gadgets virtually. 

**Note** : The geoGadgets don't handle entering text yet. 

Note: The geoGadgets are designed to over-render their icons - i.e. a 100x50 gadget is rendered internally at 200x100 to give better close-up appearance. 

### Yanking This Functionality to Other Projects

You can copy/paste these nodes to some other place (`.toe`) and go from there: 

  *`geoGadget/*`(and/or others)
  * Render TOP (which you can replace later)
  * Render Pick DAT with its callback DAT
  * Multi Touch In DAT
  * the background, camera and light - which you can delete later


Or to start from scratch within`geoPanel`, delete the right column of Geogadgets (blue), then copy/paste components from them left and move/customize them. 

### Remote Operation of geoPanel

See [remotePanel](</index.php?title=Palette:RemotePanel&action=edit&redlink=1> "Palette:RemotePanel \(page does not exist\)"). Aside from working directly with a mouse and Windows-supported touch screens (both via Multi Touch In DAT), you can remotely drive the main`geoPanel`container with`panel.interactTouch()`and`panel.interactMouse()`. 

This is locally set up in`geoPanel/virtualPanel`and`virtualMouse`. Here it runs on the same machine in the same process, but you can move it to another process and/or machine and slightly change the code. 

As it is now, you can bring up`virtualPanel`in a floating window (it will be black) and then go into Perform Mode or bring up`geoPanel`in another floating window. As you move your mouse over the black panel, a circle moves in the`geoPanel`window and you can see the effect of rolling over the buttons with border highlights. If you click, it will operate the gadgets in`geoPanel`. 

In`virtualMouse`is the Parameter Execute DAT that either uses`interactMouse()`or`interactTouch()`to operate the panel. If you want to move the virtual control to another process, you would leave`virtualMouse`where it is, and change`virtualPanel`to receive TUIO, OSC or raw TCP/IP DAT messages that affect the three parameters of`virtualMouse`: Panel Select, Panel U and Panel V, just like it does now locally.
