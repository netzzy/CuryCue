import os
import math
import re
class LocalPresetClass:

	def __init__( self, ownerComp ):
		self.ownerComp=ownerComp
	#	self.Init()
		self.ownerComp.op("feedbackEdge").par.Reset.pulse()
		return

	def Init (self):
#		self.ownerComp.op("./AnimationTimeControl/T/local/time").frame=1
#		self.ownerComp.op("./AnimationTimeControl/T/local/time").play=1
#		op('/ui/dialogs/timeline').setVar('TIMEPATH', self.ownerComp.op("AnimationTimeControl/T/local/time").path)

		pass
		
	def __del__(self):
		print ("Dying")