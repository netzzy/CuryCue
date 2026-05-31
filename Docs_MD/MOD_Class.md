# MOD Class

The MOD class provides access to Module On Demand object, which allows [DATs](<./DAT.md> "DAT") to be dynamically imported as modules. It can be accessed with the mod object, found in the automatically imported [td module](<./Td_Module.md> "Td Module"). Alternatively, one can use the regular python statement: import. Use of the import statement is limited to modules in the search path, where as the mod format allows complete statements in one line, which is more useful for entering expressions. Also note that DAT modules cannot be organized into packages as regular file system based python modules can be.   
  
## Members

No operator specific members. 

## Methods

No operator specific methods. 

## Usage

There are three methods to import DATs as modules in a script. 

  *`import datName`Import the module defined by the DAT named datName. All regular import options are supported (from, as, etc). If a DAT is not found, the regular file system search path is then used.
[code]# import a DAT named addMonth
        import addMonths
        
[/code]

  *`m = mod.datName`Import the module defined by the DAT named datName.
[code]m = mod.addMonths(1,2,3)
        
[/code]

  *`m = mod(pathToDat)`Similar to above, except a path to the DAT can be used.
[code]m = mod('myMods/adders').addMonths(1,2,3)
        
[/code]

## Comparing Usage

Example using import: 
[code] 
    import myUtils
    a = myUtils.add(5,6)
    
[/code]

Same example using mod: 
[code] 
    a = mod.myUtils.add(5,6)
    
[/code]

Example using mod outside the search path: 
[code] 
    a = mod('/projects/utils/utilsA').add(5,6)
    
[/code]

Notice however, that a single import statement will be faster than the case of multiple identical mod statements: 
[code] 
    import myUtils
    a = myUtils.add(5,6)
    b = myUtils.add(5,6)
    c = myUtils.add(5,6)
    
[/code]

will execute faster than: 
[code] 
    a = mod.myUtils.add(5,6)
    b = mod.myUtils.add(5,6)
    c = mod.myUtils.add(5,6)
    
[/code]

However the above could be rewritten more efficiently like this, which would then execute at the same speed as the import statement: 
[code] 
    m = mod.myUtils
    a = m.add(5,6)
    b = m.add(5,6)
    c = m.add(5,6)
    
[/code]

## Search Path

The current component is searched first. 

If the [DAT](<./DAT.md> "DAT") is not found, the local/modules [component](<./Component.md> "Component") of the current [component](<./Component.md> "Component") is then searched. 

Next the local/modules [component](<./Component.md> "Component") of each parent is successively searched. 

If the [DAT](<./DAT.md> "DAT") is still not found, None is returned. 

  
TouchDesigner Build: Latest\n2021.100002018.28070before 2018.28070
