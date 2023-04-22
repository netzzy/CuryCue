import re
import os
from dataclasses import dataclass
from typing import Any, Tuple
import glob
import time
import fnmatch

from QClass import QClass
from CuryCueConnector import CuryCueConnector
from MysqlBase import MysqlBase
from UtilsClass import UtilsClass, IOP, IPAR
from InTableEditBase import *
from CuryCueStructsDef import *
from CuryCueAddByDragAndDrop import *
from FixtureUtils import *


class CuryCueClass (CuryCueStructsDef, MysqlBase, CuryCueConnector, UtilsClass, InTableDataEdit, CuryCueAddByDragAndDrop, FixtureUtils):
    def __init__(self, ownerComp):
        self.ownerComp = ownerComp
        self.chopExportDisabled=False
        op.DP.PrintAndDisplay("{} init".format(ownerComp.name))
        MysqlBase.__init__(self, ownerComp)
        self.ConnectDb()
        self.LocalCueData = []
        self.LocalCueDataByID = dict()
        self.LocalFixtureData = []
        self.LocalFixturesByPath = dict()
        self.ActiveFields = []
        self.ActiveFieldsByPath = []
        self.lastActiveCompInUI=dict()
        self.lastAddedFixtureIndex=0
        self.CueEditMode=""
        CuryCueConnector.__init__(self)
        UtilsClass.__init__(self)
        InTableDataEdit.__init__(self)
        self.I = IOP(self)
        self.P = IPAR(self)

        self.UpdateFromDb()
        self.q = QClass(ownerComp)
        self.SKIPCUE=False
        print ("OK")
        self.SetInitCue(1)
        self.autoCueFrameBindPreconditionSatisfied=False
        self.SetCurrentFrameForAutoCueRequest=False
        run("op('{}').SetInitCue({})".format(
            self.ownerComp.path, 1), delayFrames=20)
        
        pass

    # CUE CHANGE
    def Storeselected(self, updateDbAfter=True):
        res=None
        myFields = ['id_cue', 'id_fixture', 'par_name',
                    'par_value', 'fade_in', 'delay_in']
        # print (op(self.I.storedat).path)
        if self.CurrentCueID > 0:
            i = 0
            for (id_fixture, par_value, path, par_name, fade, delay) in self.I.storedat.rows():
                if i > 0:
                    try:
                        par_value=float(par_value)
                        myFields[3]='par_value'
                    except: 
                        par_value=str(par_value)
                        myFields[3]='par_text_value'
                        # myFields[3]='par_value'
                    newInsertQuery = self.QUERY_INSERT(table="cue_float_data", fields=myFields,
                                                       fieldsData=[int(self.CurrentCueID), int(id_fixture), str(par_name), par_value, float(fade), float(delay)], conditionData=[])
                    # print ("{} = {}".format(par_name, par_value))
                    res = self.insertIntoTable(newInsertQuery)
                    
                i += 1
            ui.status="{} {} {} in cue \"{}\" ({})".format("Modified or added" if i==0 else "Modified or added", i, "parameter" if i==1 else "parameters", self.Curcuename, self.Curcueid)
            if updateDbAfter:
                self.UpdateFromDb()
                self.SetInitCue(1)
            return res
        else:
            ui.status="No Q selected"
        
        pass

    def Process_InputRealtimeVal(self, v1, v2):
        if op(v1) is not None:
            if hasattr(op(v1).par, str(v2)):
                myPar=getattr(op(v1).par, str(v2))
                if myPar.isToggle:
                    if myPar.eval()==True:
                        v=1 
                    else:
                        v=0
                elif myPar.isString:
                    v=myPar.eval()
                else:
                    v="%g" % myPar.eval()
                return v

        

    def RunCue(self, cue, momentary=False):
        
        ui.status=("Running CUE: {}, name: {}".format(cue.id, cue.name))
        self.q.Forcestop()
        for i in range(0, len(self.ActiveFields)):
            # Check if there is an active field in the parameters of the called key.
            if self.ActiveFields[i].full_par_path in cue.pars_float_by_path:
                # If yes, run the cue.
                myCue = cue.pars_float_by_path[self.ActiveFields[i].full_par_path]

                # If the value has changed in the PO in relation to the active table or if the text in the text field has changed, run the fader.

                if float(self.ActiveFields[i].par_value) != float(myCue.par_value) or (self.ActiveFields[i].par_text_value != myCue.par_text_value):
                    # Fill in the data structure for the fader.
                    myCueTask = self.q.Qtask(name=myCue.par_name, value_start=self.ActiveFields[i].par_value, value_target=myCue.par_value,
                                            value_text=myCue.par_text_value,
                                            fade=myCue.fade_in, delay=myCue.delay_in, 
                                            full_par_path=self.ActiveFields[i].full_par_path, callback=self.CallbackFromFader,
                                            callback_complete=self.CallbackFromFaderComplete)
                    # If fades are turned off in the interface for debugging or if the call comes from the initializer (then we don't fade).
                    if self.FadesMode=="off" or momentary:
                        myCueTask.fade=0

                    # Stop the fade if one is already running.
                    self.q.StopByPathIndex(self.ActiveFields[i].full_par_path)
                    # Start the fade calculator.
                    self.q.CreateEvaluator(myCueTask)
                    self.ActiveFields[i].is_fading = 1
                    self.ActiveFields[i].is_fadingDelay = 0

                # Fill in the value in the active table, which can be filled in immediately.
                self.ActiveFields[i].fade_in = myCue.fade_in
                self.ActiveFields[i].delay_in = myCue.delay_in
                self.ActiveFields[i].is_cue_exist = 0 if myCue.is_derived else 1
                self.ActiveFields[i].id_par = myCue.id
            else:
                # If not, do not run it, but mark that there is no such key.
                self.ActiveFields[i].is_cue_exist = 0
                self.ActiveFields[i].id_cue = 0
                if self.ActiveFields[i].is_fading == 1:
                    self.ActiveFields[i].extra_export_frames = 1

                # self.ActiveFields[i].par_value=self.ActiveFields[i].fixture_par_ref.default_value

        pass

    def CallbackFromFader(self, task):
        # print ("name:{}, from: {}, to:{}, v:{}, progress:{}, path: {}".format(task.name,task.value_start,
        #  task.value_target, task.value, task.progress, task.full_par_path))
        myField = self.ActiveFieldsByPath[task.full_par_path]
        myField.par_value = task.value
        myField.par_text_value=task.value_text

        pass

    def CallbackFromFaderComplete(self, task):
        myField = self.ActiveFieldsByPath[task.full_par_path]
        myField.is_fading = 0
        task.running=0
        # print ("Evals: {}, {}".format(len(self.q.evaluators), self.q.evaluators[0].task.running))
        if len(self.q.evaluators)==0:
            ui.status="Cue done"
            if self.LocalCueDataByID[int(self.Curcueid)].linked==1:
                self.Gonextcue()

            #self.Gonextcue()
        pass


    def Gonextcue(self):
        self.Gocue()

    def Goprevcue(self):
        self.Gocue(dir="back")
        pass
    def Gocue(self, dir="forward"):

        myCueObj=self.LocalCueDataByID[int(self.Curcueid)]
        cur_cue_index=self.LocalCueData.index(myCueObj)
        next_cue_index=cur_cue_index+1 if dir=="forward" else cur_cue_index-1
        if not next_cue_index > len(self.LocalCueData)-1 and next_cue_index >=0:
            nextCue=self.LocalCueData[next_cue_index]
            if not self.SKIPCUE:
                self.RunCue(nextCue)
            self.SetOwnerPar('Cueid', nextCue.id)
            self.SetOwnerPar('Cuearrayindex', next_cue_index)
            self.SetOwnerPar('Cuename', nextCue.name)
            self.SetOwnerPar('Cueorder', nextCue.order)
            self.SetOwnerPar('Framebind', nextCue.frame_bind)
            op(self.ownerComp.par.Ui).UpdateCueLists(next_cue_index)
            
    def AddNewCue (self, order, name):
        if name=='':
            ui.status = "Enter name for new Cue!"
            return 
        
        r=self.executeUpdateQuery("INSERT INTO cue (`order`, `name`, `memo`, `is_enabled`) VALUES (?, ?, ?, 1)",
                            [float(order), str(name), ''])

        self.UpdateFromDb()
        me.iop.fixparlistrender.cook(force=True)
        self.SetInitCue(1)


    def CueCopy(self, row, _withItems):
        
        row = int(row) - 1
        myCue=self.LocalCueData[row]
        
        
            # print("cue: {}, withpars: {}, row: {} ".format( myCue.name, _withItems, row))

        r=self.executeUpdateQuery("INSERT INTO cue (`order`, `name`, `memo`, `is_enabled`) VALUES (?, ?, ?, 1)",
                            [myCue.order+1, myCue.name + " +", myCue.memo])
        r1=None
        if _withItems:
            for cuePar in myCue.pars_float:
                if cuePar.id != -1:
                    newCueId=r[1]
                    if newCueId > 0:
                        # print ("id_cue:{}, id_fixture:{}, par_name:{}, par_value:{},par_value_text:{}, fade_in:{}, delay_in:{}".format(myCue.id, cuePar.id_fixture, 
                        # cuePar.par_name, cuePar.par_value,cuePar.par_text_value,  cuePar.fade_in, cuePar.delay_in ))
                        r1=self.executeUpdateQuery("INSERT INTO cue_float_data (id_cue, id_fixture, par_name, par_value, par_text_value, fade_in, delay_in) VALUES (?, ?, ?,?, ?, ?, ?)",
                        [newCueId, cuePar.id_fixture, cuePar.par_name, cuePar.par_value, cuePar.par_text_value, cuePar.fade_in, cuePar.delay_in])
                        if not r1[0]:
                            ui.status="Error copying the key {} in parameter {}".format(myCue.id, cuePar.par_name)
                            self.UpdateFromDb()
                            me.iop.fixparlistrender.cook(force=True)
                            self.SetInitCue(1)                            
                            return 

                    
        

        if r[0]:

            ui.status="The key has been added with ID: {}".format(r[1])
        else: 
            ui.status="Something went wrong when adding the key"

        self.UpdateFromDb()
        me.iop.fixparlistrender.cook(force=True)
        self.SetInitCue(1)
    def CueDelete(self, row):
        row = int(row) - 1
        # print (row)
        myCue=self.LocalCueData[row]
        answer=ui.messageBox('Question', 'Are you sure you want to delete the key {} ({}, id:{}) and all its parameters?'.format(myCue.name, "%g"%myCue.order, myCue.id), buttons=['Yes', 'No'])
        if answer==0:
            print ("Yes")
            r=self.executeUpdateQuery("DELETE FROM cue_float_data WHERE id_cue=?", [myCue.id]) 
            r1=self.executeUpdateQuery("DELETE FROM cue WHERE id=?", [myCue.id])
            if r[0] and r1[0]:
                ui.status="The key {} has been deleted.".format(myCue.name)
            else: 
                ui.status="Something went wrong when deleting the key"
        self.UpdateFromDb()
        me.iop.fixparlistrender.cook(force=True)
        self.SetInitCue(1)

        pass

    def Reloadsql(self):
        self.LocalCueData = []
        self.LocalCueDataByID = dict()
        self.LocalFixtureData = []
        self.LocalFixturesByID = dict()
        self.LocalFixturesByPath = dict()
        self.ActiveFields = []
        #self.DisconnectDb()
        #self.ConnectDb()
        self.UpdateFromDb()
        self.UpdateCueListRender()

    def UpdateFromDb(self):
        self.LoadCue()
        self.LoadFixtureData()
        self.LoadFixturePars()
        self.LoadCueFloatData()
        self.LoadCueFloatDataV2()
        self.ResortCuesByID()
        self.CreateActiveFields()
        
        pass

    def SetInitCue(self, val):
        # self.CueChangeByRow(val)
        self.UpdateCueListRender()
        
        if int(self.CurrentCueID) in self.LocalCueDataByID.keys():
            self.RunCue(self.LocalCueDataByID[int(self.CurrentCueID)], momentary=1)

        else:
            pass
    def GetActiveEvaluatorsByPath(self):
        return self.q.evaluatorsByPath
    def GetActiveEvaluators(self):
        return self.q.evaluators
    def UpdateEveryFrame(self):
        self.q.UpdateEveryFrame()
        me.iop.activeparsrender.cook(force=True)
        me.iop.active_evaluators.cook(force=True)
        if self.ExportMode == "ValueExport":
            self.ExportCopyAllPars()
        elif self.ExportMode == "ChopExport" and self.chopExportDisabled is not True:
            me.iop.floatsrender.cook(force=True)
        
        if self.ownerComp.par.Isframebindenabled>0 :
            frameBindRanges=self.FRAMEBINDRANGE( triggerConditionRange=[self.ownerComp.par.Framebindrange1, self.ownerComp.par.Framebindrange2], triggerRange=[self.ownerComp.par.Framebindrange2, self.ownerComp.par.Framebindrange3] )
            self.checkIfThereRangeAutoCue(frameBindRanges)

        if self.SetCurrentFrameForAutoCueRequest:
            r=self.executeUpdateQuery("UPDATE cue SET `frame_bind`= ? WHERE id=?",
                    [str(int(self.ownerComp.par.Currentframe)), str(int(self.Curcueid))])
            ui.status=r
            self.UpdateFromDb()
            #op.curycue.I.cuelist.cook(force=True)
            self.SetInitCue(1)
            self.SetCurrentFrameForAutoCueRequest=False
        
        # проверяем, не изменился ли выбранный контейнер 
        self.autoSelectFixtureByCompName()
    def checkIfThereRangeAutoCue(self, frameBindRanges):
        timelineCurrentFrame=self.ownerComp.par.Currentframe
        if frameBindRanges.triggerRange[0]==0:
            pass
        if timelineCurrentFrame in range (frameBindRanges.triggerConditionRange[0], frameBindRanges.triggerConditionRange[1]):
            self.autoCueFrameBindPreconditionSatisfied=True
        else:
            if self.autoCueFrameBindPreconditionSatisfied:
                if timelineCurrentFrame in range (frameBindRanges.triggerRange[0], frameBindRanges.triggerRange[1]):
                    ui.status="AUTOCUE by FRAME ::: GO"
                    self.Gocue()
            self.autoCueFrameBindPreconditionSatisfied=False
        pass
    def Clearselfixtures(self):
        self.lastActiveCompInUI.clear()
        self.autoSelectFixtureByCompName(isSomethingChanged=True, force=True)
        pass
    def autoSelectFixtureByCompName(self, isSomethingChanged=False, force=False):
        def findRowAndMakeList():
            myRowsToSelect=[]
            myRow=None
            for selFixId in self.lastActiveCompInUI.keys():
                if self.CueEditMode=="fixturesui":
                    myRow=self.ownerComp.I.uiFixtureModeFixlistWidget.op("out1")[str(selFixId),0]
                elif self.CueEditMode=="editmodeui":
                    myRow=self.ownerComp.I.uiEditModeFixlistWidget.op("out1")[str(selFixId),0]
                if myRow is not None:
                    myRowsToSelect.append(str(myRow.row))

            return myRowsToSelect
        
        if force or self.DeviceSelectMode!="Off":
            myAddedIndex=0
            for myFix in self.LocalFixtureData:
                if hasattr(op(myFix.global_object_location), "selected"):
                    
                    if getattr(op(myFix.global_object_location), "selected")==1:
                        myAddedIndex+=1
                        if myFix.id not in self.lastActiveCompInUI.keys():
                            # EVENT: выбран новый контейнер 
                            if self.DeviceSelectMode=="Switch1":
                                self.lastActiveCompInUI.clear()
                            myFix.is_selected=True
                            self.lastActiveCompInUI[myFix.id]=True
                            isSomethingChanged=True
                            
                            if self.DeviceSelectMode=="Switch1":
                                break

                    else:
                        if not self.DeviceSelectMode=="Switch1" and not self.DeviceSelectMode=="Add":
                            if myFix.id in self.lastActiveCompInUI.keys():
                                
                                myFix.is_selected=False
                                isSomethingChanged=True
                                
                                
                                # print ("{}, {}, {}".format(len(self.lastActiveCompInUI), self.DeviceSelectMode, myAddedIndex))
                                self.lastActiveCompInUI.pop(myFix.id)

            if self.lastAddedFixtureIndex!=myAddedIndex and self.DeviceSelectMode=="Add" and myAddedIndex==0:
                self.DeviceSelectMode=3
            self.lastAddedFixtureIndex=myAddedIndex
            if isSomethingChanged:
                    # We turn off auto-mode completely if a non-fixture-comp mode is selected during addition
                rowsToSelectList=findRowAndMakeList()
                # rowsToSelectList=
                # print (rowsToSelectList)
                rowsToSelectLine=" ".join(rowsToSelectList if self.DeviceSelectMode!="Switch1" else [rowsToSelectList[0]]) if len(rowsToSelectList)>0 else ""
                self.ownerComp.I.uiEditModeFixlistWidget.par.Selectedrows=rowsToSelectLine
                
    def SetActiveFixtureByPath(self, path):
        if len(ops(path)) > 0:
            if path in self.LocalFixturesByPath:
                myFix=self.LocalFixturesByPath[path]
                rowIndex=self.LocalFixtureData.index(myFix)
                
                self.FixtureRowsSelected=str(rowIndex)
    def UnselectAllActiveFixtures(self):
        self.FixtureRowsSelected=""
        


    def ExportCopyAllPars(self):
        for myField in self.ActiveFields:
           
