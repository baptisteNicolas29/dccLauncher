from Qt import QtWidgets, QtCore

from worker.gui.fileSelectorWidget import FileSelectorWidget


class WorkerWidget(QtWidgets.QWidget):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        # settings
        self.setWindowTitle("Pipeliner")

        # widgets
        self.project_label = QtWidgets.QLabel("project:")
        self.user_label = QtWidgets.QLabel("user:")
        self.user_label.setAlignment(
                QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter
                )

        self.tabs = QtWidgets.QTabWidget()
        self.tabs.tabBar().setDocumentMode(True)
        self.tabs.tabBar().setExpanding(True)

        self.fileSelectorContainer = QtWidgets.QWidget()
        self.fileSelectorContainer.setLayout(QtWidgets.QVBoxLayout())
        self.fileSelectorContainer.layout().setContentsMargins(0, 4, 0, 0)

        self.taskContainer = QtWidgets.QWidget()
        self.taskContainer.setLayout(QtWidgets.QVBoxLayout())
        self.taskContainer.layout().setContentsMargins(0, 4, 0, 0)

        self.fileSelectorWidget = FileSelectorWidget()

        # toolBar
        self.toolBar_tb = QtWidgets.QToolBar()

        self.toolBar_tb.addAction("krita")
        self.toolBar_tb.addAction("photoshop")

        self.toolBar_tb.addSeparator()

        self.toolBar_tb.addAction("maya")
        self.toolBar_tb.addAction("houdini")
        self.toolBar_tb.addAction("3dsmax")
        self.toolBar_tb.addSeparator()
        self.toolBar_tb.addAction("substance designer")
        self.toolBar_tb.addAction("mary")

        # layouts
        self.info_layout = QtWidgets.QHBoxLayout()
        self.info_layout.setContentsMargins(2, 2, 2, 2)
        self.info_layout.setSpacing(0)

        self.info_layout.addWidget(self.project_label)
        self.info_layout.addWidget(self.user_label)

        self.setLayout(QtWidgets.QVBoxLayout())
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.layout().setSpacing(0)
        self.layout().setMenuBar(WorkerMenuBarWidget())
        self.layout().addLayout(self.info_layout)
        self.layout().addWidget(self.toolBar_tb)
        self.layout().addWidget(self.tabs)

        self.tabs.addTab(self.fileSelectorContainer, "files selector")
        # self.tabs.addTab(self.taskContainer, "task")
        # self.tabs.addTab(QtWidgets.QWidget(), "dependency / usage")

        self.fileSelectorContainer.layout().addWidget(self.fileSelectorWidget)

        # connections


class WorkerMenuBarWidget(QtWidgets.QMenuBar):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        # menus
        self.file_menu = QtWidgets.QMenu("file")
        self.edit_menu = QtWidgets.QMenu("edit")
        self.help_menu = QtWidgets.QMenu("help")

        # subMenus
        self.project_menu = QtWidgets.QMenu("project")

        # actions
        self.loggin_act = QtWidgets.QAction("loggin")
        self.settings_act = QtWidgets.QAction("settings")
        self.addProject_act = QtWidgets.QAction("add project")
        self.about_act = QtWidgets.QAction("about")
        self.exit_act = QtWidgets.QAction("exit")

        self.file_menu.addAction(self.loggin_act)
        self.file_menu.addAction(self.addProject_act)
        self.file_menu.addAction(self.exit_act)
        self.edit_menu.addAction(self.settings_act)
        self.help_menu.addAction(self.about_act)

        self.addMenu(self.file_menu)
        self.addMenu(self.edit_menu)
        self.addMenu(self.help_menu)

        self.exit_act.triggered.connect(exit)
        self.loggin_act.triggered.connect(self.print_parent)

    def print_parent(self) -> None:

        print(
                "WorkerMenuBarWidget.parent ->", self.parent(),
                "type:", type(self.parent()),
                "is a QWidget:", isinstance(self.parent(), QtWidgets.QWidget)
                )
