# Playstation DualShock Controller

Playstation DualShock controllers can be used as input devices for TouchDesigner.   
  
## PS3 DualShock and Sixaxis controllers

What you'll need for a Playstation3 controller: 
* a PS3 DualShock3 or Sixaxis controller
  * a USB mini-B cable
  * [PS3-Windows driver](<http://dl.qj.net/SIXAXIS-driver-for-PC-PlayStation-3/pg/12/fid/11679/catid/518>)
  * [PS3sixaxis.tox Component](<http://www.derivative.ca/forum/viewtopic.php?f=22&t=1432>)


The PS3-Windows driver must be selected in the Joystick CHOP's **Joystick Source** parameter. No motion controls supported at this time. 

## PS2 DualShock controllers

What you'll need for a Playstation2 controller: 
* a PS2 Dualshock or Dualshock2 controller
  * a PS2-USB controller adaptor
  * [PS2dualshock.tox Component](<http://www.derivative.ca/forum/viewtopic.php?f=22&t=1432>)


The PS2-USB adaptor must be selected in the Joystick CHOP's **Joystick Source** parameter. 

**TIP:** If the PS2 controller is connected to the computer after TouchDesigner has started or after the PS2Dualshock.tox component was added to the network, then the joystick adaptor must be reslected from the Joystick Source menu. If you are using a different PS2-USB adaptor, it will also need to be reselected from the Joystick Source menu. 

## The Network Explained

The image below shows the network of these components. TouchDesigner creates data channels from the controllers through the [Joystick CHOP](<./Joystick_CHOP.md> "Joystick CHOP"). 

The _math1_ CHOP simply inverts one of the analog sticks for consistency. The _rename1_ CHOP renames all the channels created by the Joystick CHOP into something more meaningful. You can edit the rename parameters here if you would like to change the naming of any controls (the analog stick and directional pad channels are verbose for clarity, shorter names could be used). 

The _math2_ CHOP adjusts the range of the analog sticks and directional pad. It is re-mapped such that neutral is 0. Horizontally, left is 0 to -1, right is 0 to 1. Vertically, down is 0 to -1, up is 0 to 1. 

The _constant1_ and _replace1_ CHOPs are added so that if the joystick is not present at startup, the channels still will be present in your CHOP network using default values. If you rename your channels in the _rename1_ CHOP, be sure to update _constant1_ with your new channel names. 

**TIP:** Make sure the Analog button on the controller is on, the red LED should be on. If not, the analog sticks will not work.
