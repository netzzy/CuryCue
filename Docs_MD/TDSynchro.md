# TDSynchro

This documentation covers the usage of the TDSynchro toolkit for synchronizing streams of video travelling over SDI and NDI networks. TDSynchro's primary use case is for situations where a large canvas of continuous video is subdivided into many streams for a seamless display over a group of mapping computers. 

## Overview

This system consists of a single server application and many clients. One computer acts as a video content server, reading video files from disk and or rendering real-time content into a large high resolution canvas. The client computers are mapping computers that receive a piece of the rendered canvas for mapping and projecting to specific projectors or other display processors. These clients are synchronized to display the same frame index such that the server canvas can be reconstructed and displayed as a continuous whole image. 

#### On the Server

The Server computer renders the entire canvas which can be any resolution. The canvas is then cropped into smaller pieces for distribution to multiple synchroVideoOut components. The resolution of the cropped pieces is generally driven by the method with which the video streams are transmitted. For example, if the stream is output over an SDI card, the canvas will be cropped relative to each SDI port resolution. The synchroVideOut component wraps the [Video Device Out TOP](<./Video_Device_Out_TOP.md> "Video Device Out TOP") and manages passing along the specified frame index with the video stream. 

The way the canvas is constructed, composited and subsequently cropped into pieces is up to you. Then each cropped piece is passed into a synchroVideoOut component, which quite simply manages passing along a stream and frame index via SDI or NDI or both. 

#### On the Client

Each client TouchDesigner environment uses a single [Palette:synchroClient](<./Palette-synchroClient.md> "Palette:synchroClient") component to receive a frame index from the [Palette:synchroServer](</Palette:synchroServer> "Palette:synchroServer") a section of canvas as a video stream. It caches each video frame and uses the global sync frame index to output the correct stream frame. 

## TDSynchro Server Side Components

[Palette:synchroFrameOut](<./Palette-synchroFrameOut.md> "Palette:synchroFrameOut")

[Palette:synchroVideoOut](<./Palette-synchroVideoOut.md> "Palette:synchroVideoOut")

## TDSynchro Client Side Components

[Palette:synchroFrameIn](<./Palette-synchroFrameIn.md> "Palette:synchroFrameIn")

[Palette:synchroNDIIn](<./Palette-synchroNDIIn.md> "Palette:synchroNDIIn")

[Palette:synchroSDIIn](<./Palette-synchroSDIIn.md> "Palette:synchroSDIIn")

[Palette:synchroCache](<./Palette-synchroCache.md> "Palette:synchroCache")
