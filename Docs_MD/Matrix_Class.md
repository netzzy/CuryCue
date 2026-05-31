# Matrix Class

The matrix class holds a single 4x4 matrix for use in transformations. The matrix's data layout is in [column-major format](<http://en.wikipedia.org/wiki/Column-major_order#Column-major_order>), which is to say that the matrix is multiplied from the left of [vectors](<./Vector_Class.md> "Vector Class") and [positions](<./Position_Class.md> "Position Class"). The translation values are stored in the last column of the matrix. 

**Note:** tdu.Matrix and TDU.Matrix can be used interchangeably. In general, TDU.Matrix is used to represent the class, while tdu.Matrix is used for the instantiator function. 

A matrix is created with this line, and will always be initialized to the identity matrix. 
[code] 
    m = tdu.Matrix()
    
[/code]

You can also initialize a matrix with starting values, including another matrix or an initial set of values. When specifiying start values, valid arguments include a list of 16 values or 4 lists of 4 values (among other formats, see the instantiators below). The entries are specified column-by-column. For example, the following lines of code will all produce the shown matrix 
[code] 
    m = tdu.Matrix(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)
    
[/code]
[code] 
    m = tdu.Matrix([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
    
[/code]
[code] 
    m = tdu.Matrix([1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16])
    
[/code]
[code] 
    # matrix values
    1  5  9   13
    2  6  10  14
    3  7  11  15
    4  8  12  16
    
[/code]

Other valid instantiator arguments include a quaternion as a list of 4 values or transformation/projection matrices from [Object COMP](<./ObjectCOMP_Class.md> "ObjectCOMP Class") and [Camera COMP](<./CameraCOMP_Class.md> "CameraCOMP Class") using various methods such as`transform()`,`pretransform()`, or`projection()`. 

## Instantiators`TDU.Matrix(*args, zero=False)`→`TDU.Matrix`: 

> Create a new Matrix object. 
> 
>   *`zero`\- if True, create a matrix with all zeroes
> 

> 
> The following argument forms are valid instantiators: 
> 
>   *`tdu.Matrix()`\- identity matrix
>   *`tdu.Matrix(matrix : TDU.Matrix)`\- copy the matrix in the argument
>   *`tdu.Matrix(vals : list)`\- list of 4 values as a quaternion OR list of 9 or 16 values to fill matrix columns
>   *`tdu.Matrix(col1 : list, col2 : list, col3 : list)`\- 3 lists of 3 or 4 floats to fill columns
>   *`tdu.Matrix(col1 : list, col2 : list, col3 : list, col4 : list)`\- 4 lists of 3 or 4 floats to fill columns
>   *`tdu.Matrix(f1, f2, f3, f4, f5, f6, f7, f8, f9)`\- 9 floats to fill matrix columns
>   *`tdu.Matrix(f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13, f14, f15, f16)`\- 16 floats to fill matrix columns
> 

## Members`vals`→`float`: 

> Get or set the set of Matrix values.`rows`→`list[list]`**(Read Only)** : 

> The list of Matrix rows, each a list of values.`cols`→`list[list]`**(Read Only)** : 

> The list of Matrix columns, each a list of values.

## Methods`transpose()`→`None`: 

> Transpose the values in the matrix. 
[code]
>     m.transpose() # m now contains the transpose of the matrix
>     
[/code]`getTranspose()`→`None`: 

> Returns the transpose of the matrix, leaving the matrix itself unchanged. 
[code]
>     m2 = m.getTranspose()
>     
[/code]`invert()`→`None`: 

> Inverts the values in the matrix. 
[code]
>     m.invert() # m now contains the inverse of the matrix
>     
[/code]`getInverse()`→`TDU.Matrix`: 

> Returns the inverse of the matrix, leaving the matrix itself unchanged. 
[code]
>     m2 = m.getInverse()
>     
[/code]`determinant()`→`float`: 

> Returns the determinant of the matrix. 
[code]
>     l = m.determinant()
>     
[/code]`mapUnitSquareToQuad(blX, blY, brX, brY, tlX, tlY, trX, trY)`→`None`: 

> Set the matrix to be a projection matrix that maps coordinates from to a unit square (0,0) -> (1,1) space to a space defined by an arbitrary quadrilateral (blX, blY) -> (trX, trY). The 4 corners of the quadrilateral are given ('bl' means bottom left, 'tr' means top right etc.).`mapQuadToUnitSquare(blX, blY, brX, brY, tlX, tlY, trX, trY)`→`None`: 

> Is the inverse of mapUnitSquareToQuad(). Mapping coordinates in an arbitrary quadrilateral into a space defined by the unit square.`fillTable(tableDAT)`→`None`: 

> Fill in the contents of a table from the matrix which the method is called upon. 
> 
>   * tableDAT - The table to be filled.
>`numpyArray()`→`numpy.ndarray`: 

> Returns this matrix as a 4x4 NumPy array.`identity()`→`None`: 

> Replaces the values in the matrix with the [identity matrix](<http://en.wikipedia.org/wiki/Identity_matrix>). 
[code]
>     m.identity() # now contains the identity matrix
>     
[/code]`copy()`→`TDU.Matrix`: 

> Returns a new matrix that is a copy of the matrix. 
[code]
>     newM = m.copy() # newM will have the same values as m, m is unchanged
>     
[/code]`translate(tx, ty, tz, fromRight=False)`→`None`: 

> Multiplies the current matrix by a new translation matrix created from tx, ty and tz. The translation is applied from the left of the matrix by default. That is to say, if T is the new translation matrix, and M is the current matrix, then the result of this operation is M = T * M. 
> 
>   * tx, ty, tz - The translation value in each axis.
>   * fromRight - (Keyword, Optional) If True, the translation matrix will be multiplied from the right instead of the left.
> 

[code]
>     m = tdu.Matrix()
>     m.translate(5, 0, 10)
>     
[/code]`rotate(rx, ry, rz, fromRight=False, pivot=None)`→`None`: 

> Multiplies the current matrix by 3 rotation matrices, first a rotation around the X axis by rx degrees, followed by a rotation around the Y axis by ry degrees, followed by the same for rz. The rotation values are in degrees. The rotation is applied from the left of the matrix by default. So if M is the current matrix, then the result of this operation is M = RZ * RY * RX * M. 
> 
>   * rx, ry, rz - The rotation value around each X, Y and Z axis. The value is in degrees. The rotation is applied in XYZ order.
>   * fromRight - (Keyword, Optional) If True, the rotation matrix will be multiplied from the right instead of the left. In this case the operation is M = M * RZ * RY * RX.
>   * pivot - (Keyword, Optional) If given, the rotation will be applied around the given pivot. The pivot should be a Vector, Position or a list with 3 entries.
> 

[code]
>     m = tdu.Matrix()
>     m.rotate(45, 0, 0)
>     
>     m = tdu.Matrix()
>     m.rotate(0, 0, 90, pivot=[0, 5, 0])
>     
>     m = tdu.Matrix()
>     p = tdu.Position(0, 5, 0)
>     m.rotate(0, 90, 0, pivot=p)
>     
[/code]`rotateOnAxis(rotationAxis, angle, fromRight=False, pivot=None)`→`None`: 

> Multiplies the current matrix by a new rotation matrix created by rotation angle degrees around the axis specified by rotationAxis. The angle is in degrees. The rotation is applied from the left of the matrix by default. That is to say, if R is the new rotation matrix specified by rotationAxis and angle, and M is the current matrix, then the result of this operation is M = R * M. 
> 
>   * rotationAxis - A axis to rotate around. This should be a Vector or a list with 3 entries. It does not need to be normalized.
>   * angle - The amount to rotate around the axis, specified in degrees.
>   * fromRight - (Keyword, Optional) If True, the rotation matrix will be multiplied from the right instead of the left.
>   * pivot - (Keyword, Optional) If given, the rotation will be applied around the given pivot. The pivot should be a Vector, Position or a list with 3 entries.
>`scale(sx, sy, sz, fromRight=False, pivot=None)`→`None`: 

> Multiplies the current matrix by a scale matrix created from sx, sy and sz. The scale is applied from the left of the matrix by default. That is to say, if S is the new scale matrix, and M is the current matrix, then the result of this operation is M = S * M. 
> 
>   * sx, sy, sz - The scale value along each X, Y and Z axis.
>   * fromRight - (Keyword, Optional) If True, the scale matrix will be multiplied from the right instead of the left.
>   * pivot - (Keyword, Optional) If given, the scale will be applied around the given pivot. The pivot should be a Vector, Position or a list with 3 entries.
> 

[code]
>     m = tdu.Matrix()
>     m.scale(2, 1, 1)
>     
>     m = tdu.Matrix()
>     m.scale(2, 1, 2, pivot=[0, 5, 0])
>     
>     m = tdu.Matrix()
>     p = tdu.Position(0, 5, 0)
>     m.scale(1, 2, 1, pivot=p)
>     
[/code]`lookat(eyePos, target, up)`→`None`: 

> Multiplies the current matrix by a lookat matrix created using the given values to the matrix. The lookat matrix is applied from the left of the matrix by default. That is to say, if L is the new lookat matrix, and M is the current matrix, then the result of this operation is M = L * M. The values for to parameters can be given as anything that can be treated as a list of 3 values. E.g a TDU.Vector, TDU.Position or simply a list of size 3. 
> 
>   * eyePos - The position in space of the eye/camera.
>   * target - The position in space that should be looked at, from the eyePos.
>   * up - The Up vector. Ensure the up vector isn't pointing in the same direction as the lookat direction.
> 

[code]
>     m = tdu.Matrix()
>     eyeP = tdu.Position(0, 0, -5)
>     target = tdu.Position(0, 5, 5)
>     up = tdu.Position(0, 1, 0)
>     m.lookat(eyeP, target, up)
>     
[/code]`decompose()`→`tuple[tuple, tuple, tuple]`: 

> Decomposes the matrix into its scale, rotate and translate values. These are the same as the translate, rotate and scale that are in the [Geometry COMP](<./Geometry_COMP.md> "Geometry COMP") and other Object components. However due to rotations being able to be solved in different ways, it's likely a decomposed transform matrix from a Geometry COMP will not have the same values as its parameter. The resulting transform is the same though. This function returns a tuple of tuples (3 tuples), which are the scale, rotate and translate values respectively. 
[code]
>     s, r, t = m.decompose()
>     
[/code]`projectionFrustum(left, right, bottom, top, near, far)`→`None`: 

> Replaces the contents of the matrix with a projection matrix using the given frustum extents. The left, right, bottom, top extents are located on the near plane. The depth range generated by this matrix will be [0,1] from near to far, as is required by Vulkan.`projectionFovX(fovX, aspectX, aspectY, near, far)`→`None`: 

> Replaces the contents of the matrix with a projection matrix defined by the FOV(given in degrees), an aspect ratio and near/far planes. The depth range generated by this matrix will be [0,1] from near to far, as is required by Vulkan. 
> 
>   * fovX - The horizontal FOV, specified in degrees.
>   * aspectX, aspectY - The aspect ration values. These can be something like 16 and 9 for an aspect or the render resolution such as 1920 and 1080. The results will be the same for the same ratio.
>`projectAndClip(pos : TDU.Position)`→`TDU.Position | None`: 

> Applies a projection matrix to a position if it's within the normalized clip space. Returns None if projected position is clipped. 
> 
>   * pos - The position to be projected.
>`projectionStereo(ipd : float, convergeZ : float, fovX : float, aspectX : float, aspectY : float, near : float, far : float, rightEye : bool=False)`→`None`: 

> Replaces the contents of the matrix with an asymetrical projection matrix suitable for stereo rendering. The left eye's projection matrix is given by default, set rightEye=True to get the right eye's instead. For proper rendering, the cameras will also need to be translated in X by -ipd/2 and +ipd/2 for the left and right eyes respectively. The depth range generated by this matrix will be [0,1] from near to far, as is required by Vulkan. 
> 
>   * ipd - Interpupillary distance of the user, generally specified in meters. Typically between 0.05 and 0.08
>   * covergeZ - distance in Z from the camera where the stereo convergence should occur, in the same units as ipd.
>   * fovX - The field of view in the X direction, in degrees.
>   * aspectX, aspectY - The aspect ratio values. These can be something like 16 and 9 for an aspect or the render resolution such as 1920 and 1080. The results will be the same for the same ratio.
>   * near, far - The near and far plane distances.
>   * rightEye - (Keyword, Optional) If set to True, the matrix will contain the projection for the right eye, otherwise it will contain the projection for the left eye.
> 

### Special Functions`[row, column]`→`float`: 

> Gets or sets the specified entry in the matrix. 
[code]
>     tx = m[0, 3]
>     m[0, 3] = tx + 5
>     
[/code]`Matrix * Matrix`→`TDU.Matrix`: 

> Performs a matrix multiplication returns the results in a new matrix. 
[code]
>     newM = m1 * m2
>     
[/code]`Matrix - Matrix`→`TDU.Matrix`: 

> Subtracts the matrices, component-by-component, and returns the results in a new matrix.`Matrix + Matrix`→`TDU.Matrix`: 

> Adds the matrices, component-by-component, and returns the results in a new matrix`Matrix * [TDU.Vector](<./Vector_Class.md> "Vector Class")`→`[TDU.Vector](<./Vector_Class.md> "Vector Class")`: 

> Multiplies the vector by the matrix and returns the a new vector as the result. Since a Vector is direction only and has no notion of a position, the translate part of the matrix does not get applied to the vector. 
[code]
>     newV = M * v
>     
[/code]`Matrix * [TDU.Position](<./Position_Class.md> "Position Class")`→`[TDU.Position](<./Position_Class.md> "Position Class")`: 

> Multiplies the position by the matrix and returns the a new position as the result. If the matrix was not an transformation matrix, such as a projection matrix instead, the perspective divide by W will automatically be applied to X, Y and Z. 
[code]
>     newP = M * p
>     
[/code]

TouchDesigner Build: Latest\nwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditormw-rollbackmw-revertedmw-revertedmw-reverted2025.300002022.241402021.100002018.28070before 2018.28070
