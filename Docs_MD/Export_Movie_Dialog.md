# Export Movie Dialog

## 

Description

This dialog allows you to export movies in various container formats and codecs from any viewer in TouchDesigner. 

This export to movie does not run in real time. The rendering takes the necessary time required to display and write each frame completely. This allows movies to be produced at the highest resolutions the graphics hardware can support, while avoiding choppy playback and low frame rates that these resolutions can experience in realtime. 

[![ExportMovieDialog.png](./images/6/6f/ExportMovieDialog.png)](</File:ExportMovieDialog.png>)

After setting up the parameters the way you like, simply press the **Start** button to begin exporting your movie. Press the **Stop** button to end recording and create the .mov file. The Stop button is optional, as the recording will stop automatically when the specified duration is reached. After creating a movie, you can preview the most recent movie file by clicking the **View** button. 

## 

Parameters

### 

Input

TOP Video \- Path to the OP to be recorded. When a TOP is specified, the image data in the TOP is used for the movie. When an operator that is not a TOP is specified, the OP's node viewer is used for the movie. 

CHOP Audio \- Path to the CHOP audio to be recorded. The CHOP must be [Time Sliced](</index.php?title=Time_Slice&action=edit&redlink=1> "Time Slice \(page does not exist\)"). 

### 

Settings

Resolution \- Specifiy the resolution of the exported movie. The 2 parameters are X resolution and Y resolution. 

Movie FPS \- The frames per second of the exported movie. 

Codec \- Use this menu to select the video codec of the movie you are encoding. 

Quality \- Controls the quality of the video compression when encoding the movie. Lossless is the best quality setting, but will only provide true lossless-encoding in codecs that support lossless compression, such as Animation (rle) codec for example. 

Channels \- Select between outputing color channels or alpha only. Some codecs such as Animation (rle) and Tiff (tiff) offer RGBA which encodes the RGB and alpha channels in the movie file. 

Movie Timecode \- Will overlay the movie's SMPTE timecode over the exported movie. 

Timeline Timecode \- Will overlay the [timeline](<./Timeline.md> "Timeline")'s SMPTE timecode over the exported movie. 

Start Frame \- The frame on the timeline that the movie will start recording from. When pressing the "Start" button, the [Timeline](<./Timeline.md> "Timeline") will be set to the Start Frame and the movie will begin encoding. 

End Frame \- The frame on the timeline that the movie will stop recording at. If the timeline reaches this frame while encoding a movie, the process will automatically stop recording and finish the movie. 

Set Duration \- The duration of the movie. This can be displayed in frames, seconds, or minutes. When the Start/End Frames are changed, the Duration will be auto-updated. If the Duration is changed, then the End Frame will be auto-updated to reflect the new Duration. 

### 

Output

Filename \- The filename of the exported movie. Click the folder button on the right to open a File Save dialog. If you want to auto-increment your filenames, add "$N" to the filename and the auto-increment number below will be inserted into the filename. 

Filename Inc \- This number is automatically incremented with each movie exported. If "$N" is added to the filename parameter above, then this number will be added to the filename when the movie is created. 

Start/Stop \- Starts and Stops the movie recording. When Start is pressed, the [Timeline](<./Timeline.md> "Timeline") will be set to the Start Frame and the recording will begin. The recording will end if the End Frame is reached or the Stop button is pressed. 

View \- View the last movie created using the default movie player.
