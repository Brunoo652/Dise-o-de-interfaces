import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from cell import Cell


class MainWindow(Gtk.Window):
    flowbox=Gtk.FlowBox()

    def __init__(self):
        super(). __init__(title="Catálogo")
        self.connect("destroy", Gtk.main_quit)
        self.set_border_width(15)
        self.set_default_size(400, 400)

        header = Gtk.HeaderBar(title="Series")
        header.set_subtitle("Catálogo 2022")
        header.props.show_close_button = True

        self.set_titlebar(header)
        
        scrolled = Gtk.ScrolledWindow()
        scrolled.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        scrolled.add(self.flowbox)
        self.add(scrolled)

        for item in data_source:
            cell_one = Cell("Inazuma Eleven", Gtk.Image.new_from_File("serie1.png"))
            cell_two = Cell("Codigo Lyoko", Gtk.Image.new_from_File("serie2.png"))
            cell_three = Cell("SVLFDM", Gtk.Image.new_from_File("serie3.png"))
            cell_four = Cell("Pokemon", Gtk.Image.new_from_File("serie3.png"))
            cell_five = Cell("Bleyblade", Gtk.Image.new_from_File("serie5.png"))
            self.flowbox.add(cell_one)
            self.flowbox.add(cell_two)
            self.flowbox.add(cell_three)
            self.flowbox.add(cell_four)
            self.flowbox.add(cell_five)
