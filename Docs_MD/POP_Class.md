# POP Class

A POP describes a reference to a POP operator, containing points and primitives. 

## Members`compare`→`bool`: 

> Get or set Compare Flag.`dimension`→`Dimension`**(Read Only)** : 

> The dimension in this POP.`maxVertsPerLineStrip`→`int`**(Read Only)** : 

> The max number of verts per line strip in this POP.`pointAttributes`→ **(Read Only)** : 

> The set of point attributes defined in this POP.`pointAttributesChanged`→ **(Read Only)** : 

> The point attributes changed by this POP.`primAttributes`→ **(Read Only)** : 

> The set of primitive attributes defined in this POP.`primAttributesChanged`→ **(Read Only)** : 

> The prim attributes changed by this POP.`template`→`bool`: 

> Get or set Template Flag.`vertAttributes`→ **(Read Only)** : 

> The set of vertex attributes defined in this POP.`vertAttributesChanged`→ **(Read Only)** : 

> The vert attributes changed by this POP.

## Methods`bounds(delayed=False)`→`Bounds`: 

> Returns an [object](<./Bounds_Class.md> "Bounds Class") with the bounds, center and size of the POP's geometry. 
> 
>   * delayed - (Keyword, Optional) If set to True, the download results will be delayed until the next call to bounds(), avoiding stalling the GPU waiting for the result immediately.
>`computeBounds(display=False, render=False, delayed=False)`→`Bounds`: 

> Returns an [object](<./Bounds_Class.md> "Bounds Class") with the bounds, center and size of the POP's geometry. 
> 
>   * display - (Keyword, Optional) If set to True, only calculate Bounding Box if POP display flag is set.
>   * render - (Keyword, Optional) If set to True, only calculate Bounding Box if POP render flag is set.
>   * delayed - (Keyword, Optional) If set to True, the download results will be delayed until the next call to computeBounds(), avoiding stalling the GPU waiting for the result immediately.
>`numPoints(delayed=False, max=False)`→`int`: 

> Returns the number of points contained in this POP. 
> 
>   * delayed - (Keyword, Optional) If set to True, the download results will be delayed until the next call to numPoints(), avoiding stalling the GPU waiting for the result immediately.
>   * max - (Keyword, Optional) If set to True, returns the number of allocated points (max number of points). In that case result is always instant, delayed is disregarded.
>`numPrims(delayed=False, max=False, primType=None)`→`int`: 

> Returns the number of primitives contained in this POP. 
> 
>   * delayed - (Keyword, Optional) If set to True, the download results will be delayed until the next call to numPrims(), avoiding stalling the GPU waiting for the result immediately.
>   * max - (Keyword, Optional) If set to True, returns the number of allocated primitives (max number of primitives). In that case result is always instant, delayed is disregarded.
>   * primType - (Keyword, Optional) If set to triangles, quads, lineStrips, lines or pointPrims, returns the number of primitives for that primitive type only.
>`numVerts(delayed=False, max=False, lineStrips=False)`→`int`: 

> Returns the number of vertices contained in this POP. 
> 
>   * delayed - (Keyword, Optional) If set to True, the download results will be delayed until the next call to numVerts(), avoiding stalling the GPU waiting for the result immediately.
>   * max - (Keyword, Optional) If set to True, returns the number of allocated vertices (max number of verts). In that case result is always instant, delayed is disregarded.
>   * lineStrips - (Keyword, Optional) If set to true, returns the number of verts for line strips only.
>`points(attributeName, startIndex=0, count=-1, delayed=False)`→`list`: 

> Returns the point attribute values as a list. 
> 
>   * attributeName - The attribute name.
>   * startIndex - (Keyword, Optional )The point index to start at (default 0).
>   * count - (Keyword, Optional) The number of points to download. A value of -1 fetches all elements from the start index onward.
>   * delayed - (Keyword, Optional) If set to True, the download results will be delayed until the next call to vals(), avoiding stalling the GPU waiting for the result immediately.
>`prims(attributeName, startIndex=0, count=-1, delayed=False)`→`list`: 

> Returns the primitive attribute values as a list. 
> 
>   * attributeName - The attribute name.
>   * startIndex - (Keyword, Optional )The primitive index to start at (default 0).
>   * count - (Keyword, Optional) The number of primitives to download. A value of -1 fetches all elements from the start index onward.
>   * delayed - (Keyword, Optional) If set to True, the download results will be delayed until the next call to vals(), avoiding stalling the GPU waiting for the result immediately.
>`reallocate()`→`None`: 

> Forces the POP to reallocate its GPU buffers.`save(filepath, createFolders=False)`→`str`: 

> Save the POP geometry to file system. Multiple file types are supported. Returns the filename and path saved. 
> 
>   * filepath - (Optional) The path and filename to save to. If not given then a default filename will be used, and the file will be saved in the project.folder folder.
>   * createFolders - (Keyword, Optional) If True, it creates the not existent directories provided by the filepath.
>`verts(attributeName, startIndex=0, count=-1, delayed=False)`→`list`: 

> Returns the vertex attribute values as a list. 
> 
>   * attributeName - The attribute name.
>   * startIndex - (Keyword, Optional )The vertex index to start at (default 0).
>   * count - (Keyword, Optional) The number of vertices to download. A value of -1 fetches all elements from the start index onward.
>   * delayed - (Keyword, Optional) If set to True, the download results will be delayed until the next call to vals(), avoiding stalling the GPU waiting for the result immediately.
> 


TouchDesigner Build: Latest\nwikieditorwikieditor2025.30000
