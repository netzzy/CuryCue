# MultiTouch

This page leads to multi-touch implementations with TouchDesigner. 

The [Palette:multiTouch](<./Palette-multiTouch.md> "Palette:multiTouch") component in the [Palette](<./Palette.md> "Palette") is an example of the multi-touch workflow to move objects in 2D. It is built around the [Multi Touch In DAT](<./Multi_Touch_In_DAT.md> "Multi Touch In DAT"). 

See the [Multi Touch In DAT](<./Multi_Touch_In_DAT.md> "Multi Touch In DAT") for Windows multi-touch. (Tested with [3M](<http://solutions.3m.com/wps/portal/3M/en_US/TouchSystems/TouchScreen/Solutions/MultiTouch/M2256PW/>)) 

See [TUIO](<./TUIO.md> "TUIO") to roll-your-own. 

See [iOS and OSC](<./IOS_and_OSC.md> "IOS and OSC") for various ways to get multi-touch data into from the Apple iOS devices. 

# Panels

A touch on a panel will as as a left mouse button event. This lets you used multiple panels such as buttons, sliders via multi-touch as they are. If a panel needs to handle more than one touch, you can disable the built in multi-touch behaviour via [Panel COMP Panel Page](<./Panel_COMP_Panel_Page.md> "Panel COMP Panel Page")'s Multi-Touch parameter, and then process the incoming touches to that panel via the [Multi Touch In DAT](<./Multi_Touch_In_DAT.md> "Multi Touch In DAT"). 

# Network Editor

The first touch in the [Network Editor](<./Network_Editor.md> "Network Editor") will act as a left mouse button event. Subsequent touches are ignored. 

# Limitations

The number of touches available is limited by hardware. 

Windows 7/8 only allows the use of one touch screen at a time.
