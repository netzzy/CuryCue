# Introduction

## Overview

CuryCue is a set of tools for TouchDesigner, focused on managing and controlling content during live performances, including theater performances, installations, and interactive multimedia content. Developed and used internally for several years, it's been battle-tested on multiple projects ([here](https://1101.media/solaris/) [here](https://1101.media/curiosity-opera/) [here](https://1101.media/flora-spiens/) [here](https://1101.media/wish-delivery-multimedia-performance/) [here](https://visualartists.ru/the-rose-of-the-world/)).

CuryCue is a cue-based control system designed specifically for use within Derivative TouchDesigner with a logic inspired by QLab and lighting consoles. It organizes content into sequential cues, which not only simplifies the process of handing over the show to operators unfamiliar with TouchDesigner but also proves convenient for shows with a clear sequence of events where precise and timely scene transitions are crucial, as opposed to VJ-style performances or similar formats.

The core functionality was developed using Python & SQLite for storing cues & parameters..

## Introduction

In CuryCue, the cue list functions in a manner similar to a lighting console's cue list. You have fixtures (in this case, TouchDesigner components or nodes) with a variety of parameters, and cues to store the parameter values. There's no need to store all parameters within each cue; you can simply record the modifications. The remaining parameters are inherited from prior cues. 

![Untitled](https://mulberry-sole-9e5.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F892d3d2c-82fe-4d8e-bbf3-6a9bfed92890%2FScreenshot_2023-04-19_230756.png?id=6a2ca6dc-82fe-4817-acbe-9dbbf0efbb53&table=block&spaceId=f21a68da-c563-4b77-b77e-738b4bcf61fc&width=2000&userId=&cache=v2)


# UI basics

## Layout

![Untitled](https://mulberry-sole-9e5.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fa3d7742c-56e3-4820-b9bb-510b6ecf692a%2FUntitled.png?id=7f547135-7ed9-4539-b362-3e41c2e87b24&table=block&spaceId=f21a68da-c563-4b77-b77e-738b4bcf61fc&width=2000&userId=&cache=v2)

### Panels

You can turn on and off the panels you don't need in the View menu:

![Untitled](https://mulberry-sole-9e5.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F48a22e74-f7ab-47d1-97f1-54d6ecc99248%2FUntitled.png?id=58c3de6d-3d56-4409-b2d0-8ebfb7f97274&table=block&spaceId=f21a68da-c563-4b77-b77e-738b4bcf61fc&width=2000&userId=&cache=v2)

### File menu / Editing top menu

![Untitled](https://mulberry-sole-9e5.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F144633b1-85b8-4652-8716-a417437d06cf%2FUntitled.png?id=520dbcbd-0024-421b-8e58-f37d36535b2a&table=block&spaceId=f21a68da-c563-4b77-b77e-738b4bcf61fc&width=2000&userId=&cache=v2)

In the **File** menu, in addition to the ability to save your patch, you can open and edit the menu settings file and the Python callbacks file to configure shortcuts and other convenient features for your specific project.

### Parameters export mode

![Untitled](https://mulberry-sole-9e5.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Ff75446ec-2269-4230-9077-eeb742fa6b42%2FUntitled.png?id=4261075e-00ad-40c4-a101-5c69f39f856b&table=block&spaceId=f21a68da-c563-4b77-b77e-738b4bcf61fc&width=2000&userId=&cache=v2)

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

![Untitled](https://mulberry-sole-9e5.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F8cb503b3-274b-4204-903a-42f32748084c%2FUntitled.png?id=4623ccd9-4efb-4542-bc3e-104c101d77f8&table=block&spaceId=f21a68da-c563-4b77-b77e-738b4bcf61fc&width=2000&userId=&cache=v2)

## 1. Adding Components and Parameters to CuryCue

Add parameters to CuryCue by:

1. Dragging and dropping components/parameters inside /project1/CuryCue COMP.
2. Dragging and dropping components/parameters onto the Head Pane in the UI.

**Important!** Add COMP/node first, then parameters.

Check import success in Fixture Mode.

![Untitled](https://mulberry-sole-9e5.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fd17a5491-ece5-4347-b5a0-b787bce58fe0%2FUntitled.png?id=f779fa0a-496b-41da-9e1d-eac5024dbc72&table=block&spaceId=f21a68da-c563-4b77-b77e-738b4bcf61fc&width=2000&userId=&cache=v2)

## 2. Fixtures Mode

![Untitled](https://mulberry-sole-9e5.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F41c9ddb6-ab8b-43a6-91dc-3c5154066a75%2FUntitled.png?id=eb39a134-b34a-424b-8407-ab2f9d4ed214&table=block&spaceId=f21a68da-c563-4b77-b77e-738b4bcf61fc&width=2000&userId=&cache=v2)

## 3. Edit Mode

## Parameters management

The editor features three sections: a cue list on the left, a Component Selector panel in the middle right, and a Parameter Editor in the top right. The bottom right displays saved parameters for the selected cue. Choose components in the selector to view their parameters in the editor.

![Untitled](https://mulberry-sole-9e5.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fbe6e8846-97d0-4ad3-b88c-2c9d331e67e8%2FUntitled.png?id=f3491f98-2098-4de6-a4d2-ec7ddcf0873e&table=block&spaceId=f21a68da-c563-4b77-b77e-738b4bcf61fc&width=2000&userId=&cache=v2)

![Untitled](https://mulberry-sole-9e5.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F80ca95be-7cf3-4d24-b1ec-8c43d50dfedf%2FUntitled.png?id=97e47a42-8440-46f6-ad81-27b310f9ee04&table=block&spaceId=f21a68da-c563-4b77-b77e-738b4bcf61fc&width=2000&userId=&cache=v2)

![Untitled](https://mulberry-sole-9e5.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F72278493-677d-4edc-ba83-249406b1176d%2FUntitled.png?id=61031fe5-dd5c-4bec-8808-97eef06a4a23&table=block&spaceId=f21a68da-c563-4b77-b77e-738b4bcf61fc&width=2000&userId=&cache=v2)

1. To save the current values, you need to select one or more parameters, right-click, and choose "Write Selected Fields to the Key.”
2. To modify a value, double-click on the parameter value (Val in DB) and enter the new value, then press the Enter or Tab key (*even if the parameter was not originally in the cue, it will be added*).

## Cues management

Creating a new key can be done either by duplicating an existing key or by creating a new one through the "Create New Blank Cue" dialog.

![Untitled](https://mulberry-sole-9e5.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F14ed8c44-d333-4ef4-bdf2-6ce2aeafcad6%2FUntitled.png?id=26b9f3d4-8585-4438-9018-df8453152720&table=block&spaceId=f21a68da-c563-4b77-b77e-738b4bcf61fc&width=2000&userId=&cache=v2)

![Untitled](https://mulberry-sole-9e5.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F3f97aa19-1530-42ad-873a-69c21c151a57%2FUntitled.png?id=4b0c28db-93cd-4400-bd1f-8dce09f4d64e&table=block&spaceId=f21a68da-c563-4b77-b77e-738b4bcf61fc&width=2000&userId=&cache=v2)

Cues are typically added by duplicating. Right-click on a cue and then select "Duplicate." *Note that adding cues is not possible in Show Mode!*

## 4. Show mode

Show Mode allows only cue switching, editing cue names or memo fields, and enabling the side panel (from the View menu) if you are using the built-in preset system from VideoProjectorContent. For more information about the side panel, see the section on VideoProjectorContent. 

Switch cues using the Go button, mouse click, hotkeys Right Ctrl + Arrows, or by calling GoNextCue/GoPrevCue methods, e.g., op("/project1/CuryCue").GoNextCue().

The || column field links cues. Double-click to enter 0 or 1. When the longest fade finishes, the next cue triggers. *The ## column can be ignored; it's TBD.*

![Untitled](https://mulberry-sole-9e5.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F50a8323e-7be7-422d-afcf-6b8e6af432b9%2FUntitled.png?id=fea0ef57-8bce-4627-8d42-671fcb41c13e&table=block&spaceId=f21a68da-c563-4b77-b77e-738b4bcf61fc&width=2000&userId=&cache=v2)
