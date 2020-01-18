# https://askubuntu.com/questions/740183/store-git-credentials-permanently-and-encrypted-using-a-keystore-in-ubuntu

# Bionic Only (Has been depricated)
#sudo apt-get install libgnome-keyring-dev
#sudo make --directory=/usr/share/doc/git/contrib/credential/gnome-keyring
#git config --global credential.helper /usr/share/doc/git/contrib/credential/gnome-keyring/git-credential-gnome-keyring

# All new versions (bionic+)
# https://askubuntu.com/questions/773455/what-is-the-correct-way-to-use-git-with-gnome-keyring-and-https-repos
sudo apt-get install libsecret-1-0 libsecret-1-dev
cd /usr/share/doc/git/contrib/credential/libsecret
sudo make
git config --global credential.helper /usr/share/doc/git/contrib/credential/libsecret/git-credential-libsecret
