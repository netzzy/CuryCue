import os
from subprocess import *
import math
import re
class CameraClass:

	def __init__( self, ownerComp ):
		self.ownerComp=ownerComp
		return


	def Test(self):
		self.Istestpatterns=bool(self.Istestpatterns)^True

	def __del__(self):
		pass
	def SetCameraNdiAddress(self, val1, val2):
		op.cam.op("ndiin1").par.name=val1
		op.cam.op("ndiin2").par.name=val2
	@property
	def Istestpatterns(self):
		return self.ownerComp.par.Istestpatterns
	@Istestpatterns.setter
	def Istestpatterns(self,val):
		self.ownerComp.par.Istestpatterns=bool(val)
		__Istestpatterns=bool(val)
		return self.ownerComp.par.Istestpatterns

	# @property
	# def Device(self):
	# 	return self.ownerComp.par.Device
	# @property
	# def Pairport(self):
	# 	return self.ownerComp.par.Pairport
	# @property
	# def Code(self):
	# 	return self.ownerComp.par.Code
	# @property
	# def Connectport(self):
	# 	return [self.ownerComp.par.Connectport1, self.ownerComp.par.Connectport2]
	# @property
	# def adbPath(self):
	# 	return "{}/{}".format(project.folder, self._adb_path)
	# @property
	# def scrcpyPath(self):
	# 	adb=self.adbPath
	# 	adb=adb.replace("adb.exe", "scrcpy.exe")
	# 	return adb
	# @property
	# def connectAddress(self):
	# 	return "{}:{}".format(self.LivecamerasIP[int(self.Device)], self.Connectport[int(self.Device)])