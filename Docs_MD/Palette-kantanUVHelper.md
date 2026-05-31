# Palette:kantanUVHelper

## Summary

The kantanUVHelper is a utility tool to make use of [knatanMapper's](<./Palette-kantanMapper.md> "Palette:kantanMapper") second UV Map output. The UV map has a texture id encoded in the blue channel and kantanUVHelper uses this to map the right input texture to the correct area. The benefit of this is that kantanMapper can be disabled or even deleted if the UV map from the second output is saved or locked. 

See also [Projection Mapping](<./Projection_Mapping.md> "Projection Mapping"). 

## Usage

The input to kantanUVHelper is the UV map from kantan's second output. To assign textures, go inside the kantanUVHelper component and connect the textures that should be mapped onto the UV map to the glslmulti1 TOP directly or via [Select TOPs](<./Select_TOP.md> "Select TOP")
