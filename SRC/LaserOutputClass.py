import os
import inspect
class LaserOutputClass:

	def __init__( self, owner ):
		self.my=me.parent()
		self.ownerComp=owner
		return

	def Enableout(self):
		this_function_name = inspect.currentframe().f_code.co_name
		self.SendMessage(str(this_function_name))
	def Disableout(self):
		this_function_name = inspect.currentframe().f_code.co_name
		self.SendMessage(str(this_function_name))
		return 
	def Blackout(self):
		this_function_name = inspect.currentframe().f_code.co_name
		self.SendMessage(str(this_function_name))
		return 

	def SendMessage(self, name):
		me.iop.oscout.sendOSC('/'+name, [])
		return 
