# absTime Class

  
This class contains information on the "[absolute time](<./Absolute_Time.md> "Absolute Time")", the time TouchDesigner has been running since the process started. It can be accessed with the abstime object, found in the automatically imported [td module](<./Td_Module.md> "Td Module"). It is paused only with the power on/off button at the top of the UI, or with the power() method in the [td module](<./Td_Module.md> "Td Module"). Absolute time is the same for all nodes and is not affected by the pausing any component's timeline. See [absolute time](<http://en.wikipedia.org/wiki/Absolute_time_and_space>). 

## Members`frame`→`float`**(Read Only)** : 

> Absolute total number of frames played since the application started. Paused only with the power On/Off or with power() 
[code]
>     absTime.frame
>     tdu.rand(absTime.frame + .1) # a unique random number that is consistent across all nodes, changing every frame
>     
[/code]`seconds`→`float`**(Read Only)** : 

> Absolute total seconds played since the application started. Paused only with the power On/Off or with power().`step`→`float`**(Read Only)** : 

> Number of absolute frames elapsed between start of previous and current frame. When this value is greater than 1, the system is dropping frames.`stepSeconds`→`float`**(Read Only)** : 

> Absolute time elapsed between start of previous and current frame.

## Methods

No operator specific methods. 

  
TouchDesigner Build: Latest\nwikieditorwikieditor2022.241402021.100002018.28070before 2018.28070
