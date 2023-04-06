import os
from subprocess import *
import math
import re
class adbCameraClass:

	def __init__( self, ownerComp ):
		self.ownerComp=ownerComp
		print (ownerComp)
		return
	def Exec(self, command, communicate=True, printcommand=True):
		if printcommand:
			print (" ".join(command))
		p=Popen(command,
                     stdout=PIPE, stderr=PIPE, shell=True)

		if communicate:
			stdout, stderr = p.communicate()

			print ("STDERR: {}\n{}".format(stderr.decode() if len(stderr.decode())>0 else "NO", stdout.decode()))
			
			res= [stdout.decode(), stderr.decode()  ]
			return res
		else:
			return
	def Reboot(self):
		mylongcmd="reboot"
		allcommand=[self.adbPath, "-s", self.connectAddress] + re.split(r' ', mylongcmd)
		self.Exec(allcommand, printcommand=False)		

	def Anydeskconfig(self):
		mylongcmd="shell appops set com.anydesk.anydeskandroid PROJECT_MEDIA allow"
		allcommand=[self.adbPath, "-s", self.connectAddress] + re.split(r' ', mylongcmd)
		self.Exec(allcommand, printcommand=False)		
	def Updatefocusapp(self):
		
		mylongcmd="shell"
		allcommand=[self.adbPath, "-s", self.connectAddress] + re.split(r' ', mylongcmd) + ["dumpsys window | grep mFocusedApp=ActivityRecord"]
		(answer, sterr)=self.Exec(allcommand, printcommand=True)
		answer=answer.replace("  mFocusedApp=ActivityRecord", "")
		self.ownerComp.par.Focusapp=str(answer)

		mylongcmd="shell"
		allcommand=[self.adbPath, "-s", self.connectAddress] + re.split(r' ', mylongcmd) + ["dumpsys power | grep \"Display Power: state=\""]
		(answer, sterr)=self.Exec(allcommand, printcommand=True)
		
		self.ownerComp.par.Displaystatus=str(answer)

		pass
		
	def Scrcpy(self):
		command=[self.scrcpyPath, "-s", self.connectAddress]
		self.Exec(command, communicate=False)
		pass
	def Openndi(self):
		mylongcmd="shell monkey -p com.newtek.ndi.hxcam 1"
		allcommand=[self.adbPath, "-s", self.connectAddress] + re.split(r' ', mylongcmd)
		self.Exec(allcommand, printcommand=False)
	def Closendi(self):
		mylongcmd="shell am force-stop com.newtek.ndi.hxcam"
		allcommand=[self.adbPath, "-s", self.connectAddress] + re.split(r' ', mylongcmd)
		self.Exec(allcommand)



	def Openndi2(self):
		mylongcmd="shell monkey -p com.dev47apps.ndicamera 1"
		allcommand=[self.adbPath, "-s", self.connectAddress] + re.split(r' ', mylongcmd)
		self.Exec(allcommand, printcommand=False)
	def Closendi2(self):
		mylongcmd="shell am force-stop com.dev47apps.ndicamera"
		allcommand=[self.adbPath, "-s", self.connectAddress] + re.split(r' ', mylongcmd)
		self.Exec(allcommand)



	def Powerbutton (self):
		
		mylongcmd="shell input keyevent KEYCODE_POWER"
		allcommand=[self.adbPath, "-s", self.connectAddress] + re.split(r' ', mylongcmd)
		self.Exec(allcommand)


	def Home (self):
		mylongcmd="shell am start -W -c android.intent.category.HOME -a android.intent.action.MAIN"
		allcommand=[self.adbPath, "-s", self.connectAddress] + re.split(r' ', mylongcmd)
		self.Exec(allcommand)

	def Disconnect(self):
		command=[self.adbPath, "-s", self.connectAddress, "disconnect"]
		self.Exec(command)

	def Connect(self):
		command=[self.adbPath, "connect", self.connectAddress]
		self.Exec(command)

	def Check(self):
		command=[self.adbPath, "-s", self.connectAddress, "shell", "dumpsys", "battery"]
		self.Exec(command)


	def Pair(self):
		pairAddress="{}:{}".format(self.LivecamerasIP[int(self.Device)], self.Pairport)
		command=[self.adbPath, "pair", pairAddress, str(self.Code)]
		self.Exec(command)
	
	def Cam1par(self):
		op.cam.op("ndiin1").openParameters()
		pass
	def Cam2par(self):
		op.cam.op("ndiin2").openParameters()
		pass
	def Camvcam(self):
		op.cam.op("videodevin2").openParameters()
		pass	
	def __del__(self):
		pass
		
	@property
	def LivecamerasIP(self):
		return [self.ownerComp.par.Livecamera1, self.ownerComp.par.Livecamera2]
	@property
	def _adb_path(self):
		return self.ownerComp.par.Adb
	@property
	def Device(self):
		return self.ownerComp.par.Device
	@property
	def Pairport(self):
		return self.ownerComp.par.Pairport
	@property
	def Code(self):
		return self.ownerComp.par.Code
	@property
	def Connectport(self):
		return [self.ownerComp.par.Connectport1, self.ownerComp.par.Connectport2]
	@property
	def adbPath(self):
		return "{}/{}".format(project.folder, self._adb_path)
	@property
	def scrcpyPath(self):
		adb=self.adbPath
		adb=adb.replace("adb.exe", "scrcpy.exe")
		return adb
	@property
	def connectAddress(self):
		return "{}:{}".format(self.LivecamerasIP[int(self.Device)], self.Connectport[int(self.Device)])