import os

from Qt import QtWidgets, QtGui, QtCore

from core import config
from core import dcc as DCC


class PipelinerWidget(QtWidgets.QWidget):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        # settings
        self.setWindowTitle("Launcher")
        self.setWindowIcon(
                QtGui.QIcon(
                    os.path.join(
                        config.get_source_path(),
                        'launcher.svg'
                        )
                    )
                )

        # widgets
        # --- labels
        self.project_lab = QtWidgets.QLabel("projects")
        self.dcc_lab = QtWidgets.QLabel("dcc")
        self.environ_lab = QtWidgets.QLabel("environement")

        self.project_cmb = QtWidgets.QComboBox()
        self.custom_project_btn = QtWidgets.QToolButton()
        self.dcc_cmb = QtWidgets.QComboBox()
        self.dcc_lst = QtWidgets.QListWidget()
        self.dcc_lst.setMinimumSize(QtCore.QSize(70*3, 70*3))
        self.dcc_lst.setViewMode(QtWidgets.QListWidget.IconMode)
        self.dcc_lst.setIconSize(QtCore.QSize(70, 70))

        self.environ_cmb = QtWidgets.QComboBox()
        self.launch_btn = QtWidgets.QPushButton("launch")

        # layouts
        self.setLayout(QtWidgets.QGridLayout())
        self.layout().addWidget(self.project_lab, 0, 0, 1, 1)
        self.layout().addWidget(self.environ_lab, 1, 0, 1, 1)

        self.layout().addWidget(self.project_cmb, 0, 1, 1, 1)
        self.layout().addWidget(self.custom_project_btn, 0, 2, 1, 1)
        self.layout().addWidget(self.environ_cmb, 1, 1, 1, 2)
        self.layout().addWidget(self.dcc_lst, 2, 0, 1, 3)

        # connections
        self.dcc_lst.itemDoubleClicked.connect(self.launch_dcc)
        self.custom_project_btn.clicked.connect(self.add_custom_project)

        # post init actions
        self.load_dcc()

    def switch_project(self) -> None:
        self.environ_cmb.clear()
        path = self.project_cmb.itemData(
                self.project_cmb.currentIndex(),
                QtCore.Qt.ToolTipRole
                )
        self.environ_cmb.addItems(config.get_project_environ(path))

    def add_custom_project(self) -> None:
        print('add_custom_project')
        directory = QtWidgets.QFileDialog.getExistingDirectory(
                self, "Select Directory", os.path.expanduser('~')
                )

        if directory:
            self.project_cmb.addItem(os.path.basename(directory))
            self.project_cmb.setItemData(
                    self.project_cmb.count() - 1,
                    directory,
                    QtCore.Qt.ToolTipRole
                    )
            self.switch_project()

    def load_dcc(self) -> None:
        conf = config.load_config()

        for dcc, info in conf.get("DCC", {}).items():
            item = QtWidgets.QListWidgetItem(dcc)
            icon = info["icon"].format(src=config.get_source_path())
            item.setIcon(QtGui.QIcon(icon))
            self.dcc_lst.addItem(item)

    def launch_dcc(self, item) -> None:
        DCC.launch(
                item.text(),
                self.environ_cmb.currentText(),
                self.project_cmb.itemData(
                    self.project_cmb.currentIndex(),
                    QtCore.Qt.ToolTipRole
                    )
                )
