# RTMP

RTMP is a protocol for transporting an audio/video stream over the Internet. The standard RTMP only supports H.264 encoded content. A newer standard called Enhanced RTMP supports other codecs such as H.265 and AV1. Typically the stream is sent from an encoding source to an ingest server for transcoding and broadcast to client player devices like phones, tablets, smart TVs or computers. Follow this link for a wikipedia article on [Real-Time Messaging Protocol](<https://en.wikipedia.org/wiki/Real-Time_Messaging_Protocol>). RTMP is the most widely adopted protocol for streaming audio and video to streaming services like Facebook, Twitch and YouTube. 

See also [Video Streaming User Guide](<./Video_Streaming_User_Guide.md> "Video Streaming User Guide"), [Video Stream Out TOP](<./Video_Stream_Out_TOP.md> "Video Stream Out TOP") and [Video Stream In TOP](<./Video_Stream_In_TOP.md> "Video Stream In TOP"). 

For other video-over-IP technology see [NDI In TOP](<./NDI_In_TOP.md> "NDI In TOP"), [NDI Out TOP](<./NDI_Out_TOP.md> "NDI Out TOP") and [NDI DAT](<./NDI_DAT.md> "NDI DAT"), [SRT](<./SRT.md> "SRT"), [Touch In TOP](<./Touch_In_TOP.md> "Touch In TOP"), [Touch Out TOP](<./Touch_Out_TOP.md> "Touch Out TOP"). 

## Server Stream Ingest

The [Video Stream Out TOP](<./Video_Stream_Out_TOP.md> "Video Stream Out TOP") supports operating as an RTMP Sender. In this mode an RTMP Destination URL is provided to connect to an RTMP ingest server on a specified port using a specified stream name. It will be in the form:`rtmp://<ipaddress>:<port>/<streamName>`e.g.`rtmp://192.168.0.1:554/tdvidstream`### Encoding Options

Streaming services like Twitch and Youtube will have similar optimal settings for the [Video Stream Out TOP](<./Video_Stream_Out_TOP.md> "Video Stream Out TOP"). A search term like "twitch optimal streaming settings" will usually do the trick to get an up-to-date answer. Reference the [Video Streaming User Guide](<./Video_Streaming_User_Guide.md> "Video Streaming User Guide") for some general comparisons. 

## Client Stream Playback

Once an RTMP stream has been ingested by an RTMP server, the stream may be transcoded into a package of multiple resolutions to address a range of network bandwidths and then provided to a streaming end point where the stream is made available to client requests for playback. Client requests are often HTTP based like HLS for Apple and MPEG-DASH for Android. 

TouchDesigner will eventually support a range of HTTP based protocols to receive the streams as well. See the [Video Stream In TOP](<./Video_Stream_In_TOP.md> "Video Stream In TOP") for the stream types it currently supports. 

### HLS Playback Streams

HLS is a protocol developed by Apple. It has become an industry standard protocol for playing back audio video streams on the client side. If you are streaming on any Apple platform you are likely streaming via the HLS protocol and the video stream is playing back in an HLS video player. If you are streaming using an Android operating system you might be using HLS but you may just as likley be using MPEG-DASH. 

Depending on the RTMP server service provider, a URL will be provided that may be played in any compatible HLS player. An HLS URL will usually end with the extension:`m3u8`. 

e.g.`<https://stream.mux.com/a24aDSqw45425345nF1A1oZmrd7ABW51.m3u8>`<< This link does not work. 

An HLS stream can be quickly tested in an internet based player like this. 

<https://players.akamai.com/players/hlsjs>

## Latency

The round trip latency for an RTMP stream that leaves a [Video Stream Out TOP](<./Video_Stream_Out_TOP.md> "Video Stream Out TOP") and then returns for example via the HLS protocol using the [Video Stream In TOP](<./Video_Stream_In_TOP.md> "Video Stream In TOP") will vary greatly depending on the service used and how that service is located. Services like Twitch have tuned their servers for low latency communicated that ranges between 1 to 5 seconds on standard high bandwidth Internet connections in North America. Other services like Mux.com have tuned their servers and networks for latency as long as 30 seconds in favor of other factors like playback quality.
