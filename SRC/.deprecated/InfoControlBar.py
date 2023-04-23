import os
import math
import re
class InternalClass:

	def __init__( self ):
		self.my=me.parent()
		self.line1op=op("line1text")
		
		return

	def SetLine1 (self):
		SelObjName=op.vp_obj_picker.SelectedObject.name if hasattr(op.vp_obj_picker.SelectedObject, "name") else "---"
		# vid.index/sub:    {}, {}\n\t\t\t\t\t\t   {}\nlaser index/sub: {}, {}\n\t\t\t\t\t\t   {}
		myLine="\ncue id: {} ({})\n\n{}\n\nselected: {}\n".format( op.curycue.Curcueorder,op.curycue.Curcueid, 
				op.curycue.Curcuename, SelObjName)
		#  op.vcont.CycleIndex, op.vcont.CycleSubIndex, op.vcont.CurrentTox, op.lsg.CycleIndex, op.lsg.CycleSubIndex, op.lsg.CurrentTox
		self.line1op.par.text=myLine
		
		
	def GetFrame(self):
		return int(self.my.par.Frame.eval())

	def GetSecond(self):
		return round(self.my.par.Second.eval(), 2)
