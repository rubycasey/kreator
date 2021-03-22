
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
def importBase():
  # Importing libaries
  import os
  import sys

  # Importing configs
  from config.xbps import xbpsPackageList
  from config.arch import pacmanPackageList

# Importing base components
importBase();
from packages import installPackages
versionNum = "v0.2.0";

# Startup
#os.system(clear)
print('Welcome to Kreator %s!'%versionNum);
print('Please select a mode from the options below.');
print('1) Install Packages');
print('2) Install Configs');
print('3) Install Themes');
kreatorMode = input("Selection: ");
print('===========')

# Controller
if kreatorMode == "1":
  print("Please select your package manager from the list below.")
  print("1) Apt")
  print("2) Pacman")
  print("3) XBPS")
  packageManagerMode = input("Selection: ")
  
  if packageManagerMode == "1":
    print("Apt not yet supported.")
    print('===========')
  elif packageManagerMode == "2":
    print("Pacman not yet supported.")
    print('===========')
  elif packageManagerMode == "3":
    print("XBPS selected, you may be required to enter your password.")
    print('===========')
    blankInput = input('Press enter to continue...')
    installPackages("xbps")
  else:
    print('===========')
    print("Invalid package manager.")
elif kreatorMode == "2":
  print("Not available at the moment.")
elif kreatorMode == "3":
  print("Not available at the moment.")
else:
  print("Invalid option selected.")

print('===========')
print("Thanks for using Kreator!")

# Debugging/Testing
#print (xbpsPackageList[1]);
#print(os.getcwd());

# vvvv Yo its like 4 am rn but this shit actually works I'm learning this is great
#os.system('echo "Installing %s."'%(xbpsPackageList))
#installPackages("xbps")