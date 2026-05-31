# Hap

The Hap, Hap Q and Hap R codecs are supported in the [Movie File In TOP](<./Movie_File_In_TOP.md> "Movie File In TOP"), and the [Movie File Out TOP](<./Movie_File_Out_TOP.md> "Movie File Out TOP") encodes them as well. Hap and Hap Q are also used in the video-over-IP operators [Touch Out TOP](<./Touch_Out_TOP.md> "Touch Out TOP") and [Touch In TOP](<./Touch_In_TOP.md> "Touch In TOP").   
  
Hap is a video codec that performs decompression using a computer's graphics hardware, substantially reducing the CPU usage necessary to play video. It allows for playback of higher resolution and/or frame rate videos than any other codec we know of. It also allows for playback many more streams of lower resolution video than other codecs, assuming you have the drive speed for it. 

There are many different Hap codecs: 
* Hap - has the lowest data-rate and low image quality. 8-bit color depth.
  * Hap Alpha - has identical image quality to Hap, and supports an Alpha channel. The size of a Hap Alpha file will be twice the size of a Hap file. 8-bit color depth.
  * Hap Q - has much improved image quality, but no alpha channel. The size of a Hap Q file will be approximately twice the size of a Hap file. 8-bit color depth.
  * Hap Q Alpha - has identical image quality as Hap Q, but also includes an Alpha channel. 8-bit color depth.
  * Hap R - has higher image quality than both Hap and Hap Q, and can include alpha. 8-bit color depth. Uses [BC7 Texture Compression](<https://learn.microsoft.com/en-us/windows/win32/direct3d11/bc7-format>). ***** WARNING - GPU Driver Timeout on long GPU activities ***** Encoding this format at high-resolution may be a slow GPU-intensive operation. Consequently it will usually take longer than the default 2 seconds per frame that Windows gives the GPU driver to complete an operation. If you see a message saying that Windows has reset the GPU driver, this is the issue you are running into. To fix the issue, create this registry value:`HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\GraphicsDrivers\TdrDelay`The value should be of type`REG_DWORD`. The value is the number of seconds an operation can take before the OS resets the GPU driver. Set it to something larger, like 20-40 (seconds), depending on the resolution you intend to encode. You must reboot your machine for this setting to take effect. If you still get driver resets, make it even larger. 
* Hap HDR - has 16-bit floating point data. Intended to be used for HDR content, since the values can go outside the 0-1 range. It is **not** suitable for encoding raw data such as point cloud positions. Uses on [BC6 Texture Compression](<https://learn.microsoft.com/en-us/windows/win32/direct3d11/bc6h-format>).


Hap Q image quality is high and is a great choice for projects playing very high resolution video. Since the files have a high data rate the main bottleneck you will often hit is SSD read speed. 

## Compression Ratio and Data Rates

The Hap codec is a two stage compression. The first stage is the texture compression that is a constant compression. The second stage is a CPU compression that is variable depending on the content. On noisy/busy content the CPU stage may offer no compression at all. The first stage is a lossy compression that can introduce artifacts or banding. The second stage is lossless and will not introduce any extra image artifacts. 

Data rates of Hap video will almost never be worse than these ratios, which are the constant texture compression ratios for each format. 
* Hap = 0.5 bytes per pixel/4-bits per pixel. 6:1 compression compared to uncompressed RGB video. Also know as Hap1.
  * Hap Alpha = 1 byte per pixel/8-bits per pixel. 4:1 compression compared to uncompressed RGBA video. Also known as Hap5.
  * Hap Q = 1 byte per pixel/8-bits per pixel. 3:1 compression compared to uncompressed RGB video. Also known as HapY.
  * Hap Q Alpha 1.5 bytes per pixel/12-bits per pixel. 2.6:1 compression compared to uncompressed RGBA video. Also known as HapM.


So for a 4096x2160@60hz video, that is 530,841,600 pixels per second. The worst case data rate will be: 
* Hap = 265,420,800 Bytes/second
  * Hap Alpha = 530,841,600 Bytes/second
  * Hap Q = 530,841,600 Bytes/second
  * Hap Q Alpha = 796,262,400 Bytes/second.


After the texture compression, the resulting frames will be compressed using a fast, non-aggresive compressor called Snappy, which often gives 2:1 compression. This stage of compression is lossless, it does not introduce any artifacts. 

TouchDesigner supports the decoding and encoding of all forms of the codec. 

Its specification and sample code can be found at the github location: [Hap video codec](<http://github.com/Vidvox/hap>)

## External Tools

[VLC Media Player](<https://www.videolan.org/vlc/index.html>) can play Hap and Hap Q files, but not Hap Q Alpha or Hap R(as of VLC 3.0.4). 

[Hap Exporter for Adobe CC 2018](<https://github.com/disguise-one/hap-encoder-adobe-cc>) is a plugin to allow for Hap encoding, including using chunks. 

[Jokyo Hap Encoder](<https://jokyohapencoder.com/>) a high quality commercial Hap encoder plugin for various Adobe tools. 

[The QuickTime plugin](<https://github.com/vidvox/hap-qt-codec/releases>) is not required for HAP support in TouchDesigner, but can be useful for testing on macOS. 

## Working with High Resolution or High FPS Video

Hap Q is the best codec choice when ultra high resolution or FPS video is required. However the videos must be encoded properly to allow for multi-threaded CPU decoding. This is called 'Chunked' encoding in the Hap standard. The [Movie File Out TOP](<./Movie_File_Out_TOP.md> "Movie File Out TOP") always encodes using chunked encoding.Chunked encoding can also be done using the latest version of FFmpeg. This can be done using the -chunks option. For example 
[code] 
     ffmpeg -i source.mov -c:v hap -format hap_q -chunks 12 dest.mov
     
    
[/code]

Each chunk can utilize a different CPU to be decoded, so chunks equal or greater than the number of CPUs cores on the system (not including hyper-threading cores), will be best. Having more chunks than CPUs core should not affect performance, but ideally the number of chunks is kept within a reasonable amount. When TouchDesigner encodes it uses 12 chunks. 

**Note** : The QuickTime plugin does not encode using chunked encoding. 

### Extreme Cases

For extreme resolution cases, it's possible having any CPU compression enabled will be too heavy. This can turned off in TouchDesigner on 'Advanced' page of the [Movie File Out TOP](<./Movie_File_Out_TOP.md> "Movie File Out TOP"), under the 'Hap Secondary Compression' option. This will write the frames only using the constant ratio texture compression. This avoids any CPU decompression, and also can result in less memory bandwidth usage when 'High Performance Read' is enabled on the [Movie File In TOP](<./Movie_File_In_TOP.md> "Movie File In TOP").
