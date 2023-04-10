import os,platform
os.system('pip uninstall requests')
os.system('pip install requests')
x=platform.architecture()[0]
if x =="64bit":
     from mail import gmail
else:
     print("Your System doesn't support ")
