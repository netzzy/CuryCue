def onValueChange(par, prev):

	if prev!=par.eval() and par.eval() > 0:
		op("AnimationTimeControl/T/local/time").frame=1
		me.parent().Play()
	return

