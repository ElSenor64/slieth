# https://askubuntu.com/questions/740183/store-git-credentials-permanently-and-encrypted-using-a-keystore-in-ubuntu

sudo apt-get install libgnome-keyring-dev
sudo make --directory=/usr/share/doc/git/contrib/credential/gnome-keyring
git config --global credential.helper /usr/share/doc/git/contrib/credential/gnome-keyring/git-credential-gnome-keyring
