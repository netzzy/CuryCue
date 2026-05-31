# TouchPlayer

  
TouchPlayer will run files created with TouchDesigner in [Perform Mode](<./Perform_Mode.md> "Perform Mode") only. TouchPlayer does not have a designer interface to author files, it is meant only for playback of TouchDesigner projects. 

**TouchPlayer Non-Commercial** is free of charge for non-paying, non-commercial uses. No license, key, or registration is required to download and use TouchPlayer in Non-Commercial form. This is a great way to share your work with other who do not use TouchDesigner. All they have to do is install TouchPlayer and run your file. 

**TouchPlayer Commercial** licenses can be used for paying projects and support the same feature set as TouchDesigner Commercial. It is available in the [Store](<https://www.derivative.ca/shop/>) for $300 per license. 

**TouchPlayer Pro** licenses can be used for paying projects and support the same feature set as TouchDesigner Pro. It is available in the [Store](<https://www.derivative.ca/shop/>) for $800 per license. 

[Volume Discounts](<./Volume_Discount.md> "Volume Discount") are available for TouchPlayer. 

## Installation

TouchPlayer is included in the TouchDesigner installer on Windows. To install TouchPlayer, use the TouchDesigner installer and select **Custom Install and TouchPlayer Options**. After clicking **Install** there will be options for installing TouchPlayer. 

On macOS, TouchPlayer is a separate application and installer that can be installed next to TouchDesigner. 

The TouchDesigner and TouchPlayer installers are available on the [Official Downloads page](<https://derivative.ca/download/archive>). 

## How TouchPlayer Works
* TouchPlayer opens any [file type](<./File_Types.md> "File Types") supported by TouchDesigner and runs in [Perform Mode](<./Perform_Mode.md> "Perform Mode") only.
  * For [.toe](<./.md> ".toe") files, the perform mode settings are customizable by the author of the TouchDesigner file.
  * There is a small control panel added to every TouchPlayer Non-Commercial window with controls for play/pause, fullscreen, Key Manager, help, and quit. This control panel is suppressed when using a Commercial or Pro license but can be accessed.
  * TouchPlayer Non-Commercial will ask the user to confirm access to certain external devices (such as camera and microphones for video/audio input) and system services like web (via the [Web DAT](<./Web_DAT.md> "Web DAT")) or network (via the network operators). The confirm dialogs are suppressed in Commercial and Pro.
  * TouchPlayer has the same system requirements as TouchDesigner.


**Tip** : Pause/unpause the timeline using Shift-Spacebar in TouchPlayer and [Perform Mode](<./Perform_Mode.md> "Perform Mode"). 

## Using TouchPlayer

### Installing TouchPlayer on Windows

On Windows, TouchPlayer uses the same installer as TouchDesigner. When you are installing TouchDesigner there are options for making TouchPlayer icons on the Desktop, adding TouchPlayer to the Open With... menu, and for making it the default application to open .toe files with. 

Start the installer and select **Custom install and TouchPlayer options** when prompted. 

Then on the next dialog of the installer, select the TouchPlayer (and TouchDesigner) options you want. Then click Install. 

### Starting TouchPlayer

To start TouchPlayer, drag and drop any file you want to open onto the TouchPlayer desktop icon. Alternatively you can right-click on that file and select TouchPlayer from the **Open With...** menu if this option was selected in the installation process. 

  
You can also start TouchPlayer by double-clicking the TouchPlayer desktop icon (if this option was selected in the installation process) or selecting it from the Start > Programs menu. When opening TouchPlayer using these latter two methods, the TouchPlayer startup dialog will open as shown below. 

### TouchPlayer Non-Commercial Controls

**These features will not appear when using a Commercial or Pro license**. 

Drag and Drop any [compatible file](<./File_Types.md> "File Types") into this dialog to open it in TouchPlayer. 

The main TouchPlayer window will have a small control panel in the upper-right corner of the window. 

[![TouchPlayerControlsIcon.png](./images/1/1f/TouchPlayerControlsIcon.png)](</File:TouchPlayerControlsIcon.png>) click to go to [www.derivative.ca](<http://www.derivative.ca>)

[![TouchPlayerControlsPause.png](./images/4/4f/TouchPlayerControlsPause.png)](</File:TouchPlayerControlsPause.png>) click to pause/play. 

[![TouchPlayerControlsFullscreen.png](./images/7/71/TouchPlayerControlsFullscreen.png)](</File:TouchPlayerControlsFullscreen.png>) click to enter and exit fullscreen mode. 

[![TouchPlayerControlsHelp.png](./images/0/05/TouchPlayerControlsHelp.png)](</File:TouchPlayerControlsHelp.png>) click to go to the TouchPlayer help page. 

[![TouchPlayerControlsClose.png](./images/a/ae/TouchPlayerControlsClose.png)](</File:TouchPlayerControlsClose.png>) click to quit TouchPlayer. 

## Creating Suitable Files for TouchPlayer

Although TouchPlayer will play any`.toe`or`.tox`file, some guidelines and best practices should be followed. 
* Be aware that the`.toe`file you distribute can be also opened and edited by those with TouchDesigner.
  * If you want to protect your`.toe`file, you have to purchase Pro and set the Privacy flag on your`.toe`: Following that, others cannot open the`.toe`for examination in TouchDesigner.
  * If your`.toe`file is created in your copy of TouchDesigner Pro with the Privacy flag on, then the file cannot be opened or edited by those with TouchDesigner.
  * Media (images, movies, audio, data) can be embedded in the private`.toe`file using TouchDesigner’s “Virtual File System” (vfs).
  * TouchPlayer's different licenses use the same feature sets as the corresponding TouchDesigner licenses. For a comparison of licenses, see [Licensing](<./Licensing.md> "Licensing").
  * Be Aware that TouchPlayer Non-Commercial will open confirmation dialogs when it attempts to access network connections, the [Video Device In TOP](<./Video_Device_In_TOP.md> "Video Device In TOP"), or the [Audio Device In CHOP](<./Audio_Device_In_CHOP.md> "Audio Device In CHOP"). These confirmation dialogs will not open when using TouchPlayer Commercial or Pro.
  * TouchPlayer will open all supported image & movie files, as well as [.toe](<./.md> ".toe") & [.tox](<./.md> ".tox").
  * Although TouchPlayer does not support the network editing interface, you can open a floating parameter window on any operator via scripting, namely the`OP.openParameters()`call. See [OP Class](<./OP_Class.md>). Or you can embed the parameter dialog in your window with a [Parameter COMP](<./Parameter_COMP.md> "Parameter COMP").

## Developing when using TouchPlayer licenses

Often when building a project with many TouchPlayer license you will want to be able to go to each machine to edit/analyze the current state of a network running a TouchPlayer license. This can be done very easily by; 

1\. Run the application using the TouchDesigner executable instead of the TouchPlayer executable. The TouchPlayer Commercial/Pro license will still work inside of TouchDesigner, but the network editor will be disabled 2\. Install a full TouchDesigner license on the machine or plug in a [License Dongle](<./License_Dongle.md> "License Dongle"). The network editor will become active for editing, you will not need to restart the file.  
3\. When finished, disable the TouchDesigner license or unplug the License Dongle. The application will fall back to using the TouchPlayer license that was installed previously.
