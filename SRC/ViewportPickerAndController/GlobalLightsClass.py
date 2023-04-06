import os
import re


BaseClassesLocation=op.vp_obj_picker.op("SceneObjectBase").module

isDebugVerbose=True
#BaseClassesLocation.isDebugVerbose


class GlobalLightsClass (BaseClassesLocation.SceneObjectFlatValueControl, BaseClassesLocation.SceneToggleObject, BaseClassesLocation.SceneObjectHandPickable):
	def __init__(self, ownerComp):
		if isDebugVerbose:
			print (ownerComp.name)
		self.ownerComp=ownerComp
		self.myParams=self.loadParams(me.iop.ParamsUnderKeyControl)
		
		BaseClassesLocation.SceneObjectFlatValueControl(self)
		BaseClassesLocation.SceneToggleObject.__init__(self)
		BaseClassesLocation.SceneObjectHandPickable(self)
		
		return
	def loadParams(self, dat):
		i=0
		myParams=[]
		for row in dat.rows():
			if i>0:
				myParams.append(str(row[0]))
			i+=1
		return myParams
	@property
	def CycleIndex (self):
		v=0
		try:
			v=int(self.ownerComp.par.Index)
		except:
			v=0
		return int(v)
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

