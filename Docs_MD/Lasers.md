# Lasers

There are 5 pathways from TouchDesigner to lasers. For all cases except Pangolin, a CHOP, POP or SOP defining the shapes is sent to the [Laser CHOP](<./Laser_CHOP.md> "Laser CHOP") which processes the data into streams of samples, and then passes the samples to the [Laser Device CHOP](<./Laser_Device_CHOP.md> "Laser Device CHOP"). 

## EtherDream

EtherDream DAC (digital-to-analog converter) hardware is interfaced to TouchDesigner on a Ethernet port, and connects to a laser using an ILDA cable. 

See the [Laser Device CHOP](<./Laser_Device_CHOP.md> "Laser Device CHOP"), and to poll the attached EtherDream lasers, see [EtherDream DAT](<./EtherDream_DAT.md> "EtherDream DAT"). 

## Helios

Helios DAC (digital-to-analog converter) hardware is interfaced to TouchDesigner via a serial port, and connects to a laser using an ILDA cable. Helios also supports sending to all IDN devices, including the Helios OpenIDN adapter, which communicate over Ethernet. 

See the [Laser Device CHOP](<./Laser_Device_CHOP.md> "Laser Device CHOP"). 

## ShowNET

ShowNET hardware is interfaced to TouchDesigner on a Ethernet port, and connects to a laser device directly with an onboard DAC (digital-to-analog converter). 

See the [Laser Device CHOP](<./Laser_Device_CHOP.md> "Laser Device CHOP"). 

## LaserAnimation Sollinger and AVB Protocol

Using a [LaserAnimation Sollinger AVB](<https://en.wikipedia.org/wiki/Audio_Video_Bridging>)-capable laser projector, the [Laser CHOP](<./Laser_CHOP.md> "Laser CHOP") receives and processes the POP/CHOP/SOP data and outputs to an [Audio Device Out CHOP](<./Audio_Device_Out_CHOP.md> "Audio Device Out CHOP") driving a low-latency AVB-ready audio protocol device. AVB output devices include products from [**MOTU**](<https://motu.com/en-us/products/audio-products/pro-audio-interfaces/>), [**RME**](<https://rme-audio.de/digiface-avb.html>), [**USB2AVB** by LaserAnimation Sollinger](<https://laseranimation.com/en/product/usb2avb/>) or built-in to [**Apple macOS**](<https://support.apple.com/en-ca/guide/audio-midi-setup/amsavb001/mac>). 

In addition, [LaserAnimation Sollinger's AVB2ILDA device](<https://laseranimation.com/en/products/avb-devices>) connects to ILDA lasers and gives access to features for the professional sector including 24-bit resolution on the X/Y signal and all color channels. Additionally the AVB2ILDA device includes software for electronic masking, making it possible to limit the laser output for certain areas (for example to protect scanning areas such as auditoriums or sectors with optical equipment). Also packaged is a color correction tool that includes individual control of the color delay for 3 colors as well as a Digital Geometric Correction to allow for projection on for example uneven surfaces. 

## Pangolin Beyond

A POP, CHOP or SOP defining the shapes is sent directly to the [Pangolin CHOP](<./Pangolin_CHOP.md> "Pangolin CHOP") which routes the data through the Pangolin [Beyond](<https://pangolin.com/collections/beyond-software>) software system to the laser(s). 

Pangolin Beyond is designed to manages safety masking and shutoff, and can output one signal across multiple lasers (zones).
