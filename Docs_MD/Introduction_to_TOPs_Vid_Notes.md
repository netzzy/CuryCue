# Introduction to TOPs Vid Notes

### What you're going to create

This tutorial will introduce how to take an image of a butterfly, modify the levels of the image, place it over a larger canvas and then add a background alongside some basic compositing techniques. It is advised to watch the video version of this tutorial as it contains a stronger insight into the best practices whilst using TouchDesigner. 

### Bring an image into TouchDesigner
* Open TouchDesigner and click the X at the top of the [palette](<./Palette.md> "Palette") browser on the left quarter of the screen.
  * Double click the [network](<./Network.md> "Network") editor to open the [OP Create Dialog](<./OP_Create_Dialog.md> "OP Create Dialog") and under the TOP tab select “Movie File In” to lay down a [Movie File In TOP](<./Movie_File_In_TOP.md> "Movie File In TOP").
  * There should now be a new [node](<./Node.md> "Node") in your [network](<./Network.md> "Network"). Left click the [node](<./Node.md> "Node") to open its [parameters](</index.php?title=Parameters&action=edit&redlink=1> "Parameters \(page does not exist\)") at the top right quarter of the [network](<./Network.md> "Network") editor. If you don't see the [parameters](</index.php?title=Parameters&action=edit&redlink=1> "Parameters \(page does not exist\)") press the P key to toggle them on and off.
  * In the [parameter](<./Parameter.md> "Parameter") window where it says file click the plus icon to open up the file browser. Select the butterfly6 file from the directory that opens.

### Change the levels of the image you just imported
* On the right hand side of the [node](<./Node.md> "Node") right click the wire out icon and select a [Level TOP](<./Level_TOP.md> "Level TOP"). Left click to place the [level TOP](<./Level_TOP.md> "Level TOP") into the [network](<./Network.md> "Network").
  * In the [level TOP](<./Level_TOP.md> "Level TOP") parameters window click the “Pre” tab and set the following values: Black Level: 0.14, Brightness: 1.5.
  * The butterfly in the viewer should be much brighter and less saturated than the previous butterfly in the [Movie File In TOP](<./Movie_File_In_TOP.md> "Movie File In TOP").

### Set the Resolution of the [Viewer](<./Viewer.md> "Viewer")
* Double click the [network](<./Network.md> "Network") below the [Movie File In TOP](<./Movie_File_In_TOP.md> "Movie File In TOP") and select a [Constant TOP](<./Constant_TOP.md> "Constant TOP"). Under the constant tab in the parameter window set the Alpha value to 0. Under the common tab to the right of the Custom Res [parameter](<./Parameter.md> "Parameter") there is an arrow. Clicking the arrow brings up the [Constant TOPs](<./Constant_TOP.md> "Constant TOP") resolution. Set the resolution to 1280x720.

### Compositing the butterfly over the blank viewer
* Right click the wire out from the [Level TOP](<./Level_TOP.md> "Level TOP") you created and place down a [Composite TOP](<./Composite_TOP.md> "Composite TOP").
  * Left click the Constants output and then left click the input of the [Composite TOP](<./Composite_TOP.md> "Composite TOP").
  * Select the [Composite TOP](<./Composite_TOP.md> "Composite TOP") by left clicking the [node](<./Node.md> "Node") and then in its [parameters](</index.php?title=Parameters&action=edit&redlink=1> "Parameters \(page does not exist\)") under the Composite tab set the Operand parameter to Over. Under the Transform tab set Fixed Layer to Input 2. In the viewer you should now have a butterfly with more checkerboard space around it.

