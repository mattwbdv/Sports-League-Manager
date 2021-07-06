import sys
from curling_league.league_database import LeagueDatabase
from curling_league.league import League

from PyQt5 import uic, QtWidgets

UI_MainWindow, QTBaseWindow = uic.loadUiType("main_window.ui")


class MainWindow(QTBaseWindow, UI_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # prints all the leagues currently in the database in the window
        self.update_ui()

        # adds new league to the database from form
        self.add_button.clicked.connect(self.add_button_clicked)

    def add_button_clicked(self):
        league_oid = LeagueDatabase.instance().next_oid()
        league_name = self.name_line_edit.text
        league_to_add = League(league_oid, league_name)
        LeagueDatabase.instance().add_league(league_to_add)
        self.update_ui()

    def update_ui(self):
        self.league_list_widget.clear()
        leagues = LeagueDatabase.instance().leagues()
        for league in leagues:
            self.league_list_widget.addItem(str(league))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


