# me - this DAT
# 
# frame - the current frame
# state - True if the timeline is paused
# 
# Make sure the corresponding toggle is enabled in the Execute DAT.

def onStart():
	return

def onCreate():
	return

def onExit():
	return

def onFrameStart(frame):
	if op.vp_obj_picker.MoveByKeyKey.state is True:
		op.vp_obj_picker.MoveByArrows()
	return

def onFrameEnd(frame):
	return

def onPlayStateChange(state):
	return

def onDeviceChange():
	return

def onProjectPreSave():
	return

def onProjectPostSave():
	return

	