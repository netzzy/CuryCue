import os
import re

ContentMasterBase=op.lsg.op("ContentMasterBase").module
BaseClassesLocation=op.vp_obj_picker.op("SceneObjectBase").module



isDebugVerbose=True
#BaseClassesLocation.isDebugVerbose

class LaserPresetClass (ContentMasterBase.ContentPresetBase ):
	def __init__(self, ownerComp):
		if isDebugVerbose:
			print (ownerComp.name)
		self.ownerComp=ownerComp
		ContentMasterBase.ContentPresetBase.__init__(self, self.ownerComp)



class LaserMasterClass (ContentMasterBase.ContentMasterBase):
	def __init__(self, ownerComp):
		if isDebugVerbose:
			print (ownerComp.name)
		self.ownerComp=ownerComp


		ContentMasterBase.ContentMasterBase.__init__(self, self.ownerComp)
		BaseClassesLocation.SceneToggleObject.__init__(self)


		self.my=me.parent()
		self.I=self.IOP(self)
		
		return

class InternalClass:

	def __init__( self ):
		self.my=me.parent()
		self.I=self.IOP(self)
		return


	class IOP :
		def __init__( self, owner ):
			self.owner=owner
		
		def __getattr__(self, name):
			#def wrapper(*args, **kwargs):
			#	print ("'%s' was called" % name)
			
			return self.i(name)
		def i (self, v):
			return getattr(self.owner.my.op("iopLocate").iop, v)
