# TDResources

TDResources is a component containing system resources for TouchDesigner, some of which are available for use in your projects. Access TDResources using its **Global OP Shortcut** : **`op.TDResources`**. **Note:** Access to these resources will be maintained in future versions of TouchDesigner, but the look of them may change. For example, the system popMenu will always be available, but the colors and font may change. 

## Pop-Up Menu

The system pop-up menu, which is a clone of [popMenu](<./Palette-popMenu.md> "Palette:popMenu"), is available via **`op.TDResources.PopMenu.Open(...)`**. It is commonly used for RMB option menus and has 2 layers of sub-menus available for use as well. Example code: 
[code] 
    op.TDResources.PopMenu.Open(['Go', 'Stop'], callback=debug, callbackDetails=['test'])
    
[/code]

For full documentation, see [Palette:popMenu](<./Palette-popMenu.md> "Palette:popMenu") and [PopMenu Custom COMP Examples](<./PopMenu_Custom_COMP_Examples.md> "PopMenu Custom COMP Examples"). 

## Button Pop-Up Menu

The system button pop-up menu, which is also a clone of [popMenu](<./Palette-popMenu.md> "Palette:popMenu"), is available via **`op.TDResources.ButtonPopMenu`**. It is commonly used for menus that pop up when a button is pressed and you want to align the menu to that button, but can technically be used to align a menu to any [Panel Component](<./Panel_Component.md> "Panel Component"). It does not have sub-menus available. 

The difference between this and the system pop-up menu above is that it is meant to be attached to a button and **the Buttoncomp, Horizontalattach, and Verticalattach parameters must be set before calling`Open`.** Example code: 
[code] 
    buttonPopMenu = op.TDResources.ButtonPopMenu
    buttonPopMenu.par.Buttoncomp = op('/myButtonPanel')
    buttonPopMenu.par.Horizontalattach = 'Left'
    buttonPopMenu.par.Verticalattach = 'Top'
    buttonPopMenu.Open(['Go', 'Stop'], callback=debug, callbackDetails=['test'])
    
[/code]

For popMenu documentation, see [Palette:popMenu](<./Palette-popMenu.md> "Palette:popMenu") and [PopMenu Custom COMP Examples](<./PopMenu_Custom_COMP_Examples.md> "PopMenu Custom COMP Examples"). 

## Pop-Up Dialog

The system pop-up dialog, a clone of [popDialog](<./Palette-popDialog.md> "Palette:popDialog"), is available via **`op.TDResources.PopDialog`**. It is used for simple pop-up dialogs with up to four options and an optional text entry box. 

