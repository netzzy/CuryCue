# TUIK

TUIK is a legacy obsolete UI kit of TouchDesigner, replaced by [Widgets](<./Widgets.md> "Widgets").   
  
This article gives an overview of TUIK (pronounced _\ˈtwēk\_). TUIK stands for "Touch User Interface Kit" and is a collection of User Interface components. 

## Overview

TUIK is a collection of user interface components located in the palette that enable the user to easily build customized control panels. 

## Getting Started

In the Browser, select the [Palette](<./Palette.md> "Palette") tab. If the palette browser is not already being displayed, open the Palette by either choosing it from Dialogs->Palette or unstowing it by clicking on the tiny left stowbar of the TouchDesigner window. In the Palette open up the folder "TUIK" by clicking on it and then "Windowparts". Next choose from the list the "emptypanel" component and [Drag-and-Drop](<./Drag-and-Drop.md> "Drag-and-Drop") it into a TouchDesigner [Network](<./Network.md> "Network"). 

Next [Drag-and-Drop](<./Drag-and-Drop.md> "Drag-and-Drop") the component "titlebar" and connect it to "emptypanel" by connecting top and bottom connectors, creating a "parenting" or "hierarchical" relationship. This process is the same as with [3D_Parenting](<./3D_Parenting.md> "3D Parenting"). 

Almost all TUIK components can be customized by rolling over the container and pressing F11 on your keyboard. Doing this on the "titlebar" component will give you a table with a row called "dialogname" and a second column set to "Controlpanel". Changing this value by setting the node into its [Viewer_Active](<./Viewer_Active.md> "Viewer Active") mode will change the text in the "titlebar". 

Open the [RMB Menu](<./RMB_Menu.md> "RMB Menu") on the "emptypanel" and select the item "Open Control Panel" -> "Borderless..." to open the control panel in a floating, borderless window. 

To have the "titlebar" component resize with the "emptypanel" size, change the "Width" parameter on the [Panel_COMP_Layout_Page](</Panel_COMP_Layout_Page> "Panel COMP Layout Page") from the constant value to 
[code] 
    par(opparent(".",0)+"/panelw")
    
[/code]

The 
[code] 
    opparent(".",0)
    
[/code]

expression returns the path to the nodes hierarchical parent where "0" can be substituted by the number of levels you want to go up in the hierarchy. 

Next [Drag-and-Drop](<./Drag-and-Drop.md> "Drag-and-Drop") another "emptypanel" component and hierarchically parent it to the first "emptypanel" component. Change the "Width" and "Height" parameter on the [Panel_COMP_Layout_Page](</Panel_COMP_Layout_Page> "Panel COMP Layout Page") to 
[code] 
    par(opparent(".",0)+"/panelw")
    
[/code]

and 
[code] 
    par(opparent(".",0)+"/panelh")-25
    
[/code]

where the 25 is subtracted to account for the height of the "titlebar" component. Further change the "Margin" parameter to 5 and the "Align Margin" parameter to 2. This will make sure that components which are added next are spaced apart by 2 pixels. Last set the "Align Order" parameter to 1 to make sure the new "emptypanel" is aligned below the "titlebar" component. 

In the Palette now navigate to the "TUIK">"Sliders" folder and [Drag-and-Drop](<./Drag-and-Drop.md> "Drag-and-Drop") the "sliderhorzvalue" into the TouchDesigner [Network](<./Network.md> "Network"). Hierarchically parent the "sliderhorzvalue" to the second "emptypanel" and change the definition by rolling over it with the mouse and hitting F11 on your keyboard. Copy and paste the "sliderhorzvalue" a couple times and you should end up with a controlpanel similar to this: 

[![](./images/8/80/SampleTuikControlpanelNetwork.jpg)](</File:SampleTuikControlpanelNetwork.jpg>)

[](</File:SampleTuikControlpanelNetwork.jpg> "Enlarge")

