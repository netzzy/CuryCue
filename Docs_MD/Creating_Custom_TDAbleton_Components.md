# Creating Custom TDAbleton Components

The **TDAbleton** system contains a framework for building your own custom Components for connecting to Ableton Live. This is done using Python extensions, and will require an intermediate understanding of programming. 

See also: [TDAbleton](<./TDAbleton.md> "TDAbleton"), [TDAbleton System Components](<./TDAbleton_System_Components.md> "TDAbleton System Components"), [TDAbletonCompBaseExt Extension](<./TDAbletonCompBaseExt_Extension.md> "TDAbletonCompBaseExt Extension")

## Development Tools

The **`tdAbleton`master component** provides access to some useful tools when creating custom TDAbleton Components. On its`TDAbleton`custom parameter page, the bottom section contains parameters useful for this task. **Ableton Log File** , **Log TDA Messages** , and **Open Log File** are helpers for use with the [Ableton log file](<https://help.ableton.com/hc/en-us/articles/209071629-Where-to-find-Live-s-Crash-Reports>). See also: [tdAbleton master component](<./TDAbleton_System_Components.htm#The_tdAbleton_Master_Component> "TDAbleton System Components"). 

#### Ableton Console

**Open Console** opens a Python console into the TouchDesigner Remote Script so you can interact directly with the Live Object Model. This can be very useful for understanding the layout of Ableton's Python Live Object Model. The console provides a few special shortcut names for getting around in the Remote Script: 
1. **SONG** : the current Live Object Model (LOM) song object. Also known as a "Live Set".
  2. **APP** : the current LOM application object.
  3. **TDA** : the TouchDesigner Remote Script object.
  4. **CLIENT** : the TDA client object for this TouchDesigner process.
  5. **OSC** : the OSC Python module used for communication


For example, if you open the console and type`SONG.tracks[0].name`, you will see the name of the first track returned. 

## Ableton's Live Object Model

The TDAbleton system makes heavy use of Ableton's **Live Object Model** , abbreviated LOM, which gives Python access to just about every aspect of Ableton Live. It is beyond the scope of this wiki to go into depth about the details, but here are some very helpful documentation links: 
1. <https://docs.cycling74.com/max7/vignettes/live_object_model>
  2. <https://julienbayle.studio/PythonLiveAPI_documentation/Live9.6.xml>

## Anatomy of a TDAbleton Component

The **`abletonComp`** custom Component provided in TDAbleton is the starting point for building custom TDAbleton components. It does nothing on its own, but contains all the necessary operators and all the [Custom Parameters](<./Custom_Parameters.md> "Custom Parameters") that are used by the TDAbleton system. Operators inside TDAbleton Components that are part of the base TDAbleton system are colored orange. 

### The`abletonBase`Component

Inside all TDAbleton components is an **`abletonBase`Component** that contains the meat of the TDAbleton system. It is cloned from an`abletonBase`inside the **`tdAbleton`** master component, so will automatically update when you put an updated`tdAbleton`master component in your network. It has one output, which is the CHOP with values reported by [TDAbleton listeners](<#TDAbleton_Listeners>) (see below). This is generally connected to the out1 [Out CHOP](<./Out_CHOP.md> "Out CHOP") to report data received from Ableton Live. Of course, various CHOP techniques can be used to add custom channels to this output. 

### The Custom Ableton Extension

Every custom TDAbleton Component will need its own custom **[Extension](<./Extensions.md> "Extensions")**. To make use of the built in features in`abletonBase`, the extension should be derived from [TDAbletonCompBaseExt Extension](<./TDAbletonCompBaseExt_Extension.md> "TDAbletonCompBaseExt Extension"), which can be found in the abletonBase component. 

### TDAbleton Custom Parameters

All of the custom parameters used by`TDAbletonCompBaseExt`and`abletonBase`are included on the **Ableton Comp custom parameter page**. They are not all necessary for every custom TDAbleton Component, but are provided as a convenient starting point. Unnecessary ones can be removed. 

There is also a **TDAbleton custom parameter page** on`abletonComp`which contains parameters used by the TDAbleton system, and should not be changed. 

## Setting Up A New Custom TDAbleton Component

There are a number of things you'll want to alter on`abletonComp`to prepare for creating a custom TDAbleton Component. First, make a copy of`abletonComp`to use as a starting point, then follow the instructions below to begin customizing. 

#### Change the name

TDAbleton official Components all start with "ableton". You can adopt this standard or not, but it is always a good thing to name Operators something informative. Do not keep the name`abletonComp`, as that is sure to confuse. 

#### Change the color

Most TDAbleton components are dark orange so they are easily recognized in a network. Light orange, like the`abletonComp`and the various inner Operators, is used to signify more of a building block. 

#### Re-point the clone source

The clone source is used by TDAbleton's [Update system](<./TDAbleton_System_Components.htm#TDAbleton_Parameter_Page_\(Update_system\)> "TDAbleton System Components"). It should point to wherever you will keep your master version of this custom Component. 

#### Change the extension name

Although it is not absolutely necessary, it is a best practice to change your extension name to match your custom component's name. In the`Extension Object 1`parameter, change both occurences of`AbletonCompExt`to an appropriate name for your extension. The`Ext`suffix is again not necessary, but a best practice. After changing the extension parameter, go inside the component and change the extension DAT name and the name of the extension class inside. 

#### Set up your TDAbleton custom parameters

As mentioned above,`abletonComp`starts with all the parameters used by the TDAbleton system. Use the [Component Editor](<./Component_Editor_Dialog.md> "Component Editor Dialog") to open up your custom Component. Change the name of the **Ableton Comp** page to fit your Component's name. If you know which parameters you will need, you can remove unnecessary ones now, or leave them for later if you are unsure. 

**Important:** the Live Object Model (LOM) parameters (Track, Device, Chains, Chain Devices, and Parameter) are used to hierarchically navigate Ableton's Live Object Model. They depend on each other in specific ways. Only the following are valid setups: 
* **No LOM parameters** : no LOM navigation necessary
  * **Track only** : Component is meant to work on an Ableton track.
  * **Track and Device** : Component is meant to work on an Ableton device.
  * **Track, Device, Parameter**: Component is meant to work on an Ableton parameter on a top level Device.
  * **Track, Device, Chain (+ optional Chain Devices and Chains ending on a Chain)** : Component is meant to work on a Track or Device Chain.
  * **Track, Device, Chain, Chain Device, (+ optional Chains and Chain Devices ending on a Chain Device)** : Component is meant to work on a top level or sub-chain Device.
  * **Track, Device, Chain, Chain Device, (+ optional Chains and Chain Devices ending on a Chain Device), Parameter**: Component is meant to work on an Ableton parameter on a top level or sub-chain Device.

## Customizing A TDAbleton Component

The best way to learn how to work with the TDAbleton system is to explore the [TDAbleton System Components](<./TDAbleton_System_Components.md> "TDAbleton System Components"), especially the ones that are most similar to your goal. In many cases, all you will need to do is customize your extension. Features for connecting to Live are provided by deriving the extension from **`[TDAbletonCompBaseExt Extension](<./TDAbletonCompBaseExt_Extension.md> "TDAbletonCompBaseExt Extension")`**. 

### Example:`AbletonParameterExt`The`abletonParameter`component provides access to an Ableton device parameter. This functionality is created by a small custom extension script, which we'll explore here. If you're not familiar with inheritance in Python, there are many tutorials online, [this one](<http://www.jesshamrick.com/2011/05/18/an-introduction-to-classes-and-inheritance-in-python/>) for example. Basically, your extension class will "inherit" methods and members from its parent class, **`[TDAbletonCompBaseExt Extension](<./TDAbletonCompBaseExt_Extension.md> "TDAbletonCompBaseExt Extension")`**. 

#### Deriving from`TDAbletonCompBaseExt`[code] 
    TDAbletonCompBaseExt = mod('abletonBase/TDAbletonCompBaseExt').TDAbletonCompBaseExt
    
    class AbletonParameterExt(TDAbletonCompBaseExt):
    	"""
    	AbletonParameterExt sets up a basic 2 way connection with an Ableton parameter.
    	"""
    	def __init__(self, ownerComp):
    		# The component to which this extension is attached
    		TDAbletonCompBaseExt.__init__(self, ownerComp)
    
[/code]

The top bit of the`AbletonParameterExt`script sets the extension up as a subclass of **`[TDAbletonCompBaseExt Extension](<./TDAbletonCompBaseExt_Extension.md> "TDAbletonCompBaseExt Extension")`**. The first line grabs the class from its DAT module in`abletonBase`. The class definition uses`TDAbletonCompBaseExt`as the parent class, and also calls its`__init__`function during`AbletonParameterExt.__init__`. 

#### Setting up listeners
[code] 
    	def setupListeners(self):
    		TDAbletonCompBaseExt.setupListeners(self)
    
    		# make sure we have a valid ableton parameter
    		aParInfo = self.LomParInfo('Parameter')
    		if not aParInfo:
    			return
    
    		# set up listener parameters
    		# lomExpression: a Python expression to the live object in tda
    		lomExpression = aParInfo['lomExpression']
    
    		# returnAddress: osc address that updates will be sent to from tda.
    		# note that this must be a valid CHOP channel name
    		returnAddress = aParInfo['returnAddress'] + '/value'
    
    		# id: unique id of the object requesting a listener
    		ownerId = self.ownerComp.id
    
    		# property: the name of the live object's property to listen to
    		property = 'value'
    
    		# this tuple is what a listener key looks like
    		listener = (lomExpression, property, returnAddress, ownerId)
    
    		# addListener(listener, outgoing parameter,
    		# 		autoSync to keep par up to date, parMin, parMax)
    		self.addListener(listener, self.ownerComp.par.Valuesend,
    					aParInfo['lomInfo']['min'], aParInfo['lomInfo']['max'])
    
[/code]

This is where the real meat of the extension happens. The`setupListeners`function is called by`[TDAbletonCompBaseExt Extension](<./TDAbletonCompBaseExt_Extension.md> "TDAbletonCompBaseExt Extension")`when the Component is ready to create listeners in Ableton Live. Listeners are a LOM way to receive information when a value changes. The main way TDAbleton receives information from Ableton Live is through listeners. **Tip:** a great way to experiment with numerical listeners is the [abletonValueListener](<./TDAbleton_System_Components.htm#abletonValueListener> "TDAbleton System Components") component. 

Looking through the code, the comments explain the individual lines, but the big picture is this:`[TDAbletonCompBaseExt Extension](<./TDAbletonCompBaseExt_Extension.md> "TDAbletonCompBaseExt Extension")`provides an easy interface for setting up listeners in Ableton Live. The following line defines the actual listener: 
[code] 
    		# this tuple is what a listener key looks like
    		listener = (lomExpression, property, returnAddress, ownerId)
    
[/code]

##### Listener elements

A listener consists of four pieces of information: 
1. **`lomExpression`** : a Python expression that points to an object in Ableton's Live Object Model. If you look higher in the code you will see that this is provided easily via LOM custom parameters by this line:`aParInfo = self.LomParInfo('Parameter')`and then this line:`aParInfo['lomExpression']`. Each parameter knows how to create a LOM expression to the object referred to. It is a simple string of Python code, which can also be created by referring to the [[Live Object Model documentation](<http://julienbayle.net/PythonLiveAPI_documentation/Live9.6.xml>)] and experimenting with the TDAbleton Console.
  2. **`property`** : a property of the LOM object referred to by`lomExpression`.
  3.`**returnAddress**`: the OSC address that changes to the property will be sent to
  4.`**ownerId**`: a unique ID for the object requesting the listener.
  5.`**extra**`: The`extra`element is an optional string with special instructions. If it is 'noinit', the initial value send will be skipped. This is useful for avoiding CHOP clutter when listening to a large number of channels.

##### Adding a listener

The listener is added by this line: 
[code] 
    		self.addListener(listener, self.ownerComp.par.Valuesend,
    					aParInfo['lomInfo']['min'], aParInfo['lomInfo']['max'])
    
[/code]

In addition to the listener itself,`addListener`accepts optional arguments for a Touch parameter that will send data for **setting** the listener. This data includes the parameter and the minimum and maximum values. 

##### The`onParPulse`and`doMap`Functions

At the bottom of the`AbletonParameterExt`extension are a couple more functions for the mapping feature of this Component. These are more advanced than the scope of this tutorial, but experienced users will be able to learn important techniques from these, including: 
1. Responding to a Pulse parameter (requires its own [Parameter Execute DAT](<./Parameter_Execute_DAT.md> "Parameter Execute DAT"))
  2. Requesting and responding to remote data from Live
  3. Opening a [PopDialog Custom COMP](<./Palette-popDialog.md> "Palette:popDialog")
  4. Setting LOM Parameters by traversing the hierarchy of song info
