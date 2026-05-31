# Troubleshooting in TouchDesigner

TouchDesigner is an incredibly flexible tool, and with that flexibility comes the potential for intricate and difficult-to-find problems in your creations. This page is a brief introduction to the most important troubleshooting techniques and tools you'll use when building TouchDesigner networks. Of course, every problem is unique to its context so it will be up to you to determine which of these best suits your needs. To that end, this page will familiarize you with the range of tools at your disposal. 

Troubleshooting, or debugging, or analyzing a crash is different from optimizing, which focuses on making your networks run efficiently and quickly. For optimization information see [Optimization](<./Optimize.md> "Optimize"). 

Many (but not all) of the techniques described below will require a basic understanding of Python. 

**Important:** If you find a bug in TouchDesigner itself, please **[report it to Derivative](<#Reporting_a_Bug_to_Derivative>)**. 

## Documentation

The first place to look for information about TouchDesigner features is in this wiki, which serves as the official **TouchDesigner documentation**. Often, the documentation will provide clues (if not answers) about any problem you are having with a feature. If necessary you can [download the entire wiki](<./Offline_Help.md> "Offline Help") for use offline. 

In addition to using the wiki's search feature, there are portals in the TouchDesigner user interface directly into this wiki. All Operators have links to their wiki pages in their [Parameter Dialog](<./Parameter_Dialog.md> "Parameter Dialog") header: 

The leftmost button in the bottom header section links to Operator help, and the next button to the right links to Python help. 

Also, some Components found in the [Palette](<./Palette.md> "Palette") will have a **Help Page** custom parameter that opens a browser to that Component's wiki page. 

## Forums

Another common place to get help or information about TouchDesigner is in the **[TouchDesigner Forums](<https://forum.derivative.ca>)**. There is a strong and helpful community of users and Derivative staff to draw on. As on any forum, search for answers first before posting your questions, and when you do post be as clear and concise as possible. 

## Troubleshooting Networks

Finding errors in networks is generally easy because [nodes](<./Node.md> "Node") with errors will be displayed with an error marker, a red circle with a black X. To get info about the error, click on the error marker or middle-click anywhere on the node. Generally, when the error is fixed, the error flag will disappear immediately. 

If there is an error anywhere inside a Component, it will show an error marker, so often fixing an error will require entering components until the actual source of the error is found. 

### Errors Dialog and Error DAT

The **[Errors Dialog](<./Errors_Dialog.md> "Errors Dialog")** , found in the [Dialog](<./Dialog.md> "Dialog") menu, will allow you to see and jump to all current errors. It also allows you to filter errors by Operator type, specific operator, and error message. The **[Error DAT](<./Error_DAT.md> "Error DAT")** is very similar to the Errors Dialog, but in a DAT format, and with callback functionality. 

### OP.errors() and OP.scriptErrors()

Another way to find all node errors in your network is to open a [Textport](<./Textport.md> "Textport") and enter the command`[op('/').errors(recurse=True)](<./OP_Class.htm#Errors> "OP Class")`to get all node errors or`[op('/').scriptErrors(recurse=True)](<./OP_Class.htm#Errors> "OP Class")`to get all scriptErrors. This will print a list of all errors and which node they are associated with, or you can specify a network path and print all errors under that network. Occasionally you may find that a Component has a child with an error, but the error disappears when you enter its parent. The Error dialog, the **[Error DAT](<./Error_DAT.md> "Error DAT")** or the`[errors()](<./OP_Class.htm#Errors> "OP Class")`method is a good way to find out what the error is without having to actually navigate to its network. 

### Getting Info with Info CHOP, Panel CHOP and Info DAT

You will sometimes want to watch values on a node while researching its error. There are a few Operators that are useful for this. The [Info CHOP](<./Info_CHOP.md> "Info CHOP") holds numeric information about the node referenced in its Operator parameter. Similarly, the [Panel CHOP](<./Panel_CHOP.md> "Panel CHOP") holds numeric information about a [Panel](<./Panel.md> "Panel") Component's panel values. **TIP:** You will notice that the Info CHOP holds panel information as well, but it is best to use a Panel CHOP to watch panel information, as it is sometimes updated more reliably. 

A few Operators contain string information, which can be viewed using the [Info DAT](<./Info_DAT.md> "Info DAT"). This is especially important when working with [GLSL](<./GLSL.md> "GLSL") Operators 

### Pinpointing Errors with Bypass and Cook Flags

Often when trying to pinpoint an error in a network, you will want to narrow the possible sources down. Using the [Bypass Flag](<./Bypass_Flag.md> "Bypass Flag") to narrow down active Operators will often help you. If you want to turn off an entire network to narrow things down, you can turn off the [Cooking Flag](<./Cooking_Flag.md> "Cooking Flag") of the parent Component. 

### Using Chop Execute DAT and Parameter Execute DAT to Catch Errors

If you want to print a debug message to the Textport when a certain event happens, you will usually use a [CHOP Execute DAT](<./CHOP_Execute_DAT.md> "CHOP Execute DAT") or a [Parameter Execute DAT](<./Parameter_Execute_DAT.md> "Parameter Execute DAT") to watch values. For example, the CHOP Execute DAT can be used in tandem with the Info CHOP and Panel CHOP to notify you of changes to those values. **Note:** the execute DATs can be used to react when a change happens, but they have no direct way to trace what caused that change. Still, knowing _when_ something happens can be very helpful in finding what causes it. 

When printing a debug message from a script it is always a good idea to use the`[debug](<#Command:_debug>)`command instead of a standard Python`print`command. See below for [more info](<#Command:_debug>). 

### Troubleshooting in Perform Mode

When troubleshooting in [Perform Mode](<./Perform_Mode.md> "Perform Mode"), the editor is hidden but you will still want access to a lot of info you would normally get from it. The main technique to use here is floating viewers, which stay open when you enter Perform mode. So, if you open floating viewers (use the RMB context menu _View..._ option) and Parameter viewers (RMB context menu _Parameters..._) while in Editor mode, then enter perform mode, you will have access to the things you want to keep an eye on or change. Floating Textports will also stay open in Perform mode. Another important technique in Perform mode is using F10 to open the network of whatever panel your mouse is over. You can also use F9 to open the parent of that panel, with the network view focused on the panel Component. These hot-keys allow easy access to the specific parts of your Perform mode control panel that need attention. 

### Troubleshooting Disappearing Errors

Sometimes when you load up a .toe file, you see a network with an error, but when you enter the network, the error is gone. This is because an error can occur if a node hasn't been asked to load or cook, etc. However, manually looking at that node, or something that depends on it, will then trigger that node to update. 

Unfortunately these errors generally need to be looked at on a case by case basis, but quite often they don't affect the performance after startup. 

For a list of errors, open the Error Dialog instead of diving into the network, since that triggers updates. 

If the error is a cook order issue that isn't easily resolved, you can sometimes use a startup script to force cook this node in a specific order. 

### Under-cooking Issues

Under-cooking is when an Operator should be updating but for some reason is not. If you change data in one Operator, and it is not causing itself or another Operator looking at that data to update (cook) it may be an under-cooking problem. An important technique for verifying such an issue is to use an Info CHOP to monitor cook counts. All under-cooking issues should be **[reported to Derivative](<#Reporting_a_Bug_to_Derivative>)**. 

If you have an issue where your operators work properly in the Editor, but not in Perform mode, try turning off all your viewers in the Network Editor using the [Viewer Flag](<./Viewer_Flag.md> "Viewer Flag"). Because TouchDesigner only cooks nodes that are being used, it may be that you have no issues in the Network Editor because the node's viewer is using the node. 

## Troubleshooting Poor Performance

See the [Optimize](<./Optimize.md> "Optimize") guide. 

## Troubleshooting Python

Because TouchDesigner is a realtime engine and does not use a breakpoint/step debugger for Python, debugging can be a bit tricky. When working with Python, the [Textport](<./Textport.md> "Textport") is your best friend, and you will want to have one open at all times. Python errors are printed to the Textport (as well as showing up in error markers on nodes) and you will often want to print your own debug messages. **TIP:** if you find a floating textport inconvenient, use the [Pane Bar](<./Pane_Bar.md> "Pane Bar") to split your network view and change one of the pane types to _Textport and DATs_. 

### Python Error Markers in Networks

As with other Operators, DATs with Python scripts will show error markers when they have a problem. If a DAT is being used as a Python script and it has an error while compiling, it will display an error marker. Again, like other Operators, you can see what the compile error is by clicking the error marker or middle-clicking the node. When the compile error is resolved, the marker will disappear. 

When a Python script has a runtime error within a script, things work a little differently. The error marker will be placed on the DAT containing the script **where the error started.** This means that although the error may have happened in one module, the marker will be on the module that called that one! Luckily, the entire error stack (the chain of Python commands leading to the error) can be found in the error marker info, and usually will be printed to the Textport as well. 

### Getting Debug and Error Information

As mentioned above, because of TouchDesigner's realtime nature, the method for getting debug information from Python is to output it from scripts as they run. Here are a few important commands and techniques: 

#### Command: debug

**`debug(*objects)`**

    The`debug`command prints any number of objects to the textport. It works very much like the Python`print`command, but will print objects' string "representations", which are more detailed for some objects. The`debug`output will also append the script and line number from which`debug`was called.
    Example:`debug("Testcomp:", myComp.path, myComp.par.display)`When outputting information from a Python script for debugging purposes, **always use the`debug`command.** When using`print`, it is easy to forget where you put all your test statements and end up with unwanted Textport noise that is difficult to track down. Because`debug`always outputs the location it was called from, you will always be able to find and remove your debugging code easily. As an added perk,`debug`outputs more detail than`print`for some objects. 

#### Command: project.pythonStack

**`print(project.pythonStack())`**

    Sometimes you will want to see what Python calls have led to running one of your Python scripts. To print the stack of Python calls, use`print([project.pythonStack](<./Project_Class.md> "Project Class"))`. Python users may recognize that this parallels the`traceback.print_stack`method. It is safer to use`project.pythonStack`, because the Python version occasionally causes unwanted error markers to be placed in TouchDesigner networks. The`project.pythonStack`method has also been customised to provide additional information for TouchDesigner operators. The corresponding`project.stack()`will give the stack of operators being cooked and evaluated.

#### Outputting to DATs Instead of Textport

The above methods automatically output to the Textport, and that will suit most debugging needs. Occasionally, though, you may want to store larger amounts of debug data, or be able to keep the data around for longer, such as between file saves. To do this, you will want to output to a [Text DAT](<./Text_DAT.md> "Text DAT") or a [Table DAT](<./Table_DAT.md> "Table DAT"). Using a Table DAT can be helpful by organizing debug information into columns. 

### Raising Exceptions

Sometimes you will want to stop code execution at a certain point. To do this, simply raise a Python Exception. Code execution will stop and the error will be reported via Error Marker and Textport. When raising an exception, it is generally good practice to add a useful message. 

**Example:**`raise Exception("Width set to zero in " + parent().path)`For more detailed information about Python Exceptions see: [Python Errors and Exceptions](<http://docs.python.org/3/tutorial/errors.html#raising-exceptions>)

## Crashes and Troubleshooting .toe Files

Occasionally, TouchDesigner will crash. It has some nice features to make that less destructive and more diagnosable, which will be described in this section. In addition, every time you save your project, an incremented version is saved in your work folder and the prior file placed in the`Backup`folder. This ensures that you can jump back to previous working versions. (You may have to copy files in Backup up one level to your project folder if you are using relative paths for media.) (See 'Increment Filename on Save _in[Preference](<./Dialogs-Preferences_Dialog.md> "Dialogs:Preferences Dialog"))._

If you do find your network crashing, especially in a repeatable manner, please inform us - read the section below on reporting problems. 

### Crash Auto Save

For almost all crashes, TouchDesigner will automatically save a`CrashAutoSave._yourproject_.toe`before shutting down. The`CrashAutoSave`file is your project saved at the moment it crashed. When you load it with TouchDesigner again, it will be in a special safe mode where most functionality is bypassed. This allows you a chance to fix any problems you may have created to cause the crash. When you File -> Save this file and reload, it will be in normal mode again. 

### Tricking TouchDesigner to Open in Safe Mode

If you ever find yourself needing to work with a saved`.toe`file in the`CrashAutoSave`safe mode, you can simply change the name of your file to have`CrashAutoSave.`as a prefix and reload. E.g, rename the file to`CrashAutoSave._yourproject.1_.toe`. This ensures you can always open the file and get the contents. 

### Startup Error Dialog

Sometimes your network will have errors that occur during TouchDesigner's initial set-up. To get a full report of errors when TouchDesigner loads up, choose Edit>Preferences from the editor's menu. On the _General_ page there is a **Show Startup Errors** menu that allows you to choose whether you want to see the [Startup Errors Dialog](<./Startup_Errors_Dialog.md> "Startup Errors Dialog") when there are warnings or errors (_Warnings_ setting) or only when there are errors (_Errors_ setting). The next time you load TouchDesigner, you will see the Startup Error dialog if the criteria is met. 

### TouchDesigner Disappearing

A good way to diagnose a crash where TouchDesigner simply disappears (on startup or later) is to install the ‘Windbg Preview’ app from the Microsoft store. You can launch your app from within there and keep pressing the play button until it catches the actual crash (it may pause once or twice on startup due to an exception). From here that may give you a hint as to what is going on. More information can be found at [Using WinDbg to Debug Crashes](<./Using_WinDbg_to_Debug_Crashes.md> "Using WinDbg to Debug Crashes"). 

### TouchDesigner Hanging

If TouchDesigner is hanging, you can create a .`dmp`file or Crash report. On Windows, this can be done using the Windows Task Manager and right clicking on the process and choosing 'Create Dump File'. It's also possible using WinDbg, see [Using_WinDbg_to_Debug_Crashes](<./Using_WinDbg_to_Debug_Crashes.md> "Using WinDbg to Debug Crashes"). On macOS, see [macOS Crash logs](<./MacOS.htm#Crash_logs> "MacOS"). 

### Memory Leaks

When looking for a potential memory leak, the best place to check is the "Commit Size" column in the Details page of the Task Manager (similar on macOS). This will give a more accurate measure of whether it is leaking then the regular memory column. The "Commit Size" column may not be visible by default in which case you can right click the header to select it. 

### Diagnosing Memory Corruption

In rare cases there may be undetected memory hardware corruption. See [Diagnosing Memory Corruption Using Global Flags](<./Diagnosing_Memory_Corruption_Using_Global_Flags.md> "Diagnosing Memory Corruption Using Global Flags"). 

### ToeExpand and ToeCollapse Utilities

In rare cases, you may want to disassemble a`.toe`file into something ASCII readable. To do this, use the **[Toeexpand](<./Toeexpand.md> "Toeexpand")** and **[Toecollapse](<./Toecollapse.md> "Toecollapse")** programs provided with TouchDesigner in its installation directory. Reasons to use these include fixing something in a file that won't load or searching for a hard-to-find bit of text. This also allows you to use a "diff" program to compare two`.toe`files find all differences. 

## Reporting a Bug to Derivative

User reports are an important source of information about bugs in TouchDesigner, and your feedback is appreciated. That said, before reporting a problem as a software bug, always try to use the above techniques to make sure that the problem is in the software. 

To report a bug, please email ([support@derivative.ca](<mailto:support@derivative.ca>)) or post your .toe file on the [forums](<https://forum.derivative.ca>), along with how to replicate the error, and any`.dmp`files or crash reports created (in the case of a crash). On Windows, the`.dmp`file will be saved in your project directory. On macOS, you can find the crash reports via ​`Applications->Utilities->Console`. The Crash reports will be under User Reports or Crash Reports and named`TouchDesigner_date-xxx.crash|ips`. Right click on the report name to get the file location via Reveal in Finder. Posting problems to the forum is best, but if your project contains private data or techniques, feel free to email. 

When reporting a bug, please attempt to do the following: 
* Create a case that is as easy to reproduce as possible. Make it fast and simple for Derivative to see your bug.
  * Trim down your file as much as possible. Remove everything you can to create a small file size and easily understandable network.
  * Make sure that your file does not require extra media. Many Operators can be ["locked"](<./Lock_Flag.md> "Lock Flag") to preserve their data and remove their dependence on external files. If external files are absolutely necessary, create a ready-to-run zipped folder with your`.toe`file and all required media.
  * When sending zipped files, use`.zip`, not`.rar`,`.7z`etc. For larger files, feel free to use Google Drive, Dropbox or something similar.
