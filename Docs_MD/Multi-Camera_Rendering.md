# Multi-Camera Rendering

Multi-Camera Rendering is rendering multiple cameras in a single rendering pass, all looking at the same scene. This means the scene-graph is only traversed once, which avoids many calls to the graphics driver. Lights, textures, material and draw calls only need to be done once for the entire set of cameras being rendered. This feature is supported by Nvidia Pascal (Geforce 1000, Quadro P-Series) or AMD Polaris (Radeon R9, Radeon Pro WX) and newer GPUs. This feature is important for VR rendering, as well as things such as rendering a Cube Map in a single pass (instead of one pass per side). 

Multi-Camera Rendering will not function if the Cameras have different light masks. The cameras will be rendered one pass at a time in that case. 

This feature is used by the [Render TOP](<./Render_TOP.md> "Render TOP") when multiple cameras are listed in the 'Cameras' parameter. The 'Multi-Camera Hint' parameter can help control how this feature is used for that particular Render TOP. The results of each camera's render can be obtained using [Render Select TOP](<./Render_Select_TOP.md> "Render Select TOP"). 

Nvidia calls this feature 'Simultaneous Multi-Projection'.
