# Dialogs:Preferences Dialog

## Description

**Preferences** is a dialog for setting personal default settings for various TouchDesigner options. These preferences are found in the _Edit_ menu under _Preferences..._. These options are saved so they apply to your next TouchDesigner session. These are split into several pages. The images below provide a summary of the initial default preferences after installation. 

**Note:** The preference file can be found here: 

Windows`C:/Users/_username_ /AppData/Local/Derivative/TouchDesigner099/pref.txt`macOS`~/Library/Application Support/Derivative/TouchDesigner/pref.txt`## General Preferences

Increment Filename when Saving - When **On** name of your .toe file will have a number suffix increments every time you save the file. This does not happen with _Save As_ , only with _Save_. When set to **On and Copy to Backup Folder** then the extra numbered .toe files will be placed in folder called Backup in the project's location on disk. 

Create Link Filename when Saving - Creates a file that with no number increment that is the same as the most recent file saved. This makes it easy to open the most recent file. 

Prompt to Save on Exit - If **Prompt to Save on Exit** is enabled, a pop-up dialog will appear whenever you attempt to close TouchDesigner. You will be prompted to either **Save & Quit**, **Discard & Quit**, or **Cancel**. The value of **Increment Filename when Saving** will be honored when you select **Save & Quit**. 

Stop Playing when Minimized - When enabled, animation will stop playing forward when the main TouchDesigner window is minimized. Once the window is reopened, playback will continue. On/Off Parameter Behavior - This sets how the On/Off toggles in parameter dialog function. Choose between clicking anywhere to toggle the state or specifically clicking on the left side for Off and right side for On. 

Enable Warning Sounds - An short sound will be played whenever a warning dialog is triggered. 

Enable [Playbar](<./Timeline.md> "Timeline") Shortcuts - Turn off to disable keyboard shortcuts for TouchDesigner's main [Playbar](<./Timeline.md> "Timeline"). 

Check for Experimental Builds - Includes Experimental builds when checking for available updates. 

Help Tags - Enable or disable help pop-ups in the interface. 

Startup File Mode - Choose whether TouchDesigner starts with a default project, an empty project, or a custom project 

Custom Startup File - If Startup File Mode is "Custom File", use this file. Path to file must be absolute. 

Default Node Language - Determines whether new operators are created in Python Mode (default) or Tscript mode. 

Add External Python to Search Path \- When enabled TouchDesigner will automatically add python33 installation folder into the module search path. 

Python 64-bit Module Path \- Additional search paths for python module search. 

Search External Python Path Last - Prioritize default Python modules. Determines if the above provided path is search first before any built-in search paths, or last after the built-in paths are searched. 

Hide Splash Screen - When this is turned on, the splash screen will not show when TouchDesigner starts up. This feature is only available in Commercial and Pro. 

Show Value Ladder Increment - 

Value Ladder Step Size - 

Mouse Click Radius - Number of pixels mouse clicks cover. Helpful for using stylus or other devices where double clicking on the same pixel is difficult or other accuracy issues arise. 

Use Alt+Right-Click alternative for Middle-Click - useful when you don't have a middle mouse button 

Show Startup Errors - Show nothing, just warnings, or all errors on startup. 

Display Last Script Change in Parameter Popup Help \- When on, if a parameter is changed by a script, hovering over it will display info about the change. 

## Network Preferences

Center Zoom on Mouse - Zooms the Layout Area in the Network Editor so that the point right beneath the mouse cursor is the center of the zoom. 

Resize TOP Nodes to TOP Viewer Aspect - When selected, the size of TOP node will be locked so that the OP Viewer will not distort the underlying TOP. 

Resize Panel COMP Nodes to Controlpanel Aspect - When selected, the size of Panel node will be locked so that the OP Viewer will not distort the underlying Panel. 

Mouse Wheel Navigation - Allows users to move up and down the OP hierarchy by using the mouse wheel. 

Jump Up When Network Zoomed - Sets the network zoom level which when reached will cause TouchDesigner to move up a level in the OP hierarchy. 

Scroll Wheel Zoom Boost - A multiplier on the scroll wheel zooming feature. The higher the number, the quicker the network will zoom in and out on mouse wheel scrolls. 

Middle Mouse Button Zoom Boost - A multiplier on the middle mouse button zooming. The higher the number, the quicker the network will zoom in and out using the middle mouse button. 

Translate/Zoom Delay (sec) - Amount of lag in seconds added to translate or zoom operations on a network. 

Operator Name Max Size (pixels) - Maximum height in pixels that operator names will appear in a network when zooming in. 

