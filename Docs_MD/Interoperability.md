# Interoperability

TouchDesigner supports a wide range of devices, protocols and external tools that interface via their respective [Operators](<./Operator.md> "Operator"), [Palette](<./Palette.md> "Palette") components, and TouchDesigner Python methods, known collectively as TouchDesigner's Interops. 

### Video Capture and Output Cards

[Blackmagic (SDI, ST2110, HDMI)](<./Blackmagic_Design.md> "Blackmagic Design") | [AJA (SDI, HDMI)](<./AJA.md> "AJA") | [Deltacast](<./Deltacast.md> "Deltacast") | [Bluefish](<./Bluefish444.md> "Bluefish444") | [Datapath](<https://www.datapath-us.com/>) | [DirectShow](<https://en.wikipedia.org/wiki/DirectShow>) | [Windows Media Foundation](<https://en.wikipedia.org/wiki/Media_Foundation>) | [NVIDIA Direct Display](<./Direct_Display_Out_TOP.md> "Direct Display Out TOP")

### IP Cameras

[IDS](<https://www.ids-imaging.us/>) | [Ximea](<https://www.ximea.com/>) | [Point Grey/Flir](<https://www.flir.com/>) | [Allied Vision](<https://www.alliedvision.com/en/>)

### Movie File Codecs

[Many codecs supported by FFMPEG](<./FFmpeg.md> "FFmpeg") | [H.266 H.265 H.264](<./FFmpeg.md> "FFmpeg") | [Hap, Hap Q, Hap R and Hap HDR](<./Hap.md> "Hap") | [NotchLC](<./Notch.htm#NotchLC_Codec> "Notch") | [EXR](<./Movie_File_In_TOP.md> "Movie File In TOP") | [Apple ProRes](<./Apple_ProRes.md> "Apple ProRes") | [AV1](<./AV1.md> "AV1") | [GoPro Cineform](<./GoPro_Cineform.md> "GoPro Cineform") | 

### Video Streaming

[Newtek NDI](<./NDI.md> "NDI") | [H.264 and HLS/DASH Streaming](<./Video_Stream_In_TOP.md> "Video Stream In TOP") | [RTMP and Enhanced RTMP](<./Video_Stream_Out_TOP.md> "Video Stream Out TOP") | [Syphon and Spout](<./Syphon_Spout_In_TOP.md> "Syphon Spout In TOP") | [WebRTC](<./WebRTC.md> "WebRTC") | [RTSP](<./RTSP.md> "RTSP") | [SRT](<./SRT.md> "SRT") | [NDI Stream from iPhone](<https://apps.apple.com/ca/app/ndi-camera-easy-streaming/id1477266080>) | [iPhone as macOS Video Device In](<https://www.engadget.com/mobile/smartphones/how-to-use-your-iphone-as-a-webcam-with-your-mac-164248242.html>) | 

### DMX-Based Protocols

[DMX](<./DMX.md> "DMX") | [Art-Net](<./Art-Net.md> "Art-Net") | [sACN](<./SACN.md> "SACN") | [FTDI](<./DMX.md> "DMX") | [KiNET](<./DMX_Out_POP.md> "DMX Out POP") | 

### Lasers

[EtherDream](<./Lasers.htm#EtherDream> "Lasers") | [Helios](<./Lasers.htm#Helios> "Lasers") | [ShowNET](<./Lasers.htm#ShowNET> "Lasers") | [LaserAnimation Sollinger AVB](<./Lasers.htm#LaserAnimation_Sollinger_and_AVB_Protocol> "Lasers") | [Pangolin Beyond](<./Lasers.htm#Pangolin_Beyond> "Lasers") | 

### Audio

[Steinberg VST](<./VST.md> "VST") | [ASIO](<./Audio_Device_Out_CHOP.md> "Audio Device Out CHOP") | [DirectSound](<./Audio_Device_Out_CHOP.md> "Audio Device Out CHOP") | macOS Core Audio | [Dante](<./Dante.md> "Dante") | [MP3, AIFF, WAV, AAC, OPUS, Vorbis, ALAC](<./File_Types.htm#Files_Imported> "File Types") \+ others | [LTC TimeCode](<./LTC_In_CHOP.md> "LTC In CHOP") | [Steam Audio](<./Audio_Render_CHOP.md> "Audio Render CHOP") | [WebRTC](<./WebRTC.md> "WebRTC") | 

### Digital Audio Workstations (DAWs)

[Ableton Live and TDAbleton](<./TDAbleton.md> "TDAbleton") | [Ableton Link](<./Ableton_Link_CHOP.md> "Ableton Link CHOP") | [Bitwig Studio and TDBitwig](<./Bitwig.md> "Bitwig") | 

### Camera-based Tracking

[Orbbec (Femto Kinect replacement)](<./Orbbec.md> "Orbbec") | [ZED depth and body-track](<./ZED.md> "ZED") | [Kinect Azure](<./Kinect_Azure_TOP.md> "Kinect Azure TOP") | [NVIDIA Face Track](<./Face_Track_CHOP.md> "Face Track CHOP") | [NVIDIA Body Track](<./Body_Track_CHOP.md> "Body Track CHOP") | [Leap Motion](<./Leap_Motion.md> "Leap Motion") | [Augmenta](<https://augmenta.tech/tracking-technology/>) | [NatNet OptiTrack](<./NatNet_In_CHOP.md> "NatNet In CHOP") | [BlackTrax](<./BlackTrax.md> "BlackTrax") | [PosiStageNet](<./PosiStageNet_CHOP.md> "PosiStageNet CHOP") | Vicon | [ZIG SIM Pro (Apple AR)](<https://apps.apple.com/ca/app/zig-sim-pro/id1481556614>) | 

### [LIDAR](<./LIDAR.md> "LIDAR") Scanners and Depth Cameras

[Hokuyo Scanner](<./Hokuyo_CHOP.md> "Hokuyo CHOP") | [Intel RealSense](<./RealSense.md> "RealSense") | [Ouster LIDAR](<./Ouster_TOP.md> "Ouster TOP") | [SICK LIDAR](<./SICK.md> "SICK") | [Leuze ROD4](<./Leuze_ROD4_CHOP.md> "Leuze ROD4 CHOP") | 

### ML Cameras

[Luxonis OAK-D ML Camera](<./OAK-D.md> "OAK-D") | 

### 3D Scene Data

[FBX](<./FBX.md> "FBX") | [Alembic](<./Alembic_In_POP.md> "Alembic In POP") | [OpenUSD](<./USD.md> "USD") | 

### Graphics Languages

[GLSL](<./Write_a_GLSL_Material.md> "Write a GLSL Material") | [Compute Shaders](<./Compute_Shader.md> "Compute Shader") | Vulkan | [CUDA](<./CUDA.md> "CUDA") | [C++ Custom Operators](<./Custom_Operators.md> "Custom Operators") | 

### Materials and Renderers

[Substance Designer](<./Substance_TOP.md> "Substance TOP") | [Notch](<./Notch.md> "Notch") | 

### Virtual Reality

[OpenVR](<./OpenVR.md> "OpenVR") | [Meta Quest and Oculus Rift](<./Meta_VR.md> "Meta VR") | [Steam Audio](<./Audio_Render_CHOP.md> "Audio Render CHOP") | 

### XR Tracking

[Stype camera tracking](<./Stype.md> "Stype") | [Mosys camera tracking](<./MoSys_CHOP.md> "MoSys CHOP") | [ FreeD](<./FreeD_CHOP.md> "FreeD CHOP") | 

### Physics and Dynamics

[Bullet Rigid Body Dynamics](<./Bullet_Dynamics.md> "Bullet Dynamics") | [NVIDIA FLow](<./Nvidia_Flow_TOP.md> "Nvidia Flow TOP") | [NVIDIA Flex](<./Nvidia_Flex_Solver_COMP.md> "Nvidia Flex Solver COMP") | 

### Network Protocols

[OSC](<./OSC_In_CHOP.md> "OSC In CHOP") | [TCP/IP](<./TCP/IP_DAT.md> "TCP/IP DAT") | [UDP](<./UDP_In_DAT.md> "UDP In DAT") | [WebRTC](<./WebRTC.md> "WebRTC") | 

### Web Browser and Web Tools

[Embedded Chromium/CEF Renderer and Browser](<./Palette-webBrowser.md> "Palette:webBrowser") | [WebSockets](<./WebSocket_DAT.md> "WebSocket DAT") | [Socketio](<./SocketIO_DAT.md> "SocketIO DAT") | [Web Server](<./Web_Server_DAT.md> "Web Server DAT")/[Web Client](<./Web_Client_DAT.md> "Web Client DAT") | [WebRTC](<./WebRTC.md> "WebRTC") | 

### Projection Mapping and Calibration

[MPCDI projection mapping file standard](<./MPCDI.md> "MPCDI") | [Scalable Displays](<./Scalable_Display_TOP.md> "Scalable Display TOP") | [kantanMapper](<./Palette-kantanMapper.md> "Palette:kantanMapper") | [camSchnappr](<./Palette-camSchnappr.md> "Palette:camSchnappr") | [projectorBlend](<./Palette-projectorBlend.md> "Palette:projectorBlend") | [(key)Stoner](<./Palette-stoner.md> "Palette:stoner") | [Lens Distortion](<./Lens_Distort_TOP.md> "Lens Distort TOP") | [Nestmap](<https://nestimmersion.ca/nestmap.php>) | [Vioso](<./Vioso.md> "Vioso") | 

### Unreal Engine and other Third Party TouchEngine Integrations

[Unreal Engine Plugin](<./TouchEngine-UE_Unreal_Engine_Plugin.md> "TouchEngine-UE Unreal Engine Plugin") | [TouchEngine](<./TouchEngine.md> "TouchEngine") | 

### Arduino

[Arduino](<./Arduino.md> "Arduino") | [Firmata](<./Palette-firmata.md> "Palette:firmata") | [Serial Ports](<./Serial_DAT.md> "Serial DAT") | 

### Controllers

[MIDI](<./MIDI.md> "MIDI") | [Joystick](<./Joystick_CHOP.md> "Joystick CHOP") | [3Dconnexion SpaceMouse](<./Geometry_Viewer.htm#3D_SpaceMouse_Navigation_Modes> "Geometry Viewer") | [ZIG SIM PRO (iPhone iPad data stream)](<https://apps.apple.com/us/app/zig-sim-pro/id1481556614>) | 

### Internet of Things

[MQTT IoT](<./MQTT.md> "MQTT") | 

### Python and Structured Data

[Python 3.11](<./Python.md> "Python") | [JSON](<./JSON.md> "JSON") | [XML](<./XML_DAT.md> "XML DAT") | 

### Timecode

[Timecode](<./Timecode.md> "Timecode")

### Multi-Touch

[Windows Multi-Touch](<./Multi_Touch_In_DAT.md> "Multi Touch In DAT") | [TUIO and TUIO2](<./TUIO.md> "TUIO") | [TouchOSC](<./TouchOSC.md> "TouchOSC") | [ZIG SIM PRO (iPhone iPad multitouch)](<https://apps.apple.com/us/app/zig-sim-pro/id1481556614>) | 

### Image, Color, Text

[Color Space Workflows](<./Color_Space_Workflows.md> "Color Space Workflows") | [OpenColorIO](<./OpenColorIO_TOP.md> "OpenColorIO TOP") | [Slug Font Rendering](<./Slug_Library.md> "Slug Library") | [live video from Photoshop](<./Photoshop_In_TOP.md> "Photoshop In TOP") | SVG ( [Web Render TOP](<./Web_Render_TOP.md> "Web Render TOP")) | 

### Licensing

[CodeMeter USB and Cloud Dongles](<./License_Dongle.md> "License Dongle") | 

_Edited November 2025_
