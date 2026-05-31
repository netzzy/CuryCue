# Position Class

The position class holds a single 3 component position. A position is a single point in space, and it's important to use a position or [vector](<./Vector_Class.md> "Vector Class") as appropriate for the data that is being calculated, since matrix operations on them will end in different results. When being multiplied by a [Matrix](<./Matrix_Class.md> "Matrix Class"), this class will implicitly have a 4th component (W component) of 1. If the Matrix is a projection matrix that will cause the W component to become something other than 1, all 4 components will be divided by W to make the position homogeneous again. A new position can be created without any arguments, with 3 arguments for the x,y,z values, or with a single argument which is a variable that has 3 entries such as a list of length 3, or another position or vector. 

**Note:** tdu.___ and TDU.___ can be used interchangeably. In general, TDU.___ is used to represent a class, while tdu.___ is used for the instantiator function. 

Examples of creating a position: 
[code] 
    p = tdu.Position() # starts as (0, 0, 0)
    p2 = tdu.Position(1, 5, 0)
    values = [0, 1, 0]
    p3 = tdu.Position(values)
    
[/code]

## Instantiators`TDU.Position(*args)`→`TDU.Position`: 

> Create a new position object. The following argument forms are valid instantiators: 
> 
>   *`tdu.Position()`\- (0, 0, 0)
>   *`tdu.Position(vector : TDU.Vector)`\- copy the vector values
>   *`tdu.Position(position: TDU.Position)`\- copy the position
>   *`tdu.Position(x : float, y : float, z : float)`\- (x, y, z)
>   *`tdu.Position(f : float)`\- (f, f, f)
>   *`tdu.Position(pos : list)`\- 3 item list to fill position
> 

## Members`x`→`float`: 

> Gets or sets the X component of the position.`y`→`float`: 

> Gets or sets the Y component of the position.`z`→`float`: 

> Gets or sets the Z component of the position.

## Methods`translate(x, y, z)`→`None`: 

> Translates the position by the specified values. 
> 
>   * x, y, z - The values to translate by.
> 

[code]
>     p.translate(5, 2, 0)
>     
[/code]`scale(x, y, z)`→`None`: 

> Scales each component of the position by the specified values. 
> 
>   * x, y, z - The values to scale each component of the position by.
> 

[code]
>     p.scale(1, 2, 1)
>     
[/code]`copy()`→`TDU.Position`: 

> Returns a new position that is a copy of the position. 
[code]
>     newV = v.copy()
>     
[/code]

### Special Functions`TDU.Position[i]`→`float`: 

> Gets or sets the component of the position specified by i, where i can be 0, 1, or 2. 
[code]
>     y = p[1]
>     p[1] = y + 2.0
>     
[/code]`TDU.Position * float`→`TDU.Position`: 

> Scales the position by the give float scalar and returns a new Position as the result. 
[code]
>     p = p * 0.1
>     p = 0.1 * p
>     
[/code]`TDU.Position + float`→`TDU.Position`: 

> Adds the given scalar to all 3 components of the position and returns a new position as the result. 
[code]
>     p = p + 1.2
>     p = 1.2 + p
>     
[/code]`TDU.Position - float`→`TDU.Position`: 

> Subtracts the given scalar from all 3 components of the position and returns a new position as the result. 
[code]
>     p = p - 1.2
>     p = 1.2 - p
>     
[/code]`TDU.Vector + TDU.Position`→`TDU.Position`: 

> Adds the vector to the position. ie. it displaces the given position by the vector. Returns a new position as the result. 
[code]
>     p2 = v + p1
>     p2 = p1 + v
>     
[/code]`TDU.Position - TDU.Vector`→`TDU.Position`: 

> Subtracts the vector from the position. Notice that the reverse is not a legal operation: subtracting a position from a vector does not have any meaning. Returns a new position with the results. 
[code]
>     p2 = p1 - v
>     
[/code]`TDU.Position - TDU.Position`→`TDU.Vector`: 

> Subtracts the two positions to create a vector that is pointing from the 2nd one to the 1st one, with length equal to the distance between the positions. 
[code]
>     v = p1 - p2
>     
[/code]`TDU.Position += float`→`None`: 

> Adds the given scalar to all 3 components of the position, the position will contain the result of the operation. 
[code]
>     p += 0.1
>     
[/code]`TDU.Position += TDU.Vector`→`None`: 

> Displaces the position by the given vector, the position will contain the result of the operation. 
[code]
>     p += v
>     
[/code]`TDU.Position -= float`→`None`: 

> Subtracts the given scalar from all 3 components of the position, the position will contain the result of the operation. 
[code]
>     p -= 0.4
>     
[/code]`TDU.Position -= TDU.Vector`→`None`: 

> Displaces the position by the given vector, the position will contain the result of the operation. 
[code]
>     p -= v
>     
[/code]`TDU.Matrix * TDU.Position`→`TDU.Position`: 

> Multiplies the Position by the matrix and returns the a new position as the result. 
[code]
>     p2 = m * p1
>     
[/code]`TDU.Position / float`→`TDU.Position`: 

> Divides each component of the position by the scalar and returns the a new position as the result. 
[code]
>     p2 = p1 / 2.0
>     
[/code]`TDU.Position *= TDU.Matrix`→`None`: 

> Multiplies the position by the matrix, the position will contain the result. The is position multiplied on the right of the matrix. It is the equivalent of doing Position = Matrix * Position. 
[code]
>     p *= m
>     
[/code]`TDU.Position *= float`→`None`: 

> Scales all 3 components of the position by the given scalar. The position will contain the result. 
[code]
>     p *= 1.3
>     
[/code]`TDU.Position *= TDU.Position`→`None`: 

> Component-wise multiplies the 3 components of the first position by the 3 components of the 2nd position. 
[code]
>     p1 *= p2
>     
[/code]`abs(TDU.Position)`→`TDU.Position`: 

> Returns a new position with all 3 components being the absolute value of the given position's components. 
[code]
>     p2 = abs(p1)
>     
[/code]`-TDU.Position`→`TDU.Position`: 

> Returns a new position with all 3 component's being negated. 
[code]
>     p2 = -p1
>     
[/code]

TouchDesigner Build: Latest\n2025.300002021.100002018.28070before 2018.28070
