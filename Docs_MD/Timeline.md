# Timeline

The Timeline is found at the bottom of TouchDesigner's interface. The transport buttons and timeline settings control the playback of [Time Components](<./Time_COMP.md> "Time COMP") throughout TouchDesigner networks. 

Every component can have its own Timeline. 

See also: [Frame](<./Frame.md> "Frame") and [Time Slicing](<./Time_Slicing.md> "Time Slicing")

## 

Timepath - Changing the Scope of the Timeline

The Timeline can display the 'root' time or any [Component Time](<./Component_Time.md> "Component Time") throughout the network hierarchy. The time currently displayed by the Timeline is shown in the [Timepath](<./Timepath.md> "Timepath") field of the Timeline settings. 

By default, the Timeline displays TouchDesigner's root time (Timepath = /), which controls the playback of the entire network hierarchy. 

  
The Timeline can also display any [Component Time](<./Component_Time.md> "Component Time"). To scope a Component Time into the Timeline, press the "S" scope button in that [component's mini-timeline](<./Component_Timeline.md> "Component Timeline"). This will change the Timepath to reflect which Component Time is scoped and also change the color of the Timeline's UI elements. Each unique Component Time will have a unique color to make it easy to associate it with a component's mini-timeline. 

To quickly toggle back to 'root' time, click the / button beside the Timepath field. The color for root time is always the dark blue color used throughout TouchDesigner's dialogs and interface. 

## 

Transport Controls

This part of the Timeline holds the timecode display and the transport controls. 

The Timecode display shows the current time in either frames or beats. This can be selected using the **TimeCode** or **Beats** buttons beside the timecode display. To the right of the timecode display, the frames-per-second TouchDesigner is running at is displayed in the **[fps](<./Frame_Rate.md> "Frame Rate")** field and the current frame is displayed in the **frame** field. A frame number can also be entered into the frame field to jump to a specific frame. 

The transport controls offer the basic controls for playback. The buttons from left-to-right are: 
* **Reset** \- the playhead to the beginning of the working range
  * **Pause** \- paused the playback
  * **Reverse Play** \- playback in reverse
  * **Play** \- playback forward
  * **Step Back** \- step back one frame
  * **Step Forward** \- step forward one frame


Using the **Range Limit** buttons, the Timeline can be set to **Loop** or to play through **Once** and then stop. 

The **I** button at the left-most side of this area is the **Run Independent** button. This can be used when a Component Time is scoped in the Timeline to toggle the 'run independently' option on/off. 

## 

Timeline Settings

This part of the timeline holds the Timepath and the Timeline settings. 

The **Timepath** displays the path to the Time Component the Timeline is currently controlling (when the path is root (timepath = /), this is referred to as root time). The **[/]** button jumps back to root time from any other path. 

The Timeline settings change the parameters of the Time Component the Timeline is currently controlling. The settings are: 
* **Start/End** \- sets the Start and End frames, the overall length
  * **RStart/REnd** \- sets the Start and End frames of the working range (sub-range). Also displayed as the colored bar above the time index in the Timeline.
  * **FPS** \- sets the [frame rate](<./Frame_Rate.md> "Frame Rate") in frames per second.
  * **BPM** \- beat per minute
  * **ResetF** \- reset frame
  * **T Sig** \- the time signature used when in Beats mode.
