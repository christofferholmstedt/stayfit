#!/usr/bin/python

import sys
from PyQt4 import QtGui
from gui import actions
from gui import activity
from gui.widgets import toolbar
from gui.widgets import statusbar


class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Create all actions
        self.actions = actions.Actions(self)

        # Add toolbar to main window
        self.toolbar = toolbar.Toolbar(self)

        # Add statusbar to main window
        self.statusbar = statusbar.Statusbar(self)

        self.activity = activity.Activity(self)

        self.setCentralWidget(self.activity)

        self.setWindowTitle('Stay Fit')
        self.setGeometry(300, 300, 800, 600)
        self.show()


def main():
    app = QtGui.QApplication(sys.argv)
    MainWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
