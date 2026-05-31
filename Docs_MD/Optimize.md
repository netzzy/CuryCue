# Optimize

All realtime systems demand serious effort and production time in the optimization stage. Performance optimizations to TouchDesigner networks can often result in speed ups in the 2 to 20 times range. This can effect what is capable of running your computer hardware and it will affect the experience of your audience. 

Tools of Optimization: 
* middle-mouse click info popup on each node (alt-rclick on macOs)
  * [Performance Monitor Dialog](<./Performance_Monitor_Dialog.md> "Performance Monitor Dialog") (alt+y) under Dialogs... to assist in optimization.
  * [Probe](<./Palette-probe.md> "Palette:probe") in the Palette to graphically watch how time and memory on the CPU and GPU are being dynamically consumed, and catch momentary drops in performance.
  * Dialogs -> Errors and the [Error DAT](<./Error_DAT.md> "Error DAT") to catch errors that may be slowing thing down.
  * Textport
  * [Perform CHOP](<./Perform_CHOP.md> "Perform CHOP") followed by a [Trail CHOP](<./Trail_CHOP.md> "Trail CHOP") and turn on Frame Time and Cook channels to look at a time-history of performance.
  *`print()`or`debug()`statements in your python scripts


The frames-per-second (or milliseconds-per-frame) depends on the compute load every frame, especially the selection of procedural operators, the amount of geometry, CPU and graphics speeds, and MOST OF ALL the optimizations that the user employs in building the project. 

TouchDesigner makes heavy use of both the [CPU](<./CPU.md> "CPU") and the [GPU](<./GPU.md> "GPU"). Reducing the workload on these two processors requires two different strategies as described below. 

**Quick Tip** : The first thing to determine is if the GPU is the bottleneck. Try turning down your render resolution 64x64 and see if things speed up. If they do then you know it’s GPU related. It’s quite possible your issue isn’t a GPU bottleneck though, unless it’s just GLSL shaders you are running with little else going on in the system. Check the [Performance Monitor](<./Performance_Monitor.md> "Performance Monitor") to see what is taking up most of the time. 

See [Cook](<./Cook.md> "Cook"), [Dependency](<./Dependency.md> "Dependency"), [Event](<./Event.md> "Event"), [Troubleshooting in TouchDesigner](<./Troubleshooting_in_TouchDesigner.md> "Troubleshooting in TouchDesigner")

## Determining Bottlenecks

CPU and GPU interaction are very pipelined. Pipelining is a feature of computing that is analogous to an assembly line in a factory. Pipelining allows for much higher speed, but when trying to optimize one you need to be very aware of bottlenecks. 

Let's use a car factory as an example. Say the factory has 3 stages in its assembly line, one that makes the chassis, one that installs the engine in the chassis, and one that mounts the wheels on the chassis. Let says the chassis department can make 10 chassis and hour, the engine installers can install 7 engines an hour, and the wheel mounters can mount 15 sets of wheels an hour. Since the car is useless unless all of the parts are installed, the factory can only output 7 cars per hour. If management goes out and buys a machine that allows the wheel mounters to mount 25 sets of wheels an hour, the factory will still only output 7 cars an hour. The engine installers are the Bottleneck in the pipeline. The only way the factory can increase output is first by increasing the engine installers efficiency so they can install 10 or more engines an hour. Say they are able to increase them to 13 engines an hour. Now the factory can do 10 cars an hour, because the chassis department has now become the bottleneck, and any further improvements to the engine department are useless until the chassis department is made more efficient. 

