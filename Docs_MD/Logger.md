# Logger

## Logging in TouchDesigner

**Starting with** the first build released publicly on the **2023.10k branch** , TouchDesigner now comes with its own [Palette:logger](<./Palette-logger.md> "Palette:logger") COMP. 

Additionally, two Logger COMP instances are running from within TouchDesigner internals. 

All of the logging messages are staying on the machine where the project is running, locally, and none of those messages are being sent to a Derivative owned server or third party service. 

The first logger, accessible by all through`op.TDResources.TDAppLogger`, is a root logger onto which, by default, all additional loggers are parented to. A secondary logger is used internally for our system tools to log messages to. In the case of an unusual issue, it could be that we ask of you to forward us your log file. 

Anywhere, users can rely on the`op.TDResources.TDAppLogger`and call [the methods promoted on its extension](<./Palette-logger_Ext.htm#Methods> "Palette:logger Ext"). 

Users wishing for a more custom experience can drag n drop from the palette the [Palette:logger](<./Palette-logger.md> "Palette:logger") COMP and tweak all parameters. 

A good starting point is to setup a new logger at the root of your project to make it project based. Breaking it down to individual loggers for your larger components would be a very Python oriented approach. 

The Logger COMPs are wrapped around the Python logging library. Where the loggerCOMP.Logger member is actually a Logger object from the [Python Logging Library](<https://docs.python.org/3/library/logging.html>). Advanced users can extend the features of the Logger COMP with that in mind. 

Logging can come at a performance cost when used inefficiently. Users should [visit this page](<https://docs.python.org/3/howto/logging-cookbook.html#logging-cookbook>) which applies to TouchDesigner as well.
