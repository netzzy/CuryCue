# Palette:quadReproject Ext

These Extensions reference a specific [Palette:quadReproject](<./Palette-quadReproject.md> "Palette:quadReproject"). The Extension class of a quadReproject COMP.   
  
# QuadReprojectExt

QuadReprojectExt description 

## Members

No operator specific members. 

## Methods`QuadReprojectExt.CreateScreenParSet(curr, prev)`: 

> This method is used to create a block of parameters for one or multiple additional quad reproject screens. A parameter should be passed with the new number of screens as well as the previous value. It will add as many screens as needed between the new value and the previous value. The new value should always be bigger than the previous value. Warning: this function is called when changing the Number Of Screens parameter value.`QuadReprojectExt.DestroyScreenParSet(curr, prev)`: 

> This method is used to destroy a block of parameters for one or multiple additional quad reproject screens. A parameter should be passed with the new number of screens as well as the previous value. It will destroy as many screens as needed between the new value and the previous value. The new value should always be smaller than the previous value. Warning: this function is called when changing the Number Of Screens parameter value.`QuadReprojectExt.UpdateScreensTableRowResolution(parName)`: 

> This method is used to update the resolution of an already existing screen. The resulting update will also change it's type from Render TOP to Render Select TOP or Render Select TOP to Render TOP when necessary.
