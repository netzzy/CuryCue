# Install TouchDesigner

## How to install TouchDesigner  
  
### Download

Download the latest version of TouchDesigner from [here](<https://derivative.ca/download>)

Alternatively, if you need a specific build of TouchDesigner, you can find archived versions on the [Official Downloads page](<https://derivative.ca/download/archive>). 

### Windows

**Installer Versions for Windows**

There are 2 versions of the Installer available for windows: The Full Installer and the Web Installer. While the first one contains the complete set of all files required to run all features of TouchDesigner, the second Installer is a considerably smaller version with a minimal set of files and the option to install support for features during the installation process or later. The difference in filesize is **2.6 GB** for the Full Installer vs. **570 MB** for the Web Installer. 

The Web Installer does require an active internet connection if extra _Installer Components_ are selected during the installation process. 

Double-click the`TouchDesigner.xxxx.xxxxx.exe`file and follow the instructions on the installer dialog. Please make sure you are installing from an Administrator account. 

### macOS

Double-click the TouchDesigner.xxxx.xxxxx.dmg file and then drag the TouchDesigner icon to your Applications folder. 

**Please make sure you are installing from an Administrator account.**

### Keying

When opening TouchDesigner for the first time, the [Key Manager Dialog](<./Key_Manager_Dialog.md> "Key Manager Dialog") will guide through the process of installing a license. 

## How to install TouchPlayer

### Windows

TouchPlayer is included in the TouchDesigner installer on Windows. To install TouchPlayer, use the TouchDesigner installer and select **Custom Install and TouchPlayer Options** (See details below). After clicking **Install** there will be options for installing TouchPlayer. 

### macOS

On macOS, TouchPlayer is a separate installer you can download from the [Official Downloads page](<https://derivative.ca/download/archive>). 

## Installer Options on Windows

**Custom Install and TouchPlayer options**

Using this checkbox will give you more options after clilcking 'Next' such as 
* Give this installation a custom tag to identify it. This name will be used on the desktop icon and as an additional identifier on all OS references like 'Open With...' menus and 'Add or remove program' dialogs.
  * Display or hide the desktop icon
  * Customize file associations with TouchDesigner
  * TouchPlayer options 
    * Include TouchPlayer desktop icon
    * Include TouchPlayer in the Open With... menu
    * Make TouchPlayer the default aaplication for .toe files (ToughDesigner files)


**Install Runtime for Dongle Licensing**

Check this box to include the installation of CodeMeter service which is required to use TouchDesigner with a [License Dongle](<./License_Dongle.md> "License Dongle")

## Dealing with _Installer Components_ of the Web Installer

When using the Web Installer for Windows, after choosing the installation folder or setting extra options, you will be presented with a selection dialog for _Installer Components_. These are files that pertain to certain features (or support for devices) we have identified as making up a large amount of the installer's file size but are not used frequently by most. 

The dialog lets you choose which features the installer should download during the installation process. The size after the titles is an estimation on how much harddisc space the feature will take up when installed. 

Previously installed _Installer Components_ will be preselected. 

Choosing any of the _Installer Components_ in this process will require an active internet connection. 

### Download location of selected _Installer Component_ files

The installer will download selected component files into the folder`%USERPROFILE%\Documents\Derivative\InstallerCache`on your harddisc. 

Before proceeding with the download, the installer will check if the required file already exists in the folder. 

### Removing downloaded _Installer Component_ files

The last dialog in the Installation routine has a checkbox to remove any downloaded files. It will only remove the files downloaded during the installation process. Alternatively, you can also delete any *.zip files in`%USERPROFILE%\Documents\Derivative\InstallerCache`. 

### Adding _Installer Components_ after an initial Install

To add _Installer Components_ to a perviously installed release, go to Windows' "Installed Apps" dialog and select "Modify" from the right hand side drop down menu on the TouchDesigner installtion you want to modify. 

Choose the _Installer Components_ you want to add from the opening Dialog. 

**NOTE:** you cannot remove _Installer Components_. 

## Installing Multiple Builds at Once

Sometimes you will want multiple builds of TouchDesigner or TouchPlayer installed at the same time. You may need older builds to test previous projects, or you may want to try out the latest features in **Experimental** while keeping **Official** installed for your current project. 

### Windows

When the installer detects TouchDesigner is already installed on the system, it will give you some options for managing multiple builds 

**Install Parallel Build**

This option will install the new build alongside whatever is already installed, without removing your current TouchDesigner builds. You can also use the new 'custom tag' feature under **Custom Install and TouchPlayer options** on the next page to more easily identify it, for example a tag name like _Official_ , _Experimental_ , or _ProjectName_. 

**Replace currently installed build**

This option will replace the build you currently have installed with the new build. If you already have multiple builds installed, a list will be presented letting you pick exactly which build you would like to replace. 

### macOS
* Just drag the application to any convenient location. If it conflicts with another TouchDesigner build already there, select "Keep Both" from the pop-up dialog. To keep it more organized, you can rename the application file to include the build number.
  * Right-clicking on any TouchDesigner file and selecting 'Open With >' will show a list of all TouchDesigner builds on the computer, just select the one you wish to use.

## Useful Installer Command-line switches on Windows based Systems

The Installer can be used with a variety of command-line switches: 

  *`/SILENT`,`/VERYSILENT`Instructs Setup to be silent or very silent. When Setup is silent the wizard and the background window are not displayed but the installation progress window is. When a setup is very silent this installation progress window is not displayed. Everything else is normal so for example error messages during installation are displayed and the startup prompt is (if you haven't disabled it with DisableStartupPrompt or the '/SP-' command line).
  *`/DIR="x:\dirname"`Overrides the default directory name displayed on the Select Destination Location wizard page. A fully qualified pathname must be specified. May include an "expand:" prefix which instructs Setup to expand any constants in the name. For example: '/DIR=expand:{autopf}\My Program'.
  *`/LOG="folder\filename"`Causes Setup to create a log file in the specified directory detailing file installation and [Run] actions taken during the installation process. This can be a helpful debugging aid. For example, if you suspect a file isn't being replaced when you believe it should be (or vice versa), the log file will tell you if the file was really skipped, and why. The information contained in the log file is technical in nature and therefore not intended to be understandable by end users. Nor is it designed to be machine-parsable; the format of the file is subject to change without notice. **NOTE:** The complete path to the intended location of the log file is required.
  *`/Extract`Will extract all relevant files from the installation into a folder. In combination with`/DIR`the target folder can be specified. This can be useful if the installation process is failing for some unknown reasons. In the extracted folder structure, the TouchDesigner.exe executable can be found in the`bin`folder.
  *`/Codemeter`Will select the option to install the Codemeter runtime alongside TouchDesigner.
  *`/Tag="My Tag"`Allows for specifying the custom tag to more easily identify parallel installs.
  *`/TDDesktopIcon=false`Will not place a TouchDesigner application shortcut on the Desktop.
  *`/TDOpenWith=false`Will not include TouchDesigner into the "Open With..." context menu for supported filetypes.
  *`/TPDesktopIcon`Will add a application shortcut to TouchPlayer to the Desktop.
  *`/TPOpenWith`Will include TouchPlayer into the "Open With..." context menu for supported filetypes.
  *`/TPIsDefault`Will set TouchPlayer as the default application for .toe files.


  
For a full list of Command-line switches, please refer to this article: <https://jrsoftware.org/ishelp/index.php?topic=setupcmdline>

## Problems during Installation on Windows OS

### Installer exits during installation or aborts with an Error

When the Installer exits during Installation without giving a sufficient reason, start a Windows Command Prompt window with Administrator privileges and run:`"C:\MyFolder\TouchDesigner0xx.xxxxx.exe" /LOG="example.log"`Send the resulting log file as a zip or link including a description of the encountered error to [Derivative Support](<mailto:support@derivative.ca>)

**Note:** If you persistently run into an issue with the installer, you can try running TouchDesigner without actually installing it. To some extent the installer just copies files to disk and makes sure that some prerequisites are met. All the required files are contained separately in the installer and you can try extracting them using the above mentioned`/Extract`Installer Command-line switch. 

The extracted folderstructure will contain a`bin`folder in which you can find`TouchDesigner.exe`### Installer can't continue because of insufficient access rights to folder

This behavior can happen during the de-installation phase of a previously installed version. The best way around this is to restart your computer and start the installation process again. 

### Installer can't remove previous installed TouchDesigner version

In some cases the Installer will quit because it was not able to uninstall a previously installed TouchDesigner version. 

Geekuninstaller, available from [here](<https://geekuninstaller.com>), has had good results when trying to resolve install and uninstall related problems. 

If the error is persistent, try re-installing the previously installed version of TouchDesigner, remove it via the Windows "Apps & features" Dialog and try installing the new version again. 

## Missing libraries after Installation on Windows OS

### Installing missing libraries for Windows N and Windows KN distributions

Windows N and Windows KN versions are made for the European and Korean market and due to antitrust regulations do not include Windows Media Player which parts of are required to run TouchDesigner. 

You can download and install the missing features for Windows 10 / 11 [here](<https://support.microsoft.com/en-us/windows/media-feature-pack-for-windows-n-8622b390-4ce6-43c9-9b42-549e5328e407>)

## Problems after installation with licensing or keying

### Windows - License Retrieval Error

In some cases starting TouchDesigner will fail with a dialog titled **TouchDesigner Key Retrieval Error** or **License Retrieval Error**. The content of the error message will look similar to this: 

This can be resolved by rebuilding the wmi repository. 

**Please be advised though that deleting and rebuilding the repository can cause damage to the system or to installed applications.**

To perform a rebuild of the WMI repository, please do the following: 
1. Disable and stop the winmgmt service
  2. Locate C:\Windows\System32\wbem and copy the wbem to another location for a backup.
  3. Rename C:\Windows\System32\wbem\repository folder (Note: it will not let you rename the folder if winmngmt service is still running)
  4. Enable and start the winmgmt service
  5. Open Command Prompt as Administrator, run the following commands:`cd C:\Windows\System32\wbem\ for /f %s in ('dir /b *.mof') do mofcomp %s`If you continue to have problems, join the [support thread here](<https://forum.derivative.ca/t/resolved-touchdesigner-wont-run-error-when-reinstalling-key-retrieval-error/269765>). 

### macOS - Permissions Error when installing or disabling a key

If you get a **L1 Key Error** when installing your key (see image below), or if you get an error disabling your key, please follow these instructions. Please make sure you are in and Administrator account. 

In your admin account, open Terminal and paste in the command:`ls -l -d "/Library/Application Support/ca.derivative"`You should get a line back like so. Note that the group owner should be **admin** , not wheel:`drwxrwxr-x@ 10 root admin 340 17 Jan 2017 /Library/Application Support/ca.derivative`If you are missing the directory, then enter this command in the Terminal:`sudo mkdir "/Library/Application Support/ca.derivative"`If you do not have matching permissions (1st column), then enter this command in the Terminal:`sudo chmod 775 "/Library/Application Support/ca.derivative"`If you have wheel instead of **admin** as group owner (4th column), then enter this command in the Terminal:`sudo chgrp -R admin "/Library/Application Support/ca.derivative"`Restart TouchDesigner and try installing or disabling the key again. 

### Firewall Issues

If the Key Manager is giving connection errors, it may be due to a firewall blocking access to our key server. Ensure TCP connections to both www.derivative.ca and derivative.ca on port 443 is allowed through your firewall. 

### Proxy Server

TouchDesigner currently does not make use of proxy server configurations that your system may be using. You'll need to use the Offline key generation method if your connection requires a proxy server. 

## Problems during Uninstall

### Installer exits during Uninstall without error

When this happen, best practice has been to restart the computer to free up any possible locks on the folder. Most commonly after a restart the remaining files will have been removed and a fresh install can be started. 

## See Also

[Automatic Key Installation](<./Automatic_Key_Installation.md> "Automatic Key Installation")

TouchDesigner Build: Latest\nwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditor2023.112802021.100002020.236802018.28070before 2018.28070
