# Widgets

Widgets is a collection of extended components located in the Palette, designed for building user interfaces.   
  
The [Widget COMP](<./Widget_COMP.md> "Widget COMP") is a super-set of the [Container COMP](<./Container_COMP.md> "Container COMP") (though presently identical). 

**[Widgets Tutorials Playlist](<https://www.youtube.com/playlist?list=PLSqkC3f_BStxA4TpF6uWj3HOHPCglRpN9>)**

## TouchDesigner Widget System

[Widgets Release Notes](<./Widgets_Release_Notes.md> "Widgets Release Notes")

### Overview

Widgets is a collection of extended components designed for building user interfaces. Currently all Widgets are contained in Widget components which are part of the Panel component family. The Widget component was derived from the Container component to support any specific features that might be required by the general Widget implementation effort, however, there has yet to be a single feature added beyond that of its predecessor. 

The first release of Widgets is a stripped down version of a larger, more feature rich system currently under development. This stripped down version will be known as “Basic Widgets”. The more feature rich system is known as “Advanced Widgets”. It is expected that both “Basic Widgets” and “Advanced Widgets” will exist into the future as parallel systems. 

The main advantage “Basic Widgets” will have over “Advanced Widgets” is there will be no custom Python extension code attached to “Basic Widgets”. This makes “Basic Widgets” less prone to issues when upgrading to new versions of TouchDesigner because “Basic Widgets” are self contained components while “Advanced Widgets” will rely on an external component housing a range a centralized functionality and a constantly evolving set of features developed using the Python extension system. 

“Basic Widgets” is much more like the legacy “TUIK” system, which was simply a folder of stand alone components. “Advanced Widgets” will support a more modern workflow with a range of supporting user interfaces for rapid development of complete TouchDesigner applications. 

Basic Widgets are extracted from Advanced Widgets so there should always be parity with the names and core functionality of each widget. Because “Advanced Widgets” is not yet public there is no need to know more at this time. The following Wiki article will cover some more differences when appropriate and will continue to evolve as more features roll out. 

## Widgets

Widgets are divided into 2 main groups: Master Widgets and Main Widgets. Master Widgets are singular functional user interfaces elements like a label, button, checkbox or field. Master Widget components always hold only a single element. They are called Masters because they are the clone master components that comprise the larger more comprehensive Main group. 

Widgets are designed to be used from the top level parameters only. The internal network that comprises a Widget should not be modified. Any changes made to the inside of a Widget will be lost when the Widget is updated. There is no need to go inside a Widget to customize the look or extract information. The Widget top level parameters should provide all the tools for utilizing the user interface element. 

### Where to Find Widgets

Widgets are found in the Palette under Derivative > UI > Basic Widgets

### Do Not Enter or Make Modifications to Widget Internal Networks

One of the core design paradigms for Widgets was that the system must be upgradeable. The previous user interface toolkit, called TUIK was not upgradeable. Once a component was deployed into a larger system it was essentially “lost in space”. If there was a bug or new feature desired for the component the only way to update would be to go back to the palette find the updated component and do a manual replace. 

Both “Basic Widgets” and “Advanced Widgets” support automated upgrading. The process is slightly different for each system, though in either case the Widget is cloned and therefore it’s internal network is wiped clean and replaced with the original Widget’s clone master. Therefore all changes to the inside of a Widget will be lost after an update. 

### What if there is a deficiency, bug or feature I want to add to a Widget?

In such case that there is a change desired to a Widget, the change should be requested to the forums or Derivative support just as with any other operator in TouchDesigner. In this sense Widgets is a closed system just like a Wave CHOP or Movie TOP is a closed system. 

### What if I want to make my own Widget?

Advanced Widgets will support the construction of custom Widget Kits. Therefore you will be able to design your own Widget kits utilizing the same underlying Widget architecture. All Widgets found in “Basic Widgets” are extracted from the TDWidgetKit component. TDWidgetKit will be the first user interface kit developed and maintained by Derivative. You will be able to make and maintain your own kit using the same Advanced Widget system. 

## Common Properties

Widgets have a range of common properties. These common features are stated here: 
* All Widgets are contained in a Widget COMP.
  * All Widgets have custom parameter pages.
  * All Widgets have a Widget page that controls general Widget features.
  * All Widgets have custom pages that control the specific Widget type. For example a Label Widget will have a Label page that controls the look of the Label.
  * All “Basic Widgets” are tagged TDBasicWidget.
  * All Widgets have a reference to their original master Widget by looking at the Clone Master parameter on the Common page.
  * All Widgets have a Parent Shortcut defined as “Widget”.
  * Most but not all Widgets have values.
  * Widgets values are limited to four values.
  * Widget values are found on the Values page.
  * Widgets values pass their values out the component output.
  * Numeric Widgets will values out via CHOP outputs.
  * String Widgets have DAT outputs.
  * Menu Widgets have CHOP and DAT outputs.

## Widget Values

Widgets can hold up to 4 values. Therefore a Widget can provide a user interface for representing all value types supported by TouchDesigner. The value types supported by TouchDesigner are as follows: 
* Float1
  * Float2
  * Float3
  * Float4
  * Int1
  * Int2
  * Int3
  * Int4
  * String
  * Boolean

### The Values Page

Widget values can be found on the first Custom Page of the Widget parameters. The page is called Values. If a Widget doesn’t have a Values page then it does not have values - for example a Label, Header or Footer will have no values. 

#### Value Parameters

Widget values are found on the Values page and based on the dimension from 1 to 4, the parameters that hold the values are respectively Value0, Value1, Value2 and Value3. Therefore an RGBA Color Widget holding Red Green Blue Alpha values will store Red in parameter Value0, Blue in parameter Value1, Green in parameter Value2, and Alpha in parameter Value3. 

#### Value Names

Values have a name. which is the name that will be passed out of the Widget via its CHOP or DAT output. 

#### Customizing Value Ranges and Defaults

Basic Widgets only supports changing parameter values using the Customize Component dialog. Advanced Widgets supports much more convenient features for setting default value, ranges and clamping behavior. 

### Running Scripts When Values Change

This feature is currently in flux. Next release will have been coverage for this. 

## Updating Widgets

To update Basic Widgets you must have the basicWidgets component loaded. This component holds the entire set of widgets - and it works in conjunction with the built in op.TDUpdater component. 

The basicWidgets component can be found in Derivative > UI > BasicWidgets palette folder. It is the only component in the folder and it is called basicWidgets. 

To update to a newer version simply drag basicWidgets into your file and click the “Update Deployed” button. There can only be a single basicWidgets component loaded per file. If there is another component loaded you will get a warning error “Multiply defined Global OP Shortcuts”. If you get this error simply locate the other basicWidgets component and delete it. 

Open the Textport when you update to view progress. You may delete the basicWidgets component once complete. 

## Widget Types

### TDWidgetKit Masters vs Main

Basic Widgets are extracted from the Advanced Widget system, from the Derivative designed Widget kit called TDWidgetKit. The difference between the Master Widgets and Main Widgets are more clear when looking in the Advanced system. Nevertheless these two groups are seperated by the two subfolders in the Basic Widgets palette folder. 

The WidgetKit Masters are Widgets that hold singular UI elements. These singular elements are cloned and reused as parts in the Main set of Widgets. For example, the masterButton Widget holds the button sub component that is used in many of the Main button widgets like buttonMomentary, buttonToggle and buttonState. The masterSlider Widget sub component can be found in the Main group inside sliderHorz, sliderHorzXFade and all color slider Widgets. 

These master subcomponents come with their own set of parameter pages that manifest on the Widget parameters. For example, the masterLabel Widget subcomponent comes with pages for Label and Label Align. The masterButton Widget subcomponent comes with parameter pages for Button and Button Align. The buttonMomentary Widget contains both the masterLabel subcomponent and the masterButton subcomponent so it has Widget pages for Label, Label Align, Button and Button Align. 

## Master Widgets

Master Widgets hold a single Widget subcomponent. Therefore each masterWidget has only a Values page where applicable a Widget page and the parameter pages for the Widget subcomponent that it holds. 

### Window Parts and Labels

These Widgets have no values. They are very basic labels and section headers. 

#### masterHeader

Simply a header for the top of a panel or group of widgets. 

#### masterFooter

Simply a footer for the bottom of a panel or group of widgets. 

#### masterLabel

The masterLabel widget holds the label sub component that is used across all Main Widgets. 

#### masterSection

This is a section control that can be used to create a collapsible section of Widgets. 

#### masterValueLabel

The value label is a smaller value label used in Widgets with multiple values, like RGB and HSV color sliders. 

### Buttons and Toggles

Buttons and Toggles generally hold boolean values or integer values of either 0 or 1. However the masterButtonPush Widget has no values. 

#### masterButton

This is the standard button Widget for most use cases. It has a single value, and can be setup to support a wide range of button behaviors by settings the Button Page, Type parameter. 

#### masterButtonPush

This button does not have a value and is a simple momentary button, generally used in cases where the button supports behavior on a compound Widget in the Main section. For example the fieldFileBrowser and fieldFolderBrowser use this subcomponent to launch the operating system browser. 

#### masterRadioButton

This Widget has a single integer value, where integer value indicates what radio button is currently active. Use the Button Page, Button Labels parameter to define both the labels and the number of buttons that are desired. Use a space between text to define each button. For labels with spaces in the name use quotes. 

#### masterCheckbox

Holds a single boolean value parameter and supports generic checkbox behavior. 

#### masterRocker

Holds a single boolean value parameter and supports analogous behavior to the built in Toggle custom parameter. 

### Fields

#### masterNumericField

Provides a single value for storing either float or integer value types. When setting up either float or integer value types you must use the Field Page, Field Type parameter as well as use the component editor to set the Value parameter to the correct parameter type. To avoid these issues it is strongly recommended to use the pre-setup Main widgets of float1, float2... int1, int2 parameters. Advanced Widgets will have greater support for changing value types easily. 

#### masterStringField

This is the main Widget for setting and storing String values. 

### Sliders

Sliders are a general class of Widget that is used for selecting and moving the mouse to interactively change a value. 

#### masterSlider

The masterSlider supports Value Types for float and integer. In Basic Widgets the component editor must be used to modify the range and Value Type value parameters. 

#### masterSlider2D

This Widget controls 2 values at once. In Basic Widgets the component editor must be used to modify the range and Value type of sliders. 

#### masterRange

This Widget controls 2 values at once and supports Value Types for float and integer. In Basic Widgets the component editor must be used to modify the range and Value Type value parameters. It is useful to control ranges like start and end or minimum and maximum. 

#### masterKnob

This Widget controls a single value and supports Value Types for float and integer. In Basic Widgets the component editor must be used to modify the range and Value Type value parameters. 

### OP Reference

#### masterReferenceOP

This Widget is in flux. Use at your own risk. Updates coming next release. Updates will work but may cause loss of data. 

### Item Menus

This class of Widget are defined using the Menu Page, Menu Names parameter. They hold a single string value. Delimit each folder name with a space. In TouchDesigner all parameter menus have a menu name which is lowercase and no spaces, as well as menu labels that can have spaces. Therefore the Menu Widget follows this requirement. To define menu names use the Menu Page, Menu Names parameter. Delimit each name with a space. To define different label names for the visual pop up menu, use the Menu Labels page to use different names. Spaces may be use for individual labels here using quotes to enclose the string. 

#### masterFolderTabs

Supports a menu Value parameter that returns a string. Each folder tab is defined using the Menu Page, Menu Names parameter as indicated in the Item Menus header sectio directly above. 

#### masterDropMenu

Suuport a menu Value parameter that returns a string. Each menu item is defined using the Menu Page, Menu Names parameter as indicated in the Item Menus header sectio directly above. 

### Lists

List Widgets do not hold values as the definition of a list and its behavior is quite involved. For now refer to here: <https://www.derivative.ca/wiki099old/index.php?title=Palette:lister>

#### masterList

Text 

## Recommended WorkFlow

The widget system sits at the center of a new paradigm for approaching component building and general authoring in TouchDesigner. The widget system has only now started to roll out as some of the necessary core features have finally been completed, the most recent of which is parameter binding. This new workflow paradigm will be rolling out in stages over the next year. 

The first phase of this rollout is Basic Widgets. Basic Widgets are rolling out in such a way as to conform with the traditional process of building user interfaces (TUIK) by manually assembling them using the network editor and panel components. However once Advanced Widgets begins to roll out, much of the tedious work that goes into building panels and components in TouchDesigner will be automated and augmented with a WYSIWYG interactive panel authoring user interface. 

This automated workflow follows a particular methodology that can also be carried out manually. Many TouchDesigner developers already follow this methodology when building components to some degree or other. Once Advanced Widgets is fully rolled out, this workflow and component architecture will be shared by all components developed with the system. This in turn will lead to higher compatibility between user developed components, as well as easier readability of other designer works because all components will be following the same paradigm. 

Therefore it important to understand this workflow so it’s easier to read and understand networks, and also provides a clear well tested approach to working and building systems in TouchDesigner. 

Key features related to the widget effort to be aware of are as follows… 
* Parent shortcuts and OP shortcuts
  * Custom Parameters
  * Component layout improvements
  * Parameter binding
  * Parameter optimizations - parameter caching

## Adding Material Design Icons

Widgets support unicode icons fonts as well as regular fonts. TouchDesigner includes the [Material Design Icons](<./Material_Design_Icons.md> "Material Design Icons") font which can be used to create nice looking icons in places where normally text will go. Any label parameter will take unicode strings as long as the selected font supports the uncide codes. 

### Using Material Design Icons

To pick and icon scoll through the list of icons on the Material Design Icons Cheat Sheet. TouchDesigner 2020.40000 series of builds ships with version 5.3.45 of the Material Design Icons. Follow the link to the cheat sheet which is accessed using the cheat sheet button located here: <https://materialdesignicons.com> \- The icon font library is often updated so make sure you are using the correct cheatsheet for the version included. Newer versions will contain icons not available in older versions, and may also replace some icons. 

Click the HexCode beside each icon thumbnail and it will copy the hexidecimal string to the copy buffer. The string that is copied is just a hexidecimal index number but it must be made into a python compatible hexidecimal format by presceding the regular string with a '0x'. For example, if the hex code that was copied is 'F0EF4' the python hexidecimal notation is 0xF0EF4. Therefore, in TouchDesigner paste the hexidecimal string code into an expression of the format...`chr(0xPASTE)`or more specifically in the case of 'F0EF4'`chr(0xF0EF4)`
