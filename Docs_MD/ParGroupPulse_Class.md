# ParGroupPulse Class

The ParGroupPulse class describes a subclass of a ParGroup ending with a pulse parameter. See also Custom ParGroup. 

**Note:** the ParGroupPulse class will be deprecated in coming TouchDesigner releases. It is recommended that you access pulse parameters directly rather than through this object. 

## Members

No operator specific members. 

## Methods`pulse(value, frames=0, seconds=0)`→`None`: 

> Pulsing sets a parameter to the specific value, cooks the operator, then restores the parameter to its previous value. 
> 
> For pulse type parameters no value or time is specified or used. 
> 
>   * value - (Optional) The tuple to pulse this parGroup with, default is`[1]`.
>   * frames - (Optional) Number of frames before restoring the parameter to its original value.
>   * seconds - (Optional) Number of seconds before restoring the parameter to its original value.
> 

[code]
>     op('moviein1').parGroup.reload.pulse([1]) # set the reload toggle, then cook
>     op('glsl1').parGroup.loadvariablenames.pulse() # activate the pulse parameter
>     op('geo1').parGroup.t.pulse([0,2,0], frames=120) # pulse geometry transform for 120 frames
>     op('text1').parGroup.text.pulse(['GO!'], seconds=3) # pulse text TOP string field, for 3 seconds
>     op('noise').parGroup.type.pulse(['random'], seconds=0.5) # pulse noise menu type for half a second
>     
[/code]

TouchDesigner Build: Latest\nwikieditorwikieditorwikieditorbefore wikieditor
