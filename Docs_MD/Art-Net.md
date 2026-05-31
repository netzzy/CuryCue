# Art-Net

Art-Net is an implementation of DMX512-A protocol over UDP, in which packets containing lighting settings are transmitted over IP packets, typically on a private local area network such as Ethernet. Art-Net is basically [DMX](<./DMX.md> "DMX") over Ethernet (DOE) and was developed by Artistic Licence.   
  
Art-Net supports up to 32,768 universes over one piece of CAT-5 cable compared to one universe over a DMX cable. 

It is accessed using the [DMX In CHOP](<./DMX_In_CHOP.md> "DMX In CHOP"), the [DMX Out CHOP](<./DMX_Out_CHOP.md> "DMX Out CHOP") and the [Art-Net DAT](<./Art-Net_DAT.md> "Art-Net DAT"). 

USITT DMX512 is well known in the entertainment industry because it is the industry standard for controlling dimmers and automated lighting fixtures (moving lights). The electrical standard of DMX512 is RS485 which is as superset of RS422 which almost the same as RS232, well known as serial port on a PC. Ethernet is the electrical standard that transports data based on TCP/IPt. Art-Net is based on TCP/IP and uses UDP Packets. 

The protocol that is used is published on the Artistic Licence website and is available to anyone to use. Major vendors such as ADB, MA Lighting, High End, Entec, Avolites, Martin Professional, ChamSys and others are now using this protocol. More an more fixtures are now appearing with RJ45 connectors for use with Art-Net. Companies like Enttec and others are supplying DOE interfaces and even some free lighting control programs such as FreeStyler support Art-Net. 

Art-Net also appears as ArtNet.
