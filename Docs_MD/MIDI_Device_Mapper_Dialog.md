# MIDI Mapper Dialog

## 

Description

The MIDI Device Mapper dialog allows you to set up TouchDesigner's MIDI devices, MIDI input and output signals, and MIDI timing. 

Once a Device Mapping has been created here in the dialog, drag anywhere in that device mapping's row and drop into a network to create a CHOP with all the mapped channels ready to use. 

[![MIDIMapperDialog.PNG](./images/5/52/MIDIMapperDialog.png)](</File:MIDIMapperDialog.PNG>)

  
See also the [MIDI In DAT](<./MIDI_In_DAT.md> "MIDI In DAT"), [MIDI Event DAT](<./MIDI_Event_DAT.md> "MIDI Event DAT"), [MIDI In Map CHOP](<./MIDI_In_Map_CHOP.md> "MIDI In Map CHOP"), [MIDI In CHOP](<./MIDI_In_CHOP.md> "MIDI In CHOP"), [MIDI Out CHOP](<./MIDI_Out_CHOP.md> "MIDI Out CHOP"),`midi`command. 

## 

Device Mapping

This table creates MIDI device mappings for TouchDesigner. A unique **Device ID** is created which associates MIDI In and Out devices with a MIDI device map. This Device ID can then be used by MIDI [operators](<./Operator.md> "Operator") such as the [MIDI In CHOP](<./MIDI_In_CHOP.md> "MIDI In CHOP"), [MIDI Out CHOP](<./MIDI_Out_CHOP.md> "MIDI Out CHOP"), and [MIDI In DAT](<./MIDI_In_DAT.md> "MIDI In DAT"). 

[![DeviceMapping.png](./images/9/9f/DeviceMapping.png)](</File:DeviceMapping.png>)

### 

Creating a new Device ID

MIDI device mappings are identified by a unique **ID** in TouchDesigner. This ID is used in MIDI operator's **Device ID** parameter. The ID will specify an In and/or Out device and a device map for the MIDI operator to use to create data channels. 

To add a new device mapping, click the **Add Device Mapping** button. This will add a row to the Device Mapping list above. The **ID** and **Channel** (**Ch**) will be assigned default values. Click on the **In Device** , **Out Device** and **MIDI Map** fields to open a list of available options. 

### 

Deleting a Device Mapping

Right-click on the device mapping you wish to delete, then select **Delete** from the menu. 

### 

In/Out Device Menus

Clicking in the **In Device** or **Out Device** columns will open a menu for those respective devices. The menu will list all the devices TouchDesigner finds connected to the system. Some devices may not be listed if they are connected while TouchDesigner is already open. If this occurs, save your .toe file and restart TouchDesigner. 

### 

MIDI Map Menu

**TouchDesigner System Maps**

Clicking on the **Devices** tab will display the default MIDI maps included with TouchDesigner. Rollover the list on the right to get a preview of the mapping, click on a device to select it. The right side shows an image of the device and a list of the MIDI mappings for it (ie. channel s1 = b0 18 -- controller). 

[![MIDIMapperDialog Devices.PNG](./images/f/f0/MIDIMapperDialog_Devices.png)](</File:MIDIMapperDialog_Devices.PNG>)

  
**User Maps**

You can also create custom **User** MIDI mappings. These are stored in`/local/midi/userdevices`. To create a new user MIDI map, click **Add Device** at the bottom of the device list. A new default template mapping will be added to the list and stored in`/local/midi/userdevices`. You can rename this User Map using the **Name** field. 

Now go inside the map component that was added at`/local/midi/userdevices/_newname_`. Edit the image (optional). More importantly, edit the two tables called`sliders`and`buttons`. There is no auto-learn currently. 

**TIP** : For MIDI buttons in the`buttons`table, the first column is the On message and the second column is the Off message. If the second column is the same as the first, the button acts as a toggle. If the second column is blank, then pressing the button generates a short pulse, so it goes off automatically and does not need an Off message. 

## 

MIDI Console

[![MIDIConsole.png](./images/a/ae/MIDIConsole.png)](</File:MIDIConsole.png>)

The MIDI Console displays TouchDesigner's incoming and outgoing MIDI messages.
