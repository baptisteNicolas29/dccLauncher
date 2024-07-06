from Qt import QtWidgets, QtCore


class SettingsWidget(QtWidgets.QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('Settings')
        self.setWindowFlags(
                QtCore.Qt.Window
                )

        # widgets
        # --- dcc settings
        self.dcc_grp = QtWidgets.QGroupBox('dcc :')
        self.dcc_grp.setLayout(QtWidgets.QGridLayout())
        self.dcc_grp.layout().setContentsMargins(2, 2, 2, 2)
        self.dcc_grp.layout().setSpacing(2)

        self.dcc_tree = QtWidgets.QTreeWidget()
        self.dcc_tree.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.dcc_tree.setHeaderLabels(['dcc', 'version'])

        # --- project settings
        self.prj_grp = QtWidgets.QGroupBox('projects :')
        self.prj_grp.setLayout(QtWidgets.QVBoxLayout())
        self.prj_grp.layout().setContentsMargins(2, 2, 2, 2)
        self.prj_grp.layout().setSpacing(2)

        self.prj_lst = QtWidgets.QListWidget()
        self.prj_lst.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)

        # layouts
        # --- root
        self.setLayout(QtWidgets.QGridLayout())
        self.layout().setContentsMargins(2, 2, 2, 2)
        self.layout().setSpacing(2)

        self.layout().addWidget(self.dcc_grp)
        self.layout().addWidget(self.prj_grp)
        # --- dcc
        self.dcc_grp.layout().addWidget(self.dcc_tree)
        # --- project
        self.prj_grp.layout().addWidget(self.prj_lst)

        # connections
        # --- dcc
        self.dcc_tree.customContextMenuRequested.connect(
                self.dcc_right_clicked)
        # --- project
        self.prj_lst.customContextMenuRequested.connect(
                self.prj_right_clicked)

    def dcc_right_clicked(self, pnt: QtCore.QPoint) -> None:
        print(f'dcc_right_clicked-> called with {pnt}')
        item = self.dcc_tree.itemAt(pnt)
        menu = QtWidgets.QMenu()

        menu.addAction('add dcc')
        if not item:
            menu.addSeparator()
            menu.addAction('add version')

        menu.exec(self.dcc_tree.mapToGlobal(pnt))

    def prj_right_clicked(self, pnt: QtCore.QPoint) -> None:
        print(f'prj_right_clicked -> called with {pnt}')
        item = self.prj_lst.itemAt(pnt)
        menu = QtWidgets.QMenu()

        if item:
            menu.addAction('remove project')
            menu.addSeparator()

        menu.addAction('add project')
        menu.exec(self.prj_lst.mapToGlobal(pnt))
