
def onSelectRow(info):
#	print(info)
	me.parent.curycueui.SetSelectedCue(info['row'])	
	pass

def onEditEnd(info):
    me.parent.curycueui.dock.Callback_cue_list_mode_list("edit", info)
    
#def onClick(info):

#	me.parent.curycueui.SetSelectedCue(info['row'])

