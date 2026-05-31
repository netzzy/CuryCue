# PopDialog Custom COMP Examples

This page contains examples of how to set up a **popDialog** custom component. All examples assume a basic knowledge of TouchDesigner and Python.   
  
For full documentation of popDialog, see: [PopDialog Custom COMP](<./Palette-popDialog.md> "Palette:popDialog"). 

## Example 1 - Notification Pop-Up Dialog

In this example, we will create a very simple popDialog that gives the user a notification which must be clicked. 

##### Creating a popDialog

To create a popDialog, drag one from the [Palette](<./Palette.md> "Palette") (Derivative>UI folder) into your network. 

##### Setting the basic parameters

To create the example pop-up, go to the Pop Dialog custom parameter page and set the parameters to duplicate the image below: 
* **Title** : text for the title bar.
  * **Text** : main dialog text.
  * **Buttons** : number of buttons to display.
  * **Button Label 1** : text for button 1. **Note:** button 2 is ignored because Buttons is set to 1.
  * **On Esc Press Button** : if _Esc_ key is pressed, simulate a press of the chosen button.
  * **On Enter Press Button** : if _Enter_ key is pressed, simulate a press of the chosen button.
  * **Esc On Click Away** : if True, clicking anywhere but on the dialog (or switching to another application window) will simulate an _Esc_ key press.


For details on all popDialog parameters, see [popDialog wiki](<./Palette-popDialog.htm#Custom_Parameters_-_Pop_Dialog_Page> "Palette:popDialog"). 

##### Opening the popDialog

To test the popDialog, click the Open parameter. That works for testing, but a dialog like this is generally opened in a Python script. To open, simply invoke the popDialog's`Open`method. You can do so by typing this in the [textport](<./Textport.md> "Textport"):`op("_< path to your popDialog>_").Open()`## Example 2 - Selection Pop-Up Dialog

In this example, we will create a popDialog that gives the user a few buttons to choose from. We will also write a script to react to those buttons. 

##### Creating a popDialog

To create a popDialog, drag one from the [Palette](<./Palette.md> "Palette") (Derivative>UI folder) into your network. 

##### Setting the parameters

To create the example pop-up, go to the Pop Dialog custom parameter page and set the parameters to duplicate the image below: 

The following parameters are notably different from the first example: 
* **Title** : set to blank just to see what a popDialog looks like with no title bar.
  * **Buttons** : we want four buttons this time.
  * **Button Label 1-4** : these are the four options available.
  * **On Esc Press Button** : we want to pick the "Cancel" button if _Esc_ is pressed.
  * **On Enter Press Button** : since there is no obvious default choice for _Enter_ , just pick the "Cancel" button in this case too.


You can now test the dialog by clicking the Open parameter. It looks right, but doesn't do anything yet. 

##### Writing an onSelect callback

For this step, we will need a [Text TOP](<./Text_TOP.md> "Text TOP") in the network next to your popDialog. Create that and make sure its name is "text1". Now, to edit the popDialog's Callback DAT, click the Edit Callbacks parameter on the Callbacks page. Enter the following text into the DAT: 
[code] 
    def onSelect(info):
    	"""A button has been pressed"""
    	if info['button'] == "Cancel":
    		return
    	else:
    		textTOP = info['ownerComp'].op('../text1')
    		textTOP.par.alignx = info['buttonNum'] - 1
    
[/code]

The popDialog callbacks use the TouchDesigner [Python Callback System](</Python_Callback_System> "Python Callback System"), which sends all callbacks a single argument (`info`) which holds a dictionary of relevant information. In the`if`statement at the top of this callback, you can see that info['button'] holds the text of the button that was pressed. If that button is "Cancel" we exit the callback without doing anything. If not, we look at info['buttonNum'], which holds the number of the button pressed. This number, minus one, corresponds to the textTOP's alignx parameter to set the appropriate alignment. Notice that when identifying the textTOP location, we start from the popDialog itself, which is stored in info['ownerComp']. 

Save your callback DAT and try the popDialog again while looking at the text1. Pressing the dialog buttons now sets the alignment of the text! 

## Example 3 - Text Entry Pop-Up Dialog

In this example, we will create a popDialog that allows the user to enter text. We will also write a script to use that text. 

##### Creating a popDialog

To create a popDialog, drag one from the [Palette](<./Palette.md> "Palette") (Derivative>UI folder) into your network. 

##### Setting the parameters

To create the example pop-up, go to the Pop Dialog custom parameter page and set the parameters to duplicate the image below: 

The following parameters are notably different: 
* **Text Entry Area** : if True, the dialog will have a text entry field.
  * **Text Entry Default** : the text that will start in the text entry field.


You can now test the dialog by clicking the Open parameter. It looks right, but doesn't do anything yet. 

##### Writing another onSelect callback

For this step, we will need a [Text TOP](<./Text_TOP.md> "Text TOP") in the network next to your popDialog. You can use the one from example 2. Make sure its name is "text1". Now, edit the popDialog's Callback DAT to contain the following text: 
[code] 
    def onSelect(info):
    	"""A button has been pressed"""
    	if info['button'] == "Cancel":
    		return
    	else:
    		textTOP = info['ownerComp'].op('../text1')
    		textTOP.par.text = info['enteredText']
    
[/code]

This callback is similar to the one in example 2. The only real difference is we set the textTOP's text parameter to info['enteredText']. 

Save your callback DAT and try the popDialog again while looking at the text1. Entering text now sets the TOP's contents. 

## Example 4 - Creating a Pop-Up Dialog using script

In this example, we will create a popDialog entirely from script. 

In actual practice, you will rarely have to work with the parameters of an individual popDialog. Since popDialog is designed with the idea that only one will be on screen at a time, it is generally safe to just use the system popDialog located in op.TDResources. **TIP:** If you do use the system dialog, be sure to provide all the arguments to the`Open`method OR (better yet) use the`OpenDefault`method. 

##### Creating a popDialog script

To begin, create a [Text DAT](<./Text_DAT.md> "Text DAT") in your network. Enter the following text: 
[code] 
    def dialogChoice(info):
    	debug(info['button'])
    	debug(info['details'])
    
    op.TDResources.PopDialog.OpenDefault(
    			text='This is a dialog',
    			title='The title',
    			buttons=['OK', 'NO'],
    			callback=dialogChoice,
    			details='Any python object',
    			textEntry=False,
    			escButton=2,
    			enterButton=1,
    			escOnClickAway=True)
    
[/code]

This script does two things. It defines the callback for the dialog, then opens it. The`dialogChoice`function will work exactly like the onSelect callback used in the last two examples. The command after that opens the system popDialog. Most of the arguments are obvious, with the exceptions being the`callback`argument, which takes a python function to be called when a selection is made and the`details`argument which contains a single python object containing whatever user information you may need in the callback. **Note:**`details`can contain a list or dictionary if multiple bits of user information is needed. 

To open the dialog, right-click on the Text DAT and select Run Script. Save your callback DAT and try the popDialog again while looking at the text1. Entering text now sets the TOP's contents.
