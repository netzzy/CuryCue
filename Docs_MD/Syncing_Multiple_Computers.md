# Syncing Multiple Computers

## Overview

It is always simpler to keep projects on a single computer with a single GPU. However if a situation arises where work must be split up between more GPUs or computers, it possible that some level of synchronization between the systems will be necessary. What level of sync is necessary is highly situation dependent on the display setup and content. You may need very tight sync at the hardware level or in other cases basic sync at the software level will be sufficient. 

For projects with very slow moving content, or displays that are far apart from each other, a very basic sync may be fine and perfect sync/hardware sync would be overkill. For other projects with fast moving content and displays that are very close to each other, you may require perfect sync to make it look good. 

See also [Sync](<./Sync.md> "Sync"). 

## Source of Sync Errors

From the start of rendering a frame to when it finally gets displayed it to a monitor there are various stages where sync errors can be introduced. 

### Content Generation

For multiple computers to be outputting synced images, they must first be generating the same images for the same frame. If you are playing a video this means ensuring they are playing the same frame of video. If you are rendering a scene this means ensuring all the objects and cameras are using the same transforms and geometry on that frame. These problems are solved with software sync. Some algorithms for generating content do not lend themselves well to sync, such as the [Particle SOP](<./Particle_SOP.md> "Particle SOP"), or generating images using a network with a [Feedback TOP](<./Feedback_TOP.md> "Feedback TOP"). This is because these methods use information from the previous frame to calculate the current frame. If at any time one of the computers drops a frame its content may start to diverge from the other machine's content. Even a single dropped frame can result in drastically different results after a few seconds of more rendering. 

Ideally the project is being build should be able to guarantee that if it's given a certain command or a certain set of control channels, it will always output the same thing. This is called a 'deterministic' project. This is often achieved by having everything driving by a single frame index, or a set of channels that controls the state of everything in the project. 

Once you have a project that is 'deterministic', the next step is to ensure the computers get the commands/control channels at the same time, or as close to the same time as possible. This is done using Software Sync. Simple software sync can often have a sync error of between 1-3 frames. Perfect software sync should have 0 frame sync errors for content generation. There may still be a 1 frame sync error caused by the displays though, described in the next section. 

( Detail: The Sync Out CHOP is the server, and the In CHOP are the clients. The Out node waits for messages from the In nodes telling it they have finished a frame, before send out a new frame worth of data. As noted, Particle systems are tricky since if every client is calculating their own data, just diverging their calculations for one frame will results in drastically different results. So if you need perfection you should run your server and clients with realtime off, so it never skips a frame (which may affect the visual smoothness), and make sure all the clients are always using the exact same input when doing their calculations. Often people want to have one of their render nodes be the server, which is OK but you need to ensure the work that generates your time.absframe ($F) etc. is separate from all the nodes that do your rendering. This is doable using Component Time. Put the Sync Out CHOP in one COMP with it’s own timeline, and use a Sync In CHOP in the same file with that’s reading values from that Sync Out CHOP. It should be in another COMP with it’s own time again, and it should use the values from the Sync In CHOP to do it’s rendering, not anything direct coming from the Sync Out CHOP’s network. All the other clients will only have a Sync In CHOP active. ) 

### Displaying Content

Even if the computers are generating content in perfect sync, displaying the images may introduce up to 1 frame of sync errors. This is because the refresh interval of the displays on different machines will not be in phase. If you are running at 60fps, then the time when each display starts doing it's refresh may be offset by up to 16.6ms from each other. This is solved with Hardware Sync/Hardware Frame Lock. 

## Types of Sync

### Software Sync

Software sync ensures that all the processes are generating the same content at the same time. 

[Pro](<./TouchDesigner_Pro.md> "TouchDesigner Pro") users can get perfect software sync by using the [Sync In CHOP](<./Sync_In_CHOP.md> "Sync In CHOP"), [Sync Out CHOPs](<./Sync_Out_CHOP.md> "Sync Out CHOP"). 

[Commercial](<./TouchDesigner_Commercial.md> "TouchDesigner Commercial") and Non-Commercial users will not be able to get guaranteed perfect software sync, but can get sync that is usually within 1-3 frames by using network nodes such as the [OSC In CHOP](<./OSC_In_CHOP.md> "OSC In CHOP")/[OSC Out CHOP](<./OSC_Out_CHOP.md> "OSC Out CHOP") or [OSC In DAT](<./OSC_In_DAT.md> "OSC In DAT")/[OSC Out DAT](<./OSC_Out_DAT.md> "OSC Out DAT"), and make sure to use Multicast as the network protocol. For the OSC CHOPs, but sure to turn off queuing to ensure there is no latency added to your data by the OSC In CHOP. The vast majority of projects use this type of sync, because the content and/or display setup doesn't display 1-3 frame sync errors. If displays are far apart, or content moves slowly, perfect sync often isn't needed. 

### Hardware Sync

Hardware sync is used to ensure that all displays update their content at the same time, and ensure that one doesn't update it's content without the others being ready to update their content. This may be necessary for arrays of displays (such as a Christie Microtile Wall) with fast moving content. Without hardware sync displays may refresh at different times, adding up to 1 frame of sync error to the content. To achieve hardware sync you will need Quadro GPUs with Quadro Sync cards. For more information on hardware sync refer to the [Hardware Frame Lock](<./Hardware_Frame_Lock.md> "Hardware Frame Lock") article.
