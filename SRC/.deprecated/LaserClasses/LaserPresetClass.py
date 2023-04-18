import os
import re


from BasePresetContentClass import *
#BaseClassesLocation.isDebugVerbose


class LaserPresetClass ( ContentPresetBase ):
	def __init__(self, ownerComp):
		self.ownerComp=ownerComp
		self.I=IOP(ownerComp)
		ContentPresetBase.__init__(self, ownerComp)


