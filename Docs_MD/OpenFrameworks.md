# openFrameworks

**The previous TouchDesigner 2021.10000 series of builds of TouchDesigner, which still used OpenGL, has an infrastructure to process and render[openFrameworks](<http://www.openframeworks.cc/>) projects within the TouchDesigner process via a [CPlusPlus TOP](<./CPlusPlus_TOP.md> "CPlusPlus TOP"). openframeworks is not compatiblity currently with the 2022.20000+ builds, due to the changeover to Vulkan as our rendering API.**

The TouchDesigner sample project for openFrameworks has been upgraded to the 64-bit openFrameworks v0.9.8, with four examples of a C++ TOP. 

**Download Examples here** :   
[File:OpenFrameworksExamples.zip](</File:OpenFrameworksExamples.zip> "File:OpenFrameworksExamples.zip")

## Setup

1) [Download openFrameworks](<http://www.openframeworks.cc/download/>) and unzip it to your working directory. 

2) Copy the following folder in the TouchDesigner install folder: 
[code] 
       C:/Program Files/Derivative/TouchDesigner/Samples/CPlusPlus/OpenGLTOP
    
[/code]

to the following directory in the unzipped openFrameworks folder: 
[code] 
       apps/myApps
    
[/code]

Rename the folder to your project's name. 

**Note** : This is not strictly necessary, but it makes it a lot easier because openFrameworks includes a property sheet that lists all the "Additional Include Directories" relative to the root of the openFrameworks folder. Otherwise all the include directories would have to be added manually. 

3) Open the Visual Studio Solution (`.sln`) from the folder you just copied over. You must use Visual Studio 2012 or higher to be able to compile openFrameworks. 

4) In Visual Studio, right click on the solution in the "Solution Explorer" and click "Add > Existing Project". 

5) Locate the folder where openFrameworks was unzipped and select: 
[code] 
       libs/openFrameworksCompiled/project/vs/openframeworksLib.vcproj
    
[/code]

6) Right click on the`CPlusPlusTOPExample`project and click "Project Dependencies". Check the box next to`openframeworksLib`in the Dependencies page. Click OK. 

7) Right click on the`CPlusPlusTOPExample`project and click References. Click "Add New Reference" and check the box next to`openframeworksLib`. Click OK. 

8) Right click on the`CPlusPlusTOPExample`project and click Properties. Find "Configuration Properties > General" and set "Output Directory" to`$(SolutionDir)\bin`9) Click "View > Property Manager" (or "View > Other Windows > Property Manager"). Expand the CPlusPlus TOP project. For each of the debug folders, right click and click "Add Existing Property Sheet". Locate the folder where openFrameworks was unzipped and select: 
[code] 
       libs/openFrameworksCompiled/project/vs/openFrameworksDebug.props
    
[/code]

10) Do the same for the release folders, except instead select: 
[code] 
       libs/openFrameworksCompiled/project/vs/openFrameworksRelease.props
    
[/code]

11) Go back to the "Solution Explorer" and open`TOP_CPlusPlusBase.h`. Remove the following lines: 
[code] 
    #include <windows.h>
    #include <cstdio>
    
[/code]

and replace them with: 
[code] 
    #include "ofMain.h"
    
[/code]

12) In`CPlusPlusTOPExample.h`, add 
[code] 
    #include "ofAppNoWindow.h"
    
[/code]

and add the members 
[code] 
    ofAppNoWindow myWindow;
    ofGLProgrammableRenderer *renderer;
    
[/code]

to the class body for the TOP. 

13) In`CPlusPlusTOPExample.cpp`: Add the following lines to the constructor method`CPlusPlusTOPExample::CPlusPlusTOPExample`: 
[code] 
    renderer = new ofGLProgrammableRenderer(&myWindow);
    ofSetDataPathRoot(path_to_dir);
    
[/code]

Because the application being run is TouchDesigner, openFrameworks will search the installed TouchDesigner's`bin`for`/data`by default. If you have any shaders/images to load then`ofSetDataPathRootpath_to_dir);`is necessary to give openFrameworks the path to the`bin/data`directory.  
**Note** :`path_to_dir`must use forward slashes, and it can either be an absolute path, or a relative path from TouchDesigner's executable.   
Example:`ofSetDataPathRoot("../../../../of_v0.9.3_vs_release/apps/myApps/CPlusPlusTOPExample/bin/data/")`14) Create a`CPlusPlusTOPExample::setup`function to be called only once: 
[code] 
    void CPlusPlusTOPExample::setup() 
    {
        glewInit();
        renderer->setup(3, 2);<br>
        // load any shaders, images, etc
    }
    
