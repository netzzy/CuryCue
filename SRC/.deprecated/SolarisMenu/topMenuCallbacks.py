import os
import glob
import re
import datetime
import time
import fnmatch
"""
TopMenu callbacks

Callbacks always take a single argument, which is a dictionary
of values relevant to the callback. Print this dictionary to see what is
being passed. The keys explain what each item is.

TopMenu info keys:
	'widget': the TopMenu widget
	'item': the item label in the menu list
	'index': either menu index or -1 for none
	'indexPath': list of parent menu indexes leading to this item
	'define': TopMenu define DAT definition info for this menu item
	'menu': the popMenu component inside topMenu
"""

#################################
# exampleMenuDefine callbacks

def onQuit(info):
	"""
	A simple menu item callback, named in the Top Menu DAT table
	"""
	debug('QUIT!')

guides = False
grid = True

inFloatingpaneOrFixed=False

def onSavePatch(info):
	project.save()
def onReloadCueSystem(info):
	parent.curycueui.dock.FullReloadCuryCue()	

def onSaveDb(info, myfilename=None):
	parent.curycueui.dock.BackupSqlDb(myfilename)
def loadMysqlFile(file):
	onSaveDb([], myfilename="toUndo")
	parent.curycueui.dock.DisconnectDb()
	file_name = "{}/db/{}.{}".format(project.folder, file, "sql")
	exec_string="{}/db/mysql.exe -uroot curycue <{}".format(project.folder, file_name)
	run('import os')
	run('os.system("{}")'.format(exec_string), delayFrames=10)
	ui.status="Loaded {}".format(file_name)
	run('op("{}").FullReloadCuryCue()'.format(parent.curycueui.dock.path), delayFrames=300)
	# op.curycue.FullReloadCuryCue()	
	
def onSetting(info):
	"""
	A menu item callback that works on multiple menu items. The checkboxes in
	the menu evaluate the global guides and grid variables above to determine
	their state. The expressions used to evaluate the checkbox state are
	defined in the Top Menu DAT.
	"""
	global guides, grid
	if info['item'] == 'Show Guides':
		guides = not guides
	elif info['item'] == 'Show Grid':
		grid = not grid
def onPaneMode(info):
	global inFloatingpaneOrFixed
	inFloatingpaneOrFixed=not inFloatingpaneOrFixed
def onReload(info):
	op("topMenu/topMenu/reloadmenu").run()

def getRecentFiles(info):
	"""
	A rowCallback used in the Top Menu DAT table to automatically generate rows.
	These callbacks must return a dictionary or list of dictionaries that mimic
	the columns in the Top Menu DAT. Dictionaries only need the columns with
	data in them, but must have corresponding columns in the Top Menu DAT in
	order to be recognized.
	"""
	dir_name = project.folder+"/db/"
	list_of_files = filter( os.path.isfile,
                        glob.glob(dir_name + '*.sql') )
	list_of_files = sorted( list_of_files,
                        key = os.path.getmtime)
	list_of_files.reverse()

	#files_dir=fnmatch.filter(os.listdir(project.folder+"/db"), '*.sql')
	files_list=list()
	i=0
	for myfile in list_of_files:
		#(filename, ext)=re.split('\.',myfile)
		(fullpath, filename)=re.split(r'\\', myfile)
		(filename, ext)=re.split('\.', filename)
		
		files_list.append({'item2':filename})
		i+=1
		if i> 3:
			break
		
	return files_list

def openCompPane(name):
	if inFloatingpaneOrFixed:
		p = ui.panes.createFloating(type=PaneType.NETWORKEDITOR, name=op(name).name)
		p.owner=op(name)
	else:
		ui.panes[0].owner=op(name)

def onP(info):
	openCompPane(ipar.SetiComp.P)
	pass
def onP1(info):
	openCompPane(ipar.SetiComp.P1)
	pass
def onP2(info):
	openCompPane(ipar.SetiComp.P2)
	pass

def onL(info):
	openCompPane(ipar.SetiComp.L)
	pass
def onA(info):
	openCompPane(ipar.SetiComp.A)
	pass
def onL1(info):
	openCompPane(ipar.SetiComp.L1)
	pass
def onC(info):
	openCompPane(ipar.SetiComp.C)
	pass
def onM(info):
	openCompPane(ipar.SetiComp.M)
	pass
def onCQ(info):
	openCompPane(ipar.SetiComp.Cq)
	pass
def onCQUI(info):
	openCompPane(ipar.SetiComp.Cqui)
	pass


# standard menu callbacks

def onSelect(info):
	"""
	User selects a menu option
	"""
	indexPath=info['define']['indexPath']
	if len(indexPath) >2:
		if indexPath[0]==0 and indexPath[1]==2:
			loadMysqlFile(info['define']['name'])
	

def onRollover(info):
	"""
	Mouse rolled over an item
	"""

def onOpen(info):
	"""
	Menu opened
	"""

def onClose(info):
	"""
	Menu closed
	"""

def onMouseDown(info):
	"""
	Item pressed
	"""

def onMouseUp(info):
	"""
	Item released
	"""

def onClick(info):
	"""
	Item pressed and released
	"""

def onLostFocus(info):
	"""
	Menu lost focus
	"""