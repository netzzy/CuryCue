# ArcBall Class

Encapsulates many aspects of 3D viewer interaction. Rotation via arcball, translation and scale. 
[code] 
    a = TDU.ArcBall(forCamera=False)
    
[/code]  
  
## Instantiators`TDU.ArcBall(forCamera=False)`→`TDU.ArcBall`: 

> Create a new ArcBall object 
> 
>   *`forCamera`\- If True, matrices used are from the camera perspective (the world matrices are inverted before being returned or used)
> 

## Members

No operator specific members. 

## Methods`beginPan(u, v)`→`None`: 

> Begin a pan at at the given u and v. 
[code]
>     m.beginPan(.1, .2)
>     
[/code]`beginRotate(u, v)`→`None`: 

> Begin an arcball rotation at the given u and v. 
[code]
>     m.beginRotate(.1, .2)
>     
[/code]`beginDolly(u, v)`→`None`: 

> Begin a dolly at at the given u and v. 
[code]
>     m.beginDolly(.1, .2)
>     
[/code]`pan(u, v)`→`None`: 

> Pan the view by the given x and y. 
[code]
>     m.pan(.1, .2)
>     
[/code]`panTo(u, v, scale=1.0)`→`None`: 

> Pan from the u,v given in the last call to beginPan() to the given u and v, applying a scale as well to the pan amount. 
> 
>   * scale - (Keyword, Optional) Scale the operation by this amount.
> 

[code] 
>     m.panTo(.1, .2)
>     
[/code]`rotateTo(u, v, scale=1.0)`→`None`: 

> Rotates the arcball to the given u and v position. 
> 
>   * scale - (Keyword, Optional) Scale the operation by this amount.
> 

[code] 
>     m.rotateTo(.1, .2)
>     
[/code]`dolly(z)`→`None`: 

> Dolly the view by the given z value. 
[code]
>     m.dolly(.3)
>     
[/code]`dollyTo(u, v, scale=1.0)`→`None`: 

> Dolly from the u,v given in the last call to beginDolly() to the given u and v, applying a scale as well to the dolly amount.(Keyword, Optional) 
> 
>   * scale - Scale the operation by this amount.
> 

[code] 
>     m.dollyTo(.1, .2)
>     
[/code]`transform()`→`TDU.Matrix`: 

> Gets the current transform [matrix](<./Matrix_Class.md> "Matrix Class") for the arcball. 
[code]
>     m.transform()
>     
[/code]`setTransform(matrix:[TDU.Matrix](<./Matrix_Class.md> "Matrix Class"))`→`None`: 

> Sets the current transform matrix for the arcball. Scales in the given matrix will be ignored. 
[code]
>     m.setTransform(m)
>     
[/code]`identity()`→`None`: 

> Resets all values of the ArcBall to the default state. 
[code]
>     m.identity()
>     
[/code]

TouchDesigner Build:  Latest\nwikieditor wikieditor wikieditor mw-rollback mw-reverted 2025.30000 2022.24140 2021.10000 2018.28070 before 2018.28070
