# Alpha-Test

The **Alpha-Test** is a process to discard pixels, like the [Depth-Test](<./Depth-Test.md> "Depth-Test"). It's available on the common page of all MATs under the name 'Discard Pixels Based on Alpha'. The Alpha-Test compares the final alpha of the pixel, after the pixel shader has run, against a threshold value. If the alpha is less than the threshold value, the pixel is discarded. The Alpha-Test is performed before the Depth-Test and before Alpha-Blending.   
  
One common use of the Alpha-Test is to discard pixels based on an alpha map, to create a cut-out geometry based on the map.
