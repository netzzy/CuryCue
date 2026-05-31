# Segment Class

A Segment object describes a single segment from a Timer CHOP. 

## Members`beginFrames`→`int`**(Read Only)** : 

> The beginning point of the segment expressed in frames.`beginSamples`→`int`**(Read Only)** : 

> The beginning point of the segment expressed in samples.`beginSeconds`→`float`**(Read Only)** : 

> The beginning point of the segment expressed in seconds.`custom`→`dict`**(Read Only)** : 

> dictionary of all the extra column values associated with the segment.`cycle`→`bool`**(Read Only)** : 

> Whether or not the segment will repeat itself.`cycleEndAlertFrames`→`int`**(Read Only)** : 

> The amount of time before cycling the callback will be executed, expressed in frames.`cycleEndAlertSamples`→`int`**(Read Only)** : 

> The amount of time before cycling the callback will be executed, expressed in samples.`cycleEndAlertSeconds`→`float`**(Read Only)** : 

> The amount of time before cycling the callback will be executed, expressed in seconds.`cycleLimit`→`bool`**(Read Only)** : 

> Whether or not the segment will repeat itself indefinitely.`delayFrames`→`int`**(Read Only)** : 

> The delay portion of the segment expressed in frames.`delaySamples`→`int`**(Read Only)** : 

> The delay portion of the segment expressed in samples.`delaySeconds`→`float`**(Read Only)** : 

> The delay portion of the segment expressed in seconds.`lengthFrames`→`int`**(Read Only)** : 

> The length portion of the segment expressed in frames.`lengthSamples`→`int`**(Read Only)** : 

> The length portion of the segment expressed in samples.`lengthSeconds`→`float`**(Read Only)** : 

> The length portion of the segment expressed in seconds.`maxCycles`→`int`**(Read Only)** : 

> The maximum number of repetitions.`owner`→`OP`**(Read Only)** : 

> The OP to which this object belongs.`row`→`int`**(Read Only)** : 

> Named tuple of all the parameter or column values describing the segment.`speed`→`float`**(Read Only)** : 

> The speed multiplier of the segment.`index`→`int`**(Read Only)** : 

> The numeric index of this segment.

## Methods

No operator specific methods. 

TouchDesigner Build: Latest\nwikieditor2022.24140
