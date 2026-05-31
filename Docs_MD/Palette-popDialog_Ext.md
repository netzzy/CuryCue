# Palette:popDialog Ext

These Extensions reference a specific [Palette:popDialog](<./Palette-popDialog.md> "Palette:popDialog").   
  
# PopDialogExt

The PopDialogExt extension provides script functionality for working with popDialog. Frequently used methods are listed here. A full list can be found using the Python`help()`function. 

## Members

No operator specific members. 

## Methods`PopDialogExt.Open(text=None, title=None, buttons=None, callback=None, details=None, textEntry=None, escButton=None, escOnClickAway=None, enterButton=None)`: 

> Open a popup dialog. 
> 
>   * text goes in the center of the dialog. Default None, use pars.
>   * title goes on top of the dialog. Blank means no title bar. Default None, use pars
>   * buttons is a list of strings. The number of buttons is equal to the number of buttons, up to 4. Default is ['OK']
>   * callback: a method that will be called when a selection is made, see the SetCallback method. This is in addition to all internal callbacks. If not provided, Callback DAT will be searched.
>   * details: will be passed to callback in addition to item chosen. Default is None.
>   * If textEntry is a string, display textEntry field and use the string as a default. If textEntry is False, no entry field. Default is None, use pars
>   * escButton is a number from 1-4 indicating which button is simulated when esc is pressed or False for no button simulation. Default is None, use pars. First button is 1 not 0!!!
>   * enterButton is a number from 1-4 indicating which button is simulated when enter is pressed or False for no button simulation. Default is None, use pars. First button is 1 not 0!!!
>   * escOnClickAway is a boolean indicating whether esc is simulated when user clicks somewhere besides the dialog. Default is None, use pars
>`PopDialogExt.OpenDefault(text=_, title=_ , buttons=['OK'], callback=None, details=None, textEntry=False, escButton=1, escOnClickAway=True, enterButton=1)`: 

> Opens a popup dialog using defaults that don't rely on parameter settings.`PopDialogExt.Close(self)`: 

> Close the dialog. No button will be simulated and the selection callback will not be called.`PopDialogExt.OnButtonClicked(buttonNum)`: 

> Simulates a click of the provided button. 
> 
>   * buttonNum - the button number (1-4!) to simulate.
>`PopDialogExt.OnClickAway(self)`: 

> Callback for esc pressed. Only happens when Escbutton is not None.`PopDialogExt.OnKeyPressed(key)`: 

> Callback for esc or enterpressed.

# CallbacksExt

The CallbackExt extension provides Python callback functionality to custom components. All callbacks will be passed a single argument containing an info dictionary. Callbacks can be defined in the DAT named in the Callback DAT parameter. To report all callbacks to the textport, turn on the Print Callbacks toggle parameter. The Callback DAT and Print Callbacks parameters are often found on the Callbacks parameter page, but their location can be customized. 

The info dictionary always contains an "ownerComp" key. It will also have a "callbackName" key holding the callback name. It will sometimes contain an "about" key, describing the callback, and should always contain this key if a return value is expected. Generally, callbacks are called AFTER the internal method they are associated with, to allow over-riding of whatever that method does. 

See also: [CallbacksExt Extension](<./CallbacksExt_Extension.md> "CallbacksExt Extension")

## Callbacks

The following python callbacks are associated with this operator. 
[code] 
    #Shared Use License: This file is owned by Derivative Inc. (â€œDerivativeï¿½) 
    #and can only be used, and/or modified for use, in conjunction with 
    #Derivativeâ€™s TouchDesigner software, and only if you are a licensee who 
    #has accepted Derivativeâ€™s TouchDesigner license or assignment agreement 
    #(which also governs the use of this file).  You may share a modified version 
    #of this file with another authorized licensee of Derivativeâ€™s TouchDesigner 
    #software.  Otherwise, no redistribution or sharing of this file, with or 
    #without modification, is permitted.
    
    """
    All callbacks for this popDialog go here. For a list of available callbacks,
    see:
    
    https://www.derivative.ca/wiki099/index.php?title=PopDialog_Custom_COMP#PopDialog_Callbacks
    """
    
    # def onSelect(info):
    # 	""" A selection has been made in the dialog. 
    #       This is another way to achieve the effect of providing a callback via the Open method. 
    #       The data provided in the info dictionary is as follows:
    #       * buttonNum: The number (1-4) of the pressed button.
    #       * button: The label of the pressed button.
    #       * enteredText: The text in text entry field. Only provided if the dialog is set for text entry.
    #       * details: The details provided in Open method."""
    # 	pass
    
    # def onOpen(info):
    #	"""Dialog has been opened"""
    # 	pass
    
    # def onClose(info):
    #	"""Dialog has been closed"""
    # 	pass
    
[/code]
