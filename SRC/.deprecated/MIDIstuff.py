import os
import re
class InternalClass:

	def __init__( self ):
		self.my=me.parent()
#		self.my.par.Exportmode=0
		return

	def SetNextExportMode(self):
		if int (self.my.par.Exportmode) < 2:
			self.my.par.Exportmode=int (self.my.par.Exportmode)+1
		else:
			self.my.par.Exportmode=0
		return
	def SetPrevExportMode(self):
		if int (self.my.par.Exportmode) > 0:
			self.my.par.Exportmode=int (self.my.par.Exportmode)-1
		else:
			self.my.par.Exportmode=2
		return	
	def RecPos(self):
		op(op.KF1).InsertKeys()
	def Play(self):
		op.TC.Play()
		
	def Stop(self):
		op.TC.Stop()
		
	def RewindToStart(self):
		op.TC.SetTimeFrame(0)
		self.Stop()
		op.TC.Rewind()
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
	def setNoExportMode(self):
		op("EXPORT").export=False
		return 
	def setChopExport(self):
		op("EXPORT").export=True
		return 
	def setValueExport(self):
		op("EXPORT").export=False
		self.UpdateParValueExport=True
		self.ParValueExport()
		return 
	def ParValueExport(self):
		myChopNode=op("EXPORT")
		for r in myChopNode.chans():
			myName=r.name
			myValue=r.eval()
			if re.search(":", myName):
				(myExportPath, myExportPar)=re.split(":", myName)
#				print ("%s, %s"%(myExportPath, myExportPar))
				if op(myExportPath) is not None and hasattr(op(myExportPath).par, str(myExportPar)) is True:
					setattr(op(myExportPath).par, str(myExportPar), myValue)
		return 


	def UpdateOld (self):
		for i in range (1, 16):
			vName=getattr(self.my.par, "Var"+str(i))
			vVar=getattr(self.my.par, "Value"+str(i))
			vDef=getattr(self.my.par, "Valdef"+str(i))
			if str(vName) is not "":
				envVal=""
				try:
					envVal=os.environ[str(vName)]
				except:
					envVal=vVar

				vVar.val=envVal
			else:
				vVar.val=vDef.val
	def Store (self):
		for i in range (1, 16):
			vName=getattr(self.my.par, "Var"+str(i))
			vVar=getattr(self.my.par, "Value"+str(i))
			
			if str(vName) is not "":
				command='setx '+vName.val+ " "+ vVar.val +"\n\r"
				os.system(command)
		ui.messageBox('Warning!!!', 'Project needs to be reloaded, or env variables will be not updated!!!')


	def Copy (self):
		for i in range (1, 16):
			vName=getattr(self.my.par, "Var"+str(i))
			vVar=getattr(self.my.par, "Value"+str(i))
			vDef=getattr(self.my.par, "Valdef"+str(i))
			vDef.val=vVar.val
	def Rename (self):
		for i in range (1, 16):
			vName=getattr(self.my.par, "Var"+str(i))
			vVar=getattr(self.my.par, "Value"+str(i))
			vDef=getattr(self.my.par, "Valdef"+str(i))
			if str(vName) is not "":
				vVar.label=vName.val
			else:
				vVar.label="Value"+str(i)