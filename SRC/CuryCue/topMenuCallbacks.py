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
	parent.curycueui.dock.BackupSqlDb(None)
	project.quit()
	

guides = False
grid = True


qqModes=dict.fromkeys(['isShowMode', 'isEditMode', 'isFixtureMode'], False)
qqExport=dict.fromkeys(['no', 'chop', 'vals'], False)
qqView=dict.fromkeys(['Head', 'Sidepanel', 'Bottom'], False)
def updateModesDict():
	i=0
	global qqModes
	for mode in qqModes.keys():
		if int(parent.curycueui.I.qqmodeswidget.par.Value0)==i:
			qqModes[mode]=True
		else:
			qqModes[mode]=False
		i+=1
updateModesDict()
def updateExportModes():
	i=0
	global qqExport
	for mode in qqExport.keys():
		if int(parent.curycueui.dock.par.Exportmode)==i:
			qqExport[mode]=True
		else:
			qqExport[mode]=False
		i+=1
updateExportModes()
def updateViews():
	global qqView
	for mode in qqView.keys():
		qqView[mode]=bool(getattr(parent.curycueui.par, mode))
updateViews()

	

def onSavePatch(info):
	parent.curycueui.dock.BackupSqlDb(None)
	project.save()
def onReloadCueSystem(info):
	parent.curycueui.dock.FullReloadCuryCue()	

def onSaveDb(info, myfilename=None):
	parent.curycueui.dock.BackupSqlDb(myfilename)
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



def editTopMenuCallbacks(info):
	op("/project1/ServerUI/topMenuCallbacksLocal").par.edit.pulse()
	pass
def editTopMenuTable(info):

	op("/project1/ServerUI/topMenuDefineLocal").par.edit.pulse()
	pass

def setQQMode(info):
	
	parent.curycueui.I.qqmodeswidget.par.Value0=int(info['index'])
	updateModesDict()
def setQQExportMode(info):
	newExportModeIndex=int(info['index'])
	parent.curycueui.dock.par.Exportmode=newExportModeIndex
	updateExportModes()
def setQQView(info):
	newModeIndex=int(info['index'])
	if newModeIndex == 3:
		parent.curycueui.par.Head^=True
	elif newModeIndex == 4:
		parent.curycueui.par.Sidepanel^=True
	elif newModeIndex == 5:
		parent.curycueui.par.Bottom^=True
	updateViews()

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
	updateModesDict()

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