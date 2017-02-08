#!/usr/bin/python
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class window:
	def __init__(self):
		interface = Gtk.Builder()
		interface.add_from_file('xml_002.glade')

                interface.connect_signals(self)
                self.myLabel = interface.get_object("myLabel")
	     
        def on_mainWindow_destroy(self, widget):
		Gtk.main_quit()
        
        def on_myButton_clicked(self, widget):
		self.myLabel.set_text("Active !")
                
                
if __name__ == "__main__":
	window()
	Gtk.main()

