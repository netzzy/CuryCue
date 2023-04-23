vMath = op('vsu').module.VMath()
import traceback
import numpy as np
import colorsys
TD_CHOP_CHANNEL = Channel
from pprint import pprint

class Keyframer:
	""" Inherited  by KeyframerExt, Channel and Segment classes"""
	def __init__(self, owner, ownerComp):
		self.owner = owner
		self.ownerComp = ownerComp
		self.iParsComp = ownerComp.op('iPars')
		self.templatesComp = ownerComp.op('templates')
		self.animationTemplateComp = self.templatesComp.op('animation1')
		self.channelTemplateComp = self.templatesComp.op('channel')
		self.keysTemplateDat = self.templatesComp.op('keys')		
		self.ChannelsComp = ownerComp.op('channels')
		self.animLookupComp = ownerComp.op('animLookup')
		self.KeyframeLookupChop = self.animLookupComp.op('out')

		self.viewComp = ownerComp.op('view')
		self.keysViewComp = self.viewComp.op('keysView')
		self.keysPanel = self.keysViewComp.panel
		self.keysCamComp = self.keysViewComp.op('cam')
		self.keysTransformComp = self.keysViewComp.op('transform')
		self.keysRenderPickDat = self.keysViewComp.op('renderpick')
		self.switchMarqueeTop = self.keysViewComp.op('switchMarquee')
		self.keysViewKeysJoinChop = self.keysViewComp.op('keys/join')
		self.keysViewHandlesJoinChop = self.keysViewComp.op('handles/join')	
		self.keysViewLabelsComp = self.keysViewComp.op('labels')
		#self.keysViewLabelsJoinChop = self.keysViewLabelsComp.op('join')
		self.MasterKeyboardChop = self.viewComp.op('MasterKeyboard')
		self.keysRenderPickComp = self.viewComp.op('timeGraph')
		self.channelControlsComp = self.viewComp.op('channelControls')
#		self.channelListComp = self.channelControlsComp.op('channelList')
		self.editControlsComp = self.viewComp.op('editControls')
		self.keyframeControlsComp = self.editControlsComp.op('keyframeControls')
		self.contextMenuComp = self.viewComp.op('ContextMenu')	
		self.globalControlsComp = self.viewComp.op('globalControls')
		self.newAnimNameComp = self.globalControlsComp.op('newAnimName')
		self.animCompComp = self.globalControlsComp.op('animComp')	
		self.newChannelNamesComp = self.globalControlsComp.op('newChannelNames')

		self.kctrl = self.MasterKeyboardChop['kctrl']
		self.kalt = self.MasterKeyboardChop['kalt']
		self.kshift = self.MasterKeyboardChop['kshift']
		self.kd = self.MasterKeyboardChop['kd']
		self.kf = self.MasterKeyboardChop['kf']
		
		self.segmentClasses = {	
			'constant()': Constant,
			'linear()': Linear,
			'ease()': Ease,
			'easein()': EaseIn,
			'easeout()': EaseOut,
			'easep(2)': EaseP,
			'easeinp(2)': EaseInP,
			'easeoutp(2)':EaseOutP,
			'cubic()': Cubic,
			'bezier()': Bezier,
			'easeadjust()': EaseAdjust
		}
		self.segmentFuncNames = list(self.segmentClasses.keys())

	@property
	def AnimationComp(self): return self.ownerComp.par.Animationcomp.eval()
	@AnimationComp.setter
	def AnimationComp(self, value):
		if isinstance(value, animationCOMP):
			self.ownerComp.par.Animationcomp = value
			self.animCompComp.UpdateView(value)

	@property
	def channelsDat(self): return self.AnimationComp.op('channels')

	@property
	def keysComp(self): return self.AnimationComp.op('keys')

	@property
	def keyframeChop(self): return self.AnimationComp.op('keyframe')
	
	@property
	def AnimationRangeStart(self):
		return self.AnimationComp.par.start.eval()
	@AnimationRangeStart.setter
	def AnimationRangeStart(self, value):
		self.AnimationComp.par.start = value

	@property
	def AnimationRangeEnd(self):
		return self.AnimationComp.par.end.eval()
	@AnimationRangeEnd.setter
	def AnimationRangeEnd(self, value):
		self.AnimationComp.par.end = value

	@property
	def KeysViewHorzRange(self):
		return [self.keysViewComp.par.Horzrange1.eval(), 
				self.keysViewComp.par.Horzrange2.eval()]
	@KeysViewHorzRange.setter
	def KeysViewHorzRange(self, value):
		self.keysViewComp.par.Horzrange1 = value[0]
		self.keysViewComp.par.Horzrange2 = value[1]
		self.animLookupComp.par.start = value[0]
		self.animLookupComp.par.end = value[1]

	@property
	def KeysViewVertRange(self):
		return [self.keysViewComp.par.Vertrange1.eval(), 
				self.keysViewComp.par.Vertrange2.eval()]
	@KeysViewVertRange.setter
	def KeysViewVertRange(self, value):
		self.keysViewComp.par.Vertrange1 = value[0]
		self.keysViewComp.par.Vertrange2 = value[1]

	@property
	def LengthSeconds(self):
		if self.AnimationComp is not None:
			animStart = self.AnimationRangeStart	
			animEnd = self.AnimationRangeEnd
			numFrames = animEnd - animStart
			return numFrames / self.AnimationComp.time.rate
		else:
			return 10


