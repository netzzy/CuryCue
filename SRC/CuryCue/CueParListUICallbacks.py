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

def _isCooking(myOp):
	if myOp is None:
		return False
	if hasattr(myOp, "allowCooking") and not myOp.allowCooking:
		return False

	i=1
	while myOp.parent(i) is not None:
		parentOp=myOp.parent(i)
		if hasattr(parentOp, "allowCooking") and not parentOp.allowCooking:
			return False
		i+=1
	return True

def _setSelectedRow(ownerComp, row):
	if ownerComp is None:
		return False

	if hasattr(ownerComp.par, "Selectedrows"):
		ownerComp.par.Selectedrows="" if row is None else str(row)

	if not _isCooking(ownerComp):
		return False

	selectRow=getattr(ownerComp, "SelectRow", None)
	if selectRow is not None:
		try:
			selectRow(row)
			return True
		except Exception as e:
			print("SelectRow failed on {}: {}".format(ownerComp.path, e))

	lister=ownerComp.op("list/lister") if hasattr(ownerComp, "op") else None
	if lister is not None:
		selectRow=getattr(lister, "SelectRow", None)
		if selectRow is not None:
			try:
				selectRow(row)
				return True
			except Exception as e:
				print("SelectRow failed on {}: {}".format(lister.path, e))

		listerExt=getattr(lister.ext, "ListerExt", None)
		if listerExt is not None and hasattr(listerExt, "SelectRow"):
			try:
				listerExt.SelectRow(row)
				return True
			except Exception as e:
				print("ListerExt.SelectRow failed on {}: {}".format(lister.path, e))

	return False

def onEditEnd(info):
	_setSelectedRow(info['ownerComp'], info['row'])
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
