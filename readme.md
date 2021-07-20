# KREATOR: THE POST-INSTALL SCRIPT
This script installs and configures your GNU/Linux based OS to Ruby's liking.
```NOTE: as of v0.2.1 the script only supports the XBPS and Pacman (plus AUR) package managers. Apt support will be added soon.```

## What it does
It basically just installs common packages I end up installing on every system I setup, does some configuring, and usually installs theme files I commonly use. Packages will have options for different package managers, the script will pull lists from external files, making it fairly easy to customize. Packages can be set by modifying the ``.py`` file corresponding with you package manager in the ``config`` directory. Themes and configs may be a little more difficult to config if you don't know python, but I've done my best to keep it somewhat modular.

## How to use
Simply run it with python3.

```python kreator.py```

## How to use legacy version (v0.1.2)
Make it executable:

```chmod +x kreator-old.sh```

then, run the program and follow the prompts.

```./kreator-old.sh```

**NOTE:** The program only has support for pacman based systems at the moment.

## Where does the name come from?
I was literally in a discord call with a friend and said "give me a name for a program" and he said "creator but with a k" so that's where we are lol.
