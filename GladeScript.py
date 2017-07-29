'''import sys
try:
    import gi
    gi.require_version('Gtk', '3.0')
    from gi.repository import Gtk
except:
    pass
try:
    import gtk
    import gtk.glade
except:
    print('GTK not available')
    sys.exit(1)
    
'''

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

#from gi.repository import Gtk
#import gtk.

class Handler:   # Automatic Classification
    def __init__(self):
        '''window = Gtk.Window(Gtk.WINDOW_TOPLEVEL)
        self.gladefile = "window.glade"
        '''
        builder = Gtk.Builder()
        builder.add_from_file("window.glade")
        #self.wTree = Gtk.glade.XML(filename)
        builder.connect_signals(self)
        '''dic = {
            "exit" :self.quit,
            "start" :self.cameraOn,
            "stop" :self.cameraOff,
            }'''
        window = builder.get_object("window1")
        window.show_all()
        #self.wTree.signal_autoconnect(dic)
        #self.window = self.wTree.get_widget("window1")
        #self.window.show()
        #window.set_title("AI Automatic Classification")
        #window.set_default_size(1920, 1080)
        #window.connect("destroy", gtk.main_quit, "WM destroy")
        #window.set_border_width(3)
        #window.set_position(gtk.WIN_POS_CENTER_ALWAYS)


if __name__ == "__main__":
    cal = Handler()
    Gtk.main()


'''
if __name__ == "__main__":
    try:
        a = Handler()
        Gtk.gdk.threads_init()
        gtk.main()
    except KeyboardInterrupt:
        pass   '''
