# Summary  
  
The **searchReplace** Component lets you search and (optionally) replace text in operators. The replace operation is **undoable**. 

It will search and optionally replace all text in DATs, operator names, parameter values/expressions/bind expressions, custom parameter names, custom parameter menu items, custom parameter page names, and fieldCOMP text. 

To search a single operator, or a component recursively, set the **`Searchinop`** parameter. The first input allows you to provide a table of operators (`**path**`column) to search non-recursively. The second input allows you to provide a table of multiple search/replace string options in`**search**`and`**replace**`columns. 

# Parameters

## Search/Replace

**Version**`Version`\- Component version number. 

**Help**`Help`\- Open this help page. 
* * *

**Search In OP**`Searchinop`\- Operator to search inside. All children of components will be searched recursively. 

**Search String**`Searchstring`\- The string to search for. 

**Replace String**`Replacestring`\- The string to replace searched string with. 
* * *

**Go**`Go`\- Perform the chosen operation. 

**Operation**`Operation`\- Choose`Search Only`or`Search and Replace`. 
* * *

**Case Sensitive**`Casesensitive`\- Case sensitive search. 

**Whole Words**`Wholewords`\- Look for search string only when it is not part of a larger word. Any non alpha-numeric characters are considered word boundaries. 

    Example: Searching for 'par' with Whole Words on will find`me.par.limit`but will not find`parent`**Regular Expressions**`Regularexpressions`\- When on, search string will be processed as a regular expression. 

## Filters

**Operator Type Filter**`Operatortypefilter`\- Only operators of the given Python class will be displayed. For example,`DAT`will show all DAT types and`panelexecDAT`will show only Panel Exec DATs. Accepts a space-separated list. 

**Filter Script**`Filterscript`\- A Python expression to filter results, where`operator`is the operator being tested. For example,`operator.par.parentshortcut != ""`will only show operators with a parent shortcut. 

**Limit Max Depth**`Limitmaxdepth`\- If True, limit the network depth of the search to "Maximum Depth" 

**Maximum Depth**`Maximumdepth`\- Maximum depth of search. 0 is only the search operator itself. 1 is the selected operator and its children, 2 is the selected operator, its children and its grand-children etc. 
* * *

**Include Non-Editable DATs**`Includenoneditabledats`\- If True, search DATs that can't be edited (and thus can't have text replaced in them) 

**Include Builtin Pars/Pages**`Includebuiltinparspages`\- If True, search built-in par and page names that can't be changed (and thus can't have text replaced in them). Their editable values/expressions/etc. will **always** be included. 

**Include Hidden OPs**`Includehiddenops`\- If True, include operators whose`expose`members are False. (e.g. /sys) 
* * *

**Search DAT Text**`Searchdattext`\- Search text in DATs. 

**Search Par Data**`Searchpardata`\- Search parameter values and expressions. 

**Search Field Text**`Searchfieldtext`\- Search the panel.field member of fieldCOMPs. 

**Search Tags**`Search tags`\- Search tag text. 

**Search OP Names**`Searchopnames`\- Search operator names. 

**Search Par Page Names**`Searchparpagenames`\- Search parameter page names. 

**Search Par Labels**`Searchparlabels`\- Seach parameter labels. 

**Search Par Names**`Searchparnames`\- Seach parameter names. 

**Search Par Menu Items**`Searchparmenuitems`\- Search parameter menu items (names and labels). 

## Utilities

**Open Result Table**`Openresulttable`\- Open a view of the search result table, which is also available through the Component's DAT output. 

**Clear Result Table**`Clearresulttable`\- Clear all search results from the result table. 

**Clear Results Before Search**`Clearresultsbeforesearch`\- When on, clear the result table automatically before searching. 

**Search Again After Replace**`Searchagainafterreplace`\- Automatically search again after replace operations. 

**Results Show Par Labels**`Resultsshowparlabels`\- When True, use parameter labels instead of names in results. 

**First N Matches**`Firstnmatches`\- Stop matching after finding the string in a given number of Operators. 

**N**`N`\- The number of matches to stop after. 

# Inputs

Input 1`Search OP 'path' table`: A table of OP paths to be searched. Must have a column with header: "path". Note that these OPs' children will not be searched. To search an OP's children use the Search OP parameter. 

