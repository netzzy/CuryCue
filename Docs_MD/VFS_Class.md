# VFS Class

The VFS Class describes a COMP's [Virtual File System](<./Virtual_File_System.md> "Virtual File System").   
To access a virtual file in any operator's file parameter, use the virtual path format:`vfs:<path to comp>:<filename>`.   
[VFSFile_Class](<./VFSFile_Class.md> "VFSFile Class") does the file operators. 

## Members`owner`→`OP`**(Read Only)** : 

> Get the OP owner.

## Methods`[name]`→`VFSFile`: 

> [VFS Files](<./VFSFile_Class.md> "VFSFile Class") may be easily accessed using the [] syntax. 
> 
>   * name - Must be an exact VFS file name. Wildcards are not supported. If not found, an error will be raised.
> 

[code]
>     p = op('base1').vfs['Banana.tif']
>     
[/code]`addByteArray(byteArray, name)`→`VFSFile`: 

> Add an embedded file from a bytearray to the component. Returns a VFSFile instance of the added file. To delete the file, see`destroy()`on [VFSFile Class](<./VFSFile_Class.md> "VFSFile Class"). 
> 
>   * byteArray - A bytearray or bytes object representing the contents of the file.
>   * name - The name of the file on VFS.
>`addFile(filePath, overrideName=None)`→`VFSFile`: 

> Add an embedded file from disk to the component with an option to override the name. Returns a VFSFile instance of the added file. To delete the file, see`destroy()`on [VFSFile Class](<./VFSFile_Class.md> "VFSFile Class"). 
> 
>   * filePath - The path of the file on disk to add.
>   * overrideName (Keyword, Optional) - When specified, will override the name of the file in VFS.
>`export(folder, pattern='*', overwrite=False)`→`list`: 

> Exports any matching files to the folder on disk. If overwrite is True then any existing files on disks with the same name will be overwritten. Returns a list of paths on disk to the exported files. 
> 
>   * folder - The folder on disk to export the files to.
>   * pattern (Keyword, Optional) - The pattern to match names by.
>   * overwrite (Keyword, Optional) - When True, will overwrite any files that share the same name.
> 

[code]
>     # VFS contains one file with name 'A/B.tif'
>     COMP.vfs.export('C:/tmp') # returns ['C:/tmp/A/B.tif']
>     
[/code]`find(pattern='*')`→`list`: 

> Finds all files in VFS with names matching the pattern. Returns a list of VFSFile objects. 
> 
>   * pattern (Keyword, Optional) - The pattern to match names by.
> 

### Special Functions`len(VFS)`→`int`: 

> Returns the total number of virtual files. 
[code]
>     a = len(op('base1').vfs)
>     
[/code]`Iterator`→`str`: 

> Iterate over each virtual file name. 
[code]
>     for f in op('base1').vfs:
>     	debug(f) # print info of all virtual files on base1
>     
[/code]

  
TouchDesigner Build: Latest\n2021.10000before 2021.10000
