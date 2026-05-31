# App Class

This class contains specific application details, such as its version and installation folders. It can be accessed with the app object, found in the automatically imported [td module](<./Td_Module.md> "Td Module"). 

**NOTE:** See also [Variables](<./Variables.md> "Variables") and Dialogs -> Variables where more built-in paths and strings are available via expressions in the form`var('DESKTOP')`,`var('MYDOCUMENTS')`and`var('TOENAME')`. 

## Members`applicationsFolder`→`str`**(Read Only)** : 

> The primary location for installing applications on the system eg. 'C:/Program Files' on Windows.`architecture`→`str`**(Read Only)** : 

> The architecture of the compile. Generally 32 or 64 bit.`binFolder`→`str`**(Read Only)** : 

> Installation folder containing the binaries.`build`→`str`**(Read Only)** : 

> Application build number.`compileDate`→`Tuple[int, int, int]`**(Read Only)** : 

> The date the application was compiled, expressed as a tuple (year, month, day).`configFolder`→`str`**(Read Only)** : 

> Installation folder containing configuration files.`desktopFolder`→`str`**(Read Only)** : 

> Current user's desktop folder.`enableCachedParameters`→`bool`: 

> Get or set caching parameter values instead of always evaluating.`enableOptimizedExprs`→`bool`: 

> Get or set if Python expression optimization is enabled. Defaults to True every time TouchDesigner starts.`experimental`→`bool`**(Read Only)** : 

> Returns true if the App is an experimental build, false otherwise.`installFolder`→`str`**(Read Only)** : 

> Main installation folder.`launchTime`→`float`**(Read Only)** : 

> Total time required to launch and begin playing the toe file, measured in seconds.`logExtensionCompiles`→`bool`: 

> Get or set if extra messages for starting and ending compiling extensions is sent to the textport. Additional error stack will be printed if compilation fails. Defaults to False every time TouchDesigner starts.`osName`→`str`**(Read Only)** : 

> The operating system name.`osVersion`→`str`**(Read Only)** : 

> The operating system version.`power`→`bool`: 

> Get or set the overall processing state of the process. When True, processing is enabled. When False processing is halted. This is identical to pressing the power button on the main interface. This has a greater effect than simply pausing or stopping the playbar. 
[code]
>     app.power = False #turn off the power button.
>     
[/code]`preferencesFolder`→`str`**(Read Only)** : 

> Folder where the preferences file is located.`processId`→`int`**(Read Only)** : 

> The ID of the current running process.`product`→`str`**(Read Only)** : 

> Type of executable the project is running under. Values are 'TouchDesigner', 'TouchPlayer' or 'TouchEngine'.`pythonExecutable`→`str`**(Read Only)** : 

> Path to TouchDesigner's Python executable. This executable is not used directly by TouchDesigner but can be used to test pure Python code in an environment with all the packages and modules included with TouchDesigner. The executable can also be used to run external Python scripts without installing a separate Python installation.`recentFiles`→`list`: 

> Get or set the list of most recently saved or loaded files.`samplesFolder`→`str`**(Read Only)** : 

> Installation folder containing configuration files.`paletteFolder`→`str`**(Read Only)** : 

> Installation folder containing palette files.`userPaletteFolder`→`str`**(Read Only)** : 

> Folder where custom user palettes are located.`version`→`str`**(Read Only)** : 

> Application version number.`windowColorBits`→`int`**(Read Only)** : 

> The number of color bits per color channel the TouchDesigner window is running at. By default this will be 8-bits per channel, but can be increased to 10-bits by settings env var TOUCH_10_BIT_COLOR=1. Only works on displays that support 10-bit color.`systemFolder`→`str`**(Read Only)** : 

> Installation folder containing system files.`tempFolder`→`str`**(Read Only)** : 

> Folder used for temporary files.`pyEnvHelper`→`TDPyEnvManagerHelper`**(Read Only)** : 

> Returns access to the global [python environment helper](<./TDPyEnvManagerHelper.md> "TDPyEnvManagerHelper").

## Methods`addNonCommercialLimit(password=None)`→`None`: 

> Limits the application to operate at non-commercial license level. Multiple calls can be made, but each can be undone with a matching removeNonCommercialLimit(password). If the password is blank the operation cannot be undone. (See also [licenses.disablePro](<./Licenses_Class.md> "Licenses Class")) member. 
> 
>   * password - (Keyword, Optional) Password to later remove the restriction.
> 

[code]
>     app.addNonCommercialLimit(password='secret123')  #undoable with password
>     app.addNonCommercialLimit()  #permanent during length of session.
>     
[/code]`removeNonCommercialLimit(password=None)`→`bool`: 

> Removes the restriction previously added. Returns True if successful. 
> 
>   * password - (Keyword) Password previously used when restriction added.
> 

[code]
>     app.removeNonCommercialLimit(password='secret123')
>     
[/code]`addResolutionLimit(x, y, password=None)`→`None`: 

> Limits all textures to the specified amount. Multiple calls can be made, but each can be undone with a matching removeResolutionLimit(password). The final resolution limit will be the minimum of all calls. If the password is blank the operation cannot be undone. 
> 
>   * x - Width of maximum texture resolution, measured in pixels.
>   * y - Height of maximum texture resolution, measured in pixels.
>   * password - (Keyword, Optional) Password to later remove the restriction.
> 

[code]
>     app.addResolutionLimit(600, 480, password='secret123')  #undoable with password
>     app.addResolutionLimit()  #permanent during length of session.
>     
[/code]`removeResolutionLimit(password=None)`→`bool`: 

> Removes the restriction previously added. Returns True if successful. 
> 
>   * password - (Keyword) Password previously used when restriction added.
> 

[code]
>     app.removeResolutionLimit(password='secret123')
>     
[/code]

TouchDesigner Build: Latest\nwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditor2025.300002022.241402021.100002020.200002018.28070before 2018.28070
