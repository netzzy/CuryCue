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
        
        if v != self.prevTimerStatus:
            if v==1:
                self.OnTimerStart()
            elif v==0:
                self.OnTimerStop()
        
        self.prevTimerStatus=v
    def OnTimerStart(self):
        if self.myopRef.par.Mode.menuIndex!=2 and bool(self.myopRef.par.Exportprivateparsonstart):
            op.BasicReader.par.Mode=self.myopRef.par.Mode
        if bool(self.myopRef.par.Exportprivateparsonstart):
            print ("HERE")
            self.OnFX1Change(bool(self.myopRef.par.Fx1))
            self.OnFxccChange(bool(self.myopRef.par.Fxcc))
            self.OnFxfeedback(bool(self.myopRef.par.Fxfeedback))
            self.OnFXsceneRotator(bool(self.myopRef.par.Fxscenerot))
            self.SetFX3DRotator(True)
        # print (bool(self.myopRef.par.Fx1))
        # print ("Set to 1 basicreader")
        # print (self.myopRef.outputConnectors[0])
        # print (self.myopRef.parent().op("INPUT1"))
 #       self.myopRef.outputConnectors[0].connect(self.myopRef.parent().op("INPUT1"))
        return 
    def OnTimerStop(self):
       # self.SetFX3DRotator(False)
        # op.BasicReader.par.Mode=1
#        self.myopRef.outputConnectors[0].disconnect()
        return 
    def OpenParamsOnClick(self):
        self.myopRef.openParameters()        
    def SetFX3DRotator (self, action):
        for mypar in op.Seqi.GetEquiRotatorPars():
            if action:
                self.checkAndSetPar("BasicReader", mypar, "")
            else:
                self.checkAndSetPar("BasicReader", mypar, "0.0", isAutoCopy=False)

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
        # else:
        #     self.checkAndSetPar("GlobalFXsceneRotator", "Fxscenerot", "", isAutoCopy=False)
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
                

            