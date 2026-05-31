# UDT

**NOTE UDT has been removed from TouchDesigner 2020 Official builds and later.** UDT is not recommended in older TouchDesigner versions due to some timing bugs.   
  
[UDT](<http://en.wikipedia.org/wiki/UDP-based_Data_Transfer_Protocol>) (UDP-based Data Transfer Protocol) was added to TouchDesigner as an alternative to UDP, which is not reliable because packet loss is not recoverable in UDP. UDT is fast and recovers from lost packets. It is also faster and more immediate than TCP/IP. 

UDT is a reliable UDP-based application level data transport protocol for distributed data intensive applications over wide area high-speed networks. UDT uses UDP to transfer bulk data with its own reliability control and congestion control mechanisms. The new protocol can transfer data at a much higher speed than TCP does. UDT is also a highly configurable framework that can accommodate various congestion control algorithms. 

TouchDesigner uses UDT (in the [UDT In DAT](<./UDT_In_DAT.md> "UDT In DAT"), [UDT Out DAT](<./UDT_Out_DAT.md> "UDT Out DAT"), [Touch Out CHOP](<./Touch_Out_CHOP.md> "Touch Out CHOP") and [Touch In CHOP](<./Touch_In_CHOP.md> "Touch In CHOP")) under the following license. 

## UDT License Agreement

Copyright (c) 2001 - 2007, The Board of Trustees of the University of Illinois. 

All rights reserved. 

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met: 
1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
  2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
  3. Neither the name of the University of Illinois nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.


THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
