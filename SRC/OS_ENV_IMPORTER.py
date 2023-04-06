import os

class InternalClass:

	def __init__( self ):
		self.my=me.parent()
		self.EnvVars={}
		self.Update()
		print ("Env variables module initialized")
		
		return



	def Update (self):
		for i in range (1, 16):
			vName=getattr(self.my.par, "Var"+str(i))
			vVar=getattr(self.my.par, "Value"+str(i))
			vDef=getattr(self.my.par, "Valdef"+str(i))
			if str(vName) != "":
				envVal=""
				
				try:
					envVal=os.environ[str(vName)]
				except:
					envVal=vVar
					print ("{} loaded not from OS envs :( " .format (vName))

				vVar.val=envVal
				
			else:
				vVar.val=vDef.val
			if str(vName) != "":
				self.EnvVars[str(vName)]=vVar.val
	def GetPar(self, p):
		try:
			return self.EnvVars[p]
		except: 
			return ""
	def Store (self):
		for i in range (1, 16):
			vName=getattr(self.my.par, "Var"+str(i))
			vVar=getattr(self.my.par, "Value"+str(i))
			
			if str(vName) != "":
				command='setx '+vName.val+ " "+ vVar.val +"\n\r"
				os.system(command)
		ui.messageBox('Warning!!!', 'Project needs to be reloaded, or env variables will be not updated!!!')

	def UpdateInternal ( self) :
		for i in range (1, 16):
			vName=getattr(self.my.par, "Var"+str(i))
			vVar=getattr(self.my.par, "Value"+str(i))
			if str(vName) != "":
				self.EnvVars[str(vName)]=vVar.val
		print ("Env vars updated, but not stored")
		
		
		return 
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
			if str(vName) != "":
				vVar.label=vName.val
			else:
				vVar.label="Value"+str(i)