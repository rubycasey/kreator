# Imports
#from kreator import importBase
#importBase()
# Importing libaries
import os
import sys

# Importing configs
from config.xbps import xbpsPackageList
from config.arch import pacmanPackageList

# Scripts for installing packages.
def installPackages(packageManager):
    packageList = "";
    if packageManager == "xbps":
        print("Set to install the following: %s."%(xbpsPackageList));
        for x in range(len(xbpsPackageList)):
            if packageList == "":
                packageList = xbpsPackageList[0]
            else:
                packageList = packageList + " " + xbpsPackageList[x]
        os.system('sudo xbps-install -Sy %s'%(packageList))
        
        # This is deprecated, but will work if multiple packages in one command won't.
        #for x in xbpsPackageList:
        #    os.system('sudo xbps-install -Sy %s'%(x))
    elif packageManager == "pacman":
        print("Pacman chosen, but not yet supported.");
    elif packageManager == "apt":
        print("Apt chosen, but not yet supported.");
    else:
        print("Invalid package manager chosen.")