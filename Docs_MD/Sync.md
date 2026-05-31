# Sync

### Synchronizing Multiple Computers  
  
The levels of synchronizing computers are: 
* No Sync
  * Weak Software Sync ([Touch In CHOP](<./Touch_In_CHOP.md> "Touch In CHOP"), [Touch In TOP](<./Touch_In_TOP.md> "Touch In TOP"), [Touch Out CHOP](<./Touch_Out_CHOP.md> "Touch Out CHOP"), [Touch Out TOP](<./Touch_Out_TOP.md> "Touch Out TOP")) sending data streams with queues to assure continuity.
  * Medium Software Sync ([OSC Out DAT](<./OSC_Out_DAT.md> "OSC Out DAT") or [OSC Out CHOP](<./OSC_Out_CHOP.md> "OSC Out CHOP")) nodes sending frame number, time code, etc. to other processes.
  * Tight Software Sync ([Sync In CHOP](<./Sync_In_CHOP.md> "Sync In CHOP")/[Sync Out CHOP](<./Sync_Out_CHOP.md> "Sync Out CHOP"))
  * Tight Software Sync + Hardware Sync (Sync In/Out CHOPs + [Hardware Frame Lock](<./Hardware_Frame_Lock.md> "Hardware Frame Lock") in the [Window COMP](<./Window_COMP.md> "Window COMP") \+ Quadro Sync cards)


Sync In/Out CHOPS is a software sync that syncs the creation of the content. Hardware Sync/Frame Lock syncs the presentation of the content to the displays. Hardware Frame lock is the method to achieve hardware sync. But we can use the terms interchangeably as well. 

It is not effective to use Hardware Sync if you don’t have Tight Software Sync going since the content presented to the hardware will not be in sync in the first place. However, it can be effective to use Tight Software Sync without Hardware Sync: the content will arrive to the hardware in-sync but the vertical refresh phase of the displays may be out of sync. Additionally, Hardware Frame Lock ensures that the displays only update when they are all ready to update. So if one machine drops a frame, they all drop a frame. This may or may not be desirable, depending on the content and the display setup. 

See also: [Syncing Multiple Computers](<./Syncing_Multiple_Computers.md> "Syncing Multiple Computers"), [Hardware Frame Lock](<./Hardware_Frame_Lock.md> "Hardware Frame Lock"). 

### Syncing on One Computer

See [Vertical Sync and Horizontal Tearing](<./Vertical_Sync_and_Horizontal_Tearing.md> "Vertical Sync and Horizontal Tearing"), [Window Component](<./Window_COMP.md> "Window COMP"). 

### Syncing Movie Audio and Video

Since audio and video from a movie file take different paths, see Audio Sync Offset adjustments in [Audio Movie CHOP](<./Audio_Movie_CHOP.md> "Audio Movie CHOP") and Buffer Length in [Audio Device Out CHOP](<./Audio_Device_Out_CHOP.md> "Audio Device Out CHOP"). There will also be further delay in the audio hardware to your speakers and ears. Video delays go through double-triple buffering on your graphics card, and delays in your display monitor and your video cabling/routing. 

### Syncing Generative Content

TBD
