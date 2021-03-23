# Importing modules
import os
import sys

# Importing configs
from packages import changeDirToHome

# Gruvbox Dark - https://github.com/jmattheis/gruvbox-dark-gtk
def thm_gruvboxDark():
    changeDirToHome()
    if os.path.isdir("kreator-temp"):
        os.chdir("kreator-temp")
    else: 
        os.mkdir("kreator-temp")
        os.chdir("kreator-temp")
    
    # GTK
    print("Installing GTK widget theme.")
    os.system("git clone https://github.com/jmattheis/gruvbox-dark-gtk")
    os.system("sudo mv gruvbox-dark-gtk /usr/share/themes/gruvbox-dark-gtk")

    # Icons
    print("Installing icon theme.")
    os.system("git clone https://github.com/jmattheis/gruvbox-dark-icons-gtk")
    os.system("sudo mv gruvbox-dark-icons-gtk /usr/share/icons/gruvbox-dark-icons-gtk")

    changeDirToHome()
    os.system("rm -rf kreator-temp")

    print('===========')
    print("Theme installed, apply with preferred method. (lxappearance works pretty good)")