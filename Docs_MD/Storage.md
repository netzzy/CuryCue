# Storage

Each operator has an attached Python "**storage** " dictionary. Values stored in this dictionary are persistent, and saved with the operator. The storage dictionary contents may be manipulated directly with methods such as`OP.fetch()`or`OP.store()`. See [Storage Class](<./OP_Class.htm#Storage> "OP Class"). You can examine storage with an [Examine DAT](<./Examine_DAT.md> "Examine DAT").   
  
The storage dictionary is accessible directly via [`n.storage`](<./OP_Class.htm#Storage> "OP Class"). There are also a number of utility functions associated with storage, which can be found here: [OP Storage](<./OP_Class.htm#Storage> "OP Class"). 

#### Automatic Cooking

When an immutable element of storage changes, expressions that depend on it will automatically cook. For information about cooking of mutable elements (lists, dicts, sets), see [deeply dependable collections.](<./TDStoreTools.htm#Deeply_Dependable_Collections> "TDStoreTools")

#### Preserving in Files

Storage is saved with`.toe`and`.tox`files and is loaded on startup. If you want the values to be in an initial state on startup, regardless of what they were when the file was saved, you can use the`storeStartupValue()`method to first create the storage entry, instead of`store()`Also see: [StorageManager Class](<./StorageManager_Class.md> "StorageManager Class"), [Storage in OP_Class](<./OP_Class.htm#Storage> "OP Class").
