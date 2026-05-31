# Object COMP Xform Page

## Parameters - Xform Page  
  
The Xform parameter page controls the object component's transform in world space. 

Transform Order`xord`\- The menu attached to this parameter allows you to specify the order in which the changes to your Component will take place. Changing the Transform order will change where things go much the same way as going a block and turning east gets you to a different place than turning east and then going a block. In matrix math terms, if we use the 'multiply vector on the right' (column vector) convention, a transform order of Scale, Rotate, Translate would be written as`translate * rotate * scale * vectorOrPosition`. 

Rotate Order`rord`\- The rotational matrix presented when you click on this option allows you to set the transform order for the Component's rotations. As with transform order (above), changing the order in which the Component's rotations take place will alter the Component's final position. 

Translate / Rotation / Scale`t[xyz] r[xyz] s[xyz]`\- The three fields allow you to specify the amount of movement along any of the three axes; the amount, in degrees, of rotation around any of the three axes; and a non-uniform scaling along the three axes. As an alternative to entering the values directly into these fields, you can modify the values by manipulating the Component in the Viewport with the Select & Transform state. 

Pivot`p[xyz]`\- The Pivot point edit fields allow you to define the point about which a Component scales and rotates. Altering the pivot point of a Component produces different results depending on the transformation performed on the Component. 

For example, during a scaling operation, if the pivot point of an Component is located at`-1, -1, 0`and you wanted to scale the Component by`0.5`(reduce its size by 50%), the Component would scale toward the pivot point and appear to slide down and to the left. 

In the example above, rotations performed on an Component with different pivot points produce very different results. 

Uniform Scale`scale`\- This field allows you to change the size of an Component uniformly along the three axes. 

**Note:** Scaling a camera's channels is not generally recommended. However, should you decide to do so, the rendered output will match the Viewport as closely as possible when scales are involved. 

Constrain To`constrain`\- Allows the location of the object to be constrained to any other object whose path is specified in this parameter. 

Look At`lookat`\- Allows you to orient your Component by naming the Component you would like it to Look At, or point to. Once you have designated this Component to look at, it will continue to face that Component, even if you move it. This is useful if, for instance, you want a camera to follow another Component's movements. The Look At parameter points the Component in question at the other Component's origin. 

**Tip:** To designate a center of interest for the camera that doesn't appear in your scene, create a Null Component and disable its display flag. Then Parent the Camera to the newly created Null Component, and tell the camera to look at this Component using the Look At parameter. You can direct the attention of the camera by moving the Null Component with the Select state. If you want to see both the camera and the Null Component, enable the Null Component's display flag, and use the Select state in an additional Viewport by clicking one of the icons in the top-right corner of the TouchDesigner window. 

Look At Up Vector`lookup`\- When specifying a Look At, it is possible to specify an up vector for the lookat. Without using an up vector, it is possible to get poor animation when the lookat Component passes through the Y axis of the target Component. 
* Don't Use Up Vector - Use this option if the look at Component does not pass through the Y axis of the target Component.
  * Use Up Vector - This precisely defines the rotates on the Component doing the looking. The Up Vector specified should not be parallel to the look at direction. See Up Vector below.
  * Use Quaternions - Quaternions are a mathematical representation of a 3D rotation. This method finds the most efficient means of moving from one point to another on a sphere.


Path SOP`pathsop`\- Names the SOP that functions as the path you want this Component to move along. For instance, you can name an SOP that provides a spline path for the camera to follow. 

Production Tip: For Smooth Motion Along a Path \- Having a Component follow an animation path is simple. However, when using a NURBS curve as your path, you might notice that the Component speeds up and slows down unexpectedly as it travels along the path. This is usually because the CVs are spaced unevenly. In such a case, use the [Resample SOP](<./Resample_SOP.md> "Resample SOP") to redistribute the CVs so that they are evenly spaced along the curve. A caution however - using a Resample SOP can be slow if you have an animating path curve. 

An alternative method is to append a [Basis SOP](<./Basis_SOP.md> "Basis SOP") to the path curve and change it to a`Uniform Curve`. This way, your Component will move uniformly down the curve, and there is no need for the Resample SOP and the unnecessary points it generates. 

Roll`roll`\- Using the angle control you can specify a Component's rotation as it animates along the path. 

Position`pos`\- This parameter lets you specify the Position of the Component along the path. The values you can enter for this parameter range from`0`to`1`, where`0`equals the starting point and`1`equals the end point of the path. The value slider allows for values as high as`10`for multiple "passes" along the path. 

Orient Along Path`pathorient`\- If this option is selected, the Component will be oriented along the path. The positive Z axis of the Component will be pointing down the path. 

Up Vector`up`\- When orienting a Component, the Up Vector is used to determine where the positive Y axis points. 

Auto-Bank Factor`bank`\- The Auto-Bank Factor rolls the Component based on the curvature of the path at its current position. To turn off auto-banking, set the bank scale to`0`.
