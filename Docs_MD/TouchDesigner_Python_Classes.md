# Python Classes and Modules

The following list of important Python classes and modules is roughly grouped together by subject. 

[Python Reference](<./Category-Python_Reference.md> "Category:Python Reference") has an alphabetical list of all TouchDesigner Python pages on this wiki. 

### Operator Related Classes

The following classes are Python interfaces for operators and objects that operators use. Individual operator classes (e.g. [TextTOP Class](<./TextTOP_Class.md> "TextTOP Class") and [RampTOP Class](<./RampTOP_Class.md> "RampTOP Class")) are not listed but do exist in the [`td`module](<./Td_Module.md> "Td Module"), and links to each can be found [here](<./Category-Python_Reference.md> "Category:Python Reference") or by clicking on the Python Help button in their [parameter dialog](<./Parameter_Dialog.md> "Parameter Dialog"). These classes are found in the [td module](<./Td_Module.md> "Td Module") so do not need to be imported. 
* **[OP Class](<./OP_Class.md> "OP Class")** \- a TouchDesigner [operator](<./Operator.md> "Operator"). 
    * **[Connector Class](<./Connector_Class.md> "Connector Class")** \- a wire connector for an OP. Lists of these can be found in`OP.inputConnectors`and`OP.outputConnectors`. Components also have`COMP.inputCOMPConnectors`and`COMP.outputCOMPConnectors`.
    * **[Page Class](<./Page_Class.md> "Page Class")** \- a parameter page. Lists of these can be found in`OP.pages`and, on components and script operators,`OP.customPages`.
    * **[ParCollection Class](<./ParCollection_Class.md> "ParCollection Class")** (`OP.par`) - holds all the parameters for an OP. 
      * **[Par Class](<./Par_Class.md> "Par Class")** \- an individual [parameter](<./Parameter.md> "Parameter").
    * **[ParGroupCollection Class](<./ParGroupCollection_Class.md> "ParGroupCollection Class")** (`OP.par`) - holds all the parameter groups for an OP. 
      * **[ParGroup Class](<./ParGroup_Class.md> "ParGroup Class")** \- an individual parameter group. 
        * **[ParGroupPulse Class](<./ParGroupPulse_Class.md> "ParGroupPulse Class")** \- an individual parameter group with a pulse par.
        * **[ParGroupUnit Class](<./ParGroupUnit_Class.md> "ParGroupUnit Class")** \- an individual parameter group with a unit par.
    * **[SequenceCollection Class](<./SequenceCollection_Class.md> "SequenceCollection Class")** (`OP.seq`) - holds all the sequences for an OP. 
      * **[Sequence Class](<./Sequence_Class.md> "Sequence Class")** \- describes and controls a set of sequential parameters. Sequential parameters will have a reference to one of these objects in their`sequence`member. 
        * **[SequenceBlock Class](<./SequenceBlock_Class.md> "SequenceBlock Class")** \- used to access the parGroups of a specific block (set of parGroups) in a sequence.
    * **[CHOP Class](<./CHOP_Class.md> "CHOP Class")** \- subclass of OPs defining [CHOP](<./CHOP.md> "CHOP") operators. 
      * **[Channel Class](<./Channel_Class.md> "Channel Class")** \- a [channel](<./Channel.md> "Channel") object. Accessed through a CHOP index or other CHOP members such as`chan`,`chans`etc.
      * **[Segment Class](<./Segment_Class.md> "Segment Class")** \- describes a single segment from a [Timer CHOP](<./Timer_CHOP.md> "Timer CHOP").
    * **[COMP Class](<./COMP_Class.md> "COMP Class")** \- a subclass of OPs defining [component](<./Component.md> "Component") operators. 
      * **[ObjectCOMP Class](<./ObjectCOMP_Class.md> "ObjectCOMP Class")** \- a subclass of COMPs defining [Objects](<./Object.md> "Object"), used to create and render 3D scenes.
      * **[PanelCOMP Class](<./PanelCOMP_Class.md> "PanelCOMP Class")** \- a subclass of COMPS defining [Panel Components](<./Panel_Component.md> "Panel Component"), used to create 2D UI elements. 
        * **[Panel Class](<./Panel_Class.md> "Panel Class")** \- a member of panelCOMPs containing all associated [panel values](<./Panel_Value.md> "Panel Value"). Accessed through`panelCOMP.panel`. 
          * **[PanelValue Class](<./PanelValue_Class.md> "PanelValue Class")** \- individual [panel values](<./Panel_Value.md> "Panel Value"). Accessed through the`panel`member of panelCOMPS and also in callbacks in the [Panel Execute DAT](<./Panel_Execute_DAT.md> "Panel Execute DAT").
        * **[ListAttributes Class](<./ListAttributes_Class.md> "ListAttributes Class")** \- a collection of [list attributes](<./ListAttribute_Class.md> "ListAttribute Class") used in a [ListCOMP](<./ListCOMP_Class.md> "ListCOMP Class"). 
          * **[ListAttribute Class](<./ListAttribute_Class.md> "ListAttribute Class")** \- contains attributes defining a cell in a [ListCOMP](<./ListCOMP_Class.md> "ListCOMP Class").
        * **[Actors Class](<./Actors_Class.md> "Actors Class")** \- describes the set of all Actor COMPs used by the Bullet Solver COMP and Nvidia Flex Solver COMP. used in a [BulletsolverCOMP](<./BulletsolverCOMP_Class.md> "BulletsolverCOMP Class") or [flexsolverCOMP](<./FlexsolverCOMP_Class.md> "FlexsolverCOMP Class").
        * **[Bodies Class](<./Bodies_Class.md> "Bodies Class")** \- a collection of [bodies](<./Body_Class.md> "Body Class") used in an [ActorCOMP](<./ActorCOMP_Class.md> "ActorCOMP Class"). 
          * **[Body Class](<./Body_Class.md> "Body Class")** \- a single body (physics object) used in an [ActorCOMP](<./ActorCOMP_Class.md> "ActorCOMP Class").
      * **[VFS Class](<./VFS_Class.md> "VFS Class")** \- a COMP's Virtual File System
        * **[VFSFile Class](<./VFSFile_Class.md> "VFSFile Class")** \- a virtual file contained within a Virtual File System.
    * **[DAT Class](<./DAT_Class.md> "DAT Class")** \- a subclass of OPs defining [DAT](<./DAT.md> "DAT") operators. 
      * **[Cell Class](<./Cell_Class.md> "Cell Class")** \- defines an individual cell of a [DAT](<./DAT.md> "DAT") table.
      * **[Peer Class](<./Peer_Class.md> "Peer Class")** \- describes the network connection originating a message in the callback functions found in [oscinDAT](<./OSC_In_DAT.md> "OSC In DAT"), [tcpipDAT](<./TCP/IP_DAT.md> "TCP/IP DAT"), [udpinDAT](<./UDP_In_DAT.md> "UDP In DAT"), [udtinDAT](<./UDT_In_DAT.md> "UDT In DAT").
    * **[MAT Class](<./MAT_Class.md> "MAT Class")** \- a subclass of OPs defining [MAT](<./MAT.md> "MAT") operators.
    * **[SOP Class](<./SOP_Class.md> "SOP Class")** \- a subclass of OPs defining [SOP](<./SOP.md> "SOP") operators. 
      * **[Attributes Class](<./Attributes_Class.md> "Attributes Class")** \- a collection of SOP [attributes](<./Attribute.md> "Attribute")
        * **[Attribute Class](<./Attribute_Class.md> "Attribute Class")** \- information about an entity such as its color, velocity, normal, and so on. 
          * **[AttributeData Class](<./AttributeData_Class.md> "AttributeData Class")** \- contains specific geometric Attribute values, associated with a Prim Class, Point Class, or Vertex Class.
      * **[Group Class](<./Group_Class.md> "Group Class")** \- describes groups lists of Prim Class or Point Class.
      * **[Points Class](<./Points_Class.md> "Points Class")** \- a collection of [points](<./Point_Class.md> "Point Class"). 
        * **[Point Class](<./Point_Class.md> "Point Class")** \- a single geometry [point](<./Point.md> "Point"). 
          * **[InputPoint Class](<./InputPoint_Class.md> "InputPoint Class")** \- a special point object used in [Point SOP](<./Point_SOP.md> "Point SOP") parameters.
      * **[Prims Class](<./Prims_Class.md> "Prims Class")** \- a collection of [primitives](<./Prim_Class.md> "Prim Class"). 
        * **[Prim Class](<./Prim_Class.md> "Prim Class")** \- a single geometry [primitive](<./Primitive.md> "Primitive"). 
          * **[Poly Class](<./Poly_Class.md> "Poly Class")** \- a subclass of Prim defining a geometry [polygon](<./Polygon.md> "Polygon").
          * **[Mesh Class](<./Mesh_Class.md> "Mesh Class")** \- a subclass of Prim defining a geometry [mesh](<./Mesh.md> "Mesh").
          * **[Bezier Class](<./Bezier_Class.md> "Bezier Class")** \- a subclass of Prim defining a set of Bezier curves.
          * **[Vertex Class](<./Vertex_Class.md> "Vertex Class")** \- a member of Prim defining a single geometry [vertex](<./Vertex.md> "Vertex").
    * **[TOP Class](<./TOP_Class.md> "TOP Class")** \- a subclass of OPs defining [TOP](<./TOP.md> "TOP") operators. 
      * **[CUDAMemory Class](<./CUDAMemory_Class.md> "CUDAMemory Class")** \- holds a reference to CUDA memory. 
        * **[CUDAMemoryShape Class](<./CUDAMemoryShape_Class.md> "CUDAMemoryShape Class")** \- describes the shape of a CUDA memory segment.
      * **[TextLine Class](<./TextLine_Class.md> "TextLine Class")** \- a line of text in the [Text TOP](<./Text_TOP.md> "Text TOP") or [Text SOP](<./Text_SOP.md> "Text SOP"), after it has been formatted. Contains various members about the line such as it's text, position etc.

