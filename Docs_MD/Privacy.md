# Privacy

Privacy of TouchDesigner Components (`.tox`files) or Projects (`.toe`files) is the protection of networks that enables them to be used but not be visible or editable. 

The Privacy features can limit access to the entire`.toe`[TouchDesigner Environment](<./.md> ".toe") file, or to individual [Component](<./Component.md> "Component")`.tox`files. Privacy features require **TouchDesigner Pro** license to set after which all licenses types respect the privacy settings of a project or component. That is, the end-user will not need a Pro license to run Private`.toe`files or Private components. Non-Commercial/Commercial/Educational/Pro Designer/Player will work with a Private`.toe`file, as long as it’s not using any features their license doesn’t support. 

You can start a project in [Perform Mode](<./Perform_Mode.md> "Perform Mode") without Privacy (and the need for a Pro license) using the Dialogs->Window Placement dialog. But without Privacy, pressing Esc in TouchDesigner will bring you into [Designer Mode](<./Designer_Mode.md> "Designer Mode") where the networks are visible and editable. 

## Project Privacy

The Project Privacy option blocks access to editing networks in a`.toe`project file. This will protect the contents of the`.toe`file. 

In TouchDesigner, under **File - > Project Privacy...(Pro Only)**, you are given options to add or remove privacy from your toe file. Launching a`.toe`saved with privacy enabled will only open in [Perform Mode](<./Perform_Mode.md> "Perform Mode"), with no access to the networks. To access the network again press the **Shift+Esc** key over the Perform window, to be prompted for the password. 

Privacy will be reactivated the next time it enters perform mode. That is, the password must be re-entered each time performance mode is exited. 

Once in the network, use **File - > Project Privacy...(Pro Only)** again to remove it permanently if desired. 

  
To hide image, movie, audio and other media that you embed in the file use the [Virtual File System](<./Virtual_File_System.md> "Virtual File System"). 

## Component Privacy

Component Privacy blocks access to the contents of a component. The contents can not be viewed or access by users or other operators and scripts. You can set Component Privacy with a password or with a CodeMeter dongle. 

**NOTE:** When allowing users to load arbitrary components into a privacy protected component, these loaded components have full access to the hosting protected component's architecture and contents. 

### Component Privacy with Password

Right-click on any component and select Privacy... A dialog will open prompting for a password to enable component privacy. This will block access to the contents of a component but it will run normally. 

Right-click > Privacy... on a component that has privacy enabled and a dialog will prompt the user for a password for temporary access. This will let allow access to the component for the remainder of the session but restarting the project will restore the privacy. 

Right-click > Privacy... on a component that is temporarily accessed (as described above) will give the option for restoring the privacy again. This allows testing the component is private without having to restart the file. The other option here is to provide the password again to completely remove privacy from this component. This deletes the privacy and the component is no longer private until a new password is set. 

### Component Privacy with CodeMeter Dongle

Component Privacy can also be locked to [CodeMeter](<http://www.wibu.com/codemeter.html>) [dongles](<./License_Dongle.md> "License Dongle"). 

You can now setup CodeMeter dongles that will license a component to run (cook). These dongles do not give access to the networks inside, they just allow them to run on any licensed TouchDesigner or TouchPlayer computer. If the dongle is not present, the component will not [cook](<./Cook.md> "Cook"). This gives you a way to customize and manage the licensing of components you create and keep the internal networks private. A using this component dongle privacy requires a [Pro](<./TouchDesigner_Pro.md> "TouchDesigner Pro") license for setup but no additional fees charged by Derivative. The component with dongle privacy set will work on all license types of TouchDesigner and TouchPlayer when the appropriate dongle is present. 

#### Steps to Using CodeMeter Dongle Component Privacy

1) Initially it is required to get a Firm Security Box (FSB) dongle and **FirmCode** from [CodeMeter](<http://www.wibu.com/codemeter.html>). This is a service/product provided by CodeMeter and handled between the developer and CodeMeter. CodeMeter will issue you an FSB and FirmCode once you have an account setup with them. 

2) Once you have a FirmCode, you can then setup a dongle with your unique FirmCode and create any number of **ProductCodes**. These can be used for different products, components, or features you wish to associate with the ProductCodes. All dongle setup is handled by the CodeMeter License Editor which is part of the [CodeMeter Development Kit](<http://www.wibu.com/downloads-developer-software.html>). 

3) You can now create 2 types of dongle 
* **Developer Dongle** \- This dongle allows access and editing of the private component and is for the author(s) of the component. To create this you must set the FirmCode, the ProductCode and additionally set FeatureMap = 1 on that ProductCode. This developer dongle is also required to setup the dongle privacy on the component, in otherwords to 'lock' it.
  * **License Dongle** \- This dongle allows for the component to run in TouchDesigner or TouchPlayer when it is plugged in. However, it still blocks access to the contents of a component so the networks are private. To create this you must set the FirmCode and the ProductCode only.


4) With your Developer Dongle plugged in, setting privacy on a component can be done through python or the Privacy Dialog (right-click on component and select 'Privacy...'). After setting this privacy the only way to access inside the component is with a Developer Dongle plugged with a matching FirmCode, ProductCode, and that ProductCode's Feature Map = 1. The only way to run this component is also with the same matching Developer Dongle or with a License Dongle with matching FirmCode and ProductCode. 

CodeMeter dongles can have multiple FirmCodes and ProductCodes on the same dongle. So it is possible to add your own component licensing to the same dongle that holds a TouchDesigner or TouchPlayer Commercial or Pro license. 

Contact us for further details about Developer Dongles. 

## Privacy and Licenses

A private`.toe`or component does not affect the licensing installed on the system. They will work with any licenses (non-commercial included), and work the same as a non-private file running on that license. That means if the file uses Pro only nodes, those nodes will only function if a Pro license is installed. If the license is non-commercial, all of the TOPs will still be limited resolution. Private files will work in TouchPlayer as well, with the same limitations that TouchPlayer has with a regular`.toe`file. If a private`.toe`file is being used for a commercial (paying) project, it still requires a Commercial license.
