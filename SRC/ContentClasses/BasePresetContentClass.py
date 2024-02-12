import os
import re

from UtilsClass import IOP
from SceneObjectBase import *
class ContentPresetBase (SceneObjectControlBase, IOP):
	def __init__(self, ownerComp):
	
		self.ownerComp=ownerComp
		
		SceneObjectControlBase.__init__(self, type(self).__name__)
		
		self.Init_on_start_or_clone()
		self.LastArmed=None
		#run('op("{}").Init_on_start_or_clone()'.format(self.ownerComp.path), delayFrames=10)
		return
	def Init_on_start_or_clone(self):
		# self.GarbadgeCollect()
		self.CheckContentComp()
		# self.Copycustomparup()

	# def Disable(self):
	# 	self.Active=0
	# 	return 
	# def Enable(self):
		
	# 	self.Active=1
	# 	self.Subindex=0
	# 	return 

	def Arm(self):
		self.ownerComp.par.Armed=1
	def Disarm(self):
		self.Armed=0
		
	def Update(self):
		# !!!
		myContentComp=self.CheckContentComp()

	
	
		if myContentComp is not None:
			if self.Armingtype=="byfade":
				if self.Activefade==0:
					self.ownerComp.par.Armed=0
				elif myContentComp.allowCooking==False and self.Activefade>0:
					self.ownerComp.par.Armed=1

			if self.Armed ==0 and myContentComp.allowCooking:
				myContentComp.allowCooking=False
				
				# if self.ownerComp.op("LASER_MASER_OUT") is not None and len(self.ownerComp.op("LASER_MASER_OUT").inputs): 
				# 	self.ownerComp.color=(0,1,.5)
				# else:
				self.ownerComp.color=(0,1,0)
				 
				if hasattr(myContentComp.ext, "LocalPresetClass"):
					myClass=getattr(myContentComp.ext, "LocalPresetClass")
					if hasattr(myClass, "__del__"):
						getattr(myClass, "__del__")()
				

			if myContentComp.allowCooking==False and self.Armed ==1:
				# if self.ownerComp.op("LASER_MASER_OUT") is not None and len(self.ownerComp.op("LASER_MASER_OUT").inputs): 
				# 	self.ownerComp.color=(0.7,0,1)
				# else:
				self.ownerComp.color=(1,0.3,0.3)

				
				myContentComp.allowCooking=True
				
			self.LastArmed=self.Armed

		return 
	def CheckContentComp(self):
		contentComp=None
		contentCompSearch=[]

		if self.ownerComp.op("findContentOp") is not None:
			for myItem in self.ownerComp.op("findContentOp").rows()[1:]:
				contentCompSearch.append(self.ownerComp.op(myItem[0]))
		else:
			contentCompSearch=self.ownerComp.findChildren(tags=['content'])

		
		for myItem in contentCompSearch:
			if myItem.name==self.ownerComp.name:
				contentComp=myItem
			
		if contentCompSearch.__len__() == 0 or contentCompSearch.__len__() > 1 :
			ui.status="Err with {} preset., no internal content comp ({})".format(self.ownerComp.name, contentCompSearch.__len__())
