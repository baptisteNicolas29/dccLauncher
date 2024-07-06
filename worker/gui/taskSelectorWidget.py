from Qt import QtWidgets, QtCore


class TaskSelectorWidget(QtWidgets.QWidget):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        # settings
        self.setWindowTitle("Pipeliner")

        # widgets
        self.search_led = QtWidgets.QLineEdit()
        self.search_led.setPlaceholderText("search...")
        self.search_led.setAlignment(QtCore.Qt.AlignCenter)

        self.item_tree = QtWidgets.QTreeWidget()
        self.item_tree.header().hide()

        # layouts
        self.setLayout(QtWidgets.QVBoxLayout())
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.layout().setSpacing(2)

        self.layout().addWidget(self.search_led)
        self.layout().addWidget(self.item_tree)
