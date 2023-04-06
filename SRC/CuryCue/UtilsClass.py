#import mysql.connector
import urllib
import sys
import re
import os
from collections import namedtuple
from dataclasses import dataclass
from typing import Any


class UtilsClass:
        def __init__(self):
                pass

        def SetOwnerPar(self, mypar, myvalue):
                if hasattr(self.ownerComp, "par"):
                        if hasattr(self.ownerComp.par, mypar):
                                setattr(self.ownerComp.par, mypar, myvalue)
        def GetOwnerPar(self, mypar):
                pass

        def CheckParentCooking(self, myOp):
            allowCooking=True
            i=0
            while myOp.parent(i) is not None:
                if not myOp.parent(i).allowCooking:
                    allowCooking=False
                    break
                i+=1
            return allowCooking




class IOP:
    def __init__(self, owner):
        self.owner = owner

    def __getattr__(self, name):
        return self.i(name)

    def i(self, v):
        return getattr(self.owner.ownerComp.op("iopLocate").iop, v)


class IPAR:
    def __init__(self, owner):
        self.owner = owner

    def __getattr__(self, name):
        return self.i(name)

    def i(self, v):
        return getattr(self.owner.ownerComp.op("iopLocate").ipar, v)
class IKEY:
    def __init__(self, owner):
        self.owner = owner

    def __getattr__(self, name):
        # def wrapper(*args, **kwargs):
        #	print ("'%s' was called" % name)

        return self.owner.keysDict.get(name, self.owner.KeyAndState(name, False, False))
