# First Things to Know about TouchDesigner

These are the basics to help you become skilled in working with the TouchDesigner interface. This will take you about 2-3 hours if you pause and work through it sequentially. We will touch on all the main parts and concepts of TouchDesigner, as well as all the basics of operating the UI. Afterwards you will hopefully be more proficient and comfortable with exploring TouchDesigner on your own. 

**TIP** : If the meaning of a term in TouchDesigner is unclear, you can look it up in the **[TouchDesigner Glossary](<./TouchDesigner_Glossary.md> "TouchDesigner Glossary")** or **Search** for it, both found in the menus to the left.   

#### 1\. Starting TouchDesigner

To use TouchDesigner, you will need a 3-button mouse with a roller wheel. (If you have no mouse or middle mouse button, you can use alt+rightclick to substitute for middleclick.) 

Start by double-clicking the TouchDesigner icon on the desktop. 

When you start TouchDesigner, you see the [network](<./Network.md> "Network") editor on the right, and the [Palette](<./Palette.md> "Palette") browser on the left. Close the palette by clicking the x at its upper right corner to get more space until you need it. 

#### 2\. Pan, zoom and center the Network

To pan the network, click and drag the left mouse button ([LMB](<./Mouse_Click.md> "Mouse Click")) on an empty area of the network. 

