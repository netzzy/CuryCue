# Color Space

See also [Color Space Workflows](<./Color_Space_Workflows.md> "Color Space Workflows")

## Overview

A Color Space defines what 'true' color an RGB value specifies. For example, what light wavelength should (1, 0, 0) create out of your display device. Different color spaces will produce a different shade of red when (1, 0, 0) is converted into light. To ensure an image produces the same colors when shown on one display device vs. another display device, an image/movie must include information about what color space it was saved in. That way an application can ensure the correct values are sent to display. For example (1, 0, 0) on one device, then taken to another device that can show deeper shades of red, may need to be sent (0.8, 0, 0), to achieve the same final color of red. Without that color space information, the image will look more saturated (redder) on the second display, than on the first display. 

The same is true for devices that capture images such as cameras. They need to specify what color space they are saving their data in, so anyone consuming the content can display it properly. 

Display devices can only display a small portion of colors compared to what the human eye can see. For example the [sRGB](<https://en.wikipedia.org/wiki/SRGB>) color space, which most commercial computer monitors are limited to, only covers 35% of the colors the human eye can actually see. 

## A Primer on Color

The range of colors visible by the human eye was tested and recorded in the [CIE 1931 color space](<https://en.wikipedia.org/wiki/CIE_1931_color_space>). This 2D graph is used to help specify visible color gamuts (one of the two main parts of a color space) by specifying triangles on that chart. For example [sRGB](<https://en.wikipedia.org/wiki/SRGB>) can be seen as a triangle much smaller than the human visible range. Most monitor can produce colors within that triangle. Higher end monitors and HDR TVs, often can product colors within the larger [DCI-P3](<https://en.wikipedia.org/wiki/DCI-P3>) triangle. The [Rec.2020](<https://en.wikipedia.org/wiki/Rec._2020>) gamut is used often when communicating between applications/devices, since it a very large gamut that can hold all of the colors the application wants to show and the device could conceivably show, without losing data. Only very high-end Pro monitors for artists and editors can show Rec.2020 usually. 

### Color Incorrect Display

One thing that can be confusing when looking at the CIE graph, is that since you are looking at it on a monitor, it may be strange that you can see gradident changes all the way to the edge of the recorded human range, even though your monitor can't show gradients that far outside it's gamut. What is happening here is the one of the pitfalls of the way non-color correct display devices/applications function. If that CIE graph was displayed correctly on your monitor, then you would see the color gradients clamp at the limits of your monitor's color limitations, usually around where the sRGB triangle is, with just solid colors outside of that. However since that graph has values ranging from (1, 0, 0) -> (0, 1, 0) -> (0, 0, 1) at it's 3 corners, your monitor is showing those values as what it is able to show for it's max red, max green and max blue. In the future when these pages are displayed in a more color correct way, the values will be clamped on the monitor. Currently if you look at that same graph on a another monitor with a wider gamut, you'd see more saturated colors at the edges. 

On a standard monitor you can likely change all kinds of settings such as Hue, Saturation, Brightness, which can further adjust the colors that are shown. This results in the colors you are seeing likely not being the actual colors the author of content intended. 

### Gamut

As discussed before, a gamut defines the triangle on the CIE graph that the color space defines. This defines what (1, 0, 0), (0, 1, 0), (0, 0, 1) mean in terms of true colors visibly by the human eye. When you look at (1, 0, 0) as defined by the sRGB gamut compared to (1, 0, 0) as defined by the Rec.2020 gamut, on a monitor that supports such a wide gamut, you'll actually see that we've all been looking at a shade of orange on our sRGB monitors for years, rather than a deep red. 

A gamut is defined by 3 xy coordinates for the 3 corners of the triangle, which represent the red, green and blue corners of the triangle. Additionally a 'white point' is selected for the gamut in the center, which is often known as D65 or D60 for most color spaces, and is also defined using it's xy coordinate in the CIE graph. For example the coordinates for the primaries for Rec.2020 are defined as: 

Color space  | White point  | Primaries   
---|---|---  
xW | yW | xR | yR | xG | yG | xB | yB  
Rec.2020  | 0.3127  | 0.3290  | 0.708  | 0.292  | 0.170  | 0.797  | 0.131  | 0.046   
  
### Transfer Function

Along with a gamut, a color space also defines a [Transfer Function](<https://en.wikipedia.org/wiki/Transfer_functions_in_imaging>). This defines a curve (often known as Gamma), by which the data is stored in the file and sent to the display. This transfer function can serve many different purposes. With 8-bit data, sRGB content is saved using an sRGB transfer function, which allows the limited 256 steps of values that 8-bit provides to be better utilized. The transfer functions causes more steps of data to be used in the darker color range, which the human eye is more sensitive to. This helps reduce banding artifacts by giving more steps at the darker levels and less for the brighter ones. With more bits of precision, a transfer function can be less important for saving file data. For example 16-bit float EXR files generally always use a linear transfer function. The transfer function that is conventionally used with a gamut is chosen by standards committees usually, and although they are chosen for good reasons, there is no direct rule that a certain transfer function must be used with a certain gamut. 

Whenever you are actually combining colors (such as with compositing them, or using them in lighting calculations), you always want to be doing this with linear values. So a file that was saved with sRGB gamut with sRGB transfer, may be converted in GPU RAM to sRGB gamut and linear transfer before compositing is applied to it's content. 

Another important use for transfer functions is when communicating with a monitor. Monitor's will expect the data sent to them to be in the same transfer function that they use to display the content. So a sRGB monitor will want values sent to it using an sRGB transfer. This means after compositing the linear values will be converted back to sRGB transfer before being sent to the sRGB monitor. 

Converting beteen linear and a non-linear transfer is done with two equations (which are the inverse of each other. OETF (opto-electronic transfer function), which converts from linear to non-linear values, and EOTF (electro-optical transfer function), which converts from non-linear to linear. 

### Brightness

Another concept important to understand with color is how brightness is defined. How bright should (1, 1, 1) on a monitor? You can certainly turn up your brightness to adjust this, but that may not match what the content author intended. Brightness for color in computers is defined using a term called a [Nit](<https://en.wikipedia.org/wiki/Candela_per_square_metre>). Also defined as Candela per square meter, or cd/m2. Most standard monitors can show between 100 and 300 nits of brightness. A consumer grade HDR monitor may be able to show 500-700 nits, while a Pro one can show 1500-2500 nits. A 100-watt lightbulb is 1,600 nits, while the sun is 1.6 billion nits. The amount of nits that (1, 1, 1) should represent also depends on the viewer setting. A darker room requires less nits to achieve the same perceived brightness. Movie theater projectors for example may only show 75 nits. 

## How Computers and Monitors Display Color

In the past usually all the content (JPEGs for example) was saved in sRGB color space, and the monitors were expected to be showing sRGB color space. So you could take the values in that JPEG file and send them as-is to the monitor without any adjustment, and they would look correct. Modern image/movie formats though are often in many different color spaces, and monitors can display wider gamuts and have different amounts of maximum nits available. If you were to blindly take (1, 0, 0) from a file format and show it on different monitors with different gamuts, transfer characteristics and max nits, you'd get widely different shades of reds, and brightness levels. Being color spaces aware corrects for this by reading the files using known color spaces, and communicating with the monitor in it's expected color space, by converting between the file's color space the monitors color space. 

Both Windows and macOS have settings to control if a monitor is being driven with an SDR or an HDR signal (for HDR capable monitors). This changes mode the monitor is running in, as well as the type of data that is sent down the cable to the monitor. 

### SDR (Standard Dynamic Range) Display

SDR mode is essentially a 'dumb' mode, that contains no color space information inherently. The monitor may have controls to select which color space it should be running in, and it'll likely have other controls that can make content more saturated/vibrant. Changing these types of controls have no direct correlation to the color space being displayed, and without a calibration tool, likely will cause the colors to not correctly match the desired color space. 

Since there is no color space information exchanged between the OS and the monitor, the monitor will just display the value (1, 0, 0) as the brightness and reddest-red it is currently setup to show. 

To show colors correctly, you need to send data across the wire in the same color space that the monitor is showing. So if you have a monitor set to sRGB, then you need to send it sRGB color space colors. In the past this was done with ICC profiles, which would be used to convert from the color space the application is working in, into the color space of the monitor. 

### HDR (High Dynamic Range) Display

HDR is a different mode that HDR monitors can be driven in. This is a setting that is done in the OS, in the display settings. When in this mode the signal sent over the wire contains exact information about what color space the data is in, allowing the monitor to show the colors and brightness correctly. Usually this data is sent in a very wide gamut (Rec.2020) and using a transfer function such as the [ST2084 PQ](<https://en.wikipedia.org/wiki/Perceptual_quantizer>) function, which allows the data to encapsulate colors likely far beyond what the monitor can do, as well as brightness values much higher than what the monitor can do (PQ does up to 10,000 nits). 

When the [Window COMP](<./Window_COMP.md> "Window COMP") or the editor window is set to use an HDR pixel format, if the OS isn't already running a monitor in HDR mode, then it'll flip the monitor into that mode, causing a screen flicker. It's is not advised to use HDR pixel formats when not in HDR mode, since the monitor may flicker back and forth between SDR and HDR mode, depending on what each application that has focus is running at. 

## SDR vs HDR

When people talk about HDR the main thing that is spoken of is the brightness. HDR is meant to allow pieces of a scene such as lights or the sun to be dramatically brighter than other parts of the scene. This is done by encoding the desired brightness into the pixel data, and the monitor will attempt to show it at the desired brightness, if it's able to. 

This is different from SDR, where (1, 1, 1) is simply the brightest the monitor can run at in SDR mode. The brightness is simply whatever brightness the monitors settings are set to. 

HDR usually (but doesn't have to) also mean a wider gamut than what is usually used for SDR. Similarly, SDR can have a wider gamut, without being HDR. However as mentioned before, since there is no information sent across the wire about the SDR color space that is active, HDR is a much better way to drive wide gamut data as well. HDR colors can go above (1, 1, 1), allowing them to become 'over-bright', and drive the display to brighter pixels that content which falls in the normal [0, 1] range. 

### Reference White

Reference white, also often known as 'paper white', is a concept used to help decide how bright (1, 1, 1) should be. When dealing with SDR content, generally (1, 1, 1) is meant to be shown somewhere between 80 and 120 nits, depending on the brightness of the room. And this is as bright as the display will go with it's current settings. When creating SDR content, (1, 1, 1) is used to create the brightest pixels possible. 

Reference white is also called paper white since (1, 1, 1) is expected to be about as bright as a white piece of paper in the room when in HDR mode. So in HDR mode (1, 1, 1) is not meant to be particularly bright, but instead a neutral white. This allows the authors to more easily over-drive the values to make bright highlights. When mixing content authoring on SDR displays, it make not appear the desired brightness when mixed with HDR content. See the [Color Space Workflows](<./Color_Space_Workflows.md> "Color Space Workflows") article on information on how to control how bright reference white is with SDR vs HDR content. 

### Pixel Data

Since HDR content needs to be able to define very bright colors, it is authored using 16-bit or 32-bit floats. This allows colors to be chosen that are much brighter than the reference white level. For example of the HDR Reference White is set to 120 nits, then a pixel color of (10, 10, 10), should attempt to be shown as 1200 nits, if the monitor is able to. 

## HDR Transfer Functions

The two most popular HDR transfer functions are the [ST2084 PQ](<https://en.wikipedia.org/wiki/Perceptual_quantizer>) and the [Hybrid Log Gamma](<https://en.wikipedia.org/wiki/Hybrid_log%E2%80%93gamma>) functions. Although HDR content is authored using floating point values, data that is sent across the wire (HDMI/DisplayPort/SDI/ST2110/NDI) and data saved to most file formats that are compressed (H264, JPEG), use only fixed point data. That means values outside of [0, 1] can not be stored. Therefore when a transfer function is designed, it may specify how bright a value of 1.0 will be. This can be chosen to be anything. The ST2084 PQ transfer chooses this to be 10,000 nits. HLG does not specify what the maximum is, but content is often mastered such that 1.0 is 1,000 or 4,000 nits. 

Most high end content is saved using the 2084 PQ transfer curve, since that has a well defined brightness which a high brightness maximum, making it forward compatible with displays in the future. PQ encoded content will look incorrect on if displayed on a SDR display as-is without any conversion or tone-mapping. The benefit of HLG is that the content will still look 'ok-ish', when displayed on an SDR display. This is because the curve is about the same shape as a SDR curve. 

Since fixed point has a very limited number of values it can represent (10-bit being only 1024 values, for example), but brightness can go between 0 and 10,000 for PQ, a non linear curve is used to encode the data. This is done because most of the pixels will be 200 nits or less, so if the brightness was distributed linearly then only the lowest 20 steps of the 1024 steps in the 10-bit data would be used for the majority of the content, causing extreme banding. 

PQ instead encodes the first 512 steps, [0, 0.5], to be approximately 0 to 90 nits, then rising sharply from there. 0.6 is 245 nits, 0.7 is 621 nits, 0.8 is 1555 nits, 0.9 is 3910 nits and 1.0 is 10,000 nits. The graph in the [Perceptual quantizer](<https://en.wikipedia.org/wiki/Perceptual_quantizer>) shows this curve. 

Using a curve such as this also makes content more forward compatible. As displays become better, the higher brightness values can be shown correctly, without re-encoding the data. 

## Tone Mapping and Gamut Mapping

Tone and Gamut mapping is the process of taking content that has very high brightness (tone mapping), or colors deep outside the regular capabilities of a display (gamut mapping), and attempting to make that content look good on the displays that can't show the content exactly as authored. 

In an ideal world tone and gamut mapping would not be needed, and the display would be able to show the content directly as the creator intended. 

### Tone Mapping

Tone Mapping is a term that often used along with HDR content. Tone Mapping takes HDR content with a wide range of brightnesses, and determine how to display that information on a display that has a far more limited capabilities. It is often used to take HDR content and display it on SDR monitors. With true HDR monitors available now, tone mapping still may be used to map content authored with a certain peak-brightness (say, 4000 nits) to the actual peak brightness of the monitor (say, 1000 nits). When calibrating HDR for a video game, the actual peak brightness capability of the display is what the calibration tool is measuring. Movie files often contain metadata about the peak and average brightness available. Sometimes this metadata is for the entire file, while other standards allow it to change throughout the file. TVs have different HDR settings to control how to make use of this information to tone-map the content to it's own known capabilities. Without tone mapping a scene that has a area having a brightness range between 1000-4000 nits, but shown on a 1000 max nit monitor, would just show the same brightness for that entire area. This would look washed out to the viewer. Tone mapping map instead re-range that area to be between 700-1000 nits, so the brightness variation is still perceptible. 

### Gamut Mapping

Gamut mapping is much less well known. Likely because content is rarely authored using colors very far outside the range of what a typical display can show. Usually sRGB for video games, and DCI-P3 or Display-P3 for other media such as movies and TV. 

In the Rec.2020 color space, a (1, 0, 0) red is far deeper red than (1, 0, 0) in the sRGB color space. If for example an image has a gradient going from (0, 0, 0) to (1, 0, 0) in Rec.2020 color space, how should that be shown on a sRGB capable display? The two options are to just clamp colors outside the range, which means the gradient would stop looking like it's changing at around 75%-80% of the way through. The other option is to re-range the gradient so color changes occur throughout still, however this means none of the colors accurately represent the source material. Like tone mapping, the clamping can show up as looking like the image is washed out. 

## Working Color Space

Much like how when doing work involving measurements, the 'units' used to describe things needs to be agreed on. Feet, Meters, inches etc. If you bring in data that is in another unit, you'd want to convert it to whatever unit you are internally using, so the values are meaningful together. You don't want to be adding 1 foot to 1 meter. A Working Color Space is the 'units' used to describe color values in a project. It defines what a value of (1, 0, 0) means; which shade of red to use. All the data (images, movies, color values) need to be converted into a the same color space when they are combined together, so that the combined colors are being added/multiplied etc. in the same space. Additionally, compositing should always be done using linear values, so if the colors are defined using a non-linear transfer function, they need to be linearized before they are worked with. 

TouchDesigner supports many working color spaces, such as sRGB, ACEScg Rec.2020, DCI-P3 and ACES 2065-1. 

Learn more about how to select the working color space in the [Color Space Workflows](<./Color_Space_Workflows.md> "Color Space Workflows") article. 

## Further Reading

Other useful articles about color space:  
<https://gitlab.freedesktop.org/pq/color-and-hdr/-/blob/main/doc/learn.md>  
<https://developers.meta.com/horizon/design/display/>
