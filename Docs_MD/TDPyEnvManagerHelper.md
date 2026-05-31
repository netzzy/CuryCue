# TDPyEnvManagerHelper

These Extensions reference a specific [Palette:tdPyEnvManager](<./Palette-tdPyEnvManager.md> "Palette:tdPyEnvManager"). 

# TDPyEnvManagerHelper

A class to manage the installation and setup of Python and Conda environments for TouchDesigner. 

This class doesn't require TouchDesigner to be running and can be used as a standalone Python script. 

It gets imported as a module in TouchDesigner in the context of the TDPyEnvManager to be used as a helper class within the TDPyEnvManager. 

It provides methods to download and install Miniconda, create Conda environments, and manage Python virtual environments. It also includes methods for logging, downloading files, creating`.gitignore`files, and verifying installations as well as various other tools and utilities. 

The file can be found in your TouchDesigner installation folder,`%TD_INSTALL_PATH%\bin\Lib\tdutils\TDPyEnvManagerHelper.py`where`%TD_INSTALL_PATH%`is the path to your TouchDesigner root install folder. (or`$YOUR_TOUCHDESIGNER_INSTALL_PATH/Contents/Frameworks/Python.framework/Versions/$TD_PYENVMANAGER_PYTHONVERSION/lib/python$TD_PYENVMANAGER_PYTHONVERSION/site-packages/tdutils/TDPyEnvManagerHelper.py`on MacOS, where`$YOUR_TOUCHDESIGNER_INSTALL_PATH`is the path to your`TouchDesigner.app`and`$TD_PYENVMANAGER_PYTHONVERSION`is the current TouchDesigner build Python version, such as`3.11`.) 

The TDPyEnvManagerHelper is initialized during TouchDesigner startup. If a`TDPyEnvManagerContext.json`file is found and the environment registered in the context file is valid, then the environment will be added to the Python search path before any TouchDesigner COMP cooks and any custom extensions initialized. 

It's exposed as the`Helper`attribute of the`TDPyEnvManager`, or on`app.pyEnvHelper`. 

## Using the TDPyEnvManagerHelper as a CLI

The TDPyEnvManagerHelper can be used as a standalone CLI tool. Below is a guide on how to use it, including the arguments that can be passed, their example values, and what they do. 

Run the script from the command line:`python TDPyEnvManagerHelper.py [OPTIONS]`Where python is an alias pointing to your TouchDesigner's Python: 
* at YOUR_TOUCHDESIGNER_INSTALL_PATH\bin\python.exe on Windows
  * at YOUR_TOUCHDESIGNER_INSTALL_PATH/Contents/Frameworks/Python.framework/bin/python3.11 on MacOS

Caption text  Argument | Description | Example Value | Default Value   
---|---|---|---  
\--mode | Specifies the mode of environment setup. Can be Conda Env or Py vEnv. | \--mode "Conda Env" | Py vEnv   
\--installPath | The path where Miniconda or Python virtual environment should be created. | \--installPath "C:\Envs" | Example   
\--envName | The name of the Conda or Python virtual environment to be created. | \--envName "MyEnv" | TDPyEnv   
\--pythonVersion | The version of Python to be installed in the environment. | \--pythonVersion "3.11" | Current Python version   
\--clean | Cleans the install directory before installing. | \--clean | False   
\--keepInstaller | Keeps the installer after installation or if installation fails. | \--keepInstaller | False   
  
### Argument Details

#### \--mode

Description: Determines whether to create a Conda environment (Conda Env) or a Python virtual environment (Py vEnv). 

Example:`python TDPyEnvManagerHelper.py --mode "Conda Env"`Default: Py vEnv 

#### \--installPath

Description: Specifies the directory where the environment will be installed. 

Example:`python TDPyEnvManagerHelper.py --installPath "C:\MyEnvironments"`Default: Current working directory. 

#### \--envName

Description: The name of the environment to be created. 

Example:`python TDPyEnvManagerHelper.py --envName "MyCustomEnv"`Default: TDPyEnv 

#### \--pythonVersion

Description: Specifies the Python version to be installed in the environment. **It should always match TouchDesigner's own Python version.**

