# Event

**Events** in TouchDesigner are single-moment occurrences that are generated from a variety of conditions - from input actions that a user causes, from external devices and software, and from internal TouchDesigner states caused by things like timers and values crossing thresholds.   
  
A variety of operators (mostly DATs) respond to events. Each one has python callback functions in a DAT that enable a user to write code to react to events. 

TouchDesigner is a [Procedural](<./Procedural.md> "Procedural") pull-based system (outputs to displays, audio devices and other destinations cook the nodes it needs to generate the outputs). But it is also a push system based on operators that respond to events. 

The event operators respond to events they receive via their python callback functions. The callbacks can cause other operators to change and cook via their parameters, table cells, extension properties, storage. 

### Operators that Respond to Events

The operators that respond to events are: 

The groups of "Execute" DATs that respond to changes within TouchDesigner: 
* [CHOP Execute DAT](<./CHOP_Execute_DAT.md> "CHOP Execute DAT")
  * [Parameter Execute DAT](<./Parameter_Execute_DAT.md> "Parameter Execute DAT")
  * [DAT Execute DAT](<./DAT_Execute_DAT.md> "DAT Execute DAT")
  * [Execute DAT](<./Execute_DAT.md> "Execute DAT")
  * [OP Execute DAT](<./OP_Execute_DAT.md> "OP Execute DAT")
  * [OP Find DAT](<./OP_Find_DAT.md> "OP Find DAT")


The DATs that respond to user interface interactions: 
* [Panel Execute DAT](<./Panel_Execute_DAT.md> "Panel Execute DAT")
  * [Render Pick DAT](<./Render_Pick_DAT.md> "Render Pick DAT"), [Render Pick CHOP](<./Render_Pick_CHOP.md> "Render Pick CHOP"), [Multi Touch In DAT](<./Multi_Touch_In_DAT.md> "Multi Touch In DAT")
  * [Keyboard In DAT](<./Keyboard_In_DAT.md> "Keyboard In DAT")


Operators that react to external events: 
* [MIDI In DAT](<./MIDI_In_DAT.md> "MIDI In DAT"), [MIDI Event DAT](<./MIDI_Event_DAT.md> "MIDI Event DAT")
  * [OSC In DAT](<./OSC_In_DAT.md> "OSC In DAT")
  * [Serial DAT](<./Serial_DAT.md> "Serial DAT")
  * [TCP/IP DAT](<./TCP/IP_DAT.md> "TCP/IP DAT")
  * [WebSocket DAT](<./WebSocket_DAT.md> "WebSocket DAT")
  * [Web Client DAT](<./Web_Client_DAT.md> "Web Client DAT")
  * [Web Server DAT](<./Web_Server_DAT.md> "Web Server DAT")
  * [UDP In DAT](<./UDP_In_DAT.md> "UDP In DAT")
  * [Art-Net DAT](<./Art-Net_DAT.md> "Art-Net DAT")
  * [Folder DAT](<./Folder_DAT.md> "Folder DAT")
  * [Monitors DAT](<./Monitors_DAT.md> "Monitors DAT")
  * [MQTT Client DAT](<./MQTT_Client_DAT.md> "MQTT Client DAT")


Operators that run scripts when some of their their parameters are pulsed: 
* [Timer CHOP](<./Timer_CHOP.md> "Timer CHOP")
  * [Event CHOP](<./Event_CHOP.md> "Event CHOP")


And operators that react to event pulses: 
* [Trigger CHOP](<./Trigger_CHOP.md> "Trigger CHOP")
  * [Speed CHOP](<./Speed_CHOP.md> "Speed CHOP")
  * [Count CHOP](<./Count_CHOP.md> "Count CHOP")
  * the numerous operators that react to [Initialize and Start](<./Initialize_Start.md> "Initialize Start") pulses.


Operators like [OP Find DAT](<./OP_Find_DAT.md> "OP Find DAT") and [Folder DAT](<./Folder_DAT.md> "Folder DAT"), have callbacks that are called when conditions change. The callbacks can then change parameters and subsequently cause nodes to cook. 

[Pulse](<./Pulse.md> "Pulse") type parameters of operators can be pulsed using`OP.par._parname_.pulse()`. Custom Pulse type parameters can cause the pulse callback in a [Parameter Execute DAT](<./Parameter_Execute_DAT.md> "Parameter Execute DAT"). 

### Other Causes of Scripts Running

The Script operators ([Script CHOP](<./Script_CHOP.md> "Script CHOP"), [Script DAT](<./Script_DAT.md> "Script DAT"), [Script TOP](<./Script_TOP.md> "Script TOP"), [Script SOP](<./Script_SOP.md> "Script SOP")) are not event nodes - they are part of the pull system and will cook when TouchDesigner determines it depends on some other data in TouchDesigner - channels, parameters, table cells, extension properties, storage. 

When the event operators change parameters or other data, the target nodes will then cook according to the pull-system [cooking](<./Cook.md> "Cook") rules. 

**Note** : You can force a node to cook by calling`OP.cook()`. Its data is passed downstream according to the cooking rules. 

**See also** : [Cook](<./Cook.md> "Cook"), [Event CHOP](<./Event_CHOP.md> "Event CHOP"), [Procedural](<./Procedural.md> "Procedural")
