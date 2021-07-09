import sys

from PyQt5.QtWidgets import QFileDialog
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QDialog

from curling_league.src.user_interface.edit_league_dialogue import EditLeagueDialogue
from curling_league.src.api.league_database import LeagueDatabase
from curling_league.src.api.league import League


UI_MainWindow, QTBaseWindow = uic.loadUiType("main_window.ui")


class MainWindow(QTBaseWindow, UI_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # prints all the leagues currently in the database in the window
        self.update_ui()

        # adds new league to the database from form
        self.add_button.clicked.connect(self.add_button_clicked)

        # removes selected league from the database
        self.remove_button.clicked.connect(self.remove_button_clicked)

        # saves league
        self.save_league_button.clicked.connect(self.save_league_clicked)

        # loads new league
        self.load_league_button.clicked.connect(self.load_league_clicked)

        # edit league modal opens
        self.edit_selected_league.clicked.connect(self.edit_league_clicked)

        # file > quit closes program
        self.action_quit.triggered.connect(self.action_quit_triggered)

    def add_button_clicked(self):
        league_oid = LeagueDatabase.instance().next_oid()
        league_name = self.name_line_edit.text()
        league_to_add = League(league_oid, league_name)
        LeagueDatabase.instance().add_league(league_to_add)
        self.update_ui()

    def remove_button_clicked(self):
        row_to_remove = self.league_list_widget.currentRow()
        league_to_remove = LeagueDatabase.instance().leagues[row_to_remove]
        LeagueDatabase.instance().remove_league(league_to_remove)
        self.update_ui()

    def update_ui(self):
        self.league_list_widget.clear()
        leagues = LeagueDatabase.instance().leagues
        for league in leagues:
            self.league_list_widget.addItem(str(league))

    def save_league_clicked(self):
        result, _ = QFileDialog.getSaveFileName(
            self, "Save league")
        if result:
            LeagueDatabase.instance().save(result)

    def load_league_clicked(self):
        result, _ = QFileDialog.getOpenFileName(
            self, "Choose league to open")
        if result:
            LeagueDatabase.instance().load(result)
            self.update_ui()

    def action_quit_triggered(self):
        exit()

    def edit_league_clicked(self):
        row = self.league_list_widget.currentRow()
        league = LeagueDatabase.instance().leagues[row]
        dialog = EditLeagueDialogue(league)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            pass


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


