# Run Command Examples

This page is also posted as a tutorial with an attached example file on the Derivative website [here](<https://derivative.ca/community-post/tutorial/using-run-delay-python-code/66947>). 

The following examples are meant to be pasted into a textDAT. You can then run them (RMB>Run Script or select and ctrl-R) and see the results in a textport. 

## The Run Command

The [run command](<./Td_Module.htm#Methods> "Td Module") allows you to run a string as a Python statement. It has many a number of options available as to how to run the command. The most powerful feature of these options is to allow you to delay the execution for a certain number of frames or milliseconds. Below is the full wiki documentation for run. This tutorial will go through all the options one by one.`run(scriptOrCallable, *args, endFrame=False, fromOP=None, asParameter=False, group=None, delayFrames=0, delayMilliSeconds=0, wallTime=False, delayRef=None)`→`Run`: 

> [Run](<./Run_Class.md> "Run Class") the script, returning a [Run](<./Run_Class.md> "Run Class") object which can be used to optionally modify its execution. This is most often used to run a script with a delay, as specified in the delayFrames or delayMilliSeconds arguments. See Run Command Examples for more info. 
> 
>   * scriptOrCallable - A string that is the script code to execute OR a callable Python object such as a function or lambda.
>   * args - (Optional) One or more arguments to be passed into the`scriptOrCallable`when it executes. They are accessible in the script using a tuple named args. They will be automatically passed as arguments if`scriptOrCallable`is a callable.
>   * endFrame - (Keyword, Optional) If True, the execution will be delayed until the end of the current frame.
>   * fromOP - (Keyword, Optional) Specifies an optional [operator](<./OP_Class.md> "OP Class") from which the execution will be run relative to.
>   * asParameter - (Keyword, Optional) When fromOP used, run relative to a parameter of fromOP.
>   * group - (Keyword, Optional) Can be used to specify a string label for the group of Run objects this belongs to. This label can then be used with the [td.runs](<./Runs_Class.md> "Runs Class") object to modify its execution.
>   * delayFrames - (Keyword, Optional) The number of frames to wait before executing the script.
>   * delayMilliSeconds - (Keyword, Optional) The number of milliseconds to wait before executing the script. This value is rounded to the nearest frame.
>   * wallTime - (Keyword, Optional) Setting this to True results in the delay options being based on actual elapsed time instead of elapsed frames.
>   * delayRef - (Keyword, Optional) Specifies an optional [operator](<./OP_Class.md> "OP Class") from which the delay time is derived. You can use your own [independent time component](<./Time_COMP.md> "Time COMP") or`op.TDResources`, a built-in independent time component. If no`delayRef`is provided, uses`root`> 

## Running A Simple Script

At its most basic,`run`allows you to execute a string as a Python script. The following is exactly the same as if you had executed the`script`argument without wrapping it in the`run`command. 
[code] 
    run("print('hello, world')")
    
[/code]

The above represents the way run looked for a long time in TouchDesigner, and you will see it in many examples. In more recent versions of TouchDesigner, you can also pass a function as the first argument to run, with arguments to that function after that. This next example does the same thing as the above with this newer format: 
[code] 
    run(print, "hello, world")
    
[/code]

## Running A Script With A Delay

Delaying the script is as simple as adding a`delayFrames`or`delayMilliSeconds`argument. 
[code] 
    run("print('hello, world')", delayFrames=60)
    run("print('hello, moon')", delayMilliSeconds=2000)
    
[/code]

Use the`wallTime`argument to make the delay be based on elapsed time instead of elapsed frames. This is useful when frames are being dropped and Real-time mode is off, ensuring the delayed amount is exact as fps is dropping. 
[code] 
    run("print('hello, world')", delayFrames=60, wallTime=True)
    run("print('hello, moon')", delayMilliSeconds=2000, wallTime=True)
    
[/code]

## Including Python Objects/Arguments In The Run Command

You can include any number of`args`that will be inserted into the command when it executes. This is useful for inserting variables and running other functions. 
[code] 
    location = 'world'
    
    # our first argument is a string, then next is a variable
    run('print(args[0] + ", " + args[1])', 'hello', location, delayFrames=60)
    
    # running another function using args
    def otherFunc(thing):
        print('yo,', thing)
    
    run('args[0]("moon")', otherFunc, delayMilliSeconds=2000)
    
[/code]

As mentioned above, you can also use a Python function (or other callable, such as a lambda) as the first argument of the run command, like this: 
[code] 
    location = 'world'
     
    # our first argument is a string, then next is a variable
    run(print, 'hello,', location, delayFrames=60)
     
    # running another function using args
    def otherFunc(thing):
    	print('yo,', thing)
    
    run(otherFunc, 'moon', delayMilliSeconds=2000)
    
[/code]

As you can see, this new format can be significantly nicer to use and more readable when working with function arguments. 

## Timing of Evaluation of Arguments Vs Script

The arguments passed to the run command are evaluated when the run command is _started_. Everything in the script itself is evaluated when the run command is _executed_. 
[code] 
    # Note that the first two delayed items use args to print the frame. These are calculated when the delay
    # is started. The last two evaluate the frame in the run statement, so they are calculated when the run
    # command actually executes.
    
    print('Current Frame:', absTime.frame)
    run("print('hello, world. Frame:', args[0])", absTime.frame, delayFrames=60)
    run("print('hello, moon. Frame:', args[0])", absTime.frame, delayMilliSeconds=2000)
    run("print('hello, Venus. Frame:', absTime.frame)", delayFrames=180)
    run("print('hello, Mars. Frame:', absTime.frame)", delayMilliSeconds=4000)
    
[/code]

## Using endFrame

The`endFrame`argument causes the script to be run at the end of the current frame. In the example below, both statements run in the same frame, but the run command happens second because it is deferred to frame end, while the print command happens immediately. 
[code] 
    run("print('hello, world. Frame:', absTime.frame)", endFrame=True)
    print("hello, moon. Frame:", absTime.frame)
    
[/code]

## The delayRef Argument

Using the`delayRef`argument, you can provide a component whose timeline will be used for the delay instead of the main TouchDesigner timeline. This can be your own [independent time component](<./Time_COMP.md> "Time COMP") but more commonly you can use`op.TDResources`which has independent time. Generally, this will be used for a delayed run that will still happen even if the TouchDesigner timeline is paused. If you don't use this argument, TD doesn't consider time to be passing for the delay unless the timeline is playing! 
[code] 
    # pause timeline before trying this
    run("print('hello, world')", delayFrames=60)
    run("print('hello, moon')", delayMilliSeconds=2000, delayRef=op.TDResources)
    # unpause timeline after a couple seconds
    
[/code]

## Changing Context With fromOP

The`fromOP`argument allows you to run the script as if it is being run from another operator. In general, this will only affect Python that is sensitive to its TouchDesigner network context, such as`me`and`op`. 
[code] 
    run('debug(me)')
    run('debug(me)', fromOP=root)
    
[/code]

## Altering Context With asParameter

The`asParameter`argument affects a legacy`run`behavior where, when`fromOP`is specified, op will search inside that operator. That is, if you had _torus1_ inside _geo1_ ,`run("print(op("torus1"))', fromOP=op('geo1'))`would find the child of _geo1_ , as opposed to searching for a sibling as one might expect. Setting this argument to True (the default is False) would make it search for the sibling instead. This argument is only relevant when _fromOP_ is set to a COMP, and only affects the operation of the _op_ object. 
[code] 
    run("print(op('torus1'))", fromOP=op('geo1'))
    run("print(op('torus1'))", fromOP=op('geo1'), asParameter=True)
    
[/code]

# Advanced run Command Features

The basic usage of`run`is covered above. This section will detail some more advanced`run`features including the [`Run`object](<./Run_Class.md> "Run Class") and the [`runs`collection](<./Runs_Class.md> "Runs Class"). 

## Killing Run Objects

The`run`command returns a [Run object](<./Run_Class.md> "Run Class") which can be stored in a variable. This is most commonly used to cancel scheduled commands via the object's`kill`method. 
[code] 
    worldRun = run("print('hello, world')", delayFrames=60)
    moonRun = run("print('hello, moon')", delayMilliSeconds=2000)
    
    print(worldRun)
    worldRun.kill()
    
[/code]

## The runs Collection

All the active`Run`objects in your project can be accessed via the [`runs`collection](<./Runs_Class.md> "Runs Class"). 
[code] 
    run("print('hello, world')", delayFrames=60)
    run("print('hello, moon')", delayMilliSeconds=2000)
    
    print('total runs:', len(runs))
    for i,r in enumerate(runs):
    	print(i, r.remainingFrames)
    
[/code]

## Killing All Run Objects

It's fairly simple to kill all active`Runs`by combining the techniques above... 
[code] 
    run("print('hello, world')", delayFrames=60)
    run("print('hello, moon')", delayMilliSeconds=2000)
    
    for r in runs:
    	r.kill()    
    
    run("print('goodbye, world')", delayFrames=60)
    
[/code]

**GOTCHA:** Many internal and user-built TouchDesigner features use`run`to deal with timing. Killing all active runs can cause unexpected and hidden problems. It is much safer to kill only select run objects... 

## Killing Select Run Objects

Killing only select`run`objects can be more complicated. To facilitate this, you can assign a`group`string when you create a`Run`to distinguish the objects from one another. The`group`is available as a member of the`Run`. 
[code] 
    run("print('hello, world')", group='world', delayFrames=60)
    run("print('hello, moon')", group='moon', delayMilliSeconds=1000)
    run("print('hello, Luna')", group='moon', delayMilliSeconds=1000)
    run("print('hello, Earth')", group='world', delayMilliSeconds=1000)
    
    for r in runs:
    	if r.group == 'world':
    		r.kill()
    
[/code]

Alternatively, you can examine a`run`object's`source`member to determine if you want to kill it. This feature allows you to test the actual code string that will run. In the following example, the run with the word "Earth" is killed. 
[code] 
    run("print('hello, world')", group='world', delayFrames=60)
    run("print('hello, moon')", group='moon', delayMilliSeconds=1000)
    run("print('hello, Luna')", group='moon', delayMilliSeconds=1000)
    run("print('hello, Earth')", group='world', delayMilliSeconds=1000)
    
    for r in runs:
    	if 'Earth' in r.source:
    		r.kill()
    
[/code]

## Testing Run Object Status`Run`objects that have already executed will cause an exception if you try to access them. This creates a bit of a tricky scenario if you want to test one that is stored in a variable to see if it is still pending. To get around this conundrum, use a try/except clause testing for`tdError`. 
[code] 
    worldRun = run("print('hello, world')", delayFrames=60)
    moonRun = run("print('hello, moon')")
    
    try:
    	if worldRun.active:
    		print('world active')
    except tdError:
    	print('world inactive')
    
    try:
    	if moonRun.active:
    		print('moon active')
    except tdError:
    	print('moon inactive')
    
    print("\nThis one is okay because it's active ---")
    print(worldRun.active)
    print("\nThis one errors because it's not ---")
    print(moonRun.active)
    
[/code]

## Single Update Design Pattern Example

One very useful design pattern for`run`is when you need to do some kind of update operation that can be triggered by many different events, but you only want to do the actual update once per frame. The following example sets this up so that any event(s) can call the`scheduleUpdate`function multiple times per frame, and the actual`update`function will only run once at the end of that frame. 
[code] 
    # run the "update" function anywhere that requires an end of frame
    # update. The update will only run once! 
    
    scheduledUpdateRun = None
    
    def update():
    	# the actual update function
    	print('Run updater!')
    	global scheduledUpdateRun
    	scheduledUpdateRun = None
    
    def scheduleUpdate():
    	# called to indicate an update is needed
    	global scheduledUpdateRun
    
    	print('Called schedule update!')
    	if scheduledUpdateRun is None:
    		scheduledUpdateRun = run('args[0]()', update, endFrame=True)
    
    scheduleUpdate()
    scheduleUpdate()
    scheduleUpdate()
    
[/code]
