
def onSelectRow(info):
#	print(info)
	me.parent.curycueui.SetSelectedCue(info['row'])	
	pass

def onEditEnd(info):
    me.parent.curycueui.dock.Callback_cue_list_mode_list("edit", info)
    
#def onClick(info):

#	me.parent.curycueui.SetSelectedCue(info['row'])

#def onClickRight(info):
#	parent.curycueui.CueListItemRightClicked=info['row']
#	me.parent(2).op('popMenu').Open(callback=onMenuChoice)
	
#def onMenuChoice(info):
#	debug(info)
#	me.parent.curycueui.CuesMenuSelector(info)

