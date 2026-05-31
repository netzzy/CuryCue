# Category:Python

## Python In TouchDesigner

TouchDesigner uses [Python](<https://www.python.org/>) for scripting tasks. A custom Python build is included, with most of the features of a standard Python installation and a huge number of tools and utilities specific to working in the software. 
* Quick Start: [Tutorial: Introduction to Python in TouchDesigner](<./Introduction_to_Python_Tutorial.md> "Introduction to Python Tutorial").
  * Common script examples: [Python Tips](<./Python_Tips.md> "Python Tips")
  * List of [TouchDesigner Python Classes and Modules](<./Python_Classes_and_Modules.md> "Python Classes and Modules")
  * Index of all Python pages in this wiki: [Python Reference](<./Category-Python_Reference.md> "Category:Python Reference")


In addition, selecting **Help - > Python Examples** in the TouchDesigner UI takes you to the`PythonExamples.toe`file with 100+ working examples. 

## Learning Python

If you don't know Python, here are some good resources for learning: 
* [The official Python tutorial](<https://docs.python.org/3/tutorial/index.html>)
  * [Python Learning Resources](<https://docs.python-guide.org/intro/learning/>)
  * [List of online Python courses](<https://www.pcworld.com/article/3287981/best-python-courses.html>)
  * [General programming courses at codeacademy.com](<http://www.codeacademy.com>)
  * [Python cheat sheet](<http://overapi.com/python>)
  * [Python at freeCodeCamp](<https://www.freecodecamp.org/news/freecodecamp-python-courses-ranked-from-best-to-worst/>)
  * alphamoonbase's tips and tricks: [Part 1](<https://derivative.ca/community-post/python-tipsntricks>), [Part 2](<https://derivative.ca/community-post/python-tipsntricks-2>), [Part 3](<https://derivative.ca/community-post/python-tipsntricks-3>) \- real-world python-in-TouchDesigner experience

## Python Classes and Modules Available in TouchDesigner

TouchDesigner includes all the modules in a [standard Python installation](<https://docs.python.org/3.11/library/>) plus the following: 

###`td`: TouchDesigner's Main Python Module

**All[td module](<./Td_Module.md> "Td Module") members and methods are available in scripts, expressions, and the textport.** There is no need to import the module or its members explicitly. This is especially important in expressions, which don't allow import statements. 

The following can be found in the`td`module: 
* **[Main TouchDesigner utilities](<./Td_Module.md> "Td Module")** \- the most basic starting points for interacting with TouchDesigner, such as`me`and`op()`.
  * **[TouchDesigner Python helper classes](<./Python_Classes_and_Modules.htm#Helper_Classes> "Python Classes and Modules")** \- important helper objects used to organize functions and information pertaining to a specific part of TouchDesigner.
  * **[Operator related classes](<./Python_Classes_and_Modules.htm#Operator_Related_Classes> "Python Classes and Modules")** \- every [Operator](<./Operator.md> "Operator") in TouchDesigner has an associated Python class in the`td`module. Their wiki pages can be accessed by clicking on the Python Help button in their [parameter dialog](<./Parameter_Dialog.md> "Parameter Dialog"). There are also a number of associated Python objects that are used when working with Operators.
  * **[Useful standard Python modules](<./Python_Classes_and_Modules.htm#Standard_Python_Modules> "Python Classes and Modules")** \- the`td`module also automatically imports a number of helpful standard modules (e.g.`math`), allowing them to be accessed in expressions through their namespace.

### TouchDesigner Utility Modules

TouchDesigner also contains utility modules for advanced Python programming. Utility modules are not imported into the`td`module automatically. Instructions for their use can be found on their wiki pages. 
* **[List of Python Utility Modules and Python Utilities](<./Python_Classes_and_Modules.htm#TouchDesigner_Utility_Modules_and_Python_Utilities> "Python Classes and Modules")**.

### 3rd Party Packages

TouchDesigner includes a number of 3rd party Python packages that are generally useful when working with the software. These are not included in the`td`module so must be imported explicitly. 
* **[List of 3rd party Python Packages](<./Python_Classes_and_Modules.htm#3rd_Party_Packages> "Python Classes and Modules")**.

### Installing Custom Python Packages

Part of the great power of Python is its access to the countless number of modules that have been created. If you want to use modules that are not included in the above, use the following steps: 

Note: When adding your own version for a package that is already shipped with TouchDesigner, you might encounter unexpected behaviors. Many of our internal tools and palette components rely on NumPy and/or OpenCV. **Loading different versions of Numpy and/or OpenCV is at your own risk.** Some other issue could be with the following: considering a Package A with a dependency B, if updating your sys.path cause a different version of dependency B to load first, it could cause issues with Package A. 

#### Windows
1. Install a parallel copy of the same version of Python to the hard disk. The current version of Python shipped with TouchDesigner is 3.11. It can be found [here](<https://www.python.org/downloads/>). Use the most recent subversion of 3.11. 
     1. Alternatively, you can use a Python package and environment manager, [such as Anaconda](<https://derivative.ca/community-post/tutorial/anaconda-managing-python-environments-and-3rd-party-libraries-touchdesigner>).
  2. Install the package to the parallel python installation, following its normal installation procedure.
  3. Launch Python and import the module manually to make sure there are no errors outside of the TouchDesigner context.


Once the module is successfully installed, you can import it in TouchDesigner following those next steps: 

Under the Edit->Preferences menu, tick "Add External Python to Search Path". You can add the search path by modifying the Preference labelled "Python 32/64 bit Module Path". Multiple paths are separated by semicolons (`;`). 

Finally you can modify the search path directly by either modifying the system environment variable`PYTHONPATH`or by **firing an[Execute DAT](<./Execute_DAT.md> "Execute DAT") onStart()** with the code snippet below. 
[code] 
    import sys
    mypath = "C:/Python311/Lib/site-packages" # use the correct path to your installation, sometimes in a user folder
    if mypath not in sys.path:
    	sys.path = [mypath] + sys.path
    
[/code]

This script will prepend your custom Python install site-packages folder to your PATH. Prepending will make sure that your custom packages, when being imported, **will have priority over any other package with a matching package name found** in the path. If the package is not found in the custom path, but a package of the same name is found in the TouchDesigner Python site-packages folder then **it will fall back on this package**. 

Users can also import packages from Python installations that weren't installed with the official Python installer but with alternative Python package and environment managers, [such as Anaconda](<https://derivative.ca/community-post/tutorial/anaconda-managing-python-environments-and-3rd-party-libraries-touchdesigner>). 

Examples of other useful Python modules are [here](<http://wiki.python.org/moin/UsefulModules>). 

#### MacOS

On MacOS, use [Homebrew](<https://brew.sh/>) to manage your Python installations. Follow the instructions on Homebrew's website to get started. 

When Homebrew is installed, you can use the command`brew install python@3.11`to install Python on your system. The`@3.11`after`python`sets the version, which must be the same as TouchDesigner's. 

##### Intel Macs

On Intel's Macs, your default Homebrew path should be`/usr/local/bin/brew`##### ARM Macs

On ARM's Macs, your Homebrew path should be`/opt/homebrew/bin/brew`, **for the native ARM homebrew**. That is, when using the default Homebrew install command. 

**NOTE:** In some cases, you might want to run Homebrew Rosetta. It is required if you are using the non-native / Intel TouchDesigner build and require a Python version that is not available as an ARM installer on MacOS. 

To install Homebrew Rosetta, use the following command:`arch -x86_64 /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"`. Your Homebrew Rosetta path should be`/usr/local/bin/brew`. 

If you have both Homebrew versions installed on your system, it is advised to add an alias for the Homebrew Rosetta installation. Use the following command in your terminal`alias ibrew="arch -x86_64 /usr/local/bin/brew"`where`ibrew`stands for Intel Brew. You can add this alias to your terminal profile so that it is persistent. 

You can now use either`brew install YOUR_APP_NAME`or`ibrew install YOUR_APP_NAME`to install ARM or Intel formulas or casks respectively. 

Continue with your python installation, matching TouchDesigner's Python, as described at the top of this MacOS section. Remember, if you followed the previous steps: when your are using the ARM native TouchDesigner build, use`brew`, if it's the Intel build running with Rosetta, use`ibrew`. 

It can also be useful to add extra aliases, and precede them with an`i`when they are related to Intel / Rosetta, for Python itself, and pip: 
[code] 
    alias iPY311=/usr/local/opt/python@3.11/bin/python3
    alias iPIP311=/usr/local/opt/python@3.11/bin/pip3
[/code]

Now, all you have to do is install your custom (Intel) Python 3.11 packages using`iPIP311 install YOUR_PACKAGE_NAME`. 

Once the module is successfully installed, you can import it in TouchDesigner following these next steps: 

Under the Edit->Preferences menu, tick "Add External Python to Search Path". You can add the search path by modifying the Preference labelled "Python 32/64 bit Module Path". Multiple paths are separated by semicolons (`;`). You can enter the path to your Python packages (usually`<python install>/Lib/site-packages`) 

If the preferences method doesn't work for you, there are a couple other methods: you can modify the Python search path directly by either modifying the **system environment variable`PYTHONPATH`** or by **setting up an[Execute DAT](<./Execute_DAT.md> "Execute DAT") onStart()** with the code snippet below. 
[code] 
    import sys
    mypath = "/usr/local/lib/python3.11/site-packages" # TIP: This path is printed out in the terminal when installing this Python version with Homebrew
    if mypath not in sys.path:
    	sys.path = [mypath] + sys.path
    
[/code]

This script will prepend your custom Python install site-packages folder to your PATH. Prepending will make sure that your custom packages, when being imported, **will have priority over any other package with a matching package name found** in the path. If the package is not found in the custom path, but a package of the same name is found in the TouchDesigner Python site-packages folder then **it will fall back on this package**. 

#### I am getting the following ImportError, what should I do ? ImportError: DLL load failed while importing […]

For most cases, it is better to document your environment and to share the project and steps to reproduced with the Derivative team at forum.derivative.ca 

If you feel adventurous, what is likely to happen is that there is a dependency conflict causing an issue between TouchDesigner and the Python library you are attempting to use. 

You can use a tool such as [Dependencies](<https://github.com/lucasg/Dependencies>) to get an idea of which libraries your package is depending on. You drag n drop your python package binary, pyd, to the tool and you can see what are the libraries it is depending on. Then you investigate further to find what library might already be used by TouchDesigner, going through the dependencies of dependencies. Tedious. 

## Python Gotchas

There are a few things in standard Python that can trip you up in TouchDesigner. If you find anything that's not included here, post in the forum! 
* Some TouchDesigner objects (especially parameters and CHOP channels) will try to act as the correct data type for their context. For example, a Float parameter object (`myOp.par.Float1`) will act like a floating point number _in most cases_ , but it is still a parameter object. For example`round(myOp.par.Float1)`will not work. To get the actual value of a parameter or channel, use its`.eval()`method. If you think you may be encountering this problem, you can tell the difference by using the`repr`function. For example`repr(myOp.par.Float1)`will show that this is a parameter and not a number.
  * same goes with operator parameter types. if a parameter is a path to a CHOP,`n.par.Chop`usually works, but to be safe,`n.par.Chop.eval()`always works.
  *`subprocess.Popen`doesn't work with file-like objects. See [this forum post](<https://forum.derivative.ca/t/resolved-td-specific-stdoutcatcher-object-has-no-attribute-fileno/140106>) for details.
  * Python threads don't have access to TouchDesigner objects. Search "threading" in the forum to see some workarounds. As of TouchDesigner 2023.31500+, see [Python threading in TouchDesigner](<./Python_threading_in_TouchDesigner.md> "Python threading in TouchDesigner") and [Thread Manager](<./Thread_Manager.md> "Thread Manager").

## More In The Python Category

## Subcategories

This category has only the following subcategory. 

### P
* [Python Reference](<./Category-Python_Reference.md> "Category:Python Reference")

## Pages in category "Python"

The following 27 pages are in this category, out of 27 total. 

### C
* [CallbacksExt Extension](<./CallbacksExt_Extension.md> "CallbacksExt Extension")

### D
* [Debug module](<./Debug_module.md> "Debug module")
  * [Experimental:Debug module](</Experimental:Debug_module> "Experimental:Debug module")
  * [Dependency](<./Dependency.md> "Dependency")
  * [Dependency Class](<./Dependency_Class.md> "Dependency Class")
  * [Experimental:Dependency Class](</Experimental:Dependency_Class> "Experimental:Dependency Class")

### E
* [Extensions](<./Extensions.md> "Extensions")
  * [Talk:Extensions](<./Talk-Extensions.md> "Talk:Extensions")
  * [Experimental:Extensions](</Experimental:Extensions> "Experimental:Extensions")

### I
* [Introduction to Python Tutorial](<./Introduction_to_Python_Tutorial.md> "Introduction to Python Tutorial")

### P
* [Procedural](<./Procedural.md> "Procedural")
  * [Python Classes and Modules](<./Python_Classes_and_Modules.md> "Python Classes and Modules")
  * [Experimental:Python Classes and Modules](</Experimental:Python_Classes_and_Modules> "Experimental:Python Classes and Modules")
  * [Python f-strings](<./Python_f-strings.md> "Python f-strings")
  * [Python Tips](<./Python_Tips.md> "Python Tips")

### R
* [Run Command Examples](<./Run_Command_Examples.md> "Run Command Examples")
  * [Experimental:Run Command Examples](</Experimental:Run_Command_Examples> "Experimental:Run Command Examples")

### S
* [Storage](<./Storage.md> "Storage")
  * [StorageManager Class](<./StorageManager_Class.md> "StorageManager Class")

### T
* [Td Module](<./Td_Module.md> "Td Module")
  * [Experimental:Td Module](</Experimental:Td_Module> "Experimental:Td Module")
  * [TDFunctions](<./TDFunctions.md> "TDFunctions")
  * [TDJSON](<./TDJSON.md> "TDJSON")
  * [TDStoreTools](<./TDStoreTools.md> "TDStoreTools")

### W
* [Working with CHOPs in Python](<./Working_with_CHOPs_in_Python.md> "Working with CHOPs in Python")
  * [Working with DATs in Python](<./Working_with_DATs_in_Python.md> "Working with DATs in Python")
  * [Working with OPs in Python](<./Working_with_OPs_in_Python.md> "Working with OPs in Python")
