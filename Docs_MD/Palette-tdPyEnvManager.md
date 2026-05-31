# Palette:tdPyEnvManager

##   
  
Summary

The TDPyEnvManager is a custom TouchDesigner component that helps manage [Python environments](<https://docs.python.org/3/library/venv.html>) as well as [Conda environments](<https://docs.conda.io/en/latest/>) and helps TouchDesigner users and developers integrate easily and efficiently third party Python libraries that are installed in an external environment. 

Users can rely on this component to create, activate, and manage Python vEnvs and Conda environments. Users can easily get to the activated environment's CLI and use`pip`or`conda`commands to install packages. Users can also export the environment to a`requirements.txt`or`environment.yml`file, and create a new environment from it. 

Selected environments are added to the TouchDesigner Python path and packages installed in the environment are available to TouchDesigner. 

Additionally, the Conda Env mode allows for users to search for environments available globally on the system, granted a valid Conda installation is found and the environments are matching the Python version of the TouchDesigner installation. 

Users that wish to automate the creation of environments can use the TDPyEnvManagerHelper as a CLI. More details at [TDPyEnvManagerHelper](<./TDPyEnvManagerHelper.md> "TDPyEnvManagerHelper"). 

> 💡 Support for [UV](<https://docs.astral.sh/uv>) can be added after creating a Python vEnv and activating the environment through the Open CLI pulse parameter. In the CLI, type`pip install uv`.

The TDPyEnvManagerHelper is initialized during TouchDesigner startup. If a`TDPyEnvManagerContext.json`file is found and the environment registered in the context file is valid, then the environment will be added to the Python search path before any TouchDesigner COMP cooks and any custom extensions initialized. 

The context content is of the following format: 
[code] 
    {
        "active": true,
        "mode": "Python vEnv",
        "envName": "TDPyEnvManager_vEnv",
        "installPath": "E:\\_DERIVATIVE\\Gitlab\\TDPyEnvManager",
        "pythonVersion": "3.11",
        "pythonVersionNoDot": "311"
    }
    
[/code]

When setting up your TDPyEnvManager and side environment, you can safely ignore issues from custom components. When your environment is setup properly and you installed the required dependencies, restart TouchDesigner and any import issue should be fixed. 

### Tips

When developing using VSCode, you can setup your code-workspace to load both TouchDesigner TDI library as well as the libraries installed in the sideloaded environment: 
[code] 
    {
    	"folders": [
    		{
    			"path": "."
    		}
    	],
    	"settings": {
    		"python.defaultInterpreterPath": "C:\\Program Files\\Derivative\\TouchDesigner.2023.32465\\bin\\python.exe",
    		"python.analysis.autoSearchPaths": true,
    		"python.autoComplete.extraPaths": [
    			"C:\\Program Files\\Derivative\\TouchDesigner.2023.32465\\bin\\python\\Lib\\site-packages",
    			".\\scripts",
    			".\\TDDepthAnythingHF_vEnv\\Lib\\site-packages",
    		],
    		"python.analysis.extraPaths": [
    			"C:\\Program Files\\Derivative\\TouchDesigner.2023.32465\\bin\\python\\Lib\\site-packages",
    			".\\scripts",
    			".\\TDDepthAnythingHF_vEnv\\Lib\\site-packages",
    		],
    	}
    }
    
[/code]

In the example above, the interpreter is pointing to TouchDesigner’s own python binary and we added TouchDesigner`site-packages`as well as a Python vEnv plus a relative`scripts`folder. 

### Note
* Sideloading Python environments and third party packages is at your own risk and can cause instabilities. For more details, head to [https://docs.derivative.ca/Python](<./Python.md>)
  * When using the Conda mode, users silently install [Miniconda](<https://www.anaconda.com/docs/getting-started/miniconda/main>) and agree to the [Anaconda Inc. ToS](<https://legal.anaconda.com/policies/en/>). While the TDPyEnvManager locks on [`conda-forge`channels](<https://conda-forge.org/docs/user/introduction/>) when first installing Miniconda and creating environments, it is possible that an external configuration on the user's machine force`conda install`calls to install third party packages on the conda default channels. The default channel is subject to Anaconda Inc. ToS. More details regarding the license of the default channel at: <https://www.anaconda.com/blog/is-conda-free>


[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[Palette:tdPyEnvManager Ext](<./Palette-tdPyEnvManager_Ext.md> "Palette:tdPyEnvManager Ext")

## 

Parameters - TDPyEnvManager Page

General`General`\- 

Active`Active`\- Enable or disable the startup and initialization process of the component. Toggling active off avoid detection of a matching vEnv or conda env during startup or initialization of the component. This can be useful when debugging and prototyping but should be kept turned on for project delivery. 

Open Parameters Dialog`Openparametersdialog`\- Open a floating window of internal logger parameters dialog. 

Status`Status`\- The current status of the component. 

Mode`Mode`\- ⊞ \- The mode in which the component should run. Python vEnv are plug n play and are create relative to the .toe file with a name matching the parent folder. Conda envs require downloading and installing Miniconda if a valid Conda Install Folder is not specified upon creation of the conda env. 
* Python vEnv`Python vEnv`-
* Conda Env`Conda Env`-


Reset`Reset`\- Reset the component internal states and trigger the post init sequence. 

Restart`Restart`\- Restart TouchDesigner. While the component is trying its best at keeping the PATH and other variables clean when changing mode, creating environments... etc, restarting will guarantee a clean state using the latest settings. This will restart TouchDesigner and prompt the user for saving if unsaved changes are found. External components, if any, should be saved manually. 

Python vEnv`Pythonvenv`\- 

Create vEnv`Createvenv`\- If no existing Python vEnv is found relative to the .toe file, create a vEnv using TouchDesigner. The vEnv folder will be next to the .toe file and be named after the parent folder name followed by '_vEnv'. i.e. If the parent folder is named 'Banana', the vEnv folder will be 'Banana_vEnv'. 

Export requirements.txt`Exportrequirementstxt`\- Export a requirements.txt file with all unique packages currently installed in the vEnv, that are not part of the TouchDesigner build site-packages. **Note: This is not an optimal requirements.txt file.** You need to go through it manually and curate it to avoid setting too many version restrictions and possibly add a`--extra-index-url https://some.url`line within the requirements.txt file. 

Create from requirements.txt`Createfromrequirementstxt`\- If a requirements.txt file is available next to the .toe file in which this TDPyEnvManager instance is used, create a vEnv and install all the packages in the requirements.txt file. If the vEnv already exists, install the packages in the existing vEnv. 

Conda Env`Condaenv`\- 

Conda Install Folder`Condainstallfolder`\- The root folder of an exiting Anaconda or Miniconda installation, or the path where a Miniconda installation should be created. A Miniconda installation relative to the .toe file is a fast and efficient setup to prototype, develop and ship a project relying on a Miniconda environment. 

Environment`Environment`\- ⊞ \- The name of the environment to be created, or the name of an already existing environment in that installation. An environment name followed by a star (*) is a global environment. See parameter "Include global" for details. The environment selected, when / if exisiting, will be added to the PATH and its packages will be available to TouchDesigner. 
* TDEnv`TDEnv`-


Create Conda Env`Createcondaenv`\- Create a conda environment of the name matching the parameter Environment, in the conda install folder, if a valid conda installation is found. Otherwise, install Miniconda and create the environment of the name matching the parameter Environment in the freshly installed Miniconda installation. The created conda envs are using the conda-forge channels by default. 

Keep Conda Installer`Keepcondainstaller`\- Keep the Miniconda installer once downloaded. 

Include global`Includeglobal`\- When toggled on, include all the publicly available conda environments of the machine. Environments that are created in the conda installation specified in the Conda Install Folder parameter are always listed in the Environment parameter. The environments that are found using the conda API and are not in the specified conda install folder will be followed by a star (*). 

Export environment.yml`Exportenvironmentyml`\- Export an environment.yml file with all unique packages currently installed in the selected conda environment. This include default packages, pip packages, conda specific packages and the python version the environment was created with as well as the conda channels used for that environment. 

Create from environment.yml`Createfromenvironmentyml`\- If an environment.yml file is available next to the .toe file in which this TDPyEnvManager instance is used, create a conda env and install all the packages listed in the environment.yml file. If the environment already exists, install the packages in the existing environment. 

Refresh`Refresh`\- Refresh the list of environments listed in Environment parameter drop down. Can be useful if an environment was created through the CLI or outside of the TouchDesigner context. 

Extra`Extra`\- 

Open CLI`Opencli`\- Open a CLI and activate the environment, whether it's a Python vEnv or a conda environment. You can use pip (in both Python vEnv and conda) and conda install as well as other environment specific commands. 

## 

Parameters - About Page

Help`Help`\- 

Version`Version`\- 

.tox Save Build`Toxsavebuild`\- 

## 

Operator Outputs
* Output 0 -


TouchDesigner Build: Latest\nwikieditor2025.30000

Palette  
---  
[Palette ](<./Palette.md> "Palette")• [Palette:arcBallCamera ](<./Palette-arcBallCamera.md> "Palette:arcBallCamera")• [Palette:arcBallGeometry ](<./Palette-arcBallGeometry.md> "Palette:arcBallGeometry")• [Palette:audioAnalysis ](<./Palette-audioAnalysis.md> "Palette:audioAnalysis")• [Palette:audioSet ](<./Palette-audioSet.md> "Palette:audioSet")• [Palette:autoMediaPlayer ](<./Palette-autoMediaPlayer.md> "Palette:autoMediaPlayer")• [Palette:battery ](<./Palette-battery.md> "Palette:battery")• [Palette:bitwigClip ](<./Palette-bitwigClip.md> "Palette:bitwigClip")• [Palette:bitwigClipSlot ](<./Palette-bitwigClipSlot.md> "Palette:bitwigClipSlot")• [Palette:bitwigDeviceRemotes ](<./Palette-bitwigDeviceRemotes.md> "Palette:bitwigDeviceRemotes")• [Palette:bitwigMain ](<./Palette-bitwigMain.md> "Palette:bitwigMain")• [Palette:bitwigNote ](<./Palette-bitwigNote.md> "Palette:bitwigNote")• [Palette:bitwigProjectRemotes ](<./Palette-bitwigProjectRemotes.md> "Palette:bitwigProjectRemotes")• [Palette:bitwigRemotesDevice ](<./Palette-bitwigRemotesDevice.md> "Palette:bitwigRemotesDevice")• [Palette:bitwigRemotesProject ](<./Palette-bitwigRemotesProject.md> "Palette:bitwigRemotesProject")• [Palette:bitwigRemotesTrack ](<./Palette-bitwigRemotesTrack.md> "Palette:bitwigRemotesTrack")• [Palette:bitwigSelect ](<./Palette-bitwigSelect.md> "Palette:bitwigSelect")• [Palette:bitwigSong ](<./Palette-bitwigSong.md> "Palette:bitwigSong")• [Palette:bitwigTrack ](<./Palette-bitwigTrack.md> "Palette:bitwigTrack")• [Palette:bitwigTrackRemotes ](<./Palette-bitwigTrackRemotes.md> "Palette:bitwigTrackRemotes")• [Palette:blendModes ](<./Palette-blendModes.md> "Palette:blendModes")• [Palette:bloom ](<./Palette-bloom.md> "Palette:bloom")• [Palette:camera ](<./Palette-camera.md> "Palette:camera")• [Palette:cameraBrowser ](<./Palette-cameraBrowser.md> "Palette:cameraBrowser")• [Palette:cameraViewport ](<./Palette-cameraViewport.md> "Palette:cameraViewport")• [Palette:camSchnappr ](<./Palette-camSchnappr.md> "Palette:camSchnappr")• [Palette:changeColor ](<./Palette-changeColor.md> "Palette:changeColor")• [Palette:changeToColor ](<./Palette-changeToColor.md> "Palette:changeToColor")• [Palette:checker ](<./Palette-checker.md> "Palette:checker")• [Palette:chromaKey ](<./Palette-chromaKey.md> "Palette:chromaKey")• [Palette:colorThreshold ](<./Palette-colorThreshold.md> "Palette:colorThreshold")• [Palette:compareComp ](<./Palette-compareComp.md> "Palette:compareComp")• [Palette:convolve ](<./Palette-convolve.md> "Palette:convolve")• [Palette:cornerPinPOP ](<./Palette-cornerPinPOP.md> "Palette:cornerPinPOP")• [Palette:cornerPinSOP ](<./Palette-cornerPinSOP.md> "Palette:cornerPinSOP")• [Palette:cppParsTemplateGen ](<./Palette-cppParsTemplateGen.md> "Palette:cppParsTemplateGen")• [Palette:customAttributes ](<./Palette-customAttributes.md> "Palette:customAttributes")• [Palette:debugControl ](<./Palette-debugControl.md> "Palette:debugControl")• [Palette:dent ](<./Palette-dent.md> "Palette:dent")• [Palette:depthExtract ](<./Palette-depthExtract.md> "Palette:depthExtract")• [Palette:depthProjection ](<./Palette-depthProjection.md> "Palette:depthProjection")• [Palette:dilate ](<./Palette-dilate.md> "Palette:dilate")• [Palette:domeViewer ](<./Palette-domeViewer.md> "Palette:domeViewer")• [Palette:encoder ](<./Palette-encoder.md> "Palette:encoder")• [Palette:equalizer ](<./Palette-equalizer.md> "Palette:equalizer")• [Palette:feedback ](<./Palette-feedback.md> "Palette:feedback")• [Palette:feedbackEdge ](<./Palette-feedbackEdge.md> "Palette:feedbackEdge")• [Palette:firmata ](<./Palette-firmata.md> "Palette:firmata")• [Palette:gal ](<./Palette-gal.md> "Palette:gal")• [Palette:geoPanel ](<./Palette-geoPanel.md> "Palette:geoPanel")• [Palette:gestureCapture ](<./Palette-gestureCapture.md> "Palette:gestureCapture")• [Palette:graphPlot ](<./Palette-graphPlot.md> "Palette:graphPlot")• [Palette:histogram ](<./Palette-histogram.md> "Palette:histogram")• [Palette:hsvBlur ](<./Palette-hsvBlur.md> "Palette:hsvBlur")• [Palette:imageSearch ](<./Palette-imageSearch.md> "Palette:imageSearch")• [Palette:julia ](<./Palette-julia.md> "Palette:julia")• [Palette:kantanMapper ](<./Palette-kantanMapper.md> "Palette:kantanMapper")• [Palette:kinectCalibration ](<./Palette-kinectCalibration.md> "Palette:kinectCalibration")• [Palette:kinectPointcloud ](<./Palette-kinectPointcloud.md> "Palette:kinectPointcloud")• [Palette:leapPaint ](<./Palette-leapPaint.md> "Palette:leapPaint")• [Palette:lightTunnel ](<./Palette-lightTunnel.md> "Palette:lightTunnel")• [Palette:logger ](<./Palette-logger.md> "Palette:logger")• [Palette:mandelbrot ](<./Palette-mandelbrot.md> "Palette:mandelbrot")• [Palette:materialDesignIcons ](<./Palette-materialDesignIcons.md> "Palette:materialDesignIcons")• [Palette:mesh ](<./Palette-mesh.md> "Palette:mesh")• [Palette:monochrome ](<./Palette-monochrome.md> "Palette:monochrome")• [Palette:motionSense ](<./Palette-motionSense.md> "Palette:motionSense")• [Palette:movieEngine ](<./Palette-movieEngine.md> "Palette:movieEngine")• [Palette:moviePlayer ](<./Palette-moviePlayer.md> "Palette:moviePlayer")• [Palette:moviePlaylist ](<./Palette-moviePlaylist.md> "Palette:moviePlaylist")• [Palette:multiLevel ](<./Palette-multiLevel.md> "Palette:multiLevel")• [Palette:multiMix ](<./Palette-multiMix.md> "Palette:multiMix")• [Palette:noise ](<./Palette-noise.md> "Palette:noise")• [Palette:onScreenKeyboard ](<./Palette-onScreenKeyboard.md> "Palette:onScreenKeyboard")• [Palette:operatorPath ](<./Palette-operatorPath.md> "Palette:operatorPath")• [Palette:opticalFlow ](<./Palette-opticalFlow.md> "Palette:opticalFlow")• [Palette:particlesGpu ](<./Palette-particlesGpu.md> "Palette:particlesGpu")• [Palette:pixelate ](<./Palette-pixelate.md> "Palette:pixelate")• [Palette:pixelRelocator ](<./Palette-pixelRelocator.md> "Palette:pixelRelocator")• [Palette:pointGenerator ](<./Palette-pointGenerator.md> "Palette:pointGenerator")• [Palette:pointillize ](<./Palette-pointillize.md> "Palette:pointillize")• [Palette:pointMerge ](<./Palette-pointMerge.md> "Palette:pointMerge")• [Palette:pointRender ](<./Palette-pointRender.md> "Palette:pointRender")• [Palette:pointRepack ](<./Palette-pointRepack.md> "Palette:pointRepack")• [Palette:pointTransform ](<./Palette-pointTransform.md> "Palette:pointTransform")• [Palette:pointWeight ](<./Palette-pointWeight.md> "Palette:pointWeight")• [Palette:popDialog ](<./Palette-popDialog.md> "Palette:popDialog")• [Palette:probe ](<./Palette-probe.md> "Palette:probe")• [Palette:projectorBlend ](<./Palette-projectorBlend.md> "Palette:projectorBlend")• [Palette:pushPins ](<./Palette-pushPins.md> "Palette:pushPins")• [Palette:puzzle ](<./Palette-puzzle.md> "Palette:puzzle")• [Palette:quadReproject ](<./Palette-quadReproject.md> "Palette:quadReproject")• [Palette:radialBlur ](<./Palette-radialBlur.md> "Palette:radialBlur")• [Palette:recorder ](<./Palette-recorder.md> "Palette:recorder")• [Palette:remotePanel ](<./Palette-remotePanel.md> "Palette:remotePanel")• [Palette:rgbaBlur ](<./Palette-rgbaBlur.md> "Palette:rgbaBlur")• [Palette:rgbaDelay ](<./Palette-rgbaDelay.md> "Palette:rgbaDelay")• [Palette:rgbContrast ](<./Palette-rgbContrast.md> "Palette:rgbContrast")• [Palette:sceneChanger ](<./Palette-sceneChanger.md> "Palette:sceneChanger")• [Palette:search ](<./Palette-search.md> "Palette:search")• [Palette:searchReplace ](<./Palette-searchReplace.md> "Palette:searchReplace")• [Palette:sharpen ](<./Palette-sharpen.md> "Palette:sharpen")• [Palette:sickEngine ](<./Palette-sickEngine.md> "Palette:sickEngine")• [Palette:signalingClient ](<./Palette-signalingClient.md> "Palette:signalingClient")• [Palette:signalingServer ](<./Palette-signalingServer.md> "Palette:signalingServer")• [Palette:softenAlpha ](<./Palette-softenAlpha.md> "Palette:softenAlpha")• [Palette:solarize ](<./Palette-solarize.md> "Palette:solarize")• [Palette:sopRender ](<./Palette-sopRender.md> "Palette:sopRender")• [Palette:splitter ](<./Palette-splitter.md> "Palette:splitter")• [Palette:stitcher ](<./Palette-stitcher.md> "Palette:stitcher")• [Palette:stoner ](<./Palette-stoner.md> "Palette:stoner")• [Palette:superFormula ](<./Palette-superFormula.md> "Palette:superFormula")• [Palette:SVG ](<./Palette-SVG.md> "Palette:SVG")• [Palette:sweetSpot ](<./Palette-sweetSpot.md> "Palette:sweetSpot")• [Palette:sweetSpotPreviz ](<./Palette-sweetSpotPreviz.md> "Palette:sweetSpotPreviz")• [Palette:synchroCache ](<./Palette-synchroCache.md> "Palette:synchroCache")• [Palette:synchroClient ](<./Palette-synchroClient.md> "Palette:synchroClient")• [Palette:synchroFrameIn ](<./Palette-synchroFrameIn.md> "Palette:synchroFrameIn")• [Palette:synchroFrameOut ](<./Palette-synchroFrameOut.md> "Palette:synchroFrameOut")• [Palette:synchroNDIIn ](<./Palette-synchroNDIIn.md> "Palette:synchroNDIIn")• [Palette:synchroSDIIn ](<./Palette-synchroSDIIn.md> "Palette:synchroSDIIn")• [Palette:synchroVideoOut ](<./Palette-synchroVideoOut.md> "Palette:synchroVideoOut")• [Palette:tdBitwigPackage ](<./Palette-tdBitwigPackage.md> "Palette:tdBitwigPackage")• Palette:tdPyEnvManager • [Palette:TDVR ](<./Palette-TDVR.md> "Palette:TDVR")• [Palette:testGrid ](<./Palette-testGrid.md> "Palette:testGrid")• [Palette:threadManagerClient ](<./Palette-threadManagerClient.md> "Palette:threadManagerClient")• [Palette:threadsMonitor ](<./Palette-threadsMonitor.md> "Palette:threadsMonitor")• [Palette:transitMap ](<./Palette-transitMap.md> "Palette:transitMap")• [Palette:twirl ](<./Palette-twirl.md> "Palette:twirl")• [Palette:vectorScope ](<./Palette-vectorScope.md> "Palette:vectorScope")• [Palette:virtualFile ](<./Palette-virtualFile.md> "Palette:virtualFile")• [Palette:waveformMonitor ](<./Palette-waveformMonitor.md> "Palette:waveformMonitor")• [Palette:webBrowser ](<./Palette-webBrowser.md> "Palette:webBrowser")• [Palette:webRTC ](<./Palette-webRTC.md> "Palette:webRTC")• [Palette:webRTCPanel ](<./Palette-webRTCPanel.md> "Palette:webRTCPanel")• [Palette:webRTCPanelRcv ](<./Palette-webRTCPanelRcv.md> "Palette:webRTCPanelRcv")• [Palette:xyScope ](<./Palette-xyScope.md> "Palette:xyScope")• [Thread Manager ](<./Thread_Manager.md> "Thread Manager")
