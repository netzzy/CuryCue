# Skin Deform POP

## 

Summary

(**needs to be updated**) A popular way to deform geometry based on Transforms or a full skeleton is called Skinning. Skinning involves having each point being affected by some number of transforms, each one with a different weight. 

## Description of Attributes

#### Detail attribute pCaptPath

The pCaptPath detail attribute is an index attribute that contains a list of paths to COMPs are used as bones. The first path is for index 0, the next for index 1 etc. You can use the [SOP to DAT](<./SOP_to_DAT.md> "SOP to DAT") to inspect the values of this attribute. 

#### Detail attribute pCaptData

This attribute has the same number of entries as pCaptPath. It contains 20 floats per entry. The first 16 make up a matrix for the bind/rest pose of the joint. The other 4 are unused in TouchDesigner and are legacy values from Houdini. 

#### Point or Vertex attribute pCapt[]

This attribute contains pairs of information. In each pair the first value is the index number of the transform that affects the point, and the second number is the weight for that particular transform. When deforming, TouchDesigner uses the index from this attribute to find the correct COMP, using pCaptPath. The sum of all the weights for a given points should add up to 1. An index of -1 indicates that there is no transform to apply for that entry. The attribute has a size which will indicate the number of entries it has (pCapt[8] for example). This size includes both the indices and the weights, so if pCapt has a size of 8, it means a maximum of 4 transforms (4 transforms and 4 weights) are applied to each point. The size of pCapt will be big enough to accommodate the point with the most transforms deforming it. It's possible (or even likely) that there will be just one or two points in a geometry that are affected by many more transforms than the rest, you can use the [Bone Group SOP](<./Bone_Group_SOP.md> "Bone Group SOP") to trim out these points and make pCapt smaller. 

#### Unsupported Houdini attributes

_pCaptSkelRoot_ \- This attribute is the path to the root of the skeleton in Houdini. Since it's unlikely the path in Houdini will be a match to the path in TouchDesigner, we don't support this attribute. Instead there is a Skeleton Root Path parameter in our Deform SOP and Deform page of MATs. 

_pCaptAlpha_ \- This attribute isn't supported. 

_pCaptFrame_ \- This attribute isn't supported. 

## Deforming on the CPU

To deform on the CPU simply use the Deform SOP. The Deform SOP uses Point Capture Attributes rather than Vertex Capture Attributes. You'll need to specify the path to the skeleton in the Skeleton Root Path parameter. 

For example, to deform in [FBX](<./FBX.md> "FBX") on the CPU: an [Import Select SOP](<./Import_Select_SOP.md> "Import Select SOP") with capture attributes can be used as an input to the Deform SOP. The skeleton root path of the Deform SOP will be the [FBX COMP](<./FBX_COMP.md> "FBX COMP"). 

## Deforming on the GPU

Deforming on the GPU is very fast (practically free), but requires a bit more work to setup. The first issue is that most GPUs can only handle the required data for between 50 and 200 bones in a single pass. What this means is that the geometry needs to be split up into subsections, each of which are affected by a different subset of the bones of the skeleton. These are called Bone Groups. The [Bone Group SOP](<./Bone_Group_SOP.md> "Bone Group SOP") will split up geometry with capture attributes into different bone groups. The detail attributes pCaptData and pCaptPath will be split up into detail attributes with postfixes starting at 0. So for example if the geometry gets split into two bone groups, there will be detail attributes pCaptData0, pCaptPath0, pCaptData1, and pCaptPath1. The original pCaptData and pCaptPath will be deleted. The point/vertex attribute pCapt will become a vertex attribute named pCapt. There will also be primitives groups named boneGroup0, boneGroup1 that contain all of the primitives in each bone group. 

You should isolate out each of the primitive bone groups using the [Delete SOP](<./Delete_SOP.md> "Delete SOP"). Next drop down a MAT (like the [Phong MAT](<./Phong_MAT.md> "Phong MAT")) that supports deforms. You will need to give the MAT a few pieces of information: 
* The path to the SOP that contains the deform information you want this MAT to use. This is generally the Delete SOP, or some node after it.
  * The name of the pCaptData and pCaptPath attribute. So for example if you are rendering bone group 0 with this MAT, you'd specify pCaptData0 and pCaptPath0.
  * The path to the root of the skeleton.

#### Deforming using a GLSL MAT

The GLSL MAT supports automatic deform code, you just setup the options on the deform page just like a Phong MAT, and call [code]TDDeform()[/code] on vertex positions and normals to deform them. The correct deform code is automatically generated and prepended to your shader code when it's sent to the GPU. 

