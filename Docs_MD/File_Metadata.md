# File Metadata

  
[Movie File Out TOP](<./Movie_File_Out_TOP.md> "Movie File Out TOP") and [Audio File Out CHOP](<./Audio_File_Out_CHOP.md> "Audio File Out CHOP") allow users to provide a [Table DAT](<./Table_DAT.md> "Table DAT") of metadata key value pairs to be written to the file. Similarly [Movie File In TOP](<./Movie_File_In_TOP.md> "Movie File In TOP"), [Audio File In CHOP](<./Audio_File_In_CHOP.md> "Audio File In CHOP") and [Media File Info DAT](<./Media_File_Info_DAT.md> "Media File Info DAT") can read this metadata in. Below is a list of valid key values for the metadata table.   
  
## File Metadata

### Audio File Out Formats
* OGG: Supports arbitrary key value pairs stored as a`VorbisComment`* MP3: Supports metadata stored in its ID3v2 tag
  * AIFF: Supports metadata stored in its INFO chunk
  * WAV: Supports metadata stored in RIFF format

Formats  Tag | MP3 | WAV | AIFF   
---|---|---|---  
copyright | ✅ | ✅ | ✅   
comment | ✅ | ✅ | ✅   
title | ✅ | ✅ |   
author | ✅ | ✅ |   
album | ✅ |  | ✅   
genre | ✅ |  | ✅   
encoder | ✅ |  | ✅   
language | ✅ |  | ✅   
artist | ✅ |  | ✅   
date | ✅ |  | ✅   
composer | ✅ |  |   
album_artist | ✅ |  |   
performer | ✅ |  |   
disc | ✅ |  |   
publisher | ✅ |  |   
track | ✅ |  |   
rating | ✅ |  |   
lyrics | ✅ |  |   
compilation | ✅ |  |   
creation_time | ✅ |  |   
album-sort | ✅ |  |   
artist-sort | ✅ |  |   
title-sort | ✅ |  |   
description | ✅ |  |   
grouping | ✅ |  |   
network | ✅ |  |   
synopsis | ✅ |  |   
show | ✅ |  |   
episode_id | ✅ |  |   
year | ✅ |  |   
  
### Movie File Out Formats
* VP8/VP9: Supports arbitrary key value pairs in its Tag Directory
  * Movie formats support the following

Supported tags  artist | title | author | date   
---|---|---|---  
comment | description | genre | copyright   
  
  * OpenEXR supports arbitrary key value pairs
  * TIFF supports Exif metadata
  * JPEG supports Exif metadata
  * PNG supports Exif metadata

#### Exif Metadata
* JPEG and PNG are using libexif to generate Exif data and inserts them into its proper header when recording. [Supported tags](<https://libexif.github.io/internals/exif-tag_8h.html>)
  * TIFF is using libtiff to manage its Exif writing. [Supported tags](<http://www.simplesystems.org/libtiff/specification/coverage.html>)
  * Tags supporting multiple components can specify the components in a comma separated entry. i.e. 43,39,52.44

An example Exif headersdat  ImageDescription | my description   
---|---  
GPSLatitudeRef | N   
GPSLatitude | 43,38,52.44   
GPSLongitudeRef | W   
GPSLongitude | 79,23,42.072   
ISOSpeed | 800   
ApertureValue | 1.4   
ShutterSpeedValue | 1/300   
  
## See Also
* [Movie File Out TOP](<./Movie_File_Out_TOP.md> "Movie File Out TOP"), [Audio File Out CHOP](<./Audio_File_Out_CHOP.md> "Audio File Out CHOP"),[Movie File In TOP](<./Movie_File_In_TOP.md> "Movie File In TOP"), [Audio File In CHOP](<./Audio_File_In_CHOP.md> "Audio File In CHOP"), [Media File Info DAT](<./Media_File_Info_DAT.md> "Media File Info DAT")