There is a nice code example of this [here](<./PopDialog_Custom_COMP_Examples.htm#Example_4_-_Creating_a_Pop-Up_Dialog_using_script> "PopDialog Custom COMP Examples"). 

For full documentation, see [Palette:popDialog](<./Palette-popDialog.md> "Palette:popDialog"), [popDialog Extension](<./Palette-popDialog_Ext.md> "Palette:popDialog Ext") and [PopDialog Custom COMP Examples](<./PopDialog_Custom_COMP_Examples.md> "PopDialog Custom COMP Examples"). 

## Mouse

There is mouse information in a CHOP available for system use in **`op.TDResources.MouseCHOP`**. This can be used to get the mouse state without needing your own [Mouse In CHOP](<./Mouse_In_CHOP.md> "Mouse In CHOP"). You can see all the channels and access this information by using a [Select CHOP](<./Select_CHOP.md> "Select CHOP"). You can also access it directly using code: 
[code] 
    mouse = op.TDResources.MouseCHOP
    normalizedMouseX = mouse['tx']
    absoluteMouseX = mouse['abs_mouse_x']
    leftButton = mouse['left_button']
    
[/code]

## WebClient

There is a simple [Web Client DAT](<./Web_Client_DAT.md> "Web Client DAT") interface available via **`op.TDResources.WebClient`**. You can request data via Python by calling the following function:`**op.TDResources.WebClient.Request(callback, url, method *args)**`*`callback`\- function to be called with reply. It should have the following arguments: statusCode, headerDict, data, id. These will all be None (except id) if the request times out.
  *`url`\- The URL string to send the HTTP request to.
  *`method`\- The HTTP request method as a string. Must be one of: "GET", "POST", "PUT", "DELETE", "HEAD", "OPTIONS", or "PATCH"
  *`*args`\- The remaining arguments will be passed directly to the web client and all options can be found in the documentation for the`request`function here: [WebclientDAT Class](<./WebclientDAT_Class.md> "WebclientDAT Class")

## FileDownloader

There is a file download utility available via **`op.TDResources.FileDownloader`**. You can download files with it using its`.Download()`method. Aside from downloading onto disc, it is also possible to download a file directly into a project primarily the case for .tox components. 

File downloads can be initialized calling the following function: 

**
[code]
    op.TDResources.FileDownloader.Download(self, url:str = None, location:str = None, loadIntoProj:bool = False, 
    				 compPath:COMP = None, discCopy:bool = False, dwnldCopy:Optional[bool] = None, 
    				 renameTo:str = None, doneCallback=None, abortCallback=None, progressCallback=None, reqMethod:str = 'GET', 
    				 reqData:dict = {}, reqPars:dict = {}, authType:str = None, username:str = None, 
    				 password:str = None, appKey:str = None, appSecret:str = None, oauth1Token:str = None, oauth1Secret:str = None, 
    				 oauth2Token:str = None, uploadFile:str = None, force:bool = False, clear:bool = True, showProgress:Optional[bool]=None)
    
[/code]

**

    

  *`url`(str, optional): The url to download the data from. Defaults to None.
  *`location`(str, optional): The location to save the file to. Defaults to None.
  *`loadIntoProj`(bool, optional): If True, the file will be loaded into the project. Defaults to False.
  *`compPath`(COMP, optional): The COMP to load the file into. Only relevant if loadIntoProj is True. Defaults to None.
  *`discCopy`(bool, optional): If True, the file will be copied to the disk. Only relevant if loadIntoProj is True. Defaults to False.
  *`dwnldCopy`(Optional[bool], optional): Defines how to deal with already existing files: None - return existing file path, True - create a copy of the file, False - overwrite the existing file. Defaults to None.
  *`renameTo`(str, optional): The final name of the downloaded file. Defaults to None.
  *`doneCallback`(_type_, optional): A custom callback function called when the download has successfully finished. Defaults to None.
  *`abortCallback`(_type_, optional): A custom callback function called when the download was aborted. Defaults to None.
  *`progressCallback`(_type_, optional): A custom callback function called when the download has progressed. Defaults to None.
  *`reqMethod`(str, optional): The HTTP request method used for the download. Defaults to 'GET'. Must be one of: "GET", "POST", "PUT", "DELETE", "HEAD", "OPTIONS", or "PATCH"
  *`reqData`(dict, optional): The data to send in the body of the request. Defaults to {}.
  *`reqPars`(dict, optional): Query parameters for the request. The parameters will be URL-encoded and appended to the URL. Defaults to {}.
  *`authType`(str, optional): A case insensitive string for the authentication type. None by default (ie. no authentication), but if filled in it must be one of: basic, oauth1, oauth2.
  *`username`(str, optional): The username for basic authentication. Defaults to None.
  *`password`(str, optional): The password for basic authentication. Defaults to None.
  *`appKey`(str, optional): The application key for oauth1 authentication. Defaults to None.
  *`appSecret`(str, optional): The application secret for oauth1 authentication. Defaults to None.
  *`oauth1Token`(str, optional): The oauth1 token for oauth1 authentication. Defaults to None.
  *`oauth1Secret`(str, optional): The oauth1 secret for oauth1 authentication. Defaults to None.
  *`oauth2Token`(str, optional): The oauth2 token for oauth2 authentication. Defaults to None.
  *`uploadFile`(str, optional): The file path of the file to be uploaded in the request. Only valid with a PUT request method. Defaults to None.
  *`force`(bool, optional): Forces the download skipping the queue. Defaults to False.
  *`clear`(bool, optional): Set to false if the stateDict response should stick around for a final call of this function after successfully downloading or aborting the download. This is useful when an external call keeps probing this functions to return the state of the download. Defaults to True.
  *`showProgress`(Optional[bool], optional): If True, the progress window will be shown. Defaults to None.
