# Palette:movieEngine

## 

Summary

The movieEngine [Palette](<./Palette.md> "Palette") component is a UI-less [moviePlayer](<./Palette-moviePlayer.md> "Palette:moviePlayer"), and is a multi-purpose tool for playing, controlling and examining movies. It can be used standalone or embedded in TouchDesigner applications. Unless otherwise noted, movieEngine features are also part of moviePlayer. 
* Drag-drop movie or image files onto the viewer from the desktop or from Movie File In TOP. Alternately change the file name in the File parameter.
  * Clicking on the movieEngine viewer controls scrubbing the movie (a minimal UI).
  * It plays a movie's audio to an audio device and/or the component's output.
  * movieEngine lets you switch to a new movie without frame drops via drag-drop, scripting or parameters.
  * Movie playback can be externally controlled with CHOP ramps, python commands and pulse parameters.
  * Using cues set up in moviePlayer, you can set multiple in- and out-points and then jump to cues, play and loop.
  * movieEngine uses Movie Spec components that can hold your movie settings and cues, which enables you to later re-call and play sub-sections of movies using movieEngine or moviePlayer.


**Note** movieEngine follows the Initialize/Start convention of TouchDesigner, which gives more control over transition from one movie to the next. It separates the process of (1) specifying a new movie or movie spec via drag-drop of changing pars, (2) the Initialization of the new movie at certain starting point, cued ready to play and (3) triggering to Start at that point. This can all be done in one shot (default) or separately with the Initialize and Start pars. 

(Get movieEngine from the Palette, or, from the External page of moviePlayer, press Create Engine COMP.) 

See also [moviePlayer](<./Palette-moviePlayer.md> "Palette:moviePlayer"), [movieBlender](<./Palette-movieBlender.md> "Palette:movieBlender"), [moviePlaylist](<./Palette-moviePlaylist.md> "Palette:moviePlaylist"). 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[Palette:movieEngine Ext](<./Palette-movieEngine_Ext.md> "Palette:movieEngine Ext")

## 

Quick Start

Get movieEngine from the Palette -> Tools, then rclick -> View to get it in a floating window, or simply use movieEngine in the node viewer in the network. 

To play a new file, (1) change the file name in the File parameter, or (2) drag-drop movie files from a file browser onto the panel UI or node viewer (with [Viewer Active](<./Viewer_Active.md> "Viewer Active") on), or (3) drag-drop a [Movie File In TOP](<./Movie_File_In_TOP.md> "Movie File In TOP") onto the panel or the node viewer in the network. 

On the movieEngine parameter dialog, press Open Movie Parameters. 

On the top row of the floating dialog, you see the tabs Player (for player settings) and Movie (settings for the specific movie you are playing now). Select Movie and adjust anything (say, Speed, Gamma) and verify the speed/level changes. 

### 

Movie Settings and Adjustments

On the movieEngine parameter dialog click Open Movie Parameters, or on the movieEngine panel click the **Controls** button on the left. This brings up the custom settings of the current movie. 

Parameters on the Movie -> Settings 1 and Settings 2 pages adjust and prepare the movie: start-end trim, crop, Black Level / Luminance / Gamma adjustments, speed, audio gain, etc. Note that these adjustments don't affect the movie file itself, only how it is played in movieEngine. 

### 

Audio

The audio signal always goes out the second output. But movieEngine optionally plays audio to the default audio device (Internal Audio Player on the Control page). Its Volume parameter on the Control page is mirrored in the UI as the Audio slider. Alternately the second output of the component can be routed to a mixer/output component. 

### 

Initialize and Start

The [Initialize/Start](<./Initialize_Start.md> "Initialize Start") convention of movieEngine, and TouchDesigner in general, gives more control over a transition from one movie to the next. Normally, with On Source Change set to Initialize and Start, it will start playing the new movie as soon as it's loaded. But you can separate the process of (1) specifying a new movie or movie spec via drag-drop of changing pars, (2) the Initialization of the new movie at certain starting point, cued ready to play and (3) trigger to Start at that point. This can all be done in one shot (default) or separately with the Initialize and Start pars. 

