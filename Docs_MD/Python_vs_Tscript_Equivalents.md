# Python vs Tscript Equivalents

## All Operators

### Commands

| Python  | TScript   
---|---|---  
Creating an OP ([Sphere SOP](<./Sphere_SOP.md> "Sphere SOP"))  |`op('/project1').create(sphereSOP)`|`cc /project1  
opadd SOP:sphere`Creating a named OP |`op('/project1').create(sphereSOP, 'mysphere')`|`cc /project1  
opadd SOP:sphere "mysphere"`Copying OPs (Nodes)  |`op('/project1').copy(op('out1'), name='out2')`|`opcp /project1/out1 out2`Deleting an OP |`op('mysphere').destroy()`|`cc /project1  
oprm "mysphere"`Renaming an OP |`op('mysphere').name = 'thesphere'`|`cc /project1  
opname "mysphere" "thesphere"`Changing an OP's type  |`op('mysphere').changeType(boxSOP)`|`cc /project1  
opchangetype "mysphere" SOP:box`Changing multiple OPs' types  |`list = ops('*sphere*')  
[s.changeType(boxSOP) for s in list]`|`cc /project1  
opchangetype "*sphere*" SOP:box`Setting an OP's comment  |`op('mysphere').comment = 'this is a sphere'`|`cc /project1  
opcomment -c "this is a sphere" "mysphere"`Changing an OP's parameter  |`op('mysphere').par.frequency = 10`|`cc /project1  
opparm "mysphere" frequency ( 10 )`Changing an OP's parameter  
with more than 1 value  |`s = op('mysphere')  
s.par.tx = 1  
s.par.ty = 2  
s.par.tz = 3`|`cc /project1  
opparm "mysphere" t( 1 2 3 )`Pulsing a parameter value  |`op('moviein1').par.cue.pulse()`|`opparm -p moviein1 cue (1)`Cooking an OP |`op('mysphere').cook()`|`cc /project1  
opcook "mysphere"`Saving an OP's data to a file  |`op('mysphere').save('sphere.tog')`|`cc /project1  
opsave "mysphere" "sphere.tog"`Changing an OP's [Render](<./Render_Flag.md> "Render Flag") and [Display Flags](<./Display_Flag.md> "Display Flag") on  |`s = op('mysphere')  
s.render = True  
s.display = True`|`cc /project1  
opset -r 1 -d 1 "mysphere"`Loading a [.tox file](<./.md> ".tox") into a COMP |`op('/project1').loadTox('geo1.tox')`|`cc /project1  
loadcomponent "geo1.tox"`Wiring operators together  |`Refer to the [Connector Class](<./Connector_Class.md> "Connector Class")`|`opwire command`Clicking gadgets (panel components)  |`op('slider1').click(.6, .7)`|`click slider1 .6 .7`Timeline Play/Pause  |`me.time.play = True/False`|`playback/playback -s`### Expressions

| Python  | TScript   
---|---|---  
Querying another OP's parameter  |`op('sphere1').par.tx`|`par("sphere1:tx")`Querying a parameter in the same OP |`me.par.tx`|`par("tx")`Getting Info CHOP channels from an OP  
without cooking it  |`passive(op('moviein1')).width`|`opinfop("moviein1", "resx")`Getting an OP's parent  |`parent()`|`opparent(".", 0)`Getting an OP's grand-parent  |`parent(2)`|`opparent(".", 1)`Getting an OP's name  |`me.name`|`$ON`Getting an OP's parent's name  |`parent().name`|`$OPN`Getting digits of an OP's name in its parameters  |`me.digits`|`$OD`Getting digits of an OP's parent's  
name in its parameters  |`parent().digits`|`$OPD`Getting digits of another OP's name  |`op("moviein1").digits`|`opdigits("moviein1")`Getting an OP's type  |`# returns an op object, not a string  
type(op('moviein1'))`|`optype("moviein1")`getting a unique random number each frame  |`tdu.rand(absTime.frame+.1)`|`rand($AF+.1)`getting a unique random number per numbered operator  |`tdu.rand(me.digits+.17)`|`rand($OD+.1)`Checking for an OP's existence  |`if op('moviein1'):`or`bool(op('moviein1'))`|`opexists('moviein1')`Getting the number of children of a COMP |`len(op('geo1').children)`|`opnumchildren("geo1")`Getting the number of inputs of a multi-input OP |`len(op('switch1').inputs)`|``Getting [Info CHOP](<./Info_CHOP.md> "Info CHOP") channels from an OP, width is a member  |`op('moviein1').width`|`opinfo("moviein1", "resx")`Conditional "if" in one line of a parameter  |`22 if me.time.frame<100 else 33`|`if($F<100,22,33)`Conditional "if" alternative  |`[33,22][me.time.frame<100]`|`if($F<100,22,33)`Convert space separated string to a list  |`tdu.split('Space separated string with "two word item"')`|``List comprehension  |`[c.name for c in root.children]`|``Conditional list comprehension  |`[c.name for c in root.children if c.name != 'perform']`|``Test operator type  |`type(root) == baseCOMP`|``Test operator family  |`isinstance(root, TOP)`|``### Time

"Absolute Time" is the time since you started your TouchDesigner process, not counting when your power button was off (top bar). 

| Python  | TScript   
---|---|---  
Retrieving a node's local frame number  |`me.time.frame`|`$F`Retrieving a node's local time in seconds  |`me.time.seconds`|`$T`Retrieving absolute time in frames  |`absTime.frame`|`$AF`Retrieving absolute time in seconds  |`absTime.seconds`|`$AT`### Storage in Python

Storage is the preferred way to work with persistent global data in Python, since it can store anything data type. 

| Python   
---|---  
Setting a value in storage of a component`n`|`n.store('keyname', 0.0)`Getting a value from storage  |`n.fetch('keyname')`### Variables

Variables are always text strings. 

| Python  | TScript   
---|---|---  
Setting a value  |`me.var('DESKTOP')`|`$DESKTOP`Setting a [Root Variable](<./Variables.htm#Root_Variables> "Variables") |`root.setVar('MEDIA', 'c:/MEDIA')`|`rvar MEDIA="c:/MEDIA"`Setting a [Component Variable](<./Variables.htm#Component_Variables> "Variables")  
at the current component  |`parent().setVar('MEDIA', 'c:/MEDIA')`|`cvar MEDIA="c:/MEDIA"`Setting a Component Variable  
at another component  |`op('/project1/geo1').setVar('MEDIA', 'c:/MEDIA')`|`cvar -p "/project1/geo1" MEDIA="c:/MEDIA"`Setting a [Path Variable](<./Variables.htm#Path_Variables> "Variables") | Set the Path Variable parameter of any parent component and use`me.var('name')`in the same way.  | Set the Path Variable parameter of any parent component.   
  
## For CHOPs

### Expressions

| Python  | TScript   
---|---|---  
Evaluate channel`chan1`at the current frame  |`op('wave1')['chan1'].eval()`_or if in parameter, simply:_`op('wave1')['chan1']`|`chop("wave1:chan1")`Get sample 8 of channel`chan1`|`op('wave1')['chan1'].eval(8)`|`chopi("wave1:chan1", 8)`Get the number of CHOP Channels  |`op('wave1').numChans`|`chopn("wave1")`Get the CHOP length  |`op('wave1').numSamples`|`chopl("wave1")`Get the third sample from the first channel  |`op('wave1')[0][2]`|`chopc("wave1", 0, 2)`Get the name of the 2nd channel  |`op('wave1')[1].name`|`chopname("wave1", 1)`Get the channel index of channel`chan1`|`op('wave1')['chan1'].index`|`chopindex("wave1:chan1")`## For DATs

### Expressions

| Python  | TScript   
---|---|---  
Get a cell value by index  |`op('table1')[2,3]`|`tab("table1", 2, 3)`Get a cell value by label  |`op('table1')['r1', 'c1']`|`tabrc("table1", r1, c1)`Get a cell value by row index, col label  |`op('table1')[2, 'product']`|`tabc("table1", 2, "product")`Cast cell to integer and float  |`int(op('table1')['month', 3])  
float(op('table1')['speed', 4])`|``Get the number of table rows  |`op('table1').numRows`|`tabnr("table1")`Get the number of table columns  |`op('table1').numCols`|`tabnc("table1")`Set a cell value by indeces or labels  |`op('table1')[3,4] = 'hello'  
op('table1')[2, 'answer'] = 'hello'  
op('table1')['month', 3] = 'july'`|`tabcell table1 rc 3 4 hello  
tabcell table1 rC 2 answer hello  
tabcell table1 Rc month 3 july`Set a cell value by label  |`op('table1')['r1', 'c1'] = 'abc'`|`tabcell "table1" RC r1 c1 "abc"`Copy a table to another table  |`op('table1').copy(op('fromTable'))`|`type fromTable >table1`Append a row to a table  |`op('table1').appendRow(['s1','s2', num])`|`echo string1 string2 num >table1`Append a column to a table  |`op('table1').appendCol(['s1','s2', num])`|``Access current cell in an [Evaluate DAT](<./Evaluate_DAT.md> "Evaluate DAT") |`me.inputCell`|`$V`Access neighboring cells in an Evaluate DAT |`me.inputCell.offset(1,2)`|`v($R+1,$C+2)`
