# Importing modules
import os
import sys

# Importing configs
from config.xbps import xbpsPackageList
from config.arch import pacmanPackageList, aurPackageList

# Directory Utility
def changeDirToHome():
    os.chdir(os.path.expanduser("~"))

def aurDirSetup():
    # Setting up folder structure
    changeDirToHome()
    if os.path.isdir(".git"):
        print("'.git' directory already exists, moving on.")
    else: 
        print("Creating '.git' directory")
        os.mkdir(".git")
    os.chdir(".git")
    if os.path.isdir("aur"):
        print("'aur' directory already exists, moving on.")
    else:
        print("Creating 'aur' directory")
        os.mkdir("aur")
    os.chdir("aur")
    print("debug: current dir:", os.getcwd())

# Scripts for installing packages.
def installPackages(packageManager):
    packageList = ""
    if packageManager == "xbps":
        print("Set to install the following: %s."%(xbpsPackageList))
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
        # Arch repos.
        print("Set to install the following: %s."%(pacmanPackageList))
        for x in range(len(pacmanPackageList)):
            if packageList == "":
                packageList = pacmanPackageList[0]
            else:
                packageList = packageList + " " + pacmanPackageList[x]
        os.system('sudo pacman -S --noconfirm %s'%(packageList))
        print('===========')
        # Oh boy, this one's gonna get messy. So this is some spaghetti ass shit to choose
        # aur helpers, and go through every individual aur package and build it manually if
        # no aur helper is chosen.
        print("Would you like to install AUR packages? (this may be time consuming)")
        print("1) Yes.")
        print("2) No.")
        aurToggle = int(input("Selection: "))
        if aurToggle == 1:
            print("Would you like to use an AUR helper?")
            print("1) Yes.")
            print("2) No.")
            aurHelperToggle = int(input("Selection: "))
            if aurHelperToggle == 1:
                print("Select an AUR helper below.")
                print("1) Yay")
                print("2) Cancel Helper Selection")
                aurHelper = int(input("Selection: "))
                if aurHelper == 1:
                    packageList = ""
                    installAurPackage("yay")
                    changeDirToHome()
                    print("Set to install the following: %s."%(aurPackageList))
                    for x in range(len(aurPackageList)):
                        if packageList == "":
                            packageList = aurPackageList[0]
                        else:
                            packageList = packageList + " " + aurPackageList[x]
                    os.system('yay -S --noconfirm %s'%(packageList))
                else:
                    print("Moving on without Arch Helper.")
            else:
                print("Skipping AUR helper.")
                for x in aurPackageList:
                    installAurPackage(x)
        else:
            print("Skipping AUR packages.")
    elif packageManager == "apt":
        print("Apt chosen, but not yet supported.")
    else:
        print("Invalid package manager chosen.")

def installAurPackage(aurPackageName):
    # Manually clones and build package from AUR.
    aurDirSetup()

    # Building package
    if os.path.isdir(aurPackageName):
        print("Directory already exists, updating.")
        os.chdir(aurPackageName)
        os.system("git pull")
    else:
        os.system("git clone https://aur.archlinux.org/%s.git"%(aurPackageName))
        os.chdir(aurPackageName)
    os.system("makepkg -sic")