Assuming you want to seamlessly get the the new movie loaded, initialized and paused at a certain frame, ready-to-play, at which time you would press Start or trigger it externally. For this behavior, set On Source Change to Initialize and Pause. Alternately, you want movieEngine to initialize nothing while you drag-drop a new movie or change the File Path parameter, and then initialize only when you press Initialize, etc. You can set the starting time using Initialize Time parameter. 

While playing, Go to Done, jumps to the end of the movie and stops. The pulse parameter Go Back to Prev Movie lets you alternate between the current and previous movie. 

Timing information is sent out the out3 output of movieEngine in a CHOP, with time counters and the current initialize, start, running and done states. 

### 

Transition

movieEngine is designed to play a single movie at a time and does not crossfade between pairs. Because loading and initializing the next movie frequently takes more than one frame, the image may be invalid for one frame or more. By default it fades down for .2 sec, reloads, and fades up for .2 sec. You can set those to 0 sec but some frames of black may appear. You can set Transition to Freeze and Cut, and it will hold the last frame of the previous movie and cut to the new movie when ready. Other tools using movieEngine internally will do crossfades. 

### 

Creating Cues

In moviePlayer you can set up cues (a point or sub-section of a movie), each with a "beauty" frame, a "start" time, an optional "end" time and a end-start crossfade time. 

### 

Using Cues

in movieEngine, you can play cues via the Go page of the parameter dialog. 

### 

Movie Spec Components

A Movie Spec component specifies a movie file path and movie adjustments like in/out trim points, cropping, brightness/gamma/black level, speed, cues, metadata and more. 

To create a Movie Spec component, open a moviemovieEngine via the File parameter of movieEngine, or drop a movie from the file system or a Movie File In TOP onto movieEngine's UI viewer. Then go to the External page, and press Copy Cur Mvspec Below. A new Movie Spec component is created below whose icon is the current movie. (You can check its Settings pages and look inside to see its cues.) 

Then you can drag-drop these "mvspec" components to the moviePlayer or movieEngine panel to switch movies with all their settings and cues. You can use moviePlayer to edit the mvspec component further. 

Alternately, change the movieEngine parameter Source Type to Movie Spec COMP, and change the Movie Spec parameter to the Movie Spec component that you want to play. movieEngine 

### 

Movie Spec Metadata Info

A Movie Spec component, on its Info page, also holds persistent movie metadata (as read-only parameters) that is normally only available if you open the movie file: images per second, time lengths, resolution, aspect ratio. So you can get movie info without opening the movie. (it is updated/validated every time the movie is opened by moviePlayer/movieEngine). 

### 

More on Cues: Cue Boxes, Columns or List

You can change the display of the top area to display cues as a time-ordered list. On the UI page, change the Cue Edit Area menu to Cue List. Cue Columns is convenient for use with touch screens. 

### 

Cue Internals

Note that every cue is a Base component in`movieEngine1/mvspec/cues`, each with a few custom parameters. 

After pressing Open Movie Parameters on the parameter dialog, if you have set a cue, you can see the Cues' parameters by selecting it in the top row of buttons beside Player and Movie. Or click the Set> menu and select Cue Parameters to bring up the parameters of a cue. 

Here you see where the start, end and beauty times are held. You can name the cue. The Enable parameter undisplays the cue in the timeline, and is useful when it gets too cluttered. The Next Behavior menu allows you to stop or loop when reaching the end of a cue. You can set it to go black (0 0 0 1) or zero (0 0 0 0) at the end of the cue. You can safely delete or re-order`cue1`,`cue2`... components in the cues network, or via the Set> menu. 

### 

Outputs

The movie image and audio go out the first two outputs. Output 3 is the current movie's aspect ratio, length and rate. Output 4 contains cross-fading channels and diagnostics that may be useful. 

movieEngine contains about 44 nodes initially without cues - your GPU memory may become the limiting factor as you add many moviePlayers. But its default behavior is to pause movieEngine when it is un-selected, to avoid using GPU and CPU time (see the Behavior page). 

### 

External Control of movieEngine