All of the above is true for TouchDesigner, where the different departments are the CPU and the GPU (they can be further split into sub-departments, but we'll deal with that elsewhere). So if your system has a CPU bottleneck, reducing GPU workload will result in no change to framerates. 

### CPU Bottleneck

You can use a [Hog CHOP](<./Hog_CHOP.md> "Hog CHOP") to see if you have a CPU bottleneck. If you place down a Hog CHOP and your framerate goes down, then you have a CPU bottleneck. If your frame-rate doesn't change then you have a GPU bottleneck. 

Conversely, if you reduce the rendering or compositing of images ([TOPs](<./TOP.md> "TOP")) to a very small resolution (like 32x32) and the frame rate does not change, you have a CPU bottleneck. 

### GPU Bottleneck

The GPU itself has a few stages to its pipeline. A few of these are Vertex Shading, Pixel Shading, Blending. For TOPs in general, 95% of the time the GPU bottleneck will be caused by the pixel shader. This happens when it is shading too many pixels and/or the the operations it needs to do per pixel are too expensive. 

To determine if you have a pixel shader bottleneck try reducing the resolution of your TOPs that are cooking every frame. If your framerate goes up then you have a pixel shader bottleneck. 

If you reduce the resolution to half in X and Y (Common Page), your total pixels goes down to a quarter, and then you should see the GPU time for that TOP go down to a quarter. (Middle mouse click on the node to see the GPU time of that node). 

See the section below on the Render TOP for optimizing it. 

See also [Probe](<./Palette-probe.md> "Palette:probe"), [Phong MAT Shader Resource Usage](<./Phong_MAT_Shader_Resource_Usage.md> "Phong MAT Shader Resource Usage")

## Optimizing CPU Usage

### Performance Monitor

Use the [Performance Monitor Dialog](<./Performance_Monitor_Dialog.md> "Performance Monitor Dialog") to find expensive cook or nodes that are unnecessarily cooking. With the Performance Monitor you can see the order-of-cook of one frame, and the cook times of all the stages. Also you can trigger a dump on frames that exceed a certain threshold. Use [Probe](<./Palette-probe.md> "Palette:probe") to watch CPU usage dynamically change. 

### OP cooking time, OP info pop-up

Each OP info pop-up (middle mouse on the OP) displays how many times it has cooked and how long its last cook took, in milliseconds. 
* **cook time** : how long it takes that operator to process (or '[cook](<./Cook.md> "Cook")').
  * **number of cooks** : often what is important is whether it cooks every frame or it cooks just once, or only when its input data changes.

### Understand Why Nodes Cook

Refer to the [Cook](<./Cook.md> "Cook") article. 

### Finding unnecessary cooking
* **Re-ordering** : OPs that don't change should be moved high in the cook chain so it doesn't cook unnecessarily.
  * **Combining output length of multi-input CHOPs** : When 2 or more CHOPs combine (link in a Math CHOP), make sure the resulting CHOP length isn't unnecessarily long, due to one CHOP being at frame 1 and another being at the current frame.

### Faster Cooking

Generally speaking, DATs, SOPs, CHOPs cook faster on subsequent cooks when they don't have to add/remove cells/points/channels from their output, but merely tweak the output values from the previous cook. Therefore try to keep the amount of output being generated consistent between cooks wherever possible. 

### Make Sure Your Geometry is in an Optimal Format

While the GPU actually renders geometry, there can be a large cost involved with telling the GPU all of the information it needs to render this geometry. Refer to the [Optimize Geometry for Rendering](<./Optimize_Geometry_for_Rendering.md> "Optimize Geometry for Rendering") article and the [Render TOP](<./Render_TOP.md> "Render TOP") for more information on this. 

### Transform your Geometry at the Object Level instead of in a SOP

Transform at the [object](<./Object_Component.md> "Object Component") level if you can. Often if you have a [Transform SOP](<./Transform_SOP.md> "Transform SOP") among an object's SOPs, it has the same effect of translating, rotating, or scaling an object as if you applied the same transform parameters at the object level. That is, using a Transform SOP has the same effect as using the same numbers on the object transform. However their compute times are very different. As a SOP, the CPU needs to apply a transform to every point. But if the transform is in the object, it lets the graphics hardware do the transform, which is much faster and applied to the object as a whole. 

### Profiling Python Scripts in DATs

Python scripts can be very expensive. If they are showing up as taking significant time in the Performance Monitor, it may be worth seeing if they can be optimized at all. General Python and coding optimization techniques can be used. You can profile which parts of your script are taking time by using the`time.perf_counter()`method that is part of the`time`module. 

In many cases, chunks of python code can be replaced with a small network of TouchDesigner CHOPs or DATs, which may be an order of magnitude faster. The more CHOPs and DATs you are familiar with, the more you can save your time and the CPU's time. 

If you can, avoid scripts running every frame. The Performance Monitor will reveal script cook times. There are a number of ways to optimize python, including pre-computing quantities and references that are to be used numerous times. 

### Reducing Cooking in by Using Python in Expressions

Python in parameter expressions now are quite optimized (they usually get pre-compiled into more executable code). See the rollover popup help on parameters with expressions They will say (Optimized) or (Un-optimized). The most time-consuming will be long python functions in extensions and modules. 

### Reducing Cooking in CHOPs

The [Null CHOP](<./Null_CHOP.md> "Null CHOP") in Selective mode can be used to reduce downstream cooking in CHOP chains when the input to the Null CHOP doesn't change. However, the [Null CHOP](<./Null_CHOP.md> "Null CHOP") itself will always cook on data changes in this mode, so use with caution. 

### Other Processes Running and Interrupting TouchDesigner
* Turn off all virus checkers and spy-ware services while running TouchDesigner. These services can often use lots of CPU cycles and access the hard drive frequently.
  * Turn off all unnecessary Windows services.

### Multi-CPU Usage
* You can run multiple instances of TouchDesigner on one computer. Then using the various Touch In/Outs you can move data between the processes and thus offload some work onto other processors.
* Beware that doing this with the [Touch In TOP](<./Touch_In_TOP.md> "Touch In TOP") and [Touch Out TOP](<./Touch_Out_TOP.md> "Touch Out TOP") and large images may not get you the performance boost you are looking for as TOPs use the graphics card heavily and you only have one of those. However you could certainly do it on another physical computer and use a fast gigabit network.

## Optimizing GPU Usage

### Reduce Number of Pixels in Render TOP

As with other TOPs, if you reduce the resolution to half in X and Y (Common Page) of a Render TOP, your total pixels goes down to a quarter, and you should see the GPU render time go down to a quarter. (Middle mouse click on the node to see the times.) 

### Reduce Overdraw in Render TOP

Refer to the article on [Early Depth-Test](<./Early_Depth-Test.md> "Early Depth-Test"). 

Another feature that can help reduce overdraw is [Back-Face Culling](<./Back-Face_Culling.md> "Back-Face Culling"). 

### Reduce Vertices in Render TOP

If the number of vertices or particles is very high, the Vertex Shader engine will affect the GPU workload, especially if you have GLSL shaders with Vertex Shader code. Try reducing the number of vertices or particles in this case and see if the render time goes down. 

### Reduce GPU Workload in Render TOP

What does affect speed greatly is the number of lights, the type of lights, and the features that are used in [MATs](<./MAT.md> "MAT"). For example, a cone light is more expensive than a point or distance point (See [Light COMP](<./Light_COMP.md> "Light COMP")). Enabling features like Rim Lighting in the [Phong MAT](<./Phong_MAT.md> "Phong MAT") will increase the pixel shader cost as well (To see the cost, turn off the rim lighting and see how much faster things run). 

### Render TOP Parameters

There are some parameters on the [Render TOPs](<./Render_TOP.md> "Render TOP") **Advanced** page that can be used to speed up rendering. For example, if you are only calculating a shadow map, then you can turn on the **Draw Depth Only** feature. If you don't need the color output from that particular Render TOP, you can turn off **Color Output Needed** , which will avoid resolving the offscreen antialias buffer down into a texture which can be used as an input for other TOPs. 

### Reduce Workload of other TOPs

As noted above, the cost of other TOPs is generally tied directly to their resolution, reducing their resolution will have a 1:1 speedup for GPU workload. Some other TOPs are more expensive depending on their parameters, the filter size of [Blur TOP](<./Blur_TOP.md> "Blur TOP") is an example of this. 

## Optimizing Memory Usage

Use [Probe](<./Palette-probe.md> "Palette:probe") to see where CPU and GPU memory is being consumed. 

### Audio Play CHOP

The Audio Play CHOP currently loads the entire sound file into RAM. If you have a longer sound file, you should consider using the [Audio File In CHOP](<./Audio_File_In_CHOP.md> "Audio File In CHOP"). 

### See Also

[Stuttered Playback](<./Stuttered_Playback.md> "Stuttered Playback") [Optimized_Python_Expressions](<./Optimized_Python_Expressions.md> "Optimized Python Expressions")
