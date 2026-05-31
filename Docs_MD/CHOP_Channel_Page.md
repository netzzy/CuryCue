# CHOP Channel Page

## Channel Name Creation  
  
Channel Name - The following kinds of text patterns generate multiple channel names: 

Channel Pattern  | Channels Created   
---|---`chan1 chan2 chan3`|`chan1 chan2 chan3``chan[1-3]`|`chan1 chan2 chan3``ch[1-2]n[2-6:2]`|`ch1n2 ch1n4 ch1n6 ch2n2 ch2n4 ch2n6``r[xyz]`|`rx, ry rz``geo[1-2]:t[xy]`|`geo1:tx geo1:ty geo2:tx geo2:ty``gain band[4-6] off[lr]`|`gain band4 band5 band6 offl offr`## Start-End

Start/End - Specifies a start-end interval. The default is start-end of 0. The values in these options can be expressed in any [Units](<./CHOP_Common_Page.htm#Units> "CHOP Common Page"). 

## Sample Rate

Sample Rate \- Usually the CHOP sample rate is set to 60 "samples per second". This means TouchDesigner will attempt to cook the operation 60 times per second. Using a lower sample rate than the global sample sample rate can cause aliasing (errors) in the channel data. 

## Extend Conditions

Extend Conditions \- Found in the Extend CHOP and also in several generator CHOPs, this determines what values you get when you try to sample a CHOP outside its start-end range. It can hold values, repeat the channel and more. 

When using the`chop()`function to sample a channel, the index-value may be outside the interval of the CHOP. But a reasonable value is returned. The user is able to control the value of the channel outside the CHOP's interval. 

You can see the state of the Extend Conditions in the pop-up info of any CHOP. 

Extend Left - The extend condition before the CHOP interval. They are: 
* Hold - Hold the first or last value.
  * Slope - Continue the slope before the start, or after the end of the channel.
  * Cycle - Cycle the channel repeatedly.
  * Mirror - Cycle the channel repeatedly, mirroring every other cycle.
  * Default Value - Use the constant value specified in the Default Value parameter.


Extend Right - Extend condition after the interval. Same options as Extend Left. 

Default Value - The value used for the Default Value extend condition. 

## Legal Channel Names

CHOP channel names can have the following characters: 
* Upper and lower-case letters
  * Numbers
  * The following characters:`-``_``:``/`In general, CHOPs will replace invalid characters with underscores.
