import os
import re


from ContentMasterBase import *

isDebugVerbose=True

class ProjectorsMasterClass (ContentMasterBase):
	def __init__(self, ownerComp):
		if isDebugVerbose:
			print (ownerComp.name)
		self.ownerComp=ownerComp
		ContentMasterBase.__init__(self, self.ownerComp)

		return

