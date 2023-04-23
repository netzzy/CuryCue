![IMAGE ALT TEXT HERE](https://i.ytimg.com/an_webp/kxGlQbHNec4/mqdefault_6s.webp?du=3000&sqp=CKLNlKIG&rs=AOn4CLAHIZvhDImSP4Zr9Y0tkhvsA63G5A)

[https://www.youtube.com/watch?v=kxGlQbHNec4](https://www.youtube.com/watch?v=kxGlQbHNec4)

1. **CuryCue**  
    Introduction  
    User Interface Basics  
    CuryCue Workflow  
    Adding Components and Parameters to CuryCue  
    Fixtures Mode  
    Edit Mode: Parameters and Cues Management  
    Show Mode: Cue Switching and Linked Cues  
2. **Content Preset System (Alpha Version)**  
    Architecture's overview   
    Routing system  
    Side Panel and Preset's Internal Timelines and UI widgets  

# Introduction

## Overview

CuryCue is a set of tools for TouchDesigner, focused on managing and controlling content during live performances, including theater performances, installations, and interactive multimedia content. Developed and used internally for several years, it's been battle-tested on multiple projects ([here](https://1101.media/solaris/) [here](https://1101.media/curiosity-opera/) [here](https://1101.media/flora-spiens/) [here](https://1101.media/wish-delivery-multimedia-performance/) [here](https://visualartists.ru/the-rose-of-the-world/)).

CuryCue is a cue-based control system designed specifically for use within Derivative TouchDesigner with a logic inspired by QLab and lighting consoles. It organizes content into sequential cues, which not only simplifies the process of handing over the show to operators unfamiliar with TouchDesigner but also proves convenient for shows with a clear sequence of events where precise and timely scene transitions are crucial, as opposed to VJ-style performances or similar formats.

The core functionality was developed using Python & SQLite.

## CuryCue Logic and Functionality

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

In CuryCue there are three primary modes: **Show mode** and **Edit mode** and **Fixture mode**.  
These modes are designed to suit different phases of the production process. 

💡 **Shortcut to switch between Show/Edit Modes is CTRL+E**

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

The || column field links cues. Double-click to enter 0 or 1. When the longest fade finishes, the next cue triggers. 

![Untitled](https://mulberry-sole-9e5.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F50a8323e-7be7-422d-afcf-6b8e6af432b9%2FUntitled.png?id=fea0ef57-8bce-4627-8d42-671fcb41c13e&table=block&spaceId=f21a68da-c563-4b77-b77e-738b4bcf61fc&width=2000&userId=&cache=v2)

# Content Preset System (Alpha Version)

The alpha version of **CuryCue's** content preset system is designed as a supplementary tool for specific tasks. Users can choose to utilize this system in conjunction with core **CuryCue** functionality or rely on their preferred content management methods.

### **Here's an overview of the system architecture:**

1. Presets are stored in containers inside /project1/Content or op.vcont. Each preset container should have a "ContentPreset" tag.
![Untitled](https://mulberry-sole-9e5.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F63b9dd8d-f3e1-49bf-bdf3-9dc41565277e%2FUntitled.png?id=86c2a419-0d50-423b-8bc6-4df414cf6aad&table=block&spaceId=f21a68da-c563-4b77-b77e-738b4bcf61fc&width=1160&userId=&cache=v2)
![Untitled](https://mulberry-sole-9e5.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F60edc116-2d4e-4387-8518-7b0b136fb4b3%2FUntitled.png?id=6ac23650-9401-44d5-84b9-63cbc56ca712&table=block&spaceId=f21a68da-c563-4b77-b77e-738b4bcf61fc&width=1750&userId=&cache=v2)
2. Each preset container has an external layer (e.g., Scene1, Calibrate) and an internal layer with the same name as the main layer (e.g., Scene1/Scene1, Calibrate/Calibrate, and so on).
![Untitled](https://mulberry-sole-9e5.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F60edc116-2d4e-4387-8518-7b0b136fb4b3%2FUntitled.png?id=6ac23650-9401-44d5-84b9-63cbc56ca712&table=block&spaceId=f21a68da-c563-4b77-b77e-738b4bcf61fc&width=1750&userId=&cache=v2)
3. The external layer is constantly executed and has a set of standard custom parameters: Active, Active fade, and Arming type select .
4. The internal layer's cooking is disabled to save resources if Arming type = auto and Active fade = 0.
5. In fact, the cooking/uncooking of the internal layer is controlled by the **Active fade** parameter, while the editable **Active** parameter allows for the addition of extra filtering and other adjustments. The **Arming type** parameter switches between **auto** and **manual**, as users may want the internal layer to be constantly executed. In such cases, the **Armed toggle** controls the cooking/uncooking, and the **Active fade** parameter only manages the actual fading.
6. Everything that needs to be executed constantly should be in the external layer, while everything that can be uncooked until initialization (controlled by Active/ActiveFade/Armed parameters) should be in the internal layer.
7. **When the Active fade parameter is greater than 0, the contents of the panel component within the internal layer (for example, Scene1/Scene1) will be displayed in the Side panel interface.**
![Untitled](https://mulberry-sole-9e5.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F44ff5f6b-d703-4d01-89de-9acc0cfea594%2FUntitled.png?id=decda901-3153-487c-8480-648d8e7b856b&table=block&spaceId=f21a68da-c563-4b77-b77e-738b4bcf61fc&width=2000&userId=&cache=v2)
8. The *internal layer* can include a component called "**AnimationTimeControl**" that manages an internal timeline. If present, a widget for controlling and monitoring the preset's timeline will appear in both the Side Panel and the Head Panel of the user interface. For additional details, refer to the corresponding section in the documentation.
![Untitled](https://mulberry-sole-9e5.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Ffbec8f79-be94-414b-966d-2c7d605f82e8%2FUntitled.png?id=7fcce119-35cd-452a-ba8c-6e12fbe122e7&table=block&spaceId=f21a68da-c563-4b77-b77e-738b4bcf61fc&width=2000&userId=&cache=v2)
9. Inside every *internal container*, there's a "**LocalPresetClass**" Text DAT that includes a Python class. This allows you to define any required actions during preset initialization, such as rewinding the timeline or resetting certain nodes. You can achieve this by implementing these actions within the **init** constructor, ensuring a seamless and customized setup for your presets that caters to your project's unique needs.
10. Within the **Content** container, a system is in place that gathers output nodes and routes them via composite nodes, such as Composite TOP, Merge SOP, and Sequence CHOP. The main configuration for this system is called "**PresetsRoutingTable**." For more information, refer to the related section on Routing.

## Routing system

![Untitled](https://mulberry-sole-9e5.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F8becfe56-a7d1-4b34-bcea-827708cc31df%2FUntitled.png?id=fd606a69-73c3-4bbc-aa1e-b7dea6ef60fb&table=block&spaceId=f21a68da-c563-4b77-b77e-738b4bcf61fc&width=1690&userId=&cache=v2)

The routing algorithm in the Content Preset system works as follows:

1. In each container with the **ContentPreset** tag, a node search is performed using the name from the "Preset source" column.
2. If **ActiveFade** is enabled ( > 0), the path to the node is added to a string, which is then exported to the "**Composite par**" parameter of the "**Composite node.**"

For example, suppose there are two presets named **Scene1** and **Calibrate**. If both are Armed ( & **ActiveFade** > 0), and both have a **PROJ1_OUT** *TOP*, the parameter "**tops**" of the **PROJ1_COMP** node will be assigned a string: "*/project1/Content/Scene1/PROJ1_OUT /project1/Content/Calibrate/PROJ1_OUT*".

![Untitled](https://mulberry-sole-9e5.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Faff3d9ea-b6bb-4794-8664-14a6dac5ec4a%2FUntitled.png?id=3564bec4-8f6d-4ba3-b185-d61e336ee7e2&table=block&spaceId=f21a68da-c563-4b77-b77e-738b4bcf61fc&width=2000&userId=&cache=v2)

You can collect outputs from your presets with SOP, CHOPs, GEO comps, and more, depending on the architecture of your project. The routing system in the Content Preset system ensures an organized and efficient way to manage multiple output nodes across different presets.

## Side Panel and Preset’s Internal Timelines and UI widgets

![Untitled](https://mulberry-sole-9e5.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fe9947955-c312-4119-b34a-8687aeb12038%2FUntitled.png?id=1c4115f8-85b9-461e-957d-26afd92c372b&table=block&spaceId=f21a68da-c563-4b77-b77e-738b4bcf61fc&width=2000&userId=&cache=v2)

While in Show Mode with the Side Panel displayed, each preset with an ActiveFade value greater than 0 will present itself as a panel, consisting of:

1. The panel selected from the preset's *internal container*. This is where your custom preset UI will be displayed. **Height, width**, and **Align Order** (*important when multiple presets are enabled*) will be inherited from the original panel within the preset's *internal container*.  
2. A **time** widget, if your preset’s *internal container* includes an **AnimationTimeControl**
component.
    1. The widget displays the status (playing/stand by), current time, current frame, and total duration.
    2.  ****A red cursor moves within the widget to indicate playback progress.
        
        ![Untitled](https://mulberry-sole-9e5.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F4dbd10c3-5005-43db-92d7-02e57eef04c1%2FUntitled.png?id=fa640a3a-9e95-4441-a029-06afed39b85f&table=block&spaceId=f21a68da-c563-4b77-b77e-738b4bcf61fc&width=1250&userId=&cache=v2)
        
        When hovering over this panel with the mouse cursor, the following **shortcuts** are available:
        
        1. Left + right mouse buttons: **rewind** to the beginning.
        2. Middle mouse button: **scrub** to a specific point in time.
        3. Left + middle mouse buttons: **toggle** between play and stop.


**©** [Evgeniy Afonin](https://afonin.media) & [Curiosity Media Lab](https://visualartists.ru)
