# Panel COMP Panel Page

## Parameters - Panel Page  
  
The Panel parameter page controls panel attributes such as display on/off, enable on/off, panel help, and interactions with the cursor. 

Display`display`\- Specifies if the panel is displayed or hidden. 

Enable`enable`\- Allows you to prevent all interaction with this panel. 

Help DAT`helpdat`\- Lets you specify the path to a [Text DAT](<./Text_DAT.md> "Text DAT") whose content will be displayed as a rollover pop-up help for the control panel. 

Floating Viewer Aspect`vieweraspect`\- Controls whether the aspect ratio is proportional or unconstrained when resizing a floating viewer ie. dragging the edges of the viewer to resize it. 

  
Cursor`cursor`\- Changes the cursor displayed when cursor is over the panel. 

Multi-Touch`multitouch`\- When enabled, this panel will process the first touch it gets in a similar manner to how it processes a mouse click, with updates to u, v, state etc. The touch event must be initiated from the panel. Subsequent touches are ignored. If this panel handles multi-touch events via the [Multi Touch In DAT](<./Multi_Touch_In_DAT.md> "Multi Touch In DAT"), you may want to disable Built-in Multi-Touch so it won't interfere with script processing. 
* Use Parent's Multi-Touch Settings - Use the parent's Multi-Touch setting. This defaults to enabled in the root component.
  * Use Built-in Multi-Touch \- Enable use of first touch as mouse.
  * Do Not Use Built-in Multi-Touch \- Disable use of first touch as mouse.


Click Through`clickthrough`\- When enabled all mouse clicks are ignored by this [Panel Component](<./Panel_Component.md> "Panel Component"). 

Use Mouse Wheel`mousewheel`\- Turn on to capture events when the mouse wheel is used over the panel. 

Mouse UV Buttons`uvbuttons[left,middle,right]`\- Allows you to specify which mouse buttons update the uv [Panel Values](<./Panel_Value.md> "Panel Value"). 

Relative UV`mouserel`\- When enabled the uv [Panel Values](<./Panel_Value.md> "Panel Value") will reflect relative mouse movement. 

  
Drag Edges to Resize`resize[lrbt]`\- Four checkboxes allow you to enable resizing a panel by grabbing the corresponding edge or corner: Resize Left, Right, Bottom, Top. 

W Range`resizewmin resizewmax`\- Limits the left-right (width) resizing range. 

H Range`resizehmin resizehmax`\- Limits the bottom-top (height) resizing range. 

Drag to Reposition`reposition`\- Enables repositioning of the panel or window by dragging with the mouse. 

Component`repocomp`\- Enabled by choosing the **Component** option from the Reposition parameter. Specify the path to the panel component you would like to reposition by mouse. 

X Range`repositionx[min,max]`\- Enabled by choosing the **Component** option from the Reposition parameter. Sets the maximum range for repositioning the panel component horizontally. 

Y Range`repositiony[min,max]`\- Enabled by choosing the **Component** option from the Reposition parameter. Sets the maximum range for repositioning the panel component vertically.
