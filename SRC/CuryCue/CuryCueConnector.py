#import mysql.connector
import urllib
import sys
import re
import os
from collections import namedtuple, OrderedDict
from dataclasses import dataclass
from typing import Any


class CuryCueConnector:
    def __init__(self):
        pass
    def checkFixtureByPath(self,path):
        found=False
        if path in self.LocalFixturesByPath.keys():
            found=True
        return found
    def checkFixtureParByName(self,fixture,name):
        found=False
        for par in fixture.pars:
            if par.par_name==name:
                found=True
        return found


    def LoadCue(self):
        self.LocalCueData = []
        self.LocalFixtureData = []
        fields = ['id', 'order', 'name', 'memo', 'type', 'update_mode', 'linked', 
                  'osc_bind', 'dmx_bind', 'is_enabled', 'frame_bind']
        myQuery = self.QUERY(table='cue', fields=fields, 
                             condition=" is_enabled='1'", conditionData=[], order=" `order` ")
        for raw_row_cue in self.getListByFields(myQuery):
            self.LocalCueData.append(self.LoadDBtoStruct(
                self.CUE(), myQuery, raw_row_cue))

    def LoadCueFloatData(self):
        
        for cue in self.LocalCueData:

            fields = ['id', 'id_fixture', 'par_name', 'par_value',
                      'fade_in', 'fade_out', 'delay_in', 'delay_out', 'par_text_value']
            fields_query_prefix=[]
            for f in fields:
                fields_query_prefix.append('cfd')
                
            
            myQuery = self.QUERY(table='cue_float_data as cfd, fixture as fix', fields=fields, fields_query_prefix = fields_query_prefix,
                                 condition=" cfd.id_cue=? and cfd.id_fixture=fix.id", conditionData=[int(cue.id)], order=" fix.`order` ")
            myParsList = list()
            myParsDict = dict()
            
            for raw_row_cue in self.getListByFields(myQuery):
                # print (raw_row_cue)
                myParsFloat = self.LoadDBtoStruct(self.CUEPARFLOAT(), myQuery, raw_row_cue)
                myParsDictByFixId = dict ()
                myFixture=self.LocalFixturesByID[myParsFloat.id_fixture]
                # stitch the path for the unique field ID
                myFixturePath=myFixture.global_object_location
                myParsFloat.full_par_path="{}:{}".format(myFixturePath, myParsFloat.par_name)
                #
                myParsFloat.fixture=myFixture
                # add to the general list of key parameters
                myParsList.append(myParsFloat)
                myParsDict[myParsFloat.full_par_path]=myParsFloat
                if myParsFloat.id_fixture not in myParsDictByFixId.keys():
                    myParsDictByFixId[myParsFloat.id_fixture]=[]
                myParsDictByFixId[myParsFloat.id_fixture].append(myParsFloat)
            cue.pars_float = myParsList
            cue.pars_float_by_path = myParsDict
            try:
                cue.pars_float_by_fix_id=myParsDictByFixId
            except:
                cue.pars_float_by_fix_id=dict()


            # self.LoadDBtoStruct(myCueFloatPar, myQuery)
            # print (myCueFloatPar)

        pass

    def LoadCueFloatDataV2(self):
        # Initialize variables and lists
        CUE_PROCESS_CURSOR = []
        CUE_PROCESS_CURSORbyPath = dict()
        _allPars=[]
        
        # Iterate through all fixtures and their parameters
        for myFixture in self.LocalFixtureData:
            for myPars in myFixture.pars:
                myPathFull="{}:{}".format(myFixture.global_object_location, myPars.par_name)
                myField = self.ACTIVE_FIELDS(
                    id_par=myPars.id, id_fixture=myFixture.id, fixture_name=myFixture.name, 
                    fixture_object_location=myFixture.global_object_location, par_name=myPars.par_name,
                    par_value=myPars.default_value,par_text_value='', is_fixture_enabled=myFixture.is_enabled, 
                    fixture_ref=myFixture, fixture_par_ref=myPars, full_par_path=myPathFull, fade_in = myPars.fade_default, 
                    delay_in = myPars.delay_default)
                # Add fields to list and dictionary for later reference
                CUE_PROCESS_CURSOR.append(myField)
                CUE_PROCESS_CURSORbyPath[myPathFull]=myField
                # Add all parameters to list for reference
                _allPars.append(myPars)
            
        # Iterate through all cues and their parameters
        for myCue in self.LocalCueData:
            for myCuePar in myCue.pars_float:
                # If parameter name matches that of a fixture parameter, add reference to fixture parameter
                if myCuePar.par_name in myCuePar.fixture.pars_float_by_name.keys():
                    _fix_par_match=myCuePar.fixture.pars_float_by_name[myCuePar.par_name]
                    myCuePar.fixture_par_ref=_fix_par_match
        
        # Set field names for later reference
        _fields = ['par_name', 'par_value','par_text_value','fade_in', 'delay_in', 'fixture_name', 'id_fixture', 'fixture_object_location', 'full_par_path']
        # Iterate through all cues and their parameters, filling in empty values with previous or default values
        for myCue in self.LocalCueData:
            listForChangedFieldsByCue=[]
            for cuePar in myCue.pars_float:
                if cuePar.fixture_par_ref in _allPars:
                    for f in _fields:
                        v=getattr(cuePar, f)
                        setattr(CUE_PROCESS_CURSORbyPath[cuePar.full_par_path], f, v)
                        setattr(CUE_PROCESS_CURSORbyPath[cuePar.full_par_path], "id_par_cue", cuePar.id)
                    listForChangedFieldsByCue.append(cuePar.fixture_par_ref)
                            
            #############################################################################
            # HERE WE NEED TO ASSIGN TO KEYS WHAT THEY DID NOT HAVE
            for fixPar in _allPars:

                if fixPar not in listForChangedFieldsByCue:
                    for cpc in CUE_PROCESS_CURSOR:
                        if cpc.fixture_par_ref is fixPar:
                            
                            myFix=self.LocalFixturesByID[cpc.id_fixture]
                            myPathFull="{}:{}".format(myFix.global_object_location, cpc.par_name)
                            newPar=self.CUEPARFLOAT(id=-1, par_name=cpc.par_name,par_value=cpc.par_value,par_text_value=cpc.par_text_value, fade_in=cpc.fade_in, delay_in=cpc.delay_in,
                                                   id_fixture=cpc.id_fixture, fixture_name=cpc.fixture_name, fixture_object_location=cpc.fixture_name,
                                                   full_par_path=myPathFull, fixture=myFix, is_derived=True)
                            myCue.pars_float.append(newPar)
                            myCue.pars_float_by_path[myPathFull]=newPar
                
                        

                pass
        #############################################################################
        # ВЫЧИСЛЯЕМ ПАРАМЕТР С САМЫМ ДЛИННЫМ ФЭЙДОМ И ПРОПИСЫВАЕМ ЕГО В parWithLongestFade
        #############################################################################
        # for myCue in self.LocalCueData:
        #     parsTime=dict()
        #     for cuePar in myCue.pars_float:
        #         parsTime[cuePar.fade_in+cuePar.delay_in]=cuePar
        #     parsTime=dict(sorted(parsTime.items()))
        #     if len(parsTime.keys())>0:
        #         longestPar=parsTime.popitem()
        #         myCue.parWithLongestFade=longestPar[1].par_name
        #         print ("Cue name: {}, par: {}".format(myCue.name, longestPar[1].par_name))
            
                
                


            # parWithLongestFade
                
        
                    #CUE_PROCESS_CURSORbyPath

        pass


    def ResortCuesByID(self):
        for cue in self.LocalCueData:
            self.LocalCueDataByID[cue.id]=cue

    def LoadFixtureData(self):
        fields = ['id', 'order', 'name', 'global_object_location', 'type', 'is_enabled']
        self.LocalFixtureData = list()
        self.LocalFixturesByID=dict()
        self.LocalFixturesByPath=dict()
        myQuery = self.QUERY(table='fixture', fields=fields,
                             condition="", conditionData=[], order=" `order`")
        for raw_row_cue in self.getListByFields(myQuery):
            myFixture = self.LoadDBtoStruct(
                self.FIXTURE(), myQuery, raw_row_cue)
            myFixture.original_location=myFixture.global_object_location
            if re.search(r'op\..+', myFixture.global_object_location):
                res = re.match(
                    r'op\.(.+)', myFixture.global_object_location).groups()[0]

                if hasattr(op, res):
                    myFixture.global_object_location = getattr(op, res).path

                # print (getattr(op, str(res)).path)
                # myFixture.global_object_location=op
                #print (myFixture.global_object_location)
            self.LocalFixtureData.append(myFixture)
            self.LocalFixturesByID[myFixture.id]=myFixture
            self.LocalFixturesByPath[myFixture.global_object_location]=myFixture
        pass

    def LoadFixturePars(self):
        for myFixture in self.LocalFixtureData:

            fields = ['id', 'id_fixture', 'par_name',
                      'par_name', 'default_value','fade_default', 'delay_default', 'is_enabled']
            myQuery = self.QUERY(table='fixture_float_data', fields=fields,
                                 condition=" id_fixture=?", conditionData=[int(myFixture.id)], order="")
            myParsList = list()
            myParsDict = dict()
            for raw_row_cue in self.getListByFields(myQuery):
                myParsFloat = self.LoadDBtoStruct(
                    self.FIXPAR(), myQuery, raw_row_cue)
                myParsFloat.name = myFixture.name
                myParsFloat.global_object_location = myFixture.global_object_location
                myParsFloat.id_fixture=myFixture.id

                myParsList.append(myParsFloat)
                myParsDict[myParsFloat.par_name]=myParsFloat

            myFixture.pars = myParsList
            myFixture.pars_float_by_name = myParsDict

    def CreateActiveFields(self):
        self.ActiveFields = list()
        self.ActiveFieldsByPath = dict()
        for myFixture in self.LocalFixtureData:

            for myPars in myFixture.pars:
                myPathFull="{}:{}".format(myFixture.global_object_location, myPars.par_name)
                myField = self.ACTIVE_FIELDS(
                    id_par=myPars.id, id_fixture=myFixture.id, fixture_name=myFixture.name, 
                    fixture_object_location=myFixture.global_object_location, par_name=myPars.par_name,
                    par_value=myPars.default_value, is_fixture_enabled=myFixture.is_enabled, 
                    fixture_ref=myFixture, fixture_par_ref=myPars, full_par_path=myPathFull)

                self.ActiveFields.append(myField)
                self.ActiveFieldsByPath[myPathFull]=myField

    def LoadDBtoStruct(self, myStruct, myQuery, raw_row_cue):
        i = 0
        for myValue in raw_row_cue:
            myField = myQuery.fields[i]
            if re.search("\.", myField):
                print ("AA!!")
            #print ("Name: {}, Value: {}".format(myField, myValue))
            setattr(myStruct, myField, myValue)
            i += 1
        return myStruct
