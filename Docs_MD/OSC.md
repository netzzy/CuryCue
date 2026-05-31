# OSC

Open Sound Control is a standard that is used to exchange messages between applications that adhere to the Open Sound Control specification [OSC spec](<http://www.cnmat.berkeley.edu/OpenSoundControl/>). 

TouchDesigner supports OSC through four operators: the [OSC In CHOP](<./OSC_In_CHOP.md> "OSC In CHOP") and [OSC Out CHOP](<./OSC_Out_CHOP.md> "OSC Out CHOP") that receive and send CHOP channels, and the [OSC In DAT](<./OSC_In_DAT.md> "OSC In DAT") and [OSC Out DAT](<./OSC_Out_DAT.md> "OSC Out DAT") that receive/send OSC as messages that can be interpreted with python. 

The OSC In CHOP is based on a connection-less system, meaning that it can accept multiple messages for any number of input sources at the same time. 

TouchDesigner is listed as an application in the Open Sound Control consortium, and now supports most of the OSC features. See [OSC Implementations](<http://opensoundcontrol.org/implementations>). 

  
See also: [wikipedia on OSC](<http://en.wikipedia.org/wiki/OpenSound_Control>)
