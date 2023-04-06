import os
from subprocess import *
import math
import re
class InteractiveMoveCamClass:

	def __init__( self, ownerComp ):
		self.ownerComp=ownerComp
		return

	def ResetPosAndScale(self):
		self.ownerComp.op("scaleSpeedWheel").par.resetpulse.pulse()
		self.ownerComp.op("CursorToMove").par.x=(self.ownerComp.par.w/2)-(self.ownerComp.op("CursorToMove").par.w)
		self.ownerComp.op("CursorToMove").par.y=(self.ownerComp.par.h/2)-(self.ownerComp.op("CursorToMove").par.h)+1


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