import time, os
import subprocess
import subproc_custom
from halo import Halo
from termcolor import colored
from config import *

class func_Globals:
    log = ()

cmd = config_Globals.cmd
services = config_Globals.services
text = config_Globals.load['text']
spinner = config_Globals.load['spinner']

#https://stackoverflow.com/questions/33239308/how-to-get-exception-message-in-python-properly/33239954
def make_process(command, status=""):
    try:
        with Halo(text=text, spinner=spinner):
            subprocess.Popen(command.split(), stdout=subprocess.PIPE)
            func_Globals.log = str(subproc_custom.Popen(command.split(), stdout=subprocess.PIPE).communicate(), encoding='utf-8')

    except Exception as e:
        print('Execution failed')
        if hasattr(e, 'message'):
            print("\n"+e.message)
        else:
            print("\n"+e)


def status(service_param):
    make_process("service "+service_param+" status")
    if 'inactive' in func_Globals.log:
        return colored('Inactive', 'yellow', attrs=['bold'])
    elif 'Active' in func_Globals.log:
        return colored('Active', 'green', attrs=['bold'])
    else:
        return colored('Error', 'red', attrs=['bold', 'blink'])


def start(service_param):
    make_process("service "+service_param+" start")


def reload(service_param):
    make_process("service "+service_param+" reload")


def stop(service_param):
    make_process("service "+service_param+" stop")

def show_log(service_param):
    os.system('clear')
    print("\n")
    print("Latest log:\n")
    make_process("service "+service_param+" status")
    print(func_Globals.log)
    print("\n")
    log_option = input("\n\nPress: "
                       "\nd for detailed system log "
                       "\nor anything else to go back : ")

    if log_option == 'd':
        if service_param == 'nginx':
            os.system('clear')
            print("\n")
            make_process("cat "+config_Globals.logs['nginx-access'])
            nginx_option = input("\n\nPress: "
                                 "\nd to show error logs, otherwise "
                                 "\n press anything else to go back : ")
            if nginx_option == 'd':
                os.system('clear')
                print("\n")
                make_process("cat "+config_Globals.logs['nginx-error'])
                print("\n")
                input("Press enter to continue...")
            else:
                return

        elif service_param == 'mysql':
            os.system('clear')
            print("\n")
            make_process("cat " + config_Globals.logs['mysql-error'])
            print("\n")
            input("Press enter to continue...")

        elif service_param == 'php7.2-fpm':
            print("\nThe log files are yet to be configured!\n")
            print("\n")
            input("Press enter to continue...")

def load(sleep_param):
    with Halo(text='Loading', spinner='dots'):
        time.sleep(sleep_param)

