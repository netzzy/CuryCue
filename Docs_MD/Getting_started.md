# Getting started

These are the basics to help you become skilled in working with the TouchDesigner interface. This will take you about 1-2 hours if you work through it sequentially. Afterwards you will hopefully be more proficient and comfortable with exploring TouchDesigner on your own. 

This page is the transcript for the two beginner videos: 

**[First Things to Know Part 1](<./First_Things_to_Know_Part_1_Vid.md> "First Things to Know Part 1 Vid")** \- Section 1-17 

**[First Things to Know Part 2](<./First_Things_to_Know_Part_2_Vid.md> "First Things to Know Part 2 Vid")** \- Section 18-33 

**TIP** : If the meaning of a term in TouchDesigner is unclear, you can look it up in the **[TouchDesigner Glossary](<./TouchDesigner_Glossary.md> "TouchDesigner Glossary")** or **Search** for it, both found in the menus to the left.   

#### 1\. Starting TouchDesigner

To use TouchDesigner, you will need a 3-button mouse with a roller wheel, or the equivalent. 

Start by double-clicking the TouchDesigner icon on the desktop (or begin via the Windows Start menu). 

#### 2\. Pan, zoom and center the Network

You see the [network](<./Network.md> "Network") editor on the right when you first start TouchDesigner. The palette browser is on the left. Close the palette by clicking the x at its upper right corner. 

To pan the network, click and drag the left mouse button ([LMB](<./Mouse_Click.md> "Mouse Click")) on an empty area of the network. 

To zoom the network, click and hold down the middle mouse button ([MMB](<./Mouse_Click.md> "Mouse Click")) and drag it left-and-right. **NOTE: If you don't have a middle mouse button** , press Alt+Right-click. 

Press the "h" key to center it (this is also called **h** oming). To home just the highlighted node, press Shift-h. 

In an empty area of the network right-click ([RMB](<./Mouse_Click.md> "Mouse Click")) and release the mouse - you will see the network menu. Choose 'Home All'. 

#### 3\. Select and move Nodes

Left-click on a node and drag it to a new location. 

To box-select several nodes, click and hold down the right mouse button in an empty area and drag the mouse over the nodes. 

Left-click on any selected node and drag it - the selected nodes move together. 

Left-click on the background to un-select the nodes except for the current node in green. 

Right-click on one of the nodes - you will see the node menu. Choose 'View' to bring up a floating window. Resize it by clicking-and-dragging the edges. Now you can close the viewer window by clicking it in the corner. 

#### 4\. TouchDesigner Operators are Generators or Filters

To delete all the nodes, press Control-a, then press Delete. 

Double-click on the empty network. The [OP Create Dialog](<./OP_Create_Dialog.md> "OP Create Dialog") appears, where OP means "operator" or "node". Click on Movie File In, then click anywhere on the network to place it. 

You can also press Tab. To cancel, click the background. 

On the right side of the first node, right-click on its blue output connector, from OP Create click 'Level' and then click to the right to create`level1`, which will be connected to`moviefilein1`. You have just added an image "filter" (`level1`) that modifies the levels of an image "generator" (`moviefilein1`). 

On the top-right dialog, move the sliders labeled Black Level and Brightness. These are typical "parameters" in TouchDesigner. 

#### 5\. In the Network Editor, add an Operator

Once again, double-click on the background. The [OP Create Dialog](<./OP_Create_Dialog.md> "OP Create Dialog") has six headings of what we call [Operator Families](<./Operator.md> "Operator"). Click on 'CHOP' for 'Channel Operators'. Also you can press Tab several times to cycle back to CHOPs. 

Darker-colored OPs are generators. Generators create new data or read data from external devices and programs. Lighter colored OPs are filters. Filters modify the data of an incoming operator. 

Click on the CHOP type "Pattern" and place it in the network. 

Bring up OP Create again. You can find a specific operator by typing its name. Type "noi", click on Noise, and create a [Noise CHOP](<./Noise_CHOP.md> "Noise CHOP"). 

#### 6\. Six Families of Operators act on images, motion, 3D and text

Let's look at the six families of operators. As you likely know already Texture Operators ([TOP](<./TOP.md> "TOP")) work with images, and Channel Operators ([CHOPs](<./CHOP.md> "CHOP")) are for motion, control signals and audio. 

