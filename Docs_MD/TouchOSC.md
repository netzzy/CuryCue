# TouchOSC

TouchOSC is a modular OSC and MIDI control surface for iOS (iPhone/iPod Touch/iPad) and Android. It can send TouchDesigner messages via OSC from interactions with its control panels. Custom control panels can be created by using the TouchOSC Editor which is available for Windows/Mac OSX/Linux. 

Additional information and links to the App Store and the TouchOSC Editor can be found here: <http://hexler.net/software/touchosc>

## Using TouchOSC with TouchDesigner

### Setting up TouchOSC

First make sure that the device running TouchOSC and the computer running TouchDesigner are on the same wireless network so they can communicate with each other. 

After installing TouchOSC, launch the app and you will see the following screen. 

Open the OSC:Disabled menu. Once on this next page, turn on the **Enabled** switch to reveal the following screen. 

On this settings screen, input the IP address of your computer running TouchDesigner. If you do not want to use the default port numbers, change them here as well. Once completed, press the **Done** button to close the dialog. 

Back at the start screen for TouchOSC, select the Layout you would like to use from the Layout menu. When ready, press the **Done** button. 

### Setting up TouchDesigner

Open TouchDesigner and create a [OSC In CHOP](<./OSC_In_CHOP.md> "OSC In CHOP") or [OSC In DAT](<./OSC_In_DAT.md> "OSC In DAT"). Change the **Network Port** parameter to be the same port you select in TouchOSC's **Port(outgoing)** setting. Default is 8000. 

Now move or adjust any control in TouchOSC, you will see the incoming values in TouchDesigner.
