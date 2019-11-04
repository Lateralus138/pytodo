#!/usr/bin/env python3
import os, sys

# FUNCTIONS
def _check_create(fileOrDir,type):
    """Create directory or file if it doesn't exist."""
    def printerr():
        print('Could not create ' 
            + fileOrDir + '\nIt\'s ' 
            + 'possible you do not have ' 
            + 'the correct permissions.\n')
    def printsuccess():
        print(fileOrDir + ' was created successfully.\n')
    def printattempt():
        print('Attempting to create ' + fileOrDir)
    if type.lower() == 'dir' or type.lower() == 'directory':
        if not os.path.isdir(fileOrDir):
                try:
                    printattempt()
                    os.mkdir(fileOrDir)
                except:
                    printerr()
                    return
                else:
                    printsuccess()
                    return True
    if type.lower() == 'file':
        if not os.path.isfile(fileOrDir):
                try:
                    printattempt()
                    mkfile(fileOrDir)
                    # os.mknod(fileOrDir)
                except:
                    printerr()
                    return
                else:
                    printsuccess()
                    return True

def os_platform():
    platforms = {
        'linux1' : 'Linux',
        'linux2' : 'Linux',
        'darwin' : 'OS X',
        'win32' : 'Windows'
    }
    if sys.platform not in platforms:
        return sys.platform
    return platforms[sys.platform]

def mkfile(file):
    with open(file, 'a'):
        os.utime(file, None)

# Enable logging
import logging
log = logging.getLogger('root')
FORMAT = "File: %(filename)s" \
            + '\n' + "Line: %(lineno)s" \
            + '\n' + "Function: %(funcName)20s()" \
            + '\n' + "Message: %(message)s"
logging.basicConfig(format=FORMAT)
log.setLevel(logging.DEBUG)
# End Enable logging

# VARS

# CONSTANTS
OS_TYPE = os_platform()
if OS_TYPE in ['linux1','linux2','linux','Linux']:
    OS_TYPE = 'Linux'
elif OS_TYPE in ['Darwin','OS X']:
    OS_TYPE = 'Mac'
elif OS_TYPE in ['win32','Windows']:
    OS_TYPE = 'Windows'
else:
    exit
if OS_TYPE == 'Linux' or OS_TYPE == 'Mac':
    HOME = os.environ['HOME']
else:
    HOME = os.environ['USERPROFILE']
PYTODO_HOME = HOME + '/.pytodo'
PYTODO_LIST = PYTODO_HOME + '/pytodo.todo'
PYTODO_HOME = PYTODO_HOME.replace('\\','/')
PYTODO_LIST = PYTODO_LIST.replace('\\','/')

# GLOBALS
log.debug('\nOperating System: ' + OS_TYPE 
    + '\nPython Home: ' + PYTODO_HOME 
    + '\nPython List: ' + PYTODO_LIST + '\n')

## Check for a good environment
_check_create(PYTODO_HOME,'directory')

## Check for the list
_check_create(PYTODO_LIST,'file')

	