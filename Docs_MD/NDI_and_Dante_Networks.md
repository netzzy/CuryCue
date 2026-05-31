# NDI and Dante Networks

[NDI](<./NDI.md> "NDI") and [Dante](<./Dante.md> "Dante") Running NDI on a Dante Network will greatly increase latency. NDI must be forced to work on a different network and NIC than Dante. 

These are the results. It’s clear that Dante and NDI don't play nice. However I was never able to properly isolate NDI onto a particular NIC. 

<https://forums.newtek.com/showthread.php/154532-Required-dual-NIC-setup-having-tough-time-getting-NDI-to-only-hit-one> <https://forums.newtek.com/showthread.php/154021-Routing-NDI-traffic-to-a-specific-NIC>

Dante Latency with NDI Running 2 streams of 3840x2160. Very bad bursts of crackle. Dante Controller clearly shows greater latency. 

Dante with no NDI. No crackle. Latency is clearly lower. 

When changing from one setting to another on Dante some computers took time to resync and for the crackle to go away. Wait a few minutes. It should clean up. This was particularly frequent with the Intel / Supermicro server - it would report normally low latency - around 1.3 msec but would crackle for up to 10 minutes then settle down and be clean. 

Extra Things Hardware Realizations The 10G Asus cards has clearly very high latency by default as indicated by the Dante Controller software. The left is ASUS and the right is the SuperMicro Intel 10G. 

The NUC can’t play a single NDI 3840x2160 Input.
