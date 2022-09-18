import os
from getpass_asterisk.getpass_asterisk import getpass_asterisk

passcode = "021900"  # Specify Passcode here

value = str(getpass_asterisk("Enter Passcode : "))
if value == passcode:
    os.startfile(r'D:\MagicianPerf5003325')  # Enter Folder Path in 'here'
else:
    print("Access Denied")
    exit(0)
