import sys

from Qt import QtWidgets

from launcher.gui.pipelinerWidget import PipelinerWidget

# Todo: make the headless part of launcher
# Todo: make add / remove dcc and projects
# Todo: change the project display to allow project settings


if __name__ == "__main__":

    # launch_dcc()
    app = QtWidgets.QApplication(sys.argv)
    wdg = PipelinerWidget()
    wdg.show()

    app.exec_()
