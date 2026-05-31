# TouchEngine

TouchEngine allows other software packages to load TouchDesigner components from [.tox](<./.md> ".tox") files, process them, and pass data back and forth. 

TouchEngine is the core technology behind the [Engine COMP](<./Engine_COMP.md> "Engine COMP"), as well as the [Unreal Engine plugin](<./TouchEngine_For_Unreal_Engine_Plugin.md> "TouchEngine For Unreal Engine Plugin"). 

## TouchEngine API

The SDK, including documentation and an example project for Windows are available here: 

<https://github.com/TouchDesigner/TouchEngine-Windows>

and for macOS: 

<https://github.com/TouchDesigner/TouchEngine-macOS>

## Licensing

There is no licensing fee or royalty required to make use of TouchEngine within your software package. It can be included in any software package for free, and the feature becomes enabled by the end-user installing a paid TouchDesigner or TouchPlayer license on the machine (**Educational, Commercial,** or **Pro** , see [Licensing](<./Licensing.md> "Licensing") for details). Additionally TouchDesigner or TouchPlayer must be installed on the system to use TouchEngine. 

In TouchDesigner the [Engine COMP](<./Engine_COMP.md> "Engine COMP") works with any license including **Non-Commercial licenses**. 

## Implementations

### Derivative

**[Engine COMP](<./Engine_COMP.md> "Engine COMP")** \- The Engine COMP is a native component in TouchDesigner that loads .tox component files into a project yet runs them on a separate TouchEngine process. 

**[Unreal Engine Plugin](<./TouchEngine_For_Unreal_Engine_Plugin.md> "TouchEngine For Unreal Engine Plugin")** \- The TouchEngine For UE Plugin allows Unreal Engine users and developers to load TouchDesigner .tox files, process them, and pass data back and forth from within Unreal Engine. 

### 3rd-party

**[TouchPy](<https://github.com/IntentDev/touchpy>)** \- TouchPy is a high-performance toolset to work with TouchDesigner components in Python. By leveraging Vulkan, CUDA, and TouchEngine, TouchPy opens new pathways for integration, particularly with libraries such as PyTorch and Nvidia Warp. TouchPy supports GPU-to-GPU (zero-copy) data transfers, streamlining data exchange between standalone Python applications and Touchdesigner. 

**[SMODE](<https://www.smode.io/en/>)** \- SMODE is an integrated graphical compositing platform and media server. SMODE V10 introduces TouchEngine support allowing you to run a .tox component as a 2D layer object in SMODE. See documentation [here](<https://www.smode.io/documentation/ref/compo/integrations/tox-component.htm>). 

**[VDMX](<https://www.vidvox.net/>)** \- VDMX by VIDVOX is a fully customizable hardware accelerated layer-based video playground for macOS. VDMX6 introduces TouchEngine support combining the power of TouchDesigner with the flexibility of the VDMX6 interface. 

**[FFGLTouchEngine](<https://github.com/medcelerate/FFGLTouchEngine>)** \- An FFGL plugin that allows loading of TouchDesigner components (.tox files) into programs like [Resolume](<https://www.resolume.com/>). 

**[Screenberry](<https://screenberry.com/>)** \- A modular, powerful, multi-platform media server. [Read our blog](<https://derivative.ca/community-post/introducing-touchengine-and-front-pictures-screenberry-integration/64140>) about Front Pictures' integration of TouchEngine API. 

**[Hippotizer](<https://www.green-hippo.com/>)** \- Green Hippo media servers now support TouchEngine! [Read about it here](<https://www.green-hippo.com/about/partnerships/touchdesigner/>). 

**[LightAct](<https://lightact.com/>)** \- LightAct software and media servers now support TouchEngine.
