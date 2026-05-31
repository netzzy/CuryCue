# Tscript Commands

  
These are the commands in the [Tscript](<./Tscript.md> "Tscript") scripting language used in TouchDesigner. See also [Python](<./Python.md> "Python"). 

Type`help`in the [Textport](<./Textport.md> "Textport") to get a list of all Tscript commands, or`help _commandname_`. 

Commands can contain [Expressions](<./Tscript_Expressions.md> "Tscript Expressions") between backquotes, such as:`echo sine of 45 degrees is`sin(45)``## Sweet Sixteen Commands

Command | Purpose | Related Command   
---|---|---  
[opparm](<#opparm>) | Put a value in a parameter of an operator. | [parmls](<#parmls>)  
[tabcell](<#tabcell>) | Put a value in the cell of a specific columns or rows from a DAT. | [type](<#type>), [tabinsert](<#tabinsert>)  
[set](<#set>) | Set a variable to a value. | [rvar](<#rvar>), [cvar](<#cvar>)  
[echo](<#echo>) | Echo a string to the textport. | [ex](<#ex>)  
[if](<#if>) | Conditional check. |   
[for](<#for>) | Looping. | [foreach](<#foreach>), [while](<#while>)  
[cc](<#cc>) | Go to a different current component. | [pc](<#pc>), [lc](<#lc>), [lf](<#lf>)  
[opadd](<#opadd>) | Create a new node. | [oprm](<#oprm>)  
[opscript](<#opscript>) | Show all parameter settings of a node as a script. | [opset](<#opset>), [opwire](<#opwire>)  
[run](<#run>) | Run a script in another DAT. | [include](<#include>), [delay](<#delay>)  
[args](<#args>) | Set values sent to a script to variables. |   
[click](<#click>) | Operate a panel gadget. | [vclick](<#vclick>)  
[view](<#view>) | View a node in a floating window. | [controlpanel](<#controlpanel>)  
[send](<#send>) | Send a message by UDP, TCP/IP, serial, OSC. |   
[opcook](<#opcook>) | Force a node to cook. |   
[find](<#find>) | Search for a string. |   
  
## Alphabetical List

## 

args [options] [arguments]

This command will parse command line options and arguments into local variables, making a script more readable, by avoiding the numbered argument variables: $arg1, $arg2, etc. 
[code] 
    # Consider a DAT named text1 with the following command:		
    args "-p ''oppath" "-q ''quality" red greed blue		
    # Executing 'run dat1 -p /project1 -q 95 0.1 0.2 0.3', will cause		
    # the above args command to set the following local variables:		
    $oppath = "/project1"		
    $quality = "95"		
    $red = "0.1"		
    $green = "0.2"		
    $blue = "0.3"		
    # In addition, the following local variables will be set,		
    # signifying those particular options were specified:		
    $_q = "1"		
    $_p = "1"		
    # Note that options are optional and can be any length of		
    # letters, and specified in any order.For example, executing 'run		
    # dat1 -p /project1 0.1 0.2 0.3', would still set $oppath, $red,		
    # $green, $blue, but would set $quality to "" and $_q to "" as they		
    # were not specified.
    
[/code]

## 

audioplay [-d delay] [-p pan] [-v volume] [-f delay] [-r rolloff] choppath index [method]

This command will trigger and play audio held in an Audio Play CHOP specified by a path to a CHOP. The Audio Play CHOP can hold one or more audio files. The list of audio files is specified by the CHOP's 'Sound File' or 'DAT List' parameters. 

**Options:**
* index the row of the DAT table specified in the CHOP.
  * method describes how the file is played:
  * stop stop audio
  * playcurrent play from current position
  * loopcurrent loop from current position
  * playstart play from start position
  * loopstart loop from start position
  * -d specifies an optional delay (specified in seconds)
  * -p specifies an optional pan (0 = left, 1 = right)
  * -v specifies an optional volume
  * -f specifies an optional fade delay
  * -r specifies an optional rolloff factor while fading. A value of 1 specifies no rolloff while smaller values cause sharper rolloffs.
[code]# stop the 11th file:		
        audioplay /audioplay1 10 stop		
        # stop all files:		
        audioplay /audioplay1 -1 stop		
        # replay 11th file from the start:		
        audioplay /audioplay1 10 playstart		
        # replay 11th file from the start after a 0.5 second delay:		
        audioplay -d 0.5 /audioplay1 10 playstart		
        # set volume of 11th file to 0.8 and play from the start:		
        audioplay -v 0.8 /audioplay1 10		
        # set fade in/out delay of 11th file to two seconds with a		
        # rolloff factor of 0.7 then play from the start:		
        audioplay -f 2 -r 0.7 /audioplay1 10		
        # fade in 11th file to volume 0.5 while playing from start:		
        audioplay -v 0.5 -f 2 /audioplay1 10  playstart
        
[/code]

## 

beat [-b bpm] [-t]

This command is used to calculate a 'Beats Per Minute' or BPM value. You begin by setting the starting BPM value, then executing a series of timed tap options. The resulting BPM is returned after each command. You can then use this value to set the BPM in any timeline by using it in the timeline's Time Component BPM parameter. 

**Options:**
* -b bpm Set the initial beats per minute used in the calculation.
  * -t Send a tap signal and update the bpm calculation.
[code]# set initial BPM to 60:		
        beat -b 60		
        # Set the beginning tap:		
        beat -t		
        # After a moment tap again:		
        beat -t		
        # After a moment tap again:		
        beat -t		
        # Repeat as necessary. After each command the modified BPM is returned.
        
[/code]

## 

bonemoveend bone_object [-f world|parent] [-x xpos] [-y ypos] [-z zpos]

This command adjusts the length and rest angles of the given bone object so that in the rest chain the bone would end at the specified position. 

**Options:**
* -f <rel> Relative to 'world' or 'parent'.

## 

break [levels]

Break out of a loop. If levels is given, that is the number of loops that will be broken out of. 

    **See Also:**[end](<#end>) [foreach](<#foreach>) [while](<#while>) [for](<#for>) [continue](<#continue>)

## 

browser [-w width] off

Sets the display of the browser palette. If no options are given the current state is returned. 

**Options:**
* -w <width> Set the width of the browser palette.
[code]browser on		
        browser off		
        browser -w 300 on
        
[/code]

## 

bvar [name]

Print the built-in variables. If no name is specified, then the list of all built-in variables is printed out. Note: You cannot modify these variables directly. 
[code] 
    bvar T*		
    bvar
    
[/code]

    **See Also:**[set](<#set>) [cvar](<#cvar>) [evar](<#evar>) [rvar](<#rvar>)

## 

cc operator_path

Change the working component to the path specified. You can use wildcard characters like * and ? in the path patterns. 
[code] 
    cc /		
    # The following all go to /project1 in the default TouchDesigner:		
    cc /project1		
    cc /pr*		
    cc /project?		
    # From there you can run any command on nodes in that component:		
    lc
    
[/code]

    **See Also:**[lc](<#lc>) [pc](<#pc>)

## 

cf disk_path

Change the current working directory on the disk 

## 

checkexports

This function goes through the .toe files and checks to see if any exports aren't able to find their targets. 

## 

checkpaths [-a] [-f] [path]

This command will evaluate all parameters to ensure all expressions pointing to operators resolve properly. Any invalid parameters will be reported. 

**Options:**
* -a Check all parameters. Many parameters default to paths which do not resolve (example: Panel Help DAT). These are skipped by default.
  * -f Fix. This will attempt to modify the path if it is broken. The only type of correction are those involving extra "../" prefixes.

## 

checksamplerates [-p path] [rate1 rate2 rate3...]

This command will examine the sample rate of all CHOPs. If the sample rate is not on the list (rate1 rate2 rate3 ...), the full path to the CHOP will be output. If no rates are listed, the global sample rate (default 60) is assumed. 

**Options:**
* -p path specify the node from which to search
[code]# List all CHOPS with a rate other than the global rate:		
        checksamplerates		
        # List all CHOPs with a rate other than 30 or 60:		
        checksamplerates 30 60		
        # To search within one component, use -p, otherwise it searches		
        # from /, the root component.		
        checksamplerates -p /project1		
        # To check the current component and then search from the current component.		
        pc		
        checksamplerates -p .
        
[/code]

## 

chopls [-p pattern] [path]

List the data channels in a set of CHOPS. 

**Options:**
* -p specifies which channels to list.
[code]chopls /ch/ch1/*		
        chopls -p *:tx /ch/ch1/file1
        
[/code]

## 

chopsample [path] [channelname] [index] [value]

This command will modify the value of a single sample in the specified CHOP. This works best with storage CHOPs like the Record CHOP, other CHOPs will have to be locked first. 
[code] 
    chopsample /animate/record1 chan1 50 0.2
    
[/code]

## 

clear

Clears the textport from which this command was executed. 

## 

click [-q] [-l] [-m] [-r] [-c count] [-g groupname] [-f] [-v] path [value1] [value2]

Simulate pressing a button or operating any gadget of a component panel. 

**Options:**
* -l Simulate pressing with the left mouse button.
  * -m Simulate pressing with the middle mouse button.
  * -r Simulate pressing with the right mouse button.
  * -f Force the clicking of the component even if its enable state is set to 0.
  * -g Specify a button radio group name for the clicking of radio groups.
  * -c Update the number of clicks to count.
  * -v Set only the V component of a UV slider.
  * -q Suppress error and warning output messages.
  * value can be used to set values or specify button indices. If any value is an empty string, it will be ignored. i.e. if you pass in 0 "" 1, value1 will be 0 and value2 will be 1. If you pass in a value of 0 for a momentary click button, the click will be ignored by the button.

## 

clipblender clipblender_path [next_clip_path]

This command will manually trigger the next Clip CHOP to be sequenced by a Clip Blender CHOP. If no next_clip_path is given, it will abort its current clip and begin blending into the next. 
[code] 
    clipblender /c1/anim/clipblender1 clips/move_forward
    
[/code]

## 

clipboard [-c] [string]

This command will clear, set or list the contents of the system clipboard, (text data only). 

**Options:**
* -c Clear the clipboard.
[code]# clear the clipboard:		
        clipboard -c		
        # list the contents:		
        clipboard		
        # set the contents:		
        clipboard "This is a test"
        
[/code]

## 

clock [-s sleep] [-w wake_early] [-f frame_step] [-o offset] [-c onoff]

Adjust the clock timing parameters. When running in realtime, the time taken to process a frame may be less than the frame time, which is the inverse global frame rate (see the "fps" command). For example if fps is 60, the frame time is 16.66 msec, yet the actual processing time may take less. The "clock" command can be used to optimize that extra time. It can also be useful when running several applications concurrently. See also the "cooktime" channel of the Info CHOP. 

**Options:**
* -f This sets the number of frames that are advanced each update. Normally this is set to 1.
  * -s Set clock inter-frame sleep (1=sleep, 0=spin). This will control whether or not the application sleeps/delays at the end of each early frame. A value of 1 (default) will cause the CPU to sleep, freeing up processing for other tasks.
  * -w Set clock wakeup early time (milliseconds). This will wakeup the process before the scheduled next frame to get a head-start on the next frame. Too much of a head-start will miss input data, so setting early time to about 3 msec is reasonable.
  * -o Set clock offset (milliseconds). Adjust the phase offset of the frame processing. This is useful when several Touch .toe processes are running at the same time and you want to stagger their start times. Offset would be 0 for the primary process.
  * -c Set if Touch waits for a constant frame interval before starting cooking the new frame. I.e if frames at 16ms long (60hz), Touch will wait until a multiple of 16ms elapses before starting cooking the next frame. Otherwise Touch starts cooking the next frame as soon as the previous frame is done (unless the previous frame was less than 16 ms). This is only useful if you are trying to keep Touch in sync with other processes.
[code]# Have the application delay at the end of each early frame,		
        # Start processing 3 milliseconds after the regular start of a		
        # frame. If the previous frame finishes early, start the next frame		
        # up to 5 milliseconds early:		
        clock -s 1 -w 5 -o 3		
        # Jump two frames each interval. This may be useful when you		
        # wish to have the application cook internally at a finer precision		
        # than what is output.  In this example the internal frame rate may		
        # be 60 fps while the output is updated at 30 fps:		
        clock -s 1 -f 2
        
[/code]

## 

cmdread [-q] filename

Run the commands in the filename specified. If the -q option is given, then no warnings about missing filenames will be printed. 

## 

confirm [-t title] [-l level] message.

This command will open a message box with the specified message. The user must then hit the Ok button in order to proceed. Environment variables will be expanded in the message. 

**Options:**
* -l can be used to specify the type of message box:
  * -l 0 message box (default)
  * -l 1 warning box
  * -l 2 error box
  * -l 3 fatal
  * -t can be used to specify the window title.


    **See Also:**[status](<#status>)

## 

continue [levels]

Skips the remainder of a loop and continues with the next iteration. If levels is specified, then multiple loops will be continued. 

    **See Also:**[end](<#end>) [foreach](<#foreach>) [while](<#while>) [for](<#for>) [break](<#break>)

## 

controlpanel [-o path [-a] [-f] [-r] [-p] [-m x y] [-w x y] [-y xres yres] [-t title]] [-q] [-b path] [-k path] [-K path] [-x path] [-c path] [-C path] [-s path name value [-p] [-f]]

This command is used with control panel components. 

**Options:**
* -q Quiet mode. Do not report errors.
  * -k path Set the keyboard focus to this panel.
  * -K path Set the keyboard focus to this panel and selects all text if it's a field.
  * -b path Set the hierarchical focus to this panel, which sets the Panel Value focusselect to 1. When you click outside the panel, focusselect will return to 0. Use this flag after the panel is already open.
  * -x path Move the mouse to the middle of this panel and make sure it has hierarchical focus.
  * -o path Open the panels specified by path.
  * -r Halt execution of the current script until the window is closed. Use this option when creating menu type panels.
  * -a Open always on top.
  * -p Resize proportionally.
  * -f Open with no borders and no title bar.
  * -m x y Open the window at the current mouse location, offset by x and y.
  * -w x y Open the window at x,y.
  * -y xres yres Specify the window resolution.
  * -t title Specify a window title.
  * -c path Close the panels specified by path.
  * -C path Close the topmost panel specified by path.
  * -s path name value Set a Panel Value.
  * -p Pulse the value (use with -s)
  * -f Force the value of the control panel to change even if its enable state is set to 0.
[code]# Open a control panel with no borders and no title bar:		
        controlpanel -o /button1 -f		
        # Open a control panel at the current mouse location, offset by		
        # x=10 and y=20:		
        controlpanel -m 10 20 -o /button1		
        # Close the panel /button1:		
        controlpanel -c /button1		
        # Close the topmost panel from /button1:		
        controlpanel -C /button1		
        # Pulse the state panel value of /button1:		
        controlpanel -p -s /button1 state 1
        
[/code]


    **See Also:**[click](<#click>) [view](<#view>)

## 

cookrate [frames_per_sec]

If no frames_per_second is specified, the current cookrate is output. Otherwise, the cookrate is set to the specified value. 

## 

cvar [-p path] [-u] [-v] name = value

Set a component variable specified by name to the value given. If no name is specified, then the list of all variables is printed out. 

**Options:**
* -u will un-set the variable(s) specified.
  * -p path will specify a specific component, else the current component is used.
  * -v will return the name of the variable when set if succesful.
[code]# Set in current component:		
        cvar A = 1		
        # List current component:		
        cvar		
        # Unset in current component:		
        cvar -u A*		
        # Specify location of variable:		
        cvar -p /container1 C = 1
        
[/code]


    **See Also:**[set](<#set>) [rvar](<#rvar>) [evar](<#evar>) [bvar](<#bvar>)

## 

delay [-e] [-d seconds] [-f frames] [-m milliseconds] [-k pattern] [-l] [-g groupname] [-c] [-p path] [-v] [-q] command

Execute the given command. Enclose the command in quotes for to preserve spacing and delay variable evaluation. You must specify the delay method -d, -f, or -m. 

**Options:**
* -d Delay command execution by specified seconds
  * -f Delay command execution by specified frames
  * -m Delay command execution by specified milliseconds
  * -e Execute delayed script at the end of the frame, after nodes have had a chance to cook.
  * -c Execute in current path. Default is to execute command in dat_node_path, and return to current path after execution.
  * -p path Execute in the given path.
  * -g Specify a group name for the delayed command
  * -l List all delayed commands
  * -k Kill a set of delayed commands
[code]# Run 5 seconds from now with some arguments		
        delay -d 5 'echo "Hello"'		
        # Run 200 milliseconds from now.  Double quotes evalutates $F at		
        # current frame instaed of 200 ms from now.		
        delay -m 200 "echo $F"		
        # Run 200 milliseconds from now.  Single quotes echo $F at time		
        # of command execution.		
        delay -m 200 'echo $F'		
        # Run 200 milliseconds from now in current location.		
        delay -c -m 200 'echo Hello'		
        # Run 200 milliseconds from now, command in quotes to preserving spacing.		
        delay -m 200 'echo spacing is preserved'		
        # Run 200 milliseconds from now spaces are trimmed.		
        delay -m 200 'echo spacing is preserved'	
        # Single quotes mean $AF is evaluated when command is executed		
        # 200 ms from now.		
        delay -m 200 'echo $AF'		
        # Double quotes or no quotes mean $AF is evaluated now		
        delay -m 200 "echo $AF"		
        # Delayed command group examples:Execute echo in 5 seconds, and		
        # add it to group1:		
        delay -g group1 -d 5 'echo Group1'		
        # List all delayed commands:		
        delay -l		
        # Kill all commands under group*:		
        delay -k group*		
        # Kill and list any commands under group1:		
        delay -v -k group1		
        # Kill all delayed commands:		
        delay -k *
        
[/code]


    **See Also:**[include](<#include>) [inline](<#inline>) [args](<#args>) [click](<#click>) [run](<#run>)

## 

desk [options] [pane_pattern]

This command will display or modify all the desk layout options. See also the neteditor Command and Pane. 

**Options:**
* -l format pane_pattern List panes specified by pattern.
  * -l 0 List pane layout.
  * -l 1 List panes.
  * -l 2 List attributes.
  * -l 3 List paths.
  * -n name Rename a pane specified by pattern.
  * -h pane value [-n name] Split horizontally.
  * -v pane value [-n name] Split vertically.
  * -s value Split value of specified pane's parent.
  * -x Value is pixels instead of ratio.
  * -p path Set path of pane specified by pattern.
  * -t type Set type of pane specified by pattern. Valid pane types are: 
    * neteditor - Network Editor
    * panel - Panel
    * geoviewer - Geometry Viewer
    * topviewer - TOP Viewer
    * chopviewer - CHOP Viewer
    * parameters - Parameter
    * keyframer - Animation Editor
    * textport - Textport
  * -k linkvalue set link value of pane specified by pattern.
  * -y pane Set playbar.
  * -m [0|1] pane_pattern Minimize state.
  * -c Close panes specified by pattern.
  * -f [0|1] pane_pattern Fullscreen state.
  * -r Reset playbar.
  * -o Set tearoff state of panes specified by pattern.
  * -e how Home panes specified by pattern.
  * -e 0 home all.
  * -e 1 home selected.
  * -e 2 frame all.
  * -e 3 frame selected.
  * -e 4 home current.

## 

dialogs [interface]

This command will open a window containing a selection for all available dialogs. If an interface is specified, that dialog will be opened instead. 

**Options:**
* explorer Opens the file explorer.
  * textport Opens the textport
  * macros Opens the Macros dialog.
  * variables Opens the variables dialog
  * bookmarks Opens the bookmarks dialog
  * performance Opens the performance monitor dialog.
  * window Opens the Window Placement dialog.
  * palette Opens the palette explorer
  * midi Opens the MIDI Device Mapper.
  * beat Opens the Beat dialog.
  * error Opens the Errors dialog.
  * help Opens the Help dialog.
  * new Opens the New Project dialog.
  * preferences Opens the Preferences dialog.
  * search Opens the Search dialog.
  * key Opens the Key Manager dialog.
  * chop Opens the CHOP Exporter dialog.
  * import Opens the Import File dialog.
  * version Opens the Version dialog.
[code]dialogs		
        dialogs textport
        
[/code]

## 

echo [-n] [-r] text

Prints text to the textport. The output will be terminated with a new line unless the -n option is used. Output can be redirected to a DAT using > or appended to a DAT using >>. A "FILE:" prefix can be used to explicitly denote a disk path. See Tscript#Redirecting Command Output to DATs to route the text to DATs and files. 

**Options:**
* -r will output alternate end-of-line characters for dos/unix conversion.
[code]# Output to textport:		
        touch -> set foo1 = bob		
        > echo $foo1		
        bob		
        # Redirect to DAT called text1:		
        echo "abc" > text1		
        # Append to a DAT called text1:		
        echo "abc" > text1		
        # Redirect to the external file C:/abc.txt:		
        echo "hello world" > FILE:C:/abc.txt
        
[/code]

## 

echolocation on|off

When echolocation is on, any echo commands executed in scripts will be preceded by the script path and line number. 

## 

else [ if (statement ) then ]

Else conditional for an if statement. 
[code] 
    set a = 1		
    if ($a == 1)		
    	echo variable a is 1		
    else		
    	echo variable a is not 1		
    endif
    
[/code]

    **See Also:**[if](<#if>) [endif](<#endif>)

## 

end

Termination of while, for and foreach statement. 
[code] 
    for i=1 to 3		
    	echo $i		
    end
    
[/code]

    **See Also:**[for](<#for>) [foreach](<#foreach>) [while](<#while>) [continue](<#continue>) [break](<#break>)

## 

endif

Termination of the if statement. 
[code] 
    set a = 1		
    if ($a == 1)		
    	echo variable a is 1		
    else		
    	echo variable a is not 1		
    endif
    
[/code]

    **See Also:**[else](<#else>) [endif](<#endif>)

## 

evar [-u] [-v] name = value

Set a system environment variable specified by name to the value given. If no name is specified, then the list of all environment variables is printed out. 

**Options:**
* -u will un-set the variable(s) specified.
  * -v will return the name of the variable if succesful.
[code]# Set environment variable:		
        evar A = 1		
        # List:		
        evar		
        # Unset:		
        evar -u A*
        
[/code]

## 

ex command arg1 arg2 ...

Prints the command and arguments to the textport first, and then executes the command. A short cut for running echo command arg1 arg2 

## 

exhelp [-k help_pattern] [expression_pattern]

Show usage for all expressions matching pattern (or all expressions if no pattern is given) 

**Options:**
* -k filter results by keyword.
[code]# List all expressions.		
        exhelp		
        # Display help for opinput.		
        exhelp opinput		
        # Display help for all expressions beginning with op.		
        exhelp op*		
        # Display help for all expressions beginning with op and		
        # containing the keyword geo.		
        exhelp -k geo op*		
        # List all expressions with geo in the help.		
        exhelp -k geo
        
[/code]


    **See Also:**[help](<#help>)

## 

exit

Exit out of a script. 

## 

exportmap [-l chop_path] [-s chop_path channel_name dest_path dest_parameter] [-a chop_path channel_name dest_path dest_parameter] [-r chop_path channel_name dest_path dest_parameter] [-c chop_path channel_name] [-C chop_path] [-y]

This command allows the user to set, list or clear entries in a CHOPs export map table. 

**Options:**
* -l Lists the current exports for the given CHOP
  * -s Sets the export for the channel.
  * -s Append the export for the channel.
  * -s Removes the export from the channel.
  * -c Clears the export(s) for the channel.
  * -C Clears all exports for the given CHOP.
  * -y Lists the current yanked channel.
[code]# List:		
        exportmap -l wave1		
        # Set:		
        exportmap -s wave1 chan1 geo1 tx		
        # Append set:		
        exportmap -a -s wave1 chan1 geo1 ty		
        # Clear Exports for chan1:		
        exportmap -c wave1 chan1		
        # Clear all exports:		
        exportmap -c wave1		
        # List yanked channel:		
        exportmap -y		
        # This command is commonly proceeded by a command to turn on the		
        # CHOPs export flag:		
        opset -o on /ch/ch1/wave1
        
[/code]


    **See Also:**[opset](<#opset>)

## 

exprrm expression_path

Removes expressions from the operators specified. Operators can be specified using pattern matching (i.e. geo*). 
[code] 
    exprm /obj/geo*/tx
    
[/code]

## 

exprset [-h] operators name1 expression

Sets expressions to the operators specified. Operators can be specified using pattern matching (i.e. geo*). 

**Options:**
* -h automatically strips off first occurance of "../". This is only necessary when importing Houdini style expressions.
[code]exprset /obj/geo* tx '$F'
        
[/code]

## 

fcur [frame]

If no frame is specified, the current frame is printed. Otherwise, the current frame is set to the frame specified. 
[code] 
    # Set current frame to frame 777.		
    fcur 777		
    # List current frame.		
    fcur
    
[/code]

    **See Also:**[fplayback](<#fplayback>) [fps](<#fps>) [frange](<#frange>) [fset](<#fset>) [ftimecode](<#ftimecode>) [timecur](<#timecur>) [timerange](<#timerange>) [timeset](<#timeset>)

## 

fieldedit path

Opens an external editor to edit the contents of a Field COMP. 

## 

filechooser [-b] [-w] [-s start_path] [-f file_filters] [-p operator_path parameter] [-v variable] [-t title] [-c] [-d datpath]

Prompts a file selection box and stores the selected path. 

**Options:**
* -b Browse for folders, not files.
  * -w Make this a write dialog, not read.
  * -s start_path Specifies which path to start the file chooser in, else opens to the current active directory. Here you can also specify a complete File name.
  * -f file_filters Wildcards used to filter file choices.
  * -p operator_path parameter Specifies an operator and parameter in which to store the result.
  * -d dat_path Trim spaces and use the first line of text in dat_path as the staring folder. Stores the result in the given DAT. Must be a text or table
  * -c returns only the folder
  * -v variable Specify a variable in which to store the result.
  * -t title Sets the title of the filechoose window.
[code]filechooser -p /obj/moviein1 file		
        filechooser -s "c:/movies/" -p /moviein1 file		
        filechooser -w -s "c:/movies/movie.mov"		
        filechooser -f "*.mov; *.mpg" -p moviein1 file		
        filechooser -v FILE; echo $FILE		
        filechooser -b -v FOLDER; echo $FOLDER		
        filechooser -c -d /dat_text1
        
[/code]

## 

filetypes [-T] [category]

List the files types that Touch accepts. Category can be one of audio, channel, component, geometry, image, MIDI, movie, object or text 

**Options:**
* -T list output in table format
[code]filetypes -T movie
        
[/code]

## 

find [-u] [-A] [-l] [-m macros] [-v variable] [-c comment] [-d data] [-t type] [-n name] [-x] [-N] [-p parm] [-f flag_value] [-r run_dat] [-e everything] [-q] [search_pattern] [operator_pattern]

This command will list all macros, variables or nodes that match the specific criteria. If no options are given, the first argument is the search term and subsequent patterns are operator patterns. If a search option is given, then all arguments are treated as operator patterns. 

## 

findpanel [-q] [-S] [-x] path [mx] [my]

Finds the child panel on a component panel. mx and my are the position of the child of the given path. By default the coordinates are assumed to be between 0 and 1. U and V for the child panel will be set after the click. 

**Options:**
* -x Give the child's coordinates in pixels instead of normalized coordinates.
  * -S Coordinates are given in screen space (both pixels and normalized).
  * -q Quiet mode, supress error and warning output messsages.
[code]# Return the child's fullpath at relative position (0.2,0.5)		
        findpanel /container 0.2 0.5
        
[/code]

## 

for variable = start to end [step inc]

The for loop construct. The variable will loop from start to end by the inc specified. 
[code] 
    for i = 1 to 3		
    	echo hello $i		
    end		
    for i = 100 to 1 step -10		
    	echo hello $i		
    end
    
[/code]

    **See Also:**[end](<#end>) [while](<#while>) [foreach](<#foreach>) [continue](<#continue>) [break](<#break>)

## 

foreach variable ( list )

The foreach loop construct. The variable will take on the value of each element in the list through each iteration of the loop. 
[code] 
    foreach i ( a b c )		
    	echo $i		
    end		
    foreach object (`execute("lc -d")`)
    
[/code]

    **See Also:**[end](<#end>) [foreach](<#foreach>) [while](<#while>) [continue](<#continue>) [break](<#break>)

## 

fplayback [-i on|off] [-r on|off] [-f factor] [-s step_size]

Sets options for the playbar. 

**Options:**
* -i on|off Turn integer frame values on or off
  * -r on|off Turn real-time playback on or off
  * -f factor Set the real time playback factor
  * -s step_size Set the non-real time frame increment


    **See Also:**[fcur](<#fcur>) [fps](<#fps>) [frange](<#frange>) [fset](<#fset>) [ftimecode](<#ftimecode>)

## 

fps [-p path] [frames_per_sec]

If no frames_per_second is specified, the current frames per second is printed out. Otherwise, the frames per second is set to the specified value. 

**Options:**
* -p Specify path to component.


    **See Also:**[fcur](<#fcur>) [fplayback](<#fplayback>) [frange](<#frange>) [fset](<#fset>) [ftimecode](<#ftimecode>) [timecur](<#timecur>) [timerange](<#timerange>) [timeset](<#timeset>)

## 

frange [-p path] [rangestart] [rangeend]

Sets or lists the working range of a time component. If no range is specified, the current frame range is printed. Otherwise, the working range is set to the range specified. 

**Options:**
* -p Specify path to component.
[code]# Set working range to 1-1500		
        frange 1 1500		
        # List current working range		
        frange		
        # Specify working range for the specified time component		
        frange -p /container1
        
[/code]


    **See Also:**[fcur](<#fcur>) [fplayback](<#fplayback>) [fps](<#fps>) [fset](<#fset>) [ftimecode](<#ftimecode>) [timecur](<#timecur>) [timerange](<#timerange>) [timeset](<#timeset>)

## 

fset [-p path] [start] [end]

Sets or lists the start-end of a time component. If no start-end is specified, the current frame range is printed. Otherwise, the working range is set to the range specified. 

**Options:**
* -p Specify path to component.
[code]# Set start to 1 and end to 1500		
        fset 1 1500		
        # List current start-end range		
        fset		
        # Specify start-end range for the specified time component		
        fset -p /container1
        
[/code]


    **See Also:**[fcur](<#fcur>) [fplayback](<#fplayback>) [fps](<#fps>) [frange](<#frange>) [ftimecode](<#ftimecode>) [timecur](<#timecur>) [timerange](<#timerange>) [timeset](<#timeset>)

## 

ftimecode [timecode]

If no timecode is given, the current frame is printed in timecode format. Otherwise, the timecode specified is set. 
[code] 
    # Set timecode to 0 hours, 0 minutes, 10 seconds and 12 frames		
    ftimecode 00:00:10:12
    
[/code]

## 

geoimport [-g geofiledir] [-a animfiledir] [-t texturefiledir] [-l 0|1] [-c 0|1] [-m 0|1] [-d 0|1] [-f fps] filename destcomp

Import a geometry file to the specified network component. You can use variables in the target file directories. (prefix the variables with \ to avoid it getting expanded) These variables are evaluated relative to the desination COMP. As we don't know what nodes need to be created to import the file, the destination COMP must be be empty. 

**Options:**
* -g Geometry (.tog) files will be created in this directory. If this option is missing, geometry won't be imported.
  * -a Animation (.bchan) files for animation will be created in this directory. If this option is missing, animations won't be imported.
  * -t Texture files (.jpeg, .tiff etc.) will be created in this directory. If the texture files arn't embeded in the .fbx file, you should place the textures in this directory.
  * -l 0 to not import lights, 1 to import lights. If this option isn't specificed, lights will be imported.
  * -c 0 to not import cameras, 1 to import cameras. If this option isn't specificed, cameras will be imported.
  * -m 0 to not merge geometry, 1 to merge geometry. If this option isn't specificed, geometry will be merged. Geometry can be merged when the geometry is static, and shares materials with another geometry. Less SOPs results in faster rendering, so merge geometry whenever possible.
  * -d 0 to create Deform SOPs to deform geometry, 1 to use the deform feature in MATs to deform the geometry (GPU based deforms). If this option isn't specified, MATs will be used to


deform. 
* -f This option will specific what FPS to create the animation data in. If this option isn't specified then $FPS will be used.
[code]geoimport -g \$TOUCH/importdir/geo -t \$TOUCH/importdir/image		
        C:/test.fbx /geo1
        
[/code]

## 

help [-k] [-d dialog] [-o operator] [command_pattern]

With no arguments, the list of all commands is printed out. If a pattern is specified, the complete help for the commands is printed out. 

**Options:**
* -k Search by keyword. All command help matching the patterns will be output.
  * -d Launch the on/offline page for a specific dialog.
  * -o Launch the on/offline page for a specific operator.
[code]# Print out all commands that start with "op"		
        help op*		
        # Launch the on/offline page for the Movie In TOP		
        help -o top/moviein
        
[/code]


    **See Also:**[exhelp](<#exhelp>)

## 

hidewindows

This command will minimize all the visible Touch windows except for the main one. 

## 

history [-c]

Print the command history. 

**Options:**
* -c the command history is cleared.

## 

if (condition) [then]

The if construct. If the condition is met, then the contents of the if statement will be executed. 
[code] 
    set a = 1		
    if ($a == 1)		
    	echo variable a is 1		
    else		
    	echo variable a is not 1		
    endif
    
[/code]

    **See Also:**[else](<#else>) [endif](<#endif>) [exit](<#exit>)

## 

include dat_node_path

Execute the contents of a DAT node in the current path. Behaves the same as run -c. See run Command. 

## 

inline dat_node_path

Include the contents of a DAT node at the current script location. Unlike include, or run, no local variables will be saved or restored before executing inline. Similarly, this command takes no arguments. 

## 

keyframe [-c] [-e tolerance] path1 path2 ...

keyframe [-a 

**Options:**
* -c Convert a CHOP into a series of keyframe tables for further editing.
  * -e Specify the error tolerance during conversion. (default 0.1, minimum 0.001).
  * -a Add a keyframe.
  * -d Delete a keyframe.
  * -v Set a keyframe value.
  * -p Modify picked channels
  * -n chan_pattern Specify channels to modify
  * -t time Specify time
  * -l List channels.
[code]# Convert a CHOP:		
        keyframe -c /wave1		
        # Add keyframes:		
        keyframe -a -t 0.5 -n t* /keyframe1		
        # Add and set:		
        keyframe -a -v 5 /keyframe1		
        # Delete keyframes:		
        keyframe -d -t 0.5 /keyframe1		
        # Set keyframes:		
        keyframe -v 2 -t 0.5 -n tx /keyframe1		
        # List channels		
        keyframe -l *  /keyframe1
        
[/code]

## 

kinecttilt -d degrees nodes

Controls the tilt of the Kinect sensor selected by the specified nodes. The tilt is expressed in degrees and is relative to gravity. That means that a tilt of 0 is horizontal to the ground, not horizontal to the surface the sensor is sitting on (which may not be flat). The Kinect sensor tilt motor is not intended to be used for continuous motion and will start ignoring commands for a while if asked to move too much (more than 15 times in 20 seconds usually). 

**Options:**
* -d The degrees of tilt to set to the sensor(s) to. A negative number will aim it downwards.

## 

lc [-a] [-d] [-l] [-T] [-R] [-s] [-x] [-y] [operator_pattern]

Lists the operators specified (or all the operators in the current component). 

**Options:**
* -a Print all operators (including hidden ones)
  * -d Do not print contents of networks
  * -R Recurse through all networks and sub-networks
  * -l Print in "long" format.
  * -T Print in table format. (use with -l)
  * -s Sort names alphabetically.
  * -y Sort names by Node Y position.
  * -x Sort names by Node X position.
[code]lc -l -R geo*		
        lc -l -T geo1		
        lc -d /*/*/*
        
[/code]

## 

ld

Print the list of available logical drives. 

    **See Also:**[cf](<#cf>) [Command](<#Command>) [lf](<#lf>) [Command](<#Command>) [mf](<#mf>) [Command](<#Command>) [pf](<#pf>) [Command](<#Command>)

## 

lf [-b] [-d] [-f] [-s] [-t] pattern

List the contents of the current working directory on disk. 

**Options:**
* -b List only the filename base.
  * -d List only directory folders.
  * -f List only files.
  * -s Sort the files.
  * -t Output the timestamp and date.

## 

loadcomponent [-u] [-v] [-d] filename [pattern]

This will load the component filename into the current component. 

**Options:**
* -u leave the nodes inputs unwired.
  * -v return the name(s) of the new node(s) created.
  * -d run the destination drop script of the component.
[code]loadcomponent -v c:/test.tox		
        loadcomponent -v c:/test.tox icon1 help1		
        # To get the name of the new component:		
        set NEWNAME =`execute("loadcomponent -v mv1.tox")`[/code]


    **See Also:**[savecomponent](<#savecomponent>) [cc](<#cc>)

## 

macro [-p path] [-u] [-l] [-s] macro_name [command]

This command is used to manage Macros. This includes listing, setting, and un-setting macros. A macro is a single word that, when typed in the Textport or used in a script, will run a script for that macro. You can pass arguments to a macro. Macros can be defined for any component. A path can be specified with any options. If no path is specified, the current component is used. Macros defined at a particular component are accessible by all children and sub-children of that node. Thus, macros defined at the root level are accessible by all nodes. Note that when listing macros, wildcard patterns can be used. See also Macros Dialog. 

**Options:**
* -p path Specified component macros.
  * -u Unset a macro.
  * -l List the location of a macro.
  * -s List the script contents of a macro.
[code]# To set a macro in the current component:		
        macro greet echo Hello World.		
        # To execute that macro:		
        greet		
        # To unset the macro:		
        macro -u greet		
        # To set the macro at the root component:		
        macro -p / greet echo Hello World.		
        # Alternatively:		
        cc / ; macro greet echo Hello World.		
        # To unset the macro at the root component:		
        macro -p / -u greet		
        # To list all macros accessible from the current location:		
        macro		
        # To list all macros accessible from the current location		
        beginning with g:		
        macro g*		
        # To find the location of the closest greet macro:		
        macro -l greet		
        # To list the contents of the closest greet macro:		
        macro -s greet
        
[/code]

## 

mark [start|stop] label

Use this command to time portions of your scripts. Time usage is appended to the performance monitor, when a batch measurement is taken. 
[code] 
    mark start Testing Loop Speed		
    for i = 1 to 1000		
    	echo $i		
    end		
    mark stop		
    # Note these commands can be nested.
    
[/code]

## 

memory [options]

Show the current GPU memory usage by TOPs 

**Options:**
* -m Only shows entires for TOPs that have allocated some memory.
  * -T Output tab delimited table format.

## 

mf path [path2 path3 ...]

Make a folder inside the current working folder. Multiple nested folders can be specified at once. 
[code] 
    mf totals1	
    mf pics1/january pics2/january
    
[/code]

## 

midi [-l 01] [-q] [-d _device_path_] [-i _id_] [-n _channel note value_] [-o _channel note value_] [-t _channel controller value_] [-p _channel program value_] [-h _channel pressure value_] [-f _channel note pressure_] [-g _raw1 raw2 raw3_] [-a [-c _channel_]

This command sends various MIDI messages to the output id specified in the map table DAT. Note in the case of commands requiring three parameters, the first two parameters are 1-based, while the last is zero-based. In the case of the raw output, all parameters are zero based. If no map path is specified /local/midi/map is assumed. If no id is specified "1" is assumed. 
[code] 
    # List MIDI output devices:		
    midi -l 0		
    # List MIDI input devices:		
    midi -l 1		
    # Send Note On: Channel 1, Note 60, Velocity 127:		
    midi -n 1 60 127		
    # Send Note Off: Channel 1, Note 60:		
    midi -n 1 60 0		
    # Send Note Off on map id 2:		
    midi -i 2 -n 1 60 0		
    # Send Note Off: Channel 1, Note 60, Velocity 127:		
    midi -o 1 60 127		
    # Aftertouch: Channel 1, Note 60, Pressure 30:		
    midi -f 1 60 30		
    # Send Control Change: Channel 1, Controller 2, Value 0:		
    midi -t 1 2 0		
    # Send Program Change: Channel 1, Program 2, Value 0:		
    midi -p 1 2 0		
    # Send Channel Pressure: Channel 1, Pressure 2, Value 0		
    midi -h 1 2 0		
    # Send untranslated raw bytes: 12 34 56 (Useful for general MIDI		
    # messages of any type.):		
    midi -g 12 34 56		
    # Turn off all notes:		
    midi -a		
    # Turn off all notes on channel 5:		
    midi -a -c 5
    
[/code]

    **See Also:**[MIDI](<#MIDI>) [In](<#In>) [DAT](<#DAT>) [MIDI](<#MIDI>) [Event](<#Event>) [DAT](<#DAT>) [MIDI](<#MIDI>) [In](<#In>) [Map](<#Map>) [CHOP](<#CHOP>) [MIDI](<#MIDI>) [In](<#In>) [CHOP](<#CHOP>) [MIDI](<#MIDI>) [Out](<#Out>) [CHOP](<#CHOP>)

## 

moviedump [opnames...]

This command prints info for all the Movie In TOPs in the synth. You can optionally give a list of TOP names to print. The 
* symbol can be used as a wildcard on the names, such as movie*1


to get all movies names ending in 1. 

## 

neteditor [options] -p pane

Allows different options of the network editor to be set. A valid Pane name must be specified. See also the desk Command. 

**Options:**
* -c 0|1 Display the color palette
  * -e 0|1 Display expose flag in list mode
  * -t 0|1 Display backdrop TOPs
  * -d 0|1 Display backdrop CHOPs
  * -g 0|1 Display backdrop geometry
  * -n 0|1 Display operator names
  * -o 0|1 Display the network overview
  * -P <float> The split fraction for parameters
  * -r 0|1 Display parameters
  * -s 0|1 Toggle connection style (direct or not)
  * -v scale tx ty Set the network scale and offset in the Pane
  * -h path Set the above for a specific network
  * -w 0|1 Toggle mode (worksheet or list)
  * -p pane Specify pane
  * -N network Specify network component

## 

netscope -p path [-h homenode] [-n name] [-v]

This command will open a network editor in a floating pane. If no name is specified, a new pane with a unique name is created. If a name is specified, current existing panes are searched first. If none are found, a new pane with that name is created. That is, executing this command multiple times, specifying the same name, will always return the same window. Also note that specifying the name, affects both the window title bar as well as the name of the floating pane it creates. Be sure to not specify existing non-floating desktop panes. 

**Options:**
* -p Specify the path to open
  * -h Specify the child in the network to home onto.
  * -n Specify the name of the window.
  * -v returns the name of the pane that was opened.
[code]netscope -p /project1		
        netscope -p /project1 -n Results
        
[/code]

## 

objparent [on|off]

With no arguments, the command prints the state of the "Keep Position when Parenting" option. With an argument, the command will set the option to be on or off. Objects which are re-parented (using opwire) when the option is turned on will maintain their world space position. 

## 

opadd [-n] [-v] type [name] [name2...]

If no arguments are specified, all valid operators are listed. If the type is specified, an operator of that type will be added. If a list of names is entered, operators will be created and given the names specified. The format for type is <nodefamily>:<nodetype>. I.e TOP:constant, or CHOP:math. 

**Options:**
* -n prevents the "initialization" script from being run.
  * -v output the actual name of the new Operator.
[code]# Create two Geometry COMP objects called arms and legs:		
        opadd COMP:geo arms legs		
        # To get the name of the new node:		
        set NEWNAME =`execute("opadd -v COMP:geo")`[/code]

## 

opchange [-s] from_pattern to_pattern

This will search all operators for the from_pattern. If the pattern is found, it will be replaced with the to_pattern. All parameters of all operators will be searched for the pattern. The opchange command normally reports changed references, however if the -s option is specified then the command operates silently without reporting results. 

**Options:**
* -s don't return results.
[code]# Change the word plastic to the word constant wherever it is	found.		
        opchange plastic constant
        
[/code]


    **See Also:**[find](<#find>)

## 

opchangetype [-v] node_pattern type

This will change the operator type of all specified nodes. 

**Options:**
* -v Outputs any errors or results.
[code]opchangetype /geo1 COMP:null		
        opchangetype /button* COMP:slider
        
[/code]

## 

opcolor [-s] [-c r g b] nodes

Without the -c option this will print out the color for the operator(s) specified. If the -c option is specified, the color for the operators will be set to the space separated "r g b" values between 0 and 1 

**Options:**
* -s Output in script format.
[code]opcolor -c 0.5 0 0.5 geo1
        
[/code]

## 

opcomment [-c comment_string] nodes

Without the -c option the opcomment command will print out the comment for the operator(s) specified. If the -c option is specified, the comment for the operators will be set to the comment_string. 

**Options:**
* -c Set the comment for the specified operator.
[code]opcomment -c 'This is a comment\nwith a new line' geo*
        
[/code]

## 

opcompinput [-r compinput newindex] operator

Modifies COMP inputs 

**Options:**
* -r compinput newindex Will reorder COMP inputs. It will move compinput to be located at newindex. compinput can either an index or the name of the COMP input. newindex must be an index.

## 

opcook [-a 0|1] [-F] [-f start end] [-i frame_inc] [-v] [-r] [q] path

This will force the object to recook for the frame range specified. If no frame range is specified, the object will re-cook for the current frame. 

**Options:**
* -v cook verbosely.
  * -q quiet (suppress errors).
  * -F force the OP to cook even if a cook is not required.
  * -r recursively cook all the children of the specified objects.
  * -a 0|1 recursively allow(disallow) cooking.
  * -f start end Cook over the specified frame range.
  * -i inc Specify increment for frame range.
[code]opcook -F /project1/moviein1
        
[/code]

## 

opcookpriority [-p priority] operator_pattern

A few special nodes support controlling when they cook compared to other nodes. These nodes are generally only nodes that cook at the start/end of a frame. 

**Options:**
* -p priority Set the cook priority value. If this isn't specified then the priority will be printed out.

## 

opcopy [-e] [-i] [-o] [-d] operator

This command is similar to the UI operation of copying/paste. However, the command will also copy all operators which the given operator depends on. If no options are specified, all outputs are copied as well. Outputs consist of all the nodes which the specified operator feeds into. For example, in the Object editor, these would be the children of the object (and their SOPs). The operators are copied to a temporary file and must be pasted back with oppaste. 

**Options:**
* -i Copy the input nodes to the operator as well
  * -o Copy the output nodes of an the operator as well
  * -e Copy "extra" nodes as well. Extra nodes are ones which are referenced indirectly (i.e. via an expression).
[code]opcopy /obj/geo1		
        oppaste /obj
        
[/code]


    **See Also:**[opcp](<#opcp>) [opdepend](<#opdepend>) [oppaste](<#oppaste>) [oprm](<#oprm>)

## 

opcp [-a] [-v] [-q] operator1 [operator2...] destination

This will copy the operators specified. If the destination ends with a /, the node(s) will be copied into the destination component with their original names. If the destination does not end with a / then the destination is the path name of the new node. Specifiying a destination of . means copy the nodes into the current component using their original names. If the destination component does not exist the operation will fail. If a node of the same name as the target name already exists, the operation will fail, unless the -a option is used. 

**Options:**
* -v return the name of the created node.
  * -a cause nodes to be automatically renamed if a node that matches their target name already exists.
  * -q suppress (quiet) all errors.
[code]opcp geo* .		
        opcp /obj/geo1/* /obj/geo2/		
        opcp geo1 fred		
        # To get the name of the new node:		
        set NEWNAME =`execute("opcp -v $NAME .")`[/code]


    **See Also:**[opcopy](<#opcopy>) [opname](<#opname>) [oppaste](<#oppaste>) [oprm](<#oprm>)

## 

opcreate [-b] [-e] [-l] [-p type pane]

This method controls interactive OP creation. 

**Options:**
* -b Only display basic operators in the OP Create menu.
  * -e Display basic and expert operators in the OP Create menu.
  * -l Display the current operator visibility level.
  * -p Select an operator for placement in the given pane.
[code]opcreate -e		
        opcreate -p CHOP:math pane1
        
[/code]

## 

opdepend [-b] [-i] [-t] [-o] [-e] [-p] [-s] [-l level] node

This will list all of the operators that are either dependent on this object or that this object depends on. 

**Options:**
* -b the output only specifies the nodes
  * -l Which level to descend to in the hierarchy
  * -i lists all ops that are inputs to the node
  * -o lists all ops that are outputs of the node
  * -e lists all extra (reference) inputs to the node (for example a moviein top that references a DAT for its source image).
  * -p select the nodes specified
  * -s silent mode - no output to the textport
  * -t lists only time dependent inputs
[code]opdepend -i -e  /comp/blue_plastic		
        opdepend -i -o -e /obj/geo1		
        opdepend -i -p -s /obj/logo
        
[/code]

## 

opdock -[d parent] [-u] node

This command docks and undocks a node. Docking a node ties them together so that a docked node will be moved, copied, or deleted along when those operations are applied to its parents. Visually, docked nodes show up as a small flag under the parent node in the network editor. 

**Options:**
* -d Specifies a parent to dock to. The parent must be in the same network.
  * -u Undocks a node from its parent.
[code]opdock -d ramp1 table1
        
[/code]

## 

operror [-l] [operator_pattern]

This command recursively lists all errors starting at the specified path, echoing errors to the textport. If no path is given, the search begins at the root component. 

**Options:**
* -l Only search the listed nodes.


    **See Also:**[opexprerror](<#opexprerror>)

## 

opexprerror [-l] [-v] [-e] [-p pattern] [operator_pattern]

This command recursively evaluates every parameter starting at the specified path, echoing any evaluation errors to the textport. If no path is given, the search begins at the root component. 

**Options:**
* -l Only search the listed nodes.
  * -v Output the value of each parameter.
  * -e Output the expression of each parameter.
  * -p pattern Only search parameters matching the pattern.


    **See Also:**[operror](<#operror>)

## 

opfamilies

Lists all operator family types (DAT, COMP, SOP, TOP, CHOP, MAT, etc.). 

    **See Also:**[optypes](<#optypes>) [opparinfo](<#opparinfo>) [oppars](<#oppars>) [oppardetails](<#oppardetails>)

## 

opfiles [-p parm_pattern] paths...

This command is used to recursively list externally referenced files. 

**Options:**
* -p Specify a parameter selection.
[code]# List all referenced files.		
        opfiles		
        # List all referenced files in components matching comp* or geo*,		
        # in parameters matching *file*.		
        opfiles -p *file* comp* geo*
        
[/code]

## 

opgetinput [-n num | -o outputop] inputop

With the -n option, this function returns the name of the node that is attached to input num of the inputop. It returns the empty string if no input is attached to the given input. With the -o option, this function returns the input number of the inputop that is connected to the outputop. If the outputop is not connected to the inputop, -1 is returned. If the outputop is connected to more than one input of the inputop, the highest input number is returned. 

**Options:**
* -n num return the name of the node that is attached to input num of the inputop.
  * -o outputop return the input number of the inputop that is connected to the outputop.

## 

opglob operator_pattern

Does pattern expansion on the given pattern, then prints the output of the expansion. 

    **See Also:**[expandpattern()](<#expandpattern\(\)>)

## 

opgrid [-C] [-a] [-r num] [-c num] [-x startx] [-y starty] [-s sepx sepy] operator_pattern

Layouts the specified operators in the network view in a grid according to their numerical suffix. If there is no suffix a node is not moved. 

**Options:**
* -C Position the node from the node center
  * -a Order specified nodes by alpha numeric sort order
  * -x Specifies the starting X position. Default is 0.
  * -y Specifies the starting Y position. Default is 0.
  * -s Specifies the spacing for the nodes. Default is 200 horizontally and 100 vertically
  * -r Specifies the number of nodes in a row. Default is 10
  * -c Specifies the number of nodes in a column. Row layout is used unless this option is specified
[code]# layout all geo operators in a grid according to defaults:		
        opgrid geo*		
        # layout geo13 in the 3rd position of the 3rd column in a grid		
        # that starts at 1000,0 and each node center is separated by 200 pixels:		
        opgrid -C -c 5 -x 1000 -s 200 200 geo13
        
[/code]

## 

opinfo [-l] operator [operator2...]

Displays information about the operator, including the comment. 

**Options:**
* -l list info attributes associated with the operator.

## 

oplayout [-s] [network1 network2...]

Lays out the current network if no network paths are given. Otherwise lays out the given networks. 

**Options:**
* -s layout selected operators only.

## 

opload [-v] operator filename

The specified operator is loaded with the contents of the specified filename. It is best to lock the operator before loading data. Currently CHOP, SOP, TOP and DAT data are supported. Furthermore, CHOPs only allow oploading of the .clip format. 

**Options:**
* -v causes verbose output.
[code]opload /ch/ch1/wave1 wave.clip
        
[/code]


    **See Also:**[opscript](<#opscript>) [opwrite](<#opwrite>) [toewrite](<#toewrite>) [opsave](<#opsave>)

## 

oploadondemand [node_pattern]

This command is used to query whether a COMP that is load-on-demand has loaded it's contents or not. If you don't list any nodes, it will list every COMP in the system that is load-on-demand, but hasn't loaded it's contents yet will be listed. If you list nodes in the command, the subset of those listed nodes that still have load-on-demands pending will be listed. 

## 

oplocate [-C] [-d] [-s] [-x xval] [-y yval] [-w wval] [-h hvall] operator_pattern

Locates the specified operators in the Network. The center gridlines of the network is 0, 0. This is independent of any "scrolling" that has been done in the Network Editor. 

**Options:**
* -d The -x and -y specified are deltas and are added to the current location
  * -C Specifies the X, Y position from the node center
  * -x Specifies the X position
  * -y Specifies the Y position
  * -w Specifies the width
  * -h Specifies the height
  * -s Output in script format

## 

opname [-f] [-v] [-a] [-I] operator new_name

Renames the specified operator to the new name. 

**Options:**
* -f can be used to speed up renaming of large components, when its known to not have any external references or dependencies.
  * -v returns the name of the renamed node.
  * -a causes the node to be automatically renamed if a node that matches the target name already exists.
  * -I causes clone immune nodes that match this node to also be renamed.

## 

oppardetails [-d] [-n] [-l] [-t] [-p path] [family_group operator_type] [paramater_name]

This command will output a tab delimited text of all the attributes of the specified parameter. If not parameter is specified, all parameters are outputted. In the case of dynamic menu content, a node can be specified. This is useful for cases in which menu contents are specific to a node. 

**Options:**
* -l will output only the label field
  * -d will output only the dimension field
  * -n will output only the name field
  * -t will output only the type field
  * -p used to specify a node, in which case the family_group and operator should be omitted.
[code]oppardetails CHOP math		
        oppardetails CHOP math scope		
        oppardetails -p /project1/math1		
        oppardetails -p /project1/math1 scope
        
[/code]


    **See Also:**[optypes](<#optypes>) [opfamilies](<#opfamilies>) [opparinfo](<#opparinfo>) [oppars](<#oppars>)

## 

opparinfo [-e] [-v] [-d] [-x] [-s] [-o][-n] path parameter [index]

Will list all specific details of a particular parameter. 

**Options:**
* -e will output only the enable state.
  * -v will output only the visible state.
  * -d will output only the default state.
  * -x will output only the expression.
  * -s will output only the string value.
  * -o will output only the override information.
  * -n will output only the numeric exportability information.
[code]opparinfo /moviein1 tstart		
        opparinfo /project1 t 2		
        opparinfo /project1 tz		
        opparinfo -e /project1 tx
        
[/code]


    **See Also:**[optypes](<#optypes>) [opfamilies](<#opfamilies>) [oppars](<#oppars>) [oppardetails](<#oppardetails>)

## 

opparm [-p] operator_pattern parameter_name ( value(s) ) [parameter_name ( value(s) ) etc.]

This will set parameters for the given operator. The parameters are operator-dependent and thus are different for each operator type. The names used to reference parameters are not the names visible on the parameter page but rather special internal names. You can find the internal name for each parameter by holding your mouse over the parameter name and looking at the popup box. The first word listed is the internal name of the parameter. Or you can use commands such as opscript to see all of the internal parameter names of a node (as well as their current values). If the parameter contains multiple values, like Translate, you can give multiple values in ( )s. Or alternatively you can set each individual value using the parameter specific suffix. So for transforms, x, y and z refer to the first second and third value in the parameter. In the case of buttons, simply specify the parameter name for the button and it will behave as it was pressed and released. 

**Options:**
* -p This will pulse the parameters to the specified values, cook the node, and then return them to their original values. Useful in particular parmeters like Reset that is in many OPs, such as the Movie In TOP.
[code]# Set translate to (1, 2, 3)		
        opparm geo1 t ( 1 2 3 )		
        # Set tx to $F, in all geo* nodes		
        opparm geo* tx '$F'		
        # Set two parameters in the same command		
        opparm geo1 tx ( 5 ) sz ( 0.7 )		
        # Pressed the menu-button parameter using the initfill entry		
        opparm /project/creep1 initialize initfill		
        # Pulse the Reload parameter of the moviein1 TOP.		
        opparm moviein1 reload ( 1 )		
        # Press the Edit Keyframes button		
        opparm keyframe1 editkeyframes
        
[/code]


    **See Also:**[parmls](<#parmls>) [saveallparms](<#saveallparms>)

## 

oppars family_group operator_type

Will list all parameters of the given operator. 
[code] 
    oppars COMP geo
    
[/code]

    **See Also:**[optypes](<#optypes>) [opfamilies](<#opfamilies>) [opparinfo](<#opparinfo>) [oppardetails](<#oppardetails>)

## 

oppaste network

This command will paste the data copied by opcopy into the network specified. It is not possible to choose the name of the operator being pasted. 

    **See Also:**[opcopy](<#opcopy>) [opcp](<#opcp>) [opdepend](<#opdepend>)

## 

opplace [-d] [-p pane] [-i compin] [-o compout] [-n op_name] node1 [node2...]

This method controls interactive OP placement from existing nodes. 

**Options:**
* -d delete the parent of the nodes
  * -p select an operator for placement in the given pane
  * -i index of component input (first node is a component)
  * -o index of component output (last node is a component)
  * -n name for the operation for undo purposes
[code]opplace -p pane1 -i 0 -o 1 container1 container2
        
[/code]

## 

opread filename

Read the contents of the file into the current directory (cc). The file specified should have been created by the opwrite command. 

    **See Also:**[opwrite](<#opwrite>) [opscript](<#opscript>) [cmdread](<#cmdread>) [opload](<#opload>)

## 

oprecook

This command flags all operators as dirty, which will cause them to recook the next time they are accessed. 

    **See Also:**[opcook](<#opcook>)

## 

oprm [-f] [-I] operator_pattern

The specified operators will be deleted. 

**Options:**
* -f Will prevent error messages from being printed.
  * -I Will cause clone immune nodes that match the deleted node(s) to also be deleted.

## 

opsave [-v] [-a] [-f start end] [-i inc] operator filename

The data generated by the operator specified will be saved out to the filename specified. Currently CHOP, SOP, TOP and DAT data are supported. When you include time variables in the filename, make sure to put them in single quotes so they do not get expanded as part of the command line. 

**Options:**
* -v Verbose output.
  * -a Append. Use this option when writing out DAT txt files, to append to the end of the existing file. This option can be used to create a file logging function.
  * -f Speficy a frame range. The data will be written out for each frame.
  * -i Specify an increment with the frame range.
[code]opsave \top\blur1 blur.bmp		
        opsave \ch\audio\filter1 test.aiff		
        opsave -a \dat1 log.txt		
        opsave \ch\ch1\wave1 wave.bclip		
        opsave -f 1 10 -i 2 twist1\twist1 '$F.tog'
        
[/code]


    **See Also:**[opscript](<#opscript>) [opwrite](<#opwrite>) [toewrite](<#toewrite>)

## 

opscript [-r] [-m|-g] [-b] [-v|-c] [-s] operator_pattern

For the specified operator, this will echo the commands necessary to re-create the operator. 

**Options:**
* -r Work recursively through the whole operator hierarchy.
  * -g Top level arguments will be in "general" form. i.e. the names will have to be specified when sourcing the script file.
  * -b (brief) The values for parameters at their default values will not be printed.
  * -v Causes channel values to be evaluated and no channel information to be printed.
  * -c Causes only the channels for the specified operators to be output (overrides -v).
  * -s Output channel and keyframe times in samples (frames) instead of seconds.
[code]opscript -r /obj/geo*
        
[/code]


    **See Also:**[opwrite](<#opwrite>) [opsave](<#opsave>)

## 

opset [-q] [-R] [flag on|off]... operators...

The opset command turns various operator flags on or off. The -q option will cause no messages to be printed on an unknown flag or operator. 

**Options:**
* -d Display
  * -r Render
  * -v Viewer
  * -a Active Viewer
  * -l Lock
  * -p Set the "picked" flag
  * -C Set to be the "current"
  * -t Template
  * -f Compare
  * -o Export (CHOPs and DATs only)
  * -b Bypass
  * -e Expose
  * -k Make pickable (COMP only)
  * -c Allow/Disallow cooking (recursively)
  * -i Immune to cloning
  * -n Set COMP and it's contents immune to cloning
  * -D Shows and hides docked nodes. It only has an effect on nodes that have been docked.
  * -z Language (0=python, 1=tscript)
  * -R Apply the flag changes recursively to all children.
[code]opset -d on geo*		
        opset -p off light*		
        opset -l hard -d on geo*/*
        
[/code]

## 

opstats [-u] [-a] [-d] [-c] [-T] [-p path] [family1 family2...]

This command reports statistics on the current operators. By default it'll report the number of each type of OP that is used in the synth. OPs that arn't used won't be listed. 

**Options:**
* -u List all unused operators.
  * -a List all operators.
  * -c Don't include the count in the output.
  * -T Output tab delimited table format.
  * -p Only include nodes starting from this path.
  * -d Display the total number of parameters and the total number which are set to default values.
  * type Only include operators from the listed operator families
[code]opstats -a		
        opstats -c CHOP		
        opstats -p /project1		
        opstats -d
        
[/code]

## 

optypes [-v] family_group [pattern]

Lists all operators within a given family group. Outputs additional details per operator in a tab delimited format. 

**Options:**
* -v Will only list OPs that are visible depending on the state of the Expose Expert Nodes option.
[code]optypes CHOP		
        optypes SOP a*
        
[/code]


    **See Also:**[opfamilies](<#opfamilies>) [opparinfo](<#opparinfo>) [oppars](<#oppars>) [oppardetails](<#oppardetails>)

## 

opunwire [-a] object inputnumber [inputnumber...] [-i compinput...]

Disconnects inputs from a node. The inputnumber specifies the number of the input to unwire (starts at 0). 

**Options:**
* -i signify a COMP input.
  * -a will disconnect all inputs and outputs from a node, including component inputs and outputs.
[code]# Disconnects the input from the Box SOP.		
        opunwire box1 -0		
        # Disconnects inputs 1, 3, and 5 from the Merge SOP.		
        opunwire merge1 -1 -3 -5		
        # Disconnects input 0, and component input 1 from geo1.		
        opunwire geo1 -0 -i 1		
        # Disconnects component input named in5 from geo1.		
        opunwire geo1 -i in5		
        # Disconnects all connections to geo1.		
        opunwire -a geo1
        
[/code]


    **See Also:**[opwire](<#opwire>)

## 

opwire [-s] [-o compoutput] from_object [-inputnumber | -i compinput] to_object

Wires the output of one node to an input of another node. 

**Options:**
* -inputnumber specifies the input number, starting at 0.
  * -i compinput specifies that we are connecting to a COMP input
  * -o compoutput specifies that we are connecting from a COMP output
  * -s output a script
  * -h instead of replacing an input, this option inserts the input, shifting other inputs to higher input numbers.
[code]# Connect twist1 to the first input of box1.		
        opwire twist1 -0 box1		
        # Connect box1 to the first input of merge1, box2 to the second		
        # input of merge1. It is recommended that for multiple input OPs		
        # like the merge SOP that the inputs are filled up consecutively.		
        opwire box1 -0 merge1 ; opwire box2 -1 merge1		
        # When using -i, you can specify either the COMP input number, or		
        # the name of the In Operators (In CHOP, In TOP, etc.) to make the connection.		
        opwire -o out1 componentA -i in1 componentB		
        # The name of the COMP input is the name of the In OP that the		
        # COMP input is related to. This is all also true for -o. (note:		
        # You are connecting to the component inputs of a COMP, instead of		
        # the connections on the top of the COMP, which defines the 3D		
        # Parenting).Connect moviein1 to the 2nd COMP input of container1.		
        # If the input doesn't exist, or the input isn't the same node type		
        # as moviein1, the connection will fail.		
        opwire moviein1 -i 1 container1		
        # Connect moviein1 to whichever COMP input in5 is in container2.		
        # in5 isn't nessesarily the 5th input.		
        opwire moviein1 -i in5 container2		
        # Connect from the COMP output of container2 named out2, to the		
        # first input of null1.		
        opwire -o out2 container1 -0 null1		
        # Output a script of all geo1's wire connections (including		
        # component inputs and outputs).		
        opwire -s geo1
        
[/code]


    **See Also:**[opunwire](<#opunwire>)

## 

opwrite operator [operator2...] filename

Saves the contents of the operators into the file specified. This is a partial motion file write. The contents are stored in .cpio format and are reloadable into networks of the same type. Such files may be read back in using the opread command. 
[code] 
    opwrite geo* geometry.cmd		
    opwrite dome1 particle1 rainstorm.cmd
    
[/code]

    **See Also:**[opread](<#opread>) [opsave](<#opsave>) [opscript](<#opscript>) [toewrite](<#toewrite>)

## 

opyank parameter_path

This command will yank the current values of the specified parameter into the global yank buffer. This is equivalent to manually selecting "Yank Values" on the parameter menu choices. 
[code] 
    opyank /moviein1/interpolation
    
[/code]

## 

palette

Open the palette browser. 

## 

paramset token val

This will set the global value of parameter token to val. Issuing this command with no arguments will list all current parameters. 

## 

parmls [-v varname] [-s] [-e] node [pattern]

Echo the current values of a node. 

**Options:**
* -e will only list added extra parameters.
  * -s will list in a short format (ie only the value)
  * -v will specify a varname the output will be saved to. Use this option to avoid results being evaluated in scripts.
[code]parmls /geo1 ty		
        parmls /geo1 t*		
        parmls /geo1		
        parmls -s /geo1 ty		
        parmls -e /geo1		
        parmls -e /geo1 spare*		
        parmls -v var1 /geo1 ty
        
[/code]


    **See Also:**[opparm](<#opparm>) [saveallparms](<#saveallparms>)

## 

parse [-i on|off] [-q on|off] [-v on|off] [-e on|off]

This command will set script parsing options. 

**Options:**
* -i on|off Use this option to optimize the parsing of scripts by ommitting the evaluation of all commands between non-executed if/else/endif statements.
  * -q on|off This setting will strip all double quotes from all arguments. Use this option when dealing with complex quoted instructions.
  * -v on|off This setting will optionally report information about every line executed. This information includes: 
    * path to the current working component
    * current path to the DAT or file being executed, including 
      * line
      * current line being executed
  * -e on|off This setting will output the script name and line number before all echo output. Use this to locate errant echo statements.
[code]parse -v 1		
        echo $F		
        parse -v 0
        
[/code]

## 

pc

Print the current working component. 
[code] 
    lc, cc
    
[/code]

## 

performance [options]

Change parameters for the performance monitor. 

**Options:**
* -c on|off Set Monitor OP Cook toggle.
  * -x on|off Set Monitor OP Export toggle.
  * -o on|off Set Monitor Object Display toggle.
  * -v on|off Set Monitor Viewport Display toggle.
  * -m on|off Set Monitor MIDI toggle.
  * -f on|off Set Monitor Frame Length toggle.
  * -i on|off Set Node Statistics in OP Info toggle.
  * -h on|off Set Node Hilight when Cooking toggle.
  * -p on|off Set Pause toggle.
  * -e on|off Set Enable Output toggle.
  * -a Start analyzing, this is the same as pressing the analyze button.

## 

pf

Print the path of the current disk folder. 

## 

play [options]

Controls the play bar. The play command is obsolete. Use command: power. 

**Options:**
* -s Stop playing
  * -l Set loop mode on
  * -1 Play one time only

## 

playback [-p path] [options]

Controls the playback of the playbar. Path to a specific time component can be specified using the -p option. 

**Options:**
* -p specify path to component
  * -s stop playback
  * -f play forward
  * -r play reverse
  * -l play looping
  * -o play once through

## 

pointgrouplist operator_pattern

This will output a list of all the point groups in all the specified SOPs. 

## 

power [0|1]

Controls execution of all elements. If no arguments are, the current state is returned. 

## 

preference [-w] [-d] [-n] [-r] [-s value] pattern

List or modify user preferences. 

**Options:**
* -w Save preferences.
  * -d List default value.
  * -n List non default values only.
  * -s Set a preference value.
  * -r Revert a preference value to default.
[code]# List all preferences:		
        preference		
        # List all preferences beginning with dat:		
        preference dat*		
        # Set a preference:		
        preference -s 12 dats.preferredtextsize		
        # Save out preferences		
        preference -w
        
[/code]

## 

preloadmovie [-i index] moviein_TOP

This command pre-allocates the CPU RAM and graphics RAM needed by a movie or still image. This includes any textures, async upload buffers, the movie file itself and all read ahead frames. The command attempts to open/allocate all of this with as little impact to playback as possible. It will take a few frames before the movie is actually ready to play. You can use the open and num_pre_read_frames channels in the Info CHOP pointing to the Movie In TOP to determine if the movie is ready to play yet. See also unloadmovie Command 

**Options:**
* -i index If specified, the movie will be opened and prepped to play at the specified frame index. Otherwise the index specified in the Index parameter will be used (if Specify Index play mode is selected).

## 

primgrouplist operator_pattern

Will output all the primitive groups in the specified SOPs. 

## 

print [-c] arg1 arg2 arg3...

Prints text to an external console window as well as to the textport. 

**Options:**
* -c the output is only printed to the console window.


    **See Also:**[echo](<#echo>)

## 

prompt new_prompt

Change the prompt to the string specified. The prompt string is expanded each time it is printed, therefore. 
[code] 
    # Set the prompt to the current frame number, followed by the		
    # current OP working directory:		
    prompt '$F`trim(execute(pc))`:'
    
[/code]

## 

quit [-f]

Terminate the program 

**Options:**
* -f force quit without prompting.

## 

read [-g] variable_name [variable_name2...]

Will read the following line into the variable names specified. The first argument of the following line will be put into the first variable, the last variable specified will be set to the remaining arguments of the input line. 

**Options:**
* -g will make the variables "global" (see setenv).

## 

realtime [on|off]

Turn realtime cooking on or off. 

## 

refresh [on|off]

This will cause the application to update all viewports, UI, etc while executing scripts. Be careful to not be refreshing under certain sitations in which it may be premature to do so. (eg, before a new operator has its input fully connected, etc). 

## 

run [-e] [-d seconds] [-f frames] [-m milliseconds] [-k pattern] [-l] [-g groupname] [-c] [-p path] [-t rc|Rc|rC|RC row col][-v] [-q] [arguments] dat_node_path

Execute the contents of a DAT node. Argument Passing Optional arguments may be appended to this command, which are accessible in the called script. $arg0 will always be set to the name of the DAT being run. $arg1 will be the first argument. $arg2 will be the second argument, etc. $argc will be the total number of arguments, including the name of the DAT being run. $args will be the complete set of arguments, including the name of the DAT being run ($arg0). $pargs will be the complete set of arguments, not including $arg0. Instead of using these numbered arguments explicitly, one can use the args command to rename them accordingly. Variable Scope If you are calling run or run -c within a script, say inside script A you have the command run B, then any variables declared in A can be accessed by B. However, variables declared in script B will not subsequently be accessible to A. If variable C is declared in script A with value c, but the value was changed to d inside script B, when script A resumes execution the value of C will revert back to c. If you are calling run B with options -d or -m, then variables declared in A will NOT be accessible to script B. Without -c, the current path will be changed to B, and revert to back to the path before executing B after B has finished. If you call run -c B, then B will start execution in the current path. After B has completed execution, the current path will remain at whatever path, if any, that script B has changed to. 

**Options:**
* -d Delay command execution by specified seconds
  * -f Delay command execution by specified frames
  * -m Delay command execution by specified milliseconds
  * -e Execute delayed script at the end of the frame, after nodes have had a chance to cook.
  * -q Quiet mode. No errors if path not found
  * -c Execute in current path. Default is to execute command in dat_node_path, and return to current path after execution.
  * -p path Execute in the given path.
  * -t rc|Rc|rC|RC row col Execute the given cell in the specified dat. Specify whether the row is indexed by number with r or by name with R, and the col by number with c and column by name with C.
  * -g Specify a group name for the delayed command
  * -l List all delayed commands
  * -k Kill a set of delayed commands
  * -v Verbose output of killed commands
[code]# Run the contents of /text1:		
        run /text1		
        # Run 5 seconds from now with some arguments		
        run -d 5 /text1 "Hello" 123		
        # Run 200 milliseconds from now.		
        run -m 200 /text1		
        # Run 200 milliseconds from now in current location.		
        run -c -m 200 /text1		
        # Delayed command group Example:Run /text1 in 5 seconds, and add		
        # it to group1:		
        run -g group1 -d 5 /text1		
        # List all delayed commands:		
        run -l		
        # Kill all commands under group*:		
        run -k group*		
        # Kill and list any commands under group1:		
        run -v -k group1		
        # Kill all delayed commands:		
        run -k *
        
[/code]


    **See Also:**[include](<#include>) [inline](<#inline>) [args](<#args>) [click](<#click>) [delay](<#delay>)

## 

rvar [-u] [-r] name = value

Set a root component variable specified by name to the value given. If no name is specified, then the list of all root component variables is printed out. 

**Options:**
* -u will un-set the variable(s) specified.
  * -v will return the name of the variable if successful.
[code]# Set in root component:		
        rvar A = 1		
        # List root component:		
        rvar		
        # Unset in root component:		
        rvar -u A*
        
[/code]


    **See Also:**[set](<#set>) [cvar](<#cvar>) [evar](<#evar>) [bvar](<#bvar>)

## 

saveallparms [0|1]

This option will control how modified parameters are saved in toe and component files. 

**Options:**
* 0 will only save parameters whose values have changed. Use this option to save disk space.
  * 1 will save all parameters regardless of their value.


    **See Also:**[opparm](<#opparm>) [parmls](<#parmls>)

## 

savecomponent [-m] component_path filename

This will save the named component to disk. 

**Options:**
* -m embed local media files to the component file.
[code]savecomponent geo1 test.tox		
        savecomponent /null1 output.tox		
        savecomponent -m /null1 output.tox
        
[/code]


    **See Also:**[loadcomponent](<#loadcomponent>)

## 

send [-d|-o|-h|-s typetag(s) OSCAddress] [-r] [-n] [-z] [-x] [-p datpath] path value1 value2...

This will output a string of one or more bytes to a communication DAT. The bytes can either be individually specified for binary communication, or one or more strings of ASCII characters. When specifying binary data, the values can be specified as decimal values, hexadecimal values, or octal values. The convertbase() expression can also be used to convert values from one base to another. When sending a string of ASCII characters, unless another terminating character is specified, a null character will be appended to the sent data. You can override this with the -x option. This command will work with the following DATs: Serial DAT OSC In DAT OSC Out DAT UDP In DAT UDP Out DAT UDT In DAT UDT Out DAT TCP/IP DAT File Out DAT For connectionless network protocols such as UDP, the * In nodes will only be able to send a reply once they have received a message from the Out node. When working with binary data, it is best to set incoming format of the communication DAT to One Row Per Byte and turn on the Value column. The Message column will simply be an ASCII representation of the data. The Value column, however will contain the decimal representation of each byte received. So for example, if the bytes returned were hex 03 and hex 0F, under the Value column you would see the values 3 and 15, as those are the decimal values of those bytes, respectively. 

**Options:**
* -d Treat values as series of decimal values.
  * -o Treat values as series of octal values.
  * -h Treat values as series of hex values.
  * -r Append a carriage return to the string.
  * -n Append a line feed to the string.
  * -z Append a zero (null character) to the string. This is done automatically for strings when no other terminating charcter is specified nor OSC format is specifed.(-o, -h, -s etc.)
  * -x Disables automatically appending a null character to strings.
  * -s typetag OSCAddress Treat values as parameters to an OSC message. You can specify multiple tags to match up with multiple values to send The following types are recognized: 
    * f float
    * i integer
    * s string
    * ? automatic (replaced by s,f or i)
  * -p datpath Send the contents of the specified DAT. When sending the contents of a table DAT and sending as bytes, each cell of the table is parsed into individual bytes, else each cell of the table is separated by a space and each row is terminated by the specified terminator character. (This does not apply to OSC formatted messages.)
[code]send -d /project1/serial1 65 66 67		
        # will output three binary values: 65, 66 and 67.  This is		
        # equivalent to sending 3 ASCII characters: "ABC"		
        send -h /project1/serial1 41		
        # will output a single hexadecimal value of hex 41.  This is		
        # equivalent to sending ASCII character "A"  or decimal value 65.		
        send -z /project1/tcpipout1 "ABC"		
        # will output "ABC\0".  Note the null character send at the end		
        # of the string.		
        send    /project1/tcpipout1 A B		
        # will output two bytes ASCII characters "A" and ASCII character "B"		
        send -p text1 tcpipout1		
        # will output the contents of DAT text1 text1.		
        send -p table1 tcpipout1		
        # will output all of table1 (columns will be separated by spaces)		
        send -z -p table1 tcpipout1		
        # will output all of table1 with a null character after each		
        # rowOSC Examples:output a float, string and integer as an OSC		
        # message to OSC address "/abc"		
        send -s fsi /abc udpout1 0.5 apple 3		
        same as above, but automatically specify the parameters		
        send -s ? /abc  udpout1 0.5 apple 3		
        # parameters are a string followed by a one or more floats		
        send -s sf /abc  udpout1 apple 1.0 2 3 4.5 6.7
        
[/code]

## 

sequencer sequencer_path [next_row]

This command will manually trigger the next CHOP to be sequenced by a Sequencer CHOP. If no next_row is given, it will abort its current clip and begin blending into the next clip specified by the given row. This will also cause the sequencer to resume if it is currently paused. 
[code] 
    sequencer /project1/anim/sequencer1 5
    
[/code]

## 

set [scope_options] name = value

set [scope_options] -u name_pattern set [scope_options] [-s] [-T] Set a variable specified by name to the value given. If no name is specified, then the list of all variables is printed out. 

**Options:**
* -s will make the output is suitable for loading as a script.
  * -u will un-set the variable(s) specified.
  * -T will output the information in table format.
  * -t Top-level read-only Touch variables.
  * (blank) Local script variables (default).
[code]set A = 1		
        set -g A = 1		
        set -u A*		
        set -u		
        set -s
        
[/code]


    **See Also:**[evar](<#evar>) [cvar](<#cvar>) [evar](<#evar>) [bvar](<#bvar>)

## 

shift

Shift the command line arguments, destroying $arg0 and moving $arg1 into $arg0, $arg2 into $arg1 etc. 

## 

sleep milliseconds

This command will pause for the specified number of milliseconds. 
[code] 
    # Pause one second:		
    sleep 1000
    
[/code]

## 

status [-b] [-c] message...

This command will set the status bar to the specified message. Environment variables will be expanded in the message. 

**Options:**
* -b will play a warning sound.
  * -c will skip the update if the message has not changed.


    **See Also:**[confirm](<#confirm>)

## 

system command options..

This command will execute commands in the operating system. Preferences->Allow Scripts to run System Command must be enabled for the commands to execute. To preserve arguments with spaces, enclose them with a backslash quote. 
[code] 
    system ls \"C:/Program Files\"		
    system dir \"C:\\Program Files\"
    
[/code]

## 

tabcell table_path rc|Rc|rC|RC row col value

This command will change the value of a cell. Specify whether the row is indexed by number with r or by name with R, and the col by number with c and column by name with C. Basically, it performs operations on a a row or column of a table. A "table" is one of the two forms of DATs (the other being simply lines of text). The Table DAT creates a table and the table commands can modify it. See the type Command to copy a full table. 
[code] 
    # Specify by name:		
    tabcell /sales/table1 RC April "Year 5" 330.25		
    # Specify by index:		
    tabcell /animations/table1 rc 3 5 do_jump		
    # Specify all row by name and columns by index:		
    tabcell /animations/table1 Rc * 1-5 0
    
[/code]

    **See Also:**[tabinsertm](<#tabinsertm>) [tabinsert](<#tabinsert>) [tabdelete](<#tabdelete>) [table](<#table>)

## 

tabdelete table_path r|R|c|C|a|A [row_or_col]

This command will remove a row, a column, or empty a table. Specify a row by number with r or by name with R, and the col by number with c and by name with C. It is possible for a table to have zero rows and non-zero columns and vice versa. To empty a table of all rows and columns, use a or A. 
[code] 
    # Delete row named abc:		
    tabdelete /table1 R abc		
    # Delete column named abc:		
    tabdelete /table1 C abc		
    # Delete row 2:		
    tabdelete /table1 r 2		
    # Delete column 3:		
    tabdelete /table1 c 3		
    # Set the table to have 0 rows and 0 columns:		
    tabdelete /table1 a
    
[/code]

    **See Also:**[tabinsertm](<#tabinsertm>) [tabinsert](<#tabinsert>) [tabcell](<#tabcell>) [table](<#table>)

## 

tabinsert [-b row_or_col] [-f row_or_col] table_path r|R|c|C [value1...] [value2...] [value3...] [...]

This command will add a row or a column. Specify a row by number with r or by name with R, and the col by number with c and by name with C. The case of the r and c will determine how -b and -f options are used, if any. By default, the row or column will be added to the end of the table. If you specify a list of values, these will be used to fill the newly created row or column. If there are not enough values to fill all the cells, the remaining cell will remain blank. If there are more values than available columns or rows, extra columns or rows will be created. 

**Options:**
* -b row_or_col add the row or column before the specified
  * -f row_or_col add the row or column after the specified
[code]# Append a row:		
        tabinsert /table1 r		
        # Append an empty row - use if there are no columns:		
        tabinsert /table1 r ""		
        # Append a row with values a,b,c for columns 0, 1, 2:		
        tabinsert /table1 r a b c		
        # Append a column, and fill it with values:		
        tabinsert /table1 c 0 1 2 3 4		
        # Append a row, after row abc:		
        tabinsert -f abc /table1 R		
        # Append a col, before col def, and name it abc:		
        tabinsert -b def /table1 C abc
        
[/code]


    **See Also:**[tabinsertm](<#tabinsertm>) [tabdelete](<#tabdelete>) [tabcell](<#tabcell>)

## 

tabinsertm [-a] [-b row_or_col] [-f row_or_col] table_path r|R|c|C [name1...] [name2...] [name3...] [...]

This command will add multiple rows or columns according to the list of names. Specify a row by number with r or by name with R, and the col by number with c and by name with C. The case of the r and c will determine how -b and -f options are used, if any. By default, the row or column will be added to the end of the table. One row or column will be added for each name listed. If there are no names, no rows or columns will be added. The names of the rows and columns added will be outputted. 

**Options:**
* -b row_or_col add the row or column before the specified
  * -f row_or_col add the row or column after the specified
  * -a rename if the row or column name already exists
[code]# Append an empty row - use if there are no columns:		
        tabinsertm /table1 r ""		
        # Append 3 empty rows:		
        tabinsertm /table1 r "" "" ""		
        # Append row with names tx, ty, tz:		
        tabinsertm /table1 r`expandpattern("t[xyz]")`# Append a row, after row abc:		
        tabinsertm -f abc /table1 R		
        # Append 2 columns, before col def, and named abc & efg:		
        tabinsertm -b def /table1 C abc efg
        
[/code]


    **See Also:**[tabinsert](<#tabinsert>) [tabdelete](<#tabdelete>) [tabcell](<#tabcell>) [table](<#table>)

## 

table [-a r|c] [-d] [-r row_name] [-c col_name] path [row_index] [col_index] cell_value

This command will perform operations on a a row or column of a table. A "table" is one of the two forms of DATs (the other being simply lines of text). The Table DAT creates a table and the table commands can modify it. However it has been split into the separate commands tabinsert, tabdelete and tabcell and it is not recommeded to use table in new scripts. 

**Options:**
* -a Append a row or column
  * -d Delete a row or column
[code]# Append a row:		
        table -a r /table1		
        # Append a column:		
        table -a c /table1		
        # Append a row, after row abc:		
        table -a r -f abc /table1		
        # Append a row, before row def:		
        table -a r -b def /table1		
        # Append a row named abc:		
        table -a r -r abc /table1		
        # Append a column named abc:		
        table -a c -c abc /table1		
        # Delete row named abc:		
        table -d -r abc /table1		
        # Delete column named abc:		
        table -d -c abc /table1		
        # Delete column 3:		
        table -d /table1 -1  3		
        # Delete row 2:		
        table -d /table1  2 -1		
        # Setting values:		
        # Specify by name:		
        table -r April -c "Year 5" /sales/table1 330.25		
        # Specify by index:		
        table /animations/table1 3 5 do_jump
        
[/code]


    **See Also:**[tabinsert](<#tabinsert>) [tabdelete](<#tabdelete>) [tabcell](<#tabcell>)

## 

tcur [time]

If no time is specified, the current time is printed. Otherwise, the current time is set to the time specified. 

## 

textport [-l dat] [-c dat] [-u dat]

Allows opening and closing of DATs. If a pane is specified, the pane type must be set to textport. 

**Options:**
* -l dat dat node to be loaded in viewer
  * -u dat dat node to be unloaded in viewer
  * -c dat dat node to be made current in viewer it will be loaded if it is not already loaded.

## 

textportlines [lines]

This will set the maximum number of lines displayed in the textport. If no value is given, the current setting is returned. 

## 

time [-d] [-e]

This command will return the elapsed time the application has been running. 

**Options:**
* -d will return the current calendar date + time.
  * -e will return the Epoch time (time in seconds since midnight 1st January 1970).

## 

timecur [-p path] [seconds]

If no time is specified, the current time in seconds is printed. Otherwise, the current time is set to the seconds specified. 
[code] 
    # Set the current time to 10 seconds		
    timecur 10		
    # List current time		
    timecur
    
[/code]

    **See Also:**[fcur](<#fcur>) [fplayback](<#fplayback>) [fps](<#fps>) [frange](<#frange>) [fset](<#fset>) [ftimecode](<#ftimecode>) [timerange](<#timerange>) [timeset](<#timeset>)

## 

timerange [-p path] [rangestart] [rangeend]

Sets or lists the working range of a time component in seconds. If no range is specified, the current range in seconds is printed. Otherwise, the working range is set to the range specified in seconds. 

**Options:**
* -p Specify path to component.
[code]# Set working range to 1-1500		
        timerange 1 1500		
        # List current working range		
        timerange		
        # Specify working range for the specified time component		
        timerange -p /container1
        
[/code]


    **See Also:**[fcur](<#fcur>) [fplayback](<#fplayback>) [fps](<#fps>) [frange](<#frange>) [fset](<#fset>) [ftimecode](<#ftimecode>) [timecur](<#timecur>) [timeset](<#timeset>)

## 

timeset [-p] [start][end]

Sets or lists the start-end range of a time component in seconds. If no start-end is specified, the current range is printed in seconds. Otherwise, the start-end range is set to the range specified in seconds. 

**Options:**
* -p Specify path to component.
[code]# Set start to 1 and end to 1500		
        timeset 1 1500		
        # List current start-end range		
        timeset		
        # Specify start-end range for the specified time component		
        timeset -p /container1
        
[/code]


    **See Also:**[fcur](<#fcur>) [fplayback](<#fplayback>) [fps](<#fps>) [frange](<#frange>) [fset](<#fset>) [ftimecode](<#ftimecode>) [timecur](<#timecur>) [timerange](<#timerange>)

## 

timeslice [-c smart|always] [-d on|off]

Changes the timeslice options for timesliced CHOPs. 

**Options:**
* -c smart

## 

toediff [-p pattern] toefile1 toefile2

This command will compare the difference between two saved toe files. 

**Options:**
* -p pattern Only output the components matching the pattern.
[code]toediff untitled.1.toe untitled.2.toe		
        toediff -p *project1* untitled.1.toe untitled.2.toe
        
[/code]


    **See Also:**[toestats](<#toestats>)

## 

toename [filename]

If no arguments are given then the current filename is returned. If an arguement is given, then the current filename is set to the argument and the $TOUCH variable is updated. 
[code] 
    # Returns current filename:		
    toename		
    # Sets filename to a/b.toe:		
    toename a/b.toe
    
[/code]

## 

toeprompt

Prompt the user with a file browser to load a new project file. 

## 

toeread [-m merge_pattern|-M] [-o] filename

Read a toe file. 

**Options:**
* -m merge_pattern will merge the file into the current TOE file. A pattern is specified to indicate which sections of the file should be merged in. The -M option is an abbreviation for -m * which will merge the entire contents of the specified file.
  * -o if specified the merge will attempt to "overwrite" the nodes whose names collide with those in the current session.
[code]# Replace current TOE file with job3:		
        toeread job3.toe		
        # Merge in everything from job3:		
        toeread -m * job3.toe		
        # Merge in all ops which match *geo*:		
        toeread -m *geo* job3.toe
        
[/code]


    **See Also:**[toewrite](<#toewrite>) [opread](<#opread>)

## 

toestats [-p pattern] toefile

This command can be used to output the file components of a saved toe file. 

**Options:**
* -p pattern Only output the components matching the pattern.
[code]toestats untitled.1.toe		
        toestats -p *project1* untitled.1.toe
        
[/code]


    **See Also:**[toediff](<#toediff>)

## 

toewrite [-e 0|1] [-p 0|1] [-i] [-l] [filename]

Write out a toe file containing the entire active session. 

**Options:**
* -s saves the file using the same method as "File -> Save" from the pulldown menus
  * -a saves the file using the same method as "File -> Save As" from the pulldown menus
  * -i if specified, then the filename is automatically "incremented". If using the -i option, don't specify a filename.
  * -l is used to create a link file. A link file is identical to the currently saved file except it has a well-defined name. For example untitled.35.toe would create a link file of untitled.toe. This link file can be used to simplify scripts, etc.
[code]# Default: save encrypted and compressed:		
        toewrite -e 1 a.toe		
        # Save uncompressed:		
        toewrite -e 0 a.toe		
        # Save all parameters:		
        toewrite -p 1 a.toe		
        # Default: save only modified parameters:		
        toewrite -p 0 a.toe
        
[/code]


    **See Also:**[toeread](<#toeread>) [opwrite](<#opwrite>) [opscript](<#opscript>) [saveallparms](<#saveallparms>)

## 

tops [options]

Used to set some TOPs preferences by script instead of by the Preference dialog 

**Options:**
* -f 0

## 

tset [-T] [start_time end_time]

If no time range is specified, the current time range is printed out. Otherwise, the time range is set to time. Values are specified in seconds. 

**Options:**
* -T Output tab delimited table format.

## 

type path1 [path2 path3...]

This command displays the contents of the listed paths to the textport. If there is no prefix a DAT node is assumed. If the filename is prefixed with FILE: a file is assumed. You can make a copy of a DAT's data, creating a new Table DAT or Text DAT. See examples. 
[code] 
    type project1/text1		
    type C:/log.txt		
    # Copy one table to another, creating table2 if it does not	exist:		
    type table1 >table2
    
[/code]

## 

ucd path

Deprecated: use instead. Change the current system working directory to the path specified. 

## 

uicolors -d [-l dat_node] [-c colorname r g b]

If no arguments are given, the current list of TouchDesigner colors are printed. 

**Options:**
* -d if specified, TouchDesigner will reload default colors.
  * -l dat_node if specified, TouchDesigner will override default colors with those specified in the dat_node.
  * -c colorname r g b if specified, the color specified is replaced with the specified r g b. It is faster to load a list of colors via a DAT then one by one using the -c option.
[code]uicolors -c tooltip.fg 1 1 1		
        uicolors -l /dat_colors
        
[/code]

## 

uioptions -d [-l dat_node] [-o optionname value]

If no arguments are given, the current list of TouchDesigner user interface options are printed. Font size: uioptions can adjust parameter dialog and textport size via the font.relative.size option. uioptions -o font.relative.size 0 will set the fonts to its default size. uioptions -o font.relative.size 3 will set the fonts to 3 points larger. fonts are clamped to 5 points larger and 3 points smaller than normal. 

**Options:**
* -d if specified, TouchDesigner will reload default options.
  * -l dat_node if specified, TouchDesigner will override default options with those specified in the dat_node.
  * -o optionname value if specified, the option specified is replaced with the specified value.
[code]uioptions -o tile.resizeborder.size 8		
        uioptions -l /dat_options
        
[/code]


    **See Also:**[uicolors](<#uicolors>)

## 

undo [-g] [-s] [-c] [-u [-l] [-q]] [-r [-l] [-q]] [-n name] [on|off]

Manages undo states and creations. Undo with no arguments will print the current state. undo -s will print just the current state (on 

**Options:**
* -g Indicate global undo.
  * -s Print state in short form.
  * -c Clear all undos and redos.
  * -u undo the last block of operations.
  * -r redo the last block of operations.
  * -u -l List the name of the last block of undo operations.
  * -r -l List the name of the last block of redo operations.
  * -u -q List all available undo operations.
  * -r -q List all available redo operations.
[code]# Set to no undoable actions for textport or script:		
        undo off		
        # Set to no undoable actions for all interfaces:		
        undo -g off		
        # Print undo states:		
        undo
        
[/code]

## 

unloadmovie [-c] moviein_TOP

This command frees the CPU RAM and graphics RAM used by a movie or still image that is opened by the Movie In TOP. This includes any textures, upload buffers, the movie file itself and all read ahead frames. See also preloadmovie Command. 

**Options:**
* -c If specified, the GPU memory won't be freed, but instead cached for use later by another movie of the same format and resolution.

## 

upwd

Deprecated: use instead. Print the current unix working directory 

## 

vclick [-q] [-l] [-m] [-r] [-x ] [-S] [-s] [-d] [-e] [-i id] path mx my

Simulate pressing a button on a component panel. mx and my are the position of the child of the given path. By default the coordinates are assumed to be between 0 and 1. U and V for the child panel will be set after the click. 

**Options:**
* -l Simulate pressing with the left mouse button.
  * -m Simulate pressing with the middle mouse button.
  * -r Simulate pressing with the right mouse button.
  * -q Quiet mode, supress error and warning output messsages.
  * -x Give the child's coordinates in pixels instead of normalized coordinates.
  * -S Coordinates are given in screen space (both pixels and normalized).
  * -i Specify an identifier for a click drag sequence.
  * -s Start a click drag sequence by turning select on.
  * -d Drag a click drag sequence. path is not specified.
  * -e End a click drag sequence by turning select off.
[code]# Click on the child at relative position (0.2,0.5)		
        vclick /container 0.2 0.5		
        # Press down at child (0.2,0.5)		
        vclick -i finger1 -s /container 0.2 0.5		
        # Drag finger 1 to (0.3, 0.4)		
        vclick -i finger1 -d 0.3 0.4		
        # Lift finger 1 at (0.4, 0.5)		
        vclick -i finger1 -e 0.4 0.5
        
[/code]

## 

verbose on|off

When verbose is on, every command will be printed to the textport as it is being executed. 

## 

version [-b] [-w]

Print the current version of the program running. 

**Options:**
* -b will cause the version command to print out the version number only.
  * -w will display the info in a separate window.

## 

vfs [-p path] [-b] [-l pattern] [-L pattern] [-x pattern] [-o] [-f folder] [-r pattern] [-a file]

This command accesses the Virtual File System, the internally embedded files of any component. Components with "embedded files" have a Virtual File System, or VFS. 

**Options:**
* -p path Specify the component. If none is given it uses the current component.
  * -l pattern List the files embedded in the component.
  * -b specifies to match by label, instead of path.
  * -L pattern List the files embedded in the component and all its children components recursively.
  * -b specifies to match by label, instead of path.
  * -r Remove the specified files from the component.
  * -b specifies to match by label, instead of path.
  * -a file Add a disk file to the component.
  * -x pattern Export the embedded files.
  * -o forces files to be overwritten, else they are renamed.
  * -f specifies a new folder, else the original path is used.
  * -b specifies to match by label, instead of path. The new path to the file is returned.
[code]# Add image.jpg to /project1:		
        vfs -p /project1 -a image.jpg		
        # List /project1's embedded files:		
        vfs -p /project1 -l *		
        # List /project1's embedded files and all its children:		
        vfs -p /project1 -L *		
        # Export all JPG images in project1 to C:\images:		
        cc /project1		
        vfs -x *.jpg -f C:\images		
        # Delete all files whose label matches the pattern.		
        vfs -r house* -b
        
[/code]

## 

view [-o] [-b on|off] [-c] [-C] [-r] [-R] path1 path2 path3 ...

Open or close a node viewer in a floating window. After you manipulate the node viewer, the viewer settings are saved in the .toe or .tox file, and they get restored when you start again. This includes the rotations in SOPs and graph settings in CHOPs. To reset or clear the node viewer settings, you can use the -r and -R options. This will save a small amount of memory and load time. 

**Options:**
* -o Open a viewer in a floating window.
  * -b on|off Specify whether or not window has borders.
  * -n Open a new floating viewer. If not specified, existing viewers pointing to the same node will be brought to the front instead.
  * -c Close a viewer.
  * -C Close the topmost panel viewer containing the specified child node.
  * -r Reset the node viewer state.
  * -R Reset the node viewer state recursively from the specified nodes through their hierarchy of children nodes.
[code]# Opens a floating viewer, or brings the viewer to the front if		
        # it already exists		
        view -o /project1		
        # Open several viewers		
        view -o /project*		
        # Open a new floating viewer without borders		
        view -b off -o /project1		
        # Close viewers		
        view -c /project*		
        # Close a panel by one of its children		
        view -C /project/button_momentary/container1		
        # Reset all viewers		
        view -R /
        
[/code]

## 

viewers on|off

Print the current state of the node viewers. On means viewers are always active. Off means only selected or toggled viewers are active. 

## 

viewfile file

Open file in an external application for that filetype. File can also be a URL. Multiple arguments will be concatenated with spaces to form one argument. 
[code] 
    viewfile www.derivative.ca		
    viewfile snapshot1.tif		
    viewfile C:/Documents and Settings/
    
[/code]

## 

vkey [-a] [-c] [-s] [-k] arg0 arg1 arg2 ...

Sends a key press to the current keyboard focus. 

**Options:**
* -a Turns on Alt key.
  * -c Turns on Ctrl key.
  * -s Turns on Shift key. Will not affect character sent.
  * -k Arguments are specified in character keycodes
[code]# Sends a string of virtual keys spelling "hello world"		
        vkey "hello world"		
        # Sends a string of virtual keys spelling "hello" and "world"		
        vkey hello world		
        # Sends "hello" in character code		
        vkey -k 104 101 108 108 111
        
[/code]

## 

while ( condition ) ... end

Execute a loop while the condition specified is true. 
[code] 
    set i = 0		
    while ( $i < 10 )		
    	set i =`$i+1`echo $i		
    end
    
[/code]

    **See Also:**[end](<#end>) [for](<#for>) [foreach](<#foreach>) [continue](<#continue>) [break](<#break>)

## 

winplacement [options] [setting=value] [setting=value] ...

This command sets window attributes for the design interface, performance interface and any additional monitor interfaces. The main interface window can be in one of two modes: Designer and Perform. If no options are given, the state of all options are output. 

**Options:**
* -i Open the parameter dialog.
  * -T Output all settings in table format.
  * -d 0
[code]# Enable the Perform interface:
        winplacement perform.enable = 1
        		
        # Disable the secondary monitor interface:
        winplacement monitor2.enable = 0
        		
        # Set the Design interface to 'Always on Top':
        winplacement ontop=1
        		
        # Set the stretch factor on monitor 3:
        winplacement monitor3.stretchx=0.5 monitor3.stretchy=0.5
        
[/code]


    **See Also:**[[#[[Window|[Window](<./Window.md> "Window") [#COMP](<#COMP>)|COMP]]]]
