# Palette:logger Ext

These Extensions reference a specific [Palette:logger](<./Palette-logger.md> "Palette:logger"). The Extension class of a logger COMP.   
  
# LoggerExt

The LoggerExt constructor drives the Logger COMP and exposes various promoted methods in addition to holding essential data to the Logger COMP instance and the logging library. 

## Members`Active`→`bool`: 

> Whether the Logger COMP is currently Active or not. Should always match the`self.ownerComp.par.Active`value.`IncludePID`→`bool`: 

> Whether the Logger COMP is currently including the PID in the log messages or not. Should always be the opposite of the`self.ownerComp.par.Addpidtofilename`value.`LogFileName`→`str`: 

> A string representation of the full file name used by the logger handler when logging to file.`LogFolder`→`str`: 

> A string representation of the full folder path were the log file is being stored. Defaults to the project folder /TDLogs folder.`LogLevel`→`str`: 

> A string representation of the log level currently being selected. Can be of type CRITICAL, ERROR, WARNING, DEBUG, INFO. Should always be the opposite of the`self.ownerComp.par.Loglevel`value.`Logger`→`logging.Logger`: 

> The current logging library Logger object.`LoggerName`→`str`: 

> The logger name used for the logger object initialization. In the logger object, this will also follow the dot notation based on whether the logger has any parents. It will always get updated based on`self.ownerComp.par.Loggername`value.`Origin`→`COMP`: 

> Where the logging message are originating from. This gets added to the logging messages.`LogQueue`→`queue.Queue`: 

> A possibly empty queue that is used with the QueueHandler of the Logger COMP. The queue can sometimes be filled if the logger object was set to active, messages started being logged but no additional handlers were setup.`ExtraHandlers`→`dict`: 

> A dictionary holding the additional handlers to be used with the QueueHandler. This can be the StreamHandler, TimedRotatingFileHandler, or optional handlers added by the user using the AddExtraHandler method.`QueueHandler`→`logging.handlers.QueueHandler`: 

> The QueueHandler used with the logging.Logger object of that Logger COMP.`QueueListener`→`logging.handlers.QueueListener`: 

> The QueueListener used with the QueueHandler object of that Logger COMP.

## Methods`LoggerExt.ClearHandlers()`: 

> In the case that a Logger get reinitialized and an handler get duplicated, use this method to clear the handlers. A new handler should be created after calling createFileHandler or similar. This method is here as an helper to accomodate developers adding custom handlers.`LoggerExt.Critical(message: str, withInfos: bool = True)`→`None`: 

> Log a Critical message. 
> 
>   * message (str): The required message to be added to the LogItem. A message can be an empty string.
>`LoggerExt.Debug(message: str, withInfos: bool = True)`→`None`: 

> Log a Debug message. 
> 
>   * message (str): The required message to be added to the LogItem. A message can be an empty string.
>`LoggerExt.Error(message: str, withInfos: bool = True)`→`None`: 

> Log an Error message. 
> 
>   * message (str): The required message to be added to the LogItem. A message can be an empty string.
>`LoggerExt.Info(message: str, withInfos: bool = True)`→`None`: 

> Log an Info message. 
> 
>   * message (str): The required message to be added to the LogItem. A message can be an empty string.
>`LoggerExt.AddExtraHandler(handler:logging.Handler)`→`None`: 

> Add an extra handler to the`optionals`key of the self.ExtraHandlers dict. 
> 
> Update the listener. 
> 
> This method is exposed and is meant to be used by developers if they wish to implement an additional handler to which the QueueHandler will send dequeued log messages. 
> 
>   * handler (logging.Handler): A valid logging.Handler.
>`LoggerExt.DeleteExtraHandler(handler:logging.Handler)`→`None`: 

> A handler to be remvoed from the`optionals`ExtraHandlers. 
> 
> Update the listener. 
> 
> This method is exposed and is meant to be used by developers if they wish to implement an additional handler to which the QueueHandler will send dequeued log messages. 
> 
>   * handler (logging.Handler): A valid logging.Handler.
>`LoggerExt.ClearHandlers()`→`None`: 

> In the case that a Logger get reinitialized and an handler get duplicated use this method to clear the handlers. A new handler should be created after calling createFileHandler or similar.`LoggerExt.Log(message: str, level: str, withInfos: bool = True, **logItemDict: dict) -> None`: 

> This is the main method called from the overrides for Info, Debug, Error, etc. 
> 
> It is going through additional checks before calling the underlying methods tolog messages to file, textport, or statusbar. All those additional method calls are subject to the current parameters setup ofthe logger COMP. When a Callback DAT is added, the callback onMessageLogged() will be called,passing the logItemDict to the user. 
> 
>   * message (str): The required message to be added to the LogItem. A message can be an empty string.
>   * level (str): The required LogLevel, such as ERROR, WARNING, INFO, etc.
>   * withInfos (bool): Include additional informations in log message from the stack trace. Defaults to True.
>   * logItemDict (**dict): Additional keywords can be used to override the default data such as`source`,`absFrame`,`frame`>`LoggerExt.Warning(message: str, withInfos: bool = True)`→`None`: 

> Log a Warning message. 
> 
>   * message (str): The required message to be added to the LogItem. A message can be an empty string.
> 


TouchDesigner Build: Latest\nwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditor2025.30000
