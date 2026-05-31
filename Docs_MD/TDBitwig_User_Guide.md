# Introduction

[TDBitwig](<./TDBitwig.md> "TDBitwig") is a set of TouchDesigner components that enables bi-directional communication between [Bitwig Studio](<http://www.bitwig.com/>) and TouchDesigner. The [TDBitwig](<./TDBitwig.md> "TDBitwig") functionality enables users to create custom audio-visual performances by integrating real-time visuals with live audio output. 

For information about Bitwig Studio go here… (<https://www.bitwig.com/>) 

## NOTE

There was an oversight and we mistakenly included 2 extensions with Bitwig 5.1 and versions up to Bitwig 5.1.5. This oversight has been confirmed as fixed of Bitwig Version 5.1.6. If you are not able to update Bitwig to version 5.1.6, be sure the use the plugin version v1.1.12. 
* [![TouchDesigner OSC](./images/thumb/7/7e/BitwigControllersPage.png/441px-BitwigControllersPage.png)](</File:BitwigControllersPage.png> "TouchDesigner OSC")

TouchDesigner OSC 
* [![Bitwig OSC](./images/thumb/0/03/PluginVersion.png/700px-PluginVersion.png)](</File:PluginVersion.png> "Bitwig OSC")

Bitwig OSC 

# Overview

### Bitwig API

TDBitwig’s ability to read and control information in a Bitwig session relies entirely on the **Bitwig Studio Control Surface API**. The TouchDesigner controller script serves to extend the functionality of this API and achieve the full capability of the TDBitwig System. 

The Control Surface API is widely used to support a variety of hardware controllers like MIDI devices, and enables users to expand the level of interactivity in their recording and performance workflows. 

Much of the inspiration for the TDBitwig Controller extension comes from the well documented library of [Bitwig Studio controller scripts](<https://github.com/bitwig/bitwig-extensions>) as well as the [DrivenByMoss](<https://www.mossgrabers.de/Software/Bitwig/Bitwig.html>) extension collection written by Jurgen Mossgraber. 

### Open Sound Control (OSC)

The communication between TouchDesigner and Bitwig Studio relies on Open Sound Control (OSC), a message-based protocol using UDP. The use of OSC allows for communication between any number of devices on a network, and enables the TDBitwig System to send high-resolution data between separate devices running TouchDesigner and Bitwig Studio respectively. 

### System Design

The design for the TDBitwig System was largely motivated by the popular application of the Bitwig API to support hardware controllers. Similarly, the TDBitwig Component Set can be thought of as a collection of software-based controllers; each component communicates with it’s respective part of the Bitwig session and has its own set of buttons and sliders for controlling certain Bitwig parameters. What distinguishes software-based controllers from their physical counterparts is the increased ability to access and control Bitwig session information in a programmatic environment like TouchDesigner. 

# Getting Started

## Installation

**System Requirements:**
* Bitwig Studio Version 5.0.11 +
  * TouchDesigner 2022.35280 +

## Setup
1. Open **Bitwig Studio.**
  2. Setup your newly imported controller extension. 
     * Open _Dashboard_ → _Settings_ → _Controllers_ → _\+ Add Controller_
     * Choose Hardware Vendor : _Derivative._
     * Choose Product: _TouchDesigner._
     * Click _Add._
  3. Open **TouchDesigner.**
  4. In **TouchDesigner** , import the **bitwigMain** COMP. 
     * Open the TouchDesigner _palette._
     * Click on the _TDBitwig_ folder.
     * Drag the _bitwigMain_ COMP into your project.
  5. If you are using the system on one computer, a connection should be established at this point since the OSC ports are set to match by default. If you are working on 2 computers or wish to use different OSC port numbers, refer to the Configuring OSC section below.
  6. You can verify the connection status with the “connected” channel in the bitwigMain COMP’s OP view. If properly connected the value should be 1 and you can begin using the system. If a connection is not established, refer to the Troubleshooting section below.

### Custom Extension Installation

Bitwig Studio includes the Touchdesigner controller extension file in their Bitwig builds, so updates to that file will be timed with their minor releases. 

### Configuring OSC

You can locate the settings to configure your OSC connection in the following areas: 
* TouchDesigner: 
    * Click on the`bitwigMain`Component in your project,
    * In the **parameter window** , navigate to the **Setup** parameter page.
  * Bitwig Studio: 
    * Open the **Dashboard,** and in the **Settings** Pane, scroll to the **Controllers** Section.
    * You should see the controller settings for the **TouchDesigner** controller extension.
    * Make sure the **active icon** for the controller is **on** to view the settings window.
* [![TouchDesigner OSC](./images/thumb/c/c6/Bitwig_OSC_parameters.png/460px-Bitwig_OSC_parameters.png)](</File:Bitwig_OSC_parameters.png> "TouchDesigner OSC")

TouchDesigner OSC 
* [![Bitwig OSC](./images/thumb/5/5f/Bitwig_OSC_Settings.png/696px-Bitwig_OSC_Settings.png)](</File:Bitwig_OSC_Settings.png> "Bitwig OSC")

Bitwig OSC 


To properly setup your OSC connection, make sure of the following: 
* The`Bitwig IP Address`setting in TouchDesigner matches the **IP** address of the **device running Bitwig**
  * The`TouchDesigner IP Address`setting in Bitwig matches the **IP** address of the **device running TouchDesigner**
  * The`TouchDesigner In Port`number in TouchDesigner matches the`TouchDesigner Port`number in Bitwig
  * The`Bitwig Port`number in TouchDesigner matches the`Bitwig In Port`number in Bitwig


**Note:**

In Bitwig, you will need to restart the controller extension every time you change the`TouchDesigner IP Address`or`TouchDesigner Port`setting since they cannot be changed at run time. 

To restart the extension, de-activate and re-activate the controller by clicking the **power icon** in the top left of the controller window. 

## Troubleshooting

If you are experiencing any problems, the most useful tool for troubleshooting will be the **Textport**. Be sure to have it open while troubleshooting, as most errors will be reported there. 

The most common issues with TDBitwig will involve **connections**. The most important connection will be the network connection between the`bitwigMain`Component and the TouchDesigner controller extension in Bitwig. To test this connection, use the`Ping`parameter belonging to the`bitwigMain`Component, located in the **Debug** parameter page. Once pressed, you should see a “ping sent” message followed by a “ping reply received” message in the Textport. If the reply message does not appear, it may indicate that your OSC network is not configured properly or your device’s firewall is blocking the connection. 

The TouchDesigner controller extension in Bitwig is also equipped with a **Send Ping** button which will send a ping message to the specified IP and port. This functionality can serve useful for testing the connection from Bitwig to TouchDesigner. 

In addition to the ping test, all of the TDBitwig Components have a **Connect** parameter which can be used to manually reset connections. In the bitwigMain Component it is located in the **Setup** page, for all others it exists in the **TDBitwig** page. Toggling the parameter off and on will restart a connection and may reveal useful error messages indicating the problem. 

If connectivity issues persist, try closing your external text editor and any other sub-processes of TouchDesigner. For some reason, OSC ports can be associated with these sub-processes and the ports will not reopen until the applications are closed. Also, if two projects running TDBitwig are open and are using identical ports, it will cause port conflict issues. 

For more verbose descriptions of lower-level activity, you can enable the following parameters in the bitwigMain COMP: 

  1.`Log Messages`: print to Textport all incoming and outgoing OSC Messages
  2.`Debug Messages`: print to Texport information about calls to the python extension methods belonging to this Component. All TDBitwig Components come with this toggle and in most use cases will not be necessary.


Note: 

There is a 3rd party application called [Protokol](<https://hexler.net/protokol>), which provides a user-friendly OSC network checker. This may serve useful for network troubleshooting. 

# Component Concepts

## Cursors

The ability of Components to navigate Bitwig and select which object they are interested in (Track, Device, Clip Slot, or Parameter Page) relies on the concept of **Cursors**. In Bitwig, Cursors are used to point to a particular object, and there are different ways users can decide how a cursor selects an object. Any TDBitwig Component which communicates with a non-global Bitwig object has a corresponding cursor(s) within Bitwig. 

**Components using Cursors:**

Component | CursorTrack | CursorClip | CursorDevice | CursorRemoteControlsPage   
---|---|---|---|---`bitwigTrack`| ● | ○ | ○ | ○`bitwigClip`| ● | ● | ○ | ○`bitwigRemotesDevices`| ● | ○ | ● | ●`bitwigRemotesTrack`| ● | ○ | ○ | ●`bitwigRemotesProject`| ○ | ○ | ○ | ●`bitwigNote`| ● | ○ | ○ | ○   
  
One way to think about cursors is that if the object I am interested in **is** or **belongs to** a specific object, then I will use a cursor to select that object. For example, to access a specific device’s remote controls page, I will use the CursorTrack to select the track that the device belongs to, use the CursorDevice to select the device that the remotes page belongs to, then use the CursorRemoteControlsPage to select the remotes page. Note that the selection of objects via cursors will almost always begin by choosing the **Track** , with the exception of the bitwigRemotesProject, because the project remotes are global. 

### Cursor Navigation

**Pinning:**

By default, the cursor selection will follow whichever object is currently selected in the **Bitwig User Interface** unless it is **pinned**. The pinning functionality applies to **CursorTracks** , **CursorClips** and **CursorDevices**. If a Cursor Object is **un-pinned** , you can change the selection of the Cursor by clicking on the desired object in the Bitwig UI. 

Example: 

    Let’s say a CursorTrack is currently pointing to track “Instrument 2” and is **un-pinned.** If I click on “Instrument 1” in Bitwig Studio, my CursorTrack will **follow** the UI selection, and now points to “Instrument 1”.

If the Cursor is **pinned** , it’s selection will **not change** even if a different object is selected in the Bitwig UI. 

Going back to our example: 

    If a CursorTrack is currently pointing to track “Instrument 2” and is **pinned** ; if I click on “Instrument 1” in Bitwig Studio, my CursorTrack selection will **remain** , and still point to “Instrument 2”.

The use of pinning and un-pinning becomes a convenient way to select objects in TDBitwig by interacting with the Bitwig UI. The Component parameters`Pin Track`and`Pin Device`allow users to pin and unpin Cursors within TouchDesigner. 
* [![Cursor Track Navigation](./images/c/cd/CursorTrack_NavigationPars.png)](</File:CursorTrack_NavigationPars.png> "Cursor Track Navigation")

Cursor Track Navigation 
* [![Cursor Device Navigation](./images/f/f5/CursorDevice_NavigationPars.png)](</File:CursorDevice_NavigationPars.png> "Cursor Device Navigation")

Cursor Device Navigation 


**Scrolling:**

In addition to the pinning functionality, you can also use the scroll feature of Cursors to change their selection. The idea of scrolling is much more straightforward; cursors provide the ability to **select** the **next** or **previous** object based on the order in the Bitwig UI. 

In TDBitwig, this functionality is realized for CursorTracks with the`Prev Track`and`Next Track`parameters, or in the case of CursorDevices, the`Prev Device`and`Next Device`parameters. Pressing these will change the current cursor selection to either the previous or next object. 

## Observers

Observers (aka listeners) define which attributes belonging to a Bitwig object we are interested in. Each TDBitwig Component has a set of observers associated with it, which defines the attribute scope it has access to and can control. 

If an observer is active, any update to the attribute associated with that observer in Bitwig will trigger a callback that sends an OSC message to TouchDesigner informing the updated value. In the TDBitwig system, Component parameters are “linked” to observers, such that if an OSC message containing an updated value is received, it will change the parameter value to match the updated value from Bitwig. 

Conversely, when an update to a parameter occurs in TouchDesigner, a callback will send an OSC message to Bitwig containing the updated observed value, and the controller extension will update the Bitwig attribute associated with the observer accordingly. The use of observers allows for bi-directional control of parameters/attributes between the 2 applications in this way. 

## Limitations

Because Bitwig Observers cannot be added after controller **initialization** , we are limited to a **finite** number of **objects** we are observing as well as the **properties** of the object we are observing. This limitation is most relevant to the amount of Cursor Objects made available to the TDBitwig system, particularly the amount of CursorTracks and Project CursorRemoteControlPages. 

The system is designed such that any Component with Track Selection functionality has a one-to-one relationship with a CursorTrack. Therefore, the total number of these TDBitwig Components in a project will be limited to the number of CursorTracks available. The same relationship exists between the bitwigRemotesProject COMP and the Project CursorRemoteControlsPage. 

Currently the system supports: 

**256 CursorTracks** : 

    i.e. the **total** number of **`bitwigTrack`** , **`bitwigClipSlot`** ,**`bitwigClip`** , **`bitwigRemotesDevice`** , **`bitwigRemotesTrack`** , and **`bitwigNote`** COMPs may not exceed 256

**64 Project CursorRemoteControlsPages** : 

    i.e. the number of **`bitwigRemotesProject`** COMPs may not exceed 64

## Cursor Mapping

The correspondence between TDBitwig Object Components and their respective Bitwig Cursor is established by a mapping of the Component to the index of the Cursor it is listening to. When a Component requiring a Cursor is created, it will request a cursor index from the bitwigMain COMP; the bitwigMain COMP will find the next available Cursor and assign its index to the Object Component which made the request. This mapping allows the TDBitwig system to route incoming and outgoing information between TDBitwig Components and the Bitwig Objects they are communicating with. 

The Bitwig COMPs which use a Bitwig Cursor will have a Listener Index parameter representing the cursor index they have been assigned. This index will also exist as a header for the Out CHOP channels within the Component. Once a Component has been created and successfully assigned a cursor index, its mapping will never change as long as that Component Object exists. The only instances in which cursor mappings will change is when a new Component is created or a Component is deleted. 

# Component Set

## System Components

### [bitwigMain](<https://docs.derivative.ca/Experimental:Palette:bitwigMain>)
* [![BitwigMain TD.png](./images/thumb/0/03/BitwigMain_TD.png/1134px-BitwigMain_TD.png)](</File:BitwigMain_TD.png>)


**Description:**

The`bitwigMain`COMP serves as the **central communication** **hub** for the TDBitwig system, and is responsible for relaying most of the information between the Bitwig session and TDBitwig Object Components in a project. This COMP is necessary for every connection to a Bitwig Studio Session; for most use cases only **one** is required but there are real situations which may require more. 

The interaction with the Component will mainly pertain to connection configuration, users can locate the configuration settings in the Setup Parameter Page. A detailed explanation of the configuring process is provided in the above Configuring OSC section. Once connected, all the TDBitwig Object Components referencing this COMP will be enabled for use. 

Refer to the bitwigMain documentation page to find a detailed description of this Component and its parameters. 

### [tdBitwigPackage](<https://docs.derivative.ca/Experimental:Palette:tdBitwigPackage>)
* [![TdBitwigPackage Pars.png](./images/thumb/6/67/TdBitwigPackage_Pars.png/1077px-TdBitwigPackage_Pars.png)](</File:TdBitwigPackage_Pars.png>)


**Description:**

The`tdBitwigPackage`COMP allows users to **update** their TDBitwig Components in a project to the most recent released version. To bring your TDBitwig project up-to-date, locate this Component in the TouchDesigner _Palette_ , within the _TDBitwig_ folder. Drag this Component into your project, and press the _Update_ parameter located in the _About_ parameter page. Once pressed, all the existing TDBitwig Components existing in the current project will be updated to the version associated with the tdBitwigPackage COMP. 

## Object Components

### Common Features

The TDBitwig Object Components rely on a common framework, and therefore will share a set of common features. 

**Chop Output:**

The first (and sometimes only) output of the Object Components will be a CHOP Out. The CHOP will contain numeric data corresponding to the properties that the Component is listening to. Each property value will have its own channel, and the channel name will contain the type of object and name of the property that the value belongs to. Some Components have multiple outputs; these will be described in their respective sections. 

**TDBitwig Parameter Page:**

This parameter page will contain information and functionality pertaining to the TDBitwig system. 
* **`TDBitwig Comp`** : A reference to the Bitwig Main COMP
  * **`Connect`** : A toggle to manually enable or disable listeners associated with this COMP.
  * **`Debug Messages`** : Print information about extension method calls for the Component
  * **`Timeslice OSC Chop`** : A toggle to enable or disable time-slicing for the OSC In CHOP. When off, CHOP outputs will only cook when OSC messages are received. When on, CHOP outputs will cook constantly, but their cook time may be lower.
  * **`Strip CHOP Prefix Segments`** : Strip off the given number of address segments in the output CHOP channel names. This can help manage the length of the channel names and make them more simple to read.


**About Page:**

This parameter page will contain information and functionality pertaining to version and updates. 
* **`Help`** : Opens the Component documentation page
  * **`Version`** : The TDBitwig version that the Component is updated to
  * **`.tox Save Build`** : The TouchDesigner build version that the Component was saved in
  * **`Update`** : If the tdBitwigPackage COMP is present in the TouchDesigner project, pressing pulse will update the Component to the newest version


**Track/Device Navigation:**

Because many of the objects in Bitwig are associated with a track, users will commonly begin object navigation by selecting a track object, followed by the object belonging to the track (device, clip, remoteControlPage, etc.). For an in-depth explanation of object selection, read the Cursors section above. 

### [bitwigSong](<https://docs.derivative.ca/Experimental:Palette:bitwigSong>)
* [![BitwigSong outs.png](./images/thumb/4/4e/BitwigSong_outs.png/1127px-BitwigSong_outs.png)](</File:BitwigSong_outs.png>)


**Description:**

The`bitwigSong`COMP acts as a bi-directional interface for Bitwig’s **global transport** ; including timing, playback, and recording functionality. It also stores information about scenes and cues, and supports control for their playback. 

**Extra Outputs:**
* **beatCHOP** : simulates the Beat CHOP operator
  * **cueInfo** : a table of cueMarker info
  * **sceneInfo** : a table of scenes
  * **currentCueInfo** : provides info about the nearest cue marker left of the playhead


**Promoted Methods:**
* **`LaunchCue(cueIndex)`** :

Move playhead position to the specified cue and start playback`cueIndex`: integer index of the chosen cue to launch
* **`LaunchScene(sceneIndex)`** :

Start playback of all clips at the specified scene index`sceneIndex`: integer index of the chosen scene to launch


**Callbacks:**
* **`onCuePassed(info)`** :

The playhead location is on the cue marker’s position`**info**`: dictionary containing cue info`index`: index of cue`name`: name of cue
* **`onCueChanged(info)`** :

The nearest cue marker left of the playhead has changed`**info**`: dictionary containing cue info`index`: index of cue`name`: name of cue
* **`onPlay(info)`** :

Transport starts playback
* **`onStop(info)`** :

Transport stops playback
* **`onLoopStartPassed`** :

playhead location is on the loop start position

### [bitwigTrack](<https://docs.derivative.ca/Experimental:Palette:bitwigTrack>)
* [![BitwigTrack Pars.png](./images/thumb/2/29/BitwigTrack_Pars.png/1068px-BitwigTrack_Pars.png)](</File:BitwigTrack_Pars.png>)


**Description:**

The`bitwigTrack`COMP acts as an interface for accessing and controlling the attributes of a given Bitwig Track object. It allows users to choose the specific track they are interested in and perform any actions accordingly. 

### [bitwigClipSlot](<https://docs.derivative.ca/Experimental:Palette:bitwigClipSlot>)
* [![ClipLauncher Outs.png](./images/thumb/2/2e/ClipLauncher_Outs.png/955px-ClipLauncher_Outs.png)](</File:ClipLauncher_Outs.png>)


**Description:**

The`bitwigClipSlot`COMP serves as an interface for controlling clip slot playback and receiving playback information of all clip slots for a given track. Users begin by choosing which track they are interested in; from there they can access the clip slots associated with that track, and subsequently decide to perform actions on a specific clip slot. 

**Extra Outputs:**
* **clipInfo** : a table of clip slot information for the given track
  * **clipStatusInfo** : provides the current playing clip and current queued for playback clip


**Promoted Methods:**
* **`LaunchClip(clipSlotIndex)`** :

Launches clip at the specified index, playback behavior will depend on the Transport launch settings`clipSlotIndex`: integer index of the clip to launch
* **`SelectClip(clipSlotIndex)`** :

Selects clip at specified index in the Bitwig Clip Launcher Window`clipSlotIndex`: integer index of the clip to select
* **`StopClip(clipSlotIndex)`** :

Stops playback of clip at specified index. Behavior will depend on Transport launch settings`clipSlotIndex`: integer index of the clip to stop
* **`RecordClip(clipSlotIndex)`** :

Arms the clip for recording. If the Clip Slot is empty, a new clip will be created. Recording behavior will depend on Transport settings.`clipSlotIndex`: integer index of the clip to record


**Callbacks:**
* **`onPlayingClipChanged(info)`**

The current playing clip has changed`**info**`: dictionary containing clip info`index`: index of clip slot`name`: name of clip slot
* **`onQueuedClipChanged(info)`**

The current queued for playback clip has changed`**info**`: dictionary containing clip info`index`: index of clip slot`name`: name of clip slot

### [bitwigClip](<https://docs.derivative.ca/Experimental:Palette:bitwigClip>)
* [![ClipLauncher Outs.png](./images/thumb/2/2e/ClipLauncher_Outs.png/955px-ClipLauncher_Outs.png)](</File:ClipLauncher_Outs.png>)


**Description:**

The`bitwigClip`COMP serves as an interface for controlling clip playback and clip attributes in Bitwig’s clip launcher context. Users begin by choosing which track they are interested in; from there they can perform actions or read/modify the properties of a given launcher clip. 

### [bitwigRemotesDevice](<https://docs.derivative.ca/Experimental:Palette:bitwigRemotesDevice>)
* [![DeviceRemotes ControlsPar.png](./images/1/17/DeviceRemotes_ControlsPar.png)](</File:DeviceRemotes_ControlsPar.png>)
* [![Bitwig DeviceRemotes Page.png](./images/3/39/Bitwig_DeviceRemotes_Page.png)](</File:Bitwig_DeviceRemotes_Page.png>)


**Description:**

The`bitwigRemotesDevice`COMP serves as an interface for accessing and controlling **Device Remote Controls** in Bitwig. Navigation to controls begins by selecting a track, followed by the device within that track, and ending with the desired page. The 8 Remote Control Parameters on this Component will correspond to the 8 Remote Controls on a single page. 

### [bitwigRemotesTrack](<https://docs.derivative.ca/Experimental:Palette:bitwigRemotesTrack>)
* [![TrackRemotes ControlPars.png](./images/9/94/TrackRemotes_ControlPars.png)](</File:TrackRemotes_ControlPars.png>)
* [![Bitwig TrackRemotes Page.png](./images/4/42/Bitwig_TrackRemotes_Page.png)](</File:Bitwig_TrackRemotes_Page.png>)


**Description:**

The`bitwigRemotesTrack`COMP serves as an interface for accessing and controlling **Track Remote Controls** in Bitwig. Navigation to controls begins by selecting a track, followed by the desired page. The 8 Remote Control Parameters on this Component will correspond to the 8 Remote Controls on a single page. 

### [bitwigRemotesProject](<https://docs.derivative.ca/Experimental:Palette:bitwigRemotesProject>)
* [![ProjectRemotes TouchDesigner pars.png](./images/0/06/ProjectRemotes_TouchDesigner_pars.png)](</File:ProjectRemotes_TouchDesigner_pars.png>)
* [![Bitwig ProjectRemotes Page.png](./images/5/58/Bitwig_ProjectRemotes_Page.png)](</File:Bitwig_ProjectRemotes_Page.png>)


**Description:**

The`bitwigRemotesProject`COMP serves as an interface for accessing and controlling global **Project Remote Controls** in Bitwig. Navigation to controls begins by selecting the desired page. The 8 Remote Control Parameters on this Component will correspond to the 8 Remote Controls on a single page. 

### [bitwigNote](<https://docs.derivative.ca/Experimental:Palette:bitwigNote>)
* [![BitwigNote Pars.png](./images/thumb/1/15/BitwigNote_Pars.png/1191px-BitwigNote_Pars.png)](</File:BitwigNote_Pars.png>)


**Description:**

The`bitwigNote`COMP allows users to read a live stream of note events on a given Bitwig Track. The incoming notes will correspond to the track’s note input source, whether it be output from a midi device or side-chained from another track or device within Bitwig. Users will use the navigation controls to specify which track’s input source they want to monitor. 

**Callbacks:**
* **`onNoteEvent(info)`** :

A note event has occurred, includes note on, note off, or velocity change`**info**`: dictionary containing note event info`pitch`: pitch index of the note`velocity`: velocity of the note

## Auxiliary Components

### [bitwigSelect](<https://docs.derivative.ca/Experimental:Palette:bitwigSelect>)
* [![BitwigSelect Parameters2.png](./images/thumb/7/78/BitwigSelect_Parameters2.png/1242px-BitwigSelect_Parameters2.png)](</File:BitwigSelect_Parameters2.png>)


**Description:**

The`bitwigSelect`COMP enables users to retrieve channel information from the output CHOP of any Bitwig Object Component in a project. Component search can be filtered by the Object type, and once the output CHOP is selected, users can filter specific channels they are interested in. The selection of Components uses python references based on **relative** paths. Similarly to the application of the select OP, this Component creates a clean separation of data between the source and points of influence. 

**Relative Paths**

The`Select Relative To This Comp`parameter determines if the path used to reference the desired Object Component is relative to the bitwigMain Component or the bitwigSelect Component being used. Paths relative to the bitwigMain COMP will be stable when the location of this bitwigSelect COMP changes, but will break if the location of the selected COMP changes. Paths relative to the bitwigSelect COMP will break if the location of either the selected COMP or the bitwigSelect COMP changes, but will be easier to read and allows users to drag and drop the desired COMP into the 'Selected COMP' parameter. The choice between relative to bitwigMain or bitwigSelect will generally be a trade-off between stability and ease-of-use. 

**Channel Snapshot**

In the case of the bitwigNote COMP, there will be moments when the selected output CHOP is empty, particularly during connection processes on startup. This will cause errors in any references made to the channels which previously populated the output CHOP. To resolve this, the bitwigSelect COMP supports the ability to snapshot the current selected channels. Once snapshot, the output of the bitwigSelect COMP will remain on the snapped channels and will not be affected if the selected output CHOP is empty, keeping references to channels intact.
