import os
import re
import sys

class InternalClass:

    def __init__( self, myname ):
        print ("Track {} init".format(op.Seqi.op(myname).digits))
        self.trackdata=[]
        self.myopRef=op.Seqi.op(myname)
        self.optrack=op.Seqi.op(myname).op("trackdata")
        return

    def Reset (self):
        self.trackdata=[]
        self.optrack.clear()
        self.optrack.appendRow(["begin", "length", "posEnd", "mediaStart", "mediaDuration", "mediaEnd", "name", "filename", "mediaspeed"])
        return 

    def ReplicatorRecreate(self):
        self.myopRef.op("replicator1").par.recreateall.pulse()

    def AddClipInfo(self, name="", posStart=0, posDuration=0, posEnd=0, mediaStart=0, mediaDuration=0, mediaEnd=0, url="", speed=1):
        print (posStart)
        self.optrack.appendRow([posStart, posDuration, posEnd, mediaStart, mediaDuration, mediaEnd, name, url, speed])
        

    def OpenTrackData(self):
        self.myopRef.op("trackdata").openViewer()
    def ApplyMode (self):
        for n in range(1,self.myopRef.op("trackdata").numRows):
            trackdata=self.myopRef.op("trackdata")
            clipOp=self.myopRef.op("clip"+str(int(n)))
            clipOp.par.Mode.val=self.myopRef.par.Mode.val
