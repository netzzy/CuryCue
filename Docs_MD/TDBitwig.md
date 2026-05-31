# TDBitwig

TDBitwig is a set of TouchDesigner components that allow for communication between [Bitwig Studio](<./Bitwig.md> "Bitwig") and TouchDesigner. TDBitwig enables the creation of generative, immersive audio-visual performances and installations by combining the real-time audio processing capabilities of Bitwig Studio with the real-time 3D rendering capabilities of TouchDesigner. 

With TDBitwig, TouchDesigner can control Bitwig Studio parameters, such as tempo, track properties, clip launching, and device parameters. Conversely, Bitwig Studio can also control TouchDesigner parameters for creating tightly integrated audio and visuals. 

TouchDesigner is an interoperability platform that provides access to a wide array of hardware devices, APIs, the internet etc. Read about [TouchDesigner Interoperability](<https://derivative.ca/UserGuide/Interoperability>). Bitwig artists can interface with systems through TouchDesigner. Bitwig controlling TouchDesigner can operate as an advanced show controller for live theatre, environmental experiences and music performances. 

## Overview

The TDBitwig components are designed to enable users to control and manipulate various features of [Bitwig Studio](<./Bitwig.md> "Bitwig") from within TouchDesigner. These components provide a bridge between the two software platforms, allowing for seamless integration and communication via OSC messaging. 

## Installation
* Installation information can be found in the [TDBitwig User Guide](<./TDBitwig_User_Guide.md> "TDBitwig User Guide").

## Components

[Palette:tdBitwigPackage](<https://docs.derivative.ca/index.php?title=Palette:tdBitwigPackage&action=edit&redlink=1>): The entire toolset of TDBitwig components is provided with updating capability for deployed TDBitwig components. When an update for TDBitwig is released go the Palette and place tdBitwigPackage into your file and press Update button. All your deployed components will be updated automatically. Then delete the package when you finished as this package component is not required for operation. 

[Palette:bitwigMain](<https://docs.derivative.ca/index.php?title=Palette:bitwigMain&action=edit&redlink=1>): A singleton component that houses the Python extension responsible for communication with Bitwig Controller Java Extension via OSC protocol. You need only one of these components, and you need this component first to start using TDBitwig as it hosts the extension communication and OSC layer. 

[Palette:bitwigSong](<https://docs.derivative.ca/index.php?title=Palette:bitwigSong&action=edit&redlink=1>): A component that communicates with the main Bitwig transport and arranger. It has bidirectional access to all transport features like Play Stop BPM etc. It connects to the arranger timeline and supports callbacks for passed timeline cues. 

[Palette:bitwigTrack](<https://docs.derivative.ca/index.php?title=Palette:bitwigTrack&action=edit&redlink=1>): A component that communicates with the specified track object in Bitwig. Standard controls for Volume, Mute and Solo are bidirectional. A level channel receives the track amplitude envelope at control rate. 

[Palette:bitwigClip](<https://docs.derivative.ca/index.php?title=Palette:bitwigClip&action=edit&redlink=1>): A component that communicates with the specified track's clip. Permits the launching of the clipslot containing this clip, as well as bi-directional access to the clip's properties such as color, loop length, quantization, etc. 

[Palette:bitwigClipSlot](<https://docs.derivative.ca/index.php?title=Palette:bitwigClipSlot&action=edit&redlink=1>): A component that enables playback control of clip slots belonging to a specified track. Clip events are received as playing clipIndex channels and Python callbacks for playing, queued, and stopped clips. 

[Palette:bitwigNote](<https://docs.derivative.ca/index.php?title=Palette:bitwigNote>): A component that receives Note events as chop channels where each of the 128 notes has its own CHOP channel. By default only Note events that have triggered in the past are exposed. A python callback for onNoteEvent is generated for passing noteOn events and noteOff events. Note with velocity 0 is assumed as a Note Off event. 

[Palette:bitwigRemotesDevice](<https://docs.derivative.ca/index.php?title=Palette:bitwigRemotesDevice>)]: A component that communicates with Bitwig remote control pages. Remote control page banks are groups of UI elements that can be mapped to any parameter found in a device. Each remote page gives bidirectional control to device parameter. Remote control pages are groups of 8 parameters per page. Unused remote parameter slots in a Bitwig remotes page look like empty parameters in TouchDesigner. Used ones are dynamically matched to the label name of the controller name in Bitwig. 

[Palette:bitwigRemotesTrack](<https://docs.derivative.ca/index.php?title=Palette:bitwigRemotesTrack>): A component with identical function to the bitwigDeviceControls component dedicated to global track control of Bitwig parameters. Track parameters can be mapped to any parameter in any track in bitwig. This means any parameter in the device chain can be mapped to these global controls. This gives TouchDesigner global control of any selected set of parameter in any track, in groups of 8 controls per page. Unused remote parameter slots in a Bitwig remotes page look like empty parameters in TouchDesigner. Used ones are dynamically matched to the label name of the controller name in Bitwig. 

[Palette:bitwigRemotesProject](<https://docs.derivative.ca/index.php?title=Palette:bitwigRemotesProject>): A component with identical function to the bitwigRemotesDevice and bitwigRemotesTrack component(s) dedicated to global project control of Bitwig parameters. Project remote parameters can be mapped to any parameter in Bitwig. This means session wide, any parameter can be mapped to these global controls. This gives TouchDesigner global control of any selected set of parameter, in groups of 8 controls per page. Unused remote parameter slots in a Bitwig remotes page look like empty parameters in TouchDesigner. Used ones are dynamically matched to the label name of the controller name in Bitwig. 

[Palette:bitwigSelect](<https://docs.derivative.ca/index.php?title=Palette:bitwigSelect>): A component that enables users to retrieve channel information from the output CHOP of any Bitwig Component in a project. Component search can be filtered by the Object type, and once the ouput CHOP is selected, users can filter specific channels they are interested in. The selection of Components uses python references based on relative paths. 

## API and Communication Explained
* TDBitwig is a set of components that communicate with Bitwig using the [Bitwig Controller Extension API (Java)](<https://www.bitwig.com/support/technical_support/community-controller-extensions-and-scripts-29/>).
  * The OSC protocol is used to bidirectionally communicate with Bitwig and TouchDesigner.
  * bitwigComps bidirectionally communicates via OSC to an abstract general Bitwig cursor track object. This Bitwig object creates a generic interface through which TouchDesigner creates a durable, re-name-able, moveable connection. No word strings are used for mapping data. Instead, a fixed number of cursor objects are made available to TouchDesigner through which each bitwigComp connects to the desired Bitwig object through an automatically assigned cursor object. The connection to TouchDesigner is durable in the sense that the cursor object will persist as long as it is pinned and the TouchDesigner component is not deleted. If the TouchDesigner object is deleted, a new connection is easily recreated by adding a new Bitwig comp and pinning the scope of the TDBitwig component to the desired Bitwig user interface object.
  * TouchDesigner maps to individual parameters using a Bitwig page object that holds a fixed set of 8 customizable remote control/parameter slots. This offloads the mapping of parameters to the standard workflow in Bitwig. TouchDesigner can simply scope any Bitwig controller page and on the TouchDesigner side you will have direct access to the knobs in Bitwig via the corresponding parameter in TouchDesigner.

## TouchDesigner and Bitwig Grid

The Bitwig Grid device provides a pathway for passing audio and controller data at audio rates. This feature is powerful permitting an easy way for Bitwig and TouchDesigner to communicate in the audio rate domain both as an audio signal or control voltage (CV). This feature set is outside the scope of TDBitwig which works at controller rate via an OSC communication layer. The TDBitwig OSC protocol domain provides a framework to enable complete integration and bidirectional control of TouchDesigner and Bitwig via parameters, other user interface elements, clip events and note events. Meanwhile, Bitwig Grid and TouchDesigner’s CHOPs profide a procedural toolset for manipulating high-resolution audio and cv data.