### Helper Classes

The following helper objects are part of the [td module](<./Td_Module.md> "Td Module") and can thus be accessed anywhere, including expressions, without imports (e.g.`absTime.frame`). 
* **[AbsTime Class](<./AbsTime_Class.md> "AbsTime Class")** (`absTime`) - information about [absolute time](<./Absolute_Time.md> "Absolute Time")
  * **[App Class](<./App_Class.md> "App Class")** (`app`) - information about the TouchDesigner app, including version, installation folders, etc.
  * **[Project Class](<./Project_Class.md> "Project Class")** (`project`) - information about the current TouchDesigner session
  * **[TDU Class](<./TDU_Class.md> "TDU Class")** (`tdu`) - generic utilities for TouchDesigner not relating directly to TD objects. 
    * **[ArcBall Class](<./ArcBall_Class.md> "ArcBall Class")** (`tdu.ArcBall`) - encapsulates many aspects of 3D viewer interaction.
    * **[Camera Class](<./Camera_Class.md> "Camera Class")** (`tdu.Camera`) - maintains a 3D position and orientation for a camera and provides multiple methods for manipulating the camera's position and direction.
    * **[Color Class](<./Color_Class.md> "Color Class")** (`tdu.Color`) - holds a 4 component color
    * **[Dependency Class](<./Dependency_Class.md> "Dependency Class")** (`tdu.Dependency`) - used to create [Dependable](<./Dependency.md> "Dependency") Python data.
    * **[Matrix Class](<./Matrix_Class.md> "Matrix Class")** (`tdu.Matrix`) - holds a single 4x4 matrix for use in transformations. See [ObjectCOMP Class](<./ObjectCOMP_Class.md> "ObjectCOMP Class") for transforms of 3D objects.
    * **[Position Class](<./Position_Class.md> "Position Class")** (`tdu.Position`) - holds a 3 component position
    * **[Quaternion Class](<./Quaternion_Class.md> "Quaternion Class")** (`tdu.Quaternion`) - holds a quaternion object for 3D rotations
    * **[Timecode Class](<./Timecode_Class.md> "Timecode Class")** (`tdu.Timecode`) - holds a timecode value
    * **[Vector Class](<./Vector_Class.md> "Vector Class")** (`tdu.Vector`) - holds a 3 component vector
