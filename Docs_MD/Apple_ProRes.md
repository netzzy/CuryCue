# Apple ProRes

Apple ProRes is a format with high image quality and excellent random access performance. It is less intensive to decode than H.26x codecs but can produce larger file sizes. 

TouchDesigner supports decoding and playback of ProRes in the [Movie File In TOP](<./Movie_File_In_TOP.md> "Movie File In TOP"), and encoding of ProRes files via the [Movie File Out TOP](<./Movie_File_Out_TOP.md> "Movie File Out TOP"). These operations are hardware accelerated on [macOS](<./MacOS.md> "MacOS") (Turn on the Movie File In TOP's 'Hardware Decode' parameter toggle on the Tune page). There is no support for hardware decode/encode on Windows. 

TouchDesigner supports all 6 standard ProRes formats which you can read about here [About Apple ProRes](<https://support.apple.com/en-ca/102207>). 

All ProRes422-variants are 4:2:2 at 10-bit color depth whereas ProRes 4444 and 4444 XQ is 4:4:4 schema with a color depth of 10 or 12 bits. ProRes 4444 and 4444XQ has the option to include an alpha channel. 

TouchDesigner does not currently support Apple ProRes RAW. 

See also  
[About Apple ProRes](<https://support.apple.com/en-ca/102207>)  
[Apple ProRes White Paper](<https://www.apple.com/final-cut-pro/docs/Apple_ProRes_White_Paper.pdf>)
