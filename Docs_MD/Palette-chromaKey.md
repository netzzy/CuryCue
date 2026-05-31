# Palette:chromaKey

This helps you build an alpha channel from video with a blue-screen or green-screen (or other) background color by interactively selecting background colors from an image and refining the key. It also smooths the edges and eliminates "color spill".   
  
NOTE: Get the latest chromeKey component from the palette. 

It is a pure TouchDesigner compositing network underneath that uses methods employing the ChromaKey, Blur and Lookup TOPs together with DATs and small python scripts. 

See the forum posts: [https://www.derivative.ca/Forum/viewtopic.php?f=22&t=4907](<https://www.derivative.ca/Forum/viewtopic.php?f=22&t=4907>)

Connect a video stream (can be a movie) to Input 1 of the chromakey component, such as the video that's included with the chromaKey.tox file, and select Input 1 in the UI. 

Or you can select the source to be Movie File and drag-drop a movie in the movie player, then scrub the movie to various frames. 

Then you can hook a background video stream or still image to input 2 to see your result composited. 

Next you want to select the key color. In the large middle image of the UI, select Input 1 and then left-click the mouse over a part of the key color, and drag the mouse around to gather more pixels that are the key color. 

Then you can middle-click or Ctrl-click or Alt-click to add to the key color selection. The key color selection is a min-to-max of hue, a min-to-max of saturation and a min-to-max of luminance. 

If you mess up, press Undo or start again by left-clicking on the image. And there's Undo to go back up to 10 steps ago. 

It may be tricky to select key color when the input video is rapidly changing. Instead you can press Sample Image a number of times, then click on any of the captured image samples. You can then add to the key color selection. You can sample up to 8 images and use the sample slider to go between them. 

Above the middle large image you can select what to put in the background of the preview: Black, Red, Input 2 or a standard background still. 

You can also adjust the key color selection by moving the handles on the hue, saturation or level bars. 

Bottom small image shows the spill mask on red. Spill refers to the background color spilling on to the subjects. A green background sometimes makes the edges of the subject greenish, so the spill removal makes these areas grey instead of green. Spill is adjusted with the stack of 4 sliders beside it. 

There's also the alpha-smoothing slider to round-out and slightly soften the edges. 

You can select 4 ways to output on the right - raw RGBA, composited over red, input2, etc. 

A big thanks to Hal Lovemelt of Playatta (<http://www.playatta.com>) for the tips and the use of the sample video.
