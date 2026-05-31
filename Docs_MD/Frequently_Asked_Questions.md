# Frequently Asked Questions

**Q:** How much is TouchDesigner? Do I need to buy a license to use TouchDesigner? 

**A:** There are a number of different licenses available for TouchDesigner, you can read about the differences here [Licensing](<./Licensing.md> "Licensing"). If you are using TouchDesigner for non-commercial and personal purposes (you are NOT getting paid for your work with TouchDesigner), then you can use [TouchDesigner Non-Commercial](<./TouchDesigner_Non-Commercial.md> "TouchDesigner Non-Commercial") at no charge. All paying projects require purchase of a [Commercial](<./TouchDesigner_Commercial.md> "TouchDesigner Commercial") or [Pro](<./TouchDesigner_Pro.md> "TouchDesigner Pro") licenses from the [Derivative Store](<https://www.derivative.ca/shop/>). 

  
**Q:** What kind of graphics card (GPU) do I need for TouchDesigner? 

**A:** TouchDesigner runs on Nvidia Geforce and Quadro GPUs or AMD Radeon and FirePro GPUs. Recent Intel integrated graphics are supported but will have limitations due to the graphics requirements of TouchDesigner. See [System Requirements](<./System_Requirements.md> "System Requirements") for details. 

  
**Q:** What is the most ideal system I should buy for TouchDesigner? 

**A:** TouchDesigner runs on laptops, desktops, and rackmounts. You don't need to buy the fastest CPU, but CPU clock speed is more important than number of cores. Get the best Nvidia graphics card with the most graphics RAM you can afford. TouchDesigner can use a lot of CPU RAM, so get as much as possible. 

  
**Q:** Does TouchDesigner benefit from having multi-core CPUs in the system. 

**A:** Yes, there are quite a few parts of TouchDesigner that will use threading to off-load work onto extra CPUs. The most commonly used one is movie/audio reading and decoding, which is always done in separate threads. If you are playing high resolution movies the system will benefit greatly from having extra CPUs to do the decoding. Other things that benefit from multi-core CPUs are network communication and converting SOP data into a format that the GPU can understand. 

  
**Q:** Can I use live audio to drive TouchDesigner visuals? 

**A:** Yes, you can use live audio inputs and analyze the incoming signal to create control channels for your visuals, or you can have other audio programs send TouchDesigner raw OSC and MIDI events directly. If you use Ableton Live check out the bi-direction sync environment connecting TouchDesigner to Live called [TDAbleton](<./TDAbleton.md> "TDAbleton"). 

  
**Q:** What input devices can be used with TouchDesigner? 

**A:** See [Interoperability](<./Interoperability.md> "Interoperability"). MIDI is fully supported in TouchDesigner, so any MIDI device will work. Software and hardware devices can also connect to TouchDesigner through [OSC](<./OSC.md> "OSC") (Open Sound Control), UDP, TCP/IP, and/or serial communications. Other software like Ableton Live, apps on iOS and Android, and custom made applications can connect to TouchDesigner using these tools. There are also builtin operators for inputs from [Kinect](<./Kinect.md> "Kinect") sensors, [joysticks and gamepads](<./Joystick_CHOP.md> "Joystick CHOP"), [tablet and stylus](<./Tablet_CHOP.md> "Tablet CHOP"), and [multi-touch devices](<./Multi_Touch_In_DAT.md> "Multi Touch In DAT"). Serial devices like [Arduino](<./Arduino.md> "Arduino") can interface using the [Serial DAT](<./Serial_DAT.md> "Serial DAT") and/or [Serial CHOP](<./Serial_CHOP.md> "Serial CHOP"). 

  
**Q:** Can TouchDesigner output to multiple screens? 

**A:** Running your computer with two monitors allows two images to be displayed on two or more displays. Often the left monitor is a control panel and the right monitor(s) is a full-screen video output, at any resolution your hardware allows. 

The right monitor can be a wide view sent to 2 or display outputs, or splitters like DataPathFX4 and Matrox Dualhead2Go/TripleHead2Go devices each going to a different display or projector. This can also be used for left/right eye displays. The same TouchDesigner file can run on several computers at the same time, each with a different camera view, synced through TouchDesigner [TCP/IP](<./Touch_In_CHOP.md> "Touch In CHOP") pipes or [hardware frame-lock sync](<./Window_COMP.md> "Window COMP"), or both. 

  
**Q:** Does TouchDesigner support vertex, pixel, and geometry [shaders](<./Shader.md> "Shader")? 

**A:** Yes. [GLSL](<./GLSL.md> "GLSL") shaders are supported. macOS is limited to GLSL 4.1 while Windows OS is only limited by the graphic drivers you have installed. 

  
**Q:** Where can I find documentation for TouchDesigner? 

**A:** All documentation can be found here at [https://docs.derivative.ca](<./index.md>) and at <https://derivative.ca/UserGuide/Main_Page>.
