def onValueChange(par, prev):

	if prev!=par.eval() and par.eval() > 0:
		op("AnimationTimeControl/T/local/time").frame=2
		op("lightscaner1/speed1").par.resetpulse.pulse()

	return

