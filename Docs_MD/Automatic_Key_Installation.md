# Automatic Key Installation

To aid in deploying TouchDesigner onto many computers, keys can be installed automatically instead of manually using the [Key Manager Dialog](<./Key_Manager_Dialog.md> "Key Manager Dialog"). **Note: this method only works if no keys are currently enabled on the machine**. This can be useful to rolling out licenses onto lab machines at schools, or machines being built for a large project. Other options for multi machine licenses are:  
[Floating Licenses Using a Dongle](<./License_Dongle.htm#Floating_Licenses_Using_a_Dongle> "License Dongle")  
[Floating Cloud Licenses](<./Floating_Cloud_Licenses.md> "Floating Cloud Licenses")

## Setup

This is done by first: 
* creating a file called TDAutoKey.txt on the desktop of the target computer
  * running Touchdesigner


As with the regular License Install preocedure, **an active Internet Connection is necessary**. 

The TDAutoKey.txt file will need to have some required information such as your username and password, and there are a few optional options that can be specified if desired. The format of the .txt file is 
[code] 
     setting = value
    
[/code]

**macOS**
* You must be an administrator when you install on macOS and will need to startup TouchDesigner once as an administrator after the key is installed. Afterwards, any user will be able to use TouchDesigner.

## Required Information

The first two pieces of information are the username/password for the Derivative account that contains the key you wish to install 
[code] 
     username = <DerivativeAccountUsername>
     password = <DerivativeAccountPassword>
    
[/code]

Next you need to specify the type of key you wish to install: 
[code] 
     product = <ProductName>
    
[/code]

Valid Values: 
* TouchDesigner
  * TouchPlayer


[code] 
     license = <LinceseType>
    
[/code]

Valid Values: 
* Commercial
  * Pro
  * Educational
  * Non-Commercial

## Optional Settings

Since 099 has update dates, by default a license with an update date the farthest into the future will be selected. You can instead select one with the closest update date by setting: 
[code] 
     updateDate = closest
    
[/code]

If this is not set, then it behaves as if the option is set to: 
[code] 
     updateDate = farthest
    
[/code]

To control if a dialog comes up upon successful installation of a key use this setting. It defaults to 'true' if not specified 
[code] 
     notifySuccess = <TrueOrFalse>
    
[/code]

To control if a dialog comes up if any error occurs use this setting. It defaults to 'true' if not specified 
[code] 
     notifyFailure = <TrueOrFalse>
    
[/code]

To automatically delete the TDAutoKey.txt after a successful key installation use this setting. It defaults to 'false' if not specified 
[code] 
     deleteAfterSuccess = <TrueOrFalse>
    
[/code]

  
An example TDAutoKey.txt file is located [File:TDAutoKey.txt](</File:TDAutoKey.txt> "File:TDAutoKey.txt"). The username and password fields should be changed to match the account being used. 

See Also: [License Dongle](<./License_Dongle.md> "License Dongle")
