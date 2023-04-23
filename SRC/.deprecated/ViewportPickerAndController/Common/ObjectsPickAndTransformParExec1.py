
def onPulse(par):
	if hasattr(op.vp_obj_picker, par.name):
		getattr(op.vp_obj_picker, par.name)()
	return
