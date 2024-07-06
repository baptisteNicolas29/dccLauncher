import os

from Qt import QtWidgets, QtGui, QtCore

from launcher.core import configuration
from launcher.core import project
from launcher.core import dcc as Dcc
from launcher.gui import settingsWidget


class LauncherWidget(QtWidgets.QWidget):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        # settings
        self.setWindowTitle("Launcher")
        self.setWindowIcon(
                QtGui.QIcon(
                    os.path.join(
                        configuration.get_source_path(),
                        'icon',
                        'launcher.svg'
                        )
                    )
                )
        self.settings_wnd = settingsWidget.SettingsWidget(parent=self)

        # menu
        self.menu_bar = QtWidgets.QMenuBar()
        edit_menu = self.menu_bar.addMenu("Edit")
        help_menu = self.menu_bar.addMenu("Help")

        # --- edit menu
        self.settings_act = edit_menu.addAction("settings")

        # --- help menu
        help_menu.addAction("About")

        # widgets
        # --- labels
        self.project_lab = QtWidgets.QLabel("projects")
        self.dcc_lab = QtWidgets.QLabel("dcc")
        self.environ_lab = QtWidgets.QLabel("environement")

        self.project_cmb = QtWidgets.QComboBox()
        self.dcc_cmb = QtWidgets.QComboBox()
        self.dcc_lst = QtWidgets.QListWidget()
        self.dcc_lst.setMinimumSize(QtCore.QSize(70*3, 70*3))
        self.dcc_lst.setViewMode(QtWidgets.QListWidget.IconMode)
        self.dcc_lst.setAcceptDrops(False)
        self.dcc_lst.setIconSize(QtCore.QSize(70, 70))

        self.environ_cmb = QtWidgets.QComboBox()
        self.launch_btn = QtWidgets.QPushButton("launch")

        # layouts
        self.setLayout(QtWidgets.QGridLayout())
        self.layout().setMenuBar(self.menu_bar)
        self.layout().addWidget(self.project_lab, 0, 0, 1, 1)
        self.layout().addWidget(self.environ_lab, 1, 0, 1, 1)

        self.layout().addWidget(self.project_cmb, 0, 1, 1, 1)
        self.layout().addWidget(self.environ_cmb, 1, 1, 1, 1)
        self.layout().addWidget(self.dcc_lst, 2, 0, 1, 2)

        # connections
        self.project_cmb.currentTextChanged.connect(self.load_environ)
        self.dcc_lst.itemDoubleClicked.connect(self.launch_dcc)
        self.settings_act.triggered.connect(self.show_settings)
        # post init actions
        self.load_dcc()
        self.load_project()

    def show_settings(self):
        self.settings_wnd.show()

    def load_project(self) -> None:
        self.project_cmb.clear()
        for i, x in enumerate(configuration.get_projects()):
            self.project_cmb.addItem(os.path.basename(x))
            self.project_cmb.setItemData(i, x, QtCore.Qt.ToolTipRole)

    def load_environ(self) -> None:
        self.environ_cmb.clear()
        project_path = configuration.get_project_by_name(
                self.project_cmb.currentText()
                )
        self.environ_cmb.clear()
        if not project_path:
            return
        self.environ_cmb.addItems(project.get_project_environ(project_path))

    def load_dcc(self) -> None:
        self.dcc_lst.clear()
        for dcc in configuration.get_dcc():
            dcc_config = configuration.get_dcc_config(dcc)
            item = QtWidgets.QListWidgetItem(dcc)
            item.setIcon(
                    QtGui.QIcon(
                        dcc_config["icon"].format(
                            src=configuration.get_source_path()
                            )
                        )
                    )
            self.dcc_lst.addItem(item)

    def launch_dcc(self, item: QtWidgets.QListWidgetItem) -> None:
        print('launch_dcc -> called')
        dcc = item.text()
        env = self.environ_cmb.currentText()
        project_path = configuration.get_project_by_name(
                self.project_cmb.currentText()
                )

        Dcc.launch(dcc, env, project_path)

    def hideEvent(self, event) -> None:
        self.settings_wnd.hide()
