# Palette:debugControl

##   
  
Summary

This component facilitates experimentation with and control of the builtin`debug`statement. It is an operator based interface for the [debug module](<./Debug_module.md> "Debug module"). 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[Palette:debugControl Ext](</index.php?title=Palette:debugControl_Ext&action=edit&redlink=1> "Palette:debugControl Ext \(page does not exist\)")

## 

Usage

Setting the various parameters will use the`tdu.debug.setStyle`function to change the behavior of the builtin`debug`statement. You can use the Test pulse to print a test debug statement to the textport. 

## 

Parameters - Debug Control Page

Refresh`Refresh`\- Refreshes parameters to current debug style settings. 

Apply Settings On Start`Applysettingsonstart`\- If On, apply the component's`debug`setting parameters when TouchDesigner is started. Otherwise, the parameters will be refreshed to default settings on start. 

Print Style`Printstyle`\- ⊞ \- Define how arguments to`debug`are converted for printing. 
* pprint`pprint`\- convert non-string args to pprint.pformat(arg, indent=4). Makes lists, dicts, etc. easily readable
* repr`repr`\- convert non-string args to repr(arg)
* str`str`\- convert non-string args to str(arg)


showDAT`Showdat`\- in`debug`message, show the DAT where`debug`was called 

showFunction`Showfunction`\- in`debug`message, show function where`debug`was called 

showLineNo`Showlineno`\- in`debug`message, show line number where`debug`was called 

timeStamp`Timestamp`\- [Python time format code.](<https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes>) Menu contains examples. 

Suppress`Suppress`\- if True, suppress (don't print) any`debug`calls 

formatOverride`Formatoverride`\- overrides the default message that`debug`prints. You can use {0}, {1}, and {2} for DAT, function, and line number 

functionOverride`Functionoverride`\- overrides the builtin TD debug function. This function will be called with all arguments from any debug calls in your project. Set to False to remove override. 

Test Debug`Testdebug`\- evaluated argument to pass to`debug`as a test 

Test`Test`\- Run a test`debug`call with the argument provided in Test Debug parameter 

## 

Parameters - About Page

Help`Help`\- Opens this page. 

TouchDesigner Build: Latest\nmw-removed-redirectmw-new-redirect2023.112802021.10000