Press the Tab key to bring up OP Create. At the top right, make sure it is set to "All" versus "Basic" to see all the operators. 

Click SOP. Surface Operators ([SOPs](<./SOP.md> "SOP")) work with polygons, 3D lines and other surfaces. Choose a [Sphere SOP](<./Sphere_SOP.md> "Sphere SOP"). 

Press the Tab key and select MAT. Material Operators ([MATs](<./MAT.md> "MAT")) add textures and shading to 3D objects. Choose a [Phong MAT](<./Phong_MAT.md> "Phong MAT"). 

Press the Tab key and select COMP. There are three categories of components. From 3D Objects choose a [Geometry COMP](<./Geometry_COMP.md> "Geometry COMP") which prepares SOPs and a Material for 3D rendering. 

Press the Tab key again. From the Panels list, choose a [Slider COMP](<./Slider_COMP.md> "Slider COMP"), which one of the 2D gadgets for building control panels. 

Press the Tab key and select DAT. Data Operators ([DATs](<./DAT.md> "DAT")) manipulate text strings, both free-form text and in tables. Choose a [Monitors DAT](<./Monitors_DAT.md> "Monitors DAT"). 

If you want, you can go back to Basic while you are first learning TouchDesigner. 

#### 7\. Connect Nodes together with Wires

Node inputs are found on their left side, and outputs are on their right. Press Tab and create a TOP called Monochrome, and place it to the right of`level1`. 

Connect the output of`level1`to the input of`mono1`in one of two ways: Click-and-drag-release. Or click-release, move, click-release. 

Click and drag the Monochrome TOP to the right to create some space between. 

To insert a new node between the two already-connected nodes, right-click the output of the`level1`node and select a Tile TOP and place it. Another way is to right-click on the wire, and select Insert Operator from the menu. 

To create a new branch from a node, middle-click on the output of`level1`and select Edge from the Operator menu and place it above. 

The connecting lines between nodes are called [Wires](<./Wire.md> "Wire"). Remove a wire by clicking on the input of a connected node,`edge1`, and then clicking on empty space in the network. Reconnect`edge1`by clicking on`edge1`'s input and then`level1`'s output. 

Another way is to right-click on a wire and select Disconnect from the menu. Reconnect`edge1`again. 

#### 8\. Wires, Data Flow and Cooking

You can think of data flowing along these wires, in this case, images. Now watch the wires animate. Click on`level1`, go to its [Parameter Dialog](<./Parameter_Dialog.md> "Parameter Dialog") on the right, and operate the Brightness slider. When the wires are animating it means that data is flowing: a node upstream is [cooking](<./Cook.md> "Cook") and sending its output to the next node. 

Middle-click on the tile1 to see how many times it has cooked, and then middle-click on`moviefilein1`and see it has only had to cook once. 

The 3D components like Geometrys, Cameras and Lights have connectors and lines on their bottoms and tops which connects them as parent-child in a [3D](<./3D.md> "3D") hierarchy, but no data flows along them. 

The 2D components like Sliders, Buttons and Containers also have connectors and lines on their bottoms and tops, which is one way to group them in a panel. Again, no data flows along them, data only flows through the wires on the sides. 

#### 9\. Current Node and Selected Nodes

Click on one of the nodes to make it "current". This gives it a green border. 

Yellow borders around nodes mean they are "selected". [right-click (RMB)](<./Mouse_Click.md> "Mouse Click") on the network and box-pick some other nodes to select them. Shift-click, or Shift-box-pick to add more to the set of selected nodes. 

You can act on selected nodes together. Right-click on the network background and select Delete to remove the nodes, then press Ctrl+z to undo (Command+z on macOS). You can also undo via the Edit menu. 

Now click the top-left [Flag](<./Flag.md> "Flag") on any of the selected nodes. This toggles between their [Node Viewers](<./Node_Viewer.md> "Node Viewer") and their 3-letter icons. Turn back on the node viewers. 

To un-select all, click on the background, leaving only the current node. 

#### 10\. Make a Viewer Active to Inspect Operator Data

Up to now, when you left-click on a node, you move it or make it current. You can only see the data in the viewer. Middle-click shows the common info box, and right-click shows the node menu. 

**NOTE:** If you don't have a middle mouse button, press Alt+Right-click. 

