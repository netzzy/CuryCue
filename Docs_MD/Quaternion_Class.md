# Quaternion Class

Holds a Quaternion object which can be used to manipulate rotations in various ways.   
  
**Note:** tdu.___ and TDU.___ can be used interchangeably. In general, TDU.___ is used to represent a class, while tdu.___ is used for the instantiator function. 

Quaternions can be constructed using a few different ways to describe the initial rotation: 
[code] 
    # From Euler Angles, rx, ry, rz in degrees
    q = tdu.Quaternion(30, 5, -5)
    q = tdu.Quaternion([30, 5, -5])
    # From an angle and a rotation axis
    q = tdu.Quaternion(30, tdu.Vector(0, 1, 0))
    # From two vectors, rotate from the first vector to the 
    second vector
    q = tdu.Quaternion(tdu.Vector(1, 0, 0), tdu.Vector(0, 1, 0))
    # From a set of 4 quaternion values
    q = tdu.Quaternion(x, y, z, w)
    q = tdu.Quaternion([x, y, z, w])
    # From a Matrix
    q = tdu.Quaternion(tdu.Matrix())
    # From a quaternion
    q = tdu.Quaternion(tdu.Quaternion())
    
[/code]

Quaternions can be used like simple Python lists: 
[code] 
    print(q[1])		# same as q.y
    q[2] = 0		# same as q.z
    
[/code]

See also [Transform CHOP](<./Transform_CHOP.md> "Transform CHOP") which accepts, manipulates and outputs quaternions as sets of CHOP channels. 

## Instantiators`TDU.Quaternion(*args)`→`TDU.Quaternion`: 

> The following argument forms are valid instantiators: 
> 
>   *`tdu.Quaternion()`\- (0, 0, 0, 1)
>   *`tdu.Quaternion(quaternion : TDU.Quaternion)`\- copy the quaternion in the argument
>   *`tdu.Quaternion(rx : float, ry : float, rz : float)`\- from Euler angles in degrees
>   *`tdu.Quaternion(rot : float, axis: [TDU.Vector](<./Vector_Class.md> "Vector Class"))`\- from a rotation angle and a rotational axis
>   *`tdu.Quaternion(v1 : [TDU.Vector](<./Vector_Class.md> "Vector Class"), v2: [TDU.Vector](<./Vector_Class.md> "Vector Class"))`\- rotate from v1 to v2
>   *`tdu.Quaternion(x : float, y : float, z : float, w : float)`\- from quaternion values
>   *`tdu.Quaternion(xyzw : list)`\- from quaternion values in a list
>   *`tdu.Quaternion(matrix : TDU.Matrix)`\- from a matrix
> 

## Members`x`→`float`: 

> Get or set the x component of the quaternion.`y`→`float`: 

> Get or set the y component of the quaternion.`z`→`float`: 

> Get or set the z component of the quaternion.`w`→`float`: 

> Get or set the w component of the quaternion.

## Methods`lerp(q2, factor)`→`TDU.Quaternion`: 

> Returns the linear interpolation of the quaternion with another quaternion and an interpolation factor. 
> 
> The quaternion argument can be anything from which a quaternion can be derived ie. (x,y,z,w), Matrix, etc. The interpolation factor must be between 0 and 1. 
[code] 
>     q3 = q.lerp(q2, factor)
>     
[/code]`length()`→`float`: 

> Returns the length of the quaternion. 
[code]
>     l = q.length()
>     
[/code]`cross(q2)`→`TDU.Vector`: 

> Returns the cross product of the quaternion and argument. 
> 
> The quaternion argument can be anything from which a quaternion can be derived ie. (x,y,z,w), Matrix, etc. 
[code] 
>     l = q.cross(q2)
>     
[/code]`rotate(vec)`→`TDU.Vector`: 

> Rotates a vector using the current quaternion. Returns a new vector. 
[code]
>     v2 = q.rotate(v1)
>     
[/code]`slerp(q2, factor)`→`TDU.Quaternion`: 

> Returns the spherical interpolation of the quaternion with another quaternion and an interpolation factor. 
> 
> The quaternion argument can be anything from which a quaternion can be derived ie. (x,y,z,w), Matrix, etc. 
[code] 
>     q3 = q.slerp(q2, factor)
>     
[/code]`eulerAngles(order='xyz')`→`tuple`: 

> Returns euler angles in degrees as a tuple (i.e. pitch as x, yaw as y, roll as z) from current quaternion and a rotation order. The 'order' argument can be set to any valid rotation order which by default is set to 'xyz'. 
[code]
>     r = q.eulerAngles(order='xyz')
>     
[/code]`fromEuler(order='xyz')`→`tuple`: 

> Returns and set the current quaternion from euler angles in degrees as a 3 inputs argument (i.e. pitch as x, yaw as y, roll as z). The 'order' argument can be set to any valid rotation order which by default is set to 'xyz'. 
[code]
>     r = q.fromEuler(order='xyz')
>     
[/code]`axis()`→`TDU.Vector`: 

> Returns the rotation axis vector of the quaternion. 
[code]
>     v = q.axis()
>     
[/code]`dot(q2)`→`float`: 

> Returns the dot product of the quaternion and the argument. 
> 
> The quaternion argument can be anything from which a quaternion can be derived ie. (x,y,z,w), Matrix, etc. 
[code] 
>     l = q.dot(q2)
>     
[/code]`exp()`→`TDU.Quaternion`: 

> Returns the exponential of the quaternion as a new quaternion. 
[code]
>     q2 = q.exp()
>     
[/code]`copy()`→`TDU.Quaternion`: 

> Creates a copy of the quaternion with separate values.`log()`→`TDU.Quaternion`: 

> Returns the natural logarithm of the current quaternion as a new quaternion. 
[code]
>     l = q.log()
>     
[/code]`inverse()`→`None`: 

> Invert the quaternion in place. 
[code]
>     q.inverse()
>     
[/code]`angle()`→`float`: 

> Returns the rotation angle (in degrees) of the quaternion. 
[code]
>     a = q.angle()
>     
[/code]

### Special Functions`Quaternion *= Quaternion`→`TDU.Quaternion`: 

> Applies the rotation of one quaternion to another quaternion. 
[code]
>     # apply rotation of q2 to q1
>     q1 *= q2
>     
[/code]

TouchDesigner Build: Latest\nwikieditorwikieditor2025.300002021.100002018.28070before 2018.28070
