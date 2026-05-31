# Options Class

The Options class describes the set of configurable UI options. It can be accessed with the ui.options object. 

## Members

No operator specific members. 

## Methods`resetToDefaults()`→`None`: 

> Reset all options to their default values.

### Special Functions`len(Options)`→`int`: 

> Returns the total number of options. 
[code]
>     a = len(ui.options)
>     
[/code]`[<option name>]`→`value`: 

> Get or set specific option given an option name key. 
[code]
>     v = ui.options['DAT.width']
>     ui.options['DAT.width'] = 50
>     
[/code]`Iterator`→`str`: 

> Iterate over each option name. 
[code]
>     for n in ui.options:
>     	print(n) # print the name of all options
>     
[/code]

  
TouchDesigner Build: Latest\n2021.100002018.28070before 2018.28070
