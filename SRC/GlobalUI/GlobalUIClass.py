import os
import re
from collections import namedtuple

isDebugVerbose=True

class GlobalUIClass:

	def __init__( self, ownerComp ):
		self.ownerComp=ownerComp
		self.I=self.IOP(self)
		self.K=self.IKEY(self)
		if isDebugVerbose:
			print ("{} init".format (ownerComp.name))

		self.KeyValue=namedtuple('KeyValue', 'name value')
		self.KeyAndState=namedtuple('KeyAndState', 'value init end')
		self.COMMAND=namedtuple('Command', 'keys mods device actor function')
		self.keysDict=dict()
		self.Commands=self.LoadCommands()
		# self.keysDict.has_key
		return

		def __getattr__(self, name):
			#def wrapper(*args, **kwargs):
			#	print ("'%s' was called" % name)
			if hasattr(self, name):
				return name
			else:
				return "zzz"
	def Updatekeys(self):
		self.keysDict=dict()
		self.Commands=self.LoadCommands()
		print ("Update keys Global UI")

	def Update(self):
		for key in self.I.MasterKeyboardChop.chans('*'):
			self.ProcessKey(self.KeyValue(key.name[1:].lower(), key.eval()))
			pass
		self.CheckCallbacks()
		
	def ProcessKey(self, keyVal):
		prevVal=self.keysDict.get(keyVal.name, self.KeyAndState(keyVal.value, True, False))
		isInit=False
		isEnd=False
		isChange=(prevVal.value == keyVal.value)
		if isChange and prevVal.init is False:
			isInit=True
			isEnd=False
		elif isChange and prevVal.init is True and keyVal.value==0 :
			isInit=False
			isEnd=True

		isInit=(prevVal.value != keyVal.value)
		self.keysDict[keyVal.name]=self.KeyAndState(keyVal.value, isInit, isEnd)
		return 

	def CheckCallbacks(self):
		for cmd in self.Commands:
			self.CheckCommand(cmd.device, cmd.actor, [cmd.keys], [cmd.mods], cmd.function)

	def LoadCommands(self):
		i=0
		fieldNamesDict=dict()
		myCommands=[]
		for row in op(self.I.HotkeysToActos).rows():
			if i == 0:
				for c in row:
					fieldNamesDict[str(c)]=c.col
			elif row[0]!="":
				# keys mods device actor function
				myCommand=self.COMMAND(str(row[fieldNamesDict['keys']]), str(row[fieldNamesDict['mods']]), str(row[fieldNamesDict['device']]), str(row[fieldNamesDict['actor']]), str(row[fieldNamesDict['function']]))
				myCommands.append(myCommand)
			i+=1
		return myCommands
	def CheckCommand(self, device, actor, keysList, modsList, _method):
		isKeys=all([getattr(self.K, x).value for x in keysList])
		isInit=all([getattr(self.K, x).init for x in keysList])
		modsOnList=[]
		modsOffList=[]
		for mod in ['alt', 'lwin', 'lshift', 'rshift', 'lctrl', 'rctrl']:
			if mod in modsList:
				modsOnList.append(mod)
			else:
				modsOffList.append(mod)
		isModsOn=all([getattr(self.K, x).value for x in modsOnList])
		isModsOff=all([getattr(self.K, x).value ==0 for x in modsOffList])

		if isKeys and isInit and isModsOn and isModsOff:
			if hasattr(op, device):
				myDevice=getattr(op, device)
				print ("Device found {}".format(op(myDevice)))
# 				print ("Actor to find: {}".format(actor))

				if actor!="" and hasattr(myDevice.I, actor):
					
					myActor=getattr(myDevice.I, actor)
					print ("Actor found {}".format(myActor))
					if hasattr(myActor, _method):
						getattr(myActor, _method)()
				else:
					print ("Executing {} on device {} ".format(_method, myDevice))
					if hasattr(myDevice, _method):
						getattr(myDevice, _method)()

#		if (self.K.f1.end):
#			print ('aa')


		return 













	class IOP :
		def __init__( self, owner ):
			self.owner=owner
		
		def __getattr__(self, name):
			#def wrapper(*args, **kwargs):
			#	print ("'%s' was called" % name)
			
			return self.i(name)
		def i (self, v):
			return getattr(self.owner.ownerComp.op("iopLocate").iop, v)
	class IKEY :
		def __init__( self, owner ):
			self.owner=owner
			
		
		def __getattr__(self, name):
			#def wrapper(*args, **kwargs):
			#	print ("'%s' was called" % name)
			
			return self.owner.keysDict.get(name, self.owner.KeyAndState(name, False, False))

