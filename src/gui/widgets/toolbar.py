class Toolbar(object):
    def __init__(self, main_window):
        super(Toolbar, self).__init__()

        main_window.toolbar = main_window.addToolBar('main_toolbar')
        main_window.toolbar.setMovable(False)
        main_window.toolbar.addAction(main_window.actions.open_file)
        main_window.toolbar.addAction(main_window.actions.exit_application)
