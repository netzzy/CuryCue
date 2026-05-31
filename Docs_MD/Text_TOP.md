# Text TOP

##   
  
Summary

The Text TOP displays text strings in an image. It allows for multiple fonts, sizes, colors, borders, character separation and line separation. The text can be displayed as bit maps, anti-aliased lines, or filled polygon characters. Any TrueType font can be rendered by the Text TOP. [Unicode](<./Unicode.md> "Unicode") is supported. The new Scalable Display Method uses [Slug Library](<./Slug_Library.md> "Slug Library") to render scalable, resolution independent text at the highest qulaity available in the Text TOP. 

It can display simple text strings with embedded numeric values. It can also format lines of text and numbers in decimal or floating point format, reading the numbers from a CHOP, using special formatting characters. 

It can also render text strings from a [Table DAT](<./Table_DAT.md> "Table DAT") via the Specification DAT parameter, where column headings are the parameter names that are to ve overidden when rendering a line of text for reach row of the table. 

Any [TrueType](<http://en.wikipedia.org/wiki/TrueType>) or [OpenType](<http://en.wikipedia.org/wiki/OpenType>) font that has been loaded into Windows can be rendered by the Text TOP. To import a new font into your Windows system, open the **Fonts** folder in the **Control Panel** , then drag and drop your [ font files](<./File_Types.md> "File Types") in (`.ttf/.otf`file format). Fonts can also be specified as`.ttf/.otf`file paths in the Font File parameter. 

You can render **Unicode** text by reading the text as a python string. See [Unicode](<./Unicode.md> "Unicode"). 

**Tip:** You can use the [textTOP_Class](<./TextTOP_Class.md> "TextTOP Class").textWidth member to calculate the width of the text in the Text TOP. 

See also: [Field COMP](<./Field_COMP.md> "Field COMP"), [Text SOP](<./Text_SOP.md> "Text SOP"), [Unicode](<./Unicode.md> "Unicode"). 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[textTOP_Class](<./TextTOP_Class.md> "TextTOP Class")

## 

Parameters - Text Page

Field Component`field`\- Specifies a [Field Component](<./Field_COMP.md> "Field COMP") to use as the source of the text. The font and style of the text displayed in the Field Component are set using the parameters in the Text TOP. 

DAT`dat`\- Specifies a DAT to use for the source of the text. Drag and Drop a DAT onto this field, or manually enter the DAT's path. 

DAT Row`rowindex`\- The row number (starting from 0) of the cell, if the DAT is a table. 

DAT Col`colindex`\- The column number of the cell, if the DAT is a table. 

Specification DAT`specdat`\- A Table DAT that allows you to specify and position text by pixel, with the lower left corner being at 0, 0. Column headers must include`position1`or`x`,`position2`or`y`, and`text`. A sample table can be: 
[code]
    x	y	text		
    0	0	lower left text		
    100	100	somewhere in the middle
    
[/code]

Text`text`\- A string of text. It optionally can be followed by a numeric value and another post-string, as set with Value and Post Text below. If newlines or tabs are desired, the recommended way is to change this parameter to expression mode, and specify a Python string that includes \n or \t to signify newlines and tabs. E.g 'First Line\nSecond Line'. 

Legacy Parsing`legacyparsing`\- In older builds the syntax \XXX (E.g \200 would be character 200), \t, \n as well as [] and {} (to position strings) was parsed in the string. This is now deprecated. For specifying characters codes, \t and \n [Python syntax should be used instead.](<https://docs.python.org/3.3/howto/unicode.html>). The 'Specification DAT' should be used to position strings instead of [], {}. This parameter can be enabled to turn back on this legacy parsing though. If this is enabled and you want to display the characters`\ [ ] { }`, you must precede them with a`\`.****

Append Value`appendvalue`\- Enables the Value field defined below. This value is inserted between the Text string and the Post Text string. 

Value`valuetouse`\- The numeric value to display. 

Total Digits`totaldigits`\- The total number of digits in the value displayed. 

Decimal Digits`decimaldigits`\- The number of digits displayed after the decimal place. 

Post Text`posttext`\- The text string appended after Text and Value (if present). 

CHOP Value %-Replace`chopvaluereplace`\- Allows portions of the strings to be replaced by CHOP values via a syntax similar to C-style printf()/sprintf(). More details of the syntax are provided in the next parameter, 'CHOP' . 

CHOP`chop`\- The CHOP containing all the values to insert in the Text strings. The Text TOP will repeat the Text string until all CHOP channels are displayed. They are displayed by using a special syntax in your Text string, defined as string starting with`%`, for example`%4d`: 

>`%[flags][width][.precision][type]`*`flags`(optional) - Alignment options. 
    * \- : left align (text is right aligned by default)
    * 0 : pad the left side with zeros
  *`width`(optional) - Total number of digits in the number displayed.
  *`precision`(optional) - Number of digits after the decimal place.
  *`type`\- Number format. 
    * d : integer
    * f : float
    * g : double, exponential format is used only when the exponent of the value is less than ?4.


Drag and Drop a CHOP onto this field, or manually enter the CHOP's path. 

Word Wrap`wordwrap`\- When checked text is automatically line wrapped so it doesn't extend outside the TOP's borders. When using Word Wrap and Auto-Size together, the text will first word-wrap based on the specified font size, then auto size the resulting block of text. 

Smart Quote`smartquote`\- Enables smart quotes which use a left (opening) quotation mark and a right (closing) quotation mark instead of straight quotes. 

## 

Parameters - Font Page

Font`font`\- Select the font for the text from this drop down menu. All fonts are provided by Windows, any [TrueType](<http://en.wikipedia.org/wiki/TrueType>) font that is loaded into Windows can be used. 

Font File`fontfile`\- Specify any TrueType font file (`.ttf file`) to use for the text. When using a font file, the Font menu above is disabled. 

Character Set`charset`\- ⊞ \- Select which character set to use. 
* Unicode`unicode`-
* Symbol`symbol`-


Display Method`dispmethod`\- ⊞ \- The display method used. 
* Automatic`automatic`\- Automatically chooses which display mode to use based on font size and settings.
* Polygon`polygon`\- Uses polygons to display the text. Polygons look better using large font sizes. They also support anti-aliasing (see Anti-Aliased below).
* Stroke`stroke`\- Same as polygons but only an outline of the text is displayed.
* Bitmap`bitmap`\- Uses bitmap images for the text. Bitmap fonts are better for very small font sizes where high precision is required.
* Scalable`scalable`\- Uses [Slug Library](<./Slug_Library.md> "Slug Library") to render high-quality, scalable, resolution independent text.


Anti-Alias`antialias`\- ⊞ \- Smoothes out the edges of the text. Not available for Texture Display Mode. 
* 1x (Off)`aa1`-
* 2x`aa2`-
* 4x`aa4`-
* 8x (Medium)`aa8mid`-
* 8x (High)`aa8high`-
* 16x (Low)`aa16low`-
* 16x (Medium)`aa16mid`-
* 16x (High)`aa16high`-
* 32x`aa32`-


Stroke Width`strokewidth`\- Controls the width of the outline when using Stroke Display Method. 

Bold`bold`\- Displays the text in **bold**. 

Italic`italic`\- Displays the text in _Italic_. 

Auto-Size Font`fontautosize`\- ⊞ \- Automatically controls font size using one of the following 3 options. When using this feature along with Word Wrap turned on, it will first word-wrap the text based on the specified font size, then auto size the resulting block of text. 
* No Auto-Fit`nofit`\- Does not use any auto-fitting. Font Size specified in Font Size X and Font Size Y parameters.
* Auto-Fit Always`alwaysfit`\- The font size will be increased or decreased so the text fits across the Text TOP from edge to edge.
* Auto-Fit if Too Large`fitiffat`\- Only auto sizes the text if the text is too large and spills past the edges of the Text TOP. In this case the font size will be decreased to fit it within the borders of the TOP.


Font Size X`fontsizex`\- Sets the font size in X (horizontal). **Note:** Floating point font sizes are permissable when using _Polygon_ and _Outline_ Display Methods. 

Font Size X Unit`fontsizexunit`\- Select the units for this parameter from Pixels, Fraction, Fraction Aspect or Points (font point size). A Point is defined using the Windows conventions for 100% scaling, which is 96 pixels to 72 points. That is, a point size of 10 is the same as a pixel size of 10*(96/72) = 13.333. 

Font Size Y`fontsizey`\- Sets the font size in Y (vertical). **Note:** Floating point font sizes are permissable when using _Polygon_ and _Outline_ Display Methods. 

Font Size Y Unit`fontsizeyunit`\- Select the units for this parameter from Pixels, Fraction, Fraction Aspect or Points (font point size). 

Keep Font Ratio`keepfontratio`\- Ignores Y value in Font Size. Sets both X and Y size to Font Size X. 

Break Language`breaklang`\- Language type hint to help format the glyphs correctly. 

Reading Direction`readingdirection`\- ⊞ \- Use to set whether the language reads Left to Right or Right to Left. 
* Left To Right`lefttoright`-
* Right To Left`righttoleft`-


Tracking`tracking`\- ⊞ \- The amount of space to add between letters in X and Y. Tracking is way of adding an arbitrary offset between letters. There already is a default offset associated with each font so the letters are flush against each other. The Tracking parameter this adds to that and allows for a Y offset. 

  *`tracking1`-


  *`tracking2`-


Position`position`\- ⊞ \- The starting position of the text in X and Y. 

TIP: Inside the Text and Post Text fields the position can be overridden by using brackets. 
* **[x,y]** \-`"bleh[x,y]newtext"`will place _newtext_ at position (x,y) on the screen.
  * **{X,Y}** \-`"bleh{(+/-)x,(+/-)y}newtext"`will offset _newtext_ x,y from current position.
  * **\n** \- using`"\n"`causes the text to move down to the next line and reset its position. (i.e. New Line and Carriage Return)


  *`position1`-


  *`position2`-


Position Unit`positionunit`\- Select the units for this parameter from Pixels, Fraction (0-1), Fraction Aspect (0-1 considering aspect ratio). 

Line Spacing`linespacing`\- Determines the amount of space between lines of text. 

Line Spacing Unit`linespacingunit`\- Select the units for this parameter from Pixels, Fraction (0-1), Fraction Aspect (0-1 considering aspect ratio). 

Horizontal Align`alignx`\- ⊞ \- Sets the horizontal alignment. 
* Left`left`\- Left justifies the text.
* Center`center`\- Centers the text.
* Right`right`\- Right justifies the text.


Horizontal Align Mode`alignxmode`\- ⊞ \- Determines how horizontal alignment is calculated. 
* Use Font Metrics`metrics`\- Uses the font's built-in information to position the text.
* Use Text Bounding Box`bbox`\- Uses a bounding box around the text to position the text.


Vertical Align`aligny`\- ⊞ \- Sets the vertical alignment. 
* Bottom`bottom`\- Bottom justifies the text.
* Center`center`\- Centers the text.
* Top`top`\- Top justifies the text.


Vertical Align Mode`alignymode`\- ⊞ \- Determines how vertical alignment is calculated. 
* Use Font Metrics`metrics`\- Uses the font's built-in information to position the text.
* Use Text Bounding Box`bbox`\- Uses a bounding box around the text to position the text.


Border Space`borderspace`\- ⊞ \- When using Auto-Size Font, it will further shrink the text to give it a border. 

  *`borderspace1`-


  *`borderspace2`-

## 

Parameters - Color Page

Multiply RGB by Alpha`multrgbbyalpha`\- Multiplies the RGB channels by the alpha channel. 

Font Color`fontcolor`\- ⊞ \- RGBA values for the text displayed. (default: white (1,1,1,1)) 
* Red`fontcolorr`-
* Green`fontcolorg`-
* Blue`fontcolorb`-


Font Alpha`fontalpha`\- Set the alpha value for the font. 

Background Color`bgcolor`\- ⊞ \- RGBA values for the background. (default: black (0,0,0,0)) 
* Red`bgcolorr`-
* Green`bgcolorg`-
* Blue`bgcolorb`-


Background Alpha`bgalpha`\- Set the alpha value for the background. 

Border A`bordera`\- ⊞ \- RGBA values for border A color. 
* Red`borderar`-
* Green`borderag`-
* Blue`borderab`-


Border A Alpha`borderaalpha`\- Set the alpha value for border A. 

Border B`borderb`\- ⊞ \- RGBA values for border B color. 
* Red`borderbr`-
* Green`borderbg`-
* Blue`borderbb`-


Border B Alpha`borderbalpha`\- Set the alpha value for border B. 

Left Border`leftborder`\- What color the 2 left-most pixels are. Options are 0 (no change), Border A (uses color defined in Border A), or Border B (uses color defined in Border B). 

Left Border Inside`leftborderi`\- Same as above parameter but used for an inside border. 

Right Border`rightborder`\- What color the 2 right-most pixels are. Options are 0 (no change), Border A (uses color defined in Border A), or Border B (uses color defined in Border B). 

Right Border Inside`rightborderi`\- Same as above parameter but used for an inside border. 

Bottom Border`bottomborder`\- What color the 2 bottom-most pixels are. Options are 0 (no change), Border A (uses color defined in Border A), or Border B (uses color defined in Border B). 

Bottom Border Inside`bottomborderi`\- Same as above parameter but used for an inside border. 

Top Border`topborder`\- What color the 2 top-most pixels are. Options are 0 (no change), Border A (uses color defined in Border A), or Border B (uses color defined in Border B). 

Top Border Inside`topborderi`\- Same as above parameter but used for an inside border. 

## 

Parameters - Output Page

Comp Over Input`compoverinput`\- Turning this On will composite the input with the image. 

Operation`operand`\- ⊞ \- Choose which composite operation is performed from this menu. Search the web for 'blend modes' for more detailed information on the effects of each type. 
* Add`add`\- input1.rgba + input2.rgba
* Atop`atop`\- (input1.rgba * input2.a) + (input2.rgba * (1.0 - input1.a))
* Average`average`\- (input1.rgba + input2.rgba)/2
* Brightest`brightest`-
* Burn Color`burncolor`-
* Burn Linear`burnlinear`-
* Chroma Difference`chromadifference`-
* Color`color`-
* Darker Color`darkercolor`-
* Difference`difference`\- absoluteValue(input1.rgb - input2.rgb). Alpha always equals 1.0
* Dimmest`dimmest`-
* Divide`divide`\- input1.rgba / input2.rgba
* Dodge`dodge`-
* Exclude`exclude`-
* Freeze`freeze`-
* Glow`glow`-
* Hard Light`hardlight`-
* Hard Mix`hardmix`-
* Heat`heat`-
* Hue`hue`-
* Inside`inside`\- input1.rgba * clamp(input2.a, 0.0, 1.0)
* Inside Luminance`insideluminance`-
* Inverse`inverse`-
* Lighter Color`lightercolor`-
* Luminance Difference`luminancedifference`-
* Maximum`maximum`\- max(input1.r, input2.r), max(input1.g, input2.g), max(input1.b, input2.b), max(input1.a, input2.a)
* Minimum`minimum`\- min(input1.r, input2.r), min(input1.g, input2.g), min(input1.b, input2.b), min(input1.a, input2.a)
* Multiply`multiply`-
* Negate`negate`-
* Outside`outside`\- input1.rgba * (1.0 - input2.a)
* Outside Luminance`outsideluminance`-
* Over`over`\- (input2.rgba * (1.0 - input1.a)) + input1.rgba
* Overlay`overlay`-
* Pinlight`pinlight`-
* Reflect`reflect`-
* Screen`screen`\- 1.0 - ((1.0 - input1.rgba) * (1.0 - input2.rgba))
* Soft Light`softlight`-
* Linear Light`linearlight`-
* Stencil Luminance`stencilluminance`-
* Subtract`subtract`\- input1.rgba - input2.rgba
* Subtractive`subtractive`-
* Under`under`\- (input1.rgba * (1.0 - input2.a)) + input2.rgba
* Vivid Light`vividlight`-
* Xor`xor`\- (input1.rgba * (1.0 - input2.a)) + (input2.rgba * (1.0 - input1.a))
* Y Film`yfilm`-
* Z Film`zfilm`-


Swap Order`swaporder`\- Swaps the order of the composite with the input. 

## 

Parameters - Common Page

Output Resolution`outputresolution`\- ⊞ \- quickly change the resolution of the TOP's data. 
* Use Input`useinput`\- Uses the input's resolution
* Eighth`eighth`\- Multiply the input's resolution by that amount.
* Quarter`quarter`\- Multiply the input's resolution by that amount.
* Half`half`\- Multiply the input's resolution by that amount.
* 2X`2x`\- Multiply the input's resolution by that amount.
* 4X`4x`\- Multiply the input's resolution by that amount.
* 8X`8x`\- Multiply the input's resolution by that amount.
* Fit Resolution`fit`\- Grow or shrink the input resolution to fit this resolution, while keeping the aspect ratio the same.
* Limit Resolution`limit`\- Limit the input resolution to be not larger than this resolution, while keeping the aspect ratio the same.
* Custom Resolution`custom`\- Directly control the width and height.


Resolution`resolution`\- ⊞ \- Enabled only when the Resolution parameter is set to Custom Resolution. Some Generators like Constant and Ramp do not use inputs and only use this field to determine their size. The drop down menu on the right provides some commonly used resolutions. 
* W`resolutionw`-
* H`resolutionh`-


Resolution Menu`resmenu`\- A drop-down menu with some commonly used resolutions. 

Use Global Res Multiplier`resmult`\- Uses the Global Resolution Multiplier found in **Edit >Preferences>TOPs**. This multiplies all the TOPs resolutions by the set amount. This is handy when working on computers with different hardware specifications. If a project is designed on a desktop workstation with lots of graphics memory, a user on a laptop with only 64MB VRAM can set the Global Resolution Multiplier to a value of half or quarter so it runs at an acceptable speed. By checking this checkbox on, this TOP is affected by the global multiplier. 

Output Aspect`outputaspect`\- ⊞ \- Sets the image aspect ratio allowing any textures to be viewed in any size. Watch for unexpected results when compositing TOPs with different aspect ratios. (You can define images with non-square pixels using xres, yres, aspectx, aspecty where xres/yres != aspectx/aspecty.) 
* Use Input`useinput`\- Uses the input's aspect ratio.
* Resolution`resolution`\- Uses the aspect of the image's defined resolution (ie 512x256 would be 2:1), whereby each pixel is square.
* Custom Aspect`custom`\- Lets you explicitly define a custom aspect ratio in the Aspect parameter below.


Aspect`aspect`\- ⊞ \- Use when Output Aspect parameter is set to Custom Aspect. 
* Aspect1`aspect1`-
* Aspect2`aspect2`-


Aspect Menu`armenu`\- A drop-down menu with some commonly used aspect ratios. 

Input Smoothness`inputfiltertype`\- ⊞ \- This controls pixel filtering on the input image of the TOP. 
* Nearest Pixel`nearest`\- Uses nearest pixel or accurate image representation. Images will look jaggy when viewing at any zoom level other than Native Resolution.
* Interpolate Pixels`linear`\- Uses linear filtering between pixels. This is how you get TOP images in viewers to look good at various zoom levels, especially useful when using any Fill Viewer setting other than Native Resolution.
* Mipmap Pixels`mipmap`\- Uses [ mipmap](<./Mipmapping.md> "Mipmapping") filtering when scaling images. This can be used to reduce artifacts and sparkling in moving/scaling images that have lots of detail.


Fill Viewer`fillmode`\- ⊞ \- Determine how the TOP image is displayed in the viewer. 

**NOTE:** To get an understanding of how TOPs work with images, you will want to set this to **Native Resolution** as you lay down TOPs when starting out. This will let you see what is actually happening without any automatic viewer resizing. 
* Use Input`useinput`\- Uses the same Fill Viewer settings as it's input.
* Fill`fill`\- Stretches the image to fit the edges of the viewer.
* Fit Horizontal`width`\- Stretches image to fit viewer horizontally.
* Fit Vertical`height`\- Stretches image to fit viewer vertically.
* Fit Best`best`\- Stretches or squashes image so no part of image is cropped.
* Fit Outside`outside`\- Stretches or squashes image so image fills viewer while constraining it's proportions. This often leads to part of image getting cropped by viewer.
* Native Resolution`nativeres`\- Displays the native resolution of the image in the viewer.


Viewer Smoothness`filtertype`\- ⊞ \- This controls pixel filtering in the viewers. 
* Nearest Pixel`nearest`\- Uses nearest pixel or accurate image representation. Images will look jaggy when viewing at any zoom level other than Native Resolution.
* Interpolate Pixels`linear`\- Uses linear filtering between pixels. Use this to get TOP images in viewers to look good at various zoom levels, especially useful when using any Fill Viewer setting other than Native Resolution.
* Mipmap Pixels`mipmap`\- Uses [ mipmap](<./Mipmapping.md> "Mipmapping") filtering when scaling images. This can be used to reduce artifacts and sparkling in moving/scaling images that have lots of detail. When the input is 32-bit float format, only nearest filtering will be used (regardless of what is selected).


Passes`npasses`\- Duplicates the operation of the TOP the specified number of times. For every pass after the first it takes the result of the previous pass and replaces the node's first input with the result of the previous pass. One exception to this is the [GLSL TOP](<./GLSL_TOP.md> "GLSL TOP") when using compute shaders, where the input will continue to be the connected TOP's image. 

Channel Mask`chanmask`\- Allows you to choose which channels (R, G, B, or A) the TOP will operate on. All channels are selected by default. 

Pixel Format`format`\- ⊞ \- Format used to store data for each channel in the image (ie. R, G, B, and A). Refer to [Pixel Formats](<./Pixel_Formats.md> "Pixel Formats") for more information. 
* Use Input`useinput`\- Uses the input's pixel format.
* 8-bit fixed (RGBA)`rgba8fixed`\- Uses 8-bit integer values for each channel.
* sRGB 8-bit fixed (RGBA)`srgba8fixed`\- Uses 8-bit integer values for each channel and stores color in sRGB colorspace. Note that this does **not** apply an sRGB curve to the pixel values, it only stores them using an sRGB curve. This means more data is used for the darker values and less for the brighter values. When the values are read downstream they will be converted back to linear. For more information refer to [sRGB](<./SRGB.md> "SRGB").
* 16-bit float (RGBA)`rgba16float`\- Uses 16-bits per color channel, 64-bits per pixel.
* 32-bit float (RGBA)`rgba32float`\- Uses 32-bits per color channel, 128-bits per pixels.
* 10-bit RGB, 2-bit Alpha, fixed (RGBA)`rgb10a2fixed`\- Uses 10-bits per color channel and 2-bits for alpha, 32-bits total per pixel.
* 16-bit fixed (RGBA)`rgba16fixed`\- Uses 16-bits per color channel, 64-bits total per pixel.
* 11-bit float (RGB), Positive Values Only`rgba11float`\- A RGB floating point format that has 11 bits for the Red and Green channels, and 10-bits for the Blue Channel, 32-bits total per pixel (therefore the same memory usage as 8-bit RGBA). The Alpha channel in this format will always be 1. Values can go above one, but can't be negative. ie. the range is [0, infinite).
* 16-bit float (RGB)`rgb16float`-
* 32-bit float (RGB)`rgb32float`-
* 8-bit fixed (Mono)`mono8fixed`\- Single channel, where RGB will all have the same value, and Alpha will be 1.0. 8-bits per pixel.
* 16-bit fixed (Mono)`mono16fixed`\- Single channel, where RGB will all have the same value, and Alpha will be 1.0. 16-bits per pixel.
* 16-bit float (Mono)`mono16float`\- Single channel, where RGB will all have the same value, and Alpha will be 1.0. 16-bits per pixel.
* 32-bit float (Mono)`mono32float`\- Single channel, where RGB will all have the same value, and Alpha will be 1.0. 32-bits per pixel.
* 8-bit fixed (RG)`rg8fixed`\- A 2 channel format, R and G have values, while B is 0 always and Alpha is 1.0. 8-bits per channel, 16-bits total per pixel.
* 16-bit fixed (RG)`rg16fixed`\- A 2 channel format, R and G have values, while B is 0 always and Alpha is 1.0. 16-bits per channel, 32-bits total per pixel.
* 16-bit float (RG)`rg16float`\- A 2 channel format, R and G have values, while B is 0 always and Alpha is 1.0. 16-bits per channel, 32-bits total per pixel.
* 32-bit float (RG)`rg32float`\- A 2 channel format, R and G have values, while B is 0 always and Alpha is 1.0. 32-bits per channel, 64-bits total per pixel.
* 8-bit fixed (A)`a8fixed`\- An Alpha only format that has 8-bits per channel, 8-bits per pixel.
* 16-bit fixed (A)`a16fixed`\- An Alpha only format that has 16-bits per channel, 16-bits per pixel.
* 16-bit float (A)`a16float`\- An Alpha only format that has 16-bits per channel, 16-bits per pixel.
* 32-bit float (A)`a32float`\- An Alpha only format that has 32-bits per channel, 32-bits per pixel.
* 8-bit fixed (Mono+Alpha)`monoalpha8fixed`\- A 2 channel format, one value for RGB and one value for Alpha. 8-bits per channel, 16-bits per pixel.
* 16-bit fixed (Mono+Alpha)`monoalpha16fixed`\- A 2 channel format, one value for RGB and one value for Alpha. 16-bits per channel, 32-bits per pixel.
* 16-bit float (Mono+Alpha)`monoalpha16float`\- A 2 channel format, one value for RGB and one value for Alpha. 16-bits per channel, 32-bits per pixel.
* 32-bit float (Mono+Alpha)`monoalpha32float`\- A 2 channel format, one value for RGB and one value for Alpha. 32-bits per channel, 64-bits per pixel.


Parameter Color Space`parmcolorspace`\- ⊞ \- Controls how all color parameters on this node are interpreted. The color values as treated as being in the selected color space, and are converted to the Working [Color Space](<./Color_Space.md> "Color Space") before they are used as part of the node's operation. Note that this does not change the color space of the node itself, as that is always in the Working Color Space. 
* sRGB`srgb`\- [sRGB](<https://en.wikipedia.org/wiki/SRGB>) color space, with sRGB transfer function. Considered an SDR color space with respect to Reference White.
* sRGB - Linear`srgblinear`\- [sRGB](<https://en.wikipedia.org/wiki/SRGB>) color space, with linear transfer function. Considered an SDR color space with respect to Reference White.
* Rec.601 (NTSC)`rec601ntsc`\- [Rec.601](<https://en.wikipedia.org/wiki/Rec._601>) with NTSC primaries color space, with Rec.601 transfer function. Considered an SDR color space with respect to Reference White.
* Rec.709`rec709`\- [Rec.709](<https://en.wikipedia.org/wiki/Rec._709>) color space, with Rec.709 (same as Rec.2020) transfer function. Considered an SDR color space with respect to Reference White.
* Rec.2020`rec2020`\- [Rec.2020](<https://en.wikipedia.org/wiki/Rec._2020>) color space, with Rec.2020 (same as Rec.709) transfer function. Considered an HDR color space with respect to Reference White.
* DCI-P3`dcip3`\- [DCI-P3](<https://en.wikipedia.org/wiki/DCI-P3>) color space, with D65 white point and 2.6 gamma transfer function. Considered an HDR color space with respect to Reference White.
* DCI-P3 (D60)`dcip3d60`\- [DCI-P3 "D60 sim"](<https://en.wikipedia.org/wiki/DCI-P3>) color space, with D60 white point, and 2.6 gamma transfer function. Considered an HDR color space with respect to Reference White.
* Display-P3 (D65)`displayp3d65`\- [Display-P3](<https://en.wikipedia.org/wiki/DCI-P3>) color space, with D65 white point, and sRGB gamma transfer function. Considered an HDR color space with respect to Reference White.
* ACES2065-1`aces2065-1`\- [ACES 2065-1](<https://en.wikipedia.org/wiki/Academy_Color_Encoding_System>) (also known as ACES AP0) color space, with a linear gamma transfer function. Considered an HDR color space with respect to Reference White.
* ACEScg`acescg`\- [ACEScg](<https://en.wikipedia.org/wiki/Academy_Color_Encoding_System>) (also known as ACES AP1) color space, with a linear gamma transfer function. Considered an HDR color space with respect to Reference White.
* Passthrough`passthrough`\- When selected, the color values will be used as-is in the operation, without any modification or attempt to convert them into the Working Color Space.


Parameter Reference White`parmreferencewhite`\- ⊞ \- When converting a parameter color value to the Working Color Space, this controls how it should be treated with respect to [Reference White](<./Color_Space.htm#Reference_White> "Color Space"). If the Working Color Space is the same Reference White, then no adjustment is done. If they are different, then the Reference White level (brightness) of this color will be adjusted to the range expected by the Working Color Space. For example if the project is set to have a SDR Reference White of 120 nits, and the HDR Reference White is 80 nits, then a color of (1, 1, 1), which is 120 nits in the SDR color space, will be converted to be (1.5, 1.5, 1.5), which is 120 nits still in the HDR Working Color Space. 
* Default For Color Space`default`\- Will use either the SDR or the HDR Reference White, based on the color space selected.
* Use Parent Panel`useparent`\- Will use the Reference White that the parent panel has selected. If the top-level panel also has 'Use Parent' selected, then 'UI Reference White' will be used.
* Standard (SDR)`sdr`\- Will treat the Parameter Color Space as SDR for it's reference white value.
* High (HDR)`hdr`\- Will treat the Parameter Color Space as HDR for it's reference white value.
* UI`ui`\- Will treat the Parameter Color Space as UI for it's reference white value. This uses the 'UI Reference White Nits' value for it's brightness.


Parameter Color Space`parmcolorspace`\- ⊞ \- Controls how all color parameters on this node are interpreted. The color values as treated as being in the selected color space, and are converted to the Working [Color Space](<./Color_Space.md> "Color Space") before they are used as part of the node's operation. Note that this does not change the color space of the node itself, as that is always in the Working Color Space. 
* sRGB`srgb`\- [sRGB](<https://en.wikipedia.org/wiki/SRGB>) color space, with sRGB transfer function. Considered an SDR color space with respect to Reference White.
* sRGB - Linear`srgblinear`\- [sRGB](<https://en.wikipedia.org/wiki/SRGB>) color space, with linear transfer function. Considered an SDR color space with respect to Reference White.
* Rec.601 (NTSC)`rec601ntsc`\- [Rec.601](<https://en.wikipedia.org/wiki/Rec._601>) with NTSC primaries color space, with Rec.601 transfer function. Considered an SDR color space with respect to Reference White.
* Rec.709`rec709`\- [Rec.709](<https://en.wikipedia.org/wiki/Rec._709>) color space, with Rec.709 (same as Rec.2020) transfer function. Considered an SDR color space with respect to Reference White.
* Rec.2020`rec2020`\- [Rec.2020](<https://en.wikipedia.org/wiki/Rec._2020>) color space, with Rec.2020 (same as Rec.709) transfer function. Considered an HDR color space with respect to Reference White.
* DCI-P3`dcip3`\- [DCI-P3](<https://en.wikipedia.org/wiki/DCI-P3>) color space, with D65 white point and 2.6 gamma transfer function. Considered an HDR color space with respect to Reference White.
* DCI-P3 (D60)`dcip3d60`\- [DCI-P3 "D60 sim"](<https://en.wikipedia.org/wiki/DCI-P3>) color space, with D60 white point, and 2.6 gamma transfer function. Considered an HDR color space with respect to Reference White.
* Display-P3 (D65)`displayp3d65`\- [Display-P3](<https://en.wikipedia.org/wiki/DCI-P3>) color space, with D65 white point, and sRGB gamma transfer function. Considered an HDR color space with respect to Reference White.
* ACES2065-1`aces2065-1`\- [ACES 2065-1](<https://en.wikipedia.org/wiki/Academy_Color_Encoding_System>) (also known as ACES AP0) color space, with a linear gamma transfer function. Considered an HDR color space with respect to Reference White.
* ACEScg`acescg`\- [ACEScg](<https://en.wikipedia.org/wiki/Academy_Color_Encoding_System>) (also known as ACES AP1) color space, with a linear gamma transfer function. Considered an HDR color space with respect to Reference White.
* Passthrough`passthrough`\- When selected, the color values will be used as-is in the operation, without any modification or attempt to convert them into the Working Color Space.


Parameter Reference White`parmreferencewhite`\- ⊞ \- When converting a parameter color value to the Working Color Space, this controls how it should be treated with respect to [Reference White](<./Color_Space.htm#Reference_White> "Color Space"). If the Working Color Space is the same Reference White, then no adjustment is done. If they are different, then the Reference White level (brightness) of this color will be adjusted to the range expected by the Working Color Space. For example if the project is set to have a SDR Reference White of 120 nits, and the HDR Reference White is 80 nits, then a color of (1, 1, 1), which is 120 nits in the SDR color space, will be converted to be (1.5, 1.5, 1.5), which is 120 nits still in the HDR Working Color Space. 
* Default For Color Space`default`\- Will use either the SDR or the HDR Reference White, based on the color space selected.
* Use Parent Panel`useparent`\- Will use the Reference White that the parent panel has selected. If the top-level panel also has 'Use Parent' selected, then 'UI Reference White' will be used.
* Standard (SDR)`sdr`\- Will treat the Parameter Color Space as SDR for it's reference white value.
* High (HDR)`hdr`\- Will treat the Parameter Color Space as HDR for it's reference white value.
* UI`ui`\- Will treat the Parameter Color Space as UI for it's reference white value. This uses the 'UI Reference White Nits' value for it's brightness.


Parameter Color Space`parmcolorspace`\- ⊞ \- Controls how all color parameters on this node are interpreted. The color values as treated as being in the selected color space, and are converted to the Working [Color Space](<./Color_Space.md> "Color Space") before they are used as part of the node's operation. Note that this does not change the color space of the node itself, as that is always in the Working Color Space. 
* sRGB`srgb`\- [sRGB](<https://en.wikipedia.org/wiki/SRGB>) color space, with sRGB transfer function. Considered an SDR color space with respect to Reference White.
* sRGB - Linear`srgblinear`\- [sRGB](<https://en.wikipedia.org/wiki/SRGB>) color space, with linear transfer function. Considered an SDR color space with respect to Reference White.
* Rec.601 (NTSC)`rec601ntsc`\- [Rec.601](<https://en.wikipedia.org/wiki/Rec._601>) with NTSC primaries color space, with Rec.601 transfer function. Considered an SDR color space with respect to Reference White.
* Rec.709`rec709`\- [Rec.709](<https://en.wikipedia.org/wiki/Rec._709>) color space, with Rec.709 (same as Rec.2020) transfer function. Considered an SDR color space with respect to Reference White.
* Rec.2020`rec2020`\- [Rec.2020](<https://en.wikipedia.org/wiki/Rec._2020>) color space, with Rec.2020 (same as Rec.709) transfer function. Considered an HDR color space with respect to Reference White.
* DCI-P3`dcip3`\- [DCI-P3](<https://en.wikipedia.org/wiki/DCI-P3>) color space, with D65 white point and 2.6 gamma transfer function. Considered an HDR color space with respect to Reference White.
* DCI-P3 (D60)`dcip3d60`\- [DCI-P3 "D60 sim"](<https://en.wikipedia.org/wiki/DCI-P3>) color space, with D60 white point, and 2.6 gamma transfer function. Considered an HDR color space with respect to Reference White.
* Display-P3 (D65)`displayp3d65`\- [Display-P3](<https://en.wikipedia.org/wiki/DCI-P3>) color space, with D65 white point, and sRGB gamma transfer function. Considered an HDR color space with respect to Reference White.
* ACES2065-1`aces2065-1`\- [ACES 2065-1](<https://en.wikipedia.org/wiki/Academy_Color_Encoding_System>) (also known as ACES AP0) color space, with a linear gamma transfer function. Considered an HDR color space with respect to Reference White.
* ACEScg`acescg`\- [ACEScg](<https://en.wikipedia.org/wiki/Academy_Color_Encoding_System>) (also known as ACES AP1) color space, with a linear gamma transfer function. Considered an HDR color space with respect to Reference White.
* Passthrough`passthrough`\- When selected, the color values will be used as-is in the operation, without any modification or attempt to convert them into the Working Color Space.


Parameter Reference White`parmreferencewhite`\- ⊞ \- When converting a parameter color value to the Working Color Space, this controls how it should be treated with respect to [Reference White](<./Color_Space.htm#Reference_White> "Color Space"). If the Working Color Space is the same Reference White, then no adjustment is done. If they are different, then the Reference White level (brightness) of this color will be adjusted to the range expected by the Working Color Space. For example if the project is set to have a SDR Reference White of 120 nits, and the HDR Reference White is 80 nits, then a color of (1, 1, 1), which is 120 nits in the SDR color space, will be converted to be (1.5, 1.5, 1.5), which is 120 nits still in the HDR Working Color Space. 
* Default For Color Space`default`\- Will use either the SDR or the HDR Reference White, based on the color space selected.
* Use Parent Panel`useparent`\- Will use the Reference White that the parent panel has selected. If the top-level panel also has 'Use Parent' selected, then 'UI Reference White' will be used.
* Standard (SDR)`sdr`\- Will treat the Parameter Color Space as SDR for it's reference white value.
* High (HDR)`hdr`\- Will treat the Parameter Color Space as HDR for it's reference white value.
* UI`ui`\- Will treat the Parameter Color Space as UI for it's reference white value. This uses the 'UI Reference White Nits' value for it's brightness.


Parameter Color Space`parmcolorspace`\- ⊞ \- Controls how all color parameters on this node are interpreted. The color values as treated as being in the selected color space, and are converted to the Working [Color Space](<./Color_Space.md> "Color Space") before they are used as part of the node's operation. Note that this does not change the color space of the node itself, as that is always in the Working Color Space. 
* sRGB`srgb`\- [sRGB](<https://en.wikipedia.org/wiki/SRGB>) color space, with sRGB transfer function. Considered an SDR color space with respect to Reference White.
* sRGB - Linear`srgblinear`\- [sRGB](<https://en.wikipedia.org/wiki/SRGB>) color space, with linear transfer function. Considered an SDR color space with respect to Reference White.
* Rec.601 (NTSC)`rec601ntsc`\- [Rec.601](<https://en.wikipedia.org/wiki/Rec._601>) with NTSC primaries color space, with Rec.601 transfer function. Considered an SDR color space with respect to Reference White.
* Rec.709`rec709`\- [Rec.709](<https://en.wikipedia.org/wiki/Rec._709>) color space, with Rec.709 (same as Rec.2020) transfer function. Considered an SDR color space with respect to Reference White.
* Rec.2020`rec2020`\- [Rec.2020](<https://en.wikipedia.org/wiki/Rec._2020>) color space, with Rec.2020 (same as Rec.709) transfer function. Considered an HDR color space with respect to Reference White.
* DCI-P3`dcip3`\- [DCI-P3](<https://en.wikipedia.org/wiki/DCI-P3>) color space, with D65 white point and 2.6 gamma transfer function. Considered an HDR color space with respect to Reference White.
* DCI-P3 (D60)`dcip3d60`\- [DCI-P3 "D60 sim"](<https://en.wikipedia.org/wiki/DCI-P3>) color space, with D60 white point, and 2.6 gamma transfer function. Considered an HDR color space with respect to Reference White.
* Display-P3 (D65)`displayp3d65`\- [Display-P3](<https://en.wikipedia.org/wiki/DCI-P3>) color space, with D65 white point, and sRGB gamma transfer function. Considered an HDR color space with respect to Reference White.
* ACES2065-1`aces2065-1`\- [ACES 2065-1](<https://en.wikipedia.org/wiki/Academy_Color_Encoding_System>) (also known as ACES AP0) color space, with a linear gamma transfer function. Considered an HDR color space with respect to Reference White.
* ACEScg`acescg`\- [ACEScg](<https://en.wikipedia.org/wiki/Academy_Color_Encoding_System>) (also known as ACES AP1) color space, with a linear gamma transfer function. Considered an HDR color space with respect to Reference White.
* Passthrough`passthrough`\- When selected, the color values will be used as-is in the operation, without any modification or attempt to convert them into the Working Color Space.


Parameter Reference White`parmreferencewhite`\- ⊞ \- When converting a parameter color value to the Working Color Space, this controls how it should be treated with respect to [Reference White](<./Color_Space.htm#Reference_White> "Color Space"). If the Working Color Space is the same Reference White, then no adjustment is done. If they are different, then the Reference White level (brightness) of this color will be adjusted to the range expected by the Working Color Space. For example if the project is set to have a SDR Reference White of 120 nits, and the HDR Reference White is 80 nits, then a color of (1, 1, 1), which is 120 nits in the SDR color space, will be converted to be (1.5, 1.5, 1.5), which is 120 nits still in the HDR Working Color Space. 
* Default For Color Space`default`\- Will use either the SDR or the HDR Reference White, based on the color space selected.
* Use Parent Panel`useparent`\- Will use the Reference White that the parent panel has selected. If the top-level panel also has 'Use Parent' selected, then 'UI Reference White' will be used.
* Standard (SDR)`sdr`\- Will treat the Parameter Color Space as SDR for it's reference white value.
* High (HDR)`hdr`\- Will treat the Parameter Color Space as HDR for it's reference white value.
* UI`ui`\- Will treat the Parameter Color Space as UI for it's reference white value. This uses the 'UI Reference White Nits' value for it's brightness.

## 

Operator Inputs
* Input 0: Composite Input \- Control the Composite operation via the parameters on the Output Page of this operator.

## 

Info CHOP Channels

Extra Information for the Text TOP can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). 

### 

Specific Text TOP Info Channels
* text_width -
* text_height -
* cursor_start -
* cursor_end -
* cursor_x -
* cursor_y -
* cursor_width -
* cursor_height -

### 

Common TOP Info Channels
* resx \- Horizontal resolution of the TOP in pixels.
* resy \- Vertical resolution of the TOP in pixels.
* aspectx \- Horizontal aspect of the TOP.
* aspecty \- Vertical aspect of the TOP.
* depth \- Depth of 2D or 3D array if this TOP contains a 2D or 3D texture array.
* gpu_memory_used \- Total amount of texture memory used by this TOP.

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


  
TouchDesigner Build: Latest\n2022.241402021.100002018.28070before 2018.28070

TOPs   
---  
[Add ](<./Add_TOP.md> "Add TOP")• [Analyze ](<./Analyze_TOP.md> "Analyze TOP")• [Anti Alias ](<./Anti_Alias_TOP.md> "Anti Alias TOP")• [Blob Track ](<./Blob_Track_TOP.md> "Blob Track TOP")• [Bloom ](<./Bloom_TOP.md> "Bloom TOP")• [Blur ](<./Blur_TOP.md> "Blur TOP")• [Cache Select ](<./Cache_Select_TOP.md> "Cache Select TOP")• [Cache ](<./Cache_TOP.md> "Cache TOP")• [Channel Mix ](<./Channel_Mix_TOP.md> "Channel Mix TOP")• [CHOP to ](<./CHOP_to_TOP.md> "CHOP to TOP")• [Chroma Key ](<./Chroma_Key_TOP.md> "Chroma Key TOP")• [Circle ](<./Circle_TOP.md> "Circle TOP")• [Composite ](<./Composite_TOP.md> "Composite TOP")• [Constant ](<./Constant_TOP.md> "Constant TOP")• [Convolve ](<./Convolve_TOP.md> "Convolve TOP")• [Corner Pin ](<./Corner_Pin_TOP.md> "Corner Pin TOP")• [CPlusPlus ](<./CPlusPlus_TOP.md> "CPlusPlus TOP")• [Crop ](<./Crop_TOP.md> "Crop TOP")• [Cross ](<./Cross_TOP.md> "Cross TOP")• [Cube Map ](<./Cube_Map_TOP.md> "Cube Map TOP")• [Depth ](<./Depth_TOP.md> "Depth TOP")• [Difference ](<./Difference_TOP.md> "Difference TOP")• [Direct Display Out ](<./Direct_Display_Out_TOP.md> "Direct Display Out TOP")• [DirectX In ](<./DirectX_In_TOP.md> "DirectX In TOP")• [DirectX Out ](<./DirectX_Out_TOP.md> "DirectX Out TOP")• [Displace ](<./Displace_TOP.md> "Displace TOP")• [Edge ](<./Edge_TOP.md> "Edge TOP")• [Emboss ](<./Emboss_TOP.md> "Emboss TOP")• [Feedback ](<./Feedback_TOP.md> "Feedback TOP")• [Fit ](<./Fit_TOP.md> "Fit TOP")• [Flip ](<./Flip_TOP.md> "Flip TOP")• [Function ](<./Function_TOP.md> "Function TOP")• [GLSL Multi ](<./GLSL_Multi_TOP.md> "GLSL Multi TOP")• [GLSL ](<./GLSL_TOP.md> "GLSL TOP")• [HSV Adjust ](<./HSV_Adjust_TOP.md> "HSV Adjust TOP")• [HSV to RGB ](<./HSV_to_RGB_TOP.md> "HSV to RGB TOP")• [Import Select ](<./Import_Select_TOP.md> "Import Select TOP")• [In ](<./In_TOP.md> "In TOP")• [Inside ](<./Inside_TOP.md> "Inside TOP")• [Introduction To s Vid ](<./Introduction_To_TOPs_Vid.md> "Introduction To TOPs Vid")• [Kinect Azure Select ](<./Kinect_Azure_Select_TOP.md> "Kinect Azure Select TOP")• [Kinect Azure ](<./Kinect_Azure_TOP.md> "Kinect Azure TOP")• [Kinect ](<./Kinect_TOP.md> "Kinect TOP")• [Layer Mix ](<./Layer_Mix_TOP.md> "Layer Mix TOP")• [Layer ](<./Layer_TOP.md> "Layer TOP")• [Layout ](<./Layout_TOP.md> "Layout TOP")• [Leap Motion ](<./Leap_Motion_TOP.md> "Leap Motion TOP")• [Lens Distort ](<./Lens_Distort_TOP.md> "Lens Distort TOP")• [Level ](<./Level_TOP.md> "Level TOP")• [Limit ](<./Limit_TOP.md> "Limit TOP")• [Lookup ](<./Lookup_TOP.md> "Lookup TOP")• [Luma Blur ](<./Luma_Blur_TOP.md> "Luma Blur TOP")• [Luma Level ](<./Luma_Level_TOP.md> "Luma Level TOP")• [Math ](<./Math_TOP.md> "Math TOP")• [Matte ](<./Matte_TOP.md> "Matte TOP")• [Mirror ](<./Mirror_TOP.md> "Mirror TOP")• [Monochrome ](<./Monochrome_TOP.md> "Monochrome TOP")• [MoSys ](<./MoSys_TOP.md> "MoSys TOP")• [Movie File In ](<./Movie_File_In_TOP.md> "Movie File In TOP")• [Movie File Out ](<./Movie_File_Out_TOP.md> "Movie File Out TOP")• [MPCDI ](<./MPCDI_TOP.md> "MPCDI TOP")• [Multiply ](<./Multiply_TOP.md> "Multiply TOP")• [Ncam ](<./Ncam_TOP.md> "Ncam TOP")• [NDI In ](<./NDI_In_TOP.md> "NDI In TOP")• [NDI Out ](<./NDI_Out_TOP.md> "NDI Out TOP")• [Noise ](<./Noise_TOP.md> "Noise TOP")• [Normal Map ](<./Normal_Map_TOP.md> "Normal Map TOP")• [Notch ](<./Notch_TOP.md> "Notch TOP")• [Null ](<./Null_TOP.md> "Null TOP")• [NVIDIA Background ](<./NVIDIA_Background_TOP.md> "NVIDIA Background TOP")• [NVIDIA Denoise ](<./NVIDIA_Denoise_TOP.md> "NVIDIA Denoise TOP")• [NVIDIA Flex ](<./NVIDIA_Flex_TOP.md> "NVIDIA Flex TOP")• [NVIDIA Flow ](<./NVIDIA_Flow_TOP.md> "NVIDIA Flow TOP")• [NVIDIA Upscaler ](<./NVIDIA_Upscaler_TOP.md> "NVIDIA Upscaler TOP")• [OAK Select ](<./OAK_Select_TOP.md> "OAK Select TOP")• [Oculus Rift ](<./Oculus_Rift_TOP.md> "Oculus Rift TOP")• [OP Viewer ](<./OP_Viewer_TOP.md> "OP Viewer TOP")• [OpenColorIO ](<./OpenColorIO_TOP.md> "OpenColorIO TOP")• [OpenVR ](<./OpenVR_TOP.md> "OpenVR TOP")• [Optical Flow ](<./Optical_Flow_TOP.md> "Optical Flow TOP")• [Orbbec Select ](<./Orbbec_Select_TOP.md> "Orbbec Select TOP")• [Orbbec ](<./Orbbec_TOP.md> "Orbbec TOP")• [Ouster Select ](<./Ouster_Select_TOP.md> "Ouster Select TOP")• [Ouster ](<./Ouster_TOP.md> "Ouster TOP")• [Out ](<./Out_TOP.md> "Out TOP")• [Outside ](<./Outside_TOP.md> "Outside TOP")• [Over ](<./Over_TOP.md> "Over TOP")• [Pack ](<./Pack_TOP.md> "Pack TOP")• [Photoshop In ](<./Photoshop_In_TOP.md> "Photoshop In TOP")• [Point File In ](<./Point_File_In_TOP.md> "Point File In TOP")• [Point File Select ](<./Point_File_Select_TOP.md> "Point File Select TOP")• [Point Transform ](<./Point_Transform_TOP.md> "Point Transform TOP")• [POP to ](<./POP_to_TOP.md> "POP to TOP")• [PreFilter Map ](<./PreFilter_Map_TOP.md> "PreFilter Map TOP")• [Projection ](<./Projection_TOP.md> "Projection TOP")• [Ramp ](<./Ramp_TOP.md> "Ramp TOP")• [RealSense ](<./RealSense_TOP.md> "RealSense TOP")• [Rectangle ](<./Rectangle_TOP.md> "Rectangle TOP")• [Remap ](<./Remap_TOP.md> "Remap TOP")• [Render Pass ](<./Render_Pass_TOP.md> "Render Pass TOP")• [Render Select ](<./Render_Select_TOP.md> "Render Select TOP")• [Render Simple ](<./Render_Simple_TOP.md> "Render Simple TOP")• [Render ](<./Render_TOP.md> "Render TOP")• [RenderStream In ](<./RenderStream_In_TOP.md> "RenderStream In TOP")• [RenderStream Out ](<./RenderStream_Out_TOP.md> "RenderStream Out TOP")• [Reorder ](<./Reorder_TOP.md> "Reorder TOP")• [Resolution ](<./Resolution_TOP.md> "Resolution TOP")• [RGB Key ](<./RGB_Key_TOP.md> "RGB Key TOP")• [RGB to HSV ](<./RGB_to_HSV_TOP.md> "RGB to HSV TOP")• [Scalable Display ](<./Scalable_Display_TOP.md> "Scalable Display TOP")• [Screen Grab ](<./Screen_Grab_TOP.md> "Screen Grab TOP")• [Screen ](<./Screen_TOP.md> "Screen TOP")• [Script ](<./Script_TOP.md> "Script TOP")• [Select ](<./Select_TOP.md> "Select TOP")• [Shared Mem In ](<./Shared_Mem_In_TOP.md> "Shared Mem In TOP")• [Shared Mem Out ](<./Shared_Mem_Out_TOP.md> "Shared Mem Out TOP")• [SICK ](<./SICK_TOP.md> "SICK TOP")• [Slope ](<./Slope_TOP.md> "Slope TOP")• [Spectrum ](<./Spectrum_TOP.md> "Spectrum TOP")• [SSAO ](<./SSAO_TOP.md> "SSAO TOP")• [ST2110 In ](<./ST2110_In_TOP.md> "ST2110 In TOP")• [ST2110 Out ](<./ST2110_Out_TOP.md> "ST2110 Out TOP")• [Stype ](<./Stype_TOP.md> "Stype TOP")• [Substance Select ](<./Substance_Select_TOP.md> "Substance Select TOP")• [Substance ](<./Substance_TOP.md> "Substance TOP")• [Subtract ](<./Subtract_TOP.md> "Subtract TOP")• [SVG ](<./SVG_TOP.md> "SVG TOP")• [Switch ](<./Switch_TOP.md> "Switch TOP")• [Syphon Spout In ](<./Syphon_Spout_In_TOP.md> "Syphon Spout In TOP")• [Syphon Spout Out ](<./Syphon_Spout_Out_TOP.md> "Syphon Spout Out TOP")• Text • [Texture 3D ](<./Texture_3D_TOP.md> "Texture 3D TOP")• [Texture Sampling Parameters ](<./Texture_Sampling_Parameters.md> "Texture Sampling Parameters")• [Threshold ](<./Threshold_TOP.md> "Threshold TOP")• [Tile ](<./Tile_TOP.md> "Tile TOP")• [Time Machine ](<./Time_Machine_TOP.md> "Time Machine TOP")• [Tone Map ](<./Tone_Map_TOP.md> "Tone Map TOP")• [TOP ](<./TOP.md> "TOP")• [TOP Viewer ](<./TOP_Viewer.md> "TOP Viewer")• [Touch In ](<./Touch_In_TOP.md> "Touch In TOP")• [Touch Out ](<./Touch_Out_TOP.md> "Touch Out TOP")• [Transform ](<./Transform_TOP.md> "Transform TOP")• [Under ](<./Under_TOP.md> "Under TOP")• [Video Device In ](<./Video_Device_In_TOP.md> "Video Device In TOP")• [Video Device Out ](<./Video_Device_Out_TOP.md> "Video Device Out TOP")• [Video Stream In ](<./Video_Stream_In_TOP.md> "Video Stream In TOP")• [Video Stream Out ](<./Video_Stream_Out_TOP.md> "Video Stream Out TOP")• [Vioso ](<./Vioso_TOP.md> "Vioso TOP")• [Web Render ](<./Web_Render_TOP.md> "Web Render TOP")• [ZED Select ](<./ZED_Select_TOP.md> "ZED Select TOP")• [ZED ](<./ZED_TOP.md> "ZED TOP")
