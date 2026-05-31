# Application Shortcuts

There are two types of [Shortcuts](<./Shortcut.md> "Shortcut"): 
* **[Panel Shortcuts](<./Panel_Shortcuts.md> "Panel Shortcuts")** that you create for any custom built panels and
  * **Application Shortcuts** (described here) that are built-in to TouchDesigner's authoring interface.


The most important Application Shortcuts (as in [Designer Mode](<./Designer_Mode.md> "Designer Mode")) are: 
* Space bar stops and starts the timeline.
  * Right-arrow steps forward one frame.
  * Left-arrow steps back one frame.


(The keys are different in [Panel Shortcuts](<./Panel_Shortcuts.md> "Panel Shortcuts").) 

The **Application Shortcuts** are defined in a DAT table with 3 columns: 
* Column 1: label
  * Column 2: key
  * Column 3: optional command

### Overwriting Shortcuts

Optional shortcut overrides table can be added to a text file located at:`[app](<./App_Class.md> "App Class").preferencesFolder/TouchShortcuts.txt`If the file does not exist, no shortcut overrides are currently defined. 

The text file must be formatted with the same 3 columns and contain the same label of which Application Shortcut to replace in the first column. For Application Shortcuts starting with general, the third column must not be modified. 

To just override files in a specific toe file, in Perform Mode only, lock the DAT located in /local/shortcuts and edit the entries as necessary. 

To disable a shortcut entirely, leave the shortcut in place, and simply blank out its corresponding command. 

### Default Shortcuts

