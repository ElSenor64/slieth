sudo apt-get install openjdk-11* --yes
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk
export PATH=$PATH:$JAVA_HOME/bin

echo "Check to see if OpenJDK installed correctly. You should see something like this:"
echo "openjdk version \"11.0.5\" 2019-10-15"
echo ""
echo ""
echo ""
echo "Java Version output:"

java -version
