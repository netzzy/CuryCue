# Palette:initializeStart

The`initializeStart`component is designed to be installed into users components that have time-dependent behavior. If you follow this procedure, you will have a component that has a TouchDesigner-standard way of being controlled, mostly via its parameters on the InitStart page. Also a set of standard channels is output from your component coming from the internal [Timer CHOP](<./Timer_CHOP.md> "Timer CHOP"). 

Time-dependent behavior includes: 
* procedurally-generated dynamic objects like particles, that step forward (iterate) every frame, and that would start from a pre-determined configuration or state.
  * more deterministic playback of (possibly keyframed) animation that has its own internal timeline, like movie playback.


See the [Initialize Start](<./Initialize_Start.md> "Initialize Start") standard description. 

Once set up, internally, you can use the`initializeStart`timers and states to step forward in your simulations or playback animations, controlling speeds, pausing, initializing, unloading. 

## Procedure to Install initializeStart

This explains how to install this template into your time-dependent components to give them the standard timing behavior, which includes Timer CHOP channels and the parameters that control them: 

There are three ways - choose whatever suits you: 

(1) Use this initializeStart to start with, and copy/paste all your pre-existing functionality into it (if you are upgrading an existing COMP), including your pre-existing top-level parameters. Because this uses the Parent Shortcut called InitStart in expressions, you may want to call the Parent Shortcut something else that better suits you component, so you need to change the expressions on the Timer CHOP to use a different Parent Shortcut. 

(2) Into an existing component of yours, copy "timer", "initStartCallbacks" and "out1". Also copy the whole InitStart page of parameters to your existing component. Again you may need to change the expressions on the Timer CHOP to use a different Parent Shortcut. 

(3) is like (2) but it isolates this COMP a bit more, in case it is later cloned. it also merges initializeStart into your pre-existing component: (This example will be for particlesGpu.) Copy/paste this COMP into particlesGpu. Attach a Null CHOP to the initializeStart output and name it "times". This is what your component will use to drive its time. Attach an Out CHOP to "times" so that particlesGpu outputs the timing information. 

Copy the`initStartCallbacks`DAT in this network up a level. Then set initialzeStart's Callback parameter to point to`initStartCallbacks`instead of ./initStartCallbacks. 

With the Component Editor (on initializeStart, rclick -> Customize Component), duplicate the InitStart page onto particlesGpu so all parameters are all visible at the top level. Then bind all the parameters so that the new parameters on particlesGpu are the masters. 

You can delete some top-level parameters if you know you are not going to need them. You may know Type will be Infinite Length, so delete that par and the Length par at the top level and set Type inside to Infinite Length. 

You may want to edit the initStartCallbacks to specifically drive particlesGpu, Perhaps fill in`onInitialize()`,`onStart()`,`onDone()`. 

## Using initializeStart

Use the channels of the "timer" or "times" CHOP for whatever you want, and you can use more top-level parameters like Speed and Play in your networks. 

Sometimes you will want to drive your simulation with a timing channel externally, so the External parameters are good for that. See the [Timer CHOP](<./Timer_CHOP.md> "Timer CHOP") for further information about External control. It will drive the Timer CHOP directly. Otherwise, keep External Control off. 

If your component is a simulation where it iterates forward, you can hook the`parent().par.Speed`and`parent().par.Play`parameters to your variable that determines how much time to step forward each time the timeline steps forward. 

If your component plays back media in a pre-determined way, you can use the`op('timer')['timer_seconds']`channel or other channels to select which data or frame to display. 

You can use the other channels of`times`at your leisure. 

## External Control via Parameters

Press the Initialize parameter. The channels should go into a "ready" state with timers at 0 or an Initialize Time. 

Press Start. counters begin rising 

Adjust Speed.`timer_seconds`and other channels slow down. 

Press Play off. Some timers will stop. Press Play on. 

Press Go to Done. channels will go into a "done" state. 

Press Initialize again, or to initialize and start in one step, press Start. If you press Start and it has not been initialized yet, It will do an Initialize first and then start. 

This follows the typical [Timer CHOP](<./Timer_CHOP.md> "Timer CHOP") behavior. 

## External Control via Timing Channels

Sometimes you will want to drive the simulation with a timing channel externally, so the External parameters are good for that. See the [Timer CHOP](<./Timer_CHOP.md> "Timer CHOP") for further information about External control. Otherwise, keep External Control off. 

  
If you want to initialize your component to a certain starting point, use the Initialize Time parameter. When you pulse Initialize,`timer_seconds`will be set to that time. You can use top-level parameters, like Pre-Roll to pre-simulate some number of seconds of your sim.`Tip`: You can attach an Info DAT to the Timer CHOP to get timecodes.