To zoom the network, click and hold down the middle mouse button ([MMB](<./Mouse_Click.md> "Mouse Click")) and drag it left-and-right. (Reminder: If you don't have a middle mouse button, press alt+rightclick.) 

Alternately, to zoom you can move the rollerwheel forward and backward. 

Press the "h" key to center it (this is also called **h** oming). To home just the highlighted node, press Shift-h. 

In an empty area of the network right-click ([RMB](<./Mouse_Click.md> "Mouse Click")) and release the mouse - you will see the network menu. Choose 'Home All'. 

#### 3\. Current Nodes and Selected Nodes

Click on one of the nodes. This gives it a green border and makes it the "current" node. Only one node in a network is current. 

Left-click on another node and drag it to a new location. Notice the current node does not change. 

To box-select several nodes, click and hold down the right mouse button in an empty area, drag the mouse over the nodes, and release. 

Yellow borders around nodes mean they are "selected". The green node is selected too. 

Left-click on any selected node and drag it - all the selected nodes move together. 

To add more to the set of selected nodes, Shift-click, or Shift-box-pick other nodes. To un-select a selected node, Shift-click on it. 

You can act on selected nodes together. Right-click on the network background and select Delete to remove the nodes, then press Ctrl+z to undo (Command+z on macOS). You can also undo via the Edit menu. 

Now click the top-left corner ([Flag](<./Flag.md> "Flag")) on any of the selected nodes. This toggles between all their [Node Viewers](<./Node_Viewer.md> "Node Viewer") and their 3-letter icons. Turn back on the node viewers. 

To un-select everything, left-click on the background of the network, which un-selects all the nodes except for the green "current" node. 

Right-click on one of the nodes - you will see the node menu. Choose 'View' to bring up a floating window. Resize it by clicking-and-dragging the edges. Now you can close the viewer window by clicking it in the corner. 

#### 4\. TouchDesigner Operators Generate and Filter Data

To delete all the nodes, press Control-a to select all, then press Delete. 

Now double-click on the empty network. The [OP Create Dialog](<./OP_Create_Dialog.md> "OP Create Dialog") appears, where OP means "[operator](<./Operator.md> "Operator")", or "node". The purple "TOP" tab should be selected. [TOPs](<./TOP.md> "TOP") are Texture Operators and work with images. Click on Movie File In, then click anywhere on the network to place it. 

You can also press Tab to bring up OP Create. To cancel, click the background. 

On the right side of`moviefilein1`, right-click on its purple output connector. On the OP Create click 'Level' and then click to the right of`moviefilein1`to create`level1`, which will be connected to`moviefilein1`. You have just added an image "[filter](<./Filter.md> "Filter")" (`level1`) that modifies the levels of an image "[generator](<./Generator.md> "Generator")" (`moviefilein1`). 

TouchDesigner Operators are Generators or Filters. "Filters" require at least one input, and modify the data of an incoming operator. 

"Generators" do not require an input - they create new data or read data from external devices and programs. Darker-colored OPs are the generators. Lighter colored OPs are filters. 

Click on`level1`. On the top-right dialog, move the sliders labelled Black Level and Brightness. These are typical "[parameters](<./Parameter.md> "Parameter")" in TouchDesigner, which we will cover soon. 

#### 5\. In the Network Editor, add an Operator from each Family

Let's look at rest of the six families of operators. Once again, double-click on the background. 

The [OP Create Dialog](<./OP_Create_Dialog.md> "OP Create Dialog") has six headings of what we call [Operator Families](<./Operator.md> "Operator"). Click on '[CHOP](<./CHOP.md> "CHOP")' for 'Channel Operators'. Press Tab several times to cycle back to CHOPs. 

Click on the CHOP type "Pattern" and place the Pattern CHOP in the network in a row above the TOPs. Channel Operators are used for motion, control signals, audio and more. 

Bring up OP Create again. You can find a specific operator by typing its name. Type "noi", click on Noise, and before clicking again, you can use the roller wheel to zoom the network and find a space, and click to create a [Noise CHOP](<./Noise_CHOP.md> "Noise CHOP"). 

Bring up OP Create and Click "SOP". Surface Operators ([SOPs](<./SOP.md> "SOP")) work with polygons, 3D lines and other surfaces. Choose a [Sphere SOP](<./Sphere_SOP.md> "Sphere SOP") and place the node in the network. 

Press the Tab key and select "MAT". Material Operators ([MATs](<./MAT.md> "MAT")) add textures and shading to 3D objects. Choose a [Phong MAT](<./Phong_MAT.md> "Phong MAT") and place the node. 

Press the Tab key and select "DAT". Data Operators ([DATs](<./DAT.md> "DAT")) manipulate text strings, both free-form text and in tables. Choose a [Monitors DAT](<./Monitors_DAT.md> "Monitors DAT"), which is a table containing one row for every monitor attached to your computer. 

Press the Tab key and select "COMP" for Components. There are four categories of components. From the 3D Objects column on the left, choose a [Geometry COMP](<./Geometry_COMP.md> "Geometry COMP"), which unites SOPs and a Material for 3D rendering. 

Press the Tab key again. From the Panels column, choose a [Slider COMP](<./Slider_COMP.md> "Slider COMP"), which is one of the 2D gadgets for building control panels. 

You now have examples of all Operator Families in your network. 

#### 6\. Connect Nodes together with Wires

(Box-pick everything except the two TOPs and move them up out of the way.) 

Node inputs are found on their left side, and node outputs are on their right side. Think of the data generally flowing left-to-right. 

Now press Tab and create a TOP called Monochrome, by typing 'mon', and place it to the right of`level1`. 

Connect the output of`level1`to the input of`mono1`in one of four ways: First, click`level1`'s output and without releasing, drag to`mono1`'s input and release. 

The connecting lines between nodes in the same family are called [Wires](<./Wire.md> "Wire"). 

Press Ctrl-z to undo the wiring. Now click-release on`level1`'s output, then click-release on`mono1`'s input. Or you can connect in reverse order from the`mono1`'s input to`level1`'s output. 

Click and drag the Monochrome TOP to the right to create some space between. 

To insert a new node between the two already-connected nodes, right-click the output of the`level1`node and select a Tile TOP and place it in the network. 

Undo with Ctrl-z. Now right-click on the wire, and select Insert Operator from the menu. Choose and place a Tile TOP. 

To create a new branch from a node, middle-click on the output of`tile1`and select Edge from the Operator menu and place it in the network above`mono1`. 

Remove a wire by clicking on the input of`edge1`, and then clicking on empty space in the network. 

Now reconnect`edge1`to`tile1`. 

Another way to disconnect is to right-click on the wire and select Disconnect from the menu. Reconnect`edge1`again. 

Replace an input to a node by clicking from another node’s output to anywhere along an existing wire. 

#### 7\. Wires, Data Flow and Cooking

You can think of data flowing along these wires, in this case, images. Now watch the wires animate. Click on`level1`, go to its [Parameter Dialog](<./Parameter_Dialog.md> "Parameter Dialog") on the right, and operate the Brightness slider. When a wire is animating it means that data is flowing: the node upstream is [cooking](<./Cook.md> "Cook") and giving its output to the next node to cook, and so on downstream. 

Middle-click on`tile1`. This shows information about the TOP. Look at Total Cooks to see how many times it has cooked, and then middle-click on`moviefilein1`and see it has only had to cook once, because it's not changing. 

Let's look at top-bottom connectors. Let go back to the`geo1`Geometry component. 

Put a Null component above the geo1 component. The 3D components like Geometrys, Cameras and Lights have connectors on their bottoms and tops (connect them) which connects them as parent-child in a [3D](<./3D.md> "3D") hierarchy, but no data flows along them. 

Put a Container component above the geo1 component. In the same way, the 2D components like Sliders, Buttons and Containers also have connectors on their bottoms and tops (connect them), which is one way to group them in a panel. Again, no data flows along them, data only flows through the wires on the sides. 

#### 8\. Make a Viewer Active to inspect Operator data

(Let's look at at the`geo1`component more closely) Up to now, when you left-click on a node, you move it or make it current. You can't change the viewer. Middle-click shows the common info box, and right-click shows the common node menu that all nodes share. 

(Reminder: If you don't have a middle mouse button, press Alt+Right-click.) 

Clicking the "[Viewer Active](<./Viewer_Active.md> "Viewer Active")" flag at the bottom right of`geo1`removes its border and allows you inspect more closely the contents of the operator's data. Click-and-drag any of the mouse buttons to move around the geometry, and a quick right-click gives you an operator-specific menu of viewing options, which is where you find the wireframe toggle. 

In the case of panels, if you click Viewer Active, it lets you operate the panel. 

There are two more ways to make the viewer active: 
* First, Alt+a puts all nodes into the Viewer Active state until you let go.
* Second, with the cursor over the background, the [shortcut](<./Shortcut.md> "Shortcut") key "`a`" will toggle the Viewer Active flag of all selected nodes.


Even when a node has its Viewer Active flag on, you can still access the common popups. On the name bar at the bottom, middle click to get the node info, and right click to get the nodes' common menu. 

You can click-drag the operator from the bottom name bar any time. If you just click the name bar, it will make it current, but also puts you in a mode to edit the name until you click away, so you may prefer to just box pick it. 

( Let's tidy up before we go on: Home the network select the nodes whose Viewer Actives are on and turn them off. ) 

#### 9\. Adjust Parameters of Operators

Every Operator in TouchDesigner has a set of [Parameters](<./Parameter.md> "Parameter") that affects its output. Select and look at`pattern1`. The [Parameter Dialog](<./Parameter_Dialog.md> "Parameter Dialog") is normally docked in the upper right corner of a Network. Press the lower-case`p`key to hide it and gain more space, and`p`again to bring it back. 

To see`pattern1`'s parameters in a floating window, right-click on`pattern1`and select Parameters.... 

You can change the parameter of several OPs at once. Click`pattern1`, and press Ctrl+c and Ctrl+v twice to create`pattern2`and`pattern3`(Command+c and Command+v on macOS). Click`pattern2`and change its Type menu to Ramp. Now box-select`pattern1`to`pattern3`. Increase the parameter Number of Cycles. When you release you see that all three OPs' Cycles parameter are set to the same value. 

To reset just one parameter, right-click on the label of the Type parameter of`pattern2`, which brings up the parameter menu, and select Reset Parameter. 

To reset all parameters of operators back to their default values, right-click on a node and choose Reset all Parameters. Alternately, on the parameter dialog's "i" icon, you can right-click to bring up the same node menu. 

#### 10\. Value Ladders help you change Parameter values

Now let's adjust parameters with a value ladder. Pick the`noise1`CHOP. 

On the Parameter Dialog, on the Period parameter's name or value, middle-click and hold down the button. The [Value Ladder](<./Value_Ladder.md> "Value Ladder") will pop up with a number of increments labelled .001 .01 .1 1 10. With the middle-mouse still down, move vertically to one of the increments, say .01, then move off to the right/left to increase/decrease the parameter value. Try the same thing with another increment. 

Click on the parameter dialog's Transform page. If the parameter has two or more values like the Translate parameter, when you middle-click on the number (click the second value) and bring up the ladder, it will change only that single value. However if you click on the parameter name and operate the ladder, you modify all values of the parameter. 

Tip: You can use the left-mouse button to operate the value ladder, but you must wait a moment before it comes up, so it's faster if you middle-click on the parameter name or value. 

#### 11\. Operator Flags and Table Mode

[Operator Flags](<./Flag.md> "Flag") surround each node. The flags on the left are common to most operator families, and the ones at the bottom are more specific to a family. 

Let's look at`tile1`. We have seen the Viewer flag at the top left, and Viewer Active at the bottom right. 

The third flag on the left is Bypass, which shuts the operator down, and if there is any input connected, it will pass-through the first input directly to the output. 

The fourth flag is the Lock flag, which freezes the data in memory, and prevents new data from flowing through. Modify`level1`'s parameters and see that it doesn't affect`tile1`or beyond. The Lock flag is good for testing, but use it sparingly as it makes your project files larger. Middle-click on the Tile TOP see the GPU memory it consumes. 

Let's switch to "Table Mode". Press Shift-T. It displays one node per row. This is useful to find nodes alphabetically in large networks, and to look over the flags settings. 

Right-click on the second column to bring up parameters. Click or Ctrl-click or Shift-click in the first column to change the current and selected nodes. For now, click`moviefilein1`. 

Now press Shift-T again to get back to the network view and see`moviefilein1`is the current node. Now unlock`tile1`. 

#### 12\. Save your work

Frequently save the state of your work. Under the File menu, choose [Create Project Folder](<./New_Project_Dialog.md> "New Project Dialog"). Make sure your Path is your Desktop. Change the Project Folder to`Learning`, then press Create. 

Explorer or Finder will show you it created a folder on your desktop called`Learning`containing a bunch of folders for your media, plus two identical TouchDesigner Environment files called`Learning.1.toe`and`Learning.toe`. 

The next time you want to save, just choose File -> 'Save' which increments the file name. Bringing Explorer or Finder back shows that it created a`Backup`folder in your project, with`Learning.1.toe`moved into it, and it created a new`Learning.toe`which is now a copy of`Learning.2.toe`. 

To save again, you can also use Ctrl+s (Command+s on macOS), which you can confirm at the top of the window. 

After you quit TouchDesigner, the next time you re-start, you can go to the Learning folder and double-click`Learning.toe`, which is always the latest file. 

Or you can right-click and drag`Learning.toe`to the desktop and create a shortcut that you can always start from. 

Let's delete everything in our project. Type Ctrl-a to select all, and press your Delete key. 

#### 13\. Get Media into TouchDesigner

You can bring in common file types into TouchDesigner including movie, image, audio, FBX, point cloud, JSON files and more. It also imports TouchDesigner`.tox`component files. See the wiki page [File Types](<./File_Types.md> "File Types"). 

On the top menu bar under Dialogs, select Explorer on Windows, or Finder on macOS. 

Go to any media folder you have and Drag-drop some of your media files from the file browser into the Network Editor. (If you don't have anything on your computer, navigate to somewhere like`C:\Program Files\Derivative\TouchDesigner.2022.29040\Samples\Map`.) 

You can also get files from the desktop and drag-drop them in. 

Another way to get files in is to create appropriate operators with the OP Create menu, like the Movie File In TOP, the Audio File In CHOP, the Point File In TOP, or the FBX Component. Then set their File parameter to your desired media file. 

Alternately, on the desktop or in a folder in Windows/macOS, right-click any of these file, and select Open with..., and choose TouchDesigner. This will start a new TouchDesigner session (a new process) with that file as a node. 

Finally, within TouchDesigner, start a project (1) via the File -> Open menu or (2) the Open Recent menu. This will first terminate the process you are in and then start a new process. 

Note that the`.toe`"TouchDesigner Environment" files that contain your entire projects are not imported, they simply are started afresh by (1) double-clicking the file, or (2) doing a right-click -> Open With.... 

#### 14\. Navigate into Components that contain Networks

Components are unique in that every component contains a [Network](<./Network.md> "Network"), and every network lives in a component. 

Bring up OP Create (Tab) and create a Button component,`button1`. Note that all [Components](<./Component.md> "Component") have a grey border. 

To go into`button1`, select it and press Enter or the key "i". The path at the top of the pane`/project1/button1`tells you where you are. 

To get out of a component, press "u" for up. 

You can also double-click a component to get in, as long as its Viewer Active is off (and it's not private). 

A slicker way is to use the mouse's roller wheel to zoom close to a component, so when you mouse-wheel very close to`button1`, you will go inside it. Roll the opposite way to get out. 

#### 15\. Parameters Types

An Operator computes and generates its outputs based on its inputs and its parameters (and often the current time). So let's look at the characteristics of parameters. 

Create a Circle TOP and switch it to another color, then a Trigger CHOP, and below them a Text Component. 

Here are the 7 most common parameter types: 
1. integers (`text1`\- Layout page - Width parameter)
  2. floating point numbers (numbers with decimal places) (Font page - Font Size parameter)
  3. on-off "toggles" (Italic parameter)
  4. menus (Font menu)
  5. text strings (Text page - Text parameter)
  6. a parameter is the path to another node (Look page on text1 - drag the`circle1`TOP to the Background TOP parameter)
  7. pulses that tell the operator to do something just once (the Trigger CHOP \- click the Trigger CHOP pulse parameter)


Each parameter set can have one, two, three or four values. For example, when a parameter is a color, it has 3 or 4 values: red, green, blue and sometimes alpha. (`text1`Look page - Background Color) 

#### 16\. The Four "Parameter Modes"

Each parameter can be in one of four "Parameter Modes", which determines how it gets its value. Click on any parameter like Horiz Stretch to open it up to see what mode it's in. The four boxes represent the four parameter modes. 
* This is in the first Parameter Mode, "Constant" which is the simplest - On the parameter dialog you just click on a slider, type in a number, pick something by hand from a menu - it sets its "constant" value. (where the values are in in white)
  * The second Parameter Mode is "Export Mode", where the parameter is driven by numbers coming from CHOPs. (indicated in green)
  * The third Parameter Mode is "Expression Mode" where you can put python expressions (indicated in cyan).
  * The fourth Parameter Mode is "Binding Mode" (in purple) where two or more parameters are tied together. (right-click on circle1 and select Parameters) The Text COMP's Tracking parameter is in purple, indicating it is bound to another parameter, which you can see is`circle1`'s Border Width, which changes Text COMP's Tracking parameter, and it's bi-directional.


Let's look closer at exporting. For that we need to know more about CHOPs, channels and samples. 

#### 17\. CHOPs output Channels of Samples

CHOPs output numbers. A Channel Operator creates a set of 1 or more channels, and each Channel is a set of numbers ([Sample](<./Sample.md> "Sample")). Let's create a [Constant CHOP](<./Constant_CHOP.md> "Constant CHOP") and move its slider. It has 1 channel and 1 sample, as you can see if you middle-click (or click "i" at the top of the parameter dialog) on the node and see`1i`, where`i`means sample or index. 

Click the + under`chan1`to create new parameters which generates a second channel. Vertify that in the "info popup". 

Now create a [Noise CHOP](<./Noise_CHOP.md> "Noise CHOP"). This is one [Channel](<./Channel.md> "Channel") with multiple samples. To prove this, zoom in to the node a bit, turn on Viewer Active, right-click on the graph and select Dot per Sample. Now middle-click and drag the mouse right to reveal a dot for every sample. (Be aware that mouse clicks on the node do different things depending on whether the viewer is active or not.) 

Press 'h' over the Noise CHOP's graph to home the channel. On the parameter dialog, click the Channel page and change the Channel Names parameter to`chan[1-3]`. There are now 3 channels, each with 600 samples. To verify this, middle-click on the bottom strip of the node where then name`noise1`is located, look at the pop-up info and see 600i meaning 600 samples or indexes. 

To see CHOPs as numbers, bring up OP Create, click on DAT, and create a "CHOP to" DAT. Then turn on the parameter called "Include Names". Now connect the Noise CHOP to the CHOP to DAT by dragging a node to the CHOP to DAT and to the parameter called "CHOP". Look at the table in the viewer, where each cell is a sample. Now try the Constant CHOP You can drag Constant onto CHOP to. 

Overall, a CHOP is used to represent a curve, a motion, an audio signal or a control signal in TouchDesigner. (See: [Channel](<./Channel.md> "Channel"), [CHOP](<./CHOP.md> "CHOP")). 

#### 18\. Export CHOP Channels to Parameters

[Export](<./Export.md> "Export") sends a value from a CHOP channel to an operator's parameter. 

Create an [LFO CHOP](<./LFO_CHOP.md> "LFO CHOP"), slow it down, and connect it to a new Math CHOP. Turn on the Math CHOP's [Viewer Active](<./Viewer_Active.md> "Viewer Active") flag on the bottom right. Create a [Movie File In TOP](<./Movie_File_In_TOP.md> "Movie File In TOP"), then and add a new [Transform TOP](<./Transform_TOP.md> "Transform TOP"). 

Click the Transform TOP so you can export to its parameters. Left-click and hold down the channel in the Math CHOP's viewer and drag it to a parameter in the [Parameter Dialog](<./Parameter_Dialog.md> "Parameter Dialog"): the Transform TOP's Translate parameter over the first number, the X value, and release the mouse button. Select 'Export CHOP' from the menu that appears to complete the export. Note the parameter goes green, indicating the parameter is in Export mode. 

Select the Math CHOP again (box-pick it or click the name-bar at bottom), and then adjust the motion range by selecting the Mult-Add page and adjusting the Multiply parameter. 

You can turn off the export: On the Math CHOP, turn off Viewer Active and click the green dot at the bottom of the CHOP: the Transform TOP's Translate goes back to its constant mode. Now turn on the export again. (See [Export](<./Export.md> "Export") for more techniques). 

#### 19\. Put a Python Expression in a Parameter

Let's look at python expressions in parameters. Expressions are used in parameters and scripts. 

Create a new Pattern CHOP and call it`sine1`. In the Length parameter, type the expression`200*3`. The value now shows as`600`= the expression has been evaluated to`600`, and it is now blue to indicate that it is currently in Expression Mode. To reveal more, put your cursor over the parameter name "Length", a + appears, and click anywhere in that area. A new row appears showing the python name of the parameter ('`length`'), boxes for the four parameter modes, and the optional python expression. 

Click the grey box to the left of the blue box. This puts it back into Constant Mode, where the value is at its default value of 1000. This is useful for trying out different values before committing to it. Click the Expression Mode box again. 

On`sine1`, in the parameter called Number of Cycles type the expression`me.digits+2`. It evaluates to`3`which is the digits in the operator's name plus 2. Select just the text`me.digits`and put your cursor over the expression. It will pop up with`1`, the value of that part of the expression that you have selected. 

To enlarge the Parameter dialog to get more space: Put your cursor over the left edge of the parameter dialog and get the left-right arrow cursor, click and drag it to the left. 

If you press Ctrl-e with the cursor in a parameter it brings up the current parameter’s expression in your text editor, making it easier to see and edit long expressions. Alternately, right-click on the parameter and select Edit Expression. 

Look at this table for the most common Python expressions in TouchDesigner: [Python Tips](<./Python_Tips.md> "Python Tips"). Many examples are in Help -> Python Examples. See also [Parameter](<./Parameter.md> "Parameter"). 

#### 20\. Parameter Mode: Binding

Parameter "Binding" means making 2 or more parameters take on the same value. To set this up, create two Pattern CHOPs, then right-click on`pattern1`and select Parameters... to bring up its Parameters in a floating window, Then select`pattern2`to see its parameters. Then click-drag the Number of Cycles parameter on`pattern1`to the same on`pattern2`and select Bind. Change the value on either parameter and you will see it change in the other. 

Note that the actual value being shared is on`pattern1`\- Expand the parameter on both OPs (press the + on the parameter of both OPs) and see that`pattern2`'s Bind expression in purple is`op('pattern1').par.numcycles`, so it is inheriting the value on`pattern1`. Thus`pattern1`'s parameter is called the "master", and`pattern2`'s parameter is called the "reference". You can have several parameters bind to the master. 

#### 21\. Components Contain Networks of Operators with Inputs and Outputs

"Components" is the operator family that holds networks of operators inside them. Let's create a Component with a wired input and output. Press Tab, select COMP, select Container and place it in your network. Go into the Container (roller-wheel forward, or press Enter). Verify your path location in the top of the pane - it should say something like`/project1/container1`. 

Press Tab, select TOP, select Ramp and place it. Right-click on the ramp node's output and select an Out TOP. Press Tab, select CHOP, select the In CHOP. Go back outside the component (press`u`or roller-wheel backward) and create an LFO CHOP by right-clicking on the component's input. This connects the new LFO CHOP to the input of the component. Set its Type parameter to Ramp. 

Go back into the component and [Export](<./Export.md> "Export") the In CHOP channel to the Phase parameter of the Ramp TOP. You should see the ramp shifting. Go back outside the component. On the container's Panel page, in the Background TOP parameter, put`./out1`. You should see the rising ramp in the viewer. Right-click on the output of the container and add a Null TOP. You have now created a custom component with a CHOP input and a TOP output. 

#### 22\. Containers Hold User Interfaces

Go back into`container1`. Change the Type of the Ramp TOP to Circular. Next create a Slider COMP. Add a Null CHOP to the output of the slider, and export its channel to the Period parameter of the Ramp TOP. Go back up a level, turn on the Viewer Active flag of`container1`and operate the slider to vary the width of the rings. This is the basis of creating user interfaces in TouchDesigner. 

#### 23\. Components can have Custom Parameters

On`container1`, turn Viewer Active off. Right-click on`container1`and select Customize Component... from the node menu. In the Par Name field, type Position. Click Add Par. You should see a new tab called Custom on the parameter dialog, and a new parameter there called Position. Now on Customize Component, change the Range Min setting to -1 and leave Range Max at 1. 

Go inside`container1`and on the Ramp TOP, click on the Position parameter name to bring up the extra rows of settings for the parameter, and on the`position1`row, type`parent().par.Position`. This should now be fetching the custom parameter we just created. Go back up one level, and operate the Position custom parameter. You should see the circular ramp shift left-right. This is the basis of creating custom parameters in TouchDesigner. 

#### 24\. A Path is an address of a Node

A Path is like an address of a node or operator - it describes where a node is located in your TouchDesigner project. The path of network that you are currently in is shown on the path navigator at the top-left of a pane. You have been working in`/project1`mostly. 

Many operators have a path parameter that refers to another operator. Create a Select CHOP and type in the Operator parameter`/project1/pattern1`. You should see`pattern1`'s channels. 

Nodes are all in a tree-like hierarchy of components inside components, starting at root, which is named`/`. Click the "home" icon to go to root. Click the '`/`' and select`project1`to go back to your working network. 

Look at the Select CHOP:`/`at the start of a path means it's an "absolute path".`/project1/pattern1`is an absolute path, where in root (`/`) there is a component`project1`, and in`/project1`is a node`pattern1`. 

Here are other forms of a path: 

Create a Select TOP and put in its TOP parameter`transform1`.`transform1`is a relative path: when you see an operator name without a prefix, this will be in the current network. 

Create an Info CHOP and put in its Operator parameter`container1/out1`. This is also a relative path -`container1`is a component in the current network, and`out1`is a node in`container1`. 

Your`container1`component has`./out1`for the background image.`./`means "inside this component", so the path means "inside this component is a node called`out1`". 

Go into`container1`and create a Select DAT and put in its first parameter`../pattern1`.`../`means the parent network, so the path means, in the parent of the current component there is a node called`pattern1`. 

In python expressions you will often see`parent()`, which also refers to the parent node. To locate further up the hierarchy,`../../`is the parent's parent. You will see other ways to locate operators in parent nodes using python function`parent()`. 

#### 25\. Split Panes and fill with other Pane Types

Sometimes you want to be in two places at once. The TouchDesigner window can be split into 2 or more [Panes](<./Pane.md> "Pane"). Split a pane via the pull-down menu at the top-right corner of a pane, selecting Split Left-Right. 

Panes get filled with a choice of pane types via a pane's top-left corner menu. The Network Editor pane type is what you have been working in so far. The pane type "Panel" lets you interact with panel components. Pane type [Geometry Viewer](<./Geometry_Viewer.md> "Geometry Viewer") lets you interact with 3D scenes and objects. right-click -> Viewer on nodes give similar views in floating windows. 

Adjust the panes' sizes with the dividing bar between the panes, then close the pane via the pull-down menu at the top-right corner of a pane. You can also click the Layout or Bookmark icons at the top of a pane to select a multi-pane layout. See [Pane](<./Pane.md> "Pane") for more. 

#### 26\. Render a 3D Scene with a Render TOP

Now let's render something in 3D with the Render TOP. Create a Container component in`/project1`, rename it to`scene`and go into it. Create a Render TOP. Next create three components: a Geometry, a Light and a Camera. The dashed lines mean that parameters of the Render TOP already refer to these components. In the Render TOP's Camera parameter, you see`cam1`, which means "get your camera from the node`cam1`". In the Geometry parameter, the`*`in`geo*`means "get all Geometry components in this network whose name starts with`geo`". 

Go to the parameters of the`geo1`Geometry node and Rotate the torus in Z (the third field of Rotate) to 30 degrees. The Render TOP changes. Now click the [Viewer Active](<./Viewer_Active.md> "Viewer Active") flag of`geo1`and click/move the torus to tumble it. Note the render stays the same. The tumbling in the Geometry component viewer is for inspection only. Press`h`in the`geo1`viewer to home (reset the tumble). 

Now go back up to`/project1`. Put`absTime.seconds * 20`in the first field of the Rotate parameter (X).`absTime.seconds`is python for the "absolute time in seconds", which is a number that continues to rise by 1 every second until you quit TouchDesigner. Affecting parameters affects the render. This is your basic render setup. (`absTime.frame`increases by 1 each frame, so speed depends on your timeline frames per second) 

#### 27\. Timeline lets you Play, Pause and Examine

The [Timeline](<./Timeline.md> "Timeline") is located along the bottom of the main TouchDesigner window. The FPS at the bottom left is the number of frames TouchDesigner will step forward every second. Note that the FPS at the top of the UI is the actual number of frames TouchDesigner drew in the last second, which will be the FPS or less. 

The timeline lets you pause (||), play (>) and single-step (+) the timeline in TouchDesigner. 

Spacebar will always stop and start the timeline. Every time it steps to another frame, it redraws the screen. 

The power button at the top (0|1) shuts off all computing, clocks and communication in the TouchDesigner process, and is useful for inspecting things in a frozen state. 

You will see when the timeline reaches the far right, it loops to the beginning of the timeline. But TouchDesigner is mostly event-driven with a free-running clock, so most things you build don't follow the looping timeline and its frame number: For example, create a Constant CHOP, set it to 1 and connect it to a Speed CHOP. It increases its count continuously and does not relate to the timeline. The [Speed CHOP](<./Speed_CHOP.md> "Speed CHOP") restarts when you press its Reset parameter. 

Create a Movie File In TOP and on the File parameter select + and select`Count.mov`. Movie File In TOP plays in its default Sequential Play Mode continuously regardless of the timeline position, which you can see if you reduce the Speed parameter. 

However if you set its Play Mode menu parameter to "Locked to Timeline", the frame number of the movie and Timeline will stay in sync where the first frame of the movie will be seen at frame 1 always, and you can scrub the timeline. 

But most often, the movie is played using a CHOP channel. Create a Constant CHOP, change the Movie File In's Play Mode menu to Specify Index, and export the Constant CHOP channel to the Index parameter. Now use the value ladder on the Constant CHOP's value parameter to raise and lower the movie's frame number. 

#### 28\. Create Animation Curves with the Animation Editor

Create an [Animation Component](<./Animation_COMP.md> "Animation COMP"). By default it outputs a CHOP with no channels. Now right-click on the node and select Edit Animation... (or press Edit Animation... in its parameter dialog). 

Click Add Channels button and 3 channels will be created,`tx`,`ty`, and`tz`. Keyframes are the dots on the channels. Click on any keyframe and move it anywhere. To add additional keyframes to any channel, use alt+LMB and click on the location you want the keyframe. Use the right-mouse-button to box-select. Box-select the curve (not the keyframe dot), and change the Function menu from`cubic()`to`linear()`to change interpolation type. 

Then watch the [Timeline](<./Timeline.md> "Timeline") at the bottom and the values of the channel in the Animation component viewer. Note the channel values follow the timeline. 

If you want more control of the timing, connect an animated channel to the Animation component's input: Create a [Beat CHOP](<./Beat_CHOP.md> "Beat CHOP") and wire it to Animation COMP's input. Set the Animation COMP's **Play Mode** to "Use Input Index" and the **Input Index Unit** parameter menu to "Fraction". 

Then create a [Constant CHOP](<./Constant_CHOP.md> "Constant CHOP"), wire it to the Animation COMP first input and move the Constant's`chan1`slider. In both cases, the 0-1 value will control which part of the animation curve is output, de-coupling the Animation COMP from the timeline. You can always change Play Mode to Output Full Range to output the full-length channels. 

Another way to create an animation component pre-wired is to right-click on a parameter and select Keyframe Parameter in... 

#### 29\. DAT Operators manipulate Text

[DATs](<./DAT.md> "DAT") are "Data Operators" that allow you to store and manipulate text in your TouchDesigner networks. Text DATs are used to write scripts, shaders and any free-form text. 

Create a Web DAT and assuming you are on the Internet, press the Fetch parameter. This retrieves HTML from a website. 

Now create a Monitors DAT which a table of rows and columns of cells, each containing text. Attached to the Monitors DAT is another DAT containing some Python code that runs when you monitor configuration changes. You can see a dashed line between the two, which indicates it is "docked" to the Monitors DAT. 

This is a bit of a taste of DATs. 

#### 30\. Sweet Sixteen Operators

There are a lot of OP types in TouchDesigner, but the most common and useful operators in each family are the Sweet Sixteens. You may want to try some of them out. This includes: 
* [Sweet Sixteen CHOPs](<./CHOP.htm#Sweet_16_CHOPs> "CHOP")
  * [Sweet Sixteen TOPs](<./TOP.htm#Sweet_16_TOPs> "TOP")
  * [Sweet Sixteen SOPs](<./SOP.htm#Sweet_16_SOPs> "SOP")
  * [Sweet Sixteen DATs](<./DAT.htm#Sweet_16_DATs> "DAT")


These are in the wiki, which you can get to from the WIKI button in the UI. 

#### 31\. Explore the Operator Snippets

One way to learn more about operators is to see them in small examples. Select the menu Help -> [Operator Snippets](<./OP_Snippets.md> "OP Snippets"). This will start another TouchDesigner window that contains hundreds of examples using operators from each family. This is a rich resource of tips. 

#### 32\. Get Components from the Palette

Components from the Palette Browser contain pre-made networks, and some have a custom control panel. You can also store Components you create in the Palette for easy access and reuse them elsewhere your projects. 

To display a browser of pre-made [Components](<./Component.md> "Component"), toggle off/on the Palette icon. Alternately, click Dialogs -> Palette Browser. Click on a component and drag it to the network. Components on disk are`.tox`files. 

Watch the video [A Movie Player Panel and Building UIs](<http://www.derivative.ca/Events/2016/NorwayWorkshop/>), a tutorial on the basics of panel building. 

#### 33\. Get Components from the Community Posts

Go to [www.derivative.ca](<http://www.derivative.ca>), the TOUCHDESIGNER tab, the COMMUNITY POSTS tab, and filter by Assets: [[](<https://derivative.ca/community?sort_by=created&type>)=24 Community Assets]. 

You can download any`.tox`file to your computer and then drag-drop it into TouchDesigner. Double-clicking any`.tox`starts it in a new TouchDesigner process as well. 

Alternately Press [ [FORUM](<http://www.derivative.ca/Forum/viewforum.php?f=22>) ] on the TouchDesigner menu bar to go to Shared .tox Components. 

#### 34\. Perform Mode runs your Application Solo and Optimized

Press the F1 function key. See the container panel of`/project1`in a floating window. TouchDesigner is in [Perform Mode](<./Perform_Mode.md> "Perform Mode") which runs it without the network editor. Then press Esc to go back to [Designer Mode](<./Designer_Mode.md> "Designer Mode"). 

TouchPlayer runs your application in Perform Mode only. 

#### 35\. Speeding it up with the Performance Monitor

Dialogs -> [Performance Monitor](<./Performance_Monitor.md> "Performance Monitor") will let you see, in one frame, what nodes cook, in what order, and how long they took. Now be aware, Performance Monitor only shows what cooks on the CPU, not the GPU. But a long bar at the bottom usually means the GPU is still busy finishing rendering a frame and displaying the UI. 

middle-click on any node to see if the node is cooking every frame or not, and how long it took the most recent time it cooked. 

There is also the Perform CHOP, and you can create Info CHOP and drag any node onto it to see more detail on what happened. 

Another tool called "probe" lets you see GPU and CPU cooking and memory usage. Get`probe`from the Palette -> Tools -> probe, and see its wiki page: [Palette:probe](<./Palette-probe.md> "Palette:probe"). 

#### 36\. Quick Tips and Good Habits
* Click on the **bulls-eye** circles in a parameter dialog to see which parameters are non-default. This is very useful for understanding other people's networks.
  * To get quick help for a parameter, hold down Alt and move your cursor over a parameter. You will get the parameter's help info that is in the wiki.
  * **Color Code Nodes** \- With your cursor over the network, press "c" to bring up the color swatch. Select some nodes. Click any color in the color swatch. This only affects the node's appearance in the network.
  * **Network Overview** \- With your cursor over the network, press "o" to bring up the a miniature node map at the bottom left of the network. You can click on it to pan the network.
  * To look at nodes another way, with your cursor over the network, press "Shift-T" in the network and it will switch to **"table" mode** where you see all the nodes in a list. You can pick one via the left column, and then press "Shift-T" again to go back to the network and see that node highlighted in the network.
  * Ctrl+f (Command+f on macOS) will bring up a **Find bar** that will let you type node names that you may be looking for. Names that match what you type are highlighted and centered. Use **Edit - > Search/Replace** to generate a list of operators in your whole project that match search criteria and optionally modify them.
  * When you **don't have a mouse** , zoom and scroll the network editor by pressing the keyboard shortcuts Ctrl+=, Ctrl+-, Ctrl+up, Ctrl+down, Ctrl+left, Ctrl+right (all with Command+ on macOS).
  * In OP Create, you can **create nodes-in-a-row** faster by using Shift-click to select a sequence of nodes. Use Ctrl-click on the OP Create menu to create a node in a new independent row.
  * To connect multiple operators at once to a **multi-input OP** like a [Composite TOP](<./Composite_TOP.md> "Composite TOP") or [Switch CHOP](<./Switch_CHOP.md> "Switch CHOP"), box-pick the inputs, and connect one of their outputs to the multi-input OP's input connector. They all get wired in.
  * Node names are **case-sensitive** , so`level2`is different from`Level2`.
  * The idea of "**Absolute Time** " is a clock that counts up forever and doesn't loop to 0 like the timeline. This gives smooth always-changing values when using python:`absTime.seconds`,`absTime.frame`. Try code>absTime.seconds in a [Transform TOP](<./Transform_TOP.md> "Transform TOP") Rotate parameter.
  * Use **Null operators** when referencing or exporting - you can then insert additional operators before the Null to modify your network without having to change your reference or export location
  * use the **Info DAT or Info CHOP** on a node to see some of its internal states and possibly help troubleshooting.
  * You can turn on/off **Adaptive Homing in SOP viewers** and Geometry viewers - in the right-click menu on SOP Or Geometry viewers in Viewer Active mode. In Preferences -> Geometry turn the options on and then Accept, which makes sure you always see your 3D geometry in-view.
  * **replace an existing wire** by clicking on the output of the new source and clicking on the wire you want to replace.
  * Add **[comments and annotations](<./Network_Utilities-_Comments,_Network_Boxes,_Annotates.md> "Network Utilities: Comments, Network Boxes, Annotates")** in networks using Alt-right-click and drag to set an annotate box, or use the "a", "b" or "c" shortcuts. Comments are more concise annotates.
  * The preferred scripting language is Python, though you may see Tscript in older work, and a T in the parameter dialog where you would normally see the python icon.
  * The **Status Bar** is located at the top right of TouchDesigner's main window and provides information about recent operations. It may display a message to indicate success/failure of events, or display a hint to tell you how to use a tool. Keep an eye on it. (The [python code](<./UI_Class.md> "UI Class")`ui.status = 'My message'`can be used to place a line in the status bar.)

#### More...

Now you know the basics. Take a break. Later you can go to **[More Things to Know about TouchDesigner](<./More_Things_to_Know_about_TouchDesigner.md> "More Things to Know about TouchDesigner")**
