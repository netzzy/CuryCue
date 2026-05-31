# Write a CPlusPlus Plugin

The CPlusPlus OPs ([CPlusPlus CHOP](<./CPlusPlus_CHOP.md> "CPlusPlus CHOP"), [CPlusPlus TOP](<./CPlusPlus_TOP.md> "CPlusPlus TOP"), [CPlusPlus POP](<./CPlusPlus_POP.md> "CPlusPlus POP"), [CPlusPlus SOP](<./CPlusPlus_SOP.md> "CPlusPlus SOP") and [CPlusPlus DAT](<./CPlusPlus_DAT.md> "CPlusPlus DAT")) allow you to load your own C++ code that has been compiled into a plugin. You can use this node to create custom filters, output to some custom file format or device, or to bring data in from some custom device or file format. Depending on the type of OP the input/output, behavior and function names will be different, but the general idea is the same. Although these OPs are not the same as a full SDK, they provide much of the same functionality. 

The same code used to create a plugin to be used for a CPlusPlus node can also be used to create a [ Custom Operator](<./Custom_Operators.md> "Custom Operators") as well. 

A collection of samples is available at the [following Github repository](<https://github.com/TouchDesigner/CustomOperatorSamples>). More basic examples are also available in the Samples/CPlusPlus folder in the installation folder. 

## Interface Summary

TouchDesigner defines a base C++ class that you will inherit from to you create your own class. There are some pure-virtual functions you are required to override, while there are others that will do some default behavior of you don't provide an overridden method. Data is passed in and out of the functions using other simple classes which hold the information. 

To initialize the plugin and create an instance of the class there are 3 C functions you are required to specify. The first one will tell TouchDesigner which version of the API you are running (by returning a constant which you can see in the header file). The other two will create (using`new`) and destroy (using`delete`) an instance of the class when TouchDesigner asks them to. A single instance of the class will get created for each OP that is using the plugin. 

## Sample Code

You can find code to get started making the plugin in the`Samples/CPlusPlus/`folder, select "Browse Samples" from the Help menu in TouchDesigner. In this folder there is a sub-folder for each type of CPlusPlus Operator (CHOP and TOP), that contains all the source code as well as Visual Studio Solution and Project file and an Xcode project. 

There will be a base class defined in a header file (for example`TOP_CPlusPlusBase.h`) which should not be edited. You will make a child of this base class. An example child class has already been provided in the sample directory. Much of the information you will need to program a plugin will be in the comments of these files, as well as the base class header file. 

When you have examined the sample code and are ready to make your own plugin, use the sample code as a template for your own project. 

## General Work flow

In general when the CPlusPlus OP cooks it will call some functions in your class which are asking some questions (for example, if the node should cook every frame). It will then call the`execute()`function where your class should do the actual work. 

## Developing plugins on Windows

### Compiling

Plugins on Windows are built as a DLL. The sample was created and compiled using Visual Studio 2015. 

Build products are placed alongside the project. 

### Debugging

You can attach the Visual Studio debugger to`TouchDesigner`when it's running. Breakpoints in your plugin code will behave as normal. This is also a good way to explore all the data structures TouchDesigner passes in and out of the functions. 

To launch your project with the debugger already attached in Visual Studio, go to the project properties and under the debugging section put in the full path to`TouchDesigner.exe`in the 'Command' section. If you have a`.toe`file already setup, put that in the 'Command Arguments' section. Now you can hit F5 and your project will load up inside TouchDesigner with the debugger already attached. You'll get an error saying there is no debug information for`TouchDesigher.exe`, but that's expected. You'll have debug information for your .`dll`when the process is executing your code. 

### Seeing Console Output

To see print statement output, use`std::cout`and set a windows environment variable TOUCH_TEXT_CONSOLE=1 and you will have a black console window that will show your print statements (as well as some debug statements from TouchDesigner in general). **Note** : printing lines of text to the console window has a large impact on performance. Be sure to disable all printing when performance testing or shipping a finalized plugin. 

## Developing plugins on macOS

### Compiling

Plugins on macOS are built as a bundle named with a .plugin extension. The sample will open and build with the latest version of Xcode on macOS. 

Unlike Visual Studio, Xcode doesn't keep build products alongside project source code. 
* To create a finished plugin for distribution, you create an Archive build using Product > Archive and then Export... and Save Built Products.
  * To use a debug build during development and testing, use Product > Build in Xcode, then Product > Show Build Folder in Finder, then your plugin will be in Products/Debug. Now switch to TouchDesigner and place a CPlusPlus CHOP or TOP and hit the + button beside the Plugin Path parameter, switch back to the Finder, and drag the plugin to the choose file dialog on-screen from TouchDesigner. You can save the`.toe`to use for debugging so you don't have to repeat this (see the next section).

### Debugging

You can attach the Xcode debugger to`TouchDesigner`when it's running. Breakpoints in your plugin code will behave as normal. This is also a good way to explore all the data structures TouchDesigner passes in and out of the functions. 

To launch your project with the debugger already attached, edit the project's scheme (Product > Scheme > Edit Scheme...) so its Run target has`TouchDesigner`as its executable in the 'Info' section. If you have a`.toe`file already setup, put the path to that in the 'Arguments' section. Debugging will operate as normal. 

### Seeing Console Output

Messages sent to`std::cout`will appear in the console in Xcode's Debug area. **Note** : printing lines of text to the console has an impact on performance. Be sure to disable all printing when performance testing or shipping a finalized plugin. 

## Python

Your plugin can interface with Python both by providing a custom Python class that exposes methods and members users can access, as well as calling Callback DAT Python callbacks. See the CHOPWithPythonClass sample project for examples of how to do this. **Note: Python only works when the Plugin is installed as a[Custom Operator](</index.php?title=Custom_Operator&action=edit&redlink=1> "Custom Operator \(page does not exist\)"). It does not work when used within a CPlusPlus node.**

## Info CHOP and Info DAT

All of the CPlusPlus OPs support outputting data through the Info CHOP and Info DAT. There are functions where you can specify how much data you want to output, and then others where you specify the actual data you want to output. 

## How to Use Custom Parameters

Both the [CPlusPlus CHOP](<./CPlusPlus_CHOP.md> "CPlusPlus CHOP") and the [CPlusPlus TOP](<./CPlusPlus_TOP.md> "CPlusPlus TOP") support [Custom Parameters](<./Custom_Parameters.md> "Custom Parameters"). There are two main functions associated with the creation and management of [Custom Parameters](<./Custom_Parameters.md> "Custom Parameters"). The first is the`setupParameters()`function and the second is the`pulsePressed()`function. 

The`setupParameters()`function is where all [Custom Parameters](<./Custom_Parameters.md> "Custom Parameters") should be defined. The example below shows how to create a RGB custom parameter: 
[code] 
    {
    	OP_NumericParameter	np;
    
    	np.name = "Color1";
    	np.label = "Color 1";
    	np.defaultValues[0] = 1.0f;
    	np.defaultValues[1] = 0.0f;
    	np.defaultValues[2] = 0.0f;
    
    	for (int i=0; i<3; i++)
    	{ 
    		np.minValues[i] = 0.0f;
    		np.maxValues[i] = 1.0f;
    		np.minSliders[i] = 0.0f;
    		np.maxSliders[i] = 1.0f;
    		np.clampMins[i] = true;
    		np.clampMaxes[i] = true;
    	}
    	
    	manager->appendRGB(np);
    
    	OP_NumericParameter	npDir;
    
    	npDir.name = "Dir";
    	npDir.label = "Direction";
    	npDir.defaultValues[0] = 1.0f;
    	npDir.defaultValues[1] = 0.0f;
    	npDir.defaultValues[2] = 0.0f;
    
    	manager->appendXYZ(npDir);
    }
    
[/code]

The code snippet below demonstrates fetching the value of the [Custom Parameters](<./Custom_Parameters.md> "Custom Parameters") discussed above, 'Dir'. 
[code] 
    double dirx = (float)inputs->getParDouble("Dir", 0);
    couble diry = (float)inputs->getParDouble("Dir", 1);
    double dirz = (float)inputs->getParDouble("Dir", 2);
    
[/code]

Similarly this may be done in a single call: 
[code] 
    double dirx, diry, dirz;
    inputs->getParDouble3("Dir", dirx, diry, dirz);
    
[/code]

RGB and RGBA attibutes should be evaluated using`getParRGB(), getParRGBA()`so color space conversions can be done to the values, when doing [Color Space Workflows](<./Color_Space_Workflows.md> "Color Space Workflows"). 
[code] 
    double r, g, b;
    inputs->getParRGB("Color", r, g, b);
    
[/code]

  
Adding the [Custom Parameters](<./Custom_Parameters.md> "Custom Parameters") to the`manager`class as noted above, allows [Custom Parameters](<./Custom_Parameters.md> "Custom Parameters") value's to be retrieved from the`inputs`class. 

The second important function is the`pulsePressed()`function. This function allows you retrieve the name and values of custom pulse parameters. Below is the definition of a pulse parameter from the`setupParameters()`function in the`OpenGLTOP.cpp`source: 
[code] 
    // pulse
    {
    	OP_NumericParameter	np;
    
    	np.name = "Reset";
    	np.label = "Reset";
    	
    	manager->appendPulse(np);
    }
    
[/code]

To run code based on the 'Reset' pulse parameter, we can check the name argument passed to the`pulsePressed()`function, as per the example below from the`pulsePressed()`function in the`OpenGLTOP.cpp`source: 
[code] 
    if (!strcmp(name, "Reset"))
    {
    	myRotation = 0;
    }
    
[/code]

## Custom Parameters Class Definitions

Because Custom Parameters extend existing classes, the definition of those classes be found in the`CPlusPlus_Common.h`source file accompanied with all of the sample CPlusPlus examples. The class definitions are:`OP_ParameterManager`\- The manager class that contains functions to add custom parameters.`OP_NumericParameter`\- The class to define for numeric value fields such as pulse buttons, toggles, float parameters, integer parameters, etc.`OP_StringParameter`\- The class to define string based fields such as string entry, file or folder references, Operator references, menu items, etc. 

## See Also

[Write a CPlusPlus TOP](<./Write_a_CPlusPlus_TOP.md> "Write a CPlusPlus TOP")  
[Write a CPlusPlus CHOP](<./Write_a_CPlusPlus_CHOP.md> "Write a CPlusPlus CHOP")  
[Write a CPlusPlus DAT](</index.php?title=Write_a_CPlusPlus_DAT&action=edit&redlink=1> "Write a CPlusPlus DAT \(page does not exist\)")  
[Write a CPlusPlus POP](<./Write_a_CPlusPlus_POP.md> "Write a CPlusPlus POP")  
[CPlusPlus TOP Upgrades For 2022.20000 Builds](<./CPlusPlus_TOP_Upgrades_For_2022.md> "CPlusPlus TOP Upgrades For 2022.20000 Builds")
