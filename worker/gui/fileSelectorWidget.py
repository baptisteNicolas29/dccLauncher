from Qt import QtWidgets, QtCore

from worker.gui.contentSelectorWidget import ContentSelectorWidget
from worker.gui.taskSelectorWidget import TaskSelectorWidget
from worker.gui.contentInfoWidget import ContentInfoWidget


class FileSelectorWidget(QtWidgets.QWidget):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        # widgets
        splitter = QtWidgets.QSplitter()

        self.contentSelector_grp = QtWidgets.QGroupBox("asset selection")
        self.contentSelector_grp.setAlignment(QtCore.Qt.AlignCenter)
        self.contentSelector_grp.setLayout(QtWidgets.QVBoxLayout())
        self.contentSelector_grp.layout().setContentsMargins(0, 0, 0, 0)
        self.contentSelector_grp.layout().setSpacing(0)

        self.taskSelector_grp = QtWidgets.QGroupBox("departement / task")
        self.taskSelector_grp.setAlignment(QtCore.Qt.AlignCenter)
        self.taskSelector_grp.setLayout(QtWidgets.QVBoxLayout())
        self.taskSelector_grp.layout().setContentsMargins(0, 0, 0, 0)
        self.taskSelector_grp.layout().setSpacing(0)

        self.contentInfo_grp = QtWidgets.QGroupBox("file / info")
        self.contentInfo_grp.setAlignment(QtCore.Qt.AlignCenter)
        self.contentInfo_grp.setLayout(QtWidgets.QVBoxLayout())
        self.contentInfo_grp.layout().setContentsMargins(0, 0, 0, 0)
        self.contentInfo_grp.layout().setSpacing(0)

        self.contentSelector = ContentSelectorWidget()
        self.taskSelector = TaskSelectorWidget()
        self.contentInfo = ContentInfoWidget()

        # layouts
        splitter.addWidget(self.contentSelector_grp)
        splitter.addWidget(self.taskSelector_grp)
        splitter.addWidget(self.contentInfo_grp)

        self.contentSelector_grp.layout().addWidget(self.contentSelector)
        self.taskSelector_grp.layout().addWidget(self.taskSelector)
        self.contentInfo_grp.layout().addWidget(self.contentInfo)

        self.setLayout(QtWidgets.QGridLayout())
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.layout().setSpacing(0)

        self.layout().addWidget(splitter)

        # post actions
        splitter.setStretchFactor(0, 10)
        splitter.setStretchFactor(1, 10)
        splitter.setStretchFactor(2, 20)

