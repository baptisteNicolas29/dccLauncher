from Qt import QtWidgets, QtCore


class ContentSelectorWidget(QtWidgets.QWidget):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        # widgets
        self.search_led = QtWidgets.QLineEdit()
        self.search_led.setPlaceholderText("search ...")
        self.search_led.setAlignment(QtCore.Qt.AlignCenter)

        self.contentType = QtWidgets.QTabWidget()
        self.contentType.tabBar().setDocumentMode(True)
        self.contentType.tabBar().setExpanding(True)

        self.contentType.addTab(ContentTypeWidget(), "asset")
        self.contentType.addTab(ContentTypeWidget(), "shot")

        # layouts
        self.setLayout(QtWidgets.QVBoxLayout())
        self.layout().setSpacing(2)
        self.layout().setContentsMargins(0, 0, 0, 0)

        self.layout().addWidget(self.search_led)
        self.layout().addWidget(self.contentType)


class ContentTypeWidget(QtWidgets.QTreeWidget):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.header().hide()