To drive movieEngine externally you can use CHOP timing ramps (like from a Timer CHOP, Beat CHOP or LFO CHOP). You can use python trigger commands to position/play at specific times or cues, or pulse parameters on the dialog UI that jump to cues or specific times. 

To drive it externally, go to the External page, choose a CHOP and a channel that you want to drive it with and set the CHOP and Channel parameters. Select the appropriate units - seconds, frames (timeline frames) or 0-1 fraction. Then turn on External Control Active. 

You can refer to values in the third output of the CHOP which contains 3 constant channels: length (how many seconds long in movieEngine is the currently selected cue (cue 0 is the full movie)), duration (this is the length divided by the Speed parameter - the movie takes longer to play if you set the Speed lower than 1)) and the movie's rate (images per second). 

On the "Cues" page of the component's parameters, you can select a cue number and press Go to Cue and Play, for example. You can drive this with python or by exporting to the parameters. 

You can alternately set a time and press Go to Time and Play. Also the parameters on the Cues page of movieEngine can be used to jump to cues, pause, play, etc. 

### 

Control of movieEngine with Python

The python extension in the component has the functions such as`GoToCue(cuenum, cuepoint, play)`and`GoToTime(seconds, play)`. Example to go to 50 sec and play:`op('movieEngine1').GoToTime(50.,1)`See the extension DAT in movieEngine, which contains more functions to control via python. 

### 

Multi-movieEngines or Multi-"Movie Specs"

There are two ways to manage multiple movies. Most simply, you can duplicate`movieEngine1`in the network and alter the duplicates. This will let you play several movies at one time. Changing the file name will delete all its cues and reinitialize all the parameters. 

Alternately, if you have more that 10 movies or so, you can have a multitude of lightweight "Movie Spec" components, and drag-drop them onto any movie player. This is equivalent to setting a movieEngine's Movie Spec parameter to point to the external`mvspec`component. 

To create a Movie Spec component, on movieEngine, on the External page, press the parameter "Copy Cur mvspec Below". It copies the current settings of the movie of movieEngine to a component`mvspec1`, just below movieEngine in the network. ( Internally it is copying the template`movieEngine1/mvspec1`or the latest`mvspec`outside`movieEngineoviePlayer1`. ) 

The Movie Spec components are very lightweight. Inside it are 5 passive nodes plus one empty Base component per cue. 

You can make several copies of`mvspec1`. Then for each`mvspec*`, you can edit its parameters manually. Then you can drag-drop it onto the`movieEngine`viewer, or assign it to the Movie Spec parameter of`movieEngine`. Then you can edit and add cues etc as you normally would with the moviePlayer UI. All edits are saved in your`mvspec`components. 

### 

movieEngine - moviePlayer Without UI

movieEngine is a lightweight component that can be embedded in other tools to smoothly drive movie playback and switching. 

On moviePlayer, on the External page, press Create Engine COMP Below. It will create`movieEngine1`in the network below moviePlayer, which is the same as moviePlayer, but with its UI removed and other non-essential operators removed. 

**TIP** : On movieEngine, you can middle-click to pause/play. You can left-click/drag on the image to scrub, and to pause when you release, release the mouse when the cursor is below the panel. To assure it's playing forward after you scrub, release with the cursor above the panel. 

Also movieEngine is controllable via its parameters, its inputs and its [Extensions](<./Extensions.md> "Extensions") calls in the same way as you control moviePlayer. 

### 

Crossfading Between Two movieEngines

To do crossfading or exact frame cuts between movies, you need two movieEngines or moviePlayers. 

Every time you assign a new`mvspec`to movieEngine's Movie Spec parameter, it may take a few frames to unload the prior movie, open the new movie and load the number of pre-read frames into the GPU. (It uses the [Timer CHOP](<./Timer_CHOP.md> "Timer CHOP") for this, and you can watch the timing on the`out4`of movieEngine So one movieEngine can never guarantee a perfect cut between movies. For this reason you need two movieEngine components to perfectly cut or crossfade between them. You get the second movieEngine to pre-load the next movie before making a cut or crossfade. You can use the "`fade fadein`" channels coming out of the 4th output of movieEngine to control the cross-fading. 

### 

Select Page

