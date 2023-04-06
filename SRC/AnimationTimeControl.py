import os
import re
class InternalClass:

	def __init__( self ):
		self.my=me.parent()
		print ("AnimTimeControl")
		return
	def Play(self):
		self.my.op("T/local/time").par.play=True
	def Stop(self):
		self.my.op("local/time").par.play=False
	def PlayOrStop(self):
		self.my.op("local/time").par.play^=True
	def Rewind (self):
		self.SetTimeFrame(1)
	def getFPS(self):
		return self.my.op("T/local/time").par.rate

	def SetTimeFrame(self, frame):
		self.my.op("T/local/time").frame=frame
	def GetCurrentFrame(self):
		return self.my.op("T/local/time").frame

	def Update(self):
		return