The following table is searched for each keyboard stroke until a match is found. (000 means no key is defined.) The default shortcuts are listed in a file, read into TouchDesigner when it starts from:`[app](<./App_Class.md> "App Class").configFolder/TouchShortcuts.txt`label  | key  | command   
---|---|---  
general.pause  | space  | space   
general.forward  | left  | left   
general.backward  | right  | right   
general.cooking  | ctrl.space  | offon   
general.F1  | F1  | F1   
general.F2  | F2  | F2   
general.F3  | F3  | F3   
general.F4  | F4  | F4   
general.F5  | F5  | F5   
general.F6  | F6  | F6   
general.F7  | F7  | F7   
general.F8  | F8  | F8   
general.F9  | F9  | F9   
general.F10  | F10  | F10   
general.F11  | F11  | F11   
general.F12  | F12  | F12   
general.AF1  | alt.F1  | AF1   
general.AF2  | alt.F2  | AF2   
general.AF3  | alt.F3  | AF3   
general.AF4  | alt.F4  | AF4   
general.AF5  | alt.F5  | AF5   
general.AF6  | alt.F6  | AF6   
general.AF7  | alt.F7  | AF7   
general.AF8  | alt.F8  | AF8   
general.AF9  | alt.F9  | AF9   
general.AF10  | alt.F10  | AF10   
general.AF11  | alt.F11  | AF11   
general.AF12  | alt.F12  | AF12   
textport.back.history  | up  |   
textport.forward.history  | down  |   
textport.search  | ctrl.f  |   
network.toggle.render  | r  |   
network.toggle.bypass  | b  |   
network.toggle.display  | d  |   
network.new  | alt.n  |   
network.jump.down  | enter  |   
network.dive  | i  |   
network.jump.up  | u  |   
network.cancel  | esc  |   
network.color.palette  | c  |   
network.edit.expose  | e  |   
network.frame  | f  |   
network.frame.selected  | F  |   
network.home  | h  |   
network.home.selected  | H  |   
network.home.current  | 000  |   
network.layout  | L  |   
network.layout.all  | l  |   
network.add.group  | G  |   
network.open.groups  | g  |   
network.name  | n  |   
network.local.time  | 000  |   
network.load.component  | X  |   
network.overview  | o  |   
network.parameters  | p  |   
network.connect.style  | s  |   
network.show.datalinks  | x  |   
network.mode  | t  |   
network.hide  | D  |   
network.expose.all  | E  |   
network.select.all  | ctrl.a  |   
network.copy  | ctrl.c  |   
network.paste  | ctrl.v  |   
network.cut  | ctrl.x  |   
network.delete  | del  |   
network.find  | ctrl.f  |   
network.browser  | ctrl.b  |   
network.search  | alt.s  |   
network.switchto.net  | alt.1  |   
network.switchto.panel  | alt.2  |   
network.switchto.geoview  | alt.3  |   
network.switchto.topview  | alt.4  |   
network.switchto.chopview  | alt.5  |   
network.switchto.keyframer  | alt.6  |   
network.switchto.parm  | alt.7  |   
network.switchto.geoss  | alt.8  |   
network.switchto.textport  | alt.9  |   
network.pane.clone  | alt.shift.c  |   
network.pane.stow  | alt.\  |   
network.pane.splitlr  | alt.[  |   
network.pane.splittb  | alt.]  |   
network.pane.fullscreen  | alt.`|   
network.pane.close  | alt.z  |   
network.pane.linkplus  | alt.+  |   
network.pane.linkminus  | alt.-  |   
network.list.down  | j  |   
network.list.up  | k  |   
network.list.right  | .  |   
network.list.left  | ,  |   
network.add.operator  | tab  |   
network.edit.prefs  | 000  |   
network.license.manager  | alt.k  |   
network.winplacement  | alt.w  |   
network.new.project  | ctrl.n  |   
network.explorer  | alt.e  |   
network.channel.exports  | alt.x  |   
network.console  | alt.c  |   
network.export.movie  | ctrl.m  |   
network.midimapper  | alt.d  |   
network.beat  | 000  |   
network.open.viewer  | v  |   
network.show.version  | alt.shift.v  |   
network.align.area.keepsize  | 000  |   
network.align.area.resize  | 000  |   
network.cascade.area.keepsize  | 000  |   
network.layout.all.pack  | 000  |   
network.reset.tile.sizes  | 000  |   
network.normalize.tile.sizes  | 000  |   
network.import.file  | ctrl.i  |   
network.snap.grid.selection  | 000  |   
network.snap.grid.all  | 000  |   
network.activate.viewers  | a  |   
network.activatealways.viewers  | alt.a  |   
network.palette.browse  | alt.l  |   
network.channel.browse  | 000  |   
group.add.group  | G  |   
group.select.all  | a  |   
group.plus  | \+  |   
group.minus  | \-  |   
group.equals  | =  |   
app.operator.browse  | alt.o  |   
app.groups  | alt.g  |   
app.help  | alt.h  |   
app.load  | ctrl.o  |   
app.macros  | alt.m  |   
app.bookmarks  | alt.b  |   
app.quit  | ctrl.q  |   
app.save  | ctrl.s  |   
app.saveas  | ctrl.shift.s  |   
app.textport  | alt.t  |   
app.variables  | alt.v  |   
app.performance  | alt.y  |   
chopviewer.home  | h  |   
chopviewer.hadapt  | H  |   
chopviewer.vadapt  | V  |   
chopviewer.timebar  | t  |   
chopviewer.timescroll  | c  |   
chopviewer.labels  | l  |   
chopviewer.extend  | x  |   
chopviewer.dots  | d  |   
chopviewer.handles  | n  |   
chopviewer.grid  | g  |   
chopviewer.units  | u  |   
chopviewer.editmenu  | e  |   
chopviewer.scopemenu  | s  |   
chopviewer.precise  | p  |   
timeslice.reset.minmax  | r  |   
timeslice.home  | h  |   
timeslice.precise  | p  |   
keyframer.home  | h  |   
keyframer.home.selected  | H  |   
keyframer.home.horizontal  | F  |   
keyframer.home.vertical  | V  |   
keyframer.longnames  | n  |   
keyframer.scalehandle  | tab  |   
keyframer.toggle.selected.ties  | t  |   
keyframer.delete.selected.key  | del  |   
keyframer.copy.selected.key  | ctrl.c  |   
keyframer.paste.selected.key  | ctrl.v  |   
keyframer.timeline.next.key  | ctrl.right  |   
keyframer.timeline.prev.key  | ctrl.left  |   
keyframer.add.closest  | alt.LMB  |   
keyframer.add.selected  | alt.MMB  |   
keyframer.add.all  | alt.RMB  |
