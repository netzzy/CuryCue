import os
import re


BaseClassesLocation=op.vp_obj_picker.op("SceneObjectBase").module

isDebugVerbose=False
#BaseClassesLocation.isDebugVerbose


class MeshObjClass (BaseClassesLocation.SceneToggleObject):
	def __init__(self, ownerComp):
		if isDebugVerbose:
			print ("MeshObjClass ")
		self.ownerComp=ownerComp
		BaseClassesLocation.SceneToggleObject.__init__(self)
		
		
		return
	@property
	def CycleIndex (self):
		v=0
		try:
			v=int(self.ownerComp.par.Index)
		except:
			v=0
		return float(v)
	@CycleIndex.setter
	def CycleIndex (self, v):
		self.ownerComp.par.Index=float(v)
		__CycleIndex=v
	@property
	def CycleMax(self):
		return self.ownerComp.par.Max
	@property
	def CycleDefVal(self):
		return self.ownerComp.par.Default

	def Cycle(self):
		print ("Index: {}".format(self.CycleIndex))
		val=self.CycleIndex+1
		if val > self.CycleMax:
			self.CycleIndex=0
		else:
			self.CycleIndex=val

	def Default (self):
		self.CycleIndex=self.CycleDefVal

class InternalClass:

	def __init__( self ):
		self.my=me.parent()
		return

