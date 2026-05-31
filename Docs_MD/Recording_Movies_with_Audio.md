# Recording Movies with Audio

There are at least four ways to record [FFmpeg](<./FFmpeg.md> "FFmpeg") movies with TouchDesigner.   
  
## Realtime Recording

In realtime recording, you are creating the movie while you are performing, using the [Movie File Out TOP](<./Movie_File_Out_TOP.md> "Movie File Out TOP"). This creates a best-possible movie, which may have repeated frames if TouchDesigner and your computer cannot keep up with the desired frame rate of the recorded movies. This is the method used by [Mixxa](<./TouchMixer_\(Mixxa2015\).md> "TouchMixer \(Mixxa2015\)"). 

The Movie File Out TOP will record with audio, either from a live-generated [Time Slice](</index.php?title=Time_Slice&action=edit&redlink=1> "Time Slice \(page does not exist\)") of audio, or from a static CHOP containing the whole audio clip. 

When the Movie File Out TOP can't keep up with the desired frames per second, it replicates images in the movie file so the final movie is the correct number of frames. 

In realtime recording the timeline doesn't matter and you can record movies as long as you wish. To get smoother movies, you can lower the resolution of the TOPs including the Movie File Out TOP that creates the movie files. 

## Non-Realtime Recording

Use non-realtime recording if you are not performing and you are not using realtime input data, where you want the recording to be repeatable exactly. No frames are dropped, and you can record at any resolution with any degree of complexity. 

You record a sequence of frames using File -> Export Movie. This is locked to the timeline and is fixed to a user-defined frame range on the timeline. You can use timeline-locked variables like`me.time.frame`and`me.time.seconds`. To this end, we suggest movies in the [Movie File In TOP](<./Movie_File_In_TOP.md> "Movie File In TOP") be played with Play Mode set to Locked to Timeline, or Specify Index using`me.time.frame`. Otherwise Play Mode set to the Sequential will likely record something different each time you make a movie. 

You may want to reset [Speed CHOPs](<./Speed_CHOP.md> "Speed CHOP") and [Count CHOPs](<./Count_CHOP.md> "Count CHOP") each time you record a movie. 

## Black Art Recording

Black art recording gives top quality from a performance, but requires careful setup and is a two-pass process. 

Audio coming out the audio port from TouchDesigner are routed right back into the audio inputs to an [Audio Device In CHOP](<./Audio_Device_In_CHOP.md> "Audio Device In CHOP") feeding a [Record CHOP](<./Record_CHOP.md> "Record CHOP"). So while you are performing, audio can be generated in TouchDesigner, output, processed and mixed with other audio externally, then brought back into an Audio Device In CHOP and captured in TouchDesigner. 

Instead of making a movie while you are performing, you capture the chosen performed channels and data into a Record CHOP. Using [Select CHOPs](<./Select_CHOP.md> "Select CHOP") and [Switch CHOPs](<./Switch_CHOP.md> "Switch CHOP"), you route the data back through the networks and record a movie in non-realtime at hi-res at the exact frame rate, with the captured audio in the movie. 

Due to the audio paths being different than the video paths, you have to pay attention to delaying either to assure audio is in sync with video in your final movie. You can use [Trim CHOPs](<./Trim_CHOP.md> "Trim CHOP") on captured channels, or [Delay CHOPs](<./Delay_CHOP.md> "Delay CHOP") in realtime to acheve this, or do it in post. 

## External Camera Recording

This is the "classic" way. Record to a camera recorder from TouchDesigner, directly HDMI to a camera, or via a scan converter. Record the audio inside TouchDesigner into a [Record CHOP](<./Record_CHOP.md> "Record CHOP") that you can save to`.aif`or`.wav`via RMB -> Save CHOP Channels. Alternately, send audio out in realtime to the camera. 

## Touch Out / Touch In Recording

If you do not have enough CPU power on one computer, send the video stream out via a Touch Out TOP, through Gigabit Ethernet, into TouchDesigner on another computer, which reads the video stream via a Touch In TOP. Then do your Realtime Recording on that system. 

As time moves on with multi-cores on a single system, it is becoming possible to do more recording all on one computer. 

See also [Movie File Out TOP](<./Movie_File_Out_TOP.md> "Movie File Out TOP")
