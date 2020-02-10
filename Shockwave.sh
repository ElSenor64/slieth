sudo apt-get install wine mozplugger
#sudo gedit /etc/mozpluggerrc
#echo "Add the following:"
#echo "application/x-director: dir,dcr,dxr,cst,cct,cxt,w3d,fgd,swa: Macromedia Director file
       # swallow(firefox.exe) fill stream: wine \"C:\\Program Files\\Mozilla Firefox\\firefox.exe\" -chrome \"$file\""
sudo echo "application/x-director: dir,dcr,dxr,cst,cct,cxt,w3d,fgd,swa: Macromedia Director file
        swallow(firefox.exe) fill stream: wine "C:\\Program Files\\Mozilla Firefox\\firefox.exe" -chrome "$file"
" >> /etc/mozpluggerrc
echo "Removing pluginreg.dat from ~/.mozilla/firefox/*.default/"
sudo rm ~/.mozilla/firefox/*.default/pluginreg.dat
echo "Removing pluginreg.dat from ~/.mozilla/firefox/b4932z18.default-release/"
sudo rm ~/.mozilla/firefox/b4932z18.default-release/pluginreg.dat
