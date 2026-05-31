# Wacom Intuos Tablet

[Wacom Intuos](<http://www.wacom.com/intuos/>) pen tablets have long been a favorite input device for TouchDesigner artists. 

The Intuos4 tablets are the most recent series offered by Wacom. Their primary advantage over the previous models is that the new pen sensor now offers 2048 levels of pressure sensitivity, allowing for much smoother interactions. 

We recommend installing the latest Intuos4 hardware drivers for any Intuos tablet. The Intuos4 software will work with previous generations and offers all the most recent software features. The software can be found here: [Wacom Intuos Drivers](<http://www.wacom.com/downloads/drivers.php>)

## Using the Tablet in TouchDesigner

The [Tablet CHOP](<./Tablet_CHOP.md> "Tablet CHOP") allows most of the pen and tablet inputs to be captured in [CHOP](<./CHOP.md> "CHOP") channels. It can track 1 or 2 pens on the same tablet, and channels are provided for x,y coordinates, pressure, tilt, and up to 5 auxiliary buttons. T 

The Wacom mouse can also be used on the tablet and there are channel available for the scrollwheel and rotation of the mouse. 

## Setup Options

Options for the tablet are set in the **Wacom Tablet Properties** dialog in the **Control Panel**. 

### Pen Buttons

Since TouchDesigner requires a 3-button mouse, the default pen buttons are not well suited to working in the [Network Editor](<./Network_Editor.md> "Network Editor"). We find it useful to remap the rocker Duoswitch to use Middle Click and Right Click. With this change you get all 3 mouse-buttons at your fingertips. 

### Pressure Mapping

The Wacom software for the Intuos4 now has an option that effects pressure mapping in the Tablet CHOP. Click on the **Options** button in the Wacom Tablet Properties dialog. There is a checkbox to turn on/off **Pressure Compatibility**. 

When this is on, the pressure channel ranges from 0-1 in the Tablet CHOP, however it only samples 1024 pressure levels. 

When this option is off, the pressure channel ranges from 0-32, and all 2048 pressure levels are sampled (assuming you are using an Intuos4. This give you much more sensitivity with the pressure of the pen, but may require re-normalizing your channel values to the 0-1 range with a [Math CHOP](<./Math_CHOP.md> "Math CHOP"). 

### TouchDesigner UI Options

Since the pen and tablet are so sensitive, it is often hard to perform a single click, right click, or double-click when working in the [Network Editor](<./Network_Editor.md> "Network Editor"). The problem is that if the pen moves at all while clicking or right-clicking, then TouchDesigner will consider it a drag, not a click. When double-clicking, TouchDesigner doesn't register a double-click if the pen moves between clicks. 

There is a preference in the [Preferences Dialog](<./Dialogs-Preferences_Dialog.md> "Dialogs:Preferences Dialog") under the General tab to help with this called "Mouse Click Radius" For example, setting Mouse Click Radius = 5 will setup a circular area around the cursor with a radius of 5 pixels. Any click-drag or double-click within this area will register as a click or double-click respectively. The default TouchDesigner setting for this ui option is 2, it seems a value of 5 or higher makes the pen much more usable in the [Network Editor](<./Network_Editor.md> "Network Editor"). 

See also [Tablet CHOP](<./Tablet_CHOP.md> "Tablet CHOP").