class KeyframerExt(Keyframer):
	def __init__(self, ownerComp):
		super().__init__(self, ownerComp)
		self.labelStartTx = 30
		self.navHomeMargins = [30, 10, 20, 20] # l,r,b,t
		self.navHomeMarginSums = [
			self.navHomeMargins[0] + self.navHomeMargins[1],
			self.navHomeMargins[2] + self.navHomeMargins[3],
		]
		self.undoStateChannelsName = 'Keyframer Channels State'
		self.undoStateAnimCompName = 'Keyframer Animation Comp State'
		self.undoNavName = 'Keyframer Navigate'
		self.init()
		self.selectFuncs = [
			self.SelectKey,
			self.SelectHandle, 
			self.SelectSegment
		]
		self.SetSelectedFuncs = {
			'frame': self.SetFrameSelectedKeyframes,
			'value': self.SetValueSelectedKeyframes,
			'inslope': self.SetInslopeSelectedKeyframes,
			'inaccel': self.SetInaccelSelectedKeyframes,
			'outslope': self.SetOutslopeSelectedKeyframes,
			'outaccel': self.SetOutAccelSelectedKeyframes,
			'function': self.SetFunctionSelectedKeyframes
		}
		self.nudgeDir = {
			'right': tdu.Position(1, 0, 0),
			'left': tdu.Position(-1, 0, 0), 
			'up': tdu.Position(0, 1, 0), 
			'down': tdu.Position(0, -1, 0)
		}
		self.contextMenuLookup = {
			'channelList': {
				'headerLabel': 'Edit Channel(s)',
				'menuItems': [
					{
						'label': 'Delete Channel',
						'func': self.DeleteChannelConfirm,
					},
					{
						'label': 'Delete Displayed Channels',
						'func': self.DeleteChannelsConfirm,
					},
					{
						'label': 'Rename Channel',
						'func': self.EditChannelName,
					}				
				]
			}
		}

	@property
	def curStateChannels(self):
		return self.ownerComp.storage.get('curStateChannels')
	@curStateChannels.setter
	def curStateChannels(self, value):
		self.ownerComp.storage['curStateChannels'] = value
		
	@property
	def prevStateChannels(self):
		return self.ownerComp.storage.get('prevStateChannels')
	@prevStateChannels.setter
	def prevStateChannels(self, value):
		self.ownerComp.storage['prevStateChannels'] = value

	@property
	def ChannelNames(self):
		return tdu.Dependency(list(self.Channels.keys()))

	@property
	def currentChannelIds(self):
		return [int(cell.val) for cell in self.channelsDat.col(1)[1:]]

	@property
	def marqueeSelecting(self):
		return bool(self.switchMarqueeTop.par.index)

	def getHandleRelXY(self, slope, radius):
		s = 1 if slope >= 0 else -1
		if slope != 0.0 and radius != 0.0:
			x = radius / math.sqrt(slope * slope + 1)
			slope = 1.0 / slope
			y = radius / (s * math.sqrt(slope * slope + 1))
		elif radius == 0.0 and slope != 0.0:
			x = 0
			y = 0
		else:
			x = radius
			y = 0.0
		return x, y

	def init(self, newAnimComp=False):
		self.updateViewKeySegment = None
		self.updateViewInHandleSegment = None
		self.updateViewOutHandleSegment = None
		self.startPickOP = None
		self.keysRenderPickDat.par.strategy = 'holdfirst'
		self.selectPos = tdu.Position()
		self.selStartPos = tdu.Position()
		self.setPos = tdu.Position()
		self.startSetPosOffset = tdu.Position()
		self.insertPos = tdu.Position()
		self.insidePos = tdu.Position()
		self.scaleKeysScale = tdu.Vector(1.0, 1.0, 1.0)
		self.scaleStartPos = tdu.Position()
		self.curMarqKeys = []
		self.curMarqHandles = []
		self.startSet = False
		self.startScale = False
		self.copiedKeys = {}

		try:
			if newAnimComp:
				channelComps = self.ChannelsComp.findChildren()
				for channelComp in channelComps:
					if channelComp:
						channelComp.destroy()				
			self.SetChannels()
			self.unSelectAll()
			self.AnimationComp.cook(force=True, recurse=True)
			if newAnimComp:
				self.keysNavHome()
				self.updateKeysView(init=True)							
		except Exception as e:
			traceback.print_exc()

	def InitView(self):
		self.SetNavRange()
		#self.updateKeysView()

	def Animationcomp(self):
		if self.AnimationComp is None:
			self.AnimationComp = self.animationTemplateComp
		elif 'KEYFRAMER_ANIM_COMP' not in self.AnimationComp.tags:
			m = (f"The animationCOMP: {self.AnimationComp.path} is not 'Keyframer' "
				f"configured would you like to convert it?")
			confirm = ui.messageBox('Convert', m, 
									buttons=['Cancel', 'convert'])
			if confirm == 1:
				comp = self.convertToKeyframerAnimComp(self.AnimationComp)
				if comp is not None:
					self.AnimationComp = comp

				else:
					print(f"Unable to convert: {self.AnimationComp.path}")
					self.AnimationComp = self.animationTemplateComp		
			else:
				self.AnimationComp = self.animationTemplateComp
			

		self.init(newAnimComp=True)

	def SetChannels(self):
		channels = {}
		return 
	def OnPickEvents(self, allEvents):
		for event in allEvents:
			# print(event)
		#	self.keysNav(event)
			if event.selectStart:
				self.onPickSelectStart(event)

				#if (self.keysPanel.lselect and not self.kalt):
				#	self.startPickOP = event.pickOp
				#	if event.pickOp == None:	
				#		if not self.kshift and not self.kctrl:
				#			self.unSelectAll()
				#		self.marqueeSelectStart(event)
					
			elif event.selectEnd:

				self.keysNavEnd(event)	
				self.onPickEnd(event)	
			
			if self.keysPanel.mselect:
				self.keysNav(event)

			if event.selectEnd:
				self.keysNavEnd(event)	
				self.onPickEnd				
				

	def Appendchannel(self):
		# par callback
		name = self.iParsComp.par.Channelname.eval()
		self.AppendChannel(name)

	def Deletechannel(self):
		# par callback
		name = self.iParsComp.par.Channelname.eval()
		self.DeleteChannel(name)

	def Insertkey(self):
		# par callback		
		x = self.iParsComp.par.Insertposx.eval()
		chanName = self.iParsComp.par.Channelname.eval()
		y = None
		expr = self.iParsComp.par.Insertfunction.eval()
		self.InsertKey(chanName, x, y, expr)

	def Deletekey(self):
		# par callback
		i = self.iParsComp.par.Selectkeyframe.eval()
		chanName = self.iParsComp.par.Channelname.eval()
		self.DeleteKey(chanName, i)

	def Defaultchancol(self):
		# par callback
		if self.iParsComp.par.Chancolmode.eval() == 'DEFAULT_COL':
			col = self.iParsComp.pars('Defaultchancol*')
			templatePars = self.channelTemplateComp.pars('Color*')
			templatePars[0].val = col[0]
			templatePars[1].val = col[1]
			templatePars[2].val = col[2]
			for i, chan in enumerate(self.Channels.values(), start=1):
				self.channelsDat[i, 6] = col[0]
				self.channelsDat[i, 7] = col[1]
				self.channelsDat[i, 8] = col[2]
				chan.channelComp.par.Colorr = col[0]
				chan.channelComp.par.Colorg = col[1]
				chan.channelComp.par.Colorb = col[2]

	def Initialize(self, templateComp=False):
		if templateComp:
			comp = self.animationTemplateComp
		else:
			comp = self.AnimationComp
		confirm = ui.messageBox('Initialize', 
			(f"Are you sure? This will delete all existings data in: "
			f"{comp}"), buttons=['Cancel', 'Initialize'])
		if confirm == 1:
			if templateComp:
				self.AnimationComp = self.animationTemplateComp
			self.DeleteAllChannels()
			self.updateKeysView(init=True)
			run("args[0]()", self.keysNavHome, delayFrames=1)				

	def AppendChannel(self, name, updateKeysView=True, startVal=None):
		if name == '' or name == 'name' or self.Channels.get(name):
			print(f"'{name}' is an invalid channel name.")
			return False
		else:
			if len(self.currentChannelIds) > 0:
				index = max(self.currentChannelIds) + 1
			else:
				index = 0
			rowData = [name, index, 'hold', 'hold', 0, 
						f"keys/{name}", .8, .8, .8, 1, 1, 0]
			if name in self.channelsDat.col(0):
				self.channelsDat.replaceRow(name, rowData)
			else:
				self.channelsDat.appendRow(rowData)
			self.Channels[name] = Channel(self, name, index, index, 
										startVal=startVal)
			if self.iParsComp.par.Chancolmode.eval() == 'MULTI_COL':
				# rgbStart = self.iParsComp.pars('Defaultchancol*')
				hue = (index / 16)
				col = colorsys.hsv_to_rgb(hue, .4, .6)
				self.channelsDat[name, 6] = col[0]
				self.channelsDat[name, 7] = col[1]
				self.channelsDat[name, 8] = col[2]
				chanComp = self.Channels[name].channelComp
				chanComp.par.Colorr = col[0]		
				chanComp.par.Colorg = col[1]
				chanComp.par.Colorb = col[2]

			self.ChannelsList = list(self.Channels.values())								
			self.channelListComp.Refresh(self.Channels, self.ChannelNames.val)
			self.updateKeysView(init=True)
		if updateKeysView:
			# self.updateKeysView(init=True)
			run("args[0](init=True)", self.updateKeysView, delayFrames=1)

	def DeleteChannel(self, name):
		if self.Channels.get(name):
			self.Channels.get(name).destroy()
		self.SetChannels()
		self.updateKeysView()

	def DeleteAllChannels(self):
		self.Channels = {}
		for channel in self.Channels.values():
			channel.destroy()
		self.channelsDat.clear(keepFirstRow=True)
		channelComps = self.ChannelsComp.findChildren()
		for channelComp in channelComps:
			if channelComp:
				channelComp.destroy()
		keysDats = self.keysComp.findChildren()
		for keysDat in keysDats:
			if keysDat:
				keysDat.destroy()
		self.channelListComp.Refresh(self.Channels, self.ChannelNames.val)

	def DeleteChannelConfirm(self, chanName):
		confirm = ui.messageBox('Delete Channel',
			f"Are you sure you would like to delete: {chanName}?",
			buttons = ['Cancel', 'Delete'])
		if confirm == 1:
			prevState = self.getAnimationCompState()
			self.DeleteChannel(chanName)
			curState = self.getAnimationCompState()
			ui.undo.startBlock(self.undoStateAnimCompName)
			ui.undo.addCallback(self.undoDeleteAppendChannels, 
								[prevState, curState])
			ui.undo.endBlock()

	def DeleteChannelsConfirm(self, chanName):
		confirm = ui.messageBox('Delete Channel',
			f"Are you sure you would like to delete all displayed channels?",
			buttons = ['Cancel', 'Delete'])
		if confirm == 1:
			chans = []
			for chan in self.Channels.values():
				if chan.display:
					chans.append(chan)
			prevState = self.getAnimationCompState()
			for chan in chans:
				self.DeleteChannel(chan.name)
			curState = self.getAnimationCompState()
			ui.undo.startBlock(self.undoStateAnimCompName)
			ui.undo.addCallback(self.undoDeleteAppendChannels, 
								[prevState, curState])
			ui.undo.endBlock()

	def getAnimationCompState(self):
		state = {
			'channelsDat': self.channelsDat.text,
			'keysComp': self.keysComp.saveByteArray()
		}
		return state

	def undoDeleteAppendChannels(self, isUndo, info):
		if isUndo:
			state = info[0]
		else:
			state = info[1]	
		if state is not None:	
			self.channelsDat.text = state['channelsDat']
			self.keysComp.destroy()
			self.AnimationComp.loadByteArray(state['keysComp'])
			self.SetChannels()
			self.updateKeysView(init=True)
			pass

	def EditChannelName(self, chanName):
		self.channelListComp.StartEditCell(chanName)

	def RenameChannel(self, chanName, newName):
		if newName in self.ChannelNames.val:
			ui.messageBox('Warning', 
				f"{newName} already exists! Please use another name.",
				buttons=['Close'])
			return
		prevState = self.getAnimationCompState()
		self.Channels[chanName].setName(newName)		
		run("args[0]()", self.SetChannels, delayFrames=1)
		run("args[0](args[1])", self.postRenameChannel, prevState, 
			delayFrames=2)

	def postRenameChannel(self, prevState):
		curState = self.getAnimationCompState()
		ui.undo.startBlock(self.undoStateAnimCompName)
		ui.undo.addCallback(self.undoDeleteAppendChannels, 
							[prevState, curState])
		ui.undo.endBlock()

	def Toolmode(self):
		index = 6 if self.iParsComp.par.Toolmode.eval() == 'draw' else 0
		self.keysViewComp.par.cursor = index

	def unSelectAll(self):
		return 
	def transformPos(self, event):
		self.selectPos.x = event.u * self.keysViewComp.width
		self.selectPos.y = event.v * self.keysViewComp.height
		self.selectPos = self.keysTransformComp.worldTransform * self.selectPos
		return self.selectPos

	def SelectChannel(self, chan):
		if chan not in self.selectedChannels:
			self.selectedChannels.append(chan)

	def SelectAllKeys(self):
		firstSelected = False
		for chan in self.Channels.values():
			if chan.display:
				self.SelectChannel(chan)
				for i in range(chan.numSegments + 1):
					chan.selectKey(i, 1)
					if not firstSelected:
						self.updateViewKeySegment = chan.segments[i]
						firstSelected = True					

		self.keyframeControlsComp.ActiveAll(*self.GetKeyHandlesActive())			
		self.KeyframeControlsUpdateView(updateFunction=True)	

	def SelectAdjacentItem(self, dir):
		keyChannels = []
		handleChannels = []
		for channel in self.Channels.values():
			if channel.display:
				if channel.selectedKeys != []:
					keyChannels.append(channel)
				if channel.selectedHandles != []:
					handleChannels.append(channel)
		if keyChannels != []:
			for channel in keyChannels:
				if dir == 1:
					selected = reversed(sorted(channel.selectedKeys))
					for i in selected:
						channel.selectKey(i, 0)
						channel.selectKey(min(i + 1, channel.numSegments), 1)
				if dir == -1:
					selected = sorted(channel.selectedKeys)
					for i in selected:
						channel.selectKey(i, 0)
						channel.selectKey(max(i - 1, 0), 1)				
		if handleChannels != []:
			for channel in handleChannels:
				handleStep = -1 * (len(channel.selectedHandles) % 2) + 2	
				if dir == 1:
					selected = reversed(sorted(channel.selectedHandles))
					for i in selected:
						channel.selectHandle(i, 0)
						channel.selectHandle(min(i + handleStep, 
											channel.numSegments * 2 - 1), 1)
				if dir == -1:
					selected = sorted(channel.selectedHandles)
					for i in selected:
						channel.selectHandle(i, 0)
						channel.selectHandle(max(i - handleStep, 0), 1)	

		if len(keyChannels) > 0:
			chan = keyChannels[0]
			segmentIndex = chan.selectedKeys[0]		
			if segmentIndex < chan.numSegments:
				segment = chan.segments[segmentIndex]
			else:
				segment = (chan.segments[segmentIndex - 1], 1)		
			self.updateViewKeySegment = segment
		elif len(handleChannels) > 0:
			chan = handleChannels[0]
			handleIndex = chan.selectedHandles[0]
			segmentIndex = math.floor(handleIndex / 2.0)
			isOutHandle = handleIndex % 2	
			if isOutHandle == 1:
				self.updateViewOutHandleSegment = chan.segments[segmentIndex]
			else:
				self.updateViewInHandleSegment = chan.segments[segmentIndex]			

		self.keyframeControlsComp.ActiveAll(*self.GetKeyHandlesActive())			
		self.KeyframeControlsUpdateView(updateFunction=True)					

	def NudgeItem(self, nudge):
		x = nudge.x * 1
		y = nudge.y * self.keysTransformComp.par.sy
		keyPos = tdu.Position(math.copysign(x, nudge.x) 
							* int(abs(nudge.x) > 0), y, 0)
		numSelectedKeys = 0
		for channel in self.Channels.values():
			if channel.display:
				numSelectedKeys += len(channel.selectedKeys)
				if numSelectedKeys > 0:
					for channel in self.Channels.values():
						if channel.display:
							channel.setKeysRelXY(keyPos)
					break
		if numSelectedKeys == 0:
			x = nudge.x * self.keysTransformComp.par.sx
			keyPos = tdu.Position(math.copysign(x, nudge.x) 
							* int(abs(nudge.x) > 0), y, 0)
			for channel in self.Channels.values():
				if channel.display:	
					channel.setHandlesRelXY(keyPos)
		else:
			for chan in self.Channels.values():
				chan.setStartSetKeys()

	def InsertKey(self, chanName, x, y=None, expr='bezier()'):
		print ("InsertKey\n")
		chan = self.Channels[chanName]
		if chan.display:
			x = math.floor(self.insertPos.x)
			if all([segment.x0 != x and segment.x1 != x
						for segment in chan.segments]):
				chan.insertKey(x, y, funcName=expr)

	def insertKeyInNearestCurve(self, event):
		
		self.insertPos.x = event.u * self.keysViewComp.width
		
		
		#self.insertPos.y = event.v * self.keysViewComp.height
		#print (self.insertPos.x)
		#self.insertPos = self.keysTransformComp.worldTransform * self.insertPos
		#print (self.insertPos.x)
		#op(str(self.ownerComp.par.T) + "/local/time").frame=self.insertPos.x
		#lastSampleIndex = self.KeyframeLookupChop.numSamples - 1
		#x = math.floor(self.insertPos.x)
		#i = max(0, 
		#	min(lastSampleIndex, x - math.floor(self.KeysViewHorzRange[0])))
		#nearestChopChan = None
		#for chopChan in self.KeyframeLookupChop.chans():	
		#	if self.Channels[chopChan.name].display:	
		#		if nearestChopChan == None:
		#			nearestChopChan = chopChan
		#		elif (abs(chopChan[i] - self.insertPos.y) 
		#				< abs(nearestChopChan[i] - self.insertPos.y)):
		#			nearestChopChan = chopChan
		#if nearestChopChan is not None:		
		#	chan = self.Channels[nearestChopChan.name]
			
		#	if all([segment.x0 != x and segment.x1 != x
		#				for segment in chan.segments]):
		#		insertIndex = chan.insertKey(x, None)
		#		self.unSelectAll()
		#		chan.selectKey(insertIndex, 1)
		#		return {chan.name: insertIndex}


	def searchInExtValuesDat (self, chNameToSearch):
		
		#object_methods = [method_name for method_name in dir(self.Animationcomp)
  #                if callable(getattr(self.Animationcomp, method_name))]
		myValuesDat=op(self.ownerComp.par.Takevaluesdat)
		res=myValuesDat[str(chNameToSearch), 1]

		#print ("%s, %s" % (chNameToSearch, res ) )
		return res


	def insertKeys(self, event):
		self.insertPos.x = event.u * self.keysViewComp.width
		
		
		#self.insertPos.y = event.v * self.keysViewComp.height
		self.insertPos = self.keysTransformComp.worldTransform * self.insertPos		
		op(str(self.ownerComp.par.T) + "/local/time").frame=self.insertPos.x
		
	
		return insertInfos

	def insertKeysOriginal(self, event):
		print ("insertKeys\n")
		self.insertPos.x = event.u * self.keysViewComp.width
		self.insertPos.y = event.v * self.keysViewComp.height
		self.insertPos = self.keysTransformComp.worldTransform * self.insertPos	
		self.unSelectAll()
		insertInfos = {}
		for chan in self.Channels.values():
			if chan.display:
				print (chan.name)
				insertInfos[chan.name] = chan.insertKey(
												self.insertPos.x, None)
		return insertInfos

	def copyKeys(self):
		self.copiedKeys = {}
		offsetX = None
		for name, chan in self.Channels.items():
			if chan.display:		
				selKeys = sorted(chan.selectedKeys)
				for i, _id in enumerate(selKeys):
					if _id < chan.numSegments:
						segment = chan.segments[_id]
						if offsetX is None:
							offsetX = segment.x0
						else:
							offsetX = min(offsetX, segment.x0)
					else:
						segment = chan.segments[_id - 1]
						if offsetX is None:
							offsetX = segment.x1
						else:
							offsetX = min(offsetX, segment.x1)
		if offsetX is not None:
			for name, chan in self.Channels.items():
				if chan.display:
					self.copiedKeys[name] = []
					selKeys = sorted(chan.selectedKeys)
					for i, _id in enumerate(selKeys):
						if _id < chan.numSegments:
							segment = chan.segments[_id]
							x = segment.x0 - offsetX
							keyData = (segment.segmentType, x, segment.y0,
									segment.inslope, segment.inaccel,
									segment.outslope, segment.outaccel)
						else:
							segment = chan.segments[_id - 1]
							x = segment.x1 - offsetX
							keyData = (segment.segmentType, x, segment.y1,
									segment.inslope, segment.inaccel,
									segment.outslope, segment.outaccel)
						self.copiedKeys[name].append(keyData)
		pprint(self.copiedKeys)

	def cutKeys(self):
		self.copyKeys()
		self.DeleteSelectedKeys()

	def pasteKeys(self):
		if self.keysPanel.inside:
			self.insertPos.x = self.keysPanel.insideu * self.keysViewComp.width
			self.insertPos.y = self.keysPanel.insidev * self.keysViewComp.height
			self.insertPos = (self.keysTransformComp.worldTransform 
							* self.insertPos)
			insertIndices = {}			
			for chanName, chanKeysData in self.copiedKeys.items():
				if chanName in self.ChannelNames.val:
					chan = self.Channels[chanName]
					insertIndices[chan.name] = []
					if chan.display:
						for keyData in chanKeysData:
							x = self.insertPos.x + keyData[1]
							insertIndex = chan.insertKey(x, keyData[2], 
													funcName=keyData[0])
							insertIndices[chan.name].append(
								(insertIndex, *keyData[3:])
							)
					insertIndices[chan.name].sort()

			for chanName, insertData in insertIndices.items():
				chan = self.Channels[chanName]
				for data in insertData:
					segment = chan.segments[data[0]]
					if segment.hasHandles:
						segment.setInSlopeAccel(data[1], data[2])
						segment.setOutSlopeAccel(data[3], data[4])

	def drawKeyframes(self, event):
		# needs update to function properly
		self.unSelectAll()
		channel = list(self.Channels.values())[0]
		if event.selectStart:
			self.drawPrevPos = self.transformPos(event)
			self.drawPos = self.drawPrevPos.copy()
			self.drawPrevVector = self.drawPrevPos - self.drawPos
			self.drawPrevVector.normalize()	
			self.drawVector = self.drawPrevVector.copy()
			insertIndex = channel.insertKey(self.drawPos.x, 
								self.drawPos.y,
								self.iParsComp.par.Insertfunction.eval())
		
		else: 
			self.drawPos = self.transformPos(event)
			self.drawVector = self.drawPrevPos - self.drawPos
			self.drawVector.normalize()
			dot = self.drawPrevVector.dot(self.drawVector)
			dotThreshold = .88
			# #if self.drawPrevVector != self.drawVector:
			if dot < dotThreshold:
				insertIndex = channel.insertKey(self.drawPos.x, 
								self.drawPos.y,
								self.iParsComp.par.Insertfunction.eval())
			self.drawPrevPos = self.drawPos.copy()
			self.drawPrevVector = self.drawVector.copy()
			self.drawPrevVector.normalize()		

	def DeleteKey(self, chanName, i):
		if self.Channels[chanName].numSegments > 1:
			self.Channels[chanName].deleteKey(i)

	def DeleteSelectedKeys(self):
		for channel in self.Channels.values():
			if channel.numSegments > 1:
				channel.selectedKeys.sort()
				channel.selectedKeys.reverse()
				for i in channel.selectedKeys:
					channel.deleteKey(i)
		
		self.unSelectAll()
		self.SetChannels()

	def scaleKeys(self, event):	
		self.setPos = self.transformPos(event)
		self.setPos.x -= event.pos.x
		self.setPos.y -= event.pos.y

		geo = event.pickOp.parent()
		i = geo.par.Geotype.menuIndex
		if i == 0:
			indices = event.custom['indices']
			pickChan = self.ChannelsList[indices[0]]
			clickId = indices[2]			

			if clickId < pickChan.numSegments:
				pickSegment = pickChan.segments[clickId]
			else:
				pickSegment = pickChan.segments[clickId - 1]
			if not self.startScale:
				self.startScale = True
				self.scaleKeysScale = self.scaleKeysScale * .0 + 1
				self.scaleStartPos.x = self.setPos.x
				self.scaleStartPos.y = self.setPos.y
				for chan in self.Channels.values():
					if len(chan.selectedKeys) > 0:
						minId = min(chan.selectedKeys)
					else:
						minId = 0
					for _id in chan.selectedKeys:
						if _id < chan.numSegments:
							segment = chan.segments[_id]
							segment.scaleDeltas[0][0] = (
													segment.x0 - event.pos.x)
							segment.scaleDeltas[0][1] = (
													segment.y0 - event.pos.y)														
						else:
							segment = chan.segments[_id - 1]
							segment.scaleDeltas[1][0] = (
													segment.x1 - event.pos.x)
							segment.scaleDeltas[1][1] = (
													segment.y1 - event.pos.y)
						if segment.hasHandles:
							relX, relY = self.getHandleRelXY(
								segment.inslope, segment.inaccel
							)
							segment.scaleDeltas[2][0] = (relX)
							segment.scaleDeltas[2][1] = (relY)
							relX, relY = self.getHandleRelXY(
								segment.outslope, -segment.outaccel
							)															
							segment.scaleDeltas[3][0] = (relX)
							segment.scaleDeltas[3][1] = (relY)
					if minId != 0:
						segment = chan.segments[minId - 1]
						if segment.hasHandles:
							relX, relY = self.getHandleRelXY(
								segment.inslope, segment.inaccel
							)
							segment.scaleDeltas[2][0] = (relX)
							segment.scaleDeltas[2][1] = (relY)
							relX, relY = self.getHandleRelXY(
								segment.outslope, -segment.outaccel
							)															
							segment.scaleDeltas[3][0] = (relX)
							segment.scaleDeltas[3][1] = (relY)

			if self.kd and not self.kf:
				self.scaleKeysScale.x = (1 
					+ (self.setPos.x - self.scaleStartPos.x) 
					/ (self.KeysViewHorzRange[1] - self.KeysViewHorzRange[0]))
				self.scaleKeysScale.y = 1
			elif self.kf and not self.kd:
				self.scaleKeysScale.x = 1
				self.scaleKeysScale.y = (1 
					+ (self.setPos.y - self.scaleStartPos.y)
					/ (self.KeysViewVertRange[1] - self.KeysViewVertRange[0]))
			else:
				self.scaleKeysScale.x = (1 
					+ (self.setPos.x - self.scaleStartPos.x) 
					/ (self.KeysViewHorzRange[1] - self.KeysViewHorzRange[0]))
				self.scaleKeysScale.y = (1 
					+ (self.setPos.y - self.scaleStartPos.y)
					/ (self.KeysViewVertRange[1] - self.KeysViewVertRange[0]))

			for chan in self.Channels.values():
				if chan.display:
					if len(chan.selectedKeys) > 0:
						minId = min(chan.selectedKeys)
						maxId = max(chan.selectedKeys)
					else:
						minId = -1
					for _id in chan.selectedKeys:				
						if _id < chan.numSegments:
							segment = chan.segments[_id]
							if segment.hasHandles:
								if _id == maxId and clickId != _id:
									sx = 1 / self.scaleKeysScale.x
									sy = self.scaleKeysScale.y
								elif _id == clickId and _id == maxId:
									sx = 1
									sy = 1							
								else:
									sx = self.scaleKeysScale.x
									sy = self.scaleKeysScale.y							
								inHandleX = (segment.scaleDeltas[2][0] 
											* sx)
								inHandleY = (segment.scaleDeltas[2][1] 
											* sy)
								outHandleX = (segment.scaleDeltas[3][0] 
											* sx)
								outHandleY = (segment.scaleDeltas[3][1] 
											* sy)
								segment.setInHandleRelXY(
									inHandleX, inHandleY, True)
								segment.setOutHandleRelXY(
									outHandleX, outHandleY, True)
							deltaX = (segment.scaleDeltas[0][0] 
										* self.scaleKeysScale.x)
							deltaY = (segment.scaleDeltas[0][1] 
										* self.scaleKeysScale.y)
							x = deltaX + event.pos.x
							y = deltaY + event.pos.y
							segment.setInXY(x, y)			
						else:
							segment = chan.segments[_id - 1]
							if segment.hasHandles:
								inHandleX = (segment.scaleDeltas[2][0] 
											* self.scaleKeysScale.x)
								inHandleY = (segment.scaleDeltas[2][1] 
											* self.scaleKeysScale.y)
								outHandleX = (segment.scaleDeltas[3][0] 
											* self.scaleKeysScale.x)
								outHandleY = (segment.scaleDeltas[3][1] 
											* self.scaleKeysScale.y)
								segment.setInHandleRelXY(
									inHandleX, inHandleY, True)
								segment.setOutHandleRelXY(
									outHandleX, outHandleY, True)						
							deltaX = (segment.scaleDeltas[1][0] 
										* self.scaleKeysScale.x)
							deltaY = (segment.scaleDeltas[1][1] 
										* self.scaleKeysScale.y)
							x = deltaX + event.pos.x
							y = deltaY + event.pos.y
							segment.setOutXY(x, y)
					if minId > 0:
						segment = chan.segments[minId - 1]
						if segment.hasHandles:
							if minId == clickId:
								sx = 1
								sy = 1
							else:
								sx = 1 / self.scaleKeysScale.x
								sy = self.scaleKeysScale.y																
							inHandleX = (segment.scaleDeltas[2][0] 
										* sx)
							inHandleY = (segment.scaleDeltas[2][1] 
										* sy)
							outHandleX = (segment.scaleDeltas[3][0] 
										* sx)
							outHandleY = (segment.scaleDeltas[3][1] 
										* sy)
							segment.setInHandleRelXY(
								inHandleX, inHandleY, True)
							segment.setOutHandleRelXY(
								outHandleX, outHandleY, True)	
					self.setLabelsTy()						

	def selectItem(self, event):
		geo = event.pickOp.parent()
		
		i = geo.par.Geotype.menuIndex
		if i < 2:
			indices = event.custom['indices']
			chan = self.ChannelsList[indices[0]]
			_id = indices[2 + i]			
			self.selectFuncs[i](chan, _id, 1)
		else:
			chan = self.Channels[geo.par.Channelname.eval()]
			self.SelectSegment(chan, event)

	def SelectKey(self, chan, _id, state):
		self.SelectChannel(chan)
		chan.selectKey(_id, state)
		if len(self.selectedChannels) > 0:
			if len(chan.selectedKeys) > 0:
				if _id < chan.numSegments:
					self.updateViewKeySegment = chan.segments[_id]
				else:
					self.updateViewKeySegment = (chan.segments[_id - 1], 1)
				self.KeyframeControlsUpdateView(updateFunction=True)

	def SelectHandle(self, chan, _id, state):
		self.SelectChannel(chan)
		chan.selectHandle(_id, state)
		if len(self.selectedChannels) > 0:
			if len(chan.selectedHandles) > 0:
				segmentIndex = math.floor(_id / 2.0)
				isOutHandle = _id % 2	
				if isOutHandle == 1:
					self.updateViewOutHandleSegment = chan.segments[segmentIndex]
				else:
					self.updateViewInHandleSegment = chan.segments[segmentIndex]
				self.KeyframeControlsUpdateView()

	def SelectSegment(self, chan, event):
		pos = self.transformPos(event)
		segment = chan.selectSegment(pos.x, 1)
		self.SelectChannel(chan)
		if segment is not None:
			self.updateViewKeySegment = segment
		self.KeyframeControlsUpdateView()

	def itemIsSelected(self, event):
		geo = event.pickOp.parent()
		i = geo.par.Geotype.menuIndex
		if i < 2:
			indices = event.custom['indices']
			chan = self.ChannelsList[indices[0]]
			_id = indices[2 + i]
			isSelected = chan.isSelectedFuncs[i](_id)	
		else:
			chan = self.Channels[geo.par.Channelname.eval()]
			isSelected = chan.isSelectedFuncs[i](event.pos.x)
		return isSelected

	def setItem(self, event):
		geo = event.pickOp.parent()
		i = geo.par.Geotype.menuIndex
		if i < 2:
			indices = event.custom['indices']
			chan = self.ChannelsList[indices[0]]
			clickId = indices[2 + i]			
		else:
			chan = self.Channels[geo.par.Channelname.eval()]
			clickId = event.instanceId

		if not self.startSet:
			self.startSet = True						
			self.keyframeControlsComp.ActiveAll(*self.GetKeyHandlesActive())

		self.setPos = self.transformPos(event)
		if self.kshift == 0:
			self.setPos.x -= event.pos.x
			self.setPos.y -= event.pos.y
		else:
			if self.kctrl == 0:	
				self.setPos.x -= event.pos.x
				self.setPos.y = self.startSetPosOffset.y
			else:
				self.setPos.x = self.startSetPosOffset.x
				self.setPos.y -= event.pos.y	

		for chan in self.selectedChannels:
			chan.setFuncs[i](
				clickId,
				self.setPos, 
				self.startSetPosOffset,
				event.selectStart
			)
		## Alternate method for setting handles using relative 
		## slope and accel rather than x, y
		## needs to be relative angle not slope for better results at
		## small vertical scale (high vert zoom ie -1 to 1) since slope 
		## is a relation of distance - y/x.....
		## need to update for new geo rendering method
		# clickIds = [-2, clickId]
		# if i != 1:
		# for chan in self.selectedChannels:
		# 	chan.setFuncs[i](
		# 		clickIds[chan == pickChan],
		# 		self.setPos, 
		# 		self.startSetPosOffset,
		# 		event.selectStart
		# 	)
		# else:
		# 	segmentIndex = math.floor(clickId / 2.0)
		# 	pickSeg = pickChan.segments[segmentIndex]
		# 	outClicked = clickId % 2
		# 	if outClicked and pickSeg.lockHandles:
		# 		if segmentIndex + 1 < pickChan.numSegments:	
		# 			nextSegment = pickChan.segments[segmentIndex + 1]
		# 			i = nextSegment.handlesChopInIndex
		# 			if nextSegment.handlesChopSelected[i]:
		# 				self.setPos.x = (
		# 							self.startSetPosOffset.x - self.setPos.x)
		# 				self.setPos.y = (
		# 							self.startSetPosOffset.y - self.setPos.y)
		# 	if event.selectStart:
		# 		if outClicked == 0:
		# 			offsetX = (pickSeg.points[1].x - pickSeg.points[0].x)
		# 			offsetY = (pickSeg.points[1].y - pickSeg.points[0].y)
		# 		else:
		# 			offsetX = (pickSeg.points[2].x - pickSeg.points[3].x)
		# 			offsetY = (pickSeg.points[2].y - pickSeg.points[3].y)
		# 		self.handleOffsetX = self.setPos.x - offsetX
		# 		self.handleOffsetY = self.setPos.y - offsetY
		# 	self.setPos.x -= self.handleOffsetX
		# 	self.setPos.y -= self.handleOffsetY	 
		# 	getSlopeAccel = pickSeg.getSlopeAccelFromRelXY[outClicked]
		# 	slope, accel = getSlopeAccel(self.setPos.x, self.setPos.y)		
		# 	pickSeg.setSlopeAccel[outClicked](slope, accel)
		# 	if event.selectStart:
		# 		self.startSlope = slope	
		# 		self.startAccel = accel

		# 	relSlope = slope - self.startSlope		
		# 	relSlopes = [relSlope, -relSlope]
		# 	relAccel = (accel - self.startAccel)

		# 	for chan in self.selectedChannels:
		# 		for _id in chan.selectedHandles:
		# 			segmentIndex = math.floor(_id / 2.0)
		# 			segment = chan.segments[segmentIndex]
		# 			if chan != pickChan or _id != clickId:
		# 				isOut = _id % 2	
		# 				segment.setRelSlopeAccel[isOut](
		# 					relSlopes[isOut != outClicked],
		# 					relAccel,
		# 					event.selectStart
		# 				)					

		self.setLabelsTy()
		self.KeyframeControlsUpdateView()

	def onPickSelectStart(self, event):
		self.SetPrevStateChannels()
		
		self.startSetPosOffset.x = event.u * self.keysViewComp.width
		self.startSetPosOffset.y = event.v * self.keysViewComp.height
		self.startSetPosOffset = (self.keysTransformComp.worldTransform 
												* self.startSetPosOffset)
		self.startSetPosOffset.x = self.startSetPosOffset.x - event.pos.x
		self.startSetPosOffset.y = self.startSetPosOffset.y - event.pos.y

		self.pickStartVals = {}
		self.pickStartVals['uv'] = (event.u, event.v)
		self.pickStartVals['shift'] = self.keysViewComp.panel.shift.val
		self.pickStartVals['ctrl'] = self.keysViewComp.panel.ctrl.val
		self.pickStartVals['alt'] = self.keysViewComp.panel.alt.val

	def onPickEnd(self, didAction=True):
		self.keyframeControlsComp.ActiveAll(True, True, True)	
		#if self.switchMarqueeTop.par.index:	
		#	self.marqueeSelectEnd()	
		self.startSet = False
		self.startScale = False
		if didAction:
			self.SetCurStateChannels()	
		self.keyframeControlsComp.ActiveAll(*self.GetKeyHandlesActive())

	def SetCurStateChannels(self, force=False):
		return
	def SetPrevStateChannels(self):
		self.prevStateChannels = dict(self.curStateChannels)

	def undoStateChannels(self, isUndo, info):
		if isUndo:
			state = info[0]
		else:
			state = info[1]	
		if state is not None:
			self.channelsDat.text = state['channelsDat']
			channelsState = state['channels']
			for key, chanData in channelsState.items():
				self.Channels[key].setState(chanData)
			self.SetChannels()
			for key, chanData in channelsState.items():
				chan = self.Channels[key]
				for selKey in chanData['selectedKeys']:
					chan.selectKey(selKey, 1)
					self.SelectChannel(chan)		
				if len(chanData['selectedHandles']) > 0:
					chan.selectHandles(chanData['selectedHandles'])
					self.SelectChannel(chan)					
				chan.setStartSetKeys()				
			self.SetPrevStateChannels()
			self.curStateChannels = dict(state)			
			self.channelListComp.Refresh(self.Channels, self.ChannelNames.val)	
			self.updateKeysView(init=True)	

			keyHandlesActive = self.GetKeyHandlesActive()
			self.keyframeControlsComp.ActiveAll(*keyHandlesActive)
			self.KeyframeControlsUpdateView(updateFunction=True)	

	def marqueeSelectStart(self, event):
		self.keysRenderPickDat.par.strategy = 'select'
		self.keysViewComp.par.Marqueeselectstartu = event.u
		self.keysViewComp.par.Marqueeselectstartv = event.v
		self.switchMarqueeTop.par.index = 1
		self.selStartPos.x = event.u * self.keysViewComp.width
		self.selStartPos.y = event.v * self.keysViewComp.height
		self.selStartPos = self.keysTransformComp.worldTransform * self.selStartPos
		if self.kshift == 0:
			self.curMarqKeys = []
			self.curMarqHandles = []
			self.selectedChannels = []			
	
	def marqueeSelect(self, event):
		self.selectPos = self.transformPos(event)
		return

	def marqueeSelectEnd(self):
		if self.marqueeSelecting:
			mCoords = [[self.selStartPos.x, self.selectPos.x], 
						[self.selStartPos.y, self.selectPos.y]]
			mCoords[0].sort()
			mCoords[1].sort()
			
			chan = None
			if (self.curMarqKeys == [] and self.curMarqHandles == []):
				start = int(math.floor(mCoords[0][0]))
				end = int(math.ceil(mCoords[0][1]))
				try:
					self.animLookupComp.par.start = start
					self.animLookupComp.par.end = end
					self.KeyframeLookupChop.cook(force=True)
					if len(self.selectedChannels) > 0:
						chan = self.selectedChannels[0]
						segmentIndex = chan.selectedKeys[0]		
						self.updateViewKeySegment = chan.segments[segmentIndex]
				except Exception as e:
					traceback.print_exc()

				self.animLookupComp.par.start = (
					self.keysViewComp.par.Horzrange1)
				self.animLookupComp.par.end = (
					self.keysViewComp.par.Horzrange2)				

		self.GetKeyHandlesActive()
		self.KeyframeControlsUpdateView(updateFunction=True)

		self.keysRenderPickDat.par.strategy = 'holdfirst'
		self.switchMarqueeTop.par.index = 0		

	def OnKeyboardIn(self, key, character,
					alt, lAlt, rAlt, ctrl, lCtrl, rCtrl,
					shift, lShift, rShift, state, time, cmd, lCmd, rCmd):
		# TODO create lookup... 
		if state:
			
			if key == 'a' and ctrl:
				self.SetPrevStateChannels()	
				self.SelectAllKeys()
				self.SetCurStateChannels()		
			elif key == 'h':
				self.SetPrevStateChannels()	
				self.keysNavHome()
				self.SetCurStateChannels()		
			elif key == 't':
				self.SetPrevStateChannels()	
				self.toggleSelectedLockHandles()
				self.SetCurStateChannels()		
			elif key == 'c' and ctrl:
				self.SetPrevStateChannels()	
				self.copyKeys()
				self.SetCurStateChannels()		
			elif key == 'x' and ctrl:
				self.SetPrevStateChannels()	
				self.cutKeys()
				self.SetCurStateChannels()		
			elif key == 'v' and ctrl:
				self.SetPrevStateChannels()	
				self.pasteKeys()
				self.SetCurStateChannels()			
			elif key == 'delete':
				self.SetPrevStateChannels()	
				self.DeleteSelectedKeys()
				self.SetCurStateChannels()	
			elif key == 'tab':
				self.SetPrevStateChannels()	
				self.SelectAdjacentItem(-1 if shift else 1)
				self.SetCurStateChannels()		
			elif key in ('right', 'left', 'up', 'down'):
				self.SetPrevStateChannels()	
				scale = 1.0
				if self.kshift:
					scale = 2.0
				elif self.kctrl:
					scale = 4.0
				elif self.kalt:
					scale = 8.0
				nudge = self.nudgeDir[key] * scale
				self.NudgeItem(nudge)	
				self.SetCurStateChannels()		
				
	def keysNavHome(self):
		xBounds = [None, None]
		yBounds = [None, None]
		chansDisplayed = False
		for chan in self.Channels.values():
			if chan.display:
				chansDisplayed = True
				for segment in chan.segments:
					if xBounds[0] == None:
						xBounds[0] = segment.x0
						xBounds[1] = segment.x0
						yBounds[0] = segment.y0
						yBounds[1] = segment.y0
					xBounds[0] = min(segment.x0, xBounds[0])
					xBounds[1] = max(segment.x0, xBounds[1])
					yBounds[0] = min(segment.y0, yBounds[0])
					yBounds[1] = max(segment.y0, yBounds[1])
					if segment.hasHandles:
						relX, relY = self.getHandleRelXY(
											segment.inslope, segment.inaccel)
						y = segment.y0 + relY
						yBounds[0] = min(y, yBounds[0])
						yBounds[1] = max(y, yBounds[1])	
						relX, relY = self.getHandleRelXY(
											segment.outslope, -segment.outaccel)
						y = segment.y1 + relY
						yBounds[0] = min(y, yBounds[0])
						yBounds[1] = max(y, yBounds[1])												
					if segment.isLastSegment:
						xBounds[0] = min(segment.x1, xBounds[0])
						xBounds[1] = max(segment.x1, xBounds[1])
						yBounds[0] = min(segment.y1, yBounds[0])
						yBounds[1] = max(segment.y1, yBounds[1])

		if chansDisplayed:
			xRange = (xBounds[1] - xBounds[0])
			yRange = (yBounds[1] - yBounds[0])
			xStart = xBounds[0]
			yStart = yBounds[0]
			if yRange == 0:
				yRange = 2
				yStart -= 1
		else:
			xRange = self.AnimationRangeEnd - self.AnimationRangeStart
			yRange = 2
			xStart = self.AnimationRangeStart
			yStart = -1

		sx = xRange / (self.keysViewComp.width - self.navHomeMarginSums[0])
		tx = xStart - sx * self.navHomeMargins[0]
		sy = yRange / (self.keysViewComp.height - self.navHomeMarginSums[1])
		ty = yStart - sy * self.navHomeMargins[2]
	

		self.keysTransformComp.par.tx = tx
		self.keysTransformComp.par.ty = ty
		self.keysTransformComp.par.sx = sx
		self.keysTransformComp.par.sy = sy
		self.keysCamComp.par.tx = 0
		self.keysCamComp.par.ty = 0
		self.keysCamComp.par.px = 0
		self.keysCamComp.par.py = 0
		self.keysCamComp.par.sx = 1
		self.keysCamComp.par.sy = 1
		self.SetNavRange()

	def keysNavEnd(self, event):
		s, r, t = self.keysCamComp.worldTransform.decompose()
		self.keysTransformComp.par.tx = t[0]
		self.keysTransformComp.par.ty = t[1]
		self.keysTransformComp.par.sx = s[0]
		self.keysTransformComp.par.sy = s[1]
		self.keysCamComp.par.tx = 0
		self.keysCamComp.par.ty = 0
		self.keysCamComp.par.px = 0
		self.keysCamComp.par.py = 0
		self.keysCamComp.par.sx = 1
		self.keysCamComp.par.sy = 1

	def keysNav(self, event):
		u = event.u
		v = event.v
		startU = self.pickStartVals['uv'][0]
		startV = self.pickStartVals['uv'][1]
		if self.pickStartVals['shift']:
			pivotX = startU * self.keysViewComp.width
			pivotY = startV * self.keysViewComp.height
			self.keysCamComp.par.px = pivotX
			self.keysCamComp.par.py = pivotY
			relU = startU - u
			relV = startV - v
			su = 1.0 + relU
			sv = 1.0 + relV
			su *= su
			sv *= sv
			self.keysCamComp.par.sx = max(0.0, su)
			self.keysCamComp.par.sy = max(0.0, sv)	
		else:
			relX = vMath.expandValue(startU - u, 0.0, self.keysViewComp.width)
			relY = vMath.expandValue(startV - v, 0.0, self.keysViewComp.height)	
			self.keysCamComp.par.tx = relX
			self.keysCamComp.par.ty = relY

		self.SetNavRange()

	def GetKeysNavInsidePos(self):
		try:
			self.insidePos.x = self.keysPanel.insideu.val * self.keysViewComp.width
			self.insidePos.y = self.keysPanel.insidev.val * self.keysViewComp.height
			self.insidePos = self.keysTransformComp.worldTransform * self.insidePos

			#if self.keysPanel.lselect.val:
			#	self.insidePos.x -= self.startSetPosOffset.x
			#	self.insidePos.y -= self.startSetPosOffset.y	
		except:
			pass
		return self.insidePos

	def SetNavRange(self):
		w = self.keysViewComp.width
		h = self.keysViewComp.height
		xfm = self.keysCamComp.worldTransform
		size = xfm * tdu.Vector(w, h, 1.0)
		x0 = xfm[0, 3] 
		y0 = xfm[1, 3]
		x1 = x0 + size.x
		y1 = y0 + size.y
		self.KeysViewHorzRange = (x0, x1)
		self.KeysViewVertRange = (y0, y1)
		self.keysRenderPickComp.SetView()
		self.setLabelsTy()

	def setLabelsTy(self):
		return 

	def updateKeysView(self, init=False):
		self.animLookupComp.cook(force=True, recurse=True)
		if init:
			numChans = len(0)
			self.channelLabelsPos = np.ndarray((2, numChans))
			self.channelLabelTyPars = []
		pos = self.labelStartTx
		viewWidth = self.keysViewComp.width - self.labelStartTx
		displayed = []
		numDisplayed = len(displayed)
		maxLabelWidth = viewWidth / (numDisplayed + 1)
	
		keys = []
		handles = []
		labelTops = []
		labelValues = []
		root = self.ChannelsComp.path
		replace1 = '../../channels'
		replace2 = '../../../channels'

		
		self.keysViewKeysJoinChop.par.chops = ' '.join(keys)
		self.keysViewHandlesJoinChop.par.chops = ' '.join(handles)
		self.keysViewLabelsComp.par.instancetexs = ' '.join(labelTops)
		self.keysViewLabelsJoinChop.par.chops = ' '.join(labelValues)
		self.setLabelsTy()

	def toggleSelectedLockHandles(self):
		for chan in self.selectedChannels:
			chan.toggleSelectedLockHandles()

	def OnDropView(self, comp, info):
		for item in info['dragItems']:
			_type = type(item)
			if _type == Par:
				if (item.isNumber or item.isMenu 
								or item.isToggle 
								or item.isPulse):
					name = f"{item.owner.name}_{item.name}"
					if not self.Channels.get(name, False):
						self.AppendChannel(name, startVal=item.eval())
						outChop = self.AnimationComp.op('out')
						shortCutPath = item.owner.shortcutPath(outChop)
						expr = f"{shortCutPath}['{name}']"
						run("args[0].expr = args[1]", item, expr, delayFrames=1)
					else:
						print(
							f"Animation Comp already has channel named: {name}")
				else:
					print('Dropped non numeric par')
			elif _type == TD_CHOP_CHANNEL:
				name = f"{item.owner.name}_{item.name}"
				if not self.Channels.get(name, False):
					self.AppendChannel(name, startVal=item.eval())
				else:
					print(
						f"Animation Comp already has channel named: {name}")
			elif isinstance(item, CHOP):
				for chopChan in item.chans():
					name = f"{item.name}_{chopChan.name}"
					if not self.Channels.get(name, False):
						self.AppendChannel(name, updateKeysView=False, 
										startVal=chopChan.eval())
					else:
						print(
						f"Animation Comp already has channel named: {name}")
				run("args[0](init=True)", self.updateKeysView,
					delayFrames=item.numChans + 1)
			elif isinstance(item, DAT):
				mode = ui.messageBox('Create Channels From DAT Mode', 
					'Create Channels', 
					buttons=['Cancel', 'From First Row', 'From First Column']
				)
				if mode > 0:
					cells = item.row(0) if mode == 1 else item.col(0)
					for i, cell in enumerate(cells):
						if cell.val.isidentifier():
							name = f"{cell.val}"
							if not self.Channels.get(name, False):
								self.AppendChannel(name, updateKeysView=False)						
							else:
								print(
								f"Animation Comp already has channel named: {name}")
						else:
							print(
								f"{cell.val} is not a valid channel name")									
					run("args[0](init=True)", self.updateKeysView,
						delayFrames=len(cells) + 1)						
			elif isinstance(item, animationCOMP):
				if 'KEYFRAMER_ANIM_COMP' not in item.tags:
					m = (f"The animationCOMP: {item.path} is not 'Keyframer' "
						f"configured would you like to convert it?")
					confirm = ui.messageBox('Convert', m, 
											buttons=['Cancel', 'convert'])
					if confirm == 1:
						comp = self.convertToKeyframerAnimComp(item)
						if comp is not None:
							self.AnimationComp = comp
						else:
							print(f"Unable to convert: {item.path}")	
				else:	
					if item == self.animationTemplateComp:
						print('Dropped in Keyframer, choose another location.')
					else:
						self.AnimationComp = item
			else:
				print('Dropped invalid object.')

	def OnNewAnimDragStart(self, info):
		return [self.animationTemplateComp]

	def OnNewAnimDragEnd(self, info):
		if info['accepted']:
			results = info.get('dropResults')
			if results is not None:
				createdOPs = results.get('createdOPs', [])
				if len(createdOPs) > 0:
					animComp = createdOPs[0]
					name = self.newAnimNameComp.par.Value.eval()
					if name == '':
						name = 'animation1'
					if animComp.parent().op(name) is None:
						animComp.name = name
					else:
						print(f"{name} animation comp already exists!")
					self.animCompComp.UpdateView(animComp)

	def OnAppendChannels(self):
		prevState = self.getAnimationCompState()		
		names = self.newChannelNamesComp.par.Value.eval().split(' ')
		for i, name in enumerate(names):
			self.AppendChannel(name, updateKeysView=False)
		run("args[0](init=True)", self.updateKeysView, delayFrames=len(names) + 1)		
		curState = self.getAnimationCompState()
		ui.undo.startBlock(self.undoStateAnimCompName)
		ui.undo.addCallback(self.undoDeleteAppendChannels, 
							[prevState, curState])
		ui.undo.endBlock()

	def OpenContextMenu(self, fromComp, *args):
		info = self.contextMenuLookup[fromComp.name]
		self.contextMenuComp.OpenMenu(fromComp,
			info['menuItems'],
			*args
		)

	def KeyframeControlsUpdateView(self, updateFunction=False):
		if self.keysSelected:
			if not isinstance(self.updateViewKeySegment, tuple):
				self.keyframeControlsComp.UpdateViewKey(
					self.updateViewKeySegment.x0, 
					self.updateViewKeySegment.y0
				)
				if updateFunction:
					self.keyframeControlsComp.UpdateViewFunction(
					self.updateViewKeySegment.segmentType
					)	
			else:
				self.keyframeControlsComp.UpdateViewKey(
					self.updateViewKeySegment[0].x1, 
					self.updateViewKeySegment[0].y1
				)
				if updateFunction:
					self.keyframeControlsComp.UpdateViewFunction(
					self.updateViewKeySegment[0].segmentType
					)					
		if self.inHandlesSelected:
			self.keyframeControlsComp.UpdateViewInHandle(
				self.updateViewInHandleSegment.inslope, 
				self.updateViewInHandleSegment.inaccel
			)
		if self.outHandlesSelected:
			self.keyframeControlsComp.UpdateViewOutHandle(
				self.updateViewOutHandleSegment.outslope, 
				self.updateViewOutHandleSegment.outaccel
			)		
	
	def GetKeyHandlesActive(self):
		self.keysSelected = False
		self.inHandlesSelected = False
		self.outHandlesSelected = False
		self.lastSelectedKey = None
		self.lastSelectedInHandle = None
		self.lastSelectedOutHandle = None
		return self.keysSelected, self.inHandlesSelected, self.outHandlesSelected
		
	def OnChannelListSetValue(self, element, value):
		chanName = element.cellAttribs[value[0], 0].text
		self.Channels[chanName].display = value[2]
		self.updateKeysView()

	def SetFrameSelectedKeyframes(self, frame):
		for chan in self.Channels.values():
			for _id in chan.selectedKeys:
				if _id < chan.numSegments:
					segment = chan.segments[_id]
					value = segment.y0
					segment.setInXY(frame, value)
					segment.startSetKeyIn.x = segment.x0
				else:
					segment = chan.segments[_id - 1]
					value = segment.y1
					segment.setOutXY(frame, value)
					segment.startSetKeyOut.x= segment.x1	
		self.setLabelsTy()

	def SetValueSelectedKeyframes(self, value):
		for chan in self.Channels.values():
			for _id in chan.selectedKeys:
				if _id < chan.numSegments:
					segment = chan.segments[_id]
					frame = segment.x0
					segment.setInXY(frame, value)
					segment.startSetKeyIn.y = segment.y0
				else:
					segment = chan.segments[_id - 1]
					frame = segment.x1
					segment.setOutXY(frame, value)
					segment.startSetKeyOut.y = segment.y1				
		self.setLabelsTy()

	def SetInslopeSelectedKeyframes(self, slope):
		for chan in self.Channels.values():
			for _id in chan.selectedHandles:
				if _id % 2 == 0:
					segmentIndex = math.floor(_id / 2.0)
					segment = chan.segments[segmentIndex]
					segment.setInSlopeAccel(slope=slope)
			for _id in chan.selectedKeys:
				segment = chan.segments[_id]
				if segment.hasHandles:
					segment.setInSlopeAccel(slope=slope)					
		self.setLabelsTy()

	def SetInaccelSelectedKeyframes(self, accel):
		accel = max(0, accel)
		for chan in self.Channels.values():
			for _id in chan.selectedHandles:
				if _id % 2 == 0:
					segmentIndex = math.floor(_id / 2.0)
					segment = chan.segments[segmentIndex]
					segment.setInSlopeAccel(accel=accel)
			for _id in chan.selectedKeys:
				segment = chan.segments[_id]
				if segment.hasHandles:
					segment.setInSlopeAccel(accel=accel)	
		self.setLabelsTy()

	def SetOutslopeSelectedKeyframes(self, slope):
		for chan in self.Channels.values():
			for _id in chan.selectedHandles:
				if _id % 2 == 1:
					segmentIndex = math.floor(_id / 2.0)
					segment = chan.segments[segmentIndex]
					segment.setOutSlopeAccel(slope=slope)
			for _id in chan.selectedKeys:
				if _id != 0:
					segment = chan.segments[_id - 1]
					if segment.hasHandles:
						segment.setOutSlopeAccel(slope=slope)
		self.setLabelsTy()

	def SetOutAccelSelectedKeyframes(self, accel):
		accel = max(0, accel)
		for chan in self.Channels.values():
			for _id in chan.selectedHandles:
				if _id % 2 == 1:
					segmentIndex = math.floor(_id / 2.0)
					segment = chan.segments[segmentIndex]
					segment.setOutSlopeAccel(accel=accel)
			for _id in chan.selectedKeys:
				if _id != 0:
					segment = chan.segments[_id - 1]
					if segment.hasHandles:
						segment.setOutSlopeAccel(accel=accel)					
		self.setLabelsTy()

	def SetFunctionSelectedKeyframes(self, i):
		# TODO needs it's own undo function
		self.SetPrevStateChannels()			
		viewKeySegment = (self.updateViewKeySegment.owner.name, 
						self.updateViewKeySegment.index)
		selectedKeys = {}
		for name, chan in self.Channels.items():
			selectedKeys[name] = []
			for _id in chan.selectedKeys:
				selectedKeys[name].append(_id)
		function = self.segmentFuncNames[i]
		editedSegments = []
		for chan in self.Channels.values():		
			for _id in chan.selectedKeys:
				if _id < chan.numSegments:
					segment = chan.segments[_id]
					editedSegments.append((chan.name, _id))
					if function not in chan.altFuncs.keys():
						segment.keyInRow[5].val = function
						segment.keyInRow[9].val = ''
						if segment.isLastSegment:
							segment.keyOutRow[5].val = function
							segment.keyOutRow[9].val = ''							
					else:
						segment.keyInRow[5].val = chan.altFuncs[function]
						segment.keyInRow[9].val = function
						if segment.isLastSegment:
							segment.keyOutRow[5].val = chan.altFuncs[function]
							segment.keyOutRow[9].val = function					
		self.SetChannels()
		for chanName, segmentIndex in editedSegments:
			chan = self.Channels[chanName]
			if segmentIndex < chan.numSegments:
				segment = chan.segments[segmentIndex]
				if not segment.isLastSegment:
					nextSegment = chan.segments[segmentIndex + 1]
					if segment.segmentType != nextSegment.segmentType:
						segment.lockHandles = False
				if segment.index > 0:
					prevSegment = chan.segments[segmentIndex - 1]
					if segment.segmentType != prevSegment.segmentType:
						prevSegment.lockHandles = False	
		self.unSelectAll()
		self.setLabelsTy()
		for chanName, _ids in selectedKeys.items():
			chan = self.Channels[chanName]
			for _id in _ids:
				chan.selectKey(_id, 1)
				if chanName == viewKeySegment[0] and _id == viewKeySegment[1]:
					self.updateViewKeySegment = chan.segments[_id]
					self.GetKeyHandlesActive()
					self.KeyframeControlsUpdateView(updateFunction=True)
		self.SetCurStateChannels()

	def ReorderChannels(self, start, end):
		self.SetPrevStateChannels()		
		start += 1
		end += 1
		rowVals = [cell.val for cell in self.channelsDat.row(start)]
		if start < end:
			self.channelsDat.appendRow(rowVals, end)
			self.channelsDat.deleteRow(start)
		elif start > end:
			self.channelsDat.deleteRow(start)
			self.channelsDat.insertRow(rowVals, end)	
		self.unSelectAll()
		self.SetChannels()
		self.updateKeysView(init=True)
		self.SetCurStateChannels(force=True)	

	def convertToKeyframerAnimComp(self, comp):
		try:
			channelsDat = comp.op('channels')
			keysDat = comp.op('keys')
			chans = {}
			for row in channelsDat.rows()[1:]:
				chanName = row[0].val
				chans[chanName] = {}
				chans[chanName]['chan'] = [c.val for c in row]
				chans[chanName]['keys'] = keysDat.rows(row[1].val)
				for i, r in enumerate(chans[chanName]['keys']):
					chans[chanName]['keys'][i] = [c.val for c in r]
					chans[chanName]['keys'][i] += [0, '', 0]

			x = keysDat.nodeX
			y = keysDat.nodeY
			keysDat.destroy()
			keysComp = comp.create(baseCOMP)
			keysComp.name = 'keys'
			keysComp.nodeX = x
			keysComp.nodeY = y - 60
			templateFirstRow = [c.val for c in self.keysTemplateDat.row(0)]
			y = 0
			for i, chan in enumerate(chans.values()):
				keysDat = keysComp.create(tableDAT)
				name = chan['chan'][0]
				keysDat.name = name
				keysDat.nodeY = y				
				keysDat.clear()
				keysDat.appendRow(templateFirstRow)
				keysDat.appendRows(chan['keys'])
				channelsDat[name, 'keys'] = f"keys/{name}"
				y -= 120

			if comp.par.startunit == 'samples':
				comp.par.startunit = 'frames'
				comp.par.start = comp.par.start + 1
			elif comp.par.startunit == 'seconds':
				comp.par.startunit = 'frames'
				comp.par.start = comp.par.start * comp.time.rate + 1
			if comp.par.endunit == 'samples':
				comp.par.endunit = 'frames'
				comp.par.end = comp.par.end + 1
			elif comp.par.endunit == 'seconds':
				comp.par.endunit = 'frames'
				comp.par.end = comp.par.end * comp.time.rate 

			comp.tags = ['KEYFRAMER_ANIM_COMP']
			return comp
		except:
			return

