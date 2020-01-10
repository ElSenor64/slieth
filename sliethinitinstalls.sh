#Init
sudo apt-get install figlet gdebi
figlet Slieth Init Installer
echo "Hit the ground running."
# Basics
figlet Basics
sudo apt install neofetch sl gedit wine-stable synapse tilix terminator keepassxc gnome-tweaks
sudo apt install chromium-*
sudo snap install midori
sudo gdebi debs/googlechromestable.deb

#Themes
figlet Themes
sudo apt-get install pocillo-icon-theme papirus-icon-theme faenza-icon-theme
sudo cp -r themes/* /usr/share/themes/

#Developer Tools
figlet Dev Tools
sudo apt install git
sudo snap install code --classic
sudo snap install atom --classic
sudo snap install eclipse  --classic

#Games
figlet Games
sudo apt-get install gnome-games* gnome-breakout supertuxkart
sudo gdebi debs/steam.deb
sudo gdebi debs/minecraft.deb

#Desktop Environments
figlet Desktop Environments
echo "Alternate Desktops Environments for use. Please note that not all DEs install 100% smoothly, play well with other DEs, or play well with the GNOME stack. Use at your own risk."
read -n 1 -p "I understand (Y/n)" dewarn
dewarn=${dewarn:-y}
if [ $dewarn = y ]
then
	figlet Cinnamon
	echo "Cinnamon is a very stable and user friendly DE modled for Windows DE users. Installs well with other DEs and plays very well with the GNOME Stack."
	read -n 1 -p "Install Cinnamon? (y/N):" cinnamon
	cinnamon=${cinnamon:-n}
	
	figlet LXDE
	echo "It is safe to say LXDE is lightest DE to ever exist. It's not the most user friendly, doesn't always install well or play well with other DEs, can often break if messed with much, and doesn't look super pretty, but it will run on just about any computer, no matter how old. On newer computers, it improves performance dramaticly. Moderate knowledge of computers required for use."
	read -n 1 -p "Install LXDE? (y/N):" lxde
	lxde=${lxde:-n}

	figlet More Comming Soon...
	sleep 1s
	figlet Installing Selections...
	echo "Please wait..."
	
	if [ $cinnamon = y ]
	then
		figlet Installing Cinnamon
		sudo apt-get install cinnamon-*
	fi

	if [ $lxde = y ]
	then
		figlet Installing LXDE
		sudo apt-get install lxde-common lxappearance lxpanel-indicator-applet-plugin lxqt-powermanagement lxqt-policykit lxqt-notificationd

	fi

	figlet DE Installation Finished
fi

figlet Done
read -n 1 -p "To use all of the things you installed, it is a good idea to reboot your computer. Do so now? (Y/n):" rebot
rebot=${rebot:-y}
if [ $rebot = y ]
then
	reboot
fi
exit










