# DMX Map DAT

##   
  
Summary

The DMX Map DAT references a [DMX Out POP](<./DMX_Out_POP.md> "DMX Out POP") or a [DMX Fixture POP](<./DMX_Fixture_POP.md> "DMX Fixture POP") and outputs their DMX universes in table format. The DMX Map DAT is useful for visualizing DMX universe layouts and in the case of the DMX Out POP it can be helpful for debugging channel conflicts between DMX Fixture POPs. 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[dmxmapDAT_Class](<./DmxmapDAT_Class.md> "DmxmapDAT Class")

## 

Parameters - DMX Map Page

Active`active`\- When enabled, the DAT will grab up-to-date DMX universe data. When disabled, will hold the last universe state. 

Update Value`updateval`\- When enabled, the value column will update with the latest value. When disabled, it will hold the last value unless there is some change in the universe that rearranges channels. 

Update Value Pulse`updatevalpulse`\- When pulsed, will grab the update to the latest value. 

DMX Fixture/Out POP`dmxpop`\- The [DMX Fixture POP](<./DMX_Fixture_POP.md> "DMX Fixture POP") or [DMX Out POP](<./DMX_Out_POP.md> "DMX Out POP") from which to fetch the DMX universe data. 

Net Filter`netfilter`\- String regex to filter the table by net value. 

Subnet Filter`subnetfilter`\- String regex to filter the table by subnet value. 

Universe Filter`universefilter`\- String regex to filter the table by universe value. 

Network Address Filter`netaddressfilter`\- String regex to filter the table by netaddress value. 

Exclude Unused Channels`excludeunused`\- When disabled, all 512 channels of each DMX universe will be output to the table. When enabled, only the channels with a value set by the POP will be included in the output. 

## 

Parameters - Common Page

Language`language`\- ⊞ \- Select how the DAT decides which script language to operate on. 
* Input`input`\- The DAT uses the inputs script language.
* Node`node`\- The DAT uses it's own script language.


Edit/View Extension`extension`\- ⊞ \- Select the file extension this DAT should expose to external editors. 
* dat`dat`\- various common file extensions.
* From Language`language`\- pick extension from DATs script language.
* Custom Extension`custom`\- Specify a custom extension.


Custom Extension`customext`\- Specifiy the custom extension. 

Word Wrap`wordwrap`\- ⊞ \- Enable Word Wrap for Node Display. 
* Input`input`\- The DAT uses the inputs setting.
* On`on`\- Turn on Word Wrap.
* Off`off`\- Turn off Word Wrap.
