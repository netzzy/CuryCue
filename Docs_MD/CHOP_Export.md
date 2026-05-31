# CHOP Export

CHOP exporting sends the number values in a CHOP channel to a [Parameter](<./Parameter.md> "Parameter") of any operator.   
  
There are numerous ways to export CHOP channels in TouchDesigner. 

**TIP:** it is better to export from a [Null CHOP](<./Null_CHOP.md> "Null CHOP") so you can add various CHOPs inline to the network without the need to re-export from another CHOP. 

For exporting from DATs, see also: [DAT Export](<./DAT_Export.md> "DAT Export"). 

## How to Export Channels from CHOPs

### Exporting from a CHOP Viewer
1. Make sure you have the parameter you want to export to visible somewhere on your interface. For example, select the OP and display its parameters by pressing 'p' hotkey, or open a floating parameter dialog for that OP.
  2. Turn on the [Viewer Active Flag](<./Viewer_Active_Flag.md> "Viewer Active Flag") of the [Node Viewer](<./Node_Viewer.md> "Node Viewer") for the CHOP you wish to export from, if it is not already on.
  3. Drag a channel from the viewer to the parameter. When dropped, select **Export CHOP** from the pop-up menu. Note the parameter goes green indicating it's being exported-to.


**TIP:** You can quickly get to the parameters you need by momentarily hovering the dragged channel over the target OP, this will bring up that OP's parameter page. From there you can hover the dragged channel over any of its parameter tabs to switch to that tab of parameters, then drop onto your desired parameter. 

### Using Export by Channel Name

You can setup export by channel name by selecting **Channel Name is Path:Parameter** in the **Export Method** parameter on the Common page of any CHOP. CHOP channels will automatically be exported if the channel name can resolve to the path:parameter in the file. '`:`' and/or '`/`' are used as separators for the paths and parameter. For example a channel named`geo1:tx`, will get exported to a node named`geo1`, parameter`tx`, if it exists. The node is searched for starting at the node that the **Export Root** parameter refers to. Usually the Export Root is left as default, which is '`parent()`' in python. This means "start searching at my parent". So for the above example, the CHOP will need to be in the same network as`geo1`for the export to work. The channel names can contain paths, such as`container1/geo1:tx`. which will search for`container1/geo1`(relative to the Export Root), parameter`tx`. You can use`/`and`:`in the channel names interchangeably for this feature, however a good convention to follow is use`name1/name2`for the path to the node, followed by a`:`to separate the node from the parameter name. 

**Note:** In a CHOP using Export by Name, all channels export if they can resolve to a parameter. You can not individually disconnect channels from this method of exporting, its all channels or none. To remove a channel that is exporting, you need to select/delete/remove that channel from the input so it is no longer reaching the exporting CHOP. 

## How to Confirm Exporting

### From the Parameter

A parameter that is exported-to will be highlighted in green. Clicking on the parameter name to display the parameter’s expression will display the path to the CHOP channel that is overriding the parameter. Alternatively you can right-click on the parameter's name and the pop-up menu will display an option to **Jump to Export CHOP**. Selecting this will take you directly to the CHOP the data is exported from. 

### From the CHOP

If you go back and inspect the CHOP that the channel originates from, you will notice that the [Export Flag](<./Export_Flag.md> "Export Flag") is now on. You can toggle this flag on/off to activate/deactivate the export from this CHOP. 

You can also quickly check if the a channel is exporting by holding down middle mouse button on a CHOP and inspecting the pop-up help info. The path reported to the right of the channel’s values is the path the channel exports to. This is convenient for a quick check, but it will not display multiple paths if the channel exports to multiple parameters (The first parameter’s path will be followed by ... if there are other parameter export paths). 

## Discovering Where the Channel Comes From

### What if you forget where the parameter’s overriding channel is coming from?

Simply hold right mouse button down over the overridden parameter. When the pop-up menu appears, the last entry will be **Jump to Export CHOP** /CHOP’s path. You can then navigate your networks to this node, or selecting this menu option will take you directly to the node that is exporting the channel. 

## Removing an Export Connection

### Disabling a CHOP’s Exports
1. To disable all the exporting channels coming out of a CHOP, simply turn off that CHOP’s Export flag.
  2. Disabling the Export flag will stop all channels from exporting from this CHOP.
  3. Change the [Parameter Mode](<./Parameter_Mode.md> "Parameter Mode") from Export to Constant or Expression.

### Removing a Single Export
1. On the parameter being exported to, right-click and select **Remove Export**. NOTE: That will only remove the export from one channel from the exporting CHOP, and this is not possible when using the Export Method **Channel Name is Path:Parameter** described above.

## Tips

### Exporting from Null CHOPs

It is good practice to always export channels from a [Null CHOP](<./Null_CHOP.md> "Null CHOP") appended to the end of your network. 

The reason for this is simple. If you export from the last node in your network, but decide later that you need to filter the data further, you would have to append the new filter CHOP and then redo all your export connections form this new node. Using a Null CHOP at the end of your network as an exporting place holder, you can always insert another node into the network directly before the Null. This will keep all your export connections intact. 

It is also helpful to rename your Null CHOP to reflect the destination, like _toGearSpeed_. 

### Exporting to Toggles and Menus

Toggle checkboxes and parameter menus can be exported to as well. Drag & Drop the channel over the checkbox or menu, then select **Export CHOP** from the pop-up menu. 

For toggle checkboxes, values 0 and less are 'off' and values greater than 0 are 'on'. For parameter menus, the first menu entry is selected when the CHOP channel value is 0, the second is selected when the value is 1, the third when the value is 2, and so on. 

### Using Expressions in Parameters

CHOP Exporting is normally set up from the CHOP channel to the parameter by drag & dropping the channel to the parameter. Alternatively, parameters can reference a CHOP channel using an expression in the parameter. This is a more parameter-centric approach, and the same expression can be used in multiple parameters. In python, use an expression like`op('wave1')['chan1']`to get a CHOP channel's value. 

For example, for the CHOP`/project1/stimulate/math6`and channel`vidproc_motion`, the following Python expression could be used:`op('/project1/stimulate/math6')['vidproc_motion']`
