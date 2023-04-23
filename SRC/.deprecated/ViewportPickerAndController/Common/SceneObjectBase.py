isDebugVerbose=False
import math
class SceneObjectControlBase:
	def __init__(self, objType):
		
		self.BehaviorType=objType
		self.name=self.ownerComp.name
		self.path=self.ownerComp.path

		self.IsSceneObject=True
		if isDebugVerbose:
			print ("SceneObjectControlBase {}, {}".format (self.name, self.path))
		return
	def Select (event):
		return


class SceneMovebleObject (SceneObjectControlBase):
	def __init__(self):
		if isDebugVerbose:
			print ("SceneMovebleObject")
		SceneObjectControlBase.__init__(self, type(self).__name__)
		return

	def Move (self, v):
		myop=op(self.path)
		myop.par.tx=myop.par.tx+float(v[0])
		myop.par.tz=myop.par.tz+float(v[1])
		
		return
	def Rotate (self, v):
		myop=op(self.path)
		myop.par.ry=myop.par.ry+float(v[0])
		return

	
class SceneToggleObject (SceneObjectControlBase):
	def __init__(self):
		if isDebugVerbose:
			print (type(self).__name__)
		SceneObjectControlBase.__init__(self, type(self).__name__)
		return


class SceneObjectFlatValueControl:
	def __init__(self, owner):
		#if isDebugVerbose:
		print (type(self).__name__)
		self.owner=owner
		
	def ToggleValueUp(self):
		self.StepValue(0.1)
	def ToggleValueDown(self):
		self.StepValue(-0.1)	
	def StepValue(self, step):
		index=0
		if hasattr(self.ownerComp.par, self.myParams[self.CycleIndex]):
			v=getattr(self.ownerComp.par, self.myParams[self.CycleIndex])
			setattr(self.ownerComp.par, self.myParams[self.CycleIndex], round (v+step, 3))
			print ("Changed {} from {} to {}".format(self.myParams[self.CycleIndex], round(v+0, 3), round(v+step, 3)))
		
class SceneObjectHandPickable:
	def __init__(self, owner):
		self.owner=owner

###################################
	def SelectDevice(self):
		if op.vp_obj_picker.SelectedObject is not self.ownerComp:
			op.vp_obj_picker.SelectedObject=self.ownerComp
		else:
			op.vp_obj_picker.SelectedObject=None
###################################