Clicking the "[Viewer Active](<./Viewer_Active.md> "Viewer Active")" flag at the bottom right of the`level1`TOP removes its border and allows you inspect more closely the contents of the operator's data, or in the case of panels, let you operate the panel. Middle-click and move left-right to zoom the image, and right-click to set a menu of viewing options. 

There are three more ways to make the viewer interactive: 
* Alt+a key puts all node viewers temporarily in the Viewer Active state.
  * Shift+a toggles a global state called "Viewers Always Active", making all viewers in all networks Active. Viewers Always Active is also on the right-click network menu.
  * The [shortcut](<./Shortcut.md> "Shortcut") key "`a`" will set/unset the Viewer Active flag of all selected nodes.


Even when a node has Viewer Active on, you can still access it's common menus. On the name bar at the bottom, middle click to get the node info, and right click to get the common node menu. 

#### 11\. Adjust Parameters of Operators

Let's adjust parameters. Pick the`noise1`CHOP. Every Operator in TouchDesigner has a set of [Parameters](<./Parameter.md> "Parameter") that allow you to affect its output. Normally the [Parameter Dialog](<./Parameter_Dialog.md> "Parameter Dialog") is open and docked in the upper right corner of a Network. Press the lower-case`p`key to hide the parameter dialog, and`p`again to bring it back. 

To also see`sphere1`'s parameters in a floating window, right-click on`sphere1`and select Parameters.... 

Selecting multiple OPs with the same parameter lets you change the parameter of several OPs at once. Move`noise1`to the left, Click`pattern1`, and press Ctrl+c and Ctrl+v to create`pattern2`(Command+c and Command+v on macOS). Change the Type menu of`pattern2`parameter to Ramp. Now select both`pattern1`and`pattern2`. Increase the parameter Number of Cycles. When you release you see that both OPs' Cycles parameter are set to the same value. 

To set parameters back to their default values, there are three ways: right-click on`pattern1`and select Reset all Parameters, or right-click -> Reset on its parameter dialog's "i" icon. 

To reset just one parameter, right-click on the Type parameter of`pattern2`and select Reset Parameter from the menu. 

#### 12\. Value Ladders help you change Parameter values

Now let's adjust parameters with a value ladder. Pick the`noise1`CHOP and zoom in to its viewer with your mouse wheel. 

On the Parameter Dialog, left-click on the Period parameter's name or value, holding down the button and waiting a moment. The [Value Ladder](<./Value_Ladder.md> "Value Ladder") will pop up a number of increments labeled .001 .01 .1 1 10. With the left-mouse still down, move vertically to one of the increments, then move off to the right/left to increase/decrease the parameter value. 

Click on the parameter dialog's Transform page. If the parameter has two or more numbers like the Translate parameter, when you left-click on the number (click the third number), it will change only that single value. However if you click on the name and operate the ladder, you modify all values of the parameter. 

And here's a speed-tip: You can bring up the value ladder faster if you middle-click on a parameter name or value. 

#### 13\. Navigate into Component Operators that contain Networks

Let's navigate in and out of components to other networks. Nodes with a grey border are [Components](<./Component.md> "Component"). In our network,`geo1`and`slider1`are components. 

Every component contains a [Network](<./Network.md> "Network"), and every network lives in a component. 

To go into`slider1`, select it and press Enter or the key "i". To get out of a component, press "u" for up. You can also double-click a component to get in, as long as its Viewer Active is off. 

A slicker way is to use the mouse's roller wheel to zoom close to a component. When you mouse-wheel very close to`slider1`, you will go inside it. Roll the opposite way to get out. 

#### 14\. Save your work

Frequently save the state of your work. Under the File menu, choose [Create New Project](<./New_Project_Dialog.md> "New Project Dialog"). Change the Project Folder to`Learning`, turn on Rename File so that it creates Learning.toe and press Create. It will show you it created a folder on your desktop called Learning containing two identical files Learning.1.toe and Learning.toe, both TouchDesigner Environment files. 

The next time you want to save, just choose File -> 'Save' to increment the file name and save. You can also use Ctrl+s to save (Command+s on macOS). 

After you quit TouchDesigner, the next time you re-start, you can go to the Learning folder and double-click`Learning.toe`, which always starts the latest numbered file. 

