# Network Utilities: Comments, Network Boxes, Annotates

Network Utilities are a special class of [nodes](<./Node.md> "Node") that are used to organize TouchDesigner networks. The built-in Network Utilities are **Comments** and **Network Boxes** , while **[Annotates](<./Annotate_COMP.md> "Annotate COMP")** are more full-featured and open components. You can also create custom Network Utilities. 

# Built-in Network Utilities

The built-in Network Utilities are designed for common documentation and grouping tasks in TouchDesigner networks. They are created using options in the RMB menu, and can generally be sized or moved much like regular nodes. 

## Comments

**Comments** are used for simple text documentation in networks. **To create a Comment** , select`Add Comment`from the network RMB menu, or press Shift-C with your mouse over a network. You can click anywhere in the Comment to edit the text. **To move** the Comment, drag it from anywhere in the middle, and **to size it** , drag an edge. 

## Network Boxes

Network Boxes are used to group, label, and move nodes. **To create a Network Box** , select`Add Network Box`from the network RMB menu, or press Shift-B with your mouse over a network. You can click on the title to edit the text. **To move** the Network Box, drag it by the title, and any nodes inside it will move with it. **To drag** the box _without_ dragging the enclosed nodes, hold down Alt while dragging. **To size** the Network Box, drag an edge. You can also drag a node so that its edge overlaps the edge of the Network Box; the box will automatically grow to enclose the node. 

The title is the only part of a Network Box that you can interact with via mouse button. Clicking on the body area is exactly like clicking directly on the network. 

## Network Utility Node Details

Network Utility nodes (or just **Utility nodes**) are similar to other TouchDesigner nodes but there are a few important differences: 

### Parameters

In order to keep things simple, parameters don't appear in the standard pane parameter dialog when a Utility node is selected. Comments and Network Boxes have a simplified parameter box available via RMB, and their full parameter boxes are available via Alt-RMB. 

In the simplified parameters, you can change the text size of Comments and the title size/alignment of Network Boxes. To read about the parameters available in the full parameter box, see [Annotate COMP](<./Annotate_COMP.md> "Annotate COMP"). The Annotate COMP has a **Utility parameter** on the Annotate page that allows you to turn off an on whether it is treated as a Network Utility. 

### Hidden From OP Find DAT and Search/Replace Dialog

To keep Utility nodes from interfering with introspective networks, they will not show up in [OP Find DAT](<./OP_Find_DAT.md> "OP Find DAT") unless the **Include Utility** parameter (on the Families page) is toggled on. Similarly, when using the [Search/Replace Dialog](<./SearchReplace_Dialog.md> "SearchReplace Dialog"), Utility nodes will not show up unless **Comments (Utility)** is toggled on in the Advanced mode. 

### Hidden From Python

To keep Utility nodes from interfering with introspection, they will be hidden by default from some Python methods and members:`**op**`,`**ops**`, and`**COMP.findChildren**`will not return any Utility nodes unless`includeUtility=True`is included as an argument.`**COMP.cook(recurse=True)**`will not recurse through utility nodes unless`includeUtility=True`is included as an argument.`**COMP.children**`,`**COMP.currentChild**`, and`**COMP.selectedChildren**`will never return Utility nodes. 

### "Enter" shortcut disabled

To prevent accidentally entering Network Utilities, the "Enter" network shortcut has been disabled. To look at the inner networks, you can select a Utility node, then RMB on the network and select`Jump Down`. 

## Custom Network Utility Nodes

Network Utility nodes are based on the **[Annotate COMP](<./Annotate_COMP.md> "Annotate COMP")** , which allows a [Panel](<./Panel.md> "Panel") to be displayed as part of a TouchDesigner network. You can explore Comments, Network Boxes, and the default Annotate COMP as examples. You'll discover that Comments and Network Boxes are just modes of Annotate, and can be selected via its Mode parameter. For more details, visit the [Annotate COMP](<./Annotate_COMP.md> "Annotate COMP") page.
