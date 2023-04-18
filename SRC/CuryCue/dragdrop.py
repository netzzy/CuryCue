def onDropGetResults(comp, info):
	parent.curycue.DroppedItem (info)

def onHoverStartGetAccept(comp, info):

	#debug('\nonHoverStartGetAccept comp:', comp.path, '- info:\n', info)
	return True # accept what is being dragged

def onHoverEnd(comp, info):
	"""
	Called when dragItems leave comp's hover area.

	Args:
		comp: the panel component being hovered over
		info: A dictionary containing all info about hover, including:
			dragItems: a list of objects being dragged over comp
			callbackPanel: the panel Component pointing to this callback DAT
	"""
	#debug('\nonHoverEnd comp:', comp.path, '- info:\n', info)


# callbacks for when associated Panel is being dragged

def onDragStartGetItems(comp, info):
	"""
	Called when information about dragged items is required.

	Args:
		comp: the panel clicked on to start drag
		info: A dictionary containing all info about drag
			callbackPanel: the panel Component pointing to this callback DAT

	Returns:
		A list of dragItems: [object1, object2, ...]
	"""
	dragItems = [comp] # drag the comp itself
	#debug('\nonDragStartGetItems comp:', comp.path, '- info:\n', info)
	return dragItems

def onDragEnd(comp, info):
	"""
	Called when a drag action ends.

	Args:
		comp: the panel clicked on to start drag
		info: A dictionary containing all info about drag, including:
			accepted: True if the drag was accepted, False if not
			dropResults: a dict of drop results. This is the return value of 
				onDropGetResults
			dragItems: the original dragItems for the drag
			callbackPanel: the panel Component pointing to this callback DAT
	"""
	#debug('\nonDragEnd comp:', comp.path, '- info:\n', info)
	
