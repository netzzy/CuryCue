# Palette:tdPyEnvManager Ext

These Extensions reference a specific [Palette:tdPyEnvManager](<./Palette-tdPyEnvManager.md> "Palette:tdPyEnvManager").   
  
# TDPyEnvManagerExt

The extension of the [TDPyEnvManager COMP](<./Palette-tdPyEnvManager.md> "Palette:tdPyEnvManager"). Most users might want to access the`Context`using the`ContextLock`.`LinkPyEnv`,`LinkConda`,`LinkCondaEnv`are other methods of interest using the extension. While the promoted methods are currently the bare minimum, users wishing for specific logic found through the COMP's UI can share an RFE on the [forum](<https://forum.derivative.ca/>). Advanced users can use the [TDPyEnvManagerHelper](<./TDPyEnvManagerHelper.md> "TDPyEnvManagerHelper") module. 

## Members`Context`→`dict`: 

> Context dictionary containing information about the environment.`ContextLock`→`threading.Lock`: 

> Lock for the Context dictionary to ensure thread safety.`Helper`→`TDPyEnvManagerHelper`: 

> A class to manage the installation and setup of Python and Conda environments for TouchDesigner. This class doesn't require TouchDesigner to be running and can be used as a standalone Python script. It gets imported as a module in TouchDesigner in the context of the TDPyEnvManager to be used as a helper class within the TDPyEnvManager. It provides methods to download and install Miniconda, create Conda environments, and manage Python virtual environments. It also includes methods for logging, downloading files, creating .gitignore files, and verifying installations as well as various other tools and utilities. More details available at [TDPyEnvManagerHelper](<./TDPyEnvManagerHelper.md> "TDPyEnvManagerHelper").`Logger`→`Logger COMP`: 

> Logger COMP for logging messages used in the TDPyEnvManager extension.`Ready`→`bool`: 

> Flag to indicate if the TDPyEnvManager environment is ready to be used.`SafeLogger`→`logging.Logger`: 

> SafeLogger, Logger COMP's python logger object, for logging messages safely across threads.`ThreadManager`→`ThreadManager COMP`: 

> A reference to TouchDesigner's ThreadManager for creating TDTasks and running them in threads.`Working`→`bool`: 

> Flag to indicate if the TDPyEnvManager is currently working on a (potentially threaded) task.

## Methods`TDPyEnvManagerExt.LinkConda(installPath: pathlib.Path)`→`bool: True if successful, False otherwise.`: 

> Given a path to a conda installation, attempt to link the current TouchDesigner session to it. This will allow TouchDesigner to interact with lib conda. 
> 
> Args: 
> 
>   * installPath (pathlib.Path): Path to the conda installation folder.
>`TDPyEnvManagerExt.LinkCondaEnv(envPath: pathlib.Path = None)`→`bool: True if successful, False otherwise.`: 

> Given an environment path, attempt to link the current TouchDesigner session to a Conda environment. LinkConda must be called first to ensure the Conda install is available. 
> 
> Args: 
> 
>   * envPath (pathlib.Path): Path to the Conda environment.
>`TDPyEnvManagerExt.LinkPyVenv(envPath: pathlib.Path)`→`bool: True if successful, False otherwise.`: 

> Given a path to a Python virtual environment, attempt to link the current TouchDesigner session to it. 
> 
> Args: 
> 
>   * envPath (pathlib.Path): Path to the Python virtual environment.
>`TDPyEnvManagerExt.OpenCli()`→`None`: 

> Open the command line interface (CLI) for the current mode and environment.`TDPyEnvManagerExt.RefreshCondaEnvListThreaded()`→`None`: 

> Refresh the list of conda environments in a thread.`TDPyEnvManagerExt.Reset()`→`None`: 

> Reset the component to its initial state. Trigger onInitTD() to reinitialize the component.`TDPyEnvManagerExt.ResetContext()`→`None`: 

> Reset the context to its initial state.`TDPyEnvManagerExt.Restart()`→`None`: 

> Prompt the user to save following a restart trigger, before quitting the current TouchDesigner session.`TDPyEnvManagerExt.UnlinkConda()`→`bool: True if successful, False otherwise`: 

> Unlink the current conda installation from the current TouchDesigner session.`TDPyEnvManagerExt.UnlinkCondaEnv()`→`bool: True if successful, False otherwise.`: 

> Unlink the current conda environment from the current TouchDesigner session.`TDPyEnvManagerExt.UnlinkPyVenv()`→`bool: True if successful, False otherwise.`: 

> Unlink the current Python virtual environment from the current TouchDesigner session.

TouchDesigner Build: Latest\nwikieditor2025.30000