Example:`python TDPyEnvManagerHelper.py --pythonVersion "3.11"`Default: The current Python version of the system. 

#### \--clean

Description: If specified, the install directory will be cleaned before installation. Example:`python TDPyEnvManagerHelper.py --clean`Default: False 

#### \--keepInstaller

Description: If specified, the installer will not be deleted after installation. 

Example:`python TDPyEnvManagerHelper.py --keepInstaller`Default: False 

### Examples

#### 1\. Create a Python Virtual Environment
[code] 
    python TDPyEnvManagerHelper.py --mode "Py vEnv" --installPath "C:\Envs" --envName "MyPythonEnv" --pythonVersion "3.11"
    
[/code]

Creates a Python virtual environment named MyPythonEnv in the C:\Envs directory with Python version 3.11. 

#### 2\. Create a Conda Environment
[code] 
    python TDPyEnvManagerHelper.py --mode "Conda Env" --installPath "C:\Conda" --envName "MyCondaEnv" --pythonVersion "3.11" --clean
    
[/code]

Creates a Conda environment named MyCondaEnv in the C:\Conda directory with Python version 3.11. The C:\Conda directory will be cleaned before installation. 

#### 3\. Keep the Installer After Installation
[code] 
    python TDPyEnvManagerHelper.py --mode "Conda Env" --keepInstaller
    
[/code]

Creates a Conda environment and keeps the installer file after installation. 

### Notes
* If no arguments are provided, the script will prompt the user for input interactively.
  * Ensure that the installPath directory is writable and has sufficient space for the installation.
  * For Conda environments, the script will automatically download and install Miniconda if it is not already installed.
  * This guide should help you get started with using TDPyEnvManagerHelper as a CLI tool.


Example CLI usages can be found in Samples/TDPyEnvManager folder. You will find the script and both .sh and .bat files to run the script using arguments to create a Conda or Python virtual environment. 

## Members`mode`→`str or None`: 

> The mode used to install an environment. Can be`Conda Env`or`Py vEnv`. Defaults to None.`envname`→`str or None`: 

> The name of the environment to be created for a Python vEnv or a Conda Env. Defaults to None.`installPath`→`pathlib.Path or None`: 

> The path to the Miniconda installation, or the Python Virtual Environment. Defaults to None.`pythonVersion`→`str`: 

> Python version to be installed. Only useful for Miniconda environments. Python vEnv are created with TouchDesigner's own Python interpreter and the version is matching.`pythonVersionNoDot`→`str`: 

> Python version without dot. (e.g., '311' for '3.11')`logger`→`logging.Logger`: 

> A logger to be used in the TDPyEnvManagerHelper. Not to be mixed up with a Logger COMP. This logger is a vanilla Python logger.`taskQueue`→`queue.Queue`: 

> A queue to which tasks are being sent and picked up by a worker thread to be ran in a threading context.`runningProcess`→`subprocess.Popen or None`: 

> The currently running subprocess, if any, doing work in the context of the TDPyEnvManagerHelper.

## Methods`TDPyEnvManagerHelper.__init__(mode:str or None=None, envName:str or None=None, installPath:pathlib.Path or None=None)`→`None`: 

> Initialize the TDPyEnvManagerHelper class. 
> 
> Args: 
> 
>   * mode (str, optional): The mode used to install an environment. Can be`Conda Env`or`Py vEnv`. Defaults to None.
>   * envName (str, optional): The name of the environment to be created for a Python vEnv or a Conda Env. Defaults to None.
>   * installPath (pathlib.Path, optional): The path to the Miniconda installation, or the Python Virtual Environment. Defaults to None.
>`TDPyEnvManagerHelper.__del__()`→`None`: 

> Clean up the worker thread when the instance is deleted.`TDPyEnvManagerHelper.setupLogger()`→`logging.Logger: A logger instance to be used within the helper.`: 

> Setup the logger for the class.`TDPyEnvManagerHelper.worker()`→`None`: 

> Worker thread to process tasks from the task queue. 
> 
> This method runs in a separate thread and continuously checks for tasks in the queue. 
> 
> It executes the tasks and handles any exceptions that may occur during execution or subprocess calls.`TDPyEnvManagerHelper.downloadFile(url:str, destPath:pathlib.Path)`→`None`: 

