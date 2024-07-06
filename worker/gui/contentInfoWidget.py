from Qt import QtWidgets, QtCore


class ContentInfoWidget(QtWidgets.QWidget):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        # widgets
        self.tabs = QtWidgets.QTabWidget()
        self.tabs.tabBar().setDocumentMode(True)
        self.tabs.tabBar().setExpanding(True)

        self.tabs.addTab(ContentFileInfoWidget(), "files")
        # self.tabs.addTab(QtWidgets.QWidget(), "commentary")
        # self.tabs.addTab(QtWidgets.QWidget(), "about")

        self.setLayout(QtWidgets.QVBoxLayout())
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.layout().setSpacing(2)

        self.layout().addWidget(self.tabs)


class ContentFileInfoWidget(QtWidgets.QWidget):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        # widgets
        self.splitter = QtWidgets.QSplitter()
        self.splitter.setOrientation(QtCore.Qt.Vertical)

        self.splitter.addWidget(QtWidgets.QListWidget())
        self.splitter.addWidget(QtWidgets.QTextBrowser())

        self.setLayout(QtWidgets.QHBoxLayout())
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.layout().setSpacing(0)
        self.layout().addWidget(self.splitter)

        self.splitter.setStretchFactor(0, 60)
        self.splitter.setStretchFactor(1, 30)
