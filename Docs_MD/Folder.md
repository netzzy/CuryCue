# Folder

"Folder" in TouchDesigner always refers to a Windows or macOS operating system directory/folder system that contain files and other folders. 

In contrast, a TouchDesigner "[Path](<./Network_Path.md> "Network Path")" is the hierarchy of Components internal to TouchDesigner. A Path is a location of a node, which may be a component containing other nodes. 

Folders and filesystem paths are found in the operators that read files, such as the [Folder DAT](<./Folder_DAT.md> "Folder DAT"), [Movie File In TOP](<./Movie_File_In_TOP.md> "Movie File In TOP"), [File In CHOP](<./File_In_CHOP.md> "File In CHOP"), [File In DAT](<./File_In_DAT.md> "File In DAT"), [Audio File In CHOP](<./Audio_File_In_CHOP.md> "Audio File In CHOP"). 

Filesystem files on the internet can be referred in TouchDesigner parameters by their URL:`<http://www.internetplace.com/Movies/movie1.mp4>`, which downloads the file and reads from the temporary local file.
