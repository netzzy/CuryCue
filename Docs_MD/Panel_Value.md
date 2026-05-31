# Panel Value

**Panel Values** hold the current states of [Panel Components](<./Panel_Component.md> "Panel Component"). Panel Values change based on users interactions with control panels. 

Panel values are accessed in 4 ways: 
* Panel values can be viewed by middle-clicking on a panel component to bring up its info box. Note that string values and values that are _instant_ (set to X and then reverted to 0 or empty) will not display on a Panel CHOP. These values are denoted as _string_ and _instant_ below.
* The [Panel CHOP](<./Panel_CHOP.md> "Panel CHOP") is used to view and access all the panel values of the component.
* The [PanelValue Class](<./PanelValue_Class.md> "PanelValue Class") in Python accesses python values and states, and in TScript, the`panel()`expression returns a panel value.
* The [Panel Execute DAT](<./Panel_Execute_DAT.md> "Panel Execute DAT") will run a script when a panel values change.


Panel values are changed: 
* when users interact with the panels.
  * when virtually clicking on panels using python`click()`calls. See [ButtonCOMP Class](<./ButtonCOMP_Class.md> "ButtonCOMP Class"), [SliderCOMP Class](<./SliderCOMP_Class.md> "SliderCOMP Class"), [ContainerCOMP Class](<./ContainerCOMP_Class.md> "ContainerCOMP Class")
  * when in [Tscript](<./Tscript.md> "Tscript") the click command or the Tscript controlpanel command.

## General Panel Values

The list below gives a brief description of all the panel values. Some of the values do not have an effect on some panel types, they are described below. 
* **`select`→`int`** \- 1 when left, middle, or right mouse button is pressed over the panel.
  * **`lselect`→`int`** \- 1 when left mouse button is pressed.
  * **`mselect`→`int`** \- 1 when middle mouse button is pressed.
  * **`rselect`→`int`** \- 1 when right mouse button is pressed.
  * **`reposition`→`int`** \- 1 when component is re-positioned.
  * **`resize`→`int`** \- 1 when component is resized.
  * **`dragout`→`int`** \- when you click in the gadget, drag out of the gadget and release, it goes 0 to 1 when you release outside. It gets set to 0 any time you click inside the gadget.
  * **`ldragout`→`int`** \- same as`dragout`, but only when left mouse is used.
  * **`mdragout`→`int`** \- same as`dragout`, but only when middle mouse is used.
  * **`rdragout`→`int`** \- same as`dragout`, but only when right mouse is used.
  * **`ctrl`→`int`** \- 1 if Ctrl key is down when panel is clicked on.
  * **`alt`→`int`** \- 1 if Alt key is down when panel is clicked on.
  * **`shift`→`int`** \- 1 if Shift key is down when panel is clicked on.
  * **`cmd`→`int`** \- 1 if Cmd key is down when panel is clicked on (OSX only).
  * **`u`,`v`→`float`** \- corresponds to the x and y position of the cursor. Updated whenever any mouse button is pressed over the panel.
  * **`trueu`,`truev`→`float`** \- in all panels. By default they are the same as u and v. When in Relative UV mode, they continue to behave the same as they do when not in Relative UV mode (they don’t go into relative mode).
  * **`rollu`,`rollv`→`float`** \- give the gadget's u and v cursor position when rolling over a gadget.
  * **`dragrollover`→`int`** \- switches from 0 to 1 when something that can be dropped is dragged over. Panel must allow drop for this to be enabled.
  * **`dragrollu`,`dragrollv`** →`float`\- give the gadget's u and v cursor position when dragging and rolling over a gadget. Panel must allow drop for this to be enabled.
  * **`rollover`→`int`** \- 1 whenever the cursor is over the panel and that panel is the foremost element. NOTE: This differs from the inside value which does not need to be in the foreground.
  * **`inside`→`int`** \- 1 whenever the cursor is anywhere over the panel.
  * **`insideu`,`insidev`** →`float`\- give the gadget's u and v cursor position when the rolling over gadget.
  * **`children`→`int`** \- the number of components in the network inside the gadget (not including children of children).
  * **`display`→`int`** \- the current value of the panel's display parameter. **NOTE** : This value is readonly.
  * **`enable`→`int`** \- 1 if the panel is enabled, 0 otherwise. **NOTE** : This value is readonly.
  * **`key`→`int`** \- the most recent key that was pressed while cursor was over this gadget, followed in time by`0`. The value for the 'a' key is`97`, its ASCII value. When you press 'a', and you are triggering a Panel Execute on the panel value`key`, you will get 2 calls, one with .val of`97`, one with`0`.
  * **`focusselect`→`int`** \- 1 if you have last clicked in this panel, 0 otherwise. It keeps track of focus hierarchy, which is set by mouse clicks (any of the left/middle/right mouse buttons). If a panel is clicked on, its and all the panels in its parent hierarchy will have their`focusselect`value set to 1. If you click on a different panel, the`focusselect`of the common ancestors of the two panels will remain unchanged, the first panel and ancestors not shared will have its value set to 0, and the new panel and unset ancestors will have its value set to 1. **NOTE** : This value is readonly, use the [PanelCOMP](<./PanelCOMP_Class.md> "PanelCOMP Class") method`setFocus`to change the panel focus.
  * **`click`→`int`** \- counts the number of consecutive clicks separated by .6 seconds or less.
  * **`winopen`→`int`** \- 1 if panel is open as a floating window, 0 otherwise.
  * **`wheel`→`int`** \- (instant) sends a pulse of a positive or negative number and then back to 0 when the mouse wheel is used.
  * **`screenw`,`screenh`** →`int`\- gets updated with the most recent window size of the panel. [Node Viewers](<./Node_Viewer.md> "Node Viewer") do not affect this value. Use these values in expressions in TOPs to get them to render at a specific resolutions. Use with caution, as multiple viewers will conflict with each other.
  * **`screenwm`,`screenhm`→`int`** \- Screen Width Margin and Screen Height Margin panel values get the screen coordinates of a panel after margins are taken into account.
  * **`drag`→`int`** \- 1 if the panel is currently being dragged.
  * **`drop`→`int`** \- 1 when the panel is dropped.
  * **`scrollu`,`scrollv`** →`float`\- get or set the normalized (0-1) scroll position of the panel.

