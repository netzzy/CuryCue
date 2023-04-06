import os
import re
class InternalClass:

	def __init__( self ):
		self.my=me.parent()
#		self.my.par.Exportmode=0
		self.slidersRoute=dict([
#		['s1', ['/project1/CuryCueUI/BotMenu/ProjBrightSlider', "Value0"]],
#		['s3', ['/project1/CuryCueUI/BotMenu/LaserGeoCarve', "Value0"]],
#		['s2', ['/project1/CuryCueUI/BotMenu/LaserBright', "Value0"]],
#		['s8', ['/project1/VideoProjectorContent/LaserPatterns4_4', "Annigilatorturb"]]
		])
		run('op("{}").Init()'.format(self.my.path), delayFrames=30)
		return
	def Init(self):
		for k in self.slidersRoute.keys():
			try:
				op.MIDI.ProcessSlider(str(k), op("SlidersInput")[str(k)], 0)
				ui.status="Midi init ok"
			except: 
				ui.status="Ð¥ÑƒÐ¹Ð½Ñ Ñ MIDI"
		
	def Gocue(self):
		self.MidiWave(0)
		op.curycue.Gonextcue()
	def Backcue(self):
		self.MidiWave(1)
		op.curycue.Goprevcue()
	def Cursorforward(self):
		op.curycue.SKIPCUE=1
		op.curycue.Gocue()
		op.curycue.SKIPCUE=0
	def Cursorbackward(self):
		op.curycue.SKIPCUE=1
		op.curycue.Gocue(dir="back")
		op.curycue.SKIPCUE=0
	def ProcessSlider(self, chname, val, prev):
		#print (chname, val, prev)
		if chname in self.slidersRoute.keys():
			(targetNode, targetPar)=self.slidersRoute[chname]
			if hasattr(op(targetNode), "par"):
				if hasattr(op(targetNode).par, targetPar):
					setattr(op(targetNode).par, targetPar, val)
		pass
	def Rec(self):
		self.my.par.Rec=True
		self.my.op("REC_TIMER").par.start.pulse()
		op.curycue.Storeselected()
		pass
	def Play(self):
		pass
		
	def Stop(self):
		pass
	def Setbutton(self):
		ui.status="Set button"
		op.curycue.SetCurrentFrameForAutoCueRequest=True
	def Cycle(self):
		if op.curycue.par.Isframebindenabled==1:
			op.curycue.par.Isframebindenabled=0
		else:
			op.curycue.par.Isframebindenabled=1
	def RewindToStart(self):

		self.MidiWave(1)
	def Update (self):
		if int(self.my.par.Exportmode)  > 0:
			self.my.par.Cycle=1
		else: 
			self.my.par.Cycle=0
		#myExportMode=op("ExportMode").text

		#if myExportMode != self.ExportMode:
		#	if myExportMode == "NoExport":
		#		self.UpdateParValueExport=False
		#		self.setNoExportMode()
		#	elif myExportMode == "ChopExport":
		#		self.UpdateParValueExport=False
		#		self.setChopExport()
		#	elif myExportMode == "ValueExport":
		#		self.UpdateParValueExport=True
		#		self.setValueExport()

		#if myExportMode == "ValueExport" and self.UpdateParValueExport is True:
		#	self.ParValueExport()

		#self.ExportMode=myExportMode
		return
	def MidiWave(self, dir):
		if int(dir)==0:
			self.my.op("MidiWave").par.Waveforward.pulse()
		else:
			self.my.op("MidiWave").par.Waveback.pulse()
# 	def ParValueExport(self):
# 		myChopNode=op("EXPORT")
# 		for r in myChopNode.chans():
# 			myName=r.name
# 			myValue=r.eval()
# 			if re.search(":", myName):
# 				(myExportPath, myExportPar)=re.split(":", myName)
# #				print ("%s, %s"%(myExportPath, myExportPar))
# 				if op(myExportPath) is not None and hasattr(op(myExportPath).par, str(myExportPar)) is True:
# 					setattr(op(myExportPath).par, str(myExportPar), myValue)
# 		return 

