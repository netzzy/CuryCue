# TDAbleton

TDAbleton is a tool for linking TouchDesigner tightly with Ableton Live. It offers full access to most everything going on in an Ableton set, both for viewing and setting. The TDAbleton system contains a number of [components](<./Component.md> "Component") for 2 way communication, and a framework for building custom components and new features.   
  
TDAbleton operates through Ableton's MIDI Remote Scripts system and, when necessary, Max for Live (M4L) devices. Communication with TouchDesigner is via [OSC](<./OSC.md> "OSC") (using UDP). It is fully network-capable, so TouchDesigner can be running on a separate machine from Ableton. The Python in TDAbleton extensively uses Ableton's [Live Object Model](<#Navigating_your_Live_Set_using_the_Live_Object_Model>). Much of the groundwork for this Python interface is based on research done by [Julien Bayle's Structure Void](<https://structure-void.com/>). 

See also: [Ableton](<./Ableton.md> "Ableton"), [TDAbleton System Components](<./TDAbleton_System_Components.md> "TDAbleton System Components"), [Creating Custom TDAbleton Components](<./Creating_Custom_TDAbleton_Components.md> "Creating Custom TDAbleton Components"), and [TDAbletonCompBaseExt Extension](<./TDAbletonCompBaseExt_Extension.md> "TDAbletonCompBaseExt Extension")

### Common Ableton Tasks

The following is a list of commonly used data from Ableton Live and where to find it in TDAbleton. 
* **Scene** :`[abletonSong](<./TDAbleton_System_Components.htm#abletonSong> "TDAbleton System Components")`Component, channels`song/info/triggered_scene`and`song/info/last_started_scene`. Also available via callbacks.
  * **Time and Tempo Data** :`[abletonSong](<./TDAbleton_System_Components.htm#abletonSong> "TDAbleton System Components")`Component, channels`song/info/bars`,`song/info/beats`,`song/info/sixteenths`,`song/info/time`. **Note** : Include Time Data parameter must be`On`.
  * **Cue Points (a.k.a Timeline Locators)**:`[abletonSong](<./TDAbleton_System_Components.htm#abletonSong> "TDAbleton System Components")`Component property`LastLocatorPassed`. Also available via callbacks.
  * **Output Levels** :`[abletonTrack](<./TDAbleton_System_Components.htm#abletonTrack> "TDAbleton System Components")`Component, channels`.../output_meter_left`,`.../output_meter_right`,`.../output_meter_level`. **Note** : Due to a bug in Ableton Live Object Model, these are only updated when the meters are visible in the Ableton interface! Also, Include Audio Data parameter must be`on`.
  * **Track Slots** :`[abletonTrack](<./TDAbleton_System_Components.htm#abletonTrack> "TDAbleton System Components")`Component, channels`.../playing_slot_index`,`.../fired_slot_index`.
  * **Clips** :`[abletonTrack](<./TDAbleton_System_Components.htm#abletonTrack> "TDAbleton System Components")`Component, out_clips DAT output. When the **Include Playing Clip Data** parameter is on,`abletonTrack`'s CHOP output will also show clip time and loop information. To select specific clip slots, use`[abletonClipSlot](<./TDAbleton_System_Components.htm#abletonClipSlot> "TDAbleton System Components")`.
  * **Device Parameter Values** :`[abletonParameter](<./TDAbleton_System_Components.htm#abletonParameter> "TDAbleton System Components")`or`abletonChainParameter`Components.
  * **Control Ableton Parameters (without creating undo steps)** :`[abletonParameter](<./TDAbleton_System_Components.htm#abletonMapper> "TDAbleton System Components")`Component. Also [abletonRack](<./TDAbleton_System_Components.htm#abletonRack> "TDAbleton System Components") Component.
  * **MIDI Data** :`[abletonMIDI](<./TDAbleton_System_Components.htm#abletonMIDI> "TDAbleton System Components")`Component.
  * **MIDI Notes in a Clip** :`[abletonClipSlot](<./TDAbleton_System_Components.htm#abletonClipSlot> "TDAbleton System Components")`Component.
  * **Audio Levels and Audio Spectrum Analysis** :`[abletonLevel](<./TDAbleton_System_Components.htm#abletonLevel> "TDAbleton System Components")`Component. This includes level data on a per-track basis, and can be combined with filters to provide spectrum analysis.
  * **Sending/Receiving Rack Macro data**:`[abletonRack](<./TDAbleton_System_Components.htm#abletonRack> "TDAbleton System Components")`Component. This is also the smoothest way to receive parameter data.
  * **Ignore Parts of Your Ableton Live Set** : Large Sets can be slow to load and change when TouchDesigner is connected. To ignore parts of your set, use the TDA_Ignore and TDA_Ignore_MIDI devices in your tracks. Everything from these devices forward in the device chain will be completely ignored by TDAbleton.
  * **Access obscure Live Object Model features** : [abletonValueListener](<./TDAbleton_System_Components.htm#abletonValueListener> "TDAbleton System Components") Component.
  * **Get string data from Live** : [abletonValueListener](<./TDAbleton_System_Components.htm#abletonValueListener> "TDAbleton System Components") Component.
  * **Selected Tracks, Devices etc. in Live** : [abletonValueListener](<./TDAbleton_System_Components.htm#abletonValueListener> "TDAbleton System Components") Component.

#### TDAbleton 2.0 and up
* **Arrangement Clip Info** :`[abletonTrack](<./TDAbleton_System_Components.htm#abletonTrack> "TDAbleton System Components")`Component has channels and DAT outputs with info about clips in the arrangement.
  * **Rack Variations** :`[abletonRack](<./TDAbleton_System_Components.htm#abletonRack> "TDAbleton System Components")`Component.

## Getting Started

Note: **[(Link to TDAbleton Installation instructions for Versions prior to 1.23, or manual installation on separate computer.)](<https://docs.derivative.ca/index.php?title=TDAbleton&oldid=17862#Getting_Started>)**

#### System Requirements
* Ableton Live 11.1.5 and up
  * TouchDesigner 2021.20k+

##### System Requirements for TDAbleton 1.x (Live 9 & 10)
* Ableton Live 9.7.2 and up.
  * Max for Live 7.3.4
  * TDAbleton 1.x has been in TouchDesigner since version 099 2018.28070. Features may or may not work when moving TDAbleton versions backwards through older builds.

### Install the latest TDAbleton system

Make sure Ableton Live is closed before installing TDAbleton. **Note:** your Live install must have been opened at least once for the installation to work. 
1. Drag the tdAbletonPackage component into your TouchDesigner project from Palette>TDAbleton>Live 11+
  2. On the Utilities parameter page, use the **Ableton Live Install** menu to pick which Live version you want to install the system on.
  3. Click Install.


This sets up Ableton Live Remote Scripts and User Folders for standard installs of Ableton Live. If you have customized your Live install locations, you may have to set up the MIDI Remote Script Folder and Preferences Folder parameters yourself. Do this on the tdAbleton master component or on the tdAbletonPackage (leave the parameters bound). Instructions for finding the correct locations can be found [here](<https://help.ableton.com/hc/en-us/articles/209072009-How-to-install-a-third-party-Remote-Script>) for the remote script folder and [here](<https://help.ableton.com/hc/en-us/articles/209071629-Where-to-find-Live-s-Crash-Reports>) for the preference folder. If there are problems with the install, you should see popup dialogs that will give you instructions and a "Folder" button to open the necessary folders for manual copying/deleting. 

    **If the automatic install doesn't work, you can try the old manual installation method, found[here](<https://docs.derivative.ca/index.php?title=TDAbleton&oldid=17862#Getting_Started>). Be sure to check the links in the previous paragraph for instructions on where to install the Remote Scripts, as this has changed in recent Ableton Live versions.**

#### Set up Ableton Live
1. Open Ableton preferences (in the Options menu on Windows, and Live > Settings on macOS) and select the Link MIDI tab on left. In one of the **Control Surface** dropdowns, select TouchDesigner. Input and Output should be set to None.
  2. Reload your Live Set

#### Set up TouchDesigner and Confirm the Connection
1. If Ableton Live and TouchDesigner are running on the same computer, no additional network setup is necessary. If they are running on different computers, you must set TouchDesigner to connect to Live's address. On the **`tdAbletonPackage/tdAbleton`** Component, set the **Ableton Address** parameter to the network address of the computer running Ableton Live. The network address of the Live computer is displayed on the **TDA Master** Max device, which can be found (or dropped) on the Master track. The port parameters on the`tdAbleton`component should also match the port numbers on the TDA Master device.
  2. If the`tdAbleton`Component does not have a disconnected error flag, the connection is successful. (If you see error messages or are not connected, check the [Troubleshooting](<#Troubleshooting>) section below.)
  3. TouchDesigner will open a dialog asking you to add a TDA Master Device to your set. You can also use the **Add TDA Master Device** parameter on the`tdAbletonPackage/abletonSong`Component.


If this is your first time using TDAbleton, the best way to learn the basics is the [TDAbleton Feature Tour](<./TDAbleton.htm#TDAbleton_Feature_Tour> "TDAbleton")

### Upgrading TDAbleton

These are instructions for updating a previously installed TDAbleton. You will have to make changes to both Ableton Live and your TouchDesigner project. All TDAbleton components have a version number on their TDAbleton parameter page which you can check against the version numbers in the palette package. The latest update is always available in the TouchDesigner palette. 
1. Close Ableton Live
  2. Delete the`tdAbletonPackage`in your project. This will probably cause errors in your network until you finish this process.
  3. Follow the _[Install the latest TDAbleton system](<#Install_the_latest_TDAbleton_system>)_ instructions above.
  4. On the`tdAbleton`master component in`tdAbletonPackage`, go to the Utilities parameter page and click the Update All To <version> parameter. This updates all the TDAbleton components deployed in your project.
  5. Reopen your Ableton Live Set
  6. You may have to update your TDAbleton Max 4 Live devices. See below.

#### Updating TDA Max Devices

When you install a new version of TDAbleton, you may have to replace TDA Max devices stored locally in your Live Set. This happens when you use the Collect All and Save feature in Live, because it creates local copies of the devices. To make sure you have the proper versions of all TDAbleton Max 4 Live devices, do the following in your Live Set: 
1. Go to the Master Track of you Set and right-click on the top bar of the TDA Master device. Select **Manage Device File**. A window will appear on the right side showing all Max devices in your Set.
  2. TDAbleton Max devices are always prefixed with "TDA_". If any of these devices say "Current Project" or "Missing" in their location column, you should update them.
  3. **To Update A TDA Max Device:** drag the device with the corresponding name from the TouchDesigner User Folder in Live's browser (see image) onto the device on the right. This will replace it with the updated copy.


The three locations for TDA devices are: 
* TouchDesigner
  * TouchDesigner>TDA Project>Presets>Audio Effects>Max Audio Effect>Imported
  * TouchDesigner>TDA Project>Presets>MIDI Effects>Max MIDI Effect>Imported

## TDAbleton Feature Tour

The easiest way to learn the basics of TDAbleton is to explore the provided demo. To get started, run the **TDAbletonDemo.toe** file in the _**/Samples/TDAbleton/ <version>**_ folder (choose Browse Samples from TouchDesigner Help menu). In the same folder you'll find the **TDADemo Live Set** for Ableton Live. Inside that folder, open the **TDADemo Set.als** Ableton Set. Press play in Ableton Live and you should immediately see CHOP data moving in the TouchDesigner demo TDAbleton Components. If you don't, be sure you have properly set up Ableton Live (see [Getting Started](<#Getting_Started>)). 

#### The TDA Master Device

On the Master track of the TDADemo Set, you'll find the **TDA Master Max Device**. This device shows if Live is connected to TouchDesigner and allows you to apply some master settings for your Live Set. TouchDesigner does not have a way to access the file name loaded into Live, so the **Song ID** is provided as a numeric field you can use to identify your song. The name of your TDA Master device will be used as a text song name that is readable by TouchDesigner. The **Ableton Port** is the network port that will be used by the TouchDesigner remote script to receive messages from TouchDesigner. The **Max In Port** is the network port that will be used by TDA Max devices to receive messages from TouchDesigner. 

**Tip:** you can add a TDA Master device to a Live Set using the **Add TDA Master Device** pulse parameter on an`abletonSong`Component (see below). 

#### Anatomy of a TDAbleton Component

To look at the basic structure of a TDAbleton Component, we'll use **`abletonSong1`** as an example. 

##### Data from Ableton Live

You will notice that the data shown in the viewer reflects the current state of the Ableton Live Set. You can see a number of channels reflecting time data (e.g.`song/info/beats`) and a few others reflecting various states (e.g.`song/info/play`). Data coming in from Live is generally [CHOP](<./CHOP.md> "CHOP") data, and can be accessed by wiring from the TDAbleton Component, as has been done with the`nullSong`CHOP. Look in the parameters of the`circle1`SOP to see one way of using this incoming data. Some data from Live come in [DAT](<./DAT.md> "DAT") format, and can be accessed similarly from outputs. 

In certain cases, incoming data may also come via callback. Examples of this can be found in the`abletonSong1_callbacks`DAT. Python callbacks are beyond the scope of this guide, but if you know a little Python, looking in this DAT will reveal the examples which set the`locatorByCallback`and`sceneByCallback`textTOPs. 

##### Sending Data to Ableton Live

Data to be sent out to Ableton is usually sent via parameters. If you go to the **Ableton Song** parameter page of`abletonSong1`you will see the **Play** , **Loop** , and **Tempo** parameters which set the corresponding values in the Live Set. The`abletonChain1`component shows examples of using [CHOP exports](<./Export.md> "Export") to automatically change an outgoing parameter and thereby change a value in Live. 

These parameter values are kept up to date with incoming Live data only if the **Auto Sync Pars To CHOP** toggle is on. This option is provided because in certain cases Auto Sync can cause echoing changes between TouchDesigner and Ableton. 

#### Navigating your Live Set using the Live Object Model

The Ableton **Live Object Model** (or LOM) is an interface to all the aspects of an Ableton Live Set, including Tracks, Devices, Parameters, Scenes, etc. For detailed information about the Live Object Model, see: 
* [LOM Python Reference](<https://structure-void.com/PythonLiveAPI_documentation/Live11.0.xml>).
  * [LOM Python Reference](<https://nsuspray.github.io/Live_API_Doc/11.0.0.xml>) \- another version of the Python reference, with a more hierarchical interface.
  * [LOM Max For Live Reference](<https://docs.cycling74.com/max8/vignettes/live_object_model>) \- documentation for the Live Object Model in Max For Live, including a diagram of the relationship between all the objects.


For this section, we'll use`abletonParameter1`as an example. 

In the previous section,`abletonSong1`shows data for the entire Live Set. Most TDAbleton Components are made for observing particular parts of a Set. For example,`abletonParameter`is used to get and set the value of a single Ableton Device Parameter. As you can see in the Component's parameters, this one is set to work with _Track: 1 Muugy_ , _Device: Pitch_ , and _Parameter : Pitch_. In Ableton Live, navigate to that device and you will see that its Pitch value is being mirrored in TouchDesigner. 

TDAbleton uses menu parameters to navigate the Live Object Model. For example, all available Tracks, including Returns and the Master, will be shown in the **Track** parameter. Once you have selected a Track, its available Devices will be shown in the **Device** parameter, and so on down. To see other examples of this, take a look at the`abletonTrack1`Component, which observes a single Track, and the`abletonChainParameter1`Component, which gives access to Ableton Device Parameters within sub-chains such as those in an Instrument Rack. 

**Note:** You can change the Pitch value in Ableton by changing the **Value Send** parameter on`abletonParameter1`, but notice that this stops Ableton's automation of that parameter. This is another reason why **Auto Sync** is not always desirable. 

#### MIDI Data

The`abletonMIDI1`Component has a unique feature: a Max For Live device is necessary in order to get MIDI data out of Ableton Live. Each`abletonMIDI`component is connected to a specific **TDA MIDI** device in Live. If you look on the **1 Muggy** Track in the Ableton Set, you will see the TDA MIDI device. 

TDA MIDI devices in your Live set should be created from TouchDesigner by using the **Add TDA MIDI Device** pulse parameter on an`abletonMIDI`Component. Just select the Track to put it on and press that button. 

For more details about using TDAbleton MIDI features, see [abletonMIDI](<./TDAbleton_System_Components.htm#abletonMIDI> "TDAbleton System Components"). 

##### Incoming MIDI

The TDA MIDI device transmits MIDI data back to TouchDesigner, based on its position in its Track. In the image, for example, the changes in MIDI notes created by the _Pitch_ MIDI Device (just left of it in the Ableton Track) will be reflected in TouchDesigner. 

##### Outgoing MIDI

The TDA MIDI device can also be used to send MIDI commands to Ableton Live. To see this, use the`sendNote`button and the`pitchBend`slider next to the`abletonMIDI1`Component. 

#### TDAbleton Rack Devices

The smoothest way to control and watch Live's parameter values from TouchDesigner is using the`abletonRack`component, and its corresponding Max devices in live. These racks can be created in Live using the pulse buttons on the`abletonRack`component. For an example, look at the device chain in the "2 Muggy" Track in the Demo Set. 

The TDA Rack devices are Live presets that include standard Ableton Live Racks with a special Max device on the first chain that sends and receives data between TouchDesigner and the rack macros. In the image, this Max device is called "TDA_Rack_OSC". For the most part, you won't have to interact with this device, though it does have on/off controls for incoming and outgoing values. 

The general strategy for using these racks is to put the Live device whose parameters you want to control and/or watch into the rack. Then map the appropriate rack macros to the parameters you want to interact with. This will create a fast connection between those parameters and the corresponding abletonRack device. For more information, see [abletonRack](<./TDAbleton_System_Components.htm#abletonRack> "TDAbleton System Components"). 

## Using TDAbleton Package

In`tdAbletonPackage`, you will see the **`tdAbleton`** master Component on the top-left. This master component maintains the connection to Ableton Live and will generally not need to be altered once your connection is in place. 

The other **TDAbleton Components** provide the actual real-time data to and from Ableton. To use these Components, copy them into your project from`tdAbletonPackage`or drag them in from the TDAbleton>Live <version> folder in the Palette. In general, they use CHOP channels to transmit data _from_ Ableton Live and custom parameters for Component set up and also for transmission of data _to_ Live. For specific information about the Components see [TDAbleton System Components](<./TDAbleton_System_Components.md> "TDAbleton System Components"). 

The TDAbleton system also provides a number of features for creating your own custom Components. See **[Creating Custom TDAbleton Components](<./Creating_Custom_TDAbleton_Components.md> "Creating Custom TDAbleton Components")** for more information. 

#### Setting Up Your Project

As you have seen, TDAbleton uses a separate Component for each aspect of the Live Object Model that you want TouchDesigner to interact with. To set up all your observers, just copy as many [TDAbleton Components](<./TDAbleton_System_Components.md> "TDAbleton System Components") from`tdAbletonPackage`as you need and set them up appropriately. You can also drag TDAbleton components from the palette. As always in TouchDesigner, using [select CHOPs](<./Select_CHOP.md> "Select CHOP") for duplicate data will be more efficient than creating duplicate Components. 

#### Multiple TDAbleton Packages in One Project

If you want to connect to multiple Ableton Live sessions in a single TouchDesigner project, you will need a separate TDAbleton package for each session. Because TDAbleton uses a [global op shortcut](<./Global_OP_Shortcut.md> "Global OP Shortcut") you will need a utility to create your second instance. To change the shortcut, go to the Utilities parameter page of the package (or the tdAbleton component) and pulse the Change Global OP Shortcut parameter. Enter the new name in the dialog. 

This will change the shortcut on your package **and will also change the shortcut on all the TDAbleton components inside the package**. You can now copy those components into your project and they will be connected to this package. **TDAbleton components from the palette will no longer be connected to this package**. 

## Caveats and Gotchas
* **Most Importantly:** the system will be confused by tracks with **duplicate names** and devices with duplicate names on the same track or in the same chain. In some cases, this is also true of names that are the same after being converted to valid TouchDesigner [Channel](<./Channel.md> "Channel") names. TDAbleton will pop up a warning dialog if it finds duplicate names, and will give an option to automatically rename duplicates. This behavior can be controlled using the`tdAbleton`master Component's **Report Duplicate Names** parameter.
  * **Automatic Ableton Track Names with "#" in them** can cause some problems because Ableton does some strange renaming stuff behind the scenes. The best solution is to just rename your tracks without using the # character.
  * **Live Set is too large:** massive Live Sets can cause connection problems and overload the OSC connection, especially on Macs. This can often be avoided by using the **TDA_Ignore** and **TDA_Ignore_MIDI** max devices wherever possible. Anything after these devices in a device chain will be ignored by TouchDesigner.
  * **Duplicate VST effects in the same chain** are particularly nasty, because VST effects cannot be renamed. The auto-fix features will fail and you cannot rename the effects manually. There are two solutions for this. If you don't want to control/watch the effects in TouchDesigner, you can just ignore them by placing a **TDA_Ignore** Max device before them in the chain. All devices after the **TDA_Ignore** will be ignored. If you do want to control/watch the effects in TouchDesigner, place each one inside an effect rack. TDAbleton's abletonRack components will work particularly well for this.
  * **TDAbleton M4l devices on the same track** (e.g. TDA_MIDI and TDAbleton Racks) will need different names to broadcast properly from Max.
  * **If Ableton Live objects are renamed when TDAbleton is not connected to Live** , the connections will be broken when TDAbleton is reconnected. Connections will be maintained properly if renaming occurs while TDAbleton is connected.
  * Ableton parameters that are selected via Comp menus will always report their data as float values, even if they are integers in Ableton.
  * When using the **TDAbleton Rack devices** , you can't use spaces in **Macro names**.
  * **Ableton parameters that are being controlled by TouchDesigner** are not disabled in the Ableton interface, as is common when a value is being controlled by another value. Once TouchDesigner has altered an Ableton parameter value, that value's Ableton automation can only be restored in the Ableton interface. **Important** : changing Ableton values from TouchDesigner will create Undo steps in Ableton, which can destroy your ability to undo if a value is constantly streaming into Live. You can avoid this by using the TDAbleton Rack devices.
  * The **last_started_scene** channel on **abletonSong** components is a best guess. Ableton live does not provide this information directly, it only provides **triggered_scene**. The main problem is that multiple manual triggering of scenes in the Live interface will confuse last_started_scene.

## Troubleshooting

Because TDAbleton is linked to Ableton Live's Python Remote Scripts via OSC and the Python Remote Scripts are linked to the Ableton app through a lower-level system, troubleshooting can be a bit tricky. If you are having problems, your most important tool is the **[Textport](<./Textport.md> "Textport")**. Be sure to have it open while troubleshooting, as most errors will be reported there. 

The most common issues with TDAbleton will have to do with **connections**. The simplest connection test is the **Ping** parameter on the`tdAbleton`master. Press that and you should see a response in the textport. If not, you may have incorrect address or port settings on`tdAbleton`. All TDAbleton Components, including the master, have a **Connect** parameter. Toggling that on and off will reset the connection and will often print useful error messages as to the problem. 

**If you are not connecting** make sure that the Ableton Port (on the TDA_Master device on your Live master track) matches the Ableton Port parameter (on the tdAbleton component in TouchDesigner). If those are matching, you may have an OSC conflict with something else running on your system. Change them both to a different matching number. Unfortunately there is no way to tell if an OSC port is taken, so this must be done by trial and error. 

**If you are still not connecting** try closing your external text editor and any other sub-processes of TouchDesigner. For some reason, OSC ports can be associated with these sub-processes and the ports will not reopen until the applications are closed. 

TDAbleton will attempt to transmit any errors from the TouchDesigner Remote Script to the textport. In most cases this will be sufficient, but sometimes it may be necessary to look at the **Ableton log file**. There are Log file helper parameters on the Utilities page of the`tdAbleton`component. To find your log file, see the **Ableton Log File parameter** on the Utilities page of the tdAbletonPackage component. 

**Tip:** the Log TDA Debug Msgs parameter turns on and off verbose debugging in Ableton's log file. If this parameter is off, only errors and the most basic information will be put in the Ableton log. 

TouchDesigner Build: Latest\nwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditormw-undomw-undomw-undomw-rollbackmw-revertedmw-manual-revert2022.280402022.265902022.241402021.100002020.220802020.200002018.28070before 2018.28070