On the Setup page, Force Resolution internally scales the movie to your desired resolution when it is read. You can set the number of core for decoding, and turn on hardware decoding, which is recommended if possible. 

## 

Parameters - Control Page

Help`Help`\- 

Version`Version`\- 

Source Type`Sourcetype`\- ⊞ \- 
* File Path`filepath`-
* Movie Spec COMP`mvspec`-


File Path`File`\- 

Movie Spec`Mvspec`\- 

On Source Change`Onsourcechange`\- ⊞ \- 
* Wait for Initialize or Start`wait`-
* Initialize and Pause`initialize`-
* Initialize and Start`start`-
* Initialize and Use mvspec Play Parameter`usemvspec`-


Open Movie Parameters`Openpars`\- 

Initialize Time (sec)`Initializetime`\- 

Initialize`Initialize`\- 

Start`Start`\- 

Go to Done`Gotodone`\- 

Go Back to Prev Mv`Goback`\- 

Play`Play`\- 

## 

Parameters - Setup Page

Transition`Transition`\- ⊞ \- 
* Fade Down + Fade Up`fadedownup`-
* Freeze and Cut`cut`-


Image Fade Down (sec)`Fadedown`\- 

Image Fade Up (sec)`Fadeup`\- 

Audio Volume`Volume`\- 

Internal Audio Player`Internalaudio`\- 

Audio Driver`Audiodriver`\- ⊞ \- 
* default (DirectSound/CoreAudio)`default`-
* ASIO`asio`-


Audio Device`Audiodevice`\- ⊞ \- 
* default`default`-
* Speakers (4- RODE NT-USB)`{0.0.0.00000000}.{5071a211-8343-464c-9264-df1dbc35086e}`-
* Line 1/2 (M-Audio Fast Track Ultra)`{0.0.0.00000000}.{048c4e19-9ddb-4893-9d05-262c64b2a23e}`-
* Line 5/6 (M-Audio Fast Track Ultra)`{0.0.0.00000000}.{23ed4504-198e-49e2-9d1b-3cd3181507b8}`-
* Speakers (Plugable USB Audio Device)`{0.0.0.00000000}.{25205629-60ea-40ab-9a18-9d86f01e24a5}`-
* Line 3/4 (M-Audio Fast Track Ultra)`{0.0.0.00000000}.{6d1b0a8a-b02b-4cbc-a676-8dff634e1094}`-
* Speakers (2- USB Audio CODEC )`{0.0.0.00000000}.{725ad62d-e3ab-4188-aed5-50b53cb1f02b}`-
* S/PDIF (M-Audio Fast Track Ultra)`{0.0.0.00000000}.{74a6270b-bb92-4487-a8f2-baeee761d130}`-
* Speakers (Realtek(R) Audio)`{0.0.0.00000000}.{7731f2c6-1122-4a22-bb9d-d9d89b7d1e9b}`-
* U32J59x (2- NVIDIA High Definition Audio)`{0.0.0.00000000}.{8ca2679c-993b-4add-b51f-d35021515fbc}`-
* M2767PW (2- NVIDIA High Definition Audio)`{0.0.0.00000000}.{9d20bcfe-ca49-41ab-93ff-dd28936ca47c}`-
* Speakers (M-Audio Fast Track Ultra)`{0.0.0.00000000}.{d5c3917f-178c-4e12-bf6a-4d2cc2e05870}`-
* Speakers (USB AUDIO CODEC)`{0.0.0.00000000}.{f31f6287-0095-4cba-b2b9-b3172efcb9d1}`-


Force Resolution`Forceres`\- 

Resolution`Res`\- ⊞ \- 
* Resolution`Resw`-
* Resolution`Resh`-


Hardware Decode`Hardwaredecode`\- 

Max Decode CPUs`Maxdecodecpus`\- 

## 

Parameters - Go Page

Target Time for Go`Gotargettime`\- 

Go to Time and Pause`Gototimepause`\- 

Go to Time and Play`Gototimeplay`\- 

Target Cue for Go`Gotargetcue`\- 

Action for Go`Goaction`\- ⊞ \- 
* Cue Beauty`beauty`-
* Cue Start`start`-
* Cue End`end`-


