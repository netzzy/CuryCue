# Deforming Geometry (Skinning)

## Overview  
  
A popular way to deform geometry based on Transforms or a full skeleton is called Skinning. Skinning involves having each point being affected by some number of transforms, each one with a different weight. 

## Description of Attributes

### Detail attribute pCaptPath

The pCaptPath detail attribute is an index attribute that contains a list of paths to COMPs are used as bones. The first path is for index 0, the next for index 1 etc. You can use the [SOP to DAT](<./SOP_to_DAT.md> "SOP to DAT") to inspect the values of this attribute. 

### Detail attribute pCaptData

This attribute has the same number of entries as pCaptPath. It contains 20 floats per entry. The first 16 make up a matrix for the bind/rest pose of the joint. The other 4 are unused in TouchDesigner and are legacy values from Houdini. 

### Point or Vertex attribute

For SOPs this attribute is called pCapt[]. This attribute contains pairs of information. In each pair the first value is the index number of the transform that affects the point, and the second number is the weight for that particular transform. The attribute has a size which will indicate the number of entries it has (pCapt[8] for example). This size includes both the indices and the weights, so if pCapt has a size of 8, it means a maximum of 4 transforms (4 transforms and 4 weights) are applied to each point. 

For POPs the data has been split up into two attributes, BoneIndices[] and BoneWeights[]. They should have the same array size, and the size will indicate the maximum number of bones that could affect a vertex. 

When deforming, TouchDesigner uses the index attribute to find the correct COMP, using pCaptPath. The sum of all the weights for a given points should add up to 1. An index of -1 indicates that there is no transform to apply for that entry. The size of attributes will be big enough to accommodate the point with the most transforms deforming it. 

### Unsupported Houdini attributes

_pCaptSkelRoot_ \- This attribute is the path to the root of the skeleton in Houdini. Since it's unlikely the path in Houdini will be a match to the path in TouchDesigner, we don't support this attribute. Instead there is a Skeleton Root Path parameter in our Deform SOP and Deform page of MATs. 

_pCaptAlpha_ \- This attribute isn't supported. 

_pCaptFrame_ \- This attribute isn't supported. 

## Deforming on the CPU

To deform on the CPU simply use the Deform SOP. The Deform SOP uses Point Capture Attributes rather than Vertex Capture Attributes. You'll need to specify the path to the skeleton in the Skeleton Root Path parameter. 

For example, to deform in [FBX](<./FBX.md> "FBX") on the CPU: an [Import Select SOP](<./Import_Select_SOP.md> "Import Select SOP") with capture attributes can be used as an input to the Deform SOP. The skeleton root path of the Deform SOP will be the [FBX COMP](<./FBX_COMP.md> "FBX COMP"). 

## Deforming on the GPU

Deforming on the GPU is very fast (practically free). Deforms are enabled on the 'Deform' page of most MATs. 

### Deforming using a GLSL MAT

The GLSL MAT supports automatic deform code, you just setup the options on the deform page just like a Phong MAT, and call`TDDeform()`on vertex positions and normals to deform them. The correct deform code is automatically generated and prepended to your shader code when it's sent to the GPU. 

### Writing your own deform code

You can write whatever deform code you want yourself in a GLSL shader. Although the attribute is held in a single attribute named 'pCapt' in the SOP, this data is uploaded to the GPU as two attributes, for each of use and for future compatibility with POPs. The attributes are named 'BoneIndices' and 'BoneWeights'. To access custom attributes in MATs, you should request them using the 'Attributes' page. BoneIndices is an array of 'int' type, and BoneWeights is an array of 'float' type. You can then access the attributes using`TDAttrib_BoneIndices()`and`TDAttrib_BoneWeights()`which return an array of values. 

The matrix returned by TDBoneMat() is composed of the world transform for that bone for that frame and the bind pose. The bind pose doesn't change and is contained in the pCaptData attribute. The world transform is calculated from the COMP for the bone every frame. The are multipled together like this: WorldTransform*BindPose 
[code] 
    // Currently you need to define this to match max number of bones per point in your geometry. This would be half the size of pCapt array size. E.g pCapt[8] would mean set this to 4.
    // Future improvements are coming for this.
    #define MAX_BONES_PER_POINT 4
    
    vec4 ApplySingleBoneDeform(vec4 pos, int i, float frame)
    {
    	int ind = TDAttrib_BoneIndices()[i];
    	if (ind >= 0.0)
    	{
    		float weight = TDAttrib_BoneWeights()[i];
    		return (TDBoneMatrix(ind) * pos) * weight;
    	}
    	else
    	{
    		return vec4(0.0);
    	}
    }
    
    vec4 CustomSkinnedDeform(vec4 pos, float frame)
    {
    	vec4 newp = vec4(0.0, 0.0, 0.0, 1.0);
    	
    	for (int i = 0; i < MAX_BONES_PER_POINT; i++)
    		newp += ApplySingleBoneDeform(pos, i, frame);
    
    	newp.w = 1.0;
    	return newp;
    }
    
[/code]