> Download a file from the given URL to the specified destination path. 
> 
> Args: 
> 
>   * url (str): The URL to download the file from.
>   * destPath (pathlib.Path): The destination path where the file will be saved.
>`TDPyEnvManagerHelper.createGitIgnore(path: pathlib.Path)`→`None`: 

> Create a .gitignore file in the specified path. 
> 
> Args: 
> 
>   * path (pathlib.Path): The path where the .gitignore file will be created.
>`TDPyEnvManagerHelper.createCondaRc(path: pathlib.Path)`→`None`: 

> Create a .condarc file in the specified path. 
> 
> Args: 
> 
>   * path (pathlib.Path): The path where the .condarc file will be created.
>`TDPyEnvManagerHelper.verifyConda(installPath: pathlib.Path)`→`bool: True if Conda is installed, False otherwise.`: 

> Verify if Conda is installed in the specified path. 
> 
> Args: 
> 
>   * installPath (pathlib.Path): The path where Conda is expected to be installed.
>`TDPyEnvManagerHelper.verifyCondaLib(installPath: pathlib.Path)`→`bool: True if the Conda library is accessible, False otherwise.`: 

> Verify if the Conda library is accessible in the specified path. 
> 
> Checks if the site-packages directory is in sys.path and if the conda module can be imported. 
> 
> Args: 
> 
>   * installPath (pathlib.Path): The path where Conda is expected to be installed.
>`TDPyEnvManagerHelper.downloadConda()`→`pathlib.Path: The path to the downloaded Miniconda installer.`: 

> Download the Miniconda installer for the current platform.`TDPyEnvManagerHelper.cleanDirectory(path: pathlib.Path)`→`None`: 

> Clean the specified directory by removing it and its contents. 
> 
> Args: 
> 
>   * path (pathlib.Path): The path to the directory to be cleaned.
>`TDPyEnvManagerHelper.installConda(installPath: pathlib.Path, keepInstaller: bool = False)`→`None`: 

> Install Miniconda using the downloaded installer. 
> 
> Args: 
> 
>   * installPath (pathlib.Path): The path where Miniconda will be installed.
>   * keepInstaller (bool, optional): Keep the installer on the system after installation. Defaults to False.
>`TDPyEnvManagerHelper.cleanupFile(filePath: pathlib.Path)`→`None`: 

> Clean up the specified file by removing it. 
> 
> Args: 
> 
>   * filePath (pathlib.Path): The path to the file to be cleaned up.
>`TDPyEnvManagerHelper.createCondaEnv(installPath: pathlib.Path, envName: str, pythonVersion: str, useEnv: bool = False)`→`None`: 

> Create a Conda environment using the specified parameters. 
> 
> Args: 
> 
>   * installPath (pathlib.Path): The path where Conda is installed.
>   * envName (str): The name of the Conda environment to be created.
>   * pythonVersion (str): The version of Python to be installed in the environment.
>   * useEnv (bool, optional): Use the environment.yml file to create the environment. Defaults to False.
>`TDPyEnvManagerHelper.verifyCondaEnv(condaInstallPath: str, envName: str)`→`bool: True if the Conda environment exists, False otherwise.`: 

> Verify if the Conda environment exists in the specified path. 
> 
> Args: 
> 
>   * condaInstallPath (str): The path where Conda is installed.
>   * envName (str): The name of the Conda environment to be verified.
>`TDPyEnvManagerHelper.activateCondaEnv(installPath: pathlib.Path, envName: str)`→`None`: 

> Activate the specified Conda environment. 
> 
> Args: 
> 
>   * installPath (pathlib.Path): The path where Conda is installed.
>   * envName (str): The name of the Conda environment to be activated.
>`TDPyEnvManagerHelper.setCondaRoot(installPath: pathlib.Path)`→`pathlib.Path: The path where Conda is installed.`: 

> Set the root directory of the Conda installation. 
> 
> Args: 
> 
>   * installPath (pathlib.Path): The path where Conda is installed.
>`TDPyEnvManagerHelper.getCondaRoot()`→`pathlib.Path: The path where Conda is installed.`: 

