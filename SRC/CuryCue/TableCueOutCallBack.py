# me - this DAT
# scriptOp - the OP which is cooking
#
# press 'Setup Parameters' in the OP to call this function to re-create the parameters.
def onSetupParameters(scriptOp):
	return

# called whenever custom pulse parameter is pushed
def onPulse(par):
	return

def onCook(scriptOp):
	if hasattr(parent.curycue.ext, "CuryCueClass"): 	
		scriptOp.clear()
		for cue in parent.curycue.LocalCueData:
			manualFrameBind=cue.frame_bind
				 
			scriptOp.appendRow([cue.id, int(cue.order), cue.name, cue.memo, cue.linked, manualFrameBind] ) 

	#scriptOp.copy(scriptOp.inputs[0])	# no need to call .clear() above when copying
	#scriptOp.insertRow(['color', 'size', 'shape'], 0)
	#scriptOp.appendRow(['red', '3', 'square'])
	#scriptOp[1,0] += '**'

	return
