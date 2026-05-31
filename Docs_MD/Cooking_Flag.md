# Cooking Flag

The Cooking flag is on components only. When the Cooking flag is on, it disables the cooking of the [component](<./Component.md> "Component")'s internal network. It is also known as the Cook flag, or Cooking Off flag. 

When not cooking, the internal nodes are not changed, their output data remains the same, they use the same CPU and GPU memory for their data. The only difference is none of the nodes will cook when cooking is off, consuming 0 msec time. When you reload a`.toe`or`.tox`file containing a COMP with Cooking Off flag set, the outputs of the nodes inside are empty and undefined. 

Example: 
[code] 
    op('/project1').allowCooking = True
    
[/code]

If a component has cooking off, from an external script, setting parameters, table values, rewiring on nodes inside the component generally still work but is not recommended. 

See also [Flag](<./Flag.md> "Flag").
