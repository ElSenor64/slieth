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
        labelEyeCare = Gtk.Label.new("Eye Care") # Headers
        labelgUtils = Gtk.Label.new("GUtilities")
        # Grids
        gridBasics = Gtk.Grid.new()
        grid = Gtk.Grid.new()
        gridThemes = Gtk.Grid.new()
        # Buttons
        bNeofetch = Gtk.Button.new()
        bNeofetch.set_label("Neofetch")
        bRedShift = Gtk.Button.new()
        bRedShift.set_label("Red Shift")
        bSafeeyes = Gtk.Button.new()
        bSafeeyes.set_label("Safe Eyes")

    # Buttons
        bNeofetch.connect("clicked", self.neofetch)
        bRedShift.connect("clicked", self.redshift)
        bSafeeyes.connect("clicked", self.safeeyes)

    # Tabs
        tabs = Gtk.Notebook()
        tabs.insert_page(gridBasics, labelBasics, 0)
        # tabs.insert_page(gridgUtils, labelgUtils, -1)
        tabs.insert_page(gridThemes, labelThemes, -1)
        
        gridBasics.attach(bNeofetch, 0, 0, 2, 1)
        gridBasics.attach_next_to(bRedShift, bNeofetch, right, 2, 1)
        gridBasics.attach_next_to(bSafeeyes, bRedShift, right, 2, 1)

        # self.add(sudolock)
        self.add(tabs)
        # self.show_all()

    def neofetch(self, button):
        print("Installing Neofetch")
        system("pkexec apt-get --yes Minstall neofetch && exit")

    def redshift(self, button):
        print("Installing RedShift")
        system("pkexec apt-get --yes install redshift && exit")

    def safeeyes(self, button):
        print("Installing Safe Eyes")
        system("pkexec apt-get --yes install safeeyes && exit")




initwin = HomeWindow()
# installswin = InitInstallsWindow()
initwin.connect("destroy", Gtk.main_quit)
initwin.show_all()
Gtk.main()