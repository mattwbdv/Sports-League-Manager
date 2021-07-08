import sys

from PyQt5 import uic, QtWidgets

from curling_league.league_database import LeagueDatabase
from curling_league.team import Team

UI_MainWindow, QTBaseWindow = uic.loadUiType("edit_league_dialogue.ui")


class EditLeagueDialogue(QTBaseWindow, UI_MainWindow):
    def __init__(self, league=None, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.league = league
        if league:
            # add the teams in the league to the window
            self.update_ui()

            # adds new team to the league from form
            self.add_button.clicked.connect(self.add_button_clicked)

            # removes selected team from the league
            self.remove_button.clicked.connect(self.remove_button_clicked)

    def add_button_clicked(self):
        # get OID and team name for team to add
        team_oid = LeagueDatabase.instance().next_oid()
        team_name = self.name_line_edit.text()

        # create team object
        team_to_add = Team(team_oid, team_name)

        # add team to the instance of the league
        LeagueDatabase.instance().add_team_to_league(self.league, team_to_add)

        # update the ui 
        self.update_ui()

    def remove_button_clicked(self):
        # TODO
        # should we have an array of teams duplicated here and then interfacing with the database?
        row_to_remove = self.teams_list_widget.currentRow()
        team_to_remove = LeagueDatabase.instance().self.leagues.teams[row_to_remove]
        LeagueDatabase.instance().remove_team(team_to_remove)
        self.update_ui()

    def update_ui(self):
        self.teams_list_widget.clear()
        for team in self.league.teams:
            self.teams_list_widget.addItem(str(team))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = EditLeagueDialogue()
    window.show()
    sys.exit(app.exec_())