Set Cur Cue on Go`Gosetcurcue`\- 

Go to Cue and Pause`Gotocuepause`\- 

Go to Cue and Play`Gotocueplay`\- 

## 

Parameters - UI Page

Time Units`Timeunits`\- ⊞ \- 
* Seconds`seconds`-
* Index`index`-
* Time Code`timecode`-


View Range Start (sec)`Viewstart`\- 

View Range Length (sec)`Viewlength`\- 

View Subrange`Subview`\- 

Roller Wheel Zoom Image`Rollerzoom`\- 

Left/Mid Mouse Button Pan/Scale`Lrmbpanscale`\- 

Panel/Scale Home`Panscalehome`\- 

Output Inspect Image`Outputinspect`\- 

## 

Parameters - Arrange Page

Viewer Location`Viewerloc`\- ⊞ \- 
* Behind Controls`behind`-
* Above Controls`above`-


Control Panel Always On`Controlsalwayson`\- 

Control Panel Opacity`Controlsopacity`\- 

Expose Help Button`Exposehelp`\- 

Cue Edit Area`Cueeditarea`\- ⊞ \- 
* Nothing`nothing`-
* Cue Box`cueboxes`-
* Cue Columns`cuecols`-
* Cue List`cuelist`-


Cue Edit Area Always On`Cueeditalwayson`\- 

Cue Edit Area Opacity`Cueeditareaopacity`\- 

Size of Cuebar`Sizecuebar`\- 

Size of Cueloop`Sizecueloop`\- 

Size of Scrubber`Sizescrubber`\- 

Size of View Range`Sizeviewrange`\- 

Size of Play Controls`Sizeplaycontrols`\- 

## 

Parameters - Select Page

Action on Select Node`Actionselecton`\- ⊞ \- 
* None`none`-
* Go to Beauty`beauty`-
* Go to Start`start`-
* Go to End`end`-


Cue on Select`Cueonselect`\- 

Set as Current Cue`Curcueonselect`\- 

Play on Select`Playonselect`\- 

Viewer Active on Select`Viewonselect`\- 

Action on De-Select`Actionselectoff`\- ⊞ \- 
* None`none`-
* Pause`pause`-


Selected`Selected`\- 

Special`Special`\- 

## 

Parameters - External Page

External Control Active`Extactive`\- 

Units`Extunits`\- ⊞ \- 
* Seconds`seconds`-
* Frames`frames`-
* Fraction`fraction`-


CHOP`Extchop`\- 

Channel`Extchannel`\- 

Copy Cur mvspec Below`Copymvspec`\- 

Save Cur mvspec to .tox`Savemvspec`\- 

Create Engine COMP Below`Createengine`\- 

## 

Operator Outputs
* Output 0 -
* Output 1 -
* Output 2 -
* Output 3 -
* Output 4 -


TouchDesigner Build: Latest\nwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditor

