from PyQt4 import QtGui

class Statusbar(object):
    def __init__(self, main_window):
        super(Statusbar, self).__init__()

        self.main = main_window
        self.init_ui()


    def init_ui(self):
        self.main.statusBar().showMessage('Ready')


    def set_message(self, msg):
        if msg is not None:
            self.main.statusBar().showMessage(msg)


    # TODO: Create method that takes care of clearing status message every X
    # seconds.
