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
            ui.panes.current.owner=op(data['rowData']['Path'])
            print (data['rowData']['Path'])

    def SelectCueListRow(self, listComp, row):
        if listComp is None:
            return False

        if hasattr(listComp.par, "Selectedrows"):
            listComp.par.Selectedrows="" if row is None else str(row)

        if not self.CheckParentCooking(listComp):
            return False

        lister=listComp.op("list/lister")
        if lister is None:
            return False

        selectRow=getattr(lister, "SelectRow", None)
        if selectRow is not None:
            try:
                selectRow(row)
                return True
            except Exception as e:
                print("SelectRow failed on {}: {}".format(lister.path, e))
        
        listerExt=getattr(lister.ext, "ListerExt", None)
        if listerExt is not None and hasattr(listerExt, "SelectRow"):
            try:
                listerExt.SelectRow(row)
                return True
            except Exception as e:
                print("ListerExt.SelectRow failed on {}: {}".format(lister.path, e))

        return False

    def SyncCueListSelection(self, row):
        for tag in self.CueUILists:
            listComp=self.ownerComp.findChildren(tags=[tag])
            if len(listComp)>0:
                self.SelectCueListRow(op(listComp[0]), row)

    def SyncCurrentCueListSelection(self):
        if not self.cueSwitchBlock:
            self.cueSwitchBlock=True
            try:
                self.SyncCueListSelection(int(self.ownerComp.dock.par.Cuearrayindex)+1)
                self.switchBlockTimes=0
            finally:
                self.cueSwitchBlock=False

    def SetSelectedCue(self, val):
        if self.cueSwitchBlock:
            self.switchBlockTimes+=1
            if self.switchBlockTimes > 10:
                self.switchBlockTimes=0
                self.cueSwitchBlock=False
            return

        print (self.cueSwitchBlock)
        self.cueSwitchBlock=True
        try:
            # me.iop.cuelist.par.Selectedrows=str(val)
            self.ownerComp.dock.CueChangeByRow(val)
            self.SyncCueListSelection(val)
            self.switchBlockTimes=0
        finally:
            self.cueSwitchBlock=False

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
            try:
                self.SyncCueListSelection(ind+1)
                self.switchBlockTimes=0
            finally:
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
    def SwitchShowEditMode(self):
        currentMode=int(parent.curycueui.I.qqmodeswidget.par.Value0)
        if currentMode==1:
            parent.curycueui.I.qqmodeswidget.par.Value0=0
        else:
            parent.curycueui.I.qqmodeswidget.par.Value0=1
    def SetTabActive(self, name):
        for tab in self.tabs:
            if tab==name:
                
                if hasattr(self.I, tab):
                    self.setCompDisplay(tab, True)
                    self.ownerComp.dock.CueEditMode=name
            else:
                if hasattr(self.I, tab):
                    self.setCompDisplay(tab, False)
        run("op('{}').SyncCurrentCueListSelection()".format(self.ownerComp.path), delayFrames=1)

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
            
    def GetContentSystemBar(self):
        sideUi=op(parent.curycueui.dock.par.Sideui)
        if sideUi is not None:
            csb=sideUi.op("ContentSystemBar")
            if csb is not None:
                iconop=csb.op("ALL_CONTENT_ICONS")
                if iconop is not None:
                    return iconop.path

        return ""
        


