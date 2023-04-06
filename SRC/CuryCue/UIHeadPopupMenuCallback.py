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
menu=['Записать выбранные поля в текущий ключ', 'Включать и выключать девайс синхронно', 'Переключать и оставить (макс.1)', 'Копить выбранные', 'Не переключать']

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

	
	menuDict=dict()
	
	for i in range (1, 5):
		if int(parent.curycueui.dock.par.Autoselectdevicebycomp)+1==i:
			menuDict[menu[i]]=1
		else:
			menuDict[menu[i]]=0

	info['ownerComp'].par.Highlighteditems=str([menu[0]])
	info['ownerComp'].par.Dividersafteritems=str([menu[0]])

	info['ownerComp'].par.Items=str(menu)
	info['ownerComp'].par.Checkeditems=str(menuDict)
	# p1_1=0
	# p1_2=0
	# p2_2=0
	# p2_1=0
	# if int(parent.curycueui.dock.par.Parsselmode)==0:
	# 	p1_1=1
	# elif int(parent.curycueui.dock.par.Parsselmode)==1:
	# 	p1_2=1
	# if int(parent.curycueui.dock.par.Fades)==0:
	# 	p2_1=1
	# elif int(parent.curycueui.dock.par.Fades)==1:
	# 	p2_2=1


	# v=dict()
	# v["Выделять только уже созданные"]=p1_1
	# v["Выделять все поля"]=p1_2
	# v['Fade включен']=p2_1
	# v['Fade выключен(для отладки)']=p2_2
	# info['ownerComp'].par.Checkeditems=str(v)
	# dis=[]
	# if parent.curycueui.CueListItemRightClicked==-1:
	# 	dis=['Редактировать fade', 'Редактировать delay', 'Удалить 1 поле из ключа', 'Удалить всё выделенное']
	# info['ownerComp'].par.Disableditems=str(dis)



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
	
	if info["index"]>0:
		parent.curycueui.dock.par.Autoselectdevicebycomp=info["index"]-1

	if info['item']==menu[0]:
		parent.curycueui.dock.Storeselected()

def onLostFocus(info):
	"""
	Menu lost focus
	"""