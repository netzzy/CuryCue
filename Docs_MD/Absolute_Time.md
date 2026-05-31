# Absolute Time

**Absolute Time** starts counting from 0 when the TouchDesigner process starts, and (unlike the looping timeline) is always increasing. It will pause if the Power 0|1 button at the top of the UI is Off. 

Absolute Time in TouchDesigner is expressed in seconds and in frames, where frame 1 corresponds to seconds = 0. If the global frame rate is 60, then frame 61 corresponds to 1 second, and so on. The global frame rate is most often locked set to be the rate of the display monitors on the computer running TouchDesigner, but in fact can be anything. See`cookRate`in [Project_Class](<./Project_Class.md> "Project Class"). 

The python class is **absTime** and its members are`absTime.frame`and`absTime.seconds`. See [AbsTime_Class](<./AbsTime_Class.md> "AbsTime Class") and [absolute time](<http://en.wikipedia.org/wiki/Absolute_time_and_space>).
