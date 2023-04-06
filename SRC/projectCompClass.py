import os
import re


class ProjectCompClass:

	def __init__( self, ownerComp ):
		self.my=me.parent()
		project.paths['movies'] = "z:\\Rigoletto\\RigoServer\\CONTENT\\"
#		project.paths['models'] = ".sources.models"
		self.ownerComp=ownerComp
		self.I=self.IOP(self)
		if ownerComp.par.Autoopencontrol:
			self.OpenControlWindow()
		if ownerComp.par.Autoopenproj:
			# op(me.ipar.SetiComp.P2).par.winopen.pulse()
			op(op("CuryCueUI").op("iopLocate").ipar.SetiComp.P2).par.winopen.pulse()
		ui.status="Proj window opened"
		return
	def OpenControlWindow(self):
		self.ownerComp.op("Control_Window").par.winopen.pulse()
	def OpenProjWindow(self):
		self.ownerComp.op("PROJ_WINDOW").par.winopen.pulse()
	def Disablevissystem(self):
		self.SetcookForVissystem(False)
		pass
	def Enablevissystem(self):
		self.SetcookForVissystem(True)
	def SetcookForVissystem(self, v):
		contentCompSearch=self.ownerComp.findChildren(tags=['vis_system'])
		for n in contentCompSearch:
			n.allowCooking=v

	class IOP :
		def __init__( self, owner ):
			self.owner=owner
		
		def __getattr__(self, name):
			#def wrapper(*args, **kwargs):
			#	print ("'%s' was called" % name)
			
			return self.i(name)
		def i (self, v):
			return getattr(self.owner.my.op("iopLocate").iop, v)
