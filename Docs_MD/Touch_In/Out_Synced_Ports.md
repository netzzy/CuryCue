# Touch In/Out Synced Ports

## Overview

The concept of Synced Ports is unique to the [Touch In CHOP](<../Touch_In_CHOP.md> "Touch In CHOP") and [Touch Out CHOPs](<../Touch_Out_CHOP.md> "Touch Out CHOP"). It is not related to the [Sync In CHOP](<../Sync_In_CHOP.md> "Sync In CHOP")/[Sync Out CHOP](<../Sync_Out_CHOP.md> "Sync Out CHOP"). Usually each Touch In/Out node will create it's own network connection and send/receive information arbitrarily sometime inside of the frame time. In particular the sending will occur when the node cooks, which can happen at any time across the frame. When you have multiple of these nodes send/receiving, that means some nodes in another process may get data from earlier/later than other nodes. 

Synced Ports instead only uses a a single real network port, and all of the nodes with this feature enabled will send their data to a common manager for that port, and the entire frames data will only be sent out as a single block of data at the end of the frame, once every node has had a chance to create data. In this case the 'port' parameter on the nodes isn't a real network port, but rather just a tag to separate their data from other data that is sent across the singular real port. 

Similarly on the receiver, the entire frame's data will be received at once, and all the nodes that are reading from it will grab their data based on their 'port' setting. Multiple nodes can not read from the same 'port' within the same process. 

## Settings

Each process has a single configuration for the sender settings and the receiver settings that are used for all nodes that are using 'Synced Ports'. The settings are controlled via environment variables. 

### Sender`SYNCED_PORTS_OUT_PORT`\- The port number to send data out of. Defaults to 10500 if not set.  

### Receiver`SYNCED_PORTS_IN_ADDRESS`\- The address of the sender that the receiver will connect to. This is the IP/hostname of the computer that contains the Touch Out CHOPs. Defaults to 'localhost'.`SYNCED_PORTS_IN_PORT`\- The port of the sender that the receiver will connect to. This is the value the sender has for`SYNCED_PORTS_OUT_PORT`. Defaults to 10500 if not set.
