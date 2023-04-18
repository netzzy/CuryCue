import os
import inspect
class LaserInputClass:

	def __init__( self, owner ):
		self.my=me.parent()
		self.ownerComp=owner
		return
	@property
	def PangolinNode(self):
		v=op(self.ownerComp.par.Pangolinnode)
		self.__PangolinNode=v
		return self.__PangolinNode
		
	def GetRemotePulse(self, name):
		myPar=name[1:].lower()
		print (myPar)
		if hasattr(self.PangolinNode.par, myPar):
			getattr(self.PangolinNode.par, myPar).pulse()
			print (myPar)
		 
		return 