# Palette:logger

## 

Summary

**Starting with** the first build released publicly on the **2023.10k branch** , TouchDesigner now comes with its own Logger COMP. 

For more details about logging in TouchDesigner, please visit the [Logger](<./Logger.md> "Logger") page. 

The Logger COMP is a wrapper around the [Python Logging Library](<https://docs.python.org/3/library/logging.html>), and comes as an interface to add additional Loggers easily in your TouchDesigner projects, while relying (or not) on **the TDAppLogger internally shipping with TouchDesigner**. 

Logging can come at a performance cost when used inefficiently. Users should [visit this page](<https://docs.python.org/3/howto/logging-cookbook.html#logging-cookbook>) which applies to TouchDesigner as well. 

The easiest way to use the Logger COMP within your own components is by drag n dropping a Logger COMP in your custom component and by referencing the Logger COMP as a COMP Parameter to be used internally, or better, by assigning the Logger COMP to a member in a [custom python extension](<./Extensions.md> "Extensions"). 

From within your scripts, you can call`logger.Error('Some Error Message')`,`logger.Warning('Some Warning Message')`… etc. 

[See the Logger Extension page](<./Palette-logger_Ext.md> "Palette:logger Ext") to have a list of exposed members and methods. 

By default, the Logger COMP will be parented to an internal Logger that comes shipped with TouchDesigner, named TDAppLogger. 

For general purpose logging, users don’t have to use a new Logger COMP, you can simply use the`TDAppLogger`by accessing it using`op.TDResources.TDAppLogger`. Again, refer to [the Logger extension page](<./Palette-logger_Ext.md> "Palette:logger Ext") to get a better idea of which members and methods are exposed. 

If you rather have a more custom approach, or rely on the hierarchical structure of the Python logging library, then use the Logger COMP. 

Note that when tuning the Logger COMP parameters, it will often occur that a logger instance (read, the Python logger object) gets destroyed and re-created. Similarly, some Python logging handlers might be destroyed and re-created to follow the new Logger COMP parameters. 

Since builds **2023.31600+** , the Logger COMP, v2.6.2+, is always initializing a Logger object (from the logging library:`logging.Logger`). This is to avoid initialization issues where a Logger might be missing although part of the user network needs to log messages. Additionally, to assist the new [Thread Manager](<./Thread_Manager.md> "Thread Manager") coming in builds **2023.30k+** a QueueHandler is available at all time. The QueueHandler is the main handler on the Logger COMP, receiving log messages to be dispatched to additional handlers. Two base handlers are supported, a StreamHandler routing messages to the Textport, as well as a TimedRotatingFileHandler, logging messages to log files. New features are exposed for users to add their own handlers which will also get messages dispatched from the QueueHandler. [See the Logger Extension page](<./Palette-logger_Ext.md> "Palette:logger Ext") for details. 

If you are actively logging messages while tweaking those parameters, issues might occur. While not necessary for all cases, it is advised to turn off the Active parameter first. 

For advanced Python users, the actual Python Logger object is exposed via the`loggerCOMP.Logger`member. 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[Palette:logger Ext](<./Palette-logger_Ext.md> "Palette:logger Ext")

## 

Parameters - Settings Page

Active`Active`\- When the active flag is turned off, most logging messages will be silenced and log levels are ignored. 

Parent Logger`Parentlogger`\- The Logger COMP to which this Logger COMP is currently parented. Parenting allow for logging messages to be passed up to any handler associated with a parent. When using parenting, it is possible to see duplicates records in the textport if the records are being propagated as well as being logged to textport. 

Propagate to parent(s)`Propagate`\- When using parenting, use this toggle if you wish to prevent messages from being passed to the parent. 

Open Parameters Dialog`Openparametersdialog`\- Open a floating window of the parameters dialog. 

General Settings`Generalsettings`\- 

Origin`Origin`\- Reference a COMP for the logger to mention where the log messages are originating from. 

Log Level`Loglevel`\- ⊞ \- Filter level of logging messages. The selected level is included as well as all levels above. I.e. if Warning is selected, Warning and Error messages will be included while Info messages will be excluded. 
* INFO`INFO`-
* DEBUG`DEBUG`-
* WARNING`WARNING`-
* ERROR`ERROR`-
* CRITICAL`CRITICAL`-


Log App Errors (from Error DAT)`Logapperrors`\- Use an internal Error DAT which filters any messages matching the Origin and Log Level. 

Log to Textport`Logtotextport`\- When enabled, logging messages will be displayed in the textport. 

Log to Status Bar`Logtostatusbar`\- When enabled, logging messages will be displayed in the status bar. 

File Logger Settings`Fileloggersettings`\- 

Logger Name`Loggername`\- The name of the Logger instance. This is reflected in the logging messages when multiple loggers are passing messages to a parent and being processed by the same handler. 

Log to File`Logtofile`\- When enabled, logging messages will be written to a time rotated log file. 

Log Folder`Logfolder`\- Path to the folder in which the log files should be written. 

Open Log Folder`Openlogfolder`\- Open the folder to which the .log file is present. The folder opened isn't necesarily the folder set in the Log Folder parameter, if file logging is disabled but a parent logger with a file handler is assigned. 

Path To Log File`Pathtologfile`\- When a parameter of the current Logger COMP gets changed, it can have an impact on the current log file path. 

When the current logger doesn't have file logging turned on, it doesn't mean that the log messages are not passed to a file. The messages could be passed to a parent logger which itself will have a file handler. Internally the Logger COMP attempts to find the path to a parent logger file handler and the path would be filled automatically here. __

Add PID to file name`Addpidtofilename`\- This will add the current process PID to the file name. This can be useful to split log files originating from the same project but ran in multiple processes. 

Open Log File`Openlogfile`\- Open the current log file. Similarly to the Open Log Folder parameter, the log to file parameter doesn't have to be turned on to open the log file. A log file might be currently used by the Logger COMP if a handler is present on a parent logger. 

File Rotation`Filerotation`\- Number of backup files to be kept when rotating log. 

When`When`\- When (or the interval types): 'S' (Seconds), 'M' (Minutes), 'H' (Hours), and 'D' (Days) specify how often log files should be rolled over, they don't influence the calculation of the initial rollover time. 'W0'-'W6' (Weekday, Monday to Sunday) and 'midnight' can use the 'At Time' parameter to compute the initial rollover time. 

Interval`Interval`\- The interval, where the unit is the "When" parameter. I.e., if the 'When' parameter is set to be 'H', and the Interval is 24, it will effectively rotate files every 24 hours. Setting the 'When' parameter to be 'D' and the Interval to be 1 will have the same behaviour. 

At Time`Attime`\- In format HH:MM:SS. Only used for weekdays (W0-W6) or 'midnight' as 'When' parameter. 

Callback`Callback`\- 

Callback DAT`Callbackdat`\- A DAT with a onMessageLogged(info) method. 

Create Callback DAT`Createcallbackdat`\- Create a valid callback DAT from the template shipping with the COMP. 

Print Callbacks`Printcallbacks`\- Print the callback details to the textport. 

## 

Parameters - About Page

Help`Help`\- 

Version`Version`\- 

.tox Save Build`Toxsavebuild`\- 

TouchDesigner Build: Latest\nwikieditor2025.300002023.11280

Palette  
---  
[Palette ](<./Palette.md> "Palette")• [Palette:arcBallCamera ](<./Palette-arcBallCamera.md> "Palette:arcBallCamera")• [Palette:arcBallGeometry ](<./Palette-arcBallGeometry.md> "Palette:arcBallGeometry")• [Palette:audioAnalysis ](<./Palette-audioAnalysis.md> "Palette:audioAnalysis")• [Palette:audioSet ](<./Palette-audioSet.md> "Palette:audioSet")• [Palette:autoMediaPlayer ](<./Palette-autoMediaPlayer.md> "Palette:autoMediaPlayer")• [Palette:battery ](<./Palette-battery.md> "Palette:battery")• [Palette:bitwigClip ](<./Palette-bitwigClip.md> "Palette:bitwigClip")• [Palette:bitwigClipSlot ](<./Palette-bitwigClipSlot.md> "Palette:bitwigClipSlot")• [Palette:bitwigDeviceRemotes ](<./Palette-bitwigDeviceRemotes.md> "Palette:bitwigDeviceRemotes")• [Palette:bitwigMain ](<./Palette-bitwigMain.md> "Palette:bitwigMain")• [Palette:bitwigNote ](<./Palette-bitwigNote.md> "Palette:bitwigNote")• [Palette:bitwigProjectRemotes ](<./Palette-bitwigProjectRemotes.md> "Palette:bitwigProjectRemotes")• [Palette:bitwigRemotesDevice ](<./Palette-bitwigRemotesDevice.md> "Palette:bitwigRemotesDevice")• [Palette:bitwigRemotesProject ](<./Palette-bitwigRemotesProject.md> "Palette:bitwigRemotesProject")• [Palette:bitwigRemotesTrack ](<./Palette-bitwigRemotesTrack.md> "Palette:bitwigRemotesTrack")• [Palette:bitwigSelect ](<./Palette-bitwigSelect.md> "Palette:bitwigSelect")• [Palette:bitwigSong ](<./Palette-bitwigSong.md> "Palette:bitwigSong")• [Palette:bitwigTrack ](<./Palette-bitwigTrack.md> "Palette:bitwigTrack")• [Palette:bitwigTrackRemotes ](<./Palette-bitwigTrackRemotes.md> "Palette:bitwigTrackRemotes")• [Palette:blendModes ](<./Palette-blendModes.md> "Palette:blendModes")• [Palette:bloom ](<./Palette-bloom.md> "Palette:bloom")• [Palette:camera ](<./Palette-camera.md> "Palette:camera")• [Palette:cameraBrowser ](<./Palette-cameraBrowser.md> "Palette:cameraBrowser")• [Palette:cameraViewport ](<./Palette-cameraViewport.md> "Palette:cameraViewport")• [Palette:camSchnappr ](<./Palette-camSchnappr.md> "Palette:camSchnappr")• [Palette:changeColor ](<./Palette-changeColor.md> "Palette:changeColor")• [Palette:changeToColor ](<./Palette-changeToColor.md> "Palette:changeToColor")• [Palette:checker ](<./Palette-checker.md> "Palette:checker")• [Palette:chromaKey ](<./Palette-chromaKey.md> "Palette:chromaKey")• [Palette:colorThreshold ](<./Palette-colorThreshold.md> "Palette:colorThreshold")• [Palette:compareComp ](<./Palette-compareComp.md> "Palette:compareComp")• [Palette:convolve ](<./Palette-convolve.md> "Palette:convolve")• [Experimental:Palette:cornerPinPOP ](</index.php?title=Experimental:Palette:cornerPinPOP&action=edit&redlink=1> "Experimental:Palette:cornerPinPOP \(page does not exist\)")• [Palette:cornerPinSOP ](<./Palette-cornerPinSOP.md> "Palette:cornerPinSOP")• [Palette:cppParsTemplateGen ](<./Palette-cppParsTemplateGen.md> "Palette:cppParsTemplateGen")• [Palette:customAttributes ](<./Palette-customAttributes.md> "Palette:customAttributes")• [Palette:debugControl ](<./Palette-debugControl.md> "Palette:debugControl")• [Palette:dent ](<./Palette-dent.md> "Palette:dent")• [Palette:depthExtract ](<./Palette-depthExtract.md> "Palette:depthExtract")• [Palette:depthProjection ](<./Palette-depthProjection.md> "Palette:depthProjection")• [Palette:dilate ](<./Palette-dilate.md> "Palette:dilate")• [Experimental:Palette:domeViewer ](</index.php?title=Experimental:Palette:domeViewer&action=edit&redlink=1> "Experimental:Palette:domeViewer \(page does not exist\)")• [Palette:encoder ](<./Palette-encoder.md> "Palette:encoder")• [Palette:equalizer ](<./Palette-equalizer.md> "Palette:equalizer")• [Palette:feedback ](<./Palette-feedback.md> "Palette:feedback")• [Palette:feedbackEdge ](<./Palette-feedbackEdge.md> "Palette:feedbackEdge")• [Palette:firmata ](<./Palette-firmata.md> "Palette:firmata")• [Palette:gal ](<./Palette-gal.md> "Palette:gal")• [Palette:geoPanel ](<./Palette-geoPanel.md> "Palette:geoPanel")• [Palette:gestureCapture ](<./Palette-gestureCapture.md> "Palette:gestureCapture")• [Palette:graphPlot ](<./Palette-graphPlot.md> "Palette:graphPlot")• [Palette:histogram ](<./Palette-histogram.md> "Palette:histogram")• [Palette:hsvBlur ](<./Palette-hsvBlur.md> "Palette:hsvBlur")• [Palette:imageSearch ](<./Palette-imageSearch.md> "Palette:imageSearch")• [Palette:julia ](<./Palette-julia.md> "Palette:julia")• [Palette:kantanMapper ](<./Palette-kantanMapper.md> "Palette:kantanMapper")• [Palette:kinectCalibration ](<./Palette-kinectCalibration.md> "Palette:kinectCalibration")• [Palette:kinectPointcloud ](<./Palette-kinectPointcloud.md> "Palette:kinectPointcloud")• [Palette:leapPaint ](<./Palette-leapPaint.md> "Palette:leapPaint")• [Palette:lightTunnel ](<./Palette-lightTunnel.md> "Palette:lightTunnel")• Palette:logger • [Experimental:Palette:logger ](</index.php?title=Experimental:Palette:logger&action=edit&redlink=1> "Experimental:Palette:logger \(page does not exist\)")• [Palette:mandelbrot ](<./Palette-mandelbrot.md> "Palette:mandelbrot")• [Palette:materialDesignIcons ](<./Palette-materialDesignIcons.md> "Palette:materialDesignIcons")• [Palette:mesh ](<./Palette-mesh.md> "Palette:mesh")• [Palette:monochrome ](<./Palette-monochrome.md> "Palette:monochrome")• [Palette:motionSense ](<./Palette-motionSense.md> "Palette:motionSense")• [Palette:movieEngine ](<./Palette-movieEngine.md> "Palette:movieEngine")• [Palette:moviePlayer ](<./Palette-moviePlayer.md> "Palette:moviePlayer")• [Palette:moviePlaylist ](<./Palette-moviePlaylist.md> "Palette:moviePlaylist")• [Palette:multiLevel ](<./Palette-multiLevel.md> "Palette:multiLevel")• [Palette:multiMix ](<./Palette-multiMix.md> "Palette:multiMix")• [Palette:noise ](<./Palette-noise.md> "Palette:noise")• [Palette:onScreenKeyboard ](<./Palette-onScreenKeyboard.md> "Palette:onScreenKeyboard")• [Palette:operatorPath ](<./Palette-operatorPath.md> "Palette:operatorPath")• [Palette:opticalFlow ](<./Palette-opticalFlow.md> "Palette:opticalFlow")• [Palette:particlesGpu ](<./Palette-particlesGpu.md> "Palette:particlesGpu")• [Palette:pixelate ](<./Palette-pixelate.md> "Palette:pixelate")• [Palette:pixelRelocator ](<./Palette-pixelRelocator.md> "Palette:pixelRelocator")• [Palette:pointGenerator ](<./Palette-pointGenerator.md> "Palette:pointGenerator")• [Palette:pointillize ](<./Palette-pointillize.md> "Palette:pointillize")• [Palette:pointMerge ](<./Palette-pointMerge.md> "Palette:pointMerge")• [Palette:pointRender ](<./Palette-pointRender.md> "Palette:pointRender")• [Palette:pointRepack ](<./Palette-pointRepack.md> "Palette:pointRepack")• [Palette:pointTransform ](<./Palette-pointTransform.md> "Palette:pointTransform")• [Palette:pointWeight ](<./Palette-pointWeight.md> "Palette:pointWeight")• [Palette:popDialog ](<./Palette-popDialog.md> "Palette:popDialog")• [Experimental:Palette:popDialog ](</index.php?title=Experimental:Palette:popDialog&action=edit&redlink=1> "Experimental:Palette:popDialog \(page does not exist\)")• [Palette:probe ](<./Palette-probe.md> "Palette:probe")• [Palette:projectorBlend ](<./Palette-projectorBlend.md> "Palette:projectorBlend")• [Palette:pushPins ](<./Palette-pushPins.md> "Palette:pushPins")• [Palette:puzzle ](<./Palette-puzzle.md> "Palette:puzzle")• [Palette:quadReproject ](<./Palette-quadReproject.md> "Palette:quadReproject")• [Palette:radialBlur ](<./Palette-radialBlur.md> "Palette:radialBlur")• [Palette:recorder ](<./Palette-recorder.md> "Palette:recorder")• [Experimental:Palette:recorder ](</index.php?title=Experimental:Palette:recorder&action=edit&redlink=1> "Experimental:Palette:recorder \(page does not exist\)")• [Palette:remotePanel ](<./Palette-remotePanel.md> "Palette:remotePanel")• [Palette:rgbaBlur ](<./Palette-rgbaBlur.md> "Palette:rgbaBlur")• [Palette:rgbaDelay ](<./Palette-rgbaDelay.md> "Palette:rgbaDelay")• [Palette:rgbContrast ](<./Palette-rgbContrast.md> "Palette:rgbContrast")• [Palette:sceneChanger ](<./Palette-sceneChanger.md> "Palette:sceneChanger")• [Palette:search ](<./Palette-search.md> "Palette:search")• [Palette:searchReplace ](<./Palette-searchReplace.md> "Palette:searchReplace")• [Palette:sharpen ](<./Palette-sharpen.md> "Palette:sharpen")• [Palette:sickEngine ](<./Palette-sickEngine.md> "Palette:sickEngine")• [Palette:signalingClient ](<./Palette-signalingClient.md> "Palette:signalingClient")• [Palette:signalingServer ](<./Palette-signalingServer.md> "Palette:signalingServer")• [Palette:softenAlpha ](<./Palette-softenAlpha.md> "Palette:softenAlpha")• [Palette:solarize ](<./Palette-solarize.md> "Palette:solarize")• [Palette:sopRender ](<./Palette-sopRender.md> "Palette:sopRender")• [Palette:splitter ](<./Palette-splitter.md> "Palette:splitter")• [Palette:stitcher ](<./Palette-stitcher.md> "Palette:stitcher")• [Palette:stoner ](<./Palette-stoner.md> "Palette:stoner")• [Palette:superFormula ](<./Palette-superFormula.md> "Palette:superFormula")• [Palette:SVG ](<./Palette-SVG.md> "Palette:SVG")• [Palette:sweetSpot ](<./Palette-sweetSpot.md> "Palette:sweetSpot")• [Palette:sweetSpotPreviz ](<./Palette-sweetSpotPreviz.md> "Palette:sweetSpotPreviz")• [Palette:synchroCache ](<./Palette-synchroCache.md> "Palette:synchroCache")• [Palette:synchroClient ](<./Palette-synchroClient.md> "Palette:synchroClient")• [Palette:synchroFrameIn ](<./Palette-synchroFrameIn.md> "Palette:synchroFrameIn")• [Palette:synchroFrameOut ](<./Palette-synchroFrameOut.md> "Palette:synchroFrameOut")• [Palette:synchroNDIIn ](<./Palette-synchroNDIIn.md> "Palette:synchroNDIIn")• [Palette:synchroSDIIn ](<./Palette-synchroSDIIn.md> "Palette:synchroSDIIn")• [Palette:synchroVideoOut ](<./Palette-synchroVideoOut.md> "Palette:synchroVideoOut")• [Palette:tdBitwigPackage ](<./Palette-tdBitwigPackage.md> "Palette:tdBitwigPackage")• [Experimental:Palette:tdPyEnvManager ](</index.php?title=Experimental:Palette:tdPyEnvManager&action=edit&redlink=1> "Experimental:Palette:tdPyEnvManager \(page does not exist\)")• [Palette:TDVR ](<./Palette-TDVR.md> "Palette:TDVR")• [Palette:testGrid ](<./Palette-testGrid.md> "Palette:testGrid")• [Experimental:Palette:threadManagerClient ](</index.php?title=Experimental:Palette:threadManagerClient&action=edit&redlink=1> "Experimental:Palette:threadManagerClient \(page does not exist\)")• [Experimental:Palette:threadsMonitor ](</index.php?title=Experimental:Palette:threadsMonitor&action=edit&redlink=1> "Experimental:Palette:threadsMonitor \(page does not exist\)")• [Palette:transitMap ](<./Palette-transitMap.md> "Palette:transitMap")• [Palette:twirl ](<./Palette-twirl.md> "Palette:twirl")• [Palette:vectorScope ](<./Palette-vectorScope.md> "Palette:vectorScope")• [Palette:virtualFile ](<./Palette-virtualFile.md> "Palette:virtualFile")• [Palette:waveformMonitor ](<./Palette-waveformMonitor.md> "Palette:waveformMonitor")• [Palette:webBrowser ](<./Palette-webBrowser.md> "Palette:webBrowser")• [Palette:webRTC ](<./Palette-webRTC.md> "Palette:webRTC")• [Palette:webRTCPanel ](<./Palette-webRTCPanel.md> "Palette:webRTCPanel")• [Palette:webRTCPanelRcv ](<./Palette-webRTCPanelRcv.md> "Palette:webRTCPanelRcv")• [Palette:xyScope ](<./Palette-xyScope.md> "Palette:xyScope")• [Experimental:Thread Manager ](</index.php?title=Experimental:Thread_Manager&action=edit&redlink=1> "Experimental:Thread Manager \(page does not exist\)")
