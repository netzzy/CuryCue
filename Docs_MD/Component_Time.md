# Component Time

A [Component](<./Component.md> "Component") can have a [Time COMP](<./Time_COMP.md> "Time COMP") in its`local`network (ie. _comppath_ /local/time) to create a local **Component Time**. The parameters of that Time COMP define the time-based attributes and Timeline settings for this component, such as rate, start, end, and range. This is useful for driving various parts of the system independently of each other or for using different rate, range, or looping settings. 

Component Time is inherited by all siblings of the component. At any network location, the [Timepath](<./Timepath.md> "Timepath") is the path to the first Component Time found by traversing up the hierarchy towards the root. Component Time with a Timepath = / is referred to as [Root Time](<./Root_Time.md> "Root Time"). The Tscript`timepath()`expression can be used to find the Timepath of any node or network. 

To create a Component Time in any component, right-click on the COMP and select **Add Component Time...** from the popup menu. A Time COMP will be added to that component in the location`local/time`. 

When in a network editor viewing a network with Component Time, a [mini-timeline](<./Component_Timeline.md> "Component Timeline") will be displayed at the bottom of the editor pane. 

Analogous to [Component Variables](<./Component_Variables.md> "Component Variables")
