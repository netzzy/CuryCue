# Material Design Icons

TouchDesigner includes the "Material Design Icons" font which can be used to create nice looking icons in places where normally text will go. Any label parameter will take Unicode strings as long as the selected font supports the Unicode codes. 

### Material Design Icons Info

TouchDesigner 2022.20000+ builds come with Material Design Icons desktop version. The repo for this font is located here: <https://github.com/Templarian/MaterialDesign-Font>

The **cheatsheet** for the MDI version installed with TouchDesigner can be found in the TouchDesigner installation in the folder`Samples/Fonts/MaterialDesignIconsCheatsheet.html`. You will also find there the font file itself,`MaterialDesignIconsDesktop.ttf`and a`MaterialDesignIconsMeta.json`file with all the font descriptions. **TIP:** To open the`Samples`folder, pick Help > Browse Samples in the main TouchDesigner menu. 

The cheatsheet originates from <https://materialdesignicons.com/>. 

### Using Material Design Icons

In a [Text COMP](<./Text_COMP.md> "Text COMP"), [Geo Text COMP](<./Geo_Text_COMP.md> "Geo Text COMP"), [Text TOP](<./Text_TOP.md> "Text TOP") or other operator that displays text, set the Font parameter to Material Design Icons. 

To pick an icon, scroll through the list of icons on the Material Design Icons Cheat Sheet or search for text related to the icon you want. 

Click the HexCode beside the icon thumbnail and it will copy the hexadecimal string to the copy buffer. 

To display an icon use an expression in the operator's text parameter, with the Python`chr`function as follows:`chr(0x`<paste hex code here>`)`or more specifically, if you copied`'F0EF4'``chr(0xF0EF4)`