[/code]

In addition to`glewInit();`and`renderer->setup(3, 2);`this is where you should load any shaders or images. 

15) At the top of`CPlusPlusTOPExample::execute`query any custom parameters. 

16) Query for the resolution width and height: 
[code] 
     int width = outputFormat->width;
     int height = outputFormat->height;
    
[/code]

Then setup the window with the width and height of the C++TOP: 
[code] 
     ofSetupOpenGL(&myWindow, width, height, OF_WINDOW);
    
[/code]

17) Enclose the rest of`CPlusPlusTOPExample::execute`with:  

[code] 
    context->beginGLCommands();<br>
    // ... rest of your code<br>
    context->endGLCommands();
    
[/code]

18) Add`CPlusPlusTOPExample::setup`call enclosed by context 

19) For any rendering in openFrameworks it's necessary to enclose it with: 
[code] 
    renderer->startRender();
    renderer->setupScreen();<br>
    // any binding of shaders/images, drawing, etc.<br>
    renderer->finishRender();
    
[/code]

Example`CPlusPlusTOPExample::execute`after steps 15-19 
[code] 
    void CPlusPlusTOPExample::execute(const TOP_OutputFormatSpecs* outputFormat, OP_Inputs* inputs, TOP_Context *context) 
    {
        // query custom parameters <br>
        int width = outputFormat->width;
        int height = outputFormat->height;<br>
        ofSetupOpenGL(&myWindow, width, height, OF_WINDOW);<br>
        context->beginGLCommands();<br>
        if(!isSetup)
        {
          setup();
        }<br>
        renderer->startRender();
        renderer->setupScreen();<br>
        // any binding of shaders/images, drawing, etc.<br>
        renderer->finishRender();<br>
        context->endGLCommands();
    }
    
[/code]

19) Build the project. All the DLLs required to use the CPlusPlus TOP are in the following directory in the folder where openFrameworks was unzipped: 
[code] 
       apps/myApps/<project-name>/bin
    
[/code]

It is important that all the DLLs remain together in the same directory because of dependencies. TouchDesigner will automatically load the other required DLLs if they are in the same directory. 

## Translating openFrameworks code to work within TouchDesigner

The creation of an`ofAppNoWindow`using the above steps will cause many openFrameworks functions to break down and`ofGetCurrentRenderer()`, which queries the renderer of the window, is to blame for this.  
The renderer holds much of the useful renderering functionality, however`ofAppNoWindow`has an`ofNoopRenderer`which is missing crucial functionality. As a result`ofGetCurrentRenderer()`returns an unusable renderer that will either lead to a crash or do nothing.  
In order to render in TouchDesigner using openFrameworks`ofGetCurrentRenderer()`must be bypassed, meaning any function that calls`ofGetCurrentRenderer()`cannot be used. This is exactly why an`ofGLProgrammableRenderer`object is created in steps 12-13.  
To translate any openFrameworks function that calls`ofGetCurrentRenderer()`, look at the source and see how it uses the renderer, then move that functionality to your`CPlusPlusTOPExample`using the created`ofGLProgrammableRenderer`object.  
openFrameworks is open source so you will need to look at the source code to see specifically what functions need to be changed. All drawing, binding, and transforming will need to be changed.  
  
Example of binding a shader:  

[code] 
    shader.begin();
    
[/code]

becomes 
[code] 
    renderer->bind(shader);
    
[/code]

## Using Input TOPs

The following code is an example of how to use input TOPs with openFrameworks: 
[code] 
    void
    CPlusPlusTOPExample::execute(const TOP_OutputFormatSpecs* outputFormat,
     				const TOP_InputArrays* arrays,
     				void* reserved)
    {
        // ...
        // Use the first input TOP (here we assume it exists but in reality it might not)
        const TOP_TOPInput *topInput = &arrays->TOPInputs[0];
        ofTexture texture;
        texture.setUseExternalTextureID(topInput->textureIndex);
        texture.texData.width = topInput->width;
        texture.texData.height = topInput->height;
        texture.texData.tex_w = topInput->width;
     	
        texture.texData.tex_h = topInput->height;
        texture.texData.textureTarget = topInput->textureType;
        // ...
    }
    
[/code]