#### Writing your own deform code

You can write whatever deform code you want yourself in a GLSL shader. Here is how the automatically generated deform code looks in case you want to use this as a starting point. In this example the pCapt attribute has 12 entries (pCapt[12] in the info popup)., which means it has 6 bones it can reference. Since they are collapsed into vec4 for the shader inputs, this means pCapt in the shader is declared as`in vec4 pCapt[3]`, since that is 12 entries total. Be careful if the size of pCapt in the SOP is not evenly divisible by 4. In that case the last pair of value in the last pCapt entry in the GLSL shader would be undefined. For exmaple if pCapt was pCapt[10] in the SOP, then pCapt in the shader would still be declared as`in vec4 pCapt[3]`. However the pCapt[2].z and pCapt[2].w values are undefined and should not be used. The index will not be equal to -1 necessarily, so that can't be checked against. 

The matrix returned by TDBoneMat() is composed of the world transform for that bone for that frame and the bind pose. The bind pose doesn't change and is contained in the pCaptData attribute. The world transform is calculated from the COMP for the bone every frame. The are multipled together like this: WorldTransform*BindPose 
[code] 
    vec4 TDSkinnedDeform(vec4 pos)
    {
      vec4 newp = vec4(0.0, 0.0, 0.0, 1.0);
      int index;
      if (pCapt[0].x >= 0.0)
      {
          index = int(pCapt[0].x);
          newp += (TDBoneMat(index) * pos) * pCapt[0].y;
      }
      else
      {
          return pos;
      }
      if (pCapt[0].z >= 0.0)
      {
          index = int(pCapt[0].z);
          newp += (TDBoneMat(index) * pos) * pCapt[0].w;
      }
      if (pCapt[1].x >= 0.0)
      {
          index = int(pCapt[1].x);
          newp += (TDBoneMat(index) * pos) * pCapt[1].y;
      }
      if (pCapt[1].z >= 0.0)
      {
          index = int(pCapt[1].z);
          newp += (TDBoneMat(index) * pos) * pCapt[1].w;
      }
      if (pCapt[2].x >= 0.0)
      {
          index = int(pCapt[2].x);
          newp += (TDBoneMat(index) * pos) * pCapt[2].y;
      }
      if (pCapt[2].z >= 0.0)
      {
          index = int(pCapt[2].z);
          newp += (TDBoneMat(index) * pos) * pCapt[2].w;
      }
      newp.w = 1.0;
      return newp;
    }
    
[/code]

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[skindeformPOP_Class](</SkindeformPOP_Class> "SkindeformPOP Class")

## 

Parameters - Deform Page

Mode`mode`\- ⊞ \- Choose what the skin deform is applied to. 
* Skin Deform Geometry`skindeformgeo`-
* Skin Deform Attribute`skindeformattrib`-
* Skin Deform Attribute Scope as Position`skindeformattribscopepos`-
* Skin Deform Attribute Scope as Vector`skindeformattribscopevec`-


Attribute Class`attrclass`\- ⊞ \- Makes the POP operate on point attributes, vertex attributes or primitive attributes where applicable. 
* Point`point`-
* Vertex`vertex`-
* Primitive`primitive`-


Input Attribute (Scope)`inputattrscope`\- Input attribute when mode is Skin Deform Attribute, input attribute scope when mode is Skin Deform Attribute Scope

Bone Paths Attribute`bonepaths`\- The name of the bone paths detail attribute. 

Bone Bind Poses Attribute`bonebindposes`\- The name of the bone bind poses detail attribute. 

Delete Capture Attributes`delcaptattrs`\- Enable deleting the point capture attributes after it deforms the geometry 

Skeleton Root Path`skelrootpath`\- Specifies the path to the root of the skeleton. 

Vectors Maintain Length`vlength`\- Enable preserving the original vector length after applying transformations. 

Output Attribute (Scope)`outputattrscope`\- ⊞ \- Name of attribute to output (can choose components of attribute), can choose from menu. 
* P`P`-
* N`N`-
* Color`Color`-
* Color.rgb`Color.rgb`-
* Tex`Tex`-
* PointScale`PointScale`-
* LineWidth`LineWidth`-


Override Automatic Attribute`overrideautoattr`\- Whether to override the kind of attribute automatically created based on the POP input and parameters. Allows to specify manually the type and number of components of the new attribute. 

Attribute Type`attrtype`\- ⊞ \- The output attribute's data type, default float. 
* float`float`-
* double`double`-
* int`int`-
* uint`uint`-
* Color`color`-
* Color (double)`dcolor`-
* Direction`dir`-
* Direction (double)`ddir`-


