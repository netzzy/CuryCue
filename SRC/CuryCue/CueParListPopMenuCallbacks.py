"""
PopMenu callbacks

Callbacks always take a single argument, which is a dictionary
of values relevant to the callback. Print this dictionary to see what is
being passed. The keys explain what each item is.

PopMenu info keys:
	'index': either item index or -1 for none
	'item': the item label in the menu list
	'row': the row from the wired dat input, if applicable
	'details': details provided by object that caused menu to open
"""

def onSelect(info):
	"""
	User selects a menu option
	"""
	

def onRollover(info):
	"""
	Mouse rolled over an item
	"""

def onOpen(info):
	"""
	Menu opened
	"""
	p1_1=0
	p1_2=0
	p2_2=0
	p2_1=0
	pIsGoto=0
	if parent.curycueui.AutoGotoContentComp:
		pIsGoto=1
	else:
		pIsGoto=0

	if int(parent.curycueui.dock.par.Parsselmode)==0:
		p1_1=1
	elif int(parent.curycueui.dock.par.Parsselmode)==1:
		p1_2=1
	if int(parent.curycueui.dock.par.Fades)==0:
		p2_1=1
	elif int(parent.curycueui.dock.par.Fades)==1:
		p2_2=1

	v = dict()
	v["Highlight only already created fields"] = p1_1
	v["Highlight all fields"] = p1_2
	v['Fade enabled'] = p2_1
	v['Fade disabled (for debugging)'] = p2_2
	v['Auto-switch to the network of the selected device'] = pIsGoto
	info['ownerComp'].par.Checkeditems = str(v)
	dis = []
	if parent.curycueui.CueListItemRightClicked == -1:
	    dis = ['Delete 1 field from key']
	dis.append('Edit fade')
	dis.append('Edit delay')
	dis.append('Edit delay')
	dis.append('Delete all selected')
	info['ownerComp'].par.Disableditems = str(dis)
	



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
	
	if info['index']==0:
		parent.curycueui.dock.Storeselected()
		
	if info["index"]==3 or info["index"]==4:
		parent.curycueui.dock.par.Parsselmode=info["index"]-3
	if info["index"]==5 or info["index"]==6:
		parent.curycueui.dock.par.Fades=info["index"]-5
	if info['index']==9:
		parent.curycueui.AutoGotoContentComp=not parent.curycueui.AutoGotoContentComp
	onOpen(info)
	print (info['index'])

def onLostFocus(info):
	"""
	Menu lost focus
	"""