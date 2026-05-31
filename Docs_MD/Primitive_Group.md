# Primitive Group

Primitive groups are a collection of associated primitives that are treated as a set. This is important because you can apply operations to them as a whole - saving you from having to apply discrete operations to each element. Moreover, primitive groups can be used to filter out primitives that aren't needed for a specific operation. Rather than affecting an entire input, grouping restricts the scope of an operation to the primitives in the group. 

#### Creating Primitive Groups

To group primitives in Touch use a [Group SOP](<./Group_SOP.md> "Group SOP"), any SOP with a point group input field, or the Select state in a [SOP Editor](<./SOP_Editor.md> "SOP Editor"). To group primitives in the SOP Editor: 
1. Use the Select state, and in the sub-icons, choose the **Primitive Groups** icon.
  2. Select the desired primitives with the cursor.
  3. Call up the Parameters dialog by clicking the + button, and click on the Combine Groups page-tab.
  4. Type a new group name in the edit field.
  5. Click on the **group <\- selection** button.

#### Ordered and Unordered Groups

A primitive group can be ordered or unordered. In the SOP Editor's Select state, a single click of the mouse button performs an ordered selection. Bulk selections are made by dragging the cursor across the primitives. This action creates a marquee box that encloses a number of primitives. Primitives selected in this fashion generate an unordered group. 

The only time bulk selections generate or maintain an ordered selection is when only one primitive is caught in the marquee box. Unordered groups store their primitives in creation order; ordered groups store primitive in selection order. 

If you want to reselect the primitives in the group, you can do so by calling up the Parameters dialog from the Select state, and selecting the group name from the Group parameter pop-up menu under the Combine Groups page-tab. Then click on the button **selection <\- group**. 

When a primitive is deleted, Touch automatically removes the primitive from all the primitive groups it might belong to. 

See also: [Point Groups](<./Point_Group.md> "Point Group"), [Geometry Detail](<./Geometry_Detail.md> "Geometry Detail"), [Point](<./Point.md> "Point"), [Point List](<./Point_List.md> "Point List"), [Point Class](<./Point_Class.md> "Point Class"), [Primitive](<./Primitive.md> "Primitive"), [Prims Class](<./Prims_Class.md> "Prims Class"), [SOP](<./SOP.md> "SOP"), [SOP Class](<./SOP_Class.md> "SOP Class"), [Script SOP](<./Script_SOP.md> "Script SOP"), [Attributes](</index.php?title=Attributes&action=edit&redlink=1> "Attributes \(page does not exist\)").
