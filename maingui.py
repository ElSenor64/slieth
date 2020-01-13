from os import * # Import bash run abilities

import gi # Import GTK Stuff
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import sys

class HomeWindow(Gtk.ApplicationWindow):
    def __init__(self):
        Gtk.Window.__init__(self, title="Sleith")
        self.set_border_width(10)

        # Make Stuff
        grid = Gtk.Grid.new()
        labelInstalls = Gtk.Label.new("Init Installs")
        labelQuit = Gtk.Label.new("Quit")

        right = Gtk.PositionType.RIGHT
        left = Gtk.PositionType.LEFT
        below = Gtk.PositionType.BOTTOM

        buttonInitInstalls = Gtk.Button.new()
        buttonInitInstalls.set_label("labelInstalls")
        buttonQuit = Gtk.Button.new()
        buttonQuit.set_label("labelQuit")
        grid.attach(buttonInitInstalls, 0, 0, 2, 1)
        grid.attach_next_to(buttonQuit, buttonInitInstalls, right, 2, 1)

        # Do it!
        buttonQuit.connect("clicked", Gtk.main_quit)
        buttonInitInstalls.connect("clicked", self.launchInitInstalls)

        self.add(grid)

    def launchInitInstalls(self, button):
        print("BUTTON CLICKED")
        system ("pkexec python3 ~/Documents/slieth/sliethinitinstallsgtk.py")
        Gtk.main_quit
        # installswin = InitInstallsWindow()
    

# class InitInstallsWindow(Gtk.ApplicationWindow):
#     def __init__(self):
#         Gtk.Window.__init__(self, title="Sleith")
#         self.set_border_width(10)
#         sudolock = Gtk.LockButton.new("Write")

#         # Init Section 
#         system( "sudo apt-get install figlet gdebi" )
#         # Make
#         labelBasics = Gtk.Label.new("Basics")
#         # label

#         tabs = Gtk.Notebook()
#         tabs.insert_page(tabs, labelBasics, 0)

#         self.add(sudolock)
#         self.add(tabs)
#         # self.show_all()

initwin = HomeWindow()
# installswin = InitInstallsWindow()
initwin.connect("destroy", Gtk.main_quit)
initwin.show_all()
Gtk.main()