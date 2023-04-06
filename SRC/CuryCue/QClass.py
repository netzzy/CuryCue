
from dataclasses import dataclass
from re import I
from typing import Any
import time
from queue import Queue
from random import randint

# CreateEvaluator (qtask)
# UpdateEveryFrame ()
# Forcestop ()

class QClass:
    class FadeEvaluator:
        def __init__(self, name, task, qtime, isDelayEvaluator=False):
            self.name = name
            self.task = task
            self.qtime = qtime
            self.isComplete=False
            self.isDelayEvaluator=isDelayEvaluator
            if isDelayEvaluator:
                self.fadeOrDelayTime=self.task.delay
            else:
                self.fadeOrDelayTime=self.task.fade
        def eval(self):
            
            currentProgress=float(tdu.clamp(self.getProgress(), 0, 1))

            self.task.progress=currentProgress

            if currentProgress >=1:
                self.isComplete=True
                # self.task.running=0

            if not self.isDelayEvaluator:
                sortForClamp=sorted([self.task.value_start, self.task.value_target])
                newV=self.lerp(self.task.value_start, self.task.value_target, currentProgress)
                self.task.value=tdu.clamp(newV, sortForClamp[0], sortForClamp[1])
            return self.task.value
        def getProgress(self):
            return 1 if self.fadeOrDelayTime==0 else (self.qtime.second-self.qtime.starttime)/(self.fadeOrDelayTime) 
        def lerp(self, a, b, t):
            return a + (b-a) * t



    @dataclass
    class Qtask:
        callback: Any
        callback_complete: Any
        name: str = ""
        full_par_path: str = ""
        value: float = None
        value_text:str=""
        value_start: float =0
        value_target: float=0
         
        fade: float = 1
        delay: float = 0
        progress: float =0
        

        running: int = 1
    @dataclass
    class Qtime:
        second:float=0
        starttime:float=0


    def __init__(self, ownerComp):
        self.ownerComp = ownerComp
        print ("Q init")
        self.evaluators=[]
        self.evaluatorsByPath=dict()
        pass

    def CreateEvaluator(self, qtask):
        if qtask.delay>0:
            self.evaluators.append(self.FadeEvaluator (qtask.name, qtask, self.Qtime(second=absTime.seconds, starttime=absTime.seconds), isDelayEvaluator=True))
        else:
            self.evaluators.append(self.FadeEvaluator (qtask.name, qtask, self.Qtime(second=absTime.seconds, starttime=absTime.seconds)))
        self._indexEvaluatorsListToDict()


    def UpdateEveryFrame(self):
        for myEvaluator in self.evaluators:
            myEvaluator.qtime.second=absTime.seconds
            myEvaluator.eval()
            if not myEvaluator.isDelayEvaluator:
                myEvaluator.task.callback(myEvaluator.task)
            if myEvaluator.isComplete:
                if not myEvaluator.isDelayEvaluator:
                    self.evaluators.remove(myEvaluator)
                    myEvaluator.task.callback_complete(myEvaluator.task)
                else:
                    # print ("Завершаем delay и запускаем fade для {} ".format(myEvaluator.name))
                    self.evaluators.append(self.FadeEvaluator (myEvaluator.task.name, myEvaluator.task, self.Qtime(second=absTime.seconds, starttime=absTime.seconds)))
                    self.evaluators.remove(myEvaluator)
                self._indexEvaluatorsListToDict()
            
        # self.CleanEvaluators()
        
    # def CleanEvaluators(self):
    #     for i in range (0, len(self.evaluators)):
    #         print ("ALIVE: {}".format(self.evaluators[i].task.running))
    def Forcestop(self):
        for myEvaluator in self.evaluators:
            myEvaluator.isComplete=True

    # вызывается из RunCue
    def StopByPathIndex(self, full_par_path):
        if full_par_path in self.evaluatorsByPath.keys():
            self.evaluatorsByPath[full_par_path].isComplete=True
        pass
    
    def _indexEvaluatorsListToDict(self):
        paths=[]
        i=0
        for myEvaluator in self.evaluators:
            paths.append(myEvaluator.task.full_par_path)
        self.evaluatorsByPath=dict(zip(paths, self.evaluators))
