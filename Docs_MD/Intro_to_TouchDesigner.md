# Intro to TouchDesigner

## **Introduction**  
  
Welcome to TouchDesigner. Once you’ve gotten your license installed, graphics drivers updated, and opened the program for the first time, you should see something like this: 

## **Interface Topography**

Let’s start by identifying all of the different control regions in your new workspace. We’ll start by looking at the big picture items, slowly working our way down into the smaller elements of the interface. In our default workspace we have eight different regions that we need to know about: 
* **Menu Bar |** The menu bar holds all of the typical menu operations you’d find in a program, the save and open dialog, edit elements, help etc. This is also the space that has a toggle to turn [Cooking](<./Cook.md> "Cook") on and off, as well a toggle for Realtime processing.
* **Pane Layout |** In TouchDesigner panes are the equivalent of workspace arrangements. Each pane has multiple views and features that allow you to see various parts of your network simultaneously. This is similar to many 3D rendering environments that give you multiple views of your scene at any given time. The Layout bar gives you the ability to quickly toggle between different layouts (horizontal and vertical split for example), as well as the ability to create your own custom view configurations.
* **Pane Bar |** While the Layout bar will help you determine the configuration of your windows, the individual pane bar gives you the ability for specific configurations for your workspace.
* **Palette Browser |** The Palette Browser servers multiple functions in TouchDesigner. First and foremost here you can find examples of several different kinds of tools and solutions to different problems. This is also a place where you can store frequently used modules that you develop in your own work.
* **Parameters Window |** Nearly all of the control of a given operator can be accessed from within the parameters window. This is a window that you’ll use constantly in your work, and later on we’ll talk about how this window is organized.
* **Network Editor |** In TouchDesigner your programs and algorithms are organized into networks of operators. The Network Editor, therefore, is where you do most of your building. We can think of this space as a two-dimensional space that’s like a desktop or canvas.
* **Time Attributes |** Using the time attributes box we can control a number of different elements about how time works in our network. Here we can set our global sample rate expressed as Frames Per Second (FPS), and the length of our composition in Frames. There are some situations where time is very important for playback and programming, and in other non-linear applications you’ll be less concerned about changing the Time Attributes dialogue.
* **Time Line |** In addition to being able to set some of the time attributes in our network, we can also access a timeline to control several aspects of how we move through linear sequences. Here you’ll see a play and pause button, single frame forward and reverse buttons as indicated by the + and - signs, as well as arrows that allow you to specify the direction of travel through the timeline.

## **Operators - All in the Family**

There are lots of different ways that information is organized for us in TouchDesigner, and one of the most immediately visible distinctions is the types of operators. For TouchDesigner different kinds of operations are classified by their family affiliation. The heart of this is really about the kind of data that’s embedded in a given operator. If, for example, we think of the difference between cassettes and compact disks, it seems obvious that you can’t play a CD with a tape-player. This is partially because of the nature of the medium, but it’s also due to the encoding method used to store the information. Magnetic tape and optical disk are fundamentally different in how they treat information - even though both contain “sound.” 

  
In TouchDesigner, we can think of the different families has having different organizational systems for their respective data. As long as we keep this in mind, it’s easy to see why we can’t immediately connect unlike families together. In order to help us, visually, we can also see that different families have different colors that are associated with them: 

**COMPs | Components | Gray**
* _Computed on both the GPU and CPU - depends on the COMP_
  * Components are high level operators that are often used to “hold” other networks. In addition to having their own set of parameters, COMPs can also contain whole networks of operators. As we build more complex projects, we quickly rely on these operators both for sake of organization and to build modular and reusable networks of operators.


  
**TOPs | Texture Operators | Purple**
* _Computed on the GPU_
  * Texture operators deal with pixel information. To your graphics card, a texture is what’s applied to a piece of 3D geometry. TouchDesigner uses the GPU as much as possible for processing information, for this very reason images are treated as scenes for the graphics card to render. This is why we think of photos and video as textures - because to our GPU they are textures that are applied to a piece of geometry.


