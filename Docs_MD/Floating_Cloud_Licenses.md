# Floating Cloud Licenses

TouchDesigner offers floating licenses using [Wibu/CodeMeter's CmCloud licensing technology](<https://www.wibu.com/products/codemeter/codemeter-cloud.html>).   
  
Available for build 2020.28110 or any builds from 2021+ 

**Floating Cloud procedure - After purchase Derivative will send you a credential`.wbc`file, usually issued during Derivative business hours of 10:00-18:00 EST (UTC-4) Toronto time. For inquiries about your credential file please [email our licensing team](<https://derivative.ca/contact-us>).**

## Usage Cases

#### Local Computers Licensed from a Global Pool - Distributed Teams and Remote Working

Floating cloud licenses offer a simple solution for those looking to have a pool of licenses available to any of their team, world-wide. A pool of numerous licenses on one account can be shared between global locations such as offices, studios, or installations, delivering the license to the team member on demand wherever they have an internet connection. This is different from the [Dongle based floating licensing](<./License_Dongle.htm#Floating_Licenses_Using_a_Dongle> "License Dongle"), since that solution requires the Dongle and the local computers to be on the same LAN. 

#### Lab Computers at Schools and Universities

Sometimes lab computers are wiped often and/or don't have admin privledges. Using floating cloud licenses allows the system administrator to install the credentials onto lab computers as part of their disk image. This setup will automatically use licenses when TouchDesigner is in use and return them when TouchDesigner closes. 

See also [Educational Setup](<./Educational_Setup.md> "Educational Setup") for more information about setting up TouchDesigner at educational institutions. 

#### Running TouchDesigner on Cloud Platforms

A great usage case for floating cloud licenses is to make it easy to license TouchDesigner and TouchPlayer when running it on servers in the cloud. Often these virtual cloud servers do not have consistent system codes. This may be because a new instance is spun-up every time the cloud server is launched, or it may be because the way the cloud platform works causes the system code to change often. Dongle-based solutions also don't work since it's rare that access to the hardware is possible for cloud servers. 

## Workflow

The cloud licenses grab a license when TouchDesigner starts and releases a license when it is closed. While it's running TouchDesigner re-renews the license every 9 minutes. So if the internet connection is lost then the license will stop working on that machine when that 9 minute interval check occurs. 

If a machine crashes instead of cleanly closing TouchDesigner, the license will be automatically freed up on the cloud licensing server after 20 minutes. 

## Reliability

Since Cloud licenses require an active internet connection to function, they should only be used in non-critical situations, such as in labs or working at the office, or critical situations where internet access is also a critical element. That is, they are safe to use for cloud systems since if the cloud system loses internet, the system becomes non-functioning regardless of it's using a cloud license or not. 

## Limitations

A single .wbc credential file is limited to 100 connections at a time. If you need more licenses, we'll need to split them across multiple .wbc files. Any machine that is running and has the .wbc credential installed will count against this limit, even if TouchDesigner isn't running. 

On-site shows and installations that cannot have downtime should use a software license or a Dongle based license. 

## Converting Existing Licenses

Any existing license can be converted to a Floating Cloud License simply by paying the difference in price between the standard license and the floating license price. There is no store item to do this, so you can purchase the equivalent amount using "Payment Tokens" on the store, and contacting us at sales@derivative.ca to have your license converted over. Note that the conversion does not change the update date on the license. 

## Setup Floating Cloud Licenses

A single user account can have any number of licenses assigned to be floating in the cloud and any type of license can be used ie. Educational - Commercial - Pro. 

### Activating Floating Cloud Licenses

After purchasing your Floating Cloud License, Derivative will send you a credential file which is a`.wbc`file. 

**NOTE: The credential files are usually issued during Derivative business hours of 10:00-18:00 EST (GMT-4) Toronto time. For any inquiries about your credential file please[email our licensing team](<https://derivative.ca/contact-us>).**

**Install .wbc File**
1. Install [CodeMeter Control Center](<./License_Dongle.htm#Installing_Required_Dongle_Software> "License Dongle").
  2. Open the Codemeter Control Center app, then drag and drop the .wbc file onto the Control Center to install it.


For the computer to acquire a license from the cloud, this`.wbc`needs to be loaded into the [CodeMeter Control Center](<./License_Dongle.htm#Installing_Required_Dongle_Software> "License Dongle") and you need an active internet connection. When TouchDesigner or TouchPlayer launches, if a`.wbc`file is installed on the system, it will attempt to acquire a license available from the cloud service. If any local licenses that are installed are higher (ie. Pro is higher than Commercial), those will be used as well on top of the cloud license. If you don't want to use a cloud license anymore on a computer, you can simply remove the credentials from the CodeMeter Control by following the instructions in the section below. 

Only one`.wbc`credential file is used for all users in an organization that will be using the cloud licenses. The file does not contain any licenses itself. It only contains credentials that are used to contact the cloud server to acquire licenses. If for any reason the credential file becomes compromised (e.g given out to someone that shouldn't have access), then Derivative will need to issue your account a new credential file. All users of the account will need to install that new credential file, as the old one will stop working. 

#### Via Command Line

The credential file can be installed onto the system on the command line with the command: 
[code] 
     cmu32.exe --import --file <yourFile.wbc>
    
[/code]

### Removing Floating Cloud Credentials from a computer

Currently removing a CmCloud license from a computer takes a few steps. We are hoping CodeMeter will release a better solution soon. In the meantime the CmCloud license can be removed using one of two ways. 

#### Via Command Line

Navigate to the CodeMeter runtime directory, usually: C:\Program Files (x86)\CodeMeter\Runtime\bin Execute the command: 
[code] 
     cmu32.exe --delete-cmcloud-credentials --serial <Serial number of CmCloud license>
    
[/code]

On macOS the command is simply called`cmu`. 

#### Enable the 'Remove' button in the CodeMeter Control Panel UI

1\. Open registry editor by clicking the Windows symbols and type: regedit  
2\. Create a new DWORD(32-bit) Value at HKEY_CURRENT_USER/SOFTWARE/WIBU-SYSTEMS/CodeMeterCC with the name "AllowCmActDelete" and set entry to a value of 1.  
3\. Restart the computer.  
In order to deactivate the button follow step 1 and set "AllowCmActDelete" to a value of 0 or delete the "AllowCmActDelete" entry entirely. 

### Updating Floating Cloud Licenses

Updates for Floating Cloud Licenses can be purchased in the store just like regular licenses. Note that all licenses in a floating cloud pool need to have the same Update Date ie. they all need to be updated in a batch. For assistance in updating your Floating Cloud licenses, send us a request at licensing@derivative.ca. 

### Releasing a license that is stuck as in-use

If the computer using a Cloud license, or possibly TouchDesigner on the computer crashes, it's possible the license will still be in the 'in-use' state in the cloud licensing server. To solve this simple restart TouchDesigner on the computer that originally was using the license and then close TouchDesigner. This should release the license on the cloud licensing server. If this doesn't not fix the issue please contact us at licensing@derivative.ca. 

#### Network Port

Network Port number 22350 is the port that the CmCloud service communicates on. 

## Sharing Cloud Licenses Locally

The typical workflow for Cloud licenses is to install the .wbc credentials on each machine that wants to access the license via the cloud. However the workflow of using a local server that is the spot where the .wbc is installed, and other local machines obtain their licenses via that server is also supported, like it is for Dongles. See more information [[[1]](<./License_Dongle.htm#Sharing_Licenses_Over_a_Network%7Chere.>)] Note that the server where the .wbc is installed still needs a stable internet connection to interface with the cloud licensing server. 

## Installing Required Codemeter Software

To use USB License Dongles or Floating Cloud licenses, Codemeter Runtime software is required on your system. 

**NOTE:** Please update to CodeMeter Runtime 7.60+ 

### Windows CodeMeter Install
* When installing TouchDesigner, the first dialog of the installer will have an option for "**Install Runtime for Dongle Licensing** ", make sure this is checked on. Proceed with the installation. You can alternatively download the dongle runtime from here [CodeMeter Download](<https://www.wibu.com/support/user/downloads-user-software.html>). We suggest you turn off the 'Automatic server search' option in the CodeMeter installer options, to allow for quicker startup on networks with many machines with CodeMeter installed.

### macOS CodeMeter Install
* Download and install the CodeMeter Control Center from here:


[CodeMeter Download](<https://www.wibu.com/support/user/downloads-user-software.html>)

If the software or service fails to start, you may need to enable it in your System's Security Preferences. 

## Additional Notes

[Wibu/CodeMeter's CmCloud licensing technology](<https://www.wibu.com/products/codemeter/codemeter-cloud.html>) uses servers located in Germany 

See Also: [License Dongle](<./License_Dongle.md> "License Dongle")
