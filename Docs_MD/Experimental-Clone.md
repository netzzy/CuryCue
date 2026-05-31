# Experimental:Clone

Put all new (2025) cloning here:   
  
from Rob Status: OP.clone.status = CloneStatus. 'NONE', 'CLONE', 'MASTER' OP.clone.active True if this operator is actively cloning or mastering. (either directly or as a child of a clone or master) ParGroup.clone.sourceRevised: Removed (use ParGroup.clone.source.state) 

## Python Members for Cloning

### OP
[code] 
    OP.clone
     Contains the OP's clone related information (class OPClone):
    
[/code]

### OPClone
[code] 
    .owner (readOnly)
       The component referenced by this clone object.
    
[/code]
[code] 
    .active (readOnly)
       True if this operator is actively cloning or mastering."
    
[/code]
[code] 
    .status (readOnly)
       The current status of the OP (CloneStatus.NONE, CLONE, MASTER)."
    
[/code]
[code] 
    .master (readOnly)
       The master component this operator is directly cloned to. Defined by its 'Clone Master' parameter.
    
[/code]
[code] 
    .context (readOnly)
       The topmost component that is cloned to a master that contains this operator's counterpart source.
    
[/code]
[code] 
    .contexts (readOnly)
       The list of parent components that are cloned to a master.
    
[/code]
[code] 
    .contextMaster  (readOnly)
       The master component that contains this operator's counterpart source.
    
[/code]
[code] 
    .contextMasters (readOnly)
       The list of master components this operator's parents are cloned to.
    
[/code]
[code] 
    .clones (readOnly)
       A list of all components cloned to this component.
    
[/code]
[code] 
    .counterparts (readOnly)
       A list of all operators cloned to this operator.
    
[/code]
[code] 
    .counterpartSources (readOnly)
       The chain of operators that this operator is directly cloned to.
    
[/code]

### Non-Components

(OP.clone works for COMP or OP) 

### ParGroup
[code] 
    ParGroup.clone
     Contains the ParGroups's clone related information (class ParGroupClone):
    
[/code]

### ParGroupClone
[code] 
    .state (readOnly)
       Effective clone state of the ParGroup (CloneState.CLONE .REVISE or .IMMUNE) Based on .localState as well as any inherited status from the master.
    
[/code]
[code] 
    .localState
       Locally defined state. (One of CloneState.CLONE .REVISE or .IMMUNE). Can be directly set.
    
[/code]
[code] 
    .source (readOnly)
       The operator this parameter is cloned from. Returns None if not cloned to anything.
    
[/code]
[code] 
    .parGroup (readOnly)
       The ParGroup this clone info refers to.
    
[/code]

### Misc

Misc: 
[code] 
     UI.editClones
       Get or set ability to modify cloned operators through the editor interface.
    
[/code]
[code] 
     Clone Info DAT
        Table format of an operator's clone states.
    
[/code]