## Slider Only Panel Values
* **`stateu`,`statev`→`float`** \- (may be obsolete, use`u`,`v`,`trueu`,`truev`) corresponds to the x and y position of the cursor. Updated whenever any mouse button is pressed over the slider panel.`stateu`/`statev`differ from`u`/`v`in that the Slider's 'Slider Page' parameters (Zone, Range, Clamp, etc.) are used to determine the result of`stateu`/`statev`.

## Button and Table Only Panel Values
* **`state`→`int`** \- (button only) For momentary or toggle buttons, the value toggles on=1/off=0 with any mouse click over the panel. For Sliders, the value matches`stateu`when the slider type is 'Slider U', and`statev`when the slider type is 'Slider V'. state does nothing for slider type 'Slider UV'.
  * **`lstate`→`int`** \- (button only) value toggles on=1/off=0 with a left mouse click over the panel.
  * **`mstate`→`int`** \- (button only) value toggles on=1/off=0 with a middle mouse click over the panel.
  * **`rstate`→`int`** \- (button only) value toggles on=1/off=0 with a right mouse click over the panel.
  * **`picked`→`int`** \- (button only) the`picked`panel value works in conjunction with shift or ctrl clicking a button component. When shift or ctrl clicking multiple momentary buttons the last one clicked will hold the`state`panel value where all others state panel values will be set to 1. Here is where the`picked`panel value helps out as it remains at 1 until you click select a single button.

## Radio and Exclusive Buttons Only Panel Values
* **`radio`→`int`** \- index of which radio/exclusive button is selected by any mouse click. The index starts at 0 and the radio buttons are sorted in alphanumeric order. When using the exclusive button type, a value of -1 is used to indicate no button is selected after clicking a button twice in succession.
  * **`lradio`→`int`** \- index of which radio/exclusive button is selected by a left mouse click.
  * **`mradio`→`int`** \- index of which radio/exclusive button is selected by a middle mouse click.
  * **`rradio`→`int`** \- index of which radio/exclusive button is selected by a right mouse click.
  * **`radioname`→`str`** \- returns the name (string) of the button selected in the radio variable. Use this in an expression or function.
  * **`lradioname`→`str`** \- returns the name (string) of the button selected in the`lradio`value. Use this in an expression or function.
  * **`mradioname`→`str`** \- returns the name (string) of the button selected in the`mradio`value. Use this in an expression or function.
  * **`rradioname`→`str`** \- returns the name (string) of the button selected in the`rradio`value. Use this in an expression or function.

## Field Only Panel Values
* **`key`→`int`** \- (instant) this value is set with the ASCII code of the key when it is hit on the keyboard. it is immediately followed by the value of 0. To monitor keys with no ASCII value please use the [Keyboard In DAT](<./Keyboard_In_DAT.md> "Keyboard In DAT").
  * **`invalidkey`→`int`** \- (instant) value is pulsed whenever an invalid key is pressed. An example is pressing an _alphanumeric_ key 'a' on a field set to _numeric_ , the`invalidkey`panel value would pulse to 97 then 0 in this case.
  * **`focus`→`int`** \-`focus`is set when you click on a field. when`focus`is 1, you can type if the field is editable.
  * **`field`→`str`** \- (string) this is the current saved value of the field.
  * **`fieldediting`→`str`** \- (string) this is the contents of the field as it is being edited.

## Table Only Panel Values

Cell IDs are numeric values, beginning at 0 for the first defined cell. 
* **`celloverid`→`int`** \- Cell ID cursor is over. -1 when the cursor is not over any cell.
  * **`cellfocusid`→`int`** \- Cell ID currently being edited. -1 when no cell is being edited.
  * **`cellselectid`→`int`** \- Cell ID currently being clicked down on. -1 when no cell is being clicked down on.
  * **`celllselectid`→`int`** \- Cell ID currently being clicked down on with the left mouse button, otherwise -1.
  * **`cellmselectid`→`int`** \- Cell ID currently being clicked down on with the middle mouse button, otherwise -1.
  * **`cellrselectid`→`int`** \- Cell ID currently being clicked down on with the right mouse button, otherwise -1.
  * **`cellradioid`→`int`** \- Cell ID was last clicked on. Value remains after mouse buttons released.
  * **`celldragid`→`int`** \- Cell ID being dragged out.
  * **`celldropid`→`int`** \- Cell ID that something dropped onto.
