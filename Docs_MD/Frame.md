# Frame

The term "Frame" is a measurement of time, an integer division of a second, used (1) in the [Timeline](<./Timeline.md> "Timeline"), (2) as a time-unit in CHOPs, (3) as a time unit in movie files that are read into TOPs and written out from TOPs.   
  
'Frame' is sometimes also used in image processing and TOPs to refer to the array of pixels in an image, but we refer to these as 'images' in TouchDesigner as much as possible to avoid confusion. 

## Frames on the Timeline

The frame bar on the [Timeline](<./Timeline.md> "Timeline") at the bottom of the TouchDesigner window shows the current frame number. TouchDesigner is set at a specific number of frames per second ([FPS](<./Frame_Rate.md> "Frame Rate")), which is displayed and set in the Timeline. The default frame rate is 60 frames per second, which a common refresh rate of LCD monitor and projectors. 

You can also query and set the frames per second in python by using`project.cookRate`in the [Textport](<./Textport.md> "Textport"). For example,`project.cookRate = 60`. 

The current frame is tied to the current time in TouchDesigner: The first frame of the timeline is frame 1, which is time 0 seconds, and at 60 frames per second, frame 61 is time 1 seconds. 

TouchDesigner will cook (generate its output) up to the FPS in one second. If you know you want to cook and render only 25 frames per second, set FPS to 25. (**NOTE** : It is suggested you do this at the start of your project though it is not necessary.) 

You can set your global timeline length to any number of frames on the Timeline UI. This may be useful if you are creating content of a known length. However the timeline length doesn't matter for most realtime projects. When TouchDesigner hits its last frame, it will then go back to frame 1 and play in a loop. Most things in TouchDesigner don't pay attention to the timeline looping as they have their own time counters, like in the Movie File In TOP which by default just plays forward until it reaches its own movie end, and all time filters which ignore the timeline. 

On the other hand, you can lock some things to the timeline using`me.time.frame`or`me.time.seconds`expression in a parameter set to use index to drive it. 

With frames per second set to 60, the frame step is 1/60 second. Because TouchDesigner will not always be able to render in realtime, when it is playing forward in realtime, it will skip frames to keep up, but CHOPs that are [Time Sliced](</index.php?title=Time_Slice&action=edit&redlink=1> "Time Slice \(page does not exist\)") will internally compute in-between frames as best it can. 

Although it may skip frames, you can be assured that after 4 seconds playing in realtime, it has stepped forward by 240 frames. 

## Frames in CHOPs

CHOPs have their own view of frames and time. Parameters involving time in CHOPs (length-trim time) can be expressed in any of three time units: seconds, samples (indexes), or frames. A CHOP may have its own sample rate set to 120 samples per second, but a frame step to a CHOP is exactly the same as a frame step on the timeline. So with the timeline set to 60 frames per second, it will be the same as 120/60 = 2 samples in the CHOP. So 60 frames in a CHOP is still 1 second, no matter what the sample rate of the CHOP is. 

## Frames in TOPs and Movie Files

Although the timeline may be set to 60 frames per second, incoming movies like QuickTime MP4 movie files will have their own idea of "frame", and will typically have a built-in setting of 30 images per second. When the [Movie File In TOP](<./Movie_File_In_TOP.md> "Movie File In TOP") reads the movie, the user can refer to the images in terms of 'index', 'frames', 'seconds' or 'fraction'. As in CHOPs, 'frames' is still the timeline frames and frame 61 is one second after frame 1 in the movie. To refer to the movie's built-in setting of say, 30, you need to use 'index' to specify those images, where index of 0 is the first image, and index 30 is the 31st image (one second later).