class Channel(Keyframer):
	def __init__(self, owner, name, _id, index, startVal=None):
		super().__init__(owner, owner.ownerComp)		
		self.name = name
		self.id = _id
		self.index = index
		self.handleMinLength = 9
		self.selectedKeys = []
		self.selectedHandles = []
		self.selectedSegments = []	
		self.altFuncs = {'easeadjust()': 'bezier()'}
		self.setFuncs = [self.setKeysXY, self.setHandlesXY, self.setSegmentXY]
		self.selectFuncs = [self.selectKey, self.selectHandle, 
															self.selectSegment]
		self.unSelectFuncs = [self.unSelectKeys, self.unSelectHandles, 
														self.unSelectSegments]
		self.isSelectedFuncs = [self.keyIsSelected, self.handleIsSelected,
								self.segmentIsSelected]
		if not self.ChannelsComp.op(self.name):
			self.channelComp = self.ChannelsComp.copy(self.channelTemplateComp, 
																	name=name)
		else:
			self.channelComp = self.ChannelsComp.op(self.name)
		self.channelComp.nodeX = 0
		self.channelComp.nodeY = -150 * self.id
		self.handlesComp = self.channelComp.op('handles')
		self.handlesChop = self.handlesComp.op('script')
		self.setupHandlesChop()		
		if self.keysComp.op(self.name):
			self.keysDat = self.keysComp.op(self.name)
			self.setupSegments()
		else:
			self.keysDat = self.keysComp.copy(self.keysTemplateDat, 
													name=self.name)
			self.segments = []
			self.insertKey(self.AnimationComp.par.end.eval(), startVal, 
							funcName=self.iParsComp.par.Insertfunction.eval())
			self.keysDat[1,1] = 1
			if startVal is not None:
				self.keysDat[1, 2] = startVal			
		self.keysDat.nodeX = 0
		self.keysDat.nodeY = -100 * self.id
		self.channelComp.par.Keysdat = self.keysDat
		self.channelComp.par.Channelindex = self.index
		self.display = bool(int(self.owner.channelsDat[self.name, 10]))

		self.labelComp = self.channelComp.op('label')
		self.labelTop = self.labelComp.op('label')
		self.labelValuesChop = self.labelComp.op('values')
		self.keysChop = self.channelComp.op('keys/keys')
		self.updateHandlesChopLocked()
			
	@property
	def segmentCompNames(self):
		return self.channelComp.fetch('segmentCompNames', [], storeDefault=True)
	@segmentCompNames.setter
	def segmentCompNames(self, value):
		self.channelComp.storage['segmentCompNames'] = value
	
	@property
	def numSegments(self):
		return len(self.segments)

	@property
	def display(self):
		if self.owner.channelsDat[self.name, 10] is not None:
			return bool(int(self.owner.channelsDat[self.name, 10]))
		return False
	
	@display.setter
	def display(self, value):
		self.owner.channelsDat[self.name, 10] = int(value)
		self.channelComp.par.display = value

	def getState(self):

		state = {
			'keysDatText': self.keysDat.text,
			'selectedHandles': list(self.selectedHandles),
			'selectedKeys': list(self.selectedKeys)
		}
		return state

	def setState(self, state):
		self.keysDat.text = state['keysDatText']
		self.selectedHandles = state['selectedHandles']

	def setName(self, name):
		if self.owner.channelsDat[self.name, 0] is not None:
			self.keysDat.name = name
			self.owner.channelsDat[self.name, 5] = f"keys/{name}"
			self.owner.channelsDat[self.name, 0] = name
		self.name = name
		self.channelComp.name = name

	def setupHandlesChop(self):
		self.handlesChop.clear()
		self.handlesChop.numSamples = 1			
		self.handleX = self.handlesChop.appendChan('x')
		self.handleY = self.handlesChop.appendChan('y')
		self.handleLength = self.handlesChop.appendChan('length')
		self.handleAngle = self.handlesChop.appendChan('angle')
		self.handleDisplay = self.handlesChop.appendChan('display')	
		self.handleSelected = self.handlesChop.appendChan('selected')
		self.handleLocked = self.handlesChop.appendChan('locked')
		self.handleChanIndex = self.handlesChop.appendChan('chanIndex')
		self.handleHandleIndex = self.handlesChop.appendChan('handleIndex')
		self.handleSegmentIndex = self.handlesChop.appendChan('segmentIndex')	
		self.handlesChop.cook(force=True)

	def setHandlesChop(self, segment):
		i = segment.index * 2
		if segment.segmentType in ['bezier()', 'cubic()', 'easeadjust()']:
			self.handleX[i] = segment.x0
			self.handleY[i] = segment.y0
			self.handleDisplay[i] = 1	
			self.handleSelected[i] = 0					
			i += 1	
			self.handleX[i] = segment.x1
			self.handleY[i] = segment.y1
			self.handleDisplay[i] = 1	
			self.handleSelected[i] = 0	
		else:
			self.handleDisplay[i] = 0
			self.handleDisplay[i + 1] = 0
		
		for i in range(self.handlesChop.numSamples):
			self.handleChanIndex[i] = self.index
			self.handleHandleIndex[i] = i
			self.handleSegmentIndex[i] = math.floor(i / 2.0)

	def setHandlesChopHandleLocked(self, segment):
		if segment.index < self.numSegments - 1:
			nextSegment = self.segments[segment.index + 1]
			val = segment.lockHandles
			self.handleLocked[segment.handlesChopOutIndex] = val
			self.handleLocked[nextSegment.handlesChopInIndex] = val	
		else:
			self.handleLocked[segment.handlesChopOutIndex] = 0				

	def destroy(self):
		if self.channelComp:
			self.channelComp.destroy()
		if self.name in self.channelsDat.col(0):
			self.channelsDat.deleteRow(self.name)
		if self.keysDat:
			self.keysDat.destroy()
		self.owner.Channels.pop(self.name)

	def setupSegments(self):
		self.segments = []
		numericCols = self.keysDat.cols(3, 4, 6, 7, 8, 10)
		for col in numericCols:
			for cell in col:
				if cell.val == '':
					if col[0] == 'lockHandles':
						cell.val = 1
					else:
						cell.val = 0
		self.handlesChop.numSamples = (self.keysDat.numRows - 2) * 2
		
		for i, row in enumerate(self.keysDat.rows()[1:-1], start=1):
			index = i - 1
			segmentName = f"segment{index}"
			funcName = row[5].val
			altFuncName = row[9].val
			if altFuncName in self.altFuncs.keys():
				funcName = altFuncName
			isLastSegment = i == self.keysDat.numRows - 2
			segment = self.segmentClasses[funcName](self, 
											segmentName, index, row, 
											self.keysDat.row(i + 1),
											isLastSegment)
			self.segments.append(segment)
			self.setHandlesChop(segment)
	
		self.handlesChop.cook(force=True)

	def updateHandlesChopLocked(self):
		for i, segment in enumerate(self.segments):
			if i < self.numSegments:
				keySelected = int(segment.keyInRow[10].val)
				if keySelected == 1:
					self.selectedKeys.append(i)
			else:
				keySelected = int(segment.keyOutRow[10].val)
				if keySelected == 1:
					self.selectedKeys.append(i + 1)
			self.setHandlesChopHandleLocked(segment)		

	def insertKey(self, x, y=None, funcName=None):
		insertIndex = 0
		replaceSegment = False
		numRows = self.keysDat.numRows
		if numRows > 2:
			x0 = float(self.keysDat[1, 1].val)
			if x == x0:
				replaceSegment = True
			elif x > x0:
				for i, row in enumerate(self.keysDat.rows()[1:-1], start=1):
					x0 = float(row[1].val)
					x1 = float(self.keysDat[i + 1, 1])
					if x == x0:
						replaceSegment = True
						insertIndex = i - 1
						break
					elif x > x0 and x < x1:
						insertIndex = i
						break
				else:
					insertIndex = numRows - 2

		setAltFunc = False
		if funcName in self.altFuncs.keys():
			altFuncName = funcName
			funcName = self.altFuncs[funcName]
			setAltFunc = True
		if insertIndex > 0 and funcName is None:
			insertSegment = self.segments[insertIndex - 1]
			if insertSegment.segmentType in self.altFuncs.keys():
				altFuncName = insertSegment.segmentType
				funcName = self.altFuncs[insertSegment.segmentType]				
				setAltFunc = True		
			
		metadata = [[c.val for c in col] for col in self.keysDat.cols(8, 9, 10)]
		if funcName is not None:
			self.AnimationComp.setKeyframe(x, channel=self.name, 
										value=y, function=funcName)
		else:
			self.AnimationComp.setKeyframe(x, channel=self.name, value=y)			
		insertRowIndex = insertIndex + 1
		if setAltFunc:
			if not replaceSegment:
				metadata[1].insert(insertRowIndex, altFuncName)
			else:
				metadata[1][insertRowIndex] = altFuncName
		else:
			if not replaceSegment:
				metadata[1].insert(insertRowIndex, '')	
			else:
				metadata[1][insertRowIndex] = ''
		if not replaceSegment:
			metadata[0].insert(insertRowIndex, 1)
			metadata[2].insert(insertRowIndex, 0)
		for i in range(3):
			self.keysDat.replaceCol(8 + i, metadata[i])
		self.setupSegments()
		self.updateHandlesChopLocked()
		return insertIndex

	def deleteKey(self, i):
		n = min(self.numSegments - 1, i)
		metadata = [[c.val for c in col] for col in self.keysDat.cols(8, 9, 10)]
		for col in metadata:
			col.pop(n + 1)
		if i == self.numSegments:
			self.AnimationComp.deleteKeyframe(self.segments[i-1].x1,
															channel=self.name)
		else:													
			self.AnimationComp.deleteKeyframe(self.segments[i].x0,
															channel=self.name)
		for j in range(3):
			self.keysDat.replaceCol(8 + j, metadata[j])		
		self.setupSegments()

	def setKeysXY(self, clickId, pos, startOffset, setStart):
		for _id in self.selectedKeys:
			if _id < self.numSegments:
				segment = self.segments[_id]
				x = pos.x + segment.startSetKeyIn.x - startOffset.x
				y = pos.y + segment.startSetKeyIn.y - startOffset.y
				x = round(x)
				segment.setInXY(x, y)
			else:
				segment = self.segments[-1:][0]
				x = pos.x + segment.startSetKeyOut.x - startOffset.x
				y = pos.y + segment.startSetKeyOut.y - startOffset.y				
				x = max(x, segment.x0 + 1)
				x = round(x)
				segment.setOutXY(x, y)		
			
	def setKeysRelXY(self, relPos):
		for i, _id in enumerate(self.selectedKeys):
			if _id < self.numSegments:
				segment = self.segments[_id]
				x = relPos.x + segment.x0
				y = relPos.y + segment.y0
				x = round(x)
				segment.setInXY(x, y)
			else:
				segment = self.segments[-1:][0]
				x = relPos.x + segment.x1
				y = relPos.y + segment.y1				
				x = max(x, segment.x0 + 1)
				x = round(x)
				segment.setOutXY(x, y)
			if i == 0:
				self.keyframeControlsComp.UpdateView('frame', x)
				self.keyframeControlsComp.UpdateView('value', y)	

	def setHandlesXY(self, clickId, pos, startOffset, setStart):
		p_ = ((pos.x, pos.y), (-pos.x, pos.y))

		for _id in self.selectedHandles:
			segmentIndex = math.floor(_id / 2.0)
			segment = self.segments[segmentIndex]
			isOut = _id % 2
			flip = _id % 2 != clickId % 2
			isClicked = _id == clickId
			segment.setHandleXY[isOut](
				*p_[flip],
				setStart,
				updateView=isClicked)

	def setHandlesRelXY(self, relPos):
		for i,_id in enumerate(self.selectedHandles):
			segmentIndex = math.floor(_id / 2.0)		
			segment = self.segments[segmentIndex]
			isOut = _id % 2
			isFirstHandle = i == 0
			if isOut == 0:
				relXY = self.getHandleRelXY(segment.inslope, segment.inaccel)
				x = relPos.x + relXY[0]
				y = relPos.y + relXY[1]
				segment.setInHandleRelXY(
					x, y, updateView=isFirstHandle)	
			else:
				relXY = self.getHandleRelXY(segment.outslope, segment.outaccel)
				x = relPos.x + relXY[0]
				y = relPos.y + relXY[1]
				segment.setOutHandleRelXY(
					x, y, updateView=isFirstHandle)	
												
	def setSegmentXY(self, _id, pos, startOffset, setStart):
		self.setKeysXY(_id, pos, startOffset, setStart)

	def selectKey(self, _id, state):
		if _id < self.numSegments:
			segment = self.segments[_id]
			segment.keyInRow[10].val = state
		else:
			segment = self.segments[_id - 1]
			segment.keyOutRow[10].val = state		
		
		if state == 1 and _id not in self.selectedKeys:
			self.selectedKeys.append(_id)

		elif state == 0 and _id in self.selectedKeys:
			self.selectedKeys.pop(self.selectedKeys.index(_id))

	def setStartSetKeys(self):
		for _id in self.selectedKeys:
			if _id < self.numSegments:
				segment = self.segments[_id]
				segment.setStartSetKeyIn()
				segment.setStartSetKeyOut()
			else:
				segment = self.segments[_id - 1]
				segment.setStartSetKeyOut()

	def selectHandles(self, selectedHandles):
		self.selectedHandles = selectedHandles
		for _id in self.selectedHandles:
			self.selectHandle(_id, 1)
		self.handlesChop.cook(force=True)

	def selectHandle(self, _id, state):
		self.handleSelected[_id] = state

		if state == 1 and _id not in self.selectedHandles:
			self.selectedHandles.append(_id)
		elif state == 0 and _id in self.selectedHandles:
			self.selectedHandles.pop(self.selectedHandles.index(_id))

	def displayHandles(self):
		for i, _id in enumerate(self.selectedHandles):
			isOut = _id % 2
			segmentIndex = math.floor(_id / 2.0)
			segment = self.segments[segmentIndex]
			if (isOut and segmentIndex < self.numSegments - 1 
					and segment.lockHandles and self.handleSelected[_id + 1]):
				self.handleSelected[_id] = 0
				self.selectedHandles.pop(i)

	def selectSegment(self, x, state):
		selected = None
		for segment in self.segments:
			if segment.x0 <= x < segment.x1:
				selected = segment
				break
		else:
			return
		self.selectKey(segment.index, state)
		self.selectKey(segment.index + 1, state)
		if state == 1 and segment.index not in self.selectedSegments:
			self.selectedSegments.append(segment.index)
		elif state == 0 and segment.index in self.selectedSegments:
			self.selectedSegments.pop(self.selectedSegments.index(segment.index))		
			self.selectedKeys.pop(self.selectedKeys.index(segment.index))
		return selected
			
	def unSelectAll(self):
		self.selectedKeys = []
		self.selectedHandles = []
		self.selectedSegments = []		
		for cell in self.keysDat.col('selected')[1:]:
			cell.val = 0
		for i in range(self.handlesChop.numSamples):
			self.handleSelected[i] = 0.0

	def unSelectKeys(self, exclude):
		self.selectedKeys = []
		for i, cell in enumerate(self.keysDat.col('selected')[1:]):
			if i not in exclude:
				cell.val = 0

	def unSelectHandles(self, exclude):
		self.selectedHandles = []
		for i in range(self.handlesChop.numSamples):
			self.handleSelected[i] = 0.0	
		pass

	def unSelectSegments(self, exclude):
		self.selectedSegments = []	
		self.unSelectKeys(exclude)	
		pass

	def keyIsSelected(self, _id):
		if _id in self.selectedKeys:
			return True
		return False
		pass

	def handleIsSelected(self, _id):
		if _id in self.selectedHandles:
			return True
		return False

	def segmentIsSelected(self, x):
		for segment in self.segments:
			if segment.x0 <= x < segment.x1 \
					and segment.index in self.selectedSegments:
				return True
				break
		else:
			return False

	def toggleSelectedLockHandles(self):
		segments = []
		for _id in self.selectedKeys:
			if _id != 0:
				segments.append(self.segments[_id - 1])
		for _id in self.selectedSegments:
			if _id != 0:
				segment = self.segments[_id - 1]
				if segment not in segments:
					segments.append(segment)

		for _id in self.selectedHandles:
			if _id != 0:
				segmentIndex = math.floor(_id / 2.0) - 1
				isOutHandle = _id % 2
				segment = self.segments[segmentIndex + isOutHandle]
				if segment not in segments:
					segments.append(segment)
		for segment in segments:
			val = not segment.lockHandles
			segment.lockHandles = val


