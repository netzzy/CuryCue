# Palette:multiTouch

This is documentation for the`multiTouch`component in the TouchDesigner [Palette](<./Palette.md> "Palette"). (See also the [MultiTouch](<./MultiTouch.md> "MultiTouch") page). 

The`multiTouch`Palette Component works with any Windows multi-touch device (and the mouse as well, since the [Multi Touch In DAT](<./Multi_Touch_In_DAT.md> "Multi Touch In DAT") merges both sets of events together, though, thanks to Windows 7 and 8, you can't perfectly use both kinds of devices at the same time). 

There are two simulations in the multiTouch component switch through the Swap button. The one`multiTouch/multiTouch`(confusingly), uses the Bullet collision dynamics system and is more current. The`multiTouch/multiPinch`component is a 2-finger scaling/rotating example, but it is older - it does not use Bullet dynamics. When one simulation is active, the other one has its cooking fully shut down. 

The essence of the examples is the workflow of rendering 3D scenes, grabbing objects in the scenes and moving them around, one finger per object. 

The flow is like this, which you will see when you go into the network: 

You create a Multi Touch In DAT and point it to a container panel (in this case it's the parent component, "`..`").That gathers the touch events in a table where u=v=0 is the bottom left of the container panel, and u=v=1 is the top-right. It only gets events of finger presses for that container. 

The background image of the container panel should be the output of a [Render TOP](<./Render_TOP.md> "Render TOP") (or any TOP that follows the Render that doesn't crop the image). 

You feed the Multi Touch In DAT into a [Render Pick DAT]], and you point the Render Pick DAT to the Render TOP. 

The Render Pick DAT is then ready and it outputs a table that indicates all the objects that are under your fingers (one object per finger at most), including their names, u, v values and other attributes. 

The Render Pick DAT has a callbacks DAT attached to it that does all the work to control the table called`states`. 

The callback is called every time a row in the table changes. It stuffs information into a "`states`" table that has one row for every object in your scene that is responsive to multi-touch. 

In the network, click the Show Interface button to bring up the panel so you can watch the tables while you operate the interface. 

With that "`states`" table you drive your 3D objects. In this case, it passes each row of the states table to a`dynamics`component, which uses CHOPs to drive the objects' x and y position etc.
