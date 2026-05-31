# Text Formatting Codes

This page outlines formatting codes that can be used inside the text in the [Text COMP](<./Text_COMP.md> "Text COMP") or [Geo Text COMP](<./Geo_Text_COMP.md> "Geo Text COMP") to apply formatting such as colors, underlines, strikeouts or subscript to portions of the text. It is based on the [Slug Library](<./Slug_Library.md> "Slug Library").   
  
To use formatting codes, turn on the 'Enable Formatting Codes' parameter in the component. 

The codes are written into the text, but are processed by the component and do not display in the final output. Code sections begin with a curly brace and hashtag`{#`and end with a closing curly brace`}`. Codes are written like functions with the name first followed by arguments inside brackets e.g.`color(r, g, b)`or`strike(true)`. Multiple codes can be written in one section using a semicolon`;`to separate them e.g.`{#color(255,0,0);script(2)}`. 

When editing in the [Text COMP](<./Text_COMP.md> "Text COMP"), the formatting codes will be displayed in raw format while editing and then processed as codes when editing is complete. For multiline text in the [Text COMP](<./Text_COMP.md> "Text COMP"), formatting only applies to the current paragraph (as marked by a new line character) and resets to the default for the next paragraph. Changes to the font size or line spacing only affect wrapped lines after the line they appear on. 

## Examples

[![](./images/thumb/9/98/Textcomp_red_example.jpg/300px-Textcomp_red_example.jpg)](</File:Textcomp_red_example.jpg>)

[](</File:Textcomp_red_example.jpg> "Enlarge")

This word is {#color(255,0,0)}red

[![](./images/thumb/e/e0/Textcomp_underline.jpg/300px-Textcomp_underline.jpg)](</File:Textcomp_underline.jpg>)

[](</File:Textcomp_underline.jpg> "Enlarge")

You can also {#under(true)}underline{#reset()} or {#strike(true)}strikeout{#reset()} individual words.

## Codes

**stretch(_value_)** \- Set the text stretch to _value_ , where _value_ is a floating-point number. Ignored if _value_ is not greater than zero. 

**track(_value_)** \- Set the text tracking to _value_ in em units, where _value_ is a floating-point number. 

**skew(_value_)** \- Set the text skew to value, where value is a floating-point number. Positive values skew to the right, and negative values skew to the left. 

**scale(_x, y_)** \- Set the text scale to _(x, y)_ , where _x_ and _y_ are floating-point numbers. The _y_ component may be omitted, in which case it is set equal to the _x_ component. Ignored if either _x_ or _y_ is not greater than zero. 

**under(_value_)** \- Set the underline decoration state to value, where _value_ is either _true_ or _false_. Ignored if the font does not contain underline information. 

**strike(_value_)** \- Set the strikethrough decoration state to value, where _value_ is either _true_ or _false_. Ignored if the font does not contain strikethrough information. 

**script(_value_)** \- Set the transform-based script state to _value_ , where _value_ is an integer in the range [−3, 3]. If value is 0, then the text scale and text offset states are set to the identity transform. If _value_ is positive, then the superscript scale and offset are applied _value_ times. If _value_ is negative, then the subscript scale and offset are applied _value_ times. Ignored if _value_ is out of range or the font does not contain transform-based script information. 

**color(_red,green,blue_)** \- Set the primary text color to _(red, green, blue, 255)_ , where each component is an integer in the range [0, 255]. The _red, green, and blue_ components are specified in the sRGB color space. Ignored if any component is out of range. 

**color(_red,green,blue,alpha_)** \- Same as above, but also sets the alpha value. 

**color2(_red,green,blue_)** \- Set the secondary text color to _(red, green, blue, 255)_ using the same format as the primary color. The secondary text color is used only when gradients are enabled. 

**color2(_red,green,blue,alpha_)** \- Same as above, but also sets the alpha value. 

**grad(_value_)** \- Set the gradient state to _value_ , where _value_ is either _true_ or _false_. 

**reset()** \- Reset all formatting states to their initial values.
