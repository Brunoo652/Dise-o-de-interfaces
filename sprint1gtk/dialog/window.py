import gi

gi.require_version("Gtk", "3.0)")
from gi.repository import Gtk


class MainWindow(Gtk.Window):
    #button = Gtk.Button(label="blablablabla")
    box = Gtk.Box(orientation=Gtk.Orientation.Vertical)
    label = Gtk.Label ("Pregunta de si o no")
    button = Gtk.Button (label = "Sí")
    button = Gtk.Button(label="No")

    def __init__(self):
        super().__init__(title="Main")
        self.connect("destroy", Gtk.main_quit)
        self.button.connect("clicked", self.on_button_cliked)
        self.add(self.box)
      #  self.add(self.button)
        self.box.pack_start(self.label, True, True, 0)
        self.box.pack_start(self.label, True, True, 0)

    def on_button_clicked(self, widget):
        pass