#### 15\. Get Media into TouchDesigner

TouchDesigner [imports](<./Import.md> "Import") popular files types for images, movies, audio, and FBX. It also imports TouchDesigner .tox components. See [File Types](<./File_Types.md> "File Types"). 

Let's create an empty Component. Press Tab, in COMP select Base, and place it. Roller-wheel into base1. 

On the top menu bar, under the Dialogs menu, select the first item (Explore on Windows). 

Go to some media folder and Drag-drop some of your media files from the file browser into the Network Editor. 

You can also get files from the desktop and drop them in. 

Another way is to create appropriate operators with the Tab menu and then set their File parameter to your media file. Look for operators with File In in their names. 

There is also the File -> [Import File ...](<./Import_File_Dialog.md> "Import File Dialog") dialog, where you can see more choices on what files are supported. 

On the desktop or in a folder in Windows, right-click any of these file, and select Open with..., and choose TouchDesigner. This will start a new TouchDesigner session (a new process) with that file as a node. 

NOTE: .toe files are "TouchDesigner Environment" files that contain entire projects. They are not imported, they just started by double-clicking the file (or right-click -> Open With... on the Desktop). 

#### 16\. Split Panes and fill with other Pane Types

Sometimes you want to be in two places at once. The TouchDesigner window can be split into 2 or more [Panes](<./Pane.md> "Pane"). Split a pane via the pull-down menu at the top-right corner of a pane, selecting Split Left-Right. 

Panes get filled with pane types via a pane's top-left corner menu. The Network Editor pane type is what you have been working in so far. The pane type "Panel" lets you interact with panel components. Pane type [Geometry Viewer](<./Geometry_Viewer.md> "Geometry Viewer") lets you interact with 3D scenes and objects. right-click -> Viewer on nodes give similar views in floating windows. 

Adjust its size with the dividing bar, and close the pane. You can also click the Layout or Bookmark icons at the top of a pane to select a multi-pane layout. See [Pane](<./Pane.md> "Pane") for more. 

#### 17\. Operator Flags affect their function and appearance

[Operator Flags](<./Flag.md> "Flag") surround a node in the network. The flags on the left are common to all operator families, and the ones at the bottom are specific to a family. 

To see the complete set of flags, press`t`in the network pane, roll over the headings to see the flag types, and then press`t`again to get back. For more details on individual flags, see: [Bypass Flag](<./Bypass_Flag.md> "Bypass Flag"), [Display Flag](<./Display_Flag.md> "Display Flag"), [Lock](<./Lock_Flag.md> "Lock Flag"), [Render Flag](<./Render_Flag.md> "Render Flag"), [Viewer Flag](<./Viewer_Flag.md> "Viewer Flag"), [Viewer Active](<./Viewer_Active.md> "Viewer Active") flag. 

END OF PART 1 

START OF PART 2 

#### 18\. Parameters and the three "Parameter Modes"

Operators do all the work of processing and outputting data in TouchDesigner. The output of each operator is affected by: its inputs, its parameters, and in some cases the current time. So let's look at the characteristics of parameters. The most common types of parameters are: (1) integers, (2) floating point numbers (numbers with decimal places), (3) on-off "toggles", (4) menus, (5) text strings, and more ((6) the path to another node, (7) pulses that tell the operator to do something just once)). 

Each parameter can have one, two, three or four values. Create a Circle TOP. For example, when a parameter is a color, it has 3 or 4 values: red, green, blue and sometimes alpha. 

So each parameter can be in one of three "Parameter Modes", which means each parameter can be controlled in three ways. First is the simplest - "Constant" - On the parameter dialog you just click on a slider, type in a number, pick something by hand from a menu - it sets its "constant" value. The other two "parameter modes" are super-powerful: "Expression Mode" where you can put python expressions (indicated in green), and thirdly "Export Mode", where the parameter is driven by numbers coming from CHOPs. You can switch between all three. First let's look at exporting. For that we need to know more about CHOPs, channels and samples. 

#### 19\. CHOPs output Channels of Samples

CHOPs output numbers. A Channel Operator creates a set of 1 or more channels, and each Channel is a set of numbers ([Sample](<./Sample.md> "Sample")). Let's create a [Constant CHOP](<./Constant_CHOP.md> "Constant CHOP") and move its slider. It has 1 channel and 1 sample, as you can see if you middle-click on the node and see 1i, where i means sample or index. Click under`chan1`and type`chan2`. It is now outputting 2 channels. 

