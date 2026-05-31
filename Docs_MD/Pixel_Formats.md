# Pixel Formats

Pixel Formats is a specification of how the pixels of [TOPs](<./TOP.md> "TOP") are stored. Normally, TOPs are stored using an 8-bit pixel format. What this means is that each pixel of the TOP will have 8-bits of information for each of it's R, G, B and A channels (Red, Green, Blue, and Alpha). This adds up to a total of 32-bits of information per pixel. 8-bits of precision corresponds to a total of only 256 different values. Due to this low level of possible values, a 8-bit texture can only store values between 0 and 1 for each of its R, G, B and A channels. This format is usually adequate for most TOP and rendering operations. 

However, when doing some operations with 8-bit pixel format, some artifacts may appear such as color banding. When this occurs floating point pixel formats such as 16-bit and 32-bit floating point pixel formats can be used. Along with not being bounded to the [0-1] range, these formats can go negative and above one, they also have much higher precision. Floating point pixel formats are also used for High Dynamic Range (HDR) rendering. 

You can select the pixel format of any TOP using the Pixel Format parameter on the [Common](<./TOP_Generator_Common_Page.md> "TOP Generator Common Page") page of all TOPs. There are limitations with some pixel formats depending on your graphics card. For example, on most cards today the 32-bit pixel format can not use any [Texture Filtering](<./Texture_Filtering.md> "Texture Filtering") method other than Nearest Filtering. 

32-bit floating point format does not support any type of filtering. It will be forced to be nearest filtering everywhere that the TOP is used. 

## Fixed Point vs. Floating Point

Fixed point formats, regardless of if they are 8 or 16 bit, can only represent values between 0 and 1. The higher precision fixed point formats simply have more values between 0 and 1 they can represent. Floating point formats can represent very large values and very small values, both negative and positive. 

## Formats without all RGBA channels

For memory and performance optimization, there are formats that do not contain all Red, Green, Blue and Alpha channels. For example there are formats that only have a Red channel, or formats that only have Red and Green channels. When working with these formats other TOPs will treat any missing Red, Green and Blue channel as if it is 0, and any missing Alpha channel as if it is 1. 

## Depth TOP and Depth Textures

The Depth TOP creates an image in a special pixel format that only it can create. This is a high precision 24-bit fixed point format. It's values are bound between the range [0,1]. Other TOPs can use this TOP as an input without any loss of precision, but you will need to set the pixel format of your TOP to 32-bit to maintain the higher level of precision. Other TOPs will treat the depth texture's values as if they are RGBA = (D, D, D, 1). 

## Supported Pixel Formats
* **8-bit fixed (RGBA)** \- An RGBA format that has 8-bits per color channel, 32-bits total per pixel. Values are limited to the range [0-1].
  * **16-bit float (RGBA)** \- An RGBA format that has 16-bits per color channel, 64-bits per pixel. Values can be any number both negative and positive.
  * **32-bit float (RGBA)** \- An RGBA format that has 32-bits per color channel, 128-bits per pixels. Values can be any number both negative and positive.
* **10-bit RGB, 2-bit Alpha, fixed (RGBA)** \- An RGBA format that has 10-bits per color channel and 2-bits for alpha, 32-bits total per pixel. Values are limited to the range [0-1].
  * **16-bit fixed (RGBA)** \- An RGBA format that has 16-bits per color channel, 64-bits total per pixel. Values are limited to the range [0-1].
  * **11-bit float (RGB), Positive Values Only** \- An RGB floating point format that has 11 bits for the Red and Green channels, and 10-bits for the Blue Channel, 32-bits total per pixel (therefore the same memory usage as 8-bit RGBA). The Alpha channel in this format will always be 1. Values can go above one, but can't be negative. i.e. the range is [0, infinite).


**(R) formats** \- These formats only contain information for the red (R) channel. GB = 0 and A = 1 in these formats. 
* **8-bit fixed (R)** \- Has 8-bits for the red channel, 8-bits total per pixel. Values are limited to the range [0-1].
  * **16-bit fixed (R)** \- Has 16-bits for the red channel, 16-bits total per pixel. Values are limited to the range [0-1].
  * **16-bit float (R)** \- Has 16-bits for the red channel, 16-bits per pixel. Values can be any number both negative and positive.
  * **32-bit float (R)** \- Has 32-bits for the red channel, 32-bits per pixel. Values can be any number both negative and positive.


  
**(RG) formats** \- these formats only contain information for the red and green (RG) channels. B = 0 and A = 1 in these formats. 
* **8-bit fixed (RG)** \- Has 8-bits for the red and green channels, 16-bits total per pixel. Values are limited to the range [0-1].
  * **16-bit fixed (RG)** \- Has 16-bits for the red and green channels, 32-bits total per pixel. Values are limited to the range [0-1].
  * **16-bit float (RG)** \- Has 16-bits for the red and green channels, 32-bits per pixel. Values can be any number both negative and positive.
  * **32-bit float (RG)** \- Has 32-bits for the red and green channels, 64-bits per pixel. Values can be any number both negative and positive.


  
**(A) formats** \- These formats only contain information for the alpha (A) channel. RGB = 0 in these formats. 
* **8-bit fixed (A)** \- An Alpha only format that has 8-bits per channel, 8-bits per pixel. Values are limited to the range [0-1].
  * **16-bit float (A)** \- An Alpha only format that has 16-bits per channel, 16-bits per pixel.
  * **32-bit float (A)** \- An Alpha only format that has 32-bits per channel, 32-bits per pixel.
