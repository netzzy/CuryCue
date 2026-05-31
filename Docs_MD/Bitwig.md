# Bitwig Studio

[Bitwig Studio](<http://www.bitwig.com/>) is a digital audio workstation (DAW) and music production software developed by [Bitwig](<http://www.bitwig.com/>). It offers both linear and non-linear workflows for sound creation, recording, live performance, and environmental audio. Bitwig Studio is designed to be a complete package for sound exploration and delivery of audio experiences. 

[![Bitwig Studio Logo RGB.png](./images/thumb/1/1a/Bitwig_Studio_Logo_RGB.png/300px-Bitwig_Studio_Logo_RGB.png)](</File:Bitwig_Studio_Logo_RGB.png>)

## Bitwig Integration with TouchDesigner

[TDBitwig](<./TDBitwig.md> "TDBitwig") is a set of TouchDesigner components that allow for communication between Bitwig Studio and TouchDesigner. The TDBitwig functionality enables users to create custom audio-visual performances by integrating real-time visuals with live audio output. 

See these useful resources: 
* [TDBitwig Announcement Article](<https://derivative.ca/community-post/68285>)
  * [TDBitwig User Guide](<./TDBitwig_User_Guide.md> "TDBitwig User Guide") \- concepts and getting started
  * [Bitwig Leaning Toolkit](<https://derivative.ca/community-post/introducing-tdbitwig-demo-learning-toolkit/68543>) \- a pre-made environment with TouchDesigner hooked into Bitwig illustrating numerous pathways between the tools
  * [Introduction to TDBitwig](<https://www.youtube.com/watch?v=k-3f0-Pmu-8&t=7268s>) video at the Berlin Roundtable October 2023.

## Key Bitwig Features
* Audio Mixing: Bitwig has a superior mixing bus for mixing sound.
  * Modulation System: The modulation system allows you to modulate any device, VST plug-in, parameter, in turn supporting bidirectional modulation of TouchDesigner parameters through [TDBitwig](<./TDBitwig.md> "TDBitwig").
  * Hardware Controller Integration: Bitwig supports a wide range of music creation and performance controllers, making it an ideal solution for controlling TouchDesigner through [TDBitwig](<./TDBitwig.md> "TDBitwig").
  * The Grid: The Grid is a modular sound design environment, sharing a modulation paradigm similar to both Analog FM Synthesis and TouchDesigner's CHOPs.
  * Sampler: Includes a powerful multisample editor.
  * Extensibilty with the Bitwig SDK: Bitwig supports a publicly available SDK for extending functionality with custom Java code.
  * Links... 
    * Bitwig Home. <https://www.bitwig.com/>.
    * Try Bitwig. <https://www.bitwig.com/download/>.
    * Overview. <https://www.bitwig.com/overview/>.

# TDBitwig

With [TDBitwig](<./TDBitwig.md> "TDBitwig"), TouchDesigner can control Bitwig Studio parameters, such as tempo, track properties, clip launching, and device parameters. Conversely, Bitwig Studio can also control TouchDesigner parameters for creating tightly integrated audio and visuals. 

TDBitwig enables the creation of generative, immersive audio-visual performances and installations by combining the real-time audio processing capabilities of Bitwig Studio with the real-time 3D rendering capabilities of TouchDesigner. With its ability to generate audio visual effects simultaneously, TDBitwig empowers artists to craft complex and captivating experiences that seamlessly blend sound and vision. 

Bitwig supports a wide array of [hardware controllers](<https://www.bitwig.com/support/technical_support/which-controllers-are-supported-in-bitwig-studio-28/>) for live performances and show control. TouchDesigner can connect with these audio-centric devices through TDBitwig. 

TouchDesigner is a visual programming tool for building interactive experiences, visualizations, generative 2D/3D art, user interfaces, and is used for education, VJing, basement prototyping and experimentation. TouchDesigner includes powerful tools for massaging data and controlling signals, interoperating and communicating with a wide range of physical devices, protocols and software tools, and driving video/audio/data to pro video cards, DMX, LEDs, projectors, screens, lasers, robotics, internet, web streaming, AR/XR/VR and more. Read about TouchDesigner [Interoperability](<./Interoperability.md> "Interoperability").
