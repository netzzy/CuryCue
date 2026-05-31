# Matrix Parameters

Various nodes such as [GLSL TOP](<./GLSL_TOP.md> "GLSL TOP"), [Camera COMP](<./Camera_COMP.md> "Camera COMP"), [Geometry COMP](<./Geometry_COMP.md> "Geometry COMP") have parameters that accept matrices. Matrices in TouchDesigner parameters can be specified in a few different ways 

## Python tdu.Matrix

A [tdu.Matrix](<./Matrix_Class.md> "Matrix Class") object can be built manually, or gotten from various methods in [ObjectCOMP Class](<./ObjectCOMP_Class.md> "ObjectCOMP Class") and COMPs that inherite from that. A matrix parameter can reference a Python`tdu.Matrix`either directly from a member/method that returns one, or from one that has been placed into [Storage](<./Storage.md> "Storage"). 

E.g 
[code] 
     m = tdu.Matrix()
     m.translate(5, 0, 0)
     m.rotate(0, 45, 0)
     op('someNode').store(‘xformMat’, m)
     
    
[/code]

and in the node parameter you would put: 
[code] 
     op('someNode').fetch(‘xformMat’)
    
[/code]

## Table DAT

A [Table DAT](<./Table_DAT.md> "Table DAT") can be used to specify a matrix, as a 4x4 table. The translation should be in the last column, which means it is using the convention of multiplying vectors/points on the right of the matrix (like GLSL does). 

## CHOP

If a CHOP is used, the 16 elements of the matrix are taken from the first 16 channels of the CHOP. It only uses the first sample of each channel. The matrix data is laid out in such as way that the 13th, 14th and 15th channels contain the translation. This can be thought of as either column or row-major conventions, reading the channels column by column or row by row. 

If you are converting from a Table DAT using a DAT to CHOP, you'll want to use a [Transpose DAT](<./Transpose_DAT.md> "Transpose DAT") to get the channels in the correct order.