### Set the position of the butterfly and add a gradient background
* Right click the [composite TOPs](<./Composite_TOP.md> "Composite TOP") output and select a [Transform TOP](<./Transform_TOP.md> "Transform TOP").
  * Under the [Transform TOPs](<./Transform_TOP.md> "Transform TOP") [parameters](</index.php?title=Parameters&action=edit&redlink=1> "Parameters \(page does not exist\)") middle clicking the x and y numbers under the Translate [parameter](<./Parameter.md> "Parameter") you can drag left and right to position the butterfly. You can also enter numbers manually.
  * Double click below the [Transform TOP](<./Transform_TOP.md> "Transform TOP") and lay down a [Ramp TOP](<./Ramp_TOP.md> "Ramp TOP"). In the [Ramp TOPs](<./Ramp_TOP.md> "Ramp TOP") [parameters](</index.php?title=Parameters&action=edit&redlink=1> "Parameters \(page does not exist\)") under the Ramp tab you can set a gradient using the gradient bar. To change the color select the rectangle of the color you wish to change and then under the Hue, Saturation and Value parameters change the colors to a lighter blue and a darker blue.
  * Under the common tab change the [Ramp TOPs](<./Ramp_TOP.md> "Ramp TOP") resolution to 1280x720.
  * Right click the [Transform TOPs](<./Transform_TOP.md> "Transform TOP") output and lay down another [Composite TOP](<./Composite_TOP.md> "Composite TOP").
  * Wire the [Ramp TOP](<./Ramp_TOP.md> "Ramp TOP") into the [composite TOPs](<./Composite_TOP.md> "Composite TOP") input.
  * Set the [Composite TOPs](<./Composite_TOP.md> "Composite TOP") operand parameter to Over.

### Adding another butterfly
* Middle click the [Transform TOP](<./Transform_TOP.md> "Transform TOP") and select another [Transform TOP](<./Transform_TOP.md> "Transform TOP") from under the [TOP](<./TOP.md> "TOP") tab.
  * Select the new [Transform TOP](<./Transform_TOP.md> "Transform TOP") and set the Translate parameter to -0.2.
  * Set the Scale x and y parameters to 0.3 and 0.3. This will allow the butterflies to be different sizes.
  * Left click the output of the new [Transform TOP](<./Transform_TOP.md> "Transform TOP") and then left click the input of the second [Composite TOP](<./Composite_TOP.md> "Composite TOP") to [wire](<./Wire.md> "Wire") them together.
  * In the second [Composite TOPs](<./Composite_TOP.md> "Composite TOP") [parameters](</index.php?title=Parameters&action=edit&redlink=1> "Parameters \(page does not exist\)") where it says Input OP click the up arrow next to Transform2 to move the [Transform TOP](<./Transform_TOP.md> "Transform TOP") above the Ramp.

### Viewing the butterflies in [Perform Mode](<./Perform_Mode.md> "Perform Mode")
* Right click the output of the third [Composite TOP](<./Composite_TOP.md> "Composite TOP") (comp3) and select an [Out TOP](<./Out_TOP.md> "Out TOP") from the TOP tab.
  * At the very top left of the screen above the [Network](<./Network.md> "Network") Editor there is a ^ icon. Click it to place the project into [Perform Mode](<./Perform_Mode.md> "Perform Mode"). To exit [Perform Mode](<./Perform_Mode.md> "Perform Mode") press the Esc key.
  * The resolution is different from the [Out TOPs](<./Out_TOP.md> "Out TOP") in [Perform Mode](<./Perform_Mode.md> "Perform Mode") due to [Perform Mode](<./Perform_Mode.md> "Perform Mode") using the Project1 COMPs width and height. Zoom out of the [network](<./Network.md> "Network") until you see Project1 (or you can click the / in the path bar above the [Network](<./Network.md> "Network") Editor then click / in the drop down menu)
  * Select Project1 and in its [parameters](</index.php?title=Parameters&action=edit&redlink=1> "Parameters \(page does not exist\)") under the Layout tab set the width [parameter](<./Parameter.md> "Parameter") to 1280 and the height [parameter](<./Parameter.md> "Parameter") to 720
  * Click the ^ icon at the top left of the screen above the [Network Editor](<./Network_Editor.md> "Network Editor") to switch to [Perform Mode](<./Perform_Mode.md> "Perform Mode"). You can then press the Escape Key to close [Perform Mode](<./Perform_Mode.md> "Perform Mode").

### Extra - Making the butterflies wings flap using a transforms scale parameter
* Double click the network and under the CHOP tab whilst holding shift click the following: LFO, Math and Null. You should now have 3 new nodes.
  * In the Math CHOPs range parameters set the From Range from -1 to 1 and the To Range from 0.2 to 1.
  * Right click the null and select CHOP Export. The CHOP Export Dialog should now appear
  * Left click the first Transform TOP (transform1) whilst keeping the chop export dialog open above and to the side, then left click and drag the chan1 text to the value in the Transforms Scale x parameter. A small arrow and a plus icon will appear, let go of the drag and the parameter should turn blue. If all has worked correctly the butterflies will now flap their wings in time to the LFO CHOP.
