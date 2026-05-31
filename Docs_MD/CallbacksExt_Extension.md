# Python Callback System

The **CallbackExt** extension provides Python callback functionality to custom components. All callbacks will be passed a single argument containing an **info dictionary**. Callbacks can be defined in the DAT named in the **Callback DAT** parameter. To report all callbacks to the textport, turn on the **Print Callbacks** toggle parameter. The Callback DAT and Print Callbacks parameters are often found on the Callbacks parameter page, but their location can be customized. 

The info dictionary always contains an "ownerComp" key. It will also have a "callbackName" key holding the callback name. It will sometimes contain an "about" key, describing the callback, and should always contain this key if a return value is expected. Generally, callbacks are called AFTER the internal method they are associated with, to allow over-riding of whatever that method does. 

TouchDesigner's Python callback system uses the CallbacksExt Extension. 

# Adding CallbackExt to a Component

The standard way to add **CallbackExt** to a component is to use the [palette:callbacksHelper](<./Palette-callbacksHelper.md> "Palette:callbacksHelper") component. 

# Methods

**`DoCallback(_callbackName, callbackInfo=None, callbackOrDat=None_)`→`callbackInfo | None`**

    If it exists, call the named callback in`ownerComp.par.Callbackdat`and return`callbackInfo`with the callback's return value placed in`callbackInfo['returnValue']`.
    If a user callback was found, returns callbackInfo with the callback return value in callbackInfo['returnValue']. If no callback found, this returns None.
    If`ownerComp`has a parameter called`Printcallbacks`, and that parameter is`True`, callback debug info will be printed to textport.`DoCallbacks`is the main function you will use when implementing a callback system with CallbacksExt. 

  *`callbackName`\- Name of callback to be called
  *`callbackInfo`\- **(Optional)** an object that will be passed to the callback as its sole argument. Default is a dictionary with ownerComp and callbackName keys. This object can be of any type. If a dictionary is passed and it doesn't contain "ownerComp" or "callbackName" keys, those keys will be added automatically..
  *`callbackOrDat`\- **(Optional)** a DAT or function to pass callbacks to. If this is a DAT, the callback will be called from the named callback in the DAT. If this is a function, the callback will be called directly. If this is None (default) the callback will be called from the callback DAT set in ownercomp's callbackDAT parameter.


**`EditCallbackDAT()`**

    Edit the Callback DAT in default editor

**`SetAssignedCallback(callbackName, callback, details=None)`**

    **Note:** This is an expert feature, not for general use.
    An assigned callback sets the callback system up to call a specified python method rather than searching a callback DAT. When this is set, <callback> will be called by default when DoCallback(<callbackName>) is called. 

  *`callbackName`\- Name of callback to be called
  *`callback`\- The callback or None to remove the assigned callback
  *`details`\- **Optional** extra info to be passed in the ['details'] key of infoDict when callback is called.


**`PassCallbacksTo(passTarget)`**

    **Note:** This is an expert feature, not for general use.
    Set a target DAT or function for passing callbacks that are not found in the callback DAT. This allows you to set up a backup behavior for when callbacks are not found in the callback DAT. 

  *`passTarget`\- a DAT or function


**`PassOnCallback(info)`**

    **Note:** This is an expert feature, not for general use.
    Pass this callback to PassTarget. This is meant to be called from within a callback to intentionally pass it on. Use PassCallbacksTo to set PassTarget. 

  *`info`\- the callback's info object


\-->

# Members

**`CallbackDat`**

    Get or set the dat containing user callbacks. This will set the value of the Callbackdat parameter as well, if it exists.

**`PrintCallbacks`**

    Get or set whether to print callback info to the Textport

**`PassTarget`**

    The backup DAT or function assigned in the`PassTargetTo`method above.
