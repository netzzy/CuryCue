# Frame Rate

The frame rate is the Frames-per-Second (FPS) that TouchDesigner's [Timeline](<./Timeline.md> "Timeline") runs at. 

The global frame rate of a project is set with the`project.cookRate`Member of the [Project Class](<./Project_Class.md> "Project Class"). 

All non-audio [CHOPs](<./CHOP.md> "CHOP") have their sample rate set by default to this rate. 

Every component can have its own frame rate and start-end range. See the [Time COMP](<./Time_COMP.md> "Time COMP"). 

Frame rate is stored in the Timeline's [Time COMP](<./Time_COMP.md> "Time COMP") in the parameter called **Rate**. It can be set through the Timeline's UI, directly via the component's Rate parameter or via the`rate`Member of the [timeCOMP Class](<./TimeCOMP_Class.md> "TimeCOMP Class"). 

Note that a movie file read by the [Movie File In TOP](<./Movie_File_In_TOP.md> "Movie File In TOP") may have its own "frame rate" or "frames per second", but in TouchDesigner we call it the movie's "images per second" or "sample rate" to avoid confusion. 

See [Optimize](<./Optimize.md> "Optimize").
