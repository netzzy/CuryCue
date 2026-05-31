# Peer Class

A Peer describes the network connection originating a message in the callback functions found in [oscinDAT](<./OscinDAT_Class.md> "OscinDAT Class"), [tcpipDAT](<./TcpipDAT_Class.md> "TcpipDAT Class"), [udpinDAT](<./UdpinDAT_Class.md> "UdpinDAT Class"), [udtinDAT](<./UdtinDAT_Class.md> "UdtinDAT Class"). 

## Members`owner`→`OP`**(Read Only)** : 

> The [OP](<./OP_Class.md> "OP Class") to which this object belongs.`port`→`int`**(Read Only)** : 

> The network port associated with the peer.`address`→`str`**(Read Only)** : 

> The network address associated with the peer.`hostname`→`str`**(Read Only)** : 

> The network hostname associated with the peer.

## Methods`close()`→`bool`: 

> Close the peer connection. Returns True if successful. Closing a peer can be useful when implementing HTML server protocols for example.`sendBytes(*messages)`→`int`: 

> Send a sequence of bytes through this connection. No terminators are appended. Note: the message will not be OSC formatted. 
> 
> Messages can any combination of strings, byte arrays, or individual single-byte numeric values. To serialize non-byte values (example floats or integers) there are several python modules to do this, such as pickle or struct. Returns the number of bytes sent. 
[code] 
>     n.sendBytes( 'TYPE', 23, 255, 12, 0x34, b'\x01\x00\x02\x00\x03\x00\x00\x00')
>     
[/code]`sendOSC(address, *values, asBundle=False, useNonStandardTypes=True, use64BitPrecision=False)`→`int`: 

> Send an OSC formatted message through this connection. Multiple pairs of address/valueLists arguments to be passed. This method will automatically decide what OSC type to convert the passed values to. 
> 
> Returns the number of bytes sent. 
> 
>   * address - The OSC address to label this message with.
>   * values - A list of values to send in this message.
>   * asBundle - (Keyword, Optional) When true, all messages are sent inside a single bundle.
>   * useNonStandardTypes - (Keyword, Optional) When True, values may be sent over using the non-standard OSC type. For example True and False will be sent as boolean T and F types, rather than an int with a value of 1 and 0. **Available in 099.2018.21730 or later.**
>   * use64BitPrecision - (Keyword, Optional) When True, integer and float values will be sent over as 64-bit values. Requires useNonStandardTypes to also be True. **Available in 099.2018.21730 or later.**
> 

[code]
>      vals = [1, b'abc', 'apple', [6,7,8], True, None, float("infinity")]
>     n.sendOSC('/abc', vals)
>     
[/code]
> 
> Integers
>     If`useNonStandardTypes=True`, then either a 32-bit or 64-bit integer, depending on the magnitude of the integer's current value.
>     If`useNonStandardTypes=False`, then a 32-bit integer if the magnitude fits in a 32-bit integer, or an exception if it's too large.
>     If`use64BitPrecision=True`, then always a 64-bit integer.
> Floats
>     If`use64BitPrecision=True`, then always a 64-bit float.
>     If`use64BitPrecision=False`, then always a 32-bit float.
> Float with value Infinity
>     If`useNonStandardTypes=True`, then the OSC Infinitum type.
>     If`useNonStandardTypes=False`, then always a 32-bit float.
> Booleans
>     If`useNonStandardTypes=True`, then a boolean T or F type.
>     If`useNonStandardTypes=False`, then a 32-bit integer with a value of 1 or 0.
> None
>     If`useNonStandardTypes=True`, then an OSC nil type.
>     If`useNonStandardTypes=False`, then a 32-bit integer with a value of 0.
> Strings
>     A OSC string in all cases.
> bytes or bytearray object
>     An OSC blob. Make sure to put the bytes/bytearray object into a list, and not just pass it directly to sendOSC. If passed directly to sendOSC not in a list then it will be treated as a list of individual integer values and not get sent as a blob.`send(*messages, terminator='')`→`int`: 

> Send a sequence of strings through this connection. Note: the message will not be OSC formatted. 
> 
>   * messsage - One or more strings to send across the network connection.
>   * terminator - (Keyword, Optional) Specifies how the message is to be terminated. If no append terminator is specified, a null character will automatically be appended to the message. To send no terminator, use terminator=''.
> 

> 
> Returns the number of bytes sent. 
[code] 
>     n.send('Hello', 'World',  terminator='\r\n') # send two strings with windows newline termination.
>     
[/code]

TouchDesigner Build: Latest\n2021.100002018.28070before 2018.28070