Now create a [Noise CHOP](<./Noise_CHOP.md> "Noise CHOP"). This is one [Channel](<./Channel.md> "Channel") with multiple samples. To prove this, zoom in to the node a bit, turn on Viewer Active, right-click on the graph and select Dot per Sample. Now middle-click and drag the mouse right to reveal a dot for every sample. (Be aware that mouse clicks on the node do different things depending on whether the viewer is active or not.) 

Press 'h' over the Noise CHOP's graph to home the channel. On the parameter dialog, click the Channel page and change the Channel Names parameter to`chan[1-3]`. There are now 3 channels, each with 600 samples. To verify this, middle-click on the bottom strip of the node where then name`noise1`is located, look at the pop-up info and see 600i meaning 600 samples or indexes. 

To see CHOPs as numbers, bring up OP Create, click on DAT, and create a "CHOP to" DAT. Then turn on the parameter called "Include Names". Now connect the Noise CHOP to the CHOP to DAT by dragging a node to the CHOP to DAT and to the parameter called "CHOP". Look at the table in the viewer, where each cell is a sample. Now try the Constant CHOP You can drag Constant onto CHOP to. 

Overall, a CHOP is used to represent a curve, a motion, an audio signal or a control signal in TouchDesigner. (See: [Channel](<./Channel.md> "Channel"), [CHOP](<./CHOP.md> "CHOP")). 

#### 20\. Export CHOP Channels to Parameters

[Export](<./Export.md> "Export") sends a value from a CHOP channel to an operator's parameter. 

Create an [LFO CHOP](<./LFO_CHOP.md> "LFO CHOP"), slow it down, and connect it to a new Math CHOP. Make the Math CHOP's [Viewer Active](<./Viewer_Active.md> "Viewer Active"). Create a [Movie File In TOP](<./Movie_File_In_TOP.md> "Movie File In TOP"), right-click on its output, and add a new [Transform TOP](<./Transform_TOP.md> "Transform TOP"). 

(Click the Transform TOP so you can export to it.) Left-click the channel in the Math CHOP's viewer and drag it to a parameter in the [Parameter Dialog](<./Parameter_Dialog.md> "Parameter Dialog") (say, the Transform TOP's Translate X parameter). Select 'Export CHOP' from the menu that appears to complete the export. Note the parameter goes green, indicating the parameter is in Export mode. 

Select the Math CHOP again (box-pick it or click the name-bar at bottom), and then adjust the motion range by selecting the Mult-Add page and adjusting the Multiply parameter. 

You can turn off the export by clicking the green dot at the bottom of the CHOP, and the Transform TOP's Translate goes back to its constant mode. Turn on the export again. (See [Export](<./Export.md> "Export") for more techniques). 

#### 21\. Put a Python Expression in a Parameter

Let's look at python expressions in parameters. Expressions are used in parameters and scripts. The preferred language is Python, though you will see Tscript in older work. 

Create a new Pattern CHOP and call it`sine1`. In the Length parameter, type the expression`200*3`. The value now shows as`600`= the expression has been evaluated to`600`, and it is now blue to indicate that it is currently in Expression Mode. To reveal more, put your cursor over the parameter name "Length", a + appears, and click anywhere in that area. A new row appears showing the python name of the parameter ('length'), boxes for the three parameter modes, and the optional python expression. 

Click the grey box to the left of the blue box. This puts it back into Constant Mode, where the value is at its default value of 1000. This is useful for trying out different values before committing to it. Click the Expression Mode box again. 

The third parameter mode is Export Mode, so if you go back to the Transform TOP that holds the export, and click on Translate, you will see`tx`is in Export Mode (green) and you can see where the channel comes from. Here you can switch between Constant, Expression and Export Modes. 

On`sine1`, in the parameter called Number of Cycles type the expression`me.digits+2`. It evaluates to`3`which is the digits in the operator's name plus 2. Select just the text`me.digits`and put your cursor over the expression. It will pop up with`1`, the value of that part of the expression. 

To enlarge the Parameter dialog to get more space: Put your cursor over the left edge of the parameter dialog and get the left-right arrow cursor, click and drag it to the left. 

