import os
import re
import traceback
from collections import namedtuple
import ctypes
import sys
import inspect
isDebugVerbose=False

BaseClassesLocation=op.vp_obj_picker.op("SceneObjectBase").module


# TODO при выборе объекта сделать, чтобы выбирались подходящие каналы в кейфреймере
# TODO чтоб лазерные линии проекцировались автоматом на сетки где бы они не были
# TODO переключение ключей с помощью стрелок ctrl +- 
# TODO девайсы, которые на которые нельзя кликнуть: шаттер проектора, общиий свет
# TODO список ключей и их название отображение

# TODO система переключения пресетов для проекции и лазеров
# TODO девайс управления светом - направление, диммер, размер луча, фокус 






################################################################
################################################################
################################################################

class ObjectsPickAndTransform :

	def __init__( self, ownerComp ):
		self.ownerComp=ownerComp

		self.SelectedObject=None
		
		self.mctrl=False
		self.mshift=False
		self.malt=False
		self.keyCaps=False
		self.CapsLockActive=None
		if isDebugVerbose:
			print ("Class init: {}".format(type(self)))

		(self.ActorsInDevices, self.DevicesUnderControl)=([], [])
		self.Updatealldevicesundercontrol()
		self.KeyAndState=namedtuple('KeyAndState', 'key state')
		self.MoveByKeyKey=self.KeyAndState('', False)
		self.isToggleObject=False
		self.isMovableObject=False
		
		return
	@property
	def CapsLockActive(self):
		return self.__CapsLockActive


	@CapsLockActive.setter
	def CapsLockActive(self, v):
		op.vp_obj_picker.par.Capsstate=v
		self.__CapsLockActive=bool(v)

	@property 
	def SelectedObject(self):
		return self.__SelectedObject
	@property
	def curyCueOp(self):
		return op(self.ownerComp.par.Curycue)
	@SelectedObject.setter
	def SelectedObject(self, obj):
		if obj is not None and hasattr(obj, "name"):
			# ставим в параметре контейнера, чтоб видеть что происходит 
			op.vp_obj_picker.par.Selectedactor=obj.name
			op.vp_obj_picker.par.Selecteddevice=obj.parent().name
			op.vp_obj_picker.par.Picked=True
			if hasattr(obj, "extensions"):
				for x in obj.extensions:
					print (isinstance(x, BaseClassesLocation.SceneToggleObject))
				self.isToggleObject=all([isinstance(x, BaseClassesLocation.SceneToggleObject) for x in obj.extensions])
				self.isMovableObject=all([isinstance(x, BaseClassesLocation.SceneMovebleObject) for x in obj.extensions])
			self.curyCueOp.SetActiveFixtureByPath(obj.path)
			# op.KF1.SelectChannelsAuto(obj.name, True)
			# if hasattr(op.KF1, "SelectChannelsAuto"):
			# 	getattr(op.KF1, "SelectChannelsAuto")(obj.name,True)
			messg="Выбран объект: {}, t:{}, toggle:{}, movable:{}".format(obj.name, obj.BehaviorType, self.isToggleObject, self.isMovableObject)
			print (messg)
			ui.status=messg
		elif obj is None:
			op.vp_obj_picker.par.Selectedactor=""
			op.vp_obj_picker.par.Selecteddevice=""
			op.vp_obj_picker.par.Picked=False
			self.isMovableObject=False
			self.isToggleObject=False
			self.curyCueOp.UnselectAllActiveFixtures()
			# if hasattr(op.KF1, "SelectChannelsAuto"):
			# 	getattr(op.KF1, "UnSelectAll")()
#			print (hasattr(op.KF1, SelectChannelsAuto))
		self.__SelectedObject=obj

	def GetCapsLockState(self):
		
		hllDll = ctypes.WinDLL ("User32.dll")
		VK_CAPITAL = 0x14
		CAPSLOCK = hllDll.GetKeyState(VK_CAPITAL)
	
		if CAPSLOCK==65409:
			self.CapsLockActive=True
		else:
			self.CapsLockActive=False

	def Updatealldevicesundercontrol(self):
		myItems=[]
		myDevices=[]
		for deviceOp in op.p.findChildren(tags=["DevicesUnderControl"]):
			myDevices.append(deviceOp)
			for itemInActSpace in deviceOp.findChildren(tags=["InActSpace"]):
				myItems.append(itemInActSpace)
		(self.ActorsInDevices, self.DevicesUnderControl)=(myItems, myDevices)
		
	def Check(self):
		for x in self.ActorsInDevices:
			print ("Found actor: {}".format(x.name))
		for x in self.DevicesUnderControl:
			print ("Device found: {}".format(x.name))
		
		#if self.isMovableObject:
		#	if key in ('right', 'left', 'up', 'down'):
		#		#self.moveByArrows(key)
		#		keystate=self.KeyAndState(key, state)
		#		self.MoveByKeyKey=keystate
		#elif self.isToggleObject:
		#	if key == 'tab' and state:
		#		self.SelectedObject.Cycle()
			
			pass
			
		self.mctrl=ctrl
		self.malt=alt
		self.mshift=shift
