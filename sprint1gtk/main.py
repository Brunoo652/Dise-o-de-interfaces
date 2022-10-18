import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from  window import Mainwindow

win = Mainwindow()
win.show_all()

Gtk.main
