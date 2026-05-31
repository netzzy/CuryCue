# Serial DAT

##   
  
Summary

The Serial DAT is used for serial communication through an external port, using the RS-232 protocol. These ports are usually a 9 pin connector, or a USB port on new machines. (Using a USB port requires a USB-to-serial adapter and driver.) All of a computer's available serial ports can be found in the Device Manager in the Windows operating system under Computer –> Manage -> Devices -> Serial… -> COM ports. Their names begin with 'COM'. Example: COM1, COM2, COM3. 

To send bytes out this connection, see the send methods in the [serialDAT_Class](<./SerialDAT_Class.md> "SerialDAT Class"), or in Tscript the`send`Command. 

See also [Arduino](<./Arduino.md> "Arduino") and [Serial CHOP](<./Serial_CHOP.md> "Serial CHOP"). 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[serialDAT_Class](<./SerialDAT_Class.md> "SerialDAT Class")

## 

Parameters - Connect Page

Active`active`\- This check box enables the serial connection. 

Row/Callback Format`format`\- ⊞ \- Interpret the incoming data as binary or ASCII data. If the format is Per Byte, one row is appended for each binary byte received. If the format is Per Line, one row is appended for each null or newline delimited message received. 
* One Per Byte`perbyte`\- (formerly called 'binary').
* One Per Line`perline`\- (formerly called 'Ascii') null/newln delimited.
* One Per Message`permessage`\- Full incoming msg.


Port`port`\- Selects the COM port that the serial connection will use. Default port names 1 through 8 are available in the popup menu, though any name can be manually entered in this field. 

Baud Rate`baudrate`\- ⊞ \- The maximum number of bits of information, including "control" bits, that are transmitted per second. Check your input device's default baud rate and set accordingly. 
* 1200`1200`-
* 2400`2400`-
* 9600`9600`-
* 19200`19200`-
* 38400`38400`-
* 57600`57600`-
* 115200`115200`-
* 230400`230400`-
* 460800`460800`-
* 921600`921600`-
* 1382400`1382400`-


Data Bits`databits`\- ⊞ \- This parameter sets the number of data bits sent in each. Data bits are transmitted "backwards". Backwards refers to the order of transmission, which is from least significant bit (LSB) to most significant bit (MSB). To interpret the data bits, you must read from right to left. 
* 6`6`-
* 7`7`-
* 8`8`-
* 9`9`-


Parity`parity`\- ⊞ \- This parameter can be set to none, even, or odd. The optional parity bit follows the data bits and is included as a simple means of error checking. Parity bits work by specifying ahead of time whether the parity of the transmission is to be even or odd. If the parity is set to be odd, the transmitter will then set the parity bit in such a way as to make an odd number of 1's among the data bits and the parity bit. 
* Even`even`-
* Odd`odd`-
* None`none`-


Stop Bits`stopbits`\- ⊞ \- The last part of transmission packet consists of 1 or 2 Stop bits. The connection will now wait for the next Start bit. 
* 1`1`-
* 2`2`-


DTR`dtr`\- ⊞ \- The DTR (data-terminal-ready) flow control. (Windows Only). 
* Disable`disable`\- Disables the line when device is opened.
* Enable`enable`\- Enables the line when device is opened.
* Handshake`handshake`\- Enables handshaking with the device.


RTS`rts`\- ⊞ \- The RTS (request-to-send) flow control. (Windows Only). 
* Disable`disable`\- Disables the line when device is opened.
* Enable`enable`\- Enables the line when device is opened.
* Handshake`handshake`\- Enables RTS handshaking.
* Toggle`toggle`\- Line high only when bytes available.

## 

Parameters - Received Data Page

Callbacks DAT`callbacks`\- The Callbacks DAT will execute once for each message received. 

Execute from`executeloc`\- ⊞ \- Determines the location the script is run from. 
* Current Node`current`\- The script is executed from the current node location.
* Callbacks DAT`callbacks`\- The script is executed from the location of the DAT specified in the Callbacks DAT parameter.
* Specified Operator`op`\- The script is executed from the component specified in the Component parameter below.


From Operator`fromop`\- The path that the script will be executed from if the Execute From parameter is set to Specified Operator. 

Clamp Output`clamp`\- The DAT is limited to 100 messages by default but with Clamp Output, this can be set to anything including unlimited. 

Maximum Lines`maxlines`\- Limits the number of messages, older messages are removed from the list first. 

Clear Output`clear`\- Deletes all lines except the heading. To clear with a script command, here is an example:`opparm -c /serial1 clear`Bytes Column`bytes`\- Outputs the raw bytes of the message in a separate column. 

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

## 

Info CHOP Channels

Extra Information for the Serial DAT can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). 

### 

Specific Serial DAT Info Channels
* bytes_read -
* bytes_written -
* bytes_write_queued -
* bytes_write_rate -
* messages_pending -

### 

Common DAT Info Channels
* num_rows \- Number of rows in this DAT.
* num_cols \- Number of columns in this DAT.

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


  
TouchDesigner Build: Latest\n2021.100002018.28070before 2018.28070

