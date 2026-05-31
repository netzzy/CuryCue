# Network Path

Every node has a **network path** or **path**. The path is the location of an [operator](<./Operator.md> "Operator") within the [Hierarchy](<./Hierarchy.md> "Hierarchy") of a TouchDesigner project. For example,`/geo1/circle1`, is a node called`circle1`in a component called`geo1`. The path`/`is called Root or Home. [Components](<./Component.md> "Component") are used to create another level in the path, slike folders/directories do for the file paths on your computer. 

Example: The path of a node`text1`is`/project1/container1/button2/text1`. All nodes in the path up the last node in a path are Components. That is,`project1`,`container1`and`button2`are all components. 

If a path starts with`/`, it is an "absolute path", which refers back to the top root of the heirarchy. Example:`/project1/wave1`. 

If you refer to another node is in the same network, you can just put the node name:`text1`or`button1/out1`. This is a "relative path". 

If you are in`/project1/container1/button2`, the "parent node" is`/project1/container1`. You can refer to another node in`/project1/container1`using the "`..`" form:`../button3`, where`..`means "my parent".`../button3`is a "relative path". 

Network path does not refer to location of a TouchDesigner file in the Windows file system. The network path of the currently selected operator is located at the top of every [pane](<./Pane.md> "Pane") in TouchDesigner. The highest level of a TouchDesigner network is indicated by a ' **`/`** ' and is called the **root** of the network. 

You can navigate up and down the network hierarchy by using the mouse's roller wheel, the Enter and "i" keys, or left-clicking on the network path at the top of the pane. Clicking on the lowest level of the current path will show a drop down list of available child Components that may be selected. To navigate up the hierarchy, use the roller wheel, the "u" key, or select the appropriate '`/`' in the path to navigate to that level. 

#### Where you will find Paths

At the top of every [Network Editor](<./Network_Editor.md> "Network Editor") you see a path of the component whose network you are looking at. 

Operators often have a path parameter, like the [Select TOP](<./Select_TOP.md> "Select TOP"), which allows it to get an image from any network. 

Any parameter can have a Python expression that contains paths. 

Paths are found in Python scripts and callbacks are contained in DATs, typically a [Text DAT](<./Text_DAT.md> "Text DAT"). 

You may see an expression`op('wave1')['chan1']`, which is a channel called`chan1`in the CHOP called`wave1`. 

You may see an expression`op('/project1/effect/transform1').par.tx`, which is the`tx`parameter of the`transform1`node. 

The [OP Find DAT](<./OP_Find_DAT.md> "OP Find DAT") outputs a table of paths. 

In exporting you will see the path to a parameter:`transform:tx`This is the`tx`parameter of a Transform TOP. 

#### See Also
* * *
* [Folder](<./Folder.md> "Folder")
  * [Bookmarks](<./Bookmark.md> "Bookmark")