**CHOPs | Channel Operators | Green**
* _Computed on the CPU_
  * Channel operators are linear sequences of floats or integers. These often manifest as animations, signals, inputs, curves, waves, or graphs. Audio, as a linear stream of floats, is also considered to be in the family of Channel Operators. CHOPs are the nervous system of your network. They send control and logic information throughout your project, and are an essential piece of how you drive your program.


**SOPs | Surface Operators | Blue**
* _Computed on the CPU_
  * Surface operators are pieces of 3D geometry. When we want to work with something in 3D space, or render objects we often use Surface operators. While we can do a lot of procedural surface modeling, we have to be wary of the fact that our SOPs are computed by the CPU. Given this, it can be easy to slow your system to a crawl if you suddenly find yourself very ambitiously using SOPs.


**MATs | Materials | Yellow**
* _Computed on the GPU_
  * Materials are applied to 3D geometry. The material determines what the 3D surface will look like when rendered by specifying the color and texture of the object and how light interacts with it.


**DATs | Data Operators | Pink**
* _Computed on the CPU_
  * There are some operations require the manipulation of text, tables, or other types of data, and for those operations we have DATs. We can also use DATs to script sequences of operations, and for some more advanced programming methods.

## **Connections**

Beyond the workspace itself there are also some other visual cues that help us see what’s happening in our network at a glance. There are two categories of connections that tie our networks together - wires and links. These are presented to us in two different visual styles to help us distinguish between them. 

  
**Links** Links are represented by dotted lines with a moving arrow head in our network. Links form connections between parameters and between families in our networks. Links can be formed between operators of the same family, and between operators of different families - links between different families are also called references or exported parameters. 

  
**Wires** Wires connect operators from the same family - TOP to TOP, CHOP to CHOP, et cetera. These kinds of connections pass information between operators to form procedural networks - the outcome of one algorithmic operation passed down the network to the next operator. Wires come in two different visual varieties. Moving and Static. This difference is subtle, but recognizing it in your networks will help you read a program faster and more efficiently. 

Moving wires tell you that information is actively being passed from one operator to the next. TouchDesigner is a pull based programming environment. This means that an operator only cooks (processes information) when it is requested by another operator in the network. Moving wires help us see at a glance that something is cooking. 

  
If moving wires help us see that an operator is pulling data down the network, static wires can help us see when information isn’t actively moving in our network. Static wires are solid in their appearance. 

## **Anatomy of an Operator**

Operators are the building blocks of your network, and there are lots of things to know about them. We will start by first taking a look at the anatomy of our operator itself so we know what it’s telling us at a glance. After that we’ll take a closer look at the parameters window, to get a better sense of what we can control and how we can manipulate our building blocks. 

  
**Operator Name** In TouchDesigner every operator can have a name, and in any given network all operators should have unique names. What does mean, and why do you care? Because the relationships that we form can exist between operators of the same family and operators of different families we need unique names in order to form specific references. If you’ve ever worked on a project with more than one Bob or Jennifer, you know how important it is to develop specific names so you know exactly who you’re talking to - whether in a long email chain, or in the middle of full project meeting. 

Another important feature to take note of is the iteration of operator names. We can see in the example below that the operator name is “moviein2” - why two? This means that this is the second Movie In TOP that was added to my network. If I added an additional Movie In TOP it’s default name would be “moviein3.” This because especially useful when we start to build large and complex networks. It’s also important to know that we can ask for an operator’s name, or just it’s digits. In the example below, our operator’s name is “moviein2” and its digits are 2. Later on we’ll see why this is so useful and important, so for now just tuck away this idea in an unused corner of your mind. 

  
**Operator Viewer** One of the most powerful elements you’ll encounter in TouchDesigner is the Operator Viewer. Every operator has a viewer that you can use to view and interact with elements of the operator. In our example here we’re looking at a png of a banana (hey Andy!). In other visual programming environments we might only see a file path, or a string of letters telling us that we have an image file ready to use. In TouchDesigner we can actually see a miniature version of our file. As we start to process our image with different operators we’ll also immediately see what effect those operations are having. This means that we always get to see, in real time, the entire chain of algorithmic operations that are happening in our network. This manifests as the ability to visually debug a network. You might well be concerned with the computational impact this is going to have on your finished program, and you’d be right in thinking that this kind of convenience comes at a cost. It’s true that rendering all of these previews does in fact have a cost - that said, it’s only a cost while you’re viewing the network. As soon as you leave a given network space, or enter perform mode, TouchDesigner stops rendering previews of individual nodes. This means that you sometimes get to have your cake and eat it too - both getting the benefit of seeing what’s happening in your program, each step along the way, without a performance cost when you’re no longer rendering the programming environment. 

  
**Connector Outputs** Inputs and Outputs for connectors are how you pass information from operator to operator within a family. In TouchDesigner inputs and outputs live on the left and right (respectively) of the operators. This is different than some other visual programming environments, and also means that networks typically read left to right in terms of the order of their operations. Some operators have multiple inputs with specialized functions - volume, reset, et cetera; others allow for a large stack of inputs (a Merge CHOP, or a Composite TOP are good examples of this). 

  
**Flags**