Palette  
---  
[Palette ](<./Palette.md> "Palette")• [Palette:arcBallCamera ](<./Palette-arcBallCamera.md> "Palette:arcBallCamera")• [Palette:arcBallGeometry ](<./Palette-arcBallGeometry.md> "Palette:arcBallGeometry")• [Palette:audioAnalysis ](<./Palette-audioAnalysis.md> "Palette:audioAnalysis")• [Palette:audioSet ](<./Palette-audioSet.md> "Palette:audioSet")• [Palette:autoMediaPlayer ](<./Palette-autoMediaPlayer.md> "Palette:autoMediaPlayer")• [Palette:battery ](<./Palette-battery.md> "Palette:battery")• [Palette:bitwigClip ](<./Palette-bitwigClip.md> "Palette:bitwigClip")• [Palette:bitwigClipSlot ](<./Palette-bitwigClipSlot.md> "Palette:bitwigClipSlot")• [Palette:bitwigDeviceRemotes ](<./Palette-bitwigDeviceRemotes.md> "Palette:bitwigDeviceRemotes")• [Palette:bitwigMain ](<./Palette-bitwigMain.md> "Palette:bitwigMain")• [Palette:bitwigNote ](<./Palette-bitwigNote.md> "Palette:bitwigNote")• [Palette:bitwigProjectRemotes ](<./Palette-bitwigProjectRemotes.md> "Palette:bitwigProjectRemotes")• [Palette:bitwigRemotesDevice ](<./Palette-bitwigRemotesDevice.md> "Palette:bitwigRemotesDevice")• [Palette:bitwigRemotesProject ](<./Palette-bitwigRemotesProject.md> "Palette:bitwigRemotesProject")• [Palette:bitwigRemotesTrack ](<./Palette-bitwigRemotesTrack.md> "Palette:bitwigRemotesTrack")• [Palette:bitwigSelect ](<./Palette-bitwigSelect.md> "Palette:bitwigSelect")• [Palette:bitwigSong ](<./Palette-bitwigSong.md> "Palette:bitwigSong")• [Palette:bitwigTrack ](<./Palette-bitwigTrack.md> "Palette:bitwigTrack")• [Palette:bitwigTrackRemotes ](<./Palette-bitwigTrackRemotes.md> "Palette:bitwigTrackRemotes")• [Palette:blendModes ](<./Palette-blendModes.md> "Palette:blendModes")• [Palette:bloom ](<./Palette-bloom.md> "Palette:bloom")• [Palette:camera ](<./Palette-camera.md> "Palette:camera")• [Palette:cameraBrowser ](<./Palette-cameraBrowser.md> "Palette:cameraBrowser")• [Palette:cameraViewport ](<./Palette-cameraViewport.md> "Palette:cameraViewport")• [Palette:camSchnappr ](<./Palette-camSchnappr.md> "Palette:camSchnappr")• [Palette:changeColor ](<./Palette-changeColor.md> "Palette:changeColor")• [Palette:changeToColor ](<./Palette-changeToColor.md> "Palette:changeToColor")• [Palette:checker ](<./Palette-checker.md> "Palette:checker")• [Palette:chromaKey ](<./Palette-chromaKey.md> "Palette:chromaKey")• [Palette:colorThreshold ](<./Palette-colorThreshold.md> "Palette:colorThreshold")• [Palette:compareComp ](<./Palette-compareComp.md> "Palette:compareComp")• [Palette:convolve ](<./Palette-convolve.md> "Palette:convolve")• [Palette:cornerPinPOP ](<./Palette-cornerPinPOP.md> "Palette:cornerPinPOP")• [Palette:cornerPinSOP ](<./Palette-cornerPinSOP.md> "Palette:cornerPinSOP")• [Palette:cppParsTemplateGen ](<./Palette-cppParsTemplateGen.md> "Palette:cppParsTemplateGen")• [Palette:customAttributes ](<./Palette-customAttributes.md> "Palette:customAttributes")• [Palette:debugControl ](<./Palette-debugControl.md> "Palette:debugControl")• [Palette:dent ](<./Palette-dent.md> "Palette:dent")• [Palette:depthExtract ](<./Palette-depthExtract.md> "Palette:depthExtract")• [Palette:depthProjection ](<./Palette-depthProjection.md> "Palette:depthProjection")• [Palette:dilate ](<./Palette-dilate.md> "Palette:dilate")• [Palette:domeViewer ](<./Palette-domeViewer.md> "Palette:domeViewer")• [Palette:encoder ](<./Palette-encoder.md> "Palette:encoder")• [Palette:equalizer ](<./Palette-equalizer.md> "Palette:equalizer")• [Palette:feedback ](<./Palette-feedback.md> "Palette:feedback")• [Palette:feedbackEdge ](<./Palette-feedbackEdge.md> "Palette:feedbackEdge")• [Palette:firmata ](<./Palette-firmata.md> "Palette:firmata")• [Palette:gal ](<./Palette-gal.md> "Palette:gal")• [Palette:geoPanel ](<./Palette-geoPanel.md> "Palette:geoPanel")• [Palette:gestureCapture ](<./Palette-gestureCapture.md> "Palette:gestureCapture")• [Palette:graphPlot ](<./Palette-graphPlot.md> "Palette:graphPlot")• [Palette:histogram ](<./Palette-histogram.md> "Palette:histogram")• [Palette:hsvBlur ](<./Palette-hsvBlur.md> "Palette:hsvBlur")• [Palette:imageSearch ](<./Palette-imageSearch.md> "Palette:imageSearch")• [Palette:julia ](<./Palette-julia.md> "Palette:julia")• [Palette:kantanMapper ](<./Palette-kantanMapper.md> "Palette:kantanMapper")• [Palette:kinectCalibration ](<./Palette-kinectCalibration.md> "Palette:kinectCalibration")• [Palette:kinectPointcloud ](<./Palette-kinectPointcloud.md> "Palette:kinectPointcloud")• [Palette:leapPaint ](<./Palette-leapPaint.md> "Palette:leapPaint")• [Palette:lightTunnel ](<./Palette-lightTunnel.md> "Palette:lightTunnel")• [Palette:logger ](<./Palette-logger.md> "Palette:logger")• [Palette:mandelbrot ](<./Palette-mandelbrot.md> "Palette:mandelbrot")• [Palette:materialDesignIcons ](<./Palette-materialDesignIcons.md> "Palette:materialDesignIcons")• [Palette:mesh ](<./Palette-mesh.md> "Palette:mesh")• [Palette:monochrome ](<./Palette-monochrome.md> "Palette:monochrome")• [Palette:motionSense ](<./Palette-motionSense.md> "Palette:motionSense")• Palette:movieEngine • [Palette:moviePlayer ](<./Palette-moviePlayer.md> "Palette:moviePlayer")• [Palette:moviePlaylist ](<./Palette-moviePlaylist.md> "Palette:moviePlaylist")• [Palette:multiLevel ](<./Palette-multiLevel.md> "Palette:multiLevel")• [Palette:multiMix ](<./Palette-multiMix.md> "Palette:multiMix")• [Palette:noise ](<./Palette-noise.md> "Palette:noise")• [Palette:onScreenKeyboard ](<./Palette-onScreenKeyboard.md> "Palette:onScreenKeyboard")• [Palette:operatorPath ](<./Palette-operatorPath.md> "Palette:operatorPath")• [Palette:opticalFlow ](<./Palette-opticalFlow.md> "Palette:opticalFlow")• [Palette:particlesGpu ](<./Palette-particlesGpu.md> "Palette:particlesGpu")• [Palette:pixelate ](<./Palette-pixelate.md> "Palette:pixelate")• [Palette:pixelRelocator ](<./Palette-pixelRelocator.md> "Palette:pixelRelocator")• [Palette:pointGenerator ](<./Palette-pointGenerator.md> "Palette:pointGenerator")• [Palette:pointillize ](<./Palette-pointillize.md> "Palette:pointillize")• [Palette:pointMerge ](<./Palette-pointMerge.md> "Palette:pointMerge")• [Palette:pointRender ](<./Palette-pointRender.md> "Palette:pointRender")• [Palette:pointRepack ](<./Palette-pointRepack.md> "Palette:pointRepack")• [Palette:pointTransform ](<./Palette-pointTransform.md> "Palette:pointTransform")• [Palette:pointWeight ](<./Palette-pointWeight.md> "Palette:pointWeight")• [Palette:popDialog ](<./Palette-popDialog.md> "Palette:popDialog")• [Palette:probe ](<./Palette-probe.md> "Palette:probe")• [Palette:projectorBlend ](<./Palette-projectorBlend.md> "Palette:projectorBlend")• [Palette:pushPins ](<./Palette-pushPins.md> "Palette:pushPins")• [Palette:puzzle ](<./Palette-puzzle.md> "Palette:puzzle")• [Palette:quadReproject ](<./Palette-quadReproject.md> "Palette:quadReproject")• [Palette:radialBlur ](<./Palette-radialBlur.md> "Palette:radialBlur")• [Palette:recorder ](<./Palette-recorder.md> "Palette:recorder")• [Palette:remotePanel ](<./Palette-remotePanel.md> "Palette:remotePanel")• [Palette:rgbaBlur ](<./Palette-rgbaBlur.md> "Palette:rgbaBlur")• [Palette:rgbaDelay ](<./Palette-rgbaDelay.md> "Palette:rgbaDelay")• [Palette:rgbContrast ](<./Palette-rgbContrast.md> "Palette:rgbContrast")• [Palette:sceneChanger ](<./Palette-sceneChanger.md> "Palette:sceneChanger")• [Palette:search ](<./Palette-search.md> "Palette:search")• [Palette:searchReplace ](<./Palette-searchReplace.md> "Palette:searchReplace")• [Palette:sharpen ](<./Palette-sharpen.md> "Palette:sharpen")• [Palette:sickEngine ](<./Palette-sickEngine.md> "Palette:sickEngine")• [Palette:signalingClient ](<./Palette-signalingClient.md> "Palette:signalingClient")• [Palette:signalingServer ](<./Palette-signalingServer.md> "Palette:signalingServer")• [Palette:softenAlpha ](<./Palette-softenAlpha.md> "Palette:softenAlpha")• [Palette:solarize ](<./Palette-solarize.md> "Palette:solarize")• [Palette:sopRender ](<./Palette-sopRender.md> "Palette:sopRender")• [Palette:splitter ](<./Palette-splitter.md> "Palette:splitter")• [Palette:stitcher ](<./Palette-stitcher.md> "Palette:stitcher")• [Palette:stoner ](<./Palette-stoner.md> "Palette:stoner")• [Palette:superFormula ](<./Palette-superFormula.md> "Palette:superFormula")• [Palette:SVG ](<./Palette-SVG.md> "Palette:SVG")• [Palette:sweetSpot ](<./Palette-sweetSpot.md> "Palette:sweetSpot")• [Palette:sweetSpotPreviz ](<./Palette-sweetSpotPreviz.md> "Palette:sweetSpotPreviz")• [Palette:synchroCache ](<./Palette-synchroCache.md> "Palette:synchroCache")• [Palette:synchroClient ](<./Palette-synchroClient.md> "Palette:synchroClient")• [Palette:synchroFrameIn ](<./Palette-synchroFrameIn.md> "Palette:synchroFrameIn")• [Palette:synchroFrameOut ](<./Palette-synchroFrameOut.md> "Palette:synchroFrameOut")• [Palette:synchroNDIIn ](<./Palette-synchroNDIIn.md> "Palette:synchroNDIIn")• [Palette:synchroSDIIn ](<./Palette-synchroSDIIn.md> "Palette:synchroSDIIn")• [Palette:synchroVideoOut ](<./Palette-synchroVideoOut.md> "Palette:synchroVideoOut")• [Palette:tdBitwigPackage ](<./Palette-tdBitwigPackage.md> "Palette:tdBitwigPackage")• [Palette:tdPyEnvManager ](<./Palette-tdPyEnvManager.md> "Palette:tdPyEnvManager")• [Palette:TDVR ](<./Palette-TDVR.md> "Palette:TDVR")• [Palette:testGrid ](<./Palette-testGrid.md> "Palette:testGrid")• [Palette:threadManagerClient ](<./Palette-threadManagerClient.md> "Palette:threadManagerClient")• [Palette:threadsMonitor ](<./Palette-threadsMonitor.md> "Palette:threadsMonitor")• [Palette:transitMap ](<./Palette-transitMap.md> "Palette:transitMap")• [Palette:twirl ](<./Palette-twirl.md> "Palette:twirl")• [Palette:vectorScope ](<./Palette-vectorScope.md> "Palette:vectorScope")• [Palette:virtualFile ](<./Palette-virtualFile.md> "Palette:virtualFile")• [Palette:waveformMonitor ](<./Palette-waveformMonitor.md> "Palette:waveformMonitor")• [Palette:webBrowser ](<./Palette-webBrowser.md> "Palette:webBrowser")• [Palette:webRTC ](<./Palette-webRTC.md> "Palette:webRTC")• [Palette:webRTCPanel ](<./Palette-webRTCPanel.md> "Palette:webRTCPanel")• [Palette:webRTCPanelRcv ](<./Palette-webRTCPanelRcv.md> "Palette:webRTCPanelRcv")• [Palette:xyScope ](<./Palette-xyScope.md> "Palette:xyScope")• [Thread Manager ](<./Thread_Manager.md> "Thread Manager")
