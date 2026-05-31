# Texture Sampling Parameters

The Texture Sampling parameters can be accessed anywhere a [TOP](<./TOP.md> "TOP") is being sampled for use in a material or shader. To open these parameters, click the "**+** " button to the right of the parameter. The _parameter_ portion of the internal names depends on what map parameter these parameters are related to. For example for the colormap parameter, extendu would be colormapextendu.   
  
Extend U`/_parameter_ extendu`\- Sets the extend mode for the U coordiate/direction. Refer to [Texture Extend Modes](<./Texture_Extend_Modes.md> "Texture Extend Modes") for more information. 

Extend V`/_parameter_ extendv`\- Sets the extend mode for the V coordiate/direction. Refer to [Texture Extend Modes](<./Texture_Extend_Modes.md> "Texture Extend Modes") for more information. 

Extend W`/_parameter_ extendw`\- Sets the extend mode for the W coordiate/direction. Only used for [3D Texture](<./3D_Texture.md> "3D Texture"). Refer to [Texture Extend Modes](<./Texture_Extend_Modes.md> "Texture Extend Modes") for more information. 

Filter`/_parameter_ filter`\- Controls how this TOP is filtered when it's gets used. See [Texture Filtering](<./Texture_Filtering.md> "Texture Filtering") for more information. 

Anisotropic Filter`/_parameter_ anisotropy`\- Controls the level of anisotropic filtering used on the TOP when it's sampled. This results in more samples when sampling a TOP, increasing the texturing quality. Refer to [Anisotropic Filtering](<./Anisotropic_Filtering.md> "Anisotropic Filtering") for more information. 

Texture Coord`/_parameter_ coord`\- Determines which set of texture coordinates to use (which texture layer). 

Coord Interpolation`/_parameter_ coordinterp`\- Adjusts the interpolation of the texture coordinated between **Perspective Correct** and **Linear**(no perspective).