class Segment(Keyframer):
	def __init__(self, owner, name, index, 
				keyInRow, keyOutRow, isLastSegment):
		super().__init__(owner, owner.ownerComp)
		self.handlesChop = owner.handlesChop
		self.chanId = owner.id
		self.name = name
		self.index = index
		self.handlesChopInIndex = index * 2
		self.handlesChopOutIndex = self.handlesChopInIndex + 1
		self.handlesChopLength = self.handlesChop['length']
		self.handlesChopAngle = self.handlesChop['angle']	
		self.handlesChopX = self.handlesChop['x']
		self.handlesChopY = self.handlesChop['y']
		self.handlesChopSelected = self.handlesChop['selected']	
		self.handlesChopLocked = self.handlesChop['locked']
		self.handleMinLength = 0 # 16 
		self.hasHandles = False
		if self.index == 0:
			self.prevSegment = None
		else:
			self.prevSegment = self.owner.segments[index - 1]
		self.isLastSegment = isLastSegment
		self.keyInRow = keyInRow
		self.keyOutRow = keyOutRow
		self.setHandleXY = [self.setInHandleXY, self.setOutHandleXY]
		self.startSetKeyIn = tdu.Position(self.x0, self.y0, 0.0)
		self.startSetKeyOut = tdu.Position(self.x1, self.y1, 0.0)
		self.scaleDeltas = [[0,0], [0,0], [0,0], [0,0]]		

	@property
	def x0(self): return float(self.keyInRow[1].val)
	@x0.setter
	def x0(self, value): self.keyInRow[1].val = value

	@property
	def y0(self): return float(self.keyInRow[2].val)
	@y0.setter
	def y0(self, value): self.keyInRow[2].val = value

	@property
	def x1(self): return float(self.keyOutRow[1].val)
	@x1.setter
	def x1(self, value): self.keyOutRow[1].val = value

	@property
	def y1(self): return float(self.keyOutRow[2].val)
	@y1.setter
	def y1(self, value): self.keyOutRow[2].val = value	

	@property
	def inslope(self): return  float(self.keyInRow[3].val)
	@inslope.setter
	def inslope(self, value): self.keyInRow[3].val = value

	@property
	def inaccel(self): return  float(self.keyInRow[4].val)
	@inaccel.setter
	def inaccel(self, value): self.keyInRow[4].val = value

	@property
	def outslope(self):
		if self.isLastSegment:
			return  float(self.keyOutRow[3].val)
		else:
			return  float(self.keyOutRow[6].val)
	@outslope.setter
	def outslope(self, value):
		if self.isLastSegment:
			self.keyOutRow[3].val = value	
		else:
			self.keyOutRow[6].val = value

	@property
	def outaccel(self): 
		if self.isLastSegment:
			return float(self.keyOutRow[4].val)
		else:
			return float(self.keyOutRow[7].val)
	@outaccel.setter
	def outaccel(self, value):
		if self.isLastSegment:
			self.keyOutRow[4].val = value
		else:
			self.keyOutRow[7].val = value

	@property
	def inHandleAngle(self):
		return math.degrees(math.atan2(self.inslope, 1.0))

	@property
	def outHandleAngle(self):
		return math.degrees(math.atan2(self.outslope, 1.0)) + 180

	@property
	def lockHandles(self): return bool(int(self.keyInRow[8].val))
	@lockHandles.setter
	def lockHandles(self, value): 
		self.keyInRow[8].val = int(value)
		self.handlesChopLocked[self.handlesChopOutIndex] = value
		if self.index < self.owner.numSegments - 1:
			nextSeg = self.owner.segments[self.index + 1]
			self.handlesChopLocked[nextSeg.handlesChopInIndex] = value

	def destroy(self):
		pass

	def initView(self):
		pass

	def setStartSetKeyIn(self):
		self.startSetKeyIn.x = self.x0
		self.startSetKeyIn.y = self.y0

	def setStartSetKeyOut(self):
		self.startSetKeyOut.x = self.x1
		self.startSetKeyOut.y = self.y1	

	def setInHandleXY(self, x, y, setStart, updateView=False):
		pass
	
	def setOutHandleXY(self, x, y, setStart, updateView=False):
		pass

	def onPrevOutHandleValueChange(self, prevSegment, updateView=False):
		pass

	def onNextInHandleValueChange(self, nextSegment, updateView=False):
		pass


