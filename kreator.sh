#!/bin/sh

### Kreator: The install script.
##  A basic script for installing the shit I want


# Intro
echo "Welcome to Kreator!"
echo "This script will install and configure your distro to Ruby's liking."
echo "Feel free to take a look under the hood, to see how it's made and maybe make your own!"
echo "==========="
echo "Please choose an option below:"
echo "1) Install packages"
echo "2) Install themes [not ready]"
echo "3) Help"
echo "4) Exit"
read -p "Option: " option01
echo "--"

case $option01 in
1) # Package Manager
	echo "Please choose your package manager from the options below."
	echo "1) pacman"
	echo "2) aptitude [not ready]"
	read -p "Option: " packageManager

	if [ $packageManager = 1 ]; then
		echo "You selected pacman."

		# Install CLI tools.
		echo "--"
		echo "Checking for updates..."
		sudo pacman -Sy
		echo "Installing CLI tools and services..."
		sudo pacman -S man openssh wget curl git vim neofetch htop glances python3 cmatrix screen
		echo "--"

		# Installing GUI Tools
		echo "Installing GUI Programs..."
		sudo pacman -S thunderbird vlc
		echo "--"

		# AUR
		echo "Do you want to install AUR packages?"
		echo "1) Yes."
		echo "2) No."
		read -p "Option: " aurToggle
		case $aurToggle in
		1)
			echo "--"
			
			# Setup
			echo "Making build directories..."
			mkdir ~/Git
			mkdir ~/Git/aur
			echo "Installing development tools..."
			sudo pacman -S base-devel
			
			## Fonts
			# Microsoft Fonts
			Echo "Installing Microsoft Fonts for increased compatibility."
			cd ~/Git/aur
			git clone https://aur.archlinux.org/ttf-ms-fonts.git
			cd ttf-ms-fonts
			makepkg -sic

			# Emoji
			echo "Installing Emojis"
			cd ~/Git/aur
			git clone https://aur.archlinux.org/ttf-twemoji.git
			cd ttf-twemoji
			makepkg -sri

			# AUR GUI Packages
			echo "--"
			echo "Would you like to install GUI applications from the AUR?"
			echo "Options:"
			echo "1) Yes."
			echo "2) No."
			read -p "Option: " aurGUI
			case $aurGUI in
			1)
				# Brave Browser
				echo "Installing Brave Browser"
				cd ~/Git/aur
				git clone https://aur.archlinux.org/brave-bin.git
				cd brave-bin
				makepkg -sri

				# OnlyOffice
				echo "Installing OnlyOffice (This one takes a while)"
				cd ~/Git/aur
				git clone https://aur.archlinux.org/onlyoffice-bin
				cd onlyoffice-bin
				makepkg -sri
				;;
			2)
				#exit
				;;
			esac
			;;
		2) #exit
			;;
		esac
		cd ~
		echo "--"

		# Github Things
		echo "Do you want to install packages from 3rd party sources like Github?"
		echo "Options: "
		echo "1) Yes."
		echo "2) No."
		read -p "Option: " githubToggle
		case $githubToggle in
		1) # Extra Repos
			# Setup
			echo "Making build directories..."
			cd ~
			mkdir ~/git
			mkdir ~/git/etc

			# Sauron - AUR Search Tool
			echo "Install Sauron..."
			cd ~/git/etc
			git clone https://github.com/icorbrey/sauron.git
			cd sauron
			sudo chmod +x sauron
			export PATH="$PATH:~/git/etc/.sauron"

			;;
		2) #exit
			;;
		esac


	elif [ $packageManager = 2 ]; then
		echo "You selected aptitude, which isn't currenly supported. Ending script..."
	fi

	echo "--"
	echo "The script has finished. If you found any problems, feel free to let me know at https://github.com/pcnerd18/kreator"
	;;

2) # Theme Install
	echo "--"
	echo "Themes are not yet supported, sorry. Ending script..."
	;;


3) # Help
	echo "There is currently no help document available, however you can read the readme.md file."
	;;

4) # Exit

esac
Installing gtk theme: Ant-Dracula...