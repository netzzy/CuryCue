# Video Streaming User Guide

This guide will cover the supported protocols and services that are now available to TouchDesigner users for audio video streaming over the Internet.   
  
#### Current Protocols in Official
* [RTMP](<./RTMP.md> "RTMP") \- A widely adopted protocol for streaming audio video to streaming services like YouTube and Twitch.
  * [RTSP](<./RTSP.md> "RTSP") \- An open source server and client protocol for sending and receiving audio video data over the internet.
  * [NDI](<./NDI.md> "NDI") \- A video over IP protocol that is extremely useful in a variety of networked video use cases.
  * [SRT](<./SRT.md> "SRT") \- (Secure Reliable Transport) upcoming in [Video Stream In TOP](<./Video_Stream_In_TOP.md> "Video Stream In TOP"), currently in Experimental builds.


See also [Broadcasting to Social Media from TouchDesigner](<https://derivative.ca/community-post/broadcasting-social-media-touchdesigner>) via virtual webcams. 

## Streaming Services using RTMP

### Twitch

URL: <https://www.twitch.tv/>

A service owned and operated by Amazon. It's probably the most popular live streaming system to date. 

**Services**
* Free access
  * Integrated chat
  * Stream recording and stream playback (for a limited number of days)
  * Premium (Paid) Access offers various enhancements to recording


**Advantages**
* Free with Ads / Premium without Ads
  * Easy to use
  * The best place to try this for the first time
  * Low latency (3-5 seconds)


**Disadvantages**
* Ads for free
  * Entrance way to content is very noisey with gamers playing games
  * Recording and archiving options for video is limited and always temporary

##### Connection and Setup Instructions
1. Sign up for a user account. Follow the instructions.
  2. Once a member find your streamkey located in "Account Settings" in the "Stream" section. They "Primary Stream key" is a permanent key that you can use over and over so it should be kept to yourself or others will be able to hijack your channel. Use the copy button to copy the string the keyboard and construct the string in the VideoStream out TOP parameter called Destination URL as follows...
  3. Pick an ingest server that is closest or recommended. <https://stream.twitch.tv/ingests/>


[code]
      {ingest server url} = rtmp://live.twitch.tv/app/
      {stream key} = live_1234567_sduhy3xJ1KJ34Eg6CjksdJLubFS7gtUY
      RTMP Destination URL = rtmp://live.twitch.tv/app/live_1234567_sduhy3xJ1KJ34Eg6CjksdJLubFS7gtUY
    
[/code]

##### Maximum Quality Settings
* Resolution: 1920x1080
  * Bitrate: 6000 kbps
  * Bitrate Mode: CBR
  * Framerate: 60
  * Keyframe Interval: 2 seconds
  * Profile: Main
  * B-frames: 2
* Maximum quality settings trade quality for size / bandwidth and are possibly less compatible with a wider audience. We encourage you to try all the settings to figure out what’s best for your use case.

### Youtube

URL: <https://youtube.com>

**Services**
* Video streaming
  * Video transcoding
  * Live video streaming
  * Live video recording


**Advantages**
* Possibly the biggest video platform in the world.
  * Most viewers already have a Youtube account.
  * Smart TVs come with Youtube installed - easy to play content on TVs or any other device.
  * Free archiving of all videos.
  * Immediate access to your videos.
  * Ability to monetize your content based on advertising revenue from playback.


**Disadvantages**
* Setup is more complex than Twitch

##### Connection and Setup Instructions
1. Sign up for a user account.
  2. Use google to search for YouTube live streaming
  3. Click the search link called ["YouTube Live | Learn How to Start Your Stream"](<https://www.youtube.com/howitworks/product-features/live/?gclid=CjwKCAjwp-X0BRAFEiwAheRui043jts8yY1IuON6umPLdiUiJ3IW8YRSqoXWRkX_k0a419VDPrKi3BoC7msQAvD_BwE&gclsrc=aw.ds#live-streaming-on-youtube>)
  4. Go to <https://youtube.com/live_dashboard>. You will end up at the YouTube Studio Dashboard.
  5. Locate the "Go Live" button which is an icon with a red dot in the middle. Click that.
  6. This will bring you to a new streaming user interface. It allows you to select a Webcam or Stream sender. Select "Stream" on the left control panel.
  7. From here follow the setup dialog instructions to setup your stream. Construct the string for the VideoStreamOut TOP by concatenating the Stream URL with a "slash" ("/") as follows...


[code]
      {stream url} = rtmp://x.rtmp.youtube.com/live2
      {stream key} = asdf-56wq-6yut-9ast
      RTMP Destination URL = rtmp://x.rtmp.youtube.com/live2/asdf-56wq-6yut-9ast
    
[/code]
* *       * Important Note: Once you have successfully connected to the Studio streaming RTMP server, the connection status below the preview monitor will go from "no data" to "Excellent (or other) Connection" but it may not play the preview until you reload the page on the browser.

##### Maximum Quality Settings

[https://support.google.com/youtube/answer/2853702?hl=en&ref_topic=9257892](<https://support.google.com/youtube/answer/2853702?hl=en&ref_topic=9257892>)

(These requirement specifications have yet to be fully realized. 4K is not working yet on our side) 

### Mux

URL: <https://mux.com/>

A passionate team of video experts who have done a very good job taking some of the complexity out of streaming for business use cases. They provide a robust platform for high quality streaming geared toward application developers. 

**Services**
* Video transcoding
  * Video storage and playback backend
  * Live streaming and live stream recording
  * Data metrics
  * Application development API


**Advantages**
* Very good human support
  * Easy to use - good backend user interface - minimal
  * Clean API for supporting application development
  * They have their own network that is tuned for quality of playback
  * Supports XXXX Kbps
  * Make your own streaming application and avoid the noise and chaos to Twitch or Mixer


**Disadvantages**
* Higher latency than Twitch and Mixer - can be up to 30 seconds
  * Might be expensive. Call them with you use case or look here to start. <https://mux.com/pricing>
  * Only support RTMP and HLS currently.
  * Much more complex than Twitch or Mixer - (It's designed for professional developers)
  * Their business model seems to be geared towards ingesting and transcoding video and not live streams.
  * Their maximum frame rate is 30 and maximum bitrate is 5000.

##### Connection and Setup Instructions
1. Sign up for a user account. Follow the instructions.
  2. Once in user account use the Settings (Gear Icon) menu to locate documentation.
  3. <https://docs.mux.com/docs/live-streaming>


[code]
      {ingest server url} = rtmp://global-live.mux.com:5222/app
      {stream key} = 123412341234-JKHASDF98asdf9789fAoad
      RTMP Destination URL = rtmp://global-live.mux.com:5222/app/123412341234-JKHASDF98asdf9789fAoad
    
[/code]

##### Maximum Quality Settings
* Resolution: 1920x1080
  * Bitrate: 7000 kbps
  * Bitrate Mode: CBR
  * Framerate: 30
  * Keyframe Interval: 0 seconds
  * Profile: Main
  * Preset:
  * B-frames: 2

### Wowza

URL: <https://wowza.com/>

Pay to stream service charges you based on your bandwidth usage. <http://cloud.wowza.com> provides an easy to use system for RTMP ingest and HLS broadcasting. As well they offer a streaming engine that can be installed onto a cloud service like Microsoft Azure to manage an entire customizable streaming service. Its very technical to setup. 

**Services**
* Video transcoding
  * Live streaming and live stream recording
  * Data metrics
  * Application development API


**Advantages**
* Very good human support
  * Wowza cloud services are fairly easy to use and are very configurable.
  * Clean API for supporting application development
  * Their network provides customization of settings for higher bit rates
  * Make your own streaming application and avoid the noise and chaos to Twitch or Mixer
  * 30 day trial for testing cloud services - <https://www.wowza.com/wowza-streaming-cloud-free-trial>
  * 6 month trial for running Wowza engine - <https://www.wowza.com/wowza-streaming-engine-free-trial>
  * High resolutions and high bitrates are available


**Disadvantages**
* You must have a membership to use it
  * Pricing structure isnt very clear as it is pay to play
  * Cloud only supports RTMP
  * Much more complex than Twitch or Mixer - (It's designed for professional developers)
  * Possibly a good business model for TouchDesigner users who want to stream video content to a fixed number of high quality clients.

##### Connection and Setup Instructions
1. Sign up for a demo user account. Follow the instructions.


See also [Video Stream Out TOP](<./Video_Stream_Out_TOP.md> "Video Stream Out TOP"), [Video Stream In TOP](<./Video_Stream_In_TOP.md> "Video Stream In TOP") and [RTMP](<./RTMP.md> "RTMP").