* **[Licenses Class](<./Licenses_Class.md> "Licenses Class")** (`licenses`) - information about installed [license](<./License_Class.md> "License Class") objects 
    * **[DongleList Class](<./DongleList_Class.md> "DongleList Class")** (`licenses.dongles`) - list of attached dongles 
      * **[Dongle Class](<./Dongle_Class.md> "Dongle Class")** \- an individual dongle connected to the system
    * **[License Class](<./License_Class.md> "License Class")** \- a single instance of an installed license 
      *         * **[ProductEntry Class](<./ProductEntry_Class.md> "ProductEntry Class")** \- a dongle entry for a single dongle connected to the system
  * **[MOD Class](<./MOD_Class.md> "MOD Class")** (`mod`) - access to modules located in TouchDesigner DATs
  * **[Monitors Class](<./Monitors_Class.md> "Monitors Class")** (`monitors`) - access to information about all connected display devices 
    * **[Monitor Class](<./Monitor_Class.md> "Monitor Class")** \- an individual display device
  * **[Runs Class](<./Runs_Class.md> "Runs Class")** (`runs`) - information about all delayed [run objects](<./Run_Class.md> "Run Class")
    * **[Run Class](<./Run_Class.md> "Run Class")** \- an individual delayed run object
  * **[SysInfo Class](<./SysInfo_Class.md> "SysInfo Class")** (`sysInfo`) - current system/hardware information
  * **[UI Class](<./UI_Class.md> "UI Class")** (`ui`) - information about application ui elements 
    * **[Colors Class](<./Colors_Class.md> "Colors Class")** (`ui.colors`) - application colors
    * **[Options Class](<./Options_Class.md> "Options Class")** (`ui.options`) - configurable ui options
    * **[Panes Class](<./Panes_Class.md> "Panes Class")** (`ui.panes`) - collection of all panes open in the editor 
      * **[Pane Class](<./Pane_Class.md> "Pane Class")** \- an individual pane object 
        * **[NetworkEditor Class](<./NetworkEditor_Class.md> "NetworkEditor Class")** \- subclass of Pane that displays a network editor
    * **[Preferences Class](<./Preferences_Class.md> "Preferences Class")** (`ui.preferences`) - collection of TouchDesigner preferences
    * **[Undo Class](<./Undo_Class.md> "Undo Class")** (`ui.undo`) - tools for interacting with the undo system, including creating script-based undo steps

