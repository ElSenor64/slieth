figlet Sleith Light Updater
#sleep 1s
#Selection time
echo -e "  \e[1;32mChoose Mode\e[0m"
echo "	Yes (procede)"
echo "	View updates"
echo "	update Settings"
echo "	Exit"

read -n 1 -p "Y/v/s/e:" mainmode
mainmode=${mainmode:-y}
#echo ""
#echo "$mainmode"
clear
#DO IT
#Yes mode
if [ $mainmode = y ]
then
	echo "Sleith Light Updater"
	echo ""
	figlet "Updating"
	sudo apt-get upgrade --fix-missing --yes --no-install-recommends
	clear	
	figlet Done
	exit
fi
#View mode
if [ $mainmode = v ]
then
	echo "Sleith Light Updater"
	echo ""
	figlet "Printing Updates"
	sudo apt-get upgrade --fix-missing --no-upgrade --no-install-recommends
	echo ""
	echo ""
	echo ""
	bash sleithupdate.sh
fi
#Settings mode
if [ $mainmode = s ]
then
	echo "Sleith Light Updater"
	echo ""
	figlet "Update Settings"
	echo "Please wait for the GUI dialog and click \"Settings\""

	echo "GTK render output:"
	update-manager --no-update
	clear
	exit
fi
#Yes mode but with big Y
if [ $mainmode = Y ]
then
	echo "Sleith Light Updater"
	echo ""
	figlet "Updating"
	sudo apt-get upgrade --fix-missing --yes --no-install-recommends
	clear
	exit
fi
#Exit mode
if [ $mainmode = e ]
then
	clear
	exit
fi

#sudo apt-get upgrade --fix-missing --yes --no-install-recommends
#sudo apt-get upgrade --fix-missing --no-upgrade --no-install-recommends
#update-manager --no-update
