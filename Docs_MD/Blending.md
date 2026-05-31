# Blending

Blending is a function used to combine two pixels together in various ratios. Blending is the basic operation of image compositing and is frequently used to create [transparency](<./Transparency.md> "Transparency") effects.   
  
In blending functions, one pixel is designated as **the source** and the other is designated as **the destination**. Blending uses a source blending factor to determine what proportion of the source pixel's color to draw over the destination pixel. The destination pixel also has a blending factor that determines what percentage of its own color will be contributed to the final blended pixel. 

The blending equation is: 

    Final Pixel Value = (Source Blend Factor * Source Pixel Color) + (Destination Blend Factor * Destination Pixel Color)

In TouchDesigner, blending is a common parameter for most [MATs](<./MAT.md> "MAT").
