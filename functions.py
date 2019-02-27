import subprocess
import subproc_custom
from halo import Halo
from config import *

class func_Globals:
    log = ()


cmd = config_Globals.cmd
services = config_Globals.services

#https://stackoverflow.com/questions/33239308/how-to-get-exception-message-in-python-properly/33239954
def make_process(command):
    try:
        haloload = Halo(text=config_Globals.load['text'], spinner=config_Globals.load['spinner'])
        haloload.start()
        subprocess.Popen(command.split(), stdout=subprocess.PIPE)
        func_Globals.log = str(subproc_custom.Popen(command.split(), stdout=subprocess.PIPE).communicate(), encoding='utf-8')
        haloload.stop()

    except Exception as e:
        print('Execution failed')
        if hasattr(e, 'message'):
            print(e.message)
        else:
            print(e)


def status(service_param):
    make_process("service "+service_param+" status")
    if 'inactive' in func_Globals.log:
        return service_param+': Inactive'
    elif 'Active' in func_Globals.log:
        return service_param+': Active'
    else:
        return service_param+': Error'


def start(service_param):
    make_process("service "+service_param+" start")


def reload(service_param):
    make_process("service "+service_param+" reload")


def stop(service_param):
    make_process("service "+service_param+" stop")
