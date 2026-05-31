# Project Class

The Project class describes the current session. It can be accessed with the project object, found in the automatically imported [td module](<./Td_Module.md> "Td Module"). Members changed in this such as the 'paths' member will be written to disk when the project is saved. 

## Members`folder`→`str`**(Read Only)** : 

> The folder at which the project resides.`name`→`str`**(Read Only)** : 

> The filename under which the project is saved.`saveVersion`→`str`**(Read Only)** : 

> The [App](<./App_Class.md> "App Class") version number when the project was last saved.`saveBuild`→`str`**(Read Only)** : 

> The [App](<./App_Class.md> "App Class") build number when the project was last saved.`saveTime`→`str`**(Read Only)** : 

> The time and date the project was last saved.`saveOSName`→`str`**(Read Only)** : 

> The [App](<./App_Class.md> "App Class") operating system name when the project was last saved.`saveOSVersion`→`str`**(Read Only)** : 

> The [App](<./App_Class.md> "App Class") operating system version when the project was last saved.`paths`→`dict`**(Read Only)** : 

> A dictionary which can be used to define URL-syntax path prefixes, enabling you to move your media to different locations easily. This dictionary is saved and loaded in the`.toe`file. Example: Run`project.paths['movies'] = 'C:/MyMovies'`, and reference it with a parameter expression:`movies://butterfly.jpg`. To manually convert between expanded and collapsed paths, use`tdu.collapsePath()`and`[tdu.expandPath](<./TDU_Class.md> "TDU Class")`, for example`tdu.expandPath('movies://butterfly.jpg')`expands to`C:/MyMovies/butterfly.jpg`. If you already have your paths setup, choosing files from file browsers in OPs will create paths using these shortcuts rather than full paths. Additionally, to enable you to have different media locations on different machines, you can put a JSON file in the same folder as your`.toe`that gets read on startup. This will override any existing locations saved in projects.paths to the new machine specific file paths specified in the .json. Only existing entries in`project.paths`will be used. If the .json contains path names not specified in`project.paths`, those will be ignored. It would contain something like`{ "project.paths": { "movies": "M:/MyMovies" } }`. If your`.toe`file is called`MyProject.10.toe`, the JSON file must be called`MyProject.Settings.json`. The idea is that this .json would be unique to machines, and not commited to version control or shared between machines.`cookRate`→`float`: 

> Get or set the maximum number of frames processed each second. In general you should not need to use this. It is preferred to look at the FPS of the root component to know the cooking rate. Individual [components](<./COMP_Class.md> "COMP Class") may have their own rates, specified by rate. 
[code]
>     a = project.cookRate # get the current cook rate 
>     project.cookRate = 30 # set the cook rate to 30 FPS
>     
[/code]
> 
> Note: This is displayed and set in the user interface at the bottom-left: the "FPS" field.`realTime`→`bool`: 

> Get or set the real time cooking state. When True, frames may be skipped in order to maintain the cookRate. When False, all frames are processed sequentially regardless of duration. This is useful to render movies out using the Movie File Out TOP without dropping any frames for example. 
[code]
>     a = project.realTime
>     project.realTime = False # turn off real time playback.
>     
[/code]`isPrivate`→`bool`**(Read Only)** : 

> True when the project networks cannot be directly viewed.`isPrivateKey`→`bool`**(Read Only)** : 

> True when the private networks are accessible by a pass phrase.`cacheParameters`→`bool`: 

> Cache parameter values instead of always evaluating.`externalToxModifiedInProject`→`bool`**(Read Only)** : 

> Callback for when an external tox has been modified in the current project and there are other instances of the same tox loaded elsewhere in the project.`externalToxModifiedOnDisk`→`bool`**(Read Only)** : 

> Callback for when an external tox file has been modified on disk.`windowOnTop`→`bool`: 

> Get or set the window on top state.`windowStartMode`→`WindowStartMode`: 

> Get or set the window start mode. The mode is one of:`WindowStartMode.AUTO`,`WindowStartMode.FULL`,`WindowStartMode.LEFT`,`WindowStartMode.RIGHT`or`WindowStartMode.CUSTOM`.`windowDraw`→`bool`: 

> Get or set the window drawing state.`windowStartCustomWidth`→`int`: 

> Get or set the window start width. Only used when windowStartMode is`WindowStartMode.CUSTOM`.`windowStartCustomHeight`→`int`: 

> Get or set the window start height. Only used when windowStartMode is`WindowStartMode.CUSTOM`.`windowStartCustomX`→`int`: 