Flags in TouchDesigner are an indication of the status of an operator. We can use flags not only to see various states of operators, but also to control them. That’s all well and good, but what does that actually mean? Before we can dive into what flags do, it’s important to realize that flags come in two varieties - universal and family specific. 

  
**Universal**

Universal flags are found on all operators - and always in the same place on all operators. These flags can both be accessed in the visual programming environment, as well as with script commands. The univeral operators that are located on the upper left of operators are: 
* **Viewer |** The viewer flag allows you to toggle the viewer window on and off. You may find that at some point you don’t need to see every piece of the algorithmic chain that’s happening in your network. You might also find that you want to buy back the resources that rendering a preview of your work costs you. This is the flag to help make that happen.
* **Clone Immune |** Clone building is an essential part of making lightweight and reusable network components. At the heart of cloning is the ability to copy the contents of Base or Container Component into another. That said, you may sometimes want every individual operator to copy over, but not the parameters of that operator. The clone immune flag helps solve that problem.
* **Bypass |** You will undoubtedly ask yourself, at some point, “What is this operating doing?!” In those cases, the bypass flag can be a tremendous help. The bypass flag acts as a pass through toggle. This means that when bypassing is on the selected operator has no effect on the processing stream - instead it’s as though you have turned off that element in your algorithmic chain. When you toggle bypassing off, the selected node begins to have an effect on the network again.
* **Lock |** The lock flag is one of the most understated and yet most powerful flags. The lock flag, when toggled to the on position, will hold the contents of the operator in your project file. This means that the node will not cook, and it will not update when its inputs are changed. Initially this may not seem useful, but it means that you can save information inside of your procedural network that might otherwise be difficult to access.


  
**Viewer Active** The viewer active flag is also available on every operator, but rather than being located on the upper left, it’s instead located on the lower right. This small plus sign shaped flag toggles on and off the ability for you to directly interact with the contents of your operator. This allows you quick access to a number of different pieces of information in your operator, the ability to change view types, and in some cases the ability to change your viewing angle (this is especially important with Surface Operators). 

  
**Family Specific** As we’ve already seen, different families of operators do different kinds of information processing, this also means that we sometimes need some different options for displaying information for all of our different families. This is where family specific flags come into play. Next to the viewer active flag on the bottom right, you’ll find flags that are specific to each family. These appear as small circles that are color coded based on their function. Take a chance to look at all the flag types on the Flags page of the wiki. 

## **Parameters**

**Anatomy of the Parameters Window**

The Parameters Window is where we have access to all of the control features of a given operator. Here you’ll be able to alter how a given element in your network functions, create relationships between operators, and much more. That said, there are a few important features about the Parameters Window that we need to know in order to fully take advantage of a functions of an operator. 

  
**Names**

