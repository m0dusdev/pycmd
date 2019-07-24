import subprocess
import os

def sh(input):
	c = Command(input)
	c.run()
	return Command(input)

	
def update(distro=""):
	if(distro == "deb"):
		update = Command("sudo apt-get update && sudo apt-get upgrade")
		update.run()		
		msg = Command("echo Done Updating")
		msg.run()
	if(distro == ""):
		sh("echo oops")
	


def ls(arg=""):
	if arg == "":
		sh("ls")
	else:
		sh("ls " + arg)

def echo(arg=""):
	sh("echo " + repr(arg))

def clear():	
	sh("clear")





class Command:

	def __init__(self, value):
		self.value = value	
	
	def pipe(self, after):
		text = subprocess.call(self.value + "|" + after, shell=True)
		print(text)

	def run(self):
		text = subprocess.call(self.value, shell=True)
		print('\n')
		return text	
	
