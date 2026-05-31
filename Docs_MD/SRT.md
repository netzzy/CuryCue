# SRT

[SRT](<https://www.srtalliance.org/>) (Secure Reliable Transport) is an open source video streaming protocol that optimizes video transport over unpredictable networks by adapting to real-time network conditions and minimizing packet loss. It also supports end-to-end AES encryption so streams are better protected at all points. SRT protocol is used heavily in broadcast news, live sports and live events world. Due to its ease of transmition, support for codecs like H264 and H265 it is well suited for passing streams from field sources to broadcast stations and transcoding endpoints for real-time broadcast. As well SRT functions well for peer to peer scenerios. 

There are no fees to incorporate the technology into any device or service so it has proven itself superior to RTMP because RTMP is not open source and can not be used to download without licensing. SRT has also enjoyed better traction than RTSP for internet based applications. 

The videostreamoutTOP is used to transmit the video while the videostreaminTOP is used to receive the video. 

SRT is 2020.40000 series of builds in the [Video Stream In TOP](<./Video_Stream_In_TOP.md> "Video Stream In TOP") and [Video Stream Out TOP](<./Video_Stream_Out_TOP.md> "Video Stream Out TOP") nodes. 

See also [Video Streaming User Guide](<./Video_Streaming_User_Guide.md> "Video Streaming User Guide"), [Video Stream Out TOP](<./Video_Stream_Out_TOP.md> "Video Stream Out TOP") and [Video Stream In TOP](<./Video_Stream_In_TOP.md> "Video Stream In TOP"). 

For other video-over-IP technology see [RTMP](<./RTMP.md> "RTMP"), [NDI In TOP](<./NDI_In_TOP.md> "NDI In TOP"), [NDI Out TOP](<./NDI_Out_TOP.md> "NDI Out TOP") and [NDI DAT](<./NDI_DAT.md> "NDI DAT"). 

## Transmitting SRT - Listener and Caller

SRT uses a listener and caller model which determines the mode of transmition for the transmition start and end points. The video source and destination can be either a listener or caller. The listener end can be thought of as an available IP location with an open port. The caller side is a client that will require the address of the listener and it will try to connect when initiated. 

For example if the video source is a [Video Stream Out TOP](<./Video_Stream_Out_TOP.md> "Video Stream Out TOP"), and the desired mode for the video source to be a listener, the Desination URL will be something like:`srt://192.168.1.3:5000?mode=listener`To connect a [Video Stream In TOP](<./Video_Stream_In_TOP.md> "Video Stream In TOP") to the listener [Video Stream Out TOP](<./Video_Stream_Out_TOP.md> "Video Stream Out TOP") the URL looks like this:`srt://192.168.1.3:5000?mode=caller`The listener, caller role of the video stream in and out TOPs can be reversed simply by flipping the mode arguements "listener" and "caller" of the URLs. 

## Peer to Peer Streaming Over the Internet

Once you are able to get SRT streaming on a local network using the previous section example, to do the same over the internet requires some configuration on your intenert firewall. 

Use your Internet router configuration tools to locate settings for NAT/Gaming or Port Forwarding. You will need to setup a range of ports that forwards calls from the internet to the "host" or "device" on the protected network. The device or host will generally be assigned using its local IP address or its MAC address. 

This host, on the local network can be setup using [Video Stream Out TOP](<./Video_Stream_Out_TOP.md> "Video Stream Out TOP") using listener mode for SRT. In this scenerio you can use a broadcast address to make it easier to find for the router:`srt://0.0.0.0:5000?mode=listener`Next you can test this connection in the same instance of TouchDesigner by using a [Video Stream In TOP](<./Video_Stream_In_TOP.md> "Video Stream In TOP") configured with an SRT caller setup. However you will first need to determine the IP address of router. This can by done by typing "Whats my IP address" into google search. The serach will return an IP4 address in the format [XXX.XXX.XXX.XXX]. Use this IP address in the URL like this:`srt://[XXX.XXX.XXX.XXX]:5000?mode=caller`## Using SRT on Other Devices

The following apps have been succesfully tested with TouchDesigner's SRT implementation using an audio video stream. 

### Apple IPhone: Haivision Play Pro

<https://apps.apple.com/us/app/haivision-play-pro/id1482925169>

This is a very useful app for testing your streams from TouchDesigner over the Internet. To stream to the app from a [Video Stream Out TOP](<./Video_Stream_Out_TOP.md> "Video Stream Out TOP") use the follow URL:`srt://[XXX.XXX.XXX.XXX]:5000?mode=caller`On the app side fill out the settings as follows in the "Play and SRT Stream" section.`Mode = "Caller"``Address = "[XXX.XXX.XXX.XXX]"``Caller's Port = "5000"``Encryption = "Off"``StreamID = (Nothing - leave it blank)``Latency = 100`### SRT Relay Server

We have successfully tested this relay server. 

<https://hub.docker.com/r/ravenium/srt-live-server>