################################################################
	def SelectObject (self, event, pickOp):
		
		if self.SelectedObject is None and self.CapsLockActive is True and pickOp is not None and all([isinstance(x, BaseClassesLocation.SceneObjectControlBase) for x in pickOp.extensions]):
			if event.selectStart is True:
				self.SelectedObject=pickOp
		return
################################################################
	def Unselect (self):
		self.SelectedObject=None
		return 
################################################################

	def IndexForw(self):
		my_method="Cycle"
		print (self.isToggleObject)
		if self.SelectedObject is not None and self.isToggleObject:
			if hasattr(self.SelectedObject, my_method):
				getattr(self.SelectedObject, my_method)()

	def IndexBack(self):
#		print ("IndexBack")
		my_method="CycleBack"
		if self.SelectedObject is not None and self.isToggleObject:
			if hasattr(self.SelectedObject, my_method):
				getattr(self.SelectedObject, my_method)()
	def SubIndexForw(self):
		my_method="CycleForwkSub"
		if self.SelectedObject is not None and self.isToggleObject:
			if hasattr(self.SelectedObject, my_method):
				getattr(self.SelectedObject, my_method)()

	def SubIndexBack(self):
		my_method="CycleBackSub"
		if self.SelectedObject is not None and self.isToggleObject:
			if hasattr(self.SelectedObject, my_method):
				getattr(self.SelectedObject, my_method)()

################################################################

	def Left(self):
		self.ToggleMoveKey("left")
	def Right(self):
		self.ToggleMoveKey("right")
	def Up(self):
		self.ToggleMoveKey("up")
	def Down(self):
		self.ToggleMoveKey("down")
	def ToggleMoveKey(self, key):
		if self.SelectedObject is not None and self.isMovableObject:
			state=True
			if self.MoveByKeyKey is not None and self.MoveByKeyKey.state is True:
				state=False
			keystate=self.KeyAndState(key, state)
			print (keystate)
			self.MoveByKeyKey=keystate
	def ToggleRotateRight(self):
		self.ToggleRotate("right")
	def ToggleRotateLeft(self):
		self.ToggleRotate("left")

	def ToggleRotate(self, key):
		if self.SelectedObject is not None and self.isMovableObject:
			state=True
			self.mshift=True
			if self.MoveByKeyKey is not None and self.MoveByKeyKey.state is True:
				state=False
				self.mshift=False
			keystate=self.KeyAndState(key, state)
			print (keystate)
			self.MoveByKeyKey=keystate
################################################################


	@property
	def MoveByKeyKey(self):
		return self.__MoveByKeyKey
	@MoveByKeyKey.setter
	def MoveByKeyKey(self, v):
		#print ("Key:{}, state: {}".format( v.key, v.state ))
		if v.state is True:
			self.__MoveByKeyKey=self.KeyAndState(v.key, v.state)
		else:
			self.__MoveByKeyKey=self.KeyAndState("", False)

		op.vp_obj_picker.par.Arrowkey=self.MoveByKeyKey.key
		op.vp_obj_picker.par.Arrowstate=bool(self.MoveByKeyKey.state)
			


	def MoveByArrows(self):
		_movespeedmagnitude=0.1
		_rotspeedmagnitude=7
		if self.SelectedObject is not None:
			if self.MoveByKeyKey.key=="right":
				if self.mshift:
					self.SelectedObject.Rotate((_rotspeedmagnitude*1, 0.0))
				else:
					self.SelectedObject.Move((_movespeedmagnitude*1, 0.0))
				pass
			elif self.MoveByKeyKey.key=="left":
				if self.mshift:
					self.SelectedObject.Rotate((_rotspeedmagnitude*-1, 0.0))
				else:
					self.SelectedObject.Move((_movespeedmagnitude*-1, 0.0))
				pass
			elif self.MoveByKeyKey.key=="up":
				self.SelectedObject.Move((0.0, _movespeedmagnitude*-1))
				pass
			elif self.MoveByKeyKey.key=="down":
				self.SelectedObject.Move((0.0, _movespeedmagnitude*1))
				pass

	def ToggleValueUp(self):
		this_function_name = inspect.currentframe().f_code.co_name
		if self.SelectedObject is not None: 
			if hasattr(self.SelectedObject, this_function_name):
				getattr(self.SelectedObject, this_function_name)()
	def ToggleValueDown(self):
		this_function_name = inspect.currentframe().f_code.co_name
		if self.SelectedObject is not None: 
			if hasattr(self.SelectedObject, this_function_name):
				getattr(self.SelectedObject, this_function_name)()
			
		return
