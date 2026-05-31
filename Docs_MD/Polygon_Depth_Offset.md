# Polygon Depth Offset

Polygon Depth Offset is a way of dealing with [Z-Fighting](<./Z-Fighting.md> "Z-Fighting"). Polygon Depth Offset will push the depth values of a polygon away from the camera some number of units. This occurs in a camera-independent way, so its much easier to do than to offset your polygons by hand simply by using translations (Since a translation in one direction will work from one camera view, but not from a different one). 

The value of the offset is`polygonOffsetFactor * deltaZ + minValue * polygonOffsetUnits`, where`deltaZ`is a measurement of the change in depth relative to the screen area of the polygon, and`minValue`is the smallest value that is guaranteed to produce a resolvable offset for a given implementation. Essentially, the`polygonOffsetUnits`are a constant change to the offset, and the`polygonOffsetFactor`is a change depending on how sloped the surface is to the viewer.
