# Shadows

Refer to [Rendering Shadows](<./Rendering_Shadows.md> "Rendering Shadows"). 

With the addition of a shadow render pass and a [Depth TOP](<./Depth_TOP.md> "Depth TOP"), shadows can be rendered in a scene. The Depth TOP creates a depth map from the perspective of a light, then the shadow render pass uses this information to render shadows. Only hard shadows can be created using this method. 

The [Phong MAT](<./Phong_MAT.md> "Phong MAT") has some shadow parameters on its Advanced parameter page. Shadow Strength and Color for a material can be edited here.
