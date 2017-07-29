import sys, os
import pygtk, gtk, gobject
import pygst
pygst.require("0.10")
import gst
import time

import numpy as np
import cv2

# Adapted from https://stackoverflow.com/questions/7324908/taking-a-snapshot-from-webcam-monitor-in-python-pygtk

class AutoClass:   # Automatic Classification
    def __init__(self):
        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.set_title("AI Automatic Classification")
        window.set_default_size(1920, 1080)
        window.connect("destroy", gtk.main_quit, "WM destroy")
        
        # add overall Horizontal box
        hbox_All = gtk.HBox()
        hbox_All.set_homogeneous(False)
        window.add(hbox_All)
        
        vbox = gtk.VBox(False, 10)
        # add crazy code    frame isn't working :(
        '''f = gtk.Frame()
        f.add(hbox_All)
        window.add(f)'''
        #
        hbox_All.pack_start(vbox)
        
        self.movie_window = gtk.DrawingArea()
        hbox = gtk.HBox()
        vbox.pack_start(hbox, False)
        hbox.set_border_width(10)
        hbox.pack_start(gtk.Label())
        
        # mess with add image here
        # 1 color, 0 grayscale, -1 unchanged
        '''img = cv2.imread('cat.jpg',-1)
        cv2.imshow('cat',img)
        cv2.waitKey(0)
        dv2.destroyAllWindows()'''
        
        # Add 6 buttons at the top
        self.button_exit = gtk.Button("Exit")
        self.button_exit.connect("clicked", self.exit)
        hbox.pack_start(self.button_exit, False)
        
        self.button_start = gtk.Button("Start")
        self.button_start.connect("clicked", self.start_stop)
        hbox.pack_start(self.button_start, False)

        self.button_SnapShot = gtk.Button("SnapShot")
        self.button_SnapShot.connect("clicked", self.take_snapshot)
        hbox.pack_start(self.button_SnapShot, False)
        
        self.button_4 = gtk.Button("Button 4")
        self.button_4.connect("clicked", self.Alpha)
        hbox.pack_start(self.button_4, False)
        
        self.button_5 = gtk.Button("Button 5")
        self.button_5.connect("clicked", self.Beta)
        hbox.pack_start(self.button_5, False)
        
        self.button_6 = gtk.Button("Button 6")
        self.button_6.connect("clicked", self.Gamma)
        hbox.pack_start(self.button_6, False)

        hbox.add(gtk.Label())
        # Moved the webcam window underneath the buttons
        vbox.add(self.movie_window)

        # Set up the gstreamer pipeline
        self.player = gst.parse_launch ("v4l2src ! autovideosink")

        bus = self.player.get_bus()
        bus.add_signal_watch()
        bus.enable_sync_message_emission()
        bus.connect("message", self.on_message)
        bus.connect("sync-message::element", self.on_sync_message)
        
        # Add the three boxes on the right
        self.vbox_3 = gtk.VBox(spacing=0)
        self.vbox_3.set_homogeneous(True)
        
        # Attempt to Add Image  << WORK ON THIS >>
        #frame = gtk.Frame()
        self.box4pic = gtk.VBox(spacing=0)
        self.box4pic.set_border_width(2)
        #frame.add(self.box4pic)
        self.label2 = gtk.Label("Picture goes here")
        self.box4pic.pack_start(self.label2, True, True, 0)
        self.vbox_3.pack_start(self.box4pic, False, True, 0)
        #image = gtk.Image(gdk.IMAGE_NORMAL, gdk.VISUAL_TRUE_COLOR, 300, 300)
        #self.vbox_3.pack_start(image, False, True, 0)
        
        self.textbox = gtk.Label("Text goes here")
        self.vbox_3.pack_start(self.textbox, False, True, 0)
        self.graph = gtk.Label("Graph goes here")
        self.vbox_3.pack_start(self.graph, False, True, 0)
        
        hbox_All.pack_start(self.vbox_3, True, True, 0)

        window.set_border_width(3)
        window.set_position(gtk.WIN_POS_CENTER_ALWAYS)
        window.show_all()
        
# Definitions for button pushes
    
    def take_snapshot(self,widget):
        filename = str(time.time()) + ".jpg"     
        img = gtk.gdk.Pixbuf( gtk.gdk.COLORSPACE_RGB, True, 8, 800, 600 )
        img.get_from_drawable(self.movie_window.window, self.movie_window.window.get_colormap(), 0, 0, 0, 0, 800, 600)
        img.save(filename, "jpeg", {"quality":"100"})
        print "Snapshot"

    def start_stop(self, w):
        if self.button_start.get_label() == "Start":
            self.button_start.set_label("Stop")
            self.player.set_state(gst.STATE_PLAYING)
        else:
            self.player.set_state(gst.STATE_NULL)
            self.button_start.set_label("Start")

    def exit(self, widget, data=None):
        gtk.main_quit()
        
    def Alpha(self, widget, data=None):
        print("Button 4")
        
    def Beta(self, widget, data=None):
        print("Button 5")
        
    def Gamma(self, widget, data=None):
        print("Button 6")

    def on_message(self, bus, message):
        t = message.type
        if t == gst.MESSAGE_EOS:
            self.player.set_state(gst.STATE_NULL)
            self.button_start.set_label("Start")
        elif t == gst.MESSAGE_ERROR:
            err, debug = message.parse_error()
            print "Error: %s" % err, debug
            self.player.set_state(gst.STATE_NULL)
            self.button_start.set_label("Start")

    def on_sync_message(self, bus, message):
        if message.structure is None:
            return
        message_name = message.structure.get_name()
        if message_name == "prepare-xwindow-id":
            # Assign the viewport
            imagesink = message.src
            imagesink.set_property("force-aspect-ratio", True)
            imagesink.set_xwindow_id(self.movie_window.window.xid)

if __name__ == "__main__":
    try:
        a = AutoClass()
        gtk.gdk.threads_init()
        gtk.main()
    except KeyboardInterrupt:
        pass   
