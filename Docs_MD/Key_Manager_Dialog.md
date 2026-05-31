# Key Manager Dialog

#### Description  
  
The Key Manager lets you create, install, and disable keys for TouchDesigner. When TouchDesigner does not find a valid key on startup, the Key Manager dialog will automatically open. 

When already running TouchDesigner, the Key Manager can be opened from the **Dialogs** menu or using the **< alt+k>** shortcut. 

#### Creating a Key

This section describes creating and installing a key for TouchDesigner if your computer is connected to the internet. If you do not have an internet connection on the computer, see the **Offline** section below. 
1. Select the **Create** option along the top of the Key Manager Dialog.
  2. Sign In using your Derivative account username and password. Click the **Sign In** button.
  3. In the following dialog, it will display all the available licenses in your account. Select which license to create a key with and click the **Create Key** button. Licenses that are greyed out need to be [updated](<./Updates.md> "Updates") to work with the installed build.


The key will be created and installed and you're ready to go!. 

#### OFFLINE - Creating a Key

_ONLY Use this method if your computer is offline. To disable the key in the future you will need an internet connection._

This section describes creating and installing a key if the computer can not be connected to the internet. 

In the case that the TouchDesigner computer can not connect to the internet, keys can be created for it on another connected device. 

1\. Take note of the **Machine Name** and the **System Code** near the bottom of the Key Manager dialog on the computer you need to make a key for. 

2\. Go to [MY ACCOUNT](<https://www.derivative.ca/user>) and login. Go to **MY LICENSES**. 

  
3\. Locate the license you would like to use to create a new key with. The license must not be in use on another computer (See "Disabling a Key" if the license is in use). 

  
4\. Click on the license to expand its **Details**. Click the **Create Key** button to proceed. 

5\. In the popup dialog, enter your computer's information which is displayed at the bottom of the Key Manager Dialog. Click **Generate** when ready and the key will be created. 

  
6\. Copy and paste the key into the **Install** section of the Key Manager Dialog. Click the **Install Key** button and you're ready to go! 

#### Disabling and Transferring a Key

  
A key must be Disabled to transfer to another machine, or to create a new key when you [update](<./Updates.md> "Updates") your license. 

The computer must be connected to the internet to disable a key. This connection is required so the key can be disabled in your Derivative account which allows you to create a new key for another computer. 
1. Open the Key Manager Dialog under the Dialogs menu.
  2. Select the **Disable** option along the top of the Key Manager Dialog.
  3. The list below shows the currently valid keys. Select the key you want to disable by clicking on it.
  4. Click the **Disable Key** button. If the key was successfully disabled in your account (on the Derivative servers) and locally it will be removed from the list and is now ready to use on another computer.


The **Help** section of the dialog has answers some frequently asked questions. 

##### System Code

#### Troubleshooting

If a Key or License Retrieval Error occurs when running TouchDesigner, refer to _Problems after installation with licensing or keying_ in [Troubleshooting](<./Troubleshooting.md> "Troubleshooting"). 

The most common reason an existing key stops working is due to the machines system code changing. **TouchDesigner license keys are system code specific** , the system code is used to create the key and the key will not work if the system code has changed. You can view the current system code at the bottom of the Key Manager Dialog. You can inspect the system code used when a key was created by logging into MY ACCOUNT and reviewing the license in MY LICENSES. 

Often system codes change after making core hardware changes (CPU/Motherboard) or operating system changes (such as reformatting or changing versions). 

System Codes are made using various details from the computer’s hardware and the installed operation system, changing any of these details will result in a completely different system code. 

Before making such changes to a machine with an active TouchDesigner key installed, we recommend disabling the existing key using the Key Manager Dialog. 

For any other licensing questions or issues, please contact us at **licensing@derivative.ca**.
