# Vector Class

The vector class holds a single 3 component vector. A vector describes a direction in space, and it's important to use a vector or [Position](<./Position_Class.md> "Position Class") as appropriate for the data that is being calculated. When being multiplied by a [Matrix](<./Matrix_Class.md> "Matrix Class"), this class will implicitly have a 4th component (W component) of 0. A new vector can be created without any arguments, with 3 arguments for the x,y,z values, or with a single argument which is a variable that has 3 entries such as a list of length 3, or a position or vector. 

**Note:** tdu.___ and TDU.___ can be used interchangeably. In general, TDU.___ is used to represent a class, while tdu.___ is used for the instantiator function. 

Examples of creating a vector: 
[code] 
    v = tdu.Vector() # starts as (0, 0, 0)
    v2 = tdu.Vector(0, 0, -1)
    values = [0, 1, 0]
    v3 = tdu.Vector(values)
    
    # vectors can be accessed like Python lists
    print(v3[1])	# same as v3.y
    v3[2] = 1		# same as v3.z
    
[/code]`TDU.Vector(*args)`→`TDU.Vector`: 

> Create a new vector object. The following argument forms are valid instantiators: 
> 
>   *`tdu.Vector()`\- (0, 0, 0)
>   *`tdu.Vector(vector : TDU.Vector)`\- copy the vector
>   *`tdu.Vector(position: TDU.Position)`\- copy the position values
>   *`tdu.Vector(x : float, y : float, z : float)`\- (x, y, z)
>   *`tdu.Vector(f : float)`\- (f, f, f)
>   *`tdu.Vector(vec : list)`\- 3 item list to fill vector
> 


}} 

## Members`x`→`float`: 

> Gets or sets the X component of the vector.`y`→`float`: 

> Gets or sets the Y component of the vector.`z`→`float`: 

> Gets or sets the Z component of the vector.

## Methods`angle(vec)`→`float`: 

> Returns the angel (in degrees) between the current vector and specified vector (vec). 
[code]
>     d = v.angle(v2)
>     
[/code]`scale(x, y, z)`→`None`: 

> Scales each component of the vector by the specified values. 
> 
>   * x, y, z - The values to scale each component of the vector by.
> 

[code] 
>     v.scale(1, 2, 1)
>     
[/code]`normalize()`→`None`: 

> Makes the length of this vector 1. 
[code]
>     m.normalize()
>     
[/code]`length()`→`float`: 

> Returns the length of this vector. 
[code]
>     l = m.length()
>     
[/code]`lengthSquared()`→`float`: 

> Returns the squared length of this vector. 
[code]
>     l = v.lengthSquared()
>     
[/code]`copy()`→`TDU.Vector`: 

> Returns a new vector that is a copy of the vector. 
[code]
>     newV = v.copy()
>     
[/code]`distance(vec)`→`float`: 

> Returns the distance of the current vector to specified vector (vec). 
[code]
>     l = v.distance(v2)
>     
[/code]`lerp(vec2, t)`→`TDU.Vector`: 

> Returns the linear interpolation of this vector and vec2. That is vec1 * (1.0 - t) + vec2 * t, where vec1 is the current vector. The value for t is not restricted to the range [0, 1]. 
[code]
>     l = v.lerp(v2, t)
>     
[/code]`slerp(vec2, t)`→`TDU.Vector`: 

> Returns the spherical interpolation of this vector and vec2. The value for t is not restricted to the range [0, 1]. 
[code]
>     l = v.slerp(v2, t)
>     
[/code]`dot(vec)`→`float`: 

> Returns the dot product of this vector and the passed vector. 
> 
>   * vec - The other vector to use to calculate the dot product
> 

[code] 
>     d = v.dot(otherV)
>     
[/code]`cross(vec)`→`TDU.Vector`: 

> Returns the cross product of this vector and the passed vector. The operation is self cross vec. 
> 
>   * vec - The other vector to use to calculate the cross product.
> 

[code] 
>     c = v.cross(otherV)
>     
[/code]`project(vec1, vec2)`→`None`: 

