import sys

from Qt import QtWidgets

from gui.pipelinerWidget import PipelinerWidget


if __name__ == "__main__":

    # launch_dcc()
    app = QtWidgets.QApplication(sys.argv)
    wdg = PipelinerWidget()
    wdg.show()

    app.exec_()
