import sys

from PyQt5 import uic
from pyqt5_plugins.examplebutton import QtWidgets

from curling_league.main_window import MainWindow

UI_MainWindow, QTBaseWindow = uic.loadUiType("edit_league_dialogue.ui")


class EditLeagueDialogue(QTBaseWindow, UI_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = EditLeagueDialogue()
    window.show()
    sys.exit(app.exec_())