> Projects this vector onto the plan defined by vec1 and vec2. Both vec1 and vec2 must be normalized. The result may not be normalized. 
> 
>   * vec1, vec2 - The vectors that specify the plane to project onto. Must be normalized.
> 

[code] 
>     v.project(v1, v2)
>     
[/code]`reflect(vec)`→`None`: 

> Reflects the current vector about the specified vector (vec). 
[code]
>     v.reflect(v2)
>     
[/code]

### Special Functions`TDU.Vector[i]`→`float`: 

> Gets or sets the component of the vector specified by i, where i can be 0, 1, or 2. 
[code]
>     y = v[1]
>     v[1] = y * 2.0
>     
[/code]`TDU.Vector * float`→`TDU.Vector`: 

> Scales the vector by the give float scalar and returns a new vector as the result. 
[code]
>     v = v * 2.0
>     v = 2.0 * v
>     
[/code]`TDU.Vector + float`→`TDU.Vector`: 

> Adds the given scalar to all 3 components of the vector and returns a new vector as the result. 
[code]
>     v = v + 5.0
>     v = 5.0 + v
>     
[/code]`TDU.Vector - float`→`TDU.Vector`: 

> Subtracts the given scalar from all 3 components of the vector and returns a new vector as the result. 
[code]
>     v = v - 1.5
>     v = 1.5 - v
>     
[/code]`TDU.Vector + TDU.Vector`→`TDU.Vector`: 

> Adds the two vectors to create a new vector. 
[code]
>     v3 = v1 + v2
>     
[/code]`TDU.Vector - TDU.Vector`→`TDU.Vector`: 

> Subtracts the two vectors to create a new vector. 
[code]
>     v3 = v1 - v2
>     
[/code]`TDU.Vector += TDU.Vector`→`TDU.Vector`: 

> Adds the 2nd vector to the 1st vector, the 1st vector will contain the result of the operation. 
[code]
>     v1 += v2
>     
[/code]`TDU.Vector += float`→`TDU.Vector`: 

> Adds the given scalar to all 3 components of the vector, the vector will contain the result of the operation. 
[code]
>     v1 += 0.4
>     
[/code]`TDU.Vector -= TDU.Vector`→`TDU.Vector`: 

> Subtracts the 2nd vector from the 1st vector, the 1st vector will contain the result of the operation. 
[code]
>     v1 -= v2
>     
[/code]`tdu.Matrix * TDU.Vector`→`TDU.Vector`: 

> Multiplies the vector by the matrix and returns the a new vector as the result. Since a Vector is direction only and has no notion of a position, the translate part of the matrix does not get applied to the vector. 
[code]
>     v = M * v
>     
[/code]`TDU.Vector / float`→`TDU.Vector`: 

> Divides each component of the vector by the scalar and returns the a new vector as the result. 
[code]
>     v = v / 0.2
>     
[/code]`TDU.Vector *= tdu.Matrix`→`TDU.Vector`: 

> Multiplies the vector by the matrix, the vector will contain the result. The vector is multiplied on the right of the matrix. This is the same as doing v = M * v, although more efficient since it doesn't require assigning a new vector to v. Since a Vector is direction only and has no notion of a position, the translate part of the matrix does not get applied to the vector. 
[code]
>     v *= M
>     
[/code]`TDU.Vector *= float`→`TDU.Vector`: 

> Scales all 3 components of the vector by the given scalar. The vector will contain the result. 
[code]
>     v *= 1.1
>     
[/code]`TDU.Vector *= TDU.Vector`→`TDU.Vector`: 

> Does a component-wise scale of all 3 components of the vector by the components of the 2nd vector. The vector will contain the result. 
[code]
>     v1 *= v2
>     
[/code]`abs(TDU.Vector)`→`TDU.Vector`: 

> Returns a new vector with all 3 components being the absolute value of the given vector's components. 
[code]
>     v2 = abs(v1)
>     
[/code]`-TDU.Vector`→`TDU.Vector`: 

> Returns a new vector with all 3 components being negated. 
[code]
>     v2 = -v1
>     
[/code]

TouchDesigner Build:  Latest\n2025.30000 2021.10000 2018.28070 before 2018.28070
