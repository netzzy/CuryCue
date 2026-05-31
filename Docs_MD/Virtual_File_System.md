# Virtual File System

## Overview  
  
TouchDesigner's Virtual File system (VFS) allows image, movie, audio, fonts, other media and any files to be embedded in a`[.tox](<./.md> ".tox")`or`[.toe](<./.md> ".toe")`file. You can open and read them as if they are files in the filesystem. This makes`.tox`and`.toe`files more portable if they depend on images or sounds or font files. It will of course make your`.tox`and`.toe`files larger by whatever the hard drive file size is, but one virtual file can be referred to by multiple OPs at the same time. 

The palette component [virtualFile](<./Palette-virtualFile.md> "Palette:virtualFile") in the Tools section lets you store virtual files without scripting. 

### Accessing Files

Internal files can be addressed directly with the`vfs:`prefix. Example:`vfs:/project1:test.jpg`. This VFS address will work in any parameter that is used to point at external files. All Operators that open files, like the [Movie File In TOP](<./Movie_File_In_TOP.md> "Movie File In TOP") and [Audio File In CHOP](<./Audio_File_In_CHOP.md> "Audio File In CHOP") allow the VFS syntax in their file parameters. 

### Details

Unlike locking a TOP where the image saved in the`.tox`/`.toe`is compressed with LZW, a Movie File In TOP that refers to a`.jpeg`file in VFS, it remains fully JPEG compressed. VFS can hold entire movie files and audio files including H.264 and`.mp3`files. It can also hold`.ttf`font files and in some circumstances,`.dll`files for the [CPlusPlus TOP](<./CPlusPlus_TOP.md> "CPlusPlus TOP"), [CPlusPlus SOP](<./CPlusPlus_SOP.md> "CPlusPlus SOP") and [CPlusPlus CHOP](<./CPlusPlus_CHOP.md> "CPlusPlus CHOP"). 

Together with the [Privacy](<./Privacy.md> "Privacy") option (can be set using TouchDesigner Pro only), VFS allows for additional privacy of media built into your TouchDesigner`.tox`/`.toe`files. 

## 

Usage

Two python classes give you full access to VFS functionality. 
* [VFS Class](<./VFS_Class.md> "VFS Class") \- describes a COMP's virtual file system.
  * [VFSFile Class](<./VFSFile_Class.md> "VFSFile Class") \- describes a virtual file contained within a virtual file system.

### Examples

See the above class wikis for full details. 

Add a file from disk  |`op('/base1').vfs.addFile('Banana.tif')`---|---  
Add an image from TOP |`op('/base1').vfs.addByteArray(op('someTop').saveByteArray('.jpg'), 'imageName.jpg')`Delete an image  |`op('/base1').vfs['Banana.tif'].destroy()`Save virtual file to disk  |`op('/base1').vfs['Banana.tif'].export('diskFolderName')`Access virtual file in OP's file parameter (constant mode)  |`vfs:/base1:Banana.tif`## 

Palette Example

Use the [virtualFile](<./Palette-virtualFile.md> "Palette:virtualFile") component in the [Palette](<./Palette.md> "Palette") (under`Tools`) as a user interface for VFS. This allows you to use VFS without the scripting that is otherwise required.
