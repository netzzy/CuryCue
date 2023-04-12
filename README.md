# Introduction

## Overview

CuryCue is a set of tools for TouchDesigner, focused on managing and controlling content during live performances, including theater shows and events. Developed and used internally for several years, it's been battle-tested on multiple projects ([here](https://1101.media/solaris/) [here](https://1101.media/curiosity-opera/) [here](https://1101.media/flora-spiens/) [here](https://1101.media/wish-delivery-multimedia-performance/) [here](https://visualartists.ru/the-rose-of-the-world/)).  

The system is primarily a preset management solution for TouchDesigner, with a logic inspired by QLab and lighting consoles. It organizes content into sequential cues, which not only simplifies the process of handing over the show to operators unfamiliar with TouchDesigner but also proves convenient for shows with a clear sequence of events where precise and timely scene transitions are crucial, as opposed to VJ-style performances or similar formats.

The core functionality was developed using Python, and SQLite is utilized for storing keys and their parameters. Initially, MySQL was used for this purpose.
