# Wire

**Wires** are the colored lines that connect the output of a node to the inputs of other nodes in a network. You can think of wires as passing the data from one node to another. 

A second type of wire is the Hierarchy Wire that connects the connectors on the top/bottom of 3D Components and 2D Panel Components, and forms the parent-child relation of these components. 

Wires always connect nodes in the same [Family](<./Operator.md> "Operator"): A wire between 2 CHOPs exposes the set of channels of the source CHOP to the destination CHOP. A wire between 2 TOPs exposes the image of the source TOP to the destination TOP. Left-right Data Wires occur on [CHOPs](<./CHOP.md> "CHOP"), [TOPs](<./TOP.md> "TOP"), [SOPs](<./SOP.md> "SOP"), [DATs](<./DAT.md> "DAT") and occasionally [MATs](<./MAT.md> "MAT"). 

To create a wire: 
1. Left-click on a node's input or output.
  2. Move the cursor to the output or input of the node you wish to connect to.
  3. Click a second time to complete the connection.


or 
1. Left-click on a node's input or output, and while holding it down, drag the cursor to the output or input of the node you wish to connect to.
  2. Release the left button.


When the cursor is over a connecting wire, it will highlight in yellow. In this highlighted state, on the wire you can 
* [MMB](<./Mouse_Click.md> "Mouse Click") (middle mouse button click) to get info for the incoming node
  * [RMB](<./Mouse_Click.md> "Mouse Click") to bring up a menu that allows you to 
    * insert an operator via the OP Create Dialog
    * select the source node
    * select the destination node
    * disconnect the wire


Wires display animated dashed lines to provides visual feedback as to which nodes in a network are cooking. The animated dashed lines represent the flow of data between nodes. 

**Tip** : Wires can be displayed in two modes: spline curves and straight lines. Pressing the hotkey "**s** " (straight) in a [Network Editor](<./Network_Editor.md> "Network Editor") pane will toggle between these two modes. You can also toggle the setting by using the "**Link Straight**" menu option from the Network Editor's context menu. 

**Note** : When an operator cooks and data is generated, if it is connected by a wire to another operator, it doesn't actually pass or copy its data to the destination - it only informs the destination of where to get its data to operate on. 

  
**Wires in spline mode**

**Wires in straight mode**

## See also

[Connector](<./Connector.md> "Connector"), [Hierarchy](<./Hierarchy.md> "Hierarchy"), [Link](<./Link.md> "Link"), [Operator](<./Operator.md> "Operator"), [Node](<./Node.md> "Node")
