# Texture Extend Modes

## Overview

Texture extend modes control what happens when texture coordinate go beyond the range [0,1]. A texture can have a different extend mode for it's U, V and W texture coordinates. When dealing with TOPs, this refers to what happens beyond the edge of an image/overlay when you are combining two different TOPs that have different resolutions and/or aspect rations. 

The different extend modes are 

**Hold** \- Coordinates outside the [0,1] range will receive the pixel color at the edge of the image, depending on which edge is closest (e.g a coordinate of 1.5 for U will result in a color that is the right most pixel of the image from whichever line the V coordinate is referencing. 

**Zero** \- Coordinates outside the [0,1] range will receive a pixel color of (0,0,0,0) 

**Repeat** \- Coordinates outside the [0,1] will cause the texture to repeat itself. The coordinates are simply remapped to the [0,1] range by removing the integer portion. e.g 1.4 becomes 0.4 and -0.6 becomes 0.6. 

**Mirror** \- Much like repeat, but the coordinates are flipped for each odd/even value for the integer portion of the texture coordinates.