The names of our operator are always located in the top-most portion of the window. You’ll notice that I said names, not name. What gives? Any given operator has two names that are associated with it - the name of the type of operator, and the name you (the programmer) assign to the operator. In our example below we can see that this is a Movie In TOP (I know it’s a TOP because of its purple color). I can also see that this operator is named “moviein2” - you’ll see that next to the name of the operator type. Why should you even care about this. There are lots of reasons. The larger your networks become, the more important it will be to name your operators in a method to allow for easy reference building. You might for example, use a series of Composite TOPs in a given network. When you’re finally ready to output your video to a display, if you rely on the default naming in TouchDesigner, you suddenly have to remember if that was “composite4” or “composite8” or maybe even “composite11” that you want to use. If, instead you simply named it “finalComp” it will be easier for you to remember which operator you’re referencing. Let’s say that you give all of your operators descriptive names, when you hand off your network to another programmer (or come back to look at your work in three months), the descriptive names might not be helpful if you’re trying to see what operators were used in your network. This is why it is so useful to have both the name of type of operator, as well as its descriptive name in the top row of the parameters window. 

  
**Help and Info**

The next row in the Parameters Window has all sorts of useful materials. Left to right they are: 
* **Help |** This first help button will take you to the wiki page that’s built for the operator. Here you’ll find a short description of what the operator does, as well as a description of what all of the parameters control for a given operator.
* **Python Help |** Python 3 is the scripting language of choice for TouchDesigner, and the Python Help button will take you the corresponding Class page for a given operator. Here you’ll find information about scripting and referencing for that operator. The more you work with TouchDesigner, the more you’ll find reason to use scripting as a means of solving problems. When you’re starting you don’t need to know any Python to get working, but when you’re ready to do more complicated operations the Python Help button becomes invaluable.
* **Info |** The Info button reveals all sorts of useful information about an operator - including it’s cook time (how long it takes to process), it’s memory use (if it is a TOP it will also tell you it’s GPU memory use), and much much more.
* **Comment |** There are lots of ways to add comments to your TouchDesigner networks, and the comment function of a given operator is one of them. Here you can leave a short comment about what a given operator is doing. Comments left here will show up in the Info window.
* **Copied Values |** The copied values button reveals connections between operators. We might imagine a circumstance where we want a change in resolution of one TOP to automatically change the resolution of another TOP, rather than doing all of this by hand. In copying parameters between operators this button can help us quickly see where (the operator and the parameter) those connections exist.
* **Scripting Language |** TouchDesigner has two scripting languages - Python and TScript. While Python is now the default scripting language, there are still a lot of users and great methods for solving problems using TScript. If you need to change the scripting method for a given node, this button is how you toggle between languages.
* **Expand / Collapse Parameters |** Every parameter in TouchDesigner is scriptable. This means that anything you can control with a slider or a field in the Parameter’s Window is something you can control with a script or with another operator. This is part of what makes TouchDesigner so extremely powerful and flexible. When that’s the case, sometimes you want to expand the scripting areas of all of the parameters. The expand all button does just that. Similarly, it will also collapse all of the parameters to make your programming space a little more tidy.
* **Non-Default Parameters |** The non default parameters toggle is your new best friend. When you’re looking at the work of another programmer, or even your own work for that matter, it can be easy to quickly lose sight of what’s configured as a default setting, and what’s been altered by the programmer. This toggle will reveal only changed / non-default parameters. If you’re not sure what’s been changed in a given operator, this toggle makes it easy to see at a glance what’s going on.


  
**Pages**

Any given operator might have just a handful of parameters, or more than will fit on a single screen. For that very reason, they are often split into pages that relate to their function. You may find a piece of documentation, or a portion of the wiki or forum talking about a given page of a parameter. When you see that language, this is where you should look. 

  
**Parameters**

Finally we’re to the part of the Parameter Window that does all of the exciting work. Here you’ll find all of the control elements for a given operator. One important consideration to thinking about when working with these values is that they come in many different varieties - some of which can be changed, and some which can’t. For example, in our Movie In TOP below we can see that the Cue Point parameter is set to be a % of the video. This normalized value is operating off the assumption that you want to think of a movie’s duration in terms of 0-100%. That being said, you can change this particular parameter to be Index, Frames, Seconds, or Fraction. Working with parameters is a fundamental part of working with TouchDesigner, so don’t be afraid to take some time and experiment to with a given parameter so you can figure out what it’s doing for you.