If you press Alt-E with the cursor in a parameter it brings up the current parameter’s expression in the text editor, making it easier to see and edit long expressions. 

Look at this table for the most common Python expressions in TouchDesigner: [Python Tips](<./Python_Tips.md> "Python Tips"). See also [Parameter](<./Parameter.md> "Parameter"). 

#### 22\. Create a Component with an Input, Output and a Network of Operators

Components is the operator family that holds inside them networks of operators. Let's create a Component with an input and output operator. Press Tab, select COMP, select Container and place it in your network. Go into the Container (roller-wheel forward, or press Enter). Verify your path location in the top of the pane. 

Press Tab, select TOP, select Ramp and place it. Right-click on the ramp node's output and select an Out TOP. Press Tab, select CHOP, select the In CHOP. Go back outside the component (press`u`or roller-wheel backward) and create a Beat CHOP by right-clicking on the component's input. This connects the new Beat CHOP to the input of the component. 

Go back into the component and [export](<./Export.md> "Export") the In CHOP channel to the Phase parameter of the Ramp TOP. Go back outside the component. On the container's Panel page, in the Background TOP parameter, put`./out1`. You should see a rising ramp. right-click on the output of the container and add a Null TOP. You have now created a custom component with a CHOP input and a TOP output. 

(Go back out of this component.) 

#### 23\. A Path is an address of a Node

A Path is like an address of a node or operator - it describes where a node is located in your TouchDesigner project. Create a Select CHOP and type in the Operator parameter`/project1/pattern1`. Many operators have a path parameter that refers to another operator. 

Nodes are all in a tree-like hierarchy of components inside components, starting at root, which is named`/`. Click the "home" icon to go to root. Click the '`/`' and select`project1`to go back to your working network. Look at the Select CHOP:`/`at the start of a path means it's an absolute path.`/project1/pattern1`is an absolute path, where in root (`/`) there is a component`project1`, and in`/project1`is a node`pattern1`. 

Here are other forms of a path: 

Create a Select TOP and put in its TOP parameter`transform1`.`transform1`is a relative path: when you see an operator name without a prefix, this will be in the current network. 

Create an Info CHOP and put in its Operator parameter`container1/out1`. This is also a relative path -`container1`is a component in the current network, and`out1`is a node in`container1`. 

Your`container1`component has`./out1`for the background image.`./`means "inside this component", so the path means "inside this component is a node called`out1`". 

Go into`container1`and create a Select DAT and put in its first parameter`../chopto1`.`../`means the parent network, so the path means, in the parent of the current component there is a node called`chopto1`. 

In python expressions you will often see`parent()`, which also refers to the parent node. To locate further up the hierarchy,`../../`is the parent's parent. 

#### 24\. Render a 3D Scene with a Render TOP

Now let's render something in 3D with the Render TOP. Create a Container component and go into it. Create a Render TOP. Next create three components: a Geometry, a Light and a Camera. The dashed lines mean that parameters of the Render TOP already refer to these components. In the Render TOP's Camera parameter, you see`cam1`, which means "get your camera from the node`cam1`".`*`for Geometry means get all Geometry components in this network. 

Go to the parameters of the`geo1`Geometry node and Rotate the torus in Z (the third field of Rotate). The Render TOP changes. Now click the [Viewer Active](<./Viewer_Active.md> "Viewer Active") flag of`geo1`and click/move the torus to tumble it. Note the render stays the same. The tumbling in the Geometry component viewer is for inspection only. Press`h`in the`geo1`viewer to home (reset the tumble). 

That is your basic render setup. Now put`absTime.frame`in the first field of the Rotate parameter.`absTime.frame`is python for the "absolute frame number", which is a number that continues to rise until you quit TouchDesigner. 

#### 25\. Timeline lets you Play, Pause and Examine

The [Timeline](<./Timeline.md> "Timeline") is located along the bottom of the main TouchDesigner window. The FPS at the bottom left is the number of frames TouchDesigner will step forward every second. Note that the FPS at the top is the actual number of frames TouchDesigner actually drew in the last second. 

The timeline lets you stop (||), start(>) and step (+) the timeline in TouchDesigner. 

Shift-spacebar will always stop and start the timeline. (Hold down Shift and press the spacebar.) Every time it steps to another frame, it redraws the screen. 

