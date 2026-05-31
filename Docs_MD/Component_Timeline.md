# Component Timeline

A Component Timeline is displayed at the bottom of the [network editor](<./Network_Editor.md> "Network Editor") for any network that has a [Component Time](<./Component_Time.md> "Component Time"). 

The timeline displays the timecode and current playhead position for the Component Time. 

There are 2 buttons on the left side of the gadget; 
* **I** (Run Independently) - This toggles the Component Time to run independently from other [parent](<./Parent.md> "Parent") Component Times. When Run Independently is **on** , the timeline will maintain its play state (playing or stopped) regardless of other parent timelines. When **off** , the timeline will stay in sync with the first timeline it finds higher in the hierarchy.
  * **S** (Scope) - Clicking this button will load this Component Time into the [Timeline](<./Timeline.md> "Timeline") at the bottom of TouchDesigner's interface. The Timeline UI will take on the color of the Component Timeline to show its scope has changed from root time.


[![](./images/c/c5/TimelineColor.png)](</File:TimelineColor.png>)

alternate Timeline color indicates a Component Time is scoped
