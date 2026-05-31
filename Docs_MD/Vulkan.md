# Vulkan

TouchDesigner's graphics API is now [Vulkan](<https://www.vulkan.org/>). [macOS](<./MacOS.md> "MacOS") uses [MoltenVK](<https://github.com/KhronosGroup/MoltenVK/>), a portability project allowing Vulkan to be used on top of Apple's Metal framework. 

## Why Vulkan?

TouchDesigner has moved to Vulkan both as way to ensure it is future-proof, and as a way to reduce the current driver overhead that OpenGL has. By moving to Vulkan you should see many TOP operations have a lower CPU cook time, due to lower driver overhead. Additionally, many operations such as video I/O can be further threaded to improve performance. The ability to thread prepares us for the future when node cooking can be done in a more threaded manner as well. 

On the macOS side, targeting Vulkan means we can use MoltenVK which means our actual graphics calls are done by Metal. This ensures we are current with the API that Apple is focusing it's resources on. The one drawback is that Geometry Shaders are not supported on Metal, so geometry shaders are completely gone on macOS on all GPUs now. By using Metal underneath we can finally make use of Compute Shaders safely on all platforms, so we can start using those more for operations within TouchDesigner. This enables things such as NotchLC encode/decode on macOS out of the box. 

There are many cross-vendor extensions coming to Vulkan, such as Vulkan Video, which will allow us to harness the video encode/decode chips of all GPUs with a single API. This would remove the Nvidia-Only hardware encode/decode limitation we currently have. This work is not done yet though. 

Other exciting features we hope to bring in the future is the ability to drive GPU outputs directly without them being part of the desktop. This would avoid many issues caused by the desktop compositor and mixing EDIDs between your performance outputs and your UI output. 

Vulkan also has better support for HDR color space outputs, which is another feature we can look forward to in the future.
