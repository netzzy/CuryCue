# Network Protocols

## Overview

There are numerous network protocols that Touch supports. Protocols have different ways of delivering data and establish connections. OPs can have some or all of the possible protocols, depending on how things are organized. For example the Touch In/Out CHOPs support most protocols, while the UDP DATs only support the UDP based protocols. 

This is in reference to the [TCP/IP DAT](<./TCP/IP_DAT.md> "TCP/IP DAT"), [UDP In DAT](<./UDP_In_DAT.md> "UDP In DAT"), [OSC In DAT](<./OSC_In_DAT.md> "OSC In DAT") and others. 

Protocols are mix of the below properties. 

### Reliability

Protocols can be reliable or unreliable. A reliable protocol guarantees that all data is delivered, and it's delivered in the correct order. Unreliable protocols can deliver data out of order, or can lose data altogether. 

### Streaming vs. Messaging

Network protocols can send data either as a stream of data, or in individual messages. When sending as a stream the data is just an endless sequence of bytes that needs to be parsed using a known data layout format. A streaming protocol can choose to delay sending data for some amount of time to allow more data to be accumulated in the 'send buffer', which will allow the actual send operation to send more data in one go. This reduces network overhead, but will result in the data arriving into larger, less frequent batches than you may expect. 

A messaging protocol on the other hand sends the data immediately as a single message of known size. All or none of the message is received, you don't receive a partial message. There is a limit on how big the message can be, depending on your network hardware. The hard limit is 65535 bytes though (but you may not be able to send messages even close to this big). 

### Connection orientated or Connectionless

Protocols can either require a connection be established before sending data, or they can be connectionless. 

When a protocol is connectionless the data is just send out onto the network aimed at a particular address/port, and if someone is listening at that address/port they'll receive the data. Multiple senders can send to the same address/port without error, which can cause unexpected results. 

### Multiple clients, Unicast and Multicast

Connection orientated protocols send data from one computer to one computer. However some OPs support multiple clients (such as the Touch In/Out CHOPs), in which case the same data is send multiple times to multiple computers. 

Connectionless protocols can either be unicast or multicast. Unicast means the data to an address/port that only one computer is listening on. Multicast means it's send to an address/port that multiple computers can listen to. 

However one catch with unicast is if you have multiple listeners on in the same process. Some OPs such as all the network DATs and the OSC In CHOP can share a socket internally in a process, allowing them to receive the same data from one sender. If you try to have different listeners in different processes though, only one process will receive data. 

#### Multicast

Multicast messages are only sent once over the network (regardless of how many computers are listening) and are sent to the special address range 224.0.0.0 to 239.255.255.255. 239.255.0.1 - 239.255.0.255 is the recommended range to use, as that is part of the private local multi-cast range of addresses. The listening computers should **not** have their network card's IP address set to something in this range, but should rather specify the same address in their OP's parameter. Since the data is only sent once, multicast is a very efficient way of sending the same data to multiple computers. 

## TCP/IP

TCP/IP is reliable, streaming, connection orientated protocol. A single server can send to multiple clients at the same time. 

## UDP

UDP is an unreliable, messaging, connectionless protocol. It supports sending as both unicast and multicast.
