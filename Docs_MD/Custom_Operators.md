# Custom Operators

## Overview  
  
A Custom OP can be created for a [TOP](<./TOP.md> "TOP"), [CHOP](<./CHOP.md> "CHOP"), [SOP](<./SOP.md> "SOP"), and [DAT](<./DAT.md> "DAT") types. A Custom OP is an operator created by a 3rd party using TouchDesigner's C++ API, but they behave just like the built-in operators that TouchDesigner has. Custom OPs are very similar to the [CPlusPlus TOP](<./CPlusPlus_TOP.md> "CPlusPlus TOP"), [CPlusPlus CHOP](<./CPlusPlus_CHOP.md> "CPlusPlus CHOP"), [CPlusPlus SOP](<./CPlusPlus_SOP.md> "CPlusPlus SOP"), and [CPlusPlus DAT](<./CPlusPlus_DAT.md> "CPlusPlus DAT") operators, but they have their own unique names and appear in the OP Create menu for better integration in TouchDesigner. Use them like regular built-in operators. 

### Security and Safety

Since a Custom OP is created with binary code that is loaded and executed in TouchDesigner, it can contain malicious code. To help with this, before loading any binary TouchDesigner will check if that binary has been loaded on that machine before. If being loaded for the first time, a dialog will be presented asking for permission to load it, and if so then a signature for that binary will be saved into a .json file in the plugins directory. If the binary changes, then the user will be prompted again to load the new binary. 

## Using Custom OPs - Plugin Folder Locations

Custom OPs are used by simply placing the plugins in the correct location on disk. They will be detected when TouchDesigner starts. On Windows a plugin is a .dll file, with possible extra files included with it. On macOS a plugin is a .plugin folder. 

The Windows location is:`Documents/Derivative/Plugins`Which is usually:`C:/Users/<username>/Documents/Derivative/Plugins`On macOS the location is:`/Users/<username>/Library/Application Support/Derivative/TouchDesigner099/Plugins`If this directory does not exist on your computer, you can just create it. 

Plugins can be placed in this directory directly, or placed in another directory contained within Plugins, with any name, to organized the plugins as desired. For example, the plugins directory could contain: 
[code] 
    Documents/Derivative/Plugins/wave2.dll
    Documents/Derivative/Plugins/Company1/feature1.dll
    Documents/Derivative/Plugins/Company1/feature2.dll
    Documents/Derivative/Plugins/Mine/customMerge.dll
    
[/code]

The Custom OPs defined by wave2.dll, feature1.dll, feature2.dll and cusotmMerge.dll would all be loaded. 

### Project Specific Custom OPs

Along with the system wide Plugins folder listed above, a Plugins folder can also be placed next to the .toe file that is opened. This directory will also be searched for Plugins along with the system wide Plugins directory. 

## Creating Custom OPs

### Sample Projects

