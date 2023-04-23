inFloatingpaneOrFixed=True

def onNdiTestPatterns(info):
	op.cam.par.Test.pulse()

def laserEnableOutput(info):
	op.laz_tx.par.Enableout.pulse()
	pass
def laserDisableOutput(info):
	op.laz_tx.par.Disableout.pulse()
	pass
def onMIDIset(info):
	op("/project1/VideoProjectorContent/sel").openParameters()
def isProjWindowOpen():
	return bool(me.ipar.states.Projwindow)
def isProjWindowOpen2():
	return bool(me.ipar.states.Projwindow2)
def isProjWindowOpen3():
	return bool(me.ipar.states.Projwindow3)

def projWindowSettings(info):
	op(me.ipar.SetiComp.P2).openParameters()
def projWindowSettings1(info):
	op(me.ipar.SetiComp.P3).openParameters()
def projWindowSettings2(info):
	op(me.ipar.SetiComp.P4).openParameters()

def onProjBlind(info):
	if bool(me.ipar.states.Projblind) is not True:
		op.pproj.op("FREEZER_NULL").lock=True
		
		ui.status="The projector output is frozen on the current frame"
	else: 
		op.pproj.op("FREEZER_NULL").lock=False
		ui.status="The projector output is unfrozen"
def OS_ENV_IMPORTER(info):
	op.Env.openParameters()
def Autoprojtoggle(info):
	op.p.par.Autoopenproj=bool(op.p.par.Autoopenproj)^True

def Autocontroltoggle(info):
	op.p.par.Autoopencontrol=bool(op.p.par.Autoopencontrol)^True	
def onNdiDroidSwitch (info):
	op.cam.par.Cam1=int(bool(int(op.cam.par.Cam1))^True)
	pass

def onVCamSwitch (info):
	op.cam.par.Cam2=int(bool(int(op.cam.par.Cam2))^True)
def onAdbCam(info):
	op.ssui.par.Tab=3
	pass
def onProjWindow(info):
	print (me.ipar.SetiComp.P1)
	if bool(me.ipar.states.Projwindow) is not True:
		op(me.ipar.SetiComp.P1).par.winopen.pulse()
		ui.status="The projector window is open"
	else:
		op(me.ipar.SetiComp.P1).par.winclose.pulse()
		ui.status="The projector window is closed"
def onProjWindow1(info):
	print (me.ipar.SetiComp.P2)
	if bool(me.ipar.states.Projwindow2) is not True:
		op(me.ipar.SetiComp.P2).par.winopen.pulse()
		ui.status="The projector window is open"
	else:
		op(me.ipar.SetiComp.P2).par.winclose.pulse()
		ui.status="The projector window is closed"
def onProjWindow2(info):
	print (me.ipar.SetiComp.P3)
	if bool(me.ipar.states.Projwindow3) is not True:
		op(me.ipar.SetiComp.P3).par.winopen.pulse()
		ui.status="The projector window is open"
	else:
		op(me.ipar.SetiComp.P3).par.winclose.pulse()
		ui.status="The projector window is closed"

def onOpenStoner(info):
	op.pproj.op("stoner").par.Open.pulse()
	pass
def onOpenStoner1_1(info):
	op.pproj.op("stoner2").par.Open.pulse()
	pass
def onOpenStoner1_2(info):
	op.pproj.op("stoner3").par.Open.pulse()
	pass
def onOpenStoner2_1(info):
	op.pproj.op("stoner4").par.Open.pulse()
	pass
def onOpenStoner2_2(info):
	op.pproj.op("stoner5").par.Open.pulse()
	pass


def openCompPane(name):
	global inFloatingpaneOrFixed
	if inFloatingpaneOrFixed:
		p = ui.panes.createFloating(type=PaneType.NETWORKEDITOR, name=op(name).name)
		p.owner=op(name)
	else:
		ui.panes[0].owner=op(name)

def onVideoContent(info):
	openCompPane(op.vcont.path)
	
	pass
def onP(info):
	openCompPane(op.pproj.path)
	
	pass
def onSui(info):
	openCompPane(ipar.SetiComp.Sui)
	pass
def onSmsui(info):
	openCompPane(ipar.SetiComp.Smsui)
	pass
def onPpar(info):
	op(ipar.SetiComp.P).openParameters()
def onLpar(info):
	op(ipar.SetiComp.L).openParameters()
def onP1(info):
	openCompPane(ipar.SetiComp.P1)
	pass
def onP2(info):
	openCompPane(ipar.SetiComp.P2)
	pass

def onL(info):
	openCompPane(ipar.SetiComp.L)
	pass
def onA(info):
	openCompPane(ipar.SetiComp.A)
	pass
def onL1(info):
	openCompPane(ipar.SetiComp.L1)
	pass
def onC(info):
	# openCompPane(ipar.SetiComp.C)
	openCompPane("/project1/SEQUENCE/SequenceInside")
	pass
def onM(info):
	openCompPane(ipar.SetiComp.M)
	pass
def onCQ(info):
	openCompPane(ipar.SetiComp.Cq)
	pass
def onCQUI(info):
	openCompPane(ipar.SetiComp.Cqui)
	pass
