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

def projWindowSettings(info):
	op(me.ipar.SetiComp.P1).openParameters()
def projWindowSettings1(info):
	op(me.ipar.SetiComp.P2).openParameters()
def projWindowSettings2(info):
	op(me.ipar.SetiComp.P3).openParameters()

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
def onProjWindow(info):
	device=op.pproj.op("WALL_PROJ1_WINDOW")
	state=me.ipar.states.Projwindow
	if bool(state) is not True:
		op(device).par.winopen.pulse()
		ui.status="The projector window is open"
	else:
		op(device).par.winclose.pulse()
		ui.status="The projector window is closed"
def onProjWindow1(info):
	device=op.pproj.op("WALL_PROJ2_WINDOW")
	state=me.ipar.states.Projwindow2
	if bool(state) is not True:
		op(device).par.winopen.pulse()
		ui.status="The projector window is open"
	else:
		op(device).par.winclose.pulse()
		ui.status="The projector window is closed"
def onProjWindow2(info):
	device=op.pproj.op("LED_OUT_WINDOW")
	state=me.ipar.states.Projwindow3
	if bool(state) is not True:
		op(device).par.winopen.pulse()
		ui.status="The projector window is open"
	else:
		op(device).par.winclose.pulse()
		ui.status="The projector window is closed"

def onOpenStoner(info):
	op.pproj.op("stoner").par.Open.pulse()
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