class Constant(Segment):
	def __init__(self, owner, name, index, 
				keyInRow, keyOutRow, isLastSegment):
		self.segmentType = 'constant()'		
		super().__init__(owner, name, index, 
				keyInRow, keyOutRow, isLastSegment)
		self.initView()

	def initView(self):
		self.updateView()
	
	def updateView(self):	
		if self.index == 0:
			self.handlesChopX[self.handlesChopInIndex] = self.x0
			self.handlesChopY[self.handlesChopInIndex] = self.y0
		if self.isLastSegment:
			self.handlesChopX[self.handlesChopOutIndex] = self.x1
			self.handlesChopY[self.handlesChopOutIndex] = self.y1

	def setInXY(self, x, y):
		x = min(x, self.x1 - 1)
		if self.prevSegment:
			x = max(x, self.prevSegment.x0 + 1)
			self.prevSegment.setOutXY(x, y)
		self.x0 = x
		self.y0 = y
		self.updateView()
		
	def setOutXY(self, x, y):
		x = max(x, self.x0 + 1)
		if self.isLastSegment:
			self.y0 = y
			if self.prevSegment:
				
				self.prevSegment.setOutXY(self.x0, self.y0)
		self.x1 = x
		self.y1 = y
		self.updateView()	


class Linear(Segment):
	def __init__(self, owner, name, index, 
				keyInRow, keyOutRow, isLastSegment):
		self.segmentType = 'linear()'		
		super().__init__(owner, name, index, 
				keyInRow, keyOutRow, isLastSegment)
		self.initView()

	def initView(self):
		if self.index == 0:
			self.handlesChopX[self.handlesChopInIndex] = self.x0
			self.handlesChopY[self.handlesChopInIndex] = self.y0
		if self.isLastSegment:
			self.handlesChopX[self.handlesChopOutIndex] = self.x1
			self.handlesChopY[self.handlesChopOutIndex] = self.y1

	def setInXY(self, x, y):
		x = min(x, self.x1 - 1)
		if self.prevSegment:
			x = max(x, self.prevSegment.x0 + 1)
			self.prevSegment.setOutXY(x, y)
		self.x0 = x
		self.y0 = y
		if self.index == 0:
			self.handlesChopX[self.handlesChopInIndex] = x
			self.handlesChopY[self.handlesChopInIndex] = y

	def setOutXY(self, x, y):
		x = max(x, self.x0 + 1)
		self.x1 = x
		self.y1 = y
		if self.isLastSegment:
			self.handlesChopX[self.handlesChopOutIndex] = x
			self.handlesChopY[self.handlesChopOutIndex] = y	


