# Using WinDbg to Debug Crashes

## Overview

In cases where TouchDesigner is failing to start up on systems, but no .dmp files is being created or other information is presented, or for crashes that occur with no .dmp file after running for some time, a more in-depth analysis may be required to find a solution. This can be done using the tool 'WinDbg Preview' provided by Microsoft. 

See [Troubleshooting in TouchDesigner](<./Troubleshooting_in_TouchDesigner.md> "Troubleshooting in TouchDesigner"). 

## Downloading WinDbg

WinDbg can be downloaded from the Microsoft App store by following [this link](<https://www.microsoft.com/en-us/p/windbg-preview/9pgjgd53tn86>). 

## Debugging Startup Crashes

Start WinDbg Preview. Under the 'File' menu choose 'Launch Executable' and selected TouchDesigner.exe. This is usually located at C:/Program Files/Derivative/TouchDesigner/bin/TouchDesigner.exe. This will cause TouchDesigner to launch. Startup will likely stop very quickly at a breakpoint saying something like 'Break instruction exception - code 80000003 (first chance) ntdll!LdrpDoDebuggerBreak+0x30:' in the Command window. Press the 'Go' button on the upper left (The Play symbol), to continue execution. You may have to press Go a few times to jump over some breakpoints. Eventually you will end up at the point where TouchDesigner is failing to start up. When this occurs you can post the text from the 'Logs' and 'Command' Windows to who you are talking to on our support team. 

## Debugging Crashes That Don't Produce .dmp files

If you have a project that is randomly crashing, but not creating a .dmp file when it does (such as just disappearing). You can use Windbg to create a .dmp file for these cases. Open your project and then open windbg. In the File menu of Windbg, select 'Attach to a Process' and select TouchDesigner.exe. Now let your project run until the crash occurs, and save the .dmp file when it does. 

## Saving a .dmp file

If the logs arn't giving enough information, then saving a .dmp file will give even more information to help us diagnose the issue. In the 'Command' window you can use the command 
[code] 
     .dump /mf C:/SomeFolder/Output.dmp
    
[/code]

To create a .dmp file. You'll need to create the output folder. This file will be quite large, so .zip it and send us a link to it. Be sure to include the TouchDesigner build number used to create the .dmp, as we need to match it exactly with our backups to be able to diagnose the .dmp.
