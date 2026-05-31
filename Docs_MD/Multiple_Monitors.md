# Multiple Monitors

## Output to Multiple Monitors  
  
Multiple monitors are also known as: second monitor, multi-monitors, right monitor, dual monitors, multi-display. 

TouchDesigner can send video out to multiple projectors, monitors and recorders. TouchDesigner can run single-monitor or across many monitors. 

Most modern graphics cards allow for at least 4 outputs. The easiest way to get more outputs is to use splitters such as [QuadHead2Go](<https://www.matrox.com/en/video/products/video-walls/quadhead2go-series>) or [Datapath Fx4](<https://www.datapath.co.uk/datapath-products/video-wall-controllers/datapath-fx4/>) monitor expansion devices. 

Laptops all have different multi-monitor capabilities based on the manufacturer's specifications. Sometimes a laptop will have many output connections but still have limitations on the number of monitors it can drive simultaneously. Refer to the specifications for your specific laptop to understand its capabilities. 

### Spanning Monitors for Best Performance

TouchDesigner will run fastest in [Perform Mode](<./Perform_Mode.md> "Perform Mode") if you combine all your panels into one canvas that spans across all your monitors. This can be done easily with [Container COMPs](<./Container_COMP.md> "Container COMP"), then by assigning this to the [Window COMP](<./Window_COMP.md> "Window COMP") that is set for Perform Mode in the [Window Placement Dialog](<./Window_Placement_Dialog.md> "Window Placement Dialog"). Using multiple Window COMPs is not suggested, and will result in poor performance. 

Example for two 1920x1080 monitors [File:PerformMode Windows.toe](</File:PerformMode_Windows.toe> "File:PerformMode Windows.toe")

### Windows
* On the Desktop background, right-click -> Display Settings -> Multiple Displays -> Extend These Displays.

#### Combining Monitors into a Single Virtual Monitor Even Better Performance

If possible, you should also join your monitors together into a single virtual monitor using [Nvidia Mosaic](<./Nvidia_Geforce_vs_Quadro.htm#Mosaic> "Nvidia Geforce vs Quadro"), Nvidia Surround or AMD EyeFinity. 

### macOS
* System Preferences -> Displays -> Arrangement -> Mirror Displays = Off.


To allow monitor spanning on macOS, make sure the following is also set 
* System Preferences -> Desktop & Dock -> Mission Control -> Displays have separate Spaces = Off

### Additional Setup Tips
* [Window Placement Dialog](<./Window_Placement_Dialog.md> "Window Placement Dialog") can be used to quickly assign Perform mode to different Window COMPs, and adjust parameters, jump to the network, and open/close the windows.
  * [Perform Mode](<./Perform_Mode.md> "Perform Mode") can be turned On and Off with the [Shortcut](<./Shortcut.md> "Shortcut") keys F1 (On) and Esc (Off).
  * The **Always on Top** parameter in the Window COMP forces TouchDesigner to always be the top-most visible window.


See also [Using Multiple Graphic Cards](<./Using_Multiple_Graphic_Cards.md> "Using Multiple Graphic Cards"), [Window COMP](<./Window_COMP.md> "Window COMP"), [Window Placement Dialog](<./Window_Placement_Dialog.md> "Window Placement Dialog")