class EaseBase(Segment):
	def __init__(self, owner, name, index, 
				keyInRow, keyOutRow, isLastSegment):	
		super().__init__(owner, name, index, 
				keyInRow, keyOutRow, isLastSegment)
		self.initView()
	
	def easeFunc(self, p):
		if (p < 0.5):
			return 2 * p * p
		return (-2 * p * p) + (4 * p) - 1

	def initView(self):
		self.updateView()
	
	def updateView(self):
		xScale = self.x1 - self.x0
		yScale = self.y1 - self.y0
		if self.index == 0:
			self.handlesChopX[self.handlesChopInIndex] = self.x0
			self.handlesChopY[self.handlesChopInIndex] = self.y0
		if self.isLastSegment:
			self.handlesChopX[self.handlesChopOutIndex] = self.x1
			self.handlesChopY[self.handlesChopOutIndex] = self.y1	

	def setInXY(self, x, y):
		x = min(x, self.x1 - 1)
		if self.prevSegment:
			x = max(x, self.prevSegment.x0 + 1)
			self.prevSegment.setOutXY(x, y)
		self.x0 = x
		self.y0 = y
		self.updateView()
		
	def setOutXY(self, x, y):
		x = max(x, self.x0 + 1)
		self.x1 = x
		self.y1 = y
		self.updateView()	


class Ease(EaseBase):
	def __init__(self, owner, name, index, 
				keyInRow, keyOutRow, isLastSegment):
		self.segmentType = 'ease()'		
		super().__init__(owner, name, index, 
				keyInRow, keyOutRow, isLastSegment)


class EaseIn(EaseBase):
	def __init__(self, owner, name, index, 
				keyInRow, keyOutRow, isLastSegment):
		self.segmentType = 'easein()'		
		super().__init__(owner, name, index, 
				keyInRow, keyOutRow, isLastSegment)

	# Modeled after the parabola y = x^2
	def easeFunc(self, p):
		return p * p


class EaseOut(EaseBase):
	def __init__(self, owner, name, index, 
				keyInRow, keyOutRow, isLastSegment):
		self.segmentType = 'easeout()'		
		super().__init__(owner, name, index, 
				keyInRow, keyOutRow, isLastSegment)

	# Modeled after the parabola y = -x^2 + 2x
	def easeFunc(self, p):
		return -(p * (p - 2))


class EaseP(EaseBase):
	def __init__(self, owner, name, index, 
				keyInRow, keyOutRow, isLastSegment):
		self.segmentType = 'easep(2)'		
		super().__init__(owner, name, index, 
				keyInRow, keyOutRow, isLastSegment)

	# Modeled after the piecewise quadratic
	# with p^2 on input
	def easeFunc(self, p):
		p *= p
		if (p < 0.5):
			return 2 * p * p
		return (-2 * p * p) + (4 * p) - 1


class EaseInP(EaseBase):
	def __init__(self, owner, name, index, 
				keyInRow, keyOutRow, isLastSegment):
		self.segmentType = 'easeinp(2)'		
		super().__init__(owner, name, index, 
				keyInRow, keyOutRow, isLastSegment)

	# Modeled after the cubic y = x^3
	def easeFunc(self, p):
		return p * p * p


class EaseOutP(EaseBase):
	def __init__(self, owner, name, index, 
				keyInRow, keyOutRow, isLastSegment):
		self.segmentType = 'easeoutp(2)'		
		super().__init__(owner, name, index, 
				keyInRow, keyOutRow, isLastSegment)

	# Modeled after the cubic y = (x - 1)^3 + 1
	def easeFunc(self, p):
		f = (p - 1)
		return f * f * f + 1


