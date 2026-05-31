# VST

Steinberg VST® (Virtual Studio Technology) is a proprietary standard for audio plug-ins that run on Microsoft Windows and Apple macOS, developed by [Steinberg Media Technologies](<https://www.steinberg.net/>). 

TouchDesigner supports VST3 plugins via the [Audio VST CHOP](<./Audio_VST_CHOP.md> "Audio VST CHOP"). TouchDesigner's implementation uses the [JUCE](<http://juce.com>) framework for VST3 plugins. 

[![VST Compatible Logo Steinberg with TM.png](./images/2/25/VST_Compatible_Logo_Steinberg_with_TM.png)](</File:VST_Compatible_Logo_Steinberg_with_TM.png>)

[](</File:VST_Compatible_Logo_Steinberg_with_TM.png> "Enlarge")

The VST standard has made it possible for hundreds of third-party software programmers to create and sell virtual instruments files that run on Windows and macOS computers in popular digital audio workstations (DAWs) and audio applications including Steinberg Cubase, Ableton Live, Logic Pro, Native Instruments, Bitwig and Audacity. 

VST3 plugins can be used within TouchDesigner using the [Audio VST CHOP](<./Audio_VST_CHOP.md> "Audio VST CHOP"). **VST2 plugins are not supported**. See the discussion on which VST plugins work well with TouchDesigner - [VST Plugin Testing](<https://derivative.ca/community-post/vst-plugin-testing/65712>)

VST3 plugins in TouchDesigner output multi-channel audio as [CHOP](<./CHOP.md> "CHOP") outputs, and optionally accept multi-channel audio as inputs (VST Effects vs VST Instruments). A CHOP can run at any sample rate, which is determined by the sample rate of the inputs to, in this case, the Audio VST CHOP. 

The plugins can also be controlled by MIDI messages via python functions on the [Audio VST CHOP](<./Audio_VST_CHOP.md> "Audio VST CHOP"). The VST plugin's user interface can be displayed and operated in a floating window. 

Built-in parameters of each plugin can be exposed as TouchDesigner operator parameters and populate the Plugin page. These parameters change when the UI is manipulated, and vice versa. These parameters can be [Exported](<./Export.md> "Export") to, or bound to other parameters using [Binding](<./Binding.md> "Binding"), or driven with expressions. 

[Palette:vstHost](<./Palette-vstHost.md> "Palette:vstHost") in the palette is a good framework to set up your VST environment. 

Audio is processed internally by the plugins with up to 64-bit precision. CHOP outputs and inputs are 32-bit floating point numbers. 

VST plugins run in-line with other CHOPs on the same CPU as the main TouchDesigner process. Middle-mouse click on the node to see the cook time. They are not run in a separate process. However, to offload processing or to assure low drop-out free latency, you can run any network of TouchDesigner operators, audio included, in a separate process using the [Engine Component](<./Engine_COMP.md> "Engine COMP"). You can stream control data, audio, images and data to the Engine COMP, process using any operators, and then drive audio outputs directly with the [Audio Device Out CHOP](<./Audio_Device_Out_CHOP.md> "Audio Device Out CHOP"). Alternately audio can be streamed back to the main process. 

VST® is a trademark of Steinberg Media Technologies GmbH, registered in Europe and other countries. 

**See also** [Audio VST CHOP](<./Audio_VST_CHOP.md> "Audio VST CHOP"), [VST Plugin Testing Community Post](<https://derivative.ca/community-post/vst-plugin-testing/65712>), [Palette:vstHost](<./Palette-vstHost.md> "Palette:vstHost"), [VST Virtual Studio Technology](<https://en.wikipedia.org/wiki/Virtual_Studio_Technology>)