Components`attrnumcomps`\- ⊞ \- The number of components in the new custom attribute. 
* 1`1`-
* 2`2`-
* 3`3`-
* 4`4`-


Default Value`attrdefaultval`\- ⊞ \- Default values of the output attribute components if they cannot be computed. 
* Default Value`attrdefaultval0`\- Default value(s) of the attribute.
* Default Value`attrdefaultval1`\- Default value(s) of the attribute.
* Default Value`attrdefaultval2`\- Default value(s) of the attribute.
* Default Value`attrdefaultval3`\- Default value(s) of the attribute.

## 

Parameters - Common Page

Bypass`bypass`\- Pass through the first input to the output unchanged. 

Free Extra GPU Memory`freeextragpumem`\- Free memory that has accumulated when output memory has grown and shrunk. 

Delete Input Attributes`delinputattrs`\- Only output which attributes you specify in this POP \- helps isolate attributes into a separate branch. 

## 

Operator Inputs
* Input 0:  -

## 

Info CHOP Channels

Extra Information for the Skin Deform POP can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). __

### 

Common POP Info Channels

### 

Common Operator Info Channels
* total_cooks \- Number of times the operator has cooked since the process started.
* cook_time \- Duration of the last cook in milliseconds.
* cook_frame \- Frame number when this operator was last cooked relative to the component timeline.
* cook_abs_frame \- Frame number when this operator was last cooked relative to the absolute time.
* cook_start_time \- Time in milliseconds at which the operator started cooking in the frame it was cooked.
* cook_end_time \- Time in milliseconds at which the operator finished cooking in the frame it was cooked.
* cooked_this_frame \- 1 if operator was cooked this frame.
* warnings \- Number of warnings in this operator if any.
* errors \- Number of errors in this operator if any.


  
TouchDesigner Build: Latest\nwikieditor2025.30000

