from PyQt4 import QtGui

class Actions(object):
    def __init__(self, main_window):
        super(Actions, self).__init__()

        self.main = main_window

        # Default theme icon names (QIcon.fromTheme())
        # http://standards.freedesktop.org/icon-naming-spec/icon-naming-spec-latest.html
        self.exit_application = QtGui.QAction(
                                    QtGui.QIcon.fromTheme("application-exit"),
                                                            'Exit', self.main)
        self.exit_application.setShortcut('Ctrl+Q')
        self.exit_application.setStatusTip('Exit application')
        self.exit_application.triggered.connect(QtGui.qApp.quit)

        self.open_file = QtGui.QAction(QtGui.QIcon.fromTheme("document-open"), 'Open file', self.main)
        self.open_file.setShortcut('Ctrl+O')
        self.open_file.setStatusTip('Open file')
        self.open_file.triggered.connect(self._open_file_dialog)


    def _open_file_dialog(self):
        filename = QtGui.QFileDialog.getOpenFileName(self.main, 'Open file', '/home')

        f = open(filename, 'r')

        with f:
            data = f.read()
            self.main.text_edit.setText(data)

