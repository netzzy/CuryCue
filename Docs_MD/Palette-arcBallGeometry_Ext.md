# Palette:arcBallGeometry Ext

These Extensions reference a specific [Palette:arcBallGeometry](<./Palette-arcBallGeometry.md> "Palette:arcBallGeometry").   
  
# ArcBallExt

The ArcBallExt Class helps with interactively controlling a Geometry COMP given a Container COMP with the Mouse UV Buttons Parameters for left, middle and right enabled. 

## Members

No operator specific members. 

## Methods`ArcBallExt.LoadTransform(dat=None, matrix=None)`→`None`: 

> Given a tableDAT or a tdu.Matrix() it can be used to recall a saved transformation. 
> 
>   * dat - An tableDAT operator reference to the tableDAT that holds the matrix to be loaded.
>   * matrix - A tdu.Matrix object that holds the matrix to be loaded.
>`ArcBallExt.Reset()`→`None`: 

> Resets the ArcBall.`ArcBallExt.SaveTransform(dat=None)`→`None`: 

> Will save out the current ArcBall's transformation matrix to a tableDAT. If no TableDAT is given, the internal newMat TableDAT is being used. 
> 
>   * dat - A tableDAT operator reference to the tableDAT where to write the current transform matrix into.
>`ArcBallExt.StartTransform(btn=None, u=0, v=0)`→`None`: 

> Will begin a transform depending on the mouse button pressed. 
> 
>   * btn - The mouse btn pressed. Can be one of 'lselect', 'rselect' or 'mselect' corrseponding to 'rotate', 'pan' and 'zoom'.
>   * u - The horizontal mouse position on the control panel.
>   * v - The vertical mouse position on the control panel.
>`ArcBallExt.Transform(btn=None, u=0, v=0, scaler=1)`→`None`: 

> Applies a transform to the ArcBall depending on the mouse button pressed. 
> 
>   * btn - The mouse btn pressed. Can be one of 'lselect', 'rselect' or 'mselect' corrseponding to 'rotate', 'pan' and 'zoom'.
>   * u - The horizontal mouse position on the control panel.
>   * v - The vertical mouse position on the control panel.
>   * scaler - A multiplier to increase or decrease the transformation.
>`ArcBallExt.fillMat()`→`None`: 

> Utility function used by the ArcBall.