POPs   
---  
[Accumulate ](<./Accumulate_POP.md> "Accumulate POP")• [Alembic In ](<./Alembic_In_POP.md> "Alembic In POP")• [Analyze ](<./Analyze_POP.md> "Analyze POP")• [Attribute Combine ](<./Attribute_Combine_POP.md> "Attribute Combine POP")• [Attribute Convert ](<./Attribute_Convert_POP.md> "Attribute Convert POP")• [Attribute ](<./Attribute_POP.md> "Attribute POP")• [Blend ](<./Blend_POP.md> "Blend POP")• [Box ](<./Box_POP.md> "Box POP")• [Cache Blend ](<./Cache_Blend_POP.md> "Cache Blend POP")• [Cache ](<./Cache_POP.md> "Cache POP")• [Cache Select ](<./Cache_Select_POP.md> "Cache Select POP")• [CHOP to ](<./CHOP_to_POP.md> "CHOP to POP")• [Circle ](<./Circle_POP.md> "Circle POP")• [Connectivity ](<./Connectivity_POP.md> "Connectivity POP")• [Convert ](<./Convert_POP.md> "Convert POP")• [Copy ](<./Copy_POP.md> "Copy POP")• [CPlusPlus ](<./CPlusPlus_POP.md> "CPlusPlus POP")• [Curve ](<./Curve_POP.md> "Curve POP")• [DAT to ](<./DAT_to_POP.md> "DAT to POP")• [Delete ](<./Delete_POP.md> "Delete POP")• [Dimension ](<./Dimension_POP.md> "Dimension POP")• [DMX Fixture ](<./DMX_Fixture_POP.md> "DMX Fixture POP")• [DMX Out ](<./DMX_Out_POP.md> "DMX Out POP")• [Extrude ](<./Extrude_POP.md> "Extrude POP")• [Facet ](<./Facet_POP.md> "Facet POP")• [Feedback ](<./Feedback_POP.md> "Feedback POP")• [Field ](<./Field_POP.md> "Field POP")• [File In ](<./File_In_POP.md> "File In POP")• [File Out ](<./File_Out_POP.md> "File Out POP")• [Force Radial ](<./Force_Radial_POP.md> "Force Radial POP")• [GLSL Advanced ](<./GLSL_Advanced_POP.md> "GLSL Advanced POP")• [GLSL Copy ](<./GLSL_Copy_POP.md> "GLSL Copy POP")• [GLSL Create ](<./GLSL_Create_POP.md> "GLSL Create POP")• [GLSL ](<./GLSL_POP.md> "GLSL POP")• [GLSL Select ](<./GLSL_Select_POP.md> "GLSL Select POP")• [Grid ](<./Grid_POP.md> "Grid POP")• [Group ](<./Group_POP.md> "Group POP")• [Histogram ](<./Histogram_POP.md> "Histogram POP")• [Import Select ](<./Import_Select_POP.md> "Import Select POP")• [In ](<./In_POP.md> "In POP")• [Limit ](<./Limit_POP.md> "Limit POP")• [Line Break ](<./Line_Break_POP.md> "Line Break POP")• [Line Divide ](<./Line_Divide_POP.md> "Line Divide POP")• [Line Metrics ](<./Line_Metrics_POP.md> "Line Metrics POP")• [Line ](<./Line_POP.md> "Line POP")• [Line Resample ](<./Line_Resample_POP.md> "Line Resample POP")• [Line Smooth ](<./Line_Smooth_POP.md> "Line Smooth POP")• [Line Thick ](<./Line_Thick_POP.md> "Line Thick POP")• [Lookup Attribute ](<./Lookup_Attribute_POP.md> "Lookup Attribute POP")• [Lookup Channel ](<./Lookup_Channel_POP.md> "Lookup Channel POP")• [Lookup Texture ](<./Lookup_Texture_POP.md> "Lookup Texture POP")• [Math Combine ](<./Math_Combine_POP.md> "Math Combine POP")• [Math Mix ](<./Math_Mix_POP.md> "Math Mix POP")• [Math ](<./Math_POP.md> "Math POP")• [Merge ](<./Merge_POP.md> "Merge POP")• [Neighbor ](<./Neighbor_POP.md> "Neighbor POP")• [Noise ](<./Noise_POP.md> "Noise POP")• [Normal ](<./Normal_POP.md> "Normal POP")• [Normalize ](<./Normalize_POP.md> "Normalize POP")• [Null ](<./Null_POP.md> "Null POP")• [OAK Select ](<./OAK_Select_POP.md> "OAK Select POP")• [Out ](<./Out_POP.md> "Out POP")• [Particle ](<./Particle_POP.md> "Particle POP")• [Pattern ](<./Pattern_POP.md> "Pattern POP")• [Phaser ](<./Phaser_POP.md> "Phaser POP")• [Plane ](<./Plane_POP.md> "Plane POP")• [Point File In ](<./Point_File_In_POP.md> "Point File In POP")• [Point Generator ](<./Point_Generator_POP.md> "Point Generator POP")• [Point ](<./Point_POP.md> "Point POP")• [Points, Vertices and Primitives in s ](<./Points,_Vertices_and_Primitives_in_POPs.md> "Points, Vertices and Primitives in POPs")• [Polygonize ](<./Polygonize_POP.md> "Polygonize POP")• [POP ](<./POP.md> "POP")• [Primitive ](<./Primitive_POP.md> "Primitive POP")• [Projection ](<./Projection_POP.md> "Projection POP")• [Proximity ](<./Proximity_POP.md> "Proximity POP")• [Quantize ](<./Quantize_POP.md> "Quantize POP")• [Random ](<./Random_POP.md> "Random POP")• [Ray ](<./Ray_POP.md> "Ray POP")• [Rectangle ](<./Rectangle_POP.md> "Rectangle POP")• [ReRange ](<./ReRange_POP.md> "ReRange POP")• [Revolve ](<./Revolve_POP.md> "Revolve POP")• [Select ](<./Select_POP.md> "Select POP")• Skin Deform • [Skin ](<./Skin_POP.md> "Skin POP")• [SOP to ](<./SOP_to_POP.md> "SOP to POP")• [Sort ](<./Sort_POP.md> "Sort POP")• [Sphere ](<./Sphere_POP.md> "Sphere POP")• [Sprinkle ](<./Sprinkle_POP.md> "Sprinkle POP")• [Subdivide ](<./Subdivide_POP.md> "Subdivide POP")• [Switch ](<./Switch_POP.md> "Switch POP")• [Texture Map ](<./Texture_Map_POP.md> "Texture Map POP")• [TOP to ](<./TOP_to_POP.md> "TOP to POP")• [Topology ](<./Topology_POP.md> "Topology POP")• [Torus ](<./Torus_POP.md> "Torus POP")• [Trail ](<./Trail_POP.md> "Trail POP")• [Transform ](<./Transform_POP.md> "Transform POP")• [Trig ](<./Trig_POP.md> "Trig POP")• [Tube ](<./Tube_POP.md> "Tube POP")• [Twist ](<./Twist_POP.md> "Twist POP")• [ZED ](<./ZED_POP.md> "ZED POP")
