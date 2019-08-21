import subprocess
import os
import _thread



user = subprocess.check_output("echo $USER", shell=True)
hostname = subprocess.check_output("cat /etc/hostname", shell=True)


def sh(input):
	c = Command(input)
	c.run()
	return c #Command(input)

def newThread(input):
	_thread.start_new_thread(sh , (input, ))
	return
# ADD RETURN sh to all functions 
#GET THREADING TO WORK WITH .pipe etc
# ADD GLOBAL VARS THAT CONTAIN SYSTEM FACTS , hostname , ip , username , time , date , kernal version echo(username)
def forloop(times, arg):
	for x in range(times):
		sh(arg)
	
	
def update(distro=""):
	if(distro == "debian"):
		sh("sudo apt-get update && sudo apt-get upgrade")
	if(distro == "redhat"):
		sh("sudo dnf update")
	if(distro == "arch"):
		sh("sudo pacman -Syu")
	#if(distro == ""):

	#if(distro == ""):

	#if(distro == ""):

def ssh(username,hostname):
	sh("ssh " + username + "@" + hostname)


#for i in range(0, 300):
	#createvenv("env" + repr(i))


#qemu helpers

def vmC():
	sh("virsh")

def vmEdit(arg=""):
	if(arg == ""):
		return sh("echo Please provide a vm XML configuration file to edit")
	else:
		return sh("virsh edit " + arg)
def vmSetUserPassword(domain, user, password):
		sh("virsh set-user-password " + domain + " " + user + " " + password)

def vmStats():
	return sh("virsh cpu-stats")

def vmList():
	return sh("virsh list")

def vmDestroy(arg=""):
	if(arg == ""):
		sh("echo Please provide a vm to destroy (Shutdown)")
	else:
		sh("virsh destroy " + arg)
######





def venvCreate(arg=""):
	sh("python3 -m venv " + arg)
	sh("echo Created Virtual environment " + arg + "")

def newVenv(arg=""):
	if(arg == ""):
                sh("echo Please Supply a name for the virtual environment") 
	else:    
		_thread.start_new_thread( venvCreate, (arg, ))

def setupPip():
	sh("sudo python -m pip install --upgrade pip setuptools wheel")

def updatePip():
	sh("sudo pip install --upgrade pip")

def pipGet(arg):
	sh("sudo pip install " + arg)

def makefunc(cmd):
     print("def "+ cmd.replace(' ', '') + "():\n" + "\tsh(" +  cmd + ")")

def ls(arg=""):
	if arg == "":
		return sh("ls")
	else:
		return sh("ls " + arg)

def cat(arg):
	return sh("cat " + arg)

def echo(arg=""):
	return sh("echo " + repr(arg))

def clear():	
	sh("clear")

def grep(arg):
	return sh("grep " + arg)

def mkdir(arg):
	sh("mkdir "+ arg)

def rm(arg):
	sh("rm " + arg)

def touch(arg):
	sh("touch " + arg)


def help():
	print("")

def date():
	return sh("date")

def shutdown():
	sh("sudo shutdown -h now")

def reboot():
	sh("reboot")

def startx():
	sh("startx")
	
def terminal(arg=""):
		if(arg==""):
			sh("lxterminal")
		else: 
			sh("lxterminal -e " + arg)
	 

class Command:

	def __init__(self, value):
		self.value = value	
	
	def getOutput(self):
		output = repr(subprocess.check_output(self.value, shell=True)).replace("\\n", " ")
		return output

	def pipe(self, after):
		text = subprocess.call(self.value + "|" + after, shell=True)
		print(text)
	
	def tofile(self):
		text = subprocess.check_output(self.value, shell=True)
		cleaned = repr(text).replace("\\n", " ")
		sh("touch " + repr(self.value).replace("-"," ") + ".output")
		sh("echo " + cleaned  + " >> " + self.value + ".output")
		
	
	def less(self):
		text = subprocess.call(self.value + " | less", shell=True)
	
	def more(self):
		text = subprocess.call(self.value + " | more", shell=True)
	

	def run(self):
        	text = subprocess.call(self.value, shell=True)
        	return text
	
	
	
#SETUP 
clear()

"""
def shell():
	from pycmd import *
    	while(True):
        	f = input("pycmd shell>")
       	 	if(f == "exit"):
             		return sh("clear")
	 	else:
     	     		sh(f)
"""
