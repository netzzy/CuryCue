# Panel Toolset

### Panel Components

There are 5 Panel Components used in the construction of TouchDesigner control panels. They are found under the 'COMP' section of the [OP Create Menu](<./OP_Create_Menu.md> "OP Create Menu"). Press <Tab> and select 'COMP', you will see the Panel Components at the top of the list in dark gray. They are: Button, Slider, Container, Field, Select. 

### Panel Values

All control panel gadgets (the Panel Component types) have a list of states represented by what are called "Panel Values". See the [Panel Value](<./Panel_Value.md> "Panel Value") page for the full list of the panel values. 

It is the user's interaction with the gadgets that **sets** all the panel values. 

The panel values can be **accessed** in several places: 
* a [Panel CHOP](<./Panel_CHOP.md> "Panel CHOP"), which you can put inside any gadget, where you can also see the list of possible panel values for that gadget. Put a Panel CHOP in a Button component, display the viewer of the button component and watch the panel values in the Panel CHOP change.
  *`panel()`expression, where you can query the state of a variable.
  * Middle-click on a panel component shows the names and values of all the panel values.
  * [Panel Execute DAT](<./Panel_Execute_DAT.md> "Panel Execute DAT") allows you to trigger a script based on the changes or states of any panel value. Put a Panel Execute DAT in a Button COMP and look in the Panel Value parameter menu to see the list of values. Select a Panel Value to use as a trigger to execute the script.

### Panel CHOP

The Panel CHOP works in conjunction with [Panel Components](<./Panel_Component.md> "Panel Component") by grabbing all the [Panel Values](<./Panel_Value.md> "Panel Value") and outputs them as CHOP channels. Exporting these channels to parameters is the most straightforward way to connect custom UI panels to various operator parameters in the project. 

The Panel CHOP only has 3 parameters: 

Component \- specifies the component that the Panel CHOP is retrieving values from. You can drag and drop any panel component onto this parameter. If this path is left blank, it defaults to the [Parent](<./Parent.md> "Parent") component. 

Select - selects which values to output. The default is '*', meaning 'all values'. You can select a subset by using the drop-down menu on the right, or by typing in the names of the values you are interested in. [Pattern Matching](<./Pattern_Matching.md> "Pattern Matching") can also be used to select multiple values. 

Rename - Allows you to rename selected channels. 

### Panel Component Parameters

All Panel Components have 3 common parameter pages used to create a control panel. They are the Layout page, the Panel page, and the Color page. Additionally, the Button, Field, and Slider components have an addition parameter pages (of the respective name) to contain parameters specific to that panel type. 

[Panel COMP Layout Page](</Panel_COMP_Layout_Page> "Panel COMP Layout Page")

[Panel COMP Panel Page](<./Panel_COMP_Panel_Page.md> "Panel COMP Panel Page")

[Panel COMP Color Page](</Panel_COMP_Color_Page> "Panel COMP Color Page")
