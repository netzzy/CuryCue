# Runs Class

The Runs class describes the set of all delayed [run objects](<./Run_Class.md> "Run Class"). It can be accessed with the runs object, found in the automatically imported [td module](<./Td_Module.md> "Td Module"). See [Run Command Examples](<./Run_Command_Examples.md> "Run Command Examples") for more info. 
[code] 
    print(len(runs))	# number of active run objects 
    print(runs[0])		# first run object
    for r in runs:
    	r.kill()		# kill all run objects
    
[/code]

## Members

No operator specific members. 

## Methods

No operator specific methods. 

  
TouchDesigner Build:  Latest\n2021.10000 2018.28070 before 2018.28070
