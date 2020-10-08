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
echo "2) Help"
echo "3) Exit"
read -p "Option: " option01
echo "--"

case $option01 in
1) # Package Manager
	echo "Please choose your package manager from the options below."
	echo "1) pacman"
	echo "2) aptitude [not finished]"
	read -p "Option: " packageManager

	if [ $packageManager = 1 ]; then
		echo "You selected pacman."
		# Install CLI tools.
		echo "--"
		echo "Installing CLI tools..."
		sudo pacman -S neofetch glances python3 cmatrix
		echo "--"
		echo "Installing GUI Programs..."
		sudo pacman -S firefox vlc
		echo "--"
		echo "Do you want to install AUR packages?"
		echo "1) Yes."
		echo "2) No."
		read -p "Option: " aurToggle
	elif [ $packageManager = 2 ]; then
		echo "You selected aptitude."
	fi;;

	echo "--"
	echo "The script has finished. Thank you!"

2) # Help
	echo "There is currently no help document available, sorry.";;

3) # Exit

esac
