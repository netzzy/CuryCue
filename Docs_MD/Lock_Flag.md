# Lock Flag

If a node is locked, it will not [cook](<./Cook.md> "Cook") and its data will not update when inputs or parameters change. The node's data is saved in the locked operator. 

See also [Flag](<./Flag.md> "Flag"). 

## Locking TOPs

A locked TOP saves the image inside the`.toe`file as uncompressed image data. The`.toe`file size will increase by the same amount as the locked image data size. A [.toe](<./.md> ".toe") file saved with locked TOP(s) can be opened by anyone and the image will remain in the TOP(s). For example, a locked [Movie File In TOP](<./Movie_File_In_TOP.md> "Movie File In TOP") will keep the TOP image stored in the`.toe`file so it can be opened on any computer, even if the file the TOP references does not exist. If the [Movie File In TOP](<./Movie_File_In_TOP.md> "Movie File In TOP") is then unlocked, the TOP will try to load the file referenced by its File parameter. 

## Locking SOPs

Locking a SOP prevents it from cooking so that manual modelling changes you make to the SOP (which can only be done fi you lock the SOP) are retained instead of updating parametrically.
