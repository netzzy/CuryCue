import os
import re

BaseClassesLocation=op.vp_obj_picker.op("SceneObjectBase").module

isDebugVerbose=False
#=BaseClassesLocation.isDebugVerbose


class ActorsClass (BaseClassesLocation.SceneMovebleObject):
	def __init__(self, ownerComp):
		if isDebugVerbose:
			print ("ScenObjClass")
		self.ownerComp=ownerComp
		BaseClassesLocation.SceneMovebleObject.__init__(self)
		return

	
class InternalClass():
	def __init__( self ):
		self.my=me.parent()
		self.MyObjects=[]
		self.FindMyObjects()
		
		# ScenographyClass.__init__(self)
		return
	def FindMyObjects(self):
		for op in self.my.ops("*"):
			if hasattr(op, "IsSceneObject"):
				self.MyObjects.append(op)
