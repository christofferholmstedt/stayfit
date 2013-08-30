from PyQt4 import QtGui


class Actions(object):
    def __init__(self, main_window):
        super(Actions, self).__init__()

        self.main = main_window

        # Default theme icon names (QIcon.fromTheme())
        # http://standards.freedesktop.org/ \
        # icon-naming-spec/icon-naming-spec-latest.html

        exit_application_icon = QtGui.QIcon.fromTheme("application-exit")
        self.exit_application = QtGui.QAction(exit_application_icon,
                                              'Exit', self.main)
        self.exit_application.setShortcut('Ctrl+Q')
        self.exit_application.setStatusTip('Exit application')
        self.exit_application.triggered.connect(QtGui.qApp.quit)

        open_file_icon = QtGui.QIcon.fromTheme("document-open")
        self.open_file = QtGui.QAction(open_file_icon, 'Open file', self.main)
        self.open_file.setShortcut('Ctrl+O')
        self.open_file.setStatusTip('Open file')
        self.open_file.triggered.connect(self._open_file_dialog)

    def _open_file_dialog(self):
        filename = QtGui.QFileDialog.getOpenFileName(self.main,
                                                     'Open file', '/home')

        try:
            f = open(filename, 'r')
            data = f.read()
            self.main.text_edit.setText(data)
            self.main.statusbar.set_message("File loaded.")
        except IOError:
            self.main.statusbar.set_message("Couldn't read the file.")
