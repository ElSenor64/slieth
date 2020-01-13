from os import * # Import bash run abilities

import gi # Import GTK Stuff
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import sys

class HomeWindow(Gtk.ApplicationWindow):
    def __init__(self):
        Gtk.Window.__init__(self, title="Sleith")
        self.set_border_width(10)

        # sudolock = Gtk.LockButton.new(write)

        # Init Section 
        # system( "pkexec apt-get install figlet gdebi" )
        right = Gtk.PositionType.RIGHT
        left = Gtk.PositionType.LEFT
        below = Gtk.PositionType.BOTTOM

    # Make
        # Labels
        labelBasics = Gtk.Label.new("Basics") # Tabs labels
        labelThemes = Gtk.Label.new("Themes")
        labelBrowsers = Gtk.Label.new("Browsers")
        labelDevTools = Gtk.Label.new("Programming")
        labelGames = Gtk.Label.new("Games")
        labelDEs = Gtk.Label.new("Desktop Environments")
        labelEyeCare = Gtk.Label.new("Eye Care") # Headers
        labelgUtils = Gtk.Label.new("GUtilities")
        # Grids
        gridBasics = Gtk.Grid.new()
        gridBrowsers = Gtk.Grid.new()
        gridThemes = Gtk.Grid.new()
        gridDevTools  = Gtk.Grid.new()
        gridGames = Gtk.Grid.new()
        gridDEs = Gtk.Grid.new()
        # Buttons
            # Basics
        bNeofetch = Gtk.Button.new()
        bNeofetch.set_label("Neofetch")
        bNeofetch.connect("clicked", self.neofetch)
        bRedShift = Gtk.Button.new()
        bRedShift.set_label("Red Shift")
        bRedShift.connect("clicked", self.redshift)
        bSafeeyes = Gtk.Button.new()
        bSafeeyes.set_label("Safe Eyes")
        bSafeeyes.connect("clicked", self.safeeyes)
        bGdebi = Gtk.Button.new()
        bGdebi.set_label("Gdebi")
        bGdebi.connect("clicked", self.gdebi)
        bTilix = Gtk.Button.new()
        bTilix.set_label("Tilix")
        bTilix.connect("clicked", self.tilix)
        bSynapse = Gtk.Button.new()
        bSynapse.set_label("Synapse")
        bSynapse.connect("clicked", self.synapse)
        bGTweaks = Gtk.Button.new()
        bGTweaks.set_label("Gnome Tweaks")
        bGTweaks.connect("clicked", self.gnometweaks)
            # Browsers
        bChromiumAPT = Gtk.Button.new()
        bChromiumAPT.set_label("Chromium (via APT)")
        bChromiumAPT.connect("clicked", self.chromiumapt)
        bChromium = Gtk.Button.new()
        bChromium.set_label("Chromium")
        bChromium.connect("clicked", self.chromium)
        bFirefox = Gtk.Button.new()
        bFirefox.set_label("Firefox")
        bFirefox.connect("clicked", self.firefox)
        bMidori = Gtk.Button.new()
        bMidori.set_label("Midori")
        bMidori.connect("clicked", self.midori)
            # Themes
        bPapirus = Gtk.Button.new()
        bPapirus.set_label("Papirus")
        bPapirus.connect("clicked", self.papirus)
        bPocillo = Gtk.Button.new()
        bPocillo.set_label("Pocillo")
        bPocillo.connect("clicked", self.pocillo)
        bFaenza = Gtk.Button.new()
        bFaenza.set_label("Faenza")
        bFaenza.connect("clicked", self.faenza)
        # b*.set_border_width(3)

    # Tabs
        tabs = Gtk.Notebook()
        tabs.insert_page(gridBasics, labelBasics, 0)
        tabs.insert_page(gridBrowsers, labelBrowsers, -1)
        tabs.insert_page(gridThemes, labelThemes, -1)
        tabs.insert_page(gridDevTools, labelDevTools, -1)
        tabs.insert_page(gridGames, labelGames, -1)
        tabs.insert_page(gridDEs, labelDEs, -1)

        # Basics
        gridBasics.attach(bGdebi, 0, 0, 2, 1)
        gridBasics.attach_next_to(bNeofetch, bGdebi, right, 2, 1)
        gridBasics.attach_next_to(bRedShift, bNeofetch, right, 2, 1)
        gridBasics.attach_next_to(bSafeeyes, bRedShift, right, 2, 1)
        gridBasics.attach_next_to(bTilix, bSafeeyes, right, 2, 1)
        gridBasics.attach_next_to(bSynapse, bTilix, right, 2, 1)
        gridBasics.attach_next_to(bGTweaks, bSynapse, right, 2, 1)
        # gridBasics.attach_next_to(bSafeeyes, bRedShift, below, 2, 1)

        # Browsers
        gridBrowsers.attach(bChromium, 0, 0, 2, 1)
        gridBrowsers.attach_next_to(bChromiumAPT, bChromium, right, 2, 1)
        gridBrowsers.attach_next_to(bFirefox, bChromiumAPT, right, 2, 1)
        gridBrowsers.attach_next_to(bMidori, bFirefox, right, 2, 1)

        # Themes
        gridThemes.attach(bPapirus, 0, 0, 2, 1)
        gridThemes.attach_next_to(bPocillo, bPapirus, right, 2, 1)
        gridThemes.attach_next_to(bFaenza, bPocillo, right, 2, 1)

        # self.add(sudolock)
        self.add(tabs)
        # self.show_all()

    # Button Actions
        # Basics
    def neofetch(self, button):
        print("Installing Neofetch via Aptitude")
        system("pkexec apt-get --yes install neofetch && exit")

    def redshift(self, button):
        print("Installing RedShift via Aptitude")
        system("pkexec apt-get --yes install redshift && exit")

    def safeeyes(self, button):
        print("Installing Safe Eyes via Aptitude")
        system("pkexec apt-get --yes install safeeyes && exit")

    def gdebi(self, button):
        print("Installing Gdebi via Aptitude")
        system("pkexec apt-get --yes install gdebi && exit")

    def tilix(self, button):
        print("Installing Tilix via Aptitude")
        system("pkexec apt-get --yes install tilix && exit")

    def synapse(self, button):
        print("Installing Synapse via Aptitude")
        system("pkexec apt-get --yes install synapse && exit")

    def gnometweaks(self, button):
        print("Installing Gnome-Tweaks via Aptitude")
        system("pkexec apt-get --yes install gnome-tweaks && exit")

        #Browsers
    def chromiumapt(self, button):
        print("Installing Chromium via Aptitude")
        system("pkexec apt-get --yes install chromium-browser chromium-chromedriver chromium-codecs-ffmpeg chromium-bsu && exit")

    def chromium(self, button):
        print("Installing Chromium via snapd")
        system("pkexec snap install chromium && exit")

    def firefox(self, button):
        print("Installing Firefox via Aptitude")
        system("pkexec apt-get --yes install firefox firefoxdriver firefox-globalmenu && exit")

    def midori(self, button):
        print("Installing Midori via snapd")
        system("pkexec snap install midori && exit")

        # Themes
    def papirus(self, button):
        print("Installing Papirus Icon Theme via Aptitude")
        system("pkexec apt-get --yes install papirus-icon-theme && exit")

    def pocillo(self, button):
        print("Installing Pocillo Icon Theme via Aptitude")
        system("pkexec apt-get --yes install pocillo-icon-theme && exit")

    def faenza(self, button):
        print("Installing Faenza Icon Theme via Aptitude")
        system("pkexec apt-get --yes install faenza-icon-theme && exit")


initwin = HomeWindow()
# installswin = InitInstallsWindow()
initwin.connect("destroy", Gtk.main_quit)
initwin.show_all()
Gtk.main()