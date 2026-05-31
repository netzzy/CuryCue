# Spline

TouchDesigner allows you to create both Bézier and NURBS curves and surfaces (for the purposes of this discussion, however, we'll only be referring to curves). Spline curves and polygons are collectively termed "faces", while grids and spline surfaces are termed "hulls". As opposed to polygonal types, NURBS and Bézier entities are inherently smooth primitives known as splines. It isn't necessary to master the mathematics behind what differentiates the two spline types. It is, however, useful to understand some of the concepts that arise from the mathematics of computer-generated curves because they affect your choice of curve type when you start creating in TouchDesigner, and they influence the way you draw that curve.   
  
#### Linear Splines

The most straight-forward way of drawing a curve is by connecting a sequence of points. The resulting curve is a linear spline, and is equivalent to a polygon. There are two major drawbacks to this method of producing a curve. First, in order to produce anything that actually appears curved, you would need a large number of points. Storing and computing all those points is not an efficient use of the computer's resources. Second, manipulating a curve created in this fashion is very cumbersome because, once a point is moved, you lose the smoothness of the shape. 

#### Higher Degree Splines

The way around the jaggedness produced by linear connectivity is through a series of blending functions. The blending functions, or bases, are the mathematical foundation for generating a smooth connection between the control vertices (CVs) of the curve. A spline curve generates a smooth transition between its control vertices by a mathematical blending function that operates on these points. The set of CVs controlling the curve is referred to as the "hull". 

#### Curve Segments

NURBS and Bézier curves in TouchDesigner are piecewise curves made of a number of connected curve segments. The main difference between NURBS and Bézier curves is the level of continuity at the points where the curve segments touch. A NURBS curve will typically be very smooth at these joints (the higher the degree of the blending function, the smoother the connection). Bézier curves have a discontinuity every degree plus one points. 

#### Orders

The "degree plus one" formulation is often referred to as the order of the curve. A cubic curve, for example, has a degree of three and, therefore, an order of four. 

The degree of the spline is given by the degree of the underlying blending functions. TouchDesigner supports splines whose degrees vary from 1 to 10. The upper bound was chosen for practical reasons and efficiency. 

You'll find that cubic splines are sufficiently smooth and well behaved for most applications. You will seldom need to use other degrees. 

_In the image above - On the left is a Linear spline (degree 1, order 2), in the middle a Quadratic spline (degree 2, order 3) and on the right a Cubic spline (degree 3, order 4)._

From this illustration, we can see that the minimum number of points needed to build a curve equals the order of that curve, unless the curve is closed, in which case only degree CVs will suffice, since the remaining CV is taken to be equivalent to the first CV. 

#### Breakpoints, Knots, and Spline Basis

The point where curve segments come together is called a breakpoint. It is important to stress that this breakpoint is on the curve itself, not away from the curve like the CVs, which make up the hull. 

Breakpoints are images of special values, called "knots", in what is known as the parametric space or the domain of the spline. The domain, which is simply a sequence of knots in ascending order, together with the spline order and the spline type define a spline basis. 

Imagine the domain of a curve as a segment going from zero to one or (for example) -12.7 to 83.2, whose size and origin are given by the values of its two end-knots. 

Similarly, a surface is defined by two knot sequences forming a rectangular (U,V) domain. The knot sequences must always be sorted in ascending order. 

_Relations of World Space and Domain Space_

Since knots are the ingredients of the domain, they divide a curve's domain segment and a surface's domain rectangle into smaller pieces whose size relative to each other is often more important than the total size of the domain. Similarly, in world space, the areas delimited by breakpoints divide a curve into curve segments and a surface into patches. 

Depending on the type of spline, the relative knot distances usually determine the shape of the spline given a fixed set of control vertices. The size and the origin of the domain are relevant when identifying a surface's texture space with its parametric space. Then, if the texture is expected to cover the entire surface only once, the domain of the surface must be a unit square. Mapping a domain to a new range and origin does not affect the shape of the spline primitive because the knot ratios are preserved. 

The knots need not be evenly spaced in the domain. The more knots there are in one area, the smaller the spline segments and, therefore, you have a greater degree of control over the spline in that area. If several knots are placed at one value, something called a multiplicity is produced. Not all spline types allow multiplicities to occur. 

#### Rational Splines

TouchDesigner supports two types of rational splines: NURBS, and Bézier. Each CV of the curve has X, Y, and Z coordinates that determine its position in world space. There is also a fourth component for each CV called W. The W component determines a CV's weight (see also: Point Weight (W) ). The weight determines the "pull" (like a magnet) of a CV on the spline curve. The value of the W component makes a spline rational or non-rational. A non-rational spline has only equal weights (typically, W=1), while a rational spline contains at least one different weight. While non-positive weights (where W is less than or equal to zero) make sense in theory, they tend to generate unintuitive shapes and cause the spline to break away from its convex hull. For practical reasons, TouchDesigner supports only positive weights (W > 0). 

The higher the weight of a CV, the sharper the spline around that CV. For large weight values, the spline will almost go through the CV. Similarly, weights smaller than one tend to flatten the spline in the area influenced by that CV. 

The effect of CV weight is shown below. 

However, it isn't simply the size of the weight that causes a fluctuation in sharpness. An equally, if not more, important element is the relative difference between weights. The more equal the neighboring weights, the smaller their influence over the given region and, consequently, the less rational the spline. For example, if all the weights of a spline curve are one thousand, the shape of the curve will be identical to a non-rational curve. 

In TouchDesigner, certain models, like the perfect NURBS circles, are normally built rationally. Although you can create rational models yourself in the modeler and elsewhere, we recommend that you use weights sparingly because they increase the complexity of the model (which may result in decreased system performance) and they may also lose their effectiveness when applied to neighboring curve regions. 

Of the spline types supported in TouchDesigner, NURBS curves give you a greater degree of control over local portions of the curve and over its smoothness. 

#### NURBS Curves and Surfaces

NURBS is an acronym for Non-Uniform Rational B-Spline. A NURBS curve employs a series of blending functions called "bases" to generate a smooth curve from a sequence of control vertices (CV's) which define a NURBS hull. 

The primary advantage of using a NURBS curve is that moving a CV only affects a local portion of the spline while also maintaining the continuity of the curve, even at its breakpoints. This allows you to "pull and tug" on the CVs of the NURBS curve or surface to generate a desired shape without causing kinks or discontinuities. 

The shape of a NURBS curve is greatly influenced by the relative distances between its knots. The knots appear in ascending order, and are possibly repeated. A repeated knot is said to have a multiplicity. 

In a Bézier curve, all knots are unique and, therefore, multiplicities aren't produced. The parallel between Bézier and NURBS knots is that a Bézier knot is similar to a NURBS knot with maximum multiplicity. The Bézier discontinuities mentioned earlier happen at these knots. Similarly, a NURBS curve will have a discontinuity where a knot is at maximum multiplicity. Maximum multiplicity occurs when a knot is repeated degree times in a NURBS basis. Both NURBS and Bézier curves will have a CV on the curve at the point of discontinuity. 

If the multiplicity happens at the end of the curve, the NURBS curve is considered "clamped." Typically, NURBS curves are clamped at both ends but closed curves are usually unclamped; Bézier curves are always clamped. 

From this, it follows that the shape of a NURBS curve, given a set of CVs, is determined by the relative distance between knots. Typically, there are two types of knot parametrizations: uniform and chord length. In the first, knots are spaced evenly. In the second, the distances between knots are determined by the distances between successive CVs. Uniform parametrization is recommended for regular shapes while chord length is used for free-form shapes. A third type of parametrization, called "centripetal", is similar to chord length and is best suited for sharp curves. 

##### Creating a Sharp Point in a NURBS Curve

It is sometimes desirable to simulate a discontinuity (a sharp corner point) along a NURBS curve. This can be done one of three ways: 
1. Change the weight of a selected CV via the Curve > Parameters dialog in the [SOP Editor](<./SOP_Editor.md> "SOP Editor") to something high like 10,000. This gives the CV so much "pull" that it draws the curve almost right through it.
  2. If you drag the two adjacent CVs of a cubic curve onto a middle CV, it will look like a sharp corner point. When this is done, it is called raising the Multiplicity of the CV. Maximum CV multiplicity occurs when adjacent "degree" CVs overlap.
  3. Make "degree" knots identical. When this is done, it is called raising the multiplicity of the knot. You can do this in the Refine SOP by choosing the Subdivision option, or in the Model Editor by selecting the Refine state and dividing with the middle mouse button.

##### Clamped and Unclamped NURBS Curves

A clamped curve touches its endpoints. An unclamped curve doesn't. Much of the time you will work with clamped curves. The unclamped case is generally useful for closed curves. 

In TouchDesigner, you can build closed NURBS curves, and these can be clamped or unclamped (see below). A closed, clamped curve will show a discontinuity where the two end points touch. 

There are four types of end point conditions for NURBS curves: 

You can experiment with these properties-both for curves and for surfaces in the Curve/Hull page of the [Primitive SOP](<./Primitive_SOP.md> "Primitive SOP"). 

##### Periodic Curves

A closed unclamped curve will wrap around itself, and is known as a periodic curve because the knots of the wrapped portion are actually a cyclical repetition of the original knots. When you save a periodic NURBS curve to a file, the periodic knots are not saved, but are generated automatically upon loading the file. 

#### NURBS Surfaces

A NURBS surface has a topology similar to that of a [Mesh](<./Mesh.md> "Mesh") primitive. In a NURBS surface, each node of the UV coordinate matrix represents a CV connected by rows and columns to form a NURBS hull. This allows modeling of complex smooth surfaces, whose shape is changeable simply by moving the CVs. 

**TIP:** To create an open cubic NURBS surface, you need at least 4 x 4 CVs. In general, for an open surface with U Order m, and V Order n, you need m x n CVs. For an open NURBS curve of order m, you will need at least m CVs to define it properly. 

#### Bezier Curves and Surfaces

Béziers are similar to NURBS, however, they always touch the end-points of the hull (are clamped) and possibly CVs in between (depending on the total number of CVs and the order of the curve). The main difference between Béziers and NURBS is that Béziers have a discontinuity (which might look like a sharp point in the curve) at regular intervals based on the order of the curve. 

In the SOP Editor, set the order of the curve via the Curve State > Parameters dialog. 

For example, if the order of the curve is 4, then the degree will equal 3, meaning you will have four CVs in each curve span. Between each span there will be a discontinuity. Order four curves are best known as "cubics". 

Whereas NURBS curves change only a local portion of the curve when a control point is moved, the entire span within a Bézier curve is affected when a control point belonging to that span is moved. 

If we set the order of the curve to a low number like 2, then each span of the Bézier will be between one CV, and it will look like straight lines. Therefore setting the order to 2 results in a curve that looks like a polygon (composed of straight lines). The curve is called "linear". 

The only way to avoid the "sharp corner" of a discontinuity in a Bézier curve is to make the CVs adjacent to the point of discontinuity collinear as illustrated below. 

In the SOP Editor, a smooth Bézier curve can be built using the Breakpoints option in the Curve state. 

#### Bezier Surfaces

A Bézier surface uses a topology similar to that of a [Mesh](<./Mesh.md> "Mesh"). In a Bézier surface, each node of the UV coordinate matrix represents a CV connected by rows and columns of Bézier hulls. This allows modeling of complex smooth surfaces, whose shape is changeable simply by moving the CVs. 

**Note:** Open Bézier surfaces can only be built with the number of UVs equal to multiples of the order-1, plus one. For example, for an order 4 curve the number of Us or Vs can equal 4, 7, 10, 13, 16, etc. because if the order is 4, then we take the order-1 (=3) and multiply by the number of spans + 1 as in the following: 4=(1*3)+1, 7=(2*3)+1, 10=(3*3)+1, 13=(4*3)+1, and 16=(5*3)+1. If the Bézier surface is wrapped in U and/or V, the formula above loses the "+1" 

#### Curves on Surfaces (Profile or Trim Curves)

TouchDesigner supports curves on surfaces (also known as trim curves and profile curves or profiles for short), which are defined in and bound by the size of the parametric space (i.e. domain) of their parent surface. 

**Types of Profiles**

There are three types of profiles in TouchDesigner: polygons, NURBS curves, and Bézier curves. The definition of each profile type is very similar to that of its 3D equivalent. For example, a NURBS profile can be open or closed, clamped or unclamped, rational or non-rational, and its order can vary between 2 and 10. The fundamental difference between profiles and 3D faces is that the profiles are 2D curves whose CVs are (U, V, W) points in the domain of the parent surface; CVs of 3D faces are X, Y, Z, W quadruplets in object space. For both types of faces W is the rational component (W=1 is the non-rational case). 

**Visual Properties**

The visual representation of a profile, then, is a curve that is always glued to the surface. The 3D shape that we see is merely an image of the 2D geometry that makes up the profile, on the surface. This means that, whenever the surface changes shape, the profile image on the surface follows it. It also means that no part of the profile can ever be lifted off the surface. 

If the entire profile or part of it goes outside the boundaries of the surface domain, it becomes invisible because the surface itself is not defined past those limits. An invisible profile is still valid and can be brought back into view. See the Profile and Primitive SOPs for ways to manipulate a profile. 

A common use of the profile curve is for trimming, which keeps or removes the part of the surface enclosed by the profile (see the Trim SOP). This is why profile curves are sometimes also called trim curves. 

**Profile Numbering and Display**

Profiles are displayed in TouchDesigner as dotted curves. Their numbers can be displayed using the Display Options dialog, by clicking on the Profile Number icons in the Accessories page. A profile number is always prefixed by the primitive number of its parent surface. For example, "0.2" is the third profile of first primitive in the geo detail (numbering starts at zero). 

A profile can co-exist with 3D primitives in primitive groups. A resulting mixed group would specify its elements like this: "1 0.2 6 2.9-2.17 4.*".
