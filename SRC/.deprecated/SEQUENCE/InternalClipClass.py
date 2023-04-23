import os
import re
import sys

class InternalClass:

    def __init__( self, myname ):
        print ("Clip {} init".format(op.Seqi.op(myname).digits))
     
        self.myopRef=myname
        self.prevTimerStatus=0
        return

    def Reset (self):
        return 

    def OnTimerActiveChange (self, v):
        if v==1:
            self.OnTimerStart()
        elif v==0:
            self.OnTimerStop()
        
        self.prevTimerStatus=v
    def OnTimerStart(self):
        # print (self.myopRef.outputConnectors[0])
        # print (self.myopRef.parent().op("INPUT1"))
        self.myopRef.op("EveryFrameJob").par.active=True
        i1=self.myopRef.parent().op("INPUT1")
        i2=self.myopRef.parent().op("INPUT2")
        _i=None
        if len(i1.inputs) == 0:
            _i=i1
        elif len(i2.inputs)==0:
            _i=i2
        else: 
            _i=i1

        self.myopRef.outputConnectors[0].connect(_i)
        if self.myopRef.par.Mode.menuIndex!=2 and bool(self.myopRef.par.Exportprivateparsonstart):
            #op.BasicReader.par.Mode=self.myopRef.par.Mode
            self.OnFX1Change(bool(self.myopRef.par.Fx1))
            self.OnFX1Change(bool(self.myopRef.par.Fx1))
            self.OnFxccChange(bool(self.myopRef.par.Fxcc))
            self.OnFxfeedback(bool(self.myopRef.par.Fxfeedback))
            self.OnFXsceneRotator(bool(self.myopRef.par.Fxscenerot))


        
        # print ("Set to 1 basicreader")
        
        return 
    def OnTimerStop(self):
        self.myopRef.op("EveryFrameJob").par.active=False
        self.myopRef.outputConnectors[0].disconnect()
        return 
    def OpenParamsOnClick(self):
        self.myopRef.openParameters()

    def OnFX1Change(self, val):
        if op.GlobalFX1.GetActive() is not bool(val):
            op.GlobalFX1.EffectCtrl(bool(val))        
    def OnFxccChange (self, val):
        # GlobalFXcc
        if bool(val) is True:
            for mypar in op.Seqi.GetCCPars():
                v=getattr(self.myopRef.par, mypar)
                setattr(op.GlobalFXcc.par, mypar, v)
        else:
            mypar='Fxcc'
            v=getattr(self.myopRef.par, mypar)
            setattr(op.GlobalFXcc.par, mypar, v)
    def OnFxfeedback(self, val):
        if bool(val) is True:
            for mypar in op.Seqi.GetFeedbackPars():
                v=getattr(self.myopRef.par, mypar)
                setattr(op.GlobalFXfeedback.par, mypar, v)
        else:
            mypar='Fxfeedback'
            v=getattr(self.myopRef.par, mypar)
            setattr(op.GlobalFXfeedback.par, mypar, v)

    def OnFXsceneRotator(self, val):
        if bool(val) is True:
            for mypar in op.Seqi.GetScenerotPars():
                self.checkAndSetPar("GlobalFXsceneRotator", mypar, "")
        else:
            self.checkAndSetPar("GlobalFXsceneRotator", "Fxscenerot", "", isAutoCopy=False)
        #     mypar='Fxscenerot'
        #     v=getattr(self.myopRef.par, mypar)
        #     setattr(op.GlobalFXsceneRotator.par, mypar, v)
    def checkAndSetPar(self, fxrefname, myparname, value, isAutoCopy=True):
        fxcomp=getattr(op, fxrefname)
        if hasattr(self.myopRef.par, myparname):
            if isAutoCopy:
                value=getattr(self.myopRef.par, myparname)
            if hasattr(fxcomp, 'par'):
                if hasattr(fxcomp.par, myparname):
                    setattr(fxcomp.par, myparname, value)
                

                        
    def GetImageSequenceFrame(self, myframe):
        # 'Z:/Gagarin360/Dev/Intermediate/.vidsource.EQRT_AP/'+"FRAME{:05d}.dds".format(int(op('getLocalTimeAndStatus/timer_frames')['timer_frames']*op('par3')['Speed']))
        return str(self.myopRef.par.Imagesequencepath+self.myopRef.par.Filemask).format(int(myframe))