class BezierBase(Segment):
	def __init__(self, owner, name, index, 
			keyInRow, keyOutRow, isLastSegment):
		super().__init__(owner, name, index, 
			keyInRow, keyOutRow, isLastSegment)
		self.hasHandles = True
		self.getSlopeAccelFromRelXY = (self.getInSlopeAccelFromRelXY,
									self.getOutSlopeAccelFromRelXY)
		self.setSlopeAccel = (self.setInSlopeAccel,
									self.setOutSlopeAccel)
		self.setRelSlopeAccel = (self.setInRelSlopeAccel,
									self.setOutRelSlopeAccel)

	@property
	def inHandleRelXY(self):
		return self.getHandleRelXY(self.inslope, self.inaccel)

	@property
	def outHandleRelXY(self):
		return self.getHandleRelXY(self.outslope, self.outaccel)

	@property
	def inHandlePos(self):
		relXY = self.inHandleRelXY
		x = relXY[0] + self.x0
		y = relXY[1] + self.y0
		return (x, y)

	@property
	def outHandlePos(self):
		relXY = self.outHandleRelXY
		x = self.x1 - relXY[0]
		y = self.y1 - relXY[1]
		return (x, y)	

	def initView(self):
		self.updateView()
		pass

	def getHandleRelXY(self, slope, radius):
		s = 1 if slope >= 0 else -1
		if slope != 0.0 and radius != 0.0:
			x = radius / math.sqrt(slope * slope + 1)
			slope = 1.0 / slope
			y = radius / (s * math.sqrt(slope * slope + 1))
		elif radius == 0.0 and slope != 0.0:
			x = 0
			y = 0
		else:
			x = radius
			y = 0.0
		return x, y

	def updateView(self):
		slope = self.inslope
		accel = self.inaccel
		deltaX = self.x1 - self.x0
		hyp = slope * (deltaX)
		maxAccel = math.sqrt(pow(hyp, 2) + pow(deltaX, 2))
		accel = min(maxAccel, max(0.0, accel))
		angle = math.degrees(math.atan2(slope, 1.0))
		relX, relY = self.getHandleRelXY(slope, accel)
		length = math.sqrt(math.pow(relX, 2) + math.pow(relY, 2))
		self.handlesChopX[self.handlesChopInIndex] = self.x0
		self.handlesChopY[self.handlesChopInIndex] = self.y0
		self.handlesChopLength[self.handlesChopInIndex] = max(min(length, 
										self.inaccel), self.handleMinLength)
		self.handlesChopAngle[self.handlesChopInIndex] = self.inHandleAngle

		slope = self.outslope
		accel = self.outaccel
		hyp = slope * (deltaX)
		maxAccel = math.sqrt(pow(hyp, 2) + pow(deltaX, 2))
		accel = min(maxAccel, max(0.0, accel))
		angle = math.degrees(math.atan2(slope, 1.0))
		relX, relY = self.getHandleRelXY(slope, accel)
		length = math.sqrt(math.pow(relX, 2) + math.pow(relY, 2))	
		self.handlesChopX[self.handlesChopOutIndex] = self.x1
		self.handlesChopY[self.handlesChopOutIndex] = self.y1			
		self.handlesChopLength[self.handlesChopOutIndex] = max(min(length, 
										self.outaccel), self.handleMinLength)		
		self.handlesChopAngle[self.handlesChopOutIndex] = self.outHandleAngle	

	def setInXY(self, x, y):
		x = min(x, self.x1 - 1)
		if self.prevSegment:
			x = max(x, self.prevSegment.x0 + 1)
			self.prevSegment.setOutXY(x, y)
		self.x0 = x
		self.y0 = y
		self.updateView()
		
	def setOutXY(self, x, y):
		x = max(x, self.x0 + 1)
		self.x1 = x
		self.y1 = y
		self.updateView()	

	def getInSlopeAccelFromRelXY(self, relX, relY):
		relX = max(1, min(relX, self.x1 - self.x0))
		slope = relY / relX
		length = math.sqrt(math.pow(relX, 2) + math.pow(relY, 2))
		return slope, length

	def getOutSlopeAccelFromRelXY(self, relX, relY):
		relX = min(-1, max(relX, self.x0 - self.x1))
		slope = relY / relX
		length = math.sqrt(math.pow(relX, 2) + math.pow(relY, 2))
		return slope, length

	def setInHandleRelXY(self, x, y, updateView=False):
		relX = max(1, min(x, self.x1 - self.x0))
		relY = y

		slope = relY / relX
		length = math.sqrt(math.pow(relX, 2) + math.pow(relY, 2))
		angle = math.degrees(math.atan2(slope, 1.0))

		self.inaccel = length
		self.inslope = slope
		if updateView:
			self.keyframeControlsComp.UpdateView('inaccel', length)
			self.keyframeControlsComp.UpdateView('inslope', slope)
		self.handlesChopLength[self.handlesChopInIndex] = max(length,
														self.handleMinLength)
		self.handlesChopAngle[self.handlesChopInIndex] = angle

		if self.prevSegment is not None:
			self.prevSegment.onNextInHandleValueChange(self, updateView)

	def setOutHandleRelXY(self, x, y, updateView=False):
		relX = min(-1, max(x, self.x0 - self.x1))
		relY = y

		slope = relY / relX
		length = math.sqrt(math.pow(relX, 2) + math.pow(relY, 2))
		angle = math.degrees(math.atan2(slope, 1.0)) + 180
		self.outaccel = length
		self.outslope = slope
		if updateView:
			self.keyframeControlsComp.UpdateView('outaccel', length)
			self.keyframeControlsComp.UpdateView('outslope', slope)		
		self.handlesChopLength[self.handlesChopOutIndex] = max(length,
														self.handleMinLength)
		self.handlesChopAngle[self.handlesChopOutIndex] = angle
		if not self.isLastSegment:
			nextSegment = self.owner.segments[self.index + 1]
			nextSegment.onPrevOutHandleValueChange(self, updateView)

	def setInHandleXY(self, x, y, setStart, updateView=False):
		if setStart:
			relXY = self.getHandleRelXY(self.inslope, self.inaccel)	
			self.inHandleStartX = relXY[0]
			self.inHandleStartY = relXY[1]				
			self.inHandleOffsetX = x
			self.inHandleOffsetY = y
	
		x -= self.inHandleOffsetX
		y -= self.inHandleOffsetY
		x += self.inHandleStartX
		y += self.inHandleStartY
		self.setInHandleRelXY(x, y, updateView)

	def setOutHandleXY(self, x, y, setStart, updateView=False):
		if setStart:
			relXY = self.getHandleRelXY(self.outslope, -self.outaccel)
			self.outHandleStartX = relXY[0]
			self.outHandleStartY = relXY[1]				
			self.outHandleOffsetX = x
			self.outHandleOffsetY = y
	
		x -= self.outHandleOffsetX
		y -= self.outHandleOffsetY
		x += self.outHandleStartX
		y += self.outHandleStartY
		self.setOutHandleRelXY(x, y, updateView)

	def onPrevOutHandleValueChange(self, prevSegment, updateView=False):
		if prevSegment.lockHandles:
			self.inslope = prevSegment.outslope
			self.inaccel = prevSegment.outaccel
			self.updateView()
		if (updateView 
				and self.owner.handleSelected[self.handlesChopInIndex] == 1):
			self.keyframeControlsComp.UpdateView(
				'inslope', self.inslope
			)							
			self.keyframeControlsComp.UpdateView(
				'inaccel', self.inaccel
			)	

	def onNextInHandleValueChange(self, nextSegment, updateView=False):
		if self.lockHandles:		
			self.outslope = nextSegment.inslope
			self.outaccel = nextSegment.inaccel
			self.updateView()	
		if (updateView 
				and self.owner.handleSelected[self.handlesChopOutIndex] == 1):
			self.keyframeControlsComp.UpdateView(
				'outslope', self.outslope
			)						
			self.keyframeControlsComp.UpdateView(
				'outaccel', self.outaccel
			)

	def setInRelSlopeAccel(self, slope, accel, setStart):
		if setStart:
			self.inOffsetSlope = self.inslope
			self.inOffsetAccel = self.inaccel
		slope += self.inOffsetSlope
		accel += self.inOffsetAccel
		slope = min(.999999, slope)	
		deltaX = self.x1 - self.x0
		hyp = slope * (deltaX)
		maxAccel = math.sqrt(pow(hyp, 2) + pow(deltaX, 2))
		accel = min(maxAccel, max(0.0, accel))
		angle = math.degrees(math.atan2(slope, 1.0))
		x, y = self.getHandleRelXY(slope, accel)
		x += self.x0
		y += self.y0
		self.inslope = slope
		self.inaccel = accel
		self.keyframeControlsComp.UpdateView('inaccel', accel)
		self.keyframeControlsComp.UpdateView('inslope', slope)
		self.handlesChopLength[self.handlesChopInIndex] = max(accel,
														self.handleMinLength)
		self.handlesChopAngle[self.handlesChopInIndex] = angle
		if self.prevSegment is not None:
			if self.prevSegment.lockHandles:
				self.prevSegment.onNextInHandleValueChange(self, False)

	def setOutRelSlopeAccel(self, slope, accel, setStart):
		if setStart:
			self.outOffsetSlope = self.outslope
			self.outOffsetAccel = self.outaccel	
		slope += self.outOffsetSlope
		accel += self.outOffsetAccel	
		slope = min(.999999, slope)	
		deltaX = self.x1 - self.x0
		hyp = slope * (deltaX)
		maxAccel = math.sqrt(pow(hyp, 2) + pow(deltaX, 2))
		accel = min(maxAccel, max(0.0, accel))
		angle = math.degrees(math.atan2(slope, 1.0)) + 180
		x, y = self.getHandleRelXY(slope, accel)
		x = self.x1 - x
		y = self.y1	- y	
		self.outslope = slope
		self.outaccel = accel
		self.keyframeControlsComp.UpdateView('outaccel', accel)
		self.keyframeControlsComp.UpdateView('outslope', slope)		
		self.handlesChopLength[self.handlesChopOutIndex] = max(accel,
														self.handleMinLength)
		self.handlesChopAngle[self.handlesChopOutIndex] = angle
		if not self.isLastSegment and self.lockHandles:
			nextSegment = self.owner.segments[self.index + 1]
			nextSegment.onPrevOutHandleValueChange(self, False)	

	def setInSlopeAccel(self, slope=None, accel=None):
		if slope is None:
			slope = self.inslope
		if accel is None:
			accel = self.inaccel
		deltaX = self.x1 - self.x0
		hyp = slope * (deltaX)
		maxAccel = math.sqrt(pow(hyp, 2) + pow(deltaX, 2))
		accel = min(maxAccel, max(0.0, accel))
		angle = math.degrees(math.atan2(slope, 1.0))
		x, y = self.getHandleRelXY(slope, accel)
		x += self.x0
		y += self.y0
		self.inslope = slope
		self.inaccel = accel
		self.keyframeControlsComp.UpdateView('inaccel', accel)
		self.keyframeControlsComp.UpdateView('inslope', slope)
		self.handlesChopLength[self.handlesChopInIndex] = max(accel,
														self.handleMinLength)
		self.handlesChopAngle[self.handlesChopInIndex] = angle
		if self.prevSegment is not None:
			if self.prevSegment.lockHandles:
				self.prevSegment.onNextInHandleValueChange(self, True)

	def setOutSlopeAccel(self, slope=None, accel=None):
		if slope is None:
			slope = self.outslope
		if accel is None:
			accel = self.outaccel		
		angle = math.degrees(math.atan2(slope, 1.0)) + 180
		deltaX = self.x1 - self.x0
		hyp = slope * (deltaX)
		maxAccel = math.sqrt(pow(hyp, 2) + pow(deltaX, 2))
		accel = min(maxAccel, max(0.0, accel))		
		x, y = self.getHandleRelXY(slope, accel)
		x = self.x1 - x
		y = self.y1	- y	
		self.outslope = slope
		self.outaccel = accel
		self.keyframeControlsComp.UpdateView('outaccel', accel)
		self.keyframeControlsComp.UpdateView('outslope', slope)		
		self.handlesChopLength[self.handlesChopOutIndex] = max(accel,
														self.handleMinLength)
		self.handlesChopAngle[self.handlesChopOutIndex] = angle
		if not self.isLastSegment and self.lockHandles:
			nextSegment = self.owner.segments[self.index + 1]
			nextSegment.onPrevOutHandleValueChange(self, True)		


class Bezier(BezierBase):
	def __init__(self, owner, name, index, 
				keyInRow, keyOutRow, isLastSegment):
		self.segmentType = 'bezier()'		
		super().__init__(owner, name, index, 
				keyInRow, keyOutRow, isLastSegment)
		self.initView()


class Cubic(BezierBase):
	def __init__(self, owner, name, index, 
				keyInRow, keyOutRow, isLastSegment):
		self.segmentType = 'cubic()'						
		super().__init__(owner, name, index, 
				keyInRow, keyOutRow, isLastSegment)
		self.initView()
	
	@property
	def inHandleRelXY(self):
		deltaX = self.x1 - self.x0
		x = deltaX * .333333333333
		y = x * self.inslope
		return x, y

	@property
	def outHandleRelXY(self):
		deltaX = self.x1 - self.x0
		x = deltaX * .333333333333
		y = x * self.outslope
		return x, y

	@property
	def inHandlePos(self):
		length = self.handlesChopLength[self.handlesChopInIndex]
		relXY = self.getHandleRelXY(self.inslope, length)
		x = relXY[0] + self.x0
		y = relXY[1] + self.y0
		return (x, y)

	@property
	def outHandlePos(self):
		length = self.handlesChopLength[self.handlesChopOutIndex]
		relXY = self.getHandleRelXY(self.outslope, length)
		x = self.x1 - relXY[0]
		y = self.y1 - relXY[1]
		return (x, y)	

	def updateView(self):
		inHandle = self.inHandleRelXY
		outHandle = self.outHandleRelXY
		self.handlesChopX[self.handlesChopInIndex] = self.x0
		self.handlesChopY[self.handlesChopInIndex] = self.y0
		self.handlesChopX[self.handlesChopOutIndex] = self.x1
		self.handlesChopY[self.handlesChopOutIndex] = self.y1

		self.handlesChopLength[self.handlesChopInIndex] = max(inHandle[0],
														self.handleMinLength)
		self.handlesChopAngle[self.handlesChopInIndex] = self.inHandleAngle
		self.handlesChopLength[self.handlesChopOutIndex] = max(outHandle[0],
														self.handleMinLength)
		self.handlesChopAngle[self.handlesChopOutIndex] = self.outHandleAngle

	def getInSlopeAccelFromRelXY(self, relX, relY):
		relX = max(1, min(relX, self.x1 - self.x0))
		slope = relY / relX
		deltaX = self.x1 - self.x0
		length = deltaX * .333333333333
		return slope, length

	def getOutSlopeAccelFromRelXY(self, relX, relY):
		relX = min(-1, min(relX, self.x1 - self.x0))
		slope = relY / relX
		deltaX = self.x1 - self.x0
		length = deltaX * .333333333333
		return slope, length

	def setInHandleRelXY(self, x, y, updateView=False):
		relX = max(0.000000000001, min(x, self.x1 - self.x0))
		relY = y
		slope = relY / relX
		deltaX = self.x1 - self.x0
		length = deltaX * .333333333333
		angle = math.degrees(math.atan2(slope, 1.0))

		self.inaccel = length
		self.inslope = slope
		if updateView:
			self.keyframeControlsComp.UpdateView('inaccel', length)
			self.keyframeControlsComp.UpdateView('inslope', slope)
		self.handlesChopLength[self.handlesChopInIndex] = max(length,
														self.handleMinLength)
		self.handlesChopAngle[self.handlesChopInIndex] = angle
		if self.prevSegment is not None:
			self.prevSegment.onNextInHandleValueChange(self, updateView)

	def setOutHandleRelXY(self, x, y, updateView=False):
		relX = min(-0.000000000001, max(x, self.x0 - self.x1))
		relY = y

		slope = relY / relX
		deltaX = self.x1 - self.x0
		length = deltaX * .333333333333
		angle = math.degrees(math.atan2(slope, 1.0)) + 180
		self.outaccel = length
		self.outslope = slope
		if updateView:
			self.keyframeControlsComp.UpdateView('outaccel', length)
			self.keyframeControlsComp.UpdateView('outslope', slope)		
		self.handlesChopLength[self.handlesChopOutIndex] = max(length,
														self.handleMinLength)
		self.handlesChopAngle[self.handlesChopOutIndex] = angle
		if not self.isLastSegment:
			nextSegment = self.owner.segments[self.index + 1]
			nextSegment.onPrevOutHandleValueChange(self, updateView)

	def onPrevOutHandleValueChange(self, prevSegment, updateView=False):
		if prevSegment.lockHandles:		
			self.inslope = prevSegment.outslope
			self.updateView()
		if (updateView 
				and self.owner.handleSelected[self.handlesChopInIndex] == 1):
			self.keyframeControlsComp.UpdateView(
				'inslope', self.inslope
			)							
			self.keyframeControlsComp.UpdateView(
				'inaccel', self.inaccel
			)	

	def onNextInHandleValueChange(self, nextSegment, updateView=False):
		if self.lockHandles:		
			self.outslope = nextSegment.inslope
			self.updateView()	
		if (updateView 
				and self.owner.handleSelected[self.handlesChopOutIndex] == 1):
			self.keyframeControlsComp.UpdateView(
				'outslope', self.outslope
			)						
			self.keyframeControlsComp.UpdateView(
				'outaccel', self.outaccel
			)

	def setInRelSlopeAccel(self, slope, accel, setStart):
		if setStart:
			self.inOffsetSlope = self.inslope
		slope += self.inOffsetSlope
		deltaX = self.x1 - self.x0
		accel = deltaX * .333333333333
		slope = min(.999999, slope)	
		accel = max(0.0, accel)
		angle = math.degrees(math.atan2(slope, 1.0))
		x, y = self.getHandleRelXY(slope, accel)
		x += self.x0
		y += self.y0
		self.inslope = slope
		self.inaccel = accel
		self.keyframeControlsComp.UpdateView('inaccel', accel)
		self.keyframeControlsComp.UpdateView('inslope', slope)
		self.handlesChopLength[self.handlesChopInIndex] = max(accel,
														self.handleMinLength)
		self.handlesChopAngle[self.handlesChopInIndex] = angle
		if self.prevSegment is not None:
			if self.prevSegment.lockHandles:
				self.prevSegment.onNextInHandleValueChange(self, False)

	def setOutRelSlopeAccel(self, slope, accel, setStart):
		if setStart:
			self.outOffsetSlope = self.outslope
		slope += self.outOffsetSlope
		deltaX = self.x1 - self.x0
		accel = deltaX * .333333333333
		slope = min(.999999, slope)	
		accel = max(0.0, accel)
		angle = math.degrees(math.atan2(slope, 1.0)) + 180
		x, y = self.getHandleRelXY(slope, accel)
		x = self.x1 - x
		y = self.y1	- y	
		self.outslope = slope
		self.outaccel = accel
		self.keyframeControlsComp.UpdateView('outaccel', accel)
		self.keyframeControlsComp.UpdateView('outslope', slope)		
		self.handlesChopLength[self.handlesChopOutIndex] = max(accel,
														self.handleMinLength)
		self.handlesChopAngle[self.handlesChopOutIndex] = angle
		if not self.isLastSegment and self.lockHandles:
			nextSegment = self.owner.segments[self.index + 1]
			nextSegment.onPrevOutHandleValueChange(self, False)	

	def setInSlopeAccel(self, slope=None, accel=None):
		if slope is None:
			slope = self.inslope
		accel = self.inaccel
		angle = math.degrees(math.atan2(slope, 1.0))
		x, y = self.getHandleRelXY(slope, accel)
		x += self.x0
		y += self.y0
		self.inslope = slope
		self.inaccel = accel
		self.keyframeControlsComp.UpdateView('inaccel', accel)
		self.keyframeControlsComp.UpdateView('inslope', slope)
		self.handlesChopLength[self.handlesChopInIndex] = max(accel,
														self.handleMinLength)
		self.handlesChopAngle[self.handlesChopInIndex] = angle
		if self.prevSegment is not None:
			if self.prevSegment.lockHandles:
				self.prevSegment.onNextInHandleValueChange(self, True)

	def setOutSlopeAccel(self, slope=None, accel=None):
		if slope is None:
			slope = self.outslope
		accel = self.outaccel		
		angle = math.degrees(math.atan2(slope, 1.0)) + 180
		x, y = self.getHandleRelXY(slope, accel)
		x = self.x1 - x
		y = self.y1	- y	
		self.outslope = slope
		self.outaccel = accel
		self.keyframeControlsComp.UpdateView('outaccel', accel)
		self.keyframeControlsComp.UpdateView('outslope', slope)		
		self.handlesChopLength[self.handlesChopOutIndex] = max(accel,
														self.handleMinLength)
		self.handlesChopAngle[self.handlesChopOutIndex] = angle
		if not self.isLastSegment and self.lockHandles:
			nextSegment = self.owner.segments[self.index + 1]
			nextSegment.onPrevOutHandleValueChange(self, True)	


