
def onPulse(par):
	if hasattr(me.parent(), par.name):
		getattr(me.parent(), par.name)()
	return
