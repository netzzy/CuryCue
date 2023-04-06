import os
import re
from dataclasses import dataclass
from typing import Any

# UITabsCtrl = me.iop.utils.module.UITabsCtrl
from UtilsClass import UtilsClass, IOP, IKEY
    
        
class CuryCueUIClass (UtilsClass):
    def __init__(self, ownerComp):
        
        self.ownerComp = ownerComp
        print ("Ownercomp: {}".format(ownerComp))
        ownerComp.dock.par.Ui=ownerComp.path

        self.tabs=['fixturesui', 'editmodeui', 'showmodeui']
        op.DP.PrintAndDisplay("{} init".format(ownerComp.name))
        self.I=IOP(self)
        self.K=IKEY(self)
        self.cueSwitchBlock=False
        self.CueRunBlock=False
        self.CueListItemRightClicked=-1

        self.CueUILists=['showcuelist', 'cues_edit_list', 'cues_group_edit_list']
        self.switchBlockTimes=0
        self.AutoGotoContentComp=False
        pass

    def GoTo(self, data):
        if self.AutoGotoContentComp:
            ui.panes.current.owner=op(data['rowData']['Путь'])
            #print (data['rowData']['Путь'])
    def SetSelectedCue(self, val):
        if self.switchBlockTimes > 10:
            self.switchBlockTimes=False

        if not self.cueSwitchBlock:
            self.cueSwitchBlock=True
            # me.iop.cuelist.par.Selectedrows=str(val)
            self.ownerComp.dock.CueChangeByRow(val)
            for tag in self.CueUILists:
                listComp=self.ownerComp.findChildren(tags=[tag])
                # op(listComp.path).op("list")
                if len(listComp)>0:
                    if self.CheckParentCooking(op(listComp[0])):
                        op(listComp[0]).op("list/lister").SelectRow(val)
                        
                    # listComp.op("list").SelectRow(val)
            self.cueSwitchBlock=False
            self.switchBlockTimes=0
        else:
            self.switchBlockTimes+=1
    def CuesMenuSelector(self, info):
        print (self.CueListItemRightClicked)
        print (info)
        if info['item'] == "Duplicate Cue Without Parameters":
            self.ownerComp.dock.CueCopy(row = self.CueListItemRightClicked, _withItems=False)
            pass
        elif info['item'] == "Duplicate Cue With Parameters":
            self.ownerComp.dock.CueCopy(row = self.CueListItemRightClicked, _withItems=True)
            pass
        elif info['item'] == "Delete Cue":
            self.ownerComp.dock.CueDelete(row = self.CueListItemRightClicked)
            pass
        elif info['item'] == "Create New Blank Cue":
            self.ownerComp.op("addKeyUI").openViewer()
            n = parent.curycueui.op('addKeyUI/float1/numericValue0/field')
            n.setKeyboardFocus()			# set keyboard focus
            n.setKeyboardFocus(selectAll=True) # select all (example field text)

            pass


    def UpdateCueLists(self, ind):
        if not self.cueSwitchBlock:
            self.cueSwitchBlock=True
            for tag in self.CueUILists:
                    listComp=self.ownerComp.findChildren(tags=[tag])
                    if len(listComp)>0:
                        if self.CheckParentCooking(op(listComp[0])):
                            op(listComp[0]).op("list/lister").SelectRow(ind+1)
            self.cueSwitchBlock=False            


    def SetSelectedInfoFix(self, val):
        # me.iop.cuelist.par.Selectedrows=str(val)
        self.ownerComp.dock.FixInfoChangeByRow(val)

    def SetUIModeCUES(self):
        self.SetTabActive("cueui")
        pass
    def SetUIModeFIXTURES(self):
        self.SetTabActive("fixturesui")

        
        pass
    def SetUIModeSHOW(self):
        self.SetTabActive("showmodeui")
        pass
    def SetUIModeEDIT(self):
        self.SetTabActive("editmodeui")
        pass
    def SetTabActive(self, name):
        for tab in self.tabs:
            if tab==name:
                
                if hasattr(self.I, tab):
                    self.setCompDisplay(tab, True)
                    self.ownerComp.dock.CueEditMode=name
            else:
                if hasattr(self.I, tab):
                    self.setCompDisplay(tab, False)

    def setCompDisplay(self, name, value):
        if hasattr(self.I, name):
            path=getattr(self.I, name).path
            # print ("{}, {}".format(op(path), value))
            
            op(path).par.display=value
            cookState=value
            if cookState:
                op(path).allowCooking=True
            else:
                run("op(\"{}\").allowCooking=False".format(path, cookState), delayFrames=30)
            



