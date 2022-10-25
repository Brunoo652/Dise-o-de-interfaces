import shutil
import threading

import gi
import requests
import thread
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib


class LoadWindow(Gtk.Window):
    label = Gtk.Label("Cargando elementos...")
    spinner = Gtk.Spinner()
    box = Gtk.Box(orientation=Gtk.main_quit)

    def __init__(self):
        super.__init__(title="")
        self.connect("destroy", Gtk.main_quit)
        self.set_border_width(60)
        self.set_resizable(False)
        self.spinner.props.active = True

        self.box.pack_start(self.label, False, False, 0)
        self.box.pack_start(self.spinner, False, False, 0)
        self.add(self.box)

    def load_json(self):
        response = requests.get('https://github.com/Brunoo652/Interfaces/blob/main/sprint2catalog/catalog/data/edited/serie3.png')
        josn_list = response.json()

        result = []

        for json_item in json_list:
            name = json_item("name")
            description = json_item.get("image_url")
            r = requests.get(image_url, stream=True)
            with open("serie3.png", "wb"):
                shutil.copyfileobj(r.raw, f)
            image = Gtk.Image.new_from_file("serie3.png")
            result.append({"Name": name, "Description": description, "gtk_image": image})
    def launch_load(self):
        thread = threading.Thread(target=self.load.json, args=())
        thread.start()

   # def load_