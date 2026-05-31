# Palette:virtualFile Ext

These Extensions reference a specific [Palette:virtualFile](<./Palette-virtualFile.md> "Palette:virtualFile").   
  
# VirtualFileExt

The VirtualFileExt extension provides extended functionality for working with the virtual files embedded in the component. Many of the functions mirror the vfs functions that exist on all COMPs. 

## Members

No operator specific members. 

## Methods`AddFile(filePath=None, overrideName=None, removeAllFirst=None, returnVirtualPath=False)`→`VFSFile or virtual path`: 

> Add an embedded file from disk to the component with an option to override the name. 
> 
>   * filePath - (Keyword, Optional) The path of the file to add. Default = par.Filesource
>   * overrideName - (Keyword, Optional) When specified, will override the name of the file in VFS.
>   * removeAllFirst - (Keyword, Optional) If True, remove all the virtual files first, default = par.Removeallbeforeadds
>   * returnVirtualPath - (Keyword, Optional) If True, return the virtual path instead of VFSFile
>`AddFromImage(top=None, name=None, filetype=None, removeAllFirst=None, returnVirtualPath=False)`→`VFSFile or virtual path`: 

> Add an image file created from the provided TOP. Returns an vfs info dictionary OR vfs paths using mode defined by par.Uselabel 
> 
>   * top - (Keyword, Optional) The TOP image to use. Default = par.Imagesourcetop
>   * name: the name to be stored with the image. Default = par.Virtualfileimagename + par.Virtualfileimagefiletype
>   * filetype - (Keyword, Optional) The file filetype to save virtual file in. For available formats, see [https://docs.derivative.ca/TOP_Class](<./TOP_Class.md>) saveByteArray function. Default = par.Virtualfileimagefiletype
>   * removeAllFirst - (Keyword, Optional) If True, remove all the virtual files first, default = par.Removeallbeforeadds
>   * returnVirtualPath - (Keyword, Optional) If True, return the virtual path instead of VFSFile
>`AddFromTable(table=None, removeAllFirst=None, returnVFSPath=False)`→`list of VFSFiles or list of Virtual Paths`: 

> Add all files from 'path' column in input table. If there is an 'overrideName' column, use this for virtual names. Returns a list of VFSFiles OR virtual paths 
> 
>   * table - (Keyword, Optional) table of filepaths, default = wired input or par.Pathstable
>   * removeAllFirst - (Keyword, Optional) if True, remove all the virtual files first, default = par.Removeallbeforeadds
>   * returnVirtualPath - (Keyword, Optional) if True, return list of vfs paths instead of VFSFiles
>`FileList(pattern='*')`→`list of VFSFiles`: 

> Finds all files in VFS with names matching the pattern. Returns a list of VFSFile objects. 
> 
>   * pattern - (Keyword, Optional) The pattern to match against.
>`RemoveFiles(pattern='*')`: 

> Destroys any virtual file from the component that matches with the supplied pattern. 
> 
>   * pattern - (Keyword, Optional) The pattern to match against.
>   * useLabel - (Keyword, Optional) When true, will match against the file label instead of the full path.
>`RemoveSingle(index=None)`: 

> Destroy a virtual file by index 
> 
>   * index - (Keyword, Optional) Index of file to remove. Default = par.Virtualfileindex
>`Rename(oldName, newName)`: 

> Change the name of a virtual file 
> 
>   * oldName - name of file to rename
>   * newPath - new name for file
>`VFSFileFromIndex(index)`→`VFSFile`: 

> Get a VFSFile by index 
> 
>   * index - (Keyword) index of the file
> 


TouchDesigner Build: Latest\n2021.10000before 2021.10000
