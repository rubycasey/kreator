
"""
         _  __               _             
        | |/ /              | |            
        | ' / _ __ ___  __ _| |_ ___  _ __ 
        |  < | '__/ _ \/ _` | __/ _ \| '__|
        | . \| | |  __/ (_| | || (_) | |   
        |_|\_\_|  \___|\__,_|\__\___/|_|   

    This is the new version of Kreator, now written in python!
  Feel free to customize and play with it to your heart's content.
"""
# Importing modules
import os
import sys

# Importing configs
from config.xbps import xbpsPackageList
from config.arch import pacmanPackageList

# Importing scripts
from packages import installPackages, installAurPackage, changeDirToHome
from configs import cfg_i3Gruvbox
from themes import thm_gruvboxDark
versionNum = "v0.2.2"

# Startup
#os.system(clear)
print('Welcome to Kreator %s!'%versionNum)
print('Please select a mode from the options below.')
print('1) Install Packages')
print('2) Install Configs')
print('3) Install Themes')
kreatorMode = int(input("Selection: "))
print('===========')

# Controller
if kreatorMode == 1:
  print("Please select your package manager from the list below.")
  print("1) Apt")
  print("2) Pacman")
  print("3) XBPS")
  packageManagerMode = int(input("Selection: "))
  
  if packageManagerMode == 1:
    print("Apt not yet supported.")
    print('===========')
  elif packageManagerMode == 2:
    print("Pacman selected, you may be required to enter your password.")
    print('===========')
    blankInput = input('Press enter to continue...')
    installPackages("pacman")
  elif packageManagerMode == 3:
    print("XBPS selected, you may be required to enter your password.")
    print('===========')
    blankInput = input('Press enter to continue...')
    installPackages("xbps")
  else:
    print('===========')
    print("Invalid package manager.")
elif kreatorMode == 2:
  print("Please choose a config from the list below.")
  print("1) Ruby's i3 Gruxbox")
  configSelection = int(input("Selection: "))
  print('===========')
  if configSelection == 1:
    cfg_i3Gruvbox()
elif kreatorMode == 3:
  print("Please choose a config from the list below.")
  print("1) Gruvbox Dark")
  configSelection = int(input("Selection: "))
  print('===========')
  if configSelection == 1:
    thm_gruvboxDark()
elif kreatorMode == 4:
  # I'm using option 4 as a hidden debug menu thingy, for when
  # I'm testing things and don't want to go through thr whole
  # prompt.
  blankInput = input("Debug mode entered, press enter to continue...")
else:
  print("Invalid option selected.")

print('===========')
print("Thanks for using Kreator!")

# Debugging/Testing
#print (xbpsPackageList[1])
#print(os.getcwd())

# vvvv Yo its like 4 am rn but this shit actually works I'm learning this is great
#os.system('echo "Installing %s."'%(xbpsPackageList))
#installPackages("xbps")