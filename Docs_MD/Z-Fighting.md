# Z-Fighting

Z-Fighting occurs when you have two polygons that are co-planar. This means they essentially occupy the same spot in space. Z-Fighting is the result of the graphics card being unable to decide which polygon is in front of the other one in a consistent manner. What usually happens is some parts of one polygon will be visible, while other parts of the other polygon will be visible. This can be avoided by either slightly offsetting the position of one of the geometries, or by using the [Polygon Depth Offset](<./Polygon_Depth_Offset.md> "Polygon Depth Offset").
