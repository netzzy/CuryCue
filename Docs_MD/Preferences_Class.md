# Preferences Class

The Preferences class describes the set of configurable preferences that are retained between sessions. It can be accessed with the ui.preferences object or through the [Preferences Dialog](<./Dialogs-Preferences_Dialog.md> "Dialogs:Preferences Dialog"). 

## Members`defaults`→`dict`**(Read Only)** : 

> A dictionary of preferences with their default values.

## Methods`save()`→`None`: 

> Save preference values to disk. Unless saved, changes to preferences will be lost, next time application is started.`resetToDefaults()`→`None`: 

> Reset all preferences to their default values.`load()`→`None`: 

> Restore preference values from disk.

### Special Functions`len(Preferences)`→`int`: 

> Returns the total number of preferences. 
[code]
>     a = len(ui.preferences)
>     
[/code]`[<preference name>]`→`value`: 

> Get or set specific preference given a preference name key. 
[code]
>     v = ui.preferences['dats.autoindent']
>     ui.preferences['dats.autoindent'] = 0
>     
[/code]`Iterator`→`str`: 

> Iterate over each preference name. 
[code]
>     for p in ui.preferences:
>     	print(p) # print the name of all preferences
>     
[/code]

  
TouchDesigner Build:  Latest\n2021.10000 2018.28070 before 2018.28070
