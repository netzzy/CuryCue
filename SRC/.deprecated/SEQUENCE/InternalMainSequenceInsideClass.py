import os
import re
import sys
import urllib
import opentimelineio as otio
import mysql.connector
import re
import distutils.util

class InternalClass:

    def __init__( self ):
        print ("Sequence init")
        conn=mysql.connector.connect(host='localhost',database='premiere_to_touchdesigner',user='root',password='')
        if conn.is_connected():
            print('Connected to MySQL database')
        self.conn=conn
        self.baseCustomPars=['Fadein', 'Fadeout', 'Crossright', 'Crossleft', 'Mode', 'Fx1', 'Colorr', 'Colorg', 'Colorb', 'Exportfadeval', 'Exportprivateparsonstart', 'Exportprivateparsonstop']
        self.ccPars=['Fxcc', 'Highr', 'Highg', 'Highb', 'Gamma', 'Brightness', 'Contrast', 'Saturationmult', 'Hueoffset', 'Mono', 'Drywetfloor', 'Drywetwalls', 'Grainperiod', 'Grainmagnitude']
        self.feedbackPars=['Fxfeedback', 'Feedbackwalls', 'Feedbackdrywetwalls', 'Feedbackfloor', 'Feedbackdrywetfloor']
        self.sceneRotatorPars=['Fxscenerot', 'Sceneanglerot2d']
        self.equiRotatorPars=['Equirotator3dx', 'Equirotator3dy', 'Equirotator3dz']
        self.ddsPlayerPars=['Imagesequencepath', 'Filemask']
        return

    def Reset (self):
        print ("Reset Tracks")
        for i in range(1, op.Seqi.par.Tracks+1):
            self.ResetTrack(i)

    def Recreate (self):
        print ("Recreate replicators on tracks")
        for i in range(1, op.Seqi.par.Tracks+1):
            op.Seqi.op("Track"+str(i)).ReplicatorRecreate()

    def MoveTimeCursor(self, u, v):
        op.SeqTimerComp.op("time").frame=(u*op.Seqi.par.w)*op.Seqi.par.Framepixelratio
        return

    def ResetTrack(self, n):
        myTrack=op.Seqi.op("Track"+str(n))
        myTrack.Reset()

    def CheckTrackInRange(self):
        myframe=int(op("F")[0])
        isInRange=False
        for r in self.track1data:
            res=myframe in range (int(r[0]),int(r[1]))
            if res:
                isInRange=True
        return isInRange

            #if int(myframe) in range (int(r[0], int(r[1]))):
            #    print ("IN RANGE")
    def checkAndInsertCustomParsInSql(self, cursor, sql_id_clip, clipcomp, customPars):
        if hasattr(clipcomp, 'par'):
            for p in (customPars):
                if hasattr(clipcomp.par, p):
                    v=getattr(clipcomp.par, p)
                    myParType=v.style
                    

                    isExpr=False
                    if v.mode==ParMode.EXPRESSION:
                        isExpr=True
                        v=v.expr
                    if p=="Mode":
                        v=v.menuIndex                        
                    print ("Par: {}, Val: {}, Sqlid: {}, parType: {}, isExpr={}".format(str(p), str(v), str(sql_id_clip), myParType, isExpr))
                    # elif p=='Fx1':
                    #     v=int(v)
                    cursor.execute("REPLACE INTO clip_params (id_clip, par, value, is_expr) VALUES (?, ?, ?, ?)", (sql_id_clip, str(p), str(v), str(int(isExpr))))
                    self.conn.commit()


    def checkAndRequestCustomParInSql(self, cursor, sql_id_clip, clipcomp, customPars):
        for p in (customPars):
            cursor.execute("SELECT value, is_expr from clip_params WHERE id_clip=? and par=?", (int(sql_id_clip), p))
            v=cursor.fetchone()
            if v is not None:
                
                
                if hasattr(clipcomp, 'par'):
                    if hasattr(clipcomp.par, p):
                        myValue=v[0]
                        isExpr=v[1]
                        
                        
                        
                        v=getattr(clipcomp.par, p)
                        myParType=v.style
                        print (myParType)
                        if int(isExpr)==1:
                            myValue=str(myValue)
                        elif myParType=="Toggle" :
                            myValue=bool(distutils.util.strtobool(myValue))
                        elif myParType=="Str" or myParType=="Folder" or myParType=="File":
                            myValue=str(myValue)
                        
                        else:
                            myValue=float(myValue)
                        if myParType=="Menu" :
                            modemenu=getattr(clipcomp.par, p)
                            setattr(modemenu, "menuIndex", myValue)
                        else:
                            print ("p: {}, v: {}".format(p, myValue))
                            if int(isExpr)!=1:
                                setattr(clipcomp.par, p, myValue)
                            else:
                                setattr(v, "enableExpr", myValue)
                          
    def SaveAllCustomParams(self):
        cursor=self.conn.cursor()
        # rows = cursor.fetchall()
        #cursor.execute()
        for track_id in range(1, op.Seqi.par.Tracks+1):
            myTrack=op.Seqi.op("Track"+str(track_id))
            for n in range(1, myTrack.op("trackdata").numRows):
                trackdata=myTrack.op("trackdata")
                clipname=trackdata[n, 6]
                                
                                
                cursor.execute("SELECT id FROM clips WHERE id_track=? and name=?", (int(track_id), str(clipname).lower()))
                in_sql=cursor.fetchone()
                sql_id_clip=0
                if in_sql is None:
                    cursor.execute("INSERT INTO clips (id_track, name) VALUES (?, ?)", (int(track_id), str(clipname).lower()))
                    self.conn.commit()
                    print ("Inserted id: {}".format(cursor.lastrowid))
                    sql_id_clip=cursor.lastrowid
                else:
                    sql_id_clip=in_sql[0]

                clipcomp=myTrack.op("clip"+str(int(n)))

                print ("Trackid: {}, clipid:{}, name: {}, in_sql_id:{}, clipname: {}".format(track_id, n, clipname, sql_id_clip, clipcomp))

                self.checkAndInsertCustomParsInSql(cursor, sql_id_clip, clipcomp, self.GetBaseCustomPars())
                self.checkAndInsertCustomParsInSql(cursor, sql_id_clip, clipcomp, self.GetCCPars())
                self.checkAndInsertCustomParsInSql(cursor, sql_id_clip, clipcomp, self.GetFeedbackPars())
                self.checkAndInsertCustomParsInSql(cursor, sql_id_clip, clipcomp, self.GetScenerotPars())
                self.checkAndInsertCustomParsInSql(cursor, sql_id_clip, clipcomp, self.GetEquiRotatorPars())
                self.checkAndInsertCustomParsInSql(cursor, sql_id_clip, clipcomp, self.GetDdsPlayerPars())
        return


    def LoadCustomParams(self):
        cursor=self.conn.cursor()
        for track_id in range(1, op.Seqi.par.Tracks+1):
            myTrack=op.Seqi.op("Track"+str(track_id))
            for n in range(1, myTrack.op("trackdata").numRows):
                trackdata=myTrack.op("trackdata")
                clipname=trackdata[n, 6]
                                
                cursor.execute("SELECT id FROM clips WHERE id_track=? and name=?", (int(track_id), str(clipname).lower()))
                in_sql=cursor.fetchone()
                sql_id_clip=0
                if in_sql is not None:
                    sql_id_clip=in_sql[0]
                    clipcomp=myTrack.op("clip"+str(int(n)))
                    self.checkAndRequestCustomParInSql(cursor, sql_id_clip, clipcomp, self.GetBaseCustomPars())
                    self.checkAndRequestCustomParInSql(cursor, sql_id_clip, clipcomp, self.GetCCPars())
                    self.checkAndRequestCustomParInSql(cursor, sql_id_clip, clipcomp, self.GetFeedbackPars())
                    self.checkAndRequestCustomParInSql(cursor, sql_id_clip, clipcomp, self.GetScenerotPars())
                    self.checkAndRequestCustomParInSql(cursor, sql_id_clip, clipcomp, self.GetEquiRotatorPars())
                    self.checkAndRequestCustomParInSql(cursor, sql_id_clip, clipcomp, self.GetDdsPlayerPars())
                    cursor.execute("SELECT value from clip_params WHERE id_clip=? and par=?", (int(sql_id_clip), "clip_prototype"))
                    in_sql_val=cursor.fetchone()
                    if in_sql_val is not None:
                        myCloneNode=str(in_sql_val[0])
                        setattr(clipcomp.par, "clone", myCloneNode)
                        print ("myCloneNode: {}".format(myCloneNode))
          
    def Pushcustompar(self):
        cursor=self.conn.cursor()
        myClipid=int(op.Seqi.par.Myclipid)
        myParName=str(op.Seqi.par.Myparname)
        myParValStr=str(op.Seqi.par.Parvalstr)
        
        if myClipid > 0 and myParName!="" and myParValStr!="":
            print ("Push -> id_clip: {}, parname: {}, parstr: {}, parfloat={}".format(myClipid, myParName, myParValStr, myParValFloat))
            cursor.execute("REPLACE INTO clip_params (id_clip, par, value) VALUES (?, ?, ?)", (myClipid, str(myParName), myParValStr))
            self.conn.commit()


    def Requestclipid(self):
        cursor=self.conn.cursor()
        
        myClipname=str(op.Seqi.par.Clipname)
        myTrackid=int(op.Seqi.par.Trackid)
        cursor.execute("SELECT id FROM clips WHERE id_track=? and name=?", (int(myTrackid), str(myClipname).lower()))
        in_sql=cursor.fetchone()
        if in_sql is not None:
            op.Seqi.par.Myclipid=int(in_sql[0])
        # op.Seqi.par.Myclipid
    def GetCCPars(self):
        return self.ccPars
    def GetFeedbackPars(self):
        return self.feedbackPars
    def GetScenerotPars(self):
        return self.sceneRotatorPars
    def GetEquiRotatorPars(self):
        return self.equiRotatorPars
    def GetDdsPlayerPars(self):
        return self.ddsPlayerPars
    def GetBaseCustomPars(self):
        return self.baseCustomPars

    def Load(self):
        op("track1data").clear()
 
        timeline = otio.adapters.read_from_file(str(op.Seq.par.Fcpxml))

        track_n=1

        for track in timeline.video_tracks() + timeline.audio_tracks():
            if track_n>op.Seqi.par.Tracks:
                track_n+=1
                continue
            else:
                print("Track: {}\t\tKind: {}\t\tDuration: {}".format(track_n,track.kind,track.duration()))
            

            myTrack=op.Seqi.op("Track"+str(track_n))
            myTrack.Reset()
            
            for item in track:
                print ("Track: {}".format(item))
                if isinstance(item, otio.schema.Clip):
                    
                    clip = item
                    
                    if isinstance(clip.media_reference, otio.schema.ExternalReference):
                        mediaspeed=1
                        for effect in clip.effects:
                            if effect.metadata["fcp_xml"]["effectid"]=="timeremap":
                                for rec_ in effect.metadata["fcp_xml"]["parameter"]:
                                    if rec_["name"]=="speed":
                                        mediaspeed=float(rec_["value"])/100.0
                                        print ("Speed: {}".format(mediaspeed))
                        
                        # print("Clip: {}".format(clip.name))
                      #  print("Clip name: {}, url: {}".format(clip.name, clip.media_reference.target_url))
                        # See the documentation to understand the difference
                        # between each of these ranges:
                        # https://opentimelineio.readthedocs.io/en/latest/tutorials/time-ranges.html
                        #_summarize_range("  Trimmed Range", clip.trimmed_range())
                        #_summarize_range("  Visible Range", clip.visible_range())
                        
                     #   print ("Position: Start time:{}\t\tEnd time: {}\t\tDuration: {}".format(clip.range_in_parent().start_time.value, clip.range_in_parent().end_time_exclusive().value, clip.duration().value))
                     #   print ("Media: Start time:{}\t\tEnd time: {}\t\tDuration: {}".format(clip.visible_range().start_time.value, clip.visible_range().end_time_exclusive().value, clip.duration().value))
                #		print ("Start time:{}\t\tEnd time: {}".format(clip.trimmed_range().start_time, clip.trimmed_range().end_time_exclusive()))
                    #    print ("\n")

                        url=urllib.parse.unquote(clip.media_reference.target_url)
                        urlcut=re.split(r'file:\/\/localhost\/', url)
                        filepath=""
                        if urlcut[1] is not None:
                            filepath=urlcut[1]
                        print (filepath)
                        myPosStart=clip.range_in_parent().start_time.value
                        if myPosStart < 1:
                            myPosStart=1
                        myTrack.AddClipInfo(name=clip.name, posStart=myPosStart, posDuration=clip.duration().value, posEnd=clip.range_in_parent().end_time_exclusive().value,
                        mediaStart=clip.visible_range().start_time.value, mediaDuration=clip.duration().value, mediaEnd=clip.visible_range().end_time_exclusive().value, url=filepath, speed=mediaspeed
                        )





                        #op("track1data").appendRow([clip.range_in_parent().start_time.value, clip.duration().value, clip.name])
                        #self.op("track1data").append([clip.range_in_parent().start_time.value, clip.range_in_parent().end_time_exclusive().value, clip.name])



                elif isinstance(item, otio.schema.Gap):
                    continue			
            track_n+=1




