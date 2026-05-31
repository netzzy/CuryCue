# File Types

TouchDesigner can import and export most common media file formats. Files can be loaded into TouchDesigner by:   
  
  * [Drag-and-Drop](<./Drag-and-Drop.md> "Drag-and-Drop"): Drag a file directly into TouchDesigner and drop it to automatically create an OP or a component.
  * Open With... menu: Right-click on a TouchDesigner supported file in Windows and select Open With...->TouchDesigner 0xx to launch TouchDesigner with the file pre-loaded.
  * Load a file using Operators like [Movie File In TOP](<./Movie_File_In_TOP.md> "Movie File In TOP"), [File In CHOP](<./File_In_CHOP.md> "File In CHOP"), [File In SOP](<./File_In_SOP.md> "File In SOP"), [Audio File In CHOP](<./Audio_File_In_CHOP.md> "Audio File In CHOP"). Files can be loaded from disk or from the web using http://_file-url_.
  * Start TouchDesigner using the operating system shell command`touchdesigner filename.ext`, which will start TouchDesigner with your file pre-loaded.

## Native TouchDesigner Files

TouchDesigner has three native files types: 
* [.toe](<./.md> ".toe"): TouchDesigner Environment files are the default file type for creating projects.
  * [.tox](<./.md> ".tox"): TouchDesigner Component files let you save out components. .tox files enable the re-use and portability of component libraries.
  * [.tog](<./.md> ".tog"): TouchDesigner Geometry files are exports of other geometry types in a native TouchDesigner format.

## Files Imported

File Type | Supported Extensions | Operator Type   
---|---|---  
Image |`.tif .tiff .bmp .gif .hdr .jpeg .jpg .pic .png .swf .tga .dds .exr .dpx .ffs`| [Movie File In TOP](<./Movie_File_In_TOP.md> "Movie File In TOP")  
Movie |`.m4v .mkv .mov .mp4 .hsp .notchlc .mpeg .mpg .avi .flv .m2ts .wmv .h265 .vp8 .vp9 .3gp .mxf .ts .r3d`| [Movie File In TOP](<./Movie_File_In_TOP.md> "Movie File In TOP")  
Point Cloud |`.obj .ply .exr .xyz .pts .csv .txt .fits/.fit(astronomy format)`| [Point File In TOP](<./Point_File_In_TOP.md> "Point File In TOP")  
Audio |`.aif .aiff .wav .mp3 .flac .ogg .m4a .avi .flv .m2ts .m4v .mkv .mov .mp4 .mpeg .mpg .mts .wmv .3gp .mxf .ts .r3d`| [Audio File In CHOP](<./Audio_File_In_CHOP.md> "Audio File In CHOP"), [Audio Play CHOP](<./Audio_Play_CHOP.md> "Audio Play CHOP"), [File In CHOP](<./File_In_CHOP.md> "File In CHOP")  
Geometry and Scene |`[.usd, .usda, usdc, .usdz](<./USD.md> "USD") [.fbx](<./FBX.md> "FBX") .obj .3ds .dxf .dae .abc`| [USD COMP](<./USD_COMP.md> "USD COMP"), [FBX COMP](<./FBX_COMP.md> "FBX COMP"), [Geometry COMP](<./Geometry_COMP.md> "Geometry COMP"), [File In SOP](<./File_In_SOP.md> "File In SOP"), [Alembic SOP](<./Alembic_SOP.md> "Alembic SOP")  
Shader |`.glsl .frag .vert`, geometry shaders | [Text DAT](<./Text_DAT.md> "Text DAT")  
JSON |`.json`| [JSON DAT](<./JSON_DAT.md> "JSON DAT")  
Channel (Houdini) | .`bchan .bclip .chan .clip`| [File In CHOP](<./File_In_CHOP.md> "File In CHOP")  
Geometry (Houdini) |`.bhclassic .hclassic`| [File In SOP](<./File_In_SOP.md> "File In SOP")  
MIDI |`.mid .midi`| [MIDI In CHOP](<./MIDI_In_CHOP.md> "MIDI In CHOP")  
Script |`.bat .cmd .txt`| [Text DAT](<./Text_DAT.md> "Text DAT")  
Table |`.csv .dat`| [Table DAT](<./Table_DAT.md> "Table DAT")  
Font |`.ttf .otf`| [Text COMP](<./Text_COMP.md> "Text COMP"), [Geo Text COMP](<./Geo_Text_COMP.md> "Geo Text COMP")  
  
The Movie File In TOP also supports audio embedded in a movie. **Tip** : Tie an [Audio Movie CHOP](<./Audio_Movie_CHOP.md> "Audio Movie CHOP") to the Movie File In TOP to get the audio, then an [Audio Device Out CHOP](<./Audio_Device_Out_CHOP.md> "Audio Device Out CHOP") to play it. An [Info CHOP](<./Info_CHOP.md> "Info CHOP") attached to either operator gives extra inside info. 

## Files Exported

File Type | Supported Extensions | Operator Type or Dialog  
---|---|---  
Image |`.tif .tiff .jpeg .jpg .bmp .exr .png .dds`| File -> Create Movie, RMB menu   
Movie |`.mov .mp4 .hap .notchlc .h265 .vp8 .vp9`| [Movie File Out TOP](<./Movie_File_Out_TOP.md> "Movie File Out TOP"), File -> Create Movie   
Audio |`.aif .aiff .wav`| Save File on RMB menu   
Project |`.toe`| File -> Save Env   
Component and Scene |`.tox`| File -> Save, RMB menu components   
Channel |`.bchan .bclip .chan .clip`| [File Out CHOP](<./File_Out_CHOP.md> "File Out CHOP"), RMB menu   
Geometry |`.tog .bhclassic .fbx`| RMB menu   
MIDI |  | [MIDI Out CHOP](<./MIDI_Out_CHOP.md> "MIDI Out CHOP")  
Shader |`.frag .glsl .vert`| [Phong MAT](<./Phong_MAT.md> "Phong MAT")  
Script |`.py .html .md .dat .rtf .tsv .txt .xml`| RMB menu   
Table |`.dat`| RMB menu