Fixed-size Operator Names - If selected, operator names will not shrink and grow as the network is zoomed in and out, but instead will maintain a constant size through all network transformations. 

Node Viewer On by Default - Turn on the Node Viewers on all OPs by default. 

Turn on Node Viewers when Entering Network - Turn on the Node Viewers on all OPs in a network when the network is first entered. 

Viewers Active On Click Select - Turn on the Node Viewer of an OP when it is selected by clicking on the OP. 

Cache Node Viewers - Remember viewer layout for quicker navigation back and forth between networks. 

Show Network Editor Grid - Show grid on network background. 

Grid Brightness - If network grid is visible, adjust the brightness of the grid relative to the background. 

Snap to Grid - Sets the size of the grid to snap to for nodes. Can be set to **Off** , **Coarse** or **Fine**. 

Snap to - Sets the part of the node that will snap to the grid. Can be set to **Lower Left Corner** or **Node Center**. 

## Geometry Preferences

Keep Position when Parenting - If unchecked, objects will assumed a position relative to the parent object when parented. Leaving the selection checked will allow objects to keep the world position. 

Default Geometry Viewer Mode - Specify if geometry viewers start in 'Camera View' mode to inspect and navigate the scene or 'Select & Transform' mode to select geometry and manipulate it. 

Geometry Viewer BG Color - Adjust the grayscale level of [Geometry Viewer](<./Geometry_Viewer.md> "Geometry Viewer")'s background color. This is reflected in all 3D viewers including Object Component viewers, SOP viewers, and MAT viewers. 

Adaptive Homing by Default - All new 3D Viewers created will have Adaptive Homing turned on. 

Grid Visible by Default - All new 3D Viewers created will have Grid turned on. 

Tumbling Pivot Visible - Turn on or off the indicator for tumble pivot while pivoting. 

## TOPs Preferences

Viewer Background - Change between a **Checker Board** or a **Black** background for TOPs. 

Global Resolution Multiplier - Multiplier for default resolution in all TOPs. 

Default Viewer Fill Mode - New TOPs will be created with this setting for 'Viewer Fill Mode', which determines how the TOP image is displayed in the viewer. 

Default Viewer Smoothness - New TOPs will be created with this setting for 'Viewer Smoothness', which controls the pixel filtering in the viewer. 

## CHOPs Preferences

Maximum Time Slice Size (frames) - Sets an upper bound on the number of frames a time-sliced CHOP will process between successive screen updates. The default limits a time slice to be 6 frames). 

Minimum Text Size - The minimum text size used for [Time Sliced](<./Time_Slicing.md> "Time Slicing") CHOP viewers. 

Maximum Text Size - The maximum text size used for [Time Sliced](<./Time_Slicing.md> "Time Slicing") CHOP viewers. 

Graph Color - Sets the start color used when assigning colors to channels in CHOP graph viewers. 

Hue Steps - Sets the number of distinct hues assigned to the channels. After this number of colors is assigned, additional channels reuse the hues but apply the Value Multiplier below. 

Value Multiplier - After the number of colors specified in Hue Steps are assigned, additional channels reuse the hues but apply this Value Multiplier. This process is repeated as the Value Multiplier is reapplied each time the colors cycle through the number of Hue Steps. 

Value Minimum - Sets a minimum value for the colors assigned. 

Graph Style - Sets the way colors are assigned to the channels. 
* Set Color by Channel Order - Uses the channel order to assign colors.
  * Set Color by Channel Name - Uses the channel names to assign colors.
  * Set Color by Path and Channel Name - Uses the path and channel names to assign colors.


Graph Display - Sets the default display mode for graph viewers. 

## DATs Preferences

File Format - Select the file format that the text will be stored in. Choose from **Windows** or **Unix**. 

Minimum Text Size - Sets the minimum height in pixels for text when zooming out. 

Maximum Text Size - Sets the maximum height in pixels for text when zooming in. 

Preferred Text Size - Sets the preferred text size. Text will default to this size if not zoomed out or zoomed in too far. 

Auto Indent - When enabled, pressing enter for new line will start the next line at the same level of indentation. 

Show Indentation - Make indentation characters visible in DATs 

Display Line Numbers - Displays line numbers for DATs with text data. 

Display Row Numbers - Displays row numbers for DATs with table data. 

Display Column Numbers - Displays column numbers for DATs with table data. 

Text Editor - Specify the external editor to use when editing text in DATs. Launch by RMB-clicking on DAT and selecting **Edit Contents...**

Table Editor - Specify the external editor to use when editing tables in DATs. Launch by RMB-clicking on DAT and selecting **Edit Contents...**
