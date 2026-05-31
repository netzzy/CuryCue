# Panel Shortcuts

There are two types of [Shortcut](<./Shortcut.md> "Shortcut"): [Application Shortcuts](<./Application_Shortcuts.md> "Application Shortcuts") that are built-in to TouchDesigner's authoring interface and Panel Shortcuts (described here). Panel Shortcuts can be added to any custom built panel to add keyboard functionality.   
  
Here are default Panel Shortcuts, as you would use in [Perform Mode](<./Perform_Mode.md> "Perform Mode") or in operating any panel: 
* To stop the timeline, hold down Shift and press the Space Bar.
  * To step forward one frame, hold down Shift and press the right-arrow
  * To step back one frame, hold down Shift and press the left-arrow.

### Setting Panel Shortcuts

In [Designer Mode](<./Designer_Mode.md> "Designer Mode"), the [Application Shortcuts](<./Application_Shortcuts.md> "Application Shortcuts") behavior is: Space bar pauses, right-arrow steps forward one frame, and left arrow steps back one frame. 

To create new Panel Shortcuts, add a DAT at location`local/shortcuts`for each desired panel component. The first column is blank, the second column is the character, and the third column is the script command. It’s only read by panels, not worksheets. The reason for the unused first column is to keep the format the same as the application shortcuts table. **Note: the third column is currently only TScript. To use Python place your code in[macro](<./Macro.md> "Macro") and simply reference the macro from this table instead.**

Example:`local/shortcuts`table: (Remember the first column is blank.) 

label  | key  | command   
---|---|---  
| c  | echo you pressed c   
| D  | echo you pressed D   
| b  | echo you pressed b   
| B  | echo you pressed B   
  
You can use specially reserved labels to specify specific keyboard characters: (Remember the first column is blank.) 

label  | key  | command   
---|---|---  
| up  | echo You pressed up   
| down  | echo You pressed down   
| left  | echo You pressed left   
| right  | echo You pressed right   
| tab  | echo You pressed tab   
| enter  | echo you pressed enter   
| esc  | echo you pressed escape   
| backspace  | echo you pressed backspace   
| space  | echo you pressed space bar   
| prtsc  | echo you pressed print screen   
| scrlk  | echo you pressed scroll lock   
| pause  | echo you pressed pause   
| insert  | echo you pressed insert   
| home  | echo you pressed home   
| pgup  | echo you pressed page up   
| del  | echo you pressed del   
| end  | echo you pressed end   
| pgdn  | echo you pressed page down   
| numlk  | echo you pressed num lock   
| F1  | echo you pressed F1   
| F2  | echo you pressed F2   
| F3  | echo you pressed F3   
  
  
You may also specify characters by their ASCII value: (Remember the first column is blank.) 

label  | key  | command   
---|---|---  
| 65  | echo you pressed capital A   
| 66  | echo you pressed a   
  
  
You can add ctrl, alt, shift modifiers: (Remember the first column is blank.) 

label  | key  | command   
---|---|---  
| alt.b  | echo you pressed alt b   
| ctrl.b  | echo you pressed ctrl b   
| shift.tab  | echo you pressed shift tab   
| ctrl.alt.down  | echo you pressed ctrl alt down   
| shift.ctrl.up  | echo you pressed ctrl shift up   
  
The compound modifier order is arbitrary:`alt.ctrl.shift`,`ctrl.alt`, etc. Also note, not all keyboards report the same keys combinations identically. 

### Using Panel Values for Shortcuts

Alternatively, every panel also includes the '`key`' [Panel Value](<./Panel_Value.md> "Panel Value"), which pulses the numeric value of the key pressed over it. Whenever a key is pressed the '`key`' panel value gets set to the ASCII value of the character, then immediately back to zero. Be sure your scripts capture the off-to-on key value change. 

Every key press event is sent up its panel chain, until it is intercepted by either a field component, or a shortcut script along the way. 

  
Use the following functions to convert between ASCII values and characters: 
[code] 
    string  ftoc(int num)   // float to char
    num     ctof(string)    // char to float
    
[/code]

  
Examples: 
[code] 
    ftoc(65) = "a"
    ctof("a") = 65
    
[/code]
