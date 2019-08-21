from pycmd import *
import _thread

def createThread(arg):
	_thread.start_new_thread(sh , (arg, ))
