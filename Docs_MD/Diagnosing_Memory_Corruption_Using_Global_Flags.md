# Diagnosing Memory Corruption Using Global Flags

## Overview

In rare cases, it's possible a crash is occuring due to general memory corruption, which is difficult to track down via regular .dmp files. One way to track these down is to change the way Windows allocates memory, so that it puts read-only 'guard' section around each block of memory. If TouchDesigner tries to write beyond the bounds of where it should, a crash will occur at that moment. .dmp files created this way will be more informative. Without these guard pages being read-only the OS would allow us to write to that memory, which would likely be memory used by other parts of code, and that corrupts that memory. To force the OS to create these guard pages, you need to use a tool call Global Flags. It's part of the Debugging Tools for Windows, and can be downloaded from here: <https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/debugger-download-tools> You'll likely want to select the 'As a standalone toolset' workflow. 

## Setting the Flags

The Global Flags tool is called gflags.exe on disk. Once it is installed, run it by searching for Global Flags, or for gflags.exe. You'll need to run it as Administrator. 
* Once opened, there will be 4 tabs at the top. Select the 'Image File' tab.
  * In the 'Image:' field, type 'touchdesigner.exe' and press the tab button on your keyboard.
  * All of the checkboxes should be unchecked right now.
  * Select the 'Enable page heap' option, and hit Ok
  * Now run your project. It will load and run slower likely. If your project is very large, it may take a long time to load up.
  * Cause the crashes to occur, and .dmp files to be created.
  * Send the .dmp files to support@derivative.ca


To disable the feature and regain performance, follow the same instructions. When you press the tab button this time, the 'Enable page heap' should already be checked, and you can now uncheck it. 

See also [Troubleshooting in TouchDesigner](<./Troubleshooting_in_TouchDesigner.md> "Troubleshooting in TouchDesigner").
