import os
import shutil
import winreg

path = 'C:{0}RAT_DELETE_ME'.format(os.path.sep)
try:
    shutil.rmtree(path)
except FileNotFoundError:
    pass
try:
    run = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run', 0, winreg.KEY_WRITE)
    winreg.DeleteKeyEx(run, "JRAT")
except FileNotFoundError:
    pass
os.system('shutdown /l')
