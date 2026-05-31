# Web Client DAT

##   
  
Summary

The Web Client DAT allows you to send HTTP requests to web servers from TouchDesigner. It supports GET, POST, PUT, DELETE, HEAD, OPTIONS and PATCH http methods. 

The Web Client DAT supports various authentication types such as: basic, oauth1, oauth2. 

The Web Client DAT allows for streaming from web servers. 

The Web Client DAT sends HTTP requests to web servers and then outputs the response in the DAT. With streaming enabled it can stream data from a web server. 

When streaming is enabled, Clamp Output as Rows should be enabled. This turns the output of the DAT into a FIFO table instead of raw text. Only the last N lines will be displayed, where N is the value of the Maximum Lines parameter. This will prevent the text in the DAT from getting too larger and will keep cook-times down as a result. 

The Web Client DAT supports sending of GET, POST, PUT, DELETE, HEAD, OPTIONS, and PATCH request methods. The Web Client DAT also supports 4 authentication methods: Basic, Digest, OAuth1, and OAuth2. 

The first input is the extra headers to send in the request. It should be a table with 2 columns, structured as name/value pairs. For example: 

Content-Type  | application/json   
---|---  
Connection  | Close   
  
The second input is the data/parameters to send in the request. This can be a table with two columns, structured as name/value pairs. It can also just be text, in which case it will be sent as is. If the request method doesn't have a request body (eg. GET, OPTIONS) then it will append the input to the URL as query parameters if a table, otherwise it will be sent as the request data. 

name  | joe   
---|---  
month  | May   
  
The Web Client DAT is the successor to the [Web DAT](<./Web_DAT.md> "Web DAT"). 

See also: [Web Server DAT](<./Web_Server_DAT.md> "Web Server DAT"), [SocketIO DAT](<./SocketIO_DAT.md> "SocketIO DAT"), [XML DAT](<./XML_DAT.md> "XML DAT"), [TCP/IP DAT](<./TCP/IP_DAT.md> "TCP/IP DAT"), [WebSocket DAT](<./WebSocket_DAT.md> "WebSocket DAT"), [Web DAT](<./Web_DAT.md> "Web DAT"). 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[webclientDAT_Class](<./WebclientDAT_Class.md> "WebclientDAT Class")

## 

Parameters - Web Client Page

Active`active`\- Toggles the operator on/off. 

Request Method`reqmethod`\- ⊞ \- Selects the [HTTP request method](<https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods>). 
* GET`get`\- The GET method requests a representation of the specified resource. Requests using GET should only retrieve data.
* POST`post`\- The POST method is used to submit an entity to the specified resource, often causing a change in state or side effects on the server.
* PUT`put`\- The PUT method replaces all current representations of the target resource with the request payload.
* DELETE`delete`\- The DELETE method deletes the specified resource.
* HEAD`head`\- The HEAD method asks for a response identical to that of a GET request, but without the response body.
* OPTIONS`options`\- The OPTIONS method is used to describe the communication options for the target resource.
* PATCH`patch`\- The PATCH method is used to apply partial modifications to a resource.


URL`url`\- The URL of the server to send the HTTP request. Generally, if sending an HTTP request to a secure server, then the URL should begin with "https://". 

Upload File`uploadfile`\- The contents of the upload file will be sent to the server (chunked, if necessary). 

Request`request`\- Sends the request 

Stop`stop`\- Stops the stream of data from the server. 

Stream`stream`\- Enables streaming. This is only necessary to enable if the server support streaming. 

Verify Certificate (SSL)`verifycert`\- Enables TLS (transport layer security) certificate verification. 

Timeout`timeout`\- Timeout time in milliseconds of the request if no response is received from the web server. 

Include Header in Output`includeheader`\- Includes the header in the output of the response. 

## 

Parameters - Authentication Page

