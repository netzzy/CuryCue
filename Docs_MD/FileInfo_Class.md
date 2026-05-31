# FileInfo Class

The FileInfo object stores a file path and has a few utility properties to provide additional info. It is derived from str, so will work as a Python string, but can be differentiated from a regular string by using`isinstance(tdu.FileInfo)`. 

Utility properties include: 
* path: filepath string
  * ext: string after and including "."
  * baseName: the basename of the file
  * fileType: the TD filetype (from tdu.fileTypes)
  * absPath: the absolute path to filepath
  * dir: the containing directory of filepath
  * exists: exists in file-system
  * isDir: is a directory in the file-system
  * isFile: is a file in the file-system

## Members

No operator specific members. 

## Methods

No operator specific methods. 

  
TouchDesigner Build:  Latest\n2022.24140 2022.24140
