import sys

from Qt import QtWidgets

from worker.gui import workerWidget


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    wdg = workerWidget.WorkerWidget()
    wdg.show()

    app.exec_()