> Get or set the window start X position. Only used when windowStartMode is`WindowStartMode.CUSTOM`.`windowStartCustomY`→`int`: 

> Get or set the window start Y position. Only used when windowStartMode is`WindowStartMode.CUSTOM`.`performOnStart`→`bool`: 

> Get or set the perform on start state.`performWindowPath`→`OP`: 

> Get or set the perform window path.`resetAudioOnDeviceChange`→`bool`: 

> Get or set whether audio devices momentarily reset when devices are added or removed to the system.`sdrReferenceWhiteNits`→`int`: 

> Get or set Reference White brightness in nits, of SDR colors/content.`hdrReferenceWhiteNits`→`int`: 

> Get or set Reference White brightness in nits, of HDR colors/content.`editorWindowPixelFormat`→`WindowPixelFormat`: 

> Get or set the pixel format the editor window will use. This is not the format Window COMPs or the Perform window will use (which is set with a Window COMP). 
> 
> The project must be saved and TouchDesigner must be restarted for this to take affect. Valid values are from the WindowPixelFormat enum: 
> 
>   * WindowPixelFormat.SDR8_FIXED
>   * WindowPixelFormat.SDR10_FIXED
>   * WindowPixelFormat.HDR10_FIXED
>   * WindowPixelFormat.HDR16_FLOAT
>`workingColorSpace`→`WorkingColorSpace`: 

> Get or set the working color space used for this project. 
> 
> The project must be saved and TouchDesigner must be restarted for this to take affect. Valid values are from the WorkingColorSpace enum: 
> 
>   * WorkingColorSpace.PASS_THROUGH
>   * WorkingColorSpace.ACES_CG
>   * WorkingColorSpace.SRGB_LINEAR
> 

## Methods`load(path)`→`None`: 

> Load a specific .toe file from disk. 
> 
>   * path - (Optional) The path of the file to load. If not specified, loads the default[.toe file](</index.php?title=.toe_file&action=edit&redlink=1> ".toe file \(page does not exist\)"), as specified in preferences.
> 

[code]
>     project.load('test_demo.toe')
>     
[/code]`save(path, saveExternalToxs=False)`→`bool`: 

> Save the current session to disk. Returns True if a file was saved, False otherwise (eg, if the file exists, and when prompted, the user selects to not overwrite). 
> 
>   * path - (Optional) If not provided the default/current filename is incremented and used. The current file is project.name under folder project.folder.
>   * saveExternalToxs - (Keyword, Optional) If set to True, will save out the contents of any COMP that references an external .tox into the referenced .tox file.
> 

[code]
>     project.save('test_demo.toe')
>     project.save()
>     
[/code]`quit(force=False, crash=False)`→`None`: 

> Quit the project. 
> 
>   * force - (Keyword, Optional) If set to True, unsaved changes will be discarded without prompting.
>   * crash - (Keyword, Optional) If set to True, the application will terminate unexpectedly. This is used for system testing.
> 

[code]
>     project.quit()  #quit project, possibly prompting for unsaved changes if 'Prompt to Save on Exit' in Preferences dialog is enabled.
>     project.quit(force=True)  #quit project immediately.
>     
[/code]`addPrivacy(key)`→`bool`: 

> Add privacy to a toe file with the given key. 
> 
> Privacy can only be added to toes that currently have no privacy, and are using a Pro license. 
> 
>   * key - The key phrase. This should resolve to a non-blank string.
> 

[code]
>     project.addPrivacy('secret')
>     
[/code]`removePrivacy(key)`→`bool`: 

> Completely remove privacy from a toe file. 
> 
>   * key - The current privacy key phrase.
> 

[code]
>     project.removePrivacy('secret')
>     
[/code]`accessPrivateContents(key)`→`bool`: 

> Gain access to a private file. The file will still be private the next time it is saved or re-opened. 
> 
>   * key - The current privacy key phrase.
> 

[code]
>     project.accessPrivateContents('secret')
>     
[/code]`applyWindowSettings()`→`None`: 

> Applies the project's window start settings to the current TouchDesigner window.`stack()`→`str`: 

> Formatted contents of current cook and parameter evaluation stack. 
[code]
>     print(project.stack())
>     
[/code]`pythonStack()`→`str`: 

> Formatted contents of current python stack. 
[code]
>     print(project.pythonStack())
>     
[/code]

TouchDesigner Build: Latest\nwikieditor2025.300002022.241402021.100002018.28070before 2018.28070
