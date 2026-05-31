# TDI Library

## The TDI Library is only available for builds in 2025.30000 and later

## TouchDesigner Interface Library

The **TDI Library** contains all the information necessary for TouchDesigner popup help and code-completion in **Microsoft Visual Studio Code (VS Code)**. It contains the wiki help and Python description of all builtin TouchDesigner objects, classes and functions. In addition to help and auto-completion, using TDI library will eliminate error and warning indicators when using VS Code to edit TouchDesigner Python. 

Note that this library does not contain actual code for the TouchDesigner objects, only stub information sufficient to provide editor help. 

Future iterations will make TDI Library work with other editors. 

## Setting up TDI

The setup for TDI is simple and uses VS Code extensions that are automatically packaged with the editor. 

### Install VS Code

You will need [Microsoft Visual Studio Code](<https://code.visualstudio.com/>) installed. Nothing else special. 

### Set Up TouchDesigner to Use VS Code

To set up TouchDesigner to use VS Code as its standard text editor: 
1. From the menu choose **Edit >Preferences**.
  2. Go to the **DATs** tab.
  3. In the **Text Editor** entry, browse to and select VS Code.

### Activate Python Extensions in VS Code

Activate these extensions in VS Code if they are not already activated: 
* Python
  * Pylance


TDI is designed to be used with these standard Python extensions, which are included in a standard VS Code install. For more information about installing/activating extensions in VS Code, see <https://code.visualstudio.com/docs/editor/extension-marketplace>. 

### Switch VS Code Python Interpreter to TouchDesigner

To activate TDI, you just need to tell VS Code to use the Python executable in your TouchDesigner installation. To do this, follow these steps: 
1. Open the VS Code command palette (Win:ctrl-shift-P / macOS:cmd-shift-P)
  2. Type or select "Python: Select Interpreter"
  3. Select "Enter interpreter path..." from the menu
  4. Browse to or directly enter the path to TouchDesigner's Python executable.
* On PC this is usually **< your TD install folder>/bin/Python.exe**.
  * On Mac this is usually **/Applications/TouchDesigner.app/Contents/Frameworks/Python.framework/Versions/Current/bin/python3.11**
  * When in doubt, you can type`app.pythonExecutable`in the TouchDesigner textport. This returns the path to paste into VS Code.


**Note:** you may have to repeat this step each time you install a new TouchDesigner build. 

### Testing the TDI installation

At this point, installation is complete. It may take the editor a minute to load all the TouchDesigner information. To test if it's working: 
1. Drop a Parameter Execute DAT in your TouchDesigner network.
  2. On the DAT, select **RMB >Edit Contents...**. The file will open in VS Code.
  3. There may be a **Restricted Mode warning message** at the top of VS Code about working in a trusted environment. If there is, click "Manage" and then "Trust". You can also tell you're in restricted mode by the word "Resticted" in the bottom left of the editor, which is also clickable to change the setting. When in Restricted Mode, the TDI Library will not function properly.
  4. in VS Code, in the DAT text, type`me`. You should see something like the image below:

## Using TDI

Be sure that your TDI Library is working properly with the installation test above before using the following features. 

### Popup Help and Autocomplete

TDI provides a number of automatic features to help you work. For example, type`containerC`into a Python file in VS Code. You'll see the autocomplete menu for containerCOMP pop up. If you don't already have it set to show more extra info, you can hover over the right end of the highlight and press the`>`caret to show additional help info. 

When you type`containerCOMP.`you will see a menu of all the available members of Container Comps. Scrolling through them using arrow keys with the extra help info on will let you browse the help for each of them. 

Similarly, typing`containerCOMP.par.`will show you a list of all of containerCOMP's built-in parameters and help for each of them. 

### Providing Type Hints

While popup help and autocomplete will work automatically for TouchDesigner specific items, such as`me`or`debug()`, there are many situations in which you will have to give the editor a little more information. To do this you will use **Python type annotations** , a.k.a. **type hints**. 

The basic idea is that you can use the syntax`variable : type =`to tell VS Code what type the TouchDesigner object is. VS Code will then be able to provide help for that object whenever you use it later in the code. 

For example, if you have a Movie File In TOP called "movie1", you would use the following code: 
[code] 
    movie : moviefileinTOP = op('movie1')
    movie.par.play = False
    
[/code]

Because VS Code has no idea what type of operator`op('movie1')`returns, you have to include the type hint in your code so that the editor's code analysis can work. Now when you hover over the words`movie`,`par`, or`play`, VS Code will pop up info about each element. 

Another common usage of type hints would be in Python [Extensions](<./Extensions.md> "Extensions"). If you are writing an extension for a Container Component, you would likely use this in your extension`__init__`method: 
[code] 
    self.ownerComp : containerCOMP = ownerComp
    
[/code]

With the addition of this line, every time you access`self.ownerComp`in your extension, VS Code will know that it is a containerCOMP and provide autocomplete and popup help accordingly. 

A couple more examples: 
[code] 
    # function definition with type hints for arguments and return
    def exampleFunction(arg1 : clockCHOP, arg2 : Par) -> DAT
        # this useless function takes a clockCHOP and a parameter as arguments and returns a DAT
        print(arg1, arg2)
        return me
    
    # Because VS Code doesn't know what OP type "me" is, you can use this:
    me : parameterexecuteDAT = me
    
[/code]

For a crash course in Python annotations, go [here](<https://dev.to/dan_starner/using-pythons-type-annotations-4cfe>). 

### Determining Types

As you can see by the above examples, to use TDI to its full potential, it is important to know what type of Python objects you are using in your scripts. For operators, to see the name of their Python class, you can click on the Python Help... icon at the top of the parameter dialog. These are by far the most common class names you will need when using TDI. For other Python objects, if you need to know their class name, you can use`debug(<object>)`to return a string that includes the class name. 

### Go To Definition

Another feature that is sometimes useful in VS Code is`RMB>Go to Definition`. When you use this feature on a TD Python object in the editor, it will jump to the TDI Library stub file that contains all the information about that object. There, you can see all the object's members and help strings. You will also see some of the inner workings of TDI Library if you are curious about that sort of thing. 

Of course, you may want to go deeper down the definition rabbit hole, and you can always "Go to Definition" of the objects in the newly opened file. 

### Advanced Type Checking in Editors

The following tips are for using more strict type checking in your editor, e.g. PyLance's type checking mode. Because Python is not strictly type-checked, these features are only important if you set up your editor to warn you when there are type mismatches: [![TypeError.png](./images/4/4d/TypeError.png)](</File:TypeError.png>)

The above shows PyLance complaining because op() returns an object of type`OP`, which can't necessarily be cast to an object of type`constantTOP`. To fix this, we can use the`OP.asType()`function. 
[code] 
    a = op('constant1')
    a = a.asType(contantTOP)
    
[/code]

In the above solution, the variable`a`will show constantTOP code hints and PyLance won't complain. The reason we can't do this in one line is that`op()`can return`None`, and PyLance will complain that`None`doesn't have an`asType`function. For a one-liner solution, use`opex`, which raises an exception instead of returning None when the operator is not found: 
[code] 
    a = opex('constant1').asType(contantTOP)
    
[/code]

If you want TouchDesigner to raise an exception if you try to use`asType`with an invalid type for the operator in question, you can use the checkType argument: 
[code] 
    a = opex('someOperator').asType(contantTOP, checkType=True)
    
[/code]

## Custom Components and Parameters

Currently, TDI is not set up to provide help for custom components and parameters. Future versions will include this feature. 

## Using Multiple TouchDesigner Builds

If you use multiple TouchDesigner builds and you want to point VS Code's Python interpreter to different builds for different projects, you will need to set up VS Code workspaces. For info about how to do that, see <https://code.visualstudio.com/docs/editor/workspaces>. Once you are in a workspace, VS Code will remember which Python interpreter you set up for that workspace. When editing Python code for that TouchDesigner project, just be sure to open the VS Code workspace first. If you don't open the workspace first, VS Code just uses the last Python interpreter you selected when not using a workspace. 

## Troubleshooting

If you have trouble installing or otherwise, and especially with any of the below problems, please post in the [forum](<https://forum.derivative.ca/>) or send an email to [support@derivative.ca](<http://mailto:support@derivative.ca>). 

### Missing Help

If you find TouchDesigner objects where the help/autocomplete is incorrect or non-existent, please send your entire script file with a list of problem objects. 

### Other Editors

Currently TDI Library is designed specifically for use with VS Code. The code is fairly standard however, and all exists in the`Lib/tdi`folder of your TouchDesigner installation. If you use another editor and want to collaborate on making TDI work, send an email!
