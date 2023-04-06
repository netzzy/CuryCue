#Shared Use License: This file is owned by Derivative Inc. (â€œDerivativeï¿½) 
#and can only be used, and/or modified for use, in conjunction with 
#Derivativeâ€™s TouchDesigner software, and only if you are a licensee who 
#has accepted Derivativeâ€™s TouchDesigner license or assignment agreement 
#(which also governs the use of this file).  You may share a modified version 
#of this file with another authorized licensee of Derivativeâ€™s TouchDesigner 
#software.  Otherwise, no redistribution or sharing of this file, with or 
#without modification, is permitted.

"""
All callbacks for this lister go in this DAT. For a list of available callbacks,
see:

https://docs.derivative.ca/Palette:lister#Custom_Callbacks
"""

# def onSelectRow(info):
# 	print(info)
#me.parent.curycueui.SetSelectedCue(info['row'])	
def onEditEnd(info):
    me.parent.curycueui.dock.Callback_cue_list_mode_pars("edit", info)
    