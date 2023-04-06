def onSelectRow(info):
#	print(op(info['ownerComp']).par.Selectedrows)
#	me.parent.curycueui.SetSelectedInfoFix(info['row'])	
	pass


def onClick(info):
#	print (op(info['ownerComp']).par.Selectedrows)
#	me.parent.curycueui.SetSelectedInfoFix(info['row'])

	pass
def onClickDelete(info):
	parent.curycueui.dock.DeleteCueParByID(info['rowData']['id'], info['rowData']['id_fixture'], info['rowData']['Par'], info)

def onEditEnd(info):
	info['ownerComp'].SelectRow(info['row'])
	me.parent.curycueui.dock.Callback_edit_mode_pars("edit", info)

	pass
def onClickRight(info):
	parent.curycueui.CueListItemRightClicked=info['row']
	print (info['row'])
	me.parent(2).op('popMenu').Open(callback=onMenuChoice)
	
def onMenuChoice(info):
#	debug(info)
	print ("")
#	me.parent.curycueui.CuesMenuSelector(info)