You will see when the timeline reaches the far right, it loops to the beginning of the timeline. But TouchDesigner is mostly event-driven with a free-running clock, so most things you build don't follow the looping timeline and its frame number: For example, create a Constant CHOP, set it to 1 and connect it to a Speed CHOP. It increases its count continuously and does not relate to the timeline. The Speed CHOP restarts when you press its Reset parameter. 

Create a Movie File In TOP and on the File parameter select + and select`Count.mov`. Movie File In TOP plays in its default Sequential Play Mode continuously regardless of the timeline position. 

However if you set its Play Mode menu parameter to "Locked to Timeline", the frame number of the movie and Timeline will stay in sync where the first frame of the movie will be seen at frame 1 always, and you can scrub. 

#### 26\. Create Animation Curves with the Animation Editor

Create an [Animation Component](<./Animation_COMP.md> "Animation COMP"). By default it outputs a CHOP with no channels. Now right-click on the node and select Edit Animation... (or press Edit Animation... in its parameter dialog). 

Click Add Channels button and 3 channels will be created,`tx`,`ty`, and`tz`. Keyframes are the dots on the channels. Click on any keyframe and move it anywhere. To add additional keyframes to any channel, use alt+LMB and click on the location you want the keyframe. Use the right-mouse-button to box-select. Box-select the curve (not the keyframe dot), and change the Function menu from`cubic()`to`linear()`to change interpolation type. 

Then watch the [Timeline](<./Timeline.md> "Timeline") at the bottom and the values of the channel in the Animation component viewer. Note the channel values follow the timeline. 

If you want more control of the timing, connect an animated channel to the Animation component's input: Create a [Beat CHOP](<./Beat_CHOP.md> "Beat CHOP") and wire it to Animation COMP's input. Set the Animation COMP's **Play Mode** to "Use Input Index" and the **Input Index Unit** parameter menu to "Fraction". 

Then create a [Constant CHOP](<./Constant_CHOP.md> "Constant CHOP"), wire it to the Animation COMP first input and move the Constant's`chan1`slider. In both cases, the 0-1 value will control which part of the animation curve is output, de-coupling the Animation COMP from the timeline. You can always change Play Mode to Output Full Range to output the full-length channels. 

Another way to create an animation component pre-wired is to right-click on a parameter and select Keyframe Parameter in... 

#### 27\. DATs are Powerful Text-manipulation Operators

[DATs](<./DAT.md> "DAT") are "Data Operators" that allow you to store and manipulate text in your TouchDesigner networks. Text DATs are used to write scripts that can be run when some event occurs. 

Create a Web DAT and assuming you are on the Internet, press the Fetch parameter. This retrieves HTML, but DATs hold any ASCII text, like Glsl Shaders and scripts. 

Now create a Monitors DAT which a table of rows and columns of cells, each containing text. Attached to the Monitors DAT Is another DAT containing some Python code that runs when you monitor configuration changes. 

This is a bit of a flavor of DATs. 

#### 28\. Sweet Sixteen Operators

