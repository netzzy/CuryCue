# MacOS Environment Variables

### For the Current Login Session

To add an environment variable to the system for the duration of this login, open Terminal and type the following: 
[code]
    launchctl setenv ENV_VAR value
    
[/code]

The variable will take effect the next time you startup TouchDesigner. To remove the variable, in Terminal enter: 
[code]
    launchctl unsetenv ENV_VAR
    
[/code]

### For Every Login Session

To have the environment variables set for every login session, create a file name`ca.derivative.environment.plist`in your user library directory`~/Library/LaunchAgents`. You may need to create the`LaunchAgents`directory if it does not exist. Paste the following into the file and update with your environment variables.: 
[code] 
    <?xml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
    <plist version="1.0">
    <dict>
      <!--to set value: launchctl setenv TOUCH_ENV_VAR value-->
      <!--to unset value: launchctl unsetenv TOUCH_ENV_VAR-->
      <key>Label</key>
      <string>ca.derivative.environment</string>
      <key>ProgramArguments</key>
      <array>
        <string>sh</string>
        <string>-c</string>
        <string>
    launchctl setenv ENV_VAR_1 value1;
    launchctl setenv ENV_VAR_2 value2;
        </string>
      </array>
      <key>RunAtLoad</key>
      <true/>
    </dict>
    </plist>
    
[/code]

These variables will be loaded at the start of each login session. They may not be available in the applications that are automatically reopened by the system. To stop loading the variables for the remaining of your login, you will need to unload the file and also unset the environment variables in the file via Terminal 
[code] 
    launchctl unload ~/Library/LaunchAgents/ca.derivative.environment.plist
    launchctl unsetenv ENV_VAR_1
    launchctl unsetenv ENV_VAR_2
    
[/code]

You can run the following to reload the environment variables again. 
[code] 
    launchctl load ~/Library/LaunchAgents/ca.derivative.environment.plist
    
[/code]

If you no longer want certain environment variables to be defined, you can remove them from your plist file or remove the plist file. Restart your system, or unload the plist file and unset the variables in Terminal to take effect for the rest of the session. 

See also: [Variables](<./Variables.md> "Variables")
