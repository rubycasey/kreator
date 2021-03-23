# Importing modules
import os
import sys

# Importing configs
from packages import changeDirToHome

# Ruby's based gruvbox i3 config
def cfg_i3Gruvbox():
    # Making sure directories are set.
    changeDirToHome()
    os.chdir(".config")
    if os.path.isdir("i3"):
        print("i3 config exists, backing up old files.")
        os.chdir("i3")
        if os.path.isfile("config"):
            print("Backing up 'config'...")
            os.system('mv config config.bak')
        if os.path.isfile("i3blocks.conf"):
            print("Backing up 'i3blocks.conf'...")
            os.system('mv i3blocks.conf i3blocks.conf.bak')
    else: 
        os.mkdir("i3")

    # Downloading config
    print("Downloading config from pcnerd19.com")
    os.system('wget -4 https://pcnerd19.com/configs/gruvboxi3/config')
    os.system('wget -4 https://pcnerd19.com/configs/gruvboxi3/i3blocks.conf')
    print("Finished installing config, don't forget to restart i3!")

