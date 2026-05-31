# Anisotropic Filtering

## Overview

**Anisotropic Filtering** is a [texture filtering](<./Texture_Filtering.md> "Texture Filtering") method to improve image quality when [polygons](<./Polygon.md> "Polygon") are at an angle to the camera. Default texture filtering methods use a square sampling method which essentially assumes the polygon is facing the camera (no tilt at all). These methods work for most instances, but some textures will exhibit artifacts as they get tilted away from the camera. 

Anisotropic Filtering does extra samples when sampling the texture: the location and shape of the samples are dependent on how the geometry is orientated with respect to the camera. 

## Using Anisotropic Filtering in TouchDesigner

In [MATs](<./MAT.md> "MAT"), next to each parameter that takes a [TOP](<./TOP.md> "TOP") as an input, there is a + button. Pressing this button will display extra settings on how that texture will be used in this MAT. The Anisotropy Level parameter controls anisotropic filtering for that parameter. The higher the number the higher the quality the anisotropic filtering. 

The folowing example shows an example fo Anisotropic Filtering and how to set it up in TouchDesigner. 

[File:Anisotropic filtering.tox](</File:Anisotropic_filtering.tox> "File:Anisotropic filtering.tox")
