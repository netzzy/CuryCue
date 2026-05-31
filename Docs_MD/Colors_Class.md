# Colors Class

The Colors Class describes the application colors. It can be accessed from the global [ui](<./UI_Class.md> "UI Class") object. 

## Members

No operator specific members. 

## Methods`resetToDefaults()`→`None`: 

> Set the colors to their default values.

### Special Functions

The Colors class is an iterable object that contains a set of named color attributes. The len, subscript and assignment operators are defined. 

Each name can be used to get or set a triplet of values corresponding to that color.`len(Colors)`→`int`: 

> Returns the total color options. 
[code]
>     a = len(ui.colors)
>     
[/code]`[<color option name>]`→`triplet(r,g,b)`: 

> Get or set specific color option, given a string key. 
[code]
>     n = ui.colors['default.bg']
>     ui.colors['default.bg'] = (1,0,0)
>     
[/code]`Iterator`→`str`: 

> Iterate over each color option name. 
[code]
>     for n in ui.colors:
>     	print(n)
>     	ui.colors[n] = myColorsList[n]
>     
[/code]

  
TouchDesigner Build:  Latest\n2022.24140 2021.10000 2018.28070 before 2018.28070