Input 2`'search' 'replace' table`: A table of search and replace strings. Must have a column with header: "search" and a column with header: "replace". 

# Outputs

Output1`Results`: a list of results from the last operation. 

# Regular Expressions

The searchReplace component does not use wildcards. Use this feature for all non-specific searches. Regular expressions are a powerful system used for string search and replace. An internet search will return many regular expression resources, but below are a few good places to start. 
* [Full Python documentation](<https://docs.python.org/3/library/re.html>)
  * [A great tutorial.](<https://towardsdatascience.com/the-ultimate-guide-to-using-the-python-regex-module-69aad9e9ba56>)
  * [An online regular expression tester](<https://regex101.com>)

## Regular Expression Examples

These are very simple examples of things you can do with regular expressions. See full documentation for more. 

    

  *`par.`→ par followed by any character: pars, par1, parm
  *`par...`→ par followed by any three characters: parent, par123
  *`par\.`→ par followed by the '.' character: par. ONLY
  *`par.*`→ par followed by any number (including 0) of any character: parent, parsimonious, par1, parm, par
  *`par\b`→ par followed by any word boundary, which amounts to anything that ends with "par": par, ropar, 12par,
  *`par1*`→ par followed by any number (including 0) of the character "1": par, par1, par1111
  *`par1+`→ par followed by any number (excluding 0) of the character "1": par1, par1111
  *`par[a-e]`→ par followed by a letter "a" through "e": para, pard, pare
  *`par[^a-e]`→ par followed by any character that is not the letters "a" through "e": parh, par1, par]
  *`par[a-e]*`→ par followed by any number of instances of the letters "a" through "e": paraaaa, par, pardae
  *`par[a-eX]*`→ par followed by any number of instances of the letters "a" through "e" or 'X': paraeXa, parX, par
  *`par\d*`→ par followed by any number of digits: par, par58123, par0
  *`par\d\d*`→ par followed by at least one digits: par58123, par0
  *`par\w`→ par followed by any word character: par1, para

## Regular Expression Escape Sequences

There are a number of useful regular expression escape sequences (starting with backslash character). See full documentation for more. 

    

  *`\d`: a digit (0-9)
  *`\s`: a whitespace character
  *`\S`: a non-whitespace character
  *`\w`: a "word" character (a-z, A-Z, 0-9, and _)
  *`\W`: a non-"word" character (not a-z, A-Z, 0-9, or _)

## Replacements in Regular Expressions

Replacements are also extremely powerful in Regular Expressions, using a simple **grouping** system. Use parenthesis to separate any number of regular expressions, then in the replacement string, reference those groups using **`\g<#>`** with # being the group number. See full documentation for more info. 

### Examples
* **Search** :`dog(\d)`**Replace** :`god\g<1>`→ dog3 becomes god3, dog0 becomes god0 etc.
  * **Search** :`(dog|god)(\d)`**Replace** :`\g<2>\g<1>`→ dog3 becomes 3dog, god0 becomes 0god etc. **Note** : the`|`character is an "or" in the group.


TouchDesigner Build: Latest\n2022.241402021.10000before 2021.10000

Palette  
---  
[Palette ](<./Palette.md> "Palette")• [Palette:arcBallCamera ](<./Palette-arcBallCamera.md> "Palette:arcBallCamera")• [Palette:arcBallGeometry ](<./Palette-arcBallGeometry.md> "Palette:arcBallGeometry")• [Palette:audioAnalysis ](<./Palette-audioAnalysis.md> "Palette:audioAnalysis")• [Palette:audioSet ](<./Palette-audioSet.md> "Palette:audioSet")• [Palette:battery ](<./Palette-battery.md> "Palette:battery")• [Palette:bitwigClip ](<./Palette-bitwigClip.md> "Palette:bitwigClip")• [Palette:bitwigClipSlot ](<./Palette-bitwigClipSlot.md> "Palette:bitwigClipSlot")• [Palette:bitwigDeviceRemotes ](<./Palette-bitwigDeviceRemotes.md> "Palette:bitwigDeviceRemotes")• [Palette:bitwigMain ](<./Palette-bitwigMain.md> "Palette:bitwigMain")• [Palette:bitwigNote ](<./Palette-bitwigNote.md> "Palette:bitwigNote")• [Palette:bitwigProjectRemotes ](<./Palette-bitwigProjectRemotes.md> "Palette:bitwigProjectRemotes")• [Palette:bitwigRemotesDevice ](<./Palette-bitwigRemotesDevice.md> "Palette:bitwigRemotesDevice")• [Palette:bitwigRemotesProject ](<./Palette-bitwigRemotesProject.md> "Palette:bitwigRemotesProject")• [Palette:bitwigRemotesTrack ](<./Palette-bitwigRemotesTrack.md> "Palette:bitwigRemotesTrack")• [Palette:bitwigSelect ](<./Palette-bitwigSelect.md> "Palette:bitwigSelect")• [Palette:bitwigSong ](<./Palette-bitwigSong.md> "Palette:bitwigSong")• [Palette:bitwigTrack ](<./Palette-bitwigTrack.md> "Palette:bitwigTrack")• [Palette:bitwigTrackRemotes ](<./Palette-bitwigTrackRemotes.md> "Palette:bitwigTrackRemotes")• [Palette:blendModes ](<./Palette-blendModes.md> "Palette:blendModes")• [Palette:bloom ](<./Palette-bloom.md> "Palette:bloom")• [Palette:camera ](<./Palette-camera.md> "Palette:camera")• [Palette:cameraBrowser ](<./Palette-cameraBrowser.md> "Palette:cameraBrowser")• [Palette:cameraViewport ](<./Palette-cameraViewport.md> "Palette:cameraViewport")• [Palette:camSchnappr ](<./Palette-camSchnappr.md> "Palette:camSchnappr")• [Palette:changeColor ](<./Palette-changeColor.md> "Palette:changeColor")• [Palette:changeToColor ](<./Palette-changeToColor.md> "Palette:changeToColor")• [Palette:checker ](<./Palette-checker.md> "Palette:checker")• [Palette:chromaKey ](<./Palette-chromaKey.md> "Palette:chromaKey")• [Palette:colorThreshold ](<./Palette-colorThreshold.md> "Palette:colorThreshold")• [Palette:compareComp ](<./Palette-compareComp.md> "Palette:compareComp")• [Palette:convolve ](<./Palette-convolve.md> "Palette:convolve")• [Experimental:Palette:cornerPinPOP ](</Experimental:Palette:cornerPinPOP> "Experimental:Palette:cornerPinPOP")• [Palette:cornerPinSOP ](<./Palette-cornerPinSOP.md> "Palette:cornerPinSOP")• [Palette:cppParsTemplateGen ](<./Palette-cppParsTemplateGen.md> "Palette:cppParsTemplateGen")• [Palette:customAttributes ](<./Palette-customAttributes.md> "Palette:customAttributes")• [Palette:debugControl ](<./Palette-debugControl.md> "Palette:debugControl")• [Palette:dent ](<./Palette-dent.md> "Palette:dent")• [Palette:depthExtract ](<./Palette-depthExtract.md> "Palette:depthExtract")• [Palette:depthProjection ](<./Palette-depthProjection.md> "Palette:depthProjection")• [Palette:dilate ](<./Palette-dilate.md> "Palette:dilate")• [Palette:encoder ](<./Palette-encoder.md> "Palette:encoder")• [Palette:equalizer ](<./Palette-equalizer.md> "Palette:equalizer")• [Palette:feedback ](<./Palette-feedback.md> "Palette:feedback")• [Palette:feedbackEdge ](<./Palette-feedbackEdge.md> "Palette:feedbackEdge")• [Palette:firmata ](<./Palette-firmata.md> "Palette:firmata")• [Palette:gal ](<./Palette-gal.md> "Palette:gal")• [Palette:geoPanel ](<./Palette-geoPanel.md> "Palette:geoPanel")• [Palette:gestureCapture ](<./Palette-gestureCapture.md> "Palette:gestureCapture")• [Palette:graphPlot ](<./Palette-graphPlot.md> "Palette:graphPlot")• [Palette:histogram ](<./Palette-histogram.md> "Palette:histogram")• [Palette:hsvBlur ](<./Palette-hsvBlur.md> "Palette:hsvBlur")• [Palette:imageSearch ](<./Palette-imageSearch.md> "Palette:imageSearch")• [Palette:julia ](<./Palette-julia.md> "Palette:julia")• [Palette:kantanMapper ](<./Palette-kantanMapper.md> "Palette:kantanMapper")• [Palette:kinectCalibration ](<./Palette-kinectCalibration.md> "Palette:kinectCalibration")• [Palette:kinectPointcloud ](<./Palette-kinectPointcloud.md> "Palette:kinectPointcloud")• [Palette:leapPaint ](<./Palette-leapPaint.md> "Palette:leapPaint")• [Palette:lightTunnel ](<./Palette-lightTunnel.md> "Palette:lightTunnel")• [Palette:logger ](<./Palette-logger.md> "Palette:logger")• [Experimental:Palette:logger ](</Experimental:Palette:logger> "Experimental:Palette:logger")• [Palette:mandelbrot ](<./Palette-mandelbrot.md> "Palette:mandelbrot")• [Palette:materialDesignIcons ](<./Palette-materialDesignIcons.md> "Palette:materialDesignIcons")• [Palette:mesh ](<./Palette-mesh.md> "Palette:mesh")• [Palette:monochrome ](<./Palette-monochrome.md> "Palette:monochrome")• [Palette:motionSense ](<./Palette-motionSense.md> "Palette:motionSense")• [Palette:movieEngine ](<./Palette-movieEngine.md> "Palette:movieEngine")• [Palette:moviePlayer ](<./Palette-moviePlayer.md> "Palette:moviePlayer")• [Palette:moviePlaylist ](<./Palette-moviePlaylist.md> "Palette:moviePlaylist")• [Palette:multiLevel ](<./Palette-multiLevel.md> "Palette:multiLevel")• [Palette:multiMix ](<./Palette-multiMix.md> "Palette:multiMix")• [Palette:noise ](<./Palette-noise.md> "Palette:noise")• [Palette:onScreenKeyboard ](<./Palette-onScreenKeyboard.md> "Palette:onScreenKeyboard")• [Palette:operatorPath ](<./Palette-operatorPath.md> "Palette:operatorPath")• [Palette:opticalFlow ](<./Palette-opticalFlow.md> "Palette:opticalFlow")• [Palette:particlesGpu ](<./Palette-particlesGpu.md> "Palette:particlesGpu")• [Palette:pixelate ](<./Palette-pixelate.md> "Palette:pixelate")• [Palette:pixelRelocator ](<./Palette-pixelRelocator.md> "Palette:pixelRelocator")• [Palette:pointGenerator ](<./Palette-pointGenerator.md> "Palette:pointGenerator")• [Palette:pointillize ](<./Palette-pointillize.md> "Palette:pointillize")• [Palette:pointMerge ](<./Palette-pointMerge.md> "Palette:pointMerge")• [Palette:pointRender ](<./Palette-pointRender.md> "Palette:pointRender")• [Palette:pointRepack ](<./Palette-pointRepack.md> "Palette:pointRepack")• [Palette:pointTransform ](<./Palette-pointTransform.md> "Palette:pointTransform")• [Palette:pointWeight ](<./Palette-pointWeight.md> "Palette:pointWeight")• [Palette:popDialog ](<./Palette-popDialog.md> "Palette:popDialog")• [Experimental:Palette:popDialog ](</Experimental:Palette:popDialog> "Experimental:Palette:popDialog")• [Palette:probe ](<./Palette-probe.md> "Palette:probe")• [Palette:projectorBlend ](<./Palette-projectorBlend.md> "Palette:projectorBlend")• [Palette:pushPins ](<./Palette-pushPins.md> "Palette:pushPins")• [Palette:puzzle ](<./Palette-puzzle.md> "Palette:puzzle")• [Palette:quadReproject ](<./Palette-quadReproject.md> "Palette:quadReproject")• [Palette:radialBlur ](<./Palette-radialBlur.md> "Palette:radialBlur")• [Palette:recorder ](<./Palette-recorder.md> "Palette:recorder")• [Experimental:Palette:recorder ](</Experimental:Palette:recorder> "Experimental:Palette:recorder")• [Palette:remotePanel ](<./Palette-remotePanel.md> "Palette:remotePanel")• [Palette:rgbaBlur ](<./Palette-rgbaBlur.md> "Palette:rgbaBlur")• [Palette:rgbaDelay ](<./Palette-rgbaDelay.md> "Palette:rgbaDelay")• [Palette:rgbContrast ](<./Palette-rgbContrast.md> "Palette:rgbContrast")• [Palette:sceneChanger ](<./Palette-sceneChanger.md> "Palette:sceneChanger")• [Palette:search ](<./Palette-search.md> "Palette:search")• Palette:searchReplace • [Palette:sharpen ](<./Palette-sharpen.md> "Palette:sharpen")• [Palette:sickEngine ](<./Palette-sickEngine.md> "Palette:sickEngine")• [Palette:signalingClient ](<./Palette-signalingClient.md> "Palette:signalingClient")• [Palette:signalingServer ](<./Palette-signalingServer.md> "Palette:signalingServer")• [Palette:softenAlpha ](<./Palette-softenAlpha.md> "Palette:softenAlpha")• [Palette:solarize ](<./Palette-solarize.md> "Palette:solarize")• [Palette:sopRender ](<./Palette-sopRender.md> "Palette:sopRender")• [Palette:splitter ](<./Palette-splitter.md> "Palette:splitter")• [Palette:stitcher ](<./Palette-stitcher.md> "Palette:stitcher")• [Palette:stoner ](<./Palette-stoner.md> "Palette:stoner")• [Palette:superFormula ](<./Palette-superFormula.md> "Palette:superFormula")• [Palette:SVG ](<./Palette-SVG.md> "Palette:SVG")• [Palette:sweetSpot ](<./Palette-sweetSpot.md> "Palette:sweetSpot")• [Palette:sweetSpotPreviz ](<./Palette-sweetSpotPreviz.md> "Palette:sweetSpotPreviz")• [Palette:synchroCache ](<./Palette-synchroCache.md> "Palette:synchroCache")• [Palette:synchroClient ](<./Palette-synchroClient.md> "Palette:synchroClient")• [Palette:synchroFrameIn ](<./Palette-synchroFrameIn.md> "Palette:synchroFrameIn")• [Palette:synchroFrameOut ](<./Palette-synchroFrameOut.md> "Palette:synchroFrameOut")• [Palette:synchroNDIIn ](<./Palette-synchroNDIIn.md> "Palette:synchroNDIIn")• [Palette:synchroSDIIn ](<./Palette-synchroSDIIn.md> "Palette:synchroSDIIn")• [Palette:synchroVideoOut ](<./Palette-synchroVideoOut.md> "Palette:synchroVideoOut")• [Palette:tdBitwigPackage ](<./Palette-tdBitwigPackage.md> "Palette:tdBitwigPackage")• [Experimental:Palette:tdPyEnvManager ](</Experimental:Palette:tdPyEnvManager> "Experimental:Palette:tdPyEnvManager")• [Palette:TDVR ](<./Palette-TDVR.md> "Palette:TDVR")• [Palette:testGrid ](<./Palette-testGrid.md> "Palette:testGrid")• [Experimental:Palette:threadManagerClient ](</Experimental:Palette:threadManagerClient> "Experimental:Palette:threadManagerClient")• [Experimental:Palette:threadsMonitor ](</Experimental:Palette:threadsMonitor> "Experimental:Palette:threadsMonitor")• [Palette:transitMap ](<./Palette-transitMap.md> "Palette:transitMap")• [Palette:twirl ](<./Palette-twirl.md> "Palette:twirl")• [Palette:vectorScope ](<./Palette-vectorScope.md> "Palette:vectorScope")• [Palette:virtualFile ](<./Palette-virtualFile.md> "Palette:virtualFile")• [Palette:waveformMonitor ](<./Palette-waveformMonitor.md> "Palette:waveformMonitor")• [Palette:webBrowser ](<./Palette-webBrowser.md> "Palette:webBrowser")• [Palette:webRTC ](<./Palette-webRTC.md> "Palette:webRTC")• [Palette:webRTCPanel ](<./Palette-webRTCPanel.md> "Palette:webRTCPanel")• [Palette:webRTCPanelRcv ](<./Palette-webRTCPanelRcv.md> "Palette:webRTCPanelRcv")• [Palette:xyScope ](<./Palette-xyScope.md> "Palette:xyScope")• [Experimental:Thread Manager ](</Experimental:Thread_Manager> "Experimental:Thread Manager")
