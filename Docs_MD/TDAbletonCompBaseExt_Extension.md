# TDAbletonCompBaseExt Extension

The **`TDAbletonCompBaseExt`** extension is a base class for [TDAbleton](<./TDAbleton.md> "TDAbleton") Components. It provides a structure and utilities for communicating with the TouchDesigner Python Remote Script in Ableton Live. 

Writing custom classes derived from`TDAbletonCompBaseExt`requires intermediate knowledge of Python, or at least object oriented programming. If you're not familiar with inheritance in Python, there are many tutorials online, [this one](<http://www.jesshamrick.com/2011/05/18/an-introduction-to-classes-and-inheritance-in-python/>) for example. 

See also: [TDAbleton](<./TDAbleton.md> "TDAbleton"), [TDAbleton System Components](<./TDAbleton_System_Components.md> "TDAbleton System Components"), [Creating Custom TDAbleton Components](<./Creating_Custom_TDAbleton_Components.md> "Creating Custom TDAbleton Components")

# Glossary

There are a few glossary items worth noting before diving in to **`TDAbletonCompBaseExt`**. 
1. **`LOM`** : The abbreviation`LOM`is often used to refer to Ableton's Live Object Model.
  2. **`lomPar`** : a TDAbleton custom parameter used to navigate the Live Object Model. Includes:`Track`,`Device`,`Chain1`,`Chain1device`,`Chain2`,`Chain2device`,`Chain3`,`Chain3device`,`Chain4`,`Chain4device`,`Parameter`3. **`song`** : In code, an Ableton Live "Set" is referred to as a`song`. This is true not only in TDAbleton, but also in Ableton's Live Object Model.
  4. **`aPar`** : An Ableton Live parameter. Because both TouchDesigner and the Live Object Model have a concept of "parameters", TouchDesigner uses`aPar`to distinguish the two. There are a few exceptions, such as the "Parameter" custom parameter on TDAbleton Components. (See how that's already a bit confusing?)

# Promoted vs. Non-Promoted Members`TDAbletonCompBaseExt`promotes (capitalizes) members that may be generally useful to things outside of the TDAbleton Component. Non-promoted members can always be accessed through the extension, e.g.`op('abletonComp').ext.TDAbletonCompBaseExt.startConnection()`. 

# Attributes

Not all attributes of`TDAbletonCompBaseExt`will be listed here, only the ones meant to be used in customization. Expert users can explore the`TDAbletonCompBaseExt`code inside the`abletonBase`Component for a deeper look. 

## Common Methods To Override

The following methods will be commonly overridden by custom TDAbleton extensions: 

#####`setupListeners()`Set up all listeners used by this Component. Will be called automatically at appropriate times by the TDAbleton system. You will generally want to call the base version at the beginning of your overriding method.

    This is often the only method you will need to override when creating a custom TDAbleton extension. See: [Setting Up Listeners](<./Creating_Custom_TDAbleton_Components.htm#Setting_up_listeners> "Creating Custom TDAbleton Components").

#####`onAbletonNotify(_info_)`Callback from`tdAbleton`master component with important events from Ableton Live.
    Override this to create custom reactions to TDAbleton system events. In general, you will want to call the base version of`onAbletonNotify`as well. For an example, see the`abletonMIDI`Component's custom extension. 

  *`info`: dictionary containing`notificationType`key and any other necessary info. Common`notificationType`s:
1. reinit:`tdAbleton`'s extension was reinitialized.
  2. connected: reconnected to Ableton.
  3. disconnected: disconnected from Ableton.
  4. songInfo: the`[SongInfo](<#SongInfo>)`object has been changed.
  5. lomNameChanged: a LOM object's name has been changed in Ableton. The`infoDict`contains the new`[SongInfo](<#SongInfo>)`entry for the changed object.
  6. locatorTimeChanged: a locator (aka cue point) time has been changed in Ableton. The`infoDict`contains the locator's updated`[SongInfo](<#SongInfo>)`entry.

#####`updateLOMPar(_lomPar, lomInfo_) → currentMenuLabel`Updates a Live Object Model parameter and returns the resulting menu label (object name) for`lomPar`.
    Override this to filter options available in LOM Parameters. Filter options by creating a new [OrderedDict](<http://docs.python.org/3/library/collections.html#collections.OrderedDict>) with only the options you want from`lomInfo`included. For an example, see the`abletonMIDI`Component's custom extension. 

  *`lomPar`\- the parameter being updated.
  *`lomInfo`\- the associated dictionary of available options.

#####`onOutputsChannelChange(_channel, value_)`An OSC output channel has changed
    Override this to react to changes in incoming values from Ableton Live. 

  *`channel`\- the name of the channel that changed.
  *`value`\- the new value of that channel.

## Commonly Used Methods

The following are the methods used most often in customizing TDAbleton extensions: 

#####`LomParInfo(_lomParName_) → infoDict or ...`Return infoDict for the LOM object selected in the given par, or a value (which evaluates to False) if there is a problem. The **infoDict** contains: 

    **`'lomInfo'`** :`[SongInfo](<#SongInfo>)`entry for LOM object selected in the named parameter.
    **`'lomExpression'`** : TDA Python expression to object
    **`'returnAddress'`** : Standard address for OSC replies from TDA
    The other possible return values for`LomParInfo`are:`**None**`: no such parameter`**0**`: parameter is disabled`**False**`: not-found object is selected in menu`**{}**`: 'None' is selected in menu

  *`lomParName`\- name of the parameter (e.g.`'Track'`)

#####`addListener(_listener, outPar=None, parMin=None, parMax=None, useBaseOSC=True_)`Add a listener. See: [Setting Up Listeners](<./Creating_Custom_TDAbleton_Components.htm#Setting_up_listeners> "Creating Custom TDAbleton Components"). You will generally want to call the base version at the beginning of your overriding method. 

  *`listener`\-`(lomExpression, property, returnAddress, id, extra=None)`. The`extra`element is an optional string with special instructions. If it is 'noinit', the initial value send will be skipped. This is useful for avoiding CHOP clutter when listening to a large number of channels.
  *`outPar`\- outgoing parameter for setting listener object
  *`parMir`\- outPar minimum value
  *`parMax`\- outPar maximum value
  *`useBaseOSC`\- if True, set up listener in built-in oscin. Set to False if you want to build your own oscin.

## Utility Methods

The following methods are often useful when writing custom TDAbleton extensions: 

#####`clearOSCIn()`Clear the main incoming data CHOP.

#####`requestRemoteData(code, callback, asRepr=False)`Request data from Ableton Python Remote Script shell by sending an evaluatable Python code string. Because this code must be sent and replied to via OSC, the return value must be reacted to in a Python callback. **Tip:** Works the same as if you had entered`code`in the [Ableton Console](<./Creating_Custom_TDAbleton_Components.htm#Development_Tools> "Creating Custom TDAbleton Components"), which is a good place to test your commands. 

  *`code`: evaluatable Python code
  *`callback`: the callback to call with return data as argument
  *`asRepr`: return data will be formatted by repr()

#####`runRemoteCode(code)`Runs`code`as Python code inside the TouchDesigner Remote Script (in Ableton). **Tip:** Works the same as if you had entered`code`in the [Ableton Console](<./Creating_Custom_TDAbleton_Components.htm#Development_Tools> "Creating Custom TDAbleton Components"), which is a good place to test your commands. 

  *`code`: executable Python code

#####`getMenuLabel(lomPar) → menuLabel`Return a`lomPar`menu label. This is useful because the`lomPar`menu labels correspond to LOM object names in Ableton. 

  *`lomPar`: the parameter to examine

#####`setMenuLabel(lomPar, label)`Set a`lomPar`to the index with the given menu label. 

  *`lomPar`: the parameter to set
  *`label`: the label to set menu to

#####`validChannelName(name) → validName`Return a valid [CHOP](<./CHOP.md> "CHOP") [Channel](<./Channel.md> "Channel") name based on a string. This is useful for setting up OSC return addresses that will be received by an [OSC In CHOP](<./OSC_In_CHOP.md> "OSC In CHOP"). 

  *`name`: the string to be converted into a valid channel name

## Members

The following are members of note when writing custom TDAbleton extensions: 

#####`Connected`**(Read Only)** True if this Component is connected to Ableton.

#####`OutCHOP`The [Out CHOP](<./Out_CHOP.md> "Out CHOP") that contains the default channel info for the Component. Inside the network, this is`out1`. This member is a shortcut for setting up [select CHOPs](<./Select_CHOP.md> "Select CHOP") that use this Component's output.

#####`OSCInCHOP`The [OSC In CHOP](<./OSC_In_CHOP.md> "OSC In CHOP") used to receive listener channels. In cases with a large number of listeners, efficiency may be increased by setting the`oscaddressscope`parameter to use wildcards instead of multiple specific scopes, which is the default. You can do this by overriding the`setupListeners`and/or`addListener`methods.

#####`OSCInDAT`The [OSC In DAT](<./OSC_In_DAT.md> "OSC In DAT") used to receive other listener information. In cases with a large number of listeners, efficiency may be increased by setting the`addscope`parameter to use wildcards instead of multiple specific scopes, which is the default. You can do this by overriding the`setupListeners`and/or`addListener`methods.

#####`FinalChainPar`The name of the last LOM Chain parameter with a valid chain selected. This can be 'Track', because an Ableton track is, for all intents and purposes, a chain with extra features.

#####`FinalDevicePar`The name of the last LOM Device parameter with a valid device selected. This can be 'Track'.

#####`SongInfo`The`SongInfo`object is a deeply nested [OrderedDict](<http://docs.python.org/3/library/collections.html#collections.OrderedDict>) containing all available information about the current Ableton Live Set. Note that the`SongInfo`object is keyed by Ableton names, which is why TDAbleton does not deal with identically named tracks or identically named devices on the same track. The SongInfo object should not be changed. **Do not attempt to print the SongInfo object to the clipboard!** It is large enough to cause TouchDesigner to hang for quite a while. If you want to look around in SongInfo, always print items'`.keys()`instead of the entire item. For example, you can type this in the textport:

_print(op.TDAbleton.SongInfo['scenes'].keys()_

    The`SongInfo`object has the following structure:
[code]
    """
    {
    	'name': '<song name as defined by TDA Master name>' or None,
    	'scenes': {
    		'<scene name>': { # scene info
    			'name': '<scene name>',
    			'tempo': scene tempo,
    			'index': '<scene index>',
    			'expression': '<LOM expression within parent>',
    			'ptr': LOM Pointer (not persistent across saves)
    		}
    		... all scenes
    	}
    	'cuePoints': {
    		'<cuePoint name>': { # cuePoint info
    			'name': '<cuePoint name>',
    			'time': cuePoint time,
    			'index': '<cuePoint index>',
    			'expression': '<LOM expression within parent>',
    			'ptr': LOM Pointer (not persistent across saves)
    		}
    		... all cuePoints
    	}
    	'tracks': {
    		'<track name>': { # track info
    			'name': '<track name>',
    			'index': track index (if applicable),
    			'expression': '<LOM expression within parent>',
    			'hasMIDIInput': True if track has MIDI input,
    			'hasMIDIOutput': True if track has MIDI output,
    			'ptr': LOM Pointer (not persistent across saves),
    			'parentInfo': info of object parent
    			'clipSlots': [
    				{ # clipSlot info
    				'index': <clip slot index>,
    				'expression': '<LOM expression within parent>',
    				'ptr': LOM Pointer (not persistent across saves),
    				'parentInfo': info of object parent',
    				'clip': {
    					'name': '<clip name>',
    					'filepath': '<clip file path>',
    					'ptr': LOM Pointer (not persistent across saves)
    				}
    				... all clipSlots
    			]
    			'devices': {
    				'<device name>': { # device info
    					'name': '<device name>',
    					'index': device index (if applicable),
    					'expression': '<LOM expression within parent>',
    					'ptr': LOM Pointer (not persistent across saves),
    					'parentInfo': info of object parent
    					'aPars': {
    						'<parameter name>': { # parameter info
    							'name': '<device name>',
    							'index': device index (if applicable),
    							'expression': '<LOM expression within parent>',
    							'ptr': LOM Pointer (not persistent across saves),
    							'min': minimum value,
    							'max': maximum value,
    							'value': value at time of dump
    							'parentInfo': info of object parent
    						},
    						... all parameters
    					},
    					'chainType': 'chains', 'drumpads', or ''
    					'chains': {
    						'<chain name>': {
    							# chain info (exactly like track info),
    						}
    						... all chains
    					}
    				},
    				... all devices
    
    				'# Mixer #': {
    					'name': '# MIXER #',
    					'index': None,
    					'expression': 'mixer_device',
    					'ptr': LOM Pointer (not persistent across saves),
    					'parentInfo': info of object parent
    					'aPars': {
    						'Crossfader': {
    							# parameter info (see above)
    						},
    						'Cue Volume': {
    							# parameter info (see above)
    						},
    						'Panning': {
    							# parameter info (see above)
    						},
    						'Track Activator': {
    							# parameter info (see above)
    						},
    						'Volume': {
    							# parameter info (see above)
    						},
    
    						'Send <send letter>' {
    							# parameter info (see above)
    						},
    						... all sends
    					},
    					'chainType: '',
    					'chains': {}
    				}
    			}
    			... all tracks
    		},
    		'Return: <return track name>': {
    			# track info (see above)
    		},
    		... all return tracks
    		'# Master Track #': {
    			# track info (see above)
    		}
    	}
    }
    """
    
[/code]