#            if (myField.is_fading == 1 or myField.extra_export_frames >= 1) and myField.is_par_enabled:
            
            
            if hasattr(op(myField.fixture_object_location), "par"):
                
                if hasattr(op(myField.fixture_object_location).par, myField.par_name):
                    thePar=getattr(op(myField.fixture_object_location).par, myField.par_name)
                    if myField.par_text_value is None or len(myField.par_text_value)==0:
                        setattr(op(myField.fixture_object_location).par,
                                myField.par_name, myField.par_value)
                                
                    else:
                        setattr(op(myField.fixture_object_location).par,
                                myField.par_name, myField.par_text_value)

            if myField.is_fading == 0 and myField.extra_export_frames >= 1:
                    myField.extra_export_frames -= 1

        pass

    def UpdateCueListRender(self):
        me.iop.cuelist.cook(force=True)
        me.iop.fixlistrender.cook(force=True)
        me.iop.fixlistrender_orig_paths_for_edit.cook(force=True)
        me.iop.fixparlistrender.cook(force=True)
        me.iop.activeparsrender.cook(force=True)
        me.iop.activeparsrenderlive.cook(force=True)
        me.iop.storedat.cook(force=True)
        
    def FullReloadCuryCue(self):
        exec_string1='op("{}").allowCooking=False'.format(self.ownerComp.path)
        exec_string2='op("{}").allowCooking=False'.format(op(self.ownerComp.par.Ui).path)
        exec_string3='op("{}").allowCooking=True'.format(self.ownerComp.path)
        exec_string4='op("{}").allowCooking=True'.format(op(self.ownerComp.par.Ui).path)
        run(exec_string1, delayFrames=10)
        run(exec_string2, delayFrames=30)
        run(exec_string3, delayFrames=50)
        run(exec_string4, delayFrames=80)
    def BackupSqlDb(self, myfilename=None):
        
        # extension = "sql"
        # timestr = time.strftime("%Y%m%d-%H%M%S")
        # path=project.folder
        # if myfilename is not None:
        #     timestr=myfilename
        # file_name = "{}/db/{}.{}".format(path, timestr, extension)
        # dbPass=""
        # if self.ownerComp.par.Dbpassword.eval()!='':
        #     dbPass=" -p{} ".format(self.ownerComp.par.Dbpassword.eval())
        # exec_string="{}/db/mysqldump.exe --add-drop-table -h{} -u{} {} {} >{}".format(path,self.ownerComp.par.Dbhost, self.ownerComp.par.Dbuser, dbPass, self.ownerComp.par.Dbname, file_name)
        
        # res=os.system(exec_string)
        # print (exec_string)
        pass
        # ui.status="Saved {}".format(file_name)
    def RestoreSqlDb(self, file):
        # self.DisconnectDb()
        # file_name = "{}/db/{}.{}".format(project.folder, file, "sql")
        # dbPass=""
        # if self.ownerComp.par.Dbpassword.eval()!='':
        #     dbPass=" -p{} ".format(self.ownerComp.par.Dbpassword.eval())        
        # exec_string="{}/db/mysql.exe -h{} -u{} {} {} <{}".format(project.folder,self.ownerComp.par.Dbhost, self.ownerComp.par.Dbuser, dbPass, self.ownerComp.par.Dbname, file_name)
        # run('import os')
        # run('os.system("{}")'.format(exec_string), delayFrames=10)
        # ui.status="Loaded {}".format(file_name)
        # run('op("{}").FullReloadCuryCue()'.format(self.ownerComp.path), delayFrames=300)
        pass


    def CueChangeByRow(self, val):
        self.SetOwnerPar('Cuearrayindex', int(val)-1)
        val -= 1
        cue = self.LocalCueData[int(val)]
        self.RunCue(cue)
        self.SetOwnerPar('Cueid', cue.id)
        self.SetOwnerPar('Cuename', cue.name)
        self.SetOwnerPar('Cueorder', cue.order)
        self.SetOwnerPar('Framebind', cue.frame_bind)

    def FixInfoChangeByRow(self, val):
        self.SetOwnerPar('Cuearrayindex', int(val))
        val -= 1
        fix = self.LocalFixtureData[int(val)]
        self.SetOwnerPar('Fixtureidforinfo', fix.id)

    def SetNextExportMode(self):
        if int (self.ownerComp.par.Exportmode) < 2:
            self.ownerComp.par.Exportmode=int (self.ownerComp.par.Exportmode)+1
        else:
            self.ownerComp.par.Exportmode=0
        return
    def SetPrevExportMode(self):
        if int (self.ownerComp.par.Exportmode) > 0:
            self.ownerComp.par.Exportmode=int (self.ownerComp.par.Exportmode)-1
        else:
            self.ownerComp.par.Exportmode=2
        return

    def ExportmodeChanged(self, par, prev):
        if prev!=par:
            ui.status="Export mode has been changed to {}".format(par)
            if par == "ChopExport" and self.chopExportDisabled is not True:
                me.iop.floatsrender.export = True
            else:
                me.iop.floatsrender.export = False


    @property
    def CurrentCueID(self):
        __CurrentCueID = self.ownerComp.par.Cueid
        return self.ownerComp.par.Cueid

    @property
    def ExportMode(self):
        
        self.__ExportMode = self.ownerComp.par.Exportmode
        return self.ownerComp.par.Exportmode
    @ExportMode.setter
    def ExportMode(self, val):
        self.ownerComp.par.Exportmode=int(val)
        __ExportMode = int(val)
        return __ExportMode
    @property
    def DeviceSelectMode(self):
        __DeviceSelectMode = self.ownerComp.par.Autoselectdevicebycomp
        return __DeviceSelectMode
    @DeviceSelectMode.setter
    def DeviceSelectMode(self, val):
        self.ownerComp.par.Autoselectdevicebycomp=int(val)
        __DeviceSelectMode = int(val)
        return __DeviceSelectMode
    
    @property
    def FadesMode(self):
        __FadesMode = self.ownerComp.par.Fades
        return __FadesMode
    @FadesMode.setter
    def FadesMode(self, val):
        self.ownerComp.par.Fades.index=int(val)
        __FadesMode = int(val)
        return __FadesMode
    @property
    def ParsSelMode(self):
        __ParsSelMode = self.ownerComp.par.Parsselmode
        return __ParsSelMode
    @property
    def FixtureRowsSelected(self):
        __FixtureRowsSelected=self.ownerComp.I.uiEditModeFixlistWidget.par.Selectedrows
        return __FixtureRowsSelected
    @FixtureRowsSelected.setter
    def FixtureRowsSelected(self, val):
        myVal=""
        try:
            myVal=str(val)
        except:
            myVal=val
            ui.status = "Issues encountered when setting the active fixture!"
            print (ui.status)
        self.ownerComp.I.uiEditModeFixlistWidget.par.Selectedrows=myVal
        __FixtureRowsSelected=myVal
        return __FixtureRowsSelected
    @property
    def Curcuename(self):
        __Curcuename=self.ownerComp.par.Cuename
        return __Curcuename
    @property
    def Curcueid(self):
        __Curcueid=self.ownerComp.par.Cueid
        return __Curcueid
    @property
    def Curcueorder(self):
        __Curcueorder=self.ownerComp.par.Cueorder
        return __Curcueorder
    @property
    def Framebind(self):
        __Framebind=self.ownerComp.par.Framebind
        return __Framebind
        