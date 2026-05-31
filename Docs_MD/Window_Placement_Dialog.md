# Window Placement Dialog

##   
  
Description

The Window Placement Dialog (Alt-w) manages window placement and determines whether TouchDesigner starts in [Perform Mode](<./Perform_Mode.md> "Perform Mode") or [Designer Mode](<./Designer_Mode.md> "Designer Mode"). 

Normally you press F1 and Esc to get in and out of [Perform Mode](<./Perform_Mode.md> "Perform Mode"), which uses the single [Window Component](<./Window_COMP.md> "Window COMP")`/perform`. The default`.toe`file contains one [Window Component](<./Window_COMP.md> "Window COMP") located at`/perform`which has parameters to customize the location, look and behavior of the window when you go into Perform Mode. 

The Window Placement Dialog at Dialogs -> Window Placement (Alt-w) helps with managing one or more Window components. 

Here you see the list of existing Window Components, and for each you can open and close the window, choose it as the one that opens in Perform Mode, open its Parameter dialogs (P button) or open the network containing the Window Component. 

It displays one row for each Window component in your entire`.toe`file. It is harmonized with the parameters of the [Window Component](<./Window_COMP.md> "Window COMP"): What you see/control in Window Placement is a summary of what you see/control in all the Window Components of your project. 

The Main Perform column lets you choose which [Window component](<./Window_COMP.md> "Window COMP") it will use in [Perform Mode](<./Perform_Mode.md> "Perform Mode"), the default being`/perform`. 

You can open the parameter dialog of each Window component (the P button), or open the network where the Window components are located (the arrow), or just open the window itself (Open button). 

The Start in Perform Mode flag lets you choose to start TouchDesigner in Perform Mode or Designer Mode. 

In the Start Position and Custom Settings sections, the Window Placement Dialog determines the position of the [Designer Mode](<./Designer_Mode.md> "Designer Mode") window. 

The [Window Component](<./Window_COMP.md> "Window COMP") uses separate on/off pulse buttons to open and close the window, which can be triggered also with the Open/Close parameter`.pulse()`python method. 

The [Window Component](<./Window_COMP.md> "Window COMP") also has a pulse parameter to temporarily open any Window component in Perform Mode, versus the one specified in the Window Placement Dialog. 

The [Window Component](<./Window_COMP.md> "Window COMP") has a parameter (Redraw) to inform a window to not draw anything. It is useful when no output is needed on the main monitors, for example when you use the [Oculus Rift](<./Oculus_Rift.md> "Oculus Rift"), or when your system only outputs data via the network operators, or via the [Video Device Out TOP](<./Video_Device_Out_TOP.md> "Video Device Out TOP"), or other processes that do not render, such as audio processing or driving LED strips that don't use the video outs. 

**Tip** : You can go into/out-from Perform Mode using python: For example,`ui.PerformMode = True`. See [UI_Class](<./UI_Class.md> "UI Class"). 

**Tip** : You can make a window not appear in the list by putting a [tag](<./Tag.md> "Tag") 'hide' in the Window Component. 

## 

Designer and Perform Mode

See [Designer Mode](<./Designer_Mode.md> "Designer Mode") and [Perform Mode](<./Perform_Mode.md> "Perform Mode"). 

## 

Multiple Monitor Settings

To setup multiple monitors, see [Multiple Monitors](<./Multiple_Monitors.md> "Multiple Monitors") and use the [Window COMP](<./Window_COMP.md> "Window COMP"). For maximum performance, it is generally recommended to put your UI and all your outputs images into one large container for one Window Component, where possible.
