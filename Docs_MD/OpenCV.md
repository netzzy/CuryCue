# OpenCV

[OpenCV](<https://en.wikipedia.org/wiki/OpenCV>) (Open Source Computer Vision) is a library of programming functions mainly aimed at real-time computer vision, originally developed by an Intel research center and now open source. 

TouchDesigner comes pre-installed with OpenCV 4.8.0 (including contributed modules), and numpy which interface with TouchDesigner's Python 3.11.1, making it possible for TouchDesigner to access the OpenCV functions directly. 

OpenCV is used in the [Script TOP](<./Script_TOP.md> "Script TOP"), [Blob Track TOP](<./Blob_Track_TOP.md> "Blob Track TOP") and [camSchnappr](<./Palette-camSchnappr.md> "Palette:camSchnappr"). 

## Using OpenCV with python

### Testing OpenCV
* open TouchDesigner
  * open the Textport with Alt+t
  * run following commands:


[code]
    TouchDesigner  Build 2023.10990 compile on Wed Aug 16 08:27:59 2023
    Python 3.11.1 (heads/3.11-Derivative-dirty:82b0389147, Jan 25 2023, 22:34:27) [MSC v.1929 64 bit (AMD64)]
    
    python >>> import cv2
    python >>> cv2.__version__
    '4.8.0'
    
[/code]
* if the output is '4.8.0' and no errors, OpenCV is working properly.

### Textures to numpyArrays

Every TOP can directly be converted into a NumPy Array by calling the`myTop.numpyArray()`Method (Also see: [TOP Class#Methods](<./TOP_Class.htm#Methods> "TOP Class")) 

NumPy arrays are the default data structure openCV saves its data in. In general NumPy can be understood as a library for Python to support large, multi-dimensional arrays and matricies, along with a large collection of high level functions to operate on these arrays. (Compare: [NumPy](<https://en.wikipedia.org/wiki/NumPy>)) 

### Example: Applying a colormap to a Texture

The following example is the content of a Script TOP. The OpenCV function`cv2.applyColorMap()`takes as input a monochrome image as well as a reference to a predefined colormap essentially doing what the Lookup TOP does in TouchDesigner. More information can be found here: [ColorMaps in OpenCV](<https://docs.opencv.org/master/d3/d50/group__imgproc__colormap.html#gadf478a5e5ff49d8aa24e726ea6f65d15>)
[code] 
    def onCook(scriptOp):
    	# grab the input to the scriptTOP with a frame delayed
        # for faster operation (compare TopTo CHOP)
    	input = scriptOp.inputs[0].numpyArray(delayed=True)
    
    	# do we have a image ready?
        # the first frame will be None as we are getting things a frame later.
    	if not input is None: 
    		# extract the red channel and convert to uint8
    		sChan = cv2.extractChannel(input,0)*255
    		sChan = sChan.astype('uint8')
    
    		# apply a colormap to the red channel
    		output = cv2.applyColorMap(sChan, cv2.COLORMAP_TWILIGHT_SHIFTED)
            # output the numpyarray to the Script TOP
    		scriptOp.copyNumpyArray(output)
    	return
    
[/code]

### Example: Finding Features in a Texture

The following example is the content of a Script CHOP. First, parameters for the Script CHOP are specified. 

For each cook of the Script CHOP, the operator specified in the`Top`custom parameter is read into a numPy array and then passed on to an openCV function called goodFeaturesToTrack. 

**Note:** The referenced TOP should be a monochrom image. Converting color textures to grayscale can be done using the [Monochrome TOP](<./Monochrome_TOP.md> "Monochrome TOP"). Doing so, and using the Luminance function as the convertion, makes it unnecessary to do this step in the script (many openCV functions expect a grayscale image as input). 

The resulting output can be used in an Instancing setup. 
[code] 
    # me - this DAT
    # scriptOp - the OP which is cooking
    
    # press 'Setup Parameters' in the OP to call this function to re-create the parameters.
    def onSetupParameters(scriptOp):
    	# create a custom page
    	page = scriptOp.appendCustomPage('Good Features')
    
    	# create a custom TOP reference parameter
    	topPar = page.appendTOP('Top', label='TOP (monochrome)')
    
    	# create a custom parameter to specify number of features to detect
    	p = page.appendInt('Features', label='Number of Features')
    	p[0].default = 25
    	p[0].normMin = 1
    	p[0].normMax = 250
    
    	# create a custom parameter to specify minimum quality level
    	# under which detected features would be rejected
    	p = page.appendFloat('Quality', label='Minimum Quality Level')
    	p[0].default = 0.01
    	p[0].normMin = 0.001
    	p[0].normMax = 1
    
    	# create a custom parameter to specify the minimum distance
    	# between detected features
    	p = page.appendInt('Distance', label='Minimum Distance')
    	p[0].default = 10
    	p[0].normMin = 1
    	p[0].normMax = 1200
    	return
    
    # called whenever custom pulse parameter is pushed
    def onPulse(par):
    	return
    	
    import numpy as np
    import cv2
    
    def onCook(scriptOp):
    	scriptOp.clear()
    	
    	# read in parameters to see how many features to detect
    	topRef = scriptOp.par.Top.eval()
    	features = scriptOp.par.Features
    	quality = scriptOp.par.Quality
    	distance = scriptOp.par.Distance
    	
    	# default values
    	xVals = []
    	yVals = []
    	corners = []
    	
    	if topRef:
    		# read top as numpyArray
    		img = topRef.numpyArray()
    		
    		# since we are reading from a gray scale TOP, throw out everything but red channel
    		# we also can skip the cv2.cvtColor function you would see here otherwise for converting a color image to gray scale
    		img = img[:,:,:1]
    		
    		# run goodFeaturesToTrack openCV function
    		# https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_feature2d/py_shi_tomasi/py_shi_tomasi.html
    		corners = cv2.goodFeaturesToTrack(img,features,quality,distance)
    		
    		# slice array to have x and y positions split into 2 variables
    		xVals = corners[:,:,0:1]
    		yVals = corners[:,:,1:2]
    	
    	# setup the scriptOp with 2 channels
    	# also set length to number of features that were detected
    	scriptOp.rate = me.time.rate
    	scriptOp.numSamples = len(corners)
    	tx = scriptOp.appendChan('tx')
    	ty = scriptOp.appendChan('ty')
    	
    	# assign values to channels
    	tx.vals = xVals
    	ty.vals = yVals
    	return
    
[/code]

### Example: Adding Elements in OpenCV

A thing to pay attention to is that OpenCV's coordinate system has it's origin top/left, while TouchDesigner is bottom/left based. Therefor when overlaying elements like lines, text, or other graphics onto a texture in openCV, the source texture needs to be flipped first and after processing flipped back. 

The following example will read a texture from the input of a [Script TOP](<./Script_TOP.md> "Script TOP") and add some text: 
[code] 
    # me - this DAT
    # scriptOp - the OP which is cooking
    
    # press 'Setup Parameters' in the OP to call this function to re-create the parameters.
    def onSetupParameters(scriptOp):
    	return
    
    # called whenever custom pulse parameter is pushed
    def onPulse(par):
    	return
    
    import cv2
    def onCook(scriptOp):
    	# grab the input texture to the scriptOp
    	inputTex = scriptOp.inputs[0].numpyArray(delayed=False)
    
    	# before adding things to the image, we need to flip it as opencv's coordinate system 
    	# starts top/left while TouchDesigner starts bottom/left
    	# the second argument of flip() is the axis to flip around
    	inputTex = cv2.flip(inputTex, 0)
    
    	# now lets add some text
    	outputTex = cv2.putText(inputTex, 'Derivative', (100,400), cv2.FONT_HERSHEY_PLAIN, 10, (255, 0, 255), 2, cv2.LINE_AA)
    	
    	# flip the texture back so we are in TouchDesigner coordinate space
    	outputTex = cv2.flip(outputTex, 0)
    	
    	# write final texture to scriptOp
    	scriptOp.copyNumpyArray(outputTex)
    	return
    
[/code]

### Next Steps

There is a selection of introductory tutorials on the [OpenCV website](<http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_tutorials.html>) and [OpenCV Tutorials](<http://docs.opencv.org/master/d6/d00/tutorial_py_root.html>)

## Using OpenCV with Custom Operators

TouchDesigner includes the full set of OpenCV libraries and includes necessary to develop Custom Operators that make use of OpenCV 4.8.0 

In the TouchDesigner GitHub repository ["Custom Operator Samples"](<https://github.com/TouchDesigner/CustomOperatorSamples>) multiple examples in the TOP family make use of OpenCV: 
* [Canny Edge TOP](<https://github.com/TouchDesigner/CustomOperatorSamples/tree/main/TOP/CannyEdgeTOP>)
  * [Contours TOP](<https://github.com/TouchDesigner/CustomOperatorSamples/tree/main/TOP/ContoursTOP>)
  * [Distance Transform TOP](<https://github.com/TouchDesigner/CustomOperatorSamples/tree/main/TOP/DistanceTransformTOP>)
  * [Object Detector TOP](<https://github.com/TouchDesigner/CustomOperatorSamples/tree/main/TOP/ObjectDetectorTOP>)
  * [Optical Flow CPU TOP](<https://github.com/TouchDesigner/CustomOperatorSamples/tree/main/TOP/OpticalFlowCPUTOP>)
  * [Spectrum TOP](<https://github.com/TouchDesigner/CustomOperatorSamples/tree/main/TOP/SpectrumTOP>)


OpenCV C++ Documentation is [here](<https://docs.opencv.org/4.8.0/index.html>). 

## OpenCV License Agreement

TouchDesigner uses parts of OpenCV (the [Blob Track TOP](<./Blob_Track_TOP.md> "Blob Track TOP")) under the following license. 

Intel License Agreement. 

Copyright (C) 2000, Intel Corporation, rights reserved. Third party copyrights are property of their respective owners. 

Redistribution of OpenCV and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met: 
* Redistribution's of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
* Redistribution's in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
* The name of Intel Corporation may not be used to endorse or promote products derived from this software without specific prior written permission.


The OpenCV software is provided by the copyright holders and contributors "as is" and any express or implied warranties, including, but not limited to, the implied warranties of merchantability and fitness for a particular purpose are disclaimed. In no event shall the Intel Corporation or contributors be liable for any direct, indirect, incidental, special, exemplary, or consequential damages (including, but not limited to, procurement of substitute goods or services; loss of use, data, or profits; or business interruption) however caused and on any theory of liability, whether in contract, strict liability, or tort (including negligence or otherwise) arising in any way out of the use of this software, even if advised of the possibility of such damage.