### Standard Python Modules

The [`td`module](<./Td_Module.md> "Td Module") also automatically imports a number of helpful standard modules, allowing them to be accessed in expressions through their namespace (e.g.`math.cos(math.pi)`): 
* [`collections`](<https://docs.python.org/3.7/library/collections.html>) \- container datatypes
  * [`enum`](<https://docs.python.org/3.7/library/enum.html>) \- support for enumerations
  * [`inspect`](<https://docs.python.org/3.7/library/inspect.html>) \- inspect live objects
  * [`math`](<https://docs.python.org/3.7/library/math.html>) \- mathematical functions
  * [`re`](<https://docs.python.org/3.7/library/re.html>) \- regular expression operations
  * [`sys`](<https://docs.python.org/3.7/library/sys.html>) \- OS specific data and functions
  * [`traceback`](<https://docs.python.org/3.7/library/traceback.html>) \- stack utilities
  * [`warnings`](<https://docs.python.org/3.7/library/warnings.html>) \- warning control

### TouchDesigner Utility Modules and Python Utilities

The following contain extended Python utilities for use with TouchDesigner. 
* **[TDFunctions](<./TDFunctions.md> "TDFunctions")** \- A variety of utilities for advanced Python coding in TouchDesigner.
  * **[TDJSON](<./TDJSON.md> "TDJSON")** \- JSON utilities specific to TouchDesigner.
  * **[TDStoreTools](<./TDStoreTools.md> "TDStoreTools")** \- utilities for use with TouchDesigner's [Storage](<./Storage.md> "Storage") and [Dependency](<./Dependency.md> "Dependency") system.
  * **[TDResources](<./TDResources.md> "TDResources")** (`op.TDResources...`) - not a module, but does contain system resources that can be accessed via Python. It includes system [pop-up menu](<./TDResources.htm#Pop-Up_Menu> "TDResources"), [button pop-up menu](<./TDResources.htm#Button_Pop-Up_Menu> "TDResources"), [pop-up dialog](<./TDResources.htm#Pop-Up_Dialog> "TDResources"), and [mouse](<./TDResources.htm#Mouse> "TDResources") resources.

### 3rd Party Packages

**The following 3rd party packages are automatically installed with TouchDesigner.** They are not in the [td module](<./Td_Module.md> "Td Module"), so must be imported explicitly to be used in scripts. The name in parentheses is the actual package name used (e.g. to use OpenCV, write this at top of script:`import cv2`). For information on adding or installing other Python modules, see [Importing Modules](<./Introduction_to_Python_Tutorial.htm#Importing_Modules>). 
* **[asn1crypto](<https://pypi.org/project/asn1crypto/>)** (`asn1crypto`) - Parsing and serializing ASN.1 structures.
  * **[attr](<https://www.attr.org>)** (`attr`) - Classes without boilerplate.
  * **[Certifi](<https://pypi.org/project/certifi/>)** (`certifi`) - Root Certificates for validating the trustworthiness of SSL certificates while verifying the identity of TLS hosts.
  * **[CFFI](<https://cffi.readthedocs.io/en/latest/>)** (`cffi`) - Interaction with C code.
  * **[Chardet](<https://pypi.org/project/chardet/>)** (`chardet`) - The Universal Character Encoding Detector.
  * **[charset-normalizer](<https://pypi.org/project/charset-normalizer/>)** (`charset_normalizer`) - A library that helps you read text from an unknown charset encoding.
  * **[Cryptography](<https://cryptography.io/en/latest/#>)** (`cryptography`) - High level recipes and low level interfaces to common cryptographic algorithms.
  * **[decorator](<https://github.com/micheles/decorator>)** (`decorator`) - Define signature-preserving function decorators and decorator factories.
  * **[OAuthlib](<https://pypi.org/project/oauthlib/>)** (`oauthlib`) - Library to build OAuth and OpenID Connect servers.
  * **[opencv-python](<https://pypi.org/project/opencv-python/>)** (`cv2`) - Pre-built CPU-only OpenCV packages for Python.
  * **[depthai](<https://pypi.org/project/depthai/>)** (`depthai`) - Python bindings for C++ [depthai-core library](<https://docs.luxonis.com/projects/api/en/latest/>).
  * **[idna](<https://pypi.org/project/idna/>)** (`idna`) - Support for the Internationalised Domain Names in Applications (IDNA) protocol.
  * **[jsonpath](<https://pypi.org/project/jsonpath-ng/>)** (`jsonpath_ng`) - JSONPath tools for accessing and altering JSON structures.
  * **[jsonschema](<https://pypi.org/project/jsonschema/>)** (`jsonschema`) - jsonschema is an implementation of the [JSON Schema](<https://json-schema.org/>) specification for Python.
  * **[MWParserFromHell](<https://mwparserfromhell.readthedocs.io/en/latest/>)** (`mwparserfromhell`) - An easy-to-use and outrageously powerful parser for MediaWiki wikicode.
  * **[NumPy](<http://www.numpy.org>)** (`numpy`) - Fundamental package for scientific computing with Python.
  * **[OpenCV](<https://opencv.org>)** (`cv2`) - Open source computer vision.
  * **[packaging](<https://pypi.org/project/packaging/>)** (`packaging`) - Package tools including version handling, specifiers, markers, requirements, tags, utilities. Used for version string comparison.
  * **[pip](<https://pypi.org/project/pip/>)** (`pip`) - pip is the package installer for Python. You can use pip to install packages from the Python Package Index and other indexes.
  * **[ply](<https://www.dabeaz.com/ply/>)** (`ply`) - Parsing tools for lex and yacc.
  * **[Pygments](<https://pypi.org/project/Pygments/>)** (`pygments`) - A syntax highlighting package written in Python.
  * **[pyparsing](<https://pypi.org/project/pyparsing/>)** (`pyparsing`) - A library of classes that client code uses to construct parsing grammar directly in Python code.
  * **[pyrankvote](<https://pypi.org/project/pyrankvote/>)** (`pyrankvote`) - PyRankVote is a python library for different ranked-choice voting systems (sometimes called preferential voting systems) created by Jon Tingvold in June 2019.
  * **[pyrsistent](<https://pypi.org/project/pyrsistent/>)** (`pyrsistent`) - Pyrsistent is a number of persistent collections (by some referred to as functional data structures). Persistent in the sense that they are immutable.
  * **[PyYAML](<https://pyyaml.org/wiki/PyYAMLDocumentation>)** (`yaml`) - YAML parser and emitter.
  * **[Requests](<http://docs.python-requests.org/en/master/>)** (`requests`) - The only Non-GMO HTTP library for Python, safe for human consumption
  * **[Requests OAuthlib](<https://requests-oauthlib.readthedocs.io/en/latest/index.html>)** (`requests_oauthlib`) - Easy-to-use Python interface for building OAuth1 and OAuth2 clients
  * **[six](<https://pypi.org/project/six/>)** (`six`) - Python 2 and 3 compatibility utilities.
  * **[smartypants](<https://pypi.org/project/smartypants/>)** (`smartypants`) - a Python fork of [SmartyPants](<http://daringfireball.net/projects/smartypants/>).
  * **[tabulate](<https://pypi.org/project/tabulate/>)** (`tabulate`) - Pretty-print tabular data in Python.
  * **[urllib3](<https://urllib3.readthedocs.io/en/latest/>)** (`urllib3`) - HTTP client.
  * **[whats-that-code](<https://pypi.org/project/whats-that-code/>)** (`whats_that_code`) - programming language detection library.

### Installing Custom Packages and Modules

You can also install your own Python packages that are not included with TouchDesigner. For instructions, go [here](<./Category-Python.htm#Installing_Custom_Python_Packages> "Category:Python").