Authentication Type`authtype`\- ⊞ \- The type of authentication. 
* None`none`\- No authentication
* Basic`basic`\- Basic authentication is base-64 encoded username and password.
* Digest`digest`\- Digest authentication is base-64 encoded username and password that's encrypted with a hashing function. Digest is a more secure version of Basic authentication.
* OAuth1`ouath1`\- Version 1 of OAuth. OAuth1 requires App Key, App Secret, User OAuth Token, and User OAuth Secret. These can be found via the account on the web server that request is being sent to. For example, in the case of the Twitter API the values of these 4 parameters can be found under the account profile.
* OAuth2`ouath2`\- Version 2 of OAuth. OAuth2 first requires an HTTP request be sent to the web server to acquire the Client ID and token. It can be acquired using a browser.


Username`username`\- Username used in Basic/Digest authentication. 

Password`pw`\- Password used in Basic/Digest authentication. 

App Key`appkey`\- OAuth1 App Key retrieved from web server. 

App Secret`appsecret`\- OAuth1 App Secret retrieved from web server. 

User OAuth Token`oauthtoken`\- OAuth1 user token retrieved from web server. 

User OAuth Secret`oauthsecret`\- OAuth1 user secret retrieved from web server. 

Client ID`clientid`\- OAuth2 Client ID retrieved from web server. 

Token`token`\- OAuth2 token retrieved from web server. 

## 

Parameters - Output Page

Clear Output`clear`\- Clears the output of the DAT. 

Clamp Output as Rows`clamp`\- When enabled, the output of the DAT is table instead of text. The rows will also be clamped to Maximum lines parameter value. This should be enabled when streaming is enabled too ensure that the output does not get too large. 

Maximum Lines`maxlines`\- The maximum number of rows when clamping is enabled. 

Callbacks DAT`callbacks`\- The Callbacks DAT. 

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

Operator Inputs
* Input 0:  -
  * Input 1:  -

## 

Info CHOP Channels

Extra Information for the Web Client DAT can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). 

### 

Specific Web Client DAT Info Channels
* download_progress -
* downloaded_size -
* total_size -
* connected -
* connection_error -
* communicating -

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


  
TouchDesigner Build: Latest\nwikieditorwikieditorwikieditor2021.100002020.20000before 2020.20000

