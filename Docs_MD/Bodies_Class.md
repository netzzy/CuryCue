# Bodies Class

The Bodies Class describes the set of all [Bodies](<./Body_Class.md> "Body Class") in an [Actor COMP](<./Actor_COMP.md> "Actor COMP") (Actor COMPs are used by the [Bullet Solver COMP](<./Bullet_Solver_COMP.md> "Bullet Solver COMP") and [Nvidia Flex Solver COMP](<./Nvidia_Flex_Solver_COMP.md> "Nvidia Flex Solver COMP")). The Bodies object is accessed via its Actor COMP and is used much like a Python list. 
[code] 
    bodies = op('bsolver1/actor1').bodies	# get the Bodies object
    print(len(bodies))						# number of Bodies 
    print(bodies[0])						# first Body in the list
    for b in bodies:
    	print(b)							# print all Bodies
    
[/code]  
  
## Members

No operator specific members. 

## Methods

No operator specific methods. 

  
TouchDesigner Build: Latest\n2022.241402021.100002019.146502018.28070