Controlpanel Network

[![](./images/b/bf/SampleTuikControlpanel.jpg)](</File:SampleTuikControlpanel.jpg>)

[](</File:SampleTuikControlpanel.jpg> "Enlarge")

TUIK Controlpanel

## Customizing TUIK Components

Each component has at its root a _define_ Table DAT which lets you change the components behavior and looks. You can edit it by rolling over the TUIK gadget and hitting F11 till you see the define table in the node viewer. Alternatively, enter the TUIK gadget, select the _define_ Table DAT, hit "a" and change the values in the second column beside the entry you want to change. Values can be either strings, numbers or expressions. 

All components also come with _color_ Table DAT were colors can be specified for certain parts of the component. The first column specifies the part of the TUIK Component and the second column the color. Colors can be specified by real name like _Blue_ or you can set custom colors: 
[code] 
    rgba(125,90,80,1)
    
[/code]

where colors have a range from 0 to 255 and alpha has a range from 0 to 1. 

## TUIK Gadgets

### Window Parts
* **emptypanel** \- this component is an empty container and can be used as a starting point for a control panel. Change its X and Y width parameters to increase or decrease the panel's size.
* **titlebar** \- this component provides you with a drag-able title bar and a close button. The _define_ Table DAT lets you specify the titlebar label.
* **menu** \- this component is a drop-down menu. The _define_ Table DAT lets you specify the menus labels. Inside the component are Table DATs which are used to specify the drop-down menus entries and the scripts that are executed when selecting a drop-down menu entry. The associated scripts are located in the contained scripts BASE Component. The two inputs to the gadget are an alternative Table to specify the menu entries as well as a Table input to specify what drop-down elements are en- or disabled.
* **heading** \- this component can be used as a header for subsections of a control panel. The _define_ Table DAT lets you specify the heading label.
* **viewer** \- lets you display a TOP as a control panel viewer. The _define_ Table DAT lets you specify where to fetch the TOP from that is being displayed by the viewer component. Alternatively connecting a TOP to the viewers' In TOP will display it.
* **label** \- is being used as a simple label. The _define_ Table DAT lets you specify the label's caption.

### Slider Gadgets
* **sliderhorz** \- is a horizontal slider outputting its current value as a CHOP channel. The _define_ Table DAT lets you specify the sliders label. The _channelname_ row will change the name of the output channel. _lower_range_ and _upper_range_ let you set the value range of the slider. If _lower_clamp_ or _upper_clamp_ is set to 1 the sliders output value will be limited to the in _lower_range_ and _upper_range_ specified values. _format_ lets you chose between "float" and "integer" as the output format of the slider's value. _type_ can be set to either "std" or "xfade" where "xfade" will mimic a cross fade slider. Changing orientation from "horizontal" to "vertical" will switch the direction of the slider. You will have to adjust the Width and Height parameter of the slider component.
* **sliderhorzmulti** \- is the same as SliderHorz but comes with multiple knobs.
* **sliderhorzvalue** \- is the same as SliderHorz but comes with a value field.
* **range** \- is a horizontal slider with 2 knobs to specify a range.
* **slider2d** \- is a two-dimensional slider. The _define_ Table DAT lets you specify the slider's label. _displaylabel_ controls if the label should be displayed and _labelwidth_ will set the labels width. The _channelname_ row will change the name of the output channel.
* **knob** \- is a rotational slider similar to a pot as found on many hardware interfaces. The _define_ Table DAT lets you specify the knob's label as well as its lower_range and upper_range.
* **knobendless** \- is the same as the Knob but instead of limited rotation, it is endless. The _define_ Table DAT lets you specify the knob's label as well as its lower_range and upper_range.