DATs   
---  
[Art-Net ](<./Art-Net_DAT.md> "Art-Net DAT")• [Audio Devices ](<./Audio_Devices_DAT.md> "Audio Devices DAT")• [CHOP Execute ](<./CHOP_Execute_DAT.md> "CHOP Execute DAT")• [CHOP to ](<./CHOP_to_DAT.md> "CHOP to DAT")• [Clip ](<./Clip_DAT.md> "Clip DAT")• [Convert ](<./Convert_DAT.md> "Convert DAT")• [CPlusPlus ](<./CPlusPlus_DAT.md> "CPlusPlus DAT")• [DAT ](<./DAT.md> "DAT")• [ Execute ](<./DAT_Execute_DAT.md> "DAT Execute DAT")• [DAT Export ](<./DAT_Export.md> "DAT Export")• [Error ](<./Error_DAT.md> "Error DAT")• [EtherDream ](<./EtherDream_DAT.md> "EtherDream DAT")• [Evaluate ](<./Evaluate_DAT.md> "Evaluate DAT")• [Examine ](<./Examine_DAT.md> "Examine DAT")• [Execute ](<./Execute_DAT.md> "Execute DAT")• [FIFO ](<./FIFO_DAT.md> "FIFO DAT")• [File In ](<./File_In_DAT.md> "File In DAT")• [File Out ](<./File_Out_DAT.md> "File Out DAT")• [Folder ](<./Folder_DAT.md> "Folder DAT")• [In ](<./In_DAT.md> "In DAT")• [Indices ](<./Indices_DAT.md> "Indices DAT")• [Info ](<./Info_DAT.md> "Info DAT")• [Insert ](<./Insert_DAT.md> "Insert DAT")• [JSON ](<./JSON_DAT.md> "JSON DAT")• [Keyboard In ](<./Keyboard_In_DAT.md> "Keyboard In DAT")• [Lookup ](<./Lookup_DAT.md> "Lookup DAT")• [Media File Info ](<./Media_File_Info_DAT.md> "Media File Info DAT")• [Merge ](<./Merge_DAT.md> "Merge DAT")• [MIDI Event ](<./MIDI_Event_DAT.md> "MIDI Event DAT")• [MIDI In ](<./MIDI_In_DAT.md> "MIDI In DAT")• [Monitors ](<./Monitors_DAT.md> "Monitors DAT")• [MPCDI ](<./MPCDI_DAT.md> "MPCDI DAT")• [MQTT Client ](<./MQTT_Client_DAT.md> "MQTT Client DAT")• [Multi Touch In ](<./Multi_Touch_In_DAT.md> "Multi Touch In DAT")• [NDI ](<./NDI_DAT.md> "NDI DAT")• [Null ](<./Null_DAT.md> "Null DAT")• [OP Execute ](<./OP_Execute_DAT.md> "OP Execute DAT")• [OP Find ](<./OP_Find_DAT.md> "OP Find DAT")• [OSC In ](<./OSC_In_DAT.md> "OSC In DAT")• [OSC Out ](<./OSC_Out_DAT.md> "OSC Out DAT")• [Out ](<./Out_DAT.md> "Out DAT")• [Panel Execute ](<./Panel_Execute_DAT.md> "Panel Execute DAT")• [Parameter ](<./Parameter_DAT.md> "Parameter DAT")• [Parameter Execute ](<./Parameter_Execute_DAT.md> "Parameter Execute DAT")• [ParGroup Execute ](<./ParGroup_Execute_DAT.md> "ParGroup Execute DAT")• [Perform ](<./Perform_DAT.md> "Perform DAT")• [POP to ](<./POP_to_DAT.md> "POP to DAT")• [Render Pick ](<./Render_Pick_DAT.md> "Render Pick DAT")• [Reorder ](<./Reorder_DAT.md> "Reorder DAT")• [Script ](<./Script_DAT.md> "Script DAT")• [Select ](<./Select_DAT.md> "Select DAT")• Serial • [Serial Devices ](<./Serial_Devices_DAT.md> "Serial Devices DAT")• [SocketIO ](<./SocketIO_DAT.md> "SocketIO DAT")• [SOP to ](<./SOP_to_DAT.md> "SOP to DAT")• [Sort ](<./Sort_DAT.md> "Sort DAT")• [Substitute ](<./Substitute_DAT.md> "Substitute DAT")• [Switch ](<./Switch_DAT.md> "Switch DAT")• [Table ](<./Table_DAT.md> "Table DAT")• [TCP/IP ](<./TCP/IP_DAT.md> "TCP/IP DAT")• [Text ](<./Text_DAT.md> "Text DAT")• [Touch In ](<./Touch_In_DAT.md> "Touch In DAT")• [Touch Out ](<./Touch_Out_DAT.md> "Touch Out DAT")• [Transpose ](<./Transpose_DAT.md> "Transpose DAT")• [TUIO In ](<./TUIO_In_DAT.md> "TUIO In DAT")• [UDP In ](<./UDP_In_DAT.md> "UDP In DAT")• [UDP Out ](<./UDP_Out_DAT.md> "UDP Out DAT")• [UDT In ](<./UDT_In_DAT.md> "UDT In DAT")• [UDT Out ](<./UDT_Out_DAT.md> "UDT Out DAT")• [Video Devices ](<./Video_Devices_DAT.md> "Video Devices DAT")• [Web Client ](<./Web_Client_DAT.md> "Web Client DAT")• [Web ](<./Web_DAT.md> "Web DAT")• [Web Server ](<./Web_Server_DAT.md> "Web Server DAT")• [WebRTC ](<./WebRTC_DAT.md> "WebRTC DAT")• [WebSocket ](<./WebSocket_DAT.md> "WebSocket DAT")• [XML ](<./XML_DAT.md> "XML DAT")
