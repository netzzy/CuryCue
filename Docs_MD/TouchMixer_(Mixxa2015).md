# TouchMixer (Mixxa2015)

**TouchMixer** (also known as Mixxa June 2015) is a flexible HD video mixing tool made fully in TouchDesigner. The center of Mixxa is a matrix of 9x9 cells, each cell outputting a video stream. Typically cells feed video into the cell below it, but you can rewire the matrix any way you want. And each cell can have **[any of 35+ Mixxa effects](</Mixxa2015_Effects> "Mixxa2015 Effects")** in it - right-click on the cell title and choose another effect. Movies in the movie Bins can be assigned to cells, and Mixxa allows for up to 3 independent HD video outs. 

**Note** : The latest version of Mixxa is [Mixxa](</Mixxa> "Mixxa"). 

**Note** : Mixxa is not supported but is made freely available for use with TouchDesigner. TouchMixer originated as video mixer with TouchDesigner 017. 

**[Get TouchMixer (Mixxa June 2015) here](<http://www.derivative.ca/088/Tools/MixxaDec2014.12.zip>)** and use [TouchDesigner 088](<http://www.derivative.ca/088/Downloads/>). 

June 2015 fixes: Gestures now are simpler - just press-hold Shift and move sliders up-down and release. To turn gesture off, click slider without pressing Shift. Audio mixing tolerate movies with different audio sampling rates. 

For a crash course intro to Mixxa, check out the [Mixxa Tutorial](</Mixxa_Tutorial> "Mixxa Tutorial") made by Ivan DelSol (many thanks to Ivan!). 

## Feature Summary
* Mixxa supports virtually unlimited bins of movies and stills. It mixes throughout at a user-defined resolution set in Setup. It uses [FFmpeg](<./FFmpeg.md> "FFmpeg") to support a wide range of movie/image formats.
  * A Matrix is a 9x9 grid of cells, where each cell can be one of 30+ image Effects that [play a movie, generate images, process images, or mix images](</Mixxa2015_Effects> "Mixxa2015 Effects").
  * The input to each cell in a Matrix is typically the cell above it, though inputs can can come from any other cell in the matrix. Click Wire to see the wiring.
  * There are several ways to arrange and view the cells you are currently operating.
  * You assign movies in bins to matrix cells (left-click on movie and select destination from popup). Movies can be non-destructively in-out trimmed, cropped and level-adjusted.
  * You can drive controls with LFOs, drawn curves, MIDI, mouse gestures and audio spectrum response.
  * Mixxa can output video to 3 monitors (or projectors etc). Any cell can be sent to any monitor output.
  * A Preset is the full configuration of a 9x9 matrix. You can recall a full preset, or gradually and partially recall any preset into the matrix, transitioning from one preset to another, cell by cell. A graphic shows the difference between one preset and another.
  * You can mix audio for up to 7 movies.
  * You can create movies while you perform.
  * Event Capture saves your control movements to event files, and plays them back in realtime, or non-realtime for recording.
  * Event Capture also records wiring changes, movie settings, changes to which effect is assigned in a cell.
  * You can create your own effects and use them in same way as the built-in effects.
  * Design approach to Mixxa: minimum clicks to any control/display, minimal overlapping windows, minimum text or extraneous color (use the popup help on each gadget for gadget help), simple matrix grid structure, support for improvisation like mixing between presets and gesture capture, fast selection to 3 output displays.
  * Mixxa is designed for use with or without a touch screen such as the [3M product](<http://solutions.3m.com/wps/portal/3M/en_US/TouchSystems/TouchScreen/Solutions/MultiTouch/M2467PW/>).


You can modify Mixxa to add your own effects, and various parts can be lifted out into other TouchDesigner applications. TouchDesigner users can learn from the techniques in Mixxa to craft their own work. Feel free to mod and re-post it. 

## Setting up Mixxa

You should have **Windows 7, 8 or 10** with an **NVIDIA or Radeon graphics card with 2-4 Gigabyte of graphics memory** or better. In general Mixxa likes graphics cards with 384 or more NVIDIA GPU cores. 

**[Get the latest Mixxa here](<http://www.derivative.ca/088/Tools/MixxaDec2014.4.zip>)**. 

Expand the`MixxaDec2014.4.zip`folder on your desktop and double-click its`MixxaDec2014.*.toe`. After using it, click the **Save** button to keep your revisions for the next time you restart`MixxaDec2014.toe`. 

Note for later: To start with a relatively clean slate, in Presets, restore Preset 1 in Bank 1. 

## New in MixxaDec2014
* **Matrix X, Y and Z** \- As if one 9x9 matrix isn't enough, we have now three 9x9 matrixes, mysteriously called Matrix X, Y and Z. This sounds indulgent or obsessive, but observation of numerous drunk and non-drunk VJs has shown that they can handle, and even appreciate three 9x9 matrixes. The typical use of Matrix X, Y and Z is easily understood by anyone that has been near an A-B mix DJ mixer. In Mixxa you could mix your pre-made content with presets in the X matrix. Matrix Y is used for improvising or diddling about. Matrix Z is the crucial one here. Using the Cell Fetch effect type, it fetches outputs from X and Y and mixes/prepares them for output to your projectors, monitors, whatever. So in Matrix Z you will Crop, Corner Pin and level-adjust for the outputs that you are performing in. You don't have to cram your output processing in X. You can keep only your content playback/mixing/effects in X, making Z venue-specific. Having the Matrix Y will let you try on-the-fly ideas out before or at and event, without messing up your planned stuff in X. Or you can use X and Y for whatever you want.
  * **Wire** (new in MixxaDec2014.4) - Wire now displays all 3 matrixes, you can use the mouse wheel to navigate it, and you can wire the inputs and outputs of your cells in Wire. Shortcuts: click buttons X, Y Z, shortcut "h" key for home. The lines in blue are the connections between cells in different matrixes, which can only be achieved using a Cell Fetch effect type as you see in Z11.
  * **Stream Out and Movie Out cells** \- If you want to stream any cell to another TouchDesigner system, or record a cell to a movie file, you can choose that cell in Setup, Often X99 is used for that.
  * **Audio Mix in Recorded Files** \- If you want to record your session to H.264 or something, you can record any cell with audio. The audio sliders beside the MixxaOut button are the levels for incoming audio from and input device (choose the device in the Audio panel), plus a slider for the audio master mix in the Audio panel.
  * **Audio Compressor / Limiter** \- keeps audio mixes within -1 to +1 limits to avoid distortion.
  * **Active Monitors while editing in Designer Mode** \- In Monitors, you can choose to keep the 3 monitors sending their images to the 1-3 outputs when you are editing networks in Designer Mode.
  * **Audio Beat Follow** \- better tracking of audio at different frequency ranges.
  * **Presets** can currently only be restored in Matrix X.
  * More optimized.

## Sources, Matrix, Outputs

The Mixxa control interface is divided in three. 

Left: Sources - Bins (your movie and still image sources), Router control signal routing, History of recent movies used, and Presets. 

Middle: Matrix - your 9x9 Matrix of Cells containing Effects, where you will play video streams, apply effects and mix. 

Right: Outputs - your Monitor outputs, Audio mixing, and Combine where you can choose what you see behind the panels. 

## Bins of Movies and Stills

Select **Bins** on the bottom row of buttons. The buttons at the top let you select different bins of media. Each bin contains still images or movies. 

Select the first bin, **Mordka Elements** If you click on one of its movie icons it becomes “selected” and you can see the media displayed larger in the “movie prepare” panel below it. It is not yet assigned to any Cell, so you can inspect and prepare it first. 

You will learn how to use your own media in [Using Your Own Movies and Stills in Bins](<#Using_Your_Own_Movies_and_Stills_in_Bins>). 

## Movie Preparation

After you click an icon in the Bin to select the current movie, adjust it in the “movie prepare” panel. Click on the image to scrub the video. Hold down to freeze a frame, move left-right to scrub and let go to continue playing the movie. 

**>** and **||** pauses and plays the movie. 

[![Mixxa2012.33.1.jpg](./images/2/2f/Mixxa2012.33.1.jpg)](</File:Mixxa2012.33.1.jpg>) **5.** [![Mixxa2012.9.7.jpg](./images/0/0c/Mixxa2012.9.7.jpg)](</File:Mixxa2012.9.7.jpg>)

On the left are the speed buttons. Selecting **spd** allows you to adjust the speed using the speed slider to its right. With **-+** on, it lets you play the movie backward. To play the movie at high speeds, move the speed slider off-scale with **-+** on. 

**1 2 4 8 16** will repeat the movie in that number of beats. The beats-per-minute is set by bringing up the Beat panel (5) via the Beat button at bottom. 

(Expert: Press **Beat** to get the **Beat** panel. Press **Listen** , then press **Tap** every 4 beats until the BPM gets consistent. Then press Listen again to end the tapping session. You can also assign MIDI buttons for Listen and Tap in the MIDI Mapper.) 

**Intrp** will interpolate between frames when playing slowly. The slider above lets you **crossfade** the end of the movie clip with its beginning. 

### Window for Trimming

You can set the **in-point** and **out-point** of the movie by pressing the **+** button, then the **Trim** page, where you can loop a shorter section of the movie: 

### Window for more Image Settings

The **+** button, then the **Adjust** page brings up the movie in a window with more movie settings (the movie file itself is not altered): 
* BLK - set the black level (use if it's overall too grey)
  * BRT - adjust brightness of the movie (linear adjustment)
  * GAM - alter the gamma (black stays black, white stays white, mids are adjusted)
  * Crop your movie if it has garbage along its edges.
  * Make Mixxa skip images in the file to get a stepping effect.
  * AUD - adjust the amplification of the audio coming from the movies, and compare it with a .5 amplitude sine wave tone.


( Not available presently: **Cyc** plays the movie in cycles, **Mir** plays the movie forward then backward, **Hld** will hold the last frame when it reaches the end of the movie. **Blk** will go to black after the movie reaches the end. If you click on the movie image and scrub, it will reset the movie so you can play it again.) 

**Alternate** : Drag-drop movies or images from your Desktop or Windows Explore into a spare bin, then right-click on a movie and select **Make Icon** , or select **Make Icons** tomake icons for all movies in the bin. 

## Assign a Movie to a Cell

You can assign a movie or image in the Bins to any matrix cell that contains a **Movie Play** or **Still Cut** effect. 

Assign a movie to a Movie Play cell by pressing down on any movie icon in Bins and dragging off to the right: You will see a visual guide to help you assign to a cell. **Note, you don’t drag it all the way to the cell - you just release on the movie icon on the guide**. We do this to minimize finger/mouse movement for drunk VJs. 

The visual guide will have one row for every Movie Play or Still Cut in your matrix, and they are lettered A, B, etc. Later in the Movie Play or Still Cut cell, if you press the corresponding A, B C... it will bring up on the left the bin/movie that was the original movie assigned to that cell (though they are independent from each other now). 

If you release just to the right of the assign dialog, the movie will be paused. If you release on the assign dialog, it will play forward. 

[![Mixxa2012.30.1.jpg](./images/3/32/Mixxa2012.30.1.jpg)](</File:Mixxa2012.30.1.jpg>) -> [![Mixxa2012.31.1.jpg](./images/5/5b/Mixxa2012.31.1.jpg)](</File:Mixxa2012.31.1.jpg>) [![Mixxa2012.31.2.jpg](./images/9/98/Mixxa2012.31.2.jpg)](</File:Mixxa2012.31.2.jpg>)

Movies in Bins are decoupled from movies in the matrix. So once you assign a movie into the matrix, you can adjust it independently. As a result, you can have the same movie playing differently in any cell. 

## The Matrix containing Cells of Effects

A Matrix is a 9x9 grid of Cells, where each cell contains an effect that can play a movie, generate images, process images, or mix images. 

The matrix is arranged as 9 columns (Channels) of 9 cells each. 

### Opening and Closing Cells

If you click on a cell name in Mag or Solo, it will bring up that cell's controls alone. If you click on the image part of a closed cell, it will add that cell to the ones that are open. 

You can alternately use the roller wheel over a cell: Roller wheel up (one notch) to open a cell's controls. 

Then roller wheel up a second notch to open the cell's output viewer (so you can see the cell's output larger). One more roller wheel up gives you the control panel again. 

Roller wheel down always closes a cell, but it leaves that cell as the “current” cell. All roller movements makes the cell current.. 

Two buttons at the bottom are shortcuts: **mv** will select only Movie Play and Still Cut cells. **Unselect** will close all cells. 

### Matrix Layouts - Mag, Solo, Sel, Wire

There are four types of layout of the Matrix cells: 
* **Mag** \- All cells are visible in a grid, and individual cells can be magnified.


[![Mixxa2012.38.1.jpg](./images/c/c8/Mixxa2012.38.1.jpg)](</File:Mixxa2012.38.1.jpg>) = [![Mixxa2012.39.1.jpg](./images/8/83/Mixxa2012.39.1.jpg)](</File:Mixxa2012.39.1.jpg>)
* **Solo** \- The matrix is compressed at the bottom. Only the selected cells are fit in the space at the top, as large as possible.
* **Sel** \- No matrix is visible. Only the selected cells are fit in the full space, as large as possible.
  * **Wire** \- You can see how the cells are wired together, and you can rewire the cells by clicking on their connecting knobs.

### Wiring Cells Together

The inputs to cells can come from any other cell in the matrix. Most effects in cells have one video input, some have several inputs. All cells have one video output. 

You can change wiring in the **Wire** panel. 

You can also change the wiring in **Mag** or **Solo**. First select the source (by using the roller wheel down or up). You then right-click on the destination cell name, and you get a menu where you then select **Wire to Input 1**, **2** , **3** depending on how many inputs there are. 

For example I would lay down a Blend effect in a cell, then wire its 2 inputs to any other cell in the network. 

### Replacing a Cell with a new Effect

Right-click on the name of the cell, such as **Drift** , and you get a cell menu. Select from the menu **Replace Cell** and select a new Cell type, such as **Fizzle**. 

[![Mixxa2012.11.1.jpg](./images/6/6c/Mixxa2012.11.1.jpg)](</File:Mixxa2012.11.1.jpg>) -> [![Mixxa2012.12.1.jpg](./images/0/01/Mixxa2012.12.1.jpg)](</File:Mixxa2012.12.1.jpg>)

(Hey the right-click -> **Replace Cell** sometimes gives you the wrong FX. If that happens, just do it again ... it will work the second time you try. Sorry about that.) 

You can clear the cell so it has no effect by selecting **Clear Cell**. 

You can clear all the cells to the bottom of the column with **Clear Channel**, and clear all the channels to the bottom of Channel 9. This may pause for a while while it is doing its work. 

You can also use Presets to replace a cell. See [#Presets](<#Presets>). 

### Exposing and Unexposing Columns (Channels)

A row of buttons at the bottom (9 sets of 3x3 boxes) will expose different sets of columns (channels): **1-9** , **1-7** , **1-4** , **1-4 and 7** , etc. For example, the second button will hide column 8 and 9: 

These buttons also are on keyboard hot keys 1-9 and 0. Warning: Pressing these while performing may affect which channels are displayed. 

## Three Important Effects: Movie Play, Still Cut and Blend

There are 30+ effects types, but we cover the **Movie Play** and **Still Cut** effects first because they are the way you bring media from bins into the matrix cells. 

You can have any number of Movie Play cells, that is, Mixxa does not restrict you on the number of movies playing. It is limited by disk speed and CPU movie decoding. 

Movies and stills in **Bins** are decoupled from movies in the matrix. So once you assign a movie from a bin into the matrix, you can adjust it independently. As a result, you can have the same movie playing differently in two or more cells. 

Press the half-circle icons **A B C D E** ... to see the bin/movie that the movie originally came from. 

In Movie Play and Still Cut, press **Back** to go back to the previous movie that was playing in that cell. Its settings were preserved. Press **Back** again to revert. This is very useful because it lets you try another movie in a cell and go back if you don't like it. 

Movies and stills don't pause when you assign them. It loads the movie in the background and cross-fades to the new movie when it's ready. 

### Movie Play effect

Movies in Movie Play - you can adjust in-out points, levels, crop, as well as speed etc. 

It has the same controls as [#Movie Preparation](<#Movie_Preparation>). See also [Mixxa2015 Effects#Movie Play](</Mixxa2015_Effects#Movie_Play> "Mixxa2015 Effects"). 

### Still Cut effect

After you assign a still image or movie to Still Cut, it reads the image from disk at its native resolution (it can be hi-res) and allows you to crop out a part at the compositing resolution (see **Setup**) of Mixxa. 

Then you can manually/randomly make the rectangle drift over the original image. See [Mixxa2015 Effects#Still Cut](</Mixxa2015_Effects#Still_Cut> "Mixxa2015 Effects"). 

### Blend effect

Two cells are mixed. In the default Mixxa2014, these are at the top of column 5, 6 and 7 in Matrix X and they blend the first 4 columns, as you would see in **Wire**. 

The incoming video streams are the small icons above the cross-fader. The cross-fader mixes between the first input (cross-fader left), the blend, and the second input (cross-fader right). 

The blend effect is determined by clicking the blend type name at the left, which brings up a new "blend type" window. Select one of 35 blend types. Rolling over a blend name lets you preview the effect without changing the output of the cell. 

In the blend type window, some blend types are divided into two halves. The right side is the same as the left, but the right swaps the two inputs to the mix effect. The **12** or **21** button also swaps the two inputs to the mix effect. For some effects, A blend B is different than B blend A (like Hard Light). More at [Mixxa2015 Effects#Blend](</Mixxa2015_Effects#Blend> "Mixxa2015 Effects"). 

## Effects - common features

An effect in a cell has 0 to 4 video inputs (depending on its type), and one video out. Many effects that you would think as 0-input generators actually allow 1 input to be mixed in with effect. 

### Reset

The small **R** on each cell effect resets the effect's sliders to their default. 

The large **R** above a Channel will reset all effects for the whole layer. It resets a layer to its defaults so video goes through unmodified. Any LFOs (Expert: Low Frequency Oscillators) that were driving an effect are muted. LFOs can be manually un-muted by selecting **Un-Mute** on a slider’s right-click menu. 

The larger **R** at the top of the screen is Super-Reset - it resets all 9x9 cells. 

### Reset Gadget to its Default Value

Right-click a gadget and in the Control menu select **Reset**. 

### Bypass

Pressing the bypass **>** arrow skips the effect, but does not affect the sliders, so you can go back to the effect settings by turning bypass off. (With bypass on, the effect is seen in the preview, but the effect is not passed to the next stage.) 

## Monitors

The **Monitors** panel is the last stage before the images go to the monitors or projectors. 

It sends video from any cell (normally from the Z matrix) to any of 3 monitor outputs. (You can get 3 outputs with a Matrox TripleHead2Go, a Geforce 680 GTX, some AMD-ATI cards, or multiple NVIDIA cards in Mosaic mode.) 

Attach you monitor to your computer and turn them on before starting Mixxa. You should at least see your cursor when you move your mouse to the other monitors. 

On Windows 7, run Mixxa multi-screen with a span of 2, 3 of 4 monitors wide. On Windows XP, if you run Mixxa with the right monitor on, then we prefer you set the monitors to Horizontal Span. This will result in two monitors at the same resolution at the fastest speed. 

Start Mixxa. Bring up **Monitors**. Set **Main Monitor plus ...** to the number of extra monitors you have hooked up. Then press the tabs **1** **2** and **3** to expose the per-monitor settings. 

### Assigning a Cell to a Monitor

It will let you select which cell to use for each monitor. Then it lets you crop it and corner pin the image before outputting to each monitor. 

Selecting the cell to output: 

**1 2 3 4 5 6 7 8 9** – they take the bottom of each column. 

The button called **Sam** – if you click that, then the output to the monitors is always the current cell, that’s good for a low attention span audience. 

Also in Monitor, **Sa Ho** (sample and hold) will just take the current cell and hold on to in. If you go to another cell as output (like you press the 6) you can press Held to go back to the Held cell. 

But you can also "jam" with the monitor wiring, where in Monitors you select **Sam** (=sample) and just make any of the 81 cells the current cell, and that cell goes directly to the projector. If you want to fixate on any one cell, you can click **Sa Ho** to select a cell, the whenever you click on **Held** the held cell gets sent to the projector (your trump card). 

## Audio - Mixing Sound From Movies

In the **Audio** panel you can mix audio for up to 5 Movie Play movies. 

For each of the 5 audio channels, the audio can come from one of two places. Look at the 2 rows of buttons above the audio sliders: 

(row 1) You can use the movie that is assigned to the corresponding **Movie Play** or **Still Cut**. 

(row 2) You can choose the currently-selected movie in the movie preparation panel. If you select a new movie in a bin, the audio changes to that movie. 

If you want to hear audio in a movie and not see it, you can put a Movie Play into say row 1 column 9, and don't mix that cell into any monitors' output. 

You can mute audio (to save CPU time). Each channel has a VU meter, and level control. The red V buttons are mutes. Each channel’s fader has (1) a blue level indicator of the raw sound from the movie, (2) a white level control so you can increase or decrease the movie’s audio level and (3) a green indicator of the audio being output from the channel. 

**NOTE:** Output audio that exceeds value 1 (middle of slider) will clip and slider will turn red. 

There are two choices of audio output: 

(i) **Audio – Stereo Mix** \- All 4 movies are mixed in stereo in Touch and go out the first 2 audio ports. The Monitor levels (small sliders on top) also mixed the 4 sources separately and go out the second pair of audio out ports on your sound card. 

(ii) **Audio – One Chan/Movie** – Each movie is mixed down to mono and then goes out one channel on your sound card. The Monitor mix goes out to channel 5 and 6 of your sound card. 

## Save your Sessions

The **Save** button saves all your current settings into a new TouchDesigner .toe file. **Save** often. You can restart Mixxa by drag-dropping the new .toe file onto the Mixxa.exe program or double-clicking Mixxa.toe, it will restart your saved file. 

## Creating a New Bin

Mixxa comes with 9 bins already created, most of them are unused, so you can start naming and using them directly. 

But if you need more than 9, right-click in the bin area and select from the menu: **New Bin**. 

## Using Your Own Movies and Stills in Bins

There are two ways to add your movies and images to Mixxa: 

### Drag-Drop media from Folders

You can drag-drop movies and images from Windows folders or the Desktop onto Mixxa bins and they get added to the bin. Select an unused bin, then press Explorer at the bottom. Go to any folder in Explorer and drag-drop movies into the bin's movie area. Each movie or image will get its own button. 

### Load entire Folder

Load a folder of media via (1) the **Media** panel (40), or right-click on a bin button or (3) the currently-selected bin name, or (4) the + to the right of the bin name. 

Here you give the folder path and press **Reload Now**. Details below: 

Press **Media** to get access your own movie/stills files. Pick an unused bin, give it a name, give it a path to the movies’ folder (or hit + to pick any movie in that folder), then press **Reload Now**. One button is created for each media file. 

The **Media** window organizes your bins and lets you select the folder for 40 or more bins. 
* Pressing the + button on the bin, or right-click -> **Properties** on a bin name brings you the bin properties window where you can browse and **Accept** a new folder name. Pressing **Reload Now** replaces any reorganizing you have done in a bin. You are starting fresh, replacing all buttons in that bin. See below to Drag-Drop single or multiple media files into the bin.
* **Group** \- Color code your bins (click on right column).
* **Reordering your bins** \- Select a bin (click on the # column, then right-click on any other bin and select **Move Here**. It does not affect the contents or settings of a bin.
* **Active** – Turn off a bin if you won’t use it for a performance, or turn a bin off to save memory. Reload here too, recursive search for movie files. It will force the movies of a bin to 4x4 resolution, and take it out of the set of bin buttons at the top. (It doesn’t destroy anything. You can re-activate any time).


**40.** [![Mixxa2012.9.6.jpg](./images/0/06/Mixxa2012.9.6.jpg)](</File:Mixxa2012.9.6.jpg>)

Quit the Media window. **Right-click on any movie bin button** (41) to get the movie bin menu. Here is another place you can get the bin’s Properties, and you can de-Activate the bin and re-order the bins. 

**41.** [![Mixxa2012.15.1.jpg](./images/6/69/Mixxa2012.15.1.jpg)](</File:Mixxa2012.15.1.jpg>)

Note: The **A B C D** ... buttons in the Movie Prepare panel are useful to re-select the bin and media that is assigned to Movie Play and Still Cut cells in the matrix. 

**NOTE:** Media coming from outside the bin’s folder (non-native media) - A selected movie button whose file is not located in the bin’s native folder is **highlited in yellow** , not white. 

## Preparing Movies in a Bin

Right-click on any movie to display the '_Movie_ menu where you can organize you movies: 
* **Assign** a movie to layers A to D (in addition to drag-off method).
* **Undo Connect** the last two movie assignments to the layers.
* **Duplicate** the movie button. The new movie will ahve its own in/out points, speeds and so on. This doesn’t affect the file on disk – it just copies the button in Mixxa and both point to the same file.
* **Copy, Paste** or **Cut** (delete) movie button. A movie button that is Cut or Copied can be then pasted in any other bin.
* **Move Here** reorders the movie buttons in a bin: Select any movie (left click), then on any other movie, right-click and select **Move Here**.
* **Make Icon** or **Make Icons** creates a small .jpg file for one or all movies in an bin. It is used when TouchDesigner starts and first goes to the bin - it displays this icon, then when you roll over the button, it plays the actual media file.
* **Properties** gives the movie statistics and lets you change the movie itself. You can select Properties, then select another movie and press Open. Or right-click on any movie in its folder and select Open with QuickTime to see further properties.


TIP: You can also get the movie menu without using the right mouse button: Press (like on a touch screen) on the movie and drag off to the left. 

## Copy-Paste Groups of Movies

You can copy-paste groups of movies in bins by shift-clicking or ctrl-clicking on movies to select more than one. Then right-click on a movie to group-Copy, Delete, etc.. Then go to any bin and right-click and Paste or Move Here. 

## Presets

Presets let you take a snapshot of your current matrix settings and then at a later time, you can restore the settings. 

You can restore a preset all-at-once, or more intriguing, you can restore one or more cells at a time to gradually transition between entirely different presets. 

The settings saved in a preset include: 
* the type of effect in each cell
  * the settings of all controls of the matrix cells
  * the wiring of cells outputs to cell inputs
  * in effects like Movie Play and Still Cut, all the movie settings like in-out, crop, etc
  * in effects like Finger Paint, it retains the line strokes


A preset does not hold: 
* controller mappings like MIDI or LFO or Gesture (see Event Record)
  * audio mixing settings (see Event Record)
  * the assignments of cells to monitors


Click **Presets**. The numbers at the top are the 30 preset Banks. Most banks are empty except 1 and 2. Bank 2 has about 7 presets. 

When you click a preset, the "restore grid" at the bottom of Presets will show the color-coded difference between the currently-running matrix and the preset you are about to restore. This is hugely powerful. 

The top row of thumbnail images above the restore grid are the movie/image files that are used by the preset. Clicking them will restore just that movie. (Each thumbnail corresponds to a grey or blue box below.) (The movies in the original bins are not affected by restoring presets.) 

In the restore grid: 
* Green box means that the cell is the same effect type, but at least one of its controls is different in the preset vs he currently-running matrix. Clicking a green box will restore the preset's control settings to that cell.
  * Yellow box means that the effect in that cell is different (e.g. Fizzle vs Zoom) and clicking a yellow box will replace the matrix cell with the preset's effect and control settings.
  * Blue box means it's a Movie Play or Still Cut type of effect, and it's known that the movie is different than the movie active in the corresponding matrix cell. One of the image thumbnails above the restore grid is the new movie.
  * Grey box means it's a Movie Play or Still Cut type of effect, but the movie is the same as that in the matrix, however the movie settings MAY be different (it doesn't check that deeply, which is why it stays grey).


You can also box-pick a bunch of cells in the restore grid and it will restore just those cells. 

By saving presets, you can plan the key moments of an entire performance. Or presets can be a library of jump-points when improvising. A proper drunk VJ will just press a preset and then get distracted by someone nearby. 

You can transition from one preset to another, cell by cell. 

There are 30 preset banks that can hold unlimited presets, banks can be individually renamed. 

You click a preset and then press **Restore** , which brings the movies, effects and the mix back to the previously saved state. **Restore** restores everything, or optionally restore only one layer, a pair of layers and their mix, or all 4 layers. 

The **New** button creates a new preset and does an instant Snapshot. 

To improve a preset, restore the preset, make adjustments in the layers etc, then press **Snapshot**. 

You can re-order the presets within a bank via the right-click menu on a preset. 

**More Info on Presets**

=Preset preview - After you single-click a preset, you can see previews of what movies will play once you Restore. 

Right-click on a preset to get the menu to duplicate, delete, restore or Properties. 

To record your gestures, controls, cell assignment, etc, and play them back in realtime or non-realtime for recording, see **Event Record**. 

## Gesturing Sliders

Any slider in a Mixxa cell can be gestured and repeated. Simply press-hold Shift and move sliders up-down and release Shift. After you release the Shift Key, the slider will repeat what you just did. 

To turn the gesture off, click the slider without pressing Shift. 

Gestures are not saved in the`.toe`file. 

( Presently, this only applies to all Router connections below: You can adjust the upper-lower range with right-click -> **Range** on a gadget. ) 

## Router - Controlling Gadgets with MIDI, LFOs and more

You can control cell gadgets with signals in the **Router** like MIDI, LFOs, audio and mouse gestures. 

**Router** lets you take MIDI controllers, internally-generated LFOs (low-frequency oscillators) and other signals, and connect them to Mixxa sliders or buttons, allowing them to be automatically driven. 

Router sources include **Test** (fixed at 0, .5 and 1), **LFOs** , **MIDI In** , **OSC In** and the audio **Spectrum**. **NOTE: OSC In currently needs you to go inside Mixxa to enable functions.**

[![Mixxa2012.3.2.jpg](./images/5/51/Mixxa2012.3.2.jpg)](</File:Mixxa2012.3.2.jpg>) -> [![Mixxa2012.10.1.jpg](./images/1/14/Mixxa2012.10.1.jpg)](</File:Mixxa2012.10.1.jpg>)

### Routing LFOs to Mixxa Sliders

In each sliders/buttons’ right-click menu in Mixxa, you can directly assign the 8 **LFOs** (low-frequency oscillators) to the sliders. This can automatically drive Mixxa controls using built-in oscillators which repeat based on beat counts, or freely with a speed slider. 

Click **Router** , select **LFO** , select any **lfo1** to **lfo8**. Adjust the LFO's various timing curve shapes. Then right-click on any Mixxa slider and select **From LFO x** from the menu. Then on each LFO you can adjust the wave shape, speed, phase, smoothing and inversion. 

### Drawing LFO Curves

In any Router LFO (lfo1 to lfo8), you can select the curve type **draw** and then draw into the space above it to create the LFO curve. 

### Routing MIDI Inputs to Mixxa Sliders

To connect MIDI sources to Mixxa sliders/buttons: 

It is best to have your MIDI hooked up before you start up Mixxa. 

Press **MIDI** at the bottom-left to bring up your MIDI control panel. Assign MIDI devices to ID 1 and/or 2. Once this is done, Router -> MIDI IN should show gadgets moving as you move MIDI controllers. See below for more info on connecting MIDI In devices to sliders and buttons in the Mixxa. 

Once MIDI is set up, move a MIDI slider or button. Then right-click on a Mixxa slider and select **Connect** from the menu (47a). 

Then you can select **Mute** from the menu to temporarily disconnect, or **Disconnect** to completely dis-associate it. 

See [#MIDI Controlling Mixxa](<#MIDI_Controlling_Mixxa>). 

### Routing Audio Spectrum to Mixxa Sliders

Click Router, select SPECTRUM, make Enable ON. Connect audio to the input of your computer and assure it's generating a signal in Source Device. 

Then select any **spec1** to **spec3**. Adjust the spectrum frequency, width, threshold, gain and smoothness. Then right-click on any Mixxa slider and select **Connect** from the menu. 

If the Router -> Spectrum doesn't get audio, try turning on Demo Music and confirm all is working. Press Esc, go to`/mixxa/router/spectrumFile`, something like that, and find the Audio In CHOP and change its menu, Save, then go back to Perform mode (F1 key). 

### Tapping Rhythms on ASCII Keyboard and Mapping to Mixxa Sliders

In Router, click TAP to use the ASCII Keyboard to drive any control in the matrix with attack-sustain-decay pulses. Press Listen on (or the Q W E R keys), tap on Tap (T key), Press Listen off (or release (Q W E R). Watch it repeat, adjust Mix and Max, adjust Lag Up and Lag down. Then you can assign it to a Matrix control. On any of the 4 taps you can Mute (or the A S D F keys), or Unmute (Z X C V keys). At the top you can mute all the taps in one shot (G key), then unmute the muted ones in one shot (B key). 

### Routing OSC to Mixxa Sliders

You will need to set it manually internally. Go to`/mixxa/router/oscin`. The OSC In CHOP needs to be set up to work with your OSC stream, and connected to the`select1`CHOP. 

### Listing the Controls that are Mapped to Gadgets

Go to **Router** and press **Show Mappings**. For all Router-driven and Gesture-driven gadgets, it will list each internal parameter name and the control that is mapped to it. For example,`r2c4/level`is a level slider in the 4th effect in channel 2 (contrary to what you may think). 

### Routing Mixxa Sliders to External Software

You can send Mixxa slider states to destinations like MIDI Out or OSC. **NOTE: This feature currently needs you to go inside Mixxa to enable functions.**

Press **Router** (48), and then press **MIDI Out** ... Adjust the lower-upper value range in the bottom half of Router. 

(48) [![Mixxa2012.17.1.jpg](./images/5/56/Mixxa2012.17.1.jpg)](</File:Mixxa2012.17.1.jpg>)

## Recording to a Movie File

Press the image at the bottom right of Mixxa. 

It will keep recording a`.mp4`movie file into the`MixxaOut`filesystem folder (the Mixxa Out bin) until you press the image button again. It displays the filename of the last movie it created. At the same time it creates a new movie button in bin 2, **Mixxa Out**. If you click the text below the image, it will bring up Explorer to the folder where the movie was created. 

Output movies are by default set to 30 frames per second. Right-click on the image (or go to Setup) to bring up a window that will let you change the output bin, the movie's frame rate, codec, and choose to fill missing images with repeats, in order that the output is a complete 30 frames per second (default will record every image once only, but it may look like it's running fast). 

(To record audio, you would have to go into the network`/mixxa/movie_spec`and set the`audio`row to 1, and maybe`select_audioout`needs to be fetched from the right place.) 

## Event Record - Recording Raw Events of a Performance

The buttons **Event Capture**, **Event Replay** and **Record Movie from Events** will capture everything that happens in the matrix into an events file, which can be recalled and rendered non-realtime to a movie file. 

Event Capture captures your clicking and movements on your controls, plus it records when you change a cell to another effect, change its wiring, its movie settings and more. 

After capturing, Event Replay can play the events back in realtime or non-realtime, and can be recorded into a movie file. The event file is a readable ASCII list of time-codes and event descriptions. 

For the Extremely Drunk VJ, a full past performance can be replayed and tweaked on the fly by someone else like a Substitute Drunk VJ. This is not highly recommended however. 

Start by pressing **Event Capture** and move controls, assign movies etc. in the matrix. 

Then stop it by pressing Event Capture again and click **Browse** to find and pick the events file you just captured. 

Then press **Event Replay** to see what you captured. Cells pop open when controls in it are modified. You can close cells by hand without affecting the replay. 

You can then press **Record Movie from Events** to go through the events file again and create a movie file that gets placed in the Mixxa Out bin. 

## Setup and Tuning Mixxa

Press **Setup**. 

In its dialog: 
* Press the **Processing Resolution** buttons to use more or less graphics card memory. It can affect the speed of Mixxa, shown in the milliseconds per frame and GPU indicator at the bottom left.
* **Load Icons on Start**
* **Show Popup Help**
* **Cell Expose Time** sets how fast cells open and close. This is purely cosmetic.
* **OSC computer** is for output to OSC. You will need to go to`/mixxa/router/oscout`work out what you want to route out, then enable`/mixxa/router/oscout1`. You get and route the OSC streams in **Router - > OSC**.


Setup also lets you choose which cell goes to Mixxa Out or the output stream. 

### More Setup Tips

The taskbar -> Properties -> **Auto-hide the taskbar** should be on, or The Windows task bar **Always on front** should be off. No screen saver, no power saving options in case you need to leave for a while. Cheeose Vertical Sync on (non-tearing video) or off (could be faster). 

### Moving Settings from a Prior Version of Mixxa

Because bins, movies, presets, the library of effects and their controls are very intertwined and evolving, it may require some hand-tweaking to move your past systems over. 

#### Current Procedure

To move your work from the prior`Mixxa.toe`to the current one, you can do this: 
* click the layout called "bins" in the network (it just takes you to`/mixxa/bins`)
  * right-click on the component`binsuser`and Save Component… it will make`binsuser.tox`* click the layout called "presets" in the network (it just takes you to`/mixxa/presets`)
  * right-click on`banksuser`and Save Component… it will make`banksuser.tox`* Then go into the new`MixxaDec2014.toe`and go to /mixxa/bins. Delete`binsuser`. Drag-drop`binsuser.tox`to the network, which replaces the previous one.
  * Do the same kind of thing in`/mixxa/presets`.
  * Save the`.toe.`* Perhaps restart.
  * You may also want to change the things in Setup that you had before.
  * And if you have been making movies to the Mixxa Out bin, you may want to raise the latest movie number in`/mixxa/movie_record`\--- there is a table in there with the latest movie number in it…

#### Prior Procedure

If you receive a new version of a Mixxa`.toe`, you can preserve all the bins, movies and presets by going into **Setup** of your older Mixxa2012.exe and Mixxa2012.****.toe. 

Press **Save Media Settings** , which creates a file`mixxamedia.tox`for transporting. Then on the new Mixxa, Setup -> Restore Media Settings. Presets may need to be moved in by hand, so you will have to go into`mixxamedia.tox`and fish them out. 

### Changing the Target Frame Rate

The default frame rate is 60, which matches the frequency of many monitors. If your monitors and display devices are 50 Hz, go into Mixxa (Press Esc) and set the Rate at the bottom left from 60 to 50. Go back into **Mixxa** (press F1) and Save. 

## Making Mixxa run Fast

See also the [Setup and Tuning Mixxa](<#Setup_and_Tuning_Mixxa>) section to adjust Mixxa’s performance. 

### Turn Audio Off

If you are not mixing and outputting audio, turn it fully off: In the **Setup** panel, click the **Audio** button off. It will stop its extra processing, and the the **Audio** button on the bottom right of the main interface will disappear. You can still process audio input in **Router** -> **Spectrum**. 

### Performance Monitor

The lower-right button with four rapidly-changing numbers display: 
* the milliseconds per frame it is drawing at (33 would be 30 frames per second)
  * the % of frames dropped out (measured versus 30 fps, half the (default) 60 fps frame rate)
  * the number of megabytes of graphics card memory (GRAM or GPU RAM) you are using
  * the number of megabytes of RAM you are using


If you press that button, it will bring up the Touch Performance Monitor so you can analyze what it’s hung up on. There you can press Batch and see the sequence of events. 

If you right-click on that button, it brings up a time-history graph of your milliseconds-per-frame. 

### NVIDIA Control Panel
* Triple Buffered - In NVIDIA drivers, you can set the Display Settings -> Advanced -> Geforce xxx -> Performance & Quality Settings -> Advanced -> **Triple Buffered** to be On.
* Vertical Sync - And while you are there, try **Vertical Sync** Off. You may see some shearing of your output image on some monitors, so turn Vertical Sync On and live with a slightly lower frame rate.
* If buttons disappear in the Mixxa interface, reduce the **Quality <\--> Performance** settings to be one step down from top performance.

### Other Speed Factors

**Hiding Panels** \- Lots of things can make Mixxa slow down. Most panels in the user interface are quite fast, but it helps to hide panels when not in use. 

**Composite previews** and Mix ABCD section - it may run a bit faster if you go to **Setup** and toggle it to show the icons vs the previews. 

**Movie Formats** \- You can use your own movies and stills through the **Media** button at the bottom left. We prefer QuickTime .mov movies and .jpg stills, or .tif files if you have alpha channels. (It will also read .avi, .mp4, .mpg and .mpeg files, plus some other image formats, plus occasionally a .swf file will play as well.) 

The QuickTime .mov codec that’s best is Photo JPEG. Resolutions between 256x256 and 800x600 are OK on today’s computers, and High Quality gives the best trade-off. Recently we find that H.264 play well also, preferably with the [FFmpeg](<./FFmpeg.md> "FFmpeg") feature enabled. 

**Disks** \- Buy a Solid State Drive (SSD). The biggest chronic slow-down is having all your movies on one non-SSD disk, where if you are playing more than one movie from a disk at a time, you are forcing your disk to seek back and forth a lot, even if your disks are de-fragmented. Also using disks with a low RPM, like the sub-5000 RPM disks on laptops slow things down too. 

**Graphics Cards** \- We recommend a 1 Gb meg graphics card, a high-end Geforce 560 GTX card and above. We’re finding ATI 7000 series and above to be acceptable as well, but it’s less-tested (- your feedback welcome). 

## Beware of Memory Overload

#### GPU Memory

If total graphics memory in the Performance Monitor

is larger than the memory you have on your graphics card, that’s acceptable as NVIDIA and ATI cards overflow into your computer RAM at almost no time expense. But we find that when it exceeds the built-in graphics RAM by 20%, it may fail (white images) and run slower. It’s an NVIDIA thing. 

In this case, in **Setup** , you can reduce the **Processing Resolution** and you should see an immediate reduction in the Graphics RAM number. At 1280x720, each movie takes about 36 meg. Reduce the overall Processing Resolution to 960x540 or 800x450 or less. 

It is preferable to choose the 16x9 resolutions (the green ones). 

Tip: Also use Reset on panels to assure you are not processing more than you need. (slight improvements) 

#### CPU Memory

If Mixxa.exe in Task Manager gets to be over 1.6 Gigabytes on a 2000 Mb system, Mixxa may halt. **On Windows 64-bit versions, you get 2.6 GB of CPU memory** automatically. 

You can make Bins’ **Active** flags Off. (Click on **Media**.) To a lesser effect, use **Setup** to reduce the **Max Movies Open** , though below 10 may have side effects. 

## MIDI Controlling Mixxa

First you set up your input devices via the MIDI -> MIDI Input Device Mapper. 

See the [MIDI Device Mapper Dialog](<./MIDI_Device_Mapper_Dialog.md> "MIDI Device Mapper Dialog"). Assign your MIDI hardware to MIDI Device 1 and/or 2. The MIDI signals from these devices will reach the **Router'** s MIDI section. 

Then you assign MIDI devices to most sliders and buttons in Mixxa: 

**MIDI-assignable sliders** \- Almost all sliders and some buttons in the Mixxa UI are easily MIDI-assignable. 

First you map your MIDI input devices’ sliders/buttons/knobs to Mixxa via MIDI -> MIDI Device Mapper. Then for each MIDI-Mixxa slider assignment, you first move/press/turn a MIDI device, and then you right-click on the Mixxa slider or button to bring up the slider menu, and select **Connect**. 

In the same menu you can also **Mute** the effect of a MIDI slider on a Mixxa slider. **Un-Mute** restores the previous MIDI connection. You can also change what the 0-1 MIDI device range maps to on the slider by selecting **Range**. 

Even the **XY gadgets** in Touch are MIDI-assignable in X and Y. 

MIDI channel overrides - If you want to separate your second MIDI device from your first, you can force its MIDI channel to 3, say, by setting the overrides in the “MIDI” panel. 

### Feeding Back from Mixxa to MIDI Devices

Behringer BCF-2000, BCR-2000 and some other **motor-driven devices** are driven from TouchDesigner in the MIDI control panel. 

Edit the script in`/start`of Mixxa in the section "`for Mettler`". It sets up which controls in your matrix or other panels will feed their values back to the MIDI device. 

## Library of Effects for Cells

Go to the full effects library at [Mixxa2015 Effects](</Mixxa2015_Effects> "Mixxa2015 Effects"). 
* Black
  * Blend - 35 ways of blending images together
  * Blur
  * Clouds
  * Color Push - push color out of an image
  * Corner Pin
  * Deke
  * Drift
  * Edge
  * Extract
  * Feather - soften edges of an image
  * Feedback
  * Film - fake film effect
  * Finger Paint
  * Fizzle
  * Key Fade - luminance key
  * Level - black level, gamma, brightness
  * Luma Key - luminance key
  * Matte - use a grey-scale image to mix two images
  * Mod - monochrome, key, blur, brightness
  * Movie Play - play movie files and stills
  * Net Stream - receiving video from another TouchDesigner computer
  * Null - pass-through
  * Outs - ignore
  * Patch - rearrange an image
  * Perlin Noise
  * Repeater
  * Sample
  * Search - does a web search for images and you can select from the results.
  * Still Cut - crop a high-res image and navigate around it
  * Stoner - formerly a 4-point keystoner, now a 9x9 patch editor to warp images
  * Text Pattern
  * Tile
  * Time Jitter
  * Video In - Direct Show video devices and cameras
  * Words
  * Xform 3D - wrap image on simple 3D shapes
  * Zoom - tile and zoom into image

## Creating and Customizing you own Effect Types

Like in all of TouchDesigner, you can see the network of any gadget or effect by pressing F10 or F9 with your cursor over that item. 

You can create your own effects and use them in same way as the built-in effects. 

Go to`/mixxa/lib`. Copy-paste a similar effect and rename it. Add its name to the table`libmap_`set its`enable`column to`1`. That should enable the effect to be in the Replace Cell menu. 

Next go to the new component and change its clone parameter to refer to itself. 

Then go into the component and change the`define`table row`name`to be English name of the effect. 

Save your`.toe`file and now you can edit the new component all you want. Retain the`bypass`node. If there is a`blend`node, leave it as-is, and retain the wiring at the end of the network chain. 

If you rename sliders or other controls, or add new controls, edit the`map`table, which is used by the`reset`button, and by Presets. 

To test, on the inputs of the new component, you can hook various video streams, like you see being done to other types in **/mixxa/lib** for testing. 

Note that none of these components are seen in the Matrix. Only Clones of these effects are in the network. 

Go to Perform Mode again (F1 key). Pick a cell to replace and right-click on its name. When you Replace Cell and select your new effect type, it replaces the cell's network that was there. 

Right-click on a cell name and select **Network of Master** or **Network of this Cell**. Note that only Network of Master will have its changes saved. 

## History of Movie Assigns

Click **History** to get the icons of the last 25 movies you assigned. Assign them just like you would the movies in the Bins. 

More info on TouchDesigner: [derivative.ca](<http://www.derivative.ca>)

author: ze0time
