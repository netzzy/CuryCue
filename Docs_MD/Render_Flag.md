# Render Flag

The Render Flag is a [flag](<./Flag.md> "Flag") on all SOP nodes and on all Geometry components that is used to select the SOP for rendering by the [Render TOP](<./Render_TOP.md> "Render TOP"). 

In order for the object to be rendered by the Render TOP: 
* the SOP's Render flag must be set.
  * the Geometry component that contains the SOP must have its Render flag set.
  * the Geometry component that contains the SOP must be specified in the Render TOP's "Geometry" parameter.


See also: [Flag](<./Flag.md> "Flag") and [Display Flag](<./Display_Flag.md> "Display Flag").
