# NumPy

**NumPy** is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays.[[1]](<#cite_note-1>)  
  
Python bindings of the widely used computer vision library [OpenCV](<./OpenCV.md> "OpenCV") utilize NumPy arrays to store and operate on data. Since images with multiple channels are simply represented as three-dimensional arrays, indexing, slicing or masking with other arrays are very efficient ways to access specific pixels of an image. The NumPy array as universal data structure in OpenCV for images, extracted feature points, filter kernels and many more vastly simplifies the programming workflow and debugging.[[2]](<#cite_note-2>)

A good general introduction to NumPy can be found here: <https://numpy.org/doc/stable/user/absolute_beginners.html>

## NumPy and TouchDesigner

TouchDesigner allows for easily converting between [TOP](<./TOP.md> "TOP") and [CHOP](<./CHOP.md> "CHOP") data to NumPy arrays utilizing methods found in the [TOP](<./TOP_Class.md> "TOP Class"), [CHOP](<./CHOP_Class.md> "CHOP Class"), [Channel](<./Channel_Class.md> "Channel Class") and [Matrix](<./Matrix_Class.md> "Matrix Class") Classes. 

### NumPy and CHOPs

For example a CHOP with all its channels and samples can be converted to a NumPy array: 
[code] 
    # Returns all of the channels in this CHOP a 2D NumPy array 
    # with a width equal to the channel length (the number of samples)
    # and a height equal to the number of channels.
    # The data will be stored as 32 bit float.
    npArray = op('someChop').numpyArray()
    
[/code]

Similarly, a single CHOP Channel can be converted to a NumPy array: 
[code] 
    # Returns this channels data as a NumPy array 
    # with a length equal to the track length. 
    # The data will be stored as 32 bit float.
    npArray = op('someChop')['chan1'].numpyArray()
    
[/code]

When working with a [Script CHOP](<./Script_CHOP.md> "Script CHOP"), data stored in NumPy arrays can be converted back into CHOP Channels. In this case the shape of the array must be`shape(numChannels, numSamples)`and have a datatype of float32. [[3]](<#cite_note-3>)

The simple example here creates 3 channels in a Script CHOP with 20 samples each and sets the value of the eleventh sample in the second channel to 1 while all other values are 0: 
[code] 
    # import the NumPy library
    import numpy as np
    
    def onCook(scriptOp):
    	scriptOp.clear()
    
    	# specify number of channels and samples
    	numChannels = 3
    	numSamples = 20
    
    	# create a NumPy array filled with zeros
    	# the datatype must be float32 to be used in the CHOP
    	npArray = np.zeros((numChannels, numSamples), dtype=np.float32)
    
    	# set the 11th sample of the 2nd channel to 1.234
    	npArray[1][10] = 1.234
    
    	# copy the NumPy array into CHOP channels
    	scriptOp.copyNumpyArray(npArray)
    	return
    
[/code]

For a more practical example, lets assume a CHOP with 2 channels and 10 samples describing the xy position of some objects in 2D space and we need to calculate the pairwise Euclidian distance between all of them. This will result in 10 channels with 10 samples each. Here we can utilize the [broadcasting](<http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html>) functionality of NumPy to simplify the necessary code. 
[code] 
    # import the NumPy library
    import numpy as np
    
    def onCook(scriptOp):
    	scriptOp.clear()
    	inputs = scriptOp.inputs[0]
    	
    	# get input CHOP as NumPy array
    	inPos = inputs.numpyArray()
    	
    	# this results in a numChannels x numSamples array 
    	# we need to transpose the attay to a numSamples x numChannels array
    	# to get positions as pairs for each point
    	# this is comparable to the Shuffle CHOP's "Swap Channels and Samples"
    	inPos = inPos.T
    	
    	# using broadcasting, we can eliminate the for loop
    	# and calculate the distance between all points
    	# https://numpy.org/doc/stable/user/basics.broadcasting.html
    	npDist = np.sqrt(((inPos[:,:,None] - inPos[:,:,None].T) ** 2).sum(1))
    
    	# copy the NumPy array into the CHOP  
    	scriptOp.copyNumpyArray(npDist)
    	return
    
[/code]

For more examples check out the Script CHOP Snippets. 

### NumPy and TOPs

Similar functionality is also available for TOPs. 

A TOP can be simply read in as a NumPy array: 
[code] 
    # Returns the TOP image as a Python NumPy array. 
    # Since NumPy arrays are referenced by line first, pixels are addressed as [h, w]. 
    # Currently data will always be in 32 bit float format.
    npArray = op('someTop').numpyArray()
    
[/code]

Analogous to the TOPTo CHOP, the`.numpyArray()`method has an argument to download the data on the next call avoiding stalling the GPU. 
[code] 
    # Returns the TOP image as a Python NumPy array delayed. 
    # Since NumPy arrays are referenced by line first, pixels are addressed as [h, w]. 
    # Currently data will always be in 32 bit float format.
    npArray = op('someTop').numpyArray(delayed=True)
    
[/code]

When using [Script TOPs](<./Script_TOP.md> "Script TOP") use the`.copyNumpyArray()`method to write a NumPy array back as a texture. 
[code] 
    # download the input texture to the script TOP into a NumPy array
    npArray = scriptOp.inputs[0].numpyArray()
    
    # copy the NumPy array into the texture
    scriptOp.copyNumpyArray(npArray)
    
[/code]

You have to watch out when converting between pixel formats. Reading a texture from an input will always result in a 32-bit float. When you want to output as a 8-bit fixed, the values need to be first multiplied by 255 before changing the array datatype to unit8 
[code] 
    # import the NumPy library
    import numpy as np
    def onCook(scriptOp):
    	# copy the input top into a NumPy array
    	npArray = scriptOp.inputs[0].numpyArray()
    
    	# 8bit has a value range of 0 to 255, so multiply the array by 255
    	npArray *= 255
    
    	# change the data type to uint8
    	npArray = npArray.astype(np.uint8)
    
    	# copy the NumPy array into the TOP texture
    	scriptOp.copyNumpyArray(npArray)
    	return
    
[/code]

For more examples check out the Script TOP Snippets. 

### NumPy and the Matrix Class

The [Matrix Class](<./Matrix_Class.md> "Matrix Class") also allows for copying a TouchDesigner matrix into a NumPy array which gives access to a variety of matrix operations in NumPy otherwise not available in TouchDesigner. 
[code] 
    import numpy as np
    # create a identity matrix
    m = tdu.Matrix()
    
    # convert matrix into a NumPy array
    npArray = m.numpyArray()
    
    # output only the diagonal values of the matrix
    # this will output a NumPy array: array([1., 1., 1., 1.], dtype=float32)
    debug(npArray.diagonal())
    
[/code]

### Converting NumPy arrays to a bytearray

It can be useful to convert a NumPy array into a python bytearray. NumPy allows for this by using the`.tobytes()`method.[[4]](<#cite_note-4>)
[code] 
    # load a CHOP channel into a NumPy array
    npArray = op('someCHOP')['chan1'].numpyArray()
    # convert the NumPy array to a bytearray
    b = npArray.tobytes()
    
[/code]
1. [↑](<#cite_ref-1>) Wikipedia contributors, 'NumPy', Wikipedia, The Free Encyclopedia, 13 February 2022, 23:28 UTC, <[https://en.wikipedia.org/w/index.php?title=NumPy&oldid=1071707133](<https://en.wikipedia.org/w/index.php?title=NumPy&oldid=1071707133>)> [accessed 22 March 2022]
  2. [↑](<#cite_ref-2>) Wikipedia contributors, 'NumPy', Wikipedia, The Free Encyclopedia, 13 February 2022, 23:28 UTC, <[https://en.wikipedia.org/w/index.php?title=NumPy&oldid=1071707133#Features](<https://en.wikipedia.org/w/index.php?title=NumPy&oldid=1071707133#Features>)> [accessed 22 March 2022]
  3. [↑](<#cite_ref-3>) [Script CHOP Class](<./ScriptCHOP_Class.htm#Methods> "ScriptCHOP Class")
  4. [↑](<#cite_ref-4>) <https://numpy.org/doc/stable/reference/generated/numpy.ndarray.tobytes.html>
