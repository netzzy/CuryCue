# Channel

A **channel** is a sequence of numbers (also known as [Samples](<./Sample.md> "Sample")) that can represent motion, control signals, MIDI, audio, color maps, rolloff curves or lookup tables. Channels can be [Exported](<./Export.md> "Export") to [Parameters](<./Parameter.md> "Parameter"). 

A [CHOP](<./CHOP.md> "CHOP") generated and outputs one or more channels. The group of one or more channels created by a [CHOP](<./CHOP.md> "CHOP") is called a Clip. A clip is what a CHOP outputs. 

Each channel of a CHOP has a channel name that can be set by the user. 

Channels are passed between CHOPs in TouchDesigner networks. 

A channel can also be [Exported](<./Export.md> "Export") to a [Parameter](<./Parameter.md> "Parameter") of any operator, overriding that parameter's value. 

### Channel Names

Channel names can contain numbers, English letters (A-Z a-z), and the special characters`-`,`_`,`:`, and`/`. Other characters will be automatically converted to`_`. 

Common practice is to use only lower-case letters for channel names and`_`. 

## See Also
* [Channel Class](<./Channel_Class.md> "Channel Class")
  * [CHOP](<./CHOP.md> "CHOP")
  * [Export](<./Export.md> "Export")
  * [Clip CHOP](<./Clip_CHOP.md> "Clip CHOP")
