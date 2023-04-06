import os
from subprocess import *
import math
import re

class ContentSystemBarClone:
	def __init__( self, ownerComp ):
		self.ownerComp=ownerComp
		return
	def GetModuleOp(self, frame):
		return op(self.ownerComp.par.Contentmodule)
	def GetTimelinePath(self, frame):
		return op(self.GetModuleOp(1)).op(self.GetModuleOp(1).name).op('AnimationTimeControl/T/local/time')
	def GetTimelineCurrentFrame(self, frame):
		if self.GetTimelinePath(1) is not None:
			return self.GetTimelinePath(1).op("clock")
		else:
			return ""
		pass
	def SetAnimationCursor(self):
		if self.GetTimelinePath(1) is not None:
			if self.ownerComp.op("CursorToSet").numChans > 0:
				frameToSet=self.ownerComp.op("CursorToSet")[0]
				self.GetTimelinePath(1).frame=int(frameToSet)
		pass

class ContentSystemBar:

	def __init__( self, ownerComp ):
		self.ownerComp=ownerComp
		self.activeModulesFromContentSystem=""
		return
	def Pushactive (self, myactivemods):
		if myactivemods!=self.activeModulesFromContentSystem:
			self.activeModulesFromContentSystem=myactivemods
			self.Update()
		pass

	def Update(self):
		self.ActiveModules.clear()
		for mymodule in re.split(r' ', str(self.activeModulesFromContentSystem)):
			ui.status=mymodule
			moduleOp=op.vcont.op(mymodule)
			if moduleOp is not None:
				self.ActiveModules.appendRow([mymodule])
		self.ownerComp.op("replicator1").par.recreateall.pulse()
			
	def GetModuleById(self, myid):
		moduleName=str(self.ActiveModules[myid,0])
		moduleOp=op.vcont.op(moduleName)
		fullPath=moduleOp.path
		return fullPath
	@property
	def Contentsystempath(self):
		return self.ownerComp.par.Contentsystempath
	@property		
	def ActiveModules(self):
		return self.ownerComp.op("activeModules")

	# @ActiveModules.setter
	# def ActiveModules(self,val):
	# 	self.ownerComp.par.Istestpatterns=bool(val)
	# 	__Istestpatterns=bool(val)
	# 	return self.ownerComp.par.Istestpatterns

