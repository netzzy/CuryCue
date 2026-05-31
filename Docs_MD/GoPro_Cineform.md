# GoPro Cineform

[GoPro Cineform](<http://www.cineform.com>) is a video codec that is high quality, fast to decode and produces reasonable file sizes. The Cineform codec is used in film production, but we're finding it's a great alternative when preservation of image quality is the greatest requirement, while decoding in realtime is an imperative. Decode time is constant regardless of the complexity of the scene, which isn't true for other codec such as H.264, where decode times can climb above 100ms in a scene with a lot of motion. 

TouchDesigner is able to decode 4K by 4K Cineform codec video at 30 frames per second (or better) using fast 12-core systems. 

To create Cineform files you can use the various tools that GoPro offers. The Movie File Out TOP can also encode Cineform. Starting with build 099 2018.24840 encoding will work without any external work needed to make it functional. On older builds, to enable the cineform encoder please follow [these instructions.](<https://gopro.com/support/articles/unable-to-encode-into-the-gopro-cineform-coded-with-3rd-party-applications>)

## 4K Playback

To achieve 4K playback you need to split your files into 4 2Kx2K files (top left, bottom left etc.) and make sure you encoding using YUV colorspace, not RGBA. The system should have at least 8 cores but we've only successfully tested 4K playback using 12 core systems.