### Button Gadgets
* **buttonmomentary** \- is a simple momentary button. The _define_ Table DAT lets you specify the button's label as well as the text to appear on the button called "buttonlabel". _displaylabel_ controls if the label should be displayed and _labelwidth_ will set the labels width. The _channelname_ row will change the name of the output channel.
* **buttontoggle** \- is a simple toggle button. The _define_ Table DAT lets you specify the button's label as well as the text to appear on the button called "buttonlabel". _displaylabel_ controls if the label should be displayed and _labelwidth_ will set the labels width. The _channelname_ row will change the name of the output channel.
* **buttonradio** \- is a radio button group. The _define_ Table DAT lets you specify the radio groups label as well as all the labels for each individual radio button. _displaylabel_ controls if the label should be displayed and _labelwidth_ will set the labels width. The _channelname_ row will change the name of the output channel.
* **radiogroup** \- is the same as the ButtonRadio gadget but in a different design. The _define_ Table DAT lets you specify the radio groups label as well as all the labels for each individual radio button. _displaylabel_ controls if the label should be displayed and _labelwidth_ will set the labels width. The _channelname_ row will change the name of the output channel.
* **button checkbox** \- is a simple toggle button in the design of a checkbox. The _define_ Table DAT lets you specify the label as well as the text to appear beside the checkbox called "buttonlabel". _displaylabel_ controls if the label should be displayed and _labelwidth_ will set the labels width. The _channelname_ row will change the name of the output channel.
* **button symbol** \- is the same as the buttonmomentary gadget but uses symbols instead of text on the button face.

### Valuefield Gadgets
* **valuefield** \- is a field gadget. The _define_ Table DAT lets you define the field's label as well its format. The format can be either "float", "integer" or "string". _displaylabel_ controls if the label should be displayed and _labelwidth_ will set the labels width.
* **stringfield** \- is the same as the "ValueField" gadget with the format option of the _define_ Table DAT set to "string".
* **stringfieldexec** \- is the same as the "StringField" but comes with a button that can runs a script connected to the In DAT after being released.

### Colorpicker Gadgets
* **colorpicker** \- is a circular hsv colorpicker. It returns the picked value in hsv and rgb format.
  * **colorpickerhsv** \- is a rectangular hsv colorpicker. It returns the picked value in hsv and rgb format.
  * **sliderhsv** \- is a horizontal hsv colorpicker with a sliding knob for each value. It returns the picked value in hsv.
  * **slider3hsv** \- is the same as sliderhsv but has discreet sliders for each color value.
  * **sliderrgb** \- is a horizontal rgb colorpicker with a sliding knob for each value. It returns the picked value in rgb.
  * **slider3rgb** \- is the same as sliderrgb but has discreet sliders for each color value.

### List Gadgets
* **dropdownlist** \- is a button list gadget where all available buttons are hidden in a drop-down list. LMB clicking into the textfield or clicking on the arrow button beside it will open the drop-down list. The first input to the gadget is the list of entries and the second input is the script that is to be executed once a list item is selected. The _define_ Table DAT lets you specify the DropdownList's label. _displaylabel_ controls if the label should be displayed and _labelwidth_ will set the labels width. _listitems_ lets you specify how many buttons the drop-down list should have.
  * **dropdownbtn** \- is a similar gadget like dropdownlist but instead of showing the selected value it only has a button which opens a dropdown list.
  * **fieldlist** \- is a list of fields that can be filled in by the user. It comes attached with a script called rename where the user can specify what to do once a field is changed.
  * **list** \- is a button list gadget that has the option to reorder its content. The input to the gadget is the list of entries. The first output is the reordered list and the second output is the selected button. By resizing the gadgets height you can control how many buttons are being displayed. The _define_ Table DAT lets you specify the ButtonList's label. If reorder in the _define_ Table DAT is set to 1, the reorder buttons are enabled.

### Textfield Gadgets
* **textarea** \- takes a Text DAT as input and displays it adding scroll bars if needed.
  * **textareafixed** \- takes a Text DAT as input but only displays as many lines as defined in the _define_ Table DAT.
