# SequenceBlock Class

The SequenceBlock class can be used to access the parGroups of a specific block (set of parGroups) in a sequence. 
[code] 
    block = op('/add1').seq.point[3] # get the fourth block from the sequence named "iop"
    print([parGroup for parGroup in block]) # print all the parGroups in the block
    
[/code]

**Note:** use the parameter name _without_ the sequence prefix. 

## Members`index`→`int`**(Read Only)** : 

> The numeric index of the block.`owner`→`OP`**(Read Only)** : 

> The OP to which this object belongs.`par`→`ParCollection`**(Read Only)** : 

> An intermediate parameter collection object, from which a specific sequence parameter can be found. 
> 
> Names do not include sequence info prefix. 
[code] 
>     n.seq.Info.blocks[2].par.Tx # raises exception if not found
>     
[/code]
[code] 
>     n.seq.Info.blocks[2].parGroup['Tx'] #returns None if not found
>     
[/code]`parGroup`→`ParGroupCollection`**(Read Only)** : 

> An intermediate parameter collection object, from which a specific sequence parameter group can be found. 
> 
> Names do not include sequence info prefix. 
[code] 
>     n.seq.Info.blocks[2].par.T # raises exception if not found
>     
[/code]
[code] 
>     n.seq.Info.blocks[2].parGroup['T'] #returns None if not found
>     
[/code]`name`→`str`: 

> Get or set the sequence block name parameter value. This is implemented as a specifically named parameter in each block. The name is also used to identify a block by string via Sequence[<block name>].`namePar`→`Par | None`**(Read Only)** : 

> The parameter defining the name for this block, or None if there isn't one.`sequence`→`Sequence`**(Read Only)** : 

> The sequence object this block belongs to.

## Methods`destroy()`→`None`: 

> Destroy the block of parameters.

TouchDesigner Build: Latest\nwikieditorwikieditorwikieditorwikieditorwikieditor2025.300002023.11280
