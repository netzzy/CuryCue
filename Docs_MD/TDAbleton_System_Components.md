# TDAbleton System Components

The **TDAbleton System Components** provide the real-time data to and from Ableton. To use these Components, simply copy them into your project from tdAbletonSystem. In general, they use CHOP channels to transmit data from Ableton Live and custom parameters for Component set up and also for transmission of data to Live. 

To use TDAbleton Components, you must first set up [TDAbleton](<./TDAbleton.md> "TDAbleton") properly. 

See also: [Creating Custom TDAbleton Components](<./Creating_Custom_TDAbleton_Components.md> "Creating Custom TDAbleton Components") and [TDAbletonCompBaseExt Extension](<./TDAbletonCompBaseExt_Extension.md> "TDAbletonCompBaseExt Extension")

## The`tdAbleton`Master Component

The **`tdAbleton`master component** maintains the communication between TouchDesigner and Ableton Live. It will be in a state of error if it is not connected to Live, so that you can easily know when TDAbleton is having connection problems. 

You will generally only interact with the master component through the`TDAbleton`custom parameter page. The following parameters are available: 
* **Help Page** : Opens the [TDAbleton](<./TDAbleton.md> "TDAbleton") wiki page.
  * **Update Ableton Comps** : this will [Update](<./TDAbleton.htm#Upgrading_TDAbleton> "TDAbleton") every TDAbleton component in your .toe file.
  * **Connect** : connects/disconnects from Ableton Live.
  * **Listen Only** : when on, TDAbleton will not allow outgoing changes to the Ableton Set.
  * **Report Duplicate Names** : control what kind of warnings are displayed when duplicate names are found in the Ableton Set. Duplicate names will cause problems in TDAbleton.
  * **In Port** : the UDP port number used by TouchDesigner to receive messages from Ableton.
  * **Ableton Address** : the IP address of the computer running Ableton Live. Also accepts "localhost".
  * **Ableton Port** : the port used by Ableton Live for receiving messages.
  * **Max Port** : the port used by TDAbleton Max devices for receiving messages.
  * **Ping** : for testing connection. Reports ping results in [Textport](<./Textport.md> "Textport").
  * **Open Console** : opens a simple Python console into the TouchDesigner Ableton Remote Script.
  * **Ableton Log File** : set this to allow easy access to the Ableton Live log file, where Remote Script errors are reported. See this [Ableton help page](<https://help.ableton.com/hc/en-us/articles/209071629-Where-to-find-Live-s-Crash-Reports>).
  * **Log TDA Debug Msgs** : when on, the TouchDesigner Remote Script will log extra debug information in the Ableton log file.
  * **Open Log File** : open the log file set up above.

## Common TDAbleton Component Features

Because TDAbleton Components are built on a common framework, they will almost always share the following features: 

#### CHOP output

Output from Ableton via TDAbleton Components is provided through a CHOP output. The channels names will provide source information. In certain cases there may be multiple outputs. Additional outputs are the result of customization. 

#### TDAbleton Parameter Page

This page holds information about the TDAbleton system as well as common utility parameters used by (almost) all TDAbleton Components. 

##### System Parameters

  *`**TDAbleton Comp**`: Location of the associated`tdAbleton`master component.
  *`**TDAbleton Version**`: The TDAbleton version number that this component has been [updated](<./TDAbleton.htm#Upgrading_TDAbleton> "TDAbleton") to.
  *`**[Update](<./TDAbleton.htm#Upgrading_TDAbleton> "TDAbleton")**`: If the`tdAbleton`master has a different version number from this component, this parameter will be enabled. Pressing Update will clone the Component from its clone source, update the version number, and do any other special tasks necessary for [update](<./TDAbleton.htm#Upgrading_TDAbleton> "TDAbleton").
  *`**Help Page**`: Opens this wiki page.

##### Utility Parameters

  *`**Connect**`: When on, connect this component to Ableton. When off, all Ableton listeners will be disabled.
  *`**Clear CHOP**`: Clears the standard output CHOP for this component. If a TDAbleton Component has other output CHOPs (e.g.`[abletonMIDI](<#abletonMIDI>)`), they will have their own clearing pulse parameters.
  *`**Strip CHOP Prefix Segments**`: Because CHOP channel names are automatic and can be long, this gives you the option of stripping off address segments. Of course, deeper customization can be achieved with a [Rename CHOP](<./Rename_CHOP.md> "Rename CHOP"), but this will generally be slower.
  *`**Timeslice OSC Chops**`: Turning timeslicing on causes CHOP output to cook constantly, but the cook time may be faster. Turning this off makes output only cook when data is incoming. Different settings will be better for different projects.
  *`**Send Only**`: When on, the component only sends control data to Live, it doesn't receive anything back. This turns off OSC inputs completely.

#### Live Object Model parameters

**Live Object Model parameters** are found on a TDAbleton Component's main parameter page. **Track** , **Device** , and **Parameter** custom parameters use the TDAbleton system to provide menu access to objects in your Ableton Set. In addition, the parameters **Chain 1-4** , **Chain 1-4 Device** allow deeper access into nested chains. Generally, only valid options will be available. The system will keep "Not Found" selections around until another option is selected. This "Not Found" state can happen if the object in Ableton is deleted, or if a Live Set is loaded that doesn't contain the given object. 

#### Auto Sync Parameters

On the page with Live Object Model parameters, you will usually find these **Auto Sync** parameters to help control outgoing data: 

  *`**Auto Sync Pars To CHOP**`: Many TDAbleton Components will have custom parameters whose values will be sent to Ableton. This parameter (when on) keeps those outgoing parameters synced to incoming values. Because this can decrease speed and in certain cases may create network echo, auto-syncing is optional. **Note:** when an Ableton value is changed by an outgoing TouchDesigner parameter, auto sync of that parameter will be disabled for one second.


  *`**Sync Pars To CHOP**`: When auto-syncing is off, the Sync parameter becomes available, which will do a one time synchronization of output parameters.

## TDAbleton Components

The following is individual information for each of the standard TDAbleton Components: 

### abletonSong

Provides access to the current **Ableton Live Set**. It provides big picture song info including timeline, scene, and cue point (a.k.a. locators, a.k.a. markers) data. It also provides an interface to the [TDA Master Device](<./TDAbleton.htm#The_TDA_Master_Device> "TDAbleton"). This component also provides callbacks for triggered scenes and passed cue points. **Note:** cue point callbacks and updates are only performed when the`Include Time Data`toggle is on. 

**Extra outputs** : 
* **`beatCHOP`** simulates the [Beat CHOP](<./Beat_CHOP.md> "Beat CHOP") operator
  * **`cuePoints`** is a table of cue point info
  * **`scenes`** is a table of scenes
  * **`currentCuePointName`** holds the nearest cue point to the left of the playhead


The`abletonSong`Component provides this function for controlling playback:`**FireScene(scene=None)**`Fire a scene.`scene`: if int, number of the scene to fire. If str, name of scene to fire. If None, scene selected in Scene To Fire parameter.`**StopAllClips()**`Stops all clips in the song. Note that the`[abletonTrack](<#abletonTrack>)`Component has control over individual clip playback.`**JumpToCuePoint(cuePoint)**`Jump to a selected cue point`cuePoint`: index or name of cue point to jump to.`**GetCuePointByName(name)**`→ **`Cue point info dict`**

    Get info about a cue point`name`: name of cue point

### abletonTrack

Provides access to the selected (via Track parameter) **Ableton Live Track**. Some of the custom output parameters may be disabled if the selected track does not have those features. This component is where you will find information about **clips** , **clipSlots** , and **arrangementClips** as well, including playhead position and loop points. This component provides callbacks when clips are triggered and playing. 

**Extra outputs** : 
* **`clips`** is a table of clip information for the track, including source files.
  * **`clip_status`** is a table showing triggered and playing clips
  * **`arrangement_clips`** is a table of arrangement clip information

##### Controlling Clips

The`abletonTrack`Component provides these functions for controlling playback of clips:`**FireClipSlot(index)**`Fires the clip at the given index.`**StopClipSlot(index)**`Stops the clip at the given index.`**StopAllClips()**`Stops all clips on the track. Note that the`[abletonSong](<#abletonSong>)`Component has a version of this function that will stop all clips in the song.

### abletonChain

Similar to **`abletonTrack`** Component, but allows access to nested **chains** , such as those in Ableton Racks and Drum Pads. Note that chains provide less information than tracks, due to more limited access through the Live Object Model. 

### abletonClipSlot

Provides access to Tracks' **clip slots**. Select a Track on the **Ableton Track** parameter page, then a clip slot on the **Ableton Clip Slot** page. This component provides callbacks when clips are triggered and playing. This component also has all functions of the abletonTrack component. 

**Extra outputs** : **`clips`** is a table of clip information for the track, including source files. **`clip_status`** is a table showing triggered and playing clips. When a midi clip slot is selected, the`**midiClip**`output gives a list of midi notes in the range named in the **MIDI Clip Time Range** and **MIDI Clip Note Range** parameters. 

#### Clip Functions

The`abletonClipSlot`Component provides these functions for working with clips:`**SetNotes(notes)**`Send a set notes command to the chosen clip.`notes`: a tuple of tuples in the form (pitch, time, duration, velocity, mute) 

    

    pitch: MIDI (0-127 int)
    time: Beat (0-4 float)
    duration: in beats
    velocity: MIDI (0-127 int)
    mute: 1 to mute, 0 to play`**RemoveNotes(timeStart, pitchStart, timeEnd, pitchEnd)**`Remove all notes that start in the given range. Time is in beats, pitch is in midi values (0-127)`timeStart`: Beat (0-4 float)`pitchStart`: MIDI (0-127 int)`timeEnd`: number of beats from timeStart to end of removal area (0-4 float)`pitchEnd`: number of notes from pitchStart to bottom of removal area (0-127 int)`**ClipCommand(command)**`Send this command to the selected clip.`command`: a string to be sent to the Live clip object in the form`<clip object>.<command>`For a list of clip commands, search for "Clip.Clip" at: 

    <http://julienbayle.net/PythonLiveAPI_documentation/Live9.6.xml>

### abletonDeviceParameters

Provides read-only access to all parameters on the chosen device. The **Parameters List** allows you to filter the device parameters if you don't want all of them. 

### abletonParameter

Provides access to the selected **Ableton Live Device Parameter**. The outgoing **Value Send** parameter will always be a float, no matter what type the value in Ableton is. 

### abletonMIDI

Provides input/output access to **MIDI events** occurring in Ableton by interfacing with the **TDA MIDI** Max for Live device. That device can be created in Ableton or by clicking the **Add TDA MIDI Device** parameter on the Component. 

##### MIDI Input

MIDI events are relayed from Live to TouchDesigner by the TDA MIDI device. It transmits all types of MIDI data including notes, control messages, program messages etc., all of which appear in the`abletonMIDI`CHOP output. For convenience, the last received midi note and the last received midi velocity is automatically tracked as well. 

Because MIDI events can happen more rapidly than TouchDesigner frames, there is a potential for loss of data when using CHOP channels. To this end, the`abletonMIDI`Component provides a single callback in its callback system:`onMIDIEvent`, which provides`address`and`args`in its info dictionary. These callbacks will correspond exactly to incoming MIDI CHOP data, but will never miss an event due to frame-rate. **TIP:** notes that are touching in Live will appear constantly on in incoming CHOP data. Use the **Split Touching Notes** toggle to artificially create a one frame space between them. 

The TDA MIDI device's name in Ableton is part of the channel names that are created. That name can be changed in Ableton or via the **Device Name** parameter. **Note:** the device's placement in a chain of devices does matter if MIDI data is altered by other devices. 

##### MIDI Output

MIDI events can be sent to the TDA MIDI device from TouchDesigner using Python. MIDI events sent to the TDA MIDI device will be reported back to TouchDesigner. In order to send a MIDI event, use the following`abletonMIDI`Component method: 

  *`SendMIDI (_type_ , _*data_)`Send a MIDI command to the connected TDA MIDI device.
    Arguments are a MIDI command string and 0-2 integer data items: 

  *`**note** <pitch value> <velocity>`*`**pressure** <aftertouch pressure> <pitch value>`*`**control** <control value> <controller number>`*`**program** <program change value>`*`**aftertouch** <aftertouch pressure>`*`**pitchbend** <pitchbend amount>`*`**channel** <MIDI channel>`*`**flush** (no arguments, stops all MIDI notes)`**Note:** pitchbend uses hi-res MIDI data -8192 to 8191

### abletonLevel

This component provides level data from Ableton Live by interfacing with the **TDA Level** Max for Live device. Levels are analyzed within the chain they appear in. This allows you to analyze the levels of individual tracks and sends or use the master track to analyze the song as a whole. Levels are measured within the chain, before track mixer levels are applied. Use the **Mix/Raw** settings to apply the mix for the device's track before level analysis. **Note:** the level device does not send full audio information, only the volume level it receives. 

#### Output modes

The **`abletonLevel`** component can interface with a single **TDA Level** Max device, or multiple devices within a rack. Choose which mode to use with the **Output** parameter. In either mode, the devices can be created within Live or by using the **Add TDA Level Device** and **Add TDA Audio Analyzer Rack** parameters, respectively. **Note:** while you can only use these parameters to add devices to Ableton tracks, not to sub-chains, you can work within sub-chains by placing the devices manually in Live and then pointing to them with your TDAbleton components. 

The rack mode is extremely useful for performing spectrum analysis. The default rack is a simple example, and has a typical low/mid/high arrangement using Live's EQ Three device. You are not limited to this, and within the rack you can use any Ableton Live filter or EQ device to choose frequencies, alter levels, or perform other operations to the audio before outputting levels to TouchDesigner. The`abletonLevel`Component will report data from all **TDA Level** devices in the rack's chains. 

### abletonRack

This component provides faster and more accurate OSC communication through the **TDA Rack...** Max for Live devices. It is also useful for controlling multiple Live parameters from TouchDesigner. The`abletonRack`Component uses Live racks, and specifically their **Macros** , to create sets of 16 deeply connected parameters. The best way to create the type of Rack that you want is by using one of the three pulse parameters: **Add TDA Audio Effect Rack** , **Add TDA Instrument Rack** , and **Add TDA MIDI Effect Rack**. You can also create the racks manually, but you will also have to manually add a **TDA Rack...** device (see below) and map its parameters to the rack's macros. **Note:** while you can only use these parameters to add devices to Ableton tracks, not to sub-chains, you can work within sub-chains by placing the devices manually in Live and then pointing to them with your TDAbleton components. 

The component will report the values of the Rack's macros in it's **CHOP output**. The channels prefixed with`rack`are coming directly from Max using OSC and are slightly faster and smoother than TDAbleton values that come from the MIDI Remote Script. The`abletonRack`Component also provides control of the Rack's Macros on the **`Macros`parameter page**. **Important** : When using TDAbleton Rack devices, do not use spaces in the Rack Macro names. TDAbleton cannot automatically correct this issue. 

The **Macro Variation** and **Recall Macro Variation** allow you to activate rack variations in Live. 

You can point an abletonRack device to any rack (not just ones with TDA Max devices in them) but some functionality will be unavailable. 

#### _TDA Rack..._ Max devices

The`abletonRack`Component uses the **TDA_Rack_OSC** and **TDA_Rack_MIDI_OSC** Max devices to send and receive information. These are pre-placed in the racks when you create them from TouchDesigner. For full functionality, one (and only one) of these devices must exist in one of the Rack's device chains. These Max devices have no functionality outside of Racks. 

Each Rack macro has a corresponding In and Out toggle on the rack OSC Max device. These control whether Ableton will receive data from and send data to TouchDesigner. 

#### Sending CHOP Data to Live Rack Macros

The`abletonRack`component has a **CHOP input** and an **OSC Input CHOP parameter** for sending data to the rack's macros in a highly efficient manner. Incoming CHOP channels will be mapped to receiving macros **in the order they appear in the CHOP**. If you want to change this order, you can fill the **Reorder parameter** with the channel names in the order you want them to be mapped. 

### abletonMapper

Similar to the TDA Rack devices, this component provides faster and more accurate OSC communication through the **TDA_Mapper** Max for Live device. It is also useful for controlling multiple Live parameters from TouchDesigner, but unlike the Rack system, it uses the Ableton Live Mapping system which allows you to control any parameter in your Live Set. To set up the`abletonMapper`Component, you will have to use the Live application to map the parameters you want to control. The best way to create the abletonMapper device is to use the **Add TDA Mapper Device** pulse parameter. 

**Note:** controlling parameters using this device does not add steps to **Live's undo stack**. This can be very useful when sending a constantly changing value from TouchDesigner. 

#### _TDA Mapper_ Max devices

The **TDA Mapper** Max device receives OSC data directly from TouchDesigner and assigns values to selected Live Parameters. To select a parameter to control, click a **MAP** button on the TDA Mapper device, then click the parameter you want to control in Live. To toggle control of the parameter between Live and TouchDesigner, click the button under the MAP button (it says either TD or Live). To unmap the parameter, click the **Unmap** button. 

The data coming from TouchDesigner should be normalized between zero and one, but you can scale the output mapping using the Min and Max values, which can be controlled within Live or TouchDesigner. 

#### Sending Data to TDA Mapper

The`abletonMapper`component has a **CHOP input** and an **OSC Input CHOP parameter** for sending data to the mapper in a highly efficient manner. Incoming CHOP channels will be mapped to receiving macros **in the order they appear in the CHOP**. If you want to change this order, you can fill the **Reorder parameter** with the channel names in the order you want them to be mapped. **Any values not controlled by input CHOP can be controlled using the`abletonMapper`Component's parameters on the`Map Values`page.**

### abletonValueListener

This component provides parameter access for creating listeners to anything in the Ableton Live Object Model. You can select LOM objects via the LOM parameters, then append to the created LOM expressions. You can also specify an OSC return address. **See also** : [Setting up listeners](<./Creating_Custom_TDAbleton_Components.htm#Setting_up_listeners> "Creating Custom TDAbleton Components")

This device also allows you to follow selections in Ableton Live via its **Follow Selection** parameter. Conversely, you can select objects in Live using the **Select LOM Object** parameter. You can also access this functionality in Python by calling abletonValueListener's **`SelectLOMObject(lomExpression)`** function. 

**Extra outputs** : 
* **`LOM Info`** a table of information about the LOM object currently being watched
  * **`stringFromAbleton`** when the **Output String Value** parameter is On, this DAT contains the string value of the LOM property currently being watched

### abletonComp

This component is a starting point for building custom TDAbleton Components. It does nothing on its own, but contains all the necessary operators including the [Live Object Model parameters](<#Live_Object_Model_parameters>) above. See [Creating Custom TDAbleton Components](<./Creating_Custom_TDAbleton_Components.md> "Creating Custom TDAbleton Components") for more information.