class EaseAdjust(BezierBase):
	def __init__(self, owner, name, index, 
				keyInRow, keyOutRow, isLastSegment):
		self.segmentType = 'easeadjust()'	
		super().__init__(owner, name, index, 
				keyInRow, keyOutRow, isLastSegment)			
		self.inslope = 0.0
		self.outslope = 0.0
		self.initView()

	def setInHandleRelXY(self, x, y, updateView=False):
		relX = max(0.000000000001, min(x, self.x1 - self.x0))
		slope = 0.0
		length = abs(relX)
		angle = 0.0
		self.inaccel = length
		self.inslope = slope
		if updateView:
			self.keyframeControlsComp.UpdateView('inaccel', length)
			self.keyframeControlsComp.UpdateView('inslope', slope)
		self.handlesChopLength[self.handlesChopInIndex] = max(length,
														self.handleMinLength)
		self.handlesChopAngle[self.handlesChopInIndex] = angle
		if self.prevSegment is not None:
			self.prevSegment.onNextInHandleValueChange(self, updateView)

	def setOutHandleRelXY(self, x, y, updateView=False):
		relX = min(-0.000000000001, max(x, self.x0 - self.x1))
		slope = 0.0
		length = abs(relX)
		angle = 180
		self.outaccel = length
		self.outslope = slope
		if updateView:
			self.keyframeControlsComp.UpdateView('outaccel', length)
			self.keyframeControlsComp.UpdateView('outslope', slope)		
		self.handlesChopLength[self.handlesChopOutIndex] = max(length,
														self.handleMinLength)
		self.handlesChopAngle[self.handlesChopOutIndex] = angle
		if not self.isLastSegment:
			nextSegment = self.owner.segments[self.index + 1]
			nextSegment.onPrevOutHandleValueChange(self, updateView)

	def onPrevOutHandleValueChange(self, prevSegment, updateView=False):
		if prevSegment.lockHandles:		
			self.inslope = 0.0
			self.inaccel = prevSegment.outaccel
			self.updateView()
		if (updateView 
				and self.owner.handleSelected[self.handlesChopInIndex] == 1):
			self.keyframeControlsComp.UpdateView(
				'inslope', self.inslope
			)							
			self.keyframeControlsComp.UpdateView(
				'inaccel', self.inaccel
			)	

	def onNextInHandleValueChange(self, nextSegment, updateView=False):
		if self.lockHandles:		
			self.outslope = 0.0
			self.outaccel = nextSegment.inaccel
			self.updateView()	
		if (updateView 
				and self.owner.handleSelected[self.handlesChopOutIndex] == 1):
			self.keyframeControlsComp.UpdateView(
				'outslope', self.outslope
			)						
			self.keyframeControlsComp.UpdateView(
				'outaccel', self.outaccel
			)

	def setInRelSlopeAccel(self, slope, accel, setStart):
		if setStart:
			self.inOffsetAccel = self.inaccel
		slope = 0.0
		accel += self.inOffsetAccel
		slope = min(.999999, slope)	
		maxAccel = self.x1 - self.x0
		accel = min(maxAccel, max(0.0, accel))
		angle = math.degrees(math.atan2(slope, 1.0))
		x, y = self.getHandleRelXY(slope, accel)
		x += self.x0
		y += self.y0
		self.inslope = slope
		self.inaccel = accel
		self.keyframeControlsComp.UpdateView('inaccel', accel)
		self.keyframeControlsComp.UpdateView('inslope', slope)
		self.handlesChopLength[self.handlesChopInIndex] = max(accel,
														self.handleMinLength)
		self.handlesChopAngle[self.handlesChopInIndex] = angle
		if self.prevSegment is not None:
			if self.prevSegment.lockHandles:
				self.prevSegment.onNextInHandleValueChange(self, False)

	def setOutRelSlopeAccel(self, slope, accel, setStart):
		if setStart:
			self.outOffsetAccel = self.outaccel	
		slope = 0.0
		accel += self.outOffsetAccel	
		slope = min(.999999, slope)	
		maxAccel = self.x1 - self.x0
		accel = min(maxAccel, max(0.0, accel))
		angle = math.degrees(math.atan2(slope, 1.0)) + 180
		x, y = self.getHandleRelXY(slope, accel)
		x = self.x1 - x
		y = self.y1	- y	
		self.outslope = slope
		self.outaccel = accel
		self.keyframeControlsComp.UpdateView('outaccel', accel)
		self.keyframeControlsComp.UpdateView('outslope', slope)		
		self.handlesChopLength[self.handlesChopOutIndex] = max(accel,
														self.handleMinLength)
		self.handlesChopAngle[self.handlesChopOutIndex] = angle
		if not self.isLastSegment and self.lockHandles:
			nextSegment = self.owner.segments[self.index + 1]
			nextSegment.onPrevOutHandleValueChange(self, False)	

	def setInSlopeAccel(self, slope=None, accel=None):
		slope = 0.0
		if accel is None:
			accel = self.inaccel	
		maxAccel = self.x1 - self.x0
		accel = min(maxAccel, max(0.0, accel))				
		angle = math.degrees(math.atan2(slope, 1.0))
		x, y = self.getHandleRelXY(slope, accel)
		x += self.x0
		y += self.y0
		self.inslope = slope
		self.inaccel = accel
		self.keyframeControlsComp.UpdateView('inaccel', accel)
		self.keyframeControlsComp.UpdateView('inslope', slope)
		self.handlesChopLength[self.handlesChopInIndex] = max(accel,
														self.handleMinLength)
		self.handlesChopAngle[self.handlesChopInIndex] = angle
		if self.prevSegment is not None:
			if self.prevSegment.lockHandles:
				self.prevSegment.onNextInHandleValueChange(self, True)

	def setOutSlopeAccel(self, slope=None, accel=None):
		slope = 0.0
		if accel is None:
			accel = self.outaccel
		maxAccel = self.x1 - self.x0
		accel = min(maxAccel, max(0.0, accel))						
		angle = math.degrees(math.atan2(slope, 1.0)) + 180
		x, y = self.getHandleRelXY(slope, accel)
		x = self.x1 - x
		y = self.y1	- y	
		self.outslope = slope
		self.outaccel = accel
		self.keyframeControlsComp.UpdateView('outaccel', accel)
		self.keyframeControlsComp.UpdateView('outslope', slope)		
		self.handlesChopLength[self.handlesChopOutIndex] = max(accel,
													self.handleMinLength)
		self.handlesChopAngle[self.handlesChopOutIndex] = angle
		if not self.isLastSegment and self.lockHandles:
			nextSegment = self.owner.segments[self.index + 1]
			nextSegment.onPrevOutHandleValueChange(self, True)	


class TimeGraph:
	# TODO implement better method - use Numpy and consolidate TimerBarExt
	def __init__(self, ownerComp):
		self.ownerComp = ownerComp
		self.keyframerComp = ownerComp.parent.Keyframer
		self.viewComp = ownerComp.parent()
		self.keysViewComp = self.viewComp.op('keysView')
		self.timerBarComp = ownerComp.op('timerBar')
		self.valueLabelsComp = self.keysViewComp.op('valueLabels')
		self.valueLabelComps = self.valueLabelsComp.findChildren(name='label*')
		self.valueLabelComps.sort(key=lambda x: x.name)
		self.valueLabelPars = [(c.op('text').par.text, c.par.y, c.par.display) 
								for c in self.valueLabelComps]
		self.numValueLabelComps = len(self.valueLabelComps)
		self.GetDim()
	
	@property
	def Animrangeend(self):
		return self.ownerComp.par.Animrangeend.eval()

	@property
	def Animrangestart(self):
		return self.ownerComp.par.Animrangestart.eval()

	@property
	def numValueLabels(self):
		return self.ownerComp.storage.get('numValueLabels', 0)
	@numValueLabels.setter
	def numValueLabels(self, value):
		self.ownerComp.storage['numValueLabels'] = value

	def GetDim(self):
		self.h = self.keysViewComp.width
		self.w = self.keysViewComp.height
		self.graphH = self.h # - 15
		self.graphW = self.w

	def SetView(self):
		# self.SetTime()
		# self.SetValue()
		# TODO implement graph in with geometry instancing in keysView/render
		# below is a temp workaround due to the transform being behind 1 frame
		run("args[0]()", self.setView, delayFrames=1)

	def setView(self):
		self.SetTime()
		self.SetValue()	

	def SetTime(self):
		animStart = self.keyframerComp.AnimationRangeStart	
		animEnd = self.keyframerComp.AnimationRangeEnd
		horzRange = self.keyframerComp.KeysViewHorzRange
		start = vMath.rangeValue(animStart, *horzRange, 
								0, self.keysViewComp.width)
		end = vMath.rangeValue(animEnd, *horzRange, 0, self.keysViewComp.width)
		length = abs(end - start)
		timeWidth = length / 4 * (60 / animEnd)
		timeWidthMin = self.ownerComp.par.Timewidthmin.eval()
		minRatio = timeWidthMin / timeWidth
		minRatio = math.pow(2, math.ceil(math.log(minRatio) / math.log(2)))

		self.ownerComp.par.Timeoffset = start
		self.ownerComp.par.Endbound = length
		self.ownerComp.par.Timewidth = timeWidth * minRatio

	def SetValue(self):
		vRangeMin = self.keyframerComp.KeysViewVertRange[0]
		vRangeMax = self.keyframerComp.KeysViewVertRange[1]
		valueOffset = vMath.rangeValue(0, vRangeMin, vRangeMax, 
										0, self.keysViewComp.height)
		vRange = vRangeMax - vRangeMin
		scaleFactor = self.ownerComp.par.Valuelinesscalefactor.eval()
		vRangeRound = self.ArbRound(vRange, scaleFactor, vRangeMin)
		vRange = 1.0 / vRange * self.keysViewComp.height * .5 * vRangeRound
		self.ownerComp.par.Valueoffset = valueOffset
		self.ownerComp.par.Valueheight = vRange

	def arbRound(self, x, prec=2, base=.05):
		return round(base * round(float(x) / base), prec)

	def ArbRound(self, val, scale, minVal):
		if val < 1.0: 
			p = 4
			dPos = str(1 / val).index('.')	
			b = round(math.pow(.1, dPos), 10)		
		elif val < 2.0: 
			p = 2
			b = .25
		elif val < 5.0: 
			p =  1
			b = 1			
		elif val < 10.0: 
			p = 1
			b = 1
		else:
			p = 1
			dPos = str(val).index('.')	
			b = math.pow(10, dPos - 1)
	
		vRange = self.arbRound(val, p, b)
		minVal = self.arbRound(minVal, p, b)

		lessThanOne = False	
		if val < 1.0:
			val = 1.0 / val
			lessThanOne = True

		intLessThanOne = int(lessThanOne)
		# scale the value from 1. to 10.
		decPos = str(val).index('.')	
		decMult = math.pow(10, decPos + [0, 1][intLessThanOne])
		decMult *= .1
		val = val / decMult

		# get the scale factor
		if val < 2.0: val = .1
		elif val < 5.0: val =  .2
		elif val < 10.0: val =  .4

		if lessThanOne: 
			val /= decMult
			val *= scale *  4
			self.setValueLabels(minVal, val, vRange)
			return val

		val *= decMult
		val *= scale

		self.setValueLabels(minVal, val, vRange)

		return val

	def setValueLabels(self, minVal, val, vRange):
		self.labelVals = []
		self.numValueLabels = int((vRange * 2) / val + 2)
		for i in range(self.numValueLabels):
			posY = vMath.rangeValue(
				minVal,
				*self.keyframerComp.KeysViewVertRange,
				0,
				self.keysViewComp.height	
			)
			minVal = round(minVal, 4)
			self.labelVals.append((minVal, posY))
			minVal += val * .5

		for i, labelComp in enumerate(self.valueLabelComps):
			if i < self.numValueLabels:
				self.valueLabelPars[i][0].val = self.labelVals[i][0]
				self.valueLabelPars[i][1].val = self.labelVals[i][1]
				self.valueLabelPars[i][2].val = True
			else:
				self.valueLabelPars[i][2].val = False


class TimerBarExt(object):
	# TODO implement better method - bring into TimeGraph
	# get all values in one step in Numpy	
	def __init__(self, ownerComp):
		self.ownerComp = ownerComp
		self.keyframerComp = ownerComp.parent.Keyframer
		self.viewComp = self.keyframerComp.op('view')
		self.timeGraphComp = self.viewComp.op('timeGraph')
		self.MinRatio = 1.0
		self.PrevMinRatio = 1.0
		self.Setup()
		self.Position()

	def Position(self):
		try:
			self.NumBeats = math.ceil(self.keyframerComp.LengthSeconds * 2)

			totalWidth = self.timeGraphComp.par.Endbound
			width = totalWidth / self.NumBeats
			widthMin = 20 * self.timeGraphComp.par.Beatlinesscalefactor
			self.MinRatio = widthMin / width
			self.MinRatio = math.pow(2, 
								math.ceil(math.log(self.MinRatio) / math.log(2)))
			self.MinRatio = max(1, self.MinRatio)
			for beat in range(int(self.NumBeats / self.MinRatio) + 1):
				pos = width * self.MinRatio * beat
				self.ownerComp.op('label' + str(beat)).par.x = pos
			if self.MinRatio != self.PrevMinRatio:
				self.Setup()
			self.PrevMinRatio = self.MinRatio
		except:
			pass

	def Setup(self):
		self.SetupSeconds()

	def SetupSeconds(self):
		try:
			self.NumBeats = math.ceil(self.keyframerComp.LengthSeconds * 2)
			for beat in range(self.NumBeats + 1):
				Beat = beat * self.MinRatio	
				label = str(Beat / 2)
				labelOP = self.ownerComp.op('label' + str(beat))
				labelOP.op('text').par.text = label
				if Beat <= self.NumBeats:
					labelOP.par.display = 1
				else:
					labelOP.par.display = 0
		except:
			pass

	def Scrub(self):
		me.fetch('AnimCOMP').par.cuepoint = (self.ownerComp.panel.u * 4 *
						op.LM.fetch('TICKS_PER_BEAT') * me.fetch('LengthBars'))
