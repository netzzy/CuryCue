# Actors Class

The Actors Class describes the set of all [Actor COMPs](<./Actor_COMP.md> "Actor COMP") used by the [Bullet Solver COMP](<./Bullet_Solver_COMP.md> "Bullet Solver COMP") and [Nvidia Flex Solver COMP](<./Nvidia_Flex_Solver_COMP.md> "Nvidia Flex Solver COMP"). It can be accessed with a Bullet Solver COMP. It can be accessed much like a Python list. 
[code] 
    actors = op('bsolver1').actors	# get the Actors object
    print(len(actors))				# number of Actors 
    print(actors[0])				# first Actor component in the list
    for a in actors:
    	print(a)					# print all Actors
    
[/code]  
  
## Members

No operator specific members. 

## Methods

No operator specific methods. 

  
TouchDesigner Build: Latest\n2022.241402021.100002019.146502018.28070
