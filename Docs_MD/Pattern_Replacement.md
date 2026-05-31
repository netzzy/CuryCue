# Pattern Replacement

Pattern Replacement takes place in a 2nd parameter after certain [Pattern Matching](<./Pattern_Matching.md> "Pattern Matching") parameters, for example in the [Rename CHOP](<./Rename_CHOP.md> "Rename CHOP"). It builds up the new names to replace the matched names using both the features of [Pattern Expansion](<./Pattern_Expansion.md> "Pattern Expansion"), as well as extra syntax specific to Pattern Replacement. The extra syntax allows for pulling out wildcards matched during the Pattern Matching.   
  
The synxtax is either a`*`or a`?`, followed by (_wildcardIndex_). Where _wildcardIndex_ is an integer which is the index of the wildcard in the Pattern Matching parameter. For example if there are three`*`wildcards, you would reference them using`*(0) *(1)`and`*(2)`. Similarly if there are 2`?`wildcard, they would be referenced using`?(0)`and`?(1)`. 

For example if a CHOP has 3 channels named 
[code] 
     left_side_monitor
     right_side_projector
     top_side_led
    
[/code]

And the 'Rename From' has 
[code] 
     *_side_* 
    
[/code]

as it's entry. You can pull out what was matched by the first * and the second * by using *(0) and *(1). 

A pattern replacement of 
[code] 
     *(1)_floor_*(0)
     
    
[/code]

Will result in the channel names 
[code] 
     monitor_floor_left
     projector_floor_right
     led_floor_top
    
[/code]

Pattern Replacement occurs in: 

[Rename CHOP](<./Rename_CHOP.md> "Rename CHOP"), [Select CHOP](<./Select_CHOP.md> "Select CHOP"), [File In CHOP](<./File_In_CHOP.md> "File In CHOP"), [Parameter CHOP](<./Parameter_CHOP.md> "Parameter CHOP")

See also [Script CHOP](<./Script_CHOP.md> "Script CHOP") where you can re-create channel names.
