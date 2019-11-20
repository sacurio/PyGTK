#! /usr/bin/python

#By: Sandy H. Acurio M.

#Import the GTK module in order to have access to GTK's classes and functions.
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

#Print console
print("Starting...")

#Define a class in order to handle all the GUI stuffs
class PyGtkWindow(Gtk.Window):

    #Variable for store the clicks given on the button
    counter = 0

    #Constructor of the PyGtkWindow class
    def __init__(self):

        #Call to the constructor of the super class Window
        Gtk.Window.__init__(self, title="Hello world using PyGTK")

        #Set the default window size
        self.set_default_size(300, 150)
        #Set the attribute for the initial position of the window
        self.set_position(1)

        #Declare a VBox container
        box = Gtk.VBox()
        #Declare a Label element
        label = Gtk.Label()
        #Declare a Button element
        button = Gtk.Button()

        #Set the button label value
        button.set_label("Press me!")
        #Bind the event 'clicked' to the button
        button.connect("clicked", self.on_button_clicked, label)

        #Set the initial attributes for button and label inside the box container
        box.pack_start(button, expand = True, fill = True, padding = 10)
        box.pack_start(label, expand = True, fill = True, padding = 10)

        #Attach box container to the current window
        self.add(box)

    #Declare the event handler function for 'clicked' event of button element
    def on_button_clicked(self, widget, label):
        #Control de message that prints the event clicked counter
        msgCounter = "" if PyGtkWindow.counter < 1 else "[" + str(PyGtkWindow.counter) + "]"
        #Set the label concatenated with counter event
        label.set_text("Privacy for everyone " + msgCounter)
        #Increase the counter in every click event raised
        PyGtkWindow.counter += 1

#Assing a PyGtkWindow to win variable
win = PyGtkWindow()
#Bind the close action in order to close de window
win.connect("destroy", Gtk.main_quit)
#Show the window
win.show_all()
#Start the GTK app
Gtk.main()