# Introduction

## Overview

CuryCue is a set of tools for TouchDesigner, focused on managing and controlling content during live performances, including theater performances, installations, and interactive multimedia content. Developed and used internally for several years, it's been battle-tested on multiple projects ([here](https://1101.media/solaris/) [here](https://1101.media/curiosity-opera/) [here](https://1101.media/flora-spiens/) [here](https://1101.media/wish-delivery-multimedia-performance/) [here](https://visualartists.ru/the-rose-of-the-world/)).

CuryCue is a cue-based control system designed specifically for use within Derivative TouchDesigner with a logic inspired by QLab and lighting consoles. It organizes content into sequential cues, which not only simplifies the process of handing over the show to operators unfamiliar with TouchDesigner but also proves convenient for shows with a clear sequence of events where precise and timely scene transitions are crucial, as opposed to VJ-style performances or similar formats.

The core functionality was developed using Python & SQLite for storing cues & parameters..

## Introduction

In CuryCue, the cue list functions in a manner similar to a lighting console's cue list. You have fixtures (in this case, TouchDesigner components or nodes) with a variety of parameters, and cues to store the parameter values. There's no need to store all parameters within each cue; you can simply record the modifications. The remaining parameters are inherited from prior cues. 

<aside>
💡 For example

| Cue name | Stored Par 1 | Stored Par2 | Stored Par3 | Calculated 
Par1 | Calculated 
Par2 | Calculated 
Par3 |
| --- | --- | --- | --- | --- | --- | --- |
| Cue 1 | 1 | 0 | 1 | 1 | 0 | 1 |
| Cue 2 | 0 |  |  | 0 | 0 | 1 |
| Cue 3 |  | 1 |  | 0 | 1 | 0 |
| Cue 4 | 1 |  | 1 | 1 | 1 | 1 |
| Cue 5 |  | 0 |  | 1 | 0 | 1 |

When you execute a cue with only one altered parameter out of three, the other two parameters will be derived from the change history of all preceding cues, starting from the first up to the current one. 

</aside>

# UI basics

## Layout

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a3d7742c-56e3-4820-b9bb-510b6ecf692a/Untitled.png)

### Panels

You can turn on and off the panels you don't need in the View menu:

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/48a22e74-f7ab-47d1-97f1-54d6ecc99248/Untitled.png)

### File menu / Editing top menu

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/144633b1-85b8-4652-8716-a417437d06cf/Untitled.png)

In the **File** menu, in addition to the ability to save your patch, you can open and edit the menu settings file and the Python callbacks file to configure shortcuts and other convenient features for your specific project.

### Parameters export mode

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f75446ec-2269-4230-9077-eeb742fa6b42/Untitled.png)

CuryCue exports parameters in two ways: CHOP export (faster), direct value writing (reliable), or no export (useful for direct editing to fine-tune parameter combinations, then saving to cues and re-enabling export). Toggle with hotkey Left Ctrl/Shift + Tab.

<aside>
💡 *Attention! If everything went haywire, check your export mode or try toggling the export on and off.*

</aside>

# CuryCue workflow

In CuryCue there are three primary modes: **Show mode** and **Edit mode** and **Fixture mode**. These modes are designed to suit different phases of the production process. 

1. **Show Mode**: This mode is designed for live performance or real-time cue triggering. In Show mode, users can only execute cues without making any changes to the cue list or individual cues. The interface is simplified, and the focus is on ensuring reliable, accurate cue triggering during the actual show. Key features of Show mode include:
    - Simplified interface for clean execution
    - Real-time cue triggering
    - Safe mode to prevent accidental changes during a performance
    - Access to a side panel (see the corresponding section for more information)
    
2. **Edit Mode**: This mode is designed for setting up, programming, and modifying cues and cue lists during planning and rehearsal phases of a project. In Edit Mode, users can create, edit, and delete cues, and adjust cue settings. Key features of Edit Mode include:
- Full access to all editing features and controls
- Ability to create, modify, and delete cues
- Customization of cue properties, such as target components, parameter names, values, and transition times

1. **Fixture Mode**: Manage components and parameters in CuryCue. 

Key features include:

- Overview of controlled components and parameters
- Edit component paths and names
- Customize parameter names
- Adjust default and fade values
- Delete components and parameters

---

Switching between Show Mode, Edit Mode and Fixture mode in CuryCue can be done through a dedicated menu:

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/8cb503b3-274b-4204-903a-42f32748084c/Untitled.png)

## 1. Adding Components and Parameters to CuryCue

Add parameters to CuryCue by:

1. Dragging and dropping components/parameters inside /project1/CuryCue COMP.
2. Dragging and dropping components/parameters onto the Head Pane in the UI.

**Important!** Add COMP/node first, then parameters.

Check import success in Fixture Mode.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d17a5491-ece5-4347-b5a0-b787bce58fe0/Untitled.png)

## 2. Fixtures Mode

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/41c9ddb6-ab8b-43a6-91dc-3c5154066a75/Untitled.png)

## 3. Edit Mode

## Parameters management

The editor features three sections: a cue list on the left, a Component Selector panel in the middle right, and a Parameter Editor in the top right. The bottom right displays saved parameters for the selected cue. Choose components in the selector to view their parameters in the editor.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/be6e8846-97d0-4ad3-b88c-2c9d331e67e8/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/80ca95be-7cf3-4d24-b1ec-8c43d50dfedf/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/72278493-677d-4edc-ba83-249406b1176d/Untitled.png)

1. To save the current values, you need to select one or more parameters, right-click, and choose "Write Selected Fields to the Key.”
2. To modify a value, double-click on the parameter value (Val in DB) and enter the new value, then press the Enter or Tab key (*even if the parameter was not originally in the cue, it will be added*).

## Cues management

Creating a new key can be done either by duplicating an existing key or by creating a new one through the "Create New Blank Cue" dialog.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/14ed8c44-d333-4ef4-bdf2-6ce2aeafcad6/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/3f97aa19-1530-42ad-873a-69c21c151a57/Untitled.png)

Cues are typically added by duplicating. Right-click on a cue and then select "Duplicate." *Note that adding cues is not possible in Show Mode!*

## 4. Show mode

Show Mode allows only cue switching, editing cue names or memo fields, and enabling the side panel (from the View menu) if you are using the built-in preset system from VideoProjectorContent. For more information about the side panel, see the section on VideoProjectorContent. 

Switch cues using the Go button, mouse click, hotkeys Right Ctrl + Arrows, or by calling GoNextCue/GoPrevCue methods, e.g., op("/project1/CuryCue").GoNextCue().

The || column field links cues. Double-click to enter 0 or 1. When the longest fade finishes, the next cue triggers. *The ## column can be ignored; it's TBD.*

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/50a8323e-7be7-422d-afcf-6b8e6af432b9/Untitled.png)
