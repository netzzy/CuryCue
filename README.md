# Introduction

## Overview

CuryCue is a set of tools for TouchDesigner, focused on managing and controlling content during live performances, including theater shows and events. Developed and used internally for several years, it's been battle-tested on multiple projects ([here](https://1101.media/solaris/) [here](https://1101.media/curiosity-opera/) [here](https://1101.media/flora-spiens/) [here](https://1101.media/wish-delivery-multimedia-performance/) [here](https://visualartists.ru/the-rose-of-the-world/)).  

The system is primarily a preset management solution for TouchDesigner, with a logic inspired by QLab and lighting consoles. It organizes content into sequential cues, which not only simplifies the process of handing over the show to operators unfamiliar with TouchDesigner but also proves convenient for shows with a clear sequence of events where precise and timely scene transitions are crucial, as opposed to VJ-style performances or similar formats.

The core functionality was developed using Python, and SQLite is utilized for storing keys and their parameters. Initially, MySQL was used for this purpose.

## Introduction

In CuryCue, the cuelist functions in a manner similar to a lighting console's cuelist. You have fixtures (in this case, TouchDesigner components or nodes) with a variety of parameters, and cues to store the parameter values. To learn how to set up and configure the components and parameters that will become your "fixtures," refer to the "Setting up Components and Parameters" section.

There's no need to store all parameters within each cue; you can simply record the modifications. The remaining parameters are inherited from prior cues. For example, when you execute a cue with only one altered parameter out of ten, the other nine parameters will be derived from the change history of all preceding cues, starting from the first up to the current one. If a parameter has not been assigned a value in any previous cues, its default value will be utilized (this value is established when you first place the parameter under CuryCue's control and can be adjusted in "Fixture Mode").

CuryCue can operate in three distinct layouts: "Show Layout," "Edit Layout," and "Fixture Layout.". 

You can switch between these layouts using the menu located in the top-right corner, under the "Cue list" menu.

Show Layout: This layout is dedicated to playing your cues when all programming is complete and prepared.

Edit Layout: This layout is designed for programming your cuelist.

Fixture Layout: This layout enables you to modify the components governed by CuryCue.