DATs   
---  
[Art-Net ](<./Art-Net_DAT.md> "Art-Net DAT")• [Audio Devices ](<./Audio_Devices_DAT.md> "Audio Devices DAT")• [CHOP Execute ](<./CHOP_Execute_DAT.md> "CHOP Execute DAT")• [CHOP to ](<./CHOP_to_DAT.md> "CHOP to DAT")• [Clip ](<./Clip_DAT.md> "Clip DAT")• [Convert ](<./Convert_DAT.md> "Convert DAT")• [CPlusPlus ](<./CPlusPlus_DAT.md> "CPlusPlus DAT")• [DAT ](<./DAT.md> "DAT")• [ Execute ](<./DAT_Execute_DAT.md> "DAT Execute DAT")• [DAT Export ](<./DAT_Export.md> "DAT Export")• [Error ](<./Error_DAT.md> "Error DAT")• [EtherDream ](<./EtherDream_DAT.md> "EtherDream DAT")• [Evaluate ](<./Evaluate_DAT.md> "Evaluate DAT")• [Examine ](<./Examine_DAT.md> "Examine DAT")• [Execute ](<./Execute_DAT.md> "Execute DAT")• [FIFO ](<./FIFO_DAT.md> "FIFO DAT")• [File In ](<./File_In_DAT.md> "File In DAT")• [File Out ](<./File_Out_DAT.md> "File Out DAT")• [Folder ](<./Folder_DAT.md> "Folder DAT")• [In ](<./In_DAT.md> "In DAT")• [Indices ](<./Indices_DAT.md> "Indices DAT")• [Info ](<./Info_DAT.md> "Info DAT")• [Insert ](<./Insert_DAT.md> "Insert DAT")• [JSON ](<./JSON_DAT.md> "JSON DAT")• [Keyboard In ](<./Keyboard_In_DAT.md> "Keyboard In DAT")• [Lookup ](<./Lookup_DAT.md> "Lookup DAT")• [Media File Info ](<./Media_File_Info_DAT.md> "Media File Info DAT")• [Merge ](<./Merge_DAT.md> "Merge DAT")• [MIDI Event ](<./MIDI_Event_DAT.md> "MIDI Event DAT")• [MIDI In ](<./MIDI_In_DAT.md> "MIDI In DAT")• [Monitors ](<./Monitors_DAT.md> "Monitors DAT")• [MPCDI ](<./MPCDI_DAT.md> "MPCDI DAT")• [MQTT Client ](<./MQTT_Client_DAT.md> "MQTT Client DAT")• [Multi Touch In ](<./Multi_Touch_In_DAT.md> "Multi Touch In DAT")• [NDI ](<./NDI_DAT.md> "NDI DAT")• [Null ](<./Null_DAT.md> "Null DAT")• [OP Execute ](<./OP_Execute_DAT.md> "OP Execute DAT")• [OP Find ](<./OP_Find_DAT.md> "OP Find DAT")• [OSC In ](<./OSC_In_DAT.md> "OSC In DAT")• [OSC Out ](<./OSC_Out_DAT.md> "OSC Out DAT")• [Out ](<./Out_DAT.md> "Out DAT")• [Panel Execute ](<./Panel_Execute_DAT.md> "Panel Execute DAT")• [Parameter ](<./Parameter_DAT.md> "Parameter DAT")• [Parameter Execute ](<./Parameter_Execute_DAT.md> "Parameter Execute DAT")• [ParGroup Execute ](<./ParGroup_Execute_DAT.md> "ParGroup Execute DAT")• [Perform ](<./Perform_DAT.md> "Perform DAT")• [POP to ](<./POP_to_DAT.md> "POP to DAT")• [Render Pick ](<./Render_Pick_DAT.md> "Render Pick DAT")• [Reorder ](<./Reorder_DAT.md> "Reorder DAT")• [Script ](<./Script_DAT.md> "Script DAT")• [Select ](<./Select_DAT.md> "Select DAT")• [Serial ](<./Serial_DAT.md> "Serial DAT")• [Serial Devices ](<./Serial_Devices_DAT.md> "Serial Devices DAT")• [SocketIO ](<./SocketIO_DAT.md> "SocketIO DAT")• [SOP to ](<./SOP_to_DAT.md> "SOP to DAT")• [Sort ](<./Sort_DAT.md> "Sort DAT")• [Substitute ](<./Substitute_DAT.md> "Substitute DAT")• [Switch ](<./Switch_DAT.md> "Switch DAT")• [Table ](<./Table_DAT.md> "Table DAT")• [TCP/IP ](<./TCP/IP_DAT.md> "TCP/IP DAT")• [Text ](<./Text_DAT.md> "Text DAT")• [Touch In ](<./Touch_In_DAT.md> "Touch In DAT")• [Touch Out ](<./Touch_Out_DAT.md> "Touch Out DAT")• [Transpose ](<./Transpose_DAT.md> "Transpose DAT")• [TUIO In ](<./TUIO_In_DAT.md> "TUIO In DAT")• [UDP In ](<./UDP_In_DAT.md> "UDP In DAT")• [UDP Out ](<./UDP_Out_DAT.md> "UDP Out DAT")• [UDT In ](<./UDT_In_DAT.md> "UDT In DAT")• [UDT Out ](<./UDT_Out_DAT.md> "UDT Out DAT")• [Video Devices ](<./Video_Devices_DAT.md> "Video Devices DAT")• Web Client • [Web ](<./Web_DAT.md> "Web DAT")• [Web Server ](<./Web_Server_DAT.md> "Web Server DAT")• [WebRTC ](<./WebRTC_DAT.md> "WebRTC DAT")• [WebSocket ](<./WebSocket_DAT.md> "WebSocket DAT")• [XML ](<./XML_DAT.md> "XML DAT")