There are a lot of OP types in TouchDesigner, but the most common and useful operators in each family are the Sweet Sixteens. You may want to try some of them out. This includes: 
* [Sweet Sixteen CHOPs](<./CHOP.htm#Sweet_16_CHOPs> "CHOP")
  * [Sweet Sixteen TOPs](<./TOP.htm#Sweet_16_TOPs> "TOP")
  * [Sweet Sixteen SOPs](<./SOP.htm#Sweet_16_SOPs> "SOP")
  * [Sweet Sixteen DATs](<./DAT.htm#Sweet_16_DATs> "DAT")

#### 29\. Explore the Operator Snippets

One way to learn more about operators is to see them in small examples. Select the menu Help -> [Operator Snippets](<./OP_Snippets.md> "OP Snippets"). This will start another TouchDesigner window that contains hundreds of examples using operators from each family. This is a rich resource of tips. 

#### 30\. Get Components from the Palette

Components from the Palette Browser contain pre-made networks, and some have a custom control panel. You can also store Components you create in the Palette for easy access and reuse them elsewhere your projects. 

To display a browser of pre-made [Components](<./Component.md> "Component"), toggle off/on the Palette icon. Alternately, click Dialogs -> Palette Browser. Click on a component and drag it to the network. Components on disk are`.tox`files. 

Watch the video [A Movie Player Panel and Building UIs](<http://www.derivative.ca/Events/2016/NorwayWorkshop/>), a tutorial on the basics of panel building.`UI/gal`contains a library of 20 pre-made customizable gadgets that can be copy/pasted into your networks and used to make control panels. 

#### 31\. Get Components from the .tox Forum

Press [ [EXAMPLES](<http://www.derivative.ca/Forum/viewforum.php?f=22>) ] on the TouchDesigner menu bar to go to the .tox Component forum at www.derivative.ca/forum. You can click a .tox on the forum web page to start it in a new TouchDesigner session. You can also download the .tox file to your computer and then drag-drop it into TouchDesigner. Double-clicking any .tox starts it in a new TouchDesigner process as well. 

#### 32\. Speeding it Up with the Performance Monitor

Dialogs -> [Performance Monitor](<./Performance_Monitor.md> "Performance Monitor") will let you see, in one frame, what nodes cook, in what order, and how long they took. Nw be aware, Performance Monitor only shows what cooks on the CPU, not the GPU. But a long bar at the bottom usually means the GPU is still busy finishing rendering a frame and displaying the UI. 

middle-click on any node to see if the node is cooking every frame or not, and how long it took the most recent time it cooked. 

There is also the Perform CHOP, and you can create Info CHOP and drag any node onto it to see more detail on what happened. 

And there is in the palette: Palette -> Tools -> probe, and a wiki page on it: [Palette:probe](<./Palette-probe.md> "Palette:probe"). 

#### 33\. Quick Tips and Good Habits
* Click on the **bulls-eye** circles in a parameter dialog to see which parameters are non-default. This is very useful for understanding other people's networks.
  * **Color Code Nodes** \- With your cursor over the network, press "c" to bring up the color swatch. Select some nodes. Click any color in the color swatch. This only affects the node's appearance in the network.
  * **network overview** \- With your cursor over the network, press "o" to bring up the a miniature node map at the bottom left of the network. You can click on it to pan the network.
  * Ctrl+f (Command+f on macOS) will bring up a **Find bar** that will let you type node names that you may be looking for. Names that match what you type are highlighted and centered.
  * To look at nodes another way, with your cursor over the network, press "t" in the network and it will switch to **"table" mode** where you see all the nodes in a list. You can pick one via the left column, press "t" again, and to go back to the network and see that node highlighted in the network.
  * When you **don't have a mouse** , zoom and scroll the network editor by pressing the keyboard shortcuts Ctrl+=, Ctrl+-, Ctrl+up, Ctrl+down, Ctrl+left, Ctrl+right (all with Command+ on macOS).
  * In OP Create, you can create **nodes-in-a-row** faster by using Shift-click, and create nodes in a branch using Alt-click on the OP Create menu.
  * Node names are **case-sensitive** , so`leve1`is different from`Level1`.
  * The idea of "**Absolute Time** " is a clock that counts up forever and doesn't loop to 0 like the timeline. This gives smooth always-changing values:`absTime.frame`,`absTime.second`s.
  * Use Null operators when referencing or exporting - you can then insert additional operators before the Null to modify your network without having to change your reference or export location
  * The **Status Bar** is located at the top right of TouchDesigner's main window and provides information about recent operations. It may display a message to indicate success/failure of events, or display a hint to tell you how to use a tool. Keep an eye on it. (The [python code](<./UI_Class.md> "UI Class")`ui.status = 'My message'`can be used to place a line in the status bar.)
  * use the **Info DAT or Info CHOP** on a node to see some of its internal states and possibly troubleshoot.
  * It is common practice to use **Shift-Spacebar to stop** , but in Designer Mode, you can use Spacebar.
  * You can turn on/off auto-homing in **SOP viewers** and Geometry viewers. In Preferences -> Geometry turn the options on and then Accept, which makes sure you always see your 3D geometry in-view.
  * **replace an existing wire** by clicking on the output of the new source and clicking on the wire you want to replace.

#### More...

Now you know the basics. Take a break. Later you can go to **[More Things to Know about TouchDesigner](<./More_Things_to_Know_about_TouchDesigner.md> "More Things to Know about TouchDesigner")**
