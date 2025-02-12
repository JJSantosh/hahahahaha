import os
sd=print("Shutdown computer (Y/N):")

if sd=="N":
 exit()
else:
  os.system("shutdowm /s /t 1")