A collection of samples is available at the [following Github repository](<https://github.com/TouchDesigner/CustomOperatorSamples>). Some more basic examples are also avaialable in the Samples/CPlusPlus folder in the TouchDesigner installation directory. 

With the exceptions of how they are loaded, a Custom OP is created the same way as the [CPlusPlus TOP](<./CPlusPlus_TOP.md> "CPlusPlus TOP"), [CPlusPlus CHOP](<./CPlusPlus_CHOP.md> "CPlusPlus CHOP"), [CPlusPlus SOP](<./CPlusPlus_SOP.md> "CPlusPlus SOP") and [CPlusPlus DAT](<./CPlusPlus_DAT.md> "CPlusPlus DAT") are created. Refer to [Write a CPlusPlus Plugin](<./Write_a_CPlusPlus_Plugin.md> "Write a CPlusPlus Plugin") for more information. 

When developing your Custom OP, you may find it more convenient to load it into a CPlusPlus node to more quickly recompile/reload the plugin instead of having to restart TouchDesigner every time you change your code. Once you are done developing you use the same plugin as a Custom OP. 

### Converting existing CPlusPlus projects to Custom OPs

Taking an existing CPlusPlus project and making it can be used as a custom OP is relatively quick. 

#### Header Files

First, from the`Samples/CPlusPlus`folder for the correct OP type, take the`CPlusPlus_Common.h`and`*_CPlusPlusBase.h`header file (SOP, TOP, CHOP, DAT instead of *), and replace the versions that are in the project you are upgrading. 

#### Plugin Information

Next, you'll need to replace the functions`Get*APIVersion()`or`Get*PluginInfo()`with a new function containing one of these signatures (depending on the node type): 
[code] 
    void FillTOPPluginInfo(TOP_PluginInfo *info);
    void FillCHOPPluginInfo(CHOP_PluginInfo *info);
    void FillSOPPluginInfo(SOP_PluginInfo *info);
    void FillDATPluginInfo(DAT_PluginInfo *info);
    
[/code]

This function is used to define the name/label of the Custom OP, as well as other behavior such as how many inputs it allows. Examples of how to fill in this structure can be found in the previously mentioned example folders. 

#### Changed functions

Many of the virtual functions that your class overrides will have extra parameters or tweaks to the parameters (such as const changes). In most cases simply making your function signatures match those in the parent class should allow it to compile. 

#### OP_String

To provide a less error prone interface, any situation where a string is returned from your Custom OP to TouchDesigner, where the lifetime the memory needs to extend beyond the function call, it is done by assigning a value to an OP_String object that TouchDesigner provided for you. E.g: 
[code] 
    chan->name = "chan_name";
    
[/code]

would become: 
[code] 
    chan->name->setString("chan_name");
    
[/code]

You will likely have compile errors that will need to be fixed by replacing the = operation to a setString() function call. 

### Building on macOS using XCode
* Open one of the included .xcodeproj projects from the Samples/CPlusPlus directory.
  * Under the 'Product' menu select 'Archive'. If the build is successful a new window will come up showing a list of archives that have been created, including the one that was just created.
  * Select the one that was just created and click the 'Distribute Content' button. In the 'Select a method of distribution' dialog that comes up, select 'Build Products', and click 'Next'. Pick a location to save the archive and complete the operation.
  * In the folder where you saved the Build Products there will be a 'Products' folder and inside that <projectname>.plugin folder. This .plugin folder is what should be placed in your 'Plugins' folder to load this as a Custom OP.

## Issues Loading Custom Operators

The most common issue that will be run into when loading a custom operator fails is missing dependencies. This means that there are extra .dll (Windows) or .dylib (macOS) files that the custom operator requires, such as openCV .dlls, or CUDA .dlls which can't be found when trying to load the custom operator. 

### Windows

On Windows the dependencies should be placed next to the .dll for the custom operator, unless otherwise specified by the custom operator's author. Very useful tools for finding dependencies required by a .dll are:  
<https://github.com/lucasg/Dependencies>  
<https://www.dependencywalker.com/>  
Open the plugin binary with these tools and you can see the .dlls that plugin is dependent on and needs to be able to find to be able to load. 

#### Delay Loaded Libraries

On Windows when building a .dll, other .dlls the primary one depends on can be 'Delay-Loaded'. This is an option in the Visual Studio project file, or /DELAYLOAD on the command line. 

When a .dll is specified as Delay-Loadded, it means that .dll isn't loaded until a line of code executes that actually requires that .dll, such as a function defined in the .dll, or using a type defined by that .dll. This is useful for cases where that .dll may not exist, or where you only want to cause it to load of certain conditions are met. For example if a .dll coming from an SDK requires a driver to be installed on the system (usually in C:/Windows/System32). 

For example say the SDK file is SDK.dll, and the driver is Driver.dll, and SDK.dll has a regular dependency on Driver.dll (not delay-loaded). Without handling this case, your Custom Operator will fail to load entirely on systems that are missing Driver.dll. In your visual studio project you can specify SDK.dll as 'Delay-Loaded'. Now your custom operator will load, but as soon as you use something provided by SDK.dll, the application will crash since it'll fail to load SDK.dll due to the missing Driver.dll. To avoid this you should first check that Driver.dll existing via 
[code] 
     HMODULE lib = LoadLibrary(L"Driver.dll");
     if (lib)
     {
       // Driver.dll is found, we can use SDK.dll
     }
    
[/code]

You should only do this check ones, likely in the constructor of your Custom Operator. 

Another catch with Delay-Loaded .dlls is that while the initial load of your Custom Operator plugin will search next to that .dll for dependency .dlls, this is not the case for Delay-Loaded .dlls. That directory won't be searched. To make sure your delay-loaded .dlls are found you should manually load them into the process using LoadLibrary() before using something from that .dll that will trigger it to be loaded. 

### macOS

If the plugin requires linking with other .dylibs or frameworks, they should be included in the plugin bundle. The details of linking can depend on the libraries being used and to some extent personal preference, but we would suggest the following using rpaths: 

#### Plugin Build Setup:
* In the General tab for your plugin target in Xcode, add the library or framework to the Frameworks and Libraries section and make sure "Embed & Sign" is selected
  * In the Build Settings tab for the plugin target in Xcode, add a Runpath Search Paths setting for`@loader_path/../Frameworks`so the built plugin can locate libraries using the`@rpath`prefix

#### Library or Framework Setup:
* If you are building the library or framework yourself using Xcode, set its Dynamic Library Install Name Base (in the Build Settings for the target in Xcode) to`@rpath`(so the computed install name will be`@rpath/libYourLibrary.dylib`(or`@rpath/YourFramework.framework/Versions/A/YourFramework`for a framework). If you are using another build system there will likely be a setting to achieve the same result
  * If you are using a pre-built third-party library or framework and can't change the build process, change its linker ID, which will then be embedded by the linker when your plugin is built so it can be located when it is loaded. It may already be configured to use an rpath - you can check using`otool -D libYourLibrary.dylib`\- if the output shows`@rpath/libYourLibrary.dylib`then no change is needed. If it doesn't, you can use`install_name_tool -id @rpath/libYourLibrary.dylib libYourLibrary.dylib`to change its ID.


You can check the linkage of your built plugin using`otool -L YourPlugin.plugin/Contents/MacOS/YourPlugin```
