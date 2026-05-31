# Hierarchy

Hierarchy relates components with other components. Hierarchies let one component to be positioned relative to another component. 

There are two groups of Hierarchy in TouchDesigner. **3D Object Components**, and **2D Panel Components**. Each group can be connected via lines ([Wires](<./Wire.md> "Wire")) between the bottoms/tops of nodes in a network, or by placing one component inside the other. 
* For 3D Object hierarchies, it means that 3D objects are connected to other 3D objects and can be moved/rotated/scaled (transformed) as a group in 3D, and relative to each other.
* For 2D panel hierarchies, it means that panels are contained inside other panels, and panels can be built into larger user interfaces. panels can be moved and scaled as a group, or relative to each other, by adjusting with their parameters.


As noted, each group can be related/connected in two ways: 
1. by connecting lines between the bottoms/tops of nodes in a network as shown in the examples above. The node at the top is the parent, the node at the bottom is the child. The child can be transformed relative to the parent via its transform parameters.
  2. by placing one component inside the other. The node inside is the child, the node that encloses it is the parent. The child can be transformed relative to the parent via its transform parameters and via the parent's Layout parameters. You can see the [Network Path](<./Network_Path.md> "Network Path") hierarchy in the [Pane Bar](<./Pane_Bar.md> "Pane Bar") at the top of each network.


Hierarchy lines always connect nodes in the same component group. 

To create a hierarchy where operators are in the same network: 
1. Left-click on a component's bottom or top connector.
  2. Move the cursor to the top/bottom connector of the component you wish to connect to.
  3. Click a second time to complete the connection.


Or, using the embedded approach: For panels, put a panel inside a panel. For 3D objects put a 3D object inside the 3D object. 

  
( "Hierarchies" also exist separately the file system, and in python data structures, but it is not applicable or covered here. ) 

## See also

[Connector](<./Connector.md> "Connector"), [Wire](<./Wire.md> "Wire"), [Link](<./Link.md> "Link"), [Operator](<./Operator.md> "Operator"), [Node](<./Node.md> "Node")