#			return None
		else: 
			# меняем имя, есть изменилось
			if contentComp is not None:
				return contentComp
			else:
				for myItem in contentCompSearch:
					contentComp=myItem

				if self.ownerComp.name!=contentComp.name:
					contentComp.name=self.ownerComp.name
					ui.status="Preset {} renamed".format(self.ownerComp.name)
					return contentComp
			
		self.ownerComp.par.Active=self.GetActivePresetNames()
		

	def Copycustomparup(self):
		# define
		mainContentComp=self.ownerComp
		protectedContentComp=mainContentComp.op(mainContentComp.name)
		if protectedContentComp is None:
			ui.status="Ошибка синхр.пар.конт. {}".format(mainContentComp.name)
			return
		for sourcePage in protectedContentComp.customPages:
			for sourcePar in sourcePage:
				sourcePar.styleCloneImmune=False
		
		oldCustomValues=dict()
				# save parameters in source
		for sourcePage in mainContentComp.customPages:
			for sourcePar in sourcePage:
				oldCustomValues[sourcePar.name]=sourcePar.eval()
				

		oldActiveValue=0
		oldArmingType=0
		oldArmed=False
		
		if "PresetCommon" in mainContentComp.customPages:
			oldActiveValue=mainContentComp.par.Active.eval()
			oldArmingType=mainContentComp.par.Armingtype.menuIndex
			oldArmed=bool(mainContentComp.par.Armed)
			

		# Copy Custom Pars and Link them
		contentPreset_iPar_list=mainContentComp.findChildren(tags=['contentPreset_iPar'])
		
		if len(contentPreset_iPar_list)>0:
			contentPreset_iPar=contentPreset_iPar_list[0]
			self.CopyCustomPars(contentPreset_iPar,protectedContentComp, _link="From_ipar")
			print ("Copy from ipar")

		

		self.CopyCustomPars(protectedContentComp,mainContentComp, _link="FromSourceToDest", _nosrcToConst=True, oldCustomValues=oldCustomValues)

		# add preset common page
		page=mainContentComp.appendCustomPage("PresetCommon")
		
		myNewPar=page.appendFloat("Active", size=1, order=3, replace=True)[0]
		myNewPar.startSection=1
		page.appendFloat("Activefade", size=1, order=4, replace=True)		
		mainContentComp.par.Activefade.mode=ParMode.EXPORT
		mainContentComp.par.Active=oldActiveValue

		# add arm pulse
		myNewPar=page.appendToggle("Armed", order=0, replace=True)[0]
		myNewPar.startSection=1
		myNewPar.val=oldArmed
		
		myNewPar=page.appendMenu("Armingtype", label = "Arming type", order=0, replace=True)[0]
		myNewPar.menuNames=['byfade', 'bytoggle']
		myNewPar.menuLabels=['Auto (fade)', 'Only by ARMED toggle']
		myNewPar.menuIndex=oldArmingType
		
		myNewPar=page.appendPulse("Arm", label = "Arm", order=4, replace=True)[0]
		myNewPar.startSection=1
		
		myNewPar=page.appendPulse("Disarm", label = "Disarm", order=5, replace=True)[0]


		ui.status="Success: sync. preset parameters {}".format(mainContentComp.name)

	def CopyCustomPars(self, _source, _dest, _link="FromSourceToDest", _nosrcToConst=False, oldCustomValues=dict()):

		# define

		_dest.destroyCustomPars()
		mainContentComp=_dest
		protectedContentComp=_source
		if protectedContentComp is None:
			ui.status="Error syncing content parameters. {}".format(mainContentComp.name)
			return
		# copy protectedContentComp -> mainContentComp 
		mainContentComp.copyParameters(protectedContentComp, custom=True, builtin=False)
	
		# link parameters
		for sourcePage in protectedContentComp.customPages:
			for sourcePar in sourcePage:
				linkExpr=None
				destLinkPar=None
				srcLinkPar=None
				if _link=="FromSourceToDest":
					linkExpr="parent.ContentPreset.par.{}".format(sourcePar.name)
					destLinkPar=getattr(protectedContentComp.par, sourcePar.name)
					srcLinkPar=getattr(mainContentComp.par, sourcePar.name)
					srcLinkPar.mode=ParMode.CONSTANT

				elif _link=="From_ipar":
					linkExpr="me.parent().par.{}".format(sourcePar.name)
					destLinkPar=getattr(protectedContentComp.par, sourcePar.name)
					srcLinkPar=getattr(mainContentComp.par, sourcePar.name)
				else:
					linkExpr="op('./{}').par.{}".format(mainContentComp.name, sourcePar.name)
					destLinkPar=getattr(mainContentComp.par, sourcePar.name)
					srcLinkPar=getattr(protectedContentComp.par, sourcePar.name)
					# print (destLinkPar)
				
				destLinkPar.bindExpr=linkExpr
				destLinkPar.mode=ParMode.BIND
				if destLinkPar.name in oldCustomValues.keys():
					destLinkPar.val=oldCustomValues[destLinkPar.name]

					#print ("{}:{}".format(destLinkPar.name, oldCustomValues[destLinkPar.name]))
				

				# destLinkPar=srcLinkPar
				if not _nosrcToConst:
					srcLinkPar.mode=ParMode.CONSTANT
				# destLinkPar.styleCloneImmune=True
				# srcLinkPar.styleCloneImmune=True

	def GarbadgeCollect(self):
		contentCompSearch=self.ownerComp.findChildren(tags=['content'])
		if len(contentCompSearch) > 1:
			for myItem in contentCompSearch:
				if myItem.name!=self.ownerComp.name:
					print ("Надо бы удалить {}".format(myItem.path))
					myItem.destroy()
					

		pass
	@property
	def Active(self):
		return self.ownerComp.par.Active
	@property
	def Activefade(self):
		return self.ownerComp.par.Activefade.eval()
	@Active.setter
	def Active(self, v):
		self.ownerComp.par.Active=v
		__Active=v
	@property
	def Subindex(self):
		return self.ownerComp.par.Subindex
	@Active.setter
	def Subindex(self, v):
		self.ownerComp.par.Subindex=v
		self.ownerComp.parent().par.Subindex=v
		__Subindex=v
	@property
	def CompHistoryDat(self):
		return parent.vcont.par.op("CompHistory/COMP_HISTORY")

	@property
	def Isautoopencontentcomp(self):
		return parent.vcont.par.Isautoopencontentcomp
	@property
	def Armed(self):
		return self.ownerComp.par.Armed
	# @Armed.setter
	# def Armed(self, v):
	# 	self.ownerComp.par.Armed=v
	# 	__Armed=v

	@property
	def Armingtype(self):
		return self.ownerComp.par.Armingtype
