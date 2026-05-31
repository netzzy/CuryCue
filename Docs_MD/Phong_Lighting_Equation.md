# Phong Lighting Equation

This article explains how all of the features of the [Phong MAT](<./Phong_MAT.md> "Phong MAT") affect each other. It can often be confusing how one feature affects another (you may assume the results multiply each other, when they may not). The the aim of this article is to help clear up some of that confusion. 

This lighting equation assumes all features of the Phong MAT are used. It ignores all the math involved with calculating lighting, normal mapping, fog etc. It deals with only with how the colors are summed/multiplied. Features not being used can by simply removed from the equation. The function mix() linearly interpolated between the 1st and 2nd parameter, based on the 3rd parameter. 
[code] 
     lightingSum = 0;
     For each light:
     {
        trueLightColor = LightColor * ProjectionMapColor
        if (in a shadow)
           lightColorSum = mix(trueLightColor, ShadowColor, ShadowStrength)
        else
           lightColorSum = trueLightColor
        lightColorSum *= AttenationFactor  
    
        diffuseComponent = DiffuseLightContribution * MaterialDiffuseColor * PointColor * DiffuseMap
        specularComponent = SpecularLightContribution * MaterialSpecularColor * SpecularMap  
    
        totalLightContribution = (diffuseComponent + specularComponent) * lightColorSum
        lightingSum += totalLightContribution
     }
    
[/code]

After we’re done calculating all of the lights, we have a single value for lightingSum which is the final value for all the lights. 

Now apply the other features. 
[code] 
     finalColor = lightingSum
     finalColor += (MaterialAmbientColor * AmbientLightColor * PointColor)
     finalColor += EmitColor * EmitMapColor
     finalColor += ConstantColor * PointColor
     finalColor +=  RimLight(s)
    
[/code]

At this point we save out a value called`lightness`. This is an overall value of how much light is affecting the surface. 
[code] 
     lightness = luminance(finalColor); // Luminance is defined as (r*0.3 + g*0.6 + b*0.1)
    
[/code]

Now apply maps and other features 
[code] 
     finalColor *= ColorMap
     finalColor += EnvironementMap * EnvironmentMapColor
     finalColor = mix(FogColor * FogMapColor, finalColor, FogFactor)
     finalColor = mix(darknessEmitMapColor * darknessEmitColor, finalColor, lightness)
    
[/code]

finalAlpha is calculated as follow: 
[code] 
     finalAlpha = PointAlpha * VaryingAlphaResult * AlphaMap * ColorMapAlpha
     if (light multiplies alpha)
        finalAlpha = finalAlpha * lightness
    
[/code]

And so the color of the pixel is 
[code] 
     if (post multiply color by alpha)
        finalColor *= finalAlpha
     PixelColor = (finalColor.r, finalColor.g, finalColor.b, finalAlpha)
    
[/code]
