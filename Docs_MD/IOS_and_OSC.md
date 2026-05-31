# IOS and OSC

The Apple [iPad](<http://www.apple.com/ipad/>), [iPhone](<http://www.apple.com/iphone/>) and [iPod Touch](<http://www.apple.com/ipodtouch/>) can be used as an input devices to TouchDesigner. 

Several iOS apps allow you to build control panels of sliders and buttons on the iPhone, or have available pre-existing control panels. When the panels are operated on the iPhone, it sends the slider/button data over wireless TCP/IP using the [OSC](<./OSC.md> "OSC") protocol. It is received by the [OSC In CHOP](<./OSC_In_CHOP.md> "OSC In CHOP") and the [OSC In DAT](<./OSC_In_DAT.md> "OSC In DAT"). 

This page is a compilation of knowledge accumulated about various applications. For many purposes, these iOS apps replace the function of [MIDI](<./MIDI.md> "MIDI") input devices, if you don't mind the absence of physical tactile feedback. 

Aside from the applications listed below that generally let you set up and use custom control panels of sliders and buttons on the iPhone, numerous others apps simply output application-specific data (such as game states) via OSC. 

In the Apple App Store, search for "OSC" and "Open Sound Control". 

## Common Setup

Setting it up with TouchDesigner is super-easy. 

Each iOS app involves setting the wireless IP address of your TouchDesigner computer, and a port number (any number you choose). 

First, get your wireless IP number in Windows Control Panel -> Network and Sharing Center -> Wireless Network Connection -> Details... 

Enter that in the iOS app's settings. 

Then on the TouchDesigner side, simply lay down an [OSC In CHOP](<./OSC_In_CHOP.md> "OSC In CHOP"), change the Network Port parameter to the port number you chose above, and start using the iOS app control panels. Channels in the CHOP will be created as you press new controls. 

You can also (at the same time) lay down an [OSC In DAT](<./OSC_In_DAT.md> "OSC In DAT") to see the raw messages come in via a first-in first-out table. 

## iOS Apps

## TouchOSC

<http://hexler.net/touchosc>

[TouchOSC](<./TouchOSC.md> "TouchOSC") lets you define 1D and 2D sliders and toggle/momentary buttons in a text file. It also sends 3 accelerometer channels. 

Aside from pre-made control panels, you can download a Windows or OSX editor to make custom panels. 

Error in [widget YouTube](<./Widget-YouTube.md> "Widget:YouTube"): unable to write file /var/www/html/extensions/Widgets/compiled_templates/wrt6863ca43c2dc15_87767043

Error in [widget Vimeo](<./Widget-Vimeo.md> "Widget:Vimeo"): unable to write file /var/www/html/extensions/Widgets/compiled_templates/wrt6863ca43c40469_40968557

## ZIG SIM

ZIG SIM can capture the data from any sensor on your phone and send it to TouchDesigner via OSC. 

SIG SIM Pro also includes [NDI](<./NDI.md> "NDI") transmission of video from the phone's camera and AR support through ARkit. 
* [ZIG SIM iOS](<https://apps.apple.com/us/app/zig-sim/id1112909974>)
  * [ZIG SIM Android](<https://play.google.com/store/apps/details?id=com.oneten.drive.zig_sim&hl=en_CA>)
