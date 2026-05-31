# Palette:bitwigRemotesProject

##   
  
Summary

The bitwigRemotesProject COMP serves as an interface for accessing and controlling global Project Remote Controls in Bitwig. Navigation to controls begins by selecting the desired page. The 8 Remote Control Parameters on this Component will correspond to the 8 Remote Controls on a single page. 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[Palette:bitwigRemotesProject Ext](</index.php?title=Palette:bitwigRemotesProject_Ext&action=edit&redlink=1> "Palette:bitwigRemotesProject Ext \(page does not exist\)")

## 

Parameters - Bitwig Project Remotes Page

Remote Control Page`Remotecontrolpage`\- Indicates the name of the currently selected Project Remotes Page. 

Read Modulated Values`Readmodulatedvalues`\- If enabled, will activate listeners for the modulated values for the Remote Controls on the selected page. Note that these are read-only values as modulation can only be driven by Bitwig Modulators. 

Restore Automation Control`Restoreautomationcontrol`\- Will restore automation control for all the remotes on the current page.`Remotecontrol0`\- A bi-directional parameter corresponding to the 1st Remote Control on the selected page.`Remotecontrol1`\- A bi-directional parameter corresponding to the 2nd Remote Control on the selected page.`Remotecontrol2`\- A bi-directional parameter corresponding to the 3rd Remote Control on the selected page.`Remotecontrol3`\- A bi-directional parameter corresponding to the 4th Remote Control on the selected page.`Remotecontrol4`\- A bi-directional parameter corresponding to the 5th Remote Control on the selected page.`Remotecontrol5`\- A bi-directional parameter corresponding to the 6th Remote Control on the selected page.`Remotecontrol6`\- A bi-directional parameter corresponding to the 7th Remote Control on the selected page.`Remotecontrol7`\- A bi-directional parameter corresponding to the 8th Remote Control on the selected page. 

## 

Parameters - TDBitwig Page

TDBitwig Comp`Tdbitwigcomp`\- A reference to the Bitwig Main COMP

Connect`Connect`\- A toggle to manually enable or disable listeners associated with this COMP. 

Listener Index`Listenerindex`\- The index of the Cursor object which this COMP is communicating with. 

Debug Messages`Debugmessages`\- Print information about extension method calls for the Component

Timeslice OSC Chop`Timesliceoscchop`\- If timeslice is enabled, the OSC Chop will cook every frame. If disabled, OSC Chop will cook only during changes, but cook time may be longer. Using time slice for performance optimization will usually depend on the particular use case. 

Strip CHOP Name Prefixes`Stripchopnameprefixes`\- Strip off the given number of address segments in the output CHOP channel names 

Name Channel Prefix`Namechannelprefix`\- If enabled, the output CHOP channel names will include with the name of the currently selected Track object. Otherwise, the channel names will begin with the integer index of the Cursor this COMP is connected to. 

## 

Parameters - About Page

Help`Help`\- Opens this documentation page 

Version`Version`\- The TDBitwig version that this Component is updated to 

.tox Save Build`Toxsavebuild`\- The TouchDesigner build version that this Component was saved in 

Update`Update`\- If the tdBitwigPackage COMP is present in the TouchDesigner project, pressing pulse will update this Component to the newest version 

## 

Operator Outputs
* Output 0 \- A CHOP containing a channel for each Remote Control value


  
Error while fetching data from URL [https://03-019-81-181.plesk.page/api.php?action=query&list=categorymembers&cmtitle=Category:Palette&format=xml&cmlimit=500](<https://03-019-81-181.plesk.page/api.php?action=query&list=categorymembers&cmtitle=Category:Palette&format=xml&cmlimit=500>): $2.  
Error fetching URL: SSL: no alternative certificate subject name matches target host name '03-019-81-181.plesk.page'  
There was a problem during the HTTP request: 0 Error  
Could not get URL [https://03-019-81-181.plesk.page/api.php?action=query&list=categorymembers&cmtitle=Category:Palette&format=xml&cmlimit=500](<https://03-019-81-181.plesk.page/api.php?action=query&list=categorymembers&cmtitle=Category:Palette&format=xml&cmlimit=500>) after 3 tries.

Palette  
---
