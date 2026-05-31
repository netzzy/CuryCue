# Palette:remotePanel

The combination of these two components lets you see and interact with a TouchDesigner panel running on another machine.   
  
From the Palette,`remotePanelClient`and`remotePanelServer`must be placed in two different TouchDesigner on 2 different machines. 

## remotePanelClient

This is the component that receives the image and sends the interaction data to the server. 

Most simply, put this component into an empty TouchDesigner, make`/perform`point to it, and for good measure, make Dialogs -> Window Placement be set to Start in Perform Mode. 

You need to also copy-paste the`remotePanelServer`component (found in the palette) into your server process's control panel. It will be ready to receive data from`remotePanelClient`. 

Then change this component's "IP Address of Server" custom parameter to be the IP address of the server (you can use the computer name if on a local network). 

To increase the smoothness, try increasing the Frames per Second parameter. 

To decrease the latency, reduce the Video Queue Seconds custom parameter of this component, possibly at the expense of some smoothness. 

[ The data sent to the server defaults in remotePanelClient to port 9500, the same port that's in remotePanelServer component. They normally don't have to be changed, but if you need to, change both of them. ]( To use lower bandwidth you can instead use the Video Stream In TOP and the Video Stream Out TOP with TouchDesigner Commercial or Pro. But try`touchin2`first. ) 

## remotePanelServer

This`remotePanelServer`component is what you put into the main (server) application where the actual panel is located. 

You must also put`remotePanelClient`into a TouchDesigner application where you want to remotely view a panel. 

  
Its default port`9500`matches the default for`remotePanelClient`. 

The data from the remote computer comes in to the`touchin1`DAT. It is hard-wired to port 9500 here and in the remote panel. 

The table comes from the remote computer where the rows '`lselect`', '`mselect`' '`rselect`', '`insudeu`', '`insidev`', frames-per-second, path of the panel, etc are sent.