> Get the root directory of the Conda installation.`TDPyEnvManagerHelper.getCondaEnvPath(envName: str)`→`pathlib.Path: The path to the Conda environment.`: 

> Get the path to the Conda environment. 
> 
> Args: 
> 
>   * envName (str): The name of the Conda environment.
>`TDPyEnvManagerHelper.exportCondaEnvYaml(envPath: pathlib.Path)`→`None`: 

> Export the Conda environment to a YAML file. 
> 
> Args: 
> 
>   * envPath (pathlib.Path): The path to the Conda environment to be exported.
>`TDPyEnvManagerHelper.verifyPython(installPath: pathlib.Path)`→`bool: True if Python is installed, False otherwise.`: 

> Verify if Python is installed at the specified path. 
> 
> Args: 
> 
>   * installPath (pathlib.Path): The folder path where Python is expected to be installed.
>`TDPyEnvManagerHelper.createPythonEnv(envName: str, useReq: bool = False)`→`None`: 

> Create a Python virtual environment using the specified name. 
> 
> Args: 
> 
>   * envName (str): The folder name of the Python virtual environment to be created.
>   * useReq (bool, optional): Use a requirements.txt file if present in the current working directory. Defaults to False.
>`TDPyEnvManagerHelper.activatePythonEnv(envName: str)`→`None`: 

> Open a CLI and activate the specified Python virtual environment. 
> 
> Args: 
> 
>   * envName (str): The name of the Python virtual environment to be activated.
>`TDPyEnvManagerHelper.setPythonRoot(installPath: pathlib.Path)`→`pathlib.Path: The path where Python is installed.`: 

> Set the root directory of the Python installation. 
> 
> Args: 
> 
>   * installPath (pathlib.Path): The path where Python is installed.
>`TDPyEnvManagerHelper.getPythonEnvPath(envName: str)`→`pathlib.Path: The path to the Python virtual environment.`: 

> Get the path to the Python virtual environment. 
> 
> Args: 
> 
>   * envName (str): The name of the Python virtual environment.
>`TDPyEnvManagerHelper.getPythonSitePackagesPath(envName: str)`→`pathlib.Path: The path to the site-packages directory of the Python virtual environment.`: 

> Get the path to the site-packages directory of the Python virtual environment. 
> 
> Args: 
> 
>   * envName (str): The name of the Python virtual environment.
>`TDPyEnvManagerHelper.exportPyEnvRequirements(envPath: pathlib.Path)`→`None`: 

> Export the requirements of the Python virtual environment to a requirements.txt file. 
> 
> Args: 
> 
>   * envPath (pathlib.Path): The path to the Python virtual environment to be exported.
>`TDPyEnvManagerHelper.validatePath(path: pathlib.Path)`→`bool: True if the path is valid, False otherwise.`: 

> Validate if the given path is writable and exists. 
> 
> Args: 
> 
>   * path (pathlib.Path): The path to be validated.
>`TDPyEnvManagerHelper.validateEnvName(envName: str, maxLength: int = 30)`→`str: Cleaned and valid environment name.`: 

> Validates and sanitizes an environment name. 
> 
> Args: 
> 
>   * envName (str): Original environment name.
>   * maxLength (int): Max allowed length.
>`TDPyEnvManagerHelper.stopWorker()`→`None`: 

> Stop the worker thread by sending a shutdown signal (None) to the task queue.`TDPyEnvManagerHelper.appendVEnvSuffix(envName: str)`→`str: The environment name with '_vEnv' suffix if it was not present, otherwise the original name.`: 

> Append '_vEnv' to the environment name if it doesn't already end with it. 
> 
> Args: 
> 
>   * envName (str): The name of the environment.
>`TDPyEnvManagerHelper.getHighestPyVer(condaPath: str)`→`str or None: The highest Python version folder name if found, otherwise None.`: 

> Get the highest Python version folder in the specified conda path. 
> 
> Args: 
> 
>   * condaPath (str): The path to the conda installation.
> 


TouchDesigner Build: Latest\nwikieditor2